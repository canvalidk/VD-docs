# NML2.1 Lesson Draft: Newton II as an Addressed Triplet

**Status:** integrated working draft, d1  
**Project:** VD Newton / VD Pedagogy  
**Date:** 2026-07-18  
**Core unit:** supplied material objects, the addressed Newton-II triplet, and the route from acceleration back to trajectory  
**Audience bands:** Band I — upper primary / early secondary; Band II — GCSE / A level; Band III — introductory university  
**Recommended duration:** 60 minutes in Band I, 80 minutes in Band II, 100 minutes in Band III, with compressed and two-session variants below

> **Priority note.** `NML2_1_CONTENT.md` is the canonical content authority for this draft. Earlier NML2 documents are used only for activity ideas, teacher wording, and the structural style established by the NML1 lesson draft.

---

## 0. One-Sentence Thesis

**NML2.1 teaches that Newton II joins an inertial mass, an inertial acceleration, and a net-force vector only when all three belong to the same continuing material object; it then uses that relation to construct motion until an event makes the supplied mass unsafe to reuse automatically.**

The shortest student-facing version is:

```text
Name the thing.
Keep its numbers together.
Use two triplet values to find the third.
Use acceleration to change velocity and build the path.
Stop if the old mass no longer clearly belongs.
```

The teacher-facing route is:

```text
supplied material object A
    -> distinguish A from its trajectory r_A(t)
    -> attach m[A], a[A], and F_net[A] to the same owner
    -> use Newton II as a constraint
    -> if acceleration is obtained, combine it with initial conditions
    -> construct velocity and trajectory
    -> carry m[A] only while automatic reuse remains licensed
```

One line for the head:

> **NML2.1 runs `F = ma` without losing track of what the symbols belong to.**

---

## 1. Purpose of the Lesson

NML1 installed a kinematic direction of work:

```text
known trajectory
    -> read velocity-change
    -> read inertial acceleration
```

NML2.1 opens the reverse, predictive direction:

```text
supplied inertial mass + supplied net-force history
    -> inertial acceleration
    -> velocity
    -> trajectory
```

The lesson has four linked achievements.

### 1.1 Ownership discipline

Students learn that the three Newton-II quantities are not free-floating numbers. They are values belonging to one material object, over one relevant interval, in one chosen inertial frame.

### 1.2 Triplet discipline

Students learn that Newton II is one constraint:

$$
\mathbf F_{\mathrm{net}}[A]=m[A]\mathbf a[A].
$$

The three rearrangements do not create measurements from nothing. Two independent addressed values determine the third; all three permit a consistency check.

### 1.3 Motion-building discipline

Students learn that Newton II may give an acceleration before the future trajectory is known. Acceleration must then be combined with initial position, initial velocity, a reference frame, and an acceleration history or rule to build the trajectory.

### 1.4 Licence discipline

Students learn that a supplied mass normally stays attached to the material object through ordinary changes of motion, but that automatic reuse must stop after a trigger such as splitting, merging, material loss, material gain, or loss of target identity.

The lesson therefore does more than teach an equation. It installs a complete trace:

```text
owner audit
    -> quantity/type audit
    -> information audit
    -> Newton-II calculation
    -> motion construction
    -> reuse audit
```

---

## 2. What Makes This Lesson VD-Native

A conventional first Newton-II lesson often begins by writing:

$$
F=ma
$$

and then assigning substitution exercises.

This lesson begins with a calculation whose arithmetic and units are correct but whose physics is invalid because the numbers belong to different objects.

The opening problem is therefore:

> **How can a calculation be numerically correct and still fail to be a Newton-II calculation?**

The answer creates demand for the addressed notation:

```text
m[boat]
F_net[boat]
a[boat]
```

The notation is not announced as decorative precision. It arrives as the repair for an error the class has already seen.

The lesson is also VD-native in five further ways.

1. **The material object is separated from its trajectory.** The object is the bearer; the trajectory is the motion record.
2. **Net force remains deliberately thin.** It is one supplied or Newton-II-inferred vector, not yet a sum of force contributions or a meter reading.
3. **Newton II is treated as a constraint.** Students must ask what independent information is present before calculating.
4. **The equation is connected back to motion.** The third quantity is not the end of the trace; acceleration can be used to continue velocity and trajectory.
5. **The lesson ends at a real failure.** When the mass-reuse licence becomes uncertain, the successful response is to halt rather than invent a new mass.

The lesson's conceptual drama is:

```text
The arithmetic works.
The owner does not.

The equation works.
The inputs may not exist.

The acceleration is known.
The path is not yet known.

The old mass was usable.
Then its reuse licence expired.
```

---

## 3. Lesson Boundary

### 3.1 Prerequisites

Students should already be able, at an age-appropriate level, to:

- recognise and follow a material object through an ordinary scene;
- distinguish a path or trajectory from the thing moving;
- read simple motion-change from a trajectory;
- understand that velocity can change through speed-change, direction-change, or both;
- treat the stated classroom or laboratory frame as inertial when the problem supplies that condition;
- read arrows as directions;
- perform the required arithmetic for their band.

NML1's active handoff is:

```text
trajectory in an inertial frame -> inertial acceleration
```

NML2.1 reactivates that route but does not reteach the full Newton-I law-house.

### 3.2 What the lesson is allowed to consume

The lesson may begin with:

- an already identified material object;
- a supplied inertial-mass value bound to that object;
- a supplied net-force vector or a trajectory from which acceleration can be read;
- a supplied inertial frame;
- supplied initial position and velocity when a trajectory is to be predicted.

The supplied status should be spoken aloud. For example:

> “For this problem, the cart is already identified as material object `A`, its inertial mass is supplied as `4 kg`, and the net-force arrow for each interval is supplied.”

### 3.3 What remains deferred

NML2.1 does not yet teach:

- how changing visual scenes are converted into continuing material objects;
- trackability, redundancy, tolerance, lumping, or formal mass-address construction;
- how an inertial-mass value is originally measured or certified;
- why gravitational, inertial, and material-amount mass agree in ordinary cases;
- how several physical force contributions form one net-force vector;
- free-body diagrams, force addition, acting objects, or Newton III;
- mass additivity as an automatic law;
- fragment-mass assignment after a split;
- momentum, impulse, rockets, leaking carts, or other open-system solutions;
- centre of mass, torque, rotation, or deformation mechanics.

The later questions are deliberately visible:

```text
NML2.2:
How is a continuing material object identified, given a mass address,
and licensed to retain it?

Later force-composition lesson:
Which force contributions and acting objects produce the net-force vector?

Later momentum lesson:
How are continuously mass-changing or open systems handled?
```

---

## 4. The Active Conceptual Objects

### 4.1 Provisional classroom meaning of `material object`

Before NML2.2, use:

> **A material object is the continuing physical thing whose trajectory we describe, whose inertial mass is given, and to which a net force belongs.**

For younger learners:

> **The material object is the thing we keep following.**

The lesson uses ordinary object recognition provisionally. It does not yet analyse how that recognition is earned.

### 4.2 Material object and trajectory are distinct

For material object `A`, its trajectory in a chosen frame is:

$$
\mathbf r_A(t).
$$

Use the sentence:

> **The material object is the thing we follow. Its trajectory records what that thing does.**

Consequences the teacher should preserve:

- the material object owns inertial mass and net force;
- the trajectory records positions through time;
- inertial acceleration can be read from the trajectory;
- a trajectory does not itself own mass or net force;
- the same material object can have different trajectories in different frames;
- two different material objects can follow the same trajectory without sharing a mass;
- a trajectory alone does not reveal inertial mass or physical force contributions.

### 4.3 The addressed Newton-II triplet

For one material object `A`, over the same relevant interval and in the same inertial frame:

$$
\mathbf F_{\mathrm{net}}[A]=m[A]\mathbf a[A].
$$

