# NML2.2 Pre-Water Content Inventory

**Status:** working synthesis, d1  
**Project:** VD Newton / NML2.2 — target construction  
**Scope:** an exhaustive inventory of what the student must learn **before** the lesson opens the flowing-water / lower-dimensional-redundancy example  
**Date:** 21 July 2026

---

## 0. Purpose and stopping point

NML2.1 taught students to use Newton II when a massive target and its mass value were already supplied. It also exposed the failure point: a mass value cannot simply be carried through a split, loss of material, merge, substitution, or continuous drain.

NML2.2 begins by asking:

> **A real scene does not arrive labelled. How does the scene earn a continuing material object that can own and reuse a mass value?**

This inventory gives the entire conceptual and operational foundation required before the lesson asks whether redundancy may hold in only one or two dimensions and then applies that idea to flowing water.

The stopping point is deliberate. This note does **not** yet teach:

- projection onto one or two dimensions;
- one-dimensional fluid particles;
- an ordered stream of particles;
- emission-time labels;
- `dm/dh`, line density, or continuum coarse-graining;
- droplets, Rayleigh–Plateau instability, or splatter.

It ends with the exact question that opens that material:

> **Must tracks be redundant in every spatial dimension before they can be represented by one particle, or can redundancy be licensed only in the dimensions relevant to the task?**

---

## 1. The complete pre-water route

The student should be able to run this route before meeting the water example:

```text
NML2.1 failure seam
  -> a supplied mass cannot be reused blindly

scene with no object labels
  -> select and re-identify scene-points
  -> produce tracks
  -> repeat the operation for arbitrarily many further points
  -> declare the task, interval, region, frame, and tolerance
  -> audit coverage
  -> compare tracks for redundancy at that tolerance
  -> form redundant bundles
  -> treat each accepted bundle as one material-object target
  -> assign a target address and an empty mass address
  -> invoke a separately licensed mass-determining process
  -> bind a mass value with provenance and failure conditions
  -> carry the value only while the tolerance-indexed target remains licensed
  -> halt, reconstruct, re-lump, or invoke a new MDP when the licence fails
```

The central division of labour is:

```text
trackability       makes tracks possible
coverage           asks whether the supplied family could reveal the scene
tolerance          states which differences matter
redundancy         tests whether tracks repeat the same motion information
lumping            creates material-object targets and their addresses
MDP                 determines the value placed at a mass address
persistence audit  determines whether that value may be reused later
```

---

# Part I — What the student brings from earlier lessons

## 2. NML1 and NML2.1 prerequisites

NML2.2 should not reteach the whole of NML1 or NML2.1, but the following must be available for use.

### 2.1 Path and trajectory are different

The student must distinguish:

```text
path        a timeless spatial locus or shape
track       a time-indexed record produced by following one selected scene-point
trajectory a mathematical time-indexed function used to represent a track
```

Two points may follow the same geometric path at different times while possessing different tracks.

### 2.2 Motion is read before it is explained

The student already knows the NML1 route:

```text
trajectory in an inertial frame
  -> velocity-change
  -> inertial acceleration
```

A motion-change arrow is not yet a force contribution. Newton II later relates a massive target’s already-readable acceleration to mass and net force.

### 2.3 Newton II is an addressed triplet

For a supplied target `A`:

```text
m[A]
a[A]
F_net[A]
```

must belong to the same target, interval, and frame-qualified account.

The student should already understand:

```text
F_net[A] = m[A] a[A]
```

as a constraint among three addressed quantities, not as a machine that invents all three values from nothing.

### 2.4 NML2.1’s unresolved question

NML2.1 supplied the target and mass address. It ended when reuse became unsafe.

The student should remember the burn:

```text
piece lost
split
merge
substitution
continuous drain
  -> old mass reuse is no longer automatically licensed
```

NML2.2 now explains how a target and its reuse licence were created in the first place.

---

# Part II — Trackability

## 3. The pre-object scene

The lesson begins with a **scene**, not with a list of already-given bodies.

At this stage, the student should not assume:

```text
there is one ball
two cars are two objects
this region belongs to that body
this visible outline fixes one particle count
```

Those may become valid outputs later. They are not the starting data.

Useful distinction:

```text
material  what is physically there
scene     the material as presented to observation and tracking
```

The scene is pre-lumping. A material object is a later modelling output.

---

## 4. Trackability I — any selected scene-point can be tracked

### 4.1 Core statement

> **Trackability I:** any selected point of the scene can be re-identified at later observed times as the same point, thereby producing a track.

A concrete tracker realises this assumption only to a finite reliability and resolution; those practical limitations are recorded separately rather than built into the assumption itself.

A track may be written as observed samples:

```text
(t0, r0), (t1, r1), (t2, r2), ...
```

The physical content is not merely that positions were measured. It is that the positions are attributed to the **same re-identified scene-point**.

Without re-identification, the list is only a collection of unrelated position observations.

### 4.2 Trackability I is Newton’s real-world interface

Newtonian equations use objects such as:

```text
r(t)
v(t)
a(t)
```

Trackability I is what makes those symbols attach to observations. It is the mechanism by which a mathematical motion record becomes the motion record **of something**.

### 4.3 Trackability I is operational, not yet continuous

Trackability I does not by itself assert:

- that the point possessed a definite position at every unobserved instant;
- that the observed samples form a continuous function;
- that the identity could never branch or become ambiguous;
- that the tracker is perfect;
- that all material was represented.

It says only that the re-identification operation can succeed sufficiently well to produce tracks.

### 4.4 Tracker failure modes

Students should recognise that a nominal seed may fail to produce a usable track because of:

```text
occlusion
crossing tracks
identity swaps
featureless surfaces
repeated patterns
glare or reflection
motion blur
out-of-view motion
pattern degradation
a marker slipping relative to the material
```

These are not all failures of the material. They may be failures of access, feature choice, or the tracking procedure.

---

