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
- the systems, as ApplicationComponent elements grouped by country: the
  system actors of scenarios/actors/, each Serving the journeys whose BPMN
  has a lane played by one of its roles, and Composed of its parts, the
  components of VaxLink's architecture view (litlfred/vaxlink,
  ArchitectureDiagram.tsx), each a Specialization of the RA building block
  it is an instance of in its own country;
- each country's instance of every RA building block its parts play
  ("Provider Systems (Thailand)", "Provider Systems (Lao PDR)"): a
  Specialization of the RA block, and what the country's parts specialize,
  since Thailand and Lao PDR are different jurisdictions and neither's systems
  are the other's;
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
Composition, Specialization, Flow and Triggering (between two
ApplicationComponents), Realization (BusinessProcess to Capability, and
ApplicationComponent to Requirement), Association (BusinessRole to
Stakeholder) and Aggregation (from a Grouping).

build.py lays the overlay's views out again with room between the boxes
(LAYOUT) and routes every line orthogonally through the gaps, writing the
route as Archi bendpoints.
"""

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
    "birth-clinic-vaccinator": "stk-health-workers",
    "community-health-worker": "stk-health-workers",
    "home-clinic-provider": "stk-health-workers",
    "poc-provider": "stk-health-workers",
}

# Which RA blocks each Integrated View layer shows here (all of them are
# members of that layer's Grouping in smart-ra already).
RA_LAYERS = [
    ("layer-pos", ["ra-provider-systems", "ra-chw", "ra-citizen-apps"]),
    ("layer-reusable", ["ra-terminology", "ra-cdss", "ra-hmis"]),
    ("layer-shared", ["ra-client-registry", "ra-facility-registry", "ra-workforce-registry", "ra-product-registry", "ra-lhr"]),
    ("layer-dpif", ["ra-trust-services", "ra-mediator"]),
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
ORDER = [b for _l, bs in RA_LAYERS for b in bs]
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
# journey; a new BPMN file appears here with no edit. JOURNEY_SHORT gives a
# box its short name (the process name otherwise); JOURNEY_CAPABILITIES the
# RA capabilities a journey exercises (none otherwise).

JOURNEYS = {p["code"]: p for p in PROCESSES if p["code"]}

JOURNEY_SHORT = {
    "J1": "J1 Issue the birth-dose DVCs",
    "J2": "J2 Discover and refer the infant",
    "J3": "J3 Verify, import and schedule",
    "J4.0": "J4.0 Issue the family’s VHLs",
    "J4.1": "J4.1 Read records at the point of care",
}

JOURNEY_CAPABILITIES = {
    "J1": ["cap-access-consent-trust", "cap-health-record-mgmt"],
    "J2": ["cap-clinical-services"],
    "J3": ["cap-access-consent-trust", "cap-clinical-services", "cap-health-record-mgmt"],
    "J4.0": ["cap-access-consent-trust", "cap-health-record-mgmt"],
    "J4.1": ["cap-access-consent-trust", "cap-health-record-mgmt"],
}


def jkey(code):
    return "journey-" + code.lower().replace(".", "-")


def short(code):
    return JOURNEY_SHORT.get(code, JOURNEYS[code]["name"])


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

# Short box names; a system not listed uses its actor title.
SYSTEM_SHORT = {
    "chiang-rai-provincial-hospital": "Chiang Rai Provincial Hospital system",
    "chiang-rai-clinic-viewer": "Chiang Rai primary care clinic system",
    "chw-app": "CHW app (OHS)",
    "district-health-center-ehr": "Vientiane District Health Center EHR",
    "family-phone": "The family’s shared phone",
    "lao-national-portal": "Lao national health portal and gateway",
}


def skey(actor_id):
    return "sys-" + actor_id


# (key, name, RA block, hosting system actor, what it is in the IG)
COMPONENTS = [
    ("th-birth-ehr", "Birth hospital EHR", "ra-provider-systems", "chiang-rai-provincial-hospital", "StructureDefinition/TrustDemoThImmunization"),
    ("th-immunization-record", "Hospital immunization record service", "ra-lhr", "chiang-rai-provincial-hospital", "Immunization/TrustDemoJ1HepB"),
    ("th-product-codes", "Vaccine product code registry", "ra-product-registry", "chiang-rai-provincial-hospital", "CodeSystem/TrustDemoVaccineProduct"),
    ("th-dvc-signer", "DVC signer (HCERT)", "ra-trust-services", "chiang-rai-provincial-hospital", ""),
    ("th-vhl-viewer", "Clinic VHL viewer", "ra-provider-systems", "chiang-rai-clinic-viewer", "StructureDefinition/TrustDemoThVhlReceipt"),
    ("la-chw-app", "CHW app (OHS, SDC forms)", "ra-chw", "chw-app", "StructureDefinition/TrustDemoLaoRegistration"),
    ("la-dhc-ehr", "District health centre EHR", "ra-provider-systems", "district-health-center-ehr", "StructureDefinition/TrustDemoLaoImmunization"),
    ("la-conceptmap", "Terminology service (product to Lao EPI map)", "ra-terminology", "district-health-center-ehr", "ConceptMap/TrustDemoProductToLaoEpi"),
    ("la-schedule", "Schedule engine (infant PlanDefinition)", "ra-cdss", "district-health-center-ehr", "PlanDefinition/TrustDemoLaoInfantSchedule"),
    ("la-dvc-verifier", "DVC verifier", "ra-trust-services", "district-health-center-ehr", "StructureDefinition/TrustDemoLaoDvcVerification"),
    ("la-family-wallet", "Family wallet", "ra-citizen-apps", "family-phone", "Consent/TrustDemoJ4Consent"),
    ("la-national-fhir", "National FHIR server", "ra-lhr", "lao-national-portal", "Bundle/TrustDemoJ4Ips"),
    ("la-vhl-issuer", "VHL issuer", "ra-trust-services", "lao-national-portal", ""),
    ("la-info-gateway", "OHS Info Gateway and access log", "ra-mediator", "lao-national-portal", "StructureDefinition/TrustDemoLaoVhlAccess"),
    ("la-client-registry", "Client registry (children, households)", "ra-client-registry", "lao-national-portal", "StructureDefinition/TrustDemoLaoPatient"),
    ("la-facility-registry", "Facility registry (clinics, health centres)", "ra-facility-registry", "lao-national-portal", "Organization/TrustDemoVientianeDhc"),
    ("la-workforce-registry", "Health workforce registry (CHWs, nurses)", "ra-workforce-registry", "lao-national-portal", "Practitioner/TrustDemoVilay"),
    ("la-data-pipes", "OHS FHIR Data Pipes", "ra-hmis", "lao-national-portal", ""),
]
for _k, _n, _ra, _a, _ig in COMPONENTS:
    assert _a in ACTORS and ACTORS[_a]["kind"] == "system", f"component {_k}: {_a} is not a system actor in scenarios/actors/"
COUNTRY_OF = {"th": "Thailand", "la": "Lao PDR"}
PARTS = {a["id"]: [c for c in COMPONENTS if c[3] == a["id"]] for a in SYSTEMS}
SYSTEM_COUNTRY = {a: COUNTRY_OF[ps[0][0][:2]] for a, ps in PARTS.items() if ps}

# WHO GDHCN, the trust network beneath both countries (an external actor,
# with no lane of its own): it serves the trust components that publish a key
# to it or read its list, and so the journeys of the systems that host them.
GDHCN = ("gdhcn", "WHO GDHCN trust network (DEV)", "gdhcn-dev-trust-anchor")
GDHCN_SERVES = ["th-dvc-signer", "th-vhl-viewer", "la-dvc-verifier", "la-vhl-issuer"]
_HOST = {c[0]: c[3] for c in COMPONENTS}
GDHCN_JOURNEYS = [j for j in JOURNEYS if any(j in SYSTEM_JOURNEYS[_HOST[k]] for k in GDHCN_SERVES)]

# What both countries share, between them: GDHCN and the specifications it
# realizes. A Requirement, which an ApplicationComponent may realize.
TRUST_FRAMEWORK = ("trust-framework", "WHO SMART Trust specifications (HCERT, DVC, VHL)")

# --- Jurisdictions: each country's instance of the RA blocks it uses -------
# Thailand and Lao PDR are different jurisdictions: a Thai part is an
# instance of Thailand's provider systems, not of Lao PDR's. So each country
# has its own instance of every RA block its parts play, keyed <cc>-<RA key>
# (th-ra-provider-systems), which specializes the RA block; the country's
# parts specialize that instance.
CC = {v: k for k, v in COUNTRY_OF.items()}


def ikey(country, ra):
    return f"{CC[country]}-{ra}"


def instance_of(component):
    """The key of the per-country RA instance a COMPONENTS row specializes."""
    return ikey(SYSTEM_COUNTRY[component[3]], component[2])


INSTANCES = sorted({(SYSTEM_COUNTRY[c[3]], c[2]) for c in COMPONENTS}, key=lambda t: (t[0] != "Thailand", ORDER.index(t[1])))

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
    ("chiang-rai-provincial-hospital", "hcert-prefix-context"): "th-dvc-signer",
    ("district-health-center-ehr", "hcert-verify"): "la-dvc-verifier",
    ("lao-national-portal", "portal-serve-manifest"): "la-info-gateway",
}
INTERACTION_NAME = {
    ("J4.1", "Task_Open", "Task_Verify"): "VHL QR, shown",
    ("J4.1", "Task_Fetch", "Task_Release"): "ITI-YY5 manifest request, signed",
    ("J4.1", "Task_Release", "Task_Decrypt"): "manifest; access logged in Lao PDR",
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


# --- Elements --------------------------------------------------------------

ELEMENTS = {
    "country-th": ("Grouping", "Thailand (Country A, XXR)", "The jurisdiction where the newborn is born (J1) and later seen at the point of care (J4.1): its systems and its instances of the RA building blocks.", {}),
    "country-la": ("Grouping", "Lao PDR (Country B, home)", "The family’s home jurisdiction (J2, J3, J4.0), whose national portal serves their records abroad (J4.1): its systems and its instances of the RA building blocks.", {}),
    "intl": ("Grouping", "International: shared by both", "What the two jurisdictions share, and nothing else: WHO GDHCN and the WHO SMART Trust specifications. Neither country’s systems connect to the other’s except through what the family carries and the VHL fetch.", {}),
    "group-ra": ("Grouping", "Reference architecture (DPI-H RA)", "The DPI-H RA’s own building blocks, by the layers of its Integrated View (Fig. 3.2): generic, no country’s. Each country’s instance of a block specializes it.", {}),
    "group-journeys": ("Grouping", "Journeys (use cases)", "The demonstrator's user journeys, one BPMN process each, in processes/content/.", {}),
    "group-people": ("Grouping", "People", "The roles people play in the journeys (scenarios/roles.json); every persona is fictional.", {}),
    "group-capabilities": ("Grouping", "DPI-H RA capabilities exercised", "The capabilities of the RA's Integrated View that the journeys realize.", {}),
}

for code, p in JOURNEYS.items():
    ELEMENTS[jkey(code)] = ("BusinessProcess", short(code),
                            f"{p['name']}: journey {code} of the SMART Trust demonstrator. Its steps, lanes and the requirements they trace to are in the BPMN process.",
                            {"journey": code, "bpmn": f"processes/content/{p['stem']}.bpmn", "bpmnProcess": p["id"],
                             "ig": f"{IG_BASE}business-processes.html"})

for r in ROLES:
    ELEMENTS["role-" + r["id"]] = ("BusinessRole", r["title"], r["description"],
                                   {"role": r["id"], **({"otherNames": "; ".join(r["otherNames"])} if r.get("otherNames") else {})})

for a in SYSTEMS:
    js = SYSTEM_JOURNEYS[a["id"]]
    ELEMENTS[skey(a["id"])] = ("ApplicationComponent", SYSTEM_SHORT.get(a["id"], a["title"]),
                               f"{a['title']}: {a.get('description', '')}".strip(),
                               {"scenarioActor": f"scenarios/actors/{a['id']}.json", "roles": ", ".join(a["roles"]),
                                "journeys": ", ".join(js) if js else "none (no lane)",
                                **({"country": SYSTEM_COUNTRY[a["id"]]} if a["id"] in SYSTEM_COUNTRY else {})})

for key, name, _ra, actor, ig in COMPONENTS:
    ELEMENTS[key] = ("ApplicationComponent", name,
                     f"{SYSTEM_COUNTRY[actor]}: {name}, part of {SYSTEM_SHORT.get(actor, ACTORS[actor]['title'])}.",
                     {"country": SYSTEM_COUNTRY[actor], "partOf": f"scenarios/actors/{actor}.json", **_ig(ig)})

ELEMENTS[GDHCN[0]] = ("ApplicationComponent", GDHCN[1],
                      "WHO’s Global Digital Health Certification Network: the trust list of participants’ public keys that lets a Lao clinic believe a Thai certificate, and a Thai clinic a Lao link, with no connection between the two countries' systems. Not a building block of the RA's Integrated View: it sits beneath both countries.",
                      {"scenarioActor": f"scenarios/actors/{GDHCN[2]}.json", "spec": "https://smart.who.int/trust/"})

ELEMENTS[TRUST_FRAMEWORK[0]] = ("Requirement", TRUST_FRAMEWORK[1],
                                "The specifications both countries’ systems conform to, so that a certificate signed in one is read in the other: HCERT and the DVC payload (WHO SMART Trust), and the Verifiable Health Link (WHO SMART Trust and IHE ITI VHL). GDHCN realizes the trust network they assume.",
                                {"spec": "https://smart.who.int/trust/", "phw": "https://smart.who.int/trust-phw/"})

for country, ra in INSTANCES:
    ELEMENTS[ikey(country, ra)] = ("ApplicationComponent", f"{RA_NAME[ra]} ({country})",
                                   f"{country}’s instance of the DPI-H RA building block {RA_NAME[ra]}: what {country}’s parts in the demonstrator that play this block are, and a specialization of the RA’s block. One per jurisdiction, since neither country’s systems are the other’s.",
                                   {"country": country, "raBlock": EXISTING[ra]})

# --- Relationships ---------------------------------------------------------

RELATIONS = []
for a in SYSTEMS:
    for j in SYSTEM_JOURNEYS[a["id"]]:
        RELATIONS.append(("Serving", skey(a["id"]), jkey(j)))
    for c in PARTS[a["id"]]:
        RELATIONS.append(("Composition", skey(a["id"]), c[0]))
for c in COMPONENTS:
    RELATIONS.append(("Specialization", c[0], instance_of(c)))
for country, ra in INSTANCES:
    RELATIONS.append(("Specialization", ikey(country, ra), ra))
for t, a, b, name, _js in INTERACTIONS:
    RELATIONS.append((t, a, b, {"name": name}))
RELATIONS.append(("Realization", "gdhcn", TRUST_FRAMEWORK[0]))
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
    "country-th": [skey(a) for a, c in SYSTEM_COUNTRY.items() if c == "Thailand"] + [ikey(c, ra) for c, ra in INSTANCES if c == "Thailand"],
    "country-la": [skey(a) for a, c in SYSTEM_COUNTRY.items() if c == "Lao PDR"] + [ikey(c, ra) for c, ra in INSTANCES if c == "Lao PDR"],
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
    return [("Specialization", c[0], instance_of(c)) for c in parts] + [("Specialization", i, by_key[i]) for i in insts]


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
    for country, gkey in (("Thailand", "country-th"), ("Lao PDR", "country-la")):
        sys_ = country_systems(country, actors)
        if not sys_:
            continue
        ps = [c for a in sys_ for c in _parts_by_layer(a, shown)]
        parts += ps
        bands.append(("group", gkey, 1, [("row", [system_box(a, across=True, among=shown) for a in sys_]),
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
        rows.append(("group", "group-ra", 1, [("row", [("group", l, len(bs), [box(b) for b in bs]) for l, bs in layers if bs])]))
    _align(journey_view_name(code), parts)
    keys = {c[0] for c in parts}
    conns = [("Realization", jkey(code), c) for c in caps(code)]
    conns += [("Assignment", "role-" + r["id"], jkey(code)) for r in people]
    conns += [("Serving", skey(a), jkey(code)) for a in serving]
    conns += specializations(parts)
    conns += interactions(keys, code)
    if code in GDHCN_JOURNEYS:
        conns += [("Serving", "gdhcn", jkey(code))]
        conns += [("Serving", "gdhcn", k) for k in GDHCN_SERVES if k in keys]
    doc = (f"Journey {code} ({JOURNEYS[code]['name']}): the people assigned to it (its BPMN lanes), the systems that serve it "
           f"(the system actors that play its lanes, each holding its parts) and the other country’s parts it hands over to, "
           f"each country’s instances of the DPI-H RA building blocks those parts specialize, and the RA capabilities it realizes.")
    return (journey_view_name(code), doc, ("col", rows)), conns


# The Integrated View is drawn in two columns, Thailand left and Lao PDR
# right, with what they share between them; LAYOUT_TREES gives build.py that
# layout, and add_views.py draws the same boxes from lowered(), which has only
# the node kinds it knows. In a column the country's systems stack top to
# bottom in the order of the first journey each serves; a system's parts are a
# grid of at most COLUMN_SLOTS[country] boxes across, the parts that meet the
# other country or GDHCN on the side that faces the middle. Under the systems,
# each RA instance stands in the slot (grid column) of the first part drawn
# that specializes it, so that line runs straight down: under the system
# whose part is the first to specialize it (so each system's instances stand
# right under it, and the lines are short), not all under the last system,
# which sent most lines down past the systems between (36 crossings, not 5).
# The RA's own blocks are left out of this view: with them below both
# columns, 16 more lines ran the height of the view.
COLUMN_SLOTS = {"Thailand": 2, "Lao PDR": 3}
FACING = {"Thailand": "right", "Lao PDR": "left"}
MEETS = {k for _t, a, b, _n, _j in INTERACTIONS for k in (a, b)} | set(GDHCN_SERVES)


def _first_journey(actor_id):
    return min([list(JOURNEYS).index(j) for j in SYSTEM_JOURNEYS[actor_id]] or [len(JOURNEYS)])


def space(slots):
    """Room for slots grid cells and the gaps after them, in a row."""
    return ("space", slots * (_LEAF_W + LAYOUT["gap"]) - LAYOUT["gap"], 0)


def _instance_grid(parts, slot_of, n_slots, drawn):
    """The RA instances of parts not drawn yet, each in its first part's slot, as a grid (or nothing)."""
    columns = [[] for _ in range(n_slots)]
    for i in country_instances(parts):
        if i in drawn:
            continue
        drawn.add(i)
        first = next(c for c in parts if instance_of(c) == i)
        columns[slot_of[first[0]]].append(i)
    # Under each slot, the instance of the part drawn last stands first: its
    # line is the shortest, and the others pass beside it rather than across.
    columns = [c[::-1] for c in columns]
    depth = max(len(c) for c in columns)
    if not depth:
        return []
    return [("grid", n_slots, [box(columns[s][r]) if r < len(columns[s]) else None for r in range(depth) for s in range(n_slots)], LAYOUT["pad"])]


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


