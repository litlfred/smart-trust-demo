# smart-trust-demo-jv10
title: 'JV-10: journeys viewer, “See what … sees” is a full-width button in the right column'
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

A style difference the owner marked **Fix** in the side-by-side review of [[smart-trust-demo-jv03]] (row D09, [review page](https://claude.ai/artifact/Nyaej36JQowq5wYcZxrXFV), 2026-11-11). Spec: `docs/proposals/journeys-viewer-parity/README.md` §1; reference `docs/proposals/journeys-viewer-parity/ref/02, ref/03`.

**Today:** VaxLink puts “See what Dr. Anan sees (screen S1)” as a full-width button at the bottom of the walkthrough's right column, under the facilitator cue. The viewer shows a small chip inside the left card, under the headline.

**Fix (upstream, cat-harness-tools `scripts/journeys/`, `assets/journeys.css`):** Move the link to the right column's foot and style it as VaxLink's button.

## Done when

- every walkthrough step with a screen shows the button where ref/02 has it;
- a screenshot beside the reference is attached to the PR.
