# Proposal: a `user-scenario` kind

**Status:** draft, 2026-11-05. Bean `smart-trust-demo-kg01`, gap 1. Proposed
for cat-harness; drafted here, where the content is.

**Question:** the journeys are written three times, and no moment links to a
story:

- as prose under "User scenarios" in [`docs/journeys.md`](../../journeys.md);
- as `JourneyStep` entries in litlfred/vaxlink's `journeyData.ts`;
- partly in the BPMN.

What one node can they all come from?

## The answer: the DAK user scenario, told as a journey map

smart-base's logical model `UserScenario` has `id`, `title`,
`description[x]` and `personas`. A DAK user story is a `FunctionalRequirement`:
actor, *I want* (`capability`), *so that* (`benefit`), which is the shape of
`scenarios/stories.json`. The kind keeps the DAK fields as they are, and adds
the ordered **steps** the journey map is made of:

| Field | From | |
|---|---|---|
| `id`, `title`, `description`, `personas` | DAK `UserScenario` | `personas` are actor ids |
| `when`, `where`, `country`, `follows` | the story | `follows` chains J1 → J4 into one story |
| `trustLadder` | a `code-list` | the ordered states of the record |
| `steps[].experiences` | journey map | per actor: doing, feeling, emotion −2..2 |
| `steps[].painPoint`, `enabler`, `record`, `handoff`, `whatIf` | journey map | |
| `steps[].policy` | journey map | the policy point the step makes |
| `steps[].narrative`, `preconditions` | `docs/journeys.md` | the prose the page is generated from; a precondition holds before the step and is not part of it |
| `steps[].stories` | **edge** to user stories | many to many: a story may span steps |
| `steps[].realisedBy` | **edge** to BPMN | a process file and task ids; one step may span processes |
| `steps[].requirements` | **edge** to `req:` nodes | e.g. STT-PAY-001 |
| `steps[].examples` | **edge** to FHIR examples | `Type/id` |

The **user stories stay role-level** (caregiver, community health worker). A
scenario's steps are **persona-level** (Khamla, Vilay). The `stories` edge is
what joins the two.

**Left out on purpose:**

- **The workshop layer.** "Ask the room", the facilitator cue and the module
  questions are KG-01 gap 3. (The one-line policy point is kept, as `policy`,
  because `docs/journeys.md` states it under each step.) A workshop kind would point at
  step ids, so the scenario does not depend on any one workshop.
- **The technical layer.** Which building block a step uses, in which role, is
  KG-01 gap 2.
- **Presentation.** A persona's colours, and a step's device screen (S1–S8),
  belong to vaxlink.

## Files

- [`user-scenario.schema.json`](user-scenario.schema.json): the shape, JSON
  Schema 2020-12, kind `user-scenario/0.1.0`.
- [`scenarios/user-scenarios/`](../../../scenarios/user-scenarios/): one
  scenario per journey, chained by `follows`: J1, J2 (J2a, J2b), J3 (J3a,
  J3b), J4.0 (J4.0a, J4.0b), J4.1, and the trust ladder as a code list. They
  were converted once from vaxlink's `journeyData.ts` (the steps, experiences,
  pain points, enablers, policy points, record and what-ifs) and the prose of
  `docs/journeys.md` (narrative and preconditions; requirements and named
  examples are read from it). Stories and BPMN tasks were mapped by hand.
- **`docs/journeys.md` "User scenarios" is generated from them** by
  `tools/ig-gen/ig_gen.py`, between its markers; `ig_gen.py --check` fails in
  CI when it is stale.
- The shape and the references a schema cannot express (actors, stories,
  BPMN task ids, ladder codes, examples, `partOf`, ArchiMate views) are
  checked by the harness's `check:kind-validators` and `check:journey-refs`
  in CI (`checks.yml`, job bpmn-generated); `ig_gen.py` refuses a `follows`
  chain that is not one chain. They replace `tools/user-scenarios/check.py`
  (owner, 2026-11-06).

## What the conversion found

- **J2 was told in the opposite order to its BPMN.** The walkthrough had
  Vilay register Somsak (J2a) before reading the cards (J2b), while
  `j2-chw-discovery-referral.bpmn` reads first and then registers. **Resolved
  2026-11-05 (owner): vaxlink was reordered** to match the BPMN. J2a now reads
  the cards (`Task_Show`, `Task_Scan`, `Task_Read`), and J2b registers, saves
  the doses as reported and refers (`Task_Register`, `Task_Refer`, `Task_Slip`).
  `docs/journeys.md` and `docs/vaxlink-examples.md` follow.
- **Pain points and enablers are worded twice.** `docs/journeys.md` and vaxlink
  say the same thing in different words (and journeys.md says it once per
  journey, vaxlink once per step). The examples take vaxlink's wording, per
  step.
- **J4.0a has no BPMN task.** Looking at the wallet is not a step of
  `j4-0-family-vhl-issuance.bpmn`, so its `realisedBy` is empty.

## Open questions

1. **Granularity.** Should a scenario be one journey or one whole story? **Decided 2026-11-05 (owner): one per journey**, chained by `follows`. A journey is a BPMN process, so J4.0 and J4.1 are two scenarios, though vaxlink tells them in one chapter.
2. **Where the prose lives.** **Decided 2026-11-05 (owner): generate it. Done.**
   `ig_gen.py` writes the section from each step's `preconditions`,
   `narrative`, `painPoint`, `enabler` and `policy`. A step's `policy` is its
   one-line policy point; the workshop's questions stay for a workshop kind
   (KG-01 gap 3). The pain point, enabler and policy lines are now one per
   step, in the walkthrough's words.
3. **Stories' kind.** User stories already have one: cat-harness-tools
   `schemas/process/user-story.ts` (`id`, `role`, `want`, `soThat`, strict).
   The edge runs from the step to the story, so that kind needs no change.
   Its "I want / so that" fields overlap the bootstrap `Requirement`
   schema's `capability` and `benefit`.
