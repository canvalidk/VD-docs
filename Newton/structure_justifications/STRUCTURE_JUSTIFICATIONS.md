# Structure justifications — the mirror of the current entry structure

**Status:** provisional organisation guide, Claude-authored 2026-09-11 on the
user's instruction ("start putting in place the part of this stuff we
understand"). `ORGANIZATION.md` stays authoritative on every rule this guide
applies; this file records what the space is for, how it is stocked, and what is
still open. Revise in place as the shape firms up.

**Scope:** VD-docs only. The entry structure itself is produced in VD-Newton;
this space mirrors it, house by house, and compiles the justifications for each
house's current cut out of the Criticism History. Nothing here is authoritative
on what the entries *are*.

---

## 1. The two spaces (settled 2026-09-11)

Entry-structure criticism arrives from every branch — lesson work, Design 3,
Theory, Newton passes — and it is always about a **potential future decision**:
how the entries should be cut differently. That is why it cannot be organised
by nml or by E-number: any such tree encodes the *current* decision, and the
material inside it is the argument that the decision should change. The tree
would always be one reset behind its contents.

The resolution is two spaces with different lifetimes:

| | Space 1 — **Criticism History** | Space 2 — **Structure justifications** (this folder) |
|---|---|---|
| where | `Newton-analysis/criticism_history/` (on disk still `_dscn_entry_structure/` until the rename is run) | `Newton/structure_justifications/` |
| holds | records — every criticism of the entry structure, whatever branch wrote it | Newton's decisions per house, plus `-informing` copies of the criticisms that justify them |
| lifetime | accretes, immutable, chronological | redrafted every time Newton rules or resets |
| organised by | arrival; each record carries its *address* and its *fate* (see §3) | the **current** entry structure, one subfolder per law-house or seam |
| kind, in the model | records (a recorded exception: a bare folder of many records at branch level, neither discussion nor record-folder) | a workbench (a recorded exception: holds `-informing` copies and decision records together, is neither note nor discussion) |
| reader | anyone reconstructing *why* the cut looks the way it does; the mirror's curator | VD-Newton, writing entries house by house; anyone asking "why is this house cut this way, right now" |

History versus justification was the fork that produced this: a history never
changes and keeps the losers; a justification is pruned, cites only what won,
and is rewritten at each reset. They are two objects, not two candidates for
one folder.

## 2. The houses

One subfolder per law-house or seam of the Newton entry structure. The set is
provisional — it names the places the existing criticisms are addressed to, and
a house is added when a criticism addresses one that is not here:

| folder | what it is the justification of |
|---|---|
| `house_model/` | the six-entry house itself: chimney / triplet / two walls, every wall exposes an input, human inputs land at walls not triplets |
| `newton_I/` | the Newton I house: free-particle, inertial-frame, uniform-motion |
| `newton_I_II_seam/` | the seam: how many acceleration entries, why E7 and E8 are two headwords, where the lesson boundary falls |
| `newton_II/` | the Newton II house: inertial-acceleration / net-force / inertial-mass and their walls (including whether the net-force wall exists) |
| `force_sum/` | the Force-Sum house: net-force / interaction-set / impressed-force; generator and closer walls; the inverse orientation |
| `impressed_force_evaluation/` | behind the impressed-force wall: V(f), canonical-force acting-object, the orientation convention; action/reaction; the two acting-object architectures |
| `acting_object/` | the acting-object law: activation condition, dispatch, mechanical membership, no per-type laws, the branch mark |

Each house folder holds:

- **decision records** — Newton's rulings that shaped this house, as records
  (dated; the ruling document itself, ingested through a pass; or a short
  record stating the ruling and citing its source when no document exists);
- **`-informing` copies** of the Criticism History records that are
  load-bearing for the house's current cut, each pointing back home;
- optionally a **house justification** — one document, redrafted at each
  ruling, that says why the house is cut the way it is and cites the copies.
  When it exists it is the note-shaped object of this space; its `dN` bumps
  when Newton moves.

