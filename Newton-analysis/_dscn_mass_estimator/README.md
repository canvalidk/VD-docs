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

## Added 2026-09-23: one record folder and one reference paper at flat level

- `mass_estimator_equation/` is a **member**: the 2026-09-21 specification of
  the current estimator (ratio of mean compatible magnitudes), received from
  VD-Newton. It is one record in its own folder. `README.md` is the record, and
  the PDF, equation images and standalone code are parts of it. It is not bound
  to `inertial_mass_estimator_full_working_spec_d1.md`; that call is the user's.
- `SIM-38-2074.pdf` is a **reference paper** (Morris, White & Crowther 2019, on
  simulation studies), placed here by the user. It is not a record of the
  argument, and not part of `literature_review/`.

## Added 2026-09-23 (evening): one flat record

- `mass_estimator_regimes_priors_and_updating_2026-09-23.md` is a **flat
  member**, filed as `kind: record` at the user's request. It is VD-Newton's
  working contribution 12: readout regimes (dominance, minimax, switch rules),
  the fitted prior weight λ and what it is (a prior factor on mass centred at
  the instrument scale s, not knowledge of the object), log-normal priors, and
  the estimator read as an update rule. Received from VD-Newton @`ecd1a1c`;
  receipt `outbox/VD-Newton/PASS_RECEIPT_2026-09-23_ecd1a1c.md`. It scopes and
  binds nothing. Its code and study links point into VD-Newton's
  `investigation/` folder, which is where the reproducible studies live.

## Added 2026-09-23 (night): `papers/`

- `papers/` holds **published papers**, collected on the user's instruction as
  standard citations. They are references, not records and not members:
  nothing in this discussion is bound to them. `SIM-38-2074.pdf` (listed above)
  moved into it the same night, alongside Wang et al. (2021) on penalized
  Fieller intervals. `papers/README.md` carries the reading list, including the
  citations not yet downloaded.
- Not to be confused with `literature_review/`, which is the unsanctioned Codex
  search *about* the literature.

## Added 2026-09-23 (night): one investigation direction

- `mass_estimator_default_weighting_direction_2026-09-23.md` is a short,
  deliberately non-conclusive **investigation direction**, filed flat at the
  user's request. It asks what the default weighting may reference when
  readings are combined. It scopes and binds nothing.

## Added 2026-09-24: one flat record, and where the studies now live

- `old_information_in_the_prior_slot_2026-09-24.md` is a **flat member**,
  written at the user's request. It shows algebraically that the exact
  combination splits into old × new, so the old readings' law sits exactly
  in the prior slot, and reads contribution 12's tilt parameters as carried
  state (m₀, σ of log m). Its evidence is a preset of the tester repo. It
  scopes and binds nothing.
- **Reproducible studies now live in the tester repo,
  `canvalidk/Mass-estimator-testor`**: one program where each study is a
  recorded preset file. Records here cite a preset and a commit. It replaces
  VD-Newton's `investigation/` scripts for new work.

## Added 2026-09-24 (later): a second flat record

- `vonmises_state_2026-09-24.md` is a **flat member**, written at the
  user's request. It shows that in 2D each reading's likelihood is exactly a
  von Mises law in the doubled angle, that contribution 12's λ is a von Mises
  concentration, and that readings sharing only the mass combine by adding one
  vector each (exact in 2D, approximate in 3D). Its peak is the
  total-least-squares axis. It carries a reading list for following this
  into the literature. It scopes the morning record and binds nothing.

## Added 2026-09-24 (night): a third flat record

- `excitation_weighting_premise_2026-09-24.md` is a **flat member**,
  written at the user's request. From his premise (force and acceleration
  are symmetric, and either can take any value), it argues that the weighting
  over the true pushes must be flat in the vector, as Maxwell–Boltzmann is
  flat in velocity. The 21 September equation is unchanged in 2D. The record
  proposes a change to it in 1D and 3D, where it currently favours large or
  small pushes. It names the argument's weak spot (accelerating frames) and a
  second route (Herschel–Maxwell). Tests are a tie. It scopes and binds
  nothing.

## Added 2026-09-25: a fourth flat record, and a premise

