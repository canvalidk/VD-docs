# Identifiability and Fluid Representation: Pieces That Keep Almost Meeting

**Status:** discovery record. A gathering of parts, not an argument.
**Project:** VD Newton-analysis
**Date:** 2026-08-26
**Warning:** This document does not contain a single coherent idea, and should not be
read as if it were building toward one. It records a set of separately-motivated
observations that keep landing near each other, together with the reasons to doubt
that the landing is meaningful. The suspicion is worth keeping. The synthesis has
not been earned.

---

## 0. Why this exists

Over one session, three lines of work that had nothing to do with each other kept
producing the same shape of problem:

```text
the trackability material   (how does a scene supply tracks?)
fluid representation        (in what sense can water be said to move?)
newton_vs_gibbs             (what does Newton assume about which particle is which?)
```

Each is independently motivated. Each was developed without reference to the others.
Each ends up asking whether a thing can be told apart from its neighbours and kept
told-apart through time. That recurrence is the whole content of this record. It is
not yet a reason to think they are the same question.

---

## 1. Three senses of identity, and the fact that they keep almost coinciding

The recurring shape hides an ambiguity that has to be stated before anything else,
because most of the apparent connection may live in it.

```text
HAECCEITY (metaphysical)
  Is there a primitive fact about which particle this is, over and above all its
  properties? Newton needs yes. Nothing in the laws states it.

EXCHANGE SYMMETRY (quantum)
  Is the state symmetric or antisymmetric under swapping two particles of the same
  species? A fact about the formalism, and a positive denial of haecceity for
  identical particles - not an admission of ignorance.

TRACKABILITY (operational)
  Can a tracker re-identify a selected point through time, within a working
  tolerance, over a modelling interval? Graded, indexed twice, defeasible.
```

These are not obviously the same, and there are cases where they come apart cleanly.
Two billiard balls are haecceity-bearing and exchange-distinguishable and I can still
lose track of them in a dark room. Two electrons in adjacent localised orbitals are
exchange-identical and yet their occupied states are as well-individuated as anything
in physics.

So the excitement of this whole cluster is that the three might line up. The danger
is assuming they do. Every piece below should be read with the question: *which sense
of identity is this piece actually about?*

---

## 2. The pieces

### 2.1 Trackability sorts material; it does not describe a scene

The claim, stated for the first time this session: trackability is not a property
proposed of the whole scene. Some material supports re-identification through time
and some does not. Water and gases do not. So the trajectory formalism does not
apply uniformly to what is in front of us - it applies to the part of the world that
survives a sort.

This is a departure from how the current design note has it. `vd_trackability_scene_
to_particles_d4.md` section 0 says *the material of the world is trackable*, flat and
global. That sentence is now a known overstatement.

The corollary offered alongside it: non-trackable things are regarded by their
impacts on trackable things. That corollary is deliberately NOT developed here or in
`scene_trackability` - it needs acting-object apparatus that is not available that
early. It is recorded, not used.

### 2.2 The permanent residue was already saying this

Section 2 of the same design note grades two coverage residues:

```text
seeding residue      did we follow enough points?   DISCHARGEABLE
resolution residue   is there material transport
                     below what the video resolves? PERMANENT
```

and gives evaporation, ablation and sub-pixel flow as the examples. The note explains
the permanence as a fact about the tracker: densifying seeds adds tracks, not
resolution.

Under 2.1 the explanation changes. The residue is permanent because *there is nothing
there to re-identify*. The limitation was never the instrument. That upgrades a
recorded fact to an explained one, which is a point in the sorting's favour.

### 2.3 Water broke the criterion first, and nobody noticed why

The flagship example of the earlier draft was a tap - a falling stream. Correction C1
killed it: parcels on the same vertical line fail fixed mutual distances at first
order, so the tap is not one rigid bundle. The rescue was to lump slab-wise, yielding
an ordered chain of particles, one per slab.

Read now, the rescue looks like what it is: slab identity is *imposed*, not found.
The document's own flagship case was already a case of a fluid failing to carry the
identity the method needed, and it was patched rather than diagnosed.

### 2.4 The jump from tracer to fluid has no limit - it has a window

Standard practice says: seed a flow with small particles, track the particles, call
the result the fluid's velocity field. The usual justification gestures at a limit as
particle size goes to zero. There is no such limit. There is a band with two edges,
and both edges are already named in fluid mechanics:

```text
UPPER EDGE   Stokes number St = (particle response time)/(flow time).
             Too large and inertia decouples the tracer from the flow: it stops
             following. In turbulence the practical bound is the Kolmogorov scale.

LOWER EDGE   Knudsen number Kn = (mean free path)/(characteristic length).
             Too small and the tracer reports molecular chaos rather than flow -
             Brownian motion takes over. This edge IS the continuum hypothesis.
```

So the comfortable jump is licensed inside a band bounded above by flow structure and
below by molecular granularity. In ordinary laboratory conditions the band spans six
or seven orders of magnitude, which is why nobody has to name it, and why the jump
feels like a limit rather than a window.

