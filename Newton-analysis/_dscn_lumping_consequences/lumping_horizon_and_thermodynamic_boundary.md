# The Lumping Horizon: Why Thermodynamic Motion Cannot Be Lumped

**Status:** record, v1
**Project:** VD Newton-analysis
**Date:** 2026-08-26
**Position:** stands between the trackability material and the lumping material. Sits
alongside `identifiability_and_fluid_representation_discovery.md` in this discussion
and deliberately has the opposite character: that document is a scatter of pieces
held apart on purpose, this one is a single argument.
**Audience:** VD-literate; assumes the redundancy criterion of
`vd_trackability_scene_to_particles_d4.md` section 3.

---

## 0. The claim

Track each point of a fluid on its own and you find their tracks are random walks.
That places an upper limit on lumping them. Thermodynamic effects therefore cannot be
lumped, and the separation of thermodynamics from Newtonian mechanics follows from
the lumping criterion rather than being imposed on it.

The rest of this record does three things: makes the limit quantitative, shows the
failure is of a different kind from the two already recorded, and states the one
refinement without which the claim is false.

---

## 1. The bound

The criterion in hand:

```text
kinematic redundancy :=
tracks r_i(t), r_j(t) are redundant over the modelling interval, within the
working tolerance, when r_i(t) - r_j(t) is constant to within the tolerance.
```

Apply it to diffusive tracks. The difference of two independent random walks is
itself a random walk, so the separation does not stay constant - its mean square
grows without bound:

```text
<|r_i - r_j|^2>  =  4 D t          (D the diffusivity)
```

Setting the rms separation equal to the working tolerance e gives the interval past
which the two tracks are no longer redundant:

```text
t_max  ~  e^2 / D
```

**Lumping is licensed below this horizon and refused above it.** No new machinery was
needed: the bound falls out of the existing criterion the moment diffusive tracks are
fed to it.

Two immediate consequences.

**Stirring makes it worse, not better.** In the inertial range of a turbulent flow,
Richardson dispersion has pair separation growing like t^3 rather than t. A stirred
fluid defeats lumping faster than a still one.

**The horizon is set by temperature.** For a sphere of radius a in a medium of
viscosity eta, the Stokes-Einstein relation gives D = kT / (6 pi eta a), so

```text
t_max  ~  e^2 * 6 pi eta a / (k T)
```

The parameter that defeats lumping IS the temperature. Cold makes the horizon recede;
as T goes to zero it diverges and everything becomes lumpable again. The link between
lumping failure and thermodynamics is therefore not an analogy - it is the same
parameter appearing in both ledgers.

---

## 2. A third failure mode, and the only one that is irreducible

Two ways of failing redundancy are already recorded. This is a third, and it differs
in kind rather than degree.

```text
SHEAR       the tap: parcels on one vertical line have a systematic velocity
            difference, so separation grows linearly. C1's remedy: re-partition,
            lump slab-wise, accept an ordered chain of particles.
            -> defeats A lumping. Repairable by choosing a different decomposition.

ROTATION    the spinning wheel: fixed mutual distances, non-redundant tracks, rim
            points differing in velocity at every instant. Remedy: stage the
            definition - redundancy, not distance-rigidity, is the primitive.
            -> defeats A lumping. Repairable by fixing the criterion.

DIFFUSION   free thermal motion: separation grows like sqrt(t) with no restoring
            force. No remedy.
            -> defeats LUMPING AS SUCH.
```

The distinction is the substance of the claim. Shear and rotation defeat a particular
choice of bundle, and both were in fact repaired by re-choosing. Diffusion cannot be
re-chosen around, because the growth is not an artifact of the partition - it is a
property of the material. Any partition you pick disperses at the same rate.

That is the sense in which thermodynamic effects "cannot be lumped": not that lumping
them gives a poor answer, but that no decomposition exists for which the licence holds
over an unbounded interval.

---

## 3. The refinement without which the claim is false: bounded, not thermal

Stated as "thermal motion defeats lumping" the claim is wrong, and the counterexample
is immediate: a steel block has a temperature, its atoms are in constant thermal
motion, and we lump it without hesitation. If thermal motion defeated lumping, no
solid body could be a Newton II target.

The correct statement is **unbounded**, not thermal.

