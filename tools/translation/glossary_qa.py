#!/usr/bin/env python3
"""Translation QA report per locale, with glossary consistency from the layered glossaries.

Owner, 2026-11-06: "to the translations add a QA report... are terms in glossary
translated consistently? the layered glossaries should provide precedence for
fixed translation terms". The harness has no glossary-consistency check, so this
is the instance-side one, standard library only.

## Fixed terms, and which layer wins

A term's translation is FIXED when a glossary of a layer this instance mounts
already translates it: `<layer>/translations/<locale>/glossary/*.po` (the
`glossary:pot` catalogues) and `<layer>/translations/<locale>/glossary.po` (the
terminology hints `translation-block-qa` reads). Precedence: first the normative
reference glossaries named with `--layer` (WHO, smart-trust's GDHCN glossary —
normative content outranks the platform), then the order of `index.config.json`'s
`instances`, the most specific layer first (fhir-harness, then
folio-assistant-core, then cat-harness, which hosts bootstrap's terms), and the
instance's OWN `translations/<locale>/glossary.po` last: it may add terms,
never override one fixed above it. A layer's `#, localised` entry fixes nothing
(it says the term is localised, not how); an empty msgstr fixes nothing.

Only term LABELS are fixed (msgids under 60 characters that are not sentences);
a glossary definition is prose, not a term.

## What is checked, per locale catalogue (`translations/<locale>/**.po`)

- coverage: translated / total, fuzzy, against the `.pot` beside it;
- preservation: `{code…}`/`{lqd_…}` placeholders, `<aN>` tags, URLs;
- officiality: no header or manifest claims `official: true`;
- glossary consistency: every msgid that uses a fixed term (whole word, not part
  of an identifier such as `cat-harness` or a `{code}` span) must render it with
  the fixed translation. Matching is by word stem (inflection: ru, ar, fr, es) or
  substring (zh), so it is a reading aid with false positives, not a gate.
  A rendering that keeps the English term verbatim is reported apart, since that
  is right for a code or resource name (FHIR `Task`) and wrong in prose;
- an instance `glossary.po` entry that contradicts a fixed term (override).

The blind round-trip verdicts are the adjudicator's, read from
`test/results/translation-qa/roundtrip.json`; a script cannot reach one.

Usage:
  python3 -I tools/translation/glossary_qa.py [--layer NAME=GLOB ...] [--check]
  # writes test/results/translation-qa/<locale>.md and README.md;
  # --check exits 1 only on a placeholder/tag/URL loss or an official claim.
"""
import glob
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LOCALES = ["ar", "es", "fr", "ru", "zh"]
OUT = "test/results/translation-qa"


def unq(s):
    return re.sub(r'\\(.)', lambda m: {"n": "\n", "t": "\t", "r": "\r"}.get(m.group(1), m.group(1)), s)


def parse_po(path):
    """[(flags, comments, msgid, msgstr)] and the header text."""
    ents, header = [], ""
    text = open(path, encoding="utf-8").read()
    for block in re.split(r"\n{2,}", text):
        lines = [l for l in block.split("\n") if l and not l.startswith("#~")]
        if not lines:
            continue
        flags = " ".join(l for l in lines if l.startswith("#,"))
        comments = " ".join(l for l in lines if l.startswith("#.") or l.startswith("# "))
        v, field = {"msgid": "", "msgstr": ""}, None
        for l in lines:
            m = re.match(r'^(msgctxt|msgid|msgstr) "(.*)"$', l)
            if m:
                field = m.group(1)
                v[field] = unq(m.group(2))
            elif l.startswith('"') and field in v:
                v[field] += unq(l[1:-1])
        if v["msgid"] == "" and "msgid" in block:
            header = v["msgstr"]
            continue
        if v["msgid"]:
            ents.append((flags, comments, v["msgid"], v["msgstr"]))
    return ents, header


# ── the layers, in precedence order ─────────────────────────────────────


def layers(extra):
    cfg = json.load(open(os.path.join(ROOT, "index.config.json")))
    order = [i["name"] for i in cfg.get("instances", [])]
    out = []
    # Normative reference glossaries (WHO, smart-trust) outrank the harness layers.
    for spec in extra:
        name, pat = spec.split("=", 1)
        out.append((name, pat))
    for name in order:
        if os.path.isdir(os.path.join(ROOT, name, "translations")):
            out.append((name, os.path.join(ROOT, name, "translations", "{locale}", "glossary", "*.po")))
            out.append((name, os.path.join(ROOT, name, "translations", "{locale}", "glossary.po")))
    out.append(("(this instance)", os.path.join(ROOT, "translations", "{locale}", "glossary.po")))
    return out


