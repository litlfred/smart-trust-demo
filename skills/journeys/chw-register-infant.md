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

The CHW enters the registration form (data dictionary TD.J2A) through
smart-base's `Process_QuestionnaireDataCapture`: she completes it
(`complete-sdc-questionnaire`) and the app extracts it
(`extract-questionnaire-response`). This skill is what that extraction writes
in this journey.
