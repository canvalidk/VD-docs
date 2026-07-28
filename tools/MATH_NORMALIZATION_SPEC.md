# Math Normalization on Inbox Intake

**Status:** active. Spec ratified 2026-07-28; tool implemented and passing its corpus.
**Tool:** `tools/normalize_math.py` · **Corpus:** `tools/tests/math_normalize/`
**Supersedes:** `fix_vscode_markdown_math.py` (ad-hoc; silent-failure bugs — §1)

**Scope guard — deliberately narrow.** This runs **only** on AI-authored Markdown
being made renderable in VS Code. It is not a general Markdown formatter, not a
linter, and is not to be extended to other file types or other kinds of cleanup
without a new decision recorded here.

**Ratified decisions (2026-07-28):**

| Decision | Choice |
|---|---|
| Trigger | repo script + sort-step rule in `ORGANIZATION.md` |
| Aggression | inbox intake only; no repo-wide sweep of existing branch files |
| Filename tagging | none — no `_vscode` suffix; convert in place |
| Original preservation | **originals bank** committed to VD-docs (§2.2) |
| Tool + spec location | VD-docs, `tools/` |
| Local git working tree | leave as-is (folder is not a clone; pushes go clone-to-/tmp) |
| Render target | **VS Code / KaTeX only, for now** (§5.1) |

---

## 0. What this is for

VD Markdown arrives from several authoring surfaces. Some emit LaTeX delimiters
(`\( … \)`, `\[ … \]`); VS Code's Markdown preview renders KaTeX and wants
`$ … $` / `$$ … $$`. That conversion was being done by hand with a script that
produced output which *looked* converted and did not render.

Goal: any `.md` sorted out of `inbox/` is VS Code-renderable, with no filename
tagging, a mechanical guarantee the conversion did not damage anything, and a
recoverable original.

---

## 1. Why the previous script was replaced

Reproduced on a test corpus, 2026-07-28. Ordered by severity.

