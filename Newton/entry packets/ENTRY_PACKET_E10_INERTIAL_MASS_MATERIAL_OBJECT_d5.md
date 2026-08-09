# Entry Packet: E10 Inertial-Mass-Material-Object — d5

Status: successor after the upstream-reconciliation correction. This packet
supersedes d4 as the working account of E10. It does not promote new wording into
the active Design 2.1 entry draft, and it does not change the d4 candidate
wording at all — the wording is a placeholder by Can's instruction, and what
changed here is the architecture around it. The d4 packet remains as the
pre-correction reasoning state.

## ENTRY PACKET

Entry id:
  [E10]

Headword:
  inertial-mass-material-object

Status:
  candidate; not yet promoted

Role:
  triplet-winter

Law/block:
  Newton II; checked exact-recovery and joint-estimation corner of the addressed
  triplet

Source status:
  Revised from the E10 d4 packet using
  `Newton-analysis/vector_division_mass_estimation/why_reconciliation_cannot_be_upstream_of_E10.md`,
  a standalone correction note authored in-repo 2026-08-01 from a working session
  with Can. The governing argument in that note is ratified; the two consequences
  applied below (open question 3, the permanence of capability-naming) are
  ratified. Its expository framing is not.

Managed sources:

  1. `Newton-analysis/vector_division_mass_estimation/why_reconciliation_cannot_be_upstream_of_E10.md`
     — governing correction for this packet.
  2. `Newton-analysis/vector_division_mass_estimation/why_the_mass_entry_must_be_long_joint_measurement_d3.md`
     — current draft of that note; supplies the observation / measurement /
     joint-estimate architecture and the retention argument, both retained here.
  3. `Newton-analysis/vector_division_mass_estimation/type_theoretic_analysis_newton_II_mass_recovery_d2.md`
     — exact checked-recovery analysis, sections 1–6, still live.
  4. `Newton-analysis/vector_division_mass_estimation/vector_division_inertial_mass_measurement_d1.md`
     — still-live estimator mathematics: estimator non-uniqueness, the
     errors-in-variables structure, limiting cases, the multiple-trial argument.
     Load-bearing in d5 for the non-uniqueness rider.
  5. `Newton/entry passes/E8_ENTRY_WRITING_PASS_2026-07-25.md` — the E8 definiens.
     Load-bearing in d5: it is what makes the governing argument's first premise
     a fact about the VD rather than a convenient reading. See the verification
     note below.
  6. `Newton/entry packets/ENTRY_PACKET_E10_INERTIAL_MASS_MATERIAL_OBJECT_d4.md`
     — immediate predecessor; superseded as the working account, retained as the
     pre-correction state.
  7. `Newton/nml/nml2/nml2.1/NML2_1_CONTENT_d2.md` — NML2.1 content authority and
     lesson-side exact/measured boundary.
  8. `Newton/nml/nml2/nml2.1/NML2_1_LESSON_PLAN_d1.md` — lesson-plan draft,
     subordinate to content d2 where they conflict.
  9. `Theory/triplet_as_admission_event/why_the_triplet_rule_is_needed_d2.md` —
     supplies the warrant/content separation used below to bound what E10 is
     required to establish.

Selection method:
  Inherited d4's search, then applied every consequence of the governing
  correction to the packet, the lesson boundary, the IRIL, the evaluator
  architecture, the tests, and the open-question list. The wording sections were
  deliberately left untouched and re-checked for consistency rather than revised.

---

### Governing correction

d4 established *what* the empirical operation is. It did not establish *where*
that operation lives, and it left standing an assumption that makes E10 look
repairable by better wording: that reconciliation could in principle be a prior
operation — performed by metrology, by an evaluator pre-pass, or by a separate
numbered entry — which then hands E10 a conforming pair.

That assumption is unavailable, and the reason is internal to the triplet.

```text
E9 takes inertial-acceleration as an input and returns net-force.
   -> acceleration must be identifiable WITHOUT reference to net-force.

E8 takes net-force as an input and returns inertial-acceleration.
   -> net-force must be identifiable WITHOUT reference to acceleration.
```

Neither quantity may be defined by reference to the other, or the entry that
consumes it would need its own output in order to obtain its input. The channels
are in fact separate: a net force is determined from summed component forces,
calibrated interactions and field strengths, with no trajectory data; an
acceleration is determined from differentiated position samples or accelerometer
output, with no force data.

Two vectors produced by unrelated channels, each carrying its own error, will not
in general stand in the exact relation for any positive scalar. So consider what
an upstream reconciliation step could deliver:

```text
HORN ONE  — it delivers the quantities as its channels determined them.
            They are generically non-conforming, and an exact definition of
            mass is INERT over the entire domain on which traces actually run.

HORN TWO  — it delivers a reconciled pair.
            Fixing acceleration required force direction and vice versa.
            E8 and E9 become INOPERABLE.
```

There is no third delivery. Therefore **the estimation of a conforming pair is
internal to mass determination** — a constitutive part of what recovering a mass
from empirical inputs consists in, not a preprocessing step that precedes it.

