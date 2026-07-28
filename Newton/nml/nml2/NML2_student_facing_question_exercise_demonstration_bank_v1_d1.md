# NML2 Student-Facing Question, Exercise, and Demonstration Bank

**Status:** source-synthesis draft v1  
**Project:** VD Newton / classroom translation  
**Date:** 2026-07-11  
**Purpose:** consolidate every explicit and implied student-facing operation, question, exercise, investigation, demonstration, diagnostic, and boundary case found in the supplied NML1/NML2 and bridge documents; organise them loosely by UK educational level; and identify candidate critical questions that test whether students can run the relevant logical traces.

---

## 0. How to Read This Bank

This is not yet a single lesson plan or printable worksheet. It is the source bank from which those objects can be selected.

The bank distinguishes five kinds of classroom object:

1. **Primitive drill** — practises one small operation, sometimes as basic as identifying which number belongs to which object.
2. **Trace exercise** — makes the student perform several operations in the intended order.
3. **Critical question** — places one or more commitments under pressure and reveals whether the student understands a law-house or another load-bearing logical connection.
4. **Demonstration or investigation** — supplies perceptual experience or data from which a handle can be installed.
5. **Boundary probe** — tests whether the student stops when a quantity, address, or method is not licensed.

The level bands are deliberately loose:

- **Band I — upper primary to early secondary:** approximately KS2–KS3; mostly NML1 prerequisites and the accessible NML2B relation.
- **Band II — secondary to A level:** approximately KS3–KS5; formal Newton-II calculations, vectors, addressed bookkeeping, and introductory target audits.
- **Band III — university:** NML2A foundations, tolerance-indexed target construction, water-tap continuum, mass-address persistence, and advanced extensions.

The same logical operation may appear at more than one level in different clothing. Moving an exercise between bands should usually change its representation, not its underlying trace.

---

## 1. Current Curriculum Decisions Used in This Compilation

Where supplied documents represent different chronological stages, this bank uses the later/final position as the core and preserves earlier proposals with their status marked.

### 1.1 NML1 handoff

NML1 installs:

```text
trajectory in an inertial frame
  -> read velocity-change
  -> read inertial acceleration
```

The student should read motion-change before attempting to explain it.

### 1.2 NML2B: accessible Newton-II relation

For a supplied and already-certified massive target:

```text
inertial mass
inertial acceleration
net-force vector
```

are locked by:

$$
\mathbf F_{\mathrm{net}}[A]=m[A]\mathbf a[A].
$$

This is suitable for younger students when the target and its mass are supplied rather than audited.

### 1.3 NML2A: advanced target and mass-address discipline

University students should investigate how a scene earns a continuing massive-particle target:

```text
scene -> tracks -> redundancy under tolerance -> bundle -> target address
      -> mass address -> validity history -> licensed Newton-II use
```

This includes the bouncy-ball comparison at strict and loose tolerances and the water-tap sequence of slab-wise one-dimensional massive-particle representatives.

### 1.4 Net-force wall withheld

In NML2, net force is usable only as a thin, typed Newton-II quantity:

- it belongs to one selected massive target;
- it is a vector;
- it is measured in newtons;
- it is supplied or inferred through Newton II.

NML2 does not yet teach how force contributions are assembled into that vector. A newton meter measures a transmitted force contribution, not automatically the net force on the target.

### 1.5 Mass origination

Tracks establish the owner of a mass address, not the magnitude stored there. The current pipeline does not treat a weighing scale as an unexplained inertial-mass instrument. A mass value is supplied, previously certified, or established by an admissible dynamical comparison such as same-pull, same-time motion-change comparison.

### 1.6 Core versus extension

Mass additivity, centre of mass, force sum, momentum, impulse, Newton III, torque, deformation mechanics, fluid continuity, and open systems are not all part of a young core NML2 lesson. Some appear here as university investigations or as explicit later-boundary probes because the supplied documents suggested them.

---

## 2. What Makes a Question Critical?

The NML1 exemplar is:

> **A puck appears to curve while no other object influences it. What should you suspect?**

It is critical because the student cannot answer it by repeating one definition. They must run the Newton-I triplet:

```text
free-body + inertial-frame -> uniform-motion
```

Holding `free-body` fixed while `uniform-motion` fails puts pressure on `inertial-frame`. If the frame is confirmed inertial, pressure returns to the free-body classification.

An NML2 critical question should work similarly. It should test a load-bearing connection such as:

- all three Newton-II quantities must belong to the same target;
- acceleration is first read from motion and only then placed into force accounting;
- zero net force is not the same claim as no force contributions;
- a track-family licenses a mass address but does not calculate its value;
- present redundancy does not by itself bridge a past address failure;
- tolerance can change whether a one-target representation is licensed;
- a calculation must halt when its target or required referent is unlicensed.

A good critical question therefore has a recognisable **error shape**. It reveals not merely that the student is wrong, but which connection they failed to run.

---

## 3. Complete Inventory of Primitive Student Operations

These are the smallest operations implied by the documents. Any final worksheet should practise them before expecting students to run long traces.

| Code | Primitive operation | Minimal student action | Earliest likely band | Main source basis |
|---|---|---|---|---|
| O1 | Identify the demanded target | Circle the object whose acceleration, mass, or net force is being requested. | I | VD question-normalisation note; NML2 final draft |
| O2 | Identify every candidate target | Underline `boat`, `table`, `cup`, etc., once in the text and assign each a row. | I | Witness-sheet structure; user's classroom example |
| O3 | Identify quantity type | Sort values into mass, acceleration, net force, time, velocity, or position. | I | Newton-II entries; NML2 unit discipline |
| O4 | Attach a value to its owner | Write `5 kg -> boat`, not merely `m=5 kg`. | I | Mass-address ledger; witness sheets |
| O5 | Preserve target identity through notation | Rewrite `m`, `a`, and `F` as `m[A]`, `a[A]`, and `F_net[A]`. | II | NML2 final draft |
| O6 | Reject cross-target substitution | Detect that `F_net[boat]/m[table]` is not the boat's acceleration. | I–II | Newton-II same-target lock |
| O7 | Separate scalar from vector | Mark mass as scalar and acceleration/net force as vectors. | I–II | Newton-II triplet and wall definitions |
| O8 | Supply vector direction | Add `left`, `right`, `up`, `down`, or an arrow to every nonzero force and acceleration. | I–II | NML2 vector discipline |
| O9 | Match units to types | Match kg to mass, N to net force, and m/s² to acceleration. | I | NML2 unit section |
| O10 | Build the newton unit | Complete `1 N = 1 kg m/s²`. | II | Newton II unit derivation |
| O11 | Distinguish zero from missing | Choose among `0`, `unknown`, `not supplied`, and `not defined`. | II–III | Zero case; VD question-answering outcomes |
| O12 | Distinguish path from trajectory | Decide whether time/equal-time information is present. | I–II | Kinematic entries; NML1 E7 sheet |
| O13 | Read motion-change | Draw or calculate how velocity changes from the trajectory. | I–II | NML1 E7 |
| O14 | Qualify the frame | State whether the acceleration is read in an inertial frame. | II | E7 placement and decision notes |
| O15 | Transfer the E7 readout | Put the already-read acceleration into the massive target's force-accounting sheet. | II | E7/E8 witness-sheet decision |
| O16 | Infer net force | Given `m[A]` and `a[A]`, calculate `F_net[A]`. | I–II | Withheld-wall note |
| O17 | Predict acceleration | Given `m[A]` and a supplied `F_net[A]`, calculate `a[A]`. | I–II | NML2 core constraints/final draft |
| O18 | Infer inertial mass | Given nonzero `a[A]` and `F_net[A]`, calculate `m[A]`. | II | NML2 algebraic forms |
| O19 | Use qualitative proportionality | Compare cases without calculation: more force gives more acceleration; more mass gives less acceleration. | I | NML2 core constraints |
| O20 | Hold time interval fixed | Check that compared pushes or velocity changes use the same duration. | I–II | NML2 equal-time requirement |
| O21 | Handle the zero case | From finite positive `m` and `a=0`, return `F_net=0`; refuse to infer mass by dividing `0/0`. | II | Critical zero question |
| O22 | Update velocity | Use acceleration over an equal time step to draw or calculate the next velocity. | I–II | Force-to-path sheet |
| O23 | Update position/path | Extend the next path segment using the updated velocity. | I–II | NML2 final worksheet |
| O24 | Identify the selected track-family | Mark which visible points are being considered together. | II–III | Trackability and final draft |
| O25 | Re-identify a point through frames | Follow the same feature through time and produce a track. | I–III | Trackability ground/tracker |
| O26 | Compare relative displacement | Decide whether track offsets remain constant within tolerance. | II–III | Redundancy definition |
| O27 | State the working tolerance | Record what discrepancies are being ignored and why. | II–III | NML2 final draft; trackability note |
| O28 | Respect the tolerance floor | Reject a tolerance finer than the tracking procedure can resolve. | III | Trackability tracker section |
| O29 | Respect the tolerance budget | Reject a tolerance so loose that it merges the intended target with another object or loses required accuracy. | II–III | Bouncy-ball investigation |
| O30 | Form redundant bundles | Group tracks into maximal pairwise-redundant sets at the stated tolerance. | III | Trackability lumping/clique sections |
| O31 | Choose a representative track | Use one member to represent only the licensed motion information of its bundle. | II–III | Lumping licence |
| O32 | Count targets as an output | Report how many particle targets the family/tolerance produces, rather than assuming a body count in advance. | III | “Bodies are outputs” note |
| O33 | Densify and re-audit | Add seed tracks and check whether the target count changes. | III | Coverage and count-stability sections |
| O34 | Separate address from value | Distinguish `A`, `m[A]`, and `m[A]=2 kg`. | I–III | Mass ledger |
| O35 | Record a validity interval | Write `valid(A; epsilon, [t0,t1], task)`. | III | Final draft and mass pipeline |
| O36 | Detect an address break | Mark the interval where redundancy fails at the working tolerance. | II–III | Bouncy ball, splatter, convoy |
| O37 | Search for an acceptable bridge | Test whether a coarser or reduced representation remains continuous through the failed interval. | III | Fine–coarse–fine bridge |
| O38 | Distinguish carried from reconstructed address use | Say whether the address is continuously usable or only its value is reconstructable before/after. | III | Trackability defeat taxonomy |
| O39 | Detect offshoot tracks | Notice material departure and expire the mass certificate. | III | Mass-persistence pipeline |
| O40 | Halt rather than guess | Write `ADDRESS NOT LICENSED` when no bridge or new value is supplied. | I–III | Required halt row |
| O41 | Identify measurement provenance | Say whether a value was supplied, dynamically certified, inferred by Newton II, or assembled by bookkeeping. | II–III | Mass pipeline; withheld-wall note |
| O42 | Distinguish inference from construction | Say that `F_net=ma` inferred a net-force value but did not identify its physical contributions. | II–III | Withheld net-force wall |
| O43 | Distinguish proxy from full account | State which degrees of freedom a representative track keeps and discards. | III | Trackability bridge/spinning wheel |
| O44 | Distinguish one, ordered many, and disordered many | Classify block, tap stream, and splatter. | III | Trackability ladder |
| O45 | Project tracks onto a modelled dimension | Test redundancy of `z(t)` even when full three-dimensional redundancy fails. | III | Tap example plus current clarification |
| O46 | Index a continuous target family | Label water slabs by emission/material parameter and attach a supplied `dm` to each address. | III | Tap example plus current clarification |
| O47 | Separate prediction from retrospective repair | State whether the tolerance/address certificate existed before prediction or was revised afterwards. | III | Final teacher-theory note |
| O48 | Recognise a domain halt | Explain why a photon path question can terminate while a Newton-II inertial-mass question does not. | II–III | VD question-answering; E7/E8 notes |
| O49 | Derive a composite translational representative | Under explicit shared-acceleration and adequacy assumptions, derive `M=sum m_i` and/or `a_CM=A`. | III extension | COM and bridge notes |
| O50 | Mark the NML3 boundary | When asked where the net-force value came from, answer that force-contribution construction is the next lesson. | I–III | NML2/NML3 handoff |

