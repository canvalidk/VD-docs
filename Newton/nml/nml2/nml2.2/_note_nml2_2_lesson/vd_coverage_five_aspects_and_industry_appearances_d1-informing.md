> **Informing copy - do not edit here.**
> **Home:** the `particle_and_mass_origins` discussion - `Newton-analysis/_dscn_particle_and_mass_origins/vd_coverage_five_aspects_and_industry_appearances_d1.md`.
> Placed in `nml2.2` because it develops the coverage half of the target-persistence certificate that the lesson's pre-water inventory hands off to - the five aspects (extent, density, balance, distinctiveness, observability), their trade-offs and their industrial groundings. Custody moved to Newton-analysis on 2026-08-26; this copy is what stays behind. This is a read-only copy; refresh from home if the source changes.

---

# Coverage: Five Aspects and Their Industrial Appearances

**Status:** working note, d1  
**Project:** VD Newton / NML2.2 — target construction  
**Date:** 2026-07-20  
**Role:** develops the coverage half of the target-persistence certificate and grounds its five proposed aspects in established engineering measurement practice.

---

## 0. Thesis

A track family does not represent a scene merely because every selected point was successfully tracked. The selected tracks must also be capable of revealing the task-relevant character of the scene.

```text
trackability asks:  can this selected point be followed through time?
coverage asks:      did we select a family capable of representing the scene?
lumping asks:       which of the resulting tracks behave redundantly?
```

The proposed coverage judgement has five aspects:

```text
1. extent
2. density
3. balance
4. distinctiveness
5. observability
```

A compact student-facing version is:

```text
SPAN the scene.
FILL the gaps.
BALANCE the distribution.
DISTINGUISH the tracked features.
EXPOSE the relevant motion-patterns.
```

These five labels are a VD Newton synthesis. Engineering fields do not normally present a standard list called “the five aspects of coverage.” What is industrially established is the underlying family of requirements: suitable regions and fields of view, sufficient sampling density, controlled feature distribution, reliable feature identification, and deliberate placement for the quantities or failure modes one needs to observe.

---

## 1. Where Coverage Sits in the Scene-to-Particle Route

The NML2.2 route is:

```text
scene
  -> selected seed points
  -> tracks
  -> coverage judgement
  -> redundancy audit
  -> bundles
  -> particle targets
  -> target and mass addresses
```

Coverage belongs **before** lumping. Lumping can only classify the tracks that were supplied. A perfect redundancy calculation over a badly selected family can therefore return a precise answer to the wrong observational problem.

For example, imagine a sheet that is translating on its left half while its right half is beginning to tear away. If every seed lies on the left half, the supplied tracks may be perfectly redundant. The redundancy audit is correct. The conclusion that the whole task-relevant sheet is one translating target is not licensed, because the family failed to cover the region in which a different motion-pattern occurred.

This gives the core definition:

> **Coverage is the judgement that the selected track family is sufficient to expose every task-relevant motion distinction in the scene that could alter the result of lumping at the declared tolerance over the declared interval.**

An equivalent negative formulation is useful:

> A family has adequate coverage when no untracked task-relevant region is reasonably likely to contain a motion-pattern that would change the inferred bundles, bundle boundaries, or validity history.

Coverage is therefore a **probably-no** judgement:

```text
probably no relevant unrepresented motion-pattern remains in the scene
```

It is not a proof that nothing was missed.

A possible typed record is:

```text
coverage(F; ROI, epsilon, [t0,t1], task)
```

where:

```text
F          = selected track family
ROI        = task-relevant region of interest
epsilon    = working tolerance
[t0,t1]    = modelling interval
task       = motion information the representation must preserve
```

Coverage cannot be declared without these qualifiers. A family may cover a ball adequately for its coarse translational motion while failing to cover the fine deformation field at impact.

---

## 2. The Five Aspects

## 2.1 Extent — the family must span the task-relevant scene

```text
extent :=
the selected tracks reach across every task-relevant region of the scene
```

Extent concerns the **outer reach** of the family. Tracks must not all lie inside one convenient patch while other relevant regions, extremities, faces, or components remain untouched.

