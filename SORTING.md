# Sorting guide — the questions in order

*Created 2026-08-25. This is the operational face of `ORGANIZATION.md`, which
stays authoritative on every rule this guide applies. Run the questions in
order for each document leaving `inbox/`.*

## 0. Is it ours to hold?

Custody is by kind (`ORGANIZATION.md`, *Custody*): records, reference, guides
and history are ours; the live production surface is VD-Newton's. A superseded
packet, pass or decision is history and comes here; a live one does not.

Byte-identical to an already-homed copy → delete the staging copy (dedupe
rule). VD-Newton's active copies are authoritative — ingesting a copy here is
never grounds to demote or delete the source. Decision records arriving in
transfer bundles are dropped uningested unless ruled otherwise.

## 1. Is the filename final?

Intake is the one cheap rename moment — nothing cites the file yet; after
sorting, renaming is the one breaking act (`orig_name`). Check the basename
against the catalog: no two distinct documents may share a name. The
mechanical steps run here: **bank → normalize → hard gates** — a hard-gate
failure means the file stays in `inbox/`, fixed at source.

## 2. Which branch?

The branch line: analysis of any type belongs in Newton-analysis, unless more
directly addressed to the Newton branch (bug reports, to-do lists). Otherwise:
characteristically best-suited branch.

## 3. New object — or a new version of an existing one?

The consequential question. If it succeeds something, the successor test
decides the binding: says the same thing better → **draft**, joining that
note's line with the next `dN`; says something different or fixes what was
wrong → **supersession**; fixes while both stay live → **correction**; same
content, another format → **rendition**. The last three bind into the existing
record's folder — and a record sitting flat in a discussion gains its own
folder at its first attachment, since the folder now has something to bind.

If it's genuinely new: it is a **record**. Stamp nothing — no kind, no `dN`,
no current. Note-hood only ever arrives by explicit recognition.

## 4. If a record: does it file into a discussion?

A filing choice, no test — an existing `_dscn_` folder, or coin a new one
(with the user; discussions are named at creation, not by the sorter). Depth:
flat unless it has attachments.

## 5. Does it inform something under development?

If it feeds a note's next draft (or hands off across branches): record the
`informs` link and place an **`-informing` copy** in the receiving workbench.
Independent of question 4 — the record stays home, possibly inside a
discussion; only the copy travels. A copy never lands inside a discussion or a
record's folder.

## Promotion out of a discussion

When a record in a discussion is promoted to note: **it leaves.** A new
`_note_` folder is created beside the discussion, at branch level. If the
promotion declares several discussion members as the note's drafts, all of
them leave together and are gathered. Members that feed the note without
being drafts of it **stay in the discussion**, and `-informing` copies of them
go into the new note folder. Nothing else in the discussion changes. The
physical side is all folder operations — free; the claim (direction, drafts,
order, date) lives in the catalog.

At demotion the mirror event occurs: the folder's `-informing` copies lose
their job and become fossils. A pass **surfaces fossils, never deletes them**
— deletion is a content change and stays the user's call.

## Exceptions

Many folders stand outside both the note and discussion rules — the `nml*`
working-notes folders (which hold folder-less notes by the 2026-07-07 flat
convention), `inbox/`, `tools/`, `_math_originals/`, and others. Do not force
them into either shape while sorting, and do not count them against the
audits. As everywhere: a recorded exception is fine; an unrecorded one is a
defect.

## Audits, run each pass

- No `-informing` file inside any discussion or any record's folder (fossils
  surfaced, not deleted).
- Every `_note_` folder holds a `kind: note` file and vice versa (recorded
  folder-less exceptions aside).
- When the pass touches one of the grandfathered notes still carrying
  `direction: null`, ask the user for its direction line — "state one at next
  touch" is standing.
