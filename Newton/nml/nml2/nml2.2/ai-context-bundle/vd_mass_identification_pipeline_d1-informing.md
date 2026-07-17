> **Informing copy — do not edit here.**
> **Home note:** `mass_identification_pipeline`, draft `d1` — `Newton-analysis/mass_identification_pipeline/vd_mass_identification_pipeline_d1.md`.
> Placed in `point_particle_bridge_spine` because the spine is the orientation map annotated by this note (Wall 2 and after). This is a read-only copy; refresh from the home note if the source changes.

---

# The Mass Pipeline: How the Right Mass Enters F = ma

**Status:** synthesis note, v1
**Project:** VD Newton / NML2
**Date:** 2026-07-02
**Role:** end-to-end account of how correct mass values are identified,
transported, and assembled for the forceful method. Synthesizes the
point-particle bridge spine, the persistence-certificate results (this
session), and the additivity decomposition (this session). Contains nothing
that was not established; exists so the whole chain can be read in one pass.

---

## 0. The problem

By the actually-there discipline, inertial acceleration for a massive
particle *is* net-force over inertial-mass — an entry-forced commitment,
not a correlation. Two consequences pull against each other:

```text
1. F and m must not be kinematically computable.
   Otherwise Newton II collapses into a definition and the actually-there
   commitment is voided. The track alone pins nothing: with net-force
   hidden, any m(t) fits any a(t) under a suitable F(t).

2. Yet the forceful method (Route B) needs m bound BEFORE the predicted
   track exists. Prediction runs force -> acceleration -> velocity ->
   position; the mass slot must already hold a value.
```

So the question is not only *where does the value come from* but *why is
it still valid at prediction time*. The answer, in one line:

```text
identity by lumping · value by dynamics · transport by kinematics ·
assembly by bookkeeping
```

Or mapped to the three ingredients named in the question:

```text
lumping             answers WHICH thing the mass belongs to
no offshoot tracks  answers whether it is STILL that value
mass additivity     answers how priced parts COMBINE
```

None of the three ever binds a first magnitude. That is always dynamics.

---

## 1. The chain

```text
STAGE 0  DOMAIN GATE (trackability assumption)
         classical objects supply re-identifiable tracks; frame
         certification bracketed (co-inertial problem / photon certifier)

STAGE 1  TRACK FAMILY + COVERAGE LICENSE
         the body supplies tracks; a human input certifies the family
         covers the material at the working tolerance

STAGE 2  WALL 1 — LUMPING (which thing)
         redundant sub-family -> one target, with a count; no mass yet

STAGE 3  ORIGINATION (how much)
         Wall 2 instrument route: same-pull-same-time Δv comparison;
         tolerance-true only. At splits: C8 assignment — sum pinned by
         conservation, partition open.

STAGE 4  ESCORT (still that much)
         persistence certificate: absence of offshoot tracks carries the
         binding forward. Bill: mass-locality + coverage. No additivity.

STAGE 5  ASSEMBLY (how prices combine)
         restricted net-force additivity (B) under redundancy:
         M = Σ mᵢ, exact, constitutive of lumping-as-compression

STAGE 6  BINDING INTO ROUTE B
         mass slot bound on the witness sheet, validity interval filled
         by the certificate; F_net supplied by the force side (NML3+);
         compute forward
```

---

## 2. Stage 0–1: the ground and the family

Newtonian mechanics applies to objects describable by tracks; that is the
domain gate, and its failure point is quantum statistics. Within the
domain, tracking practice supplies a *finite* family of feature-tracks at
finite resolution — in-practice proxies of the in-principle continuum.

The family carries a license with no address yet: **coverage** — every
material parcel of the body is represented by a family member at the
working tolerance. Coverage is a "probably no" input: *probably no
untracked material*. It is the third known instance of the probably-no
type, after acting-object closure and the free-particle bootstrap.
Everything downstream — especially the certificate of Stage 4 — is only
as strong as this license.

---

## 3. Stage 2: lumping fixes the referent

Before a mass can be right, "the mass of the object" must have a
referent. Tracks alone do not individuate objects; the lumping judgment
does. A human identifies a sub-family as redundant (fixed offsets within
tolerance over the interval) and thereby fixes:

```text
the target        (this lump)
the count         (how many lumps the situation contains)
the mass ADDRESS  (a slot now exists for a value to bind to)
```

The judgment is defeasible and retrospective (convoy), verifiable but not
generable by the mechanical layer, and lands at a wall. It supplies no
value. Its product is an *identity* stable enough to own a ledger entry.

