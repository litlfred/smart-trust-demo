<!-- GENERATED from smart-trust-demo/processes/content/j3-clinic-verification-schedule.bpmn by cat-harness-tools/scripts/bpmn-checklist.ts. Do not edit: change the diagram and regenerate (bun run cat bpmn:checklist). -->

# Checklist — J3 Verify, import and schedule at the home clinic

> **Generated, and not the authority.** This is `smart-trust-demo/processes/content/j3-clinic-verification-schedule.bpmn` (process `Process_J3ClinicVerification`) walked as a state machine. The diagram and the workflow engine decide; this list only reads them. Follow the `next:` line of each step rather than the order on the page, and record each step with the call it names, so the engine's committed state — not this list — says which edge was taken.

J3, Clinic verification and schedule generation, in Country B.

## Begin — Family arrives with the referral and the paper DVCs (`Start`)

- Begin here.
- Call `workflow_start` with `process: "Process_J3ClinicVerification"` and the subject this run is about; keep the instance id it returns.
- next: → `Task_Scan` (Scan the QRs and open the referral)

### 1. Scan the QRs and open the referral (`Task_Scan`)

- Who: the `Home clinic provider` lane (role `home-clinic-provider`).
- Skill: `receiver-scan-credential`.
- Record it: `workflow_complete` with `node: "Task_Scan"`.
- next: → `Task_Verify` (Verify each HCERT against the trust list)

### 2. Verify each HCERT against the trust list (`Task_Verify`)

- Who: the `Home clinic EHR` lane (role `home-clinic-ehr`).
- Skill: `hcert-verify`.
- What: HcertVerifier.verify: STT-VER-001 order, no payload before the signature (STT-VER-002), every DSC with the kid tried (STT-KID-002), EKU (STT-VER-004), time with an injected clock (STT-VER-005), typed result naming step and reason (STT-VER-008), fully offline (STT-VER-009); several payloads per HCERT
- Record it: `workflow_complete` with `node: "Task_Verify"`.
- next: → `Gateway_Verified` (Every DVC verified?)

### Decide — Every DVC verified? (`Gateway_Verified`)

- Call `workflow_complete` with `node: "Gateway_Verified"` and `outcome` set to the label that holds:
  - «yes» → `Task_Import` (Import the doses as FHIR Immunization resources)
  - «no» → `Task_Unverified` (Note the failure; decide doses by policy)

### 3. Import the doses as FHIR Immunization resources (`Task_Import`)

- Who: the `Home clinic EHR` lane (role `home-clinic-ehr`).
- Skill: `ehr-import-immunization`.
- Record it: `workflow_complete` with `node: "Task_Import"`.
- next: → `Task_Map` (Add national codes beside foreign ones)

### 4. Note the failure; decide doses by policy (`Task_Unverified`)

- Who: the `Home clinic provider` lane (role `home-clinic-provider`).
- What: Record the failure reason; decide doses by national policy.
- Record it: `workflow_complete` with `node: "Task_Unverified"`.
- next: → `Task_Plan` (Give due doses and book the next visit)

### 5. Add national codes beside foreign ones (`Task_Map`)

- Who: the `Home clinic EHR` lane (role `home-clinic-ehr`).
- Skill: `map-vaccine-codes`.
- What: Add the national schedule code beside the foreign vaccine code.
- Record it: `workflow_complete` with `node: "Task_Map"`.
- next: → `Task_Schedule` (Evaluate the national schedule)

### 6. Give due doses and book the next visit (`Task_Plan`)

- Who: the `Home clinic provider` lane (role `home-clinic-provider`).
- Skill: `review-decision-support-guidance`.
- What: The nurse acts on the schedule evaluation's guidance (TD.DT.04, which doses are due and from when) the way smart-base's act-on-decision-support process does it: accept or decline each proposed dose, one tap each.
- Record it: `workflow_complete` with `node: "Task_Plan"`.
- next: → `End` (The child is on Country B's schedule)

### 7. Evaluate the national schedule (`Task_Schedule`)

- Who: the `Home clinic EHR` lane (role `home-clinic-ehr`).
- Skill: `schedule-evaluate`.
- What: PlanDefinition/$apply over the imported Immunizations, read by their national schedule codes: the Hep B and BCG birth doses count; the 6-week doses (pentavalent, bOPV, PCV) are due, and a reminder Task is created for that date.
- Record it: `workflow_complete` with `node: "Task_Schedule"`.
- next: → `Task_Plan` (Give due doses and book the next visit)

## Done — The child is on Country B's schedule (`End`)

- The instance completes here. `workflow_next` then reports nothing enabled — that, not this line, is the record of completion.