Questions for an extent audit:

- Does the family reach every side and extremity that matters?
- Are separate visible regions represented?
- Are long, thin, projecting, or partially occluded regions included?
- Does the tracked region remain inside the usable field of view for the whole interval?

Failure example:

```text
Fifty dense tracks cover the left half of a deforming plate.
No tracks cover the right half.
```

The family may have excellent local density but poor extent.

Extent is task-relative. If the question concerns only the motion of a marked central patch, covering the whole plate is unnecessary. If the question concerns whether the plate remains one target, the untracked half is load-bearing.

---

## 2.2 Density — the gaps must be small enough

```text
density :=
the spacing between tracks is fine enough that a task-relevant motion
variation cannot plausibly hide between neighbouring tracks
```

Density concerns the **size of the holes** within the covered region. A family can span the full scene while remaining too sparse to reveal local bending, cracking, slipping, or fission.

Questions for a density audit:

- What is the largest untracked gap?
- Could a distinct motion-region fit inside that gap?
- Is there enough local track information to compare neighbouring motions?
- Is the spacing fine enough relative to the expected spatial gradient and the working tolerance?

Failure example:

```text
Four tracks sit at the corners of a large flexible sheet.
All four translate together.
The centre buckles between them.
```

The family has good extent but inadequate density.

Density is not maximised without limit. More seeds eventually become redundant with one another, increase processing cost, or exceed the apparatus resolution. The relevant question is not “how many tracks can we produce?” but:

```text
Is the inter-track spacing small enough for this task at this tolerance?
```

---

## 2.3 Balance — the family must not contain accidental deserts and clusters

```text
balance :=
the allocation of tracks across the scene is not unintentionally concentrated
in some regions while leaving comparable regions underrepresented
```

Balance concerns the **distribution of sampling effort**. High total track count does not guarantee good coverage if most of the tracks occupy one easy or visually rich region.

Questions for a balance audit:

- Are tracks unnecessarily clustered?
- Do comparable regions receive comparable scrutiny?
- Are visually difficult regions being neglected simply because they are difficult?
- Is the distribution appropriate to the expected complexity of the scene?

Failure example:

```text
One hundred tracks occupy a textured logo on a component.
Only two tracks represent the surrounding smooth structure.
```

The total count is large, but the coverage is badly balanced.

Balance should not be confused with exact geometric uniformity. An even grid is a good default only when the scene is expected to be homogeneous. In an inhomogeneous scene, appropriate balance may be deliberately non-uniform:

```text
quiet region             -> lower seed density may be adequate
contact or crack region  -> higher seed density may be necessary
```

A useful formulation is:

> **Sampling effort should follow task-relevant complexity, not merely physical area.**

Balance prevents accidental non-uniformity. Observability, discussed below, licenses deliberate non-uniformity.

---

## 2.4 Distinctiveness — the selected features must support reliable re-identification

```text
distinctiveness :=
each selected point or local patch has enough identifying structure to be
re-identified through the interval without unacceptable ambiguity
```

Distinctiveness asks whether the nominal seeds produce **usable tracks**. Repeated, featureless, reflective, occluded, or visually interchangeable points may be selected across the whole scene yet fail to deliver stable identities.

Questions for a distinctiveness audit:

- Can the tracker distinguish this feature from nearby features?
- Is the local appearance unique enough to avoid identity swaps?
- Does the feature remain attached to and move with the material of interest?
- Does deformation, glare, blur, or occlusion destroy its identity?
- Is the pattern periodic in a way that makes different regions interchangeable?

Failure example:

```text
A perfectly regular array of identical marks covers the whole sheet.
After a large translation, several marks can be matched equally well to the
same mark in the next frame.
```

Geometric coverage is high, but effective coverage is poor because track identities are ambiguous.

### Architectural note

Distinctiveness lies at the interface between **tracker quality** and **coverage**.

```text
tracker-side reading:
Can this seed be followed reliably?

coverage-side consequence:
Does this seed contribute a usable representative to the family?
```