## 5. Iterability — if one point can be tracked, the operation can be repeated

Trackability I must be given an explicit iterability consequence.

> The selection-and-re-identification operation can be repeated for further scene-points.

Therefore, for any finite number `N`, a modeller may in principle select `N` points and attempt to produce `N` tracks:

$$
\forall N\in\mathbb N,
\quad
\text{a track family of size at least }N\text{ may be attempted.}
$$

This is **arbitrarily large finite production**, or potential infinity. It is not the claim that a human finishes an actually infinite observation.

The student should distinguish:

```text
one track through time       longitudinal tracking
many tracks across the scene transverse densification
```

The second is what later makes coverage and redundancy tests possible.

### 5.1 Finite but densifiable families

Every realised family is finite:

$$
\mathcal F_N=\{r_1(t),\ldots,r_N(t)\}.
$$

But there is no fixed finite upper bound supplied by Trackability I itself. New seeds may be added, especially when a current target claim is vulnerable.

### 5.2 What iterability does not grant

Arbitrarily many tracks do not guarantee:

- perfect material coverage;
- infinite spatial or temporal resolution;
- independence of nearby tracks;
- reliable identity for every selected feature;
- access to hidden or occluded surfaces.

Densification adds samples at the apparatus’s existing limits. It does not remove those limits.

---

## 6. Trackability II — the classical continuous-trajectory completion

### 6.1 Core statement

> **Trackability II:** successful re-identifications are observations of a material point whose position is defined at every intervening time and forms one unique, identity-preserving, non-branching continuous trajectory.

Formally, the observed points are treated as samples from:

$$
\mathbf r:I\rightarrow\mathbb R^3,
$$

with `r(t)` continuous over the relevant interval.

### 6.2 Trackability II does not follow from Trackability I

Trackability I supplies observed re-identifications at finitely or countably many times.

Trackability II fills every unobserved instant and asserts continuity and lineage. That is an additional classical completion principle.

The student should understand:

```text
observed samples
  do not by themselves equal
an already-given continuous worldline
```

Many mathematical curves can pass through the same sampled points. The continuity and unique-identity claim is a further assumption.

### 6.3 Why the distinction matters

Trackability I is enough to make practical tracking and finite audits possible.

Trackability II supports the stronger classical picture in which:

- particles possess trajectories between observations;
- velocity and acceleration are derivatives of those trajectories;
- one material identity persists continuously through time;
- later observations are points on the same underlying worldline.

### 6.4 Quantum boundary

At university level, the student should know why Trackability II is the more doubtful assumption.

Standard quantum mechanics does not generally require a particle to possess one definite, continuously existing, identity-bearing position trajectory between measurements. Identical-particle quantum mechanics can also remove any physical fact about which outgoing particle is the same individual as a particular incoming one.

The careful conclusion is:

> Trackability I can survive as an emergent macroscopic observational capacity even when Trackability II is not fundamental.

Interpretations such as Bohmian mechanics retain continuous trajectories by adding a trajectory ontology. Therefore the correct claim is not that every quantum interpretation forbids Trackability II, but that standard quantum mechanics does not itself force it.

### 6.5 Role in this lesson

Trackability II should not be allowed to hide the empirical limitations of Trackability I. The student must still record finite sampling, tolerance, coverage, occlusion, and tracker uncertainty.

---

# Part III — Declare the modelling demand

## 7. The task comes before a final coverage or lumping claim

There is no task-free answer to “how many objects are in the scene?”

Before finalising the tracking family, tolerance, and lumping, the modeller records:

```text
task
region of interest
reference frame
time interval
spatial dimensions being represented
required accuracy
smallest motion distinction that would change the answer
```

Before the flowing-water example, all redundancy claims may still be presented as full-dimensional translational claims. The possibility of projecting onto fewer dimensions is the next unresolved question.

### 7.1 Task-relative modelling

The same material may support different valid target accounts for different tasks.

Examples:

```text
coarse translation of a ball
fine deformation of its surface
detection of fracture
rotation of a door
opening of a crack
```

A family adequate for one may fail for another.

---

# Part IV — Tolerance

## 8. Tolerance is constitutive of lumping

### 8.1 Core statement

> **Tolerance states which observed differences the present model will treat as negligible.**

Tolerance is not applied after an object already exists. It participates in creating the object.

The lumping output is therefore not simply:

```text
A
```

but something like:

```text
A at tolerance epsilon for task Q
```

or:

$$
\operatorname{valid}(A;\varepsilon,[t_0,t_1],Q).
$$

### 8.2 Tolerance comes before the redundancy verdict

The logical order is:

```text
declare task
-> select a defensible tolerance
-> compare tracks under that tolerance
-> form bundles
```

Without a tolerance, finite observational differences cannot be classified as relevant or negligible.

### 8.3 Tolerance floor

The tolerance cannot be finer than the tracker and apparatus can resolve.

If tracking uncertainty is `delta`, then a tolerance below that floor is not admirably strict. It is unsupported.

Questions:

- Can the camera distinguish this displacement?
- Can the feature be re-identified to that precision?
- Is the frame rate high enough for the relevant event?
- Is depth information available?

### 8.4 Tolerance ceiling or task budget

The tolerance cannot be so loose that it:

- merges the intended target with a nearby object;
- hides a distinction that changes the answer;
- permits fracture when the task is to detect fracture;
- discards required predictive accuracy;
- makes unrelated later bundles count as the earlier target.

If no interval exists between the tracker floor and the task ceiling, the model is not supportable with the available data.

### 8.5 Tolerance stays with the target record

Once a lump is created at a chosen tolerance, that tolerance becomes part of the target-address record.

> The tolerance chosen at the birth of a lump defines the standard by which that lump’s continued validity is later judged.

The tolerance is not an intrinsic material property. The same physical material can support several simultaneous target accounts at different tolerances.

It is better to say:

> **Tolerance is a constitutive property of the represented target and its address licence.**

### 8.6 No silent tolerance changes

