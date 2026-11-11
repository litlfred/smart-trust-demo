# smart-trust-demo-jv17
title: 'JV-17: journeys viewer, the device frame has a status bar'
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

A style difference the owner marked **Fix** in the side-by-side review of [[smart-trust-demo-jv03]] (row D21, [review page](https://claude.ai/artifact/Nyaej36JQowq5wYcZxrXFV), 2026-11-11). Spec: `docs/proposals/journeys-viewer-parity/README.md` §1; reference `docs/proposals/journeys-viewer-parity/ref/10, ref/11, ref/12`.

**Today:** VaxLink's tablet frame has a dark status bar inside it: “OHS Facility Client v2.4.1 … 10:14 AM” with signal and battery icons. The viewer's frame has none.

**Fix (upstream, cat-harness-tools `scripts/journeys/`, `assets/journeys.css`):** Add the status bar to the device frame (app name and version from the screen node).

## Done when

- every device screen shows the status bar;
- a screenshot beside the reference is attached to the PR.
