# AGENTS.md — smart-trust-demo

This file is agent-generic: Claude Code, Gemini CLI, Cursor, Copilot and others
read it natively. The harness's
[`AGENTS.md`](https://github.com/litlfred/cat-harness/blob/HEAD/AGENTS.md) applies
everywhere. [`README.md`](README.md) says what this repository *is*;
[`docs/plan.md`](docs/plan.md) says what is being built and in what order.

## What this instance is

The demonstrator for the SMART Trust HCERT libraries: the user journeys J1–J4
as BPMN processes, personas and scenarios, an Open Health Stack app that runs
them with the Kotlin HCERT library, the Android emulator test of that
library, and the VaxLink walkthrough of the journeys for workshops (`web/`,
published at `vaxlink/` of this site). It becomes a cat-harness downstream of
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
  root; every other branch to `STAGING/<branch-slug>/`. The walkthrough goes
  to `vaxlink/` inside that, by `web/scripts/publish.sh`, after the site.
- **The walkthrough (`web/`) restates nothing it can read.** Actors, BPMN
  drawings and moment pictures are imported from `scenarios/actors/`,
  `processes/content/` and `docs/images/` at build time; the ArchiMate views
  are the site's own drawings. A persona's name, role, country, goal, needs
  and frustrations are its actor's `meta.persona`; only initials and colours
  are in `web/src/data/journeyData.ts`. The FHIR examples in
  `web/src/data/ig/` are SUSHI's output, copied by
  `node web/scripts/ig-examples.mjs` and checked by its `--check` in CI:
  edit `input/fsh/`, never the copy.
- **Every person is fictional.** Personas and test patients are invented.
  The journeys follow the VaxLink walkthrough's family (issue #21); the WHO
  guide's own worked example (QR Code Generation §12) stays the library's
  test vector.
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
gh-pages with `bun cat-harness-tools/scripts/stage-local.ts --repo . --publisher ig`,
then `sh web/scripts/publish.sh`, which builds `web/` and places it at
`vaxlink/` (or `STAGING/<branch>/vaxlink/`) beside the site of the same
commit. The site's publish keeps `vaxlink/` at the root because
`index.config.json` lists it in `site.build.keep`; a branch's site publish
replaces `STAGING/<branch>/` whole, so the walkthrough always goes second.

## Translations

The harness's generic process is
[`translation-refresh`](https://github.com/litlfred/cat-harness/blob/HEAD/skills/library/library-core/translation-refresh.md)
and `translation-manager` §"Translating into several locales as a team"; this
section names what that skill leaves to the instance. Locales: ar, es, fr, ru,
zh, all unofficial (agent, no human sign-off). Each locale is its own PR to
main.

| step | here |
|---|---|
| diagram templates | `bun run cat translate-bpmn --instance . --extract` (`:check` in CI) |
| page templates | `bun tools/translation/pages-pot.ts` (`--check` in CI): `docs/**` and the non-copy pages of `input/pagecontent/` into `translations/<locale>/…` |
| new and obsolete strings | `bun tools/translation/po-status.ts --merge` appends new msgids empty and keeps obsolete ones as `#~`; without `--merge` it reports |
| FHIR terms | one CodeSystem supplement per locale, `input/fsh/translations/<locale>.fsh`; never edit a resource's own text |
| QA report | `python3 -I tools/translation/glossary_qa.py --layer "smart-trust (GDHCN glossary)=<smart-trust>/…/{locale}/*.po"` writes `test/results/translation-qa/`; `--check` fails only on a lost token or an official claim |
| round-trip verdicts | `test/results/translation-qa/roundtrip.json`, the adjudicator's, by hand |

The CI job `bpmn-generated` in `.github/workflows/checks.yml` runs the template
checks, `kg:locale:check`, the officiality check, `po-status --github` and the
QA `--check`. Merge policy: **merge-when-green** (owner, 2026-11-07). A
refresh run merges its own refresh PR only when every check is green and the
untainted round trip on the changed strings records no fail; anything red,
uncertain or failing is left open and reported to the owner. Merging is not
sign-off: the translations stay unofficial.