def country_column(country, gkey, actors=None, shown=None, level=None):
    """(the country's band as a column, its parts in drawing order, the y of each system in it).

    Systems stacked, each with the RA instances its parts are the first to
    specialize under it. level = {system: y}: that system is pushed down to
    stand at y (relative to the column's first box), if it would stand higher.
    """
    n_slots, right = COLUMN_SLOTS[country], FACING[country] == "right"
    kids, parts, slot_of, drawn, at = [], [], {}, set(), {}
    gap = LAYOUT["gap"]
    y = lambda: sum(_height(k) + gap for k in kids)
    systems = country_systems(country, actors)
    for a in sorted(systems, key=lambda a: (_first_journey(a), systems.index(a))):
        ps = sorted(_parts_by_layer(a, shown), key=lambda c: c[0] not in MEETS)
        n = min(n_slots, len(ps))
        cells = []
        for i in range(0, len(ps), n):
            row = ps[i:i + n]
            row = ([None] * (n - len(row)) + row[::-1]) if right else row + [None] * (n - len(row))
            cells += row
        off = n_slots - n if right else 0
        for i, c in enumerate(cells):
            if c is not None:
                slot_of[c[0]] = off + i % n
                parts.append(c)
        sysbox = ("group", skey(a), 1, [("grid", n, [box(c[0]) if c else None for c in cells], 0)])
        want = (level or {}).get(a)
        if want is not None and want - y() - gap >= 0:
            kids.append(("space", 0, want - y() - gap))
        at[a] = y()
        kids.append(("row", [space(off), sysbox]) if off else sysbox)
        kids += _instance_grid(parts, slot_of, n_slots, drawn)
    return ("group", gkey, 1, kids), parts, at


