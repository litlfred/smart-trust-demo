#!/usr/bin/env python3
"""Check the user-scenario proposal's examples (standard library only).

Shape: user-scenario.schema.json, through the jsonschema package when it is
installed (it is not a dependency; without it only the references are checked).
References, which a JSON Schema cannot express:
- personas, step.lead, experience.actor, handoff.from/to: actors in
  scenarios/actors/, and every actor a step names is in personas;
- step.stories: ids in scenarios/stories.json;
- step.realisedBy: the BPMN file exists and each task id is a node in it;
- step.record.state: a code of the code-list trustLadder names (example/);
- step.examples: an FSH Instance with that id in input/fsh/;
- step ids unique within the scenario.
step.requirements are not checked here: smart-trust-tools' req: nodes are a
mounted layer.

Run:   python3 docs/proposals/user-scenario/check.py
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def main():
    errors = []
    schema = json.loads((HERE / "user-scenario.schema.json").read_text())
    try:
        import jsonschema
    except ImportError:
        jsonschema = None
        print("check: jsonschema not installed, shape not checked")
    actors = {json.loads(f.read_text())["id"] for f in (ROOT / "scenarios" / "actors").glob("*.json")}
    stories = {s["id"] for s in json.loads((ROOT / "scenarios" / "stories.json").read_text())["stories"]}
    lists = {}
    for f in (HERE / "example").glob("*.code-list.json"):
        c = json.loads(f.read_text())
        lists[c["id"]] = [x["code"] for x in c["codes"]]
    instances = set()
    for f in (ROOT / "input" / "fsh").rglob("*.fsh"):
        instances.update(re.findall(r"^Instance:\s*(\S+)", f.read_text(), re.M))

    scenarios = [f for f in (HERE / "example").glob("*.json") if not f.name.endswith(".code-list.json")]
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
            for ex in st.get("examples", []):
                if ex.split("/", 1)[-1] not in instances:
                    errors.append(f"{where}: no FSH Instance {ex}")
    for e in errors:
        print(e)
    print(f"user-scenario check: {len(scenarios)} scenario(s), {len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
