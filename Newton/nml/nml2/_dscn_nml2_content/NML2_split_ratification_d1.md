# NML2 Split Ratification: NML2.1 and NML2.2

**Status:** decision record, d1
**Project:** VD Newton / VD Pedagogy
**Date:** 2026-07-11
**Role:** ratifies the division of NML2 into two lessons; compiles the content,
scope, constraints, and rationale established in the design discussion of
2026-07-11. Supersedes the outstanding audience-decision item in
`NML2_FINAL_DRAFT_v1.md` and the provisional NML2A/NML2B labels in the
question-exercise-demonstration bank.

---

## 0. The decision

NML2 is two lessons.

```text
NML2.1 — THE NEWTON-II LESSON
  Understanding F = ma as an addressed triplet; inertial mass vs
  gravitational mass vs density (stuff) mass; mass additivity as an
  underexplored assumption with three distinct grades; the lesson is
  BOUNDED at the point where the mass licence changes.

NML2.2 — THE TARGET-CONSTRUCTION LESSON
  Trackability, redundancy, lumping, tolerance; how a scene earns a
  continuing massive target; worked defeat cases — fluids (tap),
  stretchy materials (bouncy ball), convoy, wheel, splatter.
```

Label migration, canonical from this document forward:

```text
bank "NML2B" (accessible supplied-target lesson)   -> NML2.1
bank "NML2A" (university target construction)      -> NML2.2
```

The numeric labels replace the letter labels entirely; the letter labels had
already suffered one usage collision and the numbers additionally encode the
teaching order. Bank operation codes (O1–O50), critical questions (CQ0–CQ18),
exercises, and demonstrations remain valid and are assigned to lessons in
sections 2.7 and 3.5.

---

## 1. Rationale, compiled

Four findings from the design discussion jointly force this shape.

**1. The band invariant survives the split.** The bank's rule — moving an
exercise between bands changes its representation, not its underlying trace —
now operates *within* NML2.1 (Band I circle-and-match through Band III
calculus) rather than across two incompatible audiences of one lesson. The
v1 draft's "adaptable from young learners to undergraduates" claim is
dissolved, not stretched.

**2. Trace order is not teaching order.** Lumping is architecturally prior to
Newton-II use (the address must exist before the value binds) but
pedagogically posterior: the lumping question is only *felt* by a student who
already uses mass values and has watched blind reuse fail. Teaching the
licence before the licensed activity produces legalism without stakes. The
curriculum therefore runs demand-driven, like the evaluator itself: NML2.1
manufactures the demand; NML2.2 supplies the machinery.

**3. NML2.1's exit boundary is a theorem, not a syllabus choice.** The lesson
ends exactly where address-carrying fails — splits, continuous material loss,
ambiguous substitution — because continuous m(t) for one target is illegal at
this level (continuous certificate expiry; the rocket/leaking-cart case).
That failure point is precisely the demand NML2.2 answers. Teaching the two
together would deliver lumping before any student had watched a mass address
die.

**4. Refusal behaviour is placed by assessment regime, not only by cognitive
load.** UK exam mark schemes reward the fast unlicensed substitution that
halt discipline penalises. NML2.1's young bands therefore install the habit
as *ownership auditing* ("which object owns this number?" — costs nothing on
any exam) and carry only the seed of halting (E6). Full halt discipline and
the refusal-as-correct-answer convention live in NML2.2 and NML2.1's Band III,
where assessment can honour them.

---

## 2. NML2.1 — The Newton-II Lesson

### 2.1 Thesis

> Newton II locks three quantities owned by one target. The mass slot in that
> relation is one of at least three things "mass" can mean, and the everyday
> certainty that masses add is not one claim but three claims with three
> different bills. This lesson runs F = ma correctly, decorrelates inertia
> from gravity, and ends at the exact point where reusing a mass value
> requires a licence the lesson has not granted.

### 2.2 Content

**(a) The addressed triplet.** `m[A]`, `a[A]`, `F_net[A]` locked by Newton II;
same target, same interval, frame-qualified. Three algebraic forms; the
triplet as constraint, not generator (CQ18 / B2.6A: no supplied values, no
output). Units, vector discipline, the zero case, the thin net-force wall
(supplied or Newton-II-inferred; a meter reads one transmitted contribution).

**(b) The three masses.** The load-bearing lecture segment, university-facing,
compressible for lower bands:

```text
DENSITY (STUFF) MASS   m = rho V; amount of matter; Newton's own definition
                       (quantity of matter = density x bulk), Mach's circle.
                       Additive BY CONSTRUCTION — two buckets of sand. This
                       is where the "obviously additive" intuition lives.

GRAVITATIONAL MASS     the coupling a scale actually reads. Its
                       identification with inertial mass is the ungranted
                       equivalence edge — a physical postulate, not a
                       convenience.

INERTIAL MASS          the m in F = ma. Legal origination at this level:
                       same-pull-same-time delta-v comparison against a
                       standard. Never a scale.
```

The textbook smuggle is the silent identification of stuff-mass with the m in
F = ma. Surfacing it is the lesson's conceptual payload.

**(c) Additivity as three claims, three grades.**

```text
stuff-mass additivity      analytic by construction        (free)
measured-mass additivity   empirical, tolerance-true only  (deuteron ~0.1%)
ledger-mass additivity     derived under adequacy (B)      (later machinery)
```

Presented as an *underexplored assumption*: the class states where each grade
will be paid, and none is paid here. This is Stage 5 of the mass pipeline
delivered as a lecture without the pipeline vocabulary.

**(d) Inertia distinct from gravity — the decorrelation goal.** On Earth,
hard-to-lift and hard-to-shove never come apart in a student's experience;
the lesson forces them apart. Sideways pushes on supported objects (gravity
orthogonal, visibly irrelevant); the Earth/Moon probe as the signature
critical question:

> The same sideways push on the same cart, on Earth and on the Moon.
> Compare the motion-changes.
> Expected: identical. Lifting got easier; shoving did not. Two different
> questions that Earth happens to fuse.

