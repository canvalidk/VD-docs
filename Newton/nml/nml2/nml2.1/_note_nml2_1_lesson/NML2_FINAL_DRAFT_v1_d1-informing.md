> **Informing copy — do not edit here.**
> **Home note:** `nml2_lesson`, draft `d1 (frozen terminal)` — `Newton/nml/nml2/NML2_FINAL_DRAFT_v1_d1.md`.
> Placed in `nml2.1` (informs `nml2_1_lesson`): the frozen v1 lesson whose supplied-target half this lesson replaces; sec 5 law-house, sheets 10.3-10.4, teacher wording, misconceptions reused. This is a read-only copy; refresh from the home note if the source changes.

---

# NML2 Final Draft: Keeping the Right Mass Address

**Status:** complete integrated lesson draft, v1  
**Project:** VD Newton / VD Pedagogy  
**Date:** 2026-07-10  
**Lesson length:** 80 minutes  
**Core unit:** tolerance-indexed target continuity, mass-address reuse, and the Newton II law-house  
**Audience range:** adaptable from young learners to introductory undergraduate mechanics  

---

## 0. One-Sentence Thesis

**NML2 teaches that a known inertial-mass value may be reused only through a mass address whose track-family remains one continuing redundant bundle at the tolerance appropriate to the modelling task; once that licence is in place, Newton II connects the target's mass and inertial acceleration to one net-force vector measured in newtons.**

The central route is:

```text
track-family at a declared tolerance
  -> redundant tracks earn one target address
  -> a known mass value is bound to that address
  -> the address is carried only through an acceptable tolerance history
  -> Newton II relates that target's mass, acceleration, and net force
  -> acceleration can be used to continue the target's predicted path
```

The student-facing habit is:

```text
Before using m, ask which target address it belongs to.
Before reusing that address, check the tracks at the working tolerance.
```

The teacher-facing formulation is:

> Never ask whether it is absolutely the same object. Ask whether the same mass address remains licensed at the tolerance required by this prediction.

---

## 1. Purpose of NML2

NML1 installed the ability to read motion-change from a point-particle trajectory in an inertial frame. Its direction of work was:

```text
trajectory
  -> velocity-change
  -> inertial acceleration
```

NML2 begins from that achievement and asks a new question:

> When Newton II contains a mass value, which continuing target is that value allowed to belong to?

Textbook exercises usually hide this problem. A diagram contains one block, a number such as `2 kg` is printed beside it, and the student substitutes the number into `F = ma`. The diagram has silently supplied a stable target identity and a valid mass address.

Real scenes do not arrive already labelled. One body may produce many visible tracks. A body may deform, rotate, divide, lose material, acquire material, disappear behind another body, or become indistinguishable from a nearby object. The modeller must decide which tracks are being represented by one target and for how long a previously bound mass value may continue to be used for that target.

NML2 makes that hidden decision visible.

Its two linked achievements are:

```text
TARGET DISCIPLINE
Use redundant tracks, interpreted at a declared tolerance, to license and
carry a mass address.

NEWTON-II DISCIPLINE
Use only values belonging to that same licensed target in the relation among
inertial mass, inertial acceleration, and net force.
```

The calculation is not the deepest difficulty. The deepest difficulty is earning the right to use the `m` that appears in the calculation.

---

## 2. Position in the Learning Sequence

### 2.1 Prerequisites

NML2 assumes that students can already:

- follow visible points through successive moments;
- treat a sequence of positions as a track or trajectory;
- compare the shapes, spacings, and velocity changes of tracks;
- read inertial acceleration from a trajectory in an inertial frame;
- understand that measurement and comparison operate at finite resolution.

Trackability may be installed as a kinematic primitive before NML1. If so, NML2 should recap it for only a few minutes rather than reteach it.

### 2.2 NML1 handoff

NML1 ended with:

```text
Read the path before explaining it.
```

NML2 adds:

```text
Audit the target before using its mass.
```

Together, the two lessons install this order:

