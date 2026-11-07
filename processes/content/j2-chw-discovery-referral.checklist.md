<!-- GENERATED from smart-trust-demo/processes/content/j2-chw-discovery-referral.bpmn by cat-harness-tools/scripts/bpmn-checklist.ts. Do not edit: change the diagram and regenerate (bun run cat bpmn:checklist). -->

# Checklist — J2 Discover and refer an unregistered infant in Country B

> **Generated, and not the authority.** This is `smart-trust-demo/processes/content/j2-chw-discovery-referral.bpmn` (process `Process_J2ChwDiscovery`) walked as a state machine. The diagram and the workflow engine decide; this list only reads them. Follow the `next:` line of each step rather than the order on the page, and record each step with the call it names, so the engine's committed state — not this list — says which edge was taken.

J2, Return home, CHW discovery and referral.

## Begin — Home visit finds an unregistered infant (`Start`)

- Begin here.
- Call `workflow_start` with `process: "Process_J2ChwDiscovery"` and the subject this run is about; keep the instance id it returns.
- next: → `Task_Show` (Show the paper DVCs from Country A)

### 1. Show the paper DVCs from Country A (`Task_Show`)

- Who: the `Caregiver` lane (role `caregiver`).
- Skill: `holder-present-credential`.
- Record it: `workflow_complete` with `node: "Task_Show"`.
- next: → `Task_Scan` (Scan each QR with the CHW app)

### 2. Scan each QR with the CHW app (`Task_Scan`)

- Who: the `Community health worker` lane (role `community-health-worker`).
- Skill: `receiver-scan-credential`.
- Record it: `workflow_complete` with `node: "Task_Scan"`.
- next: → `Task_Read` (Read each DVC unverified (triage))

### 3. Read each DVC unverified (triage) (`Task_Read`)

- Who: the `CHW app` lane (role `chw-app`).
- Skill: `hcert-verify`.
- What: read-unverified (STT-VER-011): strip HC1:, Base45, inflate within limits (STT-B45-002, STT-ZIP-002), bounded CBOR (STT-CBR-003), payloads read but flagged unverified; no trust list needed, fully offline.
- Record it: `workflow_complete` with `node: "Task_Read"`.
- next: → `Task_Register` (Add the infant; save doses as reported)

### 4. Add the infant; save doses as reported (`Task_Register`)

- Who: the `CHW app` lane (role `chw-app`).
- Skill: `chw-register-infant`.
- What: Add the infant to the household; save the doses as reported, not verified.
- A subprocess (`Process_QuestionnaireDataCapture`): `workflow_next` reports its own steps; complete those — this call activity itself is not completable.
- next: → `Task_Refer` (Create a referral to the home clinic for verification)

### 5. Create a referral to the home clinic for verification (`Task_Refer`)

- Who: the `CHW app` lane (role `chw-app`).
- Skill: `chw-refer`.
- Record it: `workflow_complete` with `node: "Task_Refer"`.
- next: → `Task_Slip` (Explain the referral to the family)

### 6. Explain the referral to the family (`Task_Slip`)

- Who: the `Community health worker` lane (role `community-health-worker`).
- Record it: `workflow_complete` with `node: "Task_Slip"`.
- next: → `End` (Family has a referral; the record syncs when online)

## Done — Family has a referral; the record syncs when online (`End`)

- The instance completes here. `workflow_next` then reports nothing enabled — that, not this line, is the record of completion.