**Verification note.** The first premise is not an interpretive choice. E8's
definiens, settled in the 2026-07-25 entry writing pass, is *"For one
material-object, its net-force divided by its inertial-mass."* E8 genuinely takes
net-force as an input. The VD chose dynamical rather than kinematic definitions
for the triplet, and the sharing requirement follows from that choice. The
argument is load-bearing on a commitment already made.

---

### What d5 changes from d4

  1. **Open question 3 is closed by dissolution.** Not answered — dissolved. Both
     of its remaining options assumed the estimator needs a home inside the
     dictionary. See the authority section below.
  2. **Decision 11 is restated as permanent.** Capability-naming is not a
     deferral pending an E12 ratification. It is what a reference to an external
     competence looks like, and it stays.
  3. **The lesson boundary's closing line is corrected.** "Whether that later
     capability is E12 or a separately named entry remains open" is withdrawn.
  4. **Decision 1 acquires its rationale.** It was asserted in d4 and is now
     derived: exact-versus-measured is the *dispatchable* form of the
     distinction. See the settled-objections section.
  5. **Open question 6 is relocated, not solved.** It is a declared-policy
     question in the admission sense, not a defect in decision 8.
  6. **A non-uniqueness rider is added** to the policy requirement, naming its
     source.
  7. **A bound is added on what E10 is not required to establish**, so that the
     retention theorem and the object-scoping question stop being read as gaps in
     this entry.
  8. **A settled-objections section is added**, recording the generator rather
     than only the instances.

### Carried forward from d4 unchanged

All twelve d4 decisions survive except decision 11, whose rationale is corrected
without changing its operative content. The exact branch, the three-stage
architecture, `JointNewtonIIFit`, the joint-result contents, the residual
argument, the circularity gate, the lesson boundary's teach/must-not-teach lists,
the IRIL and IRIE content, the boundary behaviours, the result vocabulary, and
all twelve acceptance tests are retained. Nothing in d4 is silently dropped.

**The wording is untouched.** Candidates A–D and the draft entry are reproduced
verbatim from d4. Candidate A was re-checked against the new results and is
consistent with them — it names the operation without supplying it, which is
exactly what the authority bound below requires. That the correction forces no
wording change is itself worth recording.

---

### Preserve

  - inertial mass is a positive scalar;
  - all three Newton-II quantities belong to the same material object and carry
    compatible frame and time/interval qualifications;
  - the inward relation is
    `net-force-material-object = inertial-mass-material-object ×
    inertial-acceleration-material-object`;
  - an explicitly exact compatible nonzero pair determines one positive scalar;
  - an exact zero/zero pair is compatible but non-determining;
  - exact one-zero and exact non-codirectional pairs admit no exact positive-mass
    fit for those premises;
  - supplied mass bindings remain distinct from exact recoveries, joint
    estimates, and consistency restatements;
  - the lesson-facing joint route remains `estimate two underlying codirectional
    vectors and then recover the positive scalar relating them`;
  - mass-address origination, persistence, additivity, gravitational bridges,
    and force-composition provenance remain outside E10;
  - **new:** the force-side and acceleration-side determinations remain
    separately identifiable, because E8 and E9 depend on it.

### Change / reject

All d4 prohibitions stand. Added in d5:

  - Do not install any operation that reconciles the net-force and acceleration
    inputs *before* E10 receives them. Anything upstream acts on quantities E8
    and E9 also consume, and reconciling them there makes those entries
    inoperable.
  - Do not treat the estimation capability as an unassigned dictionary entry
    awaiting a number. It is not in the dictionary.
  - Do not let E10 supply, teach, or certify the estimator. E10 names the
    operation.
  - Do not read the retention requirements as part of the definitional core.
    They belong to the evaluator and rest on a separate argument.

Plain purpose:
  Complete the Newton-II triplet by identifying the positive scalar relating one
  material object's addressed inertial acceleration and net force, while
  distinguishing checked recovery from exact supplied quantities from joint
  inference using independent empirical measurement results. E10 names the joint
  operation; it does not supply it. NML2.1 exposes the route but does not teach
  the estimator mathematics.

Relationship to the packet set:

  - one winter daughter of E8;
  - relates E9's net force to E8's inertial acceleration;
  - unlike E8 and E9, does not define a total operation on its ordinary pair of
    input quantity types;
  - **depends on E8 and E9 keeping their inputs independently identifiable, and
    is the reason no reconciliation may be sited upstream of it**;
  - triggers, but does not itself choose, teach, or own, the joint estimation
    machinery;
  - deliberately does not replace the deferred outward mass-address wall.

Trace-critical headword mentions:

  - net-force-material-object
  - inertial-acceleration-material-object

Other structural qualifiers:

  - one material object owns the mass, force, and acceleration values;
  - each force/acceleration input is classified as explicitly exact/supplied or
    empirically measured;
  - a measurement result carries uncertainty and provenance rather than only a
    displayed vector value;
  - the two empirical channels must have sufficiently independent provenance for
    the joint result to stand as independent evidence for mass;
  - a joint fit preserves both original measurement results and the discrepancy
    between them and its latent outputs;
  - **new:** the two empirical channels must remain separately identifiable at
    the point E10 receives them.