```text
track the scene
  -> identify the target at a tolerance
  -> read the target's acceleration
  -> use the mass value bound to that target
  -> infer or predict the corresponding Newton-II quantity
```

### 2.3 Future handoff

NML2 deliberately stops when its one-target representation can no longer be licensed at an acceptable tolerance.

Later lessons will explain how to handle:

- several force contributions on one target;
- acting objects and interaction pairs;
- internal-force cancellation;
- targets that divide or combine;
- assigning mass values after a genuine address break;
- momentum and mass additivity;
- rotation, deformation, torque, and extended-body dynamics;
- open or variable-mass systems.

NML2 detects when those branches are demanded. It does not open them prematurely.

---

## 3. The Core Modelling Objects

### 3.1 Track-family

A **track-family** is a selected collection of tracks being considered as possible descriptions of one target.

For example, several marked points on a translating cart produce several tracks. The tracks are not identical: they occupy different positions. But they may contain redundant translational information.

### 3.2 Translational redundancy

Student-facing wording:

> Tracks are translationally redundant when, within the tolerance being used, they move together so that following all of them gives no relevant translational information beyond following one representative track.

For a teacher-facing two-track test, let the track positions be `r_i(t)` and `r_j(t)`. Their relative displacement is:

```text
r_i(t) - r_j(t)
```

They remain translationally redundant over an interval when the change in this relative displacement stays within the accepted tolerance:

```text
| [r_i(t) - r_j(t)] - [r_i(t0) - r_j(t0)] | <= epsilon(t)
```

This test is deliberately narrower than general rigidity. A rotating rigid body can fail translational redundancy because the relative displacement vectors of its points rotate. NML2 is licensing a one-point translational representation, not installing the full theory of rigid bodies.

### 3.3 Tolerance

A **tolerance** states which observed differences the present modelling task will treat as negligible.

If `epsilon` denotes the largest accepted discrepancy, then:

- a smaller `epsilon` is a finer, stricter tolerance;
- a larger `epsilon` is a coarser, looser tolerance.

Every claim of continuity or redundancy is tolerance-relative. There is no absolute, observation-independent judgment that two moments show “the same object.”

The appropriate formal shape is therefore not:

```text
valid(A)
```

but:

```text
valid(A; epsilon(t), interval, modelling-task)
```

A tolerance must remain fine enough to:

- distinguish the selected target from nearby alternatives;
- exclude objects not intended to belong to the target;
- support the accuracy required by the prediction;
- prevent an unrelated later track-family from being identified with the earlier one merely because the tolerance is enormous.

This is the lesson's **tolerance budget**. Tolerance is a modelling tool, not an unrestricted escape from failure.

### 3.4 Target address

When a track-family is accepted as one continuing redundant bundle at the working tolerance, the lesson gives it a target address, for example:

```text
A
```

The address records which track-family the model is treating as one target. It is not a claim that the world contains a tolerance-independent object bearing the label `A`.

### 3.5 Mass address and mass value

The target address supports a mass address:

```text
m[A]
```

The address and its value must be distinguished:

```text
target address:  A
mass address:    m[A]
bound value:     m[A] = 2 kg
```

The tracks do not calculate the number `2 kg`. They establish which target a supplied or previously certified inertial-mass value belongs to.

This lesson assumes that the first mass value has been obtained by an acceptable earlier or external procedure. NML2 concentrates on whether that value may still be reused. It does not use a weighing scale to smuggle in gravitational-inertial equivalence, and it does not use mass additivity to manufacture composite values.

### 3.6 Address validity over time

A mass address is reusable across an interval when there exists an acceptable tolerance, or an explicitly recorded tolerance schedule, under which the relevant track-family remains one continuing redundant bundle through that interval.

The core licence is:

```text
track-family remains one redundant bundle at the working tolerance
  -> continue using the same target address
  -> continue using the mass value bound to that address
```

If the licence fails and no acceptable coarser description bridges the failure, the student must stop using the old mass address.

The correct response is not to guess new mass values.

---

## 4. The Bouncy-Ball Case: Why Tolerance Is Load-Bearing

