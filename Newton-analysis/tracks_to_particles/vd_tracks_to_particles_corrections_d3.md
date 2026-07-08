# Corrections: From Tracks to Particles

**Status:** corrections note, v1
**Applies to:** `tracks_to_particles_rigidity_as_lumping_criterion.md` (working draft, "the note")
**Date:** 2026-07-01

Issues found in review, with the fixes adopted. C1–C7 are resolved in principle
and await the rewrite. C8 is open and deliberately parked. Byproducts and smaller
edits at the end, then a rewrite map.

---

## C1. The tap violates the stated criterion

**Problem.** Take two parcels on the same vertical line of a steady stream. The
lower one left the tap earlier, so at any instant it is faster; both accelerate
at g, so their velocity difference is constant and their separation grows
linearly. The visible signature is the stream narrowing as it falls. The
flagship example therefore fails "fixed mutual distances" at first order, over
any interval. The tap is not one rigid bundle.

**Fix.** The tap is not represented as one particle; it is represented as a
particle stream. Lumping applies slab-wise: within a thin slab dh, parcels share
the velocity field and their tracks differ by fixed transverse offsets; across
slabs, redundancy fails. The criterion then yields an ordered chain of
particles, one per slab.

**Consequences.** §1–§3 restructure. Promote a genuinely redundant bundle
(thrown ball, brick) to the one-particle slot, and run the ladder:

```text
ball:      one bundle             -> one particle
tap:       chain of slab bundles  -> ordered many particles
splatter:  broken bundles         -> disordered many particles
```

A better pedagogical ladder than tap/splatter alone: one → ordered many →
disordered many.

**Residual caveat.** Even a slab is not strictly redundant: the material
stretches vertically at strain rate ≈ g/v, and incompressibility forces
transverse contraction at the same order. Slab-wise lumping closes only under
the tolerance clause of C2.

---

## C2. The primitive is kinematic redundancy, not rigidity

**Problem.** Strict distance-rigidity fails the tap even slab-wise (C1 caveat).
The rescue-by-"rigidity along the fall dimension" is not rigidity — fixed
mutual distance is a claim about the full separation vector — so it was an
undeclared new primitive doing load-bearing work.

**Fix.** Replace the primitive:

```text
kinematic redundancy :=
Tracks r_i(t), r_j(t) are redundant, over the modelling interval and within
the modelling tolerance, when r_i(t) − r_j(t) stays constant to within the
tolerance — the tracks differ by a fixed offset.
```

Redundant tracks share a velocity field and keep fixed mutual distances. The
"dimension-restricted" notion dissolves into component-wise agreement of the
offset; no extra primitive needed. The agreement is between trajectories
(time-indexed), never paths: two tracks tracing the same path at different
times are not redundant.

**C2a. Direction of implication — sharpening found while writing this note.**
Redundancy ⟹ fixed distances. The converse fails: fixed distances permit
rotation, and a rotating bundle's tracks are *not* redundant — rim points of a
spinning wheel have different velocities at every instant, so no one track can
stand for all. Distance-rigidity as §2 defines it therefore **over-licenses**:
it would lump a spinning wheel to one particle and silently discard the spin.
The criterion must be redundancy (fixed offset), with distance-preservation as
a consequence, not the definition. This also corrects the review discussion
itself, which had called strict rigidity "the limiting case" — the
zero-tolerance limit of redundancy is rigid *translation*, a proper subset of
rigid motion.

---

## C3. Two licenses were conflated

**Problem.** The note implies redundancy is what licenses the one-track
Newton-II description. But the centre-of-mass theorem, F_ext = M·a_cm, is
redundancy-free — it holds for the splatter, for a gas, for anything.
Redundancy cannot be what licenses the one-track *account*.

**Fix.** Separate two licenses:

```text
mass-weighting licenses the ACCOUNT:
  a single-track Newton-II ledger (the CoM track) exists for any body,
  redundant or not.

redundancy licenses the PROXY:
  any member track may be read in place of the representative, because
  the tracks are informationally interchangeable.
```

The lumping move is the epistemic license. The separating examples run in both
directions:

```text
spinning wheel: account valid, proxy invalid (rim track ≠ CoM track)
convoy:         proxy valid over the interval, no cohesion behind it (see C6)
```

**Consequences.** §3 and §6 reframe. This split is instructor/design-facing at
the NML1→2 hinge — the CoM theorem is not available to the student yet; the
lesson text needs only the proxy license.

---

## C4. The partition is not well-defined (transitivity bug)

**Problem.** Strict mutual rigidity is not transitive: let A and C circle B at
different rates — |AB| and |BC| stay constant while |AC| varies. Redundancy
within tolerance is likewise not transitive (tolerances compound). Maximal
mutually-redundant sets are cliques, not equivalence classes; cliques can
overlap; §4 step 3's "partition" is not guaranteed to exist.

**Fix — reclassification, not repair.** Define a bundle as a maximal
all-pairs-redundant set. Acknowledge that admissible bundlings may be
non-unique. The choice among them is a residual-layer judgment landing at a
wall. The mechanical layer can *verify* a proposed bundling (all-pairs
redundancy is computable from the tracks); it cannot uniquely *generate* one.
Same verify/generate split the VD uses elsewhere.

Note: strict redundancy at zero tolerance *is* transitive — fixed offsets
compose — so the bug is specifically a tolerance artifact. It cannot be removed
by removing tolerance, because C1/C2 made tolerance load-bearing.

---

## C5. "Read off the tracks" overclaims

