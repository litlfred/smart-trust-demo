<!-- GENERATED from smart-trust-demo/processes/content/j1-birth-dose-dvc.bpmn by cat-harness-tools/scripts/bpmn-checklist.ts. Do not edit: change the diagram and regenerate (bun run cat bpmn:checklist). -->

# Checklist — J1 Issue the newborn's birth-dose DVCs in Country A

> **Generated, and not the authority.** This is `smart-trust-demo/processes/content/j1-birth-dose-dvc.bpmn` (process `Process_J1BirthDoseDvc`) walked as a state machine. The diagram and the workflow engine decide; this list only reads them. Follow the `next:` line of each step rather than the order on the page, and record each step with the call it names, so the engine's committed state — not this list — says which edge was taken.

J1, Cross-border birth and initial vaccination.

## Begin — A Country B family's child is born in Country A (`Start`)

- Begin here.
- Call `workflow_start` with `process: "Process_J1BirthDoseDvc"` and the subject this run is about; keep the instance id it returns.
- next: → `Task_Vaccinate` (Give Hep B and BCG birth doses and record them)

### 1. Give Hep B and BCG birth doses and record them (`Task_Vaccinate`)

- Who: the `Birth clinic vaccinator` lane (role `birth-clinic-vaccinator`).
- What: The vaccinator records each dose (vaccine product, date, batch) in the hospital system, on its dose form, through smart-base's reusable SDC data-capture process: complete-sdc-questionnaire, then extract-questionnaire-response, which writes the Immunization each DVC is built from.
- A subprocess (`Process_QuestionnaireDataCapture`): `workflow_next` reports its own steps; complete those — this call activity itself is not completable.
- next: → `Task_Payload` (Build one DVCMinPreQual payload per dose)

### 2. Build one DVCMinPreQual payload per dose (`Task_Payload`)

- Who: the `Birth clinic issuing system` lane (role `birth-clinic-system`).
- Skill: `hcert-select-payload`.
- What: One immunization event per DVC (STT-PAY-003), typed DVCMin models (STT-PAY-001, STT-PAY-002), nationality alpha-3 XXK (STT-PAY-007), subject with no identity document (STT-PAY-005); subclaim -6 in the development range, opted into explicitly (STT-SEL-003).
- Record it: `workflow_complete` with `node: "Task_Payload"`.
- next: → `Task_Prepare` (Prepare: CWT claims and the COSE Sig_structure)

### 3. Prepare: CWT claims and the COSE Sig_structure (`Task_Prepare`)

- Who: the `Birth clinic issuing system` lane (role `birth-clinic-system`).
- Skill: `hcert-build-cwt`.
- What: iss XR, iat, exp inside the DSC validity (STT-CWT-001 to 005); kid from the DSC (STT-KID-001); the library returns the bytes to sign (STT-ISS-004).
- Record it: `workflow_complete` with `node: "Task_Prepare"`.
- next: → `Task_Sign` (Sign the bytes with XXR's DSC key)

### 4. Sign the bytes with XXR's DSC key (`Task_Sign`)

- Who: the `Issuer signing key` lane (role `issuer-key`).
- Skill: `hcert-sign-cose`.
- What: ES256 or PS256 (STT-COS-002) in the HSM, KMS or Keystore; the library never holds the private key (STT-COS-006).
- Record it: `workflow_complete` with `node: "Task_Sign"`.
- next: → `Task_Finish` (Finish: COSE_Sign1, deflate, Base45, HC1:)

### 5. Finish: COSE_Sign1, deflate, Base45, HC1: (`Task_Finish`)

- Who: the `Birth clinic issuing system` lane (role `birth-clinic-system`).
- Skill: `hcert-prefix-context`.
- What: STT-COS-001, STT-ZIP-001, STT-B45-001, STT-HC1-001; QR-ready text, no QR encoding in the library (STT-QR-001).
- Record it: `workflow_complete` with `node: "Task_Finish"`.
- next: → `Task_Print` (Print the paper DVC, one QR per dose)

### 6. Print the paper DVC, one QR per dose (`Task_Print`)

- Who: the `Birth clinic vaccinator` lane (role `birth-clinic-vaccinator`).
- Skill: `hand-over-credential`.
- Record it: `workflow_complete` with `node: "Task_Print"`.
- next: → `End` (The caregiver holds two signed paper DVCs)

## Done — The caregiver holds two signed paper DVCs (`End`)

- The instance completes here. `workflow_next` then reports nothing enabled — that, not this line, is the record of completion.
