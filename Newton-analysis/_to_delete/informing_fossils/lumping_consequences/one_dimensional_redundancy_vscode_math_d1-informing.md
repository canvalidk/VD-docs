> **Informing copy - do not edit here.**
> **Home:** the `particle_and_mass_origins` discussion - `Newton-analysis/_dscn_particle_and_mass_origins/one_dimensional_redundancy_vscode_math_d1.md`.
> **Placed in** `lumping_consequences` (user instruction, 2026-09-05) for what follows once projected bundles have been lumped: each bundle is a particle with its own mass ADDRESS and its own motion state (§5–§6), the stream is an ordered many rather than one target (§7), the stream is address-discrete whether or not it is spatially discontinuous (§8–§9), subdivision under a tighter tolerance does not make the coarser particle fictitious (§5), and the failure modes of the particle representation (§15).
> **Live here:** §5, §7–§9, §12.5, §13, §15–§16, §18, §20. **Not for this note:** §3–§4 and §19's criterion half (projection and the localisation test — `lumping_conditions`' business, where a copy also sits); §6's emission-time mass VALUES, §11 (`λ = dm/dh`) and §14 (Newton II for packets) — value territory this note hands off.
> **Caution:** §6 binds a mass value in the same breath as it creates the address. This note keeps the address half (a slot exists per projected particle, and `Dm/Dt = 0` while the address stays materially closed is an ADDRESS claim) and hands the value half off.
> This is a read-only copy; refresh from home if the source changes.

---

# One-Dimensional Redundancy and the Particle Description of a Fluid Stream

**Status:** conceptual working note  
**Project:** VD Newton / Newtonian Mechanics Pedagogy  
**Date:** 21 July 2026  

## 0. Thesis

A flowing fluid need not first be represented as one continuous massive object. A cleaner route is:

```text
material tracks
-> projection onto the dimension relevant to the task
-> local redundancy under tolerance
-> separately addressed material particles
-> an ordered stream of particles
-> optional continuum coarse-graining
```

Under this construction, each projected material particle has:

- a continuing material identity;
- a fixed mass address;
- its own one-dimensional position;
- its own one-dimensional velocity;
- and, when appropriate, its own acceleration and net-force account.

The ordinary continuous-stream description is then not the starting ontology. It is a compressed field description that becomes available when the separately addressed particles are sufficiently dense, smoothly ordered, and unresolved at the scale of the question.

The central claim is therefore:

> **One-dimensional projected redundancy licenses a fluid to be represented as an ordered, separately addressed stream of massive particles. Continuum density is a description of how those already-massive particles are distributed, not the process by which their masses first come into existence.**

A terminological warning is essential. “Discontinuous stream of particles” can mean two different things:

1. **Address-discontinuous:** the stream is represented by separately identified and separately mass-addressed material particles.
2. **Spatially discontinuous:** there are actual empty spatial gaps between material clusters, as in a spray of droplets.

One-dimensional redundancy is enough for the first claim. It does not by itself imply the second. Droplet breakup makes the address-discontinuous structure spatially conspicuous, but it is not required to create the particle description.

---

# 1. The modelling problem

Consider water leaving a hose. The usual description begins by treating the water as a continuous medium with fields such as

$$
\rho(\mathbf r,t),\qquad
\mathbf v(\mathbf r,t),\qquad
p(\mathbf r,t).
$$

For a narrow jet, this is often reduced to one-dimensional fields:

$$
\lambda(h,t)=\frac{dm}{dh},
\qquad
v(h,t),
$$

where $h$ measures distance along the direction of the stream.

This is mathematically useful, but it can hide a prior modelling question:

> What are the material targets whose mass, position, and velocity these fields describe?

If one begins with $\lambda=dm/dh$, it is easy to start speaking as though a small mass $dm$ is created anew from whatever spatial interval $dh$ happens to be selected. That produces an ambiguity:

- Is $dm$ the fixed mass of one continuing material target?
- Or is it the amount of water currently occupying a fixed laboratory interval?

These are not the same object.

The particle-first construction avoids this ambiguity. It identifies continuing material targets before introducing a density field.

---

# 2. Begin with trackability

Suppose the water is represented by material tracks

