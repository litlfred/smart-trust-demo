#!/usr/bin/env python3
"""Repository checks that need nothing but the Python standard library.

- Every `uses:` in .github/workflows pins an action by a full commit SHA
  (a local `./` action is allowed). [AGENTS.md: dependencies are pinned]
- Every *.json file in the repository parses.
- Every Markdown file under memory/ has the folio-memory front matter.
- The journeys hang together: every BPMN lane, actor and story names a role
  in scenarios/roles.json, and every skill a task or role names is one of
  this instance's (skills/*/package-manifest.json) or of smart-trust-tools'
  hcert and vhl packages (names hcert-*, vhl-*), whose existence the harness
  check verifies once mounted.

Run from anywhere: python3 tools/repo-checks/repo_checks.py
"""
import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[2]
SKIP = {".git", "node_modules", "build", ".gradle", ".kotlin", "site"}
USES = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)")
PINNED = re.compile(r"^[^@\s]+@[0-9a-f]{40}$")


def files(pattern):
    for p in ROOT.rglob(pattern):
        if not SKIP.intersection(p.relative_to(ROOT).parts):
            yield p


def main():
    errors = []
    for wf in sorted(files(".github/workflows/*.y*ml")):
        for n, line in enumerate(wf.read_text().splitlines(), 1):
            m = USES.match(line)
            if m and not m.group(1).startswith("./") and not PINNED.match(m.group(1)):
                errors.append(f"{wf.relative_to(ROOT)}:{n}: action not pinned by commit SHA: {m.group(1)}")
    for js in sorted(files("*.json")):
        try:
            json.loads(js.read_text())
        except ValueError as e:
            errors.append(f"{js.relative_to(ROOT)}: invalid JSON: {e}")
    for md in sorted((ROOT / "memory").glob("*.md")):
        head = md.read_text().split("---")
        if len(head) < 3 or "$schema: folio-memory/v1" not in head[1] or f"id: {md.stem}" not in head[1]:
            errors.append(f"{md.relative_to(ROOT)}: missing folio-memory/v1 front matter with id {md.stem}")
    errors += journey_errors()
    for e in errors:
        print(e, file=sys.stderr)
    print(f"repo-checks: {len(errors)} problem(s)")
    return 1 if errors else 0


BPMN = "{http://www.omg.org/spec/BPMN/20100524/MODEL}"
SKILL = "{https://litlfred.github.io/bootstrap/0.1.0/processes/ns#}skill"
UPSTREAM_SKILL = re.compile(r"^(hcert|vhl)-[a-z0-9-]+$")


def journey_errors():
    errors = []
    roles_file = ROOT / "scenarios" / "roles.json"
    if not roles_file.exists():
        return errors
    roles = {r["id"]: r for r in json.loads(roles_file.read_text())["roles"]}
    own_skills = set()
    for m in (ROOT / "skills").glob("*/package-manifest.json"):
        own_skills.update(json.loads(m.read_text())["skills"])
        for name in json.loads(m.read_text())["skills"]:
            if not (m.parent / f"{name}.md").exists():
                errors.append(f"{m.relative_to(ROOT)}: skill {name} has no {name}.md")

    def skill_ok(name):
        return name in own_skills or UPSTREAM_SKILL.match(name)

    for rid, r in roles.items():
        for s in r.get("skills", []):
            if not skill_ok(s):
                errors.append(f"scenarios/roles.json: role {rid} names unknown skill {s}")
    for a in sorted((ROOT / "scenarios" / "actors").glob("*.json")):
        for rid in json.loads(a.read_text()).get("roles", []):
            if rid not in roles:
                errors.append(f"{a.relative_to(ROOT)}: unknown role {rid}")
    stories = ROOT / "scenarios" / "stories.json"
    if stories.exists():
        for st in json.loads(stories.read_text())["stories"]:
            if st["role"]["role"] not in roles:
                errors.append(f"scenarios/stories.json: story {st['id']} names unknown role {st['role']['role']}")
    for b in sorted((ROOT / "processes").rglob("*.bpmn")):
        rel = b.relative_to(ROOT)
        tree = ET.parse(b).getroot()
        for lane in tree.iter(BPMN + "lane"):
            if lane.get("partitionElementRef") not in roles:
                errors.append(f"{rel}: lane {lane.get('id')} names unknown role {lane.get('partitionElementRef')}")
        for sk in tree.iter(SKILL):
            if not skill_ok(sk.get("ref")):
                errors.append(f"{rel}: unknown skill {sk.get('ref')}")
        ids = {e.get("id") for e in tree.iter() if e.get("id")}
        for f in tree.iter(BPMN + "sequenceFlow"):
            for end in ("sourceRef", "targetRef"):
                if f.get(end) not in ids:
                    errors.append(f"{rel}: flow {f.get('id')} {end} {f.get(end)} does not exist")
    return errors


if __name__ == "__main__":
    sys.exit(main())
