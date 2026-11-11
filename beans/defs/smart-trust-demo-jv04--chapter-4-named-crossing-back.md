# smart-trust-demo-jv04
title: 'JV-04: journeys viewer, chapter 4 is named “Crossing back”'
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

A style difference the owner marked **Fix** in the side-by-side review of [[smart-trust-demo-jv03]] (row D02, [review page](https://claude.ai/artifact/Nyaej36JQowq5wYcZxrXFV), 2026-11-11). Spec: `docs/proposals/journeys-viewer-parity/README.md` §1; reference `docs/proposals/journeys-viewer-parity/ref/01, ref/06`.

**Today:** VaxLink calls chapter 4 “Crossing back”. The viewer uses “One family, one phone, a history abroad”, which is cut off in the walkthrough progress bar, the journey map header and the persona curve.

**Fix (upstream, cat-harness-tools `scripts/journeys/`, `assets/journeys.css`):** Give the chapter a short label in the graph (the `user-scenario` chapter node, not a hard-coded string) and use it wherever a chapter name is shown in a tight space; the long title can stay on the chapter's own page.

## Done when

- the progress bar, map header and persona curve show “Crossing back” (or the graph's short label) uncut at 1400px;
- a screenshot beside the reference is attached to the PR.
