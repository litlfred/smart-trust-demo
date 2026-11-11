# smart-trust-demo

A demonstrator for the WHO SMART Trust HCERT libraries, built around four
user journeys of one cross-border family, and the Android test run of the
Kotlin HCERT library (requirement
[STT-GEN-004](https://github.com/litlfred/smart-trust-tools/blob/main/skills/requirements/stt-gen-004.json):
Android is a named target that has never been run).

The journeys tell the story of the [VaxLink](https://fredhersch.github.io/vaxlink/)
workshop walkthrough ([source](https://github.com/fredhersch/vaxlink)): Somsack
SENGMANY, a Lao baby born in Thailand, followed over his first year. Its FHIR
examples are materialized in the IG, and the
[Journey examples](https://litlfred.github.io/smart-trust-demo/vaxlink-examples.html)
page maps each of its screens and payloads to them. The journeys are
presented for workshops by the harness's journeys viewer, at
[the DPI-H policy track](https://litlfred.github.io/smart-trust-demo/en/smart-trust-demo/journeys/smart-trust-demo/workshops/dpi-h-policy-track/overview/),
built from the same commit as the guide.

| Journey | What happens | Library call |
|---|---|---|
| **J1** Born abroad | Somsack is born at Chiang Rai Provincial Hospital, Thailand (Country A). Dr Anan gives the Hep B and BCG birth doses; the hospital issues two signed paper Digital Vaccine Certificates (DVCs) with QR codes. No Thai identity number is needed. | issuer `prepare` / host signs / `finish` |
| **J2** Found at home | In Village 04, Lao PDR (Country B), the Community Health Worker (CHW) Vilay adds him to his household offline, reads the foreign QRs without verifying them, saves the doses as reported, and refers the family. | `HcertVerifier.readUnverified` (STT-VER-011) |
| **J3** Made official | At Vientiane District Health Center, Nurse Chanthasone's tablet verifies the DVCs against the GDHCN trust list, imports the doses with provenance, adds the Lao schedule code beside the Thai product code, and books the 6-week doses. | `HcertVerifier.verify`, `HcertTrustStore.addDidDocument` |
| **J4** Crossing back ("One Family, One Phone") | A year later, Bounmy's phone holds the family's records. He shares Somsack's IPS as a passcode-protected Verifiable Health Link (VHL); in Chiang Rai, Dr Anan views it, and the access is logged in Lao PDR. | `HcertVhl` (IHE ITI VHL, `vhlink:/`, ITI-YY5) |

Thailand is played on the GDHCN DEV network by test participant `XXR`, whose
key also signs the WHO SMART Trust guide's worked example
([QR Code Generation §12](https://smart.who.int/trust/qr_code_generation.html)),
which the library tests use. Lao PDR is played by a fictional DEV participant,
`XXH`, so nothing implies a real ministry. Every person in this repository is
fictional.

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