**(e) The extreme-mass horizon (kept, trimmed).** Earth as extremely massive
participant, D4 form only: the equal-scale action is *supplied* ("if a push
of this size landed on the Earth…"), mass-side reasoning only. The Sun–planet
centrality claim is **dropped as a learning goal**: "the Sun barely moves
because it is heavy" requires knowing the force on the Sun is comparable to
the force on the planet, which is Newton III — interaction-pair smuggling in
a gravitational scenario, doubly off-licence here. It may survive as a
one-line horizon gesture with its bill named.

### 2.3 Stratification

```text
BAND I–II CORE
  ownership drills, addressed triplet, three algebraic forms, units,
  vectors, zero case, qualitative inertial-mass comparisons, force-to-path
  stepping with supplied F_net, the halt SEED (E6) only.

BAND III EXTENSION (calculus)
  the same trace at continuum representation:
    - continuous supplied F_net(t) and F(r): genuine ODE problems
      (constant mass throughout)
    - the discrete stepper's continuum limit
    - planet activity as differentiate-twice-and-infer, labelled as
      Newton-II inference with a supplied frame certificate
    - piecewise-constant mass with EXPLICIT re-licensing events between
      phases (chip flies off; new value supplied; calculation resumes)
    - parameterised families of fixed-mass targets where each carries a
      supplied binding (previews the A_tau construction without teaching
      lumping)
  the three-masses lecture and the additivity grade table at full depth.
```

Calculus is legal because it changes representation, not licences. The
policing rule: every supplied F_net remains ONE opaque vector. Calculus
problems habitually arrive as multi-force setups (drag + gravity, spring +
friction); any such setup breaches the force-sum wall and is out.

### 2.4 Legality constraints (licence table)

```text
GRANTED
  Newton-II triplet with supplied/inferred F_net
  supplied mass bindings with owner and marked provenance
  same-pull-same-time comparison as the only inertial-mass origination
  piecewise mass with explicit re-licensing events
  stuff-mass additivity, flagged as construction-level

WITHHELD (marked debts — stated to exist, not paid)
  measured- and ledger-additivity justification        -> later
  target/address construction                          -> NML2.2
  gravitational–inertial equivalence                   -> later
  force-sum, NIII, interaction pairs                   -> NML3+
  continuous m(t) machinery (open systems)             -> momentum lessons

FORBIDDEN (revocable smuggles — never uttered as fact)
  "the scale reads inertial mass"
  "force causes motion"
  "the Sun stays put because it is heavy" (as a derived claim)
  any decomposition of a supplied F_net into contributions
```

### 2.5 Exit boundary — the burn

The lesson's climax is a designed failure, not a summary. The final Band III
problem invites blind F = m(t)a substitution on a continuously mass-losing
target; the result is demonstrably ambiguous (the leaking-cart form: the
answer depends on momentum carried by departing material, so the naive
substitution is not even well-defined). The resolution is **not given**. The
exit statement:

> Mass reuse is licensed separately from the equation that consumes it. The
> licence just expired continuously, and you do not yet own the machinery
> that handles that. Two lessons answer this: one about how targets and
> their mass addresses are built and audited (NML2.2), one about momentum
> (later).

The rocket appears only as this boundary probe — never as a solved problem.

Lower bands receive the same burn at their representation: the mandatory E6
halt-seed row, and one two-scene problem where blind reuse of m gives a wrong
prediction because the object visibly lost a piece between scenes.

### 2.6 Sequencing requirement (carried from the bank review)

Burn before machinery, inside the lesson as well as across the pair: the
cross-target trap (CQ1) or a wrong-prediction scene opens the lesson; the
addressed-triplet notation arrives as the *repair*, not as an announced
convention. This requirement is recorded here because a bank cannot hold
sequencing properties.

### 2.7 Bank assignments — NML2.1

```text
Operations       O1–O23, O34 (address/value separation at supplied level),
                 O40 seed form, O41–O42, O50
Critical Qs      CQ1, CQ2, CQ3, CQ4, CQ5, CQ6, CQ17, CQ18
                 + NEW: Earth/Moon decorrelation probe (needs a CQ number)
Exercises        B1.1–B1.22, E1–E6; B2.1–B2.20, E7–E10
                 (B1.9 bracket notation moves to Band II; owner-lines and
                  coloured rows do its Band-I work)
                 (B2.12 fenced to Band II explicitly — impulse in a wig)
Demonstrations   D1, D2, D3 (as redundancy SEED only), D4 (supplied-scale
                 form), D5, D7 (qualitative), D8, supplied-force simulation
Rubrics          10.1, 10.2, 10.3
Boundary probes  B2.14 rows, photon question in normalised form (CQ15 at
                 Band III), rocket/leaking-cart burn (needs a number)
New lecture      three-masses segment; additivity grade table
                 (not in the bank; source: pipeline Stage 5 + spine Wall 2
                  + this discussion)
```

---

## 3. NML2.2 — The Target-Construction Lesson

### 3.1 Thesis

> Real scenes do not arrive labelled. This lesson builds the thing NML2.1
> consumed: the continuing massive target. Tracks, redundancy under a
> declared tolerance, lumping, the mass address and its validity history —
> and the defeat cases that show the construction is doing live work.

### 3.2 Content

**(a) Trackability as ground.** Tracks from seeded scenes (B3.2); path vs
track; tolerance bounded from below by tracker resolution and from above by
the question's budget (B3.4).

**(b) Redundancy and lumping.** The formal two-track test (B3.5); all-pairs
bundle audits, cliques, non-transitivity, the human clique-pick (B3.6);
count-stability under densification (B3.7); representative-track licence and
what it omits (B3.8); Galilean invariance of the redundancy judgment (B3.8A).

**(c) The full persistence certificate — both halves.** The computable
redundancy audit AND the coverage probably-no, taught explicitly:
densification audits (B3.3), sub-resolution drain (B3.25), the
no-offshoot / reconstruction / expiry taxonomy (B3.18). The lesson does not
repeat the v1 draft's error of presenting the audit as the whole licence.

**(d) The worked defeat spectrum.**

```text
bouncy ball    strict/loose double ledger; fine–coarse–fine bridge;
               "return of redundancy is not return of address"
               (B3.16, B3.17; CQ7, CQ8, CQ9)
water tap      ordered many; slab-wise 1D projection; A_tau family with
               supplied dm; boundary conventionality (B3.10–B3.14; CQ10)
splatter       ordered -> disordered many; addresses without values
               (B3.15)
convoy         over-lumping; kinematics is not cohesion (B3.21; CQ12)
wheel          rigidity without translational redundancy; proxy vs
               account (B3.22; CQ11)
brick + chip   offshoot expiry and the ledger freeze (B3.29, D14; CQ13)
```

Stretchy materials and fluids are the *uncontrived* content: this lesson is
where reality that does not arrive labelled enters the curriculum. The
supplied-target lesson (NML2.1) is the contrived one; NML2.2's realism is
its selling point to the university audience.

**(e) Prediction vs retrospective repair** (B3.20; CQ14) and the
prediction-failure audit (B3.30): "Newton II failed" is not yet a diagnosis.

**(f) Extensions, explicitly marked.** Restricted additivity derivation with
the adequacy commitment named (B3.31, CQ16); centre-of-mass derivation and
its omissions (B3.32–B3.34); deuteron grade contrast (B3.24). These pay some
of the debts NML2.1 registered.

### 3.3 Audience and behaviour

Higher education. Full halt discipline: refusal as the complete correct
answer, marked as such (E7 two-stage credit, B2.20's tempting-values row
promoted to standard practice). Address ledgers, validity intervals
(O35), provenance labelling (B3.26: which pipeline stage did the work).

### 3.4 Bank assignments — NML2.2

```text
Operations       O24–O49 (full set), O40 full form
Critical Qs      CQ7–CQ16 (CQ15 shared with NML2.1 Band III)
Exercises        B2.21–B2.25 (as on-ramp); B3.1–B3.30 core;
                 B3.31–B3.37 extensions
Demonstrations   D6, D9–D16
                 + NEW: occluded-swap demonstration (twin substituted
                 behind a screen; redundancy returns, address does not) —
                 still needs a D-number; the strongest claim in the lesson
                 currently has no perceptual defeat
Rubrics          10.4, 10.5
Minimum spine    bank section 11, Band III list, unchanged
```

---

## 4. The handoff seam

```text
NML2.1 ends with:   a mass address dying three ways (piece lost, split,
                    continuous drain) and the student unable to say when
                    reuse was ever legitimate — only that it sometimes is.

NML2.2 begins with: exactly that question. "You have been using supplied
                    targets for a year. Here is a scene with no labels.
                    Earn one."
```

What NML2.1 supplies as marked debt, NML2.2 either pays (address
construction, validity histories, restricted additivity under named
adequacy) or re-registers with a forward address (equivalence edge,
force-sum, open systems). No debt is silently discharged at the seam.

---

## 5. Smuggling policy (ratified)

The founding goal was never zero assumptions — walls *are* assumptions. The
goal is zero **unmarked** assumptions. Pedagogical form:

```text
CRITERION: supply freely what will later be RATIFIED;
           never supply what will later be REVOKED.

ratified   -> may be handed out early with a flag and a forward address
              (mass additivity: refined by the deuteron, never demolished)
revoked    -> never uttered as fact at any band
              ("scale reads inertial mass" — revoked in grade;
               "force causes motion" — demolished outright)
```

The damage in standard teaching is retroactive betrayal — a convention sold
as a fact, discovered later. A supplied binding spoken as a supplied binding
("for now, masses add; there is a later lesson about where that comes from")
rests the student's understanding equally well and betrays nothing.

---

## 6. Open items carried forward

```text
1. Author NML2.1 lesson document (replaces NML2_FINAL_DRAFT_v1 for the
   supplied-target half; three-masses lecture is net-new writing).
2. Author NML2.2 lesson document (v1 draft's sections 3–4 and the bank's
   Band III material are most of it).
3. Assign a CQ number to the Earth/Moon decorrelation probe and a
   problem number to the rocket/leaking-cart burn.
4. Assign a D-number to the occluded-swap demonstration and spec its
   apparatus.
5. Operationalise the tolerance check physically for NML2.2
   (overlay band / grid-square rule) — the audit must be something hands
   can execute.
6. Write the six signature assessment objects (bank section 15) under the
   new lesson assignment.
7. Exam-regime note for teacher-facing material: why halt discipline is
   banded the way it is.
```

---

## 7. Provenance

Decisions in this record were established in the design discussion of
2026-07-11, building on: `NML2_FINAL_DRAFT_v1.md` (architecture review and
its three content flags), `NML2_student_facing_question_exercise_
demonstration_bank_v1.md` (band structure, item codes, conflict-resolution
table), `vd_mass_identification_pipeline_d1` (Stage 4 certificate
decomposition, Stage 5 additivity grades, open-system theorem),
`vd_point_particle_bridge_spine_d1` (Wall 2, (A)/(B) split, deuteron,
separating examples), and `vd_trackability_scene_to_particles_d4`
(tracker model, lumping, defeat spectrum).

External anchors: Mach (critique of Newton's density-based mass
definition); Noll (additivity axiom separation); Hestenes / Modeling
Instruction (nearest validated pedagogy; demand-driven model construction).

One line for the head:

> **NML2.1 runs the equation and watches its mass licence die.
> NML2.2 teaches how such licences are born.**
