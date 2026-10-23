---
name: chw-refer
description: >
  Record a referral of the child to the clinic so the foreign record is verified and the schedule evaluated (journey J2).
---

# chw-refer

Record a referral of the child to the clinic so the foreign record is verified and the schedule evaluated (journey J2).

## What it does

FHIR R4 `ServiceRequest` (intent `order`, reason: verify foreign vaccination record) for the child, with the unverified `Immunization`s as supporting information, and a `Task` for the clinic.
