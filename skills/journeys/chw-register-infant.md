---
name: chw-register-infant
description: >
  Register a child found on a home visit, with any foreign doses recorded as unverified (journey J2).
satisfies:
  - "req:stt-ver-011#statement"
---

# chw-register-infant

Register a child found on a home visit, with any foreign doses recorded as unverified (journey J2).

## What it does

FHIR R4 `Patient` (and `RelatedPerson` for the caregiver) in the on-device OHS FHIR engine; each dose read by read-unverified becomes an `Immunization` with status `completed` and a tag saying it is unverified, never shown as verified. Works offline and syncs later.