def platform_layers():
    cfg = json.load(open(os.path.join(ROOT, "index.config.json")))
    return {i["name"] for i in cfg.get("instances", [])}


def is_label(msgid):
    return len(msgid) < 60 and not re.search(r"[.;:]\s|\.$", msgid) and not msgid.startswith("<")


def term_base(locale, extra):
    """{term_lower: (term, fixed, layer, file)} — first layer wins; plus overrides found."""
    base, overrides, seen_files = {}, [], set()
    for name, pat in layers(extra):
        for f in sorted(glob.glob(pat.format(locale=locale))):
            if f in seen_files or os.path.basename(f) == "glossary-page.po":
                continue
            seen_files.add(f)
            ents, _ = parse_po(f)
            for flags, _c, msgid, msgstr in ents:
                if not msgstr or "localised" in flags or not is_label(msgid):
                    continue
                k = msgid.lower()
                if k in base:
                    if name == "(this instance)" and norm(base[k][1], locale) != norm(msgstr, locale):
                        overrides.append((msgid, msgstr, base[k]))
                    continue
                base[k] = (msgid, msgstr, name, os.path.relpath(f, ROOT))
    return base, overrides


# ── matching ───────────────────────────────────────────────────────────

TASHKEEL = re.compile(r"[\u064B-\u0652\u0640]")


def norm(s, locale):
    s = unicodedata.normalize("NFC", s).lower()
    if locale == "ar":
        s = TASHKEEL.sub("", s)
        s = re.sub("[أإآ]", "ا", s).replace("ى", "ي").replace("ة", "ه")
    return s.replace("’", "'")


def stem(w, locale):
    if locale == "ru" and len(w) == 4:
        return w[:3]  # сеть / сети
    if len(w) <= 4:
        return w
    cut = 3 if (locale == "ru" and len(w) > 6) else 2
    return w[: max(4, len(w) - cut)]


def renders(fixed, msgstr, locale):
    t = norm(msgstr, locale)
    f = norm(fixed, locale)
    if locale in ("zh", "ar"):
        if locale == "ar":
            f = re.sub(r"(^|\s)ال", r"\1", f)
            return all(w in t for w in f.split())
        return f in t
    toks = re.findall(r"\w+", t)
    return all(any(x.startswith(stem(w, locale)) for x in toks) for w in re.findall(r"\w+", f))


def uses(term, msgid):
    """The term as a word of prose: not inside an identifier, a path or a placeholder."""
    clean = re.sub(r"\{[^}]*\}|`[^`]*`|https?://\S+", " ", msgid)
    flags = 0 if (term.isupper() and len(term) <= 6) else re.I  # an acronym is case-sensitive: DID is not "did"
    # ASCII boundaries: an Arabic proclitic (و, ب) attached to a Latin term is not part of it.
    return re.search(r"(?<![A-Za-z0-9_\-/.@])" + re.escape(term) + r"(?![A-Za-z0-9_\-/@]|\.\w)", clean, flags) is not None


# ── per-catalogue checks ────────────────────────────────────────────────

TOKS = [("placeholder", r"\{(?:code|lqd_)[^}]*\}"), ("tag", r"</?a\d+>"), ("url", r"https?://[^\s)\"<\u3000-\u303F\uFF08-\uFF09]+")]


