# smart-trust-demo-jv16
title: 'JV-16: journeys viewer, above the device: back button, “You are looking at…”, device label'
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

A style difference the owner marked **Fix** in the side-by-side review of [[smart-trust-demo-jv03]] (row D20, [review page](https://claude.ai/artifact/Nyaej36JQowq5wYcZxrXFV), 2026-11-11). Spec: `docs/proposals/journeys-viewer-parity/README.md` §1; reference `docs/proposals/journeys-viewer-parity/ref/10, ref/11, ref/12`.

**Today:** VaxLink shows a small red “← Back to the user journey” button, “You are looking at what Nurse Chanthason sees at this moment.”, and a “Tablet / Web 1024px (OHS Player Facility Config)” label with Expand on the right. The viewer shows a big screen title and description, a back button, “Screen source”, and a person chip above the device.

**Fix (upstream, cat-harness-tools `scripts/journeys/`, `assets/journeys.css`):** Match VaxLink's compact header; the title and description can move into the Moments card below the device or the presenter note.

## Done when

- S1, S4 and S8 match the header of ref/10 to ref/12;
- a screenshot beside the reference is attached to the PR.
