# From Scene to Particles: Trackability, Redundancy, and the Lumping Criterion

**Status:** design note, v1
**Project:** VD Newton / NML1 → NML2 hinge
**Date:** 2026-07-03
**Supersedes:** `trackability_bodies_and_rigid_bodies.md`,
`tracks_to_particles_rigidity_as_lumping_criterion.md`,
`vd_tracks_to_particles_corrections.md`. Where this note contradicts
them, this note wins; they should no longer be consulted.
**Position:** read before `vd_mass_identification_pipeline.md`. This note
owns the territory of the pipeline's Stages 0–2 and supplies the
provenance of the wall inputs the pipeline consumes.
**Audience:** VD-literate; adjacent notes (pipeline, two-method
structure, actually-there taxonomy) assumed. NML2 inclusion is
deliberately unresolved — every section is a candidate; the cut is a
later editorial pass.

---

## 0. The ground

One fact stands under the entire trajectory formalism: **the material of
the world is trackable.** Points of the scene can be re-identified
through time. This is not a result of Newtonian mechanics; it is the
precondition that lets Newtonian mechanics describe anything. Every
`r(t)` ever written for something physical silently cashes it — it is
the trajectory *of* something only because some point was followable
from one moment to the next. Strip trackability away and you do not get
worse mechanics; you get no mechanics.

```text
trackability :=
selected points of the scene can be re-identified through time,
each generating a track.
```

Note the phrasing: points *of the scene*, not "on a body." The
superseded notes' central sentence — "a body supplies a family of
tracks" — is retired, and retiring it is this note's first correction.
At this stage there are no bodies. Bodies are outputs (§4).

Two registers, kept distinct:

```text
the material   ontological register: what is there, prior to any
               description
the scene      observational register: the material as presented to
               tracking — in the model of §1, the video
```

"Scene" is chosen to avoid collision with `mechanical-system` (E39),
which is post-lumping — an observer-selected subset of already-existing
particles. The scene is pre-ontology.

**Domain gate.** Newtonian mechanics applies to what tracks. The gate's
failure point is the quantum boundary: identical-particle statistics is
re-identification failing in principle, not in practice.

**Frame bracket.** The co-inertial problem is bracketed: assume it
magically resolved, so the frame in which the scene is presented is
*the* inertial frame, not a seemingly-inertial one. §3 shows the bracket
is cheap for this note's purposes — nothing below depends on *which*
inertial frame — and why it would not be cheap for a rotating one.

**Seeding.** Deciding *which* points to follow is a human act at the
residual layer, and is treated as such throughout. It is never smuggled
into the machinery.

---

## 1. The tracker

The working model of trackability, stated as a procedure so that its
grades are visible:

```text
tracker :=
a procedure taking (video, seed point on frame 0) and returning the
seed's position on every subsequent frame — a track.
```

Think of a neural network pointing at "the same point" frame after
frame. Nothing downstream depends on the implementation; everything
depends on the interface and its reliability grade.

```text
track :=
a time-indexed curve — never a bare path. Two tracks tracing the same
path at different times are different tracks. r(t) is the track's
mathematical carrier.
```

Four properties of the tracker do all the downstream work.

**Finite but densifiable.** Any run yields finitely many tracks — one
per seed. But the video persists, so the procedure re-runs at will: new
seeds, any past interval, retrodictively. The family in hand is a
finite, human-chosen proxy for an in-principle continuum, *with a
standing capacity to densify on demand*. This capacity upgrades several
downstream claims from faith to audit (§2, §4).

**Somewhat reliable — the tolerance floor.** Re-identification is
noisy, and the noise level bounds working tolerance from below: beneath
the floor, "these two tracks keep a fixed offset" is not a claim the
procedure can support. Tolerance therefore has two sources:

```text
from above: the modelling question   (what differences matter)
from below: the procedure            (what differences are resolvable)
```

A tolerance below the floor is not strict; it is meaningless.