| Quantity | Type | Unit | Owner |
|---|---|---|---|
| Inertial mass `m[A]` | positive scalar | `kg` | material object `A` |
| Inertial acceleration `a[A]` | vector | `m s^-2` | read for `A` in the chosen inertial frame |
| Net force `F_net[A]` | vector | `N` | material object `A` over the relevant interval |

The unit relation is:

$$
1\ \mathrm N=1\ \mathrm{kg\,m\,s^{-2}}.
$$

A nonzero vector answer without a direction is incomplete.

### 4.4 The thin net-force handle

Use:

> **Net force is one vector belonging to the selected material object, measured in newtons, and related to that object's inertial mass and inertial acceleration by Newton II.**

The vector may be:

- supplied as an opaque value; or
- inferred from the material object's supplied mass and trajectory-read acceleration.

Do not yet say that net force is:

- all forces added together;
- the reading of a newton meter;
- a single push or pull;
- the most noticeable physical interaction;
- “the force that causes acceleration.”

Newton II can infer the vector required by the motion without revealing its physical provenance.

### 4.5 The mass handle

The active mass in Newton II is **inertial mass**: the positive scalar `m[A]` supplied for material object `A`.

Student-facing rule:

> **A given mass belongs to a particular material object. Keep using it for that object unless something happens that makes reuse uncertain.**

Ordinary changes that do not by themselves cancel the binding include:

```text
moving to a new place
speeding up or slowing down
stopping
reversing direction
turning
receiving a different supplied net force
following a different trajectory
```

Automatic reuse must be suspended after triggers such as:

```text
piece breaks off
object splits
objects merge
material enters or leaves
continuous leakage or ejection
confidence in the continuing target is lost
```

The safe conclusion is only:

> **The previously given mass is no longer licensed for automatic reuse.**

It does not follow that the mass is zero, that the new mass is known, or that the remainder automatically owns the old value.

### 4.6 Three uses of the word `mass`

All bands should encounter the distinction, but at different depths.

| Role | Classroom anchor | What NML2.1 says |
|---|---|---|
| Material-amount or density mass | `m = rho V`; how much material is present | distinct role; not silently substituted into Newton II without a licence |
| Gravitational mass | mass-side quantity in gravitational interaction; probed in weighing contexts | not automatically identified with inertial mass |
| Inertial mass | the positive scalar in Newton II | the supplied mass used in this lesson |

The same caution applies to additivity:

```text
material-amount additivity
measured-mass additivity as an empirical, tolerance-dependent regularity
representative or ledger-mass additivity requiring an additional licence
```

NML2.1 names these as different claims and derives none of their identifications.

### 4.7 Newton II is a constraint, not an information generator

| Information supplied for one addressed object | What Newton II determines |
|---|---|
| Nothing | Nothing |
| Mass only | Neither acceleration nor net force uniquely |
| Net force only | Neither mass nor acceleration uniquely |
| Acceleration only | Neither mass nor net force uniquely |
| Mass and net force | Acceleration |
| Mass and acceleration | Net force |
| Suitable nonzero net force and acceleration | Inertial-mass magnitude |
| All three | Consistency check |

The algebraic forms are:

$$
\mathbf a=\frac{\mathbf F_{\mathrm{net}}}{m},
\qquad
\mathbf F_{\mathrm{net}}=m\mathbf a,
\qquad
m=\frac{|\mathbf F_{\mathrm{net}}|}{|\mathbf a|}
\quad (\mathbf a\ne\mathbf 0).
$$

For finite positive inertial mass:

$$
\mathbf a=\mathbf 0
\quad\Longleftrightarrow\quad
\mathbf F_{\mathrm{net}}=\mathbf 0.
$$

This does not imply zero velocity, freedom from all physical influences, or absence of force contributions. The `0/0` trial determines no mass.

### 4.8 Three licensed routes to trajectory so far

| Route | Starting information | Operation |
|---|---|---|
| Observation | successive positions and times | track and record the trajectory |
| Newton I | free particle in an inertial frame, plus initial position and velocity | continue uniform motion |
| Newton II | material object, supplied inertial mass, supplied net-force history or rule, inertial frame, initial position and velocity | calculate acceleration, update velocity, construct trajectory |

“Three and only three” means three routes licensed by the mechanics taught so far.

### 4.9 Acceleration can be known before the future trajectory

Continuous representation:

$$
\mathbf a(t)=\frac{\mathbf F_{\mathrm{net}}(t)}{m},
$$

$$
\mathbf v(t)=\mathbf v_0+\int_{t_0}^{t}\mathbf a(s)\,ds,
$$

$$
\mathbf r(t)=\mathbf r_0+\int_{t_0}^{t}\mathbf v(s)\,ds.
$$

Discrete learner handle:

```text
calculate or receive the acceleration arrow
    -> change the velocity arrow
    -> use the new velocity to draw the next path segment
    -> repeat
```

Acceleration alone does not uniquely determine a trajectory. Initial position, initial velocity, reference frame, and an acceleration history or rule are also needed.

---

## 5. The Installed Student Trace

The target behaviour is not merely “substitute into `F = ma`.” It is:

```text
1. Identify the demanded material object.
2. Put that object's data in one row or on one card.
3. Check target, interval, frame, quantity type, unit, and direction.
4. Ask which two independent triplet values are available.
5. Calculate the third, or state precisely why it is not determined.
6. Separate the Newton-II value from its physical provenance.
7. If a trajectory is demanded, add initial conditions and build it.
8. Before reusing mass later, check whether a reuse trigger occurred.
9. Halt when the old mass is no longer licensed.
```

Young learner mnemonic:

```text
Whose thing?
Whose number?
Which two corners?
Which direction?
What happens next?
May the mass card stay?
```

---

## 6. Learning Outcomes by Band

| Competence | Band I — upper primary / early secondary | Band II — GCSE / A level | Band III — introductory university |
|---|---|---|---|
| Material-object ownership | match each value to one named object; reject number borrowing | use rows and `m[A]`, `a[A]`, `F_net[A]` notation | audit target, interval, frame, and provenance explicitly |
| Object versus trajectory | say “thing” versus “motion record” | distinguish bearer from graph/trajectory | distinguish physical target, representation, and frame dependence |
| Types and units | match `kg`, `N`, `m/s²`; add left/right | classify scalar/vector; use vector components when ready | maintain full vector and dimensional consistency |
| Newton-II use | mainly find acceleration or net force with integer values | use all three algebraic forms in suitable cases | treat Newton II as a vector constraint and consistency condition |
| Information audit | recognise that two filled corners are needed | classify supplied/unknown/not determined/zero | distinguish unknown, absent, undefined, inconsistent, and unlicensed |
| Net-force provenance | say “the problem gave the arrow” | infer `F_net` without naming contributions | state precisely what Newton II establishes and withholds |
| Mass meanings | recognise that the lesson's `kg` number is inertial mass, not automatically a scale or material-amount result | sort density, gravitational, and inertial uses | analyse the three roles and three additivity claims explicitly |
| Force-to-trajectory route | update simple arrows over equal time steps | use `Delta v = a Delta t` and construct a stepped path | use integrals or differential equations with constant supplied mass |
| Three trajectory routes | sort picture scenarios | state starting data for each route | compare observational, Newton-I, and Newton-II inference structures |
| Mass reuse | stop after a visible split/loss | run audit-then-calculate and resume only after a new binding | diagnose piecewise re-licensing and the open-system boundary |

---

## 7. Materials and Preparation

### Core materials

- one opening slide or card containing the boat/table/cup cross-target trap;
- coloured owner cards or highlighters;
- one three-slot Newton-II triplet card per material object;
- mass, acceleration, and net-force quantity cards;
- a trajectory card separate from the picture or model of the material object;
- arrow tiles or a grid for the force-to-trajectory activity;
- a final two-scene break/split/leak image;
- exit tickets.

### Recommended optional materials

- a supplied-force simulation in which mass, net-force vectors, time step, initial position, and initial velocity are exact inputs;
- low-friction carts with already supplied masses for a qualitative same-action comparison;
- several markers on one translating cart, used only to reinforce that one object may have several motion records;
- a short clip of a material object visibly losing a piece.

