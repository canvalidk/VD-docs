# Scene Trackability: From a Scene to a Covered Track Family

**Status:** working argument draft  
**Project:** VD Newton / particle and mass origins  
**Role:** establishes the observational ground beneath trajectory mechanics and ends at the handoff to redundancy and lumping  
**Source policy:** reconstructed only from the supplied informing notes; speculative Gibbs, quantum-statistical, phase, and downstream mass arguments are deliberately excluded

---

## 0. Thesis

A physical trajectory is not supplied merely by a sequence of positions. It is a trajectory **of something** only when the observations at different times are attributed to the same re-identified referent. Newtonian trajectory mechanics therefore rests on a prior operational capacity:

> **Selected referents in a scene must remain re-identifiable through the modelling interval well enough to generate tracks.**

That capacity is **trackability**. It is not a Newtonian law, and it does not begin from already-given bodies. It is an upstream condition on the scene from which bodies may later be constructed.

Trackability is also not a flat property of all material. Whether a proposed referent can be kept identified depends on the observational frame, access procedure, interval, resolution, and accepted error budget. The same material may support a track-based description for one task or interval and fail to support it for another. Trackability therefore acts as a graded, defeasible **sort on proposed scene referents under a declared modelling regime**, not as a once-and-for-all division of substances into trackable and untrackable kinds.

Finally, individually successful tracks do not yet represent the scene. The selected track family must also have **coverage**: it must be capable of exposing every task-relevant motion distinction that could change the later lumping result. Coverage is assessed through extent, density, balance, distinctiveness, and observability.

The output of this note is therefore not a particle, a body count, or a mass address. It is only:

```text
A covered family of usable tracks,
qualified by frame, interval, task, tolerance, apparatus, and residue.
```

Redundancy and lumping begin after this point.

---

## 1. The argument in compact form

The argument can be stated as nine steps.

1. A bare spatial path does not identify which thing traversed it, nor whether two observations belong to the same thing.
2. A physical trajectory `r(t)` requires positions at different times to be attributed to one continuing referent.
3. That attribution is an act of re-identification. Therefore every physical use of trajectory notation presupposes trackability.
4. At this address there are no bodies yet. The input is a scene, and the candidate referents are selected points, patches, tracers, or other trackable features of that scene.
5. Re-identification can succeed or fail by degree. Its success is indexed by a frame, an access procedure, an interval, a reliability or error budget, and the scale at which identity is being claimed.
6. A finite family of successful tracks can still be unrepresentative because the modeller may have seeded only an easy, quiet, or irrelevant part of the scene.
7. Trackability must therefore be followed by a separate coverage judgement.
8. Coverage can be challenged by adversarial densification, but densification cannot remove every limitation of the apparatus or every loss of usable identity.
9. Once a covered track family exists, the note terminates. A later redundancy audit may compress tracks into bundles and represent bundles as particles, but trackability itself neither performs nor licenses that compression.

The complete upstream route is:

```text
material as presented to observation
  -> scene
  -> supplied observational frame
  -> human-selected seed referents
  -> tracker
  -> usable tracks
  -> coverage judgement
  -> covered track family
  -------------------------------- jurisdictional boundary
  -> redundancy audit
  -> bundles
  -> particle targets
```

---

## 2. Scene before bodies

Two registers must be kept apart:

```text
material   what is physically there prior to this description
scene      that material as presented to an observation and tracking procedure
```

The scene is deliberately pre-object. It must not be described as “a body supplying a family of tracks,” because that reverses the intended order. If a body is already assumed, the central construction has been skipped.

The correct direction is:

```text
scene supplies candidate referents
candidate referents may yield tracks
tracks may later be grouped
accepted groups may later be represented as bodies or particles
```

This is why trackability belongs at the ground of the point-particle bridge. It supplies the possibility of time-indexed motion records. It does not yet supply the ontology that those records will later support.

### 2.1 Why `r(t)` silently spends trackability

Suppose a record contains positions

```text
(t0, r0), (t1, r1), (t2, r2), ...
```

