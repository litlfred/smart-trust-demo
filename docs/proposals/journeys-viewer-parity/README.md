# Journeys viewer: parity with VaxLink

**Status:** spec, 2026-11-05. VaxLink was retired on 2026-11-11 by the owner's choice (issue #111): `web/` and `vaxlink/` are gone, and the gaps still open are beans.

**Owner's decisions (2026-11-05):**

- The harness's static journeys viewer is rebuilt to look and work like VaxLink. It is not replaced by VaxLink's React app.
- VaxLink is not retired, and its URL does not redirect (litlfred/vaxlink#14 stays unmerged), until the viewer reaches parity.

**Why this file exists:** the first viewer preview, at `STAGING/claude-confident-hypatia-6g67t9/en/smart-trust-demo/journeys/`, has the content but looks and works nothing like VaxLink.

- Its pages are long documentation pages inside the harness's site frame.
- VaxLink is a facilitator's presentation tool.

This file is the target. The reference screenshots in [`ref/`](ref/) are VaxLink at litlfred/vaxlink `main` `d42b216` (the same app now lives in this repository's `web/`, published at `vaxlink/`), and they are the wireframes. `ref/viewer-*.webp` are the current preview, for comparison.

The parity check is to put each `ref/NN-*.webp` beside the viewer's matching page and confirm that every element listed below is there.

## 1. Styling

| | VaxLink | Viewer today | Required |
|---|---|---|---|
| Frame | Its own app frame. The top bar holds the workshop name, the journey code range, the trust-list status and the presenter toggle. A second bar holds the app title, the **Journeys / Device Demo** switch, and FHIR IG / IG source / Reset. | The harness site frame: branch banner, site bar with search, side rail. | **The harness frame and navbar stay** (owner, 2026-11-06: "harness frame and navbar is ok"; this supersedes the 2026-11-05 rule to drop the site chrome). Inside that frame, the journey page carries VaxLink's own two bars and tabs, and must match VaxLink in its colours, spacing and layout. |
| Palette | Tailwind tokens (`tailwind.config.js`): `clinical` alabaster `#F8FAFC`, surface, ink `#0F172A`, steel `#475569`, divider `#E2E8F0`; `dpi` cobalt `#0284C7`; `verified` emerald `#15803D`; `unverified` amber `#B45309`; `tampered` crimson `#B91C1C`. Each has light and dark tints. | The harness theme's greens and greys. | Take these tokens as the journey theme. The trust states use them: verified is emerald, reported is amber, tampered is crimson. |
| Type | Plus Jakarta Sans, falling back to Inter; large bold headlines; small-caps labels. | The harness body type. | The same family and scale. |
| Hero | A dark navy panel with the story in one sentence, a cast line, and two CTAs: **Start the walkthrough** and **See the whole journey map** (`ref/01`). | A plain heading and a list. | Required on a journey set's landing page. |
| Moment cards | A numbered card per chapter, with a country chip and the illustration (`ref/01`). | Text list rows. | Cards with the step illustration, `illustration.src`. |
| People | A coloured avatar with initials, an emotion badge (Distressed…Delighted) with a face, and a quote in italics (`ref/02`). | Present (avatars, faces, quotes), but plain. | The avatar colours from `meta.persona.color` and the badge style from VaxLink `shared.tsx`. |
| Record trust | The "Follow the record" ladder, a six-stage segmented bar with the current stage filled, in a card headed "SOMSACK'S RECORD" (`ref/03`). | A thin bar. | A segmented bar with the stage names, as in VaxLink. |

## 2. Wireframes: the views

VaxLink has seven journey views as tabs, plus the device demo. Every view has its own URL.

| # | View | What it shows | Reference | Viewer today |
|---|---|---|---|---|
| 1 | **Overview** | The hero, the four moments as cards, the cast, and the "Follow the record" ladder. | `ref/01` | partly (index list) |
| 2 | **Walkthrough** | **One moment at a time** (see below). | `ref/02`, `ref/03`, `ref/04` | missing: all steps on one long page |
| 3 | **Journey map** | A swimlane: a column per moment and a lane per person, a "Focus on" persona filter that dims the rest, and toggles for pain points & enablers and for the technical layer. | `ref/05` | partly: the grid is there; there is no focus filter and no toggles |
| 4 | **Persona lens** | One person end to end: goal, needs, frustrations, an emotion curve and touchpoints. | `ref/06` | missing |
| 5 | **How it works** | Four big ideas. A grid of building blocks × moments, by layer. A detail panel for each block, listing the moments that use it. The ArchiMate views. | `ref/07` | missing (per-step "Under the hood" only) |
| 6 | **Discussion** | The closing questions, each tagged by module and linked to its moments, plus every moment's policy takeaway. | `ref/08` | partly: workshop module pages |
| 7 | **Table sheets** | The A3 canvas: a cover and Sheets 1–6, ready to print. | `ref/09` | present (workshop sheets); check the layout against `ref/09` |
| — | **Device Demo** | Screens S1–S8, one per moment, in a phone or tablet frame, with a stage bar and "Back to the user journey". Includes the tamper test (S4) and the wrong-passcode test (S8). | `ref/10`–`ref/12` | missing |
| — | **FHIR payload drawer** | A drawer at the bottom of every page with syntax-highlighted Patient, Group, Immunization, ServiceRequest, Provenance, ConceptMap, AuditEvent and CBOR, and a copy button. "Inspect JSON" opens it on the right tab. | `ref/13` | missing |

### The walkthrough page

This is the core of VaxLink. It has to be one page per **step**, not per journey.

From top to bottom:

1. **A chapter progress bar** across all steps of the journey set (J1 → J4.1). The current step is highlighted. Its controls are ← and →, a dot per step, and **Discuss →** at the end.
2. **The left card:** chapter label and country chip; the step code and position ("J4.1 · 8/8"); the title; the illustration; the headline, with persona names as inline avatar chips; when, where and touchpoint.
3. **The right column:** the **record card** (trust ladder, the state, where it is held, the hand-off), then **Ask the room** (a dark card), then **What if…** (hidden until revealed, with "Let the room guess, then reveal"), then the **Policy takeaway**.
4. **Who's in this moment:** one card per person, with their emotion badge, what they do, and their quote.
5. **Under the hood** (toggled):
   - the technical so-what;
   - building blocks by layer, each with its role in this step;
   - the data hand-off: from, to, carrier, payload, offline or online;
   - the FHIR resources it changes, with profile, why, examples, and an "Inspect JSON" link into the drawer;
   - the BPMN card for the step's process.
6. **The facilitator cue**, shown only in presenter mode.

## 3. Workflow

VaxLink is used live in a room. The viewer must support the same flow (README "Running a workshop session"):

**Overview → Walkthrough** (for each moment: ask the room, then reveal the "What if…") **→ Under the hood** when asked **→ Persona lens → How it works → Device demo** when asked **→ Discussion.**

The flow needs these interactions:

| Interaction | VaxLink | Required |
|---|---|---|
| Next and previous moment | `→`/`PageDown`, `←`/`PageUp`. Moving on from the last moment opens Discussion. | yes |
| Reveal "What if…" | `W` | yes |
| Toggle Under the hood | `T` | yes |
| Presenter mode | A banner with the facilitator cue for the current view, which the presenter can hide before sharing the screen. | yes |
| Deep links | `#/walkthrough/J3b`, `#/demo/S4`, `#/personas/khamla`, `#/how/gdhcn`, `#/map`, `#/discuss`, `#/sheets` | a stable URL for every view, step, persona and block |
| Moment ↔ screen | "See what … sees" opens the matching screen; "Back to the user journey" returns to the moment. | yes, wherever an instance has screens |
| Works offline / static | A Vite build, static on GitHub Pages | static pages and a little vanilla JS, as now |

## 4. Links

Every moment in VaxLink links outward. A rebuilt page must keep each of these links, resolved from the graph rather than hard-coded:

| From | To | Source in VaxLink |
|---|---|---|
| Step | Its **BPMN process**: an inline drawing with the step's tasks highlighted, plus "Open in the IG" (the process anchor) and "Read the scenario" (the scenario anchor). | `BPMN_FOR_STAGE`, `bpmnSvg` (`links.ts`) |
| Step | Its **FHIR examples** and **profiles** in the IG: an artifact page for each. | `IG.example`, `IG.profile` |
| Building block | Its **specification** (HL7, IHE, WHO), and in How it works every moment that uses it. | `SPEC.*`, `BLOCK_LINKS` |
| How it works | The **ArchiMate views** on the DPI-H RA, each box linking to its element page. | `ArchiMateViews.tsx` |
| Journey | The IG pages for journeys, personas, business processes and examples, and the repository. | `IG.journeys`, `IG.personas`, `IG.processes`, `IG.examples`, `IG.repo` |
| Discussion question | The moments it relates to. | `relatedSteps` |
| Moment | Its device screen, and back again. | `screenHref`, `stepHref` |

Today the viewer has breadcrumbs, follows / part-of links, and requirement and example links in Under the hood. It lacks the step-to-screen links, the block-to-moments index, the IG process and scenario anchors, and links to the ArchiMate element pages.

## 5. Data the viewer already has, and what it lacks

| | In the graph? |
|---|---|
| Steps, people, feelings, pain points, enablers, policy, record, hand-off, what-ifs, stories, BPMN tasks, requirements, examples, blocks with roles | yes (`user-scenario`, `building-blocks`) |
| Ask the room, facilitator cue, questions by module, sheets | yes (`workshop`) |
| Illustrations | yes (`illustration`). Thai–Lao chapters: `public/moments/*.jpg` in VaxLink. Pilgrimage: `input/images/pilgrim/` |
| The four "big ideas" of How it works | **no.** Today they are in VaxLink `techData.ts` (`BIG_IDEAS`). They need a home (`building-blocks` groups?) |
| FHIR change per step: profile, why, example | **no.** `STEP_TECH.fhir` in VaxLink. These are a step → `examples` edge with a reason |
| Device screens S1–S8 | **no.** They are React components. *Open question:* static mock screens per step, or a link out to the instance's own app? |
| Chapter grouping (VaxLink's four chapters over five BPMN journeys) | yes, via `partOf` (J4 holds J4.0 and J4.1) |

## Done when

- Each view in section 2 exists in the viewer and matches its `ref/` screenshot element for element, in the section 1 style.
- The section 3 interactions work, and the section 4 links resolve from the graph.
- The owner has compared the viewer and VaxLink side by side and agreed to retire VaxLink.