### Materials to avoid as core evidence

- a weighing scale presented as an automatic inertial-mass instrument;
- a newton meter presented as a net-force meter;
- multi-force apparatus requiring friction, normal reaction, tension, weight, or force addition;
- rockets or leaking carts as solved examples.

---

## 8. Lesson at a Glance

The same conceptual sequence is preserved across bands. Representation and depth change; the trace does not.

| Segment | Main purpose | Band I | Band II | Band III |
|---|---|---:|---:|---:|
| 1. Arithmetic right, physics wrong | create demand for ownership | 5 min | 7 min | 8 min |
| 2. Thing versus motion record | reactivate NML1 and separate object from trajectory | 7 min | 8 min | 10 min |
| 3. Repair with the addressed triplet | install same-object Newton II | 12 min | 16 min | 18 min |
| 4. What can Newton II determine? | types, units, zero, and input-count discipline | 8 min | 12 min | 14 min |
| 5. Which `mass` is this? | distinguish inertia from gravity and material amount | 7 min | 10 min | 16 min |
| 6. From net force to a future path | reverse the NML1 route | 12 min | 16 min | 20 min |
| 7. The mass card loses its licence | install reuse triggers and the burn | 5 min | 7 min | 10 min |
| 8. Exit trace | reveal what was installed | 4 min | 4 min | 4 min |
| **Total** |  | **60 min** | **80 min** | **100 min** |


---

## 9. Segment-by-Segment Draft

## 9.1 Segment 1 — Arithmetic Right, Physics Wrong

**Time:** Band I 0–5; Band II 0–7; Band III 0–8

### Teacher aim

Create a failure that cannot be repaired by better arithmetic or unit checking. The class should discover that Newton II requires **ownership**.

### Opening problem

Display:

| Material object | Supplied inertial mass | Supplied net force |
|---|---:|---|
| Boat | `5 kg` | `20 N` right |
| Table | `10 kg` | `50 N` right |
| Cup | `5 kg` | `25 N` left |

Ask for the boat's acceleration, then deliberately write:

$$
a[\text{boat}]=\frac{50\ \mathrm N}{5\ \mathrm{kg}}
=10\ \mathrm{m\,s^{-2}}\text{ right}.
$$

Ask:

> The division is correct. The units are correct. Why is this not the boat's acceleration?

Expected answer:

> `50 N` belongs to the table, not the boat.

Then ask:

> What would stop this error before the calculation began?

Desired proposals:

```text
put each object's information in one row
use matching colours
write the object's name beside every number
use m[boat], F_net[boat], and a[boat]
```

### Band I version

Use large object cards and coloured number cards. A student physically places each value beneath its owner. Avoid bracket notation until the repair has been understood concretely.

Teacher line:

> “The number did not become wrong. It belonged to the wrong thing.”

### Band II version

Require students to rewrite the valid boat calculation:

$$
\mathbf a[\text{boat}]
=\frac{\mathbf F_{\mathrm{net}}[\text{boat}]}{m[\text{boat}]}
=4\ \mathrm{m\,s^{-2}}\text{ right}.
$$

Ask why dimensional correctness is necessary but not sufficient.

### Band III version

Add a second invalid account using the same object but mismatched intervals or frames:

```text
m[A] from the supplied binding
F_net[A] over interval I_2
a[A] read over interval I_1
```

or:

```text
F_net[A] stated in the laboratory account
a[A] read in an accelerating frame
```

Ask students to identify the three independent audits:

```text
target
interval
frame
```

### Board

```text
Arithmetic can be correct while the Newton-II account is invalid.

First question:
Whose quantity is this?
```

### Error shapes exposed

- treating `F = ma` as a relation among any values with matching units;
- reading visual proximity as ownership;
- assuming the demanded object automatically owns every number in the paragraph;
- checking arithmetic before checking referents.

---

## 9.2 Segment 2 — The Thing and Its Motion Record

**Time:** Band I 5–12; Band II 7–15; Band III 8–18

### Teacher aim

Reactivate NML1's trajectory-to-acceleration route while preventing the trajectory from becoming the owner of mass and net force.

### Set-up

Show separately:

1. a picture or model of cart `A`;
2. a graph or dotted trajectory labelled `r_A(t)`.

Physically separate the cards.

Ask:

```text
Which one can lose a piece?
Which one can have a mass in kilograms?
Which one records positions through time?
Which one can be differentiated to read acceleration?
Which one changes when the reference frame changes?
```

Expected structure:

```text
material object A:
    continuing physical thing
    owns m[A]
    owns F_net[A]

trajectory r_A(t):
    time-indexed record in a frame
    yields velocity and acceleration
    does not own mass or force
```

### Teacher script

> “Last lesson, we learned to read acceleration from a trajectory. Today we attach that acceleration back to the material object whose motion the trajectory records.”

> “The curve is not the cart. The curve is a record of the cart.”

> “Mass and net force belong to the material object. Acceleration can be read from the object's trajectory.”

### Band I version

Use the words **thing** and **motion trail** first.

```text
thing: the cart
motion trail: the marks showing where it went and when
```

Have students place the `4 kg` card on the cart picture and an acceleration arrow on the motion-trail card, then connect the arrow back to the cart with a line.

### Band II version

Use one material object shown in two frames. Ask:

> Are these two trajectories two objects?

Expected answer: no; one material object can have different trajectories in different frames.

Then show two objects with the same trajectory and ask whether their masses must agree. Expected answer: no.

### Band III version

Use the distinction:

```text
bearer / target
versus
representation / trajectory
```

Ask what information a complete `r_A(t)` still fails to determine if `F_net` is unconstrained. Expected answer: inertial mass magnitude and physical force provenance.

### Board

```text
The material object is the thing we follow.
Its trajectory records what that thing does.

trajectory -> inertial acceleration
material object -> owns mass and net force
```

### Quick diagnostic

> A trajectory is drawn but the material object it belongs to is not identified. What Newton-II calculation is blocked?

Expected answer: no addressed mass or net-force value can be joined to that trajectory-read acceleration.

---

## 9.3 Segment 3 — Repair With the Addressed Triplet

**Time:** Band I 12–24; Band II 15–31; Band III 18–36

### Teacher aim

Install Newton II as one same-owner relation rather than a symbol pattern.

### The triplet card

Give each material object one card:

```text
MATERIAL OBJECT: A

inertial mass:          m[A] = ______ kg
inertial acceleration: a[A] = ______ m/s², direction ______
net force:             F_net[A] = ______ N, direction ______
```

Place the equation only after the ownership slots are visible:

$$
\mathbf F_{\mathrm{net}}[A]=m[A]\mathbf a[A].
$$

Teacher line:

> “The equation does not merely tell us how three numbers multiply. It tells us that three quantities belonging to one material object must fit together.”

### Core activity: owner first, calculation second

Students receive three short problems. For every problem they must:

1. circle the demanded material object;
2. mark every value's owner;
3. copy only that object's data onto one triplet card;
4. choose the algebraic form;
5. calculate;
6. include direction and unit.

The teacher should refuse to accept a bare numerical answer until the owner row is visible.

### Quantity and unit installation

Build the table together:

| Slot | Type | Unit | Direction? |
|---|---|---|---|
| `m[A]` | positive scalar | `kg` | no |
| `a[A]` | vector | `m s^-2` | yes when nonzero |
| `F_net[A]` | vector | `N` | yes when nonzero |

Then derive the unit:

$$
[\mathbf F]=[m][\mathbf a]
=\mathrm{kg\,m\,s^{-2}}
=\mathrm N.
$$

### Band I version

Use a triangle with the object name printed in the centre and the three values around it. Keep examples one-dimensional:

```text
right / left
up / down
```

Core forms:

```text
a = F_net / m
F_net = m a
```

Mass inference may be shown only in a clear nonzero whole-number example and need not be an assessed objective.

Recommended examples:

```text
m[A] = 4 kg
F_net[A] = 12 N right
-> a[A] = 3 m/s² right

m[B] = 3 kg
a[B] = 2 m/s² left
-> F_net[B] = 6 N left
```

### Band II version

Use all three algebraic forms, including a suitable nonzero mass inference:

$$
m[A]=\frac{|\mathbf F_{\mathrm{net}}[A]|}{|\mathbf a[A]|}.
$$

Require students to state that positive mass means `F_net` and `a` point in the same direction in a consistent Newton-II triplet.

Include one unit-valid but target-invalid equation:

$$
\mathbf F_{\mathrm{net}}[A]=m[B]\mathbf a[A].
$$

### Band III version

Treat the equation as a vector constraint. Include:

$$
m[A]=2\ \mathrm{kg},
\qquad
\mathbf F_{\mathrm{net}}[A]
=(6\hat{\mathbf i}-8\hat{\mathbf j})\ \mathrm N.
$$

Students find:

$$
\mathbf a[A]
=(3\hat{\mathbf i}-4\hat{\mathbf j})\ \mathrm{m\,s^{-2}}.
$$

Then give all three values with a deliberately nonparallel `F_net` and `a`; ask whether a positive scalar mass can make the triplet consistent. Expected answer: no.

### Board

```text
ONE MATERIAL OBJECT
ONE RELEVANT INTERVAL
ONE INERTIAL FRAME

F_net[A] = m[A] a[A]

mass: scalar, kg
acceleration: vector, m/s²
net force: vector, N
```

### Teacher feedback target

Reward the audit behaviour:

```text
You found the owner before the operation.
You kept one object on one row.
You preserved the direction.
You rejected an equation whose units worked but whose owner did not.
```

---

## 9.4 Segment 4 — What Can Newton II Actually Determine?

**Time:** Band I 24–32; Band II 31–43; Band III 36–50

### Teacher aim

Prevent the three rearrangements from being mistaken for three independent information sources.

### Activity: “Can Newton II answer yet?”

Give each group a triplet card and information cards. Reveal inputs in stages.

Ask after each reveal:

> What, if anything, is uniquely determined now?

Use the sequence:

```text
no cards
mass only
net force only
acceleration only
mass + net force
mass + acceleration
nonzero net force + acceleration
all three
```

The desired reaction is:

```text
one value alone -> not enough
appropriate two values -> third can be found
all three -> check whether they fit
```

Teacher line:

> “The equation constrains values. It does not manufacture observations.”

### The zero branch

Present a material object with finite positive inertial mass and zero acceleration.

Ask students to choose every licensed conclusion from:

```text
F_net = 0
velocity = 0
no force contributions exist
the object is free
mass = 0
```

Only `F_net = 0` follows from Newton II.

Then ask:

> Can `m = F_net/a` find the mass when both are zero?

Expected answer: no; `0/0` does not determine a mass.

### Classification vocabulary

Band II and III students should classify statements using:

```text
zero
unknown
not supplied
not determined by the supplied information
undefined
inconsistent
calculation not licensed
```

Examples:

| Case | Classification |
|---|---|
| `a[A]=0` for a known finite positive mass | zero acceleration and zero net force |
| mass value omitted | not supplied |
| only mass supplied; ask for acceleration | not determined by the available information |
| `0/0` mass inference | indeterminate by that trial |
| nonparallel supplied `F_net` and `a` for positive scalar mass | inconsistent triplet |
| old mass used after a split | calculation not licensed |

### Band I version

Use the phrase:

> “Two filled corners are needed to find the empty corner.”

Do not turn it into a general rule without the zero caveat. Use picture cards for:

```text
zero
blank
stop sign
```

### Band II version

Students complete the full information table and one all-three consistency check. Include a moving object with `F_net=0` to block the misconception that zero force means zero velocity.

### Band III version

Ask students to separate:

```text
law constraint
empirical input
supplied convention
missing referent
failed licence
```

Use the prompt:

> “Which quantity does Newton II calculate first when no values are supplied?”

Expected answer: none.

### Board

```text
Newton II is not an information generator.

two suitable addressed values -> third value
all three values -> consistency check
no independent values -> no numerical output
```

---

## 9.5 Segment 5 — Which `Mass` Is This?

**Time:** Band I 32–39; Band II 43–53; Band III 50–66

### Teacher aim

Make the lesson's supplied inertial mass explicit and prevent ordinary weighing or material-amount intuitions from being silently inserted into Newton II.

### Opening contrast: Earth and Moon

Ask:

> The same cart receives the same supplied sideways net-force vector on Earth and on the Moon. Its supplied inertial mass is unchanged. Compare its sideways acceleration.

Expected answer:

$$
\mathbf a=\frac{\mathbf F_{\mathrm{net}}}{m}
$$

is unchanged.

Teacher line:

> “Lifting became easier on the Moon. The same sideways Newton-II response did not.”

This separates the ordinary fusion:

```text
hard to lift
hard to accelerate sideways
```

### Three-card mass sort

Prepare three cards:

```text
m = rho V
weighing / gravitational interaction
m in F_net = m a
```

Students sort them under:

```text
material-amount mass
gravitational mass
inertial mass
```

Then state:

> “In ordinary situations these values are closely connected, but this lesson does not prove or automatically assume those connections. The mass printed on today's Newton-II card is supplied inertial mass.”

### Additivity caution

Present three claims without deriving them:

```text
1. Material amounts can be combined by the construction being used.
2. Measured masses often add within an empirical tolerance.
3. A representative ledger mass can be assigned additively only under an additional licence.
```

The purpose is not to teach advanced exceptions. It is to prevent “mass adds” from appearing as one unqualified logical fact.

### Band I version

Use icons:

```text
bucket / volume card -> how much material
planet / scale card -> gravity and weighing
cart / arrow card -> how motion responds in Newton II
```

Required takeaway:

> “Today the `kg` card is given for the cart's Newton-II response. We are not using a scale to create it.”

The additivity caution can be one sentence:

> “Putting things together does not yet give us permission to invent the new Newton-II mass card.”

### Band II version

Use the full three-card sort and the Earth/Moon question. Ask students to identify which meaning is active in:

```text
m = rho V
weighing context
F_net = m a
```

Do not require a derivation of equivalence or additivity.

### Band III version

Use a short structured mini-lecture:

| Claim | Status in NML2.1 |
|---|---|
| material-amount additivity | construction-level claim in the chosen material description |
| measured-mass additivity | empirical and tolerance-dependent |
| representative/ledger additivity | requires an explicit adequacy or composition licence |
| gravitational–inertial identification | physical equivalence not established here |

Ask students to diagnose the textbook move:

> A problem states a density and volume, calculates `rho V`, and immediately inserts the result into Newton II. Which identification has been supplied, and which has merely been assumed?

### Optional qualitative demonstration

Use already-labelled carts of different supplied inertial masses under the same repeatable sideways action programme. Compare initial motion-changes. Treat the action qualitatively unless an exact `F_net` has been supplied by a simulation or later force-accounting certificate.

### Board

```text
Today's m:
supplied inertial mass belonging to the material object

Do not silently identify:
material amount = gravitational mass = inertial mass

Earth/Moon:
same cart + same sideways F_net -> same sideways a
```

---

## 9.6 Segment 6 — From Newton II to a Future Path

**Time:** Band I 39–51; Band II 53–69; Band III 66–86

### Teacher aim

Reverse the NML1 route and make clear that knowing acceleration is not yet knowing the whole trajectory.

### Bridge from NML1

Write side by side:

```text
NML1:
known trajectory -> inertial acceleration

NML2.1:
given mass + supplied net force -> inertial acceleration
                                  -> velocity
                                  -> trajectory
```

Ask:

> Can Newton II tell us the acceleration before we know where the object will go next?

Expected answer: yes.

Then ask:

> Does the acceleration alone fix the whole trajectory?

Expected answer: no; initial position, initial velocity, frame, and acceleration history or rule are also required.

