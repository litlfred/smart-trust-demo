# French round-trip evidence (not for merge)

Untainted round trip of every French msgstr in `translations/fr/` (key
`<pot>#<n>` = nth non-empty msgid). Back-translators saw only the French (one
Read of a French-only file, one Write; TOOLS_USED recorded); adjudicators saw
only the English source and the back-translation, never the French.

- Round 1, 1729 strings: 1691 pass, 36 warn, 2 fail. Fails (A237 "who to
  share", C250 "so-what") and substantive warns fixed in 93e198e.
- Round 2, the 45 strings changed: 42 pass, 2 warn, 1 fail (C250), re-worded
  in 84a25a1 (not re-run).

Drift rule: synonyms, articles, re-ordering and equivalent terms are not drift;
a claim added, dropped, weakened, strengthened or reversed, or a term of art,
entity, number or quantifier changed, is. Verdicts are agent rulings; no human
has adjudicated. For the English session's independent check.
