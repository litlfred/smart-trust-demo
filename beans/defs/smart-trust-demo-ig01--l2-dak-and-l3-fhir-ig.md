---
# smart-trust-demo-ig01
title: 'IG-01: L2 DAK and L3 FHIR IG for the journeys J1 to J4'
status: in-progress
type: feature
priority: high
tags:
    - this-repository
created_at: 2026-10-23T16:10:00Z
updated_at: 2026-10-24T07:00:00Z
---

The journeys existed only as harness content (BPMN in `processes/content/`, roles, actors and stories in `scenarios/`). There was no L2 DAK and no L3 FHIR IG, and nothing was published as an IG (owner, 2026-10-23: "there are no L2 or L3 artefacts published yet").

Shape, as litlfred/smart-immunizations: `sushi-config.yaml`, `ig.ini`, `dak.json` and the DAK pages under `input/pagecontent/`. The L2 content is generated from the harness sources by `tools/ig-gen/ig_gen.py` (single source; CI fails if stale): roles become `ActorDefinition`s (generic personas, system actors), the BPMN is copied to `input/business-processes/`, stories and the journeys' user scenarios become pages.

FHIR R5 (5.0.0), as smart-trust and smart-trust-phw are. IG id `smart.who.int.trust-demo`, canonical `http://smart.who.int/trust-demo` (owner, 2026-10-23: memory/dir-ig-identity.md).

## Open

- L3 content beyond actors: example resources for each journey (the J1 DVCs as `Immunization`s, the J2 referral `ServiceRequest`, the J3 schedule `PlanDefinition`, the J4 IPS bundle). Blocked for the J1 DVCs: the only published smart.who.int.trust-phw package (0.1.0, the one SUSHI can pin) has an older DVCMinPreQual than the guide's §12 example at af75be2 (`ntl`, `v[]`, `dt` against the wire's `nt`, `vx`, `dv` and a version `v`), so instances of it would not match the signed certificates. Needs a newer trust-phw package (built from litlfred/smart-trust-phw main) pinned by sha256.
- BPMN diagrams as SVG in the IG pages (now linked to the harness site's viewer).

## Done when

- [x] SUSHI builds with 0 errors (CI job `ig-sushi`)
- [x] IG published on gh-pages: the root of https://litlfred.github.io/smart-trust-demo/ since 2026-10-24 (owner, 06:49Z, option C: the IG is the root, the old `proposals/` and `upstream/` addresses are dropped; their pages are IG pages now, #11). Route: `ig-ast-refresh.yml` (#9) seeds the AST cache, `ghbuild.yml` lets `stage-local.ts --publisher ig` find the IG route, which builds the folio site from the AST. No smart-base mount was needed.
- [ ] Example resources for J1 to J4.1