- `axis_splitting_and_the_24_september_change_2026-09-25.md` is a **flat
  member**, written at the user's request. It isolates the 24 September
  change as one weight on each candidate pair ($r^{d-2}$, identity in 2D),
  and shows the new law of mass is the 21 September 2D law in every
  dimension. It proposes **axis splitting** as a premise: a vector reading
  and its axes read separately must give the same law. The user judged it
  "too elementary to be wrong". It forces both the flat-in-vector weighting
  and the mass factor the previous record left open. It also proves the
  symmetric rule consistent and gives the exact width factor
  $1+d/r^{\ast2}$ for many readings. On accuracy the two equations tie; the
  gain is consistency. Evidence: four presets in the tester repo. It scopes
  and binds nothing.

## Added 2026-09-25 (evening): a fifth flat record, and a new equation

- `ours25b_the_many_reading_readout_2026-09-25.md` is a **flat member**,
  written at the user's request. It pays the debt the axis-splitting record
  left: with many readings, the readout's "size of the series" must be the
  length of all the readings' true vectors stacked into one, not the plain
  sum of their sizes. Axis splitting applied to the answer forces this,
  given one rule for joining sets of readings. It names the result
  **ours25b** (ours24's law with that readout) and presents the equation in
  full. Consequences: a series and its axis readings agree exactly, the
  recording frame does not matter, and the answer depends on the data only
  through three sums. On accuracy it ties with ours24. Evidence: two presets
  and a test file in the tester repo. It scopes the axis-splitting record and
  binds nothing.

## Added 2026-09-26: an audit record

- `what_ours24_and_ours25b_change_in_earlier_results_2026-09-26.md` is a
  **flat member**, written at the user's request after he asked whether the
  new equation breaks earlier exact results. One proof broke: the additive
  readout weight of `old_information_in_the_prior_slot_2026-09-24.md` §2.2.
  Its exact replacement is a four-number state. Everything about the law
  stands, including $m_0$, $\sigma_{\ln m}$ and λ as carried state. It also
  lists what the 24 September law change moved (the 1D Liseo identity now
  matches the reference-prior posterior, not Jeffreys; some 1D/3D closed
  forms hold only as limits), a new exact result (equal channel energies
  give exactly $s$), and what the equation note's next draft must not copy.
  It scopes several records and binds nothing.

## Added 2026-09-26: a credit and originality record

- `credit_and_originality_of_the_mass_estimator_2026-09-26.md` is a **flat
  member**, written at the user's request after the 26 September literature
  check. It splits the estimator into its law and its readout, and credits
  each part. The law is Lindley and Beale's (1966 discussion of Sprent), with
  a prior shape that matches known defaults. The readout device (a ratio of
  posterior means) is known. What was not found is the selection principle:
  composition forcing the readout, and axis splitting forcing the weighting
  and the many-reading pooling. It also lists who in the project contributed
  what, and what can honestly be claimed in public. It extends the
  5 September originality record and binds nothing.

## Added 2026-09-26 (evening): ours26, per-axis noise

- `ours26_per_axis_noise_2026-09-26.md` is a **flat member**, written at the
  user's request. Every equation up to ours25b assumed one noise pair for all
  axes; ours26 drops that. Walked by what stays forced: the law becomes a sum
  of Beale terms, one per axis (axis splitting plus the combination rule); the
  readout keeps ours25b's definition, its weight now a weighted noncentral chi
  mean computed by one Laplace-transform integral; the prior's centre comes
  off the wall (the symmetries that fixed it leave a family), so it is
  declared. Also recorded: the answer depends only on per-noise-pair sums, so
  the exact combination state survives as one (C, T, M) per pair; zero
  readings no longer return the centre through the readout. Evidence: a
  test file and a preset in the tester repo (axis splitting to 5e-11; the open
  centre moves weak-data answers by a factor of up to about 1.5, strong-data
  ones by under 1%). It extends the ours25b record and binds nothing.

## Added 2026-09-27: the combination equation, built and rerun

- `the_combination_equation_is_exact_2026-09-26.md` is a **flat member**,
  written at the user's request after he asked what in the 26 September
  session was unrecorded. It delivers the audit record's owed item: ours25b's
  carried state, four real numbers per series $(C,T,M)$, built in the tester
  and tested. Combining sets of readings is adding their states; the law, the
  median, the intervals and ours25b's readout all follow from the state and
  match the rule on all readings to $10^{-14}$ over 21,600 series. The rerun of
  the old-information study under ours25b measures what the earlier carries
  lose: keeping the law but not the old weight moves the readout by up to about
  6% (cell median), the two-number fits move the median by up to about 19%.
  It also notes, incidentally, 95% intervals covering as little as 76.5% with
  21 weak readings. It extends the audit and the old-information records and
  binds nothing.
