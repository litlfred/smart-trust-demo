#!/usr/bin/env python3
"""Check scenarios/user-scenarios/ (standard library only).

Shape: docs/proposals/user-scenario/user-scenario.schema.json, through the jsonschema package when it is
installed (it is not a dependency; without it only the references are checked).
References, which a JSON Schema cannot express:
- personas, step.lead, experience.actor, handoff.from/to: actors in
  scenarios/actors/, and every actor a step names is in personas;
- step.stories: ids in scenarios/stories.json;
- step.realisedBy: the BPMN file exists and each task id is a node in it;
- step.record.state: a code of the code-list trustLadder names (beside the scenarios);
- step.examples: an FSH Instance with that id in input/fsh/;
- step ids unique within the scenario;
- follows: another scenario here, and the chain has no loop;
- step.uses: each block is in the building-blocks catalogue, once per step,
  and a named component is one of that block's;
- the catalogue itself: unique block ids, known layers, and components that
  are element keys of tools/archimate/overlay.py.
step.requirements are not checked here: smart-trust-tools' req: nodes are a
mounted layer.

Run:   python3 tools/user-scenarios/check.py   (CI: checks.yml, repo-checks job)
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "scenarios" / "user-scenarios"
SCHEMA = ROOT / "docs" / "proposals" / "user-scenario" / "user-scenario.schema.json"
BLOCKS = ROOT / "docs" / "proposals" / "uses-building-block" / "building-blocks.json"
BLOCKS_SCHEMA = ROOT / "docs" / "proposals" / "uses-building-block" / "building-blocks.schema.json"


def catalogue(errors, jsonschema):
    """The building-blocks catalogue, checked, as {block id: block}."""
    if not BLOCKS.exists():
        return {}
    cat = json.loads(BLOCKS.read_text())
    rel = BLOCKS.relative_to(ROOT)
    if jsonschema:
        for e in jsonschema.Draft202012Validator(json.loads(BLOCKS_SCHEMA.read_text())).iter_errors(cat):
            errors.append(f"{rel}: {'/'.join(map(str, e.path)) or '(root)'}: {e.message}")
    layers = {l["id"] for l in cat.get("layers", [])}
    overlay = (ROOT / "tools" / "archimate" / "overlay.py").read_text()
    elements = set(re.findall(r'^\s*\("([a-z0-9-]+)", "', overlay, re.M)) | set(re.findall(r'^GDHCN = \("([a-z0-9-]+)"', overlay, re.M))
    out = {}
    for b in cat.get("blocks", []):
        if b["id"] in out:
            errors.append(f"{rel}: block {b['id']} repeated")
        out[b["id"]] = b
        if b.get("layer") not in layers:
            errors.append(f"{rel}: block {b['id']}: unknown layer {b.get('layer')}")
        for c in b.get("components", []):
            if c not in elements:
                errors.append(f"{rel}: block {b['id']}: {c} is not an element of tools/archimate/overlay.py")
    return out


def main():
    errors = []
    schema = json.loads(SCHEMA.read_text())
    try:
        import jsonschema
    except ImportError:
        jsonschema = None
        print("check: jsonschema not installed, shape not checked")
    actors = {json.loads(f.read_text())["id"] for f in (ROOT / "scenarios" / "actors").glob("*.json")}
    stories = {s["id"] for s in json.loads((ROOT / "scenarios" / "stories.json").read_text())["stories"]}
    lists = {}
    for f in DATA.glob("*.code-list.json"):
        c = json.loads(f.read_text())
        lists[c["id"]] = [x["code"] for x in c["codes"]]
    blocks = catalogue(errors, jsonschema)
    instances = set()
    for f in (ROOT / "input" / "fsh").rglob("*.fsh"):
        instances.update(re.findall(r"^Instance:\s*(\S+)", f.read_text(), re.M))

    scenarios = [f for f in DATA.glob("*.json") if not f.name.endswith(".code-list.json")]
    for f in scenarios:
        rel = f.relative_to(ROOT)
        s = json.loads(f.read_text())
        if jsonschema:
            for e in jsonschema.Draft202012Validator(schema).iter_errors(s):
                errors.append(f"{rel}: {'/'.join(map(str, e.path)) or '(root)'}: {e.message}")
        personas = set(s.get("personas", []))
        for a in personas - actors:
            errors.append(f"{rel}: persona {a} is not an actor")
        ladder = lists.get(s.get("trustLadder"))
        if s.get("trustLadder") and ladder is None:
            errors.append(f"{rel}: trustLadder {s['trustLadder']} is not a code-list")
        seen = set()
        for st in s.get("steps", []):
            where = f"{rel}: step {st.get('id')}"
            if st.get("id") in seen:
                errors.append(f"{where}: id repeated")
            seen.add(st.get("id"))
            named = {st.get("lead")} | {x.get("actor") for x in st.get("experiences", [])}
            named |= {st.get("handoff", {}).get(k) for k in ("from", "to")} - {None}
            for a in named - personas:
                errors.append(f"{where}: {a} is not one of the scenario's personas")
            if st.get("lead") not in {x.get("actor") for x in st.get("experiences", [])}:
                errors.append(f"{where}: the lead has no experience")
            for sid in st.get("stories", []):
                if sid not in stories:
                    errors.append(f"{where}: unknown story {sid}")
            for r in st.get("realisedBy", []):
                bpmn = ROOT / r["process"]
                if not bpmn.exists():
                    errors.append(f"{where}: no process {r['process']}")
                    continue
                ids = set(re.findall(r'\bid="([^"]+)"', bpmn.read_text()))
                for t in r.get("tasks", []):
                    if t not in ids:
                        errors.append(f"{where}: {r['process']} has no node {t}")
            state = st.get("record", {}).get("state")
            if state and ladder is not None and state not in ladder:
                errors.append(f"{where}: record state {state} is not a code of {s['trustLadder']}")
            used = set()
            for u in st.get("uses", []):
                b = blocks.get(u.get("block"))
                if b is None:
                    errors.append(f"{where}: uses unknown building block {u.get('block')}")
                    continue
                if u["block"] in used:
                    errors.append(f"{where}: uses {u['block']} twice")
                used.add(u["block"])
                if u.get("component") and u["component"] not in b.get("components", []):
                    errors.append(f"{where}: {u['component']} is not a component of {u['block']}")
            for ex in st.get("examples", []):
                if ex.split("/", 1)[-1] not in instances:
                    errors.append(f"{where}: no FSH Instance {ex}")
    ids = {json.loads(f.read_text())["id"]: json.loads(f.read_text()).get("follows") for f in scenarios}
    for sid, prev in ids.items():
        seen_chain = {sid}
        while prev:
            if prev not in ids:
                errors.append(f"scenario {sid}: follows unknown scenario {prev}")
                break
            if prev in seen_chain:
                errors.append(f"scenario {sid}: the follows chain loops")
                break
            seen_chain.add(prev)
            prev = ids[prev]
    for e in errors:
        print(e)
    print(f"user-scenario check: {len(scenarios)} scenario(s), {len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
