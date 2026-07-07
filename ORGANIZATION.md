# VD folders — organization model

## This is an idealized model, not a hard invariant

These are the rules the folders *aim* at. Because notes are actively being
excavated — their true draft order, their identity, and even their correct
branch are often uncertain — we will fall short of these rules deliberately and
often, and will need workarounds. **A shortfall that is recorded (as an
exception or a workaround in the catalog) is acceptable and expected. Only an
unrecorded shortfall is a defect.**

## Scope: these are rules for *excavated notes*

A **note** is an idea being dug out over successive drafts. This model governs
excavated notes specifically.

- **Newton-analysis** and **Theory** are *mostly* excavated notes.
- **Core**, **Code**, and **Newton** contain excavated notes too, but also other
  structures — specs, rule ledgers, entry sets, compiled releases, code-context
  copies — that these rules do **not** force into note-shape.

When a folder isn't an excavated note, this model doesn't apply to it.

## The note

- A note lives in **exactly one branch**. Iteration on a note happens only
  within that branch.
- Each note has **its own folder**. All of the note's drafts live in that folder
  together.
- Membership in the folder is what marks a file as a draft of that note.

## Drafts (versioning)

- Drafts are numbered **`d1`, `d2`, `d3` …**, appended as a suffix to the
  original filename, which is otherwise kept intact:
  `nothing_vs_zero_somethings_d1.md`.
- The folder tells you *which note*; the `dN` tells you *draft order*. The
  **current draft is the highest `dN`**, but the catalog is the source of truth
  (for cases where "current" isn't simply "highest", or the order is unknown).
- **Assign `dN` only when the order is confident.** Where the order is unknown,
  leave the filename untouched and record `draft: unknown` in the catalog rather
  than guessing.
- **Parallel variants** held at the same stage (e.g. the alpha "gems") use
  `d2a`, `d2b`, … and/or a `variant` label in the catalog — kept distinct from
  linear supersession.
- Renaming to add `dN` is purely additive and **lossless**: the catalog records
  each file's original name so the change is reversible.
- Old drafts are **never archived away** — they are live reference material for
  the next excavation pass.

## Branch placement

- Every note should be **characteristically best-suited to its branch**. A
  misfiled note is considered incorrect until relocated. (Relocation is deferred
  while cross-branch moves are paused.)
- The **informs-flow** below is a *guide* for placement and hand-offs, not an
  enforced rule:
  - **Theory** → informs all other branches.
  - **Core** → informs all others except Theory.
  - **Newton-analysis** (output) → informs at most Newton.
  - **Code**, **Newton** → position TBD.

## Hand-offs between branches (informs)

Notes may *look* like they're iterated across branches, but they aren't: a branch
produces a note whose purpose is to inform another branch, and the receiving
branch develops its **own separate note** from it.

- A note produced to inform another branch **stays one note in its home branch**.
- The hand-off is recorded as an **informs-link** in the catalog, and optionally
  as a **read-only copy placed in the receiving note's folder with an
  `-informing` suffix** (e.g. `some_source_note-informing.md`), pointing back to
  its home note and draft.
- `-informing` copies are explicit exceptions to "everything in a note folder
  belongs to that note", and are **never edited in place** — edits happen only in
  the home note. Like any copy they can drift, so the catalog links them back for
  refresh.

## Catalog is the single source of truth

`catalog.yaml` carries everything filenames and folders can't. Fields (new ones
for this model marked +):

- `path`, `type`
- `role`: primary | ai-context | reference | **+informing**
- **+`note_name`**: the note (folder) a file belongs to (distinct from the
  pre-existing free-text `note` field listed below)
- **+`draft`**: draft number (`d1`…), `unknown`, or null (not a draft)
- **+`current`**: true on the current draft of a note
- **+`variant`**: variant label for parallel drafts, else null
- **+`orig_name`**: filename before a `dN` suffix was added
- **+`informs`**: for an informing note, the home→target link
- `tags`, `project`, `status`, `dup_group`, `note`

## Exceptions

Every rule here admits **recorded** exceptions. A recorded exception is fine; an
unrecorded one is a defect. When in doubt, record it in the file's `note` field.
