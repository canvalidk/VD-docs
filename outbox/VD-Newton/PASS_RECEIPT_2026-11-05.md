# Pass receipt: 2026-11-05 (VD-Newton @ 61afb9e)

| | |
|---|---|
| From | VD-docs |
| To | VD-Newton |
| Date | 2026-11-05 |
| Source | His local clone of `canvalidk/VD-Newton`, branch `main` @ `61afb9ecf6f17a89ca6425e7e7642d6761531b05` ("Move the mass-estimator lab to the tester; clear to delete/ and passed copies"), staging folder `pass to VD-docs/`, plus one file written there after that commit and not yet tracked |
| Status | **Complete** for the 10 files the folder held. 7 ingested, 2 held at source, 1 declined. |

This receipt covers everything in `pass to VD-docs/` on 5 November. It replaces nothing: the 2026-09-08 and 2026-09-23 receipts beside it stand as issued. Eight of the documents were staged before 23 September but were untracked when those receipts were written, so no earlier receipt covers them. `THEORY_LOGICAL_STRUCTURE_2026-11-05.md` was written today. `equation.svg` was received on 23 September, and your side kept it at source because its hash did not match.

## 1. How the pass was handled

- **Read at his request.** His words: "Sort all the files you know what to do with. Look at pass to VD docs from other repos as well."
- **Hashes checked.** For each file, the full SHA-256 of the staged copy was compared with the file's blob at `HEAD`. They match for the nine tracked files. `THEORY_LOGICAL_STRUCTURE_2026-11-05.md` has no blob to compare against, since it was written at 22:03 the same evening and is untracked. Its hash is the one recorded at copy time.
- **Intake.** Each document was copied (not moved) into VD-docs `inbox/`, hash-checked again there, and put through math normalization. Eight were no-ops. `THEORY_LOGICAL_STRUCTURE_2026-11-05.md` got 5 inline-delimiter edits (`\(…\)` → `$…$`), passed every gate, and has its original banked in `_math_originals/2026-11-05/`. Each was then moved to its home and catalogued.
- **Homes by kind.**
  - The three 2026-09-08 documents and the 11-05 one justify core commitments: the authority's name, a theory's identity, and deduction as trace. Each went to its own **Theory** record folder.
  - The two 09-09 haze sources the 09-23 receipt asked for are in `Newton-analysis/_dscn_haze/`. They are now its earliest members.
  - The 09-09 proposal to change the Force-Sum triplet went to the **Criticism History**. Accepting it would change the house's corners. It was catalogued with `criticises: [force_sum]`, `at_commit: VD-docs@adfe14bb` and `fate: open`.
- **No relations bound.** Several records bear on earlier ones, such as the falsifiability analysis on the prediction-set synthesis. Binding those relations is the user's call.

## 2. Notes for your side

1. **Submission lines are stale from today.** Each document says it is "awaiting transfer" or "local handoff only". The managed copies are kept byte-identical to what you staged, except for the one normalized file, so those lines stay as written.
2. **Two files are HELD, not received:** `NML3_MEMBERSHIP_AND_SUMMATION_LOOPS_2026-09-07.md` and `NML3_INTERMEDIATE_EXPRESSION_TWO_APPROACHES_2026-09-09.md`. Their home is undecided. Each is about how the Force-Sum statement and its intermediate expression get built. It could be read as a criticism of the cut (Criticism History), as the start of the haze strand (`_dscn_haze`), or as neither. Keep them where they are. A later receipt will cover them.
3. **`equation.svg` is DECLINED.** It is mass-estimator material, and the custody of that material moved to `canvalidk/Mass-estimator-testor` on 2026-10-22. The tester already holds the received original at `docs/mass_estimator_equation/equation.svg` (sha256 `33440e89a20e…`). Your copy differs from it only by 79 CRLF line endings: stripping them reproduces the original hash exactly. Nothing is lost by deleting it at source.
4. **One link stops resolving.** `NML3_TOLERANCE_SPECIAL_ZERO_…` links to the remainder-triplet proposal and the two-approach record by relative path. In VD-docs the first is in another folder and the second is not held. Its link to the algorithm record resolves, because both are in `_dscn_haze/`.
5. **The BOTH HOLD steering file is no longer in the staging folder.** It left with the lab move (`61afb9e`), and the tester holds a context copy at `docs/vd-docs-context/`. VD-docs still holds its copy. Nothing here changes it.

## 3. Files

