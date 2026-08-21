# VD folders — organization model

*Amended 2026-08-20: records and notes. The kind model below replaces the earlier
assumption that everything filed into a branch is an excavated note.*

## This is an idealized model, not a hard invariant

These are the rules the folders *aim* at. Because material is actively being
excavated — its true draft order, its identity, and even its correct branch are
often uncertain — we will fall short of these rules deliberately and often, and
will need workarounds. **A shortfall that is recorded (as an exception or a
workaround in the catalog) is acceptable and expected. Only an unrecorded
shortfall is a defect.**

## Records and notes

Every document in a branch is one of two kinds.

- A **record** is **terminal**: it is complete as what it is. Something was
  found, decided, corrected, or worked through, and the document records it. It
  needs no successor to be whole.
- A **note** is **directional**: it is aimed at a form it has not reached. We
  care about its *presentation* — pedagogy, notation, house style, audience — so
  successive drafts improve how it says the same thing.

**Record is the default.** Filing a document asserts nothing: no draft number,
no current, no direction. Note-hood is reached only by an explicit act of
recognition (below).

Both kinds live in **their own folder**, solo or not.

### The test, when a document has more than one file

Both kinds can accumulate files, so *how many files* decides nothing. Ask what
the successor **changed**:

- Says the same thing better → a **draft**. The idea is stable, the expression
  improves. That is note behaviour.
- Says something different, or fixes what was wrong → a **supersession**. The
  expression was not the point. That is record behaviour.

Two corollaries:

- A note has a **chosen** current draft; a record has a **determined** one. You
  may prefer an earlier rendering of a note (the human `alpha_and_the_one` d1 is
  current over its three polished variants); for a record the latest
  un-superseded version wins by definition, there is nothing to prefer.
- **Parallel variants are diagnostic of note-hood.** Several polished takes at
  one stage, none superseding the others, is something a record never has.

## Records

A record's folder may hold, besides the record itself:

- **Corrections** — a document that corrects the record while both stay live.
  Recorded as `corrects` / `corrected_by`. Corrections are bound into the same
  folder so they are read together.
- **Superseded versions** — a later version replaced the earlier one on content.
  Recorded as `supersedes` / `superseded_by`. The superseded file is kept, never
  archived away.
- **Renditions** — the same content in another format (a `.docx` export of a
  `.md`, a PDF of a draft). Recorded as `rendition_of`. A rendition is neither a
  draft nor a correction and takes no number.

Records take **no `dN` and no `current`**. There is no numbering scheme for them,
which is the point: nothing is asserted at intake, when least is known.

## Notes

- A note lives in **exactly one branch**. Iteration on a note happens only within
  that branch.
- Each note has **its own folder**; all of its drafts live there together.
- A note carries a **`direction`**: one line saying what publishable form it is
  being developed toward. A note without a direction is a record that has been
  relabelled.

## Drafts (notes only)

- Drafts are numbered **`d1`, `d2`, `d3` …** **in the catalog**. The `dN` is a
  catalog fact, not a filename requirement — see *Names* below. Legacy filenames
  carrying a `dN` suffix are kept as they are.
- The **current draft is normally the highest `dN`**, but the catalog is the
  source of truth, since a note's current draft is chosen rather than determined.
- **Parallel variants** held at the same stage (e.g. the alpha "gems") use `d2a`,
  `d2b`, … and/or a `variant` label — kept distinct from linear supersession.
- `dN` is an **identity, not a position**. If a file leaves a draft line — for
  instance a corrections document unbound from it and made a record — the
  remaining drafts keep their numbers and the **gap stands, recorded**.
  Renumbering would falsify every document that cites the old number.
- Old drafts are **never archived away** — they are live reference material for
  the next excavation pass.
- **`draft: unknown` is retired.** It existed because the model demanded a draft
  number at intake. A record makes no claim, so there is nothing to be unsure
  about; where the order is not known, the files are records.

## Promotion: record → note

Recognition is an **explicit event**, and it is the excavation act itself:

1. **Name the direction** — what form this is being developed toward.
2. **Declare which existing records are its drafts**, and in what order.
3. **Gather them** into the note's folder.

Promotion is **catalog-only**: it does not rename files (see *Names*). Record the
date of recognition and the reason.

A note is **not demoted** if its direction later dies. Recognition happened;
record the abandonment in the note field rather than rewriting the history.

**Grandfathering (2026-08-20):** a pre-existing note stays a note only if
someone *argued* it was one. Draft lines that were reasoned through survive
untouched; a lone `d1` that was assigned at intake, never argued, reverts to a
record — catalog-only, with folder and filename left alone.

## Names: files identify, folders label

- **The filename is the identifier.** References point at files, and a filename
  resolves to exactly one document. (Checked 2026-08-20: of 253 catalogued files,
  36 basenames repeat and every repeat is a copy of one document — no two
  distinct documents share a name.)
- **Renaming a file is the one genuinely breaking act.** It stays lossless and
  recorded via `orig_name`, and is not done casually.
- **Folders are cosmetic.** They may be renamed, nested, or regrouped freely —
  that is what they are for: making a thing legible, and binding a record to its
  corrections. Nothing addresses a folder.
- **Path prefixes in citations decay; filenames do not.** Cite the file and let
  the catalog resolve the path. A stale path prefix in a document body is
  recorded, not silently rewritten.