The causes of failure—identity swap, occlusion, insufficient texture—belong to the tracker dossier. But a point that cannot be re-identified contributes no effective coverage. It is therefore useful to retain distinctiveness among the five coverage aspects while explicitly recording its boundary position.

---

## 2.5 Observability — the family must expose the distinctions relevant to the task

```text
observability :=
the tracks are positioned so that the competing motion-patterns relevant to
the task would produce distinguishable track evidence
```

Observability is the most strongly task-relative aspect. It asks not merely whether points occupy the scene, but whether they are located where the scene’s possible **character** would reveal itself.

Questions for an observability audit:

- Which alternative motion descriptions must the data distinguish?
- Where would those alternatives disagree most strongly?
- Are both sides of a possible boundary represented?
- Are joints, hinges, cracks, interfaces, contact zones, or thin bridges represented?
- Are off-axis points included when rotation must be distinguished from translation?
- Are multiple depths or faces represented when three-dimensional motion matters?

Failure example:

```text
A door is tracked only along its hinge axis.
Those points move very little whether the door is stationary or rotating.
```

The seeds may be extensive, dense, balanced, and distinctive along the axis, yet poorly observable for the task “detect the door’s rotation.” Off-axis points are needed because that is where the competing descriptions separate.

Another example:

```text
A plate contains a notch where a crack may open.
The track family is evenly distributed everywhere except immediately across
the two faces of the notch.
```

The family looks balanced globally but fails to expose the specific failure mode of interest.

Observability therefore converts coverage from mere spatial occupation into **motion-discriminating measurement design**.

---

## 3. The Five Aspects Are Independent Enough to Matter

The five aspects answer different failure questions:

| Aspect | Governing question | Characteristic failure |
|---|---|---|
| Extent | Did we reach every relevant region? | A whole side, end, face, or component is unrepresented. |
| Density | Are the internal gaps small enough? | A local deformation or new bundle hides between tracks. |
| Balance | Was sampling effort distributed appropriately? | High track count is concentrated in easy regions. |
| Distinctiveness | Can the selected features be followed reliably? | Ambiguous matches, identity swaps, glare, blur, or pattern loss. |
| Observability | Would relevant alternative motions look different in the data? | Tracks miss the hinge, boundary, crack, contact zone, or discriminating direction. |

A family can pass any four and fail the fifth.

### One worked scene: a flexible plate with a central notch

```text
extent failure:
  only the left half is seeded

density failure:
  the whole plate is spanned, but large gaps surround the notch

balance failure:
  most seeds cluster around printed text far from the notch

distinctiveness failure:
  a repeated grid gives ambiguous local identities

observability failure:
  no pair of tracks lies on opposite sides of the notch, so opening cannot be
  separated from common translation
```

This is why collapsing the list to “put enough points on the scene” loses useful diagnostic structure.

---

## 4. Trade-offs Between the Aspects

The aspects cooperate, but they also compete under finite camera resolution, processing capacity, access, and cost.

### 4.1 Extent versus density

At fixed image resolution, increasing the field of view usually reduces the number of pixels available per unit length. A larger scene can be covered, but local detail becomes harder to resolve.

```text
larger field of view  -> greater extent, potentially lower spatial resolution
smaller field of view -> greater local density/resolution, potentially poorer extent
```

### 4.2 Balance versus observability

Balance resists accidental clustering. Observability may require intentional clustering near a crack, joint, impact point, or high-gradient region.

The correct target is not geometric uniformity but **defensible allocation**:

```text
ordinary regions receive enough coverage
critical regions receive additional coverage for a stated reason
```

### 4.3 Density versus distinctiveness

More marks do not always improve tracking. If features overlap, become too small for the pixels, or produce nearly identical local patches, increased geometric density can reduce reliable distinctiveness.

### 4.4 Density versus independence

Very closely spaced computed tracks may be based on strongly overlapping image information. The output contains more points but not proportionally more independent evidence. Density of reported data should not be confused with density of independent information.

### 4.5 All five versus the task budget

There is no best coverage family without a declared task. A family optimised for coarse translation can be inadequate for strain, rotation, crack opening, material loss, or three-dimensional deformation.