---

## 4. Stage 3: origination — dynamics binds the first value

Magnitudes enter only dynamically. The NML2-legal instrument route is the
same-pull-same-time Δv comparison against a standard; a weighing scale
read as inertial mass traverses the ungranted gravitational–inertial
equivalence edge and is not legal here. The identification of the
measured number with the ledger number is empirical and **tolerance-true
only** — the deuteron's ledger mass exceeds its measured mass by ~0.1%,
and that grade is permanent, not provisional.

In actually-there vocabulary the result is a *witness-sheet slot binding
with input source*: accountable, not theory-forced.

The second origination route opens at splits and is only half-solved.
When a lump breaks, conservation-across-splits — itself a theorem, from
mass-locality plus retrospective adequacy — pins the fragments' ledger
masses to sum to the old value. The *partition* of that sum among
fragments, before any fragment has met an instrument, remains the open
residue of C8. Ideally each fragment is re-originated at an instrument;
where it is not, the partition is an unlicensed borrowing and must be
marked as such.

---

## 5. Stage 4: escort — the absence of offshoot tracks

Between the measurement at t₀ and the prediction at t, nothing
re-measures the mass. What carries the binding is a certificate whose
observable content is a *negative*: **no offshoot tracks appeared**.

The two directions of the certificate have different bills:

```text
PERSISTENCE (no offshoots -> value unchanged):
  mass-locality: mass changes only by material departure
                 (wall-grade input; the weakest surviving form of C8's
                 borrowed conservation premise)
  + coverage:    departing material would have had a track in the family
  + kinematics:  departure from a co-moving bundle entails developing
                 relative velocity, hence acceleration, hence a visible
                 redundancy break — an offshoot track
  NO ADDITIVITY. Nothing departed; no parts exist to sum.

DETECTION (offshoot -> certificate expired):
  the offshoot accelerated (kinematic necessity)
  -> actually-there: whatever is force-routed cannot be massless,
     so m_offshoot > 0
  -> retrospective adequacy (B) on the pre-split lump: M = m₁ + m_s
  -> locality carries values across the split: m₁ = M − m_s < M
  USES additivity — but only restricted (B), already derived, no new
  license; inherits the parts-have-masses presupposition, discharged
  lazily by the defeat event itself (the offshoot's acceleration is
  what forces its mass witness into existence).
```

One narrow escape keeps the conclusion honest: a never-accelerating
co-moving parcel — a convoy passenger in C6's sense — could depart
massless, leaving M unchanged. It is dynamically inert and its departure
changes no Newton-II account, so the two branches are Route-B
equivalent. The airtight statement of the detection direction is
therefore not "the mass changed" but:

```text
offshoot track observed -> the mass certificate has EXPIRED
                           and requires revalidation
```

The persistence direction is what prediction stands on, and it is
kinematically auditable: redundancy over the family is computable by the
Wall-1 mechanical layer. So the certificate decomposes as

```text
computable positive audit   (the family stayed redundant)
+ one probably-no input      (the family covers the material)
```

The certificate is tolerance-scoped — sub-resolution departures
(evaporation, ablation) drain mass invisibly. This matches the grade of
the value it escorts, which was only ever tolerance-true. Certificate and
certified value at uniform epistemic grade: honesty, not leakage.

Architecturally, the certificate is the category the actually-there
taxonomy lacks: that taxonomy (entry-forced / witness-forced / input) is
static, classifying commitments at a trace-moment, while Route B runs
forward in time and needs its input bindings to *survive* the run. The
certificate is a **temporal extension license** for a slot binding. In
implementation terms: witness sheets acquire a validity-interval field,
and redundancy is what fills it for `inertial-mass`.

---

## 6. Stage 5: assembly — where additivity actually works

Additivity never originates a value; it combines already-priced parts.
Its licensed form at NML2 is restricted net-force additivity (B): parts
sharing one acceleration have their Newton-II accounts aggregated by the
adequacy norm, and per-part Newton II converts the aggregate into

```text
M = Σ mᵢ        (exact; ledger route)
```

Mass additivity is the shadow of net-force additivity through Newton II —
never a primitive of its own. Its grade is analytic *relative to the
lumping concept*: deny adequacy and the coarse description is no longer a
compression of the fine one, merely a fresh particle whose mass relation
to the parts is an empirical question — which is Wall 2. The aggregation
route is exact because the ledger is ours; the instrument route is
tolerance-true because nature is not (weld a broken brick and the
measured mass falls back toward M while the carried-forward ledger says
m₁ + m₂; the daylight between routes is booked at Wall 2).

