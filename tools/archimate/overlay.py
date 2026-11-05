"""The SMART Trust demonstrator as an overlay on the DPI-H RA ArchiMate model.

A spec for smart-ra's tools/archimate-dth/add_views.py (pinned in
smart-ra.lock.json), applied by build.py to smart-ra's model 0.3.0-draft.1.
Nothing in the RA model is changed: the overlay only adds elements,
relationships and views, and every RA element keeps its Archi id.

What it adds, and where each part comes from:

- the journeys J1 to J4.1, the use cases, as BusinessProcess elements:
  one per BPMN process in processes/content/, named as the process is;
- the people who take part, as BusinessRole elements: the roles in
  scenarios/roles.json whose actorKinds is "person", each assigned to the
  journeys whose BPMN has a lane of that title;
- the systems, as ApplicationComponent elements, grouped by country: the
  components of VaxLink's architecture view (litlfred/vaxlink,
  ArchitectureDiagram.tsx), each a Specialization of the RA building block
  it is an instance of, and Serving the journeys it takes part in;
- each journey's Realization of the RA capabilities it exercises.

The relationship types are ones ArchiMate 3.2 allows between those element
types (Appendix B): Assignment (BusinessRole to BusinessProcess), Serving
(ApplicationComponent to BusinessProcess or ApplicationComponent),
Specialization (between two ApplicationComponents), Realization
(BusinessProcess to Capability) and Aggregation (from a Grouping).
"""

import html
import json
import re
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

# --- Journeys: one per BPMN process, read from processes/content/ -----------

JOURNEY_FILES = [
    # (code, BPMN file stem, short name for the box; the BPMN's own name is the documentation)
    ("J1", "j1-birth-dose-dvc", "J1 Issue the birth-dose DVCs"),
    ("J2", "j2-chw-discovery-referral", "J2 Discover and refer the infant"),
    ("J3", "j3-clinic-verification-schedule", "J3 Verify, import and schedule"),
    ("J4.0", "j4-0-family-vhl-issuance", "J4.0 Issue the family\u2019s VHLs"),
    ("J4.1", "j4-1-vhl-point-of-care", "J4.1 Read records at the point of care"),
]

# The RA capabilities each journey exercises.
JOURNEY_CAPABILITIES = {
    "J1": ["cap-access-consent-trust", "cap-health-record-mgmt"],
    "J2": ["cap-clinical-services"],
    "J3": ["cap-access-consent-trust", "cap-clinical-services", "cap-health-record-mgmt"],
    "J4.0": ["cap-access-consent-trust", "cap-health-record-mgmt"],
    "J4.1": ["cap-access-consent-trust", "cap-health-record-mgmt"],
}


def _bpmn(stem):
    text = (ROOT / "processes" / "content" / f"{stem}.bpmn").read_text(encoding="utf-8")
    proc = re.search(r'<bpmn:process id="([^"]+)" name="([^"]+)"', text)
    lanes = [html.unescape(n) for n in re.findall(r'<bpmn:lane [^>]*name="([^"]+)"', text)]
    return proc.group(1), html.unescape(proc.group(2)), lanes


def jkey(code):
    return "journey-" + code.lower().replace(".", "-")


JOURNEYS = {code: _bpmn(stem) + (stem, short) for code, stem, short in JOURNEY_FILES}

# --- People: the person roles of scenarios/roles.json ----------------------

ROLES = [r for r in json.loads((ROOT / "scenarios" / "roles.json").read_text(encoding="utf-8"))["roles"]
         if "person" in r.get("actorKinds", [])]

# --- Systems: VaxLink's architecture view, by country ----------------------
# (key, name, RA block, journeys, scenario actor or "", what it is in the IG)

