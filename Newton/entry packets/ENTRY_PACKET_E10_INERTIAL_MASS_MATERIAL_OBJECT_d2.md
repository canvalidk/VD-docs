# Entry Packet: E10 Inertial-Mass-Material-Object — d2

Status: revision of the d1 packet draft. Entry, IRIL, boundary vocabulary and
residual ledger are rewritten; three of d1's open questions are closed and
recorded as decisions. Reasoning is carried in
`E10_ENTRY_WRITING_PASS_2026-07-25.md`, with the E8 and E9 passes for the
conventions shared across the triplet.

Filing note: d1 lives outside this repo, in `07_design_2_1`. If it is catalogued,
record it as `d1` and this file as `d2`; the rename is additive and lossless.

## ENTRY PACKET

Entry id:
  [E10]

Headword:
  inertial-mass-material-object

Status:
  candidate

Role:
  triplet-winter

Law/block:
  Newton II; inertial-mass corner of the addressed triplet

Source status:
  revised from D2[E23], via the d1 packet draft. Governed by the NML2.1 managed-context
  snapshot at VD-docs commit `b23f5a215783aca8811598ceb5e783a7fdfd9726`.

Source hierarchy:
  1. `07_design_2_1/notes/lesson_entry_notes/NML2_ENTRY_RENUMBERING_DECISION_2026-07-23.md`.
  2. `Newton/nml/nml2/nml2.1/NML2_1_CONTENT.md`.
  3. `inbox/VD unsorted important/entry_writing_guide_auditable_compositions.md`.
  4. `Newton/nml/nml2/nml2.1/NML2_1_LESSON_PLAN_d1.md`.
  5. E8 and E9 packets as the other triplet corners; `Core/vd_six_entry_structure.md`.
  6. `07_design_2_1/DESIGN_2_1_ENTRY_STRUCTURE.md`.
  7. D2[E23] and older local NML2 notes, only where consistent.

Old wording lineage:

```text
inertial-mass :=
The positive scalar coefficient m such that net-force = m times
inertial-acceleration for a point-particle.
```

Preserve:
  - inertial mass is a positive scalar;
  - this entry states its inward Newton-II relation only;
  - the value is addressed to the same material object as the other corners;
  - a suitable nonzero trial can determine the value.

Change / reject:
  - Drop `coefficient`. Once the operation sits in a relative clause the noun
    restates it, and `coefficient` carries a faint claim of constancy across
    trials — a forward import of the deferred persistence account.
  - Drop the free-floating symbol `m` and the equation form of the lineage.
  - Replace the generic `point-particle` scope with one addressed material-object,
    bound by the possessive rather than by an address mark.
  - No unrestricted vector division as the defining operation.
  - No `0/0`.
  - No scale, weight, gravitational mass, density mass, or amount of matter.
  - Do not perform the deferred outward wall's target/address construction.

Plain purpose:
  Complete the Newton-II triplet by naming the positive scalar that relates this
  material object's addressed inertial acceleration and net force, without
  supplying the deferred NML2.2 mass-address wall.

Relationship to the packet set:
  - one winter daughter of E8;
  - relates E9's net force to E8's inertial acceleration;
  - carries the positivity that E8 and E9 both rely on and neither states;
  - deliberately does not replace the deferred E12 outward wall;
  - its value may be consumed by E8 and E9 only while licensed.

Routed to E12, the deferred wall:
  the determination procedure, and everything it depends on. The six-entry model
  already allocates this — the triplet corner faces inward to the law relation,
  the wall faces outward to what the quantity is in the broader dictionary and how
  a value is obtained — and NML2.2 is scoped to exactly this material: mass
  determination families, addresses, uncertainty budgets. E12 inherits, at minimum:
  the estimator is a declaration and not a consequence of the law (the
  `(|F|/|a|)·g(cos θ)` result, with `g(1) = 1` the only constraint Newton II
  imposes); errors-in-variables as the general answer; the measurement model as a
  supplied input with its own provenance and expiry; and the multi-trial design
  that makes the isotropy claim testable. A triplet corner that carried any of this
  would be doing the wall's job — the degree-contamination pattern
  `VD_Newton_inertial_acceleration_two_entries.md` warns against.

