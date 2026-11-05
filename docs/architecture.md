---
title: Architecture (ArchiMate)
nav_order: 4
---

# Architecture: the demonstrator on the DPI-H RA

The journeys and systems of this demonstrator, drawn as an ArchiMate overlay
on the [DPI-H Reference Architecture](https://litlfred.github.io/smart-ra/en/dpi-h-ra/index.html)'s
own ArchiMate model (smart-ra, version 0.3.0-draft.1). The RA's elements are
unchanged and keep their ids, so each RA box here is the element
[smart-ra publishes](https://litlfred.github.io/smart-ra/en/dpi-h-ra/archimate/0.3.0-draft.1/).
The overlay adds:

- the journeys J1 to J4.1 (the use cases) as business processes, one per
  [BPMN process](https://litlfred.github.io/smart-trust-demo/business-processes.html);
- the people who take part, as business roles assigned to the journeys
  whose BPMN has their lane;
- each of those roles **associated** with the RA stakeholder it belongs to:
  the caregiver with *Citizens / Care recipients*, the clinicians and the
  community health worker with *Health Workers* (a role and a stakeholder are
  different element types, so ArchiMate allows an association, not a
  specialization);
- the Thai and Lao systems, each a **specialization** of the RA building
  block it is an instance of, serving the journeys it takes part in;
- each journey's **realization** of the RA capabilities it exercises.

Every box in a drawing links to its element's page.
[All views and elements](en/smart-trust-demo/archimate/0.1.0/).

## Systems on the Integrated View

Thailand on the left, Lao PDR on the right, the layers of the RA's Integrated
View (Fig. 3.2) in the middle, and WHO GDHCN beneath both.

[![Systems on the DPI-H Integrated View](archimate/0.1.0/views/id-249a1002c32e50199e27a502ef0ec3d8.svg)](en/smart-trust-demo/archimate/0.1.0/views/smart-trust-demo-on-the-dpi-h-integrated-view/)

## Journeys (use cases)

[![Journeys, people and capabilities](archimate/0.1.0/views/id-c6cae81c85da5fc197ab58547274a481.svg)](en/smart-trust-demo/archimate/0.1.0/views/smart-trust-demo-journeys-use-cases/)

## One view per journey

| Journey | View |
|---|---|
| J1 Issue the birth-dose DVCs | [J1 on the DPI-H RA](en/smart-trust-demo/archimate/0.1.0/views/j1-on-the-dpi-h-ra/) |
| J2 Discover and refer the infant | [J2 on the DPI-H RA](en/smart-trust-demo/archimate/0.1.0/views/j2-on-the-dpi-h-ra/) |
| J3 Verify, import and schedule | [J3 on the DPI-H RA](en/smart-trust-demo/archimate/0.1.0/views/j3-on-the-dpi-h-ra/) |
| J4.0 Issue the family's VHLs | [J4.0 on the DPI-H RA](en/smart-trust-demo/archimate/0.1.0/views/j4-0-on-the-dpi-h-ra/) |
| J4.1 Read records at the point of care | [J4.1 on the DPI-H RA](en/smart-trust-demo/archimate/0.1.0/views/j4-1-on-the-dpi-h-ra/) |

## How it is made

The model is generated, not drawn: `python3 -I tools/archimate/build.py`
fetches smart-ra's model and its `add_views.py` at the commit in
`tools/archimate/smart-ra.lock.json` (sha256 checked), applies
`tools/archimate/overlay.py`, and writes `archimate/0.1.0/smart-trust-demo.archimate`.
The journeys and their people are read from `processes/content/` and
`scenarios/roles.json`; the systems are those of VaxLink's architecture view.
CI fails if the committed model is not what the build makes. The drawings are
cat-harness's `archimate` subgraph's: no Archi, no Java.