Forbidden headword mentions / hidden imports in the eventual entry wording:

  - scale / weight / gravitational mass / amount of matter / density mass;
  - mass additivity;
  - target construction / trackability / lumping;
  - interacting-forces-set / attached-force;
  - constancy or persistence across trials;
  - a particular estimator, covariance model, or fitting formula;
  - a claim that the independently measured values were already the reconciled
    latent values;
  - **new:** a numbered entry for the estimation capability;
  - **new:** any claim that a prior operation has already delivered a conforming
    pair.

Question or trace moment this helps with:

  1. Exact branch: do these explicitly exact force and acceleration values admit
     one positive scalar, and if so what is it?
  2. Empirical branch: what joint operation is required to infer mass from two
     independent measurement results?
  3. Fit-standing branch: what discrepancy and provenance must survive before
     the joint result can count as evidence rather than self-confirmation?
  4. Consumption branch: is there already a licensed supplied mass binding?

Witness kind:
  addressed material-object force-accounting commitment; checked exact recovery
  or joint-estimation handoff, not the deferred material-object construction or
  mass-persistence machinery.

Slots read:

  - material-object identity;
  - net-force-material-object and inertial-acceleration-material-object;
  - exact/supplied versus empirical-measurement status;
  - common frame, time/interval, units, and quantity qualifications;
  - supplied mass binding, where one exists;
  - licence and provenance status;
  - for empirical inputs, separate `MeasuredForceResult` and
    `MeasuredAccelerationResult` values, uncertainties, and provenance;
  - measurement-channel independence or circular-dependence record;
  - a declared estimation policy only after routing to the empirical branch.

Slots written / exposed:

  - inertial-mass-material-object when supplied, exactly recovered, or returned
    as a field of a licensed joint fit;
  - `ExactMass(m)`;
  - `ZeroZeroUnderdetermined`;
  - `ZeroNonzeroInconsistency`;
  - `NoncodirectionalExactInconsistency`;
  - `EstimationRequired` when empirical inputs reach the NML2.1 boundary without
    in-scope machinery;
  - `JointNewtonIIFitResult` when licensed machinery is available;
  - supplied / exact-recovered / jointly-estimated / consistency-restatement
    provenance.

---

## Exact and empirical operations

Unchanged from d4.

```text
MassExact:
  ExactForceVector × ExactAccelerationVector
  -> MassRecoveryResult

  ExactMass(m)
  ZeroZeroUnderdetermined
  ZeroNonzeroInconsistency
  NoncodirectionalExactInconsistency
```

For an exact, nonzero, codirectional pair:

```text
m = |net force| / |inertial acceleration|
```

The codirectionality check establishes that a positive scalar exists. The
magnitude quotient then reads that scalar; it does not establish compatibility.

```text
MeasuredForceResult(displayed_force, uncertainty, measurement_provenance)
MeasuredAccelerationResult(displayed_acceleration, uncertainty, measurement_provenance)

JointNewtonIIFit:
  MeasuredForceResult
  × MeasuredAccelerationResult
  × EstimationPolicy
  -> JointNewtonIIFitResult

JointNewtonIIFitResult(
  original_force_measurement,
  original_acceleration_measurement,
  underlying_force = F*,
  underlying_acceleration = a*,
  inertial_mass = m,
  uncertainty,
  corrections_or_residual,
  goodness_of_fit,
  estimation_policy,
  measurement_and_policy_provenance,
  independence_or_circularity_status
)
```

subject to `F* = m a*`, with `m > 0`. Neither latent vector is selected
independently once the constraint is imposed.

---

## The estimation capability and the limit of the dictionary's authority

`JointNewtonIIFit` is a real operation and it is necessary. It is not a VD entry,
and no VD entry owns it.

**The differentiation precedent.** E8 returns an inertial acceleration. Obtaining
one in practice means differentiating position data. The VD does not define
differentiation, does not number it, and does not own it. It is external
mathematical competence the user brings. None of that makes E8 defective or
incomplete.

The same holds here. Estimating a latent codirectional pair is external
competence, invoked *within* the mass determination, not a node in the trace.

This is what closes open question 3. Its remaining options were both malformed,
because both assumed the estimator must have a home inside the dictionary:

```text
E12 as an upstream estimation entry            -> ruled out (the dilemma)
a separate measurement entry feeding E10       -> ruled out (the dilemma)
a dictionary capability E10 owns and invokes   -> ruled out (nothing to own)
E10 teaching the estimator itself              -> ruled out (outside authority)
```

What E10 must do is **name the operation, not supply it**. Capability-naming is
therefore permanent, not a deferral.

**This dissolves the pedagogical tension.** A first-year uses acceleration
without being able to derive a numerical differentiation scheme. A first-year can
likewise hold *the true pair must be estimated* without meeting orthogonal
distance regression. That is not a gap in the entry. It is the ordinary
relationship between a dictionary and the mathematics its users bring.

**One rider, and its source.** Unlike the textbook case of differentiation, this
external competence is non-unique in a way the estimator analysis records:
magnitude-ratio, projection and componentwise estimators disagree, and the
$g(\cos\theta)$ result shows the disagreement is not a detail. So the trace must
record *which policy was applied*, where a trace invoking differentiation is not
usually asked to. The requirement was already present — policy and provenance are
both in the joint-result contents — but its source is now named: it comes from
the non-uniqueness of the external competence, not from anything peculiar to the
mass corner.

