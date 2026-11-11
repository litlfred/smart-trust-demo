# smart-trust-demo-jv09
title: 'JV-09: journeys viewer, the policy questions card uses VaxLink''s rows'
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

A style difference the owner marked **Fix** in the side-by-side review of [[smart-trust-demo-jv03]] (row D08, [review page](https://claude.ai/artifact/Nyaej36JQowq5wYcZxrXFV), 2026-11-11). Spec: `docs/proposals/journeys-viewer-parity/README.md` §1; reference `docs/proposals/journeys-viewer-parity/ref/02, ref/03`.

**Today:** In the walkthrough's Policy questions card VaxLink's rows are “Forces / Cost driver / If it is missing”, each with a small icon. The viewer's rows are “Decision rights / Legal basis / Substitution patterns / Cost drivers” with coloured pills.

**Fix (upstream, cat-harness-tools `scripts/journeys/`, `assets/journeys.css`):** Render the card's footer as the three VaxLink rows with their icons; the graph's decision-right, legal-basis, substitution and cost-driver edges map onto them (Forces = decision rights + legal basis, Cost driver, If it is missing = substitution pattern).

## Done when

- the card on J1 and J3a matches ref/02 and ref/03;
- a screenshot beside the reference is attached to the PR.
