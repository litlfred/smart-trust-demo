# smart-trust-demo-jv03
title: 'JV-03: owner compares the journeys viewer with the VaxLink reference screenshots'
status: todo
type: task
priority: normal
tags:
    - owner
    - journeys-viewer-parity
created_at: 2026-11-11T09:05:00Z
updated_at: 2026-11-11T09:05:00Z
---

The parity spec's last "done when" (`docs/proposals/journeys-viewer-parity/README.md`): the owner compares the viewer with VaxLink side by side. VaxLink was retired on 2026-11-11 before that check (issue #111), so the comparison is now against the reference screenshots in `docs/proposals/journeys-viewer-parity/ref/01..13`.

**Work:** take a screenshot of each viewer page that matches a `ref/NN-*.webp` (light, desktop width), put the pairs side by side on one page, and list each style difference (§1: frame, palette, type, hero, moment cards, people, record ladder). Each difference the owner wants fixed becomes its own bean.

The functional checks (views, keys W/T/arrows, presenter mode, deep links, step ↔ screen links, block ↔ moments index, spec links, IG process and scenario anchors) were done from the published HTML on 2026-11-11 and pass. The open gaps there are [[smart-trust-demo-jv01]] and [[smart-trust-demo-jv02]].

## Done when

- the side-by-side page exists and the owner has reviewed it;
- every difference is fixed or recorded as a bean.
