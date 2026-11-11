# smart-trust-demo-jv18
title: 'JV-18: journeys viewer, FHIR example links are labelled in words'
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

A style difference the owner marked **Fix** in the side-by-side review of [[smart-trust-demo-jv03]] (row D23, [review page](https://claude.ai/artifact/Nyaej36JQowq5wYcZxrXFV), 2026-11-11). Spec: `docs/proposals/journeys-viewer-parity/README.md` §1; reference `docs/proposals/journeys-viewer-parity/ref/13`.

**Today:** In Under the hood, “FHIR resources created or changed”, VaxLink labels example links in words (“LA verified Hep B”, “TH original”, “LA verification”). The viewer shows the example ids (“TrustDemoJ3HepB”).

**Fix (upstream, cat-harness-tools `scripts/journeys/`, `assets/journeys.css`):** Use the example's title (or a short label on the step → example edge) as the link text, with the id kept as the link target.

## Done when

- every FHIR example link in Under the hood reads as words, as in ref/13;
- a screenshot beside the reference is attached to the PR.