---

## 5. Operational Coverage Audit

Coverage should be treated as an auditable proposal rather than an intuition declared once.

### Step 1 — declare the modelling demand

Record:

```text
task
region of interest
time interval
working tolerance
required dimensions or projected coordinates
smallest motion distinction that would alter the answer
```

### Step 2 — inspect the five aspects before tracking

For the initial seed layout, record:

```text
extent          which regions are reached?
density         where are the largest gaps?
balance         where are clusters and deserts?
distinctiveness which features are likely to remain identifiable?
observability   where would relevant alternative motions disagree?
```

### Step 3 — run the tracker and remove nominal coverage that did not become usable coverage

Flag:

```text
lost tracks
identity swaps
occlusions
pattern degradation
out-of-view motion
features that do not move with the underlying material
```

### Step 4 — run the redundancy and lumping audit

Compute or judge the bundles produced by the current family at the declared tolerance.

### Step 5 — densify adversarially

Do not add new seeds only where tracking is already easy. Add them where the current claim is most vulnerable:

```text
largest untracked gaps
underrepresented extremities
suspected bundle boundaries
high-gradient regions
joints, cracks, contacts, and interfaces
regions with ambiguous or lost tracks
locations where competing motion descriptions differ most
```

### Step 6 — repeat and test stability

Compare before and after densification:

```text
bundle count
bundle membership
bundle boundaries
representative-track choice
validity intervals
```

If these change materially, the earlier coverage was inadequate.

If they remain stable under several strategically different densifications, confidence in the seeding improves.

### Step 7 — record what densification cannot repair

Even complete stability under additional seeds does not show that no sub-resolution transport occurred. The certificate must retain its apparatus and tolerance scope.

A compact ledger could be:

```text
COVERAGE LEDGER

family:       F_3
ROI:          marked ball surface visible to both cameras
interval:     [t0,t4]
tolerance:    epsilon_loose
task:         coarse translational target through impact

extent:       pass — visible front surface and extremities represented

density:      pass — no gap exceeds declared deformation scale

balance:      pass with deliberate oversampling at contact region

distinctive:  conditional — three marks briefly blurred at maximum contact

observable:   pass for translation and gross fission; not licensed for internal
              three-dimensional strain on the hidden rear surface

densification audit:
              bundle count and validity history unchanged after 20 new seeds

remaining residue:
              hidden rear face and sub-resolution material departure
```

---

## 6. The Two Coverage Residues

The project’s existing coverage account distinguishes two residues.

## 6.1 Seeding residue — dischargeable by further sampling

```text
seeding residue :=
did the selected family contain enough well-placed usable tracks?
```

The five aspects primarily decompose this question. Because the video or scene record persists, the modeller can add seeds and re-run the analysis. A changed lumping result convicts the earlier family.

The seeding residue is therefore not blind faith. It supports a standing audit:

```text
densify -> re-track -> re-lump -> compare
```

No finite sequence proves perfect coverage, but poor coverage can be exposed, and confidence can be increased through stability under adversarial densification.

## 6.2 Resolution residue — permanent for the present apparatus

```text
resolution residue :=
could relevant material transport or motion occur below what the apparatus
can distinguish?
```

Examples include:

```text
evaporation
ablation
sub-pixel fragments
motion behind an opaque surface
features smaller than optical resolution
events faster than the frame interval
```

Densifying seeds adds samples at the existing resolution. It does not manufacture finer spatial, temporal, depth, or material resolution.

This is the remaining probably-no:

```text
probably no task-relevant process occurred beneath the measurement boundary
```

The honest result is therefore never:

```text
coverage proved absolutely
```

It is:

```text
coverage supported for this task, tolerance, interval, region, and apparatus
```

---

## 7. Industrial Appearance I — Digital Image Correlation

Digital Image Correlation (DIC) is the closest mature engineering analogue to the NML2.2 scene-to-tracks problem.

A DIC experiment typically:

```text
applies or uses a visible surface pattern
records the specimen before and during deformation
matches local image subsets between frames
constructs a full-field displacement map
calculates strain or other derived quantities
```