---

## 4. Candidate Critical Questions

The questions below are intended to play the role that the curving-puck question plays in NML1. They are not all equally central; the strongest signature candidates are marked **Signature candidate**.

### CQ0 — NML1 exemplar: the curving free puck

> A puck appears to curve while no other object influences it. What should you suspect?

Expected route:

```text
free-body + inertial-frame -> uniform-motion
free-body is held fixed
uniform-motion fails
therefore inspect inertial-frame
if frame is confirmed inertial, inspect free-body classification
```

Main error exposed: premature import of a hidden force while erasing the frame commitment.

### CQ1 — Same-target Newton-II lock

**Signature candidate for younger NML2B**

> A boat has mass 5 kg and supplied net force 20 N to the right. A table has mass 10 kg and supplied net force 50 N to the right. A cup has mass 5 kg and supplied net force 25 N to the left. A student calculates the boat's acceleration using `50 N / 5 kg`. What is wrong?

Expected route:

```text
the 50 N value belongs to the table
the boat calculation must use F_net[boat] and m[boat]
a[boat] = 20 N / 5 kg = 4 m/s² right
```

Main error exposed: treating the triplet as a relation among free-floating numbers rather than three quantities owned by one target.

### CQ2 — Acceleration readout versus Newton-II account

> A trajectory shows an acceleration of 3 m/s² to the left. Have you already discovered the force contribution that physically produced it?

Expected answer:

> No. The trajectory supplies the inertial-acceleration readout. If the target's mass is known, Newton II can infer the corresponding net-force vector. It does not yet identify the force contributions or acting objects that produce that value.

Main errors exposed: force-as-arrow collapse; confusing net-force inference with force construction.

### CQ3 — The typed mystery slot

**Signature candidate for formal NML2B**

> Target `A` has `m[A]=3 kg`, and its trajectory gives `a[A]=2 m/s²` to the left. What does Newton II demand, and what does it not yet tell you?

Expected answer:

$$
\mathbf F_{\mathrm{net}}[A]=6\,\mathrm N\text{ left}.
$$

Newton II demands one addressed net-force vector of that value. It does not yet say which force contributions make it up or that a meter independently measured it.

### CQ4 — Zero acceleration

**Signature candidate for the zero branch**

> A massive target has zero inertial acceleration. What follows, and what does not follow?

Expected route:

```text
finite positive m and a=0 -> F_net=0
does not imply: no force contributions exist
does not imply: target is free
does not allow: infer m by F/a
```

Main errors exposed: zero/no-things collapse; Newton I/Newton II collapse; division by zero.

### CQ5 — Meter reading versus net force

> A newton meter reads 7 N while pulling a cart. May you immediately write `F_net[cart]=7 N`?

Expected answer:

> Not from the meter reading alone. The meter supplies one transmitted force contribution. Calling it the net-force value requires a later force-accounting certificate that no other relevant contributions alter the target's net force.

Main error exposed: treating a force sensor as an automatic net-force meter.

### CQ6 — What did the tracks establish?

> Several marker tracks earn target address `A`. Did the track analysis establish `m[A]=2 kg`?

Expected answer:

> No. It established which continuing target owns the mass slot. The magnitude must be supplied or originated dynamically.

Main error exposed: deriving inertial-mass magnitude from kinematics.

### CQ7 — The returning-redundancy trap

> A track-family is redundant, then becomes nonredundant, and later becomes redundant again. Does the later redundancy automatically restore the earlier mass address?

Expected answer:

> No. It licenses a present bundle. Reuse of the earlier mass address or value requires a continuous acceptable bridge, a no-offshoot reconstruction, or a new origination procedure, depending on the case.

Main error exposed: confusing present internal redundancy with historical lineage.

### CQ8 — Bouncy ball at two tolerances

**Signature candidate for university NML2A**

> A marked bouncy ball strikes a wall. At strict tolerance its tracks are `pass -> fail -> pass`; at loose tolerance they are `pass -> pass -> pass`. Did the target break during the bounce?

Expected answer:

> At strict tolerance, the one-point proxy fails during contact and the fine address is unavailable during that interval; the before/after value may be bridge-reconstructed if all material tracks remain accounted for. At an acceptable loose tolerance, one address is continuously licensed through the bounce. “The target broke” is therefore incomplete without the tolerance and modelling task.

Main errors exposed: tolerance erasure; treating model-relative address validity as an absolute metaphysical fact.

### CQ9 — Tolerance budget

> Why not choose a tolerance so loose that the bouncy ball always remains one target?

Expected answer:

> The tolerance must still distinguish the ball from the wall and other targets and preserve the accuracy required by the translational question. Beyond that budget, the model no longer answers the intended question.

Main error exposed: treating tolerance as an unrestricted escape from model failure.

### CQ10 — Water tap: one, many, or none?

**Signature candidate for the university continuum extension**

> A steady water jet narrows as it falls. Is the whole column one translationally redundant point-particle target? If not, how can it nevertheless be represented by a continuous stream of masses `dm`?

Expected route:

```text
whole stream: not one bundle; parcels emitted earlier move faster and separations change
thin material slab: tracks approximately share the local downward motion within tolerance
full 3D redundancy may fail because of transverse contraction
projected/downward redundancy may still hold for the intended 1D model
each slab earns its own address A_tau and supplied mass dm
continuous emission gives an ordered, continuously indexed family {A_tau}
```

Main errors exposed: lumping the entire stream into one particle; assuming full three-dimensional rigidity; confusing one continuously indexed family with one target.

### CQ11 — Spinning wheel

> A wheel is rigid in the ordinary distance-preserving sense. May any rim track represent the wheel's complete translational motion?

Expected answer:

> Not by redundancy alone. Fixed distances permit rotation, while rim tracks have different velocities. The one-track proxy fails even though a later centre-of-mass account may remain valid.

Main error exposed: rigidity/redundancy collapse; proxy/account collapse.

### CQ12 — Convoy

> Several cars keep fixed offsets for ten seconds. Does the redundant bundle prove that they form one dynamically cohesive body?

Expected answer:

> No. Redundancy licences a kinematic proxy over that interval. When one car brakes, the earlier lumping is defeated. Cohesion is a later dynamical question.

Main error exposed: treating kinematic co-motion as proof of internal constraint or bodyhood.

### CQ13 — Offshoot and expiry

> A chip flies off a previously licensed brick target. May the old mass value continue to be used for the remainder?

Expected answer:

> No. The offshoot expires the old mass certificate. The remainder and chip need revalidation or new values; NML2 must not silently assign the old value to the remainder.

Main error exposed: carrying a mass value after material departure.

### CQ14 — Prediction versus retrospective repair

> After seeing an unexpected deformation, a modeller chooses a coarser tolerance that would have preserved the target. Does that make the original advance prediction licensed?

Expected answer:

> No. It creates a new retrospective account. An advance prediction requires the tolerance and address certificate at its past boundary before the predicted interval is traversed.

Main error exposed: retroactively disguising a changed model as prior knowledge.

### CQ15 — Photon question normalisation

> Why can “What path does a free photon follow?” have an answer while “What Newton-II inertial acceleration does the photon have?” halts?

Expected answer:

> The questions demand different headwords. The path question can use the Newton-I/free-particle route. The Newton-II route demands an inertial-mass referent, which a photon lacks in this Newtonian model.

Main error exposed: treating objects rather than questions as the sole routing determinant; confusing undefined with zero.

### CQ16 — Composite representative

> Two already-priced parts share one translational acceleration. What additional commitment is needed before their one-point representative may be assigned `M=m1+m2`?

Expected answer:

> A representative-adequacy or restricted account-aggregation commitment is needed. Shared motion alone does not manufacture mass additivity. This is a university extension, not a primitive NML2B result.

Main error exposed: claiming that redundancy alone derives additive mass.

### CQ17 — Where does the next question begin?

> You know `m[A]` and have inferred `F_net[A]=6 N` from the trajectory. What is the next unresolved mechanics question?

Expected answer:

> Which force contributions and acting objects produce that net-force vector? That is the NML3 force-sum branch.

Main error exposed: false completion of the physical explanation at Newton II.

### CQ18 — Does the triplet generate values by itself?

**Signature candidate for understanding Newton II as a triplet**

> Newton II can be written `a=F_net/m`, `F_net=ma`, and `m=|F_net|/|a|` in a suitable nonzero aligned trial. If no values are supplied, which quantity does the triplet calculate first?

Expected answer:

> None. These are three rearrangements of one law constraint, not three independent value-producing equations. Newton II locks the three quantities together. Two independent addressed values, or equivalent external constraints, are required to determine the third.

Follow-up:

> If only the mass is supplied, can Newton II determine both force and acceleration?

Expected answer: no; infinitely many force–acceleration pairs satisfy the same mass.

Main errors exposed: treating circular definitions as a numerical algorithm with no inputs; treating force, mass, or acceleration as privileged by the triplet itself.

---

## 5. Band I — Upper Primary to Early Secondary

The central Band-I achievement is not advanced target construction. It is disciplined execution of NML2B under a supplied-target convention:

```text
identify the target
-> find that target's mass and supplied/inferred net force
-> keep the quantities together
-> calculate or compare acceleration
-> preserve direction
```

### 5.1 Primitive reading and ownership drills

#### B1.1 — Circle each object's mass

Prompt:

> Read the question. Circle the mass of the boat, underline the mass of the table, and put a box around the mass of the cup.
>
> The boat has a mass of 5 kg. The table has a mass of 10 kg. The cup has a mass of 5 kg.

Operation installed: attaching mass values to named targets before calculation.