If a target was created at `epsilon_1`, later persistence must first be judged at `epsilon_1`.

Changing to `epsilon_2` creates or invokes a different account and must be recorded. A modeller may use a planned fine–coarse–fine bridge, but may not enlarge tolerance after a failure and pretend the original fine account never failed.

### 8.7 Sponge and glass comparison

Use two balls:

```text
one spongy
one glass
```

A collision may scatter their tracked points by a similar observed amount. That displacement alone does not carry its own verdict.

The lesson point is:

```text
observed internal scatter
+ chosen tolerance
+ task and material-failure model
-> persistence or failure verdict
```

For a coarse translational task, reversible sponge deformation may remain below the target’s permitted discrepancy or be bridged by a coarser account.

For a fracture-sensitive glass account, comparable separation may exceed the permissible budget or be accompanied by crack/offshoot evidence, causing the old target licence to expire.

The student must learn:

> **No deviation magnitude means “the object broke” without a tolerance-indexed modelling claim.**

---

# Part V — Coverage

## 9. Coverage asks whether the chosen family could reveal the scene

### 9.1 Core definition

> **Coverage is the judgement that the selected track family is sufficient to expose every task-relevant motion distinction that could alter the lumping result at the declared tolerance over the declared interval.**

Student-facing:

> The tracks cover the scene when they are spread and chosen well enough that a different relevant motion is unlikely to be hiding where we did not look.

Coverage answers:

```text
Did we select a family capable of representing the task-relevant character of the scene?
```

Lumping later answers:

```text
Which of the supplied tracks behave redundantly?
```

A perfect redundancy calculation over a badly covered family can be correct about the supplied tracks and still license the wrong target account.

### 9.2 Coverage is tolerance- and task-relative

A useful record is:

$$
\operatorname{coverage}(\mathcal F;\mathrm{ROI},\varepsilon,[t_0,t_1],Q).
$$

A family may cover coarse translation while failing to cover deformation, rotation, crack opening, or mass loss.

---

## 10. The five aspects of coverage

The student should know all five as independent diagnostic questions.

### 10.1 Extent — span the relevant scene

> The family reaches every task-relevant region, side, extremity, face, component, or projection.

Question:

```text
Did we reach every region whose motion could change the answer?
```

Failure example:

```text
Many tracks cover the left half of a plate.
The right half, where tearing begins, is untracked.
```

High local quality cannot repair missing outer reach.

### 10.2 Density — fill consequential gaps

> Inter-track gaps are small enough that a distinct task-relevant motion region cannot plausibly hide between neighbouring tracks.

Question:

```text
Could a new bundle, local bend, crack, slip, or offshoot fit inside this gap?
```

Failure example:

```text
Four corner tracks move together.
The untracked centre buckles.
```

Density is not “as many points as possible.” It is enough local spacing for the task.

### 10.3 Balance — avoid accidental deserts and clusters

> Sampling effort is not unintentionally concentrated in easy or visually rich regions while comparable regions are neglected.

Question:

```text
Did the large track count come from one convenient patch?
```

Failure example:

```text
One hundred tracks cluster on a printed logo.
Only two represent the rest of the structure.
```

Balance does not require exact uniformity. Deliberate non-uniformity may be justified by observability.

### 10.4 Distinctiveness — make tracks genuinely usable

> Selected features contain enough identifying structure to be reliably re-identified without unacceptable ambiguity.

Question:

```text
Can this feature really be followed as the same feature?
```

Failure modes:

```text
repeated identical marks
identity swaps
glare
blur
occlusion
periodic patterns
features that detach from the material
```

Distinctiveness lies at the tracker–coverage boundary:

```text
tracker side:  can this seed be followed?
coverage side: does it contribute usable evidence to the family?
```

### 10.5 Observability — expose the distinctions the task cares about

> Tracks are placed where the competing motion descriptions relevant to the task would produce distinguishable evidence.

Question:

```text
Would the motion difference we care about reveal itself at these locations?
```

Failure examples:

```text
A door is tracked only along its hinge axis.
The points barely move whether the door is stationary or rotating.

A notched plate has no tracks on opposite sides of the notch.
Crack opening cannot be distinguished from common translation.
```

Observability turns coverage from geometric occupation into motion-discriminating measurement design.

### 10.6 Student memory handle

```text
SPAN          extent
FILL          density
BALANCE       balance
DISTINGUISH   distinctiveness
EXPOSE        observability
```

---

## 11. Coverage trade-offs

The student should know that the five aspects cannot always be maximised independently.

### 11.1 Extent versus density

A larger field of view may cover more of the scene while reducing pixels or detail per unit length.

### 11.2 Balance versus observability

Balance resists accidental clustering. Observability may justify intentional oversampling near a crack, contact zone, hinge, or expected boundary.

### 11.3 Density versus distinctiveness

Marks packed too closely may overlap or become visually interchangeable, reducing reliable tracking.

### 11.4 Reported density versus independent information

Many closely spaced computed tracks may reuse largely the same image information. More output points do not always mean proportionally more independent evidence.

### 11.5 Every aspect versus task budget

No track family is simply “well covered” without specifying what it is meant to reveal.

---

## 12. Operational coverage audit

Students should be able to perform this sequence.

### 12.1 Declare the demand

Record:

```text
task
ROI
interval
frame
tolerance
required dimensions
smallest motion distinction that changes the answer
```

### 12.2 Audit the initial family

For each aspect, state pass, fail, or conditional and give a reason.

### 12.3 Remove nominal tracks that failed as evidence

Flag lost tracks, swaps, occlusions, degraded features, and markers that did not follow the material.

### 12.4 Run a provisional lumping audit

Ask what bundles the current family appears to support.

### 12.5 Densify adversarially

Add seeds where the current claim is most vulnerable:

```text
largest gaps
untracked extremities
suspected boundaries
high-gradient regions
contacts and cracks
ambiguous regions
locations where alternative motions differ most
```

