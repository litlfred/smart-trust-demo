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

## Runtime and build dependencies

None yet. The HCERT library arrives in step 3 of the [plan](plan.md); the
Android and OHS artifacts in steps 4 and 5.