Trace critical headword mentions:
  - net-force-material-object
  - inertial-acceleration-material-object

Other headword mentions:
  - material-object, as the owner the two daughters must share. Named rather
    than marked, so the ownership constraint is a graph edge instead of a
    residual annotation.

Address binding:
  one material-object address, shared by the headword instance,
  `net-force-material-object`, and `inertial-acceleration-material-object`.
  Declared here as a structural field rather than embedded in the entry string.
  The string carries the same constraint for the reader through the possessive
  `its`, which cannot be parsed without fixing an owner.

Forbidden headword mentions / hidden imports in the eventual entry wording:
  - scale / weight / gravitational mass / amount of matter / density mass.
  - mass additivity — no additivity licence is granted here.
  - target construction / trackability / lumping — NML2.2.
  - interacting-forces-set / attached-force — later force-sum machinery.
  - constancy or persistence of the value across trials — deferred E12.

Question or trace moment this helps with:
  Two, and the second is the common one.
  - Determination: what positive scalar relates this material object's net force
    and inertial acceleration?
  - Consumption: what is the value E8 and E9 demand, and what must any supplied
    value satisfy? In NML2.1 mass is usually supplied, not determined; the
    determination is the hedged minority route.

Witness kind:
  addressed material-object force-accounting commitment; lightweight supplied
  binding only, not the deferred NML2.2 address-construction machinery.

Slots read:
  - material-object identity
  - net-force-material-object
  - inertial-acceleration-material-object
  - common frame and time/interval qualification
  - supplied mass binding, where one exists
  - licence/provenance status

Slots written / exposed:
  - inertial-mass-material-object
  - positive-scalar status
  - supplied or determined provenance
  - existence-failure or uniqueness-failure status

Boundary behavior:
  E10 states no conditions, performs no arithmetic in its string, and therefore
  has **no undefined case**. Every failure is a failure of the definite
  description, and there are exactly two kinds:
  - existence failure — no positive scalar takes the acceleration to the net
    force; the two values do not satisfy Newton II;
  - uniqueness failure — every positive scalar does; the trial is compatible with
    the relation and determines nothing.
  Alongside these, two failures of input rather than of the description:
  - missing input — no supplied binding and no available pair;
  - unlicensed input — the previous binding expired after a reuse trigger.
  And one deferral:
  - origination, address construction and persistence certification route to
    NML2.2/E12.

