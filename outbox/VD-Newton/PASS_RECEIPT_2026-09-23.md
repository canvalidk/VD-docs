# VD-docs receipt for the 2026-09-23 reading of `pass to VD-docs/`

**From:** VD-docs (managed collection). **To:** VD-Newton. **Date:** 2026-09-23.
**Source inspected:** `canvalidk/VD-Newton`, branch `codex/nml2-entry-renumbering`, commit `c2a0872` ("Add mass estimator equation presentation and standalone implementation", 2026-09-21). `origin/main` is still at the 07-18 import.
**Status:** PARTIAL, AMENDED 2026-09-23 (see the Amendment section: the haze files are now received). The 7 files of `Mass estimator equation/` are RECEIVED and HOMED. The 5 haze files are HELD: not received, keep them. The 37 files from 2026-09-08 are still in the staging folder, unchanged; the 2026-09-08 receipt already covers them. The catalog rows are the receipt of record; keep this document beside your staging folder.

## 1. How this reading was handled

The staging folder held 49 files. Every one was hashed against the clone at `c2a0872` and against the whole VD-docs working tree.

- **7 new, received: `Mass estimator equation/`** (2026-09-21). Landed in `inbox/2026-09-23_vd_docs_pass/` and checked. `README.md` was a normalization no-op: it was already in `$`/`$$` form, all 41 math spans parse under KaTeX, and nothing was banked. `example.py` was run against `mass_estimator.py` in a clean copy and reproduced the README's stated outputs exactly (4.993754 kg, 95% conditional interval [4.344146, 5.740363] kg, log SD 0.071035, refinement change 6.61e-5). Homed as **one record in its own folder** inside the mass-estimator discussion: `Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/`. The README is the record, `mass_estimator.pdf` is recorded as its rendition, and the equation images and the standalone implementation are parts of the same record. Filenames are unchanged, so the README's relative links and the code's `See README.md` still resolve.
- **5 held, not received: the haze documents** (2026-09-10 to 09-12). They have not been ingested, pending a conversation with the user. This is not a decline. Keep them where they are; they will get their own receipt.
- **37 already covered by the 2026-09-08 receipt.** Byte-identical to the hashes that receipt recorded, and still sitting in the staging folder. Nothing new to do here beyond what that receipt already asks.

Nothing was deleted here.

## 2. Notes for your side

1. **The 2026-09-08 receipt is still unapplied on your remote.** At `c2a0872` all 37 files it lists are still in `pass to VD-docs/`, unchanged. Your equation README says that receipt's closure "is already documented in the workspace guidance". If you deleted the staging copies locally, those deletions have not been pushed. If you have not, apply it: repoint, then delete. `mass_estimator_law_assumed_correct_steering_2026-09-07.md` stays **BOTH HOLD** (yours while it steers the laboratory).
2. **Haze: do not delete, do not treat as received.** The five files stay in your staging folder until a haze receipt is issued. One caution for when they come over: the 09-11 MFP1 brief *fixes* haze as a zero vector with ε-based uncertainty for outside investigators, and the 09-12 car document drops that assumption (non-zero mean, persistent friction, $H_C$ with the adequacy bound). If the brief is revised before the pass, include the revision. The two 2026-09-09 sources these documents cite (the tolerance/special-zero discovery and the remainder intermediate-expression algorithm) are not in the staging folder or pushed. Add them to the pass if they are meant to come over.
3. **Equation folder: repoint, then delete.** It was written for transfer. Your live sources remain `03_trace_and_evaluator/mass_estimator/`, which was not taken, nor was the 2026-09-18 comparison benchmark under `investigation/`. The standalone `mass_estimator.py` is kept here only as part of the record, a reference implementation frozen with its specification. It does not move custody of your laboratory code.
4. **Version pin.** Your README resolved VD-docs `main` at `8782a29` on 09-21. It is kept as written: a stale path prefix in a document body is recorded, never silently rewritten.

## 3. The 49 files

**A. Received this reading (7)**

