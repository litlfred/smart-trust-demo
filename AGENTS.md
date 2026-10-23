# AGENTS.md — smart-trust-demo

This file is agent-generic: Claude Code, Gemini CLI, Cursor, Copilot and others
read it natively. The harness's
[`AGENTS.md`](https://github.com/litlfred/cat-harness/blob/HEAD/AGENTS.md) applies
everywhere. [`README.md`](README.md) says what this repository *is*;
[`docs/plan.md`](docs/plan.md) says what is being built and in what order.

## What this instance is

The demonstrator for the SMART Trust HCERT libraries: the user journeys J1–J4
as BPMN processes, personas and scenarios, an Open Health Stack app that runs
them with the Kotlin HCERT library, and the Android emulator test of that
library. It becomes a cat-harness downstream of
[smart-trust-tools](https://github.com/litlfred/smart-trust-tools) (owner's
choice, 2026-10-23), reusing its conventions: processes in `processes/`,
roles and personas in `scenarios/`, owner directives in `memory/`, open
issues as beans in `beans/`. Requirements are not restated here: a journey
step traces to smart-trust-tools' `req:` nodes by id.

## Rules

- **Only litlfred repositories are changed from here.** WHO repositories
  (`smart-trust`, `smart-trust-phw`), the OHS Foundation's and IHE's are
  read-only: report issues there; a PR to a WHO repository only when the owner
  asks, and never merge one.
- **Every dependency is pinned and verified; nothing is resolved at run
  time.** Gradle artifacts (Maven Central and Google Maven alike) are listed
  with their sha256 in `gradle/verification-metadata.xml`; npm and Bun by
  lockfile integrity with install scripts off; GitHub Actions by commit SHA. A
  new or bumped dependency is a release at least 14 days old, and each new one
  is listed with its reason in [`docs/dependencies.md`](docs/dependencies.md).
  Prefer writing a small piece over adding a package.
- **The HCERT library comes from a pinned smart-trust-tools commit**, built
  by that repository's own Gradle build and verification metadata, never from
  a floating branch.
- **Only open standards** are normative references: IETF, W3C, HL7 FHIR, IHE,
  WHO. No paywalled ISO.
- **gh-pages is published by an agent, not a workflow.** main publishes to the
  root; every other branch to `STAGING/<branch-slug>/`.
- **Every person is fictional.** Personas and test patients are invented;
  the J1 newborn is the WHO guide's own example.
- **Test keys are test keys.** Signing keys in this repository are throw-away
  and marked TEST-ONLY; production keys never enter it.
- No model identifiers in commits, PRs or code.

## Cold start

The harness layers and smart-trust-tools are mounted from `index.lock.json`
(the mounts are gitignored; the lock is committed). In a fresh container:

```sh
python3 -c "import json;[print(m['harness'],m['repository'],m['ref']) for m in json.load(open('index.lock.json'))['mounts'] if m['harness']!='smart-trust-tools']" > /tmp/mounts.txt
while read h r ref; do git clone -q --filter=blob:none --no-checkout https://github.com/$r $h && git -C $h checkout -q $ref && rm -rf $h/.git; done < /tmp/mounts.txt
bun install --frozen-lockfile
bun run cat mount:lock            # lays down every pinned layer, smart-trust-tools included
bun run cat mount:remote:check
```

Generators that write below a mounted layer (for example `bpmn:checklist`,
which also writes into `cat-harness/`) leave that mount "modified"; re-lay it
with `rm -rf <layer>` and the clone line above, then `mount:lock`. Publish
gh-pages with `bun cat-harness-tools/scripts/stage-local.ts --repo .`.