### Core force-to-trajectory activity

Every student receives:

```text
material object A
supplied m[A]
initial position
initial velocity arrow
one supplied F_net[A] arrow for each equal interval
```

For each interval:

```text
1. calculate a[A] = F_net[A]/m[A]
2. use the acceleration to change the velocity
3. use the updated velocity to draw the next path segment
4. repeat
```

### Band I version: arrow stepping

Begin in one dimension.

Example:

```text
m[A] = 2 kg
F_net[A] = 2 N right during each beat
initial velocity = 1 arrow-unit right
```

The acceleration is one velocity-arrow unit added to the right each beat. Students draw successively longer motion arrows and path segments.

Then, if the group is ready, give a sideways acceleration arrow to a moving token and let the path begin to bend.

Use two tokens with the same acceleration arrows but different initial velocity arrows. Ask why they trace different paths.

### Band II version: equal-time numerical stepper

Use:

$$
\Delta \mathbf v_n=\mathbf a_n\Delta t,
\qquad
\mathbf v_{n+1}=\mathbf v_n+\Delta\mathbf v_n.
$$

The worksheet should state the position-stepping convention explicitly. A simple graphical version is preferable:

```text
use the new velocity arrow to draw the next equal-time path segment
```

Include:

- acceleration along the velocity;
- acceleration opposite the velocity;
- acceleration perpendicular to the velocity;
- a zero-net-force interval;
- two different initial velocities under the same acceleration history.

Students must preserve velocity through the zero-acceleration interval rather than setting it to zero.

### Band III version: continuous representation

Use constant supplied mass and a supplied `F_net(t)` or `F_net(r)`:

$$
\dot{\mathbf v}=\frac{\mathbf F_{\mathrm{net}}(t)}{m},
\qquad
\dot{\mathbf r}=\mathbf v.
$$

Students identify the required initial conditions and solve or set up one simple case. Suitable examples include:

- constant vector `F_net`;
- piecewise-constant supplied `F_net(t)`;
- a central or position-dependent **single opaque** `F_net(r)` supplied as a rule.

Do not decompose the vector into drag, gravity, spring, friction, or other contributions.

### Three-routes sorting activity

Finish by sorting three scenario cards:

1. successive observed positions and times;
2. free particle in an inertial frame with initial conditions;
3. material object with supplied mass, supplied net-force rule, inertial frame, and initial conditions.

Students label:

```text
observation
Newton I
Newton II
```

Then ask what input is missing from an incomplete example of each route.

### Critical question

> A material object's mass and net force are supplied, so its acceleration is known. Its initial velocity is not supplied. Is its future trajectory known?

Expected answer: no. Acceleration is known; the trajectory remains underdetermined.

### Board

```text
Acceleration can be known before the future trajectory.

But trajectory needs:
initial position
initial velocity
reference frame
acceleration history or rule
```

---

## 9.7 Segment 7 — The Mass Card Loses Its Licence

**Time:** Band I 51–56; Band II 69–76; Band III 86–96

### Teacher aim

End at the exact boundary where Newton II still exists but its mass input is no longer licensed for automatic reuse.

### Part A: keep or suspend?

Show event cards and ask students to sort them.

**Continue ordinary reuse:**

```text
object moves elsewhere
object speeds up
object slows down
object stops
object reverses
object turns
supplied net force changes
trajectory changes
```

**Suspend automatic reuse:**

```text
piece breaks off
object splits
objects merge
material is added
material leaks or is ejected
later target cannot confidently be identified with the earlier one
```

Teacher line:

> “Motion changing does not make the mass card fall off. A change in what material object the card belongs to might.”

### Part B: the younger burn

Scene 1:

```text
material object A
m[A] = 4 kg
```

Scene 2:

```text
a visible piece has broken off
8 N right is supplied for the remaining target
```

Invite the tempting calculation:

$$
a=\frac{8\ \mathrm N}{4\ \mathrm{kg}}.
$$

The complete correct answer is:

> **HALT: the earlier `4 kg` is no longer licensed for automatic reuse for the remainder.**

Students must reject:

```text
the remainder automatically keeps 4 kg
the new mass is zero
Newton II creates the missing mass
use the nearest available mass number
```

If a third scene explicitly supplies a new inertial mass for the remainder, the calculation may resume from that new binding.

### Band I version

Offer three cards:

```text
CALCULATE
GUESS
STOP AND ASK FOR THE NEW MASS
```

The success is choosing the stop card and explaining that the object lost a piece.

### Band II version

Use an audit-then-calculate table:

| Scene | Earlier mass reusable automatically? | Calculation action |
|---|---|---|
| cart changes direction | yes | calculate |
| cart loses a block | no | halt |
| new mass explicitly supplied | yes, from new binding | resume |

Give tempting numerical values after the failed row. Award full credit for refusing them.

### Band III version: continuous-expiry boundary

Present a leaking cart or rocket whose retained target continuously loses material. Invite the naive substitution:

$$
\mathbf F_{\mathrm{net}}=m(t)\mathbf a.
$$

Then state the boundary:

> The equation alone does not determine the retained target's open-system dynamics. The state and momentum carried by departing material matter. NML2.1 neither supplies the target-persistence machinery nor the momentum account needed to solve the case.

Do not derive a rocket equation or variable-mass formula.

### Bridge to NML2.2

Ask:

> How were we ever entitled to say that the later thing was the same mass-bearing material object as the earlier thing?

Close with:

> “NML2.1 can consume a supplied mass binding. NML2.2 asks how the target and its mass address are built, carried, challenged, and repaired.”

### Board

```text
Mass reuse is licensed separately from the equation that consumes mass.

ordinary motion-change -> keep the supplied mass binding
split / merge / material flow / identity loss -> suspend automatic reuse

No licence -> no substitution
```

---

## 9.8 Segment 8 — Exit Trace

**Time:** final 4 minutes in every band

The exit should test the route, not only arithmetic.

### Band I exit

1. Circle the object whose acceleration is asked for.
2. `m[A]=3 kg`, `F_net[A]=6 N` left. Find `a[A]` with unit and direction.
3. A piece breaks off before the next calculation. Choose: reuse, guess, or stop.

### Band II exit

1. Explain why `F_net[table]/m[boat]` is not the boat's acceleration even if the units work.
2. Only `m[A]` is supplied. What does Newton II determine?
3. `m[A]` and `F_net[A]` determine acceleration, but no initial velocity is supplied. What is known and what is not?
4. A fragment leaves. Write the minimum safe mass statement.

### Band III exit

1. State the target, interval, and frame conditions on the Newton-II triplet.
2. Distinguish the three mass roles and identify which one is supplied here.
3. Explain why a complete trajectory can yield acceleration without yielding inertial-mass magnitude.
4. Explain why `m(t)a` alone does not close the leaking-target problem.

### Desired final sentence from students

> **Newton II can use a mass value, but it does not itself establish the owner, origin, persistence, or physical force composition behind that value.**


---

## 10. Signature Worksheet Specifications

The worksheets are installation objects, not a dump of every exercise in the content bank. Four sheets are sufficient to carry the day's trace.

## 10.1 Sheet A — Owner First

### Purpose

Install the reaction:

```text
Before calculating, identify the material object and attach every value to it.
```

### Core layout

#### Part 1 — Mark the owners

A paragraph names three material objects. Students:

1. circle every material-object name;
2. assign one colour or symbol to each object;
3. mark each mass, acceleration, and net-force value with its owner's colour;
4. cross out irrelevant values.

#### Part 2 — One object, one row

| Material object | `m` | `F_net` | `a` | Requested? |
|---|---:|---|---|---|
| Boat |  |  |  |  |
| Table |  |  |  |  |
| Cup |  |  |  |  |

Instruction:

> **Do not calculate until the demanded object's row is complete.**

#### Part 3 — Diagnose the trap

Give:

$$
\mathbf a[\text{boat}]
=\frac{\mathbf F_{\mathrm{net}}[\text{table}]}{m[\text{boat}]}.
$$