Those observations form a track only if `r0`, `r1`, `r2`, and so on are attributed to the same selected referent. Without that attribution, they are merely unrelated position observations.

A trajectory is therefore not just a curve with a time parameter. Its physical use carries an identity commitment:

```text
these positions are successive positions of the same followed referent
```

Trackability is the operational basis of that commitment. It is not derived from Newton I, Newton II, force-sum, or any later mechanical law. Those laws can act only after something has become available to receive a trajectory.

---

## 3. The frame-ordering bracket

A track is always produced in some observational frame. The tracker returns coordinates relative to a camera, laboratory arrangement, or other supplied reference convention. This creates an apparent ordering problem:

```text
tracking needs a frame,
while inertial-frame status is later bootstrapped using tracked motion.
```

The required distinction is:

```text
observational frame supplied for recording coordinates
    !=
inertial-frame status granted for Newtonian analysis
```

The scene may therefore be tracked in a supplied frame before that frame has been certified as inertial. Track production requires a stable coordinate-and-time convention; it does not require the prior Newton-I verdict that the convention is inertial.

The order is:

```text
supply an observational frame
  -> produce tracks in that frame
  -> use later kinematic evidence and modelling commitments
     to assess or assume inertial-frame status
```

For the present note, the inertial-frame problem is bracketed. The frame used to present the scene is recorded, but its Newtonian status is not derived here. This prevents a circularity without pretending that frame choice is irrelevant. A rotating frame, in particular, can change later redundancy judgements even when a change between Galilean inertial frames would not.

---

## 4. The tracker

A working tracker can be represented as:

```text
tracker(record, seed referent, observational frame, interval)
  -> track
  |  ambiguous
  |  lost
  |  failure
```

A **track** is a time-indexed motion record. It is never merely a timeless path. Two referents may trace the same geometric path at different times and still possess different tracks.

The tracker need not be implemented in any particular way. It may be a person following a marker, a computer-vision system, a physical tracer, or another disciplined access procedure. What matters is the interface and the grade of the result.

Four properties are load-bearing.

### 4.1 Finite but densifiable

Every realised run yields finitely many tracks because only finitely many seeds were selected. Where the observational record persists, the modeller may rerun the procedure with further seeds over the same past interval.

```text
current family: finite
standing capacity: add further seeds and rerun
```

The family is therefore not an actual continuum. It is a finite human-selected proxy with a standing capacity for strategic densification.

This distinction matters because later confidence does not come from pretending that every material point was followed. It comes from exposing a provisional claim to further tests.

### 4.2 A reliability floor on tolerance

Re-identification is not exact. Image noise, blur, occlusion, repeated patterns, depth ambiguity, marker slip, and identity swaps place a lower bound on the differences the record can support.

Two tolerances must therefore not be confused:

```text
tracking uncertainty floor   what the access procedure can distinguish
working modelling tolerance  what differences matter to the task
```

A working tolerance below the tracking floor is not admirably strict. It asks the record to resolve a distinction the record cannot carry.

### 4.3 Proxy, not account

The tracker normally matches a visible or otherwise accessible feature. The modelling claim, however, is that this feature continues to report the same material referent.

```text
proxy:    the mark, texture, bead, patch, or signal actually matched
account:  continuity of the material referent the proxy is taken to report
```

A successful feature match does not automatically establish the account. A marker may detach or slip. Two identical marks may swap identity. A tracer may stop following the medium. The tracker dossier must therefore record known proxy failures rather than hiding them inside the word “same.”

### 4.4 Point selection is residual input

The scene does not select its own seeds. Choosing which referents to attempt to follow is a human or apparatus-design act.

The following belong at the residual layer:

```text
recording apparatus
observational frame
region of interest
seed selection
tracking procedure
accepted reliability
working interval
tracking uncertainty
```

The later mechanical trace may audit consequences of these inputs, but it must not silently generate them from the equations.

---

## 5. Trackability is a graded sort, not a global property

The sentence “the material of the world is trackable” is too strong. It suggests that every region, scale, and interval of every scene arrives with stable point identities waiting to be followed. The informing notes themselves provide the correction.

