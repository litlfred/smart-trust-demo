---
# smart-trust-demo-ig01
title: 'IG-01: L2 DAK and L3 FHIR IG for the journeys J1 to J4'
status: in-progress
type: feature
priority: high
tags:
    - this-repository
created_at: 2026-10-23T16:10:00Z
updated_at: 2026-10-29T10:40:00Z
---

The journeys existed only as harness content (BPMN in `processes/content/`, roles, actors and stories in `scenarios/`). There was no L2 DAK and no L3 FHIR IG, and nothing was published as an IG (owner, 2026-10-23: "there are no L2 or L3 artefacts published yet").

Shape, as litlfred/smart-immunizations: `sushi-config.yaml`, `ig.ini`, `dak.json` and the DAK pages under `input/pagecontent/`. The L2 content is generated from the harness sources by `tools/ig-gen/ig_gen.py` (single source; CI fails if stale): roles become `ActorDefinition`s (generic personas, system actors), the BPMN is copied to `input/business-processes/`, stories and the journeys' user scenarios become pages.

FHIR R4 (4.0.1), as smart-base, smart-trust and smart-trust-phw are (moved from R5 on 2026-11-07, owner: R4 like smart-base). IG id `smart.who.int.trust-demo`, canonical `http://smart.who.int/trust-demo` (owner, 2026-10-23: memory/dir-ig-identity.md).

## Open

- L3 examples for J1: the DVC payloads. Blocked: the only published smart.who.int.trust-phw package (0.1.0, the one SUSHI can pin) has an older DVCMinPreQual than the guide's §12 example at af75be2 (`ntl`, `v[]`, `dt` against the wire's `nt`, `vx`, `dv` and a version `v`), so instances of it would not match the signed certificates. Needs a newer trust-phw package (built from litlfred/smart-trust-phw main) pinned by sha256.

## Done when

- [x] SUSHI builds with 0 errors (CI job `ig-sushi`)
- [x] IG published on gh-pages: the root of https://litlfred.github.io/smart-trust-demo/ since 2026-10-24 (owner, 06:49Z, option C: the IG is the root, the old `proposals/` and `upstream/` addresses are dropped; their pages are IG pages now, #11). Route: `ig-ast-refresh.yml` (#9) seeds the AST cache, `ghbuild.yml` lets `stage-local.ts --publisher ig` find the IG route, which builds the folio site from the AST. No smart-base mount was needed.
- [x] BPMN diagrams as SVG in the business processes page (2026-10-28, #13: drawn beside each .bpmn by `tools/render-bpmn/render_bpmn.ts`, embedded by ig_gen.py; owner: "i dont see BPMN diagrams"). Every STT requirement id on the generated pages links to smart-trust-tools' requirements page (owner, same day: "can we move to proper links").
- [x] Example resources for J2 to J4.1 (2026-10-29, owner's card "A. J2–J4.1 now, J1 waits"): `input/fsh/examples/` — the people and places, the J2 referral (ServiceRequest), the J3 imported doses with their Provenance, the schedule evaluation (ImmunizationRecommendation) and the given OPV, the J4.0 IPS document Bundle and the J4.1 Provenance of its receipt.
- [ ] Example resources for J1 (the DVC payloads): blocked as in Open above