Ask students to explain why:

- arithmetic may be possible;
- dimensions may be correct;
- the result is still not the boat's Newton-II acceleration.

### Band variations

- **Band I:** use pictures, lines, and colours; bracket notation appears only in the final row.
- **Band II:** require `m[A]`, `a[A]`, and `F_net[A]` notation.
- **Band III:** add interval and frame mismatches and ask for a complete audit sentence.

---

## 10.2 Sheet B — Triplet Cards and the Information Gate

### Purpose

Install Newton II as a constraint and distinguish calculation from missing information.

### Card surface

```text
MATERIAL OBJECT: __________
FRAME: __________
INTERVAL: __________

m[ ]       = __________ kg
F_net[ ]   = __________ N, direction __________
a[ ]       = __________ m/s², direction __________

[ ] calculate the missing value
[ ] perform a consistency check
[ ] not enough information
[ ] calculation not licensed
```

### Required rows

1. mass and net force supplied;
2. mass and acceleration supplied;
3. nonzero net force and acceleration supplied;
4. mass only;
5. no values;
6. all three values consistent;
7. all three values inconsistent;
8. `F_net=0`, `a=0`, mass demanded;
9. correct values but wrong target owner;
10. values present after a mass-reuse trigger.

### Teacher marking rule

Award the information classification before the arithmetic mark. A numerically correct value obtained from an unlicensed row receives no calculation credit.

---

## 10.3 Sheet C — From Force to Trajectory

### Purpose

Reverse NML1's direction and install:

```text
mass + net force -> acceleration -> velocity -> trajectory
```

### Band I surface

| Beat | Mass card still attached? | Supplied force arrow | Acceleration arrow | New velocity arrow | Next path segment |
|---|---|---|---|---|---|

Use large arrows and integer ratios. Begin one-dimensionally; add one turning example only after the speed-change case is secure.

### Band II surface

| Step | `m[A]` | supplied `F_net[A]` | `a[A]` | `Delta v` | next `v` | next path segment |
|---|---:|---|---|---|---|---|

State:

$$
\Delta\mathbf v=\mathbf a\Delta t.
$$

The sheet must print its position-update convention. The learning target is the sequence of operations, not numerical-integration sophistication.

Required rows:

- force along velocity;
- force opposite velocity;
- force perpendicular to velocity;
- zero-force interval;
- same acceleration history with a different initial velocity.

### Band III surface

Provide one of:

$$
\mathbf F_{\mathrm{net}}(t),
\qquad
\mathbf F_{\mathrm{net}}(\mathbf r),
$$

with constant supplied `m[A]` and initial conditions. Students:

1. write the governing first-order system;
2. identify the data required for uniqueness;
3. solve or numerically step a simple case;
4. state which result came from the law and which came from initial data.

### Required reflection

```text
Was acceleration known before the whole trajectory?
Why did two different initial velocities produce different trajectories?
Which of the three licensed trajectory routes did this sheet use?
```

---

## 10.4 Sheet D — Audit, Calculate, or Halt

### Purpose

Install persistent-but-defeasible mass reuse.

### Core layout

| Scene or interval | Event | Earlier mass reusable automatically? | Action | Reason |
|---|---|---|---|---|
| 1 | object changes position | yes | calculate | ordinary motion change |
| 2 | object turns | yes | calculate | trajectory change does not cancel mass |
| 3 | piece breaks off | no | halt | old binding uncertain for remainder |
| 4 | new inertial mass explicitly supplied | yes, from new binding | resume | new licensed input |
| 5 | two objects merge | no | halt | no combined mass supplied |
| 6 | material leaks continuously | no fixed old binding | halt at this lesson | open-system machinery absent |

### Required halt box

```text
HALT
The previously supplied mass is no longer licensed for automatic reuse.

This does NOT mean:
[ ] the mass is zero
[ ] the new mass is already known
[ ] the remainder automatically owns the original mass
[ ] Newton II creates the missing mass
```

### Assessment-regime note

For Band I and ordinary GCSE practice, ownership auditing should be rewarded even when a conventional examination would have expected blind substitution. Use the full refusal-as-correct-answer convention only in tasks whose wording explicitly makes the trigger visible and whose mark scheme honours the audit.

---

## 11. Demonstrations and Investigations

## 11.1 Supplied-force simulation — recommended formal centrepiece

A simulation is the cleanest formal demonstration because it can supply, without hidden force-sum assumptions:

```text
material-object label
inertial mass
net-force vector for each interval
initial position
initial velocity
time step
```

Students can observe the full chain:

```text
m + F_net -> a -> changing v -> trajectory
```

Recommended controls:

- mass slider;
- net-force magnitude and direction;
- initial velocity;
- pause-by-step mode;
- simultaneous display of addressed triplet values;
- optional two-object mode for the cross-target trap.

## 11.2 Low-friction carts under a repeatable sideways action

Use already supplied or previously certified inertial masses. Apply the same repeatable action programme for equal durations and compare motion-change.

Use the demonstration qualitatively unless one exact net-force vector has genuinely been supplied. Do not rename a force-sensor reading as `F_net` without the later force-accounting certificate.

Desired noticing:

```text
same action programme + larger inertial mass -> smaller motion-change
```

## 11.3 Several markers on one translating cart

Track several markers while continuing to refer to one cart. Use the scene only to reinforce:

```text
one material object
several motion records
one supplied mass owner
```

Do not formalise redundancy, tolerance, or lump construction. Those belong to NML2.2.

## 11.4 Newton-meter misconception demonstration

If a newton meter is shown, ask:

> What did the instrument directly measure?

Safe answer:

> A force transmitted through the meter.

Then ask:

> What additional later analysis would be required before identifying that reading with the cart's net force?

Use this only as a misconception probe, not as the source of the formal net-force value.

## 11.5 Planetary trajectory investigation — Band III extension

Provide time-indexed orbital data and a supplied planetary mass. Students follow:

```text
trajectory
    -> acceleration
    -> Newton-II-inferred net-force vector
```

Required label:

> This is a Newton-II inference from motion and supplied mass. It is not an independent net-force measurement or a derivation of the gravitational force law.

## 11.6 Visible mass-reuse failure

Show a material object visibly losing a piece. Freeze immediately after the event and ask the class to decide whether the earlier mass may be reused before showing any new numerical value.

The perceptual sequence should be:

```text
recognise the trigger
suspend automatic reuse
only then inspect later data
```

---

## 12. Signature Questions and Rubrics

## 12.1 Signature Question A — Same-Target Lock

> A boat has mass `5 kg` and supplied net force `20 N` right. A table has mass `10 kg` and supplied net force `50 N` right. A student uses `50 N / 5 kg` to find the boat's acceleration. What is wrong?

| Level | Response | Interpretation |
|---:|---|---|
| 0 | Performs the division without objection. | Quantities treated as free-floating numbers. |
| 1 | Says the answer “looks wrong” but cannot identify the structural error. | Context sensitivity without ownership discipline. |
| 2 | Says `50 N` belongs to the table. | Owner mismatch recognised. |
| 3 | Rebuilds the boat row and finds `4 m/s²` right. | Same-target calculation installed. |
| 4 | States the general rule: target, interval, and frame-qualified quantities must match. | Full addressed-triplet competence. |

## 12.2 Signature Question B — Constraint, Not Generator

> Newton II can be written in three algebraic forms. If no triplet values are supplied, which quantity does the law calculate first?

| Level | Response | Interpretation |
|---:|---|---|
| 0 | Chooses force, mass, or acceleration by habit. | Formula treated as an autonomous calculator. |
| 1 | Says “not sure” without explaining input dependence. | Weak boundary recognition. |
| 2 | Says none; more information is needed. | Constraint character recognised. |
| 3 | States that two suitable independent addressed values determine the third. | Input-count discipline installed. |
| 4 | Also handles all-three consistency and the `0/0` mass trial correctly. | Full triplet-boundary competence. |

## 12.3 Signature Question C — Acceleration Before Trajectory

