"""The DAK's data dictionary, decision tables and indicators, read one way.

Sources:
- dak/data-dictionary.json             the data dictionary: one logical model per
                                       data set a journey records or exchanges,
                                       and the code lists its elements bind to
- processes/content/decisions/*.dmn    the decision tables (OMG DMN 1.3), each
                                       naming the BPMN tasks it serves, the
                                       requirements it applies, the FHIR
                                       artifacts and data elements it reads
                                       (namespace TRACE, in extensionElements)
- dak/indicators.json                  the indicators: definitions only

tools/ig-gen/ig_gen.py renders them into the IG; tools/repo-checks/repo_checks.py
calls errors() so that every reference in them resolves. Standard library
only; load it by path (importlib) so it also works under `python3 -I`.
"""

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DMN = "{https://www.omg.org/spec/DMN/20191111/MODEL/}"
TRACE = "{https://litlfred.github.io/smart-trust-demo/ns/dak/}"
BPMN = "{http://www.omg.org/spec/BPMN/20100524/MODEL}"
REQ_ID = re.compile(r"\bST[TD]-[A-Z0-9]+-\d{3}\b")
DT_ID = re.compile(r"\bTD\.DT\.\d{2}\b")
DE_ID = re.compile(r"\bTD\.[A-Z0-9]+\.DE\d{2}\b")

# The FEEL the harness's decision-table interpreter accepts (cat-harness skill
# dmn-authoring): "-" (any), literals, comparisons and one-of.
_LIT = r'(?:"[^"]*"|true|false|null|-?\d+(?:\.\d+)?|(?:<=|>=|<|>|=)\s*-?\d+(?:\.\d+)?)'
FEEL_INPUT = re.compile(rf"^(?:-|{_LIT}(?:\s*,\s*{_LIT})*)$")
FEEL_OUTPUT = re.compile(rf"^{_LIT}$")
TYPES = {"string", "boolean", "code", "date", "dateTime", "uri", "integer", "Identifier", "Coding",
         "CodeableConcept", "BackboneElement"}
CARD = re.compile(r"^(0|1)\.\.(1|\*)$")


def dictionary(root=ROOT):
    return json.loads((root / "dak" / "data-dictionary.json").read_text(encoding="utf-8"))


def indicators(root=ROOT):
    return json.loads((root / "dak" / "indicators.json").read_text(encoding="utf-8"))["indicators"]


def elements(root=ROOT):
    """Every data element by its full code (TD.J1.DE01): (model, element)."""
    out = {}
    for m in dictionary(root)["models"]:
        for e in m["elements"]:
            out[f"{m['code']}.{e['code']}"] = (m, e)
    return out


def bpmn_nodes(process, root=ROOT):
    """{id: name} of every flow node of processes/content/<process>, or None when the file is missing."""
    f = root / "processes" / "content" / process
    if not f.exists():
        return None
    return {n.get("id"): n.get("name") or n.get("id") for n in ET.parse(f).getroot().iter() if n.get("id")}


def _text(el):
    t = el.find(DMN + "text") if el is not None else None
    return (t.text or "").strip() if t is not None else ""


