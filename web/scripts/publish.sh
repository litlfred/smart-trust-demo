#!/bin/sh
# Build the VaxLink walkthrough from the current checkout and place it in the
# demonstrator's published site on gh-pages, at vaxlink/ (main) or
# branches/<branch>/vaxlink/ (any other branch), beside the site built from the
# same commit. Run it AFTER the site's own publish, which replaces the whole of
# branches/<branch>/ for a branch, and keeps vaxlink/ at the root because
# index.config.json declares it in the site's `keep`:
#
#   bun cat-harness-tools/scripts/stage-local.ts --repo . --publisher ig
#   sh web/scripts/publish.sh
#
# It refuses when the site at that place was built from another commit
# (folio-build.json): the walkthrough links into that site and shows its
# ArchiMate drawings. VAXLINK_ANY_SITE=1 publishes anyway.
#
# PUBLISH_BRANCH overrides the branch name (a detached checkout has none);
# PUBLISH_REMOTE overrides the URL pushed to. As every publish here, an agent
# runs it, not a workflow.
set -eu
cd "$(dirname "$0")/../.."
branch=${PUBLISH_BRANCH:-$(git rev-parse --abbrev-ref HEAD)}
remote=${PUBLISH_REMOTE:-$(git remote get-url origin)}
sha=$(git rev-parse HEAD)
rev=$(git rev-parse --short HEAD)
repo=$(basename "$(git remote get-url origin)" .git)

if [ "$branch" = main ]; then
  site=
else
  # The segment the site build uses (cat-harness-tools build-instance-site.ts stagingDir).
  seg=$(printf '%s' "$branch" | sed 's/[^A-Za-z0-9._-][^A-Za-z0-9._-]*/-/g; s/^-*//; s/-*$//')
  site=branches/$seg/
fi
dest=${site}vaxlink

(cd web && npm ci --ignore-scripts --no-audit --no-fund && VAXLINK_BASE="/$repo/$dest/" npm run build)

out=$(mktemp -d)
git clone -q --depth 1 --branch gh-pages "$remote" "$out"
stamp="$out/${site}folio-build.json"
if [ ! -f "$stamp" ]; then
  echo "no site at ${site:-the root} of gh-pages (no ${site}folio-build.json): publish the site first" >&2
  [ "${VAXLINK_ANY_SITE:-}" = 1 ] || exit 1
else
  built=$(node -e 'console.log(JSON.parse(require("fs").readFileSync(process.argv[1],"utf8")).source?.commit ?? "")' "$stamp")
  if [ "$built" != "$sha" ]; then
    echo "the site at ${site:-the root} was built from ${built:-an unknown commit}, not $sha: publish the site from this commit first" >&2
    [ "${VAXLINK_ANY_SITE:-}" = 1 ] || exit 1
  fi
fi

rm -rf "${out:?}/$dest"
mkdir -p "$out/$dest"
cp -r web/dist/. "$out/$dest/"

cd "$out"
git add -A
if git diff --cached --quiet; then
  echo "gh-pages already has the walkthrough built from $rev at $dest/"
  exit 0
fi
git -c user.name="${GIT_AUTHOR_NAME:-Claude}" -c user.email="${GIT_AUTHOR_EMAIL:-noreply@anthropic.com}" \
  commit -q -m "Publish the VaxLink walkthrough built from $rev ($branch) at $dest/"
git push -q "$remote" HEAD:gh-pages
echo "published the walkthrough built from $rev ($branch) at $dest/"