$$
\mathbf r_i(t)
=
\bigl(x_i(t),y_i(t),h_i(t)\bigr).
$$

A material track follows the same material through time. It is not a record of whatever water happens to occupy a fixed point in the laboratory.

Trackability gives many such tracks. It does not yet say how they should be grouped. The fluid may contain enormously many tracked points, and their full three-dimensional relative positions need not remain fixed.

The hose jet may:

- narrow;
- widen;
- shear;
- twist;
- stretch along its direction of travel;
- oscillate sideways;
- form necks;
- or break into droplets.

Therefore full three-dimensional rigidity is too strong for many fluid problems.

The next move is not to abandon particles. It is to ask whether the modelling task needs all three dimensions.

---

# 3. Project first

Suppose the task concerns transport along one direction, represented by the coordinate $h$. Apply the projection

$$
P_h:
\mathbf r_i(t)\mapsto h_i(t).
$$

After this projection, sideways structure has been intentionally omitted. Two material tracks that are far apart across the width of the jet may occupy approximately the same projected position and share approximately the same projected motion.

The projected description asks only:

```text
Where is this material along h?
How fast is it moving along h?
How is that motion changing?
```

It does not ask:

```text
What is its complete three-dimensional shape?
How far apart are all of its constituent points sideways?
Is the jet's cross-section circular?
```

This ordering matters:

```text
wrong order for the present construction:
choose a 3D slab
-> insist that it remains one slab
-> project it
-> struggle when it stretches

cleaner order:
project the tracks
-> test redundancy in the projected description
-> construct the 1D particles that the projected task requires
```

The projected particles are not merely shadows of previously fixed three-dimensional rigid bodies. They are material targets constructed at the level of the reduced description.

---

# 4. One-dimensional redundancy

Let $B_\alpha$ be a proposed bundle of material tracks. The bundle qualifies as one projected particle over a selected interval when its projected tracks remain sufficiently redundant under the tolerances of the task.

A useful finite-tolerance criterion is:

$$
\max_{i,j\in B_\alpha}
|h_i(t)-h_j(t)|
\leq \varepsilon_h,
$$

and, when one velocity is to represent the bundle,

$$
\max_{i,j\in B_\alpha}
|\dot h_i(t)-\dot h_j(t)|
\leq \varepsilon_v.
$$

The first condition says that the material in the bundle occupies one sufficiently small projected region.

The second says that the bundle has one sufficiently coherent projected velocity.

Under these conditions, the bundle may be assigned a representative projected track

$$
H_\alpha(t)
$$

and representative velocity

$$
V_\alpha(t)=\dot H_\alpha(t).
$$

The bundle is then represented as a normal one-dimensional material particle:

$$
P_\alpha
=
\bigl(
m_\alpha,
H_\alpha(t),
V_\alpha(t)
\bigr).
$$

This does not claim that the water inside $B_\alpha$ is perfectly rigid in three dimensions. It claims only that the omitted internal differences are beneath the tolerance relevant to the projected task.

The residual differences may include:

- sideways contraction;
- cross-sectional distortion;
- small velocity gradients;
- internal circulation;
- vibration;
- molecular motion.

Those differences remain real. They are simply not opened by the present description.

---

# 5. A particle is a redundant bundle, not an indivisible atom

The projected fluid particle should not be confused with a molecule or with a metaphysically indivisible piece of matter.

It is a modelling particle produced by lumping.

Its particle status means:

> The selected material tracks behave redundantly enough in the projected description that one position, velocity, and mass address can represent them for the present task.

This is scale-dependent. A bundle may qualify as one particle at a coarse tolerance and fail at a finer tolerance.

For example, a small water packet may satisfy

$$
|\dot h_i-\dot h_j|\leq \varepsilon_v
$$

for an introductory mechanics question. A detailed fluid-dynamics question may reduce $\varepsilon_v$ and reveal an internal velocity gradient. The previous particle must then be subdivided.

Subdivision does not show that the earlier particle was fictitious. It shows that it was a valid coarse target under a looser resolution.

The construction is therefore:

```text
redundant enough under current tolerance
-> one particle

not redundant enough under current tolerance
-> several finer particles
```

