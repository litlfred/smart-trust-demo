# smart-trust-demo-jv14
title: 'JV-14: journeys viewer, the table sheets start with a Cover sheet'
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

A style difference the owner marked **Fix** in the side-by-side review of [[smart-trust-demo-jv03]] (row D17, [review page](https://claude.ai/artifact/Nyaej36JQowq5wYcZxrXFV), 2026-11-11). Spec: `docs/proposals/journeys-viewer-parity/README.md` §1; reference `docs/proposals/journeys-viewer-parity/ref/09`.

**Today:** VaxLink's table sheets start with a Cover: Country, Delegation, Table and Facilitator fields, the scope promise, and the three ways to start. The viewer starts at Sheet 1.

**Fix (upstream, cat-harness-tools `scripts/journeys/`, `assets/journeys.css`):** Add the cover sheet, drawn from the workshop node (scope promise, substitution patterns).

## Done when

- sheets/ starts with the Cover and it prints on its own A3 page;
- a screenshot beside the reference is attached to the PR.
