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
| `steps[].narrative`, `preconditions` | `docs/journeys.md` | the prose the page is generated from; a precondition holds before the step and is not part of it |
| `steps[].stories` | **edge** to user stories | many to many: a story may span steps |
| `steps[].realisedBy` | **edge** to BPMN | a process file and task ids; one step may span processes |
| `steps[].requirements` | **edge** to `req:` nodes | e.g. STT-PAY-001 |
| `steps[].examples` | **edge** to FHIR examples | `Type/id` |

The **user stories stay role-level** (caregiver, community health worker). A
scenario's steps are **persona-level** (Khamla, Vilay). The `stories` edge is
what joins the two.

**Left out on purpose:**

- **The workshop layer.** "Ask the room", the policy takeaway, the facilitator
  cue and the module questions are KG-01 gap 3. A workshop kind would point at
  step ids, so the scenario does not depend on any one workshop.
- **The technical layer.** Which building block a step uses, in which role, is
  KG-01 gap 2.
- **Presentation.** A persona's colours, and a step's device screen (S1–S8),
  belong to vaxlink.

## Files

- [`user-scenario.schema.json`](user-scenario.schema.json): the shape, JSON
  Schema 2020-12, kind `user-scenario/0.1.0`.
- [`example/`](example/): the four journeys, one scenario each, chained by
  `follows`: J1 (one step), J2 (J2a, J2b), J3 (J3a, J3b), J4 (J4.0a, J4.0b,
  J4.1), and the trust ladder as a code list. They were converted once from
  vaxlink's `journeyData.ts` (the steps, experiences, pain points, enablers,
  record and what-ifs) and the prose of `docs/journeys.md` (narrative and
  preconditions; requirements and named examples are read from it). Stories and
  BPMN tasks were mapped by hand.
- [`check.py`](check.py): checks the shape, and the references a schema cannot
  express (actors, stories, BPMN task ids, ladder codes, FSH instances, the
  `follows` chain). Run `python3 docs/proposals/user-scenario/check.py`. It
  passes on all four, and reports each of seven seeded errors.

## What the conversion found

- **The J2 BPMN does not match the J2 steps in order.** In the walkthrough,
  Vilay registers Somsack (J2a), then reads the cards (J2b). In
  `j2-chw-discovery-referral.bpmn`, `Task_Register` comes after `Task_Read` and
  also saves the doses. So J2a and J2b both point at `Task_Register`. Either
  the diagram splits registration from saving the doses, or the walkthrough
  reorders.
- **Pain points and enablers are worded twice.** `docs/journeys.md` and vaxlink
  say the same thing in different words (and journeys.md says it once per
  journey, vaxlink once per step). The examples take vaxlink's wording, per
  step.
- **J4.0a has no BPMN task.** Looking at the wallet is not a step of
  `j4-0-family-vhl-issuance.bpmn`, so its `realisedBy` is empty.

## Open questions

1. **Granularity.** Should a scenario be one journey or one whole story? **Decided 2026-11-05 (owner): one per journey**, chained by `follows`, as vaxlink's four chapters are.
2. **Where the prose lives.** **Decided 2026-11-05 (owner): generate it.**
   `docs/journeys.md` "User scenarios" is to be written by `ig_gen.py` from
   each step's `narrative`, `preconditions`, `painPoint` and `enabler`, as the
   personas page is from the actors. The policy line under each journey waits
   for the workshop kind (KG-01 gap 3).
3. **Stories' kind.** User stories already have one: cat-harness-tools
   `schemas/process/user-story.ts` (`id`, `role`, `want`, `soThat`, strict).
   The edge runs from the step to the story, so that kind needs no change.
   Its "I want / so that" fields overlap the bootstrap `Requirement`
   schema's `capability` and `benefit`.