IRIL - ideal residually imparted logic:

  Allowed:
    - On a demand for `inertial-mass-material-object` for a material-object,
      return the licensed supplied binding when there is one.
    - Otherwise demand `net-force-material-object` and
      `inertial-acceleration-material-object` for that same material-object.
    - **Consistency step.** The two values satisfy Newton II when they point the
      same way to within the declared direction tolerance, or when both fall
      below the declared magnitude floor. This is a test of the law, not a guard
      on arithmetic, and the same test serves every corner. A test with zero
      tolerance is not a test — it fails on every measured trial — so the
      tolerance is what makes this a check rather than a guaranteed halt, and it
      must be declared, not assumed. As elsewhere in the house, the noise level
      bounds the working tolerance from below.
    - **Determination step.** When both values are above the magnitude floor and
      the consistency step has passed, return the magnitude of
      `net-force-material-object` divided by the magnitude of
      `inertial-acceleration-material-object`, and propagate the inputs'
      uncertainty.
      **This is a declared choice of estimator, not a consequence of the law.**
      Any single-trial estimator built from the two vectors, invariant under
      rotation of the axes, and carrying the dimensions of mass has the form
      `(|F|/|a|) · g(cos θ)`, and Newton II fixes only `g(1) = 1`. The magnitude
      quotient takes `g = 1`; least squares with all error on the force takes
      `g = cos θ`; all error on the acceleration takes `g = 1/cos θ`. These are
      different questions, not different notations, and the law does not choose
      between them. The choice is licensed here only because the consistency step
      has already bounded the angle: at `0.1°` the three differ by `3 × 10⁻⁶`, at
      `1°` by `3 × 10⁻⁴`, at `20°` by `12%`. Beyond a declared measurement model,
      `g = 1` is a claim that direction has been excluded from the measurand —
      which is not what the rest of this packet says. Where the inputs are
      measured rather than supplied, the estimator must come from the measurement
      model, not from this clause. See
      `vector_division_inertial_mass_measurement_vscode.md`.
    - When both values fall below the magnitude floor, return indeterminate: the
      relation is satisfied by every positive scalar and identifies none. The
      exact zero/zero case is the limit of this region, not a separate case —
      the trial degrades continuously as both values shrink, since a ratio of two
      small noisy numbers is unstable well before either reaches zero.
    - When both values are zero and a licensed binding is supplied, retain that
      binding and mark the trial consistent, without claiming the trial
      established the value.
    - When a licensed binding is supplied and both other values are present, run
      the consistency step as a check. Do not silently replace the binding.
    - Preserve the common material-object, inertial-frame and time/interval
      qualifications.
    - Record whether the returned value was supplied or determined, and record
      which route produced the acceleration the determination consumed.

  Blocked:
    - Dividing one vector by another. The determination divides magnitudes,
      after the consistency step, never vectors.
    - Running the determination without the consistency step. Magnitudes divide
      cleanly for antiparallel and for non-parallel values and would return a
      number that is not an inertial mass.
    - Returning a value from the zero/zero trial.
    - Combining values belonging to different material objects.
    - Treating a scale reading, weight, gravitational mass, density mass or
      amount of matter as this value without a separately licensed bridge.
    - Inferring mass additivity, target construction, persistence, or constancy
      across trials from the inward triplet relation.
    - Reusing a supplied binding after its licence has expired.
    - Generating a value when either other corner is merely named and has no
      bound value.

  Trace consequence:
    - nonzero, parallel, same way: return `|net-force-material-object| /
      |inertial-acceleration-material-object|`, marked determined.
    - both zero, no supplied binding: return indeterminate — compatible,
      non-identifying.
    - both zero, licensed supplied binding: retain the binding; mark the trial
      consistent, not confirming.
    - misalignment within the declared direction tolerance: admissible. Proceed
      to the determination step; no failure has occurred.
    - misalignment beyond the declared tolerance, one value below the floor while
      the other is not, or values that are antiparallel: **existence failure**.
      Positivity is what excludes the antiparallel case.
      The output is not "the law is false" and never "this material-object has no
      inertial mass". It is: *these two values cannot both belong to this
      material-object under Newton II.* Route to the model and the inputs, in
      this order — an unaccounted force contribution, the wrong target address, a
      non-inertial frame, an understated uncertainty budget, and only last a
      genuine anisotropy of inertial response. The conclusion licensed is the
      same shape the content spec licenses at a mass-reuse trigger: something has
      stopped being licensed, and nothing further follows about the value.
    - a corner absent: demand E9, or E8/E7, as appropriate; a cycle with no
      second independent value terminates as insufficient information.
    - owner, frame or time qualifications in conflict: mismatched-address or
      qualification halt.
    - expired mass-reuse licence: unlicensed-input halt.
    - full origin, address or persistence account demanded: halt at deferred
      E12/NML2.2.

