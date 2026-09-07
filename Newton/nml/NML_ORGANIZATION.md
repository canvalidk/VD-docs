# nml folders — default organisation (provisional)

*Created 2026-09-07. Provisional: this is the shape the nml folders are being
built up to, stated so that a new nml can be scaffolded from it without
re-deciding anything. `ORGANIZATION.md` at the repo root stays authoritative on
every rule this guide applies; where this guide records an exception, the
exception is the point.*

## The nml folders are exceptions, and stay exceptions

The note and discussion structures in `ORGANIZATION.md` were never meant to be
comprehensive — they are the first two structures that were described, not a
partition of everything. An nml folder as a whole is therefore **not** a note,
not a record and not a discussion, and is not forced into any of those shapes.
The custody exception (`ORGANIZATION.md`, *Recorded exception: the NML lesson
drafts* — homed here, shared with VD-Newton while a lesson is drafted) lives on
the nml folder and is unaffected by anything below.

What the ratified structures *do* cover is the inside of an nml folder. That is
what this default is.

## The default inside each nml folder

```text
nmlN/
  _note_nmlN_lesson/       the lesson draft line, as a note object
  _dscn_nmlN_content/      records that discuss what the lesson teaches
  _dscn_nmlN_exercises/    exercises, and files exclusively about exercises
  (flat)                   anything the three do not cover
```

**`_note_nmlN_lesson/`** — the lesson draft is a note in every respect the
model recognises: it is aimed at a form it has not reached (a teachable
lesson), successive drafts say the same thing better, and it takes `dN`s. The
folder holds the drafts and the note's workbench: `-informing` copies and the
drafting brief the lesson is written from. **It exists even when empty.** A
new nml gets this folder before it has a draft, as a note *created to write
into* — direction stated, `d1` not yet written. Recorded exception to the
audit assertion that every `_note_` folder holds a `kind: note` file: an nml
lesson note is exempt until its first draft lands.

**`_dscn_nmlN_content/`** — a discussion, so records only and no `-informing`
copies: the working notes, decision records, content specifications and
conceptual notes that discuss *what the lesson teaches*. A record with a
superseded version keeps its own folder inside (depth rule). This is where a
content specification lives when it is a record chain rather than a note.

**`_dscn_nmlN_exercises/`** — a discussion. The test is strict: a file goes
here only if it *is* exercises (a bank, a worksheet, a problem set) or
*exclusively* discusses exercises. A lesson add-on that carries problems is
content, not exercises. Created empty when nothing qualifies yet.

**Flat, at nml level** — whatever the three do not cover: a parent-level
record that defines the folder's own layers (the nml3 reset record), context
compilations with no note to serve, and anything ruled to stay flat.

## Scaffolding a new nml

When an `nmlN/` is asked for, create all of this at once, before any file
arrives:

1. `nmlN/_note_nmlN_lesson/` with a `.gitkeep`, a catalog folder entry, and
   the **standard direction line** below, written on the folder entry and on
   every draft row as it arrives.
2. `nmlN/_dscn_nmlN_content/` and `nmlN/_dscn_nmlN_exercises/`, each with a
   `.gitkeep` and a catalog folder entry.
3. Nothing else. Files are sorted in by the questions in `SORTING.md` as they
   arrive: lesson draft → the note (next `dN`); exercises → exercises; a record
   about the content → content; otherwise flat.

The `.gitkeep`s exist because git does not track empty directories; they are
exempt from the catalog↔disk bijection.

## The direction line (ruled 2026-09-07, identical on every nml lesson note)

> A single document giving a teacher, at any level of education from school to university, everything needed to design and deliver this lesson of the Newtonian-mechanics curriculum from the VD entries it covers: what it teaches and in what order, the exercises and demonstrations, the misconceptions to expect, and how the lesson adapts across levels.

Two consequences the user accepted with it: a content specification is
upstream material that eventually disappears into the lesson document, so it
files as a record chain in the content discussion; and a rendering of the
lesson at another level of education is part of the lesson note, not a
separate object (this reaches nml3's younger-student mock lesson and add-on,
left in content until the nml3 draft arrives).

## What is applied without asking, and what is ruled

Applied by the sorter: the three-folder scaffold; routing by the tests above;
the successor test on a content specification's versions; `-informing` copies
into the lesson note's workbench once that note exists; layer information
carried as tags when a layer subfolder is dissolved.

Ruled by the user: whether a non-lesson
object in an nml (a content spec, a mock lesson for another audience) is a
note; anything that leaves an nml folder for another branch.

## State at creation (2026-09-07)

| nml | lesson note | content | exercises | notes |
|---|---|---|---|---|
| nml1 | d1, d2 (current) | 2 records | empty | — |
| nml2 | d1, direction abandoned at the 07-11 split | 3 records | the question/exercise bank | parent of 2.1 and 2.2 |
| nml2.1 | d1 + brief + 10 informing copies | `nml2_1_content_spec/` (d1 → d2, record chain) | empty | content spec ruled a record chain by the successor test — reversible |
| nml2.2 | empty (created to write into) + brief + 4 informing copies | pre-water inventory | empty | — |
| nml3 | empty (created to write into) | 10 records, layers kept as tags | primitive exercise bank | draft lives in VD-Newton; reset record flat |

Still parked at `nml/` root: the Newton-III worksheet (no nml holds Newton III
yet), the pedagogy doctrine, and the generic seed set in `lesson-design-context/`.
All five lesson notes carry the ruled direction line above.