*Open, flagged, not committed:* numerical differentiation of noisy position data
is also policy-laden — filter, window, spline order — and materially affects the
result. If that is right, E8 carries the same latent under-specification, unnoticed
because the obstruction is only visible at the mass corner. Recorded as a question
for the E8 packet, not as a claim of this one.

---

## What E10 is not required to establish

Recorded because both of these have been read as defects in E10 and are not.

**The retention theorem is a separate chain.** That the residual, the original
measurements, the provenance and the independence status must be retained does
*not* follow from the argument above. It follows from the self-confirmation
argument: the latent outputs satisfy Newton II by construction, so the
discrepancy is the only thing still carrying empirical content. Two theorems, two
chains. Conflating them is what lets evaluator requirements migrate into the
definitional core and inflate the entry.

**Object-scoping is warrant, not content.** `JointNewtonIIFit` returns a
trial-scoped value, while the headword `inertial-mass-material-object` claims a
property of the object. What licenses that is the admission event, not E10.
Per the triplet note, alpha governs the warrant and the triplet records the
content of the admission; asking a triplet corner to re-justify its own admission
is a category error. The object-binding is carried by the `-material-object`
suffix, which is a further reason the suffix cannot be traded for opaque
anaphora. Where cross-trial aggregation lives is a question for the external
estimation competence, not for this entry.

---

## Lesson boundary

NML2.1 should transfer the topology of the empirical operation without teaching
its statistical formula. The teach / must-not-teach lists are unchanged from d4.

Students should retain:

```text
estimate two underlying codirectional vectors and then recover the positive
scalar relating them
```

NML2.1 may teach:

  - exact supplied values and empirical measurement results are different input
    kinds;
  - exact mass recovery checks compatibility before taking a magnitude quotient;
  - exact zero/zero does not determine mass;
  - independent force and acceleration measurements need not be codirectional;
  - every empirical mass determination takes the joint branch, even when the
    displayed values happen to align;
  - a measured disagreement does not mean the object has no mass;
  - the joint estimator would estimate two underlying codirectional vectors and
    then recover the positive scalar relating them;
  - the course-level output may be
    `estimation required — method outside the present scope`.

NML2.1 must not teach or silently select:

  - magnitude ratio as a general estimator for measured data;
  - either projection estimator;
  - componentwise averaging;
  - least squares, errors-in-variables, Deming regression, orthogonal-distance
    regression, likelihood construction, or covariance weighting;
  - how an estimation policy is selected or certified;
  - how the force-side or acceleration-side uncertainty models are certified;
  - how later force-composition machinery constructs net force.

The boundary is capability-named, permanently:

```text
NML2.1 owns recognition and conceptual routing.
The joint-mass-estimation capability owns policy selection and execution,
and lies outside the dictionary's authority.
```

d4's closing line — "whether that later capability is E12 or a separately named
entry remains open" — is **withdrawn**. It is neither.

---

## Boundary behavior

As d4, with one addition:

  - Licensed supplied binding: return it, preserving provenance and licence.
  - Exact, nonzero, codirectional pair: return `ExactMass(m)`.
  - Exact zero/zero pair: return `ZeroZeroUnderdetermined`; do not overwrite a
    licensed supplied binding.
  - Exact pair with exactly one zero: return `ZeroNonzeroInconsistency`.
  - Exact nonzero pair with no positive-scalar fit: return
    `NoncodirectionalExactInconsistency`.
  - Any empirical measurement-result pair without in-scope joint machinery:
    return `EstimationRequired`, irrespective of displayed alignment.
  - Empirical results with a declared, licensed policy: invoke `JointNewtonIIFit`
    and preserve all required result fields.
  - Empirical inputs whose evidential paths depend on the demanded mass or on
    each other through this same Newton-II relation: mark the outcome as a
    consistency restatement, not an independent mass determination.
  - A joint output that omits the original results, residual, uncertainty,
    policy, or provenance: reject as an incomplete fit result.
  - Missing exact/measured status: halt for classification; do not guess.
  - Missing value: demand it if the graph has an independent route; otherwise
    return insufficient information.
  - Address, frame, time, type, or dimensional mismatch: halt before either
    exact recovery or joint estimation.
  - Expired binding: do not reuse it automatically.
  - **New:** an input that arrives already adjusted against the other input
    through Newton II: reject the input, not merely the result. The adjustment
    has corrupted a quantity E8 or E9 also consumes.

---

## IRIL — ideal residually imparted logic

