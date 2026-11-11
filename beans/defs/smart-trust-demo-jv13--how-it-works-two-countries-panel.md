# smart-trust-demo-jv13
title: 'JV-13: journeys viewer, How it works opens with the two-countries architecture panel'
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

A style difference the owner marked **Fix** in the side-by-side review of [[smart-trust-demo-jv03]] (row D14, [review page](https://claude.ai/artifact/Nyaej36JQowq5wYcZxrXFV), 2026-11-11). Spec: `docs/proposals/journeys-viewer-parity/README.md` §1; reference `docs/proposals/journeys-viewer-parity/ref/07`.

**Today:** VaxLink's How it works opens with “Architecture: two countries on one trust foundation”: Thailand and Lao PDR side by side, one row per DPI-H RA layer (point-of-service, reusable components, shared data, foundational, interoperability standards), each system linked to its IG page and tagged with its moments, over a GDHCN foundation band. The four big ideas come last. The viewer opens with the big ideas and the building block × moment grid, and has no two-country panel.

**Fix (upstream, cat-harness-tools `scripts/journeys/`, `assets/journeys.css`):** Add the panel, drawn from the graph (systems, their RA layer and country, the moments that use them), above the ArchiMate views; move the big ideas below. Keep the block × moment grid.

## Done when

- the panel exists and matches ref/07, every box linked and resolved from the graph;
- the big ideas follow the ArchiMate views;
- a screenshot beside the reference is attached to the PR.