#### B1.2 — Circle the requested target

Prompt:

> The paragraph contains information about a boat, table, and cup. The question asks for the cup's acceleration. Circle the word naming the target you must calculate for.

Operation installed: question normalisation at its most primitive level.

#### B1.3 — Draw owner lines

Prompt:

```text
boat                 10 kg
table                 5 kg
cup                   5 kg
```

> Draw a line from each object to the mass stated for it in the sentence above. Do not calculate yet.

Variation: place the values in a different visual order from the nouns so that spatial proximity cannot replace reading.

#### B1.4 — Quantity sorting

Give cards:

```text
5 kg
20 N right
4 m/s² right
2 s
3 m/s left
```

Ask students to place them under:

```text
mass | net force | acceleration | time | velocity
```

#### B1.5 — Unit spotting

Prompts:

1. Circle every value measured in kilograms.
2. Underline every value measured in newtons.
3. Put a box around every value measured in metres per second squared.
4. Which values need a direction to be complete?

Expected answer to 4: nonzero net-force and acceleration vectors.

#### B1.6 — Direction completion

Prompt:

> A cup has mass 5 kg. Its supplied net-force vector is 25 N to the left. Complete: its acceleration is ____ m/s² to the ____.

Expected answer: `5 m/s² to the left`.

#### B1.7 — Same-row copying

Students fill one row per target before calculating:

| Target | Mass | Supplied net force | Acceleration |
|---|---:|---|---|
| Boat |  |  |  |
| Table |  |  |  |
| Cup |  |  |  |

The instruction should explicitly say:

> Copy all of one object's information into one row. Never borrow a number from another row.

#### B1.8 — Irrelevant-number restraint

Prompt:

> A 5 kg boat is 2 m long and has a supplied net force of 20 N to the right. Which two numbers are needed to find its acceleration? Cross out the unused number.

Expected selection: `5 kg` and `20 N`; cross out `2 m`.

#### B1.9 — Symbol ownership

Prompt:

> Replace each blank with `boat`, `table`, or `cup`:

```text
m[____] = 5 kg
F_net[____] = 20 N right
a[____] = F_net[____] / m[____]
```

All blanks in one equation must name the same target.

### 5.2 Primitive Newton-II drills

#### B1.10 — Divide force by mass

Use integer cases initially:

| Target | Mass | Supplied net force | Find acceleration |
|---|---:|---:|---:|
| Boat | 5 kg | 20 N right | `4 m/s² right` |
| Table | 10 kg | 50 N right | `5 m/s² right` |
| Cup | 5 kg | 25 N left | `5 m/s² left` |

Follow-up:

> The table and cup have different masses and different net forces. Can they nevertheless have the same acceleration?

Expected answer: yes; both have magnitude `5 m/s²` in this data set, though their directions differ.

#### B1.11 — Cross-target trap

Offer three proposed boat calculations:

```text
A. 20 N / 5 kg
B. 50 N / 5 kg
C. 25 N / 10 kg
```

Ask:

> Circle the calculation that uses only the boat's values. Explain why the others are illegal before saying whether the arithmetic is correct.

#### B1.12 — Same mass, larger supplied net force

Prompt:

> Cart A and Cart B each have mass 4 kg. Cart A has a supplied net force of 4 N. Cart B has a supplied net force of 12 N. Which cart has the larger acceleration? How many times larger?

Expected answer: Cart B; three times larger.

#### B1.13 — Same supplied net force, larger mass

Prompt:

> Cart A has mass 2 kg. Cart B has mass 6 kg. Each has a supplied net force of 12 N to the right. Which cart accelerates more? Calculate both accelerations.

Expected answer: `6 m/s²` and `2 m/s²`; the lighter cart accelerates more.

#### B1.14 — More/less without numbers

Students complete arrows:

```text
same mass + bigger supplied net force -> __________ acceleration
same supplied net force + bigger mass -> __________ acceleration
```

Expected words: `bigger`, `smaller`.

#### B1.15 — Same time check

Prompt:

> Cart A is pushed for 1 second. Cart B is pushed for 4 seconds. Their velocity changes are different. Can this alone show which cart has more inertial mass?

Expected answer: no; the time intervals must be controlled or acceleration must be compared.

Then give a corrected pair with equal durations.

#### B1.16 — Infer the mystery net-force value

Prompt:

> A target has mass 3 kg. Its motion sheet shows an acceleration of 4 m/s² downward. What net-force vector does Newton II demand?

Expected answer: `12 N downward`.

Add:

> Did this calculation tell you which physical objects supplied the force contributions?

Expected answer: no.

#### B1.17 — Zero card sort

Give four response cards:

```text
F_net = 0
no force contributions exist
the target is free
mass = 0
```

Prompt:

> A finite-mass target has zero acceleration. Select only the conclusion licensed by Newton II.

Expected selection: `F_net = 0`.

#### B1.18 — Build the unit

Prompt:

> A 1 kg target accelerates at 1 m/s². Newton II assigns a net-force magnitude of 1 ____.

Expected answer: `newton`.

Then complete:

```text
1 N = 1 ____ × 1 ____
```

Expected answer: `kg` and `m/s²`.

### 5.3 NML1/E7 prerequisite drills retained for Band I

These are drawn directly from the integrated NML1 lesson because NML2 calculations are supposed to account for an acceleration students can already read.

#### B1.19 — Follow the path

At each marked point on a curve, draw a short arrow toward the inside of the turn. Use:

1. straight equal-dot path;
2. gentle curve;
3. tight curve;
4. S-curve;
5. circle;
6. car turning;
7. Moon around Earth;
8. straight falling path with equal-time dots spreading.

#### B1.20 — Motion-change classification

For each trajectory, tick:

```text
[ ] speeding up
[ ] slowing down
[ ] turning
[ ] changing speed and direction
[ ] zero motion-change
```

#### B1.21 — Read before explaining

Prompt:

> Draw how the motion changes. Only after every arrow is drawn, write one sentence about what might shape the path.

Operation installed: delaying causal/force vocabulary until the kinematic readout is complete.

#### B1.22 — Arrow identity

Prompt:

> You drew an inward motion-change arrow. Is it already a force arrow?

Expected answer: no; it is an acceleration/motion-change readout.

### 5.4 Larger Band-I exercises

#### E1 — Three-target data-owner sheet

Give a short story containing three objects, their masses, supplied net-force vectors, and two distractor quantities. Students must:

1. circle the demanded target;
2. colour every value by owner;
3. copy values into one row per target;
4. select the correct row;
5. calculate acceleration;
6. state direction and unit;
7. check that no other target's value entered the equation.

This is the direct expansion of the boat/table/cup operation proposed by the user.

#### E2 — Newton-II quantity-card triangle

Give each target a three-slot card:

```text
TARGET: ______

mass:             ______ kg
acceleration:     ______ m/s², direction ______
net force:        ______ N, direction ______
```

Fill any two slots and ask the student to complete the third. Use separate coloured cards for separate targets and forbid swapping cards between them.

#### E3 — Same-action comparison ladder

Present four already-certified masses receiving the same repeatable sideways action for the same duration. Students order the expected motion-changes from largest to smallest before seeing data. Then reveal the recorded velocity changes.

Do not present the action device as an automatic net-force meter. At this level the demonstration supports qualitative inertial-mass intuition.

#### E4 — Mystery-force worksheet

For each row, provide:

```text
target name
mass
trajectory-read acceleration arrow
```

Students draw the matching net-force arrow and calculate its magnitude. The heading should say:

> Newton II tells us which net-force value belongs in the mystery slot. A later lesson asks what physical contributions fill it.

#### E5 — Equal-time arrow path builder

Use arrow tiles rather than equations:

1. give an initial velocity arrow;
2. give a supplied acceleration arrow for the next equal time step;
3. combine them to make the next velocity arrow;
4. draw the next path segment;
5. repeat.

Include straight acceleration, opposite acceleration, sideways acceleration, and zero acceleration.

#### E6 — The deliberate halt row

Even at Band I, include one row saying:

```text
The label identifying which object owns the mass has been lost.
```

Offer:

```text
[ ] guess the nearest mass number
[ ] use another object's mass
[ ] stop and ask which target the mass belongs to
```

Expected response: stop and ask. This is the seed of the later mass-address discipline.

### 5.5 Band-I demonstrations

#### D1 — Hanging balls struck sideways

Suspend balls with different already-known inertial masses. Use a repeatable striker if possible and focus on the initial sideways velocity change. Intended noticing:

```text
same repeatable action -> heavier target changes motion less
```

Status: qualitative, pre-formal intuition. A hand tap is not a controlled force history, and the later swing involves gravity and tension.

#### D2 — Low-friction carts with equal-duration action

Compare carts of different already-certified masses under the same repeatable action programme for the same duration. Record equal-time positions or velocity arrows.

Status: useful if described as a repeatable action source. Do not call its reading `net force` without the later force-accounting certificate.

#### D3 — Many marks on one translating cart

Show one marker track first, ask students to read the acceleration, then reveal several markers moving together. Ask:

> Do all of these marks give new translational motion information, or do they repeat the same information?

This is an early perceptual seed of redundancy. Do not yet demand formal tolerance analysis.

#### D4 — Very massive object thought demonstration

Compare a ball, cart, and Earth under the same imagined interaction scale. Ask why the Earth's motion-change may be too small to notice. Use only the mass-side idea; do not open Newton III calculations.

### 5.6 Band-I exit questions

1. Which target are you calculating for?
2. Which mass belongs to that target?
3. Which supplied net-force vector belongs to that target?
4. Does your answer include `m/s²` and a direction?
5. If acceleration is zero, what Newton-II value is zero?
6. Did the trajectory tell you the force contributions, or only the motion-change?
7. What question must you ask if a mass number appears without a clear owner?

---

## 6. Band II — Secondary to A Level

Band II formalises NML2B and begins to expose the bookkeeping that ordinary textbook diagrams hide. Students should calculate fluently, but also audit the type, owner, direction, interval, and provenance of every quantity.

### 6.1 Question-normalisation and data-selection drills

#### B2.1 — What is the question actually asking for?

For each natural-language question, students write the requested addressed quantity:

| Natural-language question | Normalised demand |
|---|---|
| What is the boat's acceleration? | `a[boat]` |
| What net force is required by the cup's observed motion? | `F_net[cup]` |
| What inertial mass makes the table's force and acceleration fit? | `m[table]` |
| What is the photon's Newton-II acceleration? | demands a mass referent; later boundary probe |

#### B2.2 — Given, demanded, irrelevant

Students annotate each sentence with:

```text
G = given and needed
D = demanded
I = irrelevant to this calculation
B = boundary/assumption that must be checked
```

Include target identity, frame statement, time interval, mass, supplied net force, acceleration, dimensions, colours, and nearby-object data.

#### B2.3 — One target, one row, one interval