The International Digital Image Correlation Society’s good-practice guide requires practitioners to define the **quantity of interest**, **region of interest**, and **field of view** before measurement. It also discusses pattern feature size, random variation, density, subset size, step size, spatial gradients, and measurement resolution.[^idics]

The five-aspect crosswalk is direct.

### Extent in DIC

Industry terms:

```text
region of interest (ROI)
field of view (FOV)
common field of view in stereo-DIC
line of sight
```

The relevant specimen region must be visible and remain inside the effective field of view throughout the test. In stereo-DIC, only the region shared by both camera views supports the stereo reconstruction.

### Density in DIC

Industry terms:

```text
pattern feature density
subset size
step size
spatial resolution
```

A local subset must contain enough pattern information to be matched. The iDICs guide gives a rule of thumb that a subset contain at least three pattern features and explains that sparse patterns require larger subsets, which reduces spatial resolution.[^idics]

### Balance in DIC

Industry terms:

```text
feature distribution
pattern uniformity
variation across the ROI
```

A pattern may be globally dense but locally sparse. Engineering guidance therefore considers the distribution of feature sizes and densities across the region rather than only a global feature count.

### Distinctiveness in DIC

Industry terms:

```text
random pattern variation
unique subset identification
correlation quality
pattern degradation
```

The iDICs guide states that the pattern needs enough random variation for subsets in different image regions to be identified uniquely. A repeated or strongly oriented pattern may measure one motion component while failing to distinguish another.[^idics]

### Observability in DIC

Industry terms:

```text
quantity of interest
expected spatial gradients
critical feature
required spatial resolution
measurement design
```

The measurement is designed around the deformation quantity that must be recovered. High expected gradients may require a smaller field of view, higher image scale, smaller step size, or more concentrated scrutiny near an edge or critical feature.[^idics]

### Industrial example: rocket-engine hot-fire testing

NASA applied stereo DIC during full-scale J-2X rocket-engine hot-fire testing. Paired high-speed cameras and a stochastic high-contrast speckle pattern were used to collect three-dimensional, time-resolved displacement and strain data under an extreme test-stand environment. The motivation included replacing or augmenting local strain gauges with non-contact, full-field measurements that could reveal local and global hardware behaviour.[^gradl]

This is the industrial form of the coverage problem:

```text
Which visible surface must be represented?
At what spatial resolution?
With what pattern density and uniqueness?
Which regions and gradients are critical to the engineering decision?
```

---

## 8. Industrial Appearance II — Particle Image Velocimetry

Particle Image Velocimetry (PIV) provides the fluid-mechanics analogue.

A PIV experiment typically:

```text
seeds a fluid with tracer particles
illuminates a plane or volume
records particle images at separated times
estimates local particle displacement
reconstructs a velocity field
```

The International Towing Tank Conference’s specialist report describes PIV as measuring flow velocity indirectly from the displacement of seeding particles. It states that particle choice is critical, the seeding distribution should be as homogeneous as possible, and gives a practical rule of thumb of at least ten particles per interrogation area on average. It also stresses visibility and identifiability of particles and the management of reflections and background interference.[^ittc]

### Five-aspect crosswalk for PIV

| Coverage aspect | PIV appearance |
|---|---|
| Extent | The illuminated measurement area and camera field of view must span the flow region of interest. |
| Density | Each interrogation area needs enough tracer particles to produce a reliable displacement estimate. |
| Balance | Seeding should be approximately homogeneous; local particle deserts create holes or bias. |
| Distinctiveness | Tracers must scatter enough light and remain distinguishable from reflections, the model, and the background. |
| Observability | The light sheet, camera arrangement, spatial resolution, and timing must be chosen for the wake, vortex, boundary layer, or other flow feature being measured. |

PIV is especially important for the NML2.2 water-tap material because it demonstrates that a fluid need not arrive as a labelled collection of particles. Engineers deliberately create a trackable family by seeding the flow, and the quality of the recovered velocity field depends on how well that family covers the measurement region.