IRIEs - ideal residually imparted effects:

  Reader/modeler behaviour to install:
    - Look for one positive scalar linking the two vectors. Do not attempt to
      divide vectors.
    - Test the law before taking a value: agreement of direction *is* Newton II
      holding for these two values, not a precondition for arithmetic.
    - Once that test passes, take the ratio of magnitudes without further
      conditions.
    - Verify that net force and acceleration belong to the same material object
      and share frame and time/interval qualifications.
    - Distinguish a supplied binding from a determined value, and keep the
      determination's own inputs in view.
    - Read a zero/zero trial as compatible with a positive mass and insufficient
      to identify one.
    - Treat incompatibility as evidence of a bad address, qualification, input or
      model, never as licence to take the magnitude ratio anyway.
    - Expect Newton II to produce no direction anywhere. Every direction in the
      triplet is inherited from an input or absent; direction is carried, never
      computed.

  Anti-habit / anti-misread:
    - Do not write or calculate unrestricted `force / acceleration` for vectors.
    - Do not let `0/0` choose a mass.
    - Do not take a magnitude ratio without the consistency step. The numbers
      divide even where the law fails, and that is the trap.
    - Do not substitute weight, a scale reading, gravitational mass or an
      amount-of-matter idea for inertial mass.
    - Do not assume masses add merely because they are positive scalars.
    - Do not reuse an old value across a material change without a current
      licence.
    - Do not read `positive scalar` as a formatting detail. It is the claim that
      inertial response is isotropic, and it is the only place in the triplet
      where that is said. Being a claim, it is testable — but **not by one
      misaligned pair**, which cannot separate anisotropy from noise. It is
      tested by fitting one scalar across several trials at different directions
      and inspecting the residuals. A single trial's misalignment is a
      diagnostic; the spread across directions is the test.
    - **Do not conclude from an existence failure that the material-object has no
      inertial mass.** Nothing licenses that. The failure says the two supplied
      values are not jointly admissible; the object's mass is untouched by our
      inability to determine it from this pair.
    - Do not run the consistency step without a declared tolerance. At zero
      tolerance every measured trial fails, which is not rigour — it is a broken
      test that would halt every experiment ever performed.
    - Do not treat the zero/zero indeterminacy as a knife-edge that only fires at
      exact zero. It is a region, and where its edge lies is a question for the
      declared measurement model, not a constant.

Glosses (field added to the template; the corpus already uses glosses as
first-class material — see `NM_L1_E7_E8_decision_note.md`):

  What the reader must not conclude:
    that the definition is vague. It is exact. What is underdetermined is the
    *estimate from imperfect measurements*, and only until a measurement model is
    supplied. Collapsing those two is the misread this gloss exists to prevent.

  Student-facing, younger:

  ```text
  This tells you which number the mass is. It does not tell you how to find it.
  If someone hands you exact values, those are the same thing. If you measure
  them yourself, they are not.
  ```

  Student-facing, older:

  ```text
  The definition is exact, and the way to get a value out of real measurements is
  a separate problem. That problem does not have one right answer until you say
  how good your measurements are.
  ```

  Teacher gloss:

  ```text
  E10 withholds the procedure deliberately. Newton II fixes the estimator only
  where net force and inertial acceleration are exactly aligned; away from that
  it fixes nothing, and the choice belongs to the measurement model. Do not
  repair the apparent gap by teaching m = |F|/|a| as the definition. That
  installs one estimator as the meaning of the word, and deletes the positive-
  scalar isotropy claim, which lives nowhere else in the dictionary. Name the
  gap and route it to E12.
  ```

Proposed burn activity (lesson-design decision, not settled here):

  On the model of NML2.1's mass-reuse burn. Supply a measured trial in which net
  force and inertial acceleration are a few degrees apart. The worksheet invites a
  mass calculation, and the magnitudes divide cleanly — that is the trap. The
  intended success is refusal: these two values are not jointly admissible under
  Newton II, and the missing item is not another number but a statement of how
  good the measurements are. Award full credit for the refusal and for naming what
  is missing. Do not resolve it in NML2.1.

  Two guardrails from the house's own practice. NML2.1 currently carries one burn;
  a second is the lesson owner's call, not this packet's. And the
  `E7_INERTIAL_ACCELERATION_PLACEMENT_NOTE` test applies — can the 40-minute
  version still run? If not, this is an 80-minute or advanced-track item, and the
  glosses above carry the hint alone.

Suggested wording:

  A, chosen:

  ```text
  inertial-mass-material-object :=

  For one material-object, the positive scalar that multiplies its
  inertial-acceleration-material-object to give its net-force-material-object.
  Therefore the two point the same way, and the scalar is the net-force
  magnitude divided by the inertial-acceleration magnitude.
  ```

  B, relational, without the operation:

  ```text
  inertial-mass-material-object :=

  For one material-object, the positive scalar relating its
  inertial-acceleration-material-object to its net-force-material-object.
  ```

  C, magnitude determination:

  ```text
  inertial-mass-material-object :=

  For one material-object, the magnitude of its net-force-material-object divided
  by the magnitude of its inertial-acceleration-material-object, when both are
  nonzero and point the same way.
  ```

Draft entry:

```text
inertial-mass-material-object :=

For one material-object, the positive scalar that multiplies its
inertial-acceleration-material-object to give its net-force-material-object.
Therefore the two point the same way, and the scalar is the net-force
magnitude divided by the inertial-acceleration magnitude.
```

Two sentences, on the E4 precedent, where the second sentence's job is to block a
misread the first leaves open. Sentence one states the law relation and carries
positivity. Sentence two imparts the procedure. `Therefore` is the hinge: it marks
the direction agreement and the magnitude quotient as **consequences of sentence
one**, not as extra conditions bolted on — so the reader is not left thinking
alignment is a separate assumption, and the two sentences cannot drift apart.

Why the procedure moved into the string, having been in the IRIL:

  The IRIL records what the residual *imparts*. A determination step the string
  does not trigger is not imparted logic; it is machinery living where no audit
  reaches — the defect the entry-writing guide names in as many words. The prior
  draft failed on its own terms.

  It also repairs a weak trigger. The prior entry routed every boundary case
  through the failure of a definite description, and presupposition failure is a
  poor behavioural trigger: readers accommodate rather than halt. The two-sentence
  form replaces it with stronger stimuli. Misalignment now contradicts an
  **asserted** fact instead of quietly failing a presupposition. The zero/zero
  trial now runs into `0/0`, a reaction installed in primary school, rather than
  into a uniqueness failure a reader must notice unaided. Elegance had been bought
  at the cost of reliability, which is the wrong trade for an entry whose success
  criterion is the probability of a correct trace.

  What sentence two costs: 33 words against 14, and 269 characters against 141.
  Under short headwords the same 33 words run to 237. Sentence two is where the
  suffix tax compounds, since the quotient must name both quantities a second
  time.

## DEEP AUDIT ADD-ON

Role test:
  E10 is inward-facing. Its definiens exposes only the two other Newton-II
  triplet headwords, plus `material-object` as the owner they must share. It
  states the positive-scalar relation without importing the deferred E12
  mass-address wall, a measurement procedure, or any outward sense of mass.

Necessary/sufficient/asymmetric relations:
  - A nonzero `inertial-acceleration-material-object` and a parallel, same-way
    `net-force-material-object`, under compatible qualifications, are jointly
    sufficient to determine the value.
  - Either alone is insufficient.
  - Matching the material-object address is necessary; matching units or numbers
    without matching the owner is insufficient.
  - Parallelism and same direction are **not additional conditions**. For vectors
    `F` and `a`, the existence of a positive scalar taking `a` to `F` and the
    agreement of their directions are the same statement. The direction claim of
    Newton II is carried entirely by the existence of this entry's referent.
  - Magnitude agreement alone is insufficient, and is the live trap: magnitudes
    divide cleanly in exactly the cases where the law fails.
  - Zero acceleration with zero net force is compatible with any licensed positive
    value and sufficient to determine none.
  - Exactly one zero vector is sufficient for existence failure.
  - Positivity is not derivable from the other two corners. The algebra of the
    triplet is equally satisfied by a negative scalar, which would license
    antiparallel force and acceleration. Positivity is Newton II's own
    commitment, and with `scalar` it is what makes the relation
    direction-preserving — that is, what makes inertial response isotropic. A
    tensor-valued mass would break parallelism, make direction computed rather
    than inherited, and falsify the magnitude determination.
  - E10 identifies the scalar's role. It does not establish a measurement
    procedure, mass additivity, gravitational equivalence, constancy across
    trials, or the validity and persistence of the material-object address.

Quantifier or modality:
  `the` asserts existence and uniqueness by presupposition; its two failure modes
  are the entry's two boundary behaviours. `positive` fixes the sign and, with
  `scalar`, the isotropy. No verbal modal is required.

Suspends for human/model input?
  yes; when no licensed binding and no usable pair is available, or when
  ownership, qualification or provenance is missing.

Boundary trigger:
  - absent binding together with an absent or zero/zero pair;
  - exactly one zero vector;
  - nonzero vectors that are antiparallel or not parallel;
  - different material-object addresses;
  - incompatible frame or time/interval qualifications;
  - expired mass-reuse licence;
  - scalar/vector type or dimensional mismatch;
  - disagreement between a supplied value and the other two corners.