> Material object `A` has a supplied inertial mass and a supplied net-force history, so its acceleration is known. Its initial velocity is not supplied. Is its future trajectory known?

| Level | Response | Interpretation |
|---:|---|---|
| 0 | Says yes because acceleration determines motion. | Acceleration collapsed into trajectory. |
| 1 | Says no but cannot identify missing information. | Correct intuition, weak trace. |
| 2 | Identifies initial velocity as missing. | Main initial-condition requirement recognised. |
| 3 | Adds initial position, frame, and acceleration history/rule. | Complete trajectory-input discipline. |
| 4 | Distinguishes the three licensed routes and locates this as the Newton-II route. | Full route competence. |

## 12.4 Signature Question D — Mass-Reuse Burn

> A `4 kg` material object visibly loses a piece. A later scene supplies `8 N` on the remainder but no new mass. What is the correct Newton-II response?

| Level | Response | Interpretation |
|---:|---|---|
| 0 | Uses `8/4`. | Blind value reuse. |
| 1 | Notices the split but guesses a smaller mass. | Trigger recognised; licence discipline absent. |
| 2 | Halts because the old mass is not automatically reusable. | Core boundary installed. |
| 3 | States that zero, the new value, and ownership by the remainder do not follow. | Safe-conclusion discipline installed. |
| 4 | Explains that target/address construction and new mass origination belong to later machinery. | Full handoff competence. |

## 12.5 Signature Question E — Earth/Moon Decorrelation

> The same cart receives the same sideways net-force vector on Earth and on the Moon. Its supplied inertial mass is the same. Compare the sideways accelerations.

Expected answer:

> They are the same. Gravitational circumstances and lifting difficulty differ, but the supplied inertial mass and sideways net force in Newton II are unchanged.

Main error exposed: treating inertial mass as nothing more than weight or difficulty lifting.

---

## 13. Criteria of Instillment

The lesson has succeeded when students begin to perform the following behaviours without a teacher reminder.

### 13.1 Basic criteria

| Criterion | Evidence |
|---|---|
| Owner-first attention | Student identifies the demanded material object before choosing numbers. |
| One-row discipline | Student keeps each object's triplet data together. |
| Object/trajectory distinction | Student attaches mass to the object and acceleration-readout to its trajectory without identifying them. |
| Type discipline | Student treats mass as scalar and acceleration/net force as vectors. |
| Direction discipline | Student includes a direction with every demanded nonzero vector answer. |
| Input-count discipline | Student asks whether two suitable independent values are present. |
| Zero discipline | Student returns zero net force from zero acceleration without claiming zero velocity or no contributions. |
| Provenance restraint | Student does not rename a meter reading, push, or guessed physical interaction as net force. |
| Motion-building behaviour | Student updates velocity before extending the path. |
| Reuse audit | Student checks whether the mass card survives a scene change. |
| Halt behaviour | Student refuses an unlicensed post-trigger substitution. |

### 13.2 Strong criteria

A stronger installation has occurred when the student spontaneously runs:

```text
What material object is demanded?
Which frame and interval are active?
Which values belong to that object?
Which are supplied, inferred, missing, or unlicensed?
Does the triplet fit as vectors?
What initial conditions are needed for a trajectory?
Did anything happen that invalidates automatic mass reuse?
```

### 13.3 Longitudinal criteria

Later lessons should reveal whether the student retains these distinctions:

- in the force-composition lesson, the student treats force contributions as the explanation of an already familiar `F_net` slot;
- in NML2.2, the student feels a real need for target and mass-address construction;
- in momentum/open-system lessons, the student understands why continuous material flow was a genuine boundary rather than an arbitrary prohibition;
- in centre-of-mass or composite lessons, the student does not assume additivity merely because two objects are shown together.

---

## 14. Common Misconceptions and Repairs

### 14.1 “The formula only cares about the numbers”

Repair:

> Newton II constrains addressed quantities. Correct arithmetic cannot repair an owner mismatch.

### 14.2 “The trajectory has the mass”

Repair:

> The trajectory is the time-indexed motion record. The material object whose motion it records owns the mass.

### 14.3 “Net force is the push I can see”

Repair:

> NML2.1 uses one supplied or inferred net-force vector. Which physical contributions produce it is a later question.

### 14.4 “A newton meter reads net force”

Repair:

> It reads a force transmitted through the meter. Equating that contribution with net force requires later force-accounting information.

### 14.5 “A scale gives the inertial mass automatically”

Repair:

> Weighing concerns the gravitational side and requires an equivalence account before its result is used as inertial mass. This lesson supplies inertial mass directly.

### 14.6 “Mass, weight, and amount of material are just one definition”

Repair:

> They are distinct roles whose ordinary agreement is a physical achievement, not a linguistic permission.

### 14.7 “Zero net force means the object is stopped”

Repair:

> Zero net force gives zero acceleration for finite positive mass. Velocity may be nonzero and constant.

### 14.8 “Zero net force means no physical contributions exist”

Repair:

> NML2.1 says only that the one net-force vector is zero. Contribution analysis is later.

### 14.9 “One rearrangement tells us which value is naturally first”

Repair:

> Rearrangement changes the demanded unknown, not the empirical source of information.

### 14.10 “Acceleration tells us the path”

Repair:

> Acceleration tells how velocity changes. A trajectory also requires initial conditions, frame, and the acceleration history or rule.

### 14.11 “If the object moves differently, its mass changed”

Repair:

> Changes of position, velocity, direction, acceleration, and net force do not by themselves cancel a supplied mass binding.

### 14.12 “The old mass belongs to the remainder after a piece breaks off”

Repair:

> The earlier value is no longer licensed for automatic reuse. The remainder requires a new binding or later reconstruction machinery.

### 14.13 “Writing `m(t)` solves variable-mass motion”

Repair:

> Open-system dynamics also depends on the momentum carried by entering or leaving material. NML2.1 halts before that machinery.

---

## 15. Teacher Warnings

### 15.1 Announce supplied status

Say:

```text
The problem supplies this material object.
The problem supplies its inertial mass.
The problem supplies this net-force vector.
```

Do not let a supplied value masquerade as a value derived by the lesson.

### 15.2 Do not formalise target construction early

Use ordinary recognition of cart, ball, cup, or planet. Do not open trackability, redundancy, tolerance, or lumping merely because the word `address` appears.

### 15.3 Do not let `address` become metaphysical language

At this stage, `m[A]` is bookkeeping that makes ownership visible. NML2.2 will explain how such an address is earned and carried.

### 15.4 Do not call net force “all the forces added together”

That sentence opens the force-sum branch. Keep `F_net` as one typed vector slot.

### 15.5 Do not use free-body diagrams

A free-body diagram demands force contributions and completeness judgements that NML2.1 has withheld.

### 15.6 Do not say “force causes acceleration”

Use:

> “Newton II relates the material object's net-force vector, inertial mass, and inertial acceleration.”

This avoids turning a mathematical relation into an unexplained causal slogan.

### 15.7 Do not use weight or normal-reaction calculations

Sideways examples are valuable precisely because they separate inertia from lifting and avoid multi-force accounting.

### 15.8 Do not present the three mass roles as already equal

The lesson names the distinctions and marks the missing equivalence. It does not need to resolve it.

### 15.9 Do not smuggle mass additivity

When two objects merge or one splits, halt unless a new mass is explicitly supplied. Do not total or partition inertial masses by intuition.

### 15.10 Do not let the trajectory stepper conceal its approximation

For discrete numerical work, print the update convention. The conceptual aim is operation order, not pretending a simple stepping rule is exact in every case.

### 15.11 Do not let acceleration become a complete future

Repeat:

```text
acceleration known
trajectory not yet determined
```

until initial conditions are supplied.

### 15.12 Do not solve the burn

The final split, leak, or rocket exists to create demand for later lessons. A teacher who supplies a variable-mass formula at the end erases the boundary the lesson was designed to reveal.

---