Give data for targets `A`, `B`, and `C` at times `t0`, `t1`, and `t2`. Students may combine values only when target and modelling interval match.

Example traps:

```text
m[A] at t0 with F_net[B] at t0
m[A] at t0 with a[A] from a different trial
F_net[A] in an inertial frame with a[A] read in an accelerating frame
```

#### B2.4 — Repair the notation

Prompt:

> The line `a = 24 N / 6 kg` appears in a three-object problem. Rewrite it so its target, direction, and interval are visible.

Possible answer:

$$
\mathbf a[A;t_0,t_1]
=\frac{\mathbf F_{\mathrm{net}}[A;t_0,t_1]}{m[A]}
=4\,\mathrm{m/s^2}\text{ right}.
$$

#### B2.5 — Complete the force-accounting sheet

Use the witness-sheet distinction:

```text
MOTION SHEET
target; frame; trajectory; velocity; trajectory-read acceleration

MASSIVE-TARGET FORCE-ACCOUNTING SHEET
same target; inertial mass; net force; Newton-II acceleration role
```

Students draw a line showing that both sheets refer to the same target. They must not draw one particle “inside” another.

### 6.2 Formal Newton-II exercises

#### B2.6 — Three algebraic forms

Rotate through the three prompts from the documents:

1. Given `m[A]` and `a[A]`, what net-force vector is demanded by the motion?
2. Given supplied `F_net[A]` and `m[A]`, what acceleration should be read from the predicted trajectory?
3. Given nonzero `a[A]` and supplied/inferred `F_net[A]`, what inertial-mass value makes them fit?

Every answer must include the target address, unit, and direction where applicable.

#### B2.6A — Triplet input-count drill

For each row, students decide whether Newton II can return a unique value:

| Values supplied for one addressed target | Unique result? |
|---|---|
| none | no |
| mass only | no |
| net force only | no |
| acceleration only | no |
| mass and net force | yes: acceleration |
| mass and acceleration | yes: net force |
| nonzero aligned net force and acceleration | yes: mass magnitude |
| all three | no new unknown; perform a consistency check |

Finish with CQ18: the triplet constrains values; it does not generate empirical inputs from nothing.

#### B2.7 — Mixed three-form grid

| Target | `m` | `F_net` | `a` | Requested operation |
|---|---:|---|---|---|
| A | 4 kg | — | 3 m/s² east | infer `F_net` |
| B | 6 kg | 18 N west | — | predict `a` |
| C | — | 20 N north | 5 m/s² north | infer `m` |
| D | — | 0 N | 0 m/s² | state why `m` is not inferable |

Expected numerical answers: `12 N east`, `3 m/s² west`, `4 kg`, and `indeterminate by this trial`.

#### B2.8 — Unit-valid but target-invalid

Give equations whose units work but whose owner tags do not:

$$
\mathbf F_{\mathrm{net}}[A]=m[B]\mathbf a[A].
$$

Ask:

> Is dimensional consistency enough to make an equation a valid Newton-II account?

Expected answer: no; target binding is an independent requirement.

#### B2.9 — Target-valid but direction-incomplete

Prompt:

> `m[A]=2 kg`, `|F_net[A]|=8 N`, and the force points south. A student writes `a[A]=4 m/s²`. What information is missing?

Expected answer: direction; `4 m/s² south`.

#### B2.10 — Vector components

Given:

$$
m[A]=2\,\mathrm{kg},\qquad
\mathbf F_{\mathrm{net}}[A]=(6\hat{\mathbf i}-8\hat{\mathbf j})\,\mathrm N,
$$

find `a[A]`, its magnitude, and direction. Then ask whether mass changed either component's direction.

Expected vector: `(3 i - 4 j) m/s²`, magnitude `5 m/s²`.

#### B2.11 — Ratio questions

Without substituting numbers, students answer:

1. If `F_net` doubles at fixed mass, what happens to acceleration?
2. If mass triples at fixed `F_net`, what happens to acceleration?
3. If mass and `F_net` both double, what happens to acceleration?
4. If acceleration halves while mass stays fixed, what happens to the Newton-II net-force value?

#### B2.12 — Equal-duration velocity change

Given the same supplied net-force magnitude acting for the same interval `Delta t`:

$$
\Delta\mathbf v=\frac{\mathbf F_{\mathrm{net}}\Delta t}{m},
$$

students compare targets of mass `m`, `2m`, and `4m`. Then change only the time interval and ask why a raw `Delta v` comparison no longer isolates mass.

Status: this uses integrated acceleration for fixed mass without making impulse the lesson's central object.

#### B2.13 — Unit derivation rather than recall

Ask students to derive:

$$
[\mathbf F]=[m][\mathbf a]
=\mathrm{kg}\,\mathrm{m/s^2}
=\mathrm N.
$$

Then present plausible distractors:

```text
kg/s²
kg m/s
N/kg
kg m/s²
```

#### B2.14 — Zero, unknown, and undefined table

Students classify:

| Case | Correct status |
|---|---|
| finite `m`, `a=0` | `F_net=0` |
| `F_net=0`, `a=0`, find `m` | not determined by this trial |
| target address absent | calculation not licensed |
| massless target queried through Newton II | inertial-mass referent absent / route halts |
| net-force value not supplied but `m,a` known | infer it through Newton II |

#### B2.15 — What does a newton meter establish?

Give the statement:

> The meter between the hand and cart reads 10 N, therefore the cart's net force is 10 N.

Students mark:

```text
[ ] always valid
[ ] never a force measurement
[x] valid only after a force-accounting certificate connects this contribution to net force
```

Then ask them to rewrite the safe observation:

> The meter reads a 10 N force transmitted through the meter.

#### B2.16 — What does a mass value's source establish?

Sort statements into:

```text
address evidence
mass-value evidence
neither
```

Examples:

- several markers move redundantly;
- an admissible dynamical comparison bound `m[A]=2 kg`;
- the object is blue;
- no offshoot appeared during the interval;
- a weighing scale displays a number, with no gravitational–inertial equivalence supplied.

### 6.3 Force-to-path exercises

#### B2.17 — Numerical equal-time path stepper

Supply:

```text
valid target address A
m[A]
initial position r0
initial velocity v0
time step Delta t
one supplied F_net[A] vector per step
```

Students repeatedly compute:

$$
\mathbf a_n=\frac{\mathbf F_{\mathrm{net},n}}{m},
\qquad
\mathbf v_{n+1}=\mathbf v_n+\mathbf a_n\Delta t,
$$

and extend the position with the integration convention stated on the sheet. The convention must be explicit; for a simple Euler sheet:

$$
\mathbf r_{n+1}=\mathbf r_n+\mathbf v_{n+1}\Delta t.
$$

The pedagogical point is the sequence, not numerical-integration accuracy.

#### B2.18 — Same mass, rotating force sequence

Supply equal-magnitude net-force arrows that turn by 90 degrees from step to step. Students predict the gradual curve and compare it with the sequence produced by a constant-direction force.

#### B2.19 — Zero-force interval

Insert one or more steps with supplied `F_net=0`. Students preserve velocity rather than setting velocity to zero.

This tests the distinction:

```text
zero acceleration -> velocity unchanged
not: velocity becomes zero
```

#### B2.20 — Required address-failure row

At step 4, state:

```text
The previous target address is no longer licensed, and no bridge or replacement mass value is supplied.
```

The only accepted continuation is:

```text
HALT: old mass address not licensed.
```

The row after the halt should contain tempting numerical values to check whether the student refuses an unauthorised calculation.

### 6.4 Introductory target/address exercises

These introduce some NML2A operations without yet requiring the full university account.

#### B2.21 — Marker-track pass/fail

Show three marker positions at equal-time frames. Give a grid and a stated tolerance. Students measure pairwise relative offsets and mark each interval `pass` or `fail`.

#### B2.22 — One address, three distinct things

Students complete:

```text
target address:       A
mass address:         m[A]
bound mass value:     m[A] = 2 kg
```

Then answer:

1. Which line identifies the target?
2. Which line names the slot?
3. Which line contains a magnitude?
4. Which of these did the track analysis provide?

#### B2.23 — Address ledger

| Interval | Tolerance | Redundancy | Address action | Mass usable? | Reason |
|---|---|---|---|---|---|
| `t0-t1` | stated | pass | create `A` | if supplied | tracks redundant |
| `t1-t2` | stated | pass | carry `A` | yes | continuous licence |
| `t2-t3` | stated | fail | suspend/halt at this description | only through stated bridge | representation fails |

Students fill the last two columns.

#### B2.24 — Present redundancy versus historical continuity

Show `pass -> fail -> pass`. Ask separately:

1. Is the final family redundant now?
2. Has it earned a present target address?
3. Is that enough to call the present address the earlier `A`?

Expected answers: yes, yes, no.

#### B2.25 — Introductory bouncy-ball comparison

Use a marked-ball video at two resolutions. Students mark:

```text
strict: pass -> fail -> pass
loose:  pass -> pass -> pass
```

Questions:

1. At which tolerance is one point-particle proxy continuously usable?
2. Is the loose tolerance still accurate enough for the stated translational question?
3. What would happen if ball and wall became indistinguishable?

At Band II, the teacher may supply the bridge conclusion rather than require the full fission–fusion account.

### 6.5 Larger Band-II investigations

#### E7 — Audit first, calculate second

Each row contains two stages:

```text
Stage A: Is the addressed mass licensed for this target and interval?
Stage B: If yes, run Newton II.
```

Award separate marks. A correct calculation after an invalid audit receives no Stage-B credit; a correct halt receives full credit.

#### E8 — Planet trajectory to inferred net-force vectors

Provide equal-time planetary positions and a planet mass. Students:

1. construct velocity changes;
2. infer acceleration vectors;
3. calculate `F_net=ma`;
4. plot the inferred vector magnitudes/directions against orbital position or radius;
5. describe the pattern.

Required label:

> These are Newton-II-inferred net-force values, not an independent measurement or derivation of the gravitational law.

#### E9 — Formula-compression exercise

Begin with comparison statements:

```text
same mass, bigger force value -> more acceleration
same force value, bigger mass -> less acceleration
```

Ask students to compress them into `a=F_net/m`, then recover the statements from the formula. This prevents the equation from arriving as an uninterpreted rule.

#### E10 — Error-shape diagnosis

Give anonymised student responses and ask which error occurred:

```text
target mixing
unit mixing
direction omission
zero/no-force-contributions collapse
meter/net-force collapse
trajectory/force collapse
address failure ignored
```

This makes students practise auditing another interpreter, which often reveals their own habits.

### 6.6 Band-II demonstrations

#### D5 — Cart, certified mass, and recorded motion

Use a low-friction cart, an already-certified mass value, a repeatable action programme, and equal-time motion recording. Let students predict relative acceleration before the run.

Current status: do not use a weighing scale display as an unexplained origination of inertial mass and do not call a force-sensor reading the cart's net force without the later certificate. A simulation may supply the formal net-force value more cleanly.

