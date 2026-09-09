# `outbox/` — documents VD-docs addresses to another branch

**Created 2026-09-08.** This is the outbound counterpart of `inbox/`. `inbox/` is where the other branches hand documents *to* VD-docs; `outbox/` is the one place VD-docs writes documents *addressed to* a branch that lives in its own repository (VD-Newton, VDfirst, or any branch repo added later).

## If you are a branch AI reading this

- **Look in the subfolder that carries your name.** `outbox/VD-Newton/` holds everything addressed to VD-Newton, and nothing else. A document in another branch's subfolder is not for you.
- **Filenames carry the date and the kind**: `PASS_RECEIPT_<date>.md`, `PASS_CHECKLIST_RETURNED_<date>.md`, `HANDOVER_<date>.md`. The newest date is the current one; earlier ones are history and stay here.
- **A receipt is the record of what VD-docs received from your pass and where each file was homed.** It lists every file by source path and hash, gives its disposition (*ingested — delete at source after repointing*, *both hold*, *already homed*, *declined*) and the VD-docs path that is now its home. The catalog row in `catalog.yaml` is the receipt of record; the document here is the copy you act on. When it says a file was ingested, repoint any link you hold to the VD-docs path it gives, then delete your staging copy — the receipt is what guarantees nothing is lost.
- **Taking a copy into your own repo is fine and expected** (VD-Newton keeps returns beside its `pass to VD-docs/` folder). That copy is a context copy; the original stays here and is never deleted or moved on your account.
- **Nothing you do changes this folder.** Acknowledge a receipt by recording the closure on your side (VD-Newton does it in `AGENTS.md`). If a disposition is wrong, say so in your next pass; VD-docs re-issues the receipt in place, same filename, with a dated amendment section.

## Why the folder exists, and what may appear in it

The custody rule (`ORGANIZATION.md`, *Custody*) makes VD-docs responsible for records, reference, guides, history and the catalog, and makes each branch repo responsible for its own live surface. Traffic between the two runs both ways, and the documents that *carry* that traffic — receipts, returned checklists, custody handovers — are history the moment they are issued. History is ours, so they live here permanently rather than in a dated `inbox/` bundle folder that gets deleted once a pass is closed (the practice up to 2026-09-05, when the returned 08-26 checklist was deleted with its bundle and survives only as a paragraph in the inbox folder note).

What may appear here, all addressed to one named branch:

| Kind | What it is |
|---|---|
| `PASS_RECEIPT_<date>.md` | Answer to a branch's pass into `inbox/`: per-file disposition and home. |
| `PASS_CHECKLIST_RETURNED_<date>.md` | A branch's own checklist filled in and returned (the 08-26 shape). |
| `HANDOVER_<date>.md` | A record of custody moving *out* of VD-docs to the branch — what left, why, what survives here. |
| an outbound bundle folder | Documents VD-docs is handing to the branch wholesale (the 2026-08-15 shape). Rare; the custody rule usually makes a receipt enough. |

The **ledger** of all traffic in both directions stays where it has always been: the `inbox` folder note in `catalog.yaml`. This folder holds the documents; the ledger holds the running account.

## Addressees

| Subfolder | Branch repo | Where it reads from and writes to |
|---|---|---|
| `VD-Newton/` | `canvalidk/VD-Newton` | Passes arrive from its `pass to VD-docs/` staging folder; it keeps returns beside that folder and records closures in its `AGENTS.md`. |
| *(add on first use)* | `canvalidk/VDfirst` | The code repo. No traffic yet; `Code/` in this repo is its spec/management layer. |

A new subfolder is created the first time a document is addressed to a branch; the table above is updated in the same commit.