The relevant point for this record: the lower edge is where identity fails. The
window's floor and the trackability horizon look like the same floor.

### 2.5 The tracer is a distinguishable proxy inserted into an indistinguishable medium

This piece is the one that most makes the cluster feel real, and it should be
weighed carefully because of that.

A PIV tracer bead is not a water molecule. It is a foreign, macroscopic,
property-distinguishable object placed into a medium whose constituents are
exchange-identical with one another. You cannot track a water molecule, so you insert
something that CAN be tracked and read the water off its behaviour.

Which is exactly the corollary in 2.1, arrived at from the opposite direction and
without anyone intending it: the non-trackable is regarded by its impacts on the
trackable. The dominant experimental method for measuring fluid motion is an instance
of the principle, not an exception to it.

Caution: this is an argument by pleasing fit. It shows the vocabulary applies. It does
not show the vocabulary is doing work.

### 2.6 The ambiguity already has a name: Eulerian and Lagrangian

Fluid mechanics carries two descriptions and moves between them freely.

```text
EULERIAN     fields at fixed spatial points. Needs NO identity - nothing is
             re-identified, so nothing must be trackable.
LAGRANGIAN   follow material parcels. Needs identity throughout.
```

The bridge is the material derivative, D/Dt = d/dt + u . grad. That operator asserts
the two readings are interchangeable and never states a condition. If the sorting is
right, the condition is the window of 2.4: interchangeable exactly where a tracer
would work.

This is the single most checkable item in this record, because it says something
specific about an operator physicists use daily.

### 2.7 Volume as addressable domain, not as an inventory of tracks

A conjecture raised this session: when phases are eventually encoded they will be
defined by pressure, pressure will fix volume, and volume will correspond somehow to
the tracked points.

It cannot correspond to tracked points directly. A gas has a volume and nothing
trackable in it, which would break the sort at 2.1 immediately. The repair: volume is
the *addressable domain of the field* - the region in which a tracer could be placed
and would report coherent motion. Not an inventory of tracks; a domain of possible
ones.

Repaired that way, the conjecture is the Eulerian-to-Lagrangian identification of
2.6, licensed inside the window of 2.4. Which is either a satisfying convergence or
the same idea counted three times. Not currently decidable.

### 2.8 Newton's hidden commitment to distinguishability

`newton_vs_gibbs/newton_vs_gibbs_d1.md`, written independently and filed elsewhere in
this branch, argues that writing an initial value problem at all requires particles
to be distinguishable as individuals independent of their properties - and says, in
passing:

> The framework needs to track which is which through time, and that tracking
> presupposes a primitive fact of identity that the laws themselves never state.

That is the trackability concept, used without being named, inside a document about
the Gibbs paradox. Its conclusion is that Newton's ledger and Gibbs's ledger disagree,
in units of log N! bits, about how much information the world contains about its own
particles.

If 2.1 is right, the two divides are the same divide: material that fails the sort is
material whose constituents carry no usable haecceity, which is the regime where the
N! correction is required. Solids are trackable, haecceity is usable, Newton is fine.

### 2.9 Bosons and fermions: where haecceity is positively denied

Classical thermodynamics subtracts distinguishability as a bookkeeping correction.
Quantum statistics denies it as a postulate, and does so with structure:

```text
BOSONS     symmetric under exchange; unlimited co-occupation; bunching.
           A condensate is the extreme case - macroscopic occupation of one state,
           individuation gone in principle, not merely in practice.
FERMIONS   antisymmetric under exchange; Pauli exclusion; one per state.
           States are individuated. Their occupants are not.
```

Two things worth recording. First, indistinguishability is a RELATION and not a
property: it holds between particles of the same species. An electron and a proton
remain distinguishable. This matters for 2.5 - the tracer works partly because it is
a different species from the medium.

Second, and this is the knot most worth keeping: ordinary matter is stable and
extended largely because of exclusion, which is a consequence of fermionic
antisymmetry, which is the denial of haecceity. So the microscale absence of
individual identity is a large part of what produces the macroscale bodies whose
points are trackable. The property that makes Newtonian individuals possible may be
downstream of the formal denial that particles are individuals.

Suggestive. Also exactly the sort of thing that sounds profound and turns out to be a
pun on two uses of identity. Flagged accordingly, per section 1.

### 2.10 Phases, pressure, and one prediction

Two items to carry into entry work, both cheap to record now.

Pressure fixes volume only given temperature and amount - PV = nRT and its messier
cousins. A phase entry taking pressure as THE defining quantity inherits a silent
dependency on two further quantities. That is the smuggled-input shape this project
exists to catch, and it should be caught before it is written rather than in review.

And a prediction, stated so it can fail: if phases are pressure-defined, a phase can
never be a TARGET. Pressure is a field, identity-free, on the non-trackable side of
the sort. A phase acts and is never accelerated. Nobody writes F = ma for the liquid
phase - and on this account that is a consequence rather than a habit.

### 2.11 The binary/graded mismatch

