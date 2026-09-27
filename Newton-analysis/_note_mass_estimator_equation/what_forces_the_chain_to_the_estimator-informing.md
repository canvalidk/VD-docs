# What Forces the Chain to the Estimator

## A step-by-step audit of the argument from Newton II's three corners to "mass must be estimated"

**Status:** Claude-authored review, 2026-09-02. Kind unset; filing is the author's call. Companion to `what_forces_the_ratio_of_means_readout` (same day), which audited the estimator's form; this audits the logic that makes an estimator necessary in the first place.
**Project:** VD Newton / inertial-mass estimation
**Purpose:** classify every step of the chain as *theorem* (follows from stated premises), *framework premise* (a VD commitment the chain relies on), or *ruling* (a decision, defensible but not forced); check the type-theoretic argument in particular; and record where the corpus's stated mechanism differs from the mechanism that actually holds.
**Source basis:** `type_theoretic_analysis_newton_II_mass_recovery_d2`, `vector_division_inertial_mass_measurement_d1`, `why_reconciliation_cannot_be_upstream_of_E10`, `why_the_estimator_is_the_definition`, `disagreement_rule_mass_estimator_trace`, `why_inertial_mass_must_be_estimated` (d3), `why_the_mass_entry_cannot_be_short` (d1), `why_the_mass_entry_must_be_long_joint_measurement_d3` (d2), and the full spec d1. All read in full.

---

## 1. Thesis

The chain holds. Its conclusion — that empirical mass determination is a checked, joint, policy-bearing estimation internal to the mass corner, with the residual retained and an absolute compatibility test — is forced from three framework premises and one ruling, and every step in between is a theorem. The corpus has, however, in several places given a *different* mechanism from the one that actually carries the step, and in one record built a result on the wrong mathematical object. None of these damages the conclusion. Several of them, once corrected, make it stronger.

The audit's main contributions:

1. The "type-theoretic asymmetry" is really a **counting asymmetry plus a positivity asymmetry**, and stating it that way unifies three things the corpus treats separately: the exact-branch consistency check, the empirical-branch residual, and the gate's degrees of freedom are all the same $d-1$.
2. The three "independent routes" to the asymmetry (d1 §4) are one route seen twice plus one that does not hold. The asymmetry is structural, but the evidence for that is the counting argument, not a triple coincidence.
3. The reconciliation dilemma's horn two is correct but under-specified: it bites only for **predictive** traces, and the record should say so, or it collapses into the epistemic objection it claims to be stronger than.
4. `why_the_estimator_is_the_definition` Results 1–2 are computed with the positive root of the stationarity quadratic, which is the profile's **maximum** on half of all null trials. Result 3 (the estimator is the definition) survives only with the current estimator as candidate B, and then rests on the flat latent measure.
5. The exact branch is **not** a fast path through the empirical operation, contrary to that record's §8.3: at exact zero-zero the two branches disagree, and the disagreement rule is right that they must.
6. The whole chain transfers verbatim to **every scalar-parameter corner of every law-triplet in the house**. Mass is the worked instance, not a special case.

---

## 2. The spine, classified

Each step is tagged. **[T]** theorem from what precedes; **[P]** framework premise; **[R]** ruling.

**S1 [P].** Newton II is an addressed relation on one material object over one interval in one inertial-frame-qualified account, with $m>0$. — The positivity of mass is a house commitment carried in E10's headword type. Everything about codirectionality, the positive cone, and the rejection of anti-aligned data descends from it. The corpus never says this once, plainly, and should.

**S2 [T].** The relation $R=\{(m,\mathbf a,\mathbf F):\mathbf F=m\mathbf a\}\subset\mathbb R_+\times\mathbb R^d\times\mathbb R^d$ has dimension $d+1$ in a $(2d+1)$-dimensional space: it imposes $d$ scalar constraints. Solving for a vector corner ($d$ unknowns, $d$ equations) is determined. Solving for the scalar corner (1 unknown, $d$ equations) is **overdetermined by $d-1$**, and additionally subject to the sign condition from $m>0$ and the degeneracy at $\mathbf a=\mathbf 0$. — This is the asymmetry. See §3.