| # | Defect | Consequence |
|---|---|---|
| 1 | `f"…{converted.count(r'\[')}"` — backslash inside an f-string expression | **SyntaxError on Python ≤ 3.11** (PEP 701 is 3.12+). Did not run on the sandbox's 3.10. |
| 2 | `\( x \)` → `$ x $` | **Silent non-render.** KaTeX rejects whitespace-adjacent `$` (the currency guard). The script then reported `Remaining \( delimiters: 0` — success — on a file it had broken. |
| 3 | `\[` / `\]` matched only when alone on a line | Inline display math passed through unconverted |
| 4 | Inline code spans unprotected (only fenced blocks were) | `` `\(a\)` `` → `` `$a$` `` — corrupts literal source examples, of which VD docs have many |
| 5 | Fence tracking keyed on marker *char*, ignoring *length* | A ``` ``` ``` inside a ```` ```` ```` block closed it; conversion leaked into code |
| 6 | 4-space indented code blocks unprotected | same leak |
| 7 | Backslash escapes not respected | `\\(` → `\$` |
| 8 | No balance check | One unpaired `\[` emitted a lone `$$`, corrupting every block after it |
| 9 | Pre-existing `$` not escaped | `costs $5 … mass $m$` collided into one span |
| 10 | Reporting counted residual `\[` / `\(` | Meaningless as pass/fail — occurrences inside code fences *should* remain. Never checked `$` balance or parseability. |
| 11 | `_vscode` filename suffix | Encoded provenance in the worst available place (§2.1) |

Verified against the real renderer (`markdown-it` + `markdown-it-texmath` + `katex`):

```text
"the mass $ m $ is positive"                     -> plain text
"the mass $m$ is positive"                       -> RENDERS AS MATH
"the cart costs $5 and its mass $m$ is supplied" -> "costs 5 and its mass $m is supplied"
```

Defects 2 and 9 are load-bearing: both are **silent**, and neither would be
caught by a string-equality test. That is why gate 2 (§2.5) renders rather than
compares.

---

## 2. Design

### 2.1 Convert in place; no filename tag

The `_vscode` suffix existed to preserve the original. Of the three places that
fact could live — filename, catalog, bank — the filename is the worst: it
propagates into every reference to the doc, forces an `orig_name` entry to keep
the rename lossless, and outlives its usefulness. One instance already had to be
undone (`vector_division_inertial_mass_measurement_vscode.md`, 2026-07-27).

Instead: convert in place, filename untouched; record `math_normalized: <ISO
date>` on the file's `catalog.yaml` entry; keep the original in the bank (§2.2).

### 2.2 The originals bank

**Why a bank rather than git history.** Verified 2026-07-28: the "VD folders"
working folder contains a `.gitignore` but **no `.git`** — it is not a git
working tree. Pushes are made from a clone created elsewhere, using a
fine-grained token supplied per session. "Commit the original first, then
convert" would make every intake depend on a token being present, which it
usually is not. A mechanism unavailable in most sessions is not a safety
mechanism.

**Local-first, sync-later.** The bank is a plain folder in the working tree. A
copy lands there the instant a file is converted — no token, no network. It
rides to VD-docs on the next ordinary push. Safety is immediate, durability
eventual, and neither depends on the token.

**Layout.** Date-partitioned, original relative path preserved beneath it, so
nothing collides and provenance reads off the path:

```text
_math_originals/
  MANIFEST.tsv
  2026-07-28/
    inbox/NML2_1_CONTENT_d2_mass_estimation_integrated.md
```

**MANIFEST.tsv** — one row per banked file:

```text
date  original_path  final_path  sha256_before  sha256_after  tool_version  rules_applied  flags
```

Without this the bank is a pile nobody can fish anything out of. The two hashes
make "is the live file still the one we converted?" a one-line check.

**What gets banked.** Only files the tool actually modified. A file with no math,
or already normalized, is not copied — this keeps the bank small and meaningful.

**Prune policy.** A bank with no exit condition becomes a second unsorted inbox.
Entries prune only when **both** hold: the user has confirmed the converted file
renders correctly, **and** the entry is older than 90 days. Entries with
unresolved soft flags (§2.6) are **never** auto-pruned. Pruning is a separate
explicit command, never automatic during a conversion.

**Catalog treatment.** One **folder-level** entry in `catalog.yaml`'s `folders:`
section, not one per banked file, plus an exemption in the catalog↔disk
bijection check. Per-file entries would roughly double the catalog for no gain —
MANIFEST.tsv already carries the per-file record.

### 2.3 Mask, then transform

Every no-touch region is masked *before* any substitution and restored after:

1. fenced code blocks — **length-aware** (closing fence ≥ opener, per CommonMark), info-string tolerant
2. indented (4-space / tab) code blocks
3. inline code spans, including multi-backtick spans
4. backslash-escaped delimiters (`\\(`, `\\[`, `\\$`)
5. math already in `$` / `$$` form
6. HTML comment blocks and front matter

This kills defects 4–7 and 9 by construction rather than by patching. It is the
part most worth testing hard: a mask leak is invisible in the output.

### 2.4 Conversion rules

Applied only to unmasked regions, in this order:

| Rule id | From | To | Note |
|---|---|---|---|
| `escape-literal-dollar` | pre-existing literal `$` | `\$` | defect 9; runs **first**, before any new `$` exists |
| `inline-delim` | `\( … \)` | `$…$` | interior whitespace stripped — defect 2's fix, deliberately lossy |
| `display-delim-block` | `\[` / `\]` alone on a line | `$$` / `$$` | indentation preserved |
| `display-delim-inline` | `\[ … \]` within a line | `$$…$$` **in place** | defect 3. Verified that inline `$$…$$` renders, so prose is not restructured (§5.2) |

**Balance preflight.** If a delimiter family is unbalanced outside protected
regions, that family's rules are **not applied at all** and a flag is raised —
a half-converted pair corrupts every block after it (defect 8). Gate 5 then
blocks the file.

Rules are addressable by id, so one rule's edits can be reviewed independently.

### 2.5 Hard gates — mechanical, fail closed

All five must pass or **nothing is written** and the file stays in `inbox/`:

1. **Round-trip.** An in-memory edit journal, replayed backwards over the output, reproduces the input **byte-for-byte**.
2. **Parse.** Every math span in the output parses under KaTeX (`throwOnError: true`). A span that does not parse was mis-delimited. Requires `node` + `katex`; absent those the run fails closed unless `--no-render-check` is passed explicitly, which substitutes a weaker balance check.
3. **Skeleton invariance.** Replace every math span in input and output with a uniform placeholder, unescape `\$`, compare. Must be **byte-identical**. Proves the converter touched *only* math and that no mask leaked.
4. **Idempotence.** `normalize(normalize(x)) == normalize(x)`.
5. **Residual.** No `\(` or `\[` left outside protected regions. This is the meaningful version of what defect 10 was gesturing at, and it is what surfaces unpaired delimiters as a clear diagnostic.

Gates 1 and 3 are independent and check different properties — 1 proves
recoverability, 3 proves containment. Keep both.

**On bijection (considered, rejected).** Requiring `normalize` to be invertible
and gating on that was proposed and dropped: the transform is deliberately
non-injective (`\(x\)` and `\( x \)` must both give `$x$`; output `$$` may be
converted or original). A bijection gate would fail on exactly the files most
needing conversion, and spurious gates get waved through. The journal replaces
inference with a stored record, exact even for lossy rules.

**Journal lifetime: in-memory only.** With the bank as the durable recovery
artifact, the journal exists solely to run gate 1 and is discarded after.

### 2.6 Soft flags — needs a human eye

Do **not** block; written to the manifest's `flags` column and the file's catalog `note`:

- `literal-dollars-escaped:N` — pre-existing literal `$` found and escaped
- `unbalanced-display-delimiters` / `unbalanced-inline-delimiters`
- `display-math-inline` — `\[…\]` converted mid-line rather than as a block
- `empty-math-span`
- `mixed-delimiter-styles` — both LaTeX and `$` styles in one document

---

## 3. Integration with the inbox sort

Added to `ORGANIZATION.md`:

> **Math normalization on intake.** Every `.md` leaving `inbox/` for a branch is
> run through `tools/normalize_math.py` first. The original is copied to
> `_math_originals/` before any edit. Hard-gate failure means the file does
> **not** move — it stays in `inbox/` with the failure recorded. Soft flags do
> not block the move but are copied into the file's catalog `note`.

Order within a sort: **bank → normalize → hard gates → move → catalogue.** The
original is copied first, so a crash mid-run cannot lose it. Normalizing before
the move keeps a failed file in one predictable place.

Per-file catalog additions: `math_normalized` (ISO date or null) and
`math_flags` (list of soft-flag ids, else null).

Usage:

```sh
python3 tools/normalize_math.py check FILE...     # report only, never writes
python3 tools/normalize_math.py apply FILE...     # bank + convert + gate
```

---

## 4. Test corpus and results

`tools/tests/math_normalize/run_tests.py` — one case per defect in §1, plus
mask-leak and idempotence cases. Defects 2 and 9 assert against a **live KaTeX
render**, not a string match; string equality would not have caught either,
which is how they shipped.

As of 2026-07-28: **14 checks, 0 failed.**

Real-world sweep of all 177 `.md` in VD-docs (read-only `check`):

| Result | Count |
|---|---|
| clean — no math delimiters | 155 |
| would convert, all gates pass | 22 |
| blocked | 0 |
| soft flags raised | 0 |

---

## 5. Decisions and open items

### 5.1 Render target — RESOLVED
VS Code / KaTeX only, for now (user, 2026-07-28). **If this ever changes** —
GitHub rendering, pandoc, a published PDF pipeline — §2.4's rules table must be
revisited, not merely reconfigured. GitHub is stricter about `$$` block spacing
and would need a different `display-delim-inline` rule. Record the change here.

### 5.2 `\[…\]` on one line — RESOLVED
Converted in place to inline `$$…$$` rather than promoted to its own block.
Verified 2026-07-28 that inline `$$…$$` renders as math under the VS Code
delimiter set, so there is no reason to restructure the user's prose.

### 5.3 Open — prune confirmation
How does the user signal "this file renders fine" so a bank entry can be pruned?
A command, a manifest column edit, or the 90-day backstop alone. Undecided;
until decided, nothing prunes.

### 5.4 Open — the 22 unconverted branch files
The sweep found 22 already-homed files with unconverted delimiters (mostly the
`nml2` cluster and its ai-context bundles, plus `hookean_response_type_chain_d1`
and `glass_ball_mdp_example_d1`). All pass every gate, so conversion would be
clean. Ratified scope is **inbox intake only**, so they are deliberately left
alone. Reverse this only by an explicit decision recorded here.

Note that several are ai-context copies of the same source file; converting a
copy without its original would break the `dup_group` byte-identity the catalog
records. Any sweep must convert whole `dup_group`s together.

### 5.5 Open — `NML2_1_CONTENT_d2_..._VSCODE.md`
Produced by the old script. Checked 2026-07-28: no residual delimiters and no
space-adjacent `$`, so it escaped defect 2. It still carries the `_VSCODE`
suffix, which §2.1 retires; drop it when the file is homed.
