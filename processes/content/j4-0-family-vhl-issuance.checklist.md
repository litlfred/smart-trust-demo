<!-- GENERATED from smart-trust-demo/processes/content/j4-0-family-vhl-issuance.bpmn by cat-harness-tools/scripts/bpmn-checklist.ts. Do not edit: change the diagram and regenerate (bun run cat bpmn:checklist). -->

# Checklist — J4.0 Issue the family's records to one phone as VHLs

> **Generated, and not the authority.** This is `smart-trust-demo/processes/content/j4-0-family-vhl-issuance.bpmn` (process `Process_J40FamilyVhl`) walked as a state machine. The diagram and the workflow engine decide; this list only reads them. Follow the `next:` line of each step rather than the order on the page, and record each step with the call it names, so the engine's committed state — not this list — says which edge was taken.

J4.0, Outbound family travel, "One Family, One Phone".

## Begin — Family plans to travel abroad (`Start`)

- Begin here.
- Call `workflow_start` with `process: "Process_J40FamilyVhl"` and the subject this run is about; keep the instance id it returns.
- next: → `Task_Request` (Choose who to share, with a passcode and an expiry)

### 1. Choose who to share, with a passcode and an expiry (`Task_Request`)

- Who: the `Caregiver` lane (role `caregiver`).
- Skill: `holder-consent-to-share`.
- Record it: `workflow_complete` with `node: "Task_Request"`.
- next: → `Task_Assemble` (Assemble each member's IPS and DVCs)

### 2. Assemble each member's IPS and DVCs (`Task_Assemble`)

- Who: the `National health portal` lane (role `national-portal`).
- Skill: `portal-assemble-records`.
- Record it: `workflow_complete` with `node: "Task_Assemble"`.
- next: → `Task_Share` (Encrypt, publish a passcode manifest)

### 3. Encrypt, publish a passcode manifest (`Task_Share`)

- Who: the `National health portal` lane (role `national-portal`).
- Skill: `vhl-share`.
- What: Encrypt the documents and publish a passcode-protected manifest.
- Record it: `workflow_complete` with `node: "Task_Share"`.
- next: → `Task_Prepare` (Prepare the HCERT carrying the VHL at key 5)

### 4. Prepare the HCERT carrying the VHL at key 5 (`Task_Prepare`)

- Who: the `National health portal` lane (role `national-portal`).
- Skill: `hcert-build-cwt`.
- What: VHL payload as a CBOR map at key 5 (STT-VHL-002); two-phase signing (STT-ISS-004).
- Record it: `workflow_complete` with `node: "Task_Prepare"`.
- next: → `Task_Sign` (Sign with Country B's DSC key)

### 5. Sign with Country B's DSC key (`Task_Sign`)

- Who: the `Issuer signing key` lane (role `issuer-key`).
- Skill: `hcert-sign-cose`.
- Record it: `workflow_complete` with `node: "Task_Sign"`.
- next: → `Task_Finish` (Finish the HC1 QR text)

### 6. Finish the HC1 QR text (`Task_Finish`)

- Who: the `National health portal` lane (role `national-portal`).
- Skill: `hcert-prefix-context`.
- Record it: `workflow_complete` with `node: "Task_Finish"`.
- next: → `Task_Store` (Store each member's VHL QR on the phone)

### 7. Store each member's VHL QR on the phone (`Task_Store`)

- Who: the `Family phone` lane (role `family-phone`).
- Skill: `wallet-hold-vhl`.
- What: Store one VHL QR per member on the shared phone.
- Record it: `workflow_complete` with `node: "Task_Store"`.
- next: → `End` (One phone, one QR per family member)

## Done — One phone, one QR per family member (`End`)

- The instance completes here. `workflow_next` then reports nothing enabled — that, not this line, is the record of completion.