The bouncy ball is the central conceptual demonstration of NML2.

Several visible marks are placed on a ball. Before it reaches a wall, their tracks move together. During contact, the ball squishes. After the rebound, the marks again move together.

### 4.1 Fine-tolerance description

At a fine tolerance, the deformation is visible:

```text
before contact:  tracks redundant
during contact:  tracks nonredundant
after contact:   tracks redundant again
```

The later return of redundancy does not by itself prove that the later bundle is entitled to the earlier mass address. The fine-resolution licence contains a gap.

This prevents the invalid rule:

```text
redundancy returned
  -> therefore the old address automatically returned
```

Two unrelated targets could later produce equally redundant tracks. Redundancy describes a relation within the current track-family; by itself, it does not bridge an earlier unlicensed interval.

### 4.2 Coarse-tolerance description

At a coarser tolerance, the squishing may fall below the discrepancy relevant to the task:

```text
before contact:  tracks redundant
during contact:  tracks redundant within coarse tolerance
after contact:   tracks redundant
```

At this resolution, the address never lapses. The same mass address can be carried through the bounce without mass additivity and without constructing new mass accounts for temporarily displaced regions of the ball.

### 4.3 Fine-coarse-fine bridge

The modeller may use a recorded tolerance schedule:

```text
fine description before bounce
          ↓ refines
coarse description continuous through bounce
          ↑ refines
fine description after bounce
```

In this case, the pre-bounce and post-bounce fine descriptions may reuse the mass address because both are connected through one uninterrupted coarse target.

The licence comes from the coarse bridge, not merely from the later reappearance of redundancy.

### 4.4 Changing tolerance honestly

It is legitimate to change tolerance, but the change must be visible in the modelling record.

The lesson should distinguish:

```text
The target stayed absolutely the same.
```

from the acceptable claim:

```text
At the tolerance schedule used for this investigation, the track-family
remained one continuing target.
```

For prediction, the tolerance should ideally be chosen in advance from the required accuracy. For retrospective analysis, a tolerance may be revised after inspection, but the revision must be recorded as a change in the model rather than presented as a fact discovered without judgement.

### 4.5 What NML2 does during the fine-scale failure

At fine resolution, NML2 does not attempt to calculate the ball's deformation, internal forces, torque, or constituent accelerations. It says:

```text
The one-point translational account is not licensed at this tolerance during
this interval.
```

If a coarser acceptable bridge exists, the address can still be carried for the coarser question. If no acceptable bridge exists, the old address cannot be reused automatically.

---

## 5. The Newton II Law-House

### 5.1 The three quantities

NML2 installs the relation among:

```text
inertial acceleration
inertial mass
net force
```

These must all belong to the same selected target address and the same modelling interval.

For target `A`:

```text
a[A]
m[A]
F_net[A]
```

The address notation is pedagogical bookkeeping. Its purpose is to prevent a student from combining an acceleration read from one target with a mass value belonging to another.

### 5.2 Inertial acceleration

NML1 has already installed the basic handle:

> Inertial acceleration is the acceleration read from a point-particle trajectory when the trajectory is described in an inertial frame.

NML2 does not redefine that acceleration as something created by force. It places the already-readable acceleration into the Newton II relation for a massive target.

### 5.3 Inertial mass

NML2-facing definition:

> **Inertial mass** is a positive scalar quantity assigned to a selected massive-particle target, measured in kilograms, and related by Newton II to that target's net force and inertial acceleration.

Its unit is:

```text
kilogram, kg
```

Mass has no direction. It is a scalar.

### 5.4 Net force

NML2-facing definition:

> **Net force** is a vector quantity assigned to a selected massive-particle target, measured in newtons, and related by Newton II to that target's inertial mass and inertial acceleration.

Its symbol is:

```text
F_net
```

Its unit is:

```text
newton, N
```

Because net force is a vector, its value includes both magnitude and direction.

This definition is deliberately thin. NML2 does not yet define net force as:

```text
the total of all force contributions
the reading of a newton meter
the force that causes acceleration
```

Those formulations open later branches or introduce misleading intuitions.

A newton meter reads the force transmitted through that meter. It does not automatically read the net force on the target. NML2 therefore uses supplied or inferred net-force vectors rather than calling a meter reading “the net force” without a later force-accounting certificate.

### 5.5 Newton II

For a selected massive-particle target:

```text
F_net = m a
```

In vector notation:

```text
vector F_net = m times vector a
```

The relation may be used in several directions:

```text
F_net = m a       infer the required net-force vector from mass and motion
a = F_net / m     predict acceleration from a supplied net-force vector and mass
m = |F_net| / |a| infer mass magnitude in a suitable nonzero trial
```

The third route requires nonzero acceleration and the Newton-II alignment of the force and acceleration vectors. It is not the central student route in NML2.

### 5.6 Units

Mass is measured in kilograms:

```text
[m] = kg
```

Acceleration is measured in metres per second per second:

```text
[a] = m/s^2
```

Therefore the units of `m a` are:

```text
kg times m/s^2
```

That compound unit is called the newton:

```text
1 N = 1 kg m/s^2
```

This is not an arbitrary conversion to memorize. Newton II tells us that the unit used for net force must match the units of mass times acceleration.

Example:

```text
m[A] = 2 kg
F_net[A] = 6 N to the right
```

Then:

```text
a[A] = F_net[A] / m[A]
     = 3 m/s^2 to the right
```

The direction survives because mass is a positive scalar.

### 5.7 The zero case

For finite nonzero mass:

```text
a = 0  ->  F_net = 0
```

NML2 should not turn this into:

```text
No force contributions exist.
```

Later lessons may show that several contributions can produce a zero net-force vector. At the NML2 level, the safe statement is only:

> The Newton-II net-force value assigned to this target is zero.

The equation `m = F_net / a` cannot determine mass when `a = 0`.

---

## 6. Learning Outcomes

By the end of NML2, a student should be able to:

1. Identify a selected track-family in a scene.
2. State the working tolerance or compare fine and coarse tolerances.
3. Decide whether the tracks are translationally redundant at that tolerance.
4. Assign one target address to an accepted redundant bundle.
5. Distinguish the target address, its mass address, and the numerical mass value bound there.
6. Decide whether the same mass address remains licensed across an interval.
7. Explain why the return of redundancy after an unbridged failure does not automatically restore an old address.
8. Explain how an acceptable coarser tolerance can bridge a temporary fine-scale failure such as a ball squishing during a bounce.
9. State that inertial mass is a scalar measured in kilograms.
10. State that net force is a vector measured in newtons.
11. Use `1 N = 1 kg m/s^2` as the unit relation generated by Newton II.
12. Use `F_net = m a` and `a = F_net / m` with all quantities belonging to the same target address.
13. Continue a predicted path through equal time steps when a valid mass address and supplied net-force vectors are available.
14. Halt rather than guess when the address licence fails.

---

## 7. Hard Lesson Boundaries

NML2 does **not** teach:

- mass additivity;
- centre-of-mass derivations;
- momentum or impulse;
- Newton III;
- force-contribution addition;
- free-body diagrams;
- acting-object enumeration;
- internal-force cancellation;
- normal force, friction, tension, spring force, or weight calculations;
- a newton meter as an automatic net-force meter;
- gravitational mass versus inertial mass;
- how a scale produces an inertial-mass reading;
- how mass is distributed after a split;
- how two targets acquire a new combined mass;
- rotation, torque, or full rigid-body dynamics;
- deformation mechanics;
- variable-mass or open systems.

The lesson may display a deformation or split only to teach the stopping condition and the role of tolerance.

The key boundary sentence is:

> NML2 teaches when an existing mass address may continue to be used. Future lessons teach how to build new mass and force accounts when that licence fails.

---

## 8. Lesson at a Glance

