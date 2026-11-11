# smart-trust-demo-jv11
title: 'JV-11: journeys viewer, the journey map fits all eight moments on a desktop screen'
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

A style difference the owner marked **Fix** in the side-by-side review of [[smart-trust-demo-jv03]] (row D11, [review page](https://claude.ai/artifact/Nyaej36JQowq5wYcZxrXFV), 2026-11-11). Spec: `docs/proposals/journeys-viewer-parity/README.md` §1; reference `docs/proposals/journeys-viewer-parity/ref/05`.

**Today:** VaxLink's map columns are narrow enough that all eight moments fit at 1400px. The viewer's columns are wider, chapter names are cut (“Found at…”, “Made o…”) and the last column runs off the edge.

**Fix (upstream, cat-harness-tools `scripts/journeys/`, `assets/journeys.css`):** Size the map's columns as VaxLink does (fixed narrow moment columns, chapter header spanning its moments); keep horizontal scroll only below desktop width.

## Done when

- at 1400px the map shows J1 to J4.1 and every chapter name in full;
- a screenshot beside the reference is attached to the PR.
