#!/usr/bin/env python3
"""Repository checks that need nothing but the Python standard library.

- Every `uses:` in .github/workflows pins an action by a full commit SHA
  (a local `./` action is allowed). [AGENTS.md: dependencies are pinned]
- Every *.json file in the repository parses.
- Every Markdown file under memory/ has the folio-memory front matter.

Run from anywhere: python3 tools/repo-checks/repo_checks.py
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SKIP = {".git", "node_modules", "build", ".gradle", ".kotlin", "site"}
USES = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)")
PINNED = re.compile(r"^[^@\s]+@[0-9a-f]{40}$")


def files(pattern):
    for p in ROOT.rglob(pattern):
        if not SKIP.intersection(p.relative_to(ROOT).parts):
            yield p


def main():
    errors = []
    for wf in sorted(files(".github/workflows/*.y*ml")):
        for n, line in enumerate(wf.read_text().splitlines(), 1):
            m = USES.match(line)
            if m and not m.group(1).startswith("./") and not PINNED.match(m.group(1)):
                errors.append(f"{wf.relative_to(ROOT)}:{n}: action not pinned by commit SHA: {m.group(1)}")
    for js in sorted(files("*.json")):
        try:
            json.loads(js.read_text())
        except ValueError as e:
            errors.append(f"{js.relative_to(ROOT)}: invalid JSON: {e}")
    for md in sorted((ROOT / "memory").glob("*.md")):
        head = md.read_text().split("---")
        if len(head) < 3 or "$schema: folio-memory/v1" not in head[1] or f"id: {md.stem}" not in head[1]:
            errors.append(f"{md.relative_to(ROOT)}: missing folio-memory/v1 front matter with id {md.stem}")
    for e in errors:
        print(e, file=sys.stderr)
    print(f"repo-checks: {len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
