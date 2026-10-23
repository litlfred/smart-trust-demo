# Plan

Each step is one pull request, merged when CI is green. Decisions that are the
owner's are asked before the step that needs them and recorded in `memory/`.

## Decisions so far (2026-10-23)

| Decision | Choice | Record |
|---|---|---|
| Library consumption | Build the JVM jars in CI from a pinned smart-trust-tools commit | [memory/dir-library-consumption.md](../memory/dir-library-consumption.md) |
| Harness | Full cat-harness downstream of smart-trust-tools | [memory/dir-downstream.md](../memory/dir-downstream.md) |
| Home country (J2–J4) | A fictional GDHCN DEV participant; J1's issuer stays `XXR` | [memory/dir-journeys-demo.md](../memory/dir-journeys-demo.md) |
| OHS base for the app | **Open** — options with pros and cons in [proposals/app-platform.md](proposals/app-platform.md) | — |

## Steps

### 1. Plan and skeleton (this PR)

README (including the smart-trust-phw upstream note), AGENTS.md, this plan,
the app-platform proposal, owner directives in `memory/`, the dependency
register, and a CI job that checks every GitHub Action is pinned by commit
SHA and every JSON file parses.

### 2. Journeys as cat-harness content

- (done) `smart-trust-demo.json` declaration and `index.config.json` pinning the
  harness layers smart-trust-tools pins (fhir-harness and below) plus
  smart-trust-tools itself, so `req:` ids resolve; `index.lock.json`.
- `scenarios/`: the actors (reusing smart-trust-tools' VHL Holder, Sharer,
  Receiver, Trust Network Participant), the roles that play lanes, and the
  personas: the mother and newborn (J1's IG example), the J1 clinic nurse,
  the CHW (J2), the home clinic provider (J3), the national portal and the
  border/clinic receiver abroad (J4).
- `processes/content/`: one BPMN per journey (done in step 2a; checklists and the harness mount in 2b) (J1 issuance, J2 CHW discovery
  and referral, J3 verification, import and schedule, J4.0 VHL issuance to a
  shared phone, J4.1 VHL fetch at the point of care), lanes naming roles,
  tasks naming smart-trust-tools skills; checklists generated.
- User scenarios: one per journey, each step tracing to `req:` nodes
  (e.g. J2 → STT-VER-011, J3 → STT-VER-001…, J4 → the VHL requirements).
- Beans for gaps found on the way (in this repository, or tagged upstream
  for smart-trust-tools, smart-trust or smart-trust-phw).

### 3. The HCERT library at a pinned commit

`lib/hcert/`: a script and Gradle wiring that checks out smart-trust-tools
at a pinned SHA, builds `hcert-api` and `hcert-core` (JVM) with that
repository's own Gradle and `verification-metadata.xml`, and copies the jars
to `lib/hcert/build/libs/`, failing if a jar's sha256 differs from the one
recorded in `lib/hcert/hcert.lock.json` (the build is reproducible). The app
and the Android tests depend on those files. Bumping the library is the
commit in the lock plus `build.py --update`.

### 4. Android emulator test of the library (STT-GEN-004)

`android-test/`: an Android library module whose instrumented tests run on
an emulator in CI (Android API levels to be chosen: one current, one old
enough to matter for clinics, e.g. 26 and 35):

- verify the IG's §12 example against XXR's DSC DID document (the DEV trust
  list), on Android's platform providers;
- `readUnverified` of the same QR (J2);
- issue with an Android Keystore key (prepare → Keystore sign → finish) and
  verify it, ES256, and PS256 where the platform offers it;
- VHL: build and read a `vhlink:/`, decrypt the JWE fixture.

Results are reported back to smart-trust-tools as evidence for STT-GEN-004
(and as beans there for anything Android refuses, e.g. algorithm names).
Google Maven artifacts (AGP, AndroidX test) are pinned with sha256 like every
other. The emulator job uses a pinned action by SHA and caches no
unverified artifacts.

### 5. The app

On the base the owner chooses from the proposal (recommended: a lean
Compose Multiplatform app on the OHS KMP libraries, Android first):

- J1: clinic issues the newborn's DVC (bundled test key standing in for the
  clinic's DSC, or the Keystore), prints/shows the QR.
- J2: CHW scans the paper QR offline (`readUnverified`), registers the
  infant (SDC questionnaire), creates a referral (`ServiceRequest`).
- J3: clinic verifies against the bundled DEV trust list, imports the
  `Immunization`s into the on-device FHIR engine, evaluates the schedule
  (`PlanDefinition/$apply`), shows the next doses.
- J4: portal issues per-member VHL QRs to the shared phone; a receiver
  fetches the manifest (ITI-YY5) from a local test sharer and decrypts.

An emulator UI test drives the four journeys end to end.

### 6. Web and publication

The web target (once hcert-core runs in a browser, or via the Rust/wasm
library meanwhile), and the gh-pages site (agent-published): the journeys,
BPMN viewers, personas and the test evidence.

## Open items

- **Network:** this session cannot reach `dl.google.com` (Google Maven, the
  Android SDK). Steps 4–5 need it locally to write the verification metadata;
  the owner can allow it in the environment's network settings.
- **Browser build of hcert-core** (for the web target): to be raised in
  smart-trust-tools.
- **Android algorithm names:** hcert-core's JVM code asks for `RSASSA-PSS`,
  which Android's providers may not offer under that name; step 4 will show.