TH = [
    ("th-birth-ehr", "Birth hospital EHR", "ra-provider-systems", ["J1"], "chiang-rai-provincial-hospital", "StructureDefinition/TrustDemoThImmunization"),
    ("th-immunization-record", "Hospital immunization record", "ra-lhr", ["J1"], "chiang-rai-provincial-hospital", "Immunization/TrustDemoJ1HepB"),
    ("th-product-codes", "Vaccine product codes", "ra-product-registry", ["J1"], "", "CodeSystem/TrustDemoVaccineProduct"),
    ("th-dvc-signer", "DVC signer (HCERT)", "ra-trust-services", ["J1"], "chiang-rai-provincial-hospital", ""),
    ("th-vhl-viewer", "Clinic VHL viewer", "ra-provider-systems", ["J4.1"], "chiang-rai-clinic-viewer", "StructureDefinition/TrustDemoThVhlReceipt"),
]
LA = [
    ("la-chw-app", "CHW app (OHS, SDC forms)", "ra-chw", ["J2"], "chw-app", "StructureDefinition/TrustDemoLaoRegistration"),
    ("la-dhc-ehr", "District health centre EHR", "ra-provider-systems", ["J3"], "district-health-center-ehr", "StructureDefinition/TrustDemoLaoImmunization"),
    ("la-family-wallet", "Family wallet", "ra-citizen-apps", ["J4.0", "J4.1"], "family-phone", "Consent/TrustDemoJ4Consent"),
    ("la-conceptmap", "ConceptMap: product to Lao EPI", "ra-terminology", ["J3"], "", "ConceptMap/TrustDemoProductToLaoEpi"),
    ("la-schedule", "Infant schedule (PlanDefinition)", "ra-cdss", ["J3"], "", "PlanDefinition/TrustDemoLaoInfantSchedule"),
    ("la-data-pipes", "OHS FHIR Data Pipes", "ra-hmis", ["J3"], "", ""),
    ("la-client-registry", "Child and household", "ra-client-registry", ["J2"], "", "StructureDefinition/TrustDemoLaoPatient"),
    ("la-facility-registry", "Clinics and health centres", "ra-facility-registry", ["J2", "J3"], "", "Organization/TrustDemoVientianeDhc"),
    ("la-workforce-registry", "CHWs and nurses", "ra-workforce-registry", ["J2", "J3"], "", "Practitioner/TrustDemoVilay"),
    ("la-national-fhir", "National FHIR server", "ra-lhr", ["J3", "J4.0", "J4.1"], "lao-national-portal", "Bundle/TrustDemoJ4Ips"),
    ("la-dvc-verifier", "DVC verifier, VHL issuer", "ra-trust-services", ["J3", "J4.0"], "district-health-center-ehr", "StructureDefinition/TrustDemoLaoDvcVerification"),
    ("la-info-gateway", "OHS Info Gateway and access log", "ra-mediator", ["J4.1"], "lao-national-portal", "StructureDefinition/TrustDemoLaoVhlAccess"),
]
GDHCN = ("gdhcn", "WHO GDHCN trust network (DEV)", "", ["J1", "J3", "J4.0", "J4.1"], "gdhcn-dev-trust-anchor", "")

# The trust components the GDHCN trust list serves: the signer publishes its
# key there; the verifiers and the viewer read the list.
GDHCN_SERVES = ["th-dvc-signer", "th-vhl-viewer", "la-dvc-verifier"]

IG_BASE = "https://litlfred.github.io/smart-trust-demo/"


def _ig(ref):
    if not ref:
        return {}
    kind, rid = ref.split("/")
    return {"ig": f"{IG_BASE}artifact/{kind}-{rid}.html"}


# --- Elements --------------------------------------------------------------

ELEMENTS = {
    "country-th": ("Grouping", "Thailand (Country A, XXR)", "The systems of the country where the newborn is born (J1) and later seen at the point of care (J4.1).", {}),
    "country-la": ("Grouping", "Lao PDR (Country B, home)", "The systems of the family\u2019s home country (J2, J3, J4.0) and its national portal (J4.1).", {}),
    "group-journeys": ("Grouping", "Journeys (use cases)", "The demonstrator's user journeys, one BPMN process each, in processes/content/.", {}),
    "group-people": ("Grouping", "People", "The roles people play in the journeys (scenarios/roles.json); every persona is fictional.", {}),
    "group-capabilities": ("Grouping", "DPI-H RA capabilities exercised", "The capabilities of the RA's Integrated View that the journeys realize.", {}),
}

