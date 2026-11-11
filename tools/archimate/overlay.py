"""The SMART Trust demonstrator as an overlay on the DPI-H RA ArchiMate model.

A spec for smart-ra's tools/archimate-dth/add_views.py (pinned in
smart-ra.lock.json), applied by build.py to smart-ra's model 0.3.0-draft.1.
Nothing in the RA model is changed: the overlay only adds elements,
relationships and views, and every RA element keeps its Archi id.

What it adds, and where each part comes from:

- the journeys, the use cases, as BusinessProcess elements: one per BPMN
  process in processes/content/ whose name starts with a journey code;
- the people who take part, as BusinessRole elements: the roles in
  scenarios/roles.json whose actorKinds is "person", each assigned to the
  journeys whose BPMN has a lane played by that role;
- the systems, as ApplicationComponent elements grouped by country (the
  family's phone, the Holder's device, as a Device): the system actors of
  scenarios/actors/, each Serving the journeys whose BPMN has a lane played
  by one of its roles, and Composed of its parts (the phone Realizes its
  wallet), each part an actor's meta.parts entry (first drawn as the
  components of VaxLink's architecture view, litlfred/vaxlink,
  ArchitectureDiagram.tsx), named by what it does, and Realizing its own
  country's instance of the RA building block it plays, as the RA draws a
  concrete system realizing a component (Table 3.3);
- each country's instance of every RA building block its parts play
  ("Provider Systems (Taifafeki)", "Provider Systems (Onesa)"): a
  Specialization of the RA block, since Taifafeki and Onesa are different
  jurisdictions and neither's systems are the other's;
- where the two countries meet, as Flow and Triggering relationships between
  their parts: read from the BPMN wherever a sequence flow leads from a task
  of one country's system to a task of the other's (through people's lanes
  between), and, for the paper DVC that J1 hands to J2 and J3, from
  HANDOFFS, which names the BPMN tasks at both ends;
- what the two countries share, and nothing else, between them: WHO GDHCN
  and the WHO SMART Trust specifications it realizes; the RA's own generic
  building blocks are a band of their own below both countries in each
  journey's view;
- each journey's Realization of the RA capabilities it exercises.

The BPMN, the roles and the actors are read by tools/journeys/graph.py, the
same reader repo_checks.py and ig_gen.py use; a lane's role is its
partitionElementRef.

The relationship types are ones ArchiMate 3.2 allows between those element
types (Appendix B): Assignment (BusinessRole to BusinessProcess), Serving
(ApplicationComponent to BusinessProcess or ApplicationComponent),
Composition, Realization, Specialization, Flow and Triggering (between two
ApplicationComponents), Realization (BusinessProcess to Capability,
ApplicationComponent to Requirement, and Device to ApplicationComponent),
Association (BusinessRole to Stakeholder) and Aggregation (from a Grouping).
Every element names its concept in glossary/architecture.glossary.json
(skosConcept), and every role and system the FHIR ActorDefinition it
realizes (fhir-actor).

build.py lays the overlay's views out again with room between the boxes
(LAYOUT) and routes every line orthogonally through the gaps, writing the
route as Archi bendpoints.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

NAMESPACE = "https://github.com/litlfred/smart-trust-demo#archimate-overlay"
SOURCE = "SMART Trust demonstrator (litlfred/smart-trust-demo): journeys J1 to J4.1 and the VaxLink architecture view"
VIEW_FOLDER = "SMART Trust demonstrator"

# --- RA elements reused (smart-ra model 0.3.0-draft.1; ids are Archi's) ------

EXISTING = {
    # Layers of the Integrated View (Fig. 3.2)
    "layer-pos": "id-c9b5f2ae923b5e38801bd1dbf8b382b9",
    "layer-reusable": "id-08403902fa3e5df4920a1fbe8eddd82f",
    "layer-shared": "id-00d4ffa565f55eb996137917386ecac1",
    "layer-dpif": "id-077b000f20b95c899adb1143f8ee8cd5",
    "layer-interop": "id-e12108f9f25257a9bfed47e23ac4205a",
    "grp-clinical": "id-cf6d89c99137518a81cdd98cac0129ad",  # Clinical Services, in DPI-H reusable components
    "grp-public-health": "id-a621c8cb4b915e8eb458fc3285cecd84",  # Public Health & Analytics, in DPI-H reusable components
    # Building blocks
    "ra-provider-systems": "id-270f6a946e9d5feea37702bdb93980ba",
    "ra-chw": "id-3384363f5f8d5ab09a43380f2f8962ba",
    "ra-citizen-apps": "id-b1c7360ab5595d6ca684259d405c5889",
    "ra-cdss": "id-539b04ae45f147258d8253ae5cb87402",
    "ra-terminology": "id-3f41de2b51c24041b08243bf72b140d1",
    "ra-hmis": "id-d626508a7dc55b1fb11bf34f57f8ddd9",
    "ra-client-registry": "id-bc813024f32358c98e5512e43cf2c9bc",
    "ra-facility-registry": "id-4e0767822dcf46409554156a133fbc67",
    "ra-workforce-registry": "id-350840520ae44f658b6ad3b3762e382e",
    "ra-product-registry": "id-59c26d672a4248e0bb83cf4d26cba10c",
    "ra-lhr": "id-0e6d89398fff4f20994a31b4de58e7d7",
    "ra-trust-services": "id-847e6eea9ee15a39ad97e8861444ce79",
    "ra-mediator": "id-3c5d846710034c4595e206e748d65e36",
    # Capabilities (Fig. 3.2 capability layer and the 0.2.0 model)
    "cap-access-consent-trust": "id-0faeca5a0caf5731be8009de6378775e",
    "cap-clinical-services": "id-c483685e82ce5040b04e3c2bf0138f2b",
    "cap-health-record-mgmt": "id-4a08b39b55a6469098a89697af71daae",
    # Stakeholders of the Integrated View (Fig. 3.2), which the journeys' people belong to
    "stk-care-recipients": "id-a2320dbc07e6450b94f3f0f3e03bb877",  # Citizens / Care recipients ("Families & caregivers")
    "stk-health-workers": "id-8d3dd8b68d504c2a9fe8cf414b16c127",  # Health Workers ("Providers, CHWs, system mgrs")
}

# Which RA stakeholder each person role belongs to. A BusinessRole and a
# Stakeholder are different element types, so the link is an Association
# (Specialization would need one type). The RA's own BusinessRoles
# "Individual" and "Community Health" are not used: they come from the
# supply-chain handbook (Fig. 1) and mean the actors of supply chain processes.
ROLE_STAKEHOLDER = {
    "caregiver": "stk-care-recipients",
    "subject-of-care": "stk-care-recipients",
    "birth-clinic-vaccinator": "stk-health-workers",
    "community-health-worker": "stk-health-workers",
    "home-clinic-provider": "stk-health-workers",
    "poc-provider": "stk-health-workers",
}

# Which RA blocks each Integrated View layer shows here, in the Grouping
# smart-ra's Fig. 3.2 view draws each in: a member of that Grouping in
# smart-ra's model, or (the decision support engine and the HMIS) of a
# Grouping inside it, so that drawing one inside the other says what the
# model says.
RA_LAYERS = [
    ("layer-pos", ["ra-provider-systems", "ra-chw", "ra-citizen-apps"]),
    ("layer-reusable", ["ra-cdss", "ra-hmis"]),
    ("layer-shared", ["ra-terminology", "ra-client-registry", "ra-facility-registry", "ra-workforce-registry", "ra-product-registry", "ra-lhr"]),
    ("layer-dpif", ["ra-trust-services"]),
    ("layer-interop", ["ra-mediator"]),
]

# The RA blocks' names in smart-ra's model, for their per-country instances.
RA_NAME = {
    "ra-provider-systems": "Provider Systems",
    "ra-chw": "CHW & Community",
    "ra-citizen-apps": "Citizen / Patient Apps",
    "ra-cdss": "Computable Decision Support Engine",
    "ra-terminology": "Terminology Service",
    "ra-hmis": "Health Management Information System",
    "ra-client-registry": "Client Registry for Health",
    "ra-facility-registry": "Health Facility Registry",
    "ra-workforce-registry": "Health Workforce Registry",
    "ra-product-registry": "Product Registry",
    "ra-lhr": "Lifelong Health Record",
    "ra-trust-services": "National Trust Services",
    "ra-mediator": "DPI-F Information Mediator",
}
# The two blocks that are members of a Grouping inside their layer's, drawn inside it.
RA_SUBGROUP = {"ra-cdss": "grp-clinical", "ra-hmis": "grp-public-health"}
RA_GROUPINGS = [l for l, _bs in RA_LAYERS] + sorted(set(RA_SUBGROUP.values()))  # smart-ra's Groupings drawn: bands a line may cross
ORDER = [b for _l, bs in RA_LAYERS for b in bs]


def ra_box(b):
    """An RA block's box, inside its sub-grouping if smart-ra puts it in one."""
    return ("group", RA_SUBGROUP[b], 1, [("box", b)]) if b in RA_SUBGROUP else ("box", b)
