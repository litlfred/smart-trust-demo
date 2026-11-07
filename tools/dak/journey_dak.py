"""Each journey step's `dak` edges, derived from the DAK and the step's BPMN tasks.

A step of a user scenario (scenarios/user-scenarios/*.json) names the BPMN
tasks that carry it out (`realisedBy`: a process and its task ids). The DAK
says which tasks each of its assets serves:

- a data set (dak/data-dictionary.json, a model's `serves`) is `data` to a
  step whose tasks include one it serves;
- a decision table (processes/content/decisions/*.dmn, its `trace:serves`) is
  `decides` to a step whose tasks include one it serves;
- an indicator (dak/indicators.json) is `measures` to every step of a journey
  in its `journeys` (the step id without its trailing letter: J2a is J2).

Each edge is the asset's key in the artefact index: StructureDefinition/<model
id>, PlanDefinition/<TrustDemoDTnn> for TD.DT.nn, Measure/<indicator id>. The
step's `dak` is written in that order (data, decides, measures), each sorted
by key; a step with none carries no `dak`. A file whose steps carry `dak` is
at least user-scenario/0.3.0, the minor that adds the field.

    python3 tools/dak/journey_dak.py           # write the steps' dak
    python3 tools/dak/journey_dak.py --check   # exit 1 if a file is stale

tools/repo-checks/repo_checks.py runs the check. Standard library only; it
loads tools/dak/dak.py by path, so it works under `python3 -I`.
"""

import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCENARIOS = ROOT / "scenarios" / "user-scenarios"
RELS = ("data", "decides", "measures")
MIN_SCHEMA = (0, 3, 0)
SCHEMA = re.compile(r"^user-scenario/(\d+)\.(\d+)\.(\d+)$")


def _dak():
    spec = importlib.util.spec_from_file_location("dak", Path(__file__).resolve().parent / "dak.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _journey(step_id):
    """The journey a step belongs to: its id without a trailing letter (J4.0a -> J4.0)."""
    return re.sub(r"[a-z]+$", "", step_id)


def assets(root=ROOT):
    """[(rel, key, {(process basename, task)} or None, journeys or None)] for every DAK asset."""
    dak = _dak()
    out = []
    for m in dak.dictionary(root)["models"]:
        served = {(s["process"], t) for s in m["serves"] for t in s["tasks"]}
        out.append(("data", f"StructureDefinition/{m['id']}", served, None))
    for d in dak.decisions(root):
        if not d["code"]:
            continue
        n = d["code"].rsplit(".", 1)[1]
        out.append(("decides", f"PlanDefinition/TrustDemoDT{n}", set(d["serves"]), None))
    for i in dak.indicators(root):
        out.append(("measures", f"Measure/{i['id']}", None, set(i.get("journeys", []))))
    return out


def step_dak(step, catalogue):
    """The `dak` list one step should carry."""
    tasks = {(Path(r["process"]).name, t) for r in step.get("realisedBy") or [] for t in r.get("tasks", [])}
    journey = _journey(step["id"])
    found = set()
    for rel, key, served, journeys in catalogue:
        if (served is not None and served & tasks) or (journeys is not None and journey in journeys):
            found.add((rel, key))
    return [{"key": k, "rel": r} for r, k in sorted(found, key=lambda x: (RELS.index(x[0]), x[1]))]


def _schema_at_least(tag):
    m = SCHEMA.match(tag or "")
    if not m:
        return tag
    if tuple(int(x) for x in m.groups()) >= MIN_SCHEMA:
        return tag
    return "user-scenario/" + ".".join(str(x) for x in MIN_SCHEMA)


def derive(doc, catalogue):
    """The scenario with every step's `dak` derived; the input is not changed."""
    out = json.loads(json.dumps(doc))
    any_dak = False
    for step in out.get("steps", []):
        links = step_dak(step, catalogue)
        if links:
            step["dak"] = links
            any_dak = True
        else:
            step.pop("dak", None)
    if any_dak:
        out["$schema"] = _schema_at_least(out.get("$schema"))
    return out


def render(doc):
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


def stale(root=ROOT):
    """[(path, derived text)] of every scenario file whose `dak` is not what the DAK says."""
    catalogue = assets(root)
    out = []
    for f in sorted((root / "scenarios" / "user-scenarios").glob("*.json")):
        text = f.read_text(encoding="utf-8")
        want = render(derive(json.loads(text), catalogue))
        if json.loads(want) != json.loads(text):
            out.append((f, want))
    return out


def errors(root=ROOT):
    return [f"{p.relative_to(root)}: a step's dak is stale: run python3 tools/dak/journey_dak.py" for p, _ in stale(root)]


def main(argv):
    todo = stale()
    if "--check" in argv:
        for p, _ in todo:
            print(f"journey-dak: stale: {p.relative_to(ROOT)}")
        print(f"journey-dak: {len(todo)} stale")
        return 1 if todo else 0
    for p, text in todo:
        p.write_text(text, encoding="utf-8")
    print(f"journey-dak: {len(todo)} file(s) written")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
