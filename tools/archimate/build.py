#!/usr/bin/env python3
"""Build the demonstrator's ArchiMate model: smart-ra's DPI-H RA model plus the overlay.

Usage:
    python3 -I tools/archimate/build.py            # write archimate/<version>/smart-trust-demo.archimate
    python3 -I tools/archimate/build.py --check    # fail if the committed model is not what the build makes

1. Fetch the two smart-ra files named in smart-ra.lock.json at its commit
   (into tools/archimate/.cache/, gitignored) and refuse any whose sha256
   differs from the lock.
2. Give the base model a view folder for the overlay and the demonstrator's
   model name; nothing else in it changes.
3. Apply overlay.py with smart-ra's own add_views.py.
4. Re-zip with fixed timestamps, so the output depends only on its inputs
   and --check can compare bytes.

The version is the IG's (sushi-config.yaml `version:`), as cat-harness's
archimate-models skill asks. Standard library only.
"""

import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
LOCK = json.loads((HERE / "smart-ra.lock.json").read_text(encoding="utf-8"))
CACHE = HERE / ".cache" / LOCK["commit"]
MODEL_NAME = "SMART Trust demonstrator on the WHO DPI-H Reference Architecture"
VIEW_FOLDER = "SMART Trust demonstrator"
FOLDER_ID = "id-5e1f0c1a7d0b5d3e9c2a4b6d8f0e1a2b"  # fixed: the overlay's view folder
FIXED_TIME = (2026, 1, 1, 0, 0, 0)


def version():
    m = re.search(r"^version:\s*(\S+)", (ROOT / "sushi-config.yaml").read_text(encoding="utf-8"), re.M)
    return m.group(1)


def sha256(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def fetch():
    files = LOCK["files"]
    want = [f["path"] for f in files.values()]
    if not all((CACHE / p).exists() for p in want):
        tmp = Path(tempfile.mkdtemp(prefix="smart-ra-"))
        url = f"https://github.com/{LOCK['repository']}"
        run = lambda *a: subprocess.run(["git", "-C", str(tmp), *a], check=True, capture_output=True)
        run("init", "-q")
        run("fetch", "-q", "--depth", "1", "--filter=blob:none", url, LOCK["commit"])
        run("checkout", "-q", "FETCH_HEAD", "--", *want)
        for p in want:
            (CACHE / p).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(tmp / p, CACHE / p)
        shutil.rmtree(tmp, ignore_errors=True)
    for name, f in files.items():
        got = sha256(CACHE / f["path"])
        if got != f["sha256"]:
            raise SystemExit(f"smart-ra {f['path']}: sha256 {got}, lock says {f['sha256']}")
    return CACHE / files["model"]["path"], CACHE / files["addViews"]["path"]


def prepare_base(src, dst):
    with zipfile.ZipFile(src) as z:
        xml = z.read("model.xml").decode("utf-8")
        others = {n: z.read(n) for n in z.namelist() if n != "model.xml"}
    xml, n = re.subn(r'(<archimate:model [^>]*?name=")[^"]*(")', lambda m: m.group(1) + MODEL_NAME + m.group(2), xml, count=1)
    if n != 1:
        raise SystemExit("base model: no <archimate:model name=...>")
    if f'<folder name="{VIEW_FOLDER}"' not in xml:
        m = re.search(r'\n  <folder [^>]*type="diagrams"[^>]*>', xml)
        close = xml.index("\n  </folder>", m.end())
        xml = xml[:close] + f'\n    <folder name="{VIEW_FOLDER}" id="{FOLDER_ID}">\n    </folder>' + xml[close:]
    write_zip(dst, xml.encode("utf-8"), others)


def write_zip(dst, model, others):
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in [("model.xml", model), *sorted(others.items())]:
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data)


def apply_bounds(xml):
    """Move the boxes overlay.py's VIEW_BOUNDS names to exact positions (x, width), in its views only.

    add_views.py lays boxes out left to right; this is the one step after it.
    A box is found by its element's id inside the named view, and only its own
    <bounds> (the first after its <child>) is changed.
    """
    spec = importlib.util.spec_from_file_location("overlay", HERE / "overlay.py")
    o = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(o)
    ns = uuid.uuid5(uuid.NAMESPACE_URL, o.NAMESPACE)
    eid = lambda key: o.EXISTING.get(key) or "id-" + uuid.uuid5(ns, "element/" + key).hex
    for view, boxes in getattr(o, "VIEW_BOUNDS", {}).items():
        m = re.search(r'<element xsi:type="archimate:ArchimateDiagramModel" name="%s" id="[^"]+">' % re.escape(view), xml)
        if not m:
            raise SystemExit(f"VIEW_BOUNDS: no view {view!r}")
        end = xml.index("\n      </element>", m.end())
        body = xml[m.end():end]
        for key, b in boxes.items():
            c = re.search(r'<child xsi:type="archimate:DiagramObject" id="[^"]+" archimateElement="%s"' % eid(key), body)
            if not c:
                raise SystemExit(f"VIEW_BOUNDS: {key} is not drawn in {view!r}")
            bm = re.compile(r'<bounds x="(-?\d+)" y="(-?\d+)" width="(\d+)" height="(\d+)"/>').search(body, c.end())
            x, y, w, h = bm.groups()
            new = f'<bounds x="{b.get("x", x)}" y="{y}" width="{b.get("width", w)}" height="{h}"/>'
            body = body[:bm.start()] + new + body[bm.end():]
        xml = xml[:m.end()] + body + xml[end:]
    return xml


def build(out):
    model, add_views = fetch()
    with tempfile.TemporaryDirectory() as t:
        base, applied = Path(t) / "base.archimate", Path(t) / "applied.archimate"
        prepare_base(model, base)
        r = subprocess.run([sys.executable, "-I", str(add_views), str(HERE / "overlay.py"), str(base), str(applied)],
                           capture_output=True, text=True)
        if r.returncode:
            raise SystemExit(r.stdout + r.stderr)
        with zipfile.ZipFile(applied) as z:
            xml = apply_bounds(z.read("model.xml").decode("utf-8")).encode("utf-8")
            others = {n: z.read(n) for n in z.namelist() if n != "model.xml"}
        out.parent.mkdir(parents=True, exist_ok=True)
        write_zip(out, xml, others)


def main(argv):
    target = ROOT / "archimate" / version() / "smart-trust-demo.archimate"
    if "--check" in argv:
        with tempfile.TemporaryDirectory() as t:
            fresh = Path(t) / target.name
            build(fresh)
            if not target.exists() or target.read_bytes() != fresh.read_bytes():
                raise SystemExit(f"{target.relative_to(ROOT)} is not current: run python3 -I tools/archimate/build.py")
        print(f"{target.relative_to(ROOT)}: current")
        return
    build(target)
    print(f"wrote {target.relative_to(ROOT)} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main(sys.argv[1:])
