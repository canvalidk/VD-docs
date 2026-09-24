# Pass receipt — 2026-09-23, second pass (VD-Newton @ ecd1a1c)

| | |
|---|---|
| From | VD-docs |
| To | VD-Newton |
| Date | 2026-09-23 |
| Source | `canvalidk/VD-Newton` `main` @ `ecd1a1ce4a0b9ff6f8ee491581fde23ab62b84f1` ("Add mass estimator prior-factor and sequential-update analyses"), staging folder `pass to VD-docs/` |
| Status | **Complete** for the one file this pass carries |

This receipt answers the single document the user asked to stage as a record on
23 September. It does not cover anything else in `pass to VD-docs/`; see §2.
The earlier receipt of the same date,
[`PASS_RECEIPT_2026-09-23.md`](PASS_RECEIPT_2026-09-23.md), is unaffected.

## 1. How the pass was handled

- **One file received**:
  `pass to VD-docs/Mass estimator/mass_estimator_regimes_priors_and_updating_2026-09-23.md`,
  staged as a record at the user's request ("start with staging contribution 12
  as a record").
- **Verified.** Its full SHA-256 matches the blob in the source commit above
  byte for byte.
- **Normalization.** A no-op: the document already uses `$$` blocks; all three
  parse under KaTeX; there are no inline spans or stray dollars. Nothing was
  banked in `_math_originals/`.
- **Home.** Filed flat in the mass-estimator discussion under its own name, at
  `Newton-analysis/_dscn_mass_estimator/mass_estimator_regimes_priors_and_updating_2026-09-23.md`.
  Catalogued with `kind: record`.
- **Relations.** No `supersedes` or `corrects` relation is bound. The record
  scopes earlier members; binding is the user's call.

## 2. Notes for your side

- **The staged header is out of date on one point.** It says the contribution
  has no source commit. That was true when it was staged; this receipt supplies
  it (`ecd1a1c`). The managed copy is kept byte-identical to what you staged
  rather than edited.
- **Links.** The document's relative links point into your
  `03_trace_and_evaluator/mass_estimator/investigation/` folder and its
  `.tools/` scratch area. That is expected. The working contribution there
  (`prior_factors_and_sequential_updating.md`, working contribution 12) is
  your live laboratory copy. This receipt does not touch it; its code, tests
  and protocols stay with you.
- **Not covered by this receipt:**
  - the BOTH HOLD steering file;
  - the held `equation.svg`;
  - the unreceipted documents recorded in your `AGENTS.md`, including the
    two 9 September haze sources.

  All remain as they were.

## 3. Files

| # | Source path under `pass to VD-docs/` | SHA-256 | Disposition | VD-docs home |
|---:|---|---|---|---|
| 1 | `Mass estimator/mass_estimator_regimes_priors_and_updating_2026-09-23.md` | `d17a30bbdcb0618b5f22954c8751f194e5de1953649e3aa5cb3afd20d1711c24` | Ingested; remove at source after repointing | `Newton-analysis/_dscn_mass_estimator/mass_estimator_regimes_priors_and_updating_2026-09-23.md` |

## 4. Prompt for the VD-Newton side

> Apply `canvalidk/VD-docs/outbox/VD-Newton/PASS_RECEIPT_2026-09-23_ecd1a1c.md`.
> 1. Confirm that the full SHA-256 of
>    `pass to VD-docs/Mass estimator/mass_estimator_regimes_priors_and_updating_2026-09-23.md`
>    is `d17a30bbdcb0618b5f22954c8751f194e5de1953649e3aa5cb3afd20d1711c24`.
> 2. If it matches, repoint any link that targets the staged copy to the
>    VD-docs home in row 1. Then remove the staged copy: move it to your
>    `to delete/` folder, per the user's 23 September preference, unless the
>    user says to delete it outright.
> 3. If it does not match, keep it and include the changed version in your
>    next pass.
> 4. Record the closure in `AGENTS.md`.
>
> Leave `03_trace_and_evaluator/mass_estimator/investigation/prior_factors_and_sequential_updating.md`
> and its code unchanged; they are not part of this receipt.