def decisions(root=ROOT):
    """Every decision table in processes/content/decisions/*.dmn, in the order of their codes (TD.DT.01, ...)."""
    out = []
    for f in sorted((root / "processes" / "content" / "decisions").glob("*.dmn")):
        tree = ET.parse(f).getroot()
        for d in tree.iter(DMN + "decision"):
            table = d.find(DMN + "decisionTable")
            ext = d.find(DMN + "extensionElements")
            trace = ext if ext is not None else ET.Element("none")
            code = trace.find(TRACE + "table")
            out.append({
                "file": f,
                "id": d.get("id"),
                "code": code.get("code") if code is not None else None,
                "name": d.get("name"),
                "description": (d.findtext(DMN + "description") or "").strip(),
                "hitPolicy": table.get("hitPolicy", "UNIQUE") if table is not None else None,
                "inputs": [{"label": i.get("label"), "expression": _text(i.find(DMN + "inputExpression")),
                            "typeRef": i.find(DMN + "inputExpression").get("typeRef")}
                           for i in (table.findall(DMN + "input") if table is not None else [])],
                "outputs": [{"label": o.get("label") or o.get("name"), "name": o.get("name"), "typeRef": o.get("typeRef")}
                            for o in (table.findall(DMN + "output") if table is not None else [])],
                "rules": [{"id": r.get("id"),
                           "description": (r.findtext(DMN + "description") or "").strip(),
                           "inputs": [_text(e) for e in r.findall(DMN + "inputEntry")],
                           "outputs": [_text(e) for e in r.findall(DMN + "outputEntry")]}
                          for r in (table.findall(DMN + "rule") if table is not None else [])],
                "serves": [(s.get("process"), s.get("task")) for s in trace.findall(TRACE + "serves")],
                "requirements": [r.get("ref") for r in trace.findall(TRACE + "requirement")],
                "artifacts": [a.get("ref") for a in trace.findall(TRACE + "artifact")],
                "dataElements": [e.get("ref") for e in trace.findall(TRACE + "dataElement")],
            })
    return sorted(out, key=lambda d: d["code"] or "")


def fsh_names(root=ROOT):
    """{name: kind} of every FSH entity declared under input/fsh/ (Instance, Profile, Logical, ValueSet, CodeSystem)."""
    out = {}
    for f in (root / "input" / "fsh").rglob("*.fsh"):
        for kind, name in re.findall(r"^(Instance|Profile|Logical|ValueSet|CodeSystem):\s*(\S+)", f.read_text(encoding="utf-8"), re.M):
            out[name] = kind
    return out


def _artifact_errors(where, ref, names):
    rtype, _, name = ref.partition("/")
    if not name:
        return [f"{where}: artifact {ref!r} is not Type/Name"]
    kind = names.get(name)
    want = {"StructureDefinition": {"Profile", "Logical"}, "ValueSet": {"ValueSet"}, "CodeSystem": {"CodeSystem"}}.get(rtype, {"Instance"})
    if kind not in want:
        return [f"{where}: {ref} is not an FSH {'/'.join(sorted(want))} in input/fsh/"]
    return []


def _serves_errors(where, process, tasks):
    nodes = bpmn_nodes(process)
    if nodes is None:
        return [f"{where}: no BPMN processes/content/{process}"]
    return [f"{where}: {process} has no task {t}" for t in tasks if t not in nodes]


