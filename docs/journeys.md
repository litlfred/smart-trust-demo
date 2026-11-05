---
title: Journeys J1–J4
nav_order: 2
---

# Journeys J1–J4

> Somsack is born in Thailand, grows up in Lao PDR, and one year later a Thai
> doctor can see every vaccine he has ever had, without a single record being
> copied across the border.

The story is the one the [VaxLink](https://fredhersch.github.io/vaxlink/)
workshop walkthrough tells ([source](https://github.com/fredhersch/vaxlink)),
documented here as a WHO SMART Guidelines L2 DAK and L3 implementation guide.
Its FHIR examples are materialized in this guide; the
[VaxLink examples](vaxlink-examples.html) page maps each moment and device screen
to them.

- **Country A** (birth country) is **Thailand**. Somsack is born at Chiang Rai
  Provincial Hospital and gets his birth doses there (J1). On the GDHCN DEV
  network, Thailand is played by the test participant **XXR**, whose DSC (kid
  `kW/6VnwPRKI=`, hex `916ffa567c0f44a2`) is on the live DEV trust list.
- **Country B** (country of residence, "home") is **Lao PDR**. The family
  lives there (J2, J3, J4.0). On the DEV network it is played by a fictional
  participant, written **XXH**.
- J4.1 takes the family back to Thailand, a year later.

XXR and XXH are DEV test participants, not either country's production keys,
and nothing here implies a real ministry. Every person is fictional.

**The cast:** Khamla SENGMANY (mother), Bounmy SENGMANY (father, holds the
family phone), Vilay (community health worker, Village 04), Nurse
Chanthasone (Vientiane District Health Center) and Dr Anan (Thai
clinician, at the birth and a year later).

| # | Moment | When | Where | Processes |
|---|---|---|---|---|
| 1 | **Born abroad** | birth day, 2025-10-28 | Chiang Rai, Thailand | J1 |
| 2 | **Found at home** | 3 weeks later | Village 04, Lao PDR | J2 (J2a read the cards, J2b register and refer) |
| 3 | **Made official** | 4 weeks later | District Health Center, Lao PDR | J3 (J3a verify, J3b map and schedule) |
| 4 | **Crossing back** | 12 months later | Lao PDR to Thailand | J4.0 (a wallet, b share link), J4.1 |

How far a clinician can rely on Somsack's record, step by step (the VaxLink
"follow the record" ladder):

| Step | Record state | Held where | FHIR |
|---|---|---|---|
| J1 | On paper: two signed DVCs | Khamla's bag | HC1 QR (HCERT) |
| J2b | Reported, not verified | CHW phone, then sync | `Immunization.primarySource` false |
| J3a | Verified against the GDHCN trust list | district clinic | `Provenance` (verifier) |
| J3b | Scheduled: counts toward the national schedule | Lao national records | schedule `coding` added, `ImmunizationRecommendation`, `Task` |
| J4.0 | Portable: a summary the family can share | Lao records, link on the phone | IPS `Bundle`, `Consent` |
| J4.1 | Shared and audited: viewed abroad, logged at home | Lao national records | `Provenance`, `AuditEvent` |

| | Process | Where |
|---|---|---|
| J1 | [Issue the newborn's birth-dose DVCs](https://github.com/litlfred/smart-trust-demo/blob/main/processes/content/j1-birth-dose-dvc.bpmn) | Country A |
| J2 | [Discover and refer an unregistered infant](https://github.com/litlfred/smart-trust-demo/blob/main/processes/content/j2-chw-discovery-referral.bpmn) | Country B |
| J3 | [Verify, import and schedule at the home clinic](https://github.com/litlfred/smart-trust-demo/blob/main/processes/content/j3-clinic-verification-schedule.bpmn) | Country B |
| J4.0 | [Issue the family's records to one phone as VHLs](https://github.com/litlfred/smart-trust-demo/blob/main/processes/content/j4-0-family-vhl-issuance.bpmn) | Country B |
| J4.1 | [Read a family member's records at the point of care abroad](https://github.com/litlfred/smart-trust-demo/blob/main/processes/content/j4-1-vhl-point-of-care.bpmn) | abroad |

## Roles, actors and the guides' actor definitions

Each lane is a role in [`scenarios/roles.json`](https://github.com/litlfred/smart-trust-demo/blob/main/scenarios/roles.json).
Each actor in [`scenarios/actors/`](https://github.com/litlfred/smart-trust-demo/tree/main/scenarios/actors/) names the role it
plays. Its `meta.definedBy` gives the ActorDefinitions it is an instance of,
and its `meta.playsActor` gives the smart-trust-tools actor. On the role, the
guides' names appear as `otherNames` (also known as).

| Role (lane) | Actor here | WHO SMART Trust | WHO smart-trust-phw | IHE ITI VHL | smart-trust-tools |
|---|---|---|---|---|---|
| caregiver | Khamla SENGMANY (J1–J3), Bounmy SENGMANY (J4) | [Holder](http://smart.who.int/trust/ActorDefinition/Holder) | [Holder](http://smart.who.int/trust-phw/ActorDefinition/Holder) | [VHLHolder](https://profiles.ihe.net/ITI/VHL/ActorDefinition/VHLHolder) | vhl-holder |
| family-phone | the Sengmany family's shared phone (Bounmy's) | (Holder's device) | (Holder's device: the personal health wallet) | (VHLHolder's device) | vhl-holder |
| birth-clinic-system | Chiang Rai Provincial Hospital, Thailand | [Issuer](http://smart.who.int/trust/ActorDefinition/Issuer) | [Issuer](http://smart.who.int/trust-phw/ActorDefinition/Issuer) | [VHLSharer](https://profiles.ihe.net/ITI/VHL/ActorDefinition/VHLSharer) (HCERT side) | vhl-sharer / hcert-issuing-system |
| issuer-key | XXR's DSC key (plays Thailand) | [Trust Network Participant](http://smart.who.int/trust/ActorDefinition/TrustNetworkParticipant) (its PKI) | [Trust Network Participant](http://smart.who.int/trust-phw/ActorDefinition/TrustNetworkParticipant) | — | trust-network-participant / hcert-key-holder |
| chw-app | CHW app, Lao PDR | [Receiver](http://smart.who.int/trust/ActorDefinition/Receiver) (triage read only) | [Receiver](http://smart.who.int/trust-phw/ActorDefinition/Receiver) | [VHLReceiver](https://profiles.ihe.net/ITI/VHL/ActorDefinition/VHLReceiver) | vhl-receiver / hcert-verifying-system |
| home-clinic-ehr | Vientiane District Health Center EHR | Receiver | Receiver | VHLReceiver | vhl-receiver / hcert-verifying-system |
| gdhcn-trust-anchor | GDHCN DEV (WHO) | [Trust Network Anchor](http://smart.who.int/trust/ActorDefinition/TrustNetworkAnchor) | [Trust Network Anchor](http://smart.who.int/trust-phw/ActorDefinition/TrustNetworkAnchor) | [TrustAnchor](https://profiles.ihe.net/ITI/VHL/ActorDefinition/TrustAnchor) | trust-anchor |
| national-portal | Lao PDR national portal and gateway (XXH) | Issuer; Trust Network Participant | Issuer; Trust Network Participant | [VHLSharer](https://profiles.ihe.net/ITI/VHL/ActorDefinition/VHLSharer) | vhl-sharer |
| poc-receiver | Chiang Rai primary care clinic viewer | Receiver | Receiver | VHLReceiver | vhl-receiver |
| birth-clinic-vaccinator, community-health-worker, home-clinic-provider, poc-provider | Dr Anan, Vilay, Nurse Chanthasone, Dr Anan | — (the people operating the systems; no ActorDefinition in either guide) | — | — | — |

smart-trust-phw's requirements map onto the journeys as follows:

- `provide-a-vhl-to-a-receiver` (Holder) is J2, J3 and J4.1.
- `receive-a-vhl` is J2, J3 and J4.1 too. It names the Issuer as its actor, which looks wrong: [OI-01](https://github.com/litlfred/smart-trust-demo/blob/main/beans/defs/smart-trust-demo-oi01--trust-phw-receive-a-vhl-names-the-issuer.md).
- `publish-`, `receive-`, `distribute-` and `retrieve-pki-material` are the trust anchor and the participants in J3.

## User scenarios

Each step names the requirements of
[smart-trust-tools](https://github.com/litlfred/smart-trust-tools/tree/main/skills/requirements)
it exercises, and the FHIR examples of this guide it produces. The stories are
in [`scenarios/stories.json`](https://github.com/litlfred/smart-trust-demo/blob/main/scenarios/stories.json).
Each moment ends with its pain point, what enables it, and the policy point it
makes, as the VaxLink walkthrough presents them.

### J1 — Born abroad (Thailand, birth day)

**Precondition: the issuer's DSC is on the trust list.** XXR's document
signer certificate (DSC), issued under XXR's Country Signing CA (CSCA), was
shared with the GDHCN, the Trust Anchor, before any DVC is signed; the GDHCN
publishes it as a DID document. Sharing it is not a step of issuing. A DVC
signed with a key whose DSC was never shared fails every receiver's
trust-list check (STT-VER-006).

Khamla gives birth to Somsack on 2025-10-28 at Chiang Rai Provincial
Hospital, away from home. He has no Thai identity number. Dr Anan gives the
Hep B and BCG birth doses and records them with their WHO PreQual product
codes. For each dose, the hospital system does three things:

1. It builds a DVCMinPreQual payload: STT-PAY-001…005 and STT-PAY-007, with subclaim −6 (STT-SEL-003). No identity document is needed (STT-PAY-005).
2. It prepares the CWT and the bytes to sign: STT-CWT-001…005, STT-ISS-004.
3. It has XXR's key sign them (STT-COS-002, STT-COS-006), then finishes the HC1 text: STT-COS-001, STT-ZIP-001, STT-B45-001, STT-HC1-001, STT-QR-001.

Khamla leaves with two paper DVCs.
*In the demo:* the library tests use the WHO guide's own two signed HC1
strings ([QR Code Generation §12](https://smart.who.int/trust/qr_code_generation.html)),
which verify against the live DEV trust list under the same XXR key. Somsack's
DVC payloads are illustrative, as in VaxLink. Live issuance in the app uses a
TEST-ONLY key (STT-ISS-003), whose DSC is not on the GDHCN list, so its DVCs
do not verify in J3.

- *Pain point:* without a national id, the records would stay locked in the Thai hospital's system.
- *Enabler:* a signed QR card travels with the family; no id or database lookup is needed.
- *Policy:* babies born abroad can get a verifiable vaccine record without the host country's civil registration or national id.

### J2 — Found at home (Lao PDR, 3 weeks later)

**J2a.** On a routine visit to Village 04, Vilay finds a newborn the Lao
system does not know exists. Her phone has had no signal for weeks. Khamla
shows the two cards. The CHW app reads them with **read-unverified**
(STT-VER-011; STT-B45-002, STT-ZIP-002, STT-CBR-003), which needs no trust
list. It shows the doses, but checks no signature and saves nothing yet.

**J2b.** On the CHW app's newborn form (structured data capture,
`TrustDemoHouseholdRegistration`) she adds Somsack to the Sengmany household
(`TrustDemoHousehold`), with a temporary id. Bounmy confirms the details as
head of household. The app saves the doses read from the cards as reported by
the family, not verified (`TrustDemoJ2HepBReported`, `TrustDemoJ2BcgReported`:
`primarySource` false). Vilay refers Somsack to the district health center
(`TrustDemoJ2Referral`). Everything stays queued on the phone, for 28 days if
need be, and syncs when it next reaches a signal.

- *Pain point:* babies born abroad are invisible to the home system until civil registration catches up; without a check, a forged or mistyped card could become an official record.
- *Enabler:* an offline form links the baby to his household at once, and the app keeps what the family reported apart from what has been verified.
- *Policy:* newborns can be registered at home, offline, before an id exists; and trust is not granted too early.

### J3 — Made official (Vientiane District Health Center, 4 weeks later)

**Precondition: the DID documents are already loaded.** Loading them is not
a step of this visit. The clinic may be offline all day, so the EHR fetches
nothing during it: its trust store holds the GDHCN DEV trust list as it was
last refreshed, including XXR's DSC DID document (STT-TRU-001, STT-TRU-002,
STT-TRU-005). A clinic with no connection of its own refreshes it about weekly,
when the CHW visits the base clinic or district health office, where Country
B retrieves the list the GDHCN trust anchor distributes. A DSC published after that refresh is not in
the clinic's copy, so its DVC fails the trust-list check (STT-VER-006) until
the next refresh.

**J3a.** Nurse Chanthasone opens the referral and scans the QRs. The EHR
**verifies** each DVC offline against that copy (STT-VER-001…009,
STT-KID-002), without contacting Thailand. Both verify, so it imports them as
FHIR `Immunization`s (`TrustDemoJ3HepB`, `TrustDemoJ3Bcg`) with provenance
(`TrustDemoJ3Verification`; STT-VER-007, STT-VER-008), replacing the reported
doses of J2. If a DVC fails (a tampered card, say), the EHR names the step and
the reason, the doses stay unverified, and the nurse decides by national
catch-up policy.

**J3b.** The Thai Hep B product matches nothing on the national schedule.
The EHR keeps Thailand's product coding and adds the schedule coding beside
it, from the national map (`TrustDemoProductToLaoEpi`). For the Hep B product
the map has no entry, so Nurse Chanthasone makes the clinical call that it is
the schedule's birth dose (`TrustDemoJ3Adjudication`), and her decision is
added to the map for the next clinic. The schedule (`TrustDemoLaoInfantSchedule`)
then runs: the birth doses count, and pentavalent 1, bOPV 1 and PCV 1 are due
at 6 weeks (`TrustDemoJ3Recommendation`). Khamla leaves with the date
(`TrustDemoJ3Reminder`). Over the year Somsack gets those doses and
measles-rubella at 9 months, in Lao PDR.

- *Pain point:* clinicians either distrust foreign paper and re-vaccinate, or trust it blindly; and countries name and package vaccines differently.
- *Enabler:* Thailand's key is on the shared WHO trust list, so any clinic checks it locally; the original code is kept and the national code added beside it.
- *Policy:* trust is decentralized: a Lao clinic verifies a Thai signature itself. Never overwrite another country's record.

### J4.0 — Crossing back: one family, one phone (Lao PDR, 12 months later)

**Precondition, as in J1:** Country B's DSC, under Country B's CSCA, is
already shared with the GDHCN, the Trust Anchor. That is what lets the
clinic in Thailand verify the link in J4.1.

**J4.0a.** The family plans a trip to Thailand. Bounmy's phone holds the
family wallet, with a profile for each of them. Somsack's summary
(`TrustDemoJ4Ips`) shows six doses: two from Thailand, four from Lao PDR.

**J4.0b.** For Somsack, Bounmy shares his record with a 4-digit passcode he
can say aloud, valid for 14 days. The portal records his consent
(`TrustDemoJ4Consent`), then does three things:

1. It assembles the IPS and Somsack's DVCs.
2. It encrypts them (STT-VHL-004, STT-VHL-007) behind a passcode-protected manifest with an expiry (STT-VHL-009).
3. It issues the link as an HCERT, with the VHL at key 5 (STT-VHL-001, STT-VHL-002), signed with Country B's DSC.

The QR holds only a pointer and a key: the record stays in Lao PDR.

- *Pain point:* many families share one smartphone, and photos or PDFs of records leak data and cannot be verified.
- *Enabler:* a household wallet on one phone with a summary per person; a Verifiable Health Link whose data stays home until the passcode is given.
- *Policy:* design for shared devices; data sovereignty: the record stays home until the family authorizes someone to open it.

### J4.1 — Crossing back: a Thai doctor sees the full history (Chiang Rai, 12 months later)

**Precondition, as in J3: the DID documents are already loaded.** The
clinic viewer's trust store is a cached copy of the GDHCN trust list,
including Country B's DSC DID document (STT-TRU-001, STT-TRU-002,
STT-TRU-005). The clinic refreshes it nightly or hourly, against about
weekly at the offline J3 clinic. It does not need to be online to verify:
verifying reads the cache and never fetches the list. A DSC published after
the last refresh fails the trust-list check (STT-VER-006), naming that reason.

Back where it began, Dr Anan sees Somsack at a primary care clinic in
Chiang Rai. Bounmy shows the QR on his phone and says the passcode. The
clinic viewer and the Lao gateway take five steps:

1. The viewer verifies the HCERT against Country B's DSC in its copy of the trust list.
2. It requests the manifest by ITI-YY5, signed with HTTP Message Signatures (STT-VHL-005, STT-VHL-006, STT-VHL-008).
3. The Lao gateway checks the passcode, the expiry and the consent, returns the manifest, and logs the access at home (`TrustDemoJ41Access`).
4. The viewer decrypts the IPS and DVCs (STT-VHL-007) (`TrustDemoJ41Received`).
5. It shows them to Dr Anan: every dose since the birth, viewed, never copied.

A wrong passcode is refused, and the attempt is still logged in Lao PDR
(`TrustDemoJ41WrongPasscode`). If the HCERT does not verify (for example,
Country B's DSC is missing from the cached list), there is no digital
verification. The clinic names the step and the reason (STT-VER-008), does not
follow the VHL, and Dr Anan treats whatever the family can show as he
would a paper record.

- *Pain point:* without the history, the doctor would repeat vaccines or have to guess.
- *Enabler:* the record is fetched live from Lao PDR, viewed without being copied, and an access log is kept at home.
- *Policy:* continuity of care across borders, with no central database, no international patient registry and no vendor lock-in.

## Questions for discussion

The VaxLink walkthrough closes with four policy questions:

1. **Identity for babies born abroad** (J1, J2b): how should national immunization systems handle temporary ids for cross-border infants before civil registration is complete?
2. **Where trust begins** (J2a, J3a): why should offline CHW devices store foreign cards as reported, not verified, rather than verify them in the field?
3. **Matching vaccines across countries** (J3b): when a monovalent vaccine is given abroad but the home schedule uses a combination (pentavalent), how should schedule rules count the doses still due?
4. **Cross-border access and audit** (J4.0b, J4.1): what agreements do countries need so that a clinician viewing a record abroad triggers an audit entry in the patient's home country?