The particle boundary is a modelling boundary, but it is not arbitrary. It is controlled by the observed redundancy and the demanded resolution.

---

# 6. Each projected particle receives a mass address

Once a material bundle has been identified as one projected particle, a mass-determining process may bind a mass to it.

For a steady hose, one convenient labelling method is emission time. Let $P_\tau$ denote the water emitted during the interval

$$
[\tau,\tau+\Delta\tau].
$$

Its mass is

$$
m_\tau
=
\int_{\tau}^{\tau+\Delta\tau}
\dot m(s)\,ds.
$$

For constant mass-flow rate,

$$
m_\tau=\dot m\,\Delta\tau.
$$

This mass is attached to the continuing material packet, not to its current location. As long as the packet address continues to refer to the same material and no material crosses the selected packet boundary,

$$
\frac{D m_\tau}{Dt}=0.
$$

The packet may:

- accelerate;
- move farther from its neighbours;
- become longer in the projected direction;
- narrow sideways;
- become a droplet;
- or deform internally.

None of these facts alone changes its mass address.

Thus the particle should be written as

$$
P_\tau
=
\bigl(
m_\tau,
H_\tau(t),
V_\tau(t)
\bigr),
$$

with

$$
m_\tau=\text{constant}
$$

while

$$
H_\tau(t),\qquad V_\tau(t)
$$

may change.

This is the point at which the earlier $dm$ confusion is resolved:

> **The mass belongs to the material address. The position and velocity belong to the current state of that addressed material.**

---

# 7. The stream is an ordered many, not one redundant target

Different projected particles need not move redundantly with one another.

Indeed, a falling jet generally contains particles at different heights with different velocities:

$$
V_{\tau_1}(t)\neq V_{\tau_2}(t).
$$

Their separation therefore changes according to

$$
\frac{d}{dt}
\left(
H_{\tau_2}-H_{\tau_1}
\right)
=
V_{\tau_2}-V_{\tau_1}.
$$

Consequently, the whole stream should not be lumped into one particle merely because all of it is water.

The stream is instead an ordered family:

$$
\mathcal P(t)
=
\{P_\tau\}.
$$

For a finite-resolution model, one may use a sequence

$$
P_1,P_2,\ldots,P_N,\ldots
$$

with

$$
P_n
=
\bigl(
m_n,H_n(t),V_n(t)
\bigr).
$$

Each particle is internally redundant enough to be represented by one projected motion state.

The particles are not required to be mutually redundant. They are permitted to have:

- different positions;
- different velocities;
- different accelerations;
- different net forces;
- different neighbouring separations.

This is exactly what it means for them to be normal particles rather than components of one perfectly rigid body.

The conceptual structure is:

```text
redundancy within each particle
+
non-redundancy between particles
=
an ordered stream of independently moving masses
```

---

# 8. In what sense is the stream discontinuous?

The word **discontinuous** must be used carefully.

## 8.1 Address-discontinuity

At the modelling level, the stream is discontinuous because it is represented by separately addressable material targets:

$$
P_1,\ P_2,\ P_3,\ldots
$$

There is no single mass address for “the moving stream” that replaces all of these addresses.

Each particle has its own:

$$
m_n,\qquad H_n(t),\qquad V_n(t).
$$

This is a discontinuity of identity and bookkeeping. Moving from $P_n$ to $P_{n+1}$ means moving to a different material target.

That statement can remain true even when the material fills the spatial region between their representative positions.

## 8.2 Spatial discontinuity

A stronger claim is that there are empty intervals between particles:

$$
\text{water packet}
\;|\;
\text{air gap}
\;|\;
\text{water packet}.
$$

This happens clearly after the jet separates into droplets.

One-dimensional redundancy does not by itself establish these physical gaps. It establishes separate material addresses. Whether their occupied spatial supports touch, overlap under projection, or are separated by air is an additional geometric question.

Therefore the safest formulation is:

> **One-dimensional redundancy produces an address-discrete stream of material particles. In a droplet spray, that address discreteness is accompanied by spatially discontinuous support. In an unbroken jet, the addresses may remain distinct even while the occupied material support is connected.**

This distinction prevents the particle construction from depending on droplet breakup.

