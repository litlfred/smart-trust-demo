---
# smart-trust-demo-ig01
title: 'IG-01: L2 DAK and L3 FHIR IG for the journeys J1 to J4'
status: in-progress
type: feature
priority: high
tags:
    - this-repository
created_at: 2026-10-23T16:10:00Z
updated_at: 2026-10-23T16:10:00Z
---

The journeys existed only as harness content (BPMN in `processes/content/`, roles, actors and stories in `scenarios/`). There was no L2 DAK and no L3 FHIR IG, and nothing was published as an IG (owner, 2026-10-23: "there are no L2 or L3 artefacts published yet").

Shape, as litlfred/smart-immunizations: `sushi-config.yaml`, `ig.ini`, `dak.json` and the DAK pages under `input/pagecontent/`. The L2 content is generated from the harness sources by `tools/ig-gen/ig_gen.py` (single source; CI fails if stale): roles become `ActorDefinition`s (generic personas, system actors), the BPMN is copied to `input/business-processes/`, stories and the journeys' user scenarios become pages.

FHIR R5 (5.0.0), as smart-trust and smart-trust-phw are.

## Open

- IG id and canonical: working assumption `smart.who.int.trust-demo` / `http://smart.who.int/trust-demo`, owner to confirm.
- Publish: mount smart-base, add the fhir-harness `ig-ast-refresh` caller pinned by SHA, publish under gh-pages.
- L3 content beyond actors: example resources for each journey (the J1 DVCs as `Immunization`s, the J2 referral `ServiceRequest`, the J3 schedule `PlanDefinition`, the J4 IPS bundle).
- BPMN diagrams as SVG in the IG pages (now linked to the harness site's viewer).

## Done when

- [x] SUSHI builds with 0 errors (CI job `ig-sushi`)
- [ ] IG published on gh-pages
- [ ] Example resources for J1 to J4.1
