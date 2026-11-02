---
name: portal-serve-manifest
description: >
  Serve a VHL manifest to a receiver abroad after checking the passcode, the expiry and the holder's consent, and log every request at home (journey J4.1).
---

# portal-serve-manifest

Serve a VHL manifest to a receiver abroad after checking the passcode, the expiry and the holder's consent, and log every request at home (journey J4.1).

## What it does

The home country's portal hosts each VHL's manifest (IHE ITI VHL, ITI-YY5). On a manifest request it:

1. Checks the request's HTTP Message Signature (STT-VHL-008), the link's expiry (STT-VHL-009), the passcode, and the FHIR `Consent` the holder recorded when sharing (IHE Privacy Consent on FHIR).
2. On success, returns the manifest of encrypted files; the receiver decrypts them with the key from the link (STT-VHL-007).
3. Records every request, granted or refused, as a FHIR `AuditEvent` (IHE Basic Audit Log Patterns) held in the home country. A wrong passcode is refused and still logged.

The records stay hosted at home. The receiver views them; nothing is copied into a registry abroad.