The analogy is not exact: standard PIV often correlates particle ensembles inside interrogation windows rather than preserving the identity of every individual tracer for a long interval. Particle Tracking Velocimetry is closer to literal long-lived tracks. Nevertheless, the coverage requirements are structurally the same.

---

## 9. Industrial Appearance III — Structural Health Monitoring and Optimal Sensor Placement

Structural Health Monitoring (SHM) supplies the clearest industrial form of **observability**.

Large structures cannot normally be instrumented continuously at every point. Sensors are finite, discrete, costly, and sometimes impossible to place at the most critical location. Engineers therefore ask:

```text
How many sensors are needed?
Where should they be placed?
Which unmeasured responses can be inferred from them?
Which damage states or modes will remain distinguishable?
```

Li, Coraddu, and Brennan frame this as an inverse-prediction problem: use measurements at monitored locations to predict the response at unmonitored locations. They note that a very dense network would improve information but is generally economically infeasible, motivating optimisation of sensor placement. Their demonstration places strain-gauge rosettes on a steel plate near a stress concentration.[^li]

### Five-aspect crosswalk for SHM

| Coverage aspect | SHM appearance |
|---|---|
| Extent | The sensor network must represent the structure or subsystem whose health claim is being made. |
| Density | Sensor spacing must be fine enough that damaging local responses do not occur entirely between sensors. |
| Balance | Sensors should not be wasted in mutually redundant locations while other comparable regions are neglected. |
| Distinctiveness | Sensor signals and modes must be separable enough to avoid confusing different structural states. |
| Observability | Locations are selected so that the target response, damage mode, or unmonitored state can be inferred. |

SHM also clarifies why “spread the points evenly” is not a complete rule. Optimal layouts are often intentionally non-uniform because stress concentrations, joints, inaccessible hotspots, and predicted mode shapes carry more information than quiet regions.

This supports the distinction:

```text
balance       prevents accidental sampling bias
observability justifies deliberate task-driven sampling bias
```

---

## 10. Cross-Industry Vocabulary Map

The same underlying requirements appear under different professional names.

| VD coverage aspect | DIC | PIV / PTV | Structural health monitoring |
|---|---|---|---|
| Extent | ROI, FOV, common stereo view, line of sight | measurement area, light-sheet extent, camera FOV | monitored domain, network reach, subsystem coverage |
| Density | feature density, subset/step size, spatial resolution | particles per interrogation area, vector spacing | sensor spacing, number of sensors, spatial sampling |
| Balance | feature distribution across ROI | homogeneous seeding | non-redundant allocation across structure |
| Distinctiveness | random variation, unique subset, correlation quality | visible and identifiable tracers, background rejection | distinguishable signal signatures or modes |
| Observability | QOI, expected gradients, critical feature | target flow structure, timing and optical geometry | optimal sensor placement, inverse prediction, modal observability |

This crosswalk is the main industrial grounding for retaining the five-part decomposition.

---

## 11. What Is Established and What Is New

The note should not overstate the literature.

### Established in engineering practice

The following requirements are mature and independently motivated:

```text
select the relevant region and field of view
sample finely enough for the expected spatial variation
avoid unrepresentative holes and clusters
use features or tracers that can be identified reliably
place measurements where the required states or failure modes are observable
state the limits imposed by resolution, noise, access, and cost
```

### Project-specific synthesis

The following is the VD Newton contribution:

```text
collecting these requirements under one pre-lumping concept: coverage
organising them into the five aspects:
  extent, density, balance, distinctiveness, observability
connecting coverage to bundle-count stability under densification
placing coverage beside the redundancy audit as the second half of the
persistence certificate
separating the dischargeable seeding residue from the permanent resolution
residue
```

So the principles are not invented from nothing. The **five-part packaging and its logical position in the scene-to-particle route are our construction**.

---

## 12. Proposed NML2.2 Demonstration

### Apparatus

```text
flexible rubber sheet, foam strip, marked bouncy ball, or thin plastic plate
high-contrast removable dots or printed patterns
phone or camera on a fixed support
simple grid overlay
```

### Prepare five deliberately defective patterns

