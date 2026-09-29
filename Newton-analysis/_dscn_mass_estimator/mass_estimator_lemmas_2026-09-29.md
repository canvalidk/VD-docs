# The mass estimator's properties and lemmas, 29 September

**2026-09-29.** Record, written by Claude at the user's request ("Produce me
the superseding properties list"), reviewed by him and filed on his
instruction: "It's good enough. You can just turn this into a superseding
record."

**Supersedes `mass_estimator_lemmas_2026-09-27.md`**, as that record said its
changed versions would arrive ("we can imagine the changed versions go in as
replacements"). It binds nothing else. The records whose proposed corrections
it carries (listed below) are not corrected by it; their proposals are
adopted here, in the table.

**What it is for.** The project's goal is the estimator function that can act
as the definition of mass. So the definition *is* this list: the properties
mass must have, the declared inputs, and what they force. The equation is
what the list produces. Every item below says whether it is **ruled** (the
user's words, dated), a **premise** (graded, not ruled), a **theorem** (with
its sources), **declared** (an input), **proposed** (not ruled), **struck**,
or **open**.

**What it folds in.** The 27 Sept lemma record (L1–L14, T1–T20) and every
correction proposed since:

- the ours26 sweep §4 (errors E1–E6, gaps G1–G4);
- the perturbation matrix §6;
- the ours28 record §8;
- the Jeffreys-check record §4 (L4′);
- the betweenness record §4;
- the full-covariance / declared-subspace record §§2–5;
- the no-borrowing record §5;
- the C3 narrow-form record §9;
- the reference implementation record;
- the rulings of 27–28 Sept;
- the two findings of 29 Sept (zero components contribute nothing; the
  readout fails Z).

**Numbering.** L1–L14 and T1–T20 keep their numbers so old references still
work. Struck items keep their slot. New items start at L15 and T21.

**Grades** (premises only). *bedrock*: denying it changes the problem.
*strong*: a real premise, well motivated. *medium*: plausible, narrower.
*mild*: technical.

---

## 0. The frame (inherited, not re-argued here)

| | statement | status |
|---|---|---|
| F1 | **The estimator is the definition.** What mass is equals how it is read from data; there is no further mass behind the readout ("there is no super meta mass that we can't achieve"). The goal is to answer "what are the estimators estimating?", not to build a good estimator. | ruled, 27 Sept |
| F2 | **Uniqueness is the stake.** Any choice the properties leave open counts as an alternative definition of mass, i.e. an alternative Newtonian mechanics. "The choices only differ where nobody measures" is not an answer. | ruled, Sept |
| F3 | **Inherited from `_note_why_mass_estimation`:** provenance independence, laws as predictions, the authority ruling. Named here so they are not left out silently (sweep G3); not restated. | inherited |
| F4 | **Commitment order is suspended** for this work: Newton III "and more" may be used. | ruled, 27 Sept |

## 1. The type

**Input.** A series of readings $i=1,\dots,N$, each declaring:

- data $\mathbf y_i=(\tilde{\mathbf F}_i;\tilde{\mathbf a}_i)\in\mathbb R^{2d}$, any values including zero, in the reading's own frame;
- an error covariance $\Sigma_i\in\mathbb R^{2d\times2d}$, positive definite, any correlation, including between the channels;
- a candidate subspace $N_i\in\mathbb R^{d\times k_i}$ with orthonormal columns (default $I_d$: nothing known about the push's direction);
- membership: which components belong to which reading (the reading structure).

Also declared for the series:

- the starting law $\pi$: its shape and its centre $c$;
- the size law $G$ on each reading's push scale: its shape.

**Output.** A law of mass on $(0,\infty)$ and a point $\widehat m$. The misfit
is kept with the result (sweep G2, d2 P3: an output clause, not a premise the
mathematics uses).

## 2. The properties of mass (premises)

| | name | statement | status | change since 27 Sept |
|---|---|---|---|---|
| L1 | **Newton II, one object** | $\mathbf F^\ast_i=m\,\mathbf a^\ast_i$ with one $m>0$ shared by every reading: one object, one inertial frame, over the series. Assumed, not tested: no rejection gate. | bedrock; "not tested" ruled 7 Sept | Addressing and persistence written in (sweep G1). |
| L2 | **Noisy type** | every declared $\sigma>0$ ($\Sigma_i$ positive definite). As d2 reads it, the type promises a mass for every measured input, including measured zero–zero. | bedrock; $\sigma>0$ ruled 25 Sept; "a mass for every measured input" is d2's reading, **now in tension with O1** | "So $\widehat m\in(0,\infty)$" moved to T13 (sweep E5). |
| L3 | **Units covariance** | force units $\times\lambda$, acceleration units $\times\mu$ $\Rightarrow$ law and point scale by $\lambda/\mu$. The only mass scale allowed in is the declared $\pi$, which transforms the same way. | bedrock | none |
| L3′ | **Knowledge-free default** | with no knowledge of the object, $\pi$'s scale comes from the instruments' SDs alone; knowledge of the object enters only as old information in the prior slot. | **proposed** (sweep E1), not ruled | new; T14 rests on it |
| L4 | **Swap, law half** | $\pi$ is symmetric under $m/c\leftrightarrow c/m$. | strong | none |
| L4′ | **Push–noise symmetry** | the size law is symmetric under $\omega\leftrightarrow1/\omega$ ($\beta\leftrightarrow1-\beta$): before data, a reading's push and its noise are on an equal footing. Calibration rests on it: every symmetric law covers 94–98%, every asymmetric one fails. | strong; **proposed** (Jeffreys-check record §4), not ruled | new |
| L5 | **Lumping** | $R(X_1+X_2,Y)=R(X_1,Y)+R(X_2,Y)$: glue two bodies at common acceleration and their masses add. | strong | none |
| L6 | ~~C3~~ | **struck as a premise.** Now theorem T21. | — | derived; ruled 28 Sept, 23:41 |
| L7 | **Calibration** | $R=f/\alpha$ on sure inputs; continuous at constants **in mean absolute error**; defined on every law with finite means. | mild | topology named (sweep E4) |
| L8 | **Axis splitting, restated** | a reading and its components read as 1D readings give the same law **when the components carry the reading's shared state** (its $N_i$ and its push scale). Components of different readings never share one. | strong; the restatement follows from L18 but **needs your explicit yes** | Changed. The old strong form ("however its axes are grouped") fails under ours28: 4.0807 against 3.7328. **The 27 Sept matrix had this as the sole support of the flat push size and of the stacked length. Whether the restated form still forces them is open (O3).** |
| L9 | **Isotropy, in noise units** | a reading's push weight depends only on the push's length in whitened (noise) units, within its declared subspace. | strong; units fixed by T7 (the push-units bend dies three ways) | Units fork closed except one scenario (O8). |
| L10 | ~~No push scale~~ | **struck.** It was not a symmetry but the claim that every push is infinitely large in noise units ($R^{\ast2}=\infty$); T18 measures its error. | — | struck 28 Sept (ours28 record §1); replaced by L10′ |
| L10′ | **Push scale is a per-reading nuisance** | each reading's push scale $\omega_i$ is unknown and averaged over under the declared size law $G$, never picked and never shared. | strong; follows from the chain's own rule (average nuisances) plus L19 | new |
| L11 | **Consistency** | $\widehat m_N\to m$ whenever the total true push $R^{\ast2}\to\infty$. | strong | none |
| L12 | **One joining rule** | $\operatorname{size}(A\cup B)=\operatorname{size}(A)\oplus\operatorname{size}(B)$, one fixed $\oplus$; a series has one size per channel per candidate. | medium | The narrow-C3 clause once proposed for here is now a theorem (T21). |
| L13 | **Gaussian noise model** | the model is zero-mean Gaussian with the declared covariance, independent across readings. This is a statement about the **model**, not a claim that the world's errors are Gaussian: the model uses only declared second moments. | **was declared, now forced**: by consistency under the flat push (matrix §4) and by Z under ours28 (Student-$t_5$ lets a zero reading tilt the law by up to 1.6%) | Moved to theorem-supported (T23). **Check with your 27 Sept line "any insistence that incoming data be Gaussian is of course wrong":** I read it as compatible, since the model is forced and the data need not be Gaussian. Confirm. |
| L14 | **Common force** | $1/R(X,Y_1+Y_2)=1/R(X,Y_1)+1/R(X,Y_2)$: reduced mass (uses Newton III, allowed by F4). | strong | none |
| L15 | **Betweenness** | mixing two candidate laws cannot give a readout outside both of their readouts. | ruled **provisionally**, 28 Sept ("i think we can accept betweenness provisionally") | new |
| L16 | **Frame independence** | each reading may be written in its own frame and sign convention; a fortiori the whole series may be rotated, or boosted in a Galilean way. | ruled 28 Sept ("Yes of course. Bookkeeping can't matter"); the rotation property was his, 27 Sept | New as a named premise; it forced ours27's full covariance (T22). |
| L17 | **Same candidate law, same mass** | whichever instruments produced a candidate law, it gives one mass: the readout's score cannot read the declared instrument facts. | ruled 28 Sept ("Sure") | new |
| L18 | **Declared inputs are correct** | the $\sigma$'s are correct (ruled 28 Sept, morning). The reading structure is a declared instrument fact like $\Sigma_i$ (ruled 28 Sept, 23:41: "yes they can be a proprty of the instrument"). **Proposed extension:** $N_i$ too, i.e. the push's declared direction structure is an input, not learned (full-covariance record §3). | ruled for $\sigma$ and for the reading structure; **$N_i$ proposed** | new |
| L19 | **No borrowing between readings** | nothing inferred from one reading about pushes (size, direction, spread) is used on another. Readings are joined only through the mass they share. Readings may come from any regime in any combination ("F = 1, then F = 50000000, then F = 0.00001"). | ruled 28 Sept, night | new; withdrew ours28b |
| L20 | **Z: a reading that adds no information does not change the answer** | his wording, 27 Sept: "a reading that adds no information from other dimensions must not change the answer". Applies to the law **and to the point**. | ruled as a property, 27 Sept. **Scope ruling owed (O7).** | New as a named premise; T20 and the matrix used it unnamed. **Holds for the law (T24); fails for the current readout (T29).** |

**Rulings that constrain the tests, not the equation:**

- **R1.** The declared $\sigma$'s are assumed correct. The question is whether
  the equation responds correctly, not whether misfit is evidence about the
  $\sigma$'s. (28 Sept)
- **R2.** Candidate pairs are hypotheticals the average runs over, not
  quantities recovered. Knowing $m$ leaves both slots unknown. (27 Sept)

## 3. What follows (theorems)

Sources in brackets. **[flat]** marks results that hold only for ours27's flat
push; **[one pair]** marks results that need one noise pair.

| | name | statement | from | status after 29 Sept |
|---|---|---|---|---|
| T1 | Exact branch | $\sigma=0$: one mass, no mass, or every mass; "undefined" only at exact $0/0$ | L1 | unchanged |
| T2 | Candidates | $\mathbf F^\ast=f\mathbf u$, $\mathbf a^\ast=\alpha\mathbf u$, $f,\alpha>0$ | L1 | unchanged |
| T3 | Separation | $R(X,Y)=R(X,1)\,R(1,Y)$ | L5, L14, L7 | unchanged |
| T4 | Ratio of means | $R=E[X]/E[Y]=E[\alpha m]/E[\alpha]$ | T3, L5, L14, T21, L7 | unchanged; C3 now enters as T21 |
| T5 | Swap, readout half | $R(Y,X)=1/R(X,Y)$ | T4 | unchanged |
| T6 | Push weight | L8 and L9 force the Gaussian family $e^{-\lVert\mathbf v\rVert^2/2\omega^2}$ in noise units (Herschel–Maxwell). The flat weight is its $\omega\to\infty$ endpoint. | L8, L9, **T7** (sweep E2) | **Changed.** Was "flat pushes"; now the family. L10′ averages $\omega$. |
| T7 | Prior once | nothing attached to a reading may depend on $m$. The push weight's determinant is $m$-free for every $\omega$ (ours28 §3), which forces noise units. | L11 | strengthened |
| T8 | The law (ours28) | $p(m)\propto\pi(m)\prod_iE_i(m)$, $E_i={}_1F_1\!\big(\tfrac12;1+\tfrac{k_i}2;\tfrac{H_i(m)}2\big)$ with the arcsine size law. $H_i$ is the reading's explained energy: whitened data projected on the whitened candidate subspace. ours27 is $E_i=e^{H_i/2}$. | L1, L13, T6, T7, L10′, L4′ | **Changed** from ours26 |
| T9 | Stacked size | $\lVert\mathbf a^\ast\rVert=\big(\sum_i\lVert\mathbf a^\ast_i\rVert^2\big)^{1/2}$ per candidate, before averaging | L8, L12 | Unchanged, but its support in L8 must be rechecked under the restatement (O3). |
| T10 | The readout | $\widehat m=\int mA\,p\,dm\big/\!\int A\,p\,dm$ with $A(m)=E[\lVert\mathbf a^\ast\rVert\mid m]$ over the candidate cloud | T4, T8, T9 | **Fails L20 (T29). Open (O1).** |
| T11 | Sufficiency | data enter through $(P_g,Q_g,D_g,M_g)$ per noise pair | T8, T9 | **[flat] only.** Under ours28 the state is each reading's $H_i(\cdot)$; the log-law of a union is the sum of log-laws. |
| T12 | Combination | exact, as a product of per-reading factors | T8 | Four-number form [flat]; product form holds under ours28. |
| T13 | Totality | proper $\pi$ $\Rightarrow$ $\widehat m\in(0,\infty)$; ours28's totality checks pass (perpendicular, anti-parallel, force only, acceleration only) | T8, T10, L2 | Absorbs L2's old clause (E5). **Breaks at the all-zero experiment under the O1 repair.** |
| T14 | Zero readings give $s$ | readout at zero readings is $s$ | L2, L3′, L4, T5 | Scoped to this readout, [one pair], and $c=s$; rests on L3′, which is unruled (sweep E1: at $c=3s$ the readout is 2.095). **Contested by the O1 repair.** |
| T15 | Equal energies | $P=Q\Rightarrow\widehat m=\text{median}=s$ | T11, T5, L4 | [one pair] [flat]; unchecked under ours28 |
| T16 | A tilt is an unseen reading | $\lambda\sin2\theta_c$ at any centre $c$ equals one reading with $P=Q$, $D=2\lambda$, at the level of the law | T8 | Broadened (sweep E3); **[flat]**: under ours28 a reading's evidence is ${}_1F_1$, not exponential; unchecked |
| T17 | Convergence | $\widehat m\to m$ as $R^{\ast2}\to\infty$ | T8, T7 | Unchanged; ours28 checked by Monte Carlo (ours28 record §5) |
| T18 | Width | $\mathrm{Var}_{\rm true}/\mathrm{Var}_{\rm law}=1+\sum_c\theta_c'^2\big/\sum_c\theta_c'^2r^{\ast2}_c$, $\theta_c'=s_c/(s_c^2+m^2)$ | T8 [flat], L13 | **Reinterpreted:** the width error of L10, the asymmetric endpoint. Absent under ours28 to Monte Carlo precision. Per-component form (E6). |
| T19 | No mean | $E_p[m]=\infty$ under the half-Cauchy | T8 | unchanged |
| T20 | Mixed-instrument no-go | $\pi$ is declared before data, as part of the specification | T8, T14 | Unchanged; **the size law goes in the same slot.** |
| T21 | **C3** | the readout depends only on the law of the two joined sizes $(X,Y)$: no direction weight, no weight on the per-reading size profile | L15, L16, L17, L18, composition | **new, derived 28 Sept.** The betweenness representation step (Dekel, borrowed) is owed in writing (O5). |
| T22 | Full covariance | the error model must be a full $\Sigma_i$ per reading; ours26's diagonal model gives a different answer in a rotated frame | L16 | new (ours27) |
| T23 | Gaussian noise forced | by consistency given the flat push; by Z under ours28 | L11, L20 | new; the consistency route under tempered evidence is owed (O4) |
| T24 | Z holds for the law | an exact zero reading has $H_i\equiv0$, so $E_i$ is constant for any $\Sigma_i$, any $k_i$ | T8 | new; exact |
| T25 | Zero components carry nothing; $k$ does | measured exact zeros on some axes of a signal reading leave $H_i$ exactly as without those axes, at every $m$, whatever their $\sigma$. The law changes only through $k_i$. A 3D reading declared $k=1$ equals the 1D reading exactly. | T8 | **new, 29 Sept** |
| T26 | Limits of per-reading rules | no per-reading size rule has the right width at every push size; none is never overconfident (a pure-noise reading adds score noise and no curvature) | L19, T8 | new (no-borrowing record) |
| T27 | Own-world calibration | a proper law's intervals are calibrated on average in its own world; ours27 (improper) is not. The planted-mass yardstick condemns every proper starting law at extreme masses. | L4′, T8 | new (betweenness record §2, full-covariance record §5) |
| T28 | Mass and push scale are orthogonal | Fisher-orthogonal under ours28's model; the reference prior on mass is uniform in $\theta$ (the half-Cauchy) for any size law | T8 | new (Jeffreys-check record §1) |
| T29 | **The readout fails Z** | any readout that averages a push size over each reading's candidate cloud changes when a null reading is appended: the cloud has non-zero size, and that size depends on $m$ through the noise units. ours28, 3D, +50 null readings: 2.2524 → 2.2406; law unchanged to $10^{-14}$. Using the size of each reading's **best-guess (conditional-mean) candidate** passes Z exactly, passes swap and the exact limit, and leaves the all-zero experiment with no readout. | T10, L20 | **new, 29 Sept.** Uniqueness of the repair not shown. |

## 4. What is declared (the free shapes)

| input | current declaration | forced parts | free part |
|---|---|---|---|
| $\pi$ | half-Cauchy, $\pi(m)=c/(c^2+m^2)$ | symmetric (L4), counted once (T7), declared before data (T20), unit-covariant (L3) | shape: any $m^{-1}g(\ln(m/c))$ with $g$ even; centre with several noise pairs (L3′ unruled) |
| $G$ | arcsine, $\beta\sim\mathrm{Beta}(\tfrac12,\tfrac12)$ | symmetric (L4′), per reading (L19, L20), declared before data | shape: any $\mathrm{Beta}(a,a)$, or any even density in $\ln\omega$ |
| $N_i$ | $I_d$ unless the push's direction is known | — | the declaration ladder: $k=d$ → $k<d$ → a declared push covariance → old readings in the prior slot |

**One rule, two uses.** "Uniform in the angle the noise defines" gives both the
half-Cauchy on $m/s$ and the arcsine on $\beta$. That is one shape choice, not
two, but it is still a choice.

**F2 asks a question the records have not answered.** The full-covariance
record §5 argued that a declared shape is "the experiment's description", not
a rival definition of mass. Under F2, that is the "nobody cares" move unless
it is argued. It needs your ruling (O6).

## 5. Open, in the order the definition needs them

| | item | what would close it |
|---|---|---|
| **O1** | **The readout under Z** (T29). Three things cannot all stand as now written: Z at the point (L20); a readout at the all-zero experiment (L2 as d2 reads it); a readout averaging sizes over the candidate cloud (T10). The best-guess repair keeps Z and drops the second. | your ruling on the all-zero experiment; then O2 |
| O2 | **Uniqueness of the repaired readout.** Does composition (L5, L14) still single out a ratio of means when sizes are best guesses? Does any other readout pass Z? Can any Z-passing readout give a value at the all-zero experiment? | proof, or a counterexample family |
| O3 | **L8 restated.** Does "split, carrying the reading's state" still force the flat push size and the stacked length (T9)? The 27 Sept matrix had axis splitting as their sole support. | the matrix rerun on ours28, with a declared-subspace column and a size-law bend |
| O4 | L13 under the tempered evidence (the consistency route). | quadrature, as in matrix §4 |
| O5 | The betweenness representation step, written out (T21's borrowed step). | proof on candidate space |
| O6 | **The two shapes.** Forced by some property of mass, or a parameter of an alternative Newtonian mechanics (F2)? | a forcing argument, or a ruling that records them as alternatives |
| O7 | **Z's scope.** Your proposal of 29 Sept: two kinds of zero, a whole null reading and zeros alongside a signal. T25 says zero components contribute nothing and what matters is the declared $k$. Is "embedding in more dimensions" information (then Z is about whole readings), or should Z cover it (then ours28's $k$-dependence is a defect)? | ruling |
| O8 | Physically isotropic pushes under an anisotropic instrument: is noise-unit isotropy (L9) the right hedge there? | own-world test |
| O9 | Repeated measurements of one unchanged push: are they one reading (one scale) or several? L19 treats readings as separate pushes. | ruling on the type |
| O10 | Persistence (L1): the mass as a property of the object across series. | carried from 28 Sept; untouched |
| O11 | L3′, and with it T14. | ruling |

## 6. Standards for tests (from the rulings, for the tester)

- **Tier 1, properties.** Every L and T above that is stated as exact gets a
  pass/fail check: swap, units, rotation with cross-correlation, Z (law *and*
  point), axis splitting with state carried, $k=1$ equals 1D, totality,
  lumping, common force, betweenness.
- **Tier 2, own world.** Data drawn from the definition's own declared
  measures; intervals must be calibrated (T27). A failure here is a bug in
  the code or in a derivation.
- **Tier 3, other worlds.** Planted masses, fixed-length pushes, undeclared
  direction structure, shared push size. These say what the definition *does*
  when a declaration is wrong, not whether the definition is right. Every
  tier-3 failure so far has named an undeclared input.

## 7. Sources

- `mass_estimator_lemmas_2026-09-27.md` (superseded by this record)
- `ours26/ours26_sweep_of_the_flat_records_2026-09-27.md` §§4–5
- `ours27/ours27_full_covariance_2026-09-27.md`
- `ours27/ours27_perturbation_matrix_2026-09-27.md` §§3, 6
- `ours27/ours28_candidate_push_scale_as_nuisance_2026-09-28.md` §§1–4, 8
- `ours27/ours28_size_measure_jeffreys_check_2026-09-28.md` §§1, 4
- `ours27/ours27_c3_from_betweenness_and_the_scale_fork_2026-09-28.md` §§1–4
- `ours27/ours28_full_covariance_form_and_declared_subspace_2026-09-28.md` §§1–6
- `ours28b/ours28b_no_borrowing_between_readings_2026-09-28.md` §§1, 5
- `ours27/ours28_reference_implementation_and_readout_2026-09-28.md`
- `ours27/ours28_c3_narrow_form_and_the_reading_structure_2026-09-28.md` §§4, 9
- `../_note_mass_estimator_equation/the_mass_estimator_equation_d2.md` §3.1 (P1–P8, step 1)
- 29 Sept, this session: T25 and T29, computed with
  `ours27/ours28_reference.py` (numpy, scipy). T25: $H_i$ on a 7-point mass
  grid for the 3D reading $F=(4,0,0)$, $a=(2,0,0)$ against the 1D reading
  $(4,2)$, unit noise (difference 0.0); then the law and readout with the
  transverse SDs at 10, 1, 0.1, 0.01 and 0.001 (law identical in every case).
  T29: 1, 5 and 50 exact zero readings appended to one 1D and one 3D reading
  ($c=2$, unit noise), ours27 and ours28; and 20 appended to six weak 3D
  readings with the best-guess size computed by sampling the per-reading
  scale weights (3000 draws per mass node). Scripts not kept.
