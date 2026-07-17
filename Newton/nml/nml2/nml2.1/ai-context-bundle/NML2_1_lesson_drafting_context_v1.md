# NML2.1 — Drafting Context (AI-context compilation)

> **ROLE: ai-context.** Compiled 2026-07-14 for the AI/session that will author the
> NML2.1 lesson document (ratification open item 1). This file is not a lesson
> draft and is never iterated: the document drafted FROM it becomes this folder's
> note (`nml2.1_lesson`, d1). If sources change, refresh this compilation from its
> home documents (listed in §10). Canonical authority for every decision below:
> `../NML2_split_ratification_d1.md`.

---

## 1. Mission

Author **NML2.1 — The Newton-II Lesson**: the supplied-target half of the former
NML2, replacing `../NML2_FINAL_DRAFT_v1_d1.md` for that half. The three-masses
lecture segment is **net-new writing** (no prior draft exists). Target artifact:
an integrated lesson document in the style of the frozen v1 draft (thesis,
sequence, segments, worksheet specs, teacher wording, misconceptions, criteria
of instillment, compressed/extended variants), banded I–III.

Label discipline: numeric labels only. The bank's "NML2B" = this lesson;
"NML2A" = NML2.2. Never reintroduce the letter labels.

## 2. Thesis (ratified verbatim)

> Newton II locks three quantities owned by one target. The mass slot in that
> relation is one of at least three things "mass" can mean, and the everyday
> certainty that masses add is not one claim but three claims with three
> different bills. This lesson runs F = ma correctly, decorrelates inertia
> from gravity, and ends at the exact point where reusing a mass value
> requires a licence the lesson has not granted.

One-liner: *NML2.1 runs the equation and watches its mass licence die.*

## 3. Content specification

**(a) The addressed triplet.** `m[A]`, `a[A]`, `F_net[A]` locked by Newton II;
same target, same interval, frame-qualified. Three algebraic forms. The triplet
is a constraint, not a generator (CQ18 / B2.6A: no supplied values → no output;
two independent addressed values determine the third). Units (`1 N = 1 kg m/s²`),
vector discipline, the zero case (`a=0 → F_net=0`, and nothing more), and the
thin net-force wall: net force is supplied or Newton-II-inferred; a meter reads
one transmitted contribution (see `../NML2_note_net_force_wall_withheld.md` —
the wall stays THIN, exactly as in v1 §5.4/§14.6).

**(b) The three masses** — the load-bearing lecture segment, university-facing,
compressible for lower bands. Net-new writing; sources: mass pipeline Stage 5 +
bridge spine Wall 2 + ratification §2.2(b).

```text
DENSITY (STUFF) MASS   m = rho V; amount of matter; Newton's own definition,
                       Mach's circle. Additive BY CONSTRUCTION (two buckets
                       of sand) — where the "obviously additive" intuition lives.
GRAVITATIONAL MASS     the coupling a scale actually reads. Identification
                       with inertial mass = the ungranted equivalence edge —
                       a physical postulate, not a convenience.
INERTIAL MASS          the m in F = ma. Legal origination at this level:
                       same-pull-same-time delta-v comparison against a
                       standard. Never a scale.
```

The conceptual payload: surfacing the textbook smuggle that silently identifies
stuff-mass with the m in F = ma.

**(c) Additivity as three claims, three grades** — presented as an
*underexplored assumption*; every grade's bill is named, none is paid here:

```text
stuff-mass additivity      analytic by construction        (free)
measured-mass additivity   empirical, tolerance-true only  (deuteron ~0.1%)
ledger-mass additivity     derived under adequacy (B)      (later machinery)
```

This is pipeline Stage 5 delivered as a lecture without the pipeline vocabulary.

**(d) Inertia ≠ gravity — the decorrelation goal.** Earth fuses hard-to-lift
with hard-to-shove; the lesson forces them apart. Sideways pushes on supported
objects (gravity orthogonal, visibly irrelevant). Signature probe (needs a CQ
number — open item):