**S3 [T].** Hence exact recovery is the inverse of $\Phi:(m,\mathbf a)\mapsto(m\mathbf a,\mathbf a)$, whose fibres are exactly $\{m_0\}$, $\varnothing$, or $(0,\infty)$ — the disagreement rule's trichotomy, which is therefore *exhaustive by construction* rather than by enumeration. Exact recovery is a checked operation returning a sum type.

**S4 [P].** A measurement result is a triple $(\widetilde{\mathbf x},\Sigma,P)$ — value, uncertainty, provenance — never a bare vector. — This is JCGM practice imported as a premise. It is what makes the branch *exact-vs-empirical* rather than *aligned-vs-misaligned* (d3 §8), and it is a stronger and cleaner premise than "alignment has measure zero", which becomes merely supporting once S4 is in place.

**S5 [T].** Independently produced results are generically off $R$; those that display as aligned are still S4-objects. Every empirical determination is on the empirical branch.

**S6 [P].** E8 and E9 must be runnable in traces where their output is not otherwise available — that is, as predictions. — This is what a law is *for*; it is a framework commitment, and it is the premise the reconciliation dilemma actually uses (§4 below).

**S7 [T].** From S4–S6: nothing upstream may alter the referents of `net-force` or `inertial-acceleration` toward each other (horn two), and delivering them unaltered leaves an exact definition inert (horn one). A compatible pair can only exist as a **distinct latent object** constructed where both inputs are in scope, and that construction *is* mass determination (the "third route" concedes the conclusion). Estimation is internal.

**S8 [T].** $R$ fixes the construction only on its own surface: any estimator from the two vectors alone that is rotation-invariant and dimensionally correct is $(|\widetilde{\mathbf F}|/|\widetilde{\mathbf a}|)\,g(\cos\theta)$ with only $g(1)=1$ fixed. A policy is additional input. (Footnote: in $d=2$ the invariant under rotations alone is the signed angle, so $g(\theta)$; $g(\cos\theta)$ needs parity invariance or $d\ge3$. Immaterial to the conclusion.)

**S9 [P→T].** Given the audit axiom (a trace must preserve why it ended where it did), the residual must be retained (the latent pair satisfies $R$ by construction, so only the discrepancy carries empirical content), and an absolute compatibility statistic is required, since a normalised posterior conditions on the model and cannot reject it (spec §23). The gate's statistic is a functional of the residual, so retention is forced by the gate being needed.

**S10 [P→T].** Given that the readout must compose as mass composes — additivity under lumping at common acceleration, additivity of inverse mass under common force, both house commitments at other entries — the readout is $\overline f/\overline\alpha$ (previous review).

**S11 [T].** The $d-1$ surplus equations of S2 are the $d-1$ residual degrees of freedom of the empirical fit and the $d-1$ degrees of freedom of the gate's $\chi^2$ (previous review §7). One number, three appearances. In $d=1$ it is zero: no consistency check, no interior residual, a pure sign test — and that is exactly where the corpus's "codirectional" reduces to "same sign".

**S12 [R].** The estimation capability lies outside the dictionary's authority; E10 names the operation and does not supply it (reconciliation record, ratified 08-01). — This is a ruling. It is what places the routing load *in E10* rather than in an E12; the load itself is forced by S3, S7, S9. Length is a consequence of location, and location is a consequence of the ruling.

So: three premises (S1, S4, S6), the audit axiom and the composition commitments (S9, S10), one ruling (S12), and theorems everywhere else. That is a forcing chain. What follows is where the corpus's *stated* reasons diverge from this spine.

---

## 3. The type-theoretic argument, checked

The corpus's form (type doc §3; d3 §3; d1 §3): E8/E9 are total on their input types; E10 is not, because the existence of $m$ depends on a value-level relation between the two inputs that neither type encodes. E8/E9's brevity is "subsidised by their types"; E10 "has nothing to inherit."

**What is right.** The partiality is real and the fibre structure of S3 is its exact content. The result-type formulation (preserve the reason) is correctly preferred over the partial-function one, and that preference is forced by the audit axiom.