The Gibbs argument treats distinguishability as binary: each particle either is or is
not an individual, and the disagreement is a fixed log N! bits. Trackability, as built
here, is graded and indexed twice - by interval and by tolerance.

Both cannot be the last word. If the sorting is right, the log N! disagreement is not
a constant but a LIMIT: the value approached as the modelling interval outruns the
trackability horizon, with total permutation symmetry as the fully collapsed case.

This is the sharpest claim in the record and the least supported. See 4.3.

---

## 3. What the pieces seem to want to say

Stated once, plainly, and then immediately qualified in section 4. Not adopted.

> There is one boundary, not several. On one side, material whose points can be kept
> apart through time: it supports tracks, targets, trajectories, F = ma. On the other,
> material whose constituents cannot be kept apart at all: it supports fields,
> aggregates, pressures, temperatures, and enters mechanics only through its effects
> on the first kind. The boundary is not sharp, it is a horizon indexed by interval
> and tolerance, and most of the apparatus of both mechanics and thermodynamics is
> machinery for working near it without saying so.

The reason to write that down is that it makes several independently-developed
documents in this branch read as one subject. The reason not to believe it yet is
below.

---

## 4. Where it breaks

### 4.1 The NM/thermodynamics divide sorts descriptions, not objects

A steel block has an entropy and a temperature. Thermodynamics applies happily to
trackable things. And continuum mechanics - Navier-Stokes - handles water while being
mechanics, not thermodynamics: it abandons particle identity and keeps mechanical
description via fields. So the divide is not a partition of the world's stuff into
NM-stuff and thermo-stuff. At best it is a claim about which description pays, given
where your modelling interval falls relative to the horizon.

### 4.2 Fluids are not untrackable

Lagrangian fluid mechanics follows material parcels, and does so successfully. The
honest statement is that parcel identity DECAYS under diffusion and mixing - trackable
over short intervals, not over long ones. Which means the binary claim in 2.1 as first
stated is false, and only the horizon version survives. That is a repair, but it is a
repair to the piece that starts the whole cluster.

### 4.3 N! is combinatorics; trackability decay is physics

The conjecture at 2.11 needs a quantity - bits of *usable* distinguishability - that
is well defined, interval-dependent, and runs to log N! in the limit. No such quantity
is defined here. N! counts permutations of labels. Trackability decay is a physical
process of re-identification failing. There is no argument yet that one interpolates
to the other, and it is entirely possible that they do not.

### 4.4 The Gibbs paradox may not be ontological at all

The reading in `newton_vs_gibbs` treats the N! correction as classical physics
admitting a fact about the world. There is a long-standing alternative - Jaynes is the
usual reference - on which the N! is about which macrostates the experimenter can
distinguish and control, making entropy observer-relative rather than a count of what
the world contains. If that reading is right, the "ontological incompatibility"
softens into a statement about descriptions, and the bridge to trackability changes
character completely: it would be a connection between two epistemic notions, which is
far less interesting than a connection between an epistemic and an ontic one.

This is the objection most likely to dissolve the whole cluster and it has not been
addressed.

### 4.5 The pieces may be one idea counted several times

2.4, 2.6 and 2.7 could be three views of a single fact about continuum description.
Convergence between them is then not evidence, it is bookkeeping.

### 4.6 Liquids are not gases

The coherent/incoherent decomposition - tracer reports the coherent part of molecular
motion, thermodynamics bookkeeps the incoherent part - is clean for gases, where mean
free path is a real quantity. In liquids it is a fudge. Half the examples in this
record are water.

---

## 5. What would decide it

```text
Define, or show one cannot define, a bits-of-usable-distinguishability quantity
that is interval-indexed and tends to log N! as the interval outruns the horizon.
                                                                        -> settles 4.3

Settle whether the N! correction is read ontically or epistemically here,
before any further weight is put on newton_vs_gibbs.                    -> settles 4.4

State the condition under which the material derivative's Eulerian/Lagrangian
identification holds, and check it against the tracer window.           -> tests 2.6

Check the phase prediction at 2.10 against a phase entry when one is written.
A phase that turns up in a target slot falsifies it.                    -> tests 2.10

Find a case where exchange-identity and trackability come apart in a way that
MATTERS to a trace, not just in principle.                              -> tests 1
```

---

## 6. Provenance and standing

Assembled 2026-08-26 from a working session. The trackability sorting, the fluid
two-sidedness, the observation about the unspecified limit, and the phases/pressure/
volume conjecture are the user's. The tracer window's two edges and their dimensionless
numbers, the Eulerian/Lagrangian identification, the volume repair, the bosons/fermions
material, the exclusion knot at 2.9 and the binary/graded mismatch at 2.11 were
developed by Claude in conversation and have not been independently checked.

This record is TERMINAL as what it is - a record of a suspicion and its parts. It is
not a draft of anything and no direction is declared for it. If the cluster is ever
resolved, the resolution supersedes this; if it dissolves, this stands as the record of
why it looked promising.

It sits outside `scene_trackability`'s jurisdiction by design: that note stops at the
line where tracks stop being available, and everything from 2.8 onward is past it.
