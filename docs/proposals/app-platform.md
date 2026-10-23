---
title: Proposal: Open Health Stack base
nav_order: 4
---

# Proposal: which Open Health Stack base for the demonstrator app

**Status:** for the owner's decision. Researched 2026-10-23.
**Question:** on what should the J1–J4 app be built, so that it runs the
Kotlin HCERT library on Android (and, ideally, the web) on the most recent,
most Kotlin-native Open Health Stack?

## 1. What Open Health Stack is today

Open Health Stack (OHS) began as a Google-led set of components and is now
the **OHS Software Foundation**, a community project under the Linux
Foundation, which WHO joined in July 2026. Its code lives in
[github.com/ohs-foundation](https://github.com/ohs-foundation) (28
repositories). There are two generations of the client libraries:

| Generation | Libraries | Platforms | Distribution | State |
|---|---|---|---|---|
| **android-fhir** (first) | `com.google.android.fhir:engine`, `data-capture` (SDC), `workflow`, `knowledge` | Android only | Google Maven | "Maintenance"; last commit Feb–Mar 2026. Workflow runs CQL (HAPI-based, heavy). |
| **Kotlin Multiplatform** (current) | `dev.ohs.fhir:fhir-model-r4` 1.0.0-rc03, `fhir-path-r4`, `fhir-engine` 2.0.0-alpha04, `fhir-data-capture` 2.0.0-alpha04, `fhir-workflow` 2.0.0-alpha01; `dev.ohs.player:client` 1.0.0-alpha03 | Android, desktop JVM, iOS, web (wasmJs, and JS for some) | **Maven Central** | Active (commits this week); alpha APIs. Workflow does `PlanDefinition/$apply`; CQL is "still to come". |

On top of the KMP generation sits the **OHS Player**, described by the
foundation as a cross-stack reference toolkit, "reference, not product":

