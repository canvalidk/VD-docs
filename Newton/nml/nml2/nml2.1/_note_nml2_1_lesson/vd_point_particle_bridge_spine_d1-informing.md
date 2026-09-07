> **Informing copy — do not edit here.**
> **Home note:** `point_particle_bridge_spine`, draft `d1` — `Newton-analysis/point_particle_bridge_spine/vd_point_particle_bridge_spine_d1.md`.
> Placed in `nml2.1` (informs `nml2_1_lesson`): Wall 2, deuteron, and the (A)/(B) split behind the three-masses lecture. This is a read-only copy; refresh from the home note if the source changes.

---

# The Point-Particle Bridge: Spine Note

**Status:** orientation note, v1
**Project:** VD Newton / NML1 → NML2
**Role:** the single chain that every current note annotates. Contains nothing
new; exists so the dependencies do not have to be held in the head at once.

---

## The chain

```text
GROUND (precondition, not physics):
  material points can be re-identified through time -> tracks exist

WALL 1 (human input, defeasible):
  lumping — tracks judged redundant within tolerance
  -> one target exists, with a count

DERIVATION (exact bookkeeping, no physical law of composition):
  shared acceleration A  +  per-part Newton II  +  adequacy (B)
  -> M = Σ mᵢ   and   the CoM as the carrier point

WALL 2 (human input, empirical, tolerance-true only):
  ledger mass ≡ measured mass

PERIMETER:
  the bridge is legal exactly while the net-force slot holds ONE value

LATER ADDRESSES (walled, not yet opened):
  force-sum (A)  ·  weak NIII (⟺ compositional B)  ·  strong NIII  ·
  gravitational-inertial equivalence
```

One sentence: **the entire point-particle bridge is built from kinematics plus
bookkeeping — no physical composition law is used anywhere in it.**

---

## The segments

**Ground — trackability.** Bodies supply families of re-identifiable
point-tracks. This is what every `r(t)` silently cashes. Not a result of
mechanics; the precondition for mechanics describing anything.

**Wall 1 — lumping.** A human judges a family of tracks redundant: the tracks
differ by a fixed offset, within the modelling tolerance, over the modelling
interval. This fixes the particle *count*. It is retrospective and defeasible
(the convoy lumps until one car brakes; the splatter is the canonical defeat).
The tolerance comes from the modelling question, not from the tracks — so the
identification lands at a wall. The trace can verify a proposed lumping; it
cannot generate or audit it. Same pattern as the Newton-I frame bootstrap.

**Derivation — additive mass and the CoM.** Given parts with masses mᵢ sharing
one acceleration A: each part's Newton-II account demands mᵢA; the one-point
representative must cover all part demands — adequacy, additivity type (B) —
so MA = Σ mᵢA, hence M = Σ mᵢ; the same weights then place the carrier at the
mass-weighted point, the CoM. This segment is *exact*. It never decomposes any
force into attached contributions, so it never traverses force-sum (A), never
touches Newton III, and is therefore legal inside NML2.

The two additivities, kept apart:

```text
(A) force-sum:    attached forces on ONE target -> that target's net-force.
                  Physical composition. E14+, NML3.

(B) adequacy:     net-force ACCOUNTS of part-targets aggregate to the
                  composite's account under lumping. Bookkeeping about what
                  "representative" means. This segment. NML2.
```

Standard notation writes both as ΣF; the VD keeps them as different edges
between different headwords.

**Wall 2 — mass measurement.** The derivation *propagates* mass; it does not
*originate* it. Somewhere a primitive lump gets its mass from an instrument,
and the identification of that measured number with the ledger number is
empirical and only tolerance-true (the deuteron's ledger mass exceeds its
measured mass by ~0.1%). Note: a weighing scale read as *inertial* mass also
traverses the ungranted equivalence edge; the NML2-internal measurement is
same-pull-same-time Δv comparison.

**Perimeter.** The moment two external agents act on the composite, filling the
single net-force slot requires composing their contributions — additivity (A) —
which is walled. So NML2's "one mass, one force, one motion-change" is not a
simplification for children; it is the exact region in which the bridge exists.

**Later addresses.** Force-sum (A) opens NML3. Compositional adequacy —
(B) holding for every sub-lumping — is interderivable with weak Newton III
given per-part NII and superposition, so at that house only one of the pair may
land as human input. Strong NIII (central pair-forces) is a further independent
postulate; translational bookkeeping can never yield it.

---

## Annotation map

```text
trackability_bodies_and_rigid_bodies.md   -> GROUND (+ first cut at Wall 1)
tracks_to_particles_..._lumping.md        -> WALL 1 (with corrections note)
from_rigidity_to_additive_mass.md         -> DERIVATION, mass half
from_fma_rigidity_to_com.md               -> DERIVATION, carrier half
NML2_working_note_core_constraints.md     -> PERIMETER, lesson-facing
```

Separating examples — each exists to keep two adjacent claims apart:

```text
spinning wheel   account holds, proxy fails      (mass-weighting ≠ redundancy)
convoy           proxy holds, no cohesion        (kinematics ≠ dynamics)
pushed rod       account share ≠ attached force  (B-distribution ≠ A-attachment)
deuteron         ledger mass ≠ measured mass     (derivation ≠ nature)
tap vs splatter  redundancy is interval-relative (lumping is defeasible)
```

Literature anchors: Mach (mass via mutual accelerations — NIII inside the mass
concept); Noll (force additive over parts as a separate axiom from composition
of concurrent forces — the (A)/(B) split, axiom-grade); Hestenes / Modeling
Instruction (particle-model construction as modelling choice — nearest
pedagogy, without the license table).

---

## The one open segment

**C8 — where do the mᵢ come from at a split?** The derivation presupposes part
masses; parts are themselves lumps; the regress must bottom out at Wall 2. At
the splatter, masses are being assigned to *new* bundles by conservation plus
partition-of-material before any bundle has met an instrument — a borrowing
with no license at that address. The droplet unease lives here. Open, parked,
and now located: it is a Wall-2 problem, not a Wall-1 problem.

---

## What to hold in the head

Two walls. One exact derivation between them. A perimeter that makes NML2's
scope a theorem rather than a choice. Everything else is annotation.