**Proxy, not account.** The tracker is itself the already-logged
account/proxy instance for re-identification: what it *matches* is
features (the proxy); what re-identification *means* is dynamical
continuity of material (the account). The proxy's known failure modes —
occlusion, crossings with identity swap, featureless surfaces — are
exactly where "somewhat" lives.

**Residual placement.** Video, seeds, runs, tolerance: all of it lives
at the residual layer. None of it is encoded in entries, and none of it
should be. Its role is to stand behind wall inputs. When a human writes
"inertial-mass of this point-particle" into a trace, *this* is where the
point-particle came from. This note is the provenance dossier for those
inputs.

---

## 2. Coverage: two residues of different grades

The family in hand carries one license with no address yet:
**coverage** — the non-rigorous judgment that the human noticed and
supplied enough tracks to be representative of the scene. Under the
tracker model it splits into two residues of different grades:

```text
seeding residue      did we follow enough points?
                     DISCHARGEABLE. The video persists: re-run with new
                     seeds over any past interval. Failure is visible —
                     densification that changes the bundle count (§4)
                     convicts the old seeding. Not faith; a standing
                     audit.

resolution residue   is there material transport below what the video
                     resolves? (evaporation, ablation, sub-pixel flow)
                     PERMANENT. Densifying seeds adds tracks, not
                     resolution; checking indefinitely never upgrades
                     the grade.
```

The genuine probably-no input is the resolution residue alone, plus
trust in the procedure itself (§1). This explains, rather than merely
matches, the tolerance-scoping of the persistence certificate
downstream: the certificate inherits exactly the resolution residue and
no more.

---

## 3. The primitive: kinematic redundancy

```text
kinematic redundancy :=
tracks r_i(t), r_j(t) are redundant over the modelling interval,
within the working tolerance, when r_i(t) − r_j(t) is constant to
within the tolerance — the tracks differ by a fixed offset.
```

Redundant tracks share a velocity field; either member reports the
motion of both. The definition compares trajectories, never paths.

**Redundancy, not rigidity, is the primitive.** Redundancy implies
fixed mutual distances; the converse fails. Fixed distances permit
rotation, and a rotating bundle's tracks are not redundant — rim points
of a spinning wheel differ in velocity at every instant, so no one
track can stand for all. Distance-rigidity as a criterion
*over-licenses*: it lumps the wheel and silently discards the spin.

**Rigidity, staged.** The word survives, with its scope fixed:

```text
rigidity (track sense, staged) :=
the zero-tolerance limit of redundancy — exact rigid TRANSLATION,
a proper subset of rigid motion.
```

Rotating and deforming rigid bodies are non-translating cases,
deliberately not litigated here; they enter when rotation enters the
sequence. The student-facing word may remain "rigid" if wanted; the
definition underneath is redundancy.

**Galilean invariance.** A constant offset vector is preserved by
Galilean transformations, so redundancy — and everything built on it:
bundles, counts, lumping — is indifferent to which inertial frame shot
the video. This is why §0's bracket is cheap here. It would not be
cheap for a rotating frame: a rigidly rotating platform's points are
redundant in the co-rotating frame and not in an inertial one. The
frame-dependence belongs to the frame problem, which is exactly where
the bracket sits.

---

## 4. Lumping: bodies as outputs

```text
bundle :=
a maximal set of tracks, pairwise redundant over the interval at the
working tolerance.

lumping :=
represent a bundle by one track; the representative is one particle.
```

**The direction of explanation is the reverse of the superseded
notes'.** Old: "a body supplies tracks — how many should we use to
describe it?" Ill-posed: there is no *it* before lumping. New: the
human supplies tracks from the scene; bundles fall out of (family,
tolerance); each bundle is a particle. **The count of bodies is an
output**, not a modelling decision about a given object. No sub-family
concept is needed anywhere: tolerance *is* the mechanism that separates
one family into bundles.

