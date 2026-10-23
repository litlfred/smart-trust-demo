<!-- GENERATED from smart-trust-demo/processes/content/j4-1-vhl-point-of-care.bpmn by cat-harness-tools/scripts/bpmn-checklist.ts. Do not edit: change the diagram and regenerate (bun run cat bpmn:checklist). -->

# Checklist — J4.1 Read a family member's records at the point of care abroad

> **Generated, and not the authority.** This is `smart-trust-demo/processes/content/j4-1-vhl-point-of-care.bpmn` (process `Process_J41VhlFetch`) walked as a state machine. The diagram and the workflow engine decide; this list only reads them. Follow the `next:` line of each step rather than the order on the page, and record each step with the call it names, so the engine's committed state — not this list — says which edge was taken.

J4.1.

## Begin — Chanthala needs care abroad (`Start`)

- Begin here.
- Call `workflow_start` with `process: "Process_J41VhlFetch"` and the subject this run is about; keep the instance id it returns.
- next: → `Task_Open` (Show Chanthala's VHL QR)

### 1. Show Chanthala's VHL QR (`Task_Open`)

- Who: the `Family phone` lane (role `family-phone`).
- Skill: `wallet-hold-vhl`.
- Record it: `workflow_complete` with `node: "Task_Open"`.
- next: → `Task_Scan` (Scan the QR and enter the passcode Mali gives)

### 2. Scan the QR and enter the passcode Mali gives (`Task_Scan`)

- Who: the `Point-of-care provider` lane (role `poc-provider`).
- Record it: `workflow_complete` with `node: "Task_Scan"`.
- next: → `Task_Verify` (Verify the HCERT and read the VHL at key 5)

### 3. Verify the HCERT and read the VHL at key 5 (`Task_Verify`)

- Who: the `Point-of-care receiver` lane (role `poc-receiver`).
- Skill: `hcert-verify`.
- What: STT-VER-001 against Country B's DSC on the trust list; VHL expiry (STT-VHL-009).
- Record it: `workflow_complete` with `node: "Task_Verify"`.
- next: → `Task_Fetch` (Request the manifest (ITI-YY5), signed)

### 4. Request the manifest (ITI-YY5), signed (`Task_Fetch`)

- Who: the `Point-of-care receiver` lane (role `poc-receiver`).
- Skill: `vhl-receive`.
- What: STT-VHL-005, STT-VHL-006, STT-VHL-008; the host does the HTTP, the library builds and reads (STT-VHL-010).
- Record it: `workflow_complete` with `node: "Task_Fetch"`.
- next: → `Task_Decrypt` (Decrypt the IPS and DVCs)

### 5. Decrypt the IPS and DVCs (`Task_Decrypt`)

- Who: the `Point-of-care receiver` lane (role `poc-receiver`).
- Skill: `vhl-receive`.
- What: JWE dir/A256GCM (STT-VHL-007).
- Record it: `workflow_complete` with `node: "Task_Decrypt"`.
- next: → `Task_Review` (Review history, allergies and vaccinations)

### 6. Review history, allergies and vaccinations (`Task_Review`)

- Who: the `Point-of-care provider` lane (role `poc-provider`).
- Record it: `workflow_complete` with `node: "Task_Review"`.
- next: → `End` (Chanthala is treated with her records)

## Done — Chanthala is treated with her records (`End`)

- The instance completes here. `workflow_next` then reports nothing enabled — that, not this line, is the record of completion.