Boundary output:
  - demand E9 and E8/E7 for a usable pair;
  - return indeterminate for a zero/zero trial without a supplied binding;
  - preserve a licensed binding through a consistent zero/zero trial;
  - return a contradiction for existence failure, address, qualification, type or
    dimensional failure;
  - return an unlicensed-input halt after binding expiry;
  - route origination, address construction and persistence to deferred
    E12/NML2.2.

Residual provenance ledger:

| Phrase | Backing |
|---|---|
| `For one …` | Grammar-level scope idiom; house style across K3, K9–K15 and D2[E23]. `one` triggers singularity, which is what cross-target borrowing violates. |
| `the` | Grammar-level definite description — the entry-writing guide's first and strongest category ("a definite description forces referent-finding"). Presupposes existence and uniqueness; both failures are the entry's boundary behaviour, so no condition needs writing. |
| `positive` | Newton II's own commitment, derivable from nothing else in the triplet. Excludes the antiparallel and one-zero trials without naming them. |
| `scalar` | Stock quantity-type vocabulary. Blocks the vector-division misread in one word rather than by prohibition, and with `positive` carries the isotropy of inertial response. |
| `its` (×2) | Grammar-level possessive anaphora. Unparseable without a referent; cannot bind two referents in a coordinate structure. Weaker here than at E8 and E9 — see the note below. |
| `multiplies … to give` | Primary-school arithmetic. States the scalar–vector relation without naming division, magnitudes, or a procedure. `give` is the arithmetic idiom ("2 multiplied by 3 gives 6"), not a production claim; `produce` is avoided as a causal overclaim. |
| the implicit shape | Stock across physics for a constant of proportionality (the `k` in `F = -kx`), and house practice in `hookean_response_type_chain_d1.md`, whose constants are defined relationally and never as quotients. |

No row is backed by the writer's invention.

Possessive-binding note: at E8 and E9 the possessive is closed by grammar alone,
since `For one material-object, its …` offers exactly one antecedent. E10
interposes `the positive scalar`, which is grammatically available, so the binding
is closed by semantics — a scalar has no inertial-acceleration — assisted by the
possessum's own morphology, since `-material-object` names the type its owner must
be. Closed, but by a weaker mechanism than the sibling corners use. Recorded rather
than repaired: the alternatives that restore grammatical closure are all passive or
longer.

Alternative wording assessment:
  - **A** states the relation and lets `the` and `positive` produce every boundary
    behaviour without writing a single condition. Parallelism is never mentioned
    because a positive scalar cannot turn a vector; `0/0` never arises because no
    division is named; the magnitude trap never opens because no magnitudes are
    named. Its cost is that a determination requires solving — see decision 7.
  - **B** is shorter but drops the operation, and with it the definite
    description's grip. `the` bites only as hard as the relation is precise: it
    presupposes a unique referent, and whether a referent exists depends entirely
    on what relation must hold. Worked case — supplied values with `F = -3a`, a
    law violation and a catalogued trap. Under A, no *positive* scalar multiplies
    `a` to give `-3a`, the description fails to denote, contradiction. Under B, a
    positive scalar certainly *relates* them: `3` relates their magnitudes. The
    description denotes, E10 returns `3`, and the violation is reported as a mass
    — the anti-misread *"do not ignore vector direction when magnitudes happen to
    divide cleanly"* turned from impossible into the default reading. `relating`
    also fails to say which value is dividend, leaving B ambiguous between the
    mass and its reciprocal, so all six rows of the boundary table degrade,
    including the determined one. B does not save a computation; it declines to
    say which computation, and a definition that will not say which cannot detect
    a wrong one.
  - **C** answers the solving cost directly and is the honest explicit form, but it
    is a determination procedure rather than a definition, and it cannot be the
    entry. A cart at rest under zero net force has an inertial mass and no such
    ratio. Any two non-parallel vectors divide cleanly, so a ratio-definition
    assigns an inertial mass to values that violate the law — precisely the
    catalogued error. C presupposes the law and therefore cannot detect its
    violation; A presupposes it by presupposition, which is detectable. C's
    computation is adopted, in the IRIL determination step.
  - Rejected in drafting: `the positive scalar **coefficient** that …` (the noun
    restates the relative clause and leaks constancy); `… that **scales** its
    acceleration to its net force` (names a reaction `multiplies` already
    produces, in later-installed vocabulary); `the **number of times** its
    acceleration **fits into** its net force` (reads forward rather than backward
    and would have answered the solving cost, but quotition division compares like
    with like, and newtons against `m s⁻²` are not like — the failure is
    dimensional, not stylistic); `its net-force divided by its
    inertial-acceleration` (the shape E8 and E9 predict; vector-by-vector division
    is not an operation, which is what makes this corner the exception).