The strict object of the trackability judgement is not material in the abstract. It is a proposed referent under a modelling regime:

```text
trackability(
  proposed referent;
  observational frame,
  access procedure,
  interval,
  spatial and temporal resolution,
  reliability budget
)
```

A useful informal concept is a **trackability horizon**: the scale or interval beyond which the present procedure can no longer support the claim that the same referent has been kept identified. The horizon is not necessarily sharp. It may be crossed gradually as ambiguity, diffusion, mixing, occlusion, deformation, or proxy failure accumulates.

This yields three corrections.

### 5.1 Trackability sorts proposed descriptions, not substances

It is tempting to say:

```text
solids are trackable
fluids are untrackable
```

That is false as a general division. A steel block can become untrackable under poor access. A fluid parcel can be followed over a suitable finite interval. Continuum mechanics can describe a fluid mechanically without preserving parcel identities at all.

The safer statement is:

> **Trackability sorts candidate material referents under declared conditions. It does not divide the world into Newtonian objects and non-Newtonian objects.**

### 5.2 The judgement is interval- and tolerance-indexed

A referent may be identifiable over a short interval and cease to be identifiable over a longer one. A coarse tolerance may support continuity that a fine tolerance rejects. The verdict must therefore travel with its qualifiers.

```text
trackable for this interval, at this resolution and reliability
```

is a meaningful claim.

```text
trackable, full stop
```

usually is not.

### 5.3 Failure of tracking is not failure of all mechanics

If a Lagrangian, identity-bearing description fails, a field description may remain available. Navier–Stokes does not stop being mechanics because it uses velocity, pressure, and density fields rather than a permanent inventory of individually re-identified molecules.

The relevant divide is between descriptions that require continuing referents and descriptions that do not, not between “mechanical material” and “thermodynamic material.”

---

## 6. Trackability is necessary but not sufficient: coverage

A track family does not represent a scene merely because every selected seed was successfully followed.

Consider a sheet whose left half translates while its right half begins to tear away. Suppose every selected seed lies on the left half. All supplied tracks may be perfectly coherent. A later redundancy calculation may be completely correct about them. Yet those tracks do not license a one-target description of the task-relevant sheet, because the family never observed the region in which the competing motion occurred.

This establishes a separate judgement:

```text
trackability asks:
  can this selected referent be followed through time?

coverage asks:
  did the selected family have a fair chance to reveal every
  task-relevant motion distinction in the scene?

lumping asks later:
  which supplied tracks behave redundantly?
```

Coverage must therefore precede lumping.

A working definition is:

> **Coverage is the judgement that the selected track family is sufficient to expose every task-relevant motion distinction in the scene that could alter the later lumping result at the declared tolerance over the declared interval.**

A useful record is:

```text
coverage(F; ROI, epsilon, [t0,t1], task)
```

where:

```text
F          selected usable track family
ROI        task-relevant region of interest
epsilon    working modelling tolerance
[t0,t1]    modelling interval
task       motion information the representation must preserve
```

Coverage is not proof that nothing was missed. It is the qualified judgement:

```text
probably no relevant unrepresented motion-pattern remains
above the declared measurement boundary
```

---

## 7. The five aspects of coverage

The five aspects are independent enough that a family can pass four and fail the fifth.

| Aspect | Core question | Characteristic failure |
|---|---|---|
| **Extent** | Did the family reach every task-relevant region? | A whole side, face, end, extremity, or component is unrepresented. |
| **Density** | Are the internal gaps small enough? | A bend, crack, slip, offshoot, or distinct motion region hides between tracks. |
| **Balance** | Was sampling effort distributed defensibly? | Most tracks cluster in an easy or visually rich region while comparable regions are neglected. |
| **Distinctiveness** | Can each selected feature actually be re-identified? | Repeated patterns, glare, blur, occlusion, identity swaps, or marker slip destroy usable identity. |
| **Observability** | Would the competing motions relevant to the task produce different track evidence here? | Tracks miss a hinge, crack, boundary, contact zone, off-axis region, or discriminating direction. |

A compact handle is:

```text
SPAN          extent
FILL          density
BALANCE       balance
DISTINGUISH   distinctiveness
EXPOSE        observability
```

### 7.1 Extent

Extent concerns the outer reach of the family. A dense patch does not represent an untracked half of the scene.

```text
Did we reach every region whose motion could change the answer?
```

### 7.2 Density

Density concerns the size of the holes inside the reached region.

```text
Could a task-relevant distinct motion fit inside this gap?
```

More tracks are not automatically better. Once additional tracks are below the apparatus resolution, heavily overlapping, or mutually indistinct, reported density stops corresponding to independent evidence.

### 7.3 Balance

Balance prevents accidental deserts and clusters. It does not require a geometrically uniform grid.

```text
sampling effort should follow task-relevant complexity,
not merely physical area
```

A contact zone or suspected crack may justifiably receive more scrutiny than a quiet region. That deliberate asymmetry is licensed by observability, not a failure of balance.

### 7.4 Distinctiveness

Distinctiveness lies at the tracker–coverage boundary.

```text
tracker-side question:
  can this seed be followed reliably?

coverage-side consequence:
  does this seed contribute usable evidence to the family?
```

Nominal geometric coverage supplied by ambiguous features is not effective coverage.

### 7.5 Observability

Observability asks whether the placement discriminates between the descriptions the task must distinguish.

Tracking only points on a door's hinge axis may be extensive, dense, balanced, and distinctive along that axis, while remaining useless for deciding whether the door rotated. Tracking a notched plate everywhere except across the two faces of the notch can miss the one distinction the experiment was designed to detect.

Observability therefore turns coverage from spatial occupation into motion-discriminating measurement design.

---

## 8. Coverage as an audit

Coverage should be treated as a provisional proposal exposed to challenge.

### Step 1 — declare the modelling demand

Record:

```text
task
region of interest
observational frame
modelling interval
working tolerance
required dimensions or projection
smallest motion distinction that would alter the answer
```

### Step 2 — inspect the proposed family

Record the initial judgement for:

```text
extent
density
balance
distinctiveness
observability
```

### Step 3 — run the tracker and remove nominal failures

Flag tracks compromised by:

```text
loss
identity swap
occlusion
blur or glare
pattern degradation
out-of-view motion
proxy detachment or slip
```

### Step 4 — pass the family downstream provisionally

The later redundancy and lumping result may now be computed for the current family. This note does not own that computation, but it uses the result as evidence about whether the seeding was adequate.

### Step 5 — densify adversarially

Add seeds where the current claim is most vulnerable, not merely where tracking is easiest:

```text
largest gaps
underrepresented extremities
suspected bundle boundaries
high-gradient regions
contacts, cracks, joints, and interfaces
ambiguous or lost-track regions
locations where competing motion descriptions differ most
```

### Step 6 — re-track, re-lump, and compare

Compare the downstream outputs:

```text
bundle count
bundle membership
bundle boundaries
representative choice
validity history
```

A material change convicts the earlier seeding. Stability under several strategically different densifications increases confidence, but does not convert coverage into an absolute proof.

### Step 7 — retain the unresolved residue

Record what the present observational arrangement still cannot exclude.

---

## 9. The two coverage residues

The coverage judgement contains two importantly different uncertainties.

### 9.1 Seeding residue

```text
seeding residue :=
  did the modeller choose enough well-placed usable tracks?
```

This residue is partly dischargeable because a persistent record permits new seeds and reruns.

```text
densify
  -> re-track
  -> re-lump
  -> compare
```

No finite number of reruns proves perfect coverage, but bad seeding can be exposed and confidence can be strengthened.

### 9.2 Resolution residue

```text
resolution residue :=
  could task-relevant motion or material transport occur beneath what
  the present access procedure can distinguish?
```

Examples include:

```text
sub-pixel fragments
evaporation or ablation
motion behind an opaque surface
depth motion unavailable to the apparatus
events faster than the frame interval
features too small or too interchangeable to preserve identity
```

Adding more seeds at the same resolution cannot discharge this residue.