### 12.6 Re-track, re-lump, and compare

Compare:

```text
bundle count
bundle membership
bundle boundaries
representative choice
validity intervals
```

If the result changes materially, the earlier coverage was inadequate.

### 12.7 Record the permanent residue

Stability under densification does not prove that no event occurred beneath the apparatus resolution.

---

## 13. The two coverage residues

### 13.1 Seeding residue

```text
Did we choose enough well-placed, usable tracks?
```

This is partly dischargeable. Densification can expose bad sampling and increase confidence.

### 13.2 Resolution residue

```text
Could task-relevant motion or material transport occur beneath the apparatus boundary?
```

Examples:

```text
evaporation
ablation
sub-pixel fragments
hidden rear surfaces
very fast events between frames
unresolved depth motion
```

Densification at the same resolution cannot eliminate this residue.

Coverage therefore remains a **probably-no** claim:

> Probably no relevant unrepresented motion remains above the declared measurement boundary.

---

# Part VI — Redundancy

## 14. Translational redundancy

### 14.1 Core idea

> Tracks are translationally redundant when, within the chosen tolerance and interval, following all of them supplies no task-relevant translational information beyond following one representative.

For full-dimensional tracks `r_i(t)` and `r_j(t)`, a standard fixed-offset test is:

$$
D_{ij}(t)
=
\left\|
[\mathbf r_i(t)-\mathbf r_j(t)]
-
[\mathbf r_i(t_0)-\mathbf r_j(t_0)]
\right\|.
$$

The pair passes when:

$$
D_{ij}(t)\leq\varepsilon
$$

throughout the selected interval, subject to sampling and interpolation limits.

When one representative velocity is required, the model may also need velocity coherence within its declared velocity tolerance.

### 14.2 Redundancy compares tracks, not bare paths

Two points can trace the same geometric path at different times and fail redundancy because their time-indexed motion differs.

### 14.3 Redundancy is narrower than ordinary rigidity

Fixed distances alone permit rotation. A rotating wheel may be rigid in the ordinary distance-preserving sense while rim tracks possess different velocities and fail translational redundancy.

The present redundancy licence is for one translational representative, not a full rigid-body description.

### 14.4 Redundancy is not cohesion

Tracks that move together may do so because of a physical constraint or by coincidence.

A convoy can preserve fixed offsets for an interval without becoming one permanently cohesive body.

Therefore:

> Redundancy licenses a kinematic target over an interval. It does not prove dynamical cohesion or future co-motion.

### 14.5 Redundancy is retrospective and defeasible

The audit certifies what occurred over the observed interval. A later failure does not make the earlier finite-interval account meaningless; it ends or revises its validity history.

### 14.6 Galilean-frame behaviour

Under a Galilean transformation:

$$
\mathbf r_i'(t)=\mathbf r_i(t)-\mathbf Vt-\mathbf c,
$$

pairwise relative positions are unchanged:

$$
\mathbf r_i'(t)-\mathbf r_j'(t)
=
\mathbf r_i(t)-\mathbf r_j(t).
$$

So fixed-offset redundancy is preserved between inertial frames.

A rotating frame can alter the apparent redundancy relation. The frame commitment must therefore remain visible.

---

## 15. All-pairs audits, cliques, and non-transitivity

At finite tolerance, pairwise redundancy need not be transitive.

It is possible that:

```text
A is within tolerance of B
B is within tolerance of C
A is not within tolerance of C
```

Therefore bundles are not automatically simple equivalence classes.

The student should know:

- a candidate bundle must pass the relevant all-pairs audit;
- maximal pairwise-redundant sets are cliques;
- cliques may overlap at finite tolerance;
- more than one admissible bundling may exist;
- choosing among admissible bundles is a recorded human clique-pick.

At zero tolerance, fixed offsets compose and the non-transitivity problem disappears. Finite tolerance makes the human boundary choice unavoidable.

---

# Part VII — Lumping and material objects

## 16. Lumping

> **Lumping is the act of representing one accepted redundant bundle by one particle target.**

The direction of explanation is:

```text
scene
-> tracks
-> coverage
-> tolerance
-> redundancy bundles
-> material objects and particles
```

not:

```text
pre-given objects
-> tracks that belong to them
```

### 16.1 Bodies are outputs

At this stage, the number of material objects is an output of:

```text
track family
tolerance
task
interval
coverage judgement
clique-pick
```

A different tolerance or task may support a different count.

### 16.2 What a bundle creates

An accepted lump fixes:

```text
target identity      this bundle
particle count       how many accepted bundles there are
representative       one track or constructed state for licensed motion
mass address         an empty slot that may later receive a value
validity conditions  tolerance, interval, task, and evidence
```

### 16.3 Material object, particle, and trajectory are distinct

```text
material object  the material followed by the accepted bundle
particle         the reduced representative used by the model
trajectory       the mathematical motion record of that representative
```

The particle is not a tiny literal copy of the body. It is a licensed compression.

### 16.4 Representative-track licence

One representative may stand in for only the information on which the bundle was redundant.

It does not automatically represent:

```text
size
shape
orientation
rotation
internal deformation
internal circulation
unmodelled dimensions
```

The student must be able to state what the representative keeps and what it omits.

### 16.5 Conventional but constrained boundaries

At finite tolerance, exact bundle boundaries can be conventional. That does not make them arbitrary.

Admissible boundaries are constrained by:

```text
track evidence
coverage
tolerance
task
all-pairs redundancy
stability under densification
```

---

# Part VIII — Addresses and mass-determining processes

## 17. Target address, mass address, and mass value

Once material is lumped, distinguish three records:

```text
target address:   A
mass address:     m[A]
bound mass value: m[A] = M
```

Initially:

```text
A exists
m[A] exists
m[A] may be unbound
```

Lumping answers:

> **Which thing can own a mass value?**

It does not answer:

> **What is that mass value?**

### 17.1 Address is not value

