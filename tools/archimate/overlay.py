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
  it is an instance of;
- each journey's Realization of the RA capabilities it exercises.

The BPMN, the roles and the actors are read by tools/journeys/graph.py, the
same reader repo_checks.py and ig_gen.py use; a lane's role is its
partitionElementRef.

The relationship types are ones ArchiMate 3.2 allows between those element
types (Appendix B): Assignment (BusinessRole to BusinessProcess), Serving
(ApplicationComponent to BusinessProcess or ApplicationComponent),
Composition and Specialization (between two ApplicationComponents),
Realization (BusinessProcess to Capability), Association (BusinessRole to
Stakeholder) and Aggregation (from a Grouping).
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
    ("th-immunization-record", "Hospital immunization record", "ra-lhr", "chiang-rai-provincial-hospital", "Immunization/TrustDemoJ1HepB"),
    ("th-product-codes", "Vaccine product codes", "ra-product-registry", "chiang-rai-provincial-hospital", "CodeSystem/TrustDemoVaccineProduct"),
    ("th-dvc-signer", "DVC signer (HCERT)", "ra-trust-services", "chiang-rai-provincial-hospital", ""),
    ("th-vhl-viewer", "Clinic VHL viewer", "ra-provider-systems", "chiang-rai-clinic-viewer", "StructureDefinition/TrustDemoThVhlReceipt"),
    ("la-chw-app", "CHW app (OHS, SDC forms)", "ra-chw", "chw-app", "StructureDefinition/TrustDemoLaoRegistration"),
    ("la-dhc-ehr", "District health centre EHR", "ra-provider-systems", "district-health-center-ehr", "StructureDefinition/TrustDemoLaoImmunization"),
    ("la-conceptmap", "ConceptMap: product to Lao EPI", "ra-terminology", "district-health-center-ehr", "ConceptMap/TrustDemoProductToLaoEpi"),
    ("la-schedule", "Infant schedule (PlanDefinition)", "ra-cdss", "district-health-center-ehr", "PlanDefinition/TrustDemoLaoInfantSchedule"),
    ("la-dvc-verifier", "DVC verifier", "ra-trust-services", "district-health-center-ehr", "StructureDefinition/TrustDemoLaoDvcVerification"),
    ("la-family-wallet", "Family wallet", "ra-citizen-apps", "family-phone", "Consent/TrustDemoJ4Consent"),
    ("la-national-fhir", "National FHIR server", "ra-lhr", "lao-national-portal", "Bundle/TrustDemoJ4Ips"),
    ("la-vhl-issuer", "VHL issuer", "ra-trust-services", "lao-national-portal", ""),
    ("la-info-gateway", "OHS Info Gateway and access log", "ra-mediator", "lao-national-portal", "StructureDefinition/TrustDemoLaoVhlAccess"),
    ("la-client-registry", "Child and household", "ra-client-registry", "lao-national-portal", "StructureDefinition/TrustDemoLaoPatient"),
    ("la-facility-registry", "Clinics and health centres", "ra-facility-registry", "lao-national-portal", "Organization/TrustDemoVientianeDhc"),
    ("la-workforce-registry", "CHWs and nurses", "ra-workforce-registry", "lao-national-portal", "Practitioner/TrustDemoVilay"),
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

IG_BASE = "https://litlfred.github.io/smart-trust-demo/"


def _ig(ref):
    if not ref:
        return {}
    kind, rid = ref.split("/")
    return {"ig": f"{IG_BASE}artifact/{kind}-{rid}.html"}


# --- Elements --------------------------------------------------------------

ELEMENTS = {
    "country-th": ("Grouping", "Thailand (Country A, XXR)", "The systems of the country where the newborn is born (J1) and later seen at the point of care (J4.1).", {}),
    "country-la": ("Grouping", "Lao PDR (Country B, home)", "The systems of the family’s home country (J2, J3, J4.0) and its national portal (J4.1).", {}),
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

# --- Relationships ---------------------------------------------------------

RELATIONS = []
for a in SYSTEMS:
    for j in SYSTEM_JOURNEYS[a["id"]]:
        RELATIONS.append(("Serving", skey(a["id"]), jkey(j)))
    for c in PARTS[a["id"]]:
        RELATIONS.append(("Composition", skey(a["id"]), c[0]))
for key, _n, ra, *_ in COMPONENTS:
    RELATIONS.append(("Specialization", key, ra))
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
    "country-th": [skey(a) for a, c in SYSTEM_COUNTRY.items() if c == "Thailand"],
    "country-la": [skey(a) for a, c in SYSTEM_COUNTRY.items() if c == "Lao PDR"],
    "group-journeys": [jkey(c) for c in JOURNEYS],
    "group-people": ["role-" + r["id"] for r in ROLES],
    "group-capabilities": sorted({c for code in JOURNEYS for c in caps(code)}),
}
for g, ms in GROUP_MEMBERS.items():
    for m in ms:
        RELATIONS.append(("Aggregation", g, m))

# --- Views -----------------------------------------------------------------
# One element appears at most once in a view (add_views keys a view's boxes by
# element). Lines are drawn centre to centre, so the layouts put each line's
# ends near each other: the RA layers in the middle, a country either side.
# A system is drawn as a box holding its parts (the composition).

ORDER = [b for _l, bs in RA_LAYERS for b in bs]


def _parts_by_layer(actor_id):
    return sorted(PARTS[actor_id], key=lambda c: ORDER.index(c[2]))


