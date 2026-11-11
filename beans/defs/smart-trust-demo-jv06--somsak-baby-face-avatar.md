# smart-trust-demo-jv06
title: 'JV-06: journeys viewer, Somsak''s avatar is a baby face, not initials'
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

A style difference the owner marked **Fix** in the side-by-side review of [[smart-trust-demo-jv03]] (row D05, [review page](https://claude.ai/artifact/Nyaej36JQowq5wYcZxrXFV), 2026-11-11). Spec: `docs/proposals/journeys-viewer-parity/README.md` §1; reference `docs/proposals/journeys-viewer-parity/ref/01, ref/05, ref/06`.

**Today:** VaxLink shows Somsak (the baby) with a baby-face icon. The viewer shows the initials “SS” on people cards, the journey map and the persona list (the overview cast card already has the icon).

**Fix (upstream, cat-harness-tools `scripts/journeys/`, `assets/journeys.css`):** Let a persona carry an avatar icon in the graph (`meta.persona`), and use it everywhere the avatar is drawn.

## Done when

- every avatar of Somsak in the viewer shows the baby-face icon;
- a screenshot beside the reference is attached to the PR.
