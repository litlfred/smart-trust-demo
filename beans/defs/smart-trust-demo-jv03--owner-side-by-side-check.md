# smart-trust-demo-jv03
title: 'JV-03: owner compares the journeys viewer with the VaxLink reference screenshots'
status: completed
type: task
priority: normal
tags:
    - owner
    - journeys-viewer-parity
created_at: 2026-11-11T09:05:00Z
updated_at: 2026-11-11T09:20:00Z
---

The parity spec's last "done when" (`docs/proposals/journeys-viewer-parity/README.md`): the owner compares the viewer with VaxLink side by side. VaxLink was retired on 2026-11-11 before that check (issue #111), so the comparison is now against the reference screenshots in `docs/proposals/journeys-viewer-parity/ref/01..13`.

**Work:** take a screenshot of each viewer page that matches a `ref/NN-*.webp` (light, desktop width), put the pairs side by side on one page, and list each style difference (§1: frame, palette, type, hero, moment cards, people, record ladder). Each difference the owner wants fixed becomes its own bean.

The functional checks (views, keys W/T/arrows, presenter mode, deep links, step ↔ screen links, block ↔ moments index, spec links, IG process and scenario anchors) were done from the published HTML on 2026-11-11 and pass. The open gaps there are [[smart-trust-demo-jv01]] and [[smart-trust-demo-jv02]].

## Done when

- the side-by-side page exists and the owner has reviewed it;
- every difference is fixed or recorded as a bean.

## Result (2026-11-11)

The side-by-side page is https://claude.ai/artifact/Nyaej36JQowq5wYcZxrXFV (13 pairs, 1400px, light). The owner reviewed 23 style differences: 15 Fix, 8 Keep.

- **Fix**, one bean each: D02 [[smart-trust-demo-jv04]], D03 [[smart-trust-demo-jv05]], D05 [[smart-trust-demo-jv06]], D06 [[smart-trust-demo-jv07]], D07 [[smart-trust-demo-jv08]], D08 [[smart-trust-demo-jv09]], D09 [[smart-trust-demo-jv10]], D11 [[smart-trust-demo-jv11]], D13 [[smart-trust-demo-jv12]], D14 [[smart-trust-demo-jv13]], D17 [[smart-trust-demo-jv14]], D19 [[smart-trust-demo-jv15]], D20 [[smart-trust-demo-jv16]], D21 [[smart-trust-demo-jv17]], D23 [[smart-trust-demo-jv18]].
- **Keep** (the viewer's way stays): D01 illustration on top of moment cards; D04 people's names as links; D10 the DAK strip in Under the hood; D12 taller map cards with avatar chips; D15 the ArchiMate view drawn by country; D16 the discussion's extra sections; D18 the framed sheet style; D22 small layout changes inside device screens.