def _systems_by_layer(actor_ids):
    return sorted(actor_ids, key=lambda a: ORDER.index(_parts_by_layer(a)[0][2]))


def box(k):
    return ("box", k)


def system_box(actor_id, across=False):
    """A system holding its parts: stacked (the systems view) or side by side (a journey view, so each part's line runs down to its RA block)."""
    parts = _parts_by_layer(actor_id)
    return ("group", skey(actor_id), len(parts) if across else 1, [box(c[0]) for c in parts])


def country_systems(country, among=None):
    ids = [a for a, c in SYSTEM_COUNTRY.items() if c == country and (among is None or a in among)]
    return _systems_by_layer(ids)


SYSTEMS_VIEW = "SMART Trust demo on the DPI-H Integrated View"
JOURNEYS_VIEW = "SMART Trust demo journeys (use cases)"

# The journeys view, laid out so its lines cross as little as they can: each
# person who takes part in one journey stands under it (their assignment is a
# vertical line), and the caregiver, who takes part in all five, stands at
# the end. add_views.py places boxes left to right only, so VIEW_BOUNDS
# (applied by build.py after it) moves a few boxes to exact positions: the
# capabilities spread over the journeys, Health Workers centred under the
# four health workers, Citizens / Care recipients under the caregiver. A
# person role not in PEOPLE_ORDER is drawn after these.
PEOPLE_ORDER = ["birth-clinic-vaccinator", "community-health-worker", "home-clinic-provider", "poc-provider", "caregiver"]
PEOPLE = [r for r in PEOPLE_ORDER if r in {x["id"] for x in ROLES}] + [r["id"] for r in ROLES if r["id"] not in PEOPLE_ORDER]
_LEAF_W, _PAD = 170, 12  # add_views.py's box width and padding


def _col(i):
    """x of the i-th box (fractional i allowed) inside a group, relative to the group."""
    return round(_PAD + i * (_LEAF_W + _PAD))


_GROUP_W = 2 * _PAD + 5 * _LEAF_W + 4 * _PAD  # a five-box group, as wide as the journeys
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
    """One journey: its capabilities, its people, the systems that serve it (with their parts) and the RA blocks those parts specialize."""
    serving = [a["id"] for a in SYSTEMS if code in SYSTEM_JOURNEYS[a["id"]]]
    th, la = country_systems("Thailand", serving), country_systems("Lao PDR", serving)
    parts = [c for a in serving for c in PARTS[a]]
    blocks = {c[2] for c in parts}
    layers = [(l, [b for b in bs if b in blocks]) for l, bs in RA_LAYERS]
    countries = ([("group", "country-th", len(th), [system_box(a, across=True) for a in th])] if th else []) + \
                ([("group", "country-la", len(la), [system_box(a, across=True) for a in la])] if la else [])
    if code in GDHCN_JOURNEYS:
        countries.append(box("gdhcn"))
    rows = []
    if caps(code):
        rows.append(("row", [box(c) for c in caps(code)]))
    people = roles_of(code)
    rows.append(("row", ([("group", "group-people", 1, [box("role-" + r["id"]) for r in people])] if people else []) + [box(jkey(code))]))
    if countries:
        rows.append(("row", countries))
    if any(bs for _l, bs in layers):
        rows.append(("row", [("group", l, len(bs), [box(b) for b in bs]) for l, bs in layers if bs]))
    keys = {c[0] for c in parts}
    conns = [("Realization", jkey(code), c) for c in caps(code)]
    conns += [("Assignment", "role-" + r["id"], jkey(code)) for r in people]
    conns += [("Serving", skey(a), jkey(code)) for a in serving]
    conns += [("Specialization", c[0], c[2]) for c in parts]
    if code in GDHCN_JOURNEYS:
        conns += [("Serving", "gdhcn", jkey(code))]
        conns += [("Serving", "gdhcn", k) for k in GDHCN_SERVES if k in keys]
    doc = (f"Journey {code} ({JOURNEYS[code]['name']}): the people assigned to it (its BPMN lanes), the systems that serve it "
           f"(the system actors that play its lanes, each holding its parts), the DPI-H RA building blocks those parts specialize, "
           f"and the RA capabilities it realizes.")
    return (journey_view_name(code), doc, ("col", rows)), conns


VIEWS = [
    (SYSTEMS_VIEW,
     "The demonstrator’s Thai (left) and Lao (right) systems, each holding its parts, and each part a specialization of the DPI-H RA building block it instantiates (centre: the layers of the RA’s Integrated View, Fig. 3.2), with WHO GDHCN beneath both countries (the lines from it are in each journey’s view).",
     ("row", [
         ("group", "country-th", 1, [system_box(a) for a in country_systems("Thailand")]),
         ("col", [("group", layer, 1, [box(b) for b in bs]) for layer, bs in RA_LAYERS] + [box("gdhcn")]),
         ("group", "country-la", 1, [system_box(a) for a in country_systems("Lao PDR")]),
     ])),
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
    SYSTEMS_VIEW: [("Specialization", k, ra) for k, _n, ra, *_ in COMPONENTS],
    JOURNEYS_VIEW: [r for r in RELATIONS if r[0] in ("Assignment", "Realization", "Association")],
}
for _code in JOURNEYS:
    _v, _c = journey_view(_code)
    VIEWS.append(_v)
    VIEW_CONNECTIONS[_v[0]] = _c