| # | Source path under `pass to VD-docs/` | sha256 at source | Disposition | Home in VD-docs |
|---|---|---|---|---|
| 1 | `Mass estimator equation/README.md` | `188bc1921606…` | **Ingested 2026-09-23**; Delete at source after repointing | `Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/README.md` |
| 2 | `Mass estimator equation/mass_estimator.pdf` | `689470f94c9e…` | **Ingested 2026-09-23**; Delete at source after repointing | `Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/mass_estimator.pdf` |
| 3 | `Mass estimator equation/equation.svg` | `33440e89a20e…` | **Ingested 2026-09-23**; Delete at source after repointing | `Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/equation.svg` |
| 4 | `Mass estimator equation/equation.png` | `4166652882a4…` | **Ingested 2026-09-23**; Delete at source after repointing | `Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/equation.png` |
| 5 | `Mass estimator equation/mass_estimator.py` | `e029ac5264f7…` | **Ingested 2026-09-23**; Delete at source after repointing | `Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/mass_estimator.py` |
| 6 | `Mass estimator equation/example.py` | `8d0475526025…` | **Ingested 2026-09-23**; Delete at source after repointing | `Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/example.py` |
| 7 | `Mass estimator equation/requirements.txt` | `a83a2a4ed7ab…` | **Ingested 2026-09-23**; Delete at source after repointing | `Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/requirements.txt` |

**B. Held, not received (5)**

| # | Source path under `pass to VD-docs/` | sha256 at source | Disposition | Home in VD-docs |
|---|---|---|---|---|
| 8 | `NML3_HAZE_AND_THE_LOGIC_OF_NEWTONIAN_FORCE_ACCOUNTS_2026-09-10.md` | `1799948b6e17…` | **HELD — not received.** Keep at source | — |
| 9 | `HAZE_FLUID_MECHANICS_AND_THERMODYNAMICS_RESEARCH_DIRECTION_2026-09-10.md` | `ef026821f71e…` | **HELD — not received.** Keep at source | — |
| 10 | `MFP1_DETECTION_WITH_HAZE_INVESTIGATION_BRIEF_2026-09-11.md` | `77e97f20f619…` | **HELD — not received.** Keep at source | — |
| 11 | `HAZE_APPROXIMATE_CAR_PREDICTIONS_AND_CORE_NM_2026-09-12.md` | `0e3a747c7d91…` | **HELD — not received.** Keep at source | — |
| 12 | `HAZE_FLUID_PARTICLES_AND_INVESTIGATION_DIRECTION_2026-09-12.md` | `92e547c5f0c1…` | **HELD — not received.** Keep at source | — |

**C. Already covered by the 2026-09-08 receipt (37)**