assert set(ORDER) == set(RA_NAME), "every RA block drawn has a name, and only those"

# --- The journeys' graph: read once, by tools/journeys/graph.py ------------

def _load_graph():
    import importlib.util
    spec = importlib.util.spec_from_file_location("journeys_graph", ROOT / "tools" / "journeys" / "graph.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


graph = _load_graph()
PROCESSES = graph.processes(ROOT)

# --- Journeys: one per BPMN process in processes/content/ -------------------
# Every process whose name starts with a journey code (J1, J4.0, ...) is a
# journey; a new BPMN file appears here with no edit. Its element is named
# by the process's name, the source's own term; JOURNEY_CAPABILITIES gives
# the RA capabilities a journey exercises (none otherwise).

JOURNEYS = {p["code"]: p for p in PROCESSES if p["code"]}

JOURNEY_CAPABILITIES = {
    "J1": ["cap-access-consent-trust", "cap-health-record-mgmt"],
    "J2": ["cap-clinical-services"],
    "J3": ["cap-access-consent-trust", "cap-clinical-services", "cap-health-record-mgmt"],
    "J4.0": ["cap-access-consent-trust", "cap-health-record-mgmt"],
    "J4.1": ["cap-access-consent-trust", "cap-health-record-mgmt"],
}


def jkey(code):
    return "journey-" + code.lower().replace(".", "-")


def caps(code):
    return JOURNEY_CAPABILITIES.get(code, [])


def lane_roles(code):
    return {l["role"] for l in JOURNEYS[code]["lanes"]}


# --- People: the person roles of scenarios/roles.json ----------------------

ROLES = [r for r in graph.roles(ROOT) if "person" in r.get("actorKinds", [])]


def roles_of(code):
    return [r for r in ROLES if r["id"] in lane_roles(code)]


# --- Systems: the system actors of scenarios/actors/ ------------------------
# A system actor is an ApplicationComponent; the journeys it serves are the
# journeys whose BPMN has a lane played by one of its roles. Its parts are the
# components of VaxLink's architecture view, each a specialization of the RA
# building block it instantiates. A component names the system that hosts it,
# and nothing else: its journeys are its system's.

ACTORS = {a["id"]: a for a in graph.actors(ROOT)}
SYSTEMS = [a for a in ACTORS.values() if a["kind"] == "system"]
SYSTEM_JOURNEYS = {a["id"]: graph.journeys_of_roles(a["roles"], PROCESSES) for a in SYSTEMS}


# A system actor is an ApplicationComponent, except one that is a device: the
# family's shared phone is the Holder's device (its actor says so), a
# technology Device that realizes the wallet app on it, not software.
SYSTEM_TYPE = {"family-phone": "Device"}


def system_type(actor_id):
    return SYSTEM_TYPE.get(actor_id, "ApplicationComponent")


def holds(actor_id):
    """How a system relates to its parts, drawn as nesting: an application composes them; a device realizes them."""
    return "Realization" if system_type(actor_id) == "Device" else "Composition"


def skey(actor_id):
    return "sys-" + actor_id


# The parts are each system actor's meta.parts in scenarios/actors/ (id,
# title, the RA building block it plays by the RA's own name, what it is in
# the IG, and what it does): read from there, in actor order, as
# (key, name, RA block, hosting system actor, what it is in the IG).
RA_KEY = {n: k for k, n in RA_NAME.items()}
COMPONENTS = []
for _a in ACTORS.values():
    for _p in _a.get("meta", {}).get("parts", []):
        assert _p["raBlock"] in RA_KEY, f"scenarios/actors/{_a['id']}.json: part {_p['id']} plays {_p['raBlock']!r}, not an RA block named in RA_NAME"
        COMPONENTS.append((_p["id"], _p["title"], RA_KEY[_p["raBlock"]], _a["id"], _p.get("ig", "")))
PART_DESCRIPTION = {_p["id"]: _p["description"] for _a in ACTORS.values() for _p in _a.get("meta", {}).get("parts", [])}
for _k, _n, _ra, _a, _ig in COMPONENTS:
    assert _a in ACTORS and ACTORS[_a]["kind"] == "system", f"component {_k}: {_a} is not a system actor in scenarios/actors/"
COUNTRY_OF = {"xxr": "Taifafeki", "xxk": "Onesa"}
PARTS = {a["id"]: [c for c in COMPONENTS if c[3] == a["id"]] for a in SYSTEMS}
SYSTEM_COUNTRY = {a: ACTORS[a]["meta"]["country"] for a, ps in PARTS.items() if ps}
assert set(SYSTEM_COUNTRY.values()) <= set(COUNTRY_OF.values()), "a system actor's meta.country is Taifafeki or Onesa"

# WHO GDHCN, the trust network beneath both countries (an external actor,
# with no lane of its own): it serves the trust components that publish a key
# to it or read its list, and so the journeys of the systems that host them.
GDHCN = ("gdhcn", "WHO GDHCN trust network (DEV)", "gdhcn-dev-trust-anchor")
GDHCN_SERVES = ["xxr-dvc-signer", "xxr-vhl-viewer", "xxk-dvc-verifier", "xxk-vhl-issuer"]
_HOST = {c[0]: c[3] for c in COMPONENTS}
GDHCN_JOURNEYS = [j for j in JOURNEYS if any(j in SYSTEM_JOURNEYS[_HOST[k]] for k in GDHCN_SERVES)]

# The issuer's signing key (an external actor with a lane of its own in J1):
# technology, not software the hospital runs, since the issuing system never
# holds the private key (two-phase signing). A Node, the HSM, cloud KMS or
# keystore that holds it, in its own country (meta.country), Serving the part
# it signs for and the journeys its lane is in that the part's system serves
# (the issuer-key lane of J4.0 is the Onesan portal's key, which no actor plays
# yet). (actor, the part it serves)
SIGNING_KEYS = [("xxr-dsc-key", "xxr-dvc-signer")]
KEY_JOURNEYS = {a: [j for j in graph.journeys_of_roles(ACTORS[a]["roles"], PROCESSES) if j in SYSTEM_JOURNEYS[_HOST[k]]] for a, k in SIGNING_KEYS}
KEY_COUNTRY = {a: ACTORS[a]["meta"]["country"] for a, _k in SIGNING_KEYS}
for _a, _k in SIGNING_KEYS:
    assert ACTORS[_a]["kind"] == "external" and len(ACTORS[_a]["roles"]) == 1, f"{_a}: an external actor with one role"
    assert _k in _HOST and SYSTEM_COUNTRY[_HOST[_k]] == KEY_COUNTRY[_a], f"{_a} serves {_k}, a part in its own country"


def kkey(actor_id):
    return "key-" + actor_id

# The building-block catalogue the journeys' steps use (archimate/building-blocks/,
# the harness's building-blocks kind) is the one source of which block an
# element realizes: each component it names must be an element here, and the
# element carries its blocks as a property.
CATALOGUE = json.loads((ROOT / "archimate" / "building-blocks" / "building-blocks.json").read_text(encoding="utf-8"))
BLOCKS_OF = {}
for _b in CATALOGUE["blocks"]:
    for _c in _b.get("components", []):
        assert _c in _HOST or _c == GDHCN[0], f"building block {_b['id']}: component {_c} is not an element of this overlay"
        BLOCKS_OF.setdefault(_c, []).append(_b["id"])


def _blocks(key):
    return {"buildingBlocks": ", ".join(BLOCKS_OF[key])} if key in BLOCKS_OF else {}

# What both countries share, between them: GDHCN and the specifications it
# realizes. A Requirement, which an ApplicationComponent may realize.
TRUST_FRAMEWORK = ("trust-framework", "WHO SMART Trust specifications (HCERT, DVC, VHL)")

# --- Jurisdictions: each country's instance of the RA blocks it uses -------
# Taifafeki and Onesa are different jurisdictions: a Taifafeki part is an
# instance of Taifafeki's provider systems, not of Onesa's. So each country
# has its own instance of every RA block its parts play, keyed <cc>-<RA key>
# (xxr-ra-provider-systems), which specializes the RA block; the country's
# parts specialize that instance.
CC = {v: k for k, v in COUNTRY_OF.items()}


def ikey(country, ra):
    return f"{CC[country]}-{ra}"


def instance_of(component):
    """The key of the per-country RA instance a COMPONENTS row specializes."""
    return ikey(SYSTEM_COUNTRY[component[3]], component[2])


INSTANCES = sorted({(SYSTEM_COUNTRY[c[3]], c[2]) for c in COMPONENTS}, key=lambda t: (t[0] != "Taifafeki", ORDER.index(t[1])))

# --- Where the countries meet ------------------------------------------------
# A sequence flow from a task in one system's lane to a task in another's,
# through any number of nodes in people's (or external actors') lanes, is a
# hand-over between those two systems; where the systems are in different
# countries it is an interaction between the two jurisdictions. Its ends are
# the parts that do the two tasks: a system's only part, or the part
# TASK_PART names for the task's skill. A hand-over answered by a hand-over
# straight back (a request and its response) is a Triggering; any other a
# Flow. INTERACTION_NAME gives a line a short label (the target task's name
# otherwise).
SYSTEM_OF_ROLE = {r: a["id"] for a in SYSTEMS for r in a["roles"]}
TASK_PART = {
    ("kesaro-provincial-hospital", "hcert-prefix-context"): "xxr-dvc-signer",
    ("district-health-center-ehr", "hcert-verify"): "xxk-dvc-verifier",
    ("onesa-national-portal", "portal-serve-manifest"): "xxk-info-gateway",
}
INTERACTION_NAME = {
    ("J4.1", "Task_Open", "Task_Verify"): "VHL QR, shown",
    ("J4.1", "Task_Fetch", "Task_Release"): "ITI-YY5 manifest request, signed",
    ("J4.1", "Task_Release", "Task_Decrypt"): "manifest; access logged in Onesa",
}
# Hand-overs between journeys, which no single BPMN draws: the paper DVC J1
# prints is what the family shows in J2 and J3. (journey, task, journey, task, label)
HANDOFFS = [
    ("J1", "Task_Finish", "J2", "Task_Read", "paper DVC (HC1 QR), carried by the family"),
    ("J1", "Task_Finish", "J3", "Task_Verify", "paper DVC (HC1 QR), carried by the family"),
]


def _system_of(p, node):
    lane = next((l for l in p["lanes"] if node in l["nodes"]), None)
    return SYSTEM_OF_ROLE.get(lane["role"]) if lane else None


def _part_of(p, node):
    actor = _system_of(p, node)
    skill = next((t["skill"] for t in p["tasks"] if t["id"] == node), None)
    if len(PARTS[actor]) == 1:
        return PARTS[actor][0][0]
    assert (actor, skill) in TASK_PART, f"{p['stem']}: task {node} of {actor} ({skill}) names no part: add it to TASK_PART"
    return TASK_PART[(actor, skill)]


def _hops(p):
    """(source node, target node) for every hand-over from one system's task to another's."""
    nxt = {}
    for a, b in p["flows"]:
        nxt.setdefault(a, []).append(b)
    out = []
    for n in [x for l in p["lanes"] for x in l["nodes"]]:
        a = _system_of(p, n)
        if not a:
            continue
        seen, todo = set(), list(nxt.get(n, []))
        while todo:
            m = todo.pop(0)
            if m in seen:
                continue
            seen.add(m)
            b = _system_of(p, m)
            if b is None:
                todo += nxt.get(m, [])
            elif b != a:
                out.append((n, m))
    return out


def _interactions():
    found = {}
    for code, p in JOURNEYS.items():
        hops = _hops(p)
        for n, m in hops:
            a, b = _system_of(p, n), _system_of(p, m)
            if SYSTEM_COUNTRY[a] == SYSTEM_COUNTRY[b]:
                continue
            back = any(x == m and _system_of(p, y) == a for x, y in hops)
            rel = ("Triggering" if back else "Flow", _part_of(p, n), _part_of(p, m))
            name = INTERACTION_NAME.get((code, n, m), p["names"].get(m, m))
            found.setdefault(rel, [name, []])[1].append(code)
    for j1, t1, j2, t2, name in HANDOFFS:
        p1, p2 = JOURNEYS[j1], JOURNEYS[j2]
        assert t1 in p1["names"] and t2 in p2["names"], f"HANDOFFS: {j1} {t1} or {j2} {t2} is not in the BPMN"
        a, b = _system_of(p1, t1), _system_of(p2, t2)
        assert SYSTEM_COUNTRY[a] != SYSTEM_COUNTRY[b], f"HANDOFFS: {j1} {t1} and {j2} {t2} are in one country"
        found.setdefault(("Flow", _part_of(p1, t1), _part_of(p2, t2)), [name, []])[1] += [j1, j2]
    return [(t, a, b, name, sorted(set(js), key=list(JOURNEYS).index)) for (t, a, b), (name, js) in found.items()]


INTERACTIONS = _interactions()  # (type, source part, target part, label, journeys)

IG_BASE = "https://litlfred.github.io/smart-trust-demo/"


def _ig(ref):
    if not ref:
        return {}
    kind, rid = ref.split("/")
    return {"ig": f"{IG_BASE}artifact/{kind}-{rid}.html"}


# --- Glossary and FHIR actors ----------------------------------------------
# Every element the overlay adds names its concept in this instance's glossary
# (glossary/architecture.glossary.json, written by tools/ig-gen/ig_gen.py
# from the same sources: scenarios/roles.json, scenarios/actors/ and the
# BPMN), by the skosConcept property cat-harness's archimate pages read; the
# model is drawn from the glossary's sources, never the other way. Each role
# and system names the FHIR ActorDefinition it realizes (fhir-actor), as
# cat-harness's archimate-models skill asks; ig_gen.py writes those too.
GLOSSARY_FILE = ROOT / "glossary" / "architecture.glossary.json"
GLOSSARY_NS = "https://litlfred.github.io/smart-trust-demo/v0/ns/glossary/architecture/"
_TERMS = {t["id"]: t for t in __import__("json").loads(GLOSSARY_FILE.read_text(encoding="utf-8"))["terms"]}
ACTOR_CANONICAL = "http://smart.who.int/trust-demo/ActorDefinition/TrustDemo.Role."


def concept(term):
    """The element's concept, and its short form (the term's first altLabel, generated by ig_gen.py) when it has one."""
    assert term in _TERMS, f"{term} is not a term of {GLOSSARY_FILE.relative_to(ROOT)}: run python3 tools/ig-gen/ig_gen.py"
    alt = _TERMS[term].get("altLabel") or []
    return {"skosConcept": GLOSSARY_NS + term, **({"altLabel": alt[0]} if alt and term.split("-")[0] in ("actor", "journey") else {})}


def instance_term(country, ra_name):
    """The glossary id of a country's instance of an RA block (tools/ig-gen/ig_gen.py names it the same)."""
    import re as _re
    slug = lambda t: _re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return f"instance-{slug(country)}-{slug(ra_name)}"


def fhir_actor(role_id):
    import re as _re
    return ACTOR_CANONICAL + "".join(w[:1].upper() + w[1:] for w in _re.split(r"[^A-Za-z0-9]+", role_id) if w)


# --- Elements --------------------------------------------------------------

ELEMENTS = {
    "country-xxr": ("Grouping", "Taifafeki (Country A, XXR)", "The jurisdiction where the newborn is born (J1) and later seen at the point of care (J4.1): its systems and its instances of the RA building blocks.", {}),
    "country-xxk": ("Grouping", "Onesa (Country B, home)", "The family’s home jurisdiction (J2, J3, J4.0), whose national portal serves their records abroad (J4.1): its systems and its instances of the RA building blocks.", {}),
    "intl": ("Grouping", "International: shared by both", "What the two jurisdictions share, and nothing else: WHO GDHCN and the WHO SMART Trust specifications. Neither country’s systems connect to the other’s except through what the family carries and the VHL fetch.", {}),
    "group-ra": ("Grouping", "Reference architecture (DPI-H RA)", "The DPI-H RA’s own building blocks, by the layers of its Integrated View (Fig. 3.2): generic, no country’s. Each country’s instance of a block specializes it.", {}),
    "group-journeys": ("Grouping", "Journeys (use cases)", "The demonstrator's user journeys, one BPMN process each, in processes/content/.", {}),
    "group-people": ("Grouping", "People", "The roles people play in the journeys (scenarios/roles.json); every persona is fictional.", {}),
    "group-capabilities": ("Grouping", "DPI-H RA capabilities exercised", "The capabilities of the RA's Integrated View that the journeys realize.", {}),
}

for code, p in JOURNEYS.items():
    ELEMENTS[jkey(code)] = ("BusinessProcess", p["name"],
                            f"{p['name']}: journey {code} of the SMART Trust demonstrator. Its steps, lanes and the requirements they trace to are in the BPMN process.",
                            {"journey": code, "bpmn": f"processes/content/{p['stem']}.bpmn", "bpmnProcess": p["id"],
                             "ig": f"{IG_BASE}business-processes.html", **concept(jkey(code))})

for r in ROLES:
    ELEMENTS["role-" + r["id"]] = ("BusinessRole", r["title"], r["description"],
                                   {"role": r["id"], **({"otherNames": "; ".join(r["otherNames"])} if r.get("otherNames") else {}),
                                    **concept("role-" + r["id"]), "fhir-actor": fhir_actor(r["id"])})

for a in SYSTEMS:
    js = SYSTEM_JOURNEYS[a["id"]]
    assert len(a["roles"]) == 1, f"{a['id']}: one fhir-actor tag per element (add_views.py keys properties by name)"
    ELEMENTS[skey(a["id"])] = (system_type(a["id"]), a["title"],
                               f"{a['title']}: {a.get('description', '')}".strip(),
                               {"scenarioActor": f"scenarios/actors/{a['id']}.json", "roles": ", ".join(a["roles"]),
                                "journeys": ", ".join(js) if js else "none (no lane)",
                                **({"country": SYSTEM_COUNTRY[a["id"]]} if a["id"] in SYSTEM_COUNTRY else {}),
                                **concept("actor-" + a["id"]), "fhir-actor": fhir_actor(a["roles"][0])})

for key, name, _ra, actor, ig in COMPONENTS:
    ELEMENTS[key] = ("ApplicationComponent", name,
                     f"{SYSTEM_COUNTRY[actor]}, part of {ACTORS[actor]['title']}: {PART_DESCRIPTION[key]}",
                     {"country": SYSTEM_COUNTRY[actor], "partOf": f"scenarios/actors/{actor}.json", "raBlock": RA_NAME[_ra], **_ig(ig),
                      **concept("part-" + key), **_blocks(key)})

for a, k in SIGNING_KEYS:
    ELEMENTS[kkey(a)] = ("Node", ACTORS[a]["title"], f"{ACTORS[a]['title']}: {ACTORS[a].get('description', '')}".strip(),
                         {"scenarioActor": f"scenarios/actors/{a}.json", "roles": ", ".join(ACTORS[a]["roles"]),
                          "journeys": ", ".join(KEY_JOURNEYS[a]), "country": KEY_COUNTRY[a],
                          **concept("actor-" + a), "fhir-actor": fhir_actor(ACTORS[a]["roles"][0])})

ELEMENTS[GDHCN[0]] = ("ApplicationComponent", ACTORS[GDHCN[2]]["title"],
                      "WHO’s Global Digital Health Certification Network: the trust list of participants’ public keys that lets an Onesan clinic believe a Taifafeki certificate, and a Taifafeki clinic an Onesan link, with no connection between the two countries' systems. Not a building block of the RA's Integrated View: it sits beneath both countries.",
                      {"scenarioActor": f"scenarios/actors/{GDHCN[2]}.json", "spec": "https://smart.who.int/trust/",
                       **concept("actor-" + GDHCN[2]), "fhir-actor": fhir_actor(ACTORS[GDHCN[2]]["roles"][0]), **_blocks(GDHCN[0])})

ELEMENTS[TRUST_FRAMEWORK[0]] = ("Requirement", TRUST_FRAMEWORK[1],
                                "The specifications both countries’ systems conform to, so that a certificate signed in one is read in the other: HCERT and the DVC payload (WHO SMART Trust), and the Verifiable Health Link (WHO SMART Trust and IHE ITI VHL). GDHCN realizes the trust network they assume.",
                                {"spec": "https://smart.who.int/trust/", "phw": "https://smart.who.int/trust-phw/"})

for country, ra in INSTANCES:
    ELEMENTS[ikey(country, ra)] = ("ApplicationComponent", f"{RA_NAME[ra]} ({country})",
                                   f"{country}’s instance of the DPI-H RA building block {RA_NAME[ra]}: what {country}’s parts in the demonstrator that play this block are, and a specialization of the RA’s block. One per jurisdiction, since neither country’s systems are the other’s.",
                                   {"country": country, "raBlock": EXISTING[ra], **concept(instance_term(country, RA_NAME[ra]))})

# --- Relationships ---------------------------------------------------------

RELATIONS = []
for a in SYSTEMS:
    for j in SYSTEM_JOURNEYS[a["id"]]:
        RELATIONS.append(("Serving", skey(a["id"]), jkey(j)))
    for c in PARTS[a["id"]]:
        RELATIONS.append((holds(a["id"]), skey(a["id"]), c[0]))
# A concrete part realizes its country's instance of an RA block, as the RA
# draws a concrete system realizing the component (role) it plays (Table 3.3,
# Application Component Realization Application Component); the country's
# instance is a kind of the RA's block.
for c in COMPONENTS:
    RELATIONS.append(("Realization", c[0], instance_of(c)))
for country, ra in INSTANCES:
    RELATIONS.append(("Specialization", ikey(country, ra), ra))
for t, a, b, name, _js in INTERACTIONS:
    RELATIONS.append((t, a, b, {"name": name}))
RELATIONS.append(("Realization", "gdhcn", TRUST_FRAMEWORK[0]))
for a, k in SIGNING_KEYS:
    RELATIONS.append(("Serving", kkey(a), k))
    for j in KEY_JOURNEYS[a]:
        RELATIONS.append(("Serving", kkey(a), jkey(j)))
for j in GDHCN_JOURNEYS:
    RELATIONS.append(("Serving", "gdhcn", jkey(j)))
for k in GDHCN_SERVES:
    RELATIONS.append(("Serving", "gdhcn", k))
for r in ROLES:
    for code in JOURNEYS:
        if r["id"] in lane_roles(code):
            RELATIONS.append(("Assignment", "role-" + r["id"], jkey(code)))
for code in JOURNEYS:
    for c in caps(code):
        RELATIONS.append(("Realization", jkey(code), c))
for r in ROLES:
    if r["id"] in ROLE_STAKEHOLDER:  # a role not mapped yet is drawn without one
        RELATIONS.append(("Association", "role-" + r["id"], ROLE_STAKEHOLDER[r["id"]]))
GROUP_MEMBERS = {
    "country-xxr": [skey(a) for a, c in SYSTEM_COUNTRY.items() if c == "Taifafeki"] + [kkey(a) for a, c in KEY_COUNTRY.items() if c == "Taifafeki"] + [ikey(c, ra) for c, ra in INSTANCES if c == "Taifafeki"],
    "country-xxk": [skey(a) for a, c in SYSTEM_COUNTRY.items() if c == "Onesa"] + [kkey(a) for a, c in KEY_COUNTRY.items() if c == "Onesa"] + [ikey(c, ra) for c, ra in INSTANCES if c == "Onesa"],
    "intl": ["gdhcn", TRUST_FRAMEWORK[0]],
    "group-ra": [l for l, _bs in RA_LAYERS],
    "group-journeys": [jkey(c) for c in JOURNEYS],
    "group-people": ["role-" + r["id"] for r in ROLES],
    "group-capabilities": sorted({c for code in JOURNEYS for c in caps(code)}),
}
for g, ms in GROUP_MEMBERS.items():
    for m in ms:
        RELATIONS.append(("Aggregation", g, m))

# --- Views -----------------------------------------------------------------
# One element appears at most once in a view (add_views keys a view's boxes by
# element). add_views.py packs boxes 12 px apart; build.py then lays each of
# these views out again from the same tree (or the one LAYOUT_TREES names)
# with LAYOUT's gaps, so lines have room to pass between boxes, and routes
# every line orthogonally through those gaps (Archi bendpoints), never through
# a box. A system is drawn as a box holding its parts (the composition). Each
# country is a band (in the Integrated View, a column); what the two share
# sits between them.

LAYOUT = {"gap": 40, "pad": 24, "head": 28}  # build.py: between siblings, inside a group, a group's heading
_LEAF_W = 170  # add_views.py's box width


def _parts_by_layer(actor_id, among=None):
    return sorted([c for c in PARTS[actor_id] if among is None or c[0] in among], key=lambda c: ORDER.index(c[2]))


def _systems_by_layer(actor_ids):
    return sorted(actor_ids, key=lambda a: ORDER.index(_parts_by_layer(a)[0][2]))


def box(k):
    return ("box", k)


def system_box(actor_id, across=False, among=None):
    """A system holding its parts (those in among, if given): stacked, or side by side (a journey view, so each part's line runs down)."""
    parts = _parts_by_layer(actor_id, among)
    return ("group", skey(actor_id), len(parts) if across else 1, [box(c[0]) for c in parts])


def country_systems(country, among=None):
    ids = [a for a, c in SYSTEM_COUNTRY.items() if c == country and (among is None or a in among)]
    return _systems_by_layer(ids)


def country_instances(parts):
    """The per-country RA instances the parts (in drawing order) specialize, in the order their first part is drawn."""
    out = []
    for c in parts:
        if instance_of(c) not in out:
            out.append(instance_of(c))
    return out


# Each RA instance drawn stands right under the first part drawn that
# specializes it, so that line runs straight down (build.py's layout).
ALIGN_UNDER = {}


def _align(view, parts):
    for c in parts:
        ALIGN_UNDER.setdefault(view, {}).setdefault(instance_of(c), c[0])


def specializations(parts):
    """Each part's line to its country's RA instance, and each instance's to the RA block."""
    insts = country_instances(parts)
    by_key = {ikey(c, ra): ra for c, ra in INSTANCES}
    return [("Realization", c[0], instance_of(c)) for c in parts] + [("Specialization", i, by_key[i]) for i in insts]


def interactions(keys, code=None):
    """The interactions between parts drawn (keys), of one journey or all."""
    return [(t, a, b) for t, a, b, _n, js in INTERACTIONS if a in keys and b in keys and (code is None or code in js)]


SYSTEMS_VIEW = "SMART Trust demo on the DPI-H Integrated View"
JOURNEYS_VIEW = "SMART Trust demo journeys (use cases)"

# The journeys view, laid out so its lines cross as little as they can: each
# person who takes part in one journey stands under it (their assignment is a
# vertical line), and the caregiver, who takes part in all five, stands at
# the end. VIEW_BOUNDS (applied by build.py after its layout) moves a few
# boxes to exact positions: the capabilities spread over the journeys, Health
# Workers centred under the four health workers, Citizens / Care recipients
# under the caregiver. A person role not in PEOPLE_ORDER is drawn after these.
PEOPLE_ORDER = ["birth-clinic-vaccinator", "community-health-worker", "home-clinic-provider", "poc-provider", "caregiver"]
PEOPLE = [r for r in PEOPLE_ORDER if r in {x["id"] for x in ROLES}] + [r["id"] for r in ROLES if r["id"] not in PEOPLE_ORDER]
_PAD, _GAP = LAYOUT["pad"], LAYOUT["gap"]


def _col(i):
    """x of the i-th box (fractional i allowed) inside a group, relative to the group."""
    return round(_PAD + i * (_LEAF_W + _GAP))


_GROUP_W = 2 * _PAD + 5 * _LEAF_W + 4 * _GAP  # a five-box group, as wide as the journeys
VIEW_BOUNDS = {
    JOURNEYS_VIEW: {
        "group-capabilities": {"width": _GROUP_W},
        "cap-access-consent-trust": {"x": _col(1)},
        "cap-clinical-services": {"x": _col(2)},
        "cap-health-record-mgmt": {"x": _col(3)},
        "stk-health-workers": {"x": 24 + _col(1.5)},
        "stk-care-recipients": {"x": 24 + _col(4)},
    },
}


def journey_view_name(code):
    return f"{code} on the DPI-H RA"


def journey_view(code):
    """One journey: its capabilities, its people, the systems that serve it (with their parts), the parts of the other country it meets, each country's RA instances and the RA blocks they specialize."""
    serving = [a["id"] for a in SYSTEMS if code in SYSTEM_JOURNEYS[a["id"]]]
    shown = {c[0] for a in serving for c in PARTS[a]}
    for _t, a, b, _n, js in INTERACTIONS:
        if code in js:
            shown |= {a, b}
    actors = [a["id"] for a in SYSTEMS if any(c[0] in shown for c in PARTS[a["id"]])]
    bands, parts = [], []
    for country, gkey in (("Taifafeki", "country-xxr"), ("Onesa", "country-xxk")):
        sys_ = country_systems(country, actors)
        if not sys_:
            continue
        ps = [c for a in sys_ for c in _parts_by_layer(a, shown)]
        parts += ps
        keys_ = [kkey(a) for a, k in SIGNING_KEYS if KEY_COUNTRY[a] == country and code in KEY_JOURNEYS[a] and k in {c[0] for c in ps}]
        bands.append(("group", gkey, 1, [("row", [system_box(a, across=True, among=shown) for a in sys_] + [box(k) for k in keys_]),
                                         ("row", [box(i) for i in country_instances(ps)])]))
    blocks = {c[2] for c in parts}
    layers = [(l, [b for b in bs if b in blocks]) for l, bs in RA_LAYERS]
    if code in GDHCN_JOURNEYS:
        bands.insert(1 if len(bands) > 1 else len(bands), ("group", "intl", 1, [box("gdhcn")]))
    rows = []
    if caps(code):
        rows.append(("row", [box(c) for c in caps(code)]))
    people = roles_of(code)
    rows.append(("row", ([("group", "group-people", 1, [box("role-" + r["id"]) for r in people])] if people else []) + [box(jkey(code))]))
    if bands:
        rows.append(("row", bands))
    if any(bs for _l, bs in layers):
        rows.append(("group", "group-ra", 1, [("row", [("group", l, len(bs), [ra_box(b) for b in bs]) for l, bs in layers if bs])]))
    _align(journey_view_name(code), parts)
    keys = {c[0] for c in parts}
    conns = [("Realization", jkey(code), c) for c in caps(code)]
    conns += [("Assignment", "role-" + r["id"], jkey(code)) for r in people]
    conns += [("Serving", skey(a), jkey(code)) for a in serving]
    drawn = {c[0] for c in parts}
    for a, k in SIGNING_KEYS:
        if code in KEY_JOURNEYS[a] and k in drawn:
            conns += [("Serving", kkey(a), jkey(code)), ("Serving", kkey(a), k)]
    conns += specializations(parts)
    conns += interactions(keys, code)
    if code in GDHCN_JOURNEYS:
        conns += [("Serving", "gdhcn", jkey(code))]
        conns += [("Serving", "gdhcn", k) for k in GDHCN_SERVES if k in keys]
    doc = (f"Journey {code} ({JOURNEYS[code]['name']}): the people assigned to it (its BPMN lanes), the systems that serve it "
           f"(the system actors that play its lanes, each holding its parts) and the other country’s parts it hands over to, "
           f"each country’s instances of the DPI-H RA building blocks those parts specialize, and the RA capabilities it realizes.")
    return (journey_view_name(code), doc, ("col", rows)), conns


# The Integrated View is drawn in two columns, Taifafeki left and Onesa
# right, with what they share between them; LAYOUT_TREES gives build.py that
# layout, and add_views.py draws the same boxes from lowered(), which has only
# the node kinds it knows. In a column the country's systems stack top to
# bottom in the order of the first journey each serves, each holding its parts
# (nesting is the composition, or for the phone the realization) as a grid of
# at most COLUMN_SLOTS[country] boxes across, the parts that meet the other
# country or GDHCN on the side that faces the middle. Each part says, inside
# its own box, which DPI-H RA building block it plays («Provider Systems»: a
# note build.py adds, NOTES), rather than a line to a box of its country's
# instance of that block: those boxes stood outside the systems and drew 18
# lines that said what a word can. The instances, the realizations and the
# RA's own blocks are in the model and in each journey's view.
COLUMN_SLOTS = {"Taifafeki": 2, "Onesa": 3}
FACING = {"Taifafeki": "right", "Onesa": "left"}
MEETS = {k for _t, a, b, _n, _j in INTERACTIONS for k in (a, b)} | set(GDHCN_SERVES)
PART_W, PART_H = 170, 88  # room for a two-line name and a two-line «block» tag
NOTES = {}  # view name: {part key: the tag build.py writes inside its box}


def _first_journey(actor_id):
    return min([list(JOURNEYS).index(j) for j in SYSTEM_JOURNEYS[actor_id]] or [len(JOURNEYS)])


def space(slots):
    """Room for slots grid cells and the gaps after them, in a row."""
    return ("space", slots * (PART_W + LAYOUT["gap"]) - LAYOUT["gap"], 0)


def _load_layout():
    import importlib.util
    spec = importlib.util.spec_from_file_location("archimate_layout", Path(__file__).resolve().parent / "layout.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_layout = _load_layout()


def _height(node):
    """A layout node's height as build.py lays it out."""
    return _layout._size(node, LAYOUT)[1]


def country_column(country, gkey, level=None):
    """(the country's band as a column, its parts in drawing order, the y of each system in it).

    level = {system: y}: that system is pushed down to stand at y (relative
    to the column's first box), if it would stand higher.
    """
    n_slots, right = COLUMN_SLOTS[country], FACING[country] == "right"
    kids, parts, at = [], [], {}
    gap = LAYOUT["gap"]
    y = lambda: sum(_height(k) + gap for k in kids)
    systems = country_systems(country)
    for a in sorted(systems, key=lambda a: (_first_journey(a), systems.index(a))):
        ps = sorted(_parts_by_layer(a), key=lambda c: c[0] not in MEETS)
        n = min(n_slots, len(ps))
        cells = []
        for i in range(0, len(ps), n):
            row = ps[i:i + n]
            row = ([None] * (n - len(row)) + row[::-1]) if right else row + [None] * (n - len(row))
            cells += row
        parts += [c for c in cells if c is not None]
        sysbox = ("group", skey(a), 1, [("grid", n, [("box", c[0], PART_W, PART_H) if c else None for c in cells], 0)])
        want = (level or {}).get(a)
        if want is not None and want - y() - gap >= 0:
            kids.append(("space", 0, want - y() - gap))
        at[a] = y()
        off = n_slots - n if right else 0
        kids.append(("row", [space(off), sysbox]) if off else sysbox)
        # A signing key stands under the system whose part it signs for, on the side that faces the middle.
        for k in [kkey(x) for x, part in SIGNING_KEYS if _HOST[part] == a]:
            kbox = ("box", k, PART_W, PART_H)
            kids.append(("row", [space(n_slots - 1), kbox]) if right and n_slots > 1 else kbox)
    return ("group", gkey, 1, kids), parts, at


def lowered(node):
    """node with only add_views.py's kinds (box, group, row, col): a grid becomes a column of rows; a space goes."""
    if node[0] == "box":
        return node[:2]
    if node[0] == "grid":
        rows = [[k for k in node[2][i:i + node[1]] if k is not None] for i in range(0, len(node[2]), node[1])]
        return ("col", [("row", [lowered(k) for k in r]) for r in rows if r])
    if node[0] == "group":
        return ("group", node[1], node[2], [lowered(k) for k in node[3] if k[0] != "space"])
    return (node[0], [lowered(k) for k in node[1] if k[0] != "space"])


LAYOUT_TREES = {}


def _systems_view():
    """Taifafeki (left) and Onesa (right) as columns, what they share between them.

    Onesa is laid out first: each Taifafeki system stands level with the first
    Onesan system it meets, so the lines where they meet run across.
    """
    la, la_parts, la_at = country_column("Onesa", "country-xxk")
    level = {}
    for _t, a, b, _n, _js in INTERACTIONS:
        th_end, la_end = (a, b) if SYSTEM_COUNTRY[_HOST[a]] == "Taifafeki" else (b, a)
        level[_HOST[th_end]] = min(level.get(_HOST[th_end], 1e9), la_at[_HOST[la_end]])
    th, th_parts, _ = country_column("Taifafeki", "country-xxr", level)
    intl = ("group", "intl", 1, [box("gdhcn"), box(TRUST_FRAMEWORK[0])])
    # The shared band stands just above the lowest level where the countries
    # meet (the Taifafeki system lowest down), so the lines there run straight
    # across under it, and those above it over it.
    lift = max(level.values()) - _height(intl) - LAYOUT["gap"]
    layout = ("row", [th, ("col", [("space", 0, lift - LAYOUT["gap"]), intl]) if lift >= LAYOUT["gap"] else intl, la])
    LAYOUT_TREES[SYSTEMS_VIEW] = layout
    NOTES[SYSTEMS_VIEW] = {c[0]: f"«{RA_NAME[c[2]]}»" for c in th_parts + la_parts}
    conns = interactions({c[0] for c in COMPONENTS})
    conns += [("Serving", "gdhcn", k) for k in GDHCN_SERVES] + [("Realization", "gdhcn", TRUST_FRAMEWORK[0])]
    conns += [("Serving", kkey(a), k) for a, k in SIGNING_KEYS]
    doc = ("The two jurisdictions the demonstrator spans, Taifafeki (left) and Onesa (right), with what they share between them: "
           "WHO GDHCN and the WHO SMART Trust specifications. In each country its systems hold their parts, and each part says "
           "inside its box which DPI-H RA building block it plays («Provider Systems»): it realizes its own country’s instance of "
           "that block, a kind of the RA’s own, drawn in each journey’s view. The lines that run from one country to the other "
           "are where they meet: the paper DVC the family carries from J1 to J2 and J3, and the VHL QR and ITI-YY5 manifest fetch "
           "of J4.1, logged in Onesa.")
    return (SYSTEMS_VIEW, doc, lowered(layout)), conns


_sv, _sv_conns = _systems_view()
VIEWS = [
    _sv,
    (JOURNEYS_VIEW,
     "The demonstrator’s journeys as business processes: the people assigned to each (its BPMN lanes), the DPI-H RA stakeholders those people belong to, and the RA capabilities it realizes. The systems that serve each journey are in that journey’s own view.",
     ("col", [
         ("group", "group-capabilities", 3, [box(c) for c in GROUP_MEMBERS["group-capabilities"]]),
         ("group", "group-journeys", len(JOURNEYS), [box(jkey(c)) for c in JOURNEYS]),
         ("group", "group-people", 5, [box("role-" + r) for r in PEOPLE]),
         ("row", [box("stk-health-workers"), box("stk-care-recipients")]),
     ])),
]

VIEW_CONNECTIONS = {
    SYSTEMS_VIEW: _sv_conns,
    JOURNEYS_VIEW: [r[:3] for r in RELATIONS if r[0] in ("Assignment", "Association") or (r[0] == "Realization" and r[1].startswith("journey-"))],
}
for _code in JOURNEYS:
    _v, _c = journey_view(_code)
    VIEWS.append(_v)
    VIEW_CONNECTIONS[_v[0]] = _c