**What is imprecise.** `PositiveMass` is itself a refinement type $\{x\in\mathbb R\mid x>0\}$, so E8's totality is not "no refinement" — it is a refinement on one argument, discharged by whoever *produced* that argument. The correct statement of the subsidy is: **a unary refinement can be pushed to the producer of the input; a binary (relational) refinement can only be discharged where both inputs are in scope.** E10's precondition $\mathrm{Codir}(\mathbf F,\mathbf a)$ is binary. So E10's honest total signature has a dependent pair as its input, $\Sigma(\mathbf F,\mathbf a).\mathrm{Codir}(\mathbf F,\mathbf a)\to\mathrm{PositiveMass}$ — which is d2 §7's `CertifiedNewtonIIPair` — and the dilemma (S7) says that on the empirical branch **the certificate is the estimator's output**. The type that would make E10 total is inhabited only by running the estimation. That is the type-theoretic form of "estimation is internal", and it is sharper than "nothing to inherit".

**What is conflated.** "A value-level relation" bundles two different conditions with different consequences:

- **Overdetermination** ($d-1$ conditions; codirectionality proper). Consequence: consistency check on the exact branch, residual on the empirical branch, gate dof. Absent in $d=1$.
- **Positivity and degeneracy** (sign from $m>0$; $\mathbf a=\mathbf 0$). Consequence: the cone, the boundary behaviour at zero readings, non-identification. Present in every $d$.

The disagreement rule already separates *agreement* from *identification*; this is the same split one level down. Keeping it separate is what lets S11 be stated.

**What does not hold: d1 §4's three routes.** The *algebraic* route ("$m=\mathbf F/\mathbf a$ is not a closed form because vector division is undefined") and the *type-theoretic* route are the same fact — $\Phi$ is not surjective — in two vocabularies. The *dimensional* route ("mass converts between unlike quantities; quotition fails") does not distinguish the mass corner at all: $\mathbf a=\mathbf F/m$ is also unlike-over-unlike, and division across dimensions is the most ordinary operation in physics. The asymmetry is structural, as d1 concludes, but the reason is S2, not agreement among three independent approaches. Since d1 uses the triple agreement as its evidence that "no cleverer wording restores symmetry", the evidence should be replaced, not the conclusion.

**"Vector division is not defined"** is the chain's rhetorical entry point and is not load-bearing. The operation "the unique $m>0$ with $\mathbf F=m\mathbf a$, when it exists" is perfectly well defined; what is undefined is a *notation*. d3 §5 handles this correctly. The load-bearing content is S2 plus S8.

---

## 4. The reconciliation dilemma, checked

Horn one (deliver unreconciled → exact definition inert) is a theorem given S4–S5.

Horn two as written: "if what counted as the object's acceleration depended on the direction of the net force, then supplying E9's input would require E9's output," so E8/E9 become **inoperable**. The record claims this *structural* objection is stronger than d3 §3's *epistemic* one (reconciled inputs make the law self-confirming).

Read literally, horn two overreaches. A reconciled $\mathbf a$ is built from the *measured* $\widetilde{\mathbf F}$ (the force wall), not from E9's *computed* output; in a trace where the force is already measured, E9 still runs — it just returns what was installed, which is the epistemic objection, not inoperability. Horn two is inoperability only in **predictive** traces, where E9 is invoked precisely because $\mathbf F$ is not otherwise available. There, a reconciled $\mathbf a$ requires a force that does not yet exist, and the trace cannot start. That is a genuine regress and it is the stronger objection the record wants — but only with S6 stated. The record should add the word *predictive* and cite S6; without it, a reader who assumes force is always measured will see horn two dissolve into d3 §3 and conclude the two are not independent after all. (An equivalent graph-level statement: reconciliation installs a 2-cycle $\mathbf a\leftrightarrow\mathbf F$ that bypasses $m$, collapsing the law-triplet into a degenerate cycle. Whether the constitution forbids 2-cycles outright is a question for the constitution; if it does, horn two is forced from the graph alone.)

The "third route" (a separate starred pair) is correctly shown to concede the conclusion. The trilemma is exhaustive: unaltered, altered, or distinct-object.

**The authority ruling gets stronger.** The record's rider says estimation is unlike differentiation because it is non-unique, so the trace must record the policy. The previous review changes the picture: the *form* of the readout is fixed by the dictionary's own composition commitments (S10); only the computational realisation and the policy inputs ($\rho_\Pi$, $\Sigma$, $Q_{\mathrm{crit}}$) are external. That is exactly the relationship the dictionary has with differentiation — the operation is determined by what kinematics requires of it; the numerical scheme is brought by the user. The analogy is tighter than the rider thought, and the non-uniqueness rider now applies to the policy inputs, not to the estimator.

---

