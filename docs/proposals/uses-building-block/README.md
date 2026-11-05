# Proposal: the "uses a building block, in this role" edge

**Status:** draft, 2026-11-05. Bean `smart-trust-demo-kg01`, gap 2. Proposed
for cat-harness; drafted here, where the content is.

**Question:** each step of a journey uses tools, standards and trust services,
and each one does something particular to that step. For example, the OHS FHIR
SDK caches the trust list in J3a and decodes a QR in J2a. Where does that
fact live, so that the walkthrough, the IG and the ArchiMate views all read it
from one place?

Today it is in two places that do not know about each other:

- vaxlink's `techData.ts`: 19 generic blocks (`BUILDING_BLOCKS`), and per step
  the blocks it uses with a one-line role (`STEP_TECH`);
- `tools/archimate/overlay.py`: 18 deployed components (`COMPONENTS`), each a
  part of a Thai or Lao system and a specialization of a DPI-H RA block.

## The answer: a catalogue, and an edge from the step

**[`building-blocks.schema.json`](building-blocks.schema.json)**
(`building-blocks/0.1.0`): one catalogue of blocks. Each block has:

| Field | |
|---|---|
| `kind` | `tool` (OHS FHIR SDK), `system` (the Lao national FHIR server), `standard` (IHE VHL), or `network` (WHO GDHCN) |
| `layer` | one of the catalogue's layers: tools & apps, data standards, trust & exchange |
| `jurisdiction` | `Thailand`, `Lao PDR`, or `International`. A country's deployed system is that country's; what anyone can adopt is International. The ArchiMate views are to split the RA by jurisdiction on this field (owner, 2026-11-05) |
| `owner`, `what`, `soWhat`, `links` | as the walkthrough shows them |
| `components` | the overlay's ArchiMate element keys that deploy the block (`la-info-gateway` for the OHS Info Gateway) |

**The edge** sits on a user-scenario step
([`../user-scenario/user-scenario.schema.json`](../user-scenario/user-scenario.schema.json)):

```json
"technicalSummary": "The clinic checks Thailand’s signature against WHO’s trust list, stored locally. …",
"uses": [
  { "block": "ohs-fhir-sdk", "role": "Clinic tablet app; caches the trust list" },
  { "block": "gdhcn", "role": "Supplies Thailand’s public key (downloaded in advance)" }
]
```

- `role` is the point of the edge: the same block plays a different role in
  each step.
- `component` (optional) names which deployment plays it, when a block has
  more than one (`thai-his` → `th-birth-ehr`, `th-dvc-signer`).
- The step's `handoff` gains `carrier` and `payload`: how the data travels
  and what it is.

## Files

- `building-blocks.json`: the catalogue, converted once from vaxlink's
  `techData.ts`. It has 19 blocks, 10 of them linked to overlay components.
  Kind, jurisdiction and components were mapped by hand.
- `scenarios/user-scenarios/*.json`: every step now has `technicalSummary` and
  `uses`, and its hand-off has `carrier` and `payload`, converted from
  `STEP_TECH`.
- `tools/user-scenarios/check.py` now also checks:
  - each `uses` names a block in the catalogue, once per step, and a
    `component` is one of that block's;
  - the catalogue's block ids are unique, its layers are known, and its
    components are element keys of `overlay.py`.

  It passes, and reports each of three seeded errors.

## Left out on purpose

- **The FHIR changes per step** (vaxlink's `STEP_TECH.fhir`: resource, change,
  profile, why). This is the step → `examples` edge with a reason, and could
  be added there.
- **The RA building blocks themselves.** They are smart-ra's ArchiMate
  elements, which `overlay.py` already reads. A catalogue `system` block points
  at overlay components, and those components specialize RA blocks, so the
  path from a step to the RA is step → block → component → RA block.

## Open questions

1. **Where the catalogue lives once adopted.** It could live in `archimate/`,
   with `overlay.py` reading it instead of its own `COMPONENTS` list, so the
   components are kept once. That is the ArchiMate session's file, so it is
   their call.
2. **Rendering.** Should `docs/journeys.md` show a "Uses" line per step, from
   `uses`, as it shows pain points and enablers? The walkthrough already shows
   it under "Under the hood".