| # | Source path under `pass to VD-docs/` | sha256 at source | Disposition | Home in VD-docs |
|---|---|---|---|---|
| 13 | `Mass estimator/mass_estimation_introduction_candidate_2026-09-06.md` | `d6c130af9e85…` | Ingested; Delete at source after repointing (09-08 receipt row 1; unchanged) | `Newton-analysis/_note_why_mass_estimation/mass_estimation_introduction_candidate_2026-09-06.md` |
| 14 | `Mass estimator/mass_estimation_introduction_candidate_sources_2026-09-06.md` | `9b3385dcb31a…` | Ingested; Delete at source after repointing (09-08 receipt row 2; unchanged) | `Newton-analysis/_note_why_mass_estimation/mass_estimation_introduction_candidate_sources_2026-09-06.md` |
| 15 | `Mass estimator/mass_estimation_introduction_development_plan_2026-09-06.md` | `9e3461f6251a…` | Ingested; Delete at source after repointing (09-08 receipt row 3; unchanged) | `Newton-analysis/_note_why_mass_estimation/mass_estimation_introduction_development_plan_2026-09-06.md` |
| 16 | `Mass estimator/mass_estimator_air_track_trial_2026-09-06.md` | `52e2ba365962…` | Ingested; Delete at source after repointing (09-08 receipt row 4; unchanged) | `Newton-analysis/_dscn_mass_estimator/mass_estimator_air_track_trial_2026-09-06.md` |
| 17 | `Mass estimator/mass_estimator_arrow_data_audit_2026-09-06.md` | `353aa37ecb11…` | Ingested; Delete at source after repointing (09-08 receipt row 5; unchanged) | `Newton-analysis/_dscn_mass_estimator/mass_estimator_arrow_data_audit_2026-09-06.md` |
| 18 | `Mass estimator/mass_estimator_behavior_test_report_2026-09-06.md` | `a4db059ebd72…` | Ingested; Delete at source after repointing (09-08 receipt row 6; unchanged) | `Newton-analysis/_dscn_mass_estimator/mass_estimator_behavior_test_report_2026-09-06.md` |
| 19 | `Mass estimator/mass_estimator_contribution_statement_draft_2026-09-08.md` | `ba5a3af4b392…` | Ingested; Delete at source after repointing (09-08 receipt row 7; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_estimator_contribution_statement_draft_2026-09-08.md` |
| 20 | `Mass estimator/mass_estimator_law_assumed_correct_steering_2026-09-07.md` | `360e80c95079…` | Ingested; BOTH HOLD — keep your copy while it steers the laboratory (09-08 receipt row 8; unchanged) | `Newton-analysis/_dscn_mass_estimator/mass_estimator_law_assumed_correct_steering_2026-09-07.md` |
| 21 | `Mass estimator/mass_estimator_practical_limits_and_uncertainty_2026-09-07.md` | `718be1068e8f…` | Ingested with one fix (see note 2); Delete at source after repointing (09-08 receipt row 9; unchanged) | `Newton-analysis/_dscn_mass_estimator/mass_estimator_practical_limits_and_uncertainty_2026-09-07.md` |
| 22 | `Mass estimator/mass_estimator_robot_cart_trials_2026-09-06.md` | `1b781d07011e…` | Ingested; Delete at source after repointing (09-08 receipt row 10; unchanged) | `Newton-analysis/_dscn_mass_estimator/mass_estimator_robot_cart_trials_2026-09-06.md` |
| 23 | `Mass estimator/mass_estimator_uncertainty_and_reuse_walkthrough_2026-09-07.md` | `9693f323748a…` | Ingested; Delete at source after repointing (09-08 receipt row 11; unchanged) | `Newton-analysis/_dscn_mass_estimator/mass_estimator_uncertainty_and_reuse_walkthrough_2026-09-07.md` |
| 24 | `Mass estimator/mass_readout_composition_uniqueness_2026-09-06.md` | `4eb361e5e538…` | Ingested; Delete at source after repointing (09-08 receipt row 12; unchanged) | `Newton-analysis/_dscn_mass_estimator/mass_readout_composition_uniqueness_2026-09-06.md` |
| 25 | `Mass estimator/vd_shared_quantity_argument_mass_estimation_2026-09-06.md` | `4378e2c28988…` | Ingested; Delete at source after repointing (09-08 receipt row 13; unchanged) | `Newton-analysis/_dscn_mass_estimator/vd_shared_quantity_argument_mass_estimation_2026-09-06.md` |
| 26 | `Mass estimator literature review/mass_candidate_bartel_evidence_2026-09-08.md` | `cfec23a61119…` | Ingested; Delete at source after repointing (09-08 receipt row 14; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_bartel_evidence_2026-09-08.md` |
| 27 | `Mass estimator literature review/mass_candidate_butler_evidence_2026-09-08.md` | `6c5e9ccfade4…` | Ingested; Delete at source after repointing (09-08 receipt row 15; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_butler_evidence_2026-09-08.md` |
| 28 | `Mass estimator literature review/mass_candidate_fieller_geometry_evidence_2026-09-08.md` | `1faeb4765a52…` | Ingested; Delete at source after repointing (09-08 receipt row 16; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_fieller_geometry_evidence_2026-09-08.md` |
| 29 | `Mass estimator literature review/mass_candidate_huard_mailhot_evidence_2026-09-08.md` | `09524e8f2b22…` | Ingested; Delete at source after repointing (09-08 receipt row 17; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_huard_mailhot_evidence_2026-09-08.md` |
| 30 | `Mass estimator literature review/mass_candidate_katz_evidence_2026-09-08.md` | `1aec0ea1ab69…` | Ingested; Delete at source after repointing (09-08 receipt row 18; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_katz_evidence_2026-09-08.md` |
| 31 | `Mass estimator literature review/mass_candidate_kelly_evidence_2026-09-08.md` | `c8a81f70cd27…` | Ingested; Delete at source after repointing (09-08 receipt row 19; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_kelly_evidence_2026-09-08.md` |
| 32 | `Mass estimator literature review/mass_candidate_leonard_evidence_2026-09-08.md` | `dc78e77ea089…` | Ingested; Delete at source after repointing (09-08 receipt row 20; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_leonard_evidence_2026-09-08.md` |
| 33 | `Mass estimator literature review/mass_candidate_liseo_evidence_2026-09-08.md` | `5f5aeae29856…` | Ingested; Delete at source after repointing (09-08 receipt row 21; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_liseo_evidence_2026-09-08.md` |
| 34 | `Mass estimator literature review/mass_candidate_mantz_evidence_2026-09-08.md` | `1a779d2e631f…` | Ingested; Delete at source after repointing (09-08 receipt row 22; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_mantz_evidence_2026-09-08.md` |
| 35 | `Mass estimator literature review/mass_candidate_marchand_strawderman_evidence_2026-09-08.md` | `40d98fdba95d…` | Ingested; Delete at source after repointing (09-08 receipt row 23; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_marchand_strawderman_evidence_2026-09-08.md` |
| 36 | `Mass estimator literature review/mass_candidate_mardia_evidence_2026-09-08.md` | `0861223382c0…` | Ingested; Delete at source after repointing (09-08 receipt row 24; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_mardia_evidence_2026-09-08.md` |
| 37 | `Mass estimator literature review/mass_candidate_roe_woodroofe_evidence_2026-09-08.md` | `8bf8b16e3bd3…` | Ingested; Delete at source after repointing (09-08 receipt row 25; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_roe_woodroofe_evidence_2026-09-08.md` |
| 38 | `Mass estimator literature review/mass_candidate_zhou_etal_evidence_2026-09-08.md` | `f5e52265f929…` | Ingested; Delete at source after repointing (09-08 receipt row 26; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_candidate_zhou_etal_evidence_2026-09-08.md` |
| 39 | `Mass estimator literature review/mass_equation_comparison_review_2026-09-08.md` | `d56f3f32e1f0…` | Ingested; Delete at source after repointing (09-08 receipt row 27; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_equation_comparison_review_2026-09-08.md` |
| 40 | `Mass estimator literature review/mass_equation_comparison_second_review_2026-09-08.md` | `18a5de796904…` | Ingested; Delete at source after repointing (09-08 receipt row 28; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_equation_comparison_second_review_2026-09-08.md` |
| 41 | `Mass estimator literature review/mass_equation_comparison_third_review_2026-09-08.md` | `1802363fdec7…` | Ingested; Delete at source after repointing (09-08 receipt row 29; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_equation_comparison_third_review_2026-09-08.md` |
| 42 | `Mass estimator literature review/mass_equation_final_focused_review_2026-09-08.md` | `61626d86a17c…` | Ingested; Delete at source after repointing (09-08 receipt row 30; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_equation_final_focused_review_2026-09-08.md` |
| 43 | `Mass estimator literature review/mass_estimator_literature_recheck_2026-09-07.md` | `a386af9081f4…` | Ingested; Delete at source after repointing (09-08 receipt row 31; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_estimator_literature_recheck_2026-09-07.md` |
| 44 | `Mass estimator literature review/mass_point_functional_ancestry_evidence_2026-09-08.md` | `009fe8d99626…` | Ingested; Delete at source after repointing (09-08 receipt row 32; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_point_functional_ancestry_evidence_2026-09-08.md` |
| 45 | `Mass estimator literature review/mass_predecessor_gull_werman_focused_check_2026-09-08.md` | `b91cb65d409c…` | Ingested; Delete at source after repointing (09-08 receipt row 33; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_predecessor_gull_werman_focused_check_2026-09-08.md` |
| 46 | `Mass estimator literature review/mass_predecessor_lindley_dellaportas_focused_check_2026-09-08.md` | `42a04abb55c4…` | Ingested; Delete at source after repointing (09-08 receipt row 34; unchanged) | `Newton-analysis/_dscn_mass_estimator/literature_review/mass_predecessor_lindley_dellaportas_focused_check_2026-09-08.md` |
| 47 | `mass_estimation_zero_zero_two_cases.md` | `4da9f5f86763…` | Delete at source — already homed 2026-09-05, byte-identical (09-08 receipt row 35; unchanged) | `Newton-analysis/_dscn_mass_estimator/mass_estimation_zero_zero_two_cases.md` |
| 48 | `mass_estimator_additional_derivations_2026-09-05.md` | `2cc41c37a7fa…` | Delete at source — already homed 2026-09-05, byte-identical (09-08 receipt row 36; unchanged) | `Newton-analysis/_dscn_mass_estimator/mass_estimator_additional_derivations_2026-09-05.md` |
| 49 | `mass_estimator_originality_research_2026-09-05.md` | `c663b8940c6c…` | Delete at source — already homed 2026-09-05, byte-identical (09-08 receipt row 37; unchanged) | `Newton-analysis/_dscn_mass_estimator/mass_estimator_originality_research_2026-09-05.md` |

## 4. Newton-side prompt (paste into the VD-Newton workspace)

> VD-docs issued `outbox/VD-Newton/PASS_RECEIPT_2026-09-23.md`. (1) `pass to VD-docs/Mass estimator equation/` is received and homed at `Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/`. Repoint any link to it, then delete the staging folder. (2) The 2026-09-08 receipt is still unapplied on the remote: its 37 files are all still in `pass to VD-docs/`, byte-identical. Apply it (repoint, then delete; keep the steering record, BOTH HOLD) and push. (3) The five haze files are HELD, not received. Leave them in `pass to VD-docs/`. If the MFP1 brief is revised or the two 09-09 sources are meant to come over, add them there. (4) Record this receipt as partial in `AGENTS.md`. Check each file's hash against the receipt before deleting it.

## Amendment, 2026-09-23 (later the same day): the haze files are received

This amendment supersedes §1's "5 held", §2 note 2, table B, and items (3) of the prompt in §4.

After a conversation with the user, all five haze files were **received** from `c2a0872`. They are byte-identical to `9f9e3f8`, and their hashes match table B. All five were normalization no-ops and passed the KaTeX gate.

| # | File | Disposition | Home in VD-docs |
|---|---|---|---|
| 8 | `NML3_HAZE_AND_THE_LOGIC_OF_NEWTONIAN_FORCE_ACCOUNTS_2026-09-10.md` | Ingested; Delete at source after repointing | `Newton-analysis/_dscn_haze/` |
| 9 | `HAZE_FLUID_MECHANICS_AND_THERMODYNAMICS_RESEARCH_DIRECTION_2026-09-10.md` | Received, **held unsorted**; Delete at source after repointing | `inbox/` (home to be decided) |
| 10 | `MFP1_DETECTION_WITH_HAZE_INVESTIGATION_BRIEF_2026-09-11.md` | Ingested; Delete at source after repointing | `Newton-analysis/_dscn_haze/` |
| 11 | `HAZE_APPROXIMATE_CAR_PREDICTIONS_AND_CORE_NM_2026-09-12.md` | Ingested; Delete at source after repointing | `Newton-analysis/_dscn_haze/` |
| 12 | `HAZE_FLUID_PARTICLES_AND_INVESTIGATION_DIRECTION_2026-09-12.md` | Received, **held unsorted**; Delete at source after repointing | `inbox/` (home to be decided) |

- **`Newton-analysis/_dscn_haze/` is a new discussion.** It holds the three records above plus a VD-docs-side piece of 2026-09-13, `HAZE_AND_THE_LANGUAGE_OF_APPROXIMATION_2026-09-13.md`, which you can read there. None of them is filed as an entry-structure criticism, because each leaves haze's entry placement open. When a concrete proposal for where haze goes in the entries is written, send it as its own document; it will be filed in the Criticism History.
- **The two fluid records** are received, catalogued, and waiting in `inbox/` to be homed. They are safe to delete at source. Their eventual path will be in the catalog; cite them by filename.
- **Correction to §2 note 2.** It said the 09-11 brief *fixes* a premise that the 09-12 car document *drops*. That overstated it. The brief deliberately leaves haze's statistical form open and forbids formalising it as a zero-expectation random force. The car document fills that in (a nominal zero plus a bounded allowance, not necessarily zero-mean or random) and says it supersedes earlier drafts where they left the definition open. So the car document refines the brief rather than contradicting it. Revising the brief is not required.
- **Still wanted:** the two 2026-09-09 sources that the 09-10 argument cites (the tolerance/special-zero discovery and the remainder intermediate-expression algorithm). They are where the discussion starts, and they are not on your remote.

**Replacement prompt (supersedes §4):**

> VD-docs issued `outbox/VD-Newton/PASS_RECEIPT_2026-09-23.md`, amended the same day. (1) `pass to VD-docs/Mass estimator equation/` is received and homed at `Newton-analysis/_dscn_mass_estimator/mass_estimator_equation/`. (2) All five haze files are received: three are homed in `Newton-analysis/_dscn_haze/`, and the two fluid records are held in VD-docs `inbox/`. (3) The 2026-09-08 receipt is still unapplied on the remote. Its 37 files remain in `pass to VD-docs/`. Keep the steering record (BOTH HOLD). (4) For every file listed as received in (1) to (3): repoint any links, check its hash against the receipt, then delete it from `pass to VD-docs/`. Push. (5) If the two 2026-09-09 haze sources (tolerance/special-zero discovery, remainder intermediate-expression algorithm) should come over, put them in `pass to VD-docs/`. (6) Record the closure in `AGENTS.md`.

---
*Issued from `outbox/VD-Newton/`. A record of VD-docs under the custody rule; this copy is permanent. The ledger entry is the 2026-09-23 paragraph of the `inbox` folder note in `catalog.yaml`.*
