# smart-trust-demo-jv07
title: 'JV-07: journeys viewer, the header has a “Reset Simulation” button'
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

A style difference the owner marked **Fix** in the side-by-side review of [[smart-trust-demo-jv03]] (row D06, [review page](https://claude.ai/artifact/Nyaej36JQowq5wYcZxrXFV), 2026-11-11). Spec: `docs/proposals/journeys-viewer-parity/README.md` §1; reference `docs/proposals/journeys-viewer-parity/ref/01`.

**Today:** VaxLink's second bar has FHIR IG, IG source and Reset Simulation. The viewer has the first two only.

**Fix (upstream, cat-harness-tools `scripts/journeys/`, `assets/journeys.css`):** Add the button to the journey header. It clears what the page keeps in the browser (revealed What-ifs, gap-strip answers, presenter-note dismissal) and returns to the overview.

## Done when

- the header shows Reset Simulation and it clears the page's stored state;
- a screenshot beside the reference is attached to the PR.