The informing notes support two readings of why this residue persists:

1. **Apparatus reading:** the process exists, but the present record cannot resolve it.
2. **Identity-horizon reading:** at the claimed scale or interval, no stable individual referent remains available to be re-identified.

These readings should not be silently collapsed. The stronger ontological claim is not established here. The present note needs only their shared operational consequence:

> **Densification adds samples under the existing access conditions; it does not manufacture finer resolution or a stable identity where the procedure cannot supply one.**

---

## 10. The fluid test

Fluids are the case that prevents the argument from becoming a crude binary sort.

### 10.1 The wrong conclusion

The wrong conclusion is:

```text
solids support tracks
fluids do not support tracks
therefore point-particle mechanics applies to solids but not fluids
```

Lagrangian fluid mechanics does follow material parcels. Particle-tracking and tracer methods can supply successful tracks. Fluid parcel identity is therefore not simply absent.

### 10.2 The corrected conclusion

The honest claim is that parcel identity is limited and can decay under mixing, diffusion, deformation, and the chosen scale of coarse-graining.

```text
short or coarse interval:
  a parcel or tracer may remain re-identifiable

longer or finer interval:
  the same identity claim may fail
```

This is precisely why trackability must be indexed by interval, scale, and access method.

### 10.3 Eulerian and Lagrangian descriptions

Fluid mechanics already carries the relevant distinction:

```text
Lagrangian description
  follows material parcels
  therefore spends continuing identity

Eulerian description
  assigns fields to spatial locations
  therefore does not require the same parcel to be re-identified through time
```

The two descriptions are not two kinds of material. They are two ways of representing the same material, with different identity requirements.

### 10.4 Tracers as proxies

A distinguishable tracer inserted into a fluid can serve as a trackable proxy for local flow. This illustrates the proxy/account split: the tracer is what is directly re-identified; the fluid motion is what its behaviour is taken to report.

That fit is suggestive, not by itself a proof of a deeper theory of identity. The tracker dossier must still record when tracer inertia, slip, diffusion, or other failures break the proxy relation.

### 10.5 The tap and imposed parcel identity

The falling-tap example exposed the issue early. The whole stream does not form one fixed-offset bundle. Representing it slab-wise creates an ordered chain of particle-like parcels, but the slab boundaries are imposed by tolerance and modelling purpose rather than discovered as pre-existing permanent identities.

That is not automatically illegitimate. It means only that the construction belongs downstream, at the redundancy and lumping stage. Trackability supplies the motion evidence; it does not claim to have found natural parcel boundaries already written into the water.

---

## 11. Handoff to redundancy and lumping

This note ends with a covered track family.

```text
OUTPUT OF SCENE TRACKABILITY

scene record
observational frame
modelling interval
selected seed referents
usable tracks
tracker reliability and failure dossier
tracking uncertainty floor
coverage judgement across five aspects
densification history
remaining resolution / identity residue
```

The next stage asks a different question:

```text
Which of these tracks repeat the same task-relevant motion information
within the working tolerance over the modelling interval?
```

That is the redundancy question. If a later audit accepts a family of tracks as redundant, lumping may compress them into one representative particle target.

The compression framing helps preserve the boundary:

```text
trackability produces motion records
coverage qualifies the supplied family
redundancy identifies repeated information
lumping compresses that repeated information, losslessly up to tolerance
```

If little redundancy exists, little compression is licensed. The description may approach a fine-grained or continuum representation rather than collapsing into a small particle count. Failure to compress is not failure to describe.

Trackability itself does **not** determine:

```text
bundle boundaries
particle count
cohesion
future co-motion
mass address
mass value
centre of mass
force account
```

Those are later questions with different licences.

---

## 12. What this note claims

This draft claims:

1. Physical trajectory notation presupposes re-identification of a continuing referent.
2. Re-identification acts on selected scene referents before bodies or particles are licensed.
3. Trackability is graded and defeasible, indexed by frame, interval, access conditions, and reliability.
4. Individually successful tracks require a separate coverage judgement before they can support later lumping.
5. Coverage has five useful and independently diagnostic aspects: extent, density, balance, distinctiveness, and observability.
6. Adversarial densification can audit seeding but cannot remove every resolution or identity limitation.
7. The output of this stage is a covered track family, not a body or particle.