- [`player-reference`](https://github.com/ohs-foundation/player-reference):
  the client, a GitHub *template* app in Compose Multiplatform (Android, iOS,
  desktop, web from one tree). Screens are driven by configuration
  (SQL-on-FHIR `ViewDefinition`s compiled at build time), data entry by SDC
  questionnaires. It opens on an OIDC login and blocks on a first sync with a
  FHIR server; there is no bundled-data mode.
- [`player-client`](https://github.com/ohs-foundation/player-client): the
  library behind it (configuration-driven FHIR views), usable on its own.
- [`ohs-player-reference-web-portal`](https://github.com/ohs-foundation/ohs-player-reference-web-portal):
  a TypeScript admin portal for workforce hierarchies (users, access). Not a
  clinical web app; not relevant to J1–J4.
- `ohs-player-reference-backend`, `-infrastructure`: backend and deployment
  (FHIR gateway, data pipes).
- [`player-reference-examples`](https://github.com/ohs-foundation/player-reference-examples):
  variants of the reference app (empty today). A natural place to offer the
  journeys upstream later — an OHS Foundation repository, so only by
  proposal, never from here.

The most recent and most Kotlin-native choice is therefore the **KMP
generation**, with or without the Player template.

## 2. Constraints every option must meet

1. **The Android emulator test of the HCERT library** (STT-GEN-004) must run
   in CI on an Android runtime, platform crypto included. This is
   independent of the app: it is a small Android test module that depends
   only on the HCERT jar (plan step 4). It can land before the app decision.
2. **Offline and serverless demo.** J2 is offline by definition, and CI
   cannot stand up an OIDC provider and FHIR server for an emulator run
   cheaply. The app needs a bundled-data mode.
3. **Supply chain.** Every artifact pinned with sha256, releases ≥ 14 days
   old, no install scripts. Fewer dependencies is better.
4. **The HCERT library** comes from a pinned smart-trust-tools commit as a
   JVM jar (owner's choice). On Android the JVM jar works as is. **On the web
   it does not yet:** hcert-core's Kotlin/JS target uses `node:crypto` and
   `node:zlib`, so it runs on Node, not in a browser, and there is no wasmJs
   target. Any web front end needs either a browser target in hcert-core
   (WebCrypto, `CompressionStream`), a library change in smart-trust-tools,
   or the Rust/wasm library, which already runs in the browser with WebCrypto
   keys.

## 3. Options

### Option A — Fork the OHS Player reference app

Create the app from the `player-reference` template; add an offline demo
mode (bundled FHIR bundle, no login), the J1–J4 screens and the HCERT calls.

| Pros | Cons |
|---|---|
| It *is* the OHS Player: the most visibly "OHS" outcome, and the closest to what OHS implementers will start from. | Requires an OIDC provider and a FHIR server to start; the offline mode is ours to write and to keep merging against a template that moves weekly. |
| Android, iOS, desktop and web from one tree; configuration-driven screens; SDC questionnaires for registration (J2) and import (J3) come wired. | ~57 libraries and 8 plugins in its catalogue (Koin, Ktor CIO/Darwin, Kermit, ksafe, kotlinpoet, BigNum, Compose adaptive …), several alpha, plus their transitive graph: the largest pinning and verification burden of all options. |
| Upstreamable: journeys could later become a variant in `player-reference-examples`. | Kotlin 2.3 / AGP 8.11 / JDK 21; its build-logic and code generation (`ig-codegen`) are ours to audit. |
| | Much of the template (auth, sync, workforce registers) is unrelated to the journeys and is noise in a demonstrator. |

### Option B — Own lean Compose Multiplatform app on the OHS KMP libraries (recommended)

A small Compose Multiplatform app (Android first, web target alongside)
written for the four journeys, using the same foundational libraries the
Player uses — `fhir-model-r4`, `fhir-engine` (on-device store), 
`fhir-data-capture` (SDC questionnaires for J2 registration and J3 import),
`fhir-workflow` (`PlanDefinition/$apply` for the J3 schedule) — and,
optionally, `dev.ohs.player:client` for configuration-driven views.

| Pros | Cons |
|---|---|
| Same current OHS libraries as the Player, so it demonstrates the stack the OHS Foundation is building towards, without the template's auth/sync/DI layer. | Not the Player app itself; screens are ours. |
| Offline and serverless from the start; the emulator CI job can drive the journeys. | The KMP libraries are alpha: API breaks between alphas are ours to absorb. |
| Dependency set is roughly the libraries' own graph (Compose MP, Ktor client, Room3/SQLite, kotlinx) — still sizeable, but every addition is chosen and listed in `docs/dependencies.md`. | `fhir-workflow` has no CQL yet: the J3 schedule rules must be expressed as `PlanDefinition` applicability conditions in FHIRPath (enough for a birth-dose schedule; WHO SMART immunization CQL would wait). |
| Shapes the code so the journey screens can later be offered to `player-reference-examples` as a Player variant. | |

### Option C — Android only, on android-fhir (first generation)

A plain Android app on `com.google.android.fhir` Engine + SDC (+ Workflow).

| Pros | Cons |
|---|---|
| Mature, production-proven (OpenSRP, EmCare); most documentation and examples. | In maintenance; not where OHS is going; Android only (no web). |
| Workflow library runs CQL today (WHO SMART Guidelines content). | Workflow pulls HAPI FHIR + CQL engine: a very large, JVM-heavy dependency graph. |
| | Google Maven artifacts; the session's network policy currently blocks `dl.google.com` (needed for this and for AGP/AndroidX in every option). |

### Option D — Web first, no Android app

A static page on gh-pages running J1–J4 in the browser with the Rust/wasm
library (or a future browser build of hcert-core), plus only the Android test
module for STT-GEN-004.

| Pros | Cons |
|---|---|
| Smallest: almost no dependencies; easiest to show anyone with a link. | Not OHS; does not show the Kotlin library inside an OHS app, which is the stated goal. |
| The Rust/wasm library already runs in the browser. | The Kotlin library on Android is exercised only by tests, not by a journey. |

## 4. Recommendation

**Option B**, staged:

1. Android test module for STT-GEN-004 first (independent of this choice).
2. The B app, Android target, offline, J1–J4, on `dev.ohs.fhir`
   engine + data capture + workflow.
3. The web target of the same app once hcert-core has a browser target (to
   be requested in smart-trust-tools) — or, in the meantime, the journeys'
   QR steps on the web through the Rust/wasm library.
4. Later, propose the journeys to the OHS Foundation as a
   `player-reference-examples` variant (owner's call; never pushed from
   here).

If being *the* OHS Player matters more than dependency count and an offline
demo, choose **A**: the plan is the same, with step 2 starting from the
template and adding the offline mode first.

## 5. What any option needs from the environment

- `dl.google.com` (Google Maven: AGP, AndroidX, the Android SDK) is blocked
  by this session's network policy. It is needed to write the Gradle
  verification metadata for any Android build. GitHub's runners can reach it,
  so CI is unaffected; local builds here are.

## Sources

- [OHS Foundation on GitHub](https://github.com/ohs-foundation) — repository list and descriptions, 2026-10-23.
- [ohs-player README](https://github.com/ohs-foundation/ohs-player), [player-reference README](https://github.com/ohs-foundation/player-reference), [player-client README](https://github.com/ohs-foundation/player-client), [kotlin-fhir-engine README](https://github.com/ohs-foundation/kotlin-fhir-engine), [kotlin-fhir-workflow README](https://github.com/ohs-foundation/kotlin-fhir-workflow).
- Maven Central metadata for `dev.ohs.fhir` and `dev.ohs.player` (versions and publication dates).
- [Android FHIR SDK](https://developers.google.com/open-health-stack/android-fhir) and its [Workflow library](https://developers.google.com/open-health-stack/android-fhir/workflow).
- [WHO joins the Open Health Stack Software Foundation](https://www.who.int/news/item/09-07-2026-who-joins-the-open-health-stack-software-foundation-to-advance-open--standards-based-digital-health-for-all-countries), WHO, July 2026.
