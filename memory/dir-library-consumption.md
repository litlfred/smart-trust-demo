---
$schema: folio-memory/v1
id: dir-library-consumption
label: stable
summary: "Owner directive: consume the Kotlin HCERT library as jars built in CI from a pinned smart-trust-tools commit"
createdAt: 2026-10-23
---
Given by the owner on 2026-10-23, choosing between a Gradle composite build of a pinned checkout and a build in CI: "Build pinned jar in CI". The library is not yet on Maven Central. A script checks out litlfred/smart-trust-tools at a pinned commit, builds hcert-api and hcert-core (JVM) with that repository's own Gradle build and verification metadata, and publishes them to a build-local Maven directory the demo depends on, so the two builds' plugin versions and verification metadata stay separate.