---

# 9. Droplets make the construction obvious, but do not create it

After a hose jet breaks into droplets, each droplet is an especially stable redundancy bundle.

For droplet $D_n$, its material points may have sideways and internal motion, but their projected translational motion can remain approximately common:

$$
|h_i-H_n|\leq \varepsilon_h,
\qquad
|\dot h_i-V_n|\leq \varepsilon_v.
$$

The droplet then receives the particle representation

$$
D_n
=
\bigl(
m_n,H_n(t),V_n(t)
\bigr).
$$

The spray becomes visibly:

```text
droplet particle
-> gap
-> droplet particle
-> gap
-> droplet particle
```

This is the easiest case because the material boundaries are physically conspicuous.

But the logical order is not:

```text
continuous water
-> breakup
-> particles begin to exist
```

It is:

```text
trackable material
-> projected redundancy classes
-> particles already available

then possibly:
connected support
-> necking and breakup
-> visibly separated particle clusters
```

Droplet formation changes the organisation of the particle stream. It does not supply the original right to represent material bundles as massive particles.

---

# 10. Why Rayleigh–Plateau instability is not foundational here

The Rayleigh–Plateau instability explains why a sufficiently long liquid column can develop necks and separate into droplets.

Under the present construction, that instability is not required to explain the existence of projected particles. The particles were already supplied by trackability, projection, redundancy, and mass addressing.

Its role is downstream:

```text
projected particles already exist
-> particles initially occupy connected liquid support
-> capillary disturbance grows
-> necks form
-> connected support fails
-> some particle bundles become spatially isolated droplets
```

The instability therefore explains a transition from

$$
\text{address-discrete but spatially connected}
$$

to

$$
\text{address-discrete and spatially separated}.
$$

This reverses the explanatory burden.

The question is no longer:

> How does apparently continuous water become particles?

It becomes:

> Under what conditions may an ordered many of massive particles be compressed into the appearance of one continuous stream, and under what conditions does that compression visibly fail?

---

# 11. The continuum description is derived from the particle stream

Let the projected particles be labelled continuously by emission time $\tau$:

$$
H=H(\tau,t).
$$

A small label interval $d\tau$ carries the fixed material mass

$$
dm=\dot m(\tau)\,d\tau.
$$

Neighbouring labels occupy the current projected separation

$$
dh
=
\left|
\frac{\partial H}{\partial\tau}
\right|d\tau.
$$

The current linear mass density is therefore

$$
\lambda(h,t)
=
\frac{dm}{dh}
=
\frac{\dot m(\tau)}
{
\left|
\partial H/\partial\tau
\right|
}.
$$

This formula should be read from left to right as:

```text
already identified material masses
divided by
their current spatial spacing
equals
mass per unit length
```

It should not be read as:

```text
choose a length
multiply by a density
thereby create a material mass with a new identity
```

For a steady one-dimensional stream, the material emitted at different times follows the same velocity profile shifted in time. Locally,

$$
\left|
\frac{\partial H}{\partial\tau}
\right|
=
v(h),
$$

so

$$
\lambda(h)
=
\frac{\dot m}{v(h)}.
$$

If the particles accelerate and move farther apart, $v(h)$ rises and $\lambda(h)$ falls.

The mass of each particle remains fixed:

$$
dm=\dot m\,d\tau.
$$

The changing quantity is the spacing:

$$
dh=v(h)\,d\tau.
$$

Thus:

```text
same mass per emitted packet
-> greater distance occupied by neighbouring packets
-> lower mass per unit height
```

No particle loses mass merely because the line density decreases.

---

# 12. What must be true for a continuum field to be a good compression?

The continuum picture does not require the particles to cease being separately addressable. It requires the distinctions between nearby particles to become unnecessary at the scale of the question.

Several conditions support this compression.

## 12.1 Dense coverage

Each observational interval $\Delta h_{\mathrm{obs}}$ should contain many projected particles:

$$
N(\Delta h_{\mathrm{obs}})\gg 1.
$$

Then individual particle-to-particle variations are not resolved.

## 12.2 Smooth variation

Neighbouring particles should have slowly varying masses and velocities:

$$
m_{n+1}-m_n
$$

and

$$
V_{n+1}-V_n
$$

should be small relative to the scale of the model.

This permits interpolation by fields such as

$$
\lambda(h,t)
\qquad\text{and}\qquad
v(h,t).
$$

## 12.3 Preserved ordering

For a simple one-dimensional stream, neighbouring material packets should remain consistently ordered. In a continuous label description, the map

$$
\tau\mapsto H(\tau,t)
$$

should remain locally invertible:

$$
\frac{\partial H}{\partial\tau}\neq 0.
$$

If multiple materially distinct packets become inseparably projected onto the same $h$ with different velocities, a single-valued field $v(h,t)$ may fail. The particle description can survive such a failure even when the simple continuum field cannot.

## 12.4 No resolved gaps, for the connected-stream picture

If the model specifically claims one connected jet, then at the selected resolution there should be no interval of visible air separating successive water supports.

This is stronger than the requirement for a particle stream. A particle stream may continue through gaps; a connected continuum stream may not.

## 12.5 Stable local lumping

Each representative particle must remain internally redundant within the current tolerances. If one packet develops a large internal velocity gradient, it must be subdivided before a reliable single-particle velocity can be assigned.

These conditions license:

$$
\{P_n\}
\quad\rightsquigarrow\quad
\lambda(h,t),v(h,t).
$$

The arrow is a coarse-graining operation, not an ontological conversion.

---

# 13. Two valid descriptions of the same hose jet

At an appropriate scale, the same water can be represented in two ways.

## Particle description

$$
P_n
=
\bigl(
m_n,H_n(t),V_n(t)
\bigr),
\qquad n=1,2,3,\ldots
$$

This description preserves:

- material identity;
- individual mass addresses;
- particle ordering;
- particle separation;
- individual velocities;
- possible particle-by-particle force accounting.

## Continuum description

$$
\lambda(h,t),\qquad
v(h,t).
$$

This description preserves:

- local mass per unit length;
- local average velocity;
- large-scale transport;
- smooth compression and expansion;
- field equations.

Neither description must be declared universally “the real one.”

The particle description is better when:

- identity through time matters;
- droplets or packets are separately visible;
- gaps appear;
- neighbouring velocities are not smoothly related;
- one wants to reuse fixed mass addresses;
- or one wants Newtonian equations for selected material lumps.

The continuum description is better when:

- individual packets are unresolved;
- many packets occupy every observational region;
- neighbouring states vary smoothly;
- and aggregate transport is the question.

The conceptual hierarchy proposed here is nevertheless asymmetric:

> The continuum field is constructed from the distribution of addressed particles. The particles are not first constructed by cutting a pre-existing density field into arbitrary pieces.

That asymmetry preserves the logic of mass addressing.

---

# 14. Newtonian mechanics for the projected particles

Once a projected bundle has a fixed mass address, it can enter ordinary Newtonian mechanics as a massive particle, provided the force-accounting approximation is adequate.

For particle $P_n$,

$$
m_n a_n
=
F_{\mathrm{net},n}^{(h)},
$$

where

$$
a_n=\dot V_n
$$

is its acceleration along the projected direction and

$$
F_{\mathrm{net},n}^{(h)}
$$

is the projected net force assigned to that material particle.

Different particles may have different accelerations:

$$
a_n\neq a_{n+1}.
$$

That is not a failure of the particle picture. It is expected in a flowing fluid.

The forces may include coarse-grained contributions from:

- gravity;
- pressure interactions with neighbouring packets;
- surface tension;
- air drag;
- contact with a pipe or nozzle;
- internal viscous interactions represented at the packet boundary.

A fluid particle is therefore not a free point mass. It is a material lump whose internal structure is neglected while the relevant external and inter-packet effects are attached to its force account.

This is another reason the ordered-many picture is useful:

```text
one particle
-> one mass address
-> one projected acceleration
-> one projected net-force account

many particles
-> many linked Newton II problems
-> fluid behaviour
```

The continuum equations may later compress those many coupled particle equations.

---

# 15. Failure modes of the projected particle representation

The construction is not unconditional. Several failures can occur.

## 15.1 Trackability failure