| Time | Segment | Main installation |
|---:|---|---|
| 0-8 min | NML1 handoff | Acceleration is already readable from a trajectory. |
| 8-20 min | Many tracks, one target | Translational redundancy under tolerance earns one address. |
| 20-31 min | The mass ledger | Address, mass address, mass value, and kilogram are separated. |
| 31-45 min | Bouncy-ball investigation | Continuity and redundancy are tolerance-relative; a coarse bridge can preserve an address. |
| 45-59 min | Newton II law-house | Inertial mass, inertial acceleration, net-force vector, and newton units are connected. |
| 59-74 min | Address-to-path worksheet | Audit first, calculate second, halt when unlicensed. |
| 74-80 min | Debrief and handoff | State the installed habit and mark future branches. |

---

## 9. Detailed Lesson Run

### Segment 1 - NML1 handoff: motion-change is already visible (0-8 min)

Show a short sequence of equal-time positions for a moving point.

Ask:

```text
How is the velocity changing?
What acceleration would you draw?
```

Do not begin with force. The purpose is to reactivate the NML1 behaviour:

```text
trajectory -> acceleration
```

Then widen the scene. Reveal that the point was one of several marked points on the same translating cart.

Ask:

```text
If all these points are visible, how many Newton-II targets should we use?
```

Do not accept “one” merely because the picture looks like one familiar object. Make the track evidence do the work.

### Segment 2 - Many tracks, one target (8-20 min)

Plot three marker tracks from the cart. Compare their relative spacings at successive equal-time moments.

Introduce:

```text
working tolerance
track-family
translational redundancy
representative track
target address
```

Student-facing rule:

> If the tracks stay together in the same translational pattern within our tolerance, we may use one of them to represent the bundle's translational motion.

Give the bundle address `A`.

Immediately show that the address is conditional:

```text
A at tolerance epsilon over interval [t0, t1]
```

Avoid saying simply:

```text
This really is one object.
```

Prefer:

```text
At this tolerance, these tracks earn one target for this question.
```

### Segment 3 - The mass ledger (20-31 min)

Write:

```text
target:       A
mass address: m[A]
mass value:   m[A] = 2 kg
```

Ask students to distinguish the three lines.

Key questions:

```text
Did the tracks tell us the number 2?
What did the tracks tell us?
If another cart passes nearby, may we put its mass value into m[A]?
What must remain stable before we reuse m[A] at a later time?
```

Expected understanding:

```text
The numerical value comes from a certified source.
The track analysis tells us which continuing target owns the slot.
```

Introduce the kilogram as the mass unit. Do not explain the value through weight or a balance of gravitational and support forces.

### Segment 4 - The bouncy-ball investigation (31-45 min)

Show the same marked bouncy-ball collision twice:

1. a fine-resolution view in which the squish is visible;
2. a coarse-resolution view in which the ball remains one moving blob.

At the fine tolerance, students should mark:

```text
pass -> fail -> pass
```

Ask:

```text
Does the final pass, by itself, restore the old address?
```

Expected answer:

```text
No. It shows that the present tracks are redundant. It does not bridge the
interval in which the fine-resolution licence failed.
```

At the coarse tolerance, students should mark:

```text
pass -> pass -> pass
```

Now ask:

```text
Is this tolerance still good enough to distinguish the ball from the wall and
to answer our translational question?
```

If yes, the coarse description supplies the bridge.

Draw:

```text
fine before -> coarse through bounce -> fine after
```

State:

> We may reuse the address after returning to fine resolution because the coarse description kept the target licensed through the collision. The later return of fine redundancy was not sufficient by itself.

Optional extension question:

```text
What if the tolerance is made so coarse that the ball and wall count as one
target?
```

Expected answer:

```text
The tolerance has exceeded the budget of the question and can no longer license
the intended address.
```

### Segment 5 - Newton II and its units (45-59 min)

Return to a simple translating target whose address is valid.

Put the three addressed values on the board:

```text
a[A]       inertial acceleration, vector, m/s^2
m[A]       inertial mass, scalar, kg
F_net[A]   net force, vector, N
```

Give the net-force definition in full:

> Net force is a vector quantity assigned to a selected massive-particle target, measured in newtons, and related by Newton II to that target's inertial mass and inertial acceleration.

Then expose:

```text
F_net[A] = m[A] a[A]
```

Work the unit relation:

```text
kg times m/s^2 = N

1 N = 1 kg m/s^2
```

Use two short examples:

```text
Prediction:
m[A] = 2 kg
F_net[A] = 6 N right
a[A] = 3 m/s^2 right

Inference:
m[B] = 3 kg
a[B] = 4 m/s^2 left
F_net[B] = 12 N left
```

Finish with the zero case:

```text
a[A] = 0 -> F_net[A] = 0
```

Add verbally:

```text
This does not yet say that no force contributions exist.
```

### Segment 6 - Address-to-path worksheet (59-74 min)

The worksheet combines the target audit with the reverse of NML1's path-to-arrow activity.

NML1 worked:

```text
path -> acceleration arrows
```

NML2 now works:

```text
valid address + mass + supplied net force
  -> acceleration
  -> velocity change
  -> next path segment
```

The first prompt in every row is:

```text
May I still use this mass address at the stated tolerance?
```

Only after answering yes may the student calculate.

If the answer is no and no acceptable bridge is supplied, the correct worksheet entry is:

```text
HALT: old mass address not licensed.
```

This is a successful answer, not an incomplete calculation.

### Segment 7 - Debrief and future boundary (74-80 min)

Ask four exit questions:

```text
1. What does a mass address identify?
2. What must be recorded before that address is reused later?
3. Why does redundancy returning after a gap not automatically restore an address?
4. What kind of quantity is net force, and what unit measures it?
```

Desired answers:

```text
1. The target licensed from a track-family at a tolerance.
2. An acceptable tolerance history that keeps the target continuously licensed.
3. Present redundancy does not bridge an earlier unlicensed interval; a coarse
   or otherwise certified bridge is required.
4. Net force is a vector assigned to the target and measured in newtons.
```

Close with:

> First preserve the address at an acceptable tolerance. Then use the mass stored there. If the address cannot be preserved, stop: the next lesson begins where this representation fails.

---

## 10. Signature Worksheet Specification

### 10.1 Purpose

The worksheet is not primarily a test of algebra. It is designed to install a repeated modelling behaviour:

```text
audit -> address -> calculate -> continue
```

The student should become slightly uncomfortable whenever a mass number appears without a clearly licensed target address.

### 10.2 Part A - Address ledger

Each scene should include:

- a small set of marked tracks;
- a stated fine or coarse tolerance;
- a time interval;
- a candidate address;
- a known mass binding when appropriate.

Suggested columns:

| Interval | Working tolerance | Redundancy result | Address decision | Mass binding available? | Reason |
|---|---|---|---|---|---|
| `t0-t1` | fine | pass | create `A` | `m[A] = 2 kg` | tracks remain redundant |
| `t1-t2` | fine | pass | reuse `A` | yes | licence continuous |
| `t2-t3` | fine | fail | do not use `A` at fine resolution | retained only if bridged | ball deforms |
| `t2-t3` | coarse | pass | carry `A` | yes | acceptable coarse bridge |
| `t3-t4` | fine | pass | reuse `A` through bridge | yes | both fine bundles refine continuous coarse target |

Include one unbridged case in which a track-family disappears or becomes indistinguishable from another target. The correct response must be:

```text
Old address cannot be restored automatically.
```

### 10.3 Part B - Force-to-path installation sheet

For each equal time step, provide:

| Step | Address valid? | `m` | supplied `F_net` | calculated `a` | velocity change | next velocity | next position |
|---|---|---:|---|---|---|---|---|

Use cases such as:

- same net force with two different already-certified mass values;
- same mass with different net-force magnitudes;
- same mass with net-force vectors in different directions;
- zero net force;
- a supplied position-dependent net-force sequence that gradually curves the path.

Do not ask students to construct the supplied net-force vector from physical contributions.

### 10.4 Required halt row