> The same sideways push on the same cart, on Earth and on the Moon. Compare
> the motion-changes. Expected: identical. Lifting got easier; shoving did not.

**(e) Extreme-mass horizon** — kept, trimmed: Earth as extremely massive
participant, D4 form only (equal-scale action *supplied*, mass-side reasoning
only). The Sun–planet centrality claim is **dropped as a learning goal**
(it needs Newton III — interaction-pair smuggling); at most a one-line horizon
gesture with its bill named.

## 4. Stratification

```text
BAND I–II CORE
  ownership drills, addressed triplet, three algebraic forms, units, vectors,
  zero case, qualitative inertial-mass comparisons, force-to-path stepping
  with supplied F_net, the halt SEED (E6) only.

BAND III EXTENSION (calculus — changes representation, not licences)
  continuous supplied F_net(t), F(r): genuine ODE problems, constant mass;
  the discrete stepper's continuum limit;
  planet activity as differentiate-twice-and-infer (Newton-II inference with
    a supplied frame certificate);
  piecewise-constant mass with EXPLICIT re-licensing events between phases;
  parameterised families of fixed-mass targets with supplied bindings
    (previews A_tau without teaching lumping);
  three-masses lecture and additivity grade table at full depth.
```

Policing rule: every supplied F_net remains ONE opaque vector. Standard
multi-force calculus setups (drag + gravity, spring + friction) breach the
force-sum wall and are OUT.

Assessment-regime placement (ratification finding 4): young bands install
*ownership auditing* ("which object owns this number?" — costs nothing on any
exam) and only the E6 halt seed; full halt discipline and refusal-as-correct-
answer live in Band III here and in NML2.2, where assessment can honour them.
A teacher-facing exam-regime note is open item 7.

## 5. Licence table (ratified)

```text
GRANTED
  Newton-II triplet with supplied/inferred F_net
  supplied mass bindings with owner and marked provenance
  same-pull-same-time comparison as the ONLY inertial-mass origination
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

Smuggling policy: supply freely what will later be RATIFIED (flag + forward
address); never supply what will later be REVOKED. Zero *unmarked* assumptions,
not zero assumptions.

## 6. Exit boundary — the burn (design requirement, not summary)

The climax is a designed failure. Final Band III problem invites blind
F = m(t)a substitution on a continuously mass-losing target; the leaking-cart
form makes the naive substitution demonstrably not-even-well-defined (answer
depends on momentum carried by departing material). **The resolution is not
given.** Exit statement (ratified verbatim):

> Mass reuse is licensed separately from the equation that consumes it. The
> licence just expired continuously, and you do not yet own the machinery that
> handles that. Two lessons answer this: one about how targets and their mass
> addresses are built and audited (NML2.2), one about momentum (later).

The rocket appears ONLY as this boundary probe — never as a solved problem.
Lower-band burn at their representation: mandatory E6 halt-seed row + one
two-scene problem where blind reuse of m fails because the object visibly lost
a piece between scenes.

Sequencing requirement (bank can't hold it; the lesson doc must): burn before
machinery *inside* the lesson too — open with the cross-target trap (CQ1) or a
wrong-prediction scene; addressed-triplet notation arrives as the *repair*,
never as an announced convention.

## 7. Bank assignments (pull from `../NML2_student_facing_question_exercise_demonstration_bank_v1_d1.md`)

```text
Operations       O1–O23, O34 (address/value separation at supplied level),
                 O40 seed form, O41–O42, O50
Critical Qs      CQ1, CQ2, CQ3, CQ4, CQ5, CQ6, CQ17, CQ18
                 + NEW: Earth/Moon decorrelation probe (assign CQ number)
Exercises        B1.1–B1.22, E1–E6; B2.1–B2.20, E7–E10
                 (B1.9 bracket notation -> Band II; owner-lines and coloured
                  rows do its Band-I work)
                 (B2.12 fenced to Band II explicitly — impulse in a wig)