---

## 13. What this note does not claim

This draft does **not** claim:

- that all material is globally trackable;
- that fluids or gases are categorically untrackable;
- that operational trackability is identical to metaphysical haecceity;
- that operational trackability is identical to quantum exchange identity;
- that Newtonian mechanics and thermodynamics apply to disjoint kinds of matter;
- that every resolution failure proves the absence of an underlying individual;
- that a tracer automatically reports the medium perfectly;
- that successful co-tracking proves cohesion or future unity;
- that trackability determines a particle count or a mass;
- that non-trackable material can already be routed through acting-object machinery at this address.

The stronger conjecture that non-trackable material is known only through its effects on trackable targets may be worth developing later, but it requires apparatus unavailable in this note and is not used in the argument.

---

## 14. Compact scene-trackability record

```text
SCENE TRACKABILITY RECORD

scene / record:
observational frame:
region of interest:
modelling interval:
task:
required dimensions or projection:

TRACKER
  access procedure:
  seed referents:
  usable tracks:
  lost / ambiguous tracks:
  proxy-to-material assumptions:
  tracking uncertainty floor:

COVERAGE
  extent:
  density:
  balance:
  distinctiveness:
  observability:

AUDIT
  adversarial densification performed:
  downstream bundle result before:
  downstream bundle result after:
  stability judgement:

RESIDUE
  unresolved apparatus limits:
  possible identity-horizon limits:
  remaining probably-no:

HANDOFF
  covered track family available: YES / NO / CONDITIONAL
  conditions attached to handoff:
```

---

## 15. Open questions

The argument is coherent without resolving the following questions, but the final note should leave them visible.

1. **Trackability grade.** What exact quantity, if any, should represent the strength of a re-identification claim across interval and tolerance?
2. **Horizon structure.** Is the trackability horizon primarily an apparatus limit, a physical identity-decay process, or a combination that must be decomposed case by case?
3. **Frame ordering.** What is the final one-sentence rule that distinguishes the observational frame needed to produce tracks from the later inertial-frame commitment?
4. **Eulerian–Lagrangian bridge.** Under what explicit conditions may a field description and a parcel-following description be treated as interchangeable for the task?
5. **Tracker/account fidelity.** What evidence is sufficient to say that a visible feature, marker, or tracer remained attached to the material referent it was supposed to report?
6. **Downstream interface.** What exact data structure should the redundancy/lumping note receive so that every coverage qualifier and residue remains attached to the track family?

---

## 16. Source map

This draft draws its load-bearing claims from the supplied notes as follows:

- `vd_trackability_scene_to_particles_d4-informing(6).md`
  - scene before bodies;
  - every physical `r(t)` spends re-identification;
  - tracker procedure;
  - finite-but-densifiable families;
  - tolerance floor;
  - proxy/account distinction;
  - seeding and resolution residues.

- `vd_coverage_five_aspects_and_industry_appearances_d1-informing.md`
  - coverage as distinct from trackability and lumping;
  - the five coverage aspects;
  - adversarial densification;
  - seeding versus resolution residue;
  - the claim that a perfect redundancy audit over bad seeding answers the wrong observational question.

- `vd_point_particle_bridge_spine_d1-informing(1).md`
  - trackability as the ground;
  - lumping as the next wall;
  - the jurisdictional line separating track production from particle construction.

- `vd_tracks_to_particles_corrections_d3-informing.md`
  - the owed frame-ordering sentence;
  - point selection as a residual-layer act;
  - the compression framing and continuum limit;
  - the warning not to forward-reference mass.

- `identifiability_and_fluid_representation_discovery-informing.md`
  - correction of the global trackability claim;
  - trackability as graded and interval/tolerance indexed;
  - the fluid counterexample to a binary sort;
  - the warning that the divide concerns descriptions rather than substances;
  - the distinction between established operational claims and speculative identity syntheses.