| # | Source path under `pass to VD-docs/` | SHA-256 at source | Disposition | VD-docs home |
|---:|---|---|---|---|
| 1 | `AUTHORITY_DICTIONARY_NAME_AND_ACCORDING_TO_RECONSTRUCTION_2026-09-08.md` | `a6f7b22aa13074fffeecdcbfeb22a176b3f0f5d594be7bbc452be1563b3f32f5` | Ingested; remove at source after repointing | `Theory/authority_dictionary_name/` |
| 2 | `AUTHORITY_NAMES_PREDICTION_SETS_AND_FALSIFIABILITY_2026-09-08.md` | `f568f8e9b607be1b5af3fbe1131b6ee59405806475c8652ccac9770a88bdb8d5` | Ingested; remove at source after repointing | `Theory/authority_names_and_falsifiability/` |
| 3 | `WHY_A_THEORY_NEEDS_AN_IMMUTABLE_OBJECT_AND_UNIQUE_ID_2026-09-08.md` | `0fbc7addb4aa9efc4c5308b1056f2e0ff73a5f5fd14205d47cea90a4a1455db3` | Ingested; remove at source after repointing | `Theory/theory_immutable_object_and_id/` |
| 4 | `THEORY_LOGICAL_STRUCTURE_2026-11-05.md` (untracked) | `303a2075aef834e4de9371927bb08d29dbc30e0f314c1829d076576ba6f676ac` | Ingested with math normalization (managed copy `36ed1abccf17…`); remove at source | `Theory/theory_logical_structure/` |
| 5 | `NML3_TOLERANCE_SPECIAL_ZERO_AND_NET_FORCE_UNCERTAINTY_DISCOVERY_2026-09-09.md` | `f48a21d76a3377379d0be66c7c351baabd941fbedfcf7efeec66555ff232c874` | Ingested; remove at source after repointing | `Newton-analysis/_dscn_haze/` |
| 6 | `NML3_REMAINDER_INTERMEDIATE_EXPRESSION_ALGORITHM_2026-09-09.md` | `ed548bd3b626011cf7477f63bce887fe3dd62d1dc756ffbde7f17586c02c1261` | Ingested; remove at source after repointing | `Newton-analysis/_dscn_haze/` |
| 7 | `NML3_REMAINDER_TRIPLET_AND_ACTING_OBJECT_DISCOVERY_PROPOSAL_2026-09-09.md` | `1a0220d08c3ac9f704f08dd73c739db53ef78e747a7bd8c97483b4cd9c08b586` | Ingested; remove at source after repointing | `Newton-analysis/criticism_history/` |
| 8 | `NML3_MEMBERSHIP_AND_SUMMATION_LOOPS_2026-09-07.md` | `d3e30ab25c3129d3efd20a95d2ecca78e193bb0527e7a70e0a23052f360ed929` | **HELD, not received.** Keep at source | — |
| 9 | `NML3_INTERMEDIATE_EXPRESSION_TWO_APPROACHES_2026-09-09.md` | `717be139453e7182fd3bd94520e062be26744c78bf791b5db435ed6d17aba578` | **HELD, not received.** Keep at source | — |
| 10 | `Mass estimator equation/equation.svg` | `2bc29432c3184af349b18add772dbbdc4aece51421291c7c6328f12011e06cf8` | **Declined.** Already homed in the tester (CRLF-only difference); delete at source | — (tester: `docs/mass_estimator_equation/equation.svg`) |

## 4. Applied on the VD-Newton side, same session

VD-Newton is now worked on only from the VD-docs project, and since 2026-10-20 Claude runs the outboxes of every repo, so this receipt was applied here rather than handed over as a prompt.

- **Rows 1–7 and 10 moved unchanged** into the workspace-root `to delete/` folder, under `to delete/pass to VD-docs/` with their paths kept. This follows the user's 23 September preference to collect safe-to-delete files rather than delete them. Each hash was checked before and after the move.
- **The two emptied subfolders were moved too**, into `to delete/empty_folders/`: `Mass estimator equation/` and `Mass estimator literature review/`.
- **Rows 8 and 9 stay** in `pass to VD-docs/`.
- **The closure is recorded** in VD-Newton's `AGENTS.md`.
- **Nothing is committed in VD-Newton.** The user commits and pushes.

If you are a VD-Newton session reading this later: check that `to delete/` still holds those eight files with the hashes above before anyone empties it.

---
*Issued from `outbox/VD-Newton/`. A record of VD-docs under the custody rule; this copy is permanent. The ledger entry is the 2026-11-05 paragraph of the `inbox` folder note in `catalog.yaml`.*

## Amendment, 2026-11-05 (later the same evening): row 4 is now tracked at source

At 22:55 a separate session pushed `THEORY_LOGICAL_STRUCTURE_2026-11-05.md` to `canvalidk/VD-Newton` `main` as `f64a886` ("Add Theory Logical Structure record to VD-docs handoff folder"). Its blob hash is `303a2075aef834e4de9371927bb08d29dbc30e0f314c1829d076576ba6f676ac`, the same as row 4, so the receipt stands unchanged. The file is no longer untracked, and `f64a886` is now the source commit for that row.

**Consequence for the local clone.** The local copy was moved to `to delete/pass to VD-docs/` before that push. When the clone pulls `f64a886`, the file reappears in `pass to VD-docs/`. It has already been received: confirm the hash above and remove it from `pass to VD-docs/` again (move it to `to delete/`, or delete it).