def check_locale(locale, extra, verdicts):
    base, overrides = term_base(locale, extra)
    tdir = os.path.join(ROOT, "translations", locale)
    pots = sorted(glob.glob(os.path.join(tdir, "**", "*.pot"), recursive=True))
    cov = {"catalogues": 0, "templates": len(pots), "strings": 0, "translated": 0, "fuzzy": 0}
    losses, violations, verbatim, official, sense = [], [], [], [], []
    for pot in pots:
        po = pot[:-1]
        tpl, _ = parse_po(pot)
        cov["strings"] += len(tpl)
        if not os.path.exists(po):
            continue
        cov["catalogues"] += 1
        ents, header = parse_po(po)
        if re.search(r"Official:\s*true", header, re.I):
            official.append(os.path.relpath(po, ROOT))
        keys = {e[2] for e in tpl}
        for flags, _c, msgid, msgstr in ents:
            if msgid not in keys:
                continue
            if "fuzzy" in flags:
                cov["fuzzy"] += 1
            if not msgstr:
                continue
            cov["translated"] += 1
            for kind, rx in TOKS:
                a, b = re.findall(rx, msgid), re.findall(rx, msgstr)
                miss = [x for x in set(a) if a.count(x) > b.count(x)]
                if miss:
                    losses.append((os.path.relpath(po, ROOT), kind, miss, msgid))
            for k, (term, fixed, layer, _f) in sorted(base.items(), key=lambda kv: -len(kv[0])):
                if not uses(term, msgid):
                    continue
                if renders(fixed, msgstr, locale):
                    continue
                rel = os.path.relpath(po, ROOT)
                if uses(term, msgstr):
                    verbatim.append((term, fixed, layer, rel, msgid))
                elif layer in PLATFORM:
                    sense.append((term, fixed, layer, rel, msgid))
                else:
                    violations.append((term, fixed, layer, rel, msgid))
    for man in glob.glob(os.path.join(tdir, "**", "*.json"), recursive=True):
        try:
            j = json.load(open(man, encoding="utf-8"))
            if (j.get("status") or {}).get("official") is not False:
                official.append(os.path.relpath(man, ROOT))
        except Exception:
            official.append(os.path.relpath(man, ROOT) + " (unreadable)")
    return base, overrides, cov, losses, violations, verbatim, official, sense


PLATFORM = set()


def md_escape(s, n=110):
    s = s.replace("|", "\\|").replace("\n", " ")
    return s if len(s) <= n else s[: n - 1] + "…"


def report(locale, res, verdict):
    base, overrides, cov, losses, violations, verbatim, official, sense = res
    pct = 100.0 * cov["translated"] / cov["strings"] if cov["strings"] else 0.0
    L = [f"# Translation QA — {locale}", "",
         "Unofficial agent translation: no person has signed it off. Generated by "
         "`tools/translation/glossary_qa.py`; the round-trip verdict is the adjudicator's "
         "(`test/results/translation-qa/roundtrip.json`).", "",
         "## Summary", "",
         "| check | result |", "|---|---|",
         f"| coverage | {cov['translated']}/{cov['strings']} strings ({pct:.1f} %), {cov['catalogues']}/{cov['templates']} catalogues, {cov['fuzzy']} fuzzy |",
         f"| placeholders, tags, URLs | {'none lost' if not losses else str(len(losses)) + ' lost'} |",
         f"| officiality | {'nothing claims official' if not official else ', '.join(official)} |",
         f"| blind round trip | {verdict.get('verdict', 'not run')}{' — ' + verdict['summary'] if verdict.get('summary') else ''} |",
         f"| glossary: fixed terms | {len(base)} |",
         f"| glossary: normative or instance term not used (fix) | {len(violations)} |",
         f"| glossary: platform term rendered otherwise (sense check, not a violation) | {len(sense)} |",
         f"| glossary: English term kept verbatim (right for a code name, wrong in prose) | {len(verbatim)} |",
         f"| glossary: instance glossary.po overriding a fixed term | {len(overrides)} |", ""]
    if verdict:
        L += ["## Blind round trip", "",
              f"Sample: {verdict.get('sample', '?')}. Back-translator saw only the target text "
              f"(TOOLS_USED: {verdict.get('tools_used', '?')}); adjudicated against the source by "
              f"{verdict.get('adjudicator', 'the EN source session')} at {verdict.get('sha', '?')}.", ""]
        for d in verdict.get("drifts", []):
            L.append(f"- {d}")
        L.append("")
    L += ["## Fixed terms (layered glossaries, first layer wins)", "",
          "| term | fixed translation | layer | file |", "|---|---|---|---|"]
    for k in sorted(base):
        t, f, layer, file = base[k]
        L.append(f"| {md_escape(t, 50)} | {md_escape(f, 60)} | {layer} | `{file}` |")
    L.append("")
    if overrides:
        L += ["## Instance glossary.po entries overriding a fixed term", ""]
        for msgid, mine, (t, f, layer, file) in overrides:
            L.append(f"- `{msgid}`: instance has «{mine}», {layer} fixes «{f}» (`{file}`)")
        L.append("")
    if violations:
        L += ["## Renderings not using the fixed term", "",
              "Stem/substring matching: review each; a correct paraphrase is possible.", "",
              "| term | fixed | layer | catalogue | msgid |", "|---|---|---|---|---|"]
        for term, fixed, layer, rel, msgid in violations:
            L.append(f"| {md_escape(term, 40)} | {md_escape(fixed, 40)} | {layer} | `{rel}` | {md_escape(msgid)} |")
        L.append("")
    if sense:
        L += ["## Platform terms rendered otherwise — sense check", "",
              "A platform glossary (cat-harness, bootstrap, folio-assistant-core) fixes the term for the harness's own "
              "vocabulary; its entries carry no domain or sense, so in health-domain prose the same word may mean "
              "something else (\"Reference Architecture\", IHE \"actors\", health \"policy\"). Grouped by term:", "",
              "| term | platform fixed | layer | occurrences | example catalogue | example msgid |", "|---|---|---|---|---|---|"]
        groups = {}
        for term, fixed, layer, rel, msgid in sense:
            groups.setdefault((term, fixed, layer), []).append((rel, msgid))
        for (term, fixed, layer), occ in sorted(groups.items(), key=lambda kv: -len(kv[1])):
            L.append(f"| {md_escape(term, 40)} | {md_escape(fixed, 40)} | {layer} | {len(occ)} | `{occ[0][0]}` | {md_escape(occ[0][1])} |")
        L.append("")
    if verbatim:
        L += ["## English term kept verbatim", "",
              "| term | fixed | catalogue | msgid |", "|---|---|---|---|"]
        for term, fixed, layer, rel, msgid in verbatim:
            L.append(f"| {md_escape(term, 40)} | {md_escape(fixed, 40)} | `{rel}` | {md_escape(msgid)} |")
        L.append("")
    if losses:
        L += ["## Lost placeholders, tags or URLs", ""]
        for rel, kind, miss, msgid in losses:
            L.append(f"- `{rel}` {kind} {miss}: {md_escape(msgid)}")
        L.append("")
    return "\n".join(L) + "\n"


