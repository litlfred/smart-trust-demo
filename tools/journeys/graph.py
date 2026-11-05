"""The journeys' graph, read one way for every tool that needs it.

repo_checks.py, ig-gen/ig_gen.py and archimate/overlay.py all read the BPMN
processes, the roles and the actors. They used to read a lane three ways (by
its role reference, by its id less "Lane_", and by its name matched to a role
title), and only the first was checked. Now each reads it here, by the lane's
partitionElementRef, which names the role's id; a lane without one is an
error, never a silent fallback.

Standard library only; load it by path (importlib) so it also works under
`python3 -I`.
"""

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BPMN = "{http://www.omg.org/spec/BPMN/20100524/MODEL}"
SKILL = "{https://litlfred.github.io/bootstrap/v0/processes/ns/}skill"
CODE = re.compile(r"^(J\d+(?:\.\d+)?)\s")  # a journey's code: the first word of its process name


class GraphError(ValueError):
    """The journeys' sources do not hang together."""


def roles(root=ROOT):
    """scenarios/roles.json's roles, in file order."""
    return json.loads((root / "scenarios" / "roles.json").read_text(encoding="utf-8"))["roles"]


def actors(root=ROOT):
    """scenarios/actors/*.json, by file name."""
    return [json.loads(f.read_text(encoding="utf-8")) for f in sorted((root / "scenarios" / "actors").glob("*.json"))]


def processes(root=ROOT):
    """Every BPMN process in processes/content/, in file order.

    Each is {file, stem, id, name, code, doc, lanes: [{id, role, name, nodes}],
    skills, tasks: [{id, skill}]}, where a lane's role is its
    partitionElementRef, its nodes the flow nodes it holds, and code the
    journey code that starts the process name (J1, J4.0, ...), or None.
    """
    out = []
    for f in sorted((root / "processes" / "content").glob("*.bpmn")):
        tree = ET.parse(f).getroot()
        proc = next(tree.iter(BPMN + "process"))
        doc = proc.find(BPMN + "documentation")
        lanes = []
        for lane in tree.iter(BPMN + "lane"):
            role = lane.get("partitionElementRef")
            if not role:
                raise GraphError(f"{f.relative_to(root)}: lane {lane.get('id')} has no partitionElementRef naming its role")
            lanes.append({"id": lane.get("id"), "role": role, "name": lane.get("name"),
                          "nodes": [n.text.strip() for n in lane.findall(BPMN + "flowNodeRef") if n.text]})
        m = CODE.match(proc.get("name") or "")
        out.append({
            "file": f,
            "stem": f.stem,
            "id": proc.get("id"),
            "name": proc.get("name"),
            "code": m.group(1) if m else None,
            "doc": (doc.text or "").strip() if doc is not None else "",
            "lanes": lanes,
            "skills": [s.get("ref") for s in tree.iter(SKILL)],
            # every flow node that names a skill: {id, skill}
            "tasks": [{"id": n.get("id"), "skill": sk.get("ref")}
                      for n in proc.iter() if n.get("id") for sk in n.findall(f"{BPMN}extensionElements/{SKILL}")],
        })
    return out


def journeys_of_roles(role_ids, procs=None, root=ROOT):
    """The journey codes whose BPMN has a lane played by any of these roles, in process order."""
    procs = procs if procs is not None else processes(root)
    want = set(role_ids)
    return [p["code"] for p in procs if p["code"] and want & {l["role"] for l in p["lanes"]}]
