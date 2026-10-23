---
# smart-trust-demo-oi01
title: 'OI-01: smart-trust-phw requirement receive-a-vhl names the Issuer as its actor'
status: todo
type: bug
priority: normal
tags:
    - open-issue
    - upstream
created_at: 2026-10-23T08:40:00Z
updated_at: 2026-10-23T08:40:00Z
---

In smart-trust-phw (input/fsh/requirements/requirements.fsh, at fd3b548, the same in WorldHealthOrganization/smart-trust-phw main), the Requirements instance `receive-a-vhl` ("Receive VHL or VDHC": "Is able to receive a VHL authorization mechanism or a VDHC from a Holder") gives `actor = Canonical(Issuer)`. Its counterpart `provide-a-vhl-to-a-receiver` names the Holder, and the description is the Receiver's capability, so the actor should be `Receiver`.

The journeys follow the description: the CHW app (J2), the home clinic EHR (J3) and the hospital system abroad (J4.1) receive the VDHC or VHL from the Holder as Receivers.

Also: smart-trust-phw's personas.md and scenarios.md are template placeholders ("[insert health domain here]"); this repository's personas and user scenarios for J1 to J4 could fill them.

## Resolution

Fixed and pre-adopted in litlfred/smart-trust-phw#1 (merged 2026-10-23: actor = Canonical(Receiver)). A WHO issue on WorldHealthOrganization/smart-trust-phw is drafted in docs/upstream/who-smart-trust-phw-receive-a-vhl.md for the owner to file; the PR to WHO follows when the owner asks.

## Sources

- smart-trust-phw input/fsh/requirements/requirements.fsh, instances provide-a-vhl-to-a-receiver and receive-a-vhl
- smart-trust-phw input/fsh/actors/actors.fsh