The vocabulary, with its licensed re-entry points:

```text
bundle     the maximal pairwise-redundant track set
body       the material the bundle follows — the word "body" is first
           licensed HERE, as an output of lumping
particle   the bundle's representative — a mathematical track-carrier,
           not a miniature body
```

What the lump fixes:

```text
the target        this bundle, as one particle
the count         how many bundles the scene contains
the mass ADDRESS  a slot now exists for a value to bind to (§8)
```

**The computable residual core.** Given (family, tolerance, proposed
bundling), all-pairs redundancy is checkable by computation —
mathematics over track data. This is *not* the VD's mechanical layer,
which audits entries; no entry is touched. The residual layer has
internal structure:

```text
computable core   redundancy audit; count extraction;
                  densification-stability check
human residues    seeding, tolerance choice, clique-pick (§5),
                  trust in the tracker
```

The verify/generate split recurs here, one level inside the residual
layer: the core verifies a bundling; it cannot generate the human
residues.

**Count stability under densification.** For the count to be a property
of the scene rather than of the seeding, new seeds must land in
existing bundles. That is the audit that discharges the seeding residue
(§2): densify; if the count moves, the old seeding is convicted; if it
holds, the count is certified at this tolerance (modulo the boundary
conventions of §5).

**Two licenses, separated.** Lumping licenses the **proxy**: any member
track may be read in place of the representative, because the tracks
are informationally interchangeable. It does not license the
**account** — the mass-weighted single-track Newton-II ledger
(F_ext = M·a_cm), which exists for *any* body, redundant or not, as a
theorem whose ingredients (superposition, weak NIII) sit at NML3
addresses. The separating examples run in both directions:

```text
spinning wheel   account valid, proxy invalid (rim track ≠ CoM track)
convoy           proxy valid over the interval, no cohesion behind it
                 (§7)
```

And the corrected place of the centre of mass: it is not *selected
from* the family — usually it is not a material point at all (hollow
ring: the CoM sits in empty space). It is *constructed* from the
family, mass-weighted, its trackability derivative. Bookkeeping over
material points: a tenant of trackability, not its foundation. At this
note's address it cannot even be constructed — no masses exist yet — so
it is named only to fix its future position.

---

## 5. Cliques, and what replaces the circularity claim

Redundancy-within-tolerance is not transitive: tolerances compound.
Maximal pairwise-redundant sets are **cliques**, not equivalence
classes; cliques can overlap; admissible bundlings can be non-unique.
At zero tolerance redundancy *is* transitive — fixed offsets compose —
so this is a tolerance artifact; it cannot be removed, because
tolerance is load-bearing everywhere above.

The **clique-pick** — choosing among admissible bundlings — is a human
residue. The tap (§6) makes it concrete: a continuous velocity gradient
admits sliding-window slab decompositions; the count is stable, the
boundaries conventional.

**Retraction.** The corrections note (C5) claimed the lumping
identification is unauditable in principle — "the audit presupposes the
ontology the lumping establishes" — and on that basis nominated lumping
as the second instance of the Newton-I pattern, with a provenance claim
attached. Under the tracker model the circularity claim is false: the
redundancy audit runs on tracks and tolerance, *pre*-ontology; particles
are its output, not its input. What is genuinely beyond audit
decomposes into four residues:

```text
1. trust in the tracker    proxy fidelity                        (§1)
2. tolerance choice        floored below, question-set above     (§1)
3. clique-pick             among admissible bundlings            (§5)
4. resolution residue      the permanent probably-no             (§2)
```

C5's wording is retracted; the provenance claim is dropped with it. The
four-residue decomposition is what the pipeline's wall inputs actually
rest on.

---

## 6. The ladder: one, ordered many, disordered many

Three scenes, one criterion. Tracks carry no mass anywhere in this
section.

**Block (one).** A thrown block. Seed it anywhere; every track differs
from every other by a fixed offset for the whole flight. One bundle,
one particle. Densify at will; the count holds. The maximal-compression
case.