Tracks can establish or carry an owner. They do not calculate kilograms by themselves.

A mass number must have provenance.

---

## 18. Mass-determining process (MDP)

### 18.1 Core definition

> **A mass-determining process is a separately licensed procedure that binds, derives, reconstructs, transfers, or assembles a numerical mass value at the mass address of an already-lumped material target.**

The general route is:

```text
lump first
-> mass address exists
-> select an appropriate MDP
-> check the MDP’s prerequisites
-> determine a value and uncertainty/grade
-> bind the value to that address
-> record its failure modes
```

### 18.2 There are many MDPs

There is no single undifferentiated act called “finding the mass.” Different MDPs use different evidence and can fail in different ways.

The student need not master every conceivable MDP before water, but must understand the plurality and be able to identify the process used in a worked case.

---

## 19. Main MDP families introduced before water

### 19.1 Dynamical or Newton-II MDP

A controlled Newton-II trial may determine inertial mass from independently licensed net force and nonzero acceleration:

$$
m[A]
=
\frac{|\mathbf F_{\mathrm{net}}[A]|}{|\mathbf a[A]|}.
$$

A comparison against a standard under the same action and interval is another dynamical form.

Typical failure modes:

```text
wrong target or interval
non-inertial frame
net force not independently licensed
zero acceleration
force and acceleration misaligned or incomplete
address changes during the trial
supposedly equal actions were not equal
```

This is the reference route for inertial mass because it determines the quantity through its Newton-II role.

### 19.2 Volume–density MDP

For material with a supplied density model:

$$
m[A]=\int_{V[A]}\rho(\mathbf r)\,dV,
$$

or, for uniform density:

$$
m[A]=\rho V[A].
$$

Typical failure modes:

```text
wrong material
non-uniform density
hidden voids or porosity
compression
moisture or temperature change
incorrect volume
phase change
unlicensed identification of density/stuff mass with inertial mass
```

NML2.1’s distinction among density mass, gravitational mass, and inertial mass must remain visible.

### 19.3 Scale or gravitational MDP — conditional

A scale-like process determines a gravitationally coupled quantity. It may be used as an inertial-mass MDP only when the gravitational–inertial equivalence link has been explicitly licensed.

It must not silently replace a dynamical inertial-mass procedure.

### 19.4 Assembly/additivity MDP

Already valued components may be combined to assign a value to a newly lumped composite:

$$
m[C]=m[A]+m[B].
$$

This process requires:

```text
valid component bindings
one newly licensed composite target C
an explicit additivity/adequacy commitment
the demanded precision to fit the grade of the rule
```

Redundancy supplies the reason a one-target account is now demanded. It does not, by itself, prove additivity.

### 19.5 Partition or remainder MDP after scattering/splitting

If an original value `M` is known and a target divides into fragments:

$$
M=m_1+m_2+\cdots+m_n
$$

may constrain the fragment values under a licensed conservation/additivity rule.

But the total does not determine the partition by itself.

The student should distinguish:

```text
sum known, all fragment values unknown
  -> underdetermined

all but one fragment known
  -> remaining value can be deduced

extra symmetry, volume, count, or dynamical information supplied
  -> partition may become determinate
```

A new address does not automatically arrive with a mass value.

---

## 20. MDP record and provenance

Every mass binding should carry an auditable record:

```text
MDP name
target address
input data
assumptions
output value
uncertainty or epistemic grade
interval of origination
known failure modes
conditions requiring re-determination
```

The student should be able to label a mass value as:

```text
supplied
dynamically determined
inferred through Newton II
calculated from density and geometry
assembled by additivity
reconstructed after a split
borrowed without licence
```

---

## 21. Why lumping determines when an MDP is invoked

This is a central lesson claim.

Lumping does not determine the mass magnitude. It determines when a new mass question exists.

### 21.1 Block on a toy car

Initially:

```text
A = toy car, with m[A]
B = wooden block, with m[B]
```

Place the block on the car. If the covered tracks of car and block now travel redundantly under the selected tolerance, the scene supports a new composite target:

```text
C = block-and-car lump
```

The new address creates a new demand:

```text
What value belongs in m[C]?
```

That is why the assembly/additivity MDP is engaged.

The best answer to “Why add the masses?” is:

> Because the car and block have now been lumped into one redundantly travelling target that requires one mass value for its one-target Newton-II account, and the assembly MDP assigns that new address the combined value.

### 21.2 Anticipated failure

If the block later slips or flies off:

```text
car and block tracks cease to be redundant
-> composite target C loses its licence
-> m[C] may no longer be used as the mass of one present target
```

The component bindings may survive if their own addresses remain continuous.

A failed prediction using `m[C]` is then diagnosed as consumption of an expired target binding, not as a mysterious failure of Newton II.

---

# Part IX — Persistence and reuse

## 22. Reusing a determined mass later

Once an MDP has bound:

$$
m[A]=M,
$$

that value may be reused at later times only while `A` remains a licensed continuing material target.

The core record is:

$$
\operatorname{valid}(A;\varepsilon,[t_0,t_1],Q).
$$

A complete reuse licence includes:

```text
target lineage
constitutive tolerance
task and interval
coverage scope
redundancy history
mass-value provenance
MDP assumptions
material-closure / no-crossing assumptions
```

### 22.1 Mass-locality or material-closure premise

The persistence story requires an explicit premise of the form:

> The mass bound to a material address changes only when relevant material or mass-energy crosses the address boundary, or when the MDP’s domain assumptions fail.

Within the present Newtonian lesson, the practical form is:

```text
same tracked material
+ no relevant offshoot or ingress
-> mass value may be carried
```

The premise is tolerance-scoped and later meets relativistic/open-system boundaries.

---

## 23. The full persistence certificate has two observational halves

The mass binding is not escorted by redundancy alone.

### 23.1 Positive half — redundancy audit

The tracked family continues to behave as one bundle at the target’s tolerance.

### 23.2 Limiting half — coverage judgement