**Problem.** With tolerance in the primitive, particle count is relative to a
question-supplied tolerance. Two descriptions of the same splatter at different
tolerances legitimately yield different counts. The tracks alone do not fix the
number; "read off" suggests mechanical extraction.

**Fix.** Rhetoric change: the tracks *constrain and certify* the count; the
modelling question supplies the tolerance; the human supplies the
identification. VD placement: the lumping identification lands at a wall.
Downstream consistency is auditable; the lumping itself is not, because the
audit presupposes the ontology the lumping establishes.

This is the second known instance of the Newton-I pattern — an unauditable
human judgment the trace stands on (first instance: the initial
free-particle/frame identification). Flagged as the strongest current candidate
for the claim that these findings are products of the VD; to be checked against
session history for whether wall-landing discipline actually forced the
question.

---

## C6. The criterion is retrospective and defeasible (convoy case)

**Problem.** Redundancy is certified over an *observed* interval. Two cars in
convoy are one bundle by the criterion — right up until one brakes. The
criterion cannot distinguish constraint (cohesion enforced by internal forces)
from coincidence (co-movement that happens to hold). It over-lumps coincidences
and detects splits only after they occur.

**Fix.** State it rather than hide it: lumping is a defeasible, retrospective
judgment. The splatter is the canonical defeating event; re-lumping after
defeat is the normal revision cycle. The dynamical notion of unit-hood — what
responds to force as one — belongs later in the sequence, once force accounting
exists. NML2 gets the kinematic notion, honestly labelled.

---

## C7. §0's centre-of-mass sentence is wrong

**Problem.** "The centre of mass is simply one of them that happens to be
trackable too" — false in general. The CoM is usually not a material point at
all (hollow ring: the CoM sits in empty space). It is not *selected from* the
family of tracks; it is *constructed from* it.

**Fix.** CoM = constructed, mass-weighted representative track; its
trackability is derivative, inherited from the family. This strengthens the
tenant-not-foundation line rather than weakening it: the CoM is not even a
resident material point — it is bookkeeping over them. Also soften
"trackability is a property of *all* material points": fluids already strain
point re-identification, and the trackability note itself hedges the fluid
case.

---

## C8. §5 mass assignment — OPEN, parked

Two identified issues, no adopted fix:

1. "Each particle carries the mass of the material that moves rigidly with it"
   borrows a pre-Newtonian mass concept (amount-of-stuff, density × volume)
   plus a conservation assumption across the split, at a stage of the sequence
   where mass has not been operationally introduced. The count criterion is
   kinematic; the mass criterion is not. The asymmetry is unacknowledged in the
   note.
2. A separately flagged unease about the masses of the scattered droplets —
   parked deliberately, not yet articulated.

§5 is the active front. Nothing in C1–C7 depends on resolving it.

---

## Byproducts worth keeping

```text
compression framing:
  lumping is compression of redundant tracks, lossless up to tolerance.
  ball = maximal compression; tap = per-slab compression; splatter =
  compression broken into pieces; full shear = incompressible description.
  The fine-grain limit recovers the continuum-mechanics fluid element —
  the criterion has a limit story, the mark of a concept rather than a trick.

Newton-I echo:
  two known instances of "unauditable wall judgment the trace stands on":
  the frame bootstrap, and now the lumping identification. Candidate general
  pattern; candidate core of the VD-provenance claim. Verify causal history
  against session notes.
```

---

## Smaller edits (S-list)

- **S1, §1.** "100 tracks, each carrying 1/100 of the flow's material"
  forward-references mass before §5 introduces the rule. Keep tracks mass-free
  until §5.
- **S2, §3.** "Nothing to distinguish them *dynamically*" → *kinematically*.
  The criterion never tests dynamics; that is exactly C6's point.
- **S3, §5.** "A track ... is just a geometric line through space and time" →
  *a time-indexed curve*. The note's own foundation is trajectory-not-path;
  don't undersell it in passing.
- **S4, §5.** Drop the "double duty" slogan. After C3/C8, count and mass are
  answered by different criteria of different kinds; the slogan papers over
  the asymmetry.
- **S5, §7.** The compact summary restates every pre-correction claim (strict
  rigidity, tap-as-one-particle, partition-as-given). Rewrite it last, from the
  corrected sections, not alongside them.
- **S6, title.** The primitive is now redundancy. Either retitle ("Kinematic
  Redundancy as the Lumping Criterion; Rigidity as the Special Case") or keep
  "rigidity" as the student-facing word and let the definition carry the load.
  A deliberate choice to make, not a default to inherit.
- **S7, §0.** Add one-line pointers to the two upstream trackability-note
  issues that leak into §0: (a) re-identification is frame-relative while
  frames are bootstrapped from tracked bodies — the ordering sentence is owed
  there; (b) point *selection* is a residual-layer act and should be labelled
  as one.
- **S8, whole note.** Mark which corrections are student-facing (C1 ladder,
  C6 defeasibility label) and which are instructor/design-facing (C3 split,
  C4 clique caveat, C5 wall-placement). The draft currently mixes registers.

---

## Rewrite map

```text
§0:      C7 sentence fix + S7 pointers
§1–§3:   C1 restructure (ball/tap/splatter), C2 definition swap,
         C3 reframe, S1, S2
§4:      C4 clique wording, C5 rhetoric change,
         new short defeasibility paragraph (C6)
§5:      unchanged, marked OPEN (C8); S3, S4
§6:      corrected ladder + two-license split (instructor register),
         C5 wall-placement
§7:      rewrite last, from corrected text (S5)
title:   S6 decision
```
