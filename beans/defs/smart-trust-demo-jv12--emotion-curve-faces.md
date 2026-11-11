# smart-trust-demo-jv12
title: 'JV-12: journeys viewer, the persona emotion curve has faces on its axis'
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

A style difference the owner marked **Fix** in the side-by-side review of [[smart-trust-demo-jv03]] (row D13, [review page](https://claude.ai/artifact/Nyaej36JQowq5wYcZxrXFV), 2026-11-11). Spec: `docs/proposals/journeys-viewer-parity/README.md` §1; reference `docs/proposals/journeys-viewer-parity/ref/06`.

**Today:** VaxLink labels the vertical axis of “How Khamla feels along the way” with small happy, neutral and sad faces. The viewer shows faint empty circles there.

**Fix (upstream, cat-harness-tools `scripts/journeys/`, `assets/journeys.css`):** Draw the three faces (the same icons as the emotion badges) on the axis.

## Done when

- every persona page's curve shows the three faces;
- a screenshot beside the reference is attached to the PR.
