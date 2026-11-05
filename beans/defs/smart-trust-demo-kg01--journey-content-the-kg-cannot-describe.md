---
# smart-trust-demo-kg01
title: 'KG-01: the journey content no cat-harness kind describes'
status: in-progress
type: feature
priority: normal
tags:
    - open-issue
    - upstream
created_at: 2026-11-05T12:00:00Z
updated_at: 2026-11-05T14:00:00Z
---

The VaxLink walkthrough (litlfred/vaxlink) is the presentation of these journeys. It was reviewed on 2026-11-05 against the cat-harness kind schemas at `f9423d7`. The site, the snapshots it copies from here, the standards, the personas' identity and its closed code sets all map to existing kinds (`basic-cdn-site`, `processes`, `archimate`, `external-schema`, `scenarios`, `code-list`). About 40% of its content maps to none. It lives only as TypeScript in `src/data/`. The fix belongs in cat-harness (and its Zod source in cat-harness-tools), so this bean is tagged upstream.

## Gaps, largest first

1. **Journey map, as the DAK user scenario it elaborates.** A journey (J1 to J4.1) is a DAK *user scenario*: one persona-level story through the generic roles' *user stories*. Its moments are the scenario's ordered steps. Each moment has when, where, the touchpoint and the lead person; for each person what they do, what they feel and an emotion score (−2..2); the pain point, the enabler, the state of the record on an ordered trust ladder, a "what if" branch, and a facilitator cue. Its edges:
   - `stories`: the user stories in `scenarios/stories.json` it satisfies (role-level, many to many);
   - `realisedBy`: the BPMN tasks that carry it out (one moment spans J2a and J2b);
   - `requirements` and `examples`: the smart-trust-tools `req:` ids and the FHIR examples, as `docs/journeys.md` lists them.

   Today the scenario is written three times: as prose in `docs/journeys.md` "User scenarios" (which already carries VaxLink's pain points, enablers and policy points), as `JourneyStep` in vaxlink's `journeyData.ts` (9 moments), and in part as the BPMN. Nothing links a moment to a story. User stories have a kind (cat-harness-tools `schemas/process/user-story.ts`: `id`, `role`, `want`, `soThat`, strict), with no field for a step or a requirement. User scenarios have none.

   **Draft:** [`docs/proposals/user-scenario/`](../../docs/proposals/user-scenario/README.md): schema `user-scenario/0.1.0` (the DAK `UserScenario` fields plus ordered steps and the four edges), J1 as a worked example, and `check.py` for the references.
2. **"Uses a building block, in this role" edge.** A moment (or BPMN task) uses a building block, with a one-line role that is particular to that moment, and a data hand-off (from, to, payload, offline or not). ArchiMate's serving or realisation relations carry the block but not the per-moment role text. vaxlink: `techData.ts` `STEP_TECH`, 22 blocks.
3. **Workshop / facilitation layer.** Modules (M1–M7, day, canvas sheet, the question each carries), questions tagged by module and asked of a moment, decision rights, legal bases, cost drivers and substitution patterns. `policies` is ODRL (what an actor may do) and does not fit. vaxlink: `policyData.ts`.
4. **Persona fields on an actor.** The `scenarios` actor kind has `id`, `title`, `kind`, `description`, `roles` and no `meta`. This repository now keeps `meta.persona` (name, role, country, goal, needs, frustrations) on each person actor, checked by `tools/repo-checks`. The kind should declare it (or a `persona` sub-object), so the check is the harness's rather than this repository's.
5. **Smaller ones.**
   - A device screen (device type, the actor who sees it, its learning objective): partly a system actor.
   - `software-library` reads `bun.lock` only, so an npm `package-lock.json` layer has no library nodes.

## Done when

- a user scenario has a kind, with its moments, and `docs/journeys.md` and vaxlink's `journeyData.ts` are generated from it or checked against it;
- each gap has a kind or a field in cat-harness, or a recorded decision that it stays out of the graph;
- vaxlink's `src/data/` can be generated from (or checked against) nodes for every gap that gets a kind.

## Sources

- litlfred/vaxlink `src/data/journeyData.ts`, `techData.ts`, `policyData.ts` at `82112b0`
- cat-harness `schemas/kinds/scenarios.schema.json`, `basic-cdn-site.schema.json`, `policies.schema.json` at `f9423d7`