def errors(known_requirements, root=ROOT):
    """Every reference in the DAK sources resolves: requirement ids, BPMN tasks,
    FSH artifacts, data elements, decision tables, and each table's FEEL."""
    errs = []
    names = fsh_names(root)
    dd = dictionary(root)
    lists = {c["id"] for c in dd["codeLists"]}
    model_codes = set()
    for m in dd["models"]:
        where = f"dak/data-dictionary.json: model {m['id']}"
        if m["code"] in model_codes:
            errs.append(f"{where}: code {m['code']} is used twice")
        model_codes.add(m["code"])
        for s in m["serves"]:
            errs += _serves_errors(where, s["process"], s["tasks"])
        for ref in m["realisedBy"]:
            errs += _artifact_errors(where, ref, names)
        paths, codes = set(), set()
        for e in m["elements"]:
            w = f"{where} element {e['path']}"
            if e["code"] in codes:
                errs.append(f"{w}: code {e['code']} is used twice")
            codes.add(e["code"])
            parent = e["path"].rpartition(".")[0]
            if parent and parent not in paths:
                errs.append(f"{w}: parent {parent} is not an earlier element")
            paths.add(e["path"])
            if not CARD.match(e["card"]):
                errs.append(f"{w}: cardinality {e['card']} is not 0..1, 1..1, 0..* or 1..*")
            if e["type"] not in TYPES and not re.match(r"^Reference\([A-Za-z]+\)$", e["type"]):
                errs.append(f"{w}: type {e['type']} is not one the dictionary uses")
            vs = (e.get("binding") or {}).get("valueSet")
            if vs and not vs.startswith("http") and vs not in names and vs[:-2] not in lists:
                errs.append(f"{w}: binds to {vs}, which is neither a code list here nor an FSH ValueSet")
        for r in m["requirements"]:
            if r not in known_requirements:
                errs.append(f"{where}: cites {r}, which no requirement defines")
    all_elements = elements(root)
    tables = {}
    for d in decisions(root):
        where = f"{d['file'].relative_to(root)}: {d['id']}"
        if not d["code"]:
            errs.append(f"{where}: no trace:table code")
        elif d["code"] in tables:
            errs.append(f"{where}: code {d['code']} is used twice")
        tables[d["code"]] = d
        if d["hitPolicy"] not in ("FIRST", "UNIQUE"):
            errs.append(f"{where}: hit policy {d['hitPolicy']}; say FIRST or UNIQUE")
        if not d["serves"]:
            errs.append(f"{where}: serves no BPMN task")
        for process, task in d["serves"]:
            errs += _serves_errors(where, process, [task])
        for ref in d["artifacts"]:
            errs += _artifact_errors(where, ref, names)
        for de in d["dataElements"]:
            if de not in all_elements:
                errs.append(f"{where}: data element {de} is not in dak/data-dictionary.json")
        for rule in d["rules"]:
            w = f"{where} rule {rule['id']}"
            if len(rule["inputs"]) != len(d["inputs"]) or len(rule["outputs"]) != len(d["outputs"]):
                errs.append(f"{w}: {len(rule['inputs'])} input and {len(rule['outputs'])} output entries for "
                            f"{len(d['inputs'])} inputs and {len(d['outputs'])} outputs")
            for text, col in zip(rule["inputs"], d["inputs"]):
                if not FEEL_INPUT.match(text):
                    errs.append(f"{w}: input entry {text!r} is outside the FEEL subset (-, literals, comparisons, one-of)")
                elif col["typeRef"] == "boolean" and text not in ("-", "true", "false"):
                    errs.append(f"{w}: boolean input {col['label']!r} has entry {text!r}")
            for text, col in zip(rule["outputs"], d["outputs"]):
                if not FEEL_OUTPUT.match(text):
                    errs.append(f"{w}: output entry {text!r} is not one literal")
                elif col["typeRef"] == "boolean" and text not in ("true", "false", "null"):
                    errs.append(f"{w}: boolean output {col['label']!r} has entry {text!r}")
        text = d["file"].read_text(encoding="utf-8")
        for r in sorted(set(REQ_ID.findall(text))):
            if r not in known_requirements:
                errs.append(f"{d['file'].relative_to(root)}: cites {r}, which no requirement defines")
        for t in sorted(set(DT_ID.findall(text))):
            if t not in {x["code"] for x in decisions(root)}:
                errs.append(f"{d['file'].relative_to(root)}: names decision table {t}, which no .dmn defines")
    codes = set()
    for ind in indicators(root):
        where = f"dak/indicators.json: {ind['code']}"
        if ind["code"] in codes:
            errs.append(f"{where}: code is used twice")
        codes.add(ind["code"])
        for de in ind["dataElements"]:
            if de not in all_elements:
                errs.append(f"{where}: data element {de} is not in dak/data-dictionary.json")
        for t in ind["decisionTables"]:
            if t not in tables:
                errs.append(f"{where}: decision table {t} is not in processes/content/decisions/")
        for r in ind["requirements"]:
            if r not in known_requirements:
                errs.append(f"{where}: cites {r}, which no requirement defines")
    for rel in ("dak/data-dictionary.json", "dak/indicators.json"):
        text = (root / rel).read_text(encoding="utf-8")
        for r in sorted(set(REQ_ID.findall(text))):
            if r not in known_requirements:
                errs.append(f"{rel}: cites {r}, which no requirement defines")
        for t in sorted(set(DT_ID.findall(text))):
            if t not in tables:
                errs.append(f"{rel}: names decision table {t}, which no .dmn defines")
        for de in sorted(set(DE_ID.findall(text))):
            if de not in all_elements:
                errs.append(f"{rel}: names data element {de}, which the dictionary does not define")
    return errs