```text
SOLID       thermal displacement about a lattice site, restoring force present.
            Equipartition gives <u^2> ~ kT / (m w^2): the mean square SATURATES.
            Track separation fluctuates and does not drift. Redundancy survives.
            -> lumpable AND thermal, no contradiction.

FLUID       no restoring force, free walk, <|dr|^2> = 4Dt: unbounded.
            Redundancy expires at t_max.
            -> not lumpable beyond the horizon.
```

So thermodynamics does not sort objects into lumpable and unlumpable; **boundedness
does.** A steel block is simultaneously a Newtonian target and a thermodynamic object
precisely because its thermal motion is confined, and this is why the divide never
looked like a clean partition of the world's stuff.

**The two failure regimes map onto the criterion's two indices.** Redundancy is
indexed by tolerance and by interval. A solid fails on TOLERANCE - if kT/(m w^2)
exceeds e^2, the vibration is too large to lump at that tolerance, whatever interval
you use. A fluid fails on INTERVAL - it lumps at any tolerance for long enough, and
at no tolerance forever. The criterion already carried both indices; the two kinds of
thermal motion use one each.

**Suggestive, and not checked here:** solid-state physics locates melting by the
Lindemann criterion - rms vibration reaching roughly a tenth of the interatomic
spacing. That is a tolerance condition on lattice-site retention. If the above is
right, melting is the point at which bounded vibration becomes unbounded diffusion,
which is the point at which lumping's licence changes from tolerance-limited to
interval-limited. That would make a phase transition a change in the character of the
lumping licence. Recorded as a lead, not a result.

---

## 4. Where the divide actually sits

This relocates the boundary by one stage, and the relocation is the reason the record
exists.

```text
STAGE 1  can a track be had at all?
         Fluid points: YES. They are individually trackable. Lagrangian fluid
         mechanics follows parcels and is not making a mistake.

STAGE 2  can those tracks be lumped into one target with a count?
         Fluid points: ONLY BELOW t_max. This is where it fails.
```

The trackable/non-trackable framing put the failure at stage 1, which was always
awkward: the objection that Lagrangian mechanics tracks parcels perfectly well had no
good answer. On this account the objection is simply granted. Fluid points pass stage
1. What they cannot do is supply a bundle whose redundancy survives the interval, and
a target requires a bundle.

The consequence for the two notes is structural rather than editorial. The
trackability note and the lumping note are not merely adjacent stages of one chain:
the boundary this record describes falls exactly between them, so each note sits on
one side of it. Neither note owns this document. It states where their shared edge is.

---

## 5. What this does not establish

**It does not partition the world into NM-objects and thermo-objects.** Section 3
shows why: the same steel block is both. What the horizon sorts is whether a given
material supports a lumping licence over a given interval at a given tolerance -
three arguments, not one.

**It does not cover equilibrium thermodynamics.** The mechanism here is transport and
fluctuation - diffusion, dispersion, vibration amplitude. The state-function side of
thermodynamics (entropy of a static body, equations of state) is not obviously a
matter of tracks failing to lump, and nothing above reaches it.

**It does not establish the identification with the Gibbs material.** Whether the
lumping horizon has anything to do with the log N! distinguishability disagreement in
`newton_vs_gibbs` is open, and is the subject of the discovery record next to this
one, not of this one.

**The claim of novelty needs narrowing.** That diffusion destroys parcel identity, and
that solids vibrate while fluids wander, are standard. What is not standard is a
formalism in which "may I treat this as one object" is a stated licensing condition
carrying a tolerance and an interval, so that the NM/thermodynamics boundary comes out
as a licence expiring rather than as a modelling convention adopted after the fact.
Narrowed that way the contribution stands. Unnarrowed it invites an easy dismissal.

---

## 6. Provenance

The observation is the user's: that individually tracked fluid points execute random
walks, that this places an upper limit on lumping them, and that thermodynamics is
therefore separated from Newtonian mechanics by the lumping criterion itself.

Developed by Claude in the same conversation and NOT independently checked: the bound
t_max ~ e^2/D and its temperature dependence via Stokes-Einstein; the three-failure-
mode taxonomy and the repairable/irreducible distinction; the bounded-versus-thermal
refinement in section 3 and the steel-block case; the mapping of the two regimes onto
the criterion's two indices; the Lindemann lead.

Terminal. No direction; no draft number. Where the notes later draw on it they take
informing copies - nothing here is a draft of either.