def lowered(node):
    """node with only add_views.py's kinds (box, group, row, col): a grid becomes a column of rows; a space goes."""
    if node[0] == "box":
        return node
    if node[0] == "grid":
        rows = [[k for k in node[2][i:i + node[1]] if k is not None] for i in range(0, len(node[2]), node[1])]
        return ("col", [("row", [lowered(k) for k in r]) for r in rows if r])
    if node[0] == "group":
        return ("group", node[1], node[2], [lowered(k) for k in node[3] if k[0] != "space"])
    return (node[0], [lowered(k) for k in node[1] if k[0] != "space"])


LAYOUT_TREES = {}


def _intl_level(la_at):
    """How far down the shared band stands: midway between the first and last Lao systems GDHCN serves, so its lines to both are short."""
    ys = [la_at[_HOST[k]] for k in GDHCN_SERVES if _HOST[k] in la_at]
    return (min(ys) + max(ys)) // 4 * 2 if ys else 0


def country_bands(actors=None, shown=None, code=None, shared=("gdhcn", TRUST_FRAMEWORK[0])):
    """(Thailand's column, the shared band, Lao PDR's column, as a row; the parts drawn).

    Lao PDR is laid out first: each Thai system stands level with the first
    Lao system it meets (in journey code's interactions, or all), so the lines
    where they meet run across; the shared band stands midway between the Lao
    systems GDHCN serves. A country with no system drawn, or no shared box, is
    left out.
    """
    la, la_parts, la_at = country_column("Lao PDR", "country-la", actors, shown) if country_systems("Lao PDR", actors) else (None, [], {})
    level = {}
    for _t, a, b, _n, js in INTERACTIONS:
        if code is not None and code not in js:
            continue
        th_end, la_end = (a, b) if SYSTEM_COUNTRY[_HOST[a]] == "Thailand" else (b, a)
        if _HOST[la_end] in la_at:
            level[_HOST[th_end]] = min(level.get(_HOST[th_end], 1e9), la_at[_HOST[la_end]])
    th, th_parts, _ = country_column("Thailand", "country-th", actors, shown, level) if country_systems("Thailand", actors) else (None, [], {})
    bands = [th]
    if shared:
        intl = ("group", "intl", 1, [box(k) for k in shared])
        lift = _intl_level(la_at)
        bands.append(("col", [("space", 0, lift - LAYOUT["gap"]), intl]) if lift >= LAYOUT["gap"] else intl)
    bands.append(la)
    return ("row", [b for b in bands if b]), th_parts + la_parts