**Tap (ordered many).** A steady stream from a tap. Two parcels on the
same vertical line: the lower left the tap earlier, so at any instant
it is faster; both accelerate at g; their separation grows linearly.
Visible signature: the stream narrows as it falls. So the whole stream
fails redundancy at first order over any interval — the tap is *not*
one bundle. Lumping applies slab-wise: within a thin slab dh, tracks
share the velocity field and differ by fixed transverse offsets; across
slabs, redundancy fails. The criterion returns an ordered chain of
particles, one per slab.

Two caveats, both load-bearing:

```text
(i)  even a slab is not strictly redundant: vertical strain rate
     ≈ g/v, and incompressibility forces transverse contraction at
     the same order. Slab lumping closes only under tolerance.
(ii) slab boundaries are conventional: the velocity gradient is
     continuous, so admissible slabbings overlap (§5). The count
     (≈ height/dh, with dh set by the tolerance) is stable; the
     partition is a clique-pick.
```

The tap is where infinity is spent, in two instalments: seeding takes
the continuum of material to a finite family; tolerance takes the
family to a finite count that is *stable under densification* — which
is what entitles the count to be called a property of the scene. This
is not an approximation concession: without tolerance, no finite count
is well-defined at all.

**Splatter (disordered many).** The stream hits the floor and scatters.
Tracks that flew left no longer keep fixed offsets to tracks that flew
right; the incoming chain breaks into bundles with no ordering. Several
particles, counted the same way. The splash converts few into many
because it is the event that breaks bundles.

The rhetoric throughout is deliberately weaker than "read off the
tracks": the tracks **constrain and certify** the count; tolerance and
clique-pick are supplied; the count is then computable.

---

## 7. Defeat: retrospective, defeasible, graded

Redundancy is certified over an *observed* interval — retrospective —
and says nothing about cohesion. The criterion cannot distinguish
constraint (co-movement enforced by internal forces) from coincidence
(co-movement that happens to hold). Both defects are stated, not
hidden. The dynamical notion of unit-hood — what responds to force as
one — has a later address, once force accounting exists. This note owns
the kinematic notion, honestly labelled, and the defeat taxonomy:

```text
block into wall   break stays below tolerance (elastic waves, sub-ε)
                  -> no defeat; one certificate spans the impact
bouncy ball       break exceeds tolerance during contact, then heals
                  -> temporary defeat: fission–fusion (below)
splatter          break is permanent
                  -> defeat; re-lump; the normal revision cycle
convoy            no break during the interval — and no cohesion either
                  -> over-lumping, exposed only when one car brakes;
                     the coincidence case
```

**The bounce at two tolerances.** One event, two bookkeepings.

*Loose tolerance.* The contact deformation never exceeds ε. No defeat;
the ball is one bundle throughout; one mass address with one validity
interval spanning the bounce. The address is **certificate-carried**:
directly usable at every moment.

*Strict tolerance.* During contact the offsets move by more than ε —
redundancy breaks. But the velocity field is continuous, so small
neighbourhoods stay internally redundant: the ball does not dissolve;
it **fissions** into micro-lumps (slab-style; count blowing up as ε
shrinks), then **fuses** back into one bundle after contact. The
original address dies at contact; N micro-addresses with undetermined
values exist during; a fresh address is created after.

The value nonetheless survives, because this defeat has a signature the
certificate taxonomy must name:

```text
no-offshoot break :=
redundancy fails while every track remains in the family — nothing
departs. Third certificate case, alongside persistence (no break, no
offshoot) and expiry (offshoot observed).
```

Mass-locality says mass changes only by material departure; full track
accounting says nothing departed; so the post-fusion address is pinned
to the pre-fission value. The address is **bridge-reconstructed**: same
number, more machinery, and no usable address *during* the episode.
That is the honest grading — cheap at loose tolerance, reconstructive
at strict, never lost.

