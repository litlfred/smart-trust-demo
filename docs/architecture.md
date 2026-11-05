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
- the Thai and Lao systems, serving the journeys they take part in, each
  holding its parts;
- for each country, its own **instance** of every RA building block its parts
  play, such as *Provider Systems (Thailand)* and *Provider Systems (Lao
  PDR)*: Thailand and Lao PDR are different jurisdictions, so a Thai part is
  a **specialization** of Thailand's instance, which is in turn a
  specialization of the RA's block;
- **where the two countries meet**, as flow and triggering relationships
  between their parts, read from the BPMN: the paper DVC that J1 prints and
  the family carries to J2 and J3; in J4.1, the VHL QR the family's phone
  shows the Thai clinic, the clinic's signed ITI-YY5 manifest request to the
  Lao gateway, and the manifest it returns, the access logged in Lao PDR;
- **what they share**, and nothing else, between them: WHO GDHCN and the WHO
  SMART Trust specifications it realizes;
- the RA's own building blocks, generic and no country's, in a band of their
  own below both countries;
- each journey's **realization** of the RA capabilities it exercises.

Every line is routed orthogonally through the gaps between boxes and never
through a box.

Every box in a drawing links to its element's page.
[All views and elements](en/smart-trust-demo/archimate/0.1.0/).

## Systems on the Integrated View

Thailand on the left, Lao PDR on the right, each with its systems above its
instances of the RA building blocks (each instance under the part that plays
it); between them, only what both share: WHO GDHCN and the SMART Trust
specifications. Below both, the RA's own building blocks, by the layers of its
Integrated View (Fig. 3.2). The dashed lines that run from one country to the
other are where they meet.

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
`tools/archimate/overlay.py`, lays the overlay's views out again with room
between the boxes and routes every line orthogonally as Archi bendpoints
(`tools/archimate/layout.py`), and writes `archimate/0.1.0/smart-trust-demo.archimate`.
The journeys and their people are read from `processes/content/` and
`scenarios/roles.json`, and where the countries meet from the BPMN's sequence
flows; the systems are those of VaxLink's architecture view.
CI fails if the committed model is not what the build makes. The drawings are
cat-harness's `archimate` subgraph's: no Archi, no Java.