#### D6 — Marked bouncy ball in normal and slow motion

Place visible marks on a compressible ball. Show the same collision:

- at ordinary/coarse resolution;
- in high-speed/fine resolution.

The perceptual aim is that the same event supports different target bookkeepings without either observation being “fake.”

#### D7 — Repeatable kick/constant-impulse device

Use a device that gives similar kicks to different masses and compare `Delta v`.

Status: good inertial-mass intuition, but formally closer to impulse/momentum. Keep it qualitative in NML2 or move the formal treatment later.

#### D8 — Newton meter misconception demonstration

Display a meter reading but explicitly ask:

> What did this instrument directly measure, and what further information would be required before calling the reading the target's net force?

The demonstration is useful as a misconception probe, not as the source of the NML2 net-force wall.

### 6.7 Band-II exit/critical set

1. What three addressed quantities are locked by Newton II?
2. Why can numbers with correct units still form an invalid Newton-II equation?
3. What does `a[A]=0` permit you to conclude? What does it not permit?
4. A meter reads 7 N. What exactly has been measured?
5. Did the track determine the mass value or only its possible owner?
6. Why is `pass -> fail -> pass` not, by itself, a continuous address history?
7. When is `HALT` the complete correct answer?
8. What later question remains after `F_net[A]=m[A]a[A]` has been evaluated?
9. Why can Newton II not calculate anything when none of its three values has been supplied?

---

## 7. Band III — University

Band III is primarily NML2A. Its goal is to make explicit the modelling work hidden by the textbook phrase “a particle of mass `m`.” Students should be able to build, grade, carry, suspend, reconstruct, or reject the target and mass address that Newton II consumes.

### 7.1 Trackability and trajectory construction

#### B3.1 — Path or track?

Give two points that traverse the same geometric curve at different times. Ask:

1. Do they have the same path?
2. Do they have the same trajectory/track?
3. Which object can be tested for redundancy?

Expected answer: same path is possible; tracks differ because they are time-indexed; redundancy compares tracks/trajectories, not bare paths.

#### B3.2 — Re-identification from video

Provide a short frame sequence with several visible features. Students:

1. choose seed points on frame 0;
2. re-identify each seed across frames;
3. record `r_i(t_k)`;
4. state any occlusion, crossing, feature-loss, or identity-swap uncertainty;
5. give a lower bound on meaningful tolerance from the tracking noise.

This practises the tracker interface rather than assuming that trajectories are already supplied.

#### B3.3 — Coverage audit

Prompt:

> The current seed family produces two bundles. What observation would test whether sparse seeding missed a third bundle?

Expected operation: add seeds in previously untracked regions and repeat the count. If densification changes the count, the earlier coverage was inadequate.

Then ask:

> Can densifying seeds detect evaporation or transport below the video's spatial resolution?

Expected answer: no; that is the permanent resolution residue.

#### B3.4 — Tolerance from above and below

For a stated tracking uncertainty `delta` and required modelling accuracy `Delta`, ask students to identify the meaningful tolerance window:

```text
tolerance must be no finer than the tracker can resolve
tolerance must be no coarser than the question can tolerate
```

If no overlap exists, the proposed model is not supportable with the data.

### 7.2 Redundancy, bundles, and the particle count

#### B3.5 — Formal two-track redundancy test

For sampled positions, evaluate:

$$
D_{ij}(t_k)=
\left\|
[\mathbf r_i(t_k)-\mathbf r_j(t_k)]
-[\mathbf r_i(t_0)-\mathbf r_j(t_0)]
\right\|.
$$

Given tolerance `epsilon`, mark the pair redundant over the interval only if every sampled `D_ij` is within the accepted bound, with interpolation/measurement limitations stated.

#### B3.6 — All-pairs bundle audit

Given six tracks and a redundancy matrix, students:

1. find maximal pairwise-redundant cliques;
2. identify any overlaps;
3. show why finite-tolerance redundancy need not be transitive;
4. record the human clique-pick where more than one admissible bundling exists.

This is the formal version of “how many particle targets does the scene produce?”

#### B3.7 — Count stability under densification

Start with a sparse family yielding `n` bundles. Add new tracks in stages. Plot inferred bundle count against seed density. Students decide whether the count has stabilised at the working tolerance and distinguish:

```text
stability under more seeds
from
certainty about sub-resolution material flow
```

#### B3.8 — Representative-track licence

For an accepted bundle, ask:

> Which outputs may one representative track stand in for, and which properties of the material have not been represented?

Expected answer: it may stand in for the motion information on which the bundle is redundant. Size, shape, orientation, rotation, internal deformation, and unmodelled dimensions are not thereby represented.

#### B3.8A — Galilean-frame invariance of redundancy

Transform a track-family between inertial frames using:

$$
\mathbf r_i'(t)=\mathbf r_i(t)-\mathbf Vt-\mathbf c.
$$

Students show:

$$
\mathbf r_i'(t)-\mathbf r_j'(t)
=\mathbf r_i(t)-\mathbf r_j(t),
$$

so a fixed-offset redundancy judgement and resulting bundle count are preserved between Galilean inertial frames. Contrast this with a rotating frame, where the coordinate transformation can make the same track-family appear redundant or nonredundant. Ask students to locate the frame commitment rather than treating the bundle count as frame-free in every possible frame.

### 7.3 The one–ordered-many–disordered-many ladder

#### B3.9 — Thrown block

Seed a translating block densely. Students show that all tracks differ by approximately fixed offsets at the chosen tolerance and conclude:

```text
one bundle -> one point-particle proxy
```

Then rotate the block or add visible vibration and repeat the audit.

#### B3.10 — Whole water stream is not one bundle

For a steady falling jet, compare parcels emitted at different times. The lower parcel is faster and the longitudinal separation changes. Students show that the entire stream fails the fixed-offset test over a finite interval.

Expected classification:

```text
not one particle
not disordered many
ordered many
```

#### B3.11 — Slab-wise redundancy

Choose a thin material slab of height `dh`. Students test whether tracks within it share the local velocity field closely enough that deviations remain below the working tolerance over the modelling interval.

They must state both caveats from the trackability note:

1. vertical strain means even a finite slab is not exactly redundant;
2. incompressibility produces transverse contraction, so full three-dimensional redundancy is tolerance-dependent.

#### B3.12 — One-dimensional projection of the tap

Let `P_z` project a track onto its downward coordinate:

$$
P_z\mathbf r_i(t)=z_i(t).
$$

Students compare:

```text
full 3D redundancy of tracks within a material slab
downward-coordinate redundancy of the same tracks
```

They should be able to conclude:

> The water can fail as a rigid three-dimensional point-particle target while succeeding, within tolerance, as a one-dimensional downward-motion target.

#### B3.13 — Continuous stream of addressed masses `dm`

Label successive material slabs by emission time or another material label `tau`. For each slab:

```text
target address: A_tau
represented coordinate: z_tau(t)
supplied mass binding: m[A_tau] = dm
```

Ask students to explain why:

$$
\{A_\tau\}
$$

is a continuously indexed family of massive point-particle representatives, not one point-particle representing the entire jet.

Optional fluid extension, clearly marked beyond core mass-address origination:

$$
dm=\dot m\,d\tau
=\rho A(z)v(z)\,d\tau.
$$

Students connect increased `v(z)` and decreased cross-sectional area `A(z)` without treating the narrowing as loss of the material parcel's mass.

#### B3.14 — Slab boundary conventionality

Give a smooth velocity gradient and two overlapping admissible slab decompositions. Ask:

1. Which aspects of the particle count are tolerance-set?
2. Why are the exact slab boundaries a clique-pick rather than a fact forced uniquely by the tracks?
3. What happens to the count as the tolerance is tightened?

#### B3.15 — Splatter

Continue the tap video through impact with the floor. Students re-run the redundancy audit and identify the transition:

```text
ordered many -> disordered many
```

They must not assign each new droplet a mass value merely because it now has an address. Per-fragment values require later origination or licensed partition structure.

### 7.4 Bouncy-ball investigation at two tolerances

#### B3.16 — Strict/loose double ledger

Students analyse the same marked-ball collision twice.

Loose-tolerance ledger:

```text
pass -> pass -> pass
one address continuously certificate-carried
mass slot usable throughout
```

Strict-tolerance ledger:

```text
pass -> fail -> pass
fine proxy unavailable during contact
micro-bundles may exist during deformation
post-contact value may be bridge-reconstructed if no material departed
```

Students write both accounts without deciding that one is the uniquely “real” object history.

#### B3.17 — Fine–coarse–fine bridge

Construct explicitly:

```text
fine address before
    -> refines continuous acceptable coarse target
continuous coarse target through contact
    -> refined by fine address after
```

Ask whether the fine address was directly usable during contact. A high-quality answer distinguishes:

- continuous coarse-address use;
- unavailable fine proxy during deformation;
- before/after reuse or reconstruction of the same bound value.

#### B3.18 — No-offshoot audit

Students inspect whether every tracked material feature remains in the family during deformation. Classify:

```text
no break, no offshoot -> persistence
redundancy break, no offshoot -> reconstruction case
offshoot observed -> certificate expiry
```

Follow-up:

> In the no-offshoot fission–fusion case, why need we not assign a separately measured mass to every temporary micro-bundle merely to recover the post-bounce value?

Expected answer: the fine partition is not consumed separately; complete material tracking and mass-locality support reconstruction of the before/after total value. If the micro-targets were to be used individually in Newton-II predictions, their individual mass values would require further origination.

#### B3.19 — Tolerance-budget challenge

Offer a sequence of increasingly coarse image resolutions. Students identify the coarsest resolution that still:

1. distinguishes ball from wall;
2. excludes unrelated nearby objects;
3. supports the requested translational accuracy.

They must reject coarser choices even if those choices make continuity easier.

#### B3.20 — Prediction versus retrospective revision

Give two modelling records:

```text
Record A: tolerance schedule declared before prediction
Record B: tolerance changed only after unexpected deformation was observed
```

Students classify A as an advance certificate and B as a new retrospective account. They explain why B cannot retroactively licence the original prediction.

### 7.5 Defeat and separating-case exercises

#### B3.21 — Convoy over-lumping

Track cars maintaining fixed offsets. At first the bundle passes; later one brakes. Ask:

1. Was the earlier redundancy calculation wrong?
2. Did it establish cohesion?
3. How should the target history be revised?

Expected answer: the earlier finite-interval proxy was valid at its stated interval/tolerance; it did not establish dynamical cohesion; later defeat requires re-lumping.

#### B3.22 — Spinning wheel

Track centre, rim, and another rim point. Students show:

```text
fixed pairwise distances
but changing relative displacement vectors/velocities
therefore ordinary rigidity without translational redundancy
```

Ask which later representative would preserve bulk translation and why that representative is constructed rather than selected from a rim track.