for code, (pid, name, lanes, stem, short) in JOURNEYS.items():
    ELEMENTS[jkey(code)] = ("BusinessProcess", short,
                            f"{name}: journey {code} of the SMART Trust demonstrator. Its steps, lanes and the requirements they trace to are in the BPMN process.",
                            {"journey": code, "bpmn": f"processes/content/{stem}.bpmn", "bpmnProcess": pid,
                             "ig": f"{IG_BASE}business-processes.html"})

for r in ROLES:
    ELEMENTS["role-" + r["id"]] = ("BusinessRole", r["title"], r["description"],
                                   {"role": r["id"], **({"otherNames": "; ".join(r["otherNames"])} if r.get("otherNames") else {})})

for country, comps in (("Thailand", TH), ("Lao PDR", LA)):
    for key, name, _ra, js, actor, ig in comps:
        ELEMENTS[key] = ("ApplicationComponent", name,
                         f"{country}: {name}, in journeys {', '.join(js)}.",
                         {"country": country, "journeys": ", ".join(js),
                          **({"scenarioActor": f"scenarios/actors/{actor}.json"} if actor else {}), **_ig(ig)})

ELEMENTS[GDHCN[0]] = ("ApplicationComponent", GDHCN[1],
                      "WHO\u2019s Global Digital Health Certification Network: the trust list of participants\u2019 public keys that lets a Lao clinic believe a Thai certificate, and a Thai clinic a Lao link, with no connection between the two countries' systems. Not a building block of the RA's Integrated View: it sits beneath both countries.",
                      {"scenarioActor": f"scenarios/actors/{GDHCN[4]}.json", "spec": "https://smart.who.int/trust/"})

# --- Relationships ---------------------------------------------------------

RELATIONS = []
SYSTEMS = TH + LA
for key, _n, ra, js, *_ in SYSTEMS:
    RELATIONS.append(("Specialization", key, ra))
    for j in js:
        RELATIONS.append(("Serving", key, jkey(j)))
for j in GDHCN[3]:
    RELATIONS.append(("Serving", "gdhcn", jkey(j)))
for k in GDHCN_SERVES:
    RELATIONS.append(("Serving", "gdhcn", k))
for r in ROLES:
    for code, (_pid, _name, lanes, _stem, _short) in JOURNEYS.items():
        if r["title"] in lanes:
            RELATIONS.append(("Assignment", "role-" + r["id"], jkey(code)))
for code, caps in JOURNEY_CAPABILITIES.items():
    for c in caps:
        RELATIONS.append(("Realization", jkey(code), c))
for r in ROLES:
    RELATIONS.append(("Association", "role-" + r["id"], ROLE_STAKEHOLDER[r["id"]]))
GROUP_MEMBERS = {
    "country-th": [c[0] for c in TH],
    "country-la": [c[0] for c in LA],
    "group-journeys": [jkey(c) for c in JOURNEYS],
    "group-people": ["role-" + r["id"] for r in ROLES],
    "group-capabilities": sorted({c for cs in JOURNEY_CAPABILITIES.values() for c in cs}),
}
for g, ms in GROUP_MEMBERS.items():
    for m in ms:
        RELATIONS.append(("Aggregation", g, m))

# --- Views -----------------------------------------------------------------
# One element appears at most once in a view (add_views keys a view's boxes by
# element). Lines are drawn centre to centre, so the layouts put each line's
# ends near each other: the RA layers in the middle, a country either side.

ORDER = [b for _l, bs in RA_LAYERS for b in bs]
JOURNEY_SYSTEMS = {j: [c for c in SYSTEMS if j in c[3]] for j in JOURNEYS}


def _by_layer(comps):
    return sorted(comps, key=lambda c: ORDER.index(c[2]))


def box(k):
    return ("box", k)


def roles_of(code):
    return [r for r in ROLES if r["title"] in JOURNEYS[code][2]]


SYSTEMS_VIEW = "SMART Trust demo on the DPI-H Integrated View"
JOURNEYS_VIEW = "SMART Trust demo journeys (use cases)"

