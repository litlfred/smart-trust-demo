# smart-trust-demo-jv15
title: 'JV-15: journeys viewer, the device demo has VaxLink''s stage bar'
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

A style difference the owner marked **Fix** in the side-by-side review of [[smart-trust-demo-jv03]] (row D19, [review page](https://claude.ai/artifact/Nyaej36JQowq5wYcZxrXFV), 2026-11-11). Spec: `docs/proposals/journeys-viewer-parity/README.md` §1; reference `docs/proposals/journeys-viewer-parity/ref/10, ref/11, ref/12`.

**Today:** VaxLink's device demo has a two-row “Journey stage:” bar of pills (J1 Birth Abroad & Printed DVC QR Cards … J4.1 Foreign Clinic VHL Viewer & Audit Trace) inside the app frame, above the presenter note; the current stage is a filled cobalt pill. The viewer has a strip of S1 to S8 cards below the presenter note.

**Fix (upstream, cat-harness-tools `scripts/journeys/`, `assets/journeys.css`):** Render the stage bar as pills in the header, labelled by journey step code and screen title.

## Done when

- S1, S4 and S8 match ref/10 to ref/12 in the stage bar;
- a screenshot beside the reference is attached to the PR.