Allowed:

  - On a demand for `inertial-mass-material-object` for one material object,
    first return a licensed supplied binding if present.
  - Otherwise demand that object's net-force and inertial-acceleration inputs
    together with their exact/supplied or empirical-measurement status and
    common qualifications.
  - **New:** confirm that each empirical input was determined by its own channel
    and was not adjusted against the other before arrival.
  - If the pair is explicitly exact, run `MassExact`:
    1. check zero/nonzero status;
    2. for a nonzero pair, check whether one positive scalar relates them;
    3. only after compatibility passes, divide net-force magnitude by
       inertial-acceleration magnitude;
    4. return the appropriate result-valued outcome.
  - If the inputs are empirical measurement results, preserve each result,
    uncertainty account, and provenance as a separate input to the joint branch,
    regardless of displayed codirectionality.
  - Test whether either empirical input already depended on the demanded mass or
    on the other input through the same Newton-II relation.
  - Within NML2.1, stop the empirical branch at `EstimationRequired` and state
    the conceptual route: estimate two underlying codirectional vectors and then
    recover the positive scalar relating them.
  - Outside that lesson boundary, invoke `JointNewtonIIFit` only with a declared,
    licensed estimation policy.
  - Preserve the original measurement results alongside the latent values and
    retain uncertainty, corrections or residual, goodness of fit, policy, and
    provenance in the joint result.
  - Record whether a mass value was supplied, exactly recovered, jointly
    estimated from sufficiently independent channels, or merely restated through
    circular inputs.
  - When a licensed mass binding and the other two corners are all present, use
    the relation as a consistency check; do not silently replace the binding.

Blocked:

  - Dividing one vector by another.
  - Dividing magnitudes before checking compatibility on the exact branch.
  - Applying the exact branch to empirical results because their displayed
    vectors align.
  - Sending only visibly non-codirectional empirical pairs to joint estimation.
  - Rewriting either independent measurement so that it already satisfies
    Newton II before the joint fit.
  - Returning only a mass or only compatible latent values from the joint fit.
  - Discarding the original discrepancy, correction record, or goodness of fit.
  - Reporting circularly derived inputs as independent evidence for mass.
  - Applying an undeclared direction tolerance, magnitude floor, magnitude ratio,
    projection, componentwise division, or fitting formula.
  - Returning a value from an exact zero/zero trial.
  - Combining values belonging to different material objects or incompatible
    frame/time qualifications.
  - Treating scale readings, weight, gravitational mass, density mass, or amount
    of matter as this value without a separately licensed bridge.
  - Inferring mass additivity, target construction, persistence, or constancy
    from the inward triplet relation.
  - Reusing an expired binding.
  - **New:** accepting an input that a prior operation reconciled against the
    other input through Newton II.
  - **New:** wiring the joint-estimation capability to an entry number.

Trace consequence:

  - exact, nonzero, codirectional: return the magnitude quotient, marked
    `exact-recovered`;
  - exact zero/zero, no supplied binding: return `ZeroZeroUnderdetermined`;
  - exact zero/zero, licensed supplied binding: retain the binding and mark the
    trial compatible but non-identifying;
  - exact one-zero or exact non-codirectional: return the corresponding no-fit
    result for the supplied exact premises;
  - any empirical pair without a licensed in-scope policy: return
    `EstimationRequired`, even if its displayed vectors align;
  - empirical pair with licensed policy: return a complete
    `JointNewtonIIFitResult`, not a bare mass estimate;
  - circular empirical provenance: preserve any consistency result but withhold
    independent-evidence standing;
  - fit missing its residual or original measurements: reject as incomplete;
  - absent independent values: terminate as insufficient information rather than
    recurse through the triplet;
  - **estimator ownership is not unresolved.** Route by the capability name
    `joint-mass-estimation` permanently; it is outside the dictionary and will
    not later acquire an entry number.

---

## IRIEs — ideal residually imparted effects

Reader/modeler behaviour to install:

  - Ask first whether the inputs are explicitly exact quantities or empirical
    measurement results.
  - Treat exact mass recovery as a checked operation, not an unconditional
    rearrangement.
  - Preserve independent force-side and acceleration-side measurement results
    before applying Newton II jointly.
  - Route every empirical mass determination to joint estimation, including an
    accidentally or approximately aligned displayed pair.
  - Distinguish the original measurements from the latent codirectional values
    selected by the joint model.
  - Require a declared estimation policy and retain uncertainty, residual,
    goodness of fit, and provenance.
  - Check whether the evidential paths are sufficiently independent before
    calling the result an empirical mass determination.
  - Distinguish exact incompatibility, empirical estimation required, poor fit,
    and circular restatement.
  - **New:** expect the two empirical inputs to disagree, and do not seek a prior
    step that removes the disagreement before mass is determined.
  - **New:** treat the estimation as part of determining the mass, not as cleanup
    performed beforehand.

Anti-habit / anti-misread:

  - Do not write or calculate unrestricted `force / acceleration` for vectors.
  - Do not let `0/0` choose a mass.
  - Do not confuse displayed empirical alignment with exact supply.
  - Do not confuse a measurement with a latent value already reconciled under
    Newton II.
  - Do not confuse `no exact fit for these exact premises` with `this object has
    no mass`.
  - Do not confuse `estimation required` with `experiment unusable`.
  - Do not allow an imposed fit to confirm itself by hiding its residual.
  - Do not count a circular reconstruction as independent evidence.
  - Do not substitute weight, scale reading, gravitational mass, or amount of
    matter for inertial mass.
  - **New:** do not look for the entry that "does the estimation". There isn't
    one, and the absence is not an omission.
  - **New:** do not read `estimation required` as a placeholder awaiting a future
    entry number.

