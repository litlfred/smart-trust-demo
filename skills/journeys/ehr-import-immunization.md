---
name: ehr-import-immunization
description: >
  Import the doses of verified DVCs as FHIR Immunization resources in the domestic record (journey J3).
satisfies:
  - "req:stt-ver-007#statement"
  - "req:stt-ver-008#statement"
---

# ehr-import-immunization

Import the doses of verified DVCs as FHIR Immunization resources in the domestic record (journey J3).

## What it does

Each verified DVCMin payload maps to an `Immunization` (vaccine product from `vp`, date `dv`, batch `bo`, performer `cn`, issuer `is`), with a `Provenance` naming the HCERT's issuer, kid and verification time; unverified ones from J2 are superseded.
