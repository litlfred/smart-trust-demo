<!-- GENERATED from smart-trust-demo/processes/content/j4-1-vhl-point-of-care.bpmn by cat-harness-tools/scripts/bpmn-checklist.ts. Do not edit: change the diagram and regenerate (bun run cat bpmn:checklist). -->

# Checklist — J4.1 Read a family member's records at the point of care abroad

> **Generated, and not the authority.** This is `smart-trust-demo/processes/content/j4-1-vhl-point-of-care.bpmn` (process `Process_J41VhlFetch`) walked as a state machine. The diagram and the workflow engine decide; this list only reads them. Follow the `next:` line of each step rather than the order on the page, and record each step with the call it names, so the engine's committed state — not this list — says which edge was taken.

J4.1.

## Begin — A child of the family needs care abroad (`Start`)

- Begin here.
- Call `workflow_start` with `process: "Process_J41VhlFetch"` and the subject this run is about; keep the instance id it returns.
- next: → `Task_Open` (Show the child's VHL QR)

### 1. Show the child's VHL QR (`Task_Open`)

- Who: the `Family phone` lane (role `family-phone`).
- Skill: `wallet-hold-vhl`.
- Record it: `workflow_complete` with `node: "Task_Open"`.
- next: → `Task_Scan` (Scan the QR and enter the passcode the caregiver says)

### 2. Scan the QR and enter the passcode the caregiver says (`Task_Scan`)

- Who: the `Point-of-care provider` lane (role `poc-provider`).
- Record it: `workflow_complete` with `node: "Task_Scan"`.
- next: → `Task_Verify` (Verify the HCERT and read the VHL at key 5)

### 3. Verify the HCERT and read the VHL at key 5 (`Task_Verify`)

- Who: the `Point-of-care receiver` lane (role `poc-receiver`).
- Skill: `hcert-verify`.
- What: STT-VER-001 against Country B's DSC on the trust list the preconditions establish; VHL expiry (STT-VHL-009).
- Record it: `workflow_complete` with `node: "Task_Verify"`.
- next: → `Gateway_Verified` (HCERT verified?)

### Decide — HCERT verified? (`Gateway_Verified`)

- Call `workflow_complete` with `node: "Gateway_Verified"` and `outcome` set to the label that holds:
  - «yes» → `Task_Fetch` (Request the manifest (ITI-YY5), signed)
  - «no» → `Task_Unverified` (No digital verification: treat the records like paper)

### 4. Request the manifest (ITI-YY5), signed (`Task_Fetch`)

- Who: the `Point-of-care receiver` lane (role `poc-receiver`).
- Skill: `vhl-receive`.
- What: STT-VHL-005, STT-VHL-006, STT-VHL-008; the host does the HTTP, the library builds and reads (STT-VHL-010).
- Record it: `workflow_complete` with `node: "Task_Fetch"`.
- next: → `Task_Release` (Check the passcode, return the manifest and log the access)

### 5. No digital verification: treat the records like paper (`Task_Unverified`)

- Who: the `Point-of-care provider` lane (role `poc-provider`).
- What: The HCERT failed verification.
- Record it: `workflow_complete` with `node: "Task_Unverified"`.
- next: → `Task_Review` (Review history, allergies and vaccinations)

### 6. Check the passcode, return the manifest and log the access (`Task_Release`)

- Who: the `National health portal` lane (role `national-portal`).
- Skill: `portal-serve-manifest`.
- What: The home country's portal hosts the manifest (ITI-YY5).
- Record it: `workflow_complete` with `node: "Task_Release"`.
- next: → `Task_Decrypt` (Decrypt the IPS and DVCs)

### 7. Review history, allergies and vaccinations (`Task_Review`)

- Who: the `Point-of-care provider` lane (role `poc-provider`).
- Record it: `workflow_complete` with `node: "Task_Review"`.
- next: → `End` (The child is treated with the full record)

### 8. Decrypt the IPS and DVCs (`Task_Decrypt`)

- Who: the `Point-of-care receiver` lane (role `poc-receiver`).
- Skill: `vhl-receive`.
- What: JWE dir/A256GCM (STT-VHL-007).
- Record it: `workflow_complete` with `node: "Task_Decrypt"`.
- next: → `Task_Review` (Review history, allergies and vaccinations)

## Done — The child is treated with the full record (`End`)

- The instance completes here. `workflow_next` then reports nothing enabled — that, not this line, is the record of completion.