## 5. `why_the_estimator_is_the_definition`, checked

**Result 1** ("the estimator always returns exactly one positive mass"; "antiparallel measured vectors do not break the estimator; they return a positive mass with a large residual"). The quadratic has exactly one positive root — correct. But for $s=\widetilde{\mathbf F}\cdot\widetilde{\mathbf a}<0$ the profile $Q_{\mathrm{prof}}(m)=(p^2+m^2q^2-2ms)/(\sigma_F^2+m^2\sigma_a^2)$ rises from $Q(0)=p^2/\sigma_F^2$ to that root and falls to $Q(\infty)=q^2/\sigma_a^2$: **the positive root is the maximum**, and the errors-in-variables estimator (the argmin) is at $m\to0^+$ or $m\to\infty$. The antiparallel sentence is false. The spec's §7 already says this; the record does not.

**Result 2** (null trials return $\sigma_F/\sigma_a$; table of medians and IQRs). Re-simulated (200,000 null trials, $\sigma_F=1,\sigma_a=0.5$): the *root* gives median 2.003, IQR $[0.83,4.84]$ — the record's numbers exactly. But $s<0$ on 50.2% of null trials, and on all of them the root is the maximum. The true argmin is exactly $0$ on 25.1% of null trials and $\infty$ on 25.1%; its median is still 2.006 by symmetry, and its IQR is $[0,\infty)$. So the record reproduced its table with the wrong object, and the symmetric median hid it. The record's "the mean does not exist" paragraph is likewise about the root's tail, not the estimator's.

**Result 3** (therefore B is the definition and A its limit). The argument's shape is sound: A and B disagree in truth value on a reachable input, and an outside standard adjudicates. But the input it needs — a null *measurement* returning a finite apparatus-scale value — is not delivered by the old B (a quarter of the time it returns $0$, a quarter $\infty$). It **is** delivered by the current estimator (spec §21: $\widehat m\sim\sigma_F/\sigma_a$, exactly, always). So Result 3 survives with the compatible-pair mean as candidate B and not otherwise. Its remaining dependencies, made explicit: (i) detection-limit practice as a legitimate determination — the record flags this as an undefended premise, correctly; (ii) the empirical zero-zero returning a number at all, which the disagreement rule §10 declines to require and d3 §16 declines to assume, and which in the current estimator rests on **$\rho_\Pi$ flat** (the log-flat measure collapses zero readings onto the exact boundary, previous review §5). So the chain from "estimation is internal" (forced) to "the estimator is the definition" (argued) passes through the choice of latent measure. That is not a defect; it is a dependency the corpus should draw.

**Result 4** (the singularity moved to $\sigma_F=\sigma_a=0$, path-dependent limit). Holds for the current estimator too, and for the same reason.

**§8.3 ("the `if` in E10 is a capability branch, not an operation branch — the exact clause is a fast path through the general operation").** This contradicts Result 4 in the same record, and the disagreement rule. At exact zero-zero the exact branch returns *undefined*; the empirical operation as $\sigma\to0$ returns $\sigma_F/\sigma_a$ along whatever path the instruments improved — Result 4's own content. The exact branch is therefore **not** the noise-free limit of the empirical one at the non-identification point, and an editor who reads §8.3 and merges the branches would manufacture a mass at exact $0/0$, which §7.3 of the disagreement rule forbids. The disagreement rule is right; §8.3 is wrong; E10 needs a genuine two-branch structure, with the branch condition being input *kind* (S4), not a fast path. This has a direct consequence for entry writing and should be ruled on.

**§6 (free-body test: improve one instrument and see whether the answer moves).** Survives unchanged with the current estimator, which tracks $\sigma_F/\sigma_a$ on null trials by construction.

---

## 6. The disagreement rule, checked

The trichotomy is exhaustive (S3). "Repair disagreement, preserve non-identification" is forced by the audit axiom: $F/0$ is a fact about the pair against the law, and ending the trace at "$m$ undefined" mislabels the halt cause. The empirical continuation is forced by S4. The exact-input rider and §7.3 are forced by S3. §7's five requirements on the estimator are all met by the spec.