# The journeys view, laid out so its lines cross as little as they can: each
# person who takes part in one journey stands under it (their assignment is a
# vertical line), and the caregiver, who takes part in all five, stands at
# the end. add_views.py places boxes left to right only, so VIEW_BOUNDS
# (applied by build.py after it) moves a few boxes to exact positions: the
# capabilities spread over the journeys, Health Workers centred under the
# four health workers, Citizens / Care recipients under the caregiver.
PEOPLE_ORDER = ["birth-clinic-vaccinator", "community-health-worker", "home-clinic-provider", "poc-provider", "caregiver"]
assert sorted(PEOPLE_ORDER) == sorted(r["id"] for r in ROLES), "PEOPLE_ORDER must name every person role"
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
    """One journey: its capabilities, its people, the systems that serve it and the RA blocks they specialize."""
    sys_ = JOURNEY_SYSTEMS[code]
    th = [c for c in _by_layer(sys_) if c in TH]
    la = [c for c in _by_layer(sys_) if c in LA]
    blocks = {c[2] for c in sys_}
    layers = [(l, [b for b in bs if b in blocks]) for l, bs in RA_LAYERS]
    countries = ([("group", "country-th", len(th), [box(c[0]) for c in th])] if th else []) + \
                ([("group", "country-la", len(la), [box(c[0]) for c in la])] if la else [])
    if code in GDHCN[3]:
        countries.append(box("gdhcn"))
    layout = ("col", [
        ("row", [box(c) for c in JOURNEY_CAPABILITIES[code]]),
        ("row", [("group", "group-people", 1, [box("role-" + r["id"]) for r in roles_of(code)]), box(jkey(code))]),
        ("row", countries),
        ("row", [("group", l, len(bs), [box(b) for b in bs]) for l, bs in layers if bs]),
    ])
    keys = {c[0] for c in sys_}
    conns = [("Realization", jkey(code), c) for c in JOURNEY_CAPABILITIES[code]]
    conns += [("Assignment", "role-" + r["id"], jkey(code)) for r in roles_of(code)]
    conns += [("Serving", c[0], jkey(code)) for c in sys_]
    conns += [("Specialization", c[0], c[2]) for c in sys_]
    if code in GDHCN[3]:
        conns += [("Serving", "gdhcn", jkey(code))]
        conns += [("Serving", "gdhcn", k) for k in GDHCN_SERVES if k in keys]
    doc = (f"Journey {code} ({JOURNEYS[code][1]}): the people assigned to it (its BPMN lanes), the systems that serve it, "
           f"the DPI-H RA building blocks they specialize, and the RA capabilities it realizes.")
    return (journey_view_name(code), doc, layout), conns


VIEWS = [
    (SYSTEMS_VIEW,
     "The demonstrator\u2019s Thai (left) and Lao (right) systems, each a specialization of the DPI-H RA building block it instantiates (centre: the layers of the RA\u2019s Integrated View, Fig. 3.2), with WHO GDHCN beneath both countries (the lines from it are in each journey\u2019s view).",
     ("row", [
         ("group", "country-th", 1, [box(c[0]) for c in _by_layer(TH)]),
         ("col", [("group", layer, 1, [box(b) for b in bs]) for layer, bs in RA_LAYERS] + [box("gdhcn")]),
         ("group", "country-la", 1, [box(c[0]) for c in _by_layer(LA)]),
     ])),
    (JOURNEYS_VIEW,
     "The demonstrator\u2019s journeys J1 to J4.1 as business processes: the people assigned to each (its BPMN lanes), the DPI-H RA stakeholders those people belong to, and the RA capabilities it realizes. The systems that serve each journey are in that journey\u2019s own view.",
     ("col", [
         ("group", "group-capabilities", 3, [box(c) for c in GROUP_MEMBERS["group-capabilities"]]),
         ("group", "group-journeys", 5, [box(jkey(c)) for c in JOURNEYS]),
         ("group", "group-people", 5, [box("role-" + r) for r in PEOPLE_ORDER]),
         ("row", [box("stk-health-workers"), box("stk-care-recipients")]),
     ])),
]

VIEW_CONNECTIONS = {
    SYSTEMS_VIEW: [("Specialization", k, ra) for k, _n, ra, *_ in SYSTEMS],
    JOURNEYS_VIEW: [r for r in RELATIONS if r[0] in ("Assignment", "Realization", "Association")],
}
for _code in JOURNEYS:
    _v, _c = journey_view(_code)
    VIEWS.append(_v)
    VIEW_CONNECTIONS[_v[0]] = _c

