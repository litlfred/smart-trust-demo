# smart-trust-demo

A demonstrator for the WHO SMART Trust HCERT libraries, built around four
user journeys of one cross-border family, and the Android test run of the
Kotlin HCERT library (requirement
[STT-GEN-004](https://github.com/litlfred/smart-trust-tools/blob/main/skills/requirements/stt-gen-004.json):
Android is a named target that has never been run).

| Journey | What happens | Library call |
|---|---|---|
| **J1** Cross-border birth and initial vaccination | A mother delivers abroad in Asia; the newborn gets the birth doses (Hep B, BCG/Polio); the clinic issues a signed paper Digital Vaccine Certificate (DVC) with a QR code. | issuer `prepare` / host signs / `finish` |
| **J2** Return home, CHW discovery and referral | Back home, a Community Health Worker (CHW) finds the unregistered infant on a home visit, reads the foreign QR offline, logs it and refers the family to the clinic. | `HcertVerifier.readUnverified` (STT-VER-011) |
| **J3** Clinic verification and schedule generation | The clinic verifies the foreign DVC against the GDHCN trust list, imports the immunizations into the domestic record and evaluates the national schedule. | `HcertVerifier.verify`, `HcertTrustStore.addDidDocument` |
| **J4** Outbound family travel ("One Family, One Phone") | The national portal issues each family member's IPS and DVCs to one shared phone as passcode-protected Verifiable Health Link (VHL) QR codes, fetched at the point of care abroad. | `HcertVhl` (IHE ITI VHL, `vhlink:/`, ITI-YY5) |

J1 reuses the worked example of the WHO SMART Trust guide,
[QR Code Generation §12](https://smart.who.int/trust/qr_code_generation.html):
a Lao newborn, Chanthala SOUVANNALATH, Hep B and BCG birth doses, issued by
GDHCN DEV participant `XXR`. Home (J2–J4) is a fictional GDHCN DEV
participant, so nothing implies a real ministry. Every person in this
repository is fictional.

**Status:** planning. See [docs/plan.md](docs/plan.md) for the work plan and
[docs/proposals/app-platform.md](docs/proposals/app-platform.md) for the
Open Health Stack options awaiting the owner's choice.

## Related repositories

| Repository | Role here |
|---|---|
| [litlfred/smart-trust-tools](https://github.com/litlfred/smart-trust-tools) | The HCERT requirements (`req:` nodes), the WIT contract, the Kotlin library (`tools/hcert-kotlin`), the Rust/wasm library and the shared test vectors. Consumed at a pinned commit (see the plan). |
| [litlfred/smart-trust-phw](https://github.com/litlfred/smart-trust-phw) | The logical models (DVCMin, DVCMinPreQual, HealthLinkPayload …). **This is the working copy; [WorldHealthOrganization/smart-trust-phw](https://github.com/WorldHealthOrganization/smart-trust-phw) is upstream** (git remote `upstream`); GitHub records it so (litlfred's is the fork, WHO's is not, checked 2026-10-23). |
| [WorldHealthOrganization/smart-trust](https://github.com/WorldHealthOrganization/smart-trust) | The WHO SMART Trust implementation guide. Read-only from here. |
| [ohs-foundation](https://github.com/ohs-foundation) | Open Health Stack: the FHIR engine, data capture, workflow libraries and the OHS Player reference app the demonstrator builds on. Read-only from here. |

## Rules

The rules in [AGENTS.md](AGENTS.md) apply: only litlfred repositories are
changed from here, every dependency is pinned and verified, only open
standards are normative, and gh-pages is published by an agent, never by a
workflow.

## Licence

Apache-2.0, as smart-trust-tools (to be confirmed with the owner before the
first release).