### Labelling notes in folder names (2026-08-20)

A note's folder is prefixed **`_note_`** — `_note_photon_frame_certification/`.
Records stay bare, because they are the overwhelming majority and marking the
minority is the cheaper convention. The underscore sorts the notes to the top of
a listing, as `_math_originals/` already does. (Capitalised folder names still
sort above them in some explorers; harmless.)

- The label is a **mirror, not a source.** `kind` in the catalog is
  authoritative; the prefix is derived from it. A folder name that asserts kind
  on its own authority is a second source of truth, and it will rot.
- **`note_name` does not take the prefix.** The object keeps its name; only the
  folder label carries the marker — which is what "folders are cosmetic" means.
- **Audit assertion:** every `_note_` folder contains at least one file with
  `kind: note`, and every file with `kind: note` sits in a `_note_` folder. Drift
  is then a defect rather than a quiet lie.
- **Recorded exception:** a note that does not own a folder cannot be labelled.
  `nml1_lesson` and `nml2_1_content_spec` live inside `nml1/` and `nml2.1/`
  alongside working notes, by the 2026-07-07 convention that keeps working notes
  flat and separates them in the catalog only. They stay unlabelled; the catalog
  carries their kind.

## Branch placement

- Every document should be **characteristically best-suited to its branch**.
- **Newton-analysis (ruling 2026-08-20, amending the 2026-07-07
  branch-character rule):** *if it is analysis of any type it belongs in
  Newton-analysis, unless it is more directly addressed to the Newton branch* —
  bug reports and to-do lists being the examples. Discussion about what the
  Newton entries should be belongs in Newton-analysis. The branch holds
  in-between material; it is **not** restricted to outward-facing publishable
  content, and the earlier wording that implied so is withdrawn.
- The **informs-flow** below is a *guide* for placement and hand-offs, not an
  enforced rule:
  - **Theory** → informs all other branches.
  - **Core** → informs all others except Theory.
  - **Newton-analysis** → informs at most Newton.
  - **Code**, **Newton** → position TBD.

## Hand-offs between branches (informs)

Documents may *look* like they're iterated across branches, but they aren't: a
branch produces a document whose purpose is to inform another branch, and the
receiving branch develops its **own separate** one from it.

- A document produced to inform another branch **stays in its home branch**.
- The hand-off is recorded as an **informs-link** in the catalog, and optionally
  as a **read-only copy placed in the receiving folder with an `-informing`
  suffix** (e.g. `some_source_note-informing.md`), pointing back to its home.
- `-informing` copies are explicit exceptions to "everything in a folder belongs
  to that object", and are **never edited in place** — edits happen only at home.
  Like any copy they can drift, so the catalog links them back for refresh.

## Catalog is the single source of truth

`catalog.yaml` carries everything filenames and folders can't. Fields (ones added
or changed by the 2026-08-20 kind model marked ‡):

- `path`, `type`
- `role`: primary | ai-context | reference | informing
- **‡`kind`**: `note`, or `record` when a document has been *reviewed and
  confirmed* a record. **Absent means record by default, not yet reviewed** —
  the default is never stamped, since stamping it would reassert the very claim
  the model stops making.
- **‡`direction`**: notes only — the form the note is developed toward. Required
  at promotion.
- `note_name`: the object (folder) a file belongs to — for records as well as
  notes, despite the name.
- `draft`: **notes only.** `d1`…, or null. (`unknown` retired.)
- `current`: true on the current draft of a note
- `variant`: variant label for parallel drafts, else null
- **‡`supersedes` / `superseded_by`**: records — a later version replaced an
  earlier one on content
- **‡`corrects` / `corrected_by`**: records — a correction bound alongside what
  it corrects
- **‡`rendition_of`**: same content, another format
- `orig_name`: filename before any rename
- `informs`: for an informing document, the home→target link
- `tags`, `project`, `status`, `dup_group`, `note`
- `math_normalized`: ISO date the file was math-normalized, or null
- `math_flags`: soft flags raised by normalization, else null

## Math normalization on intake

Every `.md` leaving `inbox/` for a branch is run through
`tools/normalize_math.py` first, converting LaTeX math delimiters to the
`$`/`$$` form VS Code renders. Order within a sort:

```text
bank -> normalize -> hard gates -> move -> catalogue
```

- The original is copied to `_math_originals/` **before** any edit, so a crash
  mid-run cannot lose it.
- **Hard-gate failure means the file does not move.** It stays in `inbox/` with
  the failure recorded, and is fixed at the source rather than worked around.
- Soft flags do not block the move; they are copied into the file's catalog
  `note`.
- Conversion is **in place**. Filenames are never tagged (no `_vscode` suffix) —
  provenance lives in the catalog and the bank.

Scope is deliberately narrow: math delimiters only, AI-authored markdown only.
Rationale, the rejected alternatives, and open items are in
`tools/MATH_NORMALIZATION_SPEC.md`.

`_math_originals/` is an explicit **exception** to catalog completeness: it
carries one folder-level entry rather than one entry per banked file, and the
catalog↔disk check skips that subtree. `MANIFEST.tsv` is its per-file record.

## Exceptions

Every rule here admits **recorded** exceptions. A recorded exception is fine; an
unrecorded one is a defect. When in doubt, record it in the file's `note` field.