Probably no relevant untracked material motion, offshoot, or hidden region invalidates the bundle or mass claim above the measurement boundary.

Therefore:

```text
redundancy audit
+ coverage probably-no
+ mass-locality / MDP assumptions
-> temporal reuse licence
```

Neither redundancy nor coverage alone is sufficient.

---

## 24. Persistence, reconstruction, and expiry

Students should distinguish at least three cases.

### 24.1 Persistence

```text
redundancy continues
no offshoot is observed
coverage remains adequate
-> same target address and mass binding are carried
```

### 24.2 Redundancy break with no offshoot — reconstruction case

```text
fine one-particle proxy fails
all tracked material remains accounted for
no material leaves the family
-> no usable fine address during the failure
-> before/after mass value may be reconstructed under mass-locality
```

The new post-event address is not automatically numerically new, but the history must record that it was reconstructed rather than continuously carried at that resolution.

### 24.3 Offshoot or material exchange — expiry

```text
an offshoot develops independent motion
or material crosses the boundary
-> old mass certificate expires
-> remainder and offshoot need revalidation or new MDPs
```

Expiry means “do not reuse without repair.” It need not mean that the old numerical total ceased to exist as a historical value.

---

## 25. Return of redundancy is not return of address

A family may be:

```text
redundant
-> nonredundant
-> redundant again
```

The final redundancy proves only that a present bundle can be formed.

It does not by itself prove that the present bundle is the earlier material target.

Historical lineage requires:

- an uninterrupted acceptable bridge;
- complete material accounting and a licensed reconstruction rule;
- or a new MDP/address assignment.

### 25.1 Occluded-swap test

Two visually identical objects pass behind a screen. One returns with tracks indistinguishable from the earlier target.

Present similarity and redundancy do not establish historical identity. The lesson should use this to separate:

```text
present bundle structure
from
continuing lineage
```

---

## 26. The bouncy-ball double ledger

A marked bouncy ball is the main pre-water persistence case.

### 26.1 Loose-tolerance account

If impact deformation stays below a coarse tolerance adequate for the translational task:

```text
pass -> pass -> pass
```

One coarse target and mass address remain continuously licensed.

### 26.2 Strict-tolerance account

At a finer tolerance:

```text
pass -> fail -> pass
```

The one-particle fine proxy fails during contact. The ball may fission into temporary micro-bundles and later fuse into a new fine bundle.

### 26.3 Fine–coarse–fine bridge

A recorded coarse target may remain continuous through the collision:

```text
fine before
  -> refines a continuous coarse target
coarse target through impact
  -> refined by fine after
```

The later fine address is connected through the coarse bridge, not merely by the return of fine redundancy.

### 26.4 What the student must say

A strong answer distinguishes:

```text
continuous coarse address
fine proxy unavailable during contact
post-contact fine reuse/reconstruction through a named bridge
```

It must not say merely “it is obviously the same ball.”

---

## 27. Prediction versus retrospective repair

A tolerance or address certificate used for advance prediction must exist at the prediction’s past boundary.

If the modeller changes tolerance only after seeing an unexpected deformation, the result is a new retrospective account.

It does not retroactively license the original prediction.

Students should distinguish:

```text
planned tolerance schedule before prediction
from
post-hoc widening after failure
```

---

## 28. Halt discipline

When no acceptable address, bridge, or new mass binding is supplied, the complete correct answer is:

```text
HALT: mass address not licensed.
```

The student must not:

- borrow a nearby value;
- assign the old composite mass to the remainder;
- treat returned redundancy as automatic restoration;
- continue Newton-II substitution with an expired owner;
- invent fragment masses whose partition is underdetermined.

Refusal is successful modelling behaviour.

---

# Part X — Pre-water worked sequence

## 29. Recommended order of examples

These examples collectively install the required content before flowing water.

### 29.1 Many marks on one translating cart

Installs:

```text
trackability
iterability
track family
redundancy
one representative
material object as output
```

Question:

> Do the additional tracks add new translational information or repeat the same information?

### 29.2 Flexible plate with five defective seed layouts

Installs the five coverage aspects.

Use separate failures for:

```text
extent
density
balance
distinctiveness
observability
```

Then densify adversarially and re-lump.

### 29.3 Sponge ball and glass ball

Installs:

```text
tolerance before lumping
tolerance as part of the address record
task/material dependence of failure budgets
observed scattering is not self-interpreting
```

### 29.4 Marked bouncy ball at strict and loose tolerances

Installs:

```text
two simultaneous valid ledgers
fine proxy failure
coarse continuity
fine–coarse–fine bridge
return of redundancy is not enough
```

### 29.5 Occluded swap

Installs:

```text
present redundancy != historical lineage
```

### 29.6 Block placed on toy car

Installs:

```text
new lump -> new address -> MDP demand
assembly/additivity as one MDP
failure mode declared at origination
block flies off -> composite address expires
```

### 29.7 Optional brick-and-chip micro-run

Installs the full mass pipeline:

```text
cover brick
lump brick
bind mass by MDP
carry binding
assemble with a second priced object
observe chip offshoot
expire certificate
identify underdetermined fragment partition
```

This may be reserved for consolidation if the pre-water sequence is already long.

---

# Part XI — Student operations

## 30. Operations the student must be able to perform before water

### 30.1 Trackability operations

- distinguish path, track, and trajectory;
- select a seed point;
- re-identify it across frames;
- flag uncertain or failed identity;
- produce several tracks from one scene;
- explain why the family is finite but densifiable;
- distinguish Trackability I from Trackability II.

### 30.2 Task and tolerance operations

- state the task, ROI, frame, and interval;
- state the working tolerance;
- identify the tracker-imposed tolerance floor;
- identify the task-imposed tolerance ceiling;
- reject a tolerance with no supported window;
- keep the chosen tolerance attached to the target’s validity record;
- record any later tolerance change as a new or bridged account.

### 30.3 Coverage operations

