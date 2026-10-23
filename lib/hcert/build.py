#!/usr/bin/env python3
"""Build the Kotlin HCERT library's JVM jars from the pinned smart-trust-tools commit.

Reads hcert.lock.json beside this file, fetches exactly that commit (never a
branch), builds the jars with the library's own Gradle build, whose
gradle/verification-metadata.xml pins every artifact it resolves, and copies
them to lib/hcert/build/libs/. A jar whose sha256 differs from the lock fails
the build. [memory/dir-library-consumption, AGENTS.md]

  python3 lib/hcert/build.py                 # build and check against the lock
  python3 lib/hcert/build.py --update        # after changing "commit": record the new hashes
  python3 lib/hcert/build.py --source DIR    # use an existing checkout (must be at the commit)
"""
import argparse
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
LOCK = HERE / "hcert.lock.json"
OUT = HERE / "build"


def run(*cmd, cwd=None):
    print("+", " ".join(str(c) for c in cmd), flush=True)
    subprocess.run([str(c) for c in cmd], cwd=cwd, check=True)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checkout(lock):
    src = OUT / "src"
    if src.exists():
        shutil.rmtree(src)
    src.mkdir(parents=True)
    run("git", "init", "-q", cwd=src)
    run("git", "fetch", "-q", "--depth", "1", lock["repository"], lock["commit"], cwd=src)
    run("git", "checkout", "-q", "--detach", "FETCH_HEAD", cwd=src)
    return src


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--update", action="store_true", help="record the built jars' sha256 in the lock")
    ap.add_argument("--source", type=pathlib.Path, help="an existing smart-trust-tools checkout at the pinned commit")
    args = ap.parse_args()

    lock = json.loads(LOCK.read_text())
    src = args.source.resolve() if args.source else checkout(lock)
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=src, check=True, capture_output=True, text=True).stdout.strip()
    if head != lock["commit"]:
        sys.exit(f"{src} is at {head}, the lock pins {lock['commit']}")

    project = src / lock["gradleProject"]
    run("gradle", "-p", project, "--no-daemon", "-q", *(j["task"] for j in lock["jars"].values()))

    libs = OUT / "libs"
    libs.mkdir(parents=True, exist_ok=True)
    bad = []
    for name, jar in lock["jars"].items():
        dest = libs / name
        shutil.copyfile(project / jar["built"], dest)
        digest = sha256(dest)
        print(f"{digest}  {dest.relative_to(HERE.parents[1])}")
        if args.update:
            jar["sha256"] = digest
        elif digest != jar["sha256"]:
            bad.append(f"{name}: built {digest}, lock records {jar['sha256']}")
    if args.update:
        LOCK.write_text(json.dumps(lock, indent=2) + "\n")
    for b in bad:
        print(b, file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