---

## Suggested wording

**Unchanged from d4. Placeholder by instruction; not revised in this packet.**

### A — chosen candidate, carried forward

```text
inertial-mass-material-object :=

For one material-object, the positive scalar that multiplies its
inertial-acceleration-material-object to give its net-force-material-object.
For exact supplied vectors, first check that both are nonzero and codirectional,
then divide the net-force magnitude by the inertial-acceleration magnitude. A
zero-zero pair does not determine the scalar; any other incompatible exact pair
has no exact positive-mass fit. For empirical force and acceleration measurement
results, keep the two results separate and check their provenance. With
sufficiently independent results and a declared policy, jointly estimate two
underlying codirectional vectors and the positive scalar relating them; if no
policy is available, report that estimation is required. Retain the original
measurements, their uncertainty and discrepancy, the policy, and their
provenance. If either result already depended on the mass being sought or on the
other result through this relation, the outcome is only a consistency
restatement.
```

Consistency re-check against d5's results: candidate A names the joint operation
and does not supply it; it requires the two results be kept separate, which is
what the dilemma demands; it does not refer to any prior reconciling entry. No
change forced.

### B — lesson-facing compression

```text
For empirical force and acceleration measurement results, estimate two
underlying codirectional vectors and then recover the positive scalar relating
them.
```

### C — d3 measured sentence, rejected

```text
For non-codirectional measured vectors, estimate two underlying codirectional
vectors and then recover the positive scalar relating them.
```

Rejected in d4 because empirical provenance, not visible alignment, selects the
joint branch. Rejection stands.

### D — short refined-type form, deferred

```text
For a certified Newton-II pair, the positive scalar relating its force and
acceleration.
```

d4 deferred this as hiding the machinery inside `certified`. **d5 upgrades the
deferral to a rejection.** A "certified pair" is precisely the output of an
upstream reconciliation, and horn two shows no such predecessor can exist without
making E8 and E9 inoperable. There is no named predecessor that could construct
the refined input, so the form is not merely opaque — it presupposes something
the triplet forbids.

---

## Draft entry

As candidate A above, unchanged from d4. Intentionally longer than E8 and E9: it
makes the branch, the joint operation, and the standing of the result visible. It
does not teach or choose the estimator formula.

---

## Deep audit add-on

Role test:
  E10 remains inward-facing. It exposes the other two Newton-II quantities and
  the branch required to recover or estimate the scalar relating them. It does
  not construct the material object, certify persistence, compose force
  contributions, own the estimation capability, or teach a statistical fitting
  rule.

Necessary / sufficient / asymmetric relations:

  - On the exact branch, a nonzero codirectional pair under compatible
    qualifications is sufficient to determine one positive scalar.
  - Ordinary `ForceVector × AccelerationVector` typing is not sufficient.
  - Exact zero/zero is compatible but not identifying.
  - Exact one-zero and exact non-codirectional pairs admit no positive-scalar fit.
  - Empirical alignment is neither necessary nor sufficient to license exact
    recovery.
  - Separate empirical measurement results plus a declared estimation policy are
    jointly sufficient to define a joint estimation problem; the displayed values
    alone are not.
  - A complete joint result requires latent values, mass, uncertainty, residual
    or goodness of fit, policy, and provenance.
  - Sufficiently independent evidential paths are necessary for the result to
    count as independent evidence for mass.
  - Matching material-object address, frame, interval, quantity type, units, and
    epistemic status is necessary before either branch runs.
  - **New:** independent identifiability of the two inputs is necessary for E8
    and E9 to run, and therefore necessary for any account of E10 that leaves the
    triplet operable.
  - **New:** no upstream operation is sufficient to supply E10 with a conforming
    pair without destroying that independence.

Quantifier or modality:
  `the positive scalar` states the Newton-II role. `exact supplied` and
  `empirical ... measurement results` are branch selectors. `Jointly estimate`
  declares that neither latent vector is selected independently after the
  Newton-II constraint is imposed, and additionally that the operation is
  internal to this determination rather than performed beforehand. `Retain` makes
  fit standing part of the result rather than optional evaluator metadata.

Suspends for human/model input?
  yes; for missing values, missing epistemic classification, missing
  qualifications, unresolved measurement provenance, or an empirical request
  whose joint estimation policy is not installed in the current scope.

Residual provenance ledger:

| Phrase | Backing |
|---|---|
| `For one material-object` / `its` | Current E8–E10 one-owner grammar; prevents cross-target mixing without a free address mark. |
| `positive scalar` | Newton II's mass commitment; excludes antiparallel exact fits and states isotropic response. |
| `multiplies ... to give` | Stock scalar-vector arithmetic; states the inward relation without inventing vector division. |
| `exact supplied vectors` | NML2.1 content d2's required exact/measured distinction and the surviving exact analysis. |
| `nonzero and codirectional` | Exact `MassRecoveryResult` domain preserved from the type-theoretic analysis. |
| `divide the net-force magnitude by the inertial-acceleration magnitude` | Exact scalar readout after compatibility, never a general empirical estimator. |
| `zero-zero ... does not determine` | Newton II admits every positive mass for the exact zero/zero pair. |
| `no exact positive-mass fit` | Failure belongs to the supplied exact premises, not to the object's possession of mass. |
| `empirical ... measurement results` / `keep the two results separate and check their provenance` | The separation of the measurement channels from the joint fit and the evidential-independence test — and, new in d5, the E8/E9 input-independence requirement: a prior reconciliation would make those entries inoperable. |
| `jointly estimate two underlying codirectional vectors and the positive scalar` | Explicit conceptual topology of `JointNewtonIIFit`; neither latent vector is independently selected after imposing Newton II. New in d5: the operation is internal to mass determination, not preprocessing. |
| `Retain the original measurements ...` | Prevents the imposed relation from self-confirming and preserves uncertainty, residual, policy, and provenance. |

