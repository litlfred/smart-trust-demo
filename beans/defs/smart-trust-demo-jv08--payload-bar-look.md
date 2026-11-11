# smart-trust-demo-jv08
title: 'JV-08: journeys viewer, the payload bar looks like VaxLink''s'
status: todo
type: feature
priority: normal
tags:
    - upstream
    - journeys-viewer-parity
    - style
created_at: 2026-11-11T09:20:00Z
updated_at: 2026-11-11T09:20:00Z
---

A style difference the owner marked **Fix** in the side-by-side review of [[smart-trust-demo-jv03]] (row D07, [review page](https://claude.ai/artifact/Nyaej36JQowq5wYcZxrXFV), 2026-11-11). Spec: `docs/proposals/journeys-viewer-parity/README.md` §1; reference `docs/proposals/journeys-viewer-parity/ref/01, ref/13`.

**Today:** VaxLink's bar at the bottom of every page is dark and monospace: “FHIR R4 & WHO GDHCN PAYLOAD INSPECTOR · Active Stage: J3a · DEV Key: 916ffa…(XXR)”, with “Click to inspect raw FHIR / CBOR payload” on the right. The viewer's bar says “FHIR PAYLOAD INSPECTOR · N resources at this moment” in the body font. Showing it on every page is [[smart-trust-demo-jv02]]; this bean is only its look.

**Fix (upstream, cat-harness-tools `scripts/journeys/`, `assets/journeys.css`):** Restyle `jp-drawer-bar`: mono type, the stage chip, the trust-list key chip, the same right-hand hint.

## Done when

- the bar matches ref/01 and ref/13 in type, labels and chips;
- a screenshot beside the reference is attached to the PR.