Demonstrations   D1, D2, D3 (redundancy SEED only), D4 (supplied-scale form),
                 D5, D7 (qualitative), D8, supplied-force simulation
Rubrics          10.1, 10.2, 10.3
Boundary probes  B2.14 rows, photon question normalised (CQ15 at Band III,
                 shared with NML2.2), rocket/leaking-cart burn (assign number)
New lecture      three-masses segment; additivity grade table (NOT in bank)
```

Also honour bank §14 (operations that must not be smuggled into core NML2) and
bank §11 Band I/II minimum spines.

## 8. Reuse from the frozen v1 (`../NML2_FINAL_DRAFT_v1_d1.md`)

Reusable for this lesson: §5 (Newton-II law-house: triplet, thin net-force
definition, three forms, units, zero case), §10.3 (force-to-path sheet), §10.4
(halt row), §11 teacher wording (Newton-II lines), §12.6–12.8 misconceptions,
§13.5–13.8 criteria, §15 planet extension (relabelled Band III). The v1
"adaptable from young learners to undergraduates" audience claim is DISSOLVED
by the split — the band invariant (moving an exercise between bands changes
representation, not trace) now operates within NML2.1.

NOT for this lesson (belongs to NML2.2): v1 §§3–4 (track-families, redundancy,
tolerance, bouncy ball), §10.2 address ledger, §12.1–12.5, §13.1–13.4. Here,
targets and masses are always SUPPLIED with owner and provenance marked.

## 9. Prerequisites and constraints from working notes

- `../NML2_working_note_core_constraints.md`: entry scope E8–E13; E7 (inertial
  acceleration readout) is a prerequisite reactivated, not retaught; E14+
  deferred; one force / one mass / one motion-change.
- `../NML2_note_net_force_wall_withheld.md`: the thin typed net-force wall —
  addressed vector, newtons, Newton-II relation; production withheld to NML3.
- NML1 handoff: trajectory → velocity-change → inertial acceleration must be
  in place (bank §1.1, §9); brief E7 diagnostics allowed (B1.19–B1.22).

## 10. Open items to resolve while drafting (ratification §6)

1. Assign a CQ number to the Earth/Moon decorrelation probe.
2. Assign a problem number to the rocket/leaking-cart burn.
3. Write this lesson's share of the six signature assessment objects (bank §15:
   items 1–4 and the shared item 7 are NML2.1-facing).
4. Exam-regime note (teacher-facing): why halt discipline is banded as it is.

## 11. Source set to co-locate when drafting

From `../` (nml2 parent): `NML2_split_ratification_d1.md` (canonical),
`NML2_student_facing_question_exercise_demonstration_bank_v1_d1.md`,
`NML2_FINAL_DRAFT_v1_d1.md` (frozen; §5/§10.3–10.4/§11–§15 mine-able),
`NML2_note_net_force_wall_withheld.md`, `NML2_working_note_core_constraints.md`.

From `../ai-context-bundle/` (or their home notes): `newton_II_cleaned.md`
(exact triplet commitments), `VD_Newton_inertial_acceleration_two_entries.md`
(free-route vs Newton-II acceleration; photon boundary),
`vd_mass_identification_pipeline_d1-informing.md` (Stage 5 → three-masses
lecture and grade table), `vd_point_particle_bridge_spine_d1.md` (Wall 2,
deuteron, (A)/(B) split), E7 docs (`E7_INERTIAL_ACCELERATION_PLACEMENT_NOTE.md`,
`NM_L1_E7_E8_decision_note.md`, `NM_L1_E7_integrated_complete_draft_d2.md`),
`vd_pedagogy_note.md` (probe design over illustrative examples).

External anchors (cite, don't re-derive): Mach (critique of Newton's density
definition), Noll (additivity axiom separation), Hestenes / Modeling
Instruction (demand-driven model construction — nearest validated pedagogy).
