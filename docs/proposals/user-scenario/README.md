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
| `when`, `where`, `country`, `partOf`, `sequence` | the story | `partOf` chains J1 → J4 into one story |
| `trustLadder` | a `code-list` | the ordered states of the record |
| `steps[].experiences` | journey map | per actor: doing, feeling, emotion −2..2 |
| `steps[].painPoint`, `enabler`, `record`, `handoff`, `whatIf` | journey map | |
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
- [`example/j1-born-abroad.json`](example/j1-born-abroad.json): J1 from the
  walkthrough's text, with its stories, BPMN tasks, requirements and examples.
- [`example/record-trust.code-list.json`](example/record-trust.code-list.json):
  the trust ladder.
- [`check.py`](check.py): checks the shape, and the references a schema cannot
  express (actors, stories, BPMN task ids, ladder codes, FSH instances). Run
  `python3 docs/proposals/user-scenario/check.py`; it passes on J1, and
  reports each of seven seeded errors.

## Open questions

1. **Granularity.** Should a scenario be one journey (J1; J4 holding J4.0a,
   J4.0b and J4.1) or one whole story with chapters? The draft says one
   journey, chained by `partOf`, which matches vaxlink's four chapters and the
   sections of `journeys.md`.
2. **Where the prose lives.** Should `docs/journeys.md` "User scenarios" be
   generated from these files (by `ig_gen.py`, as the personas page now is),
   or keep its prose and be pointed to by `description`? Generating it is the
   only way the scenario is written once.
3. **Stories' kind.** `scenarios/stories.json` has no kind either. The draft
   takes the DAK `FunctionalRequirement` shape it already has (role, want,
   soThat) as given; it needs its own kind, or a place in `scenarios`.