If the material cannot be reidentified under the observational procedure, a continuing material address cannot be maintained.

## 15.2 Internal redundancy failure

If tracks inside one packet acquire projected position or velocity differences larger than tolerance, the packet can no longer be represented by one projected particle.

The normal repair is subdivision:

$$
P_n
\longrightarrow
\{P_{n,1},P_{n,2},\ldots\}.
$$

## 15.3 Material exchange across the chosen boundary

If the packet boundary is not material and water crosses it, then the packet mass may change. Such a packet is an Eulerian control volume, not the continuing material particle being defended in this note.

The fixed-mass claim applies only to material addresses.

## 15.4 Projection overlap

Different three-dimensional streams may project onto the same $h$. If they have different velocities, one single-valued $v(h,t)$ cannot represent them both.

The particle description may still retain the different addresses:

$$
P_\alpha,\qquad P_\beta,
\qquad
H_\alpha=H_\beta,
\qquad
V_\alpha\neq V_\beta.
$$

This is a failure of the simple field description, not necessarily a failure of trackability.

## 15.5 Excessively coarse particles

A packet may be so large that one velocity hides important internal deformation. The cure is to tighten the tolerance or reduce the packet size.

These failures show that particle construction is governed by explicit reuse rules rather than by an unconditional declaration that “all fluid parcels are particles.”

---

# 16. Objections and replies

## Objection 1: “But an unbroken jet is spatially continuous.”

It may be. The claim of this note is first about separate material addresses, not necessarily about empty spatial gaps.

Connected spatial support does not imply one material identity or one velocity. A rope is connected but can be divided into separately tracked segments. A fluid jet can likewise contain separately tracked material packets whose occupied regions touch.

## Objection 2: “The packet boundaries are arbitrary.”

Their precise placement can be conventional, but their admissible size is constrained by redundancy and tolerance.

Any partition sufficiently fine to maintain coherent projected position and velocity may work. This is similar to choosing a numerical mesh: several meshes may be valid without all meshes being equally good.

## Objection 3: “As the packets become smaller, their masses approach zero.”

That is not a problem. A finite-resolution model uses finite packets with finite masses. A differential notation $dm$ describes the limiting local mass assignment.

The fact that a limiting element becomes arbitrarily small does not mean that a finite addressed packet changes its mass while being tracked.

## Objection 4: “A fluid particle deforms, so it is not a particle.”

Full rigidity is not required. The particle status is projected and tolerance-relative.

The packet may deform in omitted dimensions while still possessing one adequate projected position and velocity.

## Objection 5: “The continuum equations already work.”

The argument does not deny that. It explains what must be true for their use to be licensed and clarifies what $dm$ refers to.

A successful compression does not erase the more resolved targets from which it was constructed.

## Objection 6: “Droplets are the real particles; the unbroken jet is not.”

Droplets provide clear spatial boundaries, but particle status here comes from material trackability and projected redundancy.

A pre-breakup packet can already have a continuing identity, fixed mass, position, and velocity. Breakup merely makes some packet boundaries physically visible.

---

# 17. The hose example, stated cleanly

Consider water leaving a hose and travelling through air.

## Stage 1: Select the projected dimension

Choose $h$ along the main direction of motion.

$$
\mathbf r_i(t)\mapsto h_i(t).
$$

## Stage 2: Build local redundancy bundles

Group material tracks that are sufficiently close in projected position and projected velocity.

$$
B_n
\longrightarrow
P_n.
$$

## Stage 3: Determine each packet mass

For water emitted during a short interval $\Delta\tau$,

$$
m_n
=
\dot m\,\Delta\tau
$$

for steady flow.

Bind this value to the packet address.

## Stage 4: Follow the packet motion

Each packet has

$$
H_n(t),\qquad
V_n(t),\qquad
a_n(t).
$$

Different packets may have different velocities and accelerations.

## Stage 5: Form the ordered stream

$$
\mathcal P
=
\{P_1,P_2,\ldots\}.
$$

The stream is an ordered many of massive particles, not one redundant body.

## Stage 6: Decide whether to coarse-grain

If the packets are densely and smoothly distributed, replace the ordered many by fields:

$$
\lambda(h,t),\qquad
v(h,t).
$$

If gaps, sharp variations, or multivalued velocities become important, retain the particle description.

## Stage 7: Breakup, if it occurs

If the jet forms droplets, several previously neighbouring packets may become organised into isolated clusters.

The projected particle basis survives. The spatial support changes from connected to separated.

---

# 18. The main conceptual reversal

The usual intuitive narrative is:

```text
water is fundamentally represented as a continuous stream
-> instability breaks the stream
-> droplets become particles
```

The proposed VD-native narrative is:

```text
trackable material is projected
-> locally redundant tracks are lumped
-> each lump receives a fixed mass address
-> many lumps form an ordered particle stream

then:
if the ordered many is dense and smooth
-> it may be compressed into a continuum field

if connected support later breaks
-> the already-existing particle structure becomes visible as droplets
```

The burden of explanation has changed.

We do not need a breakup mechanism to explain why there are material particles.

We need regularity conditions to explain why the ordered particles may be treated *as though* they form one continuous stream.

---

# 19. Compact formal statement

Let the fluid contain trackable material points $i$, with projected tracks $h_i(t)$.

Choose tolerances $\varepsilon_h$ and $\varepsilon_v$. A projected material particle $P_\alpha$ is a bundle $B_\alpha$ such that, over the selected interval,

$$
\max_{i,j\in B_\alpha}
|h_i-h_j|
\leq \varepsilon_h,
$$

and

$$
\max_{i,j\in B_\alpha}
|\dot h_i-\dot h_j|
\leq \varepsilon_v.
$$

Assign the representative state

$$
H_\alpha(t),
\qquad
V_\alpha(t)=\dot H_\alpha(t),
$$

and bind the material mass

$$
m_\alpha
$$

to the continuing bundle address.

Then

$$
P_\alpha
=
\bigl(
m_\alpha,H_\alpha,V_\alpha
\bigr),
\qquad
\frac{D m_\alpha}{Dt}=0
$$

while the address remains materially closed.

A fluid stream is an ordered family

$$
\mathcal P
=
\{P_\alpha\}.
$$

A continuum representation is licensed when this family is sufficiently dense and regular that fields such as

$$
\lambda(h,t)
\qquad\text{and}\qquad
v(h,t)
$$

provide an adequate compression.

For a label $\tau$,

$$
dm=\dot m(\tau)d\tau,
$$

$$
dh=
\left|
\frac{\partial H}{\partial\tau}
\right|d\tau,
$$

and hence

$$
\lambda
=
\frac{dm}{dh}
=
\frac{\dot m(\tau)}
{
\left|
\partial H/\partial\tau
\right|
}.
$$

The density changes when particle spacing changes. The addressed particle mass does not.

---

# 20. Final conclusion

One-dimensional redundancy supplies a principled route from fluid motion to ordinary massive particles.

The construction does not require the fluid to begin as a set of visible droplets. It requires:

1. trackable material;
2. projection onto the dimension relevant to the task;
3. bundles whose projected tracks are redundant within tolerance;
4. continuing material addresses;
5. mass values bound to those addresses;
6. separate positions and velocities for the resulting particles.

The result is an ordered, address-discrete stream:

$$
\{P_n\}
=
\{
(m_n,H_n,V_n)
\}.
$$

The particles may remain spatially adjacent in an unbroken jet or become spatially separated after breakup. In both cases, they are separately addressed material targets.

The continuum description is then a further modelling achievement:

$$
\text{many addressed particles}
+
\text{dense coverage}
+
\text{smooth variation}
+
\text{adequate resolution}
\longrightarrow
\text{continuous fields}.
$$

Accordingly:

> **A fluid is not required to be introduced as one continuous massive object. Under one-dimensional projected redundancy, it can first be represented as a discontinuous—or more precisely, address-discrete—stream of material particles, each with a fixed mass and its own motion. The familiar continuum stream is a coarse-grained description of that ordered many.**

This framing preserves the key mass-address principle:

> **Once a material particle has been identified and its mass determined, the mass is reused while that address continues to track the same material. Changes in $dm/dh$ describe changes in particle distribution and spacing, not changes in the masses already bound to the particles.**