Checks:

  - same material-object ownership explicit: yes;
  - positive-scalar commitment explicit: yes;
  - exact branch result-valued rather than total: yes;
  - exact compatibility checked before magnitude quotient: yes;
  - exact zero/zero non-determination explicit: yes;
  - empirical provenance, not displayed alignment, selects the joint branch: yes;
  - measurement results distinguished from latent fitted values: yes;
  - joint result retains original measurements and residual: yes;
  - uncertainty, policy, and provenance retained: yes;
  - circular evidence distinguished from independent determination: yes;
  - no estimator formula silently selected: yes;
  - no upstream reconciliation assumed or permitted: yes;
  - estimation capability sited outside the dictionary, not awaiting a number:
    yes;
  - no mass-address construction, persistence, additivity, gravitational bridge,
    or force-composition provenance imported: yes.

---

## Decisions made in d5

Decisions 1–10 and 12 of d4 stand. Restated and added:

1. **(d4-1, now derived.)** The branch selector is explicitly exact/supplied
   versus empirically measured. Rationale added: this is the *dispatchable* form
   of the distinction. A reader at the node can answer "do I hold supplied values
   or measurement results". "Is this constitutive or procedural" is a level
   distinction the trace cannot branch on, and belongs to Theory.
2. **(d4-11, corrected.)** Estimator ownership is capability-named
   **permanently**, not pending an E12 ratification.
3. **New.** Reconciliation of the two inputs may not be sited upstream of E10.
   Any upstream reconciliation acts on quantities E8 and E9 also consume.
4. **New.** The estimation capability exists but lies outside the scope of the
   VD's authority, on the differentiation precedent. No dictionary entry owns it.
5. **New.** E10 names the joint operation; it does not supply, teach, or certify
   it.
6. **New.** The policy-recording requirement is sourced from the non-uniqueness
   of the external competence, not from the mass corner.
7. **New.** Candidate D is upgraded from deferred to rejected: a "certified pair"
   presupposes the ruled-out upstream predecessor.
8. **New.** The retention requirements are not part of the definitional core.
   They rest on the separate self-confirmation argument.
9. **New.** Object-scoping is not E10's to establish. Warrant belongs to the
   admission machinery; the triplet records content.

---

## Evaluator requirements

```text
input provenance
  -> was either input adjusted against the other through Newton II?
     -> yes: reject the input (upstream reconciliation)
  -> explicitly exact/supplied?
     -> MassExact -> MassRecoveryResult
  -> empirical measurement results?
     -> provenance sufficiently independent?
        -> no: ConsistencyRestatement
        -> unresolved: ProvenanceRequired
        -> yes: joint policy available?
           -> no: EstimationRequired
           -> yes: JointNewtonIIFit -> JointNewtonIIFitResult
```

Minimum exact-result vocabulary:

```text
ExactMass(m)
ZeroZeroUnderdetermined
ZeroNonzeroInconsistency
NoncodirectionalExactInconsistency
```

Minimum empirical boundary result in NML2.1:

```text
EstimationRequired(
  conceptual_route =
    "estimate two underlying codirectional vectors and then recover the
     positive scalar relating them",
  method_status = "outside present scope"
)
```

The evaluator must never silently convert

```text
MeasuredForceResult × MeasuredAccelerationResult
```

into `ExactMass`, even when their displayed vectors align. It must also reject a
joint result that returns only `m` or only the compatible latent values, and it
must not resolve the `joint-mass-estimation` capability name to an entry number.

---

## Acceptance tests

1. **Exact compatible pair**

   ```text
   F = (6, 0) N
   a = (2, 0) m s^-2
   status = exact
   -> ExactMass(3 kg)
   ```

2. **Exact zero/zero**

   ```text
   F = 0
   a = 0
   status = exact
   -> ZeroZeroUnderdetermined
   ```

3. **Exact one-zero**

   ```text
   F = (1, 0) N
   a = 0
   status = exact
   -> ZeroNonzeroInconsistency
   ```

4. **Exact antiparallel or oblique pair**

   ```text
   F = (-6, 0) N, a = (2, 0) m s^-2, status = exact
   -> NoncodirectionalExactInconsistency

   F = (6, 0) N, a = (2, 0.1) m s^-2, status = exact
   -> NoncodirectionalExactInconsistency
   ```

