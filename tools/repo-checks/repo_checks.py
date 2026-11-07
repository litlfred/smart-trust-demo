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
- Every user story traces to requirements (scenarios/story-requirements.json:
  every story has an entry, an empty one says why in `note`), and every
  requirement id cited there, in docs/journeys.md and in the BPMN exists:
  STT-* in smart-trust-tools' skills/requirements/ at the pinned commit (the
  mount, or the --smart-trust-tools directory; CI fetches it), STD-* in
  this repository's skills/requirements/, whose actors must be our roles.

- The DAK's data dictionary (dak/data-dictionary.json), decision tables
  (processes/content/decisions/*.dmn) and indicators (dak/indicators.json)
  resolve: every requirement id they cite exists, every BPMN task they serve,
  every FSH artifact and data element they name, every decision table an
  indicator names; and each table's entries stay in the FEEL subset the
  harness interprets (tools/dak/dak.py).

- Every skill a BPMN task names exists (this instance's, or a smart-trust-tools
  package's at the pinned commit); a task's skill is one its lane's role
  has; and every person and system role plays a lane in some journey.

Run from anywhere: python3 tools/repo-checks/repo_checks.py [--smart-trust-tools DIR]
(DIR defaults to the smart-trust-tools mount; CI fetches its skills/ there.)
"""
import fnmatch
import json
import pathlib
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[2]

def _load_graph():
    """tools/journeys/graph.py, the one reader of the journeys' sources (loaded by path: works under -I)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("journeys_graph", ROOT / "tools" / "journeys" / "graph.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


graph = _load_graph()


def _load_dak():
    """tools/dak/dak.py, the one reader of the DAK's dictionary, decision tables and indicators."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("dak", ROOT / "tools" / "dak" / "dak.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


SKIP = {".git", "node_modules", "build", ".gradle", ".kotlin", "site"}
USES = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)")
PINNED = re.compile(r"^[^@\s]+@[0-9a-f]{40}$")


def tracked():
    # Only this repository's own files: the mounted harness layers are
    # gitignored and checked by their own repositories.
    out = subprocess.run(["git", "ls-files", "-co", "--exclude-standard"], cwd=ROOT,
                         check=True, capture_output=True, text=True).stdout
    return [ROOT / line for line in out.splitlines() if line]


def files(pattern):
    for p in tracked():
        rel = p.relative_to(ROOT)
        if fnmatch.fnmatch(str(rel), pattern) or fnmatch.fnmatch(rel.name, pattern):
            if not SKIP.intersection(rel.parts) and p.exists():
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
    stt = pathlib.Path(_arg("--smart-trust-tools") or ROOT / "smart-trust-tools")
    errors += requirement_errors(stt / "skills" / "requirements")
    errors += binding_errors(stt / "skills")
    errors += dak_errors(stt / "skills" / "requirements")
    for e in errors:
        print(e, file=sys.stderr)
    print(f"repo-checks: {len(errors)} problem(s)")
    return 1 if errors else 0


BPMN = "{http://www.omg.org/spec/BPMN/20100524/MODEL}"
SKILL = "{https://litlfred.github.io/bootstrap/v0/processes/ns/}skill"
UPSTREAM_SKILL = re.compile(r"^(hcert|vhl)-[a-z0-9-]+$")


def journey_errors():
    errors = []
    roles_file = ROOT / "scenarios" / "roles.json"
    if not roles_file.exists():
        return errors
    roles = {r["id"]: r for r in json.loads(roles_file.read_text())["roles"]}
    # A title or other name names one role (cat-harness role-graph).
    names = {}
    for rid, r in roles.items():
        for n in [r["title"], *r.get("otherNames", [])]:
            prev = names.setdefault(n.casefold(), rid)
            if prev != rid:
                errors.append(f"scenarios/roles.json: the name {n!r} belongs to both role {prev} and role {rid}")
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
        actor = json.loads(a.read_text())
        for rid in actor.get("roles", []):
            if rid not in roles:
                errors.append(f"{a.relative_to(ROOT)}: unknown role {rid}")
        # meta.persona is read by the IG's personas page and by the VaxLink walkthrough.
        persona = actor.get("meta", {}).get("persona")
        if persona is not None:
            for key in ("name", "role", "country", "goal"):
                if not isinstance(persona.get(key), str) or not persona[key]:
                    errors.append(f"{a.relative_to(ROOT)}: meta.persona.{key} must be a non-empty string")
            for key in ("needs", "frustrations"):
                v = persona.get(key)
                if not isinstance(v, list) or not v or not all(isinstance(x, str) and x for x in v):
                    errors.append(f"{a.relative_to(ROOT)}: meta.persona.{key} must be a non-empty list of strings")
    stories = ROOT / "scenarios" / "stories.json"
    if stories.exists():
        for st in json.loads(stories.read_text())["stories"]:
            if st["role"]["role"] not in roles:
                errors.append(f"scenarios/stories.json: story {st['id']} names unknown role {st['role']['role']}")
    try:
        lanes = {p["file"]: p["lanes"] for p in graph.processes(ROOT)}
    except graph.GraphError as e:
        errors.append(str(e))
        lanes = {}
    for b in sorted(files("processes/*.bpmn")):
        rel = b.relative_to(ROOT)
        tree = ET.parse(b).getroot()
        for lane in lanes.get(b, []):
            if lane["role"] not in roles:
                errors.append(f"{rel}: lane {lane['id']} names unknown role {lane['role']}")
        for sk in tree.iter(SKILL):
            if not skill_ok(sk.get("ref")):
                errors.append(f"{rel}: unknown skill {sk.get('ref')}")
        ids = {e.get("id") for e in tree.iter() if e.get("id")}
        for f in tree.iter(BPMN + "sequenceFlow"):
            for end in ("sourceRef", "targetRef"):
                if f.get(end) not in ids:
                    errors.append(f"{rel}: flow {f.get('id')} {end} {f.get(end)} does not exist")
    return errors


REQ_ID = re.compile(r"\bST[TD]-[A-Z0-9]+-\d{3}\b")  # STT-*: smart-trust-tools'; STD-*: this demonstrator's own


def _arg(name):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv[:-1] else None


def requirement_errors(req_dir):
    """Stories trace to requirements, and every cited requirement id exists at the pinned smart-trust-tools."""
    errors = []
    req_dir = pathlib.Path(req_dir)
    if not req_dir.is_dir():
        return [f"{req_dir}: no smart-trust-tools requirements here; mount the pinned layers (bun run cat mount:lock) or pass --smart-trust-tools DIR"]
    known = set()
    roles = {r["id"] for r in json.loads((ROOT / "scenarios" / "roles.json").read_text())["roles"]}
    for d in (req_dir, ROOT / "skills" / "requirements"):
        for f in sorted(d.glob("*.json")):
            req = json.loads(f.read_text())
            rid = req.get("id", "")
            if rid.startswith("req:"):
                known.add(rid[4:].upper())
            if d != req_dir:  # this demonstrator's own: its actors are our roles
                for a in req.get("actors", []):
                    if a not in roles:
                        errors.append(f"{f.relative_to(ROOT)}: actor {a} is not a role in scenarios/roles.json")
    stories = [s["id"] for s in json.loads((ROOT / "scenarios" / "stories.json").read_text())["stories"]]
    trace_file = ROOT / "scenarios" / "story-requirements.json"
    trace = json.loads(trace_file.read_text())["stories"] if trace_file.exists() else {}
    for sid in stories:
        if sid not in trace:
            errors.append(f"scenarios/story-requirements.json: story {sid} has no entry")
    for sid, t in trace.items():
        if sid not in stories:
            errors.append(f"scenarios/story-requirements.json: {sid} is not a story in stories.json")
        if not t.get("requirements") and not t.get("note"):
            errors.append(f"scenarios/story-requirements.json: story {sid} traces to no requirement and gives no note saying why")
        for r in t.get("requirements", []):
            if r not in known:
                errors.append(f"scenarios/story-requirements.json: story {sid} cites {r}, which no requirement defines (STT-* in smart-trust-tools, STD-* in skills/requirements/)")
    for src in [ROOT / "docs" / "journeys.md", *sorted((ROOT / "processes" / "content").glob("*.bpmn"))]:
        for r in sorted(set(REQ_ID.findall(src.read_text(encoding="utf-8")))):
            if r not in known:
                errors.append(f"{src.relative_to(ROOT)}: cites {r}, which no requirement defines (STT-* in smart-trust-tools, STD-* in skills/requirements/)")
    return errors


def binding_errors(stt_skills):
    """Task skills exist and belong to their lane's role; every person and system role plays a lane, or (a person's) is a scenario persona's."""
    errors = []
    if not stt_skills.is_dir():
        return [f"{stt_skills}: no smart-trust-tools skills here; mount the pinned layers or pass --smart-trust-tools DIR"]
    known = set()
    for m in [*stt_skills.glob("*/package-manifest.json"), *(ROOT / "skills").glob("*/package-manifest.json")]:
        known.update(json.loads(m.read_text()).get("skills", []))
    roles = {r["id"]: r for r in graph.roles(ROOT)}
    in_lanes = set()
    for p in graph.processes(ROOT):
        rel = p["file"].relative_to(ROOT)
        lane_of = {n: l["role"] for l in p["lanes"] for n in l["nodes"]}
        in_lanes.update(l["role"] for l in p["lanes"])
        for t in p["tasks"]:
            if t["skill"] not in known:
                errors.append(f"{rel}: task {t['id']} names skill {t['skill']}, which no skill package defines")
            role = lane_of.get(t["id"])
            if role is None:
                errors.append(f"{rel}: task {t['id']} is in no lane")
            elif role in roles and t["skill"] not in roles[role].get("skills", []):
                errors.append(f"{rel}: task {t['id']}'s skill {t['skill']} is not one of its lane role {role}'s skills (scenarios/roles.json)")
    # A person who takes part in a journey without a lane of their own (the
    # newborn, the subject of care, acts through the caregiver) plays a role
    # that is in a journey by a user scenario naming one of its actors as a
    # persona; a role nobody in any journey plays is still an error.
    personas = {a for f in (ROOT / "scenarios" / "user-scenarios").glob("*.json") for a in json.loads(f.read_text(encoding="utf-8")).get("personas", [])}
    in_scenes = {rr for f in (ROOT / "scenarios" / "actors").glob("*.json") for a in [json.loads(f.read_text(encoding="utf-8"))]
                 if a["id"] in personas and a.get("kind") == "person" for rr in a.get("roles", [])}
    for rid, r in roles.items():
        for s in r.get("skills", []):
            if s not in known:
                errors.append(f"scenarios/roles.json: role {rid} names skill {s}, which no skill package defines")
        if rid not in in_lanes and rid not in in_scenes and set(r.get("actorKinds", [])) & {"person", "system"}:
            errors.append(f"scenarios/roles.json: role {rid} plays no lane in any journey")
    return errors


def dak_errors(req_dir):
    """The DAK sources' references resolve, with STT-* and STD-* requirement ids as requirement_errors reads them."""
    req_dir = pathlib.Path(req_dir)
    if not req_dir.is_dir():
        return []  # requirement_errors already names the missing mount
    known = set()
    for d in (req_dir, ROOT / "skills" / "requirements"):
        for f in sorted(d.glob("*.json")):
            rid = json.loads(f.read_text()).get("id", "")
            if rid.startswith("req:"):
                known.add(rid[4:].upper())
    return _load_dak().errors(known, ROOT)


if __name__ == "__main__":
    sys.exit(main())
