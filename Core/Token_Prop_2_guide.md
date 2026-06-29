# Token Prop 3: VD Entry Authoring Guide

**Date:** 2026-03-10
**Status:** ACTIVE — supersedes Token Prop 1 and Token Prop 2
**Scope:** How to name headwords and write definitions so the tokeniser produces correct dependency edges.

---

## What the tokeniser does

The tokeniser has one job: given a definition string and the set of all headwords in the dictionary, it reports which headwords appear in that definition. That's it. Each match becomes an edge in the dependency graph. The tokeniser does not interpret meaning, track classes, or infer relationships — those belong to the human reader.

## How the tokeniser works

1. Normalise the definition (collapse whitespace, tidy parenthetical formatting).
2. Sort all headwords longest-first.
3. For each headword, scan the definition for exact matches at **delimiter boundaries** — the character before and after the match must both be delimiters (or start/end of string).
4. When a match is found, **blank** that region so shorter headwords can't re-match the same text.
5. Whatever remains after all headword matches is **residue** — ordinary words the tokeniser doesn't track.

Self-references (a headword appearing in its own definition) are detected but discarded. They don't create edges.

## The delimiter set

```
space  tab  newline  . , ; : ! ? / = + * < > [ ] { } ( ) | " ' – — − # @ & ^ ~
```

Everything else (letters, digits, hyphen `-`, underscore `_`) is **not** a delimiter.

The two critical non-delimiters:
- **Hyphen `-`** — glues words together. `inertial-frame` is one token.
- **Underscore `_`** — attaches qualifiers. `canonical-force_acting-object` is one token.

---

## How to name headwords

### Single words
Just write them plain. `time`, `velocity`, `acceleration`, `position`, `speed`.

These match anywhere they appear in a definition at delimiter boundaries.

### Compound names
Hyphenate all words. `reference-frame`, `point-particle`, `uniform-motion`, `straight-line`.

The hyphen makes the whole string one atomic token. The tokeniser will never match part of it — either the whole thing matches or nothing does.

### Qualified names (subscript convention)
Use underscore to attach a qualifier: `canonical-force_acting-object`, `activation-condition_acting-object`, `paired-particle_acting-object`.

Read the underscore as a subscript: "canonical force, subscripted by acting object." The entire string including the qualifier is one atomic token.

### Arguments
Drop them. Don't put `(p,t)` or `(x,C)` or `(I)` in headwords.

Parentheses are delimiters, so `net-force(p,t)` would match as `net-force` followed by delimiter-bounded residue `p`, `,`, `t`. The arguments aren't part of the headword identity. Put them in the definition prose instead.

| Don't write | Write instead |
|---|---|
| `net force(p,t)` | `net-force` |
| `instance of(x,C)` | `instance-of` |
| `class specific features(C)` | `class-specific-features` |
| `uniform motion on interval(I)` | `uniform-motion` |

---

## How to write definitions

### Referencing a headword: hyphenate it

To create a dependency edge, write the headword exactly as it's named — with hyphens.

```
A reference-frame in which every free-particle exhibits uniform-motion.
```

This definition creates three edges: → `reference-frame`, → `free-particle`, → `uniform-motion`.

### Not referencing: leave it unhyphenated

If you use a phrase from natural language without wanting a formal reference, don't hyphenate.

```
A reference frame standard for Newtonian analysis of motion.
```

Here "reference frame" (with space) does NOT match the headword `reference-frame`. No edge is created. The words "reference" and "frame" both become residue.

This is the **opt-in principle**: the author controls which edges exist by choosing whether to hyphenate. The tokeniser never guesses.

### Plurals: use pipe

To reference a headword in plural form, write `headword|s`.

```
For two point-particle|s in the same reference-frame...
```

The pipe `|` is a delimiter, so the tokeniser sees `point-particle` followed by a delimiter boundary. Match succeeds. The `s` falls into residue.

Without the pipe, `point-particles` would fail — the `s` directly after `point-particle` is not a delimiter, so there's no right boundary.

| Write | Matches? | Why |
|---|---|---|
| `point-particle\|s` | YES | `\|` is a delimiter boundary |
| `point-particles` | NO | `s` is not a delimiter |
| `acting-force\|s` | YES | same mechanism |
| `interaction-candidate\|s` | YES | same mechanism |

### Qualified headwords in definitions

Write them exactly as named: `canonical-force_acting-object`, `activation-condition_acting-object`.

Longest-match-first ensures the full qualified name matches before any shorter headword (like `acting-object` on its own) gets a chance. After the full match is blanked, the shorter headword can't re-match the blanked region.

### Formula shorthand

In **triplet entries**, replace all formula shorthand with the actual headword so the tokeniser picks up the edge:

| Don't write | Write instead |
|---|---|
| `a = F_net/m` | `inertial-acceleration equals net-force divided by inertial-mass` |
| `F_net = m · a` | `net-force = inertial-mass times inertial-acceleration` |

In **non-triplet entries** (scaffold, walls, chimneys), shorthand like `m`, `a`, `F`, `p`, `t` is fine. These don't need edges for law detection. Shorthand entries can be added later if needed (e.g. `E_new: m := shorthand for inertial-mass`).

### Arguments in definitions

Since arguments are dropped from headwords, you still use them freely in definition prose:

```
net-force on particle p at time t is the vector sum of the acting-force element|s
in the interacting-forces-set for p at t.
```

Here `(p,t)` style arguments appear as natural language. The parentheses are delimiters, so they don't interfere with headword matching.

---

## Triplet discipline

A law is detected when three headwords form a 3-cycle in the dependency graph AND satisfy the temporal constraint (one previously-defined anchor, two new winter words). The engine requires each triplet entry to reference **both** other trio members. This means:

- The November (anchor) redefine must mention both winter words.
- Each winter word's definition must mention the anchor and the other winter word.

If any corner references only one of the other two, the law is not recognised. This is strict by design — it catches spurious cycles that happen to share edges with other laws.

**Check your triplet entries.** For each entry in a triplet, confirm it contains both other headwords hyphenated. This is the most common authoring mistake.

---

## Summary of conventions

| Convention | Example | Effect |
|---|---|---|
| Hyphen in headword | `inertial-frame` | Compound name, one atomic token |
| Underscore in headword | `canonical-force_acting-object` | Qualifier/subscript, one atomic token |
| No arguments in headword | `net-force` not `net force(p,t)` | Arguments are prose, not identity |
| Hyphenate in definition | `...an inertial-frame...` | Creates dependency edge |
| Don't hyphenate in definition | `...an inertial frame...` | No edge (prose use) |
| Pipe for plural | `point-particle\|s` | Matches headword, `s` is residue |
| Spell out in triplets | `net-force = inertial-mass times...` | Ensures 3-cycle closes |

---

## Pitfalls

**Plural without pipe.** `point-particles` → no match. Always use `point-particle|s`.

**Forgetting to hyphenate a reference.** `"exhibited by a free particle"` → no edge to `free-particle`. If you want the edge, write `free-particle`.

**Accidental reference.** If your definition mentions `acting-force` but you only meant it as prose, you'll create an unwanted edge. Use "acting force" (unhyphenated) to avoid this.

**Norm notation.** `||v(t)||` contains pipes. Harmless — `v` and `t` don't match any headword. Just be aware.

**Partial matches blocked.** `"particle"` does NOT match `point-particle`. `"force"` does NOT match `acting-force` or `net-force`. The full hyphenated string must appear.

**Underscore qualifier overlap.** `acting-object` as a standalone headword is NOT matched inside `canonical-force_acting-object`, because longest-match-first blanks the full qualified name first. This is correct and intentional.
