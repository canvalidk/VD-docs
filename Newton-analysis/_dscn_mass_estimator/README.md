# _dscn_mass_estimator — read this before treating the folder as one argument

This is a discussion: a folder grouping records that address one another. The
FLAT files are its members — records the user chose, one by one, to file here.
They scope each other; nothing is bound (no `supersedes` / `corrects` asserted
anywhere in the folder). Content, provenance and relations live in
`catalog.yaml` — the `files:` rows and the `folders:` entry for this path. Read
the rows, not just the filenames.

## The two subfolders are not members in the same sense

`literature_review/` (22 files) and `unsanctioned/` (7 files) hold the output of
one VD-Newton Codex session, 2026-09-06 to 2026-09-08, received in the
2026-09-08 pass. That session produced records on its own initiative. In this
repo a record is something the user decides to make, and these were not decided
one by one. The user's ruling of 2026-09-15: keep them, do not formalise them,
keep them out of the flat view. That is a RECORDED EXCEPTION under
ORGANIZATION.md "Exceptions" — nothing more, no new object kind, no "log" model.

What that means if you are an AI working here:

- Do not read the subfolder files as part of the discussion's argument unless
  the user brings one up or moves it flat. Do not promote, bind, stamp a kind
  on, or reorganise them on your own initiative.
- Do not delete them either. A pass surfaces fossils, never deletes.
- Their in-file "Status: local, awaiting transfer to VD-docs, not submitted"
  banners are stale — this repo IS the transfer. Ignore the banners.
- Two files in `unsanctioned/` (behavior_test_report, uncertainty_and_reuse_
  walkthrough) were written under a gate/rejection spec that the flat steering
  record of 2026-09-07 retired the next day. They carry a banner saying so and
  were not rewritten. The banner links point at the steering record by bare
  filename; the file now sits one level up. Filenames are the identifiers;
  paths in citations decay (ORGANIZATION.md). VD-Newton's lab README links
  these files by path — that is theirs to repoint, not a reason to move
  anything back.

## Two of the session's files stayed flat, by decision

- `mass_estimator_law_assumed_correct_steering_2026-09-07.md` — the user's own
  ruling, quoted verbatim. His content, not the session's.
- `mass_readout_composition_uniqueness_2026-09-06.md` — a self-contained theorem
  (C1–C5 force E[f]/E[α]) answering a question the flat records themselves pose
  (`what_forces_the_ratio_of_means_readout`). Claude's call, 2026-09-15; cheap
  to push down if the user disagrees.

The three 2026-09-05 files (`mass_estimation_zero_zero_two_cases`,
`mass_estimator_originality_research_2026-09-05`,
`mass_estimator_additional_derivations_2026-09-05`) predate the session, were
filed on the user's instruction the day they were written, and are flat members.