#### B3.23 — Pushed rod

Use the separating claim from the bridge spine:

> A mass-proportional share in an equivalent composite account is not automatically the attached physical force acting at that part.

Students distinguish account distribution from force-contribution attachment. This is an advanced boundary to force-sum.

#### B3.24 — Deuteron/measurement-grade thought question

Use the conceptual contrast:

```text
ledger combination rule
versus
empirically measured mass at finite tolerance
```

Ask why an exact bookkeeping sum need not be numerically identical to nature's measured composite mass once binding-energy effects matter. Mark this as a relativistic/domain-boundary extension, not core Newtonian calculation.

#### B3.25 — Sub-resolution mass loss

Give a target that slowly evaporates while all visible tracks remain redundant. Ask whether visible redundancy alone certifies constant mass exactly.

Expected answer: no; coverage and resolution limit the certificate. Sub-resolution departure can drain mass without a visible offshoot.

### 7.6 Mass-pipeline exercises

#### B3.26 — Which stage did the work?

Students label each statement:

```text
trackability/domain gate
coverage
lumping/address creation
value origination by dynamics
persistence escort
composite assembly
Newton-II consumption
```

Example statements:

- “The same feature was followed through every frame.”
- “These tracks form one redundant bundle.”
- “This bundle now has a mass slot.”
- “A same-pull, same-time comparison bound the value 2.30 kg.”
- “No offshoot tracks appeared over the interval.”
- “Two already-priced co-accelerating parts were represented together.”
- “The supplied net force predicted the next acceleration.”

#### B3.27 — What kinematics can and cannot do

Prompt:

> A complete trajectory `r(t)` is known. Can the trajectory alone determine the inertial mass magnitude?

Students justify:

$$
\mathbf F(t)=m\mathbf a(t)
$$

for any chosen positive `m` if the corresponding force is left free. Therefore kinematics can license an address and escort a binding, but not originate its magnitude.

#### B3.28 — Same-pull, same-time comparison against a standard

Given a standard mass `m_s`, equal action history, and observed nonzero velocity changes over equal time, students infer the unknown inertial-mass ratio. They must state the experiment's tolerance and why equal time/action matters.

Do not use a weighing scale to bypass the dynamical comparison.

#### B3.29 — Brick micro-run

Turn the mass-pipeline worked example into a ledger exercise:

1. seed and cover a brick;
2. lump it to target `A`;
3. dynamically bind `m[A]=2.30 kg`;
4. carry the certificate across weeks of redundant tracks;
5. clip on another already-priced brick;
6. under explicitly supplied extension assumptions, price the composite;
7. observe a chip offshoot;
8. expire the certificate and identify which values now require revalidation.

Students colour each step by source: human wall input, kinematic audit, dynamical origination, bookkeeping, or Newton-II computation.

#### B3.30 — Prediction-failure audit

When a Newton-II prediction fails, students classify possible mass-side causes from the pipeline:

- sub-resolution departure;
- over-lumping, as with a convoy;
- bad origination value;
- assembly applied without shared/redundant motion;
- domain-gate failure such as unbooked mass-energy change.

The purpose is to teach that “Newton II failed” is not yet a diagnosis.

### 7.7 Composite and centre-of-mass extensions

These exercises were suggested by the bridge and COM notes but are excluded from the final young NML2 core. They are suitable for a university extension or teacher-theory seminar.

#### B3.31 — Derive additive representative mass under stated assumptions

For parts with masses `m1`, `m2` and shared translational acceleration `A`, give the per-part Newton-II accounts and an explicit representative-adequacy aggregation rule. Students derive:

$$
M\mathbf A=m_1\mathbf A+m_2\mathbf A
\quad\Rightarrow\quad
M=m_1+m_2
$$

for nonzero/shared comparison, while naming the added adequacy commitment. They must not claim rigidity alone proves additivity.

#### B3.32 — Derive the centre-of-mass acceleration

Given:

$$
\mathbf R_{\mathrm{CM}}
=\frac{m_1\mathbf r_1+m_2\mathbf r_2}{m_1+m_2},
$$

differentiate twice and use `a1=a2=A` to show:

$$
\mathbf a_{\mathrm{CM}}=\mathbf A.
$$

Then ask what motion information the centre-of-mass representative omits.

Expected omissions: rotation, orientation, deformation, internal motion, size, and shape.

#### B3.33 — Off-centre force limitation

Compare two trials with the same total force but different application points. Ask which prediction remains the same for the centre of mass and which aspect of motion can differ because of torque.

#### B3.34 — Joined/slack-string carts

Track individual carts and the centre of mass while a slack connector becomes taut. Students compare:

- messy individual accelerations and jerks;
- smoother whole-system centre-of-mass account;
- the assumptions required to call the external value the system's net force.

Status: advanced system/COM apparatus; not core NML2 because it invites internal-force and force-sum machinery.

### 7.8 Advanced Newton-II and question-routing exercises

#### B3.35 — Forward and inverse methods

Students distinguish:

```text
observational route: trajectory -> inertial acceleration -> inferred F_net if m known
forceful route: supplied/certified F_net + already-bound m -> acceleration -> predicted trajectory
```

They identify where each route requires contingent inputs and why prediction cannot use a future observed trajectory to certify its own mass address.

#### B3.36 — Planet-field inference

From orbital trajectory data and supplied masses, infer `F_net(t)=m a(t)` and plot vectors. Then ask:

1. What was empirically read from motion?
2. What was assigned through Newton II?
3. What force law has not yet been independently derived?

#### B3.37 — Photon pair of questions

Compare:

```text
What path does a free photon follow in an inertial frame?
What Newton-II inertial acceleration does a photon have?
```

Students write the demanded headword, ancestry, and outcome for each: terminating path route versus absent inertial-mass referent.

#### B3.38 — Malformed mixed-address question

Prompt:

> What is the acceleration obtained from the boat's net force and the table's mass?

Students should not merely calculate the ratio. They should say the natural-language request does not name a valid single-target Newton-II quantity unless it is explicitly asking for an artificial numerical ratio.

#### B3.39 — Net-force value versus force-sum explanation

Give an inferred `F_net[A]` and ask students to list which further objects must be supplied before a force-sum analysis could begin:

```text
candidate acting objects
force contributions attached to A
activation conditions
time/interval
closure/completeness judgement
```

Then stop. This is a handoff exercise, not an NML3 calculation.

### 7.9 University demonstrations and investigations

#### D9 — Live water tap with high-speed side video

Record a laminar tap stream with a scale grid. If possible, use dye pulses or illumination bands to suggest material slices. Students estimate `v(z)`, observe narrowing, and compare whole-stream, slab-wise, and projected-downward redundancy.

Key warning: fixed horizontal spatial boxes are not material parcels. The continuing mass address belongs to a tracked material slab, not to whatever water occupies one laboratory-height interval at successive times.

#### D10 — Marked bouncy ball with synchronised resolutions

Use the same frames to construct both a strict and a loose tracker data set. Students should produce two ledgers from one event and defend the tolerance budget of each.

#### D11 — Block–tap–splatter video triptych

Show:

1. a translating block;
2. a falling water jet;
3. the jet splattering.

Students predict `one`, `ordered many`, or `disordered many` before running the redundancy audit.

#### D12 — Convoy defeat data

Use overhead traffic/drone footage or synthetic tracks in which vehicles maintain formation and one later brakes. Students experience a kinematically successful lumping that later loses its certificate without retroactively becoming meaningless.

#### D13 — Spinning-wheel marker demonstration

Put markers at the centre and rim of a rotating/translating wheel. Plot their tracks and compare fixed distances with nonredundant velocity histories.

#### D14 — Brick/chip offshoot demonstration or simulation

Track a target that visibly loses a fragment. Ask the class to freeze the Newton-II calculation at the offshoot frame and update the mass ledger before continuing.

#### D15 — Joined/slack carts and centre of mass

Track cart positions and calculate the mass-weighted point through a slack-to-taut event. Use only as the explicit COM/system extension.

#### D16 — Planet trajectory plotting

Use astronomical ephemeris or idealised orbit data to infer acceleration and Newton-II net-force vectors. Label the result as inference, not independent force measurement.

### 7.10 University exit/critical set

1. What observational fact makes a physical trajectory the trajectory *of* a continuing target?
2. Why is tolerance bounded both from below and above?
3. Why are finite-tolerance bundles cliques rather than necessarily equivalence classes?
4. Which parts of a proposed bundling are computationally auditable, and which remain human/residual inputs?
5. Why is a rotating rigid wheel not translationally redundant?
6. Why is the water stream ordered many rather than one target?
7. How does one-dimensional projection license slab representatives even while the stream narrows?
8. What does `m[A_tau]=dm` attach the mass to: a fixed place, the whole column, or a tracked material slab?
9. In the strict bouncy-ball account, what is unavailable during contact? What can still be reconstructed afterwards?
10. What evidence distinguishes a no-offshoot break from certificate expiry?
11. Why can redundancy escort a mass value without originating its magnitude?
12. What does an offshoot force the modeller to stop doing?
13. Why does a retrospective tolerance revision not certify an earlier prediction?
14. What additional commitment is required to move from shared acceleration to additive representative mass?
15. Why can the centre of mass preserve translation while failing to represent the full rigid-body motion?
16. What is the exact difference between inferring a net-force vector and constructing it from force contributions?

---

## 8. Consolidated Demonstration and Investigation Inventory

This table gathers every demonstration or apparatus idea suggested explicitly in the lesson/working notes, plus the direct scene investigations implied by the trackability and mass-pipeline documents.

