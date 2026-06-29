# Token Prop 2: The Pipe-Plural Convention

**Date:** 2026-03-09
**Status:** VERIFIED — working in engine, tested on Newton v0.5

---

## Convention

To pluralise a headword reference in a definition, write `headword|s`.

Examples:
- `point-particle|s` → matches headword `point-particle`
- `interaction-candidate|s` → matches headword `interaction-candidate`
- `acting-force element|s` → matches headword `acting-force` (pipe is on "element", not the headword, but `acting-force` still matches at the preceding space boundary)

## Why it works

The pipe character `|` is already in the tokeniser's delimiter set. The matching rule is: a headword matches only when the character before it and the character after it are both delimiters (or start/end of string).

So `point-particle|s` has:
- Left boundary: space (delimiter) or start of string
- Right boundary: `|` (delimiter)
- Match succeeds. The `|s` becomes residue.

Meanwhile `point-particles` (no pipe) has:
- Right boundary: `s` — NOT a delimiter
- Match fails. "point-particles" is never recognised as containing the headword.

No special-casing was added. The convention is purely an authoring practice that exploits the existing delimiter rule.

## Test results

| Input | Headword | Match? | Reason |
|---|---|---|---|
| `point-particle\|s` | `point-particle` | YES | `\|` is delimiter boundary |
| `point-particles` | `point-particle` | NO | `s` is not a delimiter |
| `interaction-candidate\|s` | `interaction-candidate` | YES | same mechanism |
| `acting-force\|s` | `acting-force` | YES | same mechanism |
| `acting-force element\|s` | `acting-force` | YES | space boundary before "element" |

## Note on norm notation

Mathematical norm notation `||v(t)||` contains pipes. These are harmless — the pipes create delimiter boundaries around `v`, `t`, etc., but none of those match any headword. No action needed; just be aware that `||` in definitions is parsed as two consecutive delimiters.

## Entries using this convention (Newton v0.5)

- E12 (`relative-position`): `point-particle|s`
- E13 (`relative-velocity`): `point-particle|s`
- E24 (`net-force`): `acting-force element|s`
- E25 (`interacting-forces-set`): `acting-force element|s`
- E43 (`interaction-pair`): `interaction-candidate|s`

## Rule ledger placement

This convention is an authoring practice, not a core rule. It belongs under R-TOK-00 (tokenizer interface) as a usage note, or as a new practice entry P-13 in the practice ledger.

Suggested wording: "To reference a headword in its plural form within a definition, write `headword|s`. The pipe acts as a delimiter boundary, allowing the tokeniser to match the headword while the trailing `s` falls into residue."