def main():
    argv = sys.argv[1:]
    extra = [argv[i + 1] for i, a in enumerate(argv) if a == "--layer"]
    check = "--check" in argv
    vpath = os.path.join(ROOT, OUT, "roundtrip.json")
    verdicts = json.load(open(vpath, encoding="utf-8")) if os.path.exists(vpath) else {}
    os.makedirs(os.path.join(ROOT, OUT), exist_ok=True)
    PLATFORM.update(platform_layers())
    rows, bad = [], 0
    for locale in LOCALES:
        if not glob.glob(os.path.join(ROOT, "translations", locale, "**", "*.po"), recursive=True):
            rows.append(f"| {locale} | no catalogues yet | | | | |")
            continue
        res = check_locale(locale, extra, verdicts.get(locale, {}))
        _b, ov, cov, losses, viol, verb, off, sense = res
        bad += len(losses) + len(off)
        if not check:
            open(os.path.join(ROOT, OUT, f"{locale}.md"), "w", encoding="utf-8").write(report(locale, res, verdicts.get(locale, {})))
        v = verdicts.get(locale, {}).get("verdict", "not run")
        rows.append(f"| [{locale}]({locale}.md) | {cov['translated']}/{cov['strings']} | {len(losses)} | {len(off)} | {v} | {len(viol)} / {len(sense)} / {len(verb)} / {len(ov)} |")
        print(f"{locale}: {cov['translated']}/{cov['strings']}, losses {len(losses)}, official {len(off)}, glossary {len(viol)} to fix / {len(sense)} sense-check / {len(verb)} verbatim / {len(ov)} overrides, round trip {v}")
    if not check:
        open(os.path.join(ROOT, OUT, "README.md"), "w", encoding="utf-8").write(
            "# Translation QA\n\nOne report per locale, from `tools/translation/glossary_qa.py`. Every translation here is "
            "unofficial (agent, no human sign-off).\n\n| locale | strings | lost tokens | official claims | blind round trip | glossary: to fix / sense check / verbatim / overrides |\n|---|---|---|---|---|---|\n"
            + "\n".join(rows) + "\n")
    if check and bad:
        sys.exit(1)


if __name__ == "__main__":
    main()