| Demonstration / investigation | Student-facing operation | Likely band | Current NML2 status | Critical caveat |
|---|---|---|---|---|
| Everyday path gallery: leaf, ball, car, Moon, smoke, boat, Mars | Describe path; identify possible influence; inspect frame | I | NML1 prerequisite | Do not open formal force language too early. |
| E7 path-to-arrow sheet | Draw repeated local motion-change arrows | I | Required prerequisite/review | Arrow is acceleration readout, not force. |
| Many markers on translating cart | Notice repeated translational information; begin bundling | I–II | Core bridge into target discipline | Familiar objecthood must not substitute for track evidence. |
| Already-certified masses receiving comparable sideways actions | Compare mass-side resistance to motion-change | I | Core intuition | Same action and same time must be controlled for formal claims. |
| Hanging balls struck sideways | Compare initial motion-change | I | Qualitative/conditional | Hand taps are uncontrolled; later swing brings gravity/tension. |
| Low-friction carts under equal-duration repeatable action | Compare accelerations and paths | I–II | Useful | Do not equate device reading with net force without certificate. |
| Scale display | Identify a mass-side number | I–II | Earlier proposal superseded as inertial-mass origination | Current design requires supplied or dynamically certified inertial mass; do not smuggle gravitational–inertial equivalence. |
| Newton meter / force sensor | Read one transmitted force contribution | II | Misconception probe or NML3 bridge | Not automatically the target's net force. |
| Constant-force cart puller | Compare motion under a controlled action programme | II | Conditional/later | Formal net-force use requires force accounting. |
| Constant-impulse/kick device | Compare velocity change for different masses | I–II | Intuition object | Formally opens impulse/momentum; not core Newton-II proof object. |
| Supplied-force simulation | Run clean `m,F_net -> a -> path` trials | I–II | Strong core option | Make supplied status explicit. |
| Marked bouncy ball at normal/high-speed resolution | Compare strict and loose redundancy ledgers | II–III | Central NML2A demonstration | Return of redundancy alone is not historical continuity. |
| Thrown/translating block | Produce one redundant bundle | III | Trackability ladder | Add rotation/vibration to test limits. |
| Live falling water tap | Produce ordered slab-wise targets; project to downward coordinate | III | Central continuum extension | Entire stream is not one bundle; fixed spatial cells are not material parcels. |
| Tap stream splattering | Re-lump ordered many into disordered many | III | Advanced defeat investigation | Addresses do not supply droplet mass values. |
| Convoy whose car later brakes | Expose over-lumping/coincidental co-motion | III | Advanced separating case | Kinematic redundancy does not prove cohesion. |
| Translating/spinning wheel with markers | Contrast fixed distances and translational redundancy | III | Advanced separating case | One-track proxy and centre-of-mass account are different licences. |
| Brick monitored over time, then chip flies off | Expire mass certificate at offshoot | III | Mass-pipeline investigation | Do not keep using the original value for the remainder. |
| Two already-priced bricks clipped together | Illustrate restricted composite assembly | III extension | Not final core NML2 | Requires explicit adequacy/assembly assumptions; redundancy alone is insufficient. |
| Joined/slack-string carts with centre-of-mass tracking | Contrast internal jerks with bulk representative motion | III extension | Teacher-side/advanced | Invites force-sum, internal-force, momentum, and COM machinery. |
| Planet trajectory plotting | Infer `a` and then Newton-II `F_net`; plot pattern | II–III | Advanced extension | Not an independent gravity-force measurement or law derivation. |
| Earth as extremely massive participant | Explain imperceptibly small motion-change | I–II thought demonstration | Small bridge to later work | Do not open Newton III computation in NML2. |
| Atwood machine | Demand-tree/force-sum/constraint exercise | III | Explicitly later than NML2 | Requires multiple force contributions, tension, constraints, and closure. |
| Spring/load-deflection demonstrator | Distinguish scalar load law, fixed-axis vector law, and central spring | II–III | Later acting-object/spring lesson | Opens Hookean acting-object and force-contribution machinery. |
| Off-centre force on rigid body | Compare COM translation and rotation | III extension | Later rigid-body dynamics | Torque required for full motion. |

### 8.1 Apparatus choice rule

The cleanest NML2 apparatus is not necessarily the most physically complete apparatus. Select apparatus according to the demanded operation:

```text
qualitative inertial-mass intuition
  -> repeatable action, equal time, compare motion-change

formal Newton-II calculation
  -> supplied/certified F_net and already-bound m

target-address investigation
  -> visible marker tracks, stated resolution/tolerance, replayable video

force-contribution construction
  -> not NML2; move to NML3
```

---

## 9. NML1 Student-Facing Question Inventory Retained as Prerequisite or Model

The user specifically pointed to the NML1 critical-question model. These are the deduplicated student-facing prompts in the supplied NML1 drafts that either establish prerequisites for NML2 or illustrate how a VD-native probe should work.

### 9.1 Opening/path questions

1. Do most things around you move in perfect straight lines forever?
2. If almost nothing seems to go straight, why would anybody think straight-line motion is fundamental?
3. What is moving?
4. What does its path look like?
5. What other object or surroundings might be influencing that path?
6. What might the path look like if that influence were removed?
7. When should simple motion appear?

### 9.2 Classification drills

Classify leaf in wind, falling ball, slowing car, gliding puck, photon path, and block on table as free-body candidates or not. Classify stationary stone, straight steady puck, turning car, orbiting planet, accelerating falling ball, and curling smoke as uniform-motion or not.

### 9.3 Newton-I anti-inversion questions

1. A block is stationary on a table. It has uniform-motion. Is it a free body?
2. A car travels around a circle at constant speed. Is it in uniform-motion?
3. A puck appears to curve but no object influences it. What should you inspect?
4. Can a photon in empty space be treated as a free body for a path question?
5. If you draw inward arrows on a circular path, have you explained the cause?

### 9.4 E7 motion-reading prompts

1. Is the motion simple?
2. If not, how is velocity changing?
3. Where is the path bending?
4. Where is the motion turning?
5. Draw how the motion changes.
6. On a circle, where do the turning arrows point?
7. What should you ask after drawing the motion-change arrows?

### 9.5 NML1 exit/pre-post questions

1. What is a free body?
2. What is an inertial frame?
3. Is Newton I just the zero-force case of Newton II?
4. A puck appears to curve while no other object influences it. What should you suspect?
5. A block sits still on a table. Is it free?
6. Can a photon in empty space be treated as free for a path question?
7. A car moves around a circle at constant speed. Is it accelerating?
8. Draw arrows showing how the Moon's motion changes as it orbits Earth.
9. Have those arrows explained the cause or only read the motion-change?
10. When a sky path looks strange, what should you check before inventing a cause?

These should not dominate NML2, but brief versions can diagnose whether the E7 prerequisite is present.

---

## 10. Suggested Critical-Question Rubrics

### 10.1 Same-target Newton-II lock rubric

Question: a student uses the table's force with the boat's mass to calculate the boat's acceleration.

| Level | Response pattern | Interpretation |
|---:|---|---|
| 0 | Performs arithmetic without noticing ownership. | Newton II treated as a relation among free-floating numbers. |
| 1 | Notices the answer “looks wrong” but cannot state why. | Weak contextual sensitivity. |
| 2 | Says the force belongs to the wrong object. | Target ownership recognised. |
| 3 | Rebuilds the boat row and uses only `F_net[boat]` and `m[boat]`. | Same-target discipline installed. |
| 4 | States the general law: `m[A]`, `a[A]`, and `F_net[A]` must refer to the same target, interval, and frame-qualified account. | Full addressed-triplet competence. |

### 10.2 Typed mystery-slot rubric

Question: given `m[A]` and trajectory-read `a[A]`, what does Newton II tell you?

| Level | Response pattern | Interpretation |
|---:|---|---|
| 0 | Names a physical force contribution by guess. | Premature downstream explanation. |
| 1 | Calculates a magnitude but omits target/direction/unit. | Algebra without type discipline. |
| 2 | Returns a correctly typed net-force vector. | Triplet calculation achieved. |
| 3 | Says it was inferred through Newton II, not independently measured. | Provenance discipline achieved. |
| 4 | Also states that contribution construction and acting-object identification remain for NML3. | Full boundary competence. |

### 10.3 Zero-case rubric

| Level | Response pattern | Interpretation |
|---:|---|---|
| 0 | “No forces exist” or “the mass is zero.” | Zero/no-things or type collapse. |
| 1 | Says only `a=0`. | Restates premise. |
| 2 | Correctly returns `F_net=0`. | Newton-II implication understood. |
| 3 | Adds that force contributions may later cancel and target need not be free. | Boundary preserved. |
| 4 | Also recognises that `m=F/a` cannot identify mass in the `0/0` trial. | Full zero-branch competence. |

### 10.4 Bouncy-ball tolerance rubric

| Level | Response pattern | Interpretation |
|---:|---|---|
| 0 | “It obviously remains the same ball” or “it definitely breaks.” | Absolute-object answer; tolerance erased. |
| 1 | Notices deformation but gives only one bookkeeping. | Partial track sensitivity. |
| 2 | Distinguishes strict failure from loose continuity. | Tolerance-indexed validity understood. |
| 3 | Explains why loose tolerance must remain inside the question's budget. | Model adequacy understood. |
| 4 | Distinguishes continuous coarse use, unavailable fine proxy, and no-offshoot bridge reconstruction of the bound value. | Full NML2A competence. |

### 10.5 Water-tap rubric

| Level | Response pattern | Interpretation |
|---:|---|---|
| 0 | Calls the whole stream one particle because it is visibly connected. | Familiar-object/continuity over-lumping. |
| 1 | Calls it merely “many particles” without structure. | Count recognised; ordering/model dimension absent. |
| 2 | Identifies thin slabs as ordered point-particle representatives. | Slab-wise lumping achieved. |
| 3 | Distinguishes full 3D failure from downward-coordinate redundancy and labels material slabs. | Representation-relative redundancy understood. |
| 4 | Explains the continuously indexed family `A_tau`, attaches supplied `dm` to each material address, and distinguishes material parcels from fixed spatial cells. | Full continuum bridge competence. |

---

## 11. A Minimal Assessment Spine by Level

If the complete bank is too large, these are the smallest coherent selections.

### Band I minimum

1. Circle and match target-owned quantities.
2. Sort kg/N/m/s².
3. Calculate `a=F_net/m` for three targets without mixing rows.
4. Compare same force/different mass qualitatively.
5. Complete one zero-acceleration card sort.
6. Draw one E7 motion-change arrow sequence.
7. Answer CQ1, the same-target lock.

### Band II minimum

1. Normalise questions to `m[A]`, `a[A]`, or `F_net[A]`.
2. Perform all three Newton-II algebraic forms.
3. Pass unit, direction, target, and interval audits.
4. Complete a force-to-path stepper with a zero interval.
5. Complete one required halt row.
6. Answer CQ3, CQ4, and CQ5.

### Band III minimum

1. Produce tracks from a seeded scene.
2. Run a redundancy audit at two tolerances.
3. Construct an address ledger and validity interval.
4. Analyse the bouncy ball under strict and loose tolerance.
5. Analyse the water tap as ordered slab-wise many and construct `A_tau -> dm` bindings.
6. Detect offshoot expiry and distinguish it from a no-offshoot break.
7. Explain address/value/provenance through the mass pipeline.
8. Answer CQ8, CQ10, CQ13, and CQ14.

---

## 12. Source Coverage Audit

### 12.1 Direct lesson and pedagogy sources