def _systems_view():
    """Thailand (left) and Lao PDR (right) as columns, what they share between them."""
    layout, parts = country_bands()
    LAYOUT_TREES[SYSTEMS_VIEW] = layout
    _align(SYSTEMS_VIEW, parts)
    keys = {c[0] for c in COMPONENTS}
    conns = [("Specialization", c[0], instance_of(c)) for c in parts] + interactions(keys)
    conns += [("Serving", "gdhcn", k) for k in GDHCN_SERVES] + [("Realization", "gdhcn", TRUST_FRAMEWORK[0])]
    doc = ("The two jurisdictions the demonstrator spans, Thailand (left) and Lao PDR (right), with what they share between them: "
           "WHO GDHCN and the WHO SMART Trust specifications. In each country its systems, each holding its parts, stand above its "
           "instances of the DPI-H RA building blocks; each part specializes its own country’s instance, which stands under it. "
           "The RA’s own blocks, which each instance specializes, are drawn in the journeys’ views. The lines that run from one "
           "country to the other are where they meet: the paper DVC the family carries from J1 to J2 and J3, and the VHL QR and "
           "ITI-YY5 manifest fetch of J4.1, logged in Lao PDR.")
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
    JOURNEYS_VIEW: [r[:3] for r in RELATIONS if r[0] in ("Assignment", "Realization", "Association") and r[1] != "gdhcn"],
}
for _code in JOURNEYS:
    _v, _c = journey_view(_code)
    VIEWS.append(_v)
    VIEW_CONNECTIONS[_v[0]] = _c
