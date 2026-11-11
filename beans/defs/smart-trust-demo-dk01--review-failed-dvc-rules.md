---
# smart-trust-demo-dk01
title: 'DK-01: owner review of the DAK rules for failed DVCs'
status: todo
type: task
priority: normal
tags:
    - this-repository
created_at: 2026-11-05T12:00:00Z
updated_at: 2026-11-05T12:00:00Z
---

The BPMN says only "decide doses by national policy" for a DVC that fails verification. Decision table TD.DT.01 (`processes/content/decisions/`) turns that into outcomes: verified, kept as reported-unverified, rejected, or not read. Those outcomes are an illustrative reading, not a stated policy, and the Decision-support Logic page says so (owner, 2026-11-05: "B. Make a bean to review").

Related gap found at the same time: `TrustDemoOnesaImmunization` requires a national schedule code, so it cannot hold a verified dose that TD.DT.02 leaves unmapped.

## Done when

- [ ] The owner has confirmed or changed each TD.DT.01 outcome for a failed DVC
- [ ] TD.DT.01, the dictionary and the page follow that decision, and drop "illustrative" where the rule is now policy
- [ ] The unmapped-dose case has a decided representation (profile relaxed, or the dose kept outside it)