| Supplied file | Contribution extracted |
|---|---|
| `NML2_FINAL_DRAFT_v1(1).md` | Current thesis; target/address/tolerance questions; bouncy-ball investigation; Newton-II unit/vector work; address ledger; force-to-path sheet; halt row; misconceptions; criteria of instillment; planet extension. |
| `NML2_note_net_force_wall_withheld(1).md` | Typed hidden net-force slot; four-question student route; zero question; all three algebraic forms; planet, kick device, hanging balls, slack carts, meter, and constant-puller demonstrations. |
| `NML2_note_net_force_wall_withheld(2).md` | Byte-identical duplicate of the preceding file; counted once. |
| `NML2_working_note_core_constraints(1).md` | Three-reading bridge; primitive same-force/same-mass comparisons; three algebraic forms; equal-time requirement; zero critical question; cart apparatus; Earth thought bridge; early device proposals. |
| `NML2_working_note_core_constraints(2).md` | Byte-identical duplicate of the preceding file; counted once. |
| `NM_L1_E7_integrated_complete_draft_d2(1).md` | NML1 critical-question model; E7 path-to-arrow operations; anti-inversion drills; exit/pre-post questions; motion sheet; rubrics and error shapes. |
| `nm_l1_lesson_draft_d1.md` | Earlier NML1 lesson version confirming path gallery, influence game, uniform-motion classifications, signature puck question, trace practice, and exit ticket. Subsumed where duplicated by integrated d2. |
| `vd_pedagogy_note(1).md` | Rule for designing probes rather than illustrative examples; pressure-testing a law-house; tracking error shapes; age translation without changing the underlying trace. |

### 12.2 Target, trackability, and mass sources

| Supplied file | Contribution extracted |
|---|---|
| `vd_trackability_scene_to_particles_d4-informing(1).md` | Tracker/seeding exercises; coverage and densification; tolerance floor; formal redundancy; bundles/cliques; count as output; block–tap–splatter ladder; convoy, wheel, bounce, no-offshoot and offshoot cases; address grading. |
| `vd_mass_identification_pipeline_d1-informing(1).md` | Address/value/provenance operations; dynamical origination; persistence escort; offshoot expiry; composite assembly as an extension; brick micro-run; prediction-failure audit. |
| `vd_point_particle_bridge_spine_d1(1).md` | Separating examples: wheel, convoy, pushed rod, deuteron, tap/splatter; same-pull mass origination; perimeter at one net-force slot; COM/additivity extension status. |
| `from_fma_rigidity_to_com_plain_math_d3-informing(1).md` | University derivations of shared acceleration, additive representative mass under stated assumptions, centre-of-mass acceleration, and off-centre/torque limitation. |

### 12.3 Entry, question-routing, and structural sources

| Supplied file | Contribution extracted |
|---|---|
| `DESIGN_2_1_DRAFT_1_ENTRIES(1).md` | Primitive kinematic type/slot drills: path versus trajectory, time interval, point-particle, velocity, acceleration, relative position/velocity, uniform-motion. |
| `E7_INERTIAL_ACCELERATION_PLACEMENT_NOTE(1).md` | Frame-qualified acceleration as NML1/NML2 bridge; guardrail against opening Newton II too early. |
| `NM_L1_E7_E8_decision_note(1).md` | Same target with motion sheet and force-accounting sheet; photon, puck, and block boundary questions. |
| `VD_Newton_inertial_acceleration_two_entries(1).md` | Distinction between trajectory/free-route acceleration and massive Newton-II acceleration; photon boundary and ordinary massive-particle witness. |
| `newton_II_cleaned(1).md` | Exact Newton-II triplet roles; positivity/scalar/vector commitments; need for outward walls. |
| `vd_design_3_newton_i_correction(1).md` | Raw versus inertial acceleration; question-driven routing; path question versus Newton-II question; empty/zero distinction. |
| `project_sources/04-vd_dictionary_question_answering.md` | Natural-language normalisation; termination with a value, undefined referent, or contradiction; Atwood, free massive particle, and photon examples. |
| `project_sources/10-DESIGN_3_ENTRY_STRUCTURE.md` and backups/copy | Witness-sheet slots and same-target attributes used to construct the primitive ownership, slot-filling, and provenance drills. |
| `project_sources/14-VD_Newton_v0.6.pdf` | Formal Newton I/II/force-sum entry surface; supports triplet, type, and later-boundary classification. |
| `project_sources/09-vd_trace_level2_v3.md` | Atwood-machine trace, blocked-thunk and closure exercise; retained only as an explicit NML3+/university boundary example. |

### 12.4 Adjacent or general-theory sources reviewed

| Supplied file(s) | Outcome for this bank |
|---|---|
| `hookean_response_type_chain_d1(1).md` | Contains a spring-direction critical question and load-deflection demonstrator, but these open later acting-object/Hookean branches. Listed only in the demonstration inventory as out of NML2 core. |
| `project_sources/01-READ_ME_FIRST.md` | Orientation and source-status guidance; no direct student prompts. |
| `project_sources/02-VD_CORE_MODEL_HANDLE_RESIDUAL.md` | Supports the idea that lessons install operations through ordered exposure; no direct NML2 exercise supplied. |
| `project_sources/05-DESIGN_3_ENTRY_STRUCTURE.backup-attribute-refs.md`, `11-DESIGN_3_ENTRY_STRUCTURE.copy.md`, `12-DESIGN_3_ENTRY_STRUCTURE.backup-abstract-witness-sheets.md` | Earlier structural ledgers; relevant witness-slot ideas are covered by the current Design 3 structure. |
| `project_sources/06-vd_six_entry_structure.md` | Explains chimney/triplet/wall unit; informs the demand for triplet and wall questions but supplies no direct classroom exercise. |
| `project_sources/07-vd_logic_tracker_guidance_PRELIMINARY_v0.5.md` | Lazy evaluation, blocked states, and typed human inputs; used indirectly for halt/provenance operations. |
| `project_sources/08-factorial_vs_sum_residual_note.pdf` | Supports wording as an operational handle; no direct NML2 student activity. |
| `project_sources/13-vd_law_writing_guide.pdf` | General triplet/wall authoring guidance; supports law-house probe design but no direct NML2 exercise. |
| `project_sources/15-vd_haskell_essay.md` | Its cyclic Newton-II encoding motivates CQ18 and the triplet input-count drill; the essay itself is theory-facing rather than a classroom plan. |
| `project_sources/16-residue_derivation_note_revised.docx` | Supports primitive drill/handle installation and tolerance/budget thinking in general; no direct NML2 prompt. |
| `project_sources/03-vd_newton_v05_graph.png` | Structural visual orientation; no additional student-facing question beyond the entry relations represented elsewhere. |

### 12.5 Chronological conflicts and current resolution

| Issue | Earlier supplied position | Later/current position used here |
|---|---|---|
| Scale | May be used as black-box mass supplier. | Do not treat an unexplained weighing scale as an inertial-mass origination route; use supplied or dynamically certified mass. |
| Newton meter | May supply one force-accounting reading. | It measures a transmitted contribution, not automatically `F_net`; use as misconception probe or later certified apparatus. |
| Net-force wall | Options ranged from normal wall to negative wall to removal. | Use a thin typed wall: addressed vector, newtons, Newton-II relation; physical production withheld. |
| Bouncy-ball strict account | Fine address dies; value bridge-reconstructed after no-offshoot fission–fusion. | Retain this at strict tolerance while also teaching continuous loose-tolerance address. The double account is the advanced result. |
| Mass additivity/COM | Some theory notes licence a restricted derivation inside an expanded NML2 perimeter. | Final classroom draft excludes it from core; retain only as university extension with assumptions explicit. |
| E7 placement | Early note proposed only a light NML1 capstone. | Integrated NML1 installs motion-reading practice; NML2 reviews and places the readout into the massive-target triplet. |
| Tap | Trackability note: whole stream fails redundancy; thin slabs form ordered many under tolerance. | Current clarification adds explicit one-dimensional projection and a continuously indexed family of slab addresses carrying supplied `dm`. |

---

## 13. Systematic Exercise Generator

The bank can be expanded without inventing new conceptual content by crossing the following dimensions.

### 13.1 Select a demanded quantity

```text
mass
inertial acceleration
net-force vector
next velocity
next position
target count
address validity
value provenance
```

### 13.2 Select an operation

```text
circle / underline
match
sort
copy into a target row
draw an arrow
compare more/less
calculate
infer
predict
audit
explain
halt
```

### 13.3 Select a pressure condition

```text
several targets
distractor values
same units but wrong owner
missing direction
different intervals
zero value
missing referent
address break
return of redundancy without bridge
tolerance too fine
tolerance too coarse
meter reading presented as net force
trajectory presented as force explanation
```

### 13.4 Select a scene

```text
boat / table / cup
balls / carts
marked translating object
bouncy ball
water tap
splatter
convoy
spinning wheel
brick losing a chip
planet trajectory
photon question
```

One item from each column generates a targeted exercise. For example:

```text
demand: acceleration
operation: calculate
pressure: several targets with same units
scene: boat/table/cup

-> cross-target Newton-II ownership drill
```

or:

```text
demand: address validity
operation: halt
pressure: redundancy returns without a bridge
scene: marked bouncy ball

-> historical-continuity critical probe
```

---

## 14. Operations That Must Not Be Smuggled into Core NML2

Do not ask core NML2 students to:

- add several force contributions to manufacture `F_net`;
- draw conventional free-body diagrams;
- calculate weight, normal reaction, friction, tension, or spring force;
- infer inertial mass from an unexplained weighing-scale display;
- treat a newton-meter reading as automatically equal to net force;
- derive mass values from tracks alone;
- assign fragment masses after a split without a supplied origination/partition rule;
- assume `M=sum m_i` from redundancy alone;
- use centre of mass without marking it as an extension and supplying the needed structure;
- calculate deformation, torque, or internal-force distributions in the bouncy-ball core case;
- treat fixed spatial water cells as continuing material parcels;
- continue a force-to-path calculation after its mass address becomes unlicensed;
- interpret `F_net=0` as “no force contributions exist”;
- interpret `a=0` as “the target is free”;
- use `m=F/a` in a zero-acceleration trial;
- call an absent referent zero.

These operations are not false in every later context. They are blocked because NML2 has not yet supplied the machinery that would make them accountable.

---

## 15. Recommended Signature Set for the Next Lesson-Design Pass

The source bank suggests six questions worth developing into polished, age-specific assessment objects:

1. **Band I ownership:** The boat/table/cup cross-target calculation — can the student keep the Newton-II values attached to their owners?
2. **Band II triplet:** Given addressed mass and trajectory-read acceleration, what net-force vector does Newton II demand, and what has not yet been explained?
3. **Band II triplet structure:** With no supplied values, which corner of the triplet calculates first?
4. **Band II zero:** What follows and does not follow from zero acceleration of a finite-mass target?
5. **Band III address:** At strict and loose tolerance, did the bouncy-ball target break during the bounce?
6. **Band III continuum:** Why is the tap an ordered stream of slab-wise masses `dm`, rather than one target or an unstructured collection?
7. **All levels boundary:** When is refusing to calculate the complete correct Newtonian response?

These six questions jointly test:

```text
target ownership
Newton-II triplet competence
triplet input/boundary competence
zero discipline
tolerance-indexed identity
dimension/model-relative redundancy
halt discipline
```

They are the strongest candidates for the next stage: writing exact question wording, response rubrics, worksheet layouts, and teaching sequences for each level.