Folders are cosmetic; a house may be renamed or split freely. The house key
used in the catalog's `criticises` field is the folder name, so a rename here
is a catalog edit too.

## 3. The two fields a criticism carries

Written on the record's catalog row at intake into the Criticism History
(`ORGANIZATION.md`, *Entry-structure criticisms*):

- **`criticises`** — the house key(s) whose cut would change if Newton accepted
  the record. The test for whether a record is a criticism at all: *what would
  change if Newton accepted it?* A list of entries, walls or corners → it is.
  Something inside an entry (an estimator, a lumping criterion, which concrete
  acting objects exist) → it is not; that is another discussion's business,
  however much it talks about entries.
- **`at_commit`** — the entry structure the criticism was written against, by
  reference: `VD-Newton@<sha>` preferred; `VD-docs@<sha>` when that is what the
  record itself pins; `null` when unknown — never guessed.
- **`fate`** — `open` | `accepted` | `rejected` | `withdrawn` | `superseded`,
  with **`fate_ref`** naming the ruling (a Newton decision document, a commit,
  or the superseding record). A fate other than `open` is a ruling: it is
  written when Newton's answer comes back through a pass, and by the user.

## 4. The cycle (agreed 2026-09-11)

1. **Arrive** — `inbox/`; SORTING.md §0–1 (custody, filename, bank → normalize
   → hard gates). Unchanged.
2. **Recognise** — SORTING.md §2a: is it a criticism of the entry structure?
   If yes its home is the Criticism History whatever branch wrote it; the
   folder it came from keeps an `-informing` copy.
3. **Address** — write `criticises` and `at_commit` on the row.
4. **Argue** — if other records answer it, a discussion may be coined *inside*
   the history around that argument. This is the only point where a discussion
   exists here.
5. **Hand to Newton** — `outbox/VD-Newton/`, README, receipt. Unchanged.
6. **Fate** — Newton's ruling comes back through a pass; `fate` / `fate_ref`
   are written on the criticism's row, and the ruling document is ingested as
   a record into the history, dated.
7. **Restock the mirror** — *the new responsibility.* Triggered by step 6 or by
   a reset, never by step 1: with Newton's cut in hand, go house by house
   through this folder — add `-informing` copies of what is now load-bearing,
   surface as fossils what no longer is (never delete), redraft the house
   justification, bump its `dN`, pin the commit it mirrors.
8. **Loop** — the redraft is where gaps show (a house with no justification;
   two criticisms that conflict); those become the next criticisms into
   `inbox/`.

Steps 1–5 move files; steps 6–7 move claims. All the machinery the repo had
before 2026-09-11 was for the first kind.

## 5. State at creation (2026-09-11)

- Seven house folders created EMPTY (`.gitkeep` only). No copies stocked, no
  house justification written, no decision record ingested.
- The first restock is owed and needs, before a word is written, the current
  entry list from VD-Newton (the read token exists) so that `at_commit` on the
  mirror is real.
- Criticism History: the eight members of the former discussion carry
  `criticises` / `at_commit` / `fate` as of today, with the fates that are
  Claude's reading marked as such on each row and reversible. The nine nml
  candidates and the Design 3 strand are not yet moved in (the move list is
  with the user; the mount cannot rename from the sandbox this week).
- The rename `_dscn_entry_structure/` → `criticism_history/` is ruled and
  pending.

## 6. Open

- Whether the house justification is one document per house or one for the
  whole structure (the 08-21 "statement-record owed" is this document under its
  old label).
- Whether `fate` needs finer values (accepted-in-part is already the real
  state of the two 08-26 records: their triplet *names* were ruled at source,
  their structural claims were not).
- The trigger for step 7 in practice: every receipt, or only rulings that
  change a house.
- Whether this space is recorded as a new shape in its own right once it has
  run a full cycle, or stays an exception.
