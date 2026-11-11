# smart-trust-demo-jv02
title: 'JV-02: journeys viewer, the FHIR payload drawer on every view'
status: todo
type: feature
priority: normal
tags:
    - upstream
    - journeys-viewer-parity
created_at: 2026-11-11T09:05:00Z
updated_at: 2026-11-11T09:05:00Z
---

A parity gap left after VaxLink was retired (issue #111). Spec: `docs/proposals/journeys-viewer-parity/README.md` §2, row "FHIR payload drawer: a drawer at the bottom of every page … and a copy button" (`ref/13`).

**Today:** the drawer (`jp-drawer`) is on the walkthrough pages and the overview only. Map, personas, how it works, discussion, sheets and the device demo (S1 to S8) have none, checked on the published root 2026-11-11. VaxLink's device screens opened the drawer on the payload the screen shows.

**Fix (upstream, cat-harness-tools `scripts/journeys/present.ts` / `present-views.ts`):** render the drawer on every view, with the tabs for the examples the view's steps or screen name. On a device screen, "Inspect JSON" opens the tab of the payload it shows.

## Done when

- every view has the drawer, with copy;
- each device screen S1 to S8 opens the drawer on its own payload;
- covered by `scripts/tests/journeys-viz.test.ts`.
