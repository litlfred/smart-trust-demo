# smart-trust-demo-jv01
title: 'JV-01: journeys viewer, each ArchiMate box links to its element page'
status: todo
type: feature
priority: normal
tags:
    - upstream
    - journeys-viewer-parity
created_at: 2026-11-11T09:05:00Z
updated_at: 2026-11-11T09:05:00Z
---

A parity gap left after VaxLink was retired (issue #111). Spec: `docs/proposals/journeys-viewer-parity/README.md` §4, row "How it works → The ArchiMate views on the DPI-H RA, each box linking to its element page".

**Today:** the How it works pages (`how/`, `how/<block>/`) link each ArchiMate *view* page (`en/smart-trust-demo/archimate/0.1.0/views/<view>/`). No page of the viewer links an *element* page (`archimate/0.1.0/elements/<slug>/`): 0 links on the published root, checked 2026-11-11.

**Fix (upstream, cat-harness-tools `scripts/journeys/present-views.ts`):** draw the views inline (or the per-block element list) with each box linked to its element page, resolved from the graph (`planSlugs`), not hard-coded.

## Done when

- every box of each ArchiMate view on How it works opens its element page;
- a block's page lists its ArchiMate elements, each linked;
- a test in `scripts/tests/journeys-viz.test.ts` covers it.