One inconsistency. §8's compact function has case 2, `undefined when C = (0,∞)`, with no exact-input condition; the empirical qualifier appears only on case 3. Read as written, an empirical reading displayed as $(\mathbf 0,\mathbf 0)$ falls to case 2 and returns undefined — contradicting spec §21, which returns an apparatus-dominated estimate. The spec's own governing structure (§1) conditions that case on *exact* inputs correctly. §8 of the rule should be brought into line: the branch is by input kind first, then by fibre.

One dependency to make visible. The rule's §10 deliberately stops short of the empirical-null claim; the spec's §21 makes it; Result 3 above needs it. The rule is the minimal reconciliation argument, the spec is the full estimator, and the estimator-is-the-definition thesis lives at the spec's level, not the rule's.

---

## 7. "The entry must be long", checked

d1's account is a report of persuasion, and it says so. Its hinge (§3, the subsidy) is right in conclusion and imprecise in mechanism (§3 above). Its §5–7 — the check cannot be a precondition because failure is the normal case, and an asserted alignment misdirects toward "no mass" — are forced by S5 plus the behavioural-trigger principle.

d2 §7's five distinctions are the correct statement of the *load*, and its closing line — "the design may relocate the load; it may not erase it" — is the honest form of the claim. The derivation order is: load forced (S3, S7, S9) → location in E10 by ruling (S12) → length by consequence. The corpus already knows kind-not-length is the point (the 08-31 retraction); this is the same point as a derivation order. Stated that way, the length claim is not a concession and not a theorem either: it is what the ruling costs, and the ruling was correctly made.

---

## 8. A consequence the corpus should own

Nothing in S1–S12 uses anything specific to mass except the composition laws in S10. Every law-triplet in the house with a scalar-parameter corner — Hooke's $k$, the gravitational constant, resistivity, any "constant of proportionality" — has the same structure: two vector (or higher-dimensional) corners that are forward maps and total, and one scalar corner that is the inverse map, overdetermined by $d-1$, checked on exact inputs and estimated on empirical ones, with the same dilemma forbidding upstream reconciliation and the same audit axiom forcing retention of the residual. d1 §1 records that "the Hookean entries define their constants relationally, never as quotients" as if that were the convention that made the short mass entry look acceptable. It is the reverse: the mass argument shows those entries carry the same unpaid load. The chain is a theorem about scalar-parameter corners, and mass is the instance where the house first noticed.

---

## 9. Corrections owed, by record

1. **Type doc §3 / d3 §3 / d1 §3.** Replace "nothing to inherit" with the unary/binary refinement statement; split overdetermination from positivity; state $m>0$ as a house premise once.
2. **d1 §4.** Retire the dimensional route; the other two are one. Replace the triple-agreement evidence with the counting argument.
3. **Reconciliation record §1, horn two.** Add "predictive" and cite S6. Optionally restate as the 2-cycle objection, pending a ruling on whether the constitution forbids degree-2 cycles.
4. **Reconciliation record, rider on non-uniqueness.** Reassign the non-uniqueness to policy inputs; the estimator's form is dictionary-determined (previous review).
5. **`why_the_estimator_is_the_definition`.** Result 1's antiparallel sentence is false; Result 2's IQRs are the root's, not the estimator's; Result 3 stands only with the current estimator as B and depends on $\rho_\Pi$ flat; §8.3 is wrong and contradicts Result 4 and the disagreement rule.
6. **Disagreement rule §8.** Condition case 2 on exact inputs.
7. **All records.** State once that the chain generalises to every scalar-parameter corner.

None of these is a `corrects`; each record's conclusion survives. They are scoping, and they should be filed as such under the 08-26 rule.

---

## 10. Verdict

The logic that leads to the estimator is forcing. It rests on three premises a VD reader has already accepted by being one — addressed positive mass, measurements as triples, laws as predictions — plus the audit axiom, the composition commitments, and one ruling about authority that was correctly made. The corpus reached the right conclusion at every step. Where it went wrong was in *which* argument it thought was carrying the step: the type-theoretic asymmetry is a counting asymmetry; the three routes are one; horn two needs the word "predictive"; and one record computed a maximum and called it the estimate. The fix in each case is to swap the stated reason for the operative one — and in the last case, to let the current estimator do the job the old one could not.

The single most useful sentence to add to the corpus is S11: **the $d-1$ conditions that make exact recovery a check are the $d-1$ residual degrees of freedom that make empirical recovery an estimation, and they are the $d-1$ degrees of freedom of the gate.** That is the chain in one number.