Scope discipline:

```text
restricted (B), shared acceleration:   licensed, NML2, exact
general (B), any internal motion:      ⟺ weak Newton III given
                                       superposition — FORBIDDEN at NML2;
                                       "masses always add" is the third
                                       law wearing mass-vocabulary
empirical additivity:                  tolerance-true, Wall 2
```

Practically, assembly is what lets Route B price composite targets
without new measurement: measure the carts once, clip them, and the pair
enters F = ma at m₁ + m₂ — legal precisely because lumping-first keeps
the coupling force off the books (the one-force perimeter doing live
work).

---

## 7. Stage 6: binding, and the temporal shape

At prediction time the mass slot is bound by a value whose full forcing
path is on the record:

```text
Wall-1 identity (which lump)
  -> Wall-2 / assembly origination (which value, with grade)
  -> certificate over [t₀, t] (why still that value)
  -> witness-sheet slot binding with validity interval
  -> Route B consumes it
```

Every observational element in the path is past-facing: the measurement,
the redundancy audit, the coverage judgment. Route B is future-facing and
never consults a future observed track. Observation feeds prediction only
at its past boundary — which is why no circularity arises between the
observational and forceful methods.

Division of labour, and the grade of each link:

```text
kinematics    forces existence (a ≠ 0 -> m > 0), certifies persistence;
              never binds a magnitude
dynamics      originates magnitudes                 [tolerance-true]
bookkeeping   combines magnitudes                   [exact / analytic]
human inputs  lumping, locality, coverage           [wall-grade]
```

The value plugged into F = ma inherits the weakest grade in its chain:
tolerance-true. Nothing in the pipeline pretends otherwise, and nothing
needs to.

---

## 8. Expiry and repair: the prediction-set branches

Because every link is on the record, a failed Newton-II prediction can be
audited against the mass story. The licensed branches:

```text
certificate expired mid-run   undetected / sub-resolution departure
                              (evaporation, ablation; rockets are the
                              systematic case — continuous expiry at the
                              nozzle, which is WHY open systems are
                              outside NML2 as a theorem, not a choice)
over-lumping                  a convoy was priced as one target
origination error             bad Wall-2 value or unlicensed C8 partition
assembly misapplied           parts not actually redundant
                              (spinning wheel: account holds, proxy and
                              shared-A both fail)
domain-gate failure           mass-locality violated with no material
                              departing — binding energy radiated; the
                              relativistic boundary announcing itself
```

The last branch completes a pattern worth keeping: each precondition
entry predicts a domain boundary at its own failure point —

```text
trackability fails       ->  quantum statistics
mass-locality fails      ->  relativistic mass–energy
Galilean append-only     ->  Lorentz covariance (EM incompatibility)
```

---

## 9. A worked micro-run

```text
1. A brick supplies a track family; coverage judged adequate.      [S1]
2. The family is redundant; lumped to one target.                  [S2]
3. Same-pull comparison binds m = 2.30 (tolerance-true).           [S3]
4. Weeks pass; the family stays redundant; binding carried.        [S4]
5. A second brick, priced at 1.15, is clipped on; the pair is
   redundant; assembly prices the composite at 3.45 (exact).       [S5]
6. Route B predicts under a known pull; prediction lands.          [S6]
7. Later a chip flies off — an offshoot track. Certificate
   expires. The chip's acceleration forces its mass witness;
   conservation pins chip + remainder to 3.45; the partition
   awaits an instrument.                                       [S4→S3]
```

Steps 1, 2, and the coverage half of 4 are human inputs at walls. Steps
3 and 7's re-origination are dynamics. Steps 4's audit and 5 are
machine-checkable. Step 6 never looks backward.

---

## 10. Compact summary

```text
The right mass is not read off any track.

Lumping fixes WHICH thing owns a mass slot (Wall 1; defeasible).
Dynamics binds HOW MUCH, once (Wall 2; tolerance-true).
The absence of offshoot tracks certifies STILL THAT MUCH
  (locality + coverage; computable audit + one probably-no;
   no additivity; expiry observable).
Restricted additivity (B) prices COMPOSITES of already-priced parts
  (exact bookkeeping; general form forbidden — it is weak NIII).

Kinematics forces existence and escorts values; dynamics originates
them; bookkeeping combines them. Route B consumes the binding through
a validity interval and never consults the future.
```