At least one row must contain an address failure with no acceptable bridge.

The sheet should make the correct response visually explicit:

```text
ADDRESS NOT LICENSED
Do not substitute the old mass.
Future target analysis required.
```

The climax of the worksheet is the student's refusal to perform an unauthorized calculation.

---

## 11. Recommended Teacher Wording

Use:

```text
At this tolerance, these tracks may be treated as one target.

The tracks establish the address; they do not calculate the mass value.

The mass value is measured in kilograms.

Net force is a vector assigned to the selected target and measured in newtons.

One newton is one kilogram metre per second squared.

The fine description failed during the squish, but the acceptable coarse
description remained continuous.

Redundancy has returned, but we still need a bridge to the earlier address.

No acceptable bridge is available, so the old mass address cannot be used.
```

Avoid:

```text
These points really are one object.

It is obviously the same ball.

The mass must still be the same because the ball looks the same again.

Net force is just all the forces added together.

The newton meter measures the net force.

Force causes acceleration.

The pieces' masses must add to the original mass.
```

The avoided statements either erase the tolerance judgment, open later force machinery, or reintroduce mass additivity.

---

## 12. Common Misconceptions and Repairs

### 12.1 “The address is the object”

Repair:

> The address is a modelling record attached to a track-family under a stated tolerance. A different tolerance may support a different target decomposition.

### 12.2 “If redundancy fails once, the address is destroyed forever”

Repair:

> Failure at one tolerance does not prove failure at every acceptable tolerance. A coarser continuous description may bridge the interval.

### 12.3 “If redundancy returns, the old address automatically returns”

Repair:

> The current bundle has earned an address, but its identity with the earlier address requires an acceptable bridge across the gap.

### 12.4 “We can always increase tolerance until the address survives”

Repair:

> The tolerance must still distinguish the intended target and support the required prediction. Beyond the tolerance budget, the model no longer answers the question.

### 12.5 “The track tells us the mass”

Repair:

> The track licenses the address. A dynamical measurement or supplied certificate binds the numerical mass value.

### 12.6 “A newton is another name for a kilogram”

Repair:

```text
kg measures mass.
N measures force.
1 N = 1 kg m/s^2.
```

### 12.7 “Net force is a number without direction”

Repair:

> Net force is a vector. A complete value includes magnitude and direction.

### 12.8 “Zero net force means nothing is acting”

Repair:

> NML2 concludes only that the one Newton-II net-force vector is zero. The later force-accounting lesson determines whether contributions exist and cancel.

---

## 13. Criteria of Instillment

NML2 has succeeded when the student reliably performs the following behaviours without needing a teacher prompt.

### 13.1 Address-first behaviour

When shown `m = 3 kg`, the student asks:

```text
Three kilograms belonging to which target address?
```

### 13.2 Tolerance-explicit behaviour

When asked whether two moments show the same target, the student asks:

```text
At what tolerance and for what modelling question?
```

### 13.3 Bridge behaviour

When redundancy disappears and later returns, the student does not immediately restore the old address. They search for an acceptable continuous description across the interval.

### 13.4 Halt behaviour

When no bridge is available, the student stops using the old mass value rather than inventing a split, sum, or reassignment rule.

### 13.5 Newton-II type discipline

The student checks that:

```text
m[A], a[A], and F_net[A]
```

all refer to the same selected target.

### 13.6 Unit discipline

The student can state:

```text
mass:         kg
acceleration: m/s^2
net force:    N
1 N:          1 kg m/s^2
```

### 13.7 Vector discipline

The student supplies a direction with every nonzero net-force and acceleration value.

### 13.8 Path-building behaviour

Given a valid mass address and a sequence of supplied net-force vectors, the student repeatedly calculates acceleration, updates the velocity arrow, and extends the predicted path without abandoning the address audit.

---

## 14. Teacher-Theory Notes

### 14.1 Why mass additivity is absent

NML2 does not assert:

```text
M = m1 + m2
```

