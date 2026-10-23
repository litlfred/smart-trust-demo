#!/usr/bin/env bash
# site.build sourceStep: copy the pages under docs/ (other than the home page,
# which the recipe's `home` places) into the Jekyll site source, keeping the
# proposals/ and upstream/ subfolders. As smart-trust-tools' site_docs.sh.
set -euo pipefail
src="${1:?usage: site_docs.sh <site source>}"
docs="$(cd "$(dirname "$0")/../../docs" && pwd)"
for f in "$docs"/*.md; do
  [ "$(basename "$f")" = index.md ] || cp "$f" "$src/"
done
for d in proposals upstream; do
  [ -d "$docs/$d" ] && mkdir -p "$src/$d" && cp "$docs/$d"/*.md "$src/$d/"
done