```text
A. extent failure
   distinctive dense dots on only one half

B. density failure
   dots reach all extremities but leave very large internal gaps

C. balance failure
   many dots cluster in one visually convenient region

D. distinctiveness failure
   a repeated regular pattern of near-identical marks

E. observability failure
   a generally good pattern that omits the hinge, notch, contact zone, or
   opposite sides of the expected boundary
```

A sixth pattern can combine all five successfully, with deliberate extra density near the critical region.

### Motion sequence

Use motions that separate the aspects:

```text
common translation
rotation
uniform stretch
local bend
opening at a notch
brief impact deformation
partial tear or offshoot
```

### Student task

For each pattern:

1. identify which tracks can be constructed;
2. state which of the five aspects passes or fails;
3. infer the bundles at the declared tolerance;
4. add seeds where the claim is most vulnerable;
5. repeat the audit;
6. record whether the bundle result changed;
7. state the remaining resolution residue.

### Signature question

> The current tracks are all redundant. What must still be true before those tracks can license one target for the task?

Expected answer:

> The family must also cover the task-relevant scene: it must span the relevant region, leave no consequential gaps, distribute sampling appropriately, supply reliably distinguishable tracks, and expose the motion differences that could change the lumping result.

---

## 13. Compact Definition for the Lesson

A concise final definition is:

> **Coverage is the judgement that a track family spans the task-relevant scene with sufficient density, appropriate distribution, reliable distinctiveness, and motion-discriminating placement to expose any difference that would alter the lumping result at the working tolerance.**

A shorter student-facing form is:

> **The tracks cover the scene when they are spread and chosen well enough that a different relevant motion is unlikely to be hiding where we did not look.**

The associated checklist is:

```text
EXTENT          Did we reach every relevant region?
DENSITY         Could a different motion hide in a gap?
BALANCE         Did clusters leave comparable regions neglected?
DISTINCTIVENESS Can each selected feature be followed reliably?
OBSERVABILITY   Would the differences we care about reveal themselves here?
```

And the audit rule remains:

```text
densify strategically
-> re-track
-> re-lump
-> compare the target count, boundaries, and validity history
```

Stability supports the seeding judgement. It never erases the resolution residue.

---

## 14. Internal Project Sources

- `vd_trackability_scene_to_particles_d4-informing.md` — coverage as the pre-address licence; seeding/resolution split; densification and count stability.
- `NML2_student_facing_question_exercise_demonstration_bank_v1_d1.md` — B3.3 coverage audit, B3.7 count stability, B3.25 sub-resolution loss.
- `NML2_split_ratification_d1.md` — NML2.2 requirement that coverage and redundancy form the two halves of the persistence certificate.

## 15. External References

[^idics]: International Digital Image Correlation Society; Jones, E. M. C. and Iadicola, M. A. (eds.), *A Good Practices Guide for Digital Image Correlation*, 1st ed., 2018. DOI: [10.32720/idics/gpg.ed1/print.format](https://doi.org/10.32720/idics/gpg.ed1/print.format). The current iDICs guide has since received a second edition; the first edition is cited here because the specific ROI, FOV, pattern-variation, density, subset, and step-size passages used in this note are directly traceable to it.

[^gradl]: Gradl, P. R., “Digital Image Correlation Techniques Applied to Large Scale Rocket Engine Testing,” AIAA 2016-4977, 2016. DOI: [10.2514/6.2016-4977](https://doi.org/10.2514/6.2016-4977). NASA Technical Reports Server document 20160009712.

[^ittc]: The Specialist Committee on Detailed Flow Measurements, “Final Report and Recommendations to the 26th ITTC,” *Proceedings of the 26th International Towing Tank Conference*, Vol. II, 2011, especially the practical PIV/SPIV discussion on measurement area, homogeneous seeding, particle density, visibility, and identifiability.

[^li]: Li, S.; Coraddu, A.; Brennan, F., “A Framework for Optimal Sensor Placement to Support Structural Health Monitoring,” *Journal of Marine Science and Engineering* **10**(12), 1819, 2022. DOI: [10.3390/jmse10121819](https://doi.org/10.3390/jmse10121819).