Chosen wording:
  Candidate A.

Why chosen:
  It states the corner's relation and nothing else. Positivity, which no other
  entry can carry, is explicit; the vector type, which the daughters already
  carry, is not. Every blocked case and every boundary status follows from the
  definite description and the word `positive`, so the entry needs no conditions,
  no prohibitions and no procedure. The determination the entry does not perform
  is performed in the IRIL, where its direction test can be enforced as a step
  rather than skimmed as a subordinate clause.

Checks:
  - exactly two daughter headwords exposed: yes;
  - owner named rather than marked, so ownership is a graph edge: yes;
  - same-owner constraint enforced by the possessive, not described: yes, by a
    weaker mechanism than E8/E9 — recorded above;
  - positivity explicit because it is a commitment, not a consequence: yes;
  - vector type omitted because it is a consequence, not a commitment: yes;
  - no vector division, no magnitudes, no `0/0`, no procedure in the string: yes,
    and none needed forbidding;
  - direction condition entailed by the operation rather than fenced: yes;
  - no scale, weight, gravitational mass, density mass or amount of matter: yes;
  - no additivity, target construction, persistence or constancy: yes;
  - no causal claim: yes;
  - use-time solving discharged in the IRIL rather than left to the reader: yes;
  - structurally continuous with E8 and E9: the frame `For one material-object,
    its … its …` holds; the definiens is a characterisation where theirs are
    expressions, and that difference is forced by the mathematics.

## Decisions made in this pass

1. No `[A]` in the entry string. The address mark is skimmable — a reader can run
   the relation without consulting it — where the possessive `its` cannot be
   parsed until an owner is found. Address binding is declared as a structural
   field instead, so the graph gets a checkable variable and the reader gets
   English.
2. `material-object` is named in the definiens. This converts the ownership
   constraint from a residual mark into a graph edge, which is the direction the
   entry-writing guide asks entries to move in.
3. `coefficient` is cut. The relative clause states the operation the noun would
   restate, and `coefficient` leaks a claim of constancy that belongs to deferred
   E12.
4. Positivity is explicit here, and only here. It is not derivable from the other
   two corners, and it is what makes Newton II direction-preserving.