## 16. Compressed and Extended Variants

## 16.1 Compressed 45-minute version

| Time | Segment | Preserve |
|---:|---|---|
| 0–5 | cross-target trap | arithmetic-right/owner-wrong failure |
| 5–10 | object versus trajectory | bearer versus record |
| 10–22 | addressed triplet | owner, type, unit, direction |
| 22–29 | information gate | two values, zero branch |
| 29–39 | one force-to-path stepper | acceleration before trajectory |
| 39–45 | visible split and exit | halt behaviour |

The three-mass distinction is compressed to one explicit caution:

> “Today's supplied `kg` value is inertial mass. Material amount and gravitational weighing are different roles whose connection is not established here.”

Do not compress by dropping the opening trap or the final burn. They give the notation and boundary their purpose.

## 16.2 Two-session version

### Session A — Whose values fit together?

```text
cross-target trap
material object versus trajectory
addressed triplet
types and units
constraint / information gate
three meanings of mass
```

### Session B — What motion follows, and when must we stop?

```text
NML1 handoff
force-to-trajectory stepper
three licensed trajectory routes
zero-force interval
mass-reuse sort
split/leak burn
handoff to NML2.2
```

This is the preferred implementation when Band II students need substantial vector practice or when Band III students receive the full mass/additivity discussion.

## 16.3 Extended university seminar/lab

Add:

- vector consistency tests with nonparallel supplied data;
- piecewise-constant supplied `F_net(t)` and explicit re-licensing between phases;
- a simple position-dependent opaque net-force ODE;
- trajectory differentiation followed by Newton-II net-force inference;
- a short audit of three mass roles and three additivity claims;
- the leaking-cart boundary as the final unsolved problem.

Every advanced force remains one opaque supplied vector. Do not import drag-plus-gravity, spring-plus-friction, or other multi-contribution examples.

---

## 17. Age-Adapted Handles

| Concept | Band I wording | Band II wording | Band III wording |
|---|---|---|---|
| Material object | the continuing thing we follow | the physical target whose motion and mass are described | the identity-bearing target that owns addressed dynamical quantities |
| Trajectory | its timed motion trail | its position through time in a frame | the frame-dependent map `r_A(t)` |
| Address | the object's name on every card | bracket label showing quantity ownership | explicit referent and bookkeeping binding |
| Inertial mass | the given `kg` card that sets how much its motion changes for a net-force arrow | positive scalar in Newton II | supplied coefficient relating `F_net` and inertial acceleration |
| Net force | one supplied force arrow belonging to that thing | one supplied or Newton-II-inferred vector in newtons | thin typed force-accounting slot with physical provenance withheld |
| Constraint | two corners let us find the empty corner | two independent values determine the third | one vector relation plus external inputs and consistency conditions |
| Zero case | no acceleration arrow means zero net-force arrow | `a=0` iff `F_net=0` for finite positive mass | zero branch without force-provenance or free-particle overclaim |
| Trajectory construction | change the motion arrow, then draw the next step | update velocity from acceleration over equal intervals | integrate the first-order dynamical system from initial data |
| Mass reuse | keep the mass card unless the thing loses, gains, splits, or joins | supplied binding persists until an identifiable trigger | temporal use licence is defeasible and separate from Newton II |
| Halt | stop and ask for a new mass | old mass not licensed for automatic reuse | the required referent/input certificate has expired |

---

## 18. Consensus Deviation

| Standard first `F = ma` lesson | VD-native NML2.1 |
|---|---|
| Starts with the formula. | Starts with a correct-looking calculation that fails ownership. |
| Treats `m`, `a`, and `F` as values in a word problem. | Treats them as quantities addressed to one material object, interval, and frame. |
| Uses “force” as an intuitive push or pull. | Keeps `F_net` as one supplied or inferred vector until force composition is taught. |
| Often uses a newton meter as though it reads net force. | Separates transmitted meter force from the later net-force certificate. |
| Treats a scale value as unproblematic mass. | Marks the gravitational–inertial identification as unestablished here. |
| Treats mass as one obvious additive quantity. | Distinguishes material amount, gravitational mass, inertial mass, and three additivity claims. |
| Presents three rearrangements as three calculation recipes. | Presents one law constraint and asks what independent information exists. |
| Stops when the requested number is found. | Continues from acceleration to velocity and trajectory. |
| Treats acceleration as enough to predict motion. | Requires initial conditions, frame, and an acceleration history or rule. |
| Continues substituting after a split or leak. | Treats halting as the complete correct response when the mass licence fails. |

The sharpest deviation is:

> **The central skill is not rearranging `F = ma`; it is maintaining the referent and licence of every quantity long enough for the relation to mean anything.**

---

## 19. Optional Evaluation Design

The lesson can be tested against a conventional formula-first lesson.

### Prediction

Students receiving the addressed-triplet lesson should later produce fewer:

```text
cross-target substitutions
unit-correct owner errors
missing vector directions
meter/net-force collapses
zero-acceleration overclaims
acceleration/trajectory collapses
blind mass reuse after splits
```

### Assessment set

Use before and after:

1. the boat/table/cup cross-target problem;
2. a mass-only input-count problem;
3. a trajectory-read acceleration followed by a net-force provenance question;
4. a zero-acceleration case;
5. same acceleration history with different initial velocities;
6. a visible piece-loss halt problem.

Code error shapes rather than only total scores.

---

## 20. Final Teacher Summary

At the end, say:

> “Today we learned why `F = ma` is not a licence to combine any force number with any mass number. Newton II joins three quantities belonging to one material object.”

> “The material object is the thing we follow. Its trajectory is the record of what it does. We can read acceleration from that record, or use supplied mass and net force to obtain acceleration before the future path is known.”

> “The equation does not create its own information. We need suitable independent inputs. We also need initial conditions before acceleration becomes a trajectory.”

> “A supplied mass usually stays with the material object while it moves, turns, accelerates, stops, or reverses. But when the object splits, merges, gains material, loses material, or can no longer be confidently reidentified, automatic reuse stops.”

> “The next target-construction lesson asks how a material object earns and carries a mass address. A later force-composition lesson asks which physical contributions produce the net-force vector.”

### Final board

```text
NML1:
trajectory -> inertial acceleration

NML2.1:
material object A
    owns m[A]
    has trajectory r_A(t) -> a[A]
    owns F_net[A]

F_net[A] = m[A] a[A]

owner audit
-> information audit
-> calculate third triplet value
-> update velocity
-> construct trajectory
-> audit mass reuse

split / merge / material flow / lost identity
-> HALT automatic reuse
```

### Final working summary

NML2.1 is the first Newton-II lesson, but its deepest achievement is not algebraic. It teaches the learner to preserve the identity of the material object across the motion account, to distinguish the bearer from its trajectory, to understand Newton II as a typed and addressed constraint, and to carry the resulting acceleration forward into velocity and trajectory.

The lesson deliberately consumes three supplied objects that later lessons must explain:

```text
a continuing material object
a bound inertial-mass value
a net-force vector
```

It marks each debt instead of hiding it. The material object is provisionally recognised, not yet constructed. The mass is supplied, not yet originated. The net force is supplied or inferred, not yet decomposed. The equation is fully usable inside those boundaries.

The final student habit is:

> **Attach every quantity to its material object, run Newton II only when the inputs are licensed, and stop the moment the mass no longer has a secure owner.**

---

## 21. Source Use Within the Project

This draft was constructed from:

- `NML2_1_CONTENT.md` as the current content authority;
- `NM_L1_E7_integrated_complete_draft_d2(1).md` as the structural and pedagogical model;
- `NML2_student_facing_question_exercise_demonstration_bank_v1_d1(1).md` for candidate exercises, probes, rubrics, and demonstrations;
- `NML2_split_ratification_d1(1).md` and `NML2_1_lesson_drafting_context_v1(1).md` for the lesson split and banding rationale;
- the net-force, mass-pipeline, material-object, and point-particle bridge notes only where they remain consistent with the current content specification.

