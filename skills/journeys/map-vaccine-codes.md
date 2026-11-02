---
name: map-vaccine-codes
description: >
  Add the national schedule code beside the foreign vaccine code of an imported dose, keeping the issuer's coding (journey J3).
---

# map-vaccine-codes

Add the national schedule code beside the foreign vaccine code of an imported dose, keeping the issuer's coding (journey J3).

## What it does

For each imported FHIR `Immunization`, translate its `vaccineCode` (the issuer's coding: a WHO PreQual product as signed in the DVC) with the national `ConceptMap` (`$translate`) and add the national schedule coding as a second `coding`. The issuer's coding is never replaced or removed.

Three layers, in order:

1. **Product**: the PreQual product code as issued.
2. **Antigen**: the vaccine type it belongs to (for example Hep B, monovalent, paediatric).
3. **Schedule**: the national schedule antigen and dose it counts as (for example the Hep B birth dose).

When the map has no target for a product, the dose goes to the nurse, who confirms the equivalent schedule antigen and dose. The decision is recorded (a `Provenance` naming the nurse, or a new `ConceptMap` element for review) so the next clinic does not have to decide again.