5. The vector type is *not* stated, on the same rule that requires positivity to
   be: state a type when it is a commitment, omit it when it is a consequence.
   Scalar × vector = vector is derivable across graph edges the reader already
   has. (E9's `the vector` was dropped for the same reason.)
6. Frame, time, provenance and licence remain trace qualifications. Owner is the
   only co-qualification no daughter entry can state; frame and time propagate
   down from the headword and the daughters.
7. **The determination is stated in the entry, in a second sentence.** This
   reverses an earlier decision in this pass, which had left the entry implicit
   and stashed the determination in the IRIL. That was a guide violation: the IRIL
   records what the residual imparts, so a step the string does not trigger is
   undeclared machinery by definition. The reversal also trades an elegant weak
   trigger (presupposition failure) for reliable strong ones (a contradicted
   assertion, and `0/0`). The entry's success criterion is the probability that a
   stimulated reader performs the correct procedure, not the exactness of a
   statement about what mass is — and the earlier draft was optimising the second.
   Constants of proportionality are conventionally defined implicitly, which is
   why the implicit form looked right; convention is not the criterion here.
8. The direction test is reclassified. It is not a guard on the division but the
   Newton-II claim itself; the determination that follows it is unconditional.
9. Boundary vocabulary is rebuilt on existence failure versus uniqueness failure.
   E10 has no undefined case: it states no conditions and performs no arithmetic,
   so every failure is a failure of the definite description. (Closes d1 Q3.)
10. Directional and one-zero failures are not classified by E10. It has nothing to
    classify with, and they are not mass questions — they are the law being
    tested, and the same test serves every corner. (Closes d1 Q4.)
11. An expired reuse licence does not block a fresh determination. It kills a
    *binding*, not the entry. What a trigger destroys is confidence that the later
    target is the same target — an address question, deferred to E12/NML2.2.
    (Closes d1 Q5.)
12. E10 supplies no measurement procedure, additivity, gravitational bridge,
    constancy, or address origination.

## Requirement this packet places on the evaluator

The entry is implicit, so a consumer reading only the string must solve for the
value. The IRIL's determination step is what prevents that, and it must be
implemented rather than derived: the evaluator runs the consistency step and then
the magnitude quotient. This is not an assumption to leave in the air.

It also reframes the sibling corners. E8 and E9 are not computation rules that
happen to be handy; they are relations that happen to be directly readable. All
three corners state relations and the evaluator solves — which is what "Newton II
is a constraint, not an information generator" means operationally. The asymmetry
across the triplet is a fact about which relations invert in closed form, not a
difference in what the entries do.

## Questions and decisions still open

1. **Headword suffixes.** `VD_Newton_inertial_acceleration_two_entries.md`
   retracted domain-encoding in headword strings; `-material-object` is
   domain-encoding in headword strings. For `inertial-acceleration` the suffix
   marks a real definitional-role cut. For `net-force` and `inertial-mass` there
   is no competing entry and no cut. This entry runs 141 characters against 109
   for the same fourteen words under short headwords, and the same tax lands on
   E11, E12 and every later entry mentioning force or mass. Against that, the
   possessive-binding note above is the first real argument *for* the suffix: the
   possessum's morphology names the type its owner must be. The trade now has a
   cost on both sides. This still outranks everything below.
2. **Finiteness.** The d1 audit twice says "positive finite-mass commitment" while
   the entry says only `positive`. The gap closes only if `scalar` is defined over
   the reals. General quantity-type machinery, not this string.
3. **Dimensional checking** (`N / m s⁻² -> kg`): E10 residual effect, general
   quantity-type operation, or both?
4. **Provenance depth.** Whether `determined` needs to record not just that the
   value was inferred but *which route produced the acceleration it consumed*. A
   value determined from a trajectory-read E7 acceleration is an empirical result;
   one determined from an acceleration that was itself computed from a net force
   is a tautology. Same value, different standing. Shared with E9's packet.
5. **Zero/zero status name.** `indeterminate` is used above for the uniqueness
   failure. Confirm it against the evaluator's vocabulary, and that it is
   distinguishable from `insufficient information`, which is what an absent corner
   returns.
6. **The two budgets are one object, and it is a measurement model.** An earlier
   draft of this packet asked for a declared direction tolerance and a declared
   magnitude floor, on the pattern of `eps_shape` / `eps_trans` / the demanded
   `eps_m`. That was two scalars reconstructing, badly, what a covariance already
   does properly: a misalignment's significance depends on how precisely each
   direction is known, so a single angular number is itself a hidden isotropy
   assumption — about the *errors* this time, not the response. And a magnitude
   floor is not a threshold either; it is where the estimate becomes broad rather
   than where it becomes invalid. Both collapse into `Σ_F` and `Σ_a`. What E10
   needs declared is therefore one thing, not two: **a measurement model for the
   two inputs**, and it should go through the ratification route.
   Two consequences. First, that model is itself a supplied, licensed input with
   its own provenance — structurally the same as the mass binding, and it inherits
   the same failure mode, since an estimator built on guessed covariances inherits
   the guess. Errors-in-variables is not identifiable without independently
   established error behaviour or replicates. Second, NML2.1 does not need any of
   this: its inputs are supplied exact, every estimator agrees there, and the
   licensed simple case should be named as such rather than allowed to pass for
   the general one.
7. **Does the tolerance belong to the trial or to the material-object?** A
   declared tolerance is a property of the determination, and different trials on
   the same object may reasonably use different ones. Whether a value determined
   under a loose tolerance may later be consumed by E8 or E9 in a context
   demanding a tighter one is a provenance question this packet does not settle —
   related to open question 4.