Rigid or redundant motion alone does not derive mass additivity. A derivation requires additional system-composition structure, such as additive momentum or net-force accounts together with the relevant Newtonian laws. Teaching mass additivity here would either add an independent assumption or borrow machinery from later lessons without marking the debt.

NML2 therefore carries already-bound values only while their addresses remain licensed. When a target genuinely divides or combines, the lesson halts.

### 14.2 Why the centre of mass is absent

For pure translation, every fixed point of an exactly translating rigid body shares the same acceleration. The centre of mass is a canonical and powerful later representative, but pure translational redundancy does not uniquely select it.

Introducing the centre of mass here would also invite mass additivity, internal motion, momentum, and system-level force accounting. NML2 uses a representative track only within its translational tolerance.

### 14.3 Why the bouncy ball does not require mass additivity

At an acceptable coarse tolerance, the ball remains one target throughout the bounce. The lesson never decomposes it into separately massed parts. It therefore reuses one existing address rather than reconstructing a total from components.

At fine tolerance, the one-point licence fails during deformation. The coarse description may bridge that failure, but NML2 does not calculate the fine-scale dynamics.

### 14.4 Address validity is model-relative, not arbitrary

The address is relative to:

```text
track selection
tolerance or tolerance schedule
time interval
reference frame
modelling task
required accuracy
```

This does not make the address subjective in the sense of unconstrained preference. Once those inputs are fixed, the track comparison can be audited and challenged.

### 14.5 Prediction versus retrospective repair

For an advance prediction, the tolerance and address certificate must be available before the predicted interval is traversed.

For a retrospective analysis, the modeller may revise the tolerance after observing a deformation. That revision produces a new modelling account and must be recorded as such. It does not retroactively turn a previously unsupported prediction into a licensed one.

### 14.6 Net force remains a deliberately under-specified Winter term

NML2 makes net force usable enough to participate in Newton II:

- it belongs to one selected massive-particle target;
- it is a vector;
- it is measured in newtons;
- it satisfies the Newton-II relation with inertial mass and inertial acceleration.

It does not yet explain where the vector comes from physically. That explanation belongs to the later force-contribution and acting-object entries.

---

## 15. Compressed and Extended Variants

### 15.1 Compressed 50-minute version

```text
0-6 min    NML1 acceleration recap
6-16 min   track redundancy and target address
16-24 min  mass address versus kilogram value
24-34 min  bouncy ball at fine and coarse tolerance
34-44 min  Newton II, net-force vector, and newton units
44-50 min  short audit-and-calculate exit sheet
```

Remove mass inference and the position-dependent force-to-path extension. Retain the bouncy-ball bridge and the required halt row.

### 15.2 Extended two-session version

Session A:

```text
track-families
redundancy
tolerance budgets
mass addresses
bouncy-ball cross-resolution bridge
address-ledger worksheet
```

Session B:

```text
Newton II triplet
kilograms and newtons
zero case
force-to-path installation sheet
planet trajectory -> inferred net-force extension
```

The advanced planet activity may infer:

```text
trajectory -> acceleration -> F_net = m a
```

It must be labelled as a Newton-II-inferred net-force account, not an independent measurement of gravity or a derivation of the gravitational force law.

---

## 16. Final Lesson Summary

NML2 is not fundamentally a lesson about rearranging `F = ma`.

It is a lesson about maintaining the referent of `m` carefully enough that Newton II can be run without smuggling in an object identity.

The complete conceptual route is:

```text
1. Select and track features in a scene.
2. Declare the tolerance required by the modelling task.
3. Test whether the selected tracks form one translationally redundant bundle.
4. Give the licensed bundle a target address.
5. Bind or retrieve the known inertial-mass value at that address.
6. Carry the address only through an acceptable tolerance history.
7. Use the same address for inertial mass, inertial acceleration, and net force.
8. Apply Newton II.
9. If the licence fails, halt rather than guess.
10. Let later lessons construct the new system, mass, and force accounts.
```

The final student habit is:

> **Audit the target at the tolerance of the question. Preserve the mass address before using its value. Then—and only then—run Newton II.**

