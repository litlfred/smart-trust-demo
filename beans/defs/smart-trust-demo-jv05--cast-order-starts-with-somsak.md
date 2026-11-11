# smart-trust-demo-jv05
title: 'JV-05: journeys viewer, the cast is listed starting with Somsak'
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

A style difference the owner marked **Fix** in the side-by-side review of [[smart-trust-demo-jv03]] (row D03, [review page](https://claude.ai/artifact/Nyaej36JQowq5wYcZxrXFV), 2026-11-11). Spec: `docs/proposals/journeys-viewer-parity/README.md` §1; reference `docs/proposals/journeys-viewer-parity/ref/01, ref/05, ref/06`.

**Today:** VaxLink lists the cast Somsak, Khamla, Bounmy, Vilay, Chanthason, Dr. Anan: the baby first, then his family, then the health workers. The viewer starts with Dr. Anan on the overview, the journey map rows and the persona list.

**Fix (upstream, cat-harness-tools `scripts/journeys/`, `assets/journeys.css`):** Order people by an explicit order from the graph (the workshop's cast order), not by first appearance or name.

## Done when

- overview, journey map and persona lens list the cast in the VaxLink order;
- a screenshot beside the reference is attached to the PR.