The C8 partition residue is **inert under fission–fusion**: the
micro-lump partition is never determined and never needed — only the
sum is consumed at re-fusion. The residue bites only when fragments are
*separately* consumed by Route B (splatter droplets, individually
predicted), which is exactly where the pipeline books it.

Tolerance-invariant through all of this: the account. F_ext = M·a_cm
holds through the contact on either bookkeeping (license address NML3;
named here only as the invariant the two readings share). Warping
breaks the proxy, never the account.

---

## 8. Mass: address only

This note assigns no mass. What lumping creates is the **address**:

```text
lumping fixes the referent — WHICH thing owns a mass slot.
what is in the slot is determined by nothing in this note.
```

Value origination is dynamics (Wall 2, tolerance-true); escort is the
persistence certificate — whose observable content, the absence of
offshoots, is pure track-talk, but whose bill includes mass-locality,
priced downstream; assembly is restricted additivity-(B). All pipeline
territory. The superseded claim that the lumping criterion "answers
both questions at once" — count and mass — is dead: the two questions
have different criteria of different kinds at different addresses.

What this note *can* grade is the address itself, from §7:

```text
certificate-carried    block; loose-ε bounce
                       usable at every t
bridge-reconstructed   strict-ε bounce
                       usable before and after, not during
re-originated          splatter fragments
                       sum pinned by the conservation theorem;
                       per-fragment values await instruments
                       (the open C8 residue)
```

Everything in this note is past-facing — observation feeding the
forceful method only at its past boundary. Route B consumes the bound
address; it never consults the scene again.

---

## 9. Compact summary

```text
Ground:      the material of the world is trackable — the domain gate.
             Bodies are not given; the scene is. Frame bracketed.

Tracker:     (video, seed) -> track. Finite family, densifiable on
             demand (the video persists); noisy, so tolerance is
             floored from below; feature-matching proxy for a
             continuity account. All residual: the provenance dossier
             for wall inputs.

Coverage:    seeding residue dischargeable (densify and watch the
             count); resolution residue permanent — the one genuine
             probably-no.

Redundancy:  fixed offset within tolerance over the interval;
             trajectory-not-path; Galilean-invariant. Implies fixed
             distances, converse fails (spinning wheel). Rigidity =
             zero-tolerance translation; non-translating cases parked.

Lumping:     bundles = maximal pairwise-redundant cliques; bodies,
             particles, and the count are OUTPUTS of (family,
             tolerance, clique-pick). Computable core inside the
             residual layer; four human residues: tracker-trust,
             tolerance, clique-pick, resolution. C5's circularity
             claim retracted.

Licenses:    lumping licenses the proxy; the account (CoM ledger) is a
             later theorem; the CoM is constructed, never selected.

Ladder:      block (one) -> tap (ordered many; slab-wise; infinity
             spent in two instalments) -> splatter (disordered many).

Defeat:      retrospective, defeasible, graded — sub-tolerance (block),
             temporary fission–fusion (ball; no-offshoot break; value
             bridge-reconstructed; C8 inert), permanent (splatter),
             coincidence (convoy).

Mass:        address only, usability graded: certificate-carried /
             bridge-reconstructed / re-originated. Values, escort,
             assembly: the pipeline note.
```

---

## Downstream edits owed (not performed here)

```text
pipeline Stage 1   "coverage" -> seeding/resolution split; the
                   probably-no is resolution + tracker-trust only
pipeline Stage 2   "a human identifies a sub-family as redundant" ->
                   human supplies family + tolerance; bundles fall
                   out; the remaining human act is the clique-pick.
                   Drop "sub-family".
pipeline Stage 4   certificate taxonomy gains the no-offshoot break
                   as third case; validity-interval machinery gains
                   the fission–fusion bridge
pipeline §7        the single "lumping" human input decomposes into
                   the four residues of §5 where cited
```
