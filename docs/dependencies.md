---
title: Dependency register
nav_order: 5
---

# Dependency register

Every dependency of this repository, with its reason. A new or bumped
dependency is a release at least 14 days old, pinned (lockfile or
`gradle/verification-metadata.xml` with sha256) and added here in the same
pull request.

## GitHub Actions (pinned by commit SHA)

| Action | Pin | Release | Why |
|---|---|---|---|
| `actions/checkout` | `11d5960a326750d5838078e36cf38b85af677262` | v4.4.0 | Check out the repository; the same pin smart-trust-tools uses. |
| `actions/setup-python` | `a26af69be951a213d495a4c3e4e4022e16d87065` | v5.6.0 | Python 3.12 for the repository checks (standard library only). |
| `actions/setup-java` | `cf277c60eb25467037889841efdb72551f06f6c3` | v4.9.1 | Temurin JDK 17 to build the HCERT library; the same pin smart-trust-tools uses. |
| `gradle/actions/setup-gradle` | `748248ddd2a24f49513d8f472f81c3a07d4d50e1` | v4.4.4 | Gradle 8.14.3, the version smart-trust-tools builds with. |

## Runtime and build dependencies

| Dependency | Pin | Why |
|---|---|---|
| Kotlin HCERT library (`hcert-api`, `hcert-core`, JVM jars) | litlfred/smart-trust-tools at the commit and jar sha256 in [`lib/hcert/hcert.lock.json`](https://github.com/litlfred/smart-trust-demo/blob/main/lib/hcert/hcert.lock.json) | The library this demonstrator exists to exercise. Built from source by [`lib/hcert/build.py`](https://github.com/litlfred/smart-trust-demo/blob/main/lib/hcert/build.py) with smart-trust-tools' own `verification-metadata.xml` (Kotlin 2.0.21 Gradle plugin and its graph); no third-party runtime dependency beyond the Kotlin standard library. |
| SUSHI (`fsh-sushi` 3.20.1, 2026-08-18) and its npm graph | [`tools/ig-gen/package-lock.json`](https://github.com/litlfred/smart-trust-demo/blob/main/tools/ig-gen/package-lock.json) integrity, installed with `npm ci --ignore-scripts`, resolved with `--before` 14 days back | Builds the L3 IG from FSH (CI job `ig-sushi`). The HL7 tool every FHIR IG is built with; not reimplementable. |
| FHIR packages: `hl7.fhir.r5.core` 5.0.0, `hl7.terminology.r5` 7.0.1, `hl7.fhir.uv.extensions.r5` 5.3.0-ballot-tc1, `hl7.fhir.uv.tools.r5` 1.1.0, `smart.who.int.base` 0.2.0, `smart.who.int.trust-phw` 0.1.0 | sha512 in [`tools/ig-gen/fhir-packages.lock.json`](https://github.com/litlfred/smart-trust-demo/blob/main/tools/ig-gen/fhir-packages.lock.json), checked by `fhir_cache.py` before unpacking | The packages the IG's FSH is resolved against: FHIR R5 (as smart-trust and smart-trust-phw use), the three SUSHI provides for an R5 guide, and the WHO SMART guides the IG depends on. Taken from the registry.npmjs.org mirrors of the FHIR package registry, because SUSHI must not download at run time. |

The Android and OHS artifacts arrive in steps 4 and 5 of the [plan](plan.html).