5. **Oblique empirical measurement results, no policy**

   ```text
   measured F = (6, 0) N with uncertainty and provenance
   measured a = (2, 0.1) m s^-2 with uncertainty and provenance
   -> EstimationRequired
   ```

   This must not return exact inconsistency, `no mass`, or an unqualified
   magnitude ratio.

6. **Aligned empirical measurement results, no policy**

   ```text
   measured F = (6, 0) N with uncertainty and provenance
   measured a = (2, 0) m s^-2 with uncertainty and provenance
   -> EstimationRequired
   ```

   Displayed alignment must not silently route to `ExactMass(3 kg)`.

7. **Independent empirical results with a licensed policy**

   ```text
   MeasuredForceResult, MeasuredAccelerationResult, licensed EstimationPolicy
   -> JointNewtonIIFitResult(
        original measurements,
        F*, a*, m,
        uncertainty,
        residual/goodness of fit,
        policy and provenance,
        independent-evidence standing
      )
   ```

8. **Joint fit omits residual**

   ```text
   result = (F*, a*, m) only
   -> reject incomplete fit result
   ```

9. **Circular empirical provenance**

   ```text
   measured a was calculated from measured F and the demanded/supplied m
   -> ConsistencyRestatement, not independent mass determination
   ```

10. **Independent measurements remain distinct from latent outputs**

    ```text
    hold force-side observations and procedure fixed;
    change only trajectory observations
    -> MeasuredForceResult unchanged; jointly fitted F* may change
    ```

11. **Missing epistemic status**

    ```text
    F and a present; exact/measured status absent
    -> halt for classification
    ```

12. **Different owners or incompatible qualifications**

    ```text
    F[A], a[B]
    -> address mismatch halt
    ```

Added in d5:

13. **Upstream reconciliation rejected**

    ```text
    measured a was adjusted to be codirectional with measured F
    before E10 was invoked
    -> reject the input as reconciled upstream
    ```

    Must not proceed to either branch. The adjusted acceleration is no longer
    the quantity E9 consumes.

14. **E8 and E9 remain operable on the same inputs**

    ```text
    take the measured F and measured a handed to E10;
    supply a licensed mass binding
    -> E8 runs on F without needing a
    -> E9 runs on a without needing F
    ```

    If either fails, something upstream has reconciled the pair.

15. **Capability name does not resolve to an entry**

    ```text
    demand the owner of joint-mass-estimation
    -> capability name, outside dictionary authority
    ```

    Must not return E12, a separate measurement entry, or "unassigned".

---

## Settled — do not reopen

Recorded as a class, not only as instances. The generator behind every objection
below is the same: **reading entries as statements to be judged for accuracy and
completeness, rather than as triggers judged by P(correct trace).** An objection
of that shape should be checked against this list before it is written up.

| Objection | Why it fails |
|---|---|
| E10 should be short; define mass exactly and leave measurement to metrology. | Horn one — inert over the whole domain traces run on. |
| Metrology can hand E10 a clean codirectional pair. | Horn two — makes E8 and E9 inoperable. |
| The exact/measured split is mis-typed; these are levels, not branches. | Entries dispatch. A distinction the trace cannot branch on is invisible to it; the level distinction belongs to Theory. |
| Decision 8 states dependence as a binary gate, but dependence is graded. | A gate is binary because a trace proceeds or halts. The gradedness lives in the declared policy — the alpha structure. |
| The operation returns a trial-scoped mass but the headword claims an object property. | Warrant versus content. Admission licenses the object-scoping; a triplet corner does not re-justify its own admission. |
| The fix belongs in the IRIL rather than the entry string. | Raised in the 2026-07-25 pass; superseded — the IRIL cannot carry a distinction the entry never triggers. |

---

## Questions and decisions still open

1. **Final wording.** Candidate A is semantically complete and consistent with
   d5's results, but its rhythm and length still require reader testing before
   promotion. Placeholder by instruction.
2. **Headword suffixes.** Repeating `-material-object` remains expensive.
   Argument added, not closed: the suffix carries the object-binding that the
   admission licenses, so opaque anaphora loses a trace-critical edge and not
   merely a stylistic one.
3. ~~**Estimator ownership.**~~ **Closed in d5** by dissolution — outside the
   dictionary's authority.
4. **Result vocabulary.** Ratify the exact names for underdetermination, exact
   incompatibility, estimation required, provenance required, consistency
   restatement, incomplete fit, and insufficient information.
5. **Finiteness and quantity types.** Confirm whether `positive scalar` is
   already restricted to finite real mass values by general quantity machinery.
6. **Provenance threshold.** Still open, **relocated**: this is a declared-policy
   question in the admission sense, not a defect in decision 8. Specify the
   policy by which the evaluator judges the channels sufficiently independent and
   reports partial dependence.
7. **Joint-result schema.** Ratify the exact representation of corrections,
   residual, goodness of fit, uncertainty, and repeated-trial evidence.
8. **Lesson-plan successor.** NML2.1 lesson d1 remains behind content d2 and this
   packet. A successor should install the exact/empirical split and the joint
   route before E10 is taught from it.
9. **New — E8's latent policy-dependence.** Whether numerical differentiation's
   policy-ladenness gives E8 the same under-specification found here. Flagged for
   the E8 packet; not a claim of this one.