- audit extent;
- audit density;
- audit balance;
- audit distinctiveness;
- audit observability;
- identify trade-offs;
- densify in vulnerable regions;
- re-track and re-lump;
- distinguish seeding residue from resolution residue.

### 30.4 Redundancy and lumping operations

- calculate or judge pairwise relative-position change;
- perform an all-pairs audit;
- form maximal pairwise-redundant bundles;
- identify non-transitivity and overlapping cliques;
- record a clique-pick;
- count material-object targets as an output;
- choose a representative only for licensed motion information;
- state what the representative omits;
- distinguish redundancy from rigidity and cohesion.

### 30.5 Address operations

- write target address `A`;
- write mass address `m[A]`;
- distinguish the address from a bound numerical value;
- record `valid(A; epsilon, interval, task)`;
- track whether an address was carried, reconstructed, newly created, or expired.

### 30.6 MDP operations

- identify which MDP is being used;
- list its inputs and assumptions;
- label the output’s provenance;
- state at least one characteristic failure mode;
- explain why a new lump creates a new MDP demand;
- distinguish first-value determination, assembly, and reconstruction;
- detect an underdetermined fragment partition.

### 30.7 Persistence operations

- run the redundancy half of the certificate;
- run the coverage half;
- detect an offshoot or ingress;
- distinguish persistence, reconstruction, and expiry;
- refuse to restore an old address merely because redundancy returned;
- distinguish advance licence from retrospective repair;
- halt when no licence is available.

---

# Part XII — Critical questions

## 31. Minimum critical-question set before water

### Q1 — What did the tracks establish?

> Several tracks earn target address `A`. Did that track analysis establish `m[A]=2 kg`?

Expected:

> No. It created or escorted the owner/address. A separate MDP determines the value.

### Q2 — Coverage despite redundancy

> All currently selected tracks are redundant. Why is one target not yet fully licensed?

Expected:

> The family must also cover the task-relevant scene through extent, density, balance, distinctiveness, and observability.

### Q3 — Tolerance window

> Why not choose a tolerance so loose that the object never splits?

Expected:

> The tolerance must remain inside the task budget and distinguish the intended target and failure modes.

### Q4 — Sponge and glass

> Why does the same magnitude of internal point separation not carry one universal verdict?

Expected:

> A deviation is interpreted through the target’s chosen tolerance, task, material/failure model, and accompanying evidence.

### Q5 — Bodies as outputs

> How many objects are in the scene before tracks, coverage, tolerance, and lumping are specified?

Expected:

> The modelling particle count has not yet been earned. It is an output of the construction.

### Q6 — Returning redundancy

> Tracks pass, fail, then pass again. Does the final pass restore the original address?

Expected:

> No. It licenses a present bundle. Historical lineage requires a bridge, reconstruction, or new origination.

### Q7 — Block and car

> Why is mass additivity invoked after a block is placed on a toy car?

Expected:

> Their covered tracks now support one composite target, creating a new mass address that needs an assembly MDP.

### Q8 — Block flies off

> A prediction using the composite mass fails after the block leaves. Did Newton II unexpectedly fail?

Expected:

> No. The composite redundancy and address licence had expired; the equation consumed an invalid binding.

### Q9 — Split masses

> A target of mass `M` scatters into three fragments. Does `M=m1+m2+m3` determine all three fragment masses?

Expected:

> No. It constrains the total. The partition needs more information or new MDPs.

### Q10 — Trackability split

> What does Trackability II add beyond the fact that we can repeatedly re-identify points?

Expected:

> It adds a unique continuous identity-bearing trajectory through all intervening times.

---

# Part XIII — Common misconceptions to block

## 32. Misconception list

### 32.1 “The scene obviously contains familiar objects”

Repair:

> Familiar objecthood is a useful expectation, but the lesson requires the target to be earned from tracks, coverage, tolerance, and lumping.

### 32.2 “Any number of tracked points means complete coverage”

Repair:

> Arbitrarily many possible seeds do not erase poor extent, gaps, imbalance, ambiguity, blind placements, or apparatus resolution.

### 32.3 “A tighter tolerance is always more truthful”

Repair:

> A tolerance below the tracker floor is unsupported; a tolerance must also fit the task.

### 32.4 “A looser tolerance can always save the object”

Repair:

> A tolerance above the task budget no longer answers the intended question.

### 32.5 “Tolerance belongs intrinsically to the material”

Repair:

> Tolerance belongs to the material target as represented for a task. The same material may support several tolerance-indexed accounts.

### 32.6 “Redundancy means rigidity”

Repair:

> Ordinary rigidity can include rotation. Translational redundancy is the narrower one-representative licence.

### 32.7 “Redundancy proves cohesion”

Repair:

> It proves only finite-interval kinematic co-motion at the declared tolerance.

### 32.8 “The representative track is the whole object”

Repair:

> It represents only the motion information on which the bundle was redundant.

### 32.9 “Tracks determine the mass”

Repair:

> Tracks determine or escort the owner. An MDP determines the value.

### 32.10 “Mass additivity is why the block and car are one object”

Repair:

> Lumping creates the composite target. Additivity is then invoked as an MDP to price the new address.

### 32.11 “Redundancy returned, so the old object returned”

Repair:

> Present structure and historical lineage are different claims.

### 32.12 “If the mass number still exists, it may be used”

Repair:

> A historical number is usable only when its present owner/address remains licensed.

### 32.13 “A split total determines every fragment mass”

Repair:

> Conservation/additivity may fix the sum while leaving the partition open.

### 32.14 “A successful later fit validates the earlier prediction”

Repair:

> Retrospective repair is a new model, not a retroactive advance certificate.

### 32.15 “Continuity was observed directly”

Repair:

> Observations supply samples and re-identifications. Trackability II supplies the continuous completion.

---

# Part XIV — Mastery gate before flowing water

## 33. Required conceptual mastery

Before opening lower-dimensional redundancy, the student should be able to explain in their own words:

1. why a track is not merely a path;
2. what Trackability I asserts;
3. why Trackability I may be iterated to create arbitrarily large finite families;
4. what Trackability II adds;
5. why the scene is pre-labelled and material objects are outputs;
6. why the task and tolerance must be declared;
7. all five aspects of coverage;
8. why densification audits seeding but not resolution;
9. what translational redundancy means;
10. why redundancy is not rigidity or cohesion;
11. why finite-tolerance bundles may require a clique-pick;
12. what lumping licenses and omits;
13. the difference among `A`, `m[A]`, and `m[A]=M`;
14. what an MDP is and why there are many;
15. why lumping determines when an MDP is demanded;
16. why mass additivity is one MDP rather than the definition of lumping;
17. when a mass binding may be reused;
18. why coverage and redundancy are both required for persistence;
19. the difference among carrying, reconstructing, and expiring an address;
20. why a correct halt can be the complete answer.

## 34. Required practical mastery

The student should be able to take a marked solid or deformable scene and produce a ledger containing:

```text
TASK RECORD
  task
  ROI
  frame
  interval
  tolerance floor
  chosen tolerance
  tolerance budget

TRACK RECORD
  seed identities
  tracks
  tracker uncertainties

COVERAGE RECORD
  extent
  density
  balance
  distinctiveness
  observability
  densification result
  resolution residue

LUMPING RECORD
  pairwise redundancy results
  bundles/cliques
  clique-pick
  representative licence
  target count

ADDRESS RECORD
  target address
  mass address
  current binding or UNBOUND
  MDP provenance
  validity interval
  known failure modes

PERSISTENCE RECORD
  carried / bridged / reconstructed / expired
  reason
  HALT if unlicensed
```

## 35. One final integrated trace

The student should be able to narrate a case such as the block on the toy car:

```text
1. Track points on car and block.
2. Declare the translational task, interval, and tolerance.
3. Confirm coverage for that task at the chosen tolerance.
4. Find that car and block tracks are redundant after attachment.
5. Lump them into composite target C.
6. Create m[C].
7. Invoke the assembly MDP using valid m[car] and m[block].
8. Bind m[C] = m[car] + m[block], with assumptions recorded.
9. Use the value while C remains valid at its tolerance.
10. When the block flies off, expire C.
11. Do not use m[C] for the car alone.
12. Continue only with surviving component addresses or new MDPs.
```

If the student can run that trace and diagnose each possible failure, the foundational target-construction machinery is in place.

---

# Part XV — Explicit boundaries before the water example

## 36. Not yet opened

Before the flowing-water example, do not require the student to solve:

```text
one-dimensional projected redundancy
two-dimensional projected redundancy
ordered-many fluid particles
mass-flow MDPs
emission-time material labels
dm/dh or dm/dA
continuum density derived from particle spacing
fluid pressure-force construction
viscosity
surface tension
Rayleigh–Plateau breakup
open-system momentum equations
force sum and Newton III
centre-of-mass derivations
torque and full rigid-body dynamics
```

These may be named as future branches only.

## 37. The handoff question

Once the student understands full-dimensional, tolerance-indexed lumping, ask:

> **Suppose a material’s tracked points fail full three-dimensional redundancy because they contract sideways or deform internally, but their motion along one selected direction remains coherent. Must the particle description fail completely?**

That question opens lower-dimensional redundancy.

The flowing-water example then becomes the first major test of whether the entire construction can survive projection:

```text
Trackability I
+ coverage
+ tolerance
+ redundancy
+ lumping
+ mass addresses
+ MDPs
+ persistence

now ask:
Can all of this be applied in only the dimension relevant to the task?
```

---

# 38. Compact checklist

```text
BEFORE FLOWING WATER, THE STUDENT MUST OWN:

[ ] path / track / trajectory distinction
[ ] Trackability I
[ ] iterability and finite-but-densifiable track families
[ ] Trackability II and the classical continuity completion
[ ] scene before objects
[ ] task / ROI / frame / interval declaration
[ ] tolerance floor and task budget
[ ] tolerance as constitutive of a target address
[ ] coverage definition
[ ] extent
[ ] density
[ ] balance
[ ] distinctiveness
[ ] observability
[ ] adversarial densification
[ ] seeding residue vs resolution residue
[ ] translational redundancy
[ ] all-pairs audit
[ ] cliques, non-transitivity, clique-pick
[ ] redundancy vs rigidity
[ ] redundancy vs cohesion
[ ] material object as output
[ ] representative-track licence and omissions
[ ] target address
[ ] mass address
[ ] mass value and provenance
[ ] MDP as a general category
[ ] dynamical MDP
[ ] volume–density MDP
[ ] conditional scale/gravitational MDP
[ ] assembly/additivity MDP
[ ] partition/remainder MDP
[ ] lumping as the trigger for a new MDP demand
[ ] validity interval
[ ] mass-locality/material-closure premise
[ ] redundancy + coverage persistence certificate
[ ] persistence
[ ] bridge/reconstruction
[ ] expiry
[ ] return of redundancy != return of address
[ ] prediction vs retrospective repair
[ ] halt discipline
[ ] integrated block-on-car trace
```

---

## 39. Source basis and update note

This inventory synthesises the current NML2.2 drafting context, split ratification, student exercise bank, trackability/lumping note, mass pipeline, five-aspect coverage note, and the subsequent design discussion.

Where the older notes conflict with the latest discussion, this inventory follows the later decisions, especially:

- Trackability is split into Trackability I and Trackability II;
- Trackability I includes explicit iterability/densifiability;
- coverage has five aspects: extent, density, balance, distinctiveness, observability;
- tolerance is selected before lumping and remains part of the target-address licence;
- a lump creates a mass address but not a mass value;
- mass values are supplied by distinct mass-determining processes with distinct failure modes;
- lumping determines when an MDP is demanded;
- lower-dimensional redundancy and flowing water are postponed to the next section.
