# NML2 Working Note 2: Withholding the Net-Force Wall

**Status:** working design note  
**Project:** VD Newton / Newtonian Mechanics Lesson 2  
**Date:** 2026-06-22  
**Core issue:** whether NML2 should teach the Newton-II `net-force` wall at all, or leave `net-force` as a mystery slot exposed by the triplet.

---

## 0. One-sentence update

**NML2 should probably not teach `net-force` as a directly understood or directly measured object. It should teach that, for a massive target, the motion-readout and the mass-readout demand a hidden `net-force` value; the later force-sum lesson explains where that value comes from.**

Short form:

```text
NML1: read motion-change from the path.
NML2: add mass, and infer that a net-force value is demanded.
NML3: explain how force-contributions produce that net-force value.
```

---

## 1. The design correction

The earlier NML2 plan quietly treated a newton meter as if it could supply `net-force`.

That is not honest.

A newton meter reads a force transmitted through the meter. It does not automatically read the net-force on the target. A newton meter reading is equal to `net-force` only after a modelling certificate has been supplied:

```text
The meter force is the only relevant force contribution on the chosen target
in the direction being analysed.
```

But that certificate is already force-sum logic. It asks what other force-contributions exist, whether they are relevant, whether they cancel, and whether the measured pull is the whole force-accounting value. That belongs to the later force-sum block, not to NML2.

So the correction is:

```text
Do not say:
  The newton meter measures net-force.

Say:
  The newton meter measures one force-contribution.
  Whether that contribution is the net-force is a later question.
```

This makes `net-force` stranger, but more honest.

---

## 2. What happens to E12?

In the current entry structure, E12 is listed as the Newton-II wall for `net-force`:

```text
E12: Newton II wall; net-force
```

But the proposed lesson choice is to **withhold** that wall from NML2.

There are three possible interpretations of this choice.

### Option A — Pedagogical withholding only

The dictionary may still eventually contain a `net-force` wall, but NML2 does not teach it.

In the lesson, `net-force` remains a hidden value demanded by the Newton-II relation.

This is the safest option.

### Option B — Replace E12 with a negative / boundary wall

Instead of giving `net-force` a comfortable outward definition, E12 could explicitly warn:

```text
net-force is the force-accounting value required by the Newton-II relation
for a massive target. This entry does not tell the modeller how to identify,
measure, or assemble that value from force-contributions.
```

This would make E12 a boundary entry rather than a normal residual wall.

It would say:

```text
You have exposed the net-force slot.
You have not yet learned how to fill it from physical force-contributions.
```

### Option C — Remove E12 as an independent wall

This is the stronger design experiment.

Maybe there is no independent residual wall for `net-force` at this stage. Maybe the only honest outward life of `net-force` comes later, when force-sum defines it through force-contributions.

In that case, the would-be wall is not really an NML2 teaching object. It is a pointer forward:

```text
net-force becomes outwardly usable only when the force-sum block is opened.
```

This challenges the ordinary six-entry law-house expectation, so it should be treated as speculative until the full entry structure is checked.

---

## 3. Why the normal wall fails pedagogically

A tempting wall would be something like:

```text
net-force := the total force on the object
```

or:

```text
net-force := the force that causes the acceleration
```

Both are dangerous.

### 3.1 “Total force” secretly imports force-sum

To understand “total force,” the student must already know that there can be multiple force-contributions and that they can be combined.

That opens:

```text
force-contributions
interacting-forces-set
attached-force
force diagrams
cancellation
balanced forces
normal force
friction
tension
```

Those are not NML2. They are the next lesson layer.

### 3.2 “The force that causes acceleration” blurs the triplet

If the wall says net-force is “the force that causes acceleration,” the student may think `net-force` is directly obvious from the motion, or that it is a cause-word with ordinary intuitive content.

But in NML2, `net-force` should not be an ordinary intuitive object. It should be the unknown force-accounting value demanded by the relation among:

```text
massive-particle inertial-acceleration
net-force
inertial-mass
```

The point is not that the student already knows what `net-force` is.

The point is that Newton II forces the student to recognise that such a value must be assigned if the massive target’s motion-change is to be accounted for.

---

## 4. What NML2 becomes after withholding the net-force wall

NML2 becomes a lesson about **investigating the net-force slot**, not directly measuring net-force.

The lesson route becomes:

```text
1. NML1 gave us path-reading.
2. A massive target also has a mass-side value.
3. For a massive target, mass and motion-change are locked to a hidden net-force value.
4. We can infer or investigate that value using the Newton-II relation.
5. We do not yet explain how physical force-contributions produce that value.
```

Student-facing version:

```text
First, watch how the path changes.
Then, check how massive the thing is.
Newton II says those two readings point to a hidden force-number.
Later, we learn where that force-number comes from.
```

Teacher-facing version:

```text
NML2 installs the Newton-II relation while deliberately leaving net-force
outwardly under-specified. `Net-force` is exposed as a required accounting slot,
not as a directly measured residual object.
```

---

## 5. What remains active in the lesson

### 5.1 E7 remains the prerequisite

NML2 still begins from E7:

```text
trajectory in inertial-frame
  -> acceleration / motion-change readout
```

The student already learned:

```text
motion-change is visible before it is explained
```

NML2 should preserve that ordering.

### 5.2 E8 opens the massive-particle sheet

E8 says, in lesson terms:

```text
The same target whose motion was read can now be treated as massive.
```

This means the target receives a mass-side slot.

Young-learner version:

```text
Now we are not only watching the path.
We are also asking how much massive thing is being moved.
```

### 5.3 E9–E11 provide the triplet lock

The Newton-II triplet still exists:

```text
massive-particle inertial-acceleration
net-force
inertial-mass
```

Mathematical surface:

$$
F_{\text{net}} = ma
$$

But pedagogically, only two of the three corners are outwardly stable in NML2:

```text
path-change / acceleration: read from E7 motion sheet
inertial-mass: supplied by mass reading / scale reading / known mass
net-force: hidden accounting value demanded by the relation
```

### 5.4 E13 remains teachable

`inertial-mass` can still receive an NML2 wall-like handle.

Core handle:

```text
Mass is how much the same action changes motion less.
```

More precise teacher version:

```text
Inertial mass is the mass-side value by which a massive target resists motion-change in the Newton-II relation.
```

This is why sideways examples matter. Students need to see that heavy things are hard to move not only because Earth pulls them down, but because massive things resist acceleration.

---

## 6. What is no longer active in NML2

NML2 should not actively teach:

```text
newton meter reading = net-force
net-force = total force
force diagrams
balanced forces
normal force
friction
tension
springs as force producers
how to decide whether all forces have been included
```

Those are later force-sum and acting-object lessons.

A newton meter may still appear as a physical object, but only with the caveat:

```text
A newton meter reads one force-contribution.
NML2 is not yet teaching when that reading equals net-force.
```

In most NML2 versions, it is cleaner to avoid newton meters entirely.

---

## 7. The new student target behaviour

The student should not merely plug numbers into:

$$
F = ma
$$

The student should learn the target discipline:

```text
Which thing are we tracking?
How does its path change?
What is its mass-side value?
What hidden net-force value would account for that?
```

Desired young-learner behaviours:

```text
Heavier things change motion less under the same kind of action.
This is true even sideways, not only when lifting.
If a huge thing is involved, it may move too little to notice.
If the motion-change is zero, the net-force value is zero.
```

Desired older-learner behaviours:

```text
Use the acceleration read from the trajectory.
Use the inertial mass of the same target.
Infer F_net = ma as the demanded force-accounting value.
Do not identify F_net with a meter reading unless force-sum conditions have been supplied.
```

---

## 8. Zero acceleration remains critical

Question:

```text
If a massive particle has zero acceleration, what does that mean?
```

Answer:

$$
a = 0 \quad \Rightarrow \quad F_{\text{net}} = 0
$$

So:

```text
Zero acceleration means zero net-force.
```

But NML2 must not overclaim:

```text
Zero acceleration means no forces exist.
```

That would be wrong or at least premature.

The correct NML2 wording is:

```text
The net-force value is zero.
We have not yet learned whether that means no force-contributions, or several
force-contributions cancelling.
```

This is now a feature, not a bug. It creates the need for NML3.

---

## 9. The role of scales after the change

Scales remain allowed, but only as black-box mass suppliers.

Do not teach:

```text
A scale works because gravity pulls down and the scale pushes up.
```

That opens weight, normal force, equilibrium, and force addition.

NML2-safe scale wording:

```text
The scale gives the mass-side value for the target.
We are not yet explaining how the scale works.
```

This is especially important because the lesson wants to distinguish:

```text
hard to lift because Earth pulls down
```

from:

```text
hard to accelerate because of inertial mass
```

The second idea is the NML2 idea.

---

## 10. Heavy things are hard to move even without gravity as the explanation

This should become one of the central NML2 intuitions.

Student-facing contrast:

```text
A heavy object is hard to lift partly because Earth pulls it down.
But a heavy object is also hard to move sideways.
That sideways difficulty is not explained by “Earth pulls it down.”
It is the mass-side resistance to motion-change.
```

This is probably the cleanest reason to include horizontal or sideways examples.

Examples:

```text
A light ball and a heavy ball receive the same sideways tap.
A light cart and a heavier cart receive the same kind of push.
A small object and a massive object are involved in the same interaction; the massive one barely changes motion.
```

NML2 should install:

```text
same action-scale + bigger mass -> smaller motion-change
```

without yet needing to name or measure the action as net-force.

---

## 11. Very massive bodies may move too little to notice

NML2 can prepare later Newton III and centre-of-mass ideas with a simple mass-side observation:

```text
If a very massive thing is involved, its motion-change may be too small to spot.
```

Examples:

```text
A child pushes against Earth through the floor; Earth’s motion-change is too tiny to notice.
A planet and the Sun are mutually involved; the Sun moves too, but much less.
A ball hits a wall; the wall/Earth system may move too little for us to see.
```

Do not yet say:

```text
Every force has an equal and opposite force.
```

That opens Newton III.

NML2-safe version:

```text
The same mass-idea explains why huge things may have tiny motion-change.
```

---

## 12. The three algebraic question forms after the change

The familiar three forms remain, but their interpretation changes.

### 12.1 Find the hidden net-force value

Given:

```text
mass-side value
path-change / acceleration readout
```

Ask:

```text
What net-force value is demanded by this motion?
```

Equation:

$$
F_{\text{net}} = ma
$$

This is now the most NML2-native exam form.

### 12.2 Predict the path-change from a supplied net-force value

Given:

```text
mass-side value
supplied or hypothesised net-force value
```

Ask:

```text
What acceleration should be read from the path?
```

Equation:

$$
a = \frac{F_{\text{net}}}{m}
$$

But pedagogically, the net-force value is not read from a newton meter in this lesson. It is supplied as a formal value or left as a mystery to be explained later.

### 12.3 Infer the mass-side value

Given:

```text
path-change / acceleration readout
supplied or inferred net-force value
```

Ask:

```text
What inertial-mass value would make these fit?
```

Equation:

$$
m = \frac{F_{\text{net}}}{a}
$$

Boundary warning:

```text
This fails when a = 0.
```

If acceleration is zero, then the net-force value is zero for finite nonzero mass; this equation cannot be used to find mass by division.

---

## 13. What the lesson looks like now

### Segment 1 — Recall NML1

```text
Watch the path.
Read motion-change before naming a cause.
```

Use one or two E7 examples:

```text
straight steady path -> zero motion-change
speeding up / slowing down -> motion-change
turning path -> motion-change
```

### Segment 2 — Add mass

Introduce the mass-side reading:

```text
Some targets are more massive than others.
The scale/known mass gives the mass-side value.
```

Do not explain the scale through gravity.

### Segment 3 — Sideways mass intuition

Show or discuss:

```text
light object vs heavy object
same sideways action
heavy object changes motion less
```

Point:

```text
Heavy things are not only hard to lift.
They are hard to change sideways too.
```

### Segment 4 — The hidden net-force slot

Introduce:

```text
For a massive target, the motion-change and mass-side value demand a net-force value.
```

Equation appears as compression:

$$
F_{\text{net}} = ma
$$

Teacher wording:

```text
This tells us the net-force value required by the motion.
It does not yet tell us what physical force-contributions produced that value.
```

### Segment 5 — Zero acceleration

Ask:

```text
If the motion-change is zero, what is the net-force value?
```

Answer:

```text
zero
```

Then explicitly block the overclaim:

```text
Zero net-force does not yet mean no force-contributions.
That is for the next lesson.
```

### Segment 6 — Very massive things move little

Use Earth/Sun/wall examples:

```text
Huge mass -> tiny motion-change.
```

Do not open Newton III yet.

### Segment 7 — Bridge to NML3

End with the mystery:

```text
We can infer the net-force value from mass and motion.
Next we ask: where does that value come from?
```

That opens force-sum.

---

## 14. The lesson’s new thesis

Old thesis:

```text
NML2 relates path-reading, scale-reading, and newton-meter-reading.
```

New thesis:

```text
NML2 relates path-reading and mass-reading to a hidden net-force value.
```

Better version:

```text
NML2 is the lesson where massive motion-change exposes the net-force slot,
without yet explaining how that slot is physically filled.
```

Student version:

```text
If you know how massive the thing is, and you watch how its motion changes,
Newton II tells you the force-number that would account for that change.
Next time, we learn where that force-number comes from.
```

---

# Separate Record: Experiment / Demonstration Ideas Discussed

These are deliberately kept separate from the core lesson logic. None should be allowed to quietly reintroduce a `net-force` wall.

---

## A. Planet path plotting — advanced inferred-net-force investigation

Idea:

```text
Measure or model the acceleration of planets from their paths.
Use planet masses.
Infer F_net = ma.
Plot the inferred values.
See that a pattern appears.
```

Why it fits the new design:

```text
The net-force values are inferred from mass and motion.
They are not read from a meter.
```

Caution:

```text
Do not present this as independent measurement of net-force.
It is Newton-II assignment of a net-force value from observed motion and mass.
```

Possible role:

```text
Advanced extension / astronomy bridge.
```

---

## B. Constant impulse device — useful but opens momentum

Idea:

```text
A device gives repeatable same kicks / impulses to different-mass targets.
Heavier target receives less velocity-change.
```

Pedagogical value:

```text
Excellent for showing inertial mass as resistance to motion-change.
```

Caution:

```text
Formally closer to J = mΔv than F = ma.
May open momentum/impulse earlier than desired.
```

Possible role:

```text
Intuition object, not the formal core.
```

---

## C. Hanging balls hit sideways — young-learner mass intuition

Idea:

```text
Suspend balls of different mass.
Hit or tap them sideways.
The heavier ball changes motion less.
```

Why it matters:

```text
Shows heaviness as sideways resistance to motion-change, not just difficulty lifting against gravity.
```

Caution:

```text
A child's hit is not a controlled force history.
A spring-loaded striker would be cleaner.
The swing after impact involves gravity/tension, so focus on the initial sideways change.
```

Possible role:

```text
Pre-formal intuition demo.
```

---

## D. Joined / slack-string carts and centre-of-mass tracking — advanced apparatus idea

Idea:

```text
Use two carts as a multi-part target.
Track the centre of mass of the complete system.
Internal string jerks, stretching, and cart wiggles do not determine the centre-of-mass acceleration.
```

Core physics:

For the complete system:

$$
F_{\text{ext}} = M a_{\text{CM}}
$$

Internal interactions may be messy:

```text
slack string
tautening jerk
string stretch
tension waves
carts wiggling relative to each other
```

But if the target is the whole system, those are internal.

Pedagogical value:

```text
This may let an advanced student see why centre of mass can be treated as the motion of the whole object.
It also shows that real objects can wiggle internally while the whole-object motion remains clean.
```

Caution:

```text
Centre of mass is probably not core NML2 for young students.
This is an advanced branch or teacher-side apparatus logic.
```

Additional unresolved apparatus note:

```text
Pulling the heavier cart may make the individual motions look smoother, but the centre-of-mass equation does not require the pulled cart to be the heavier one if the whole system is tracked correctly.
```

---

## E. Newton meters / force sensors — reclassified

Earlier idea:

```text
Use a newton meter to measure the applied force and call it net-force.
```

Correction:

```text
A newton meter reads one force-contribution, not automatically net-force.
```

Possible later role:

```text
NML3 or force-sum lesson, where students learn when and why a measured contribution can or cannot equal the net-force value.
```

If used in NML2 at all, the caveat must be explicit:

```text
This meter is not being used as a net-force meter in this lesson.
```

---

## F. Constant-force cart puller — formerly central, now conditional

Earlier idea:

```text
Use a black-box constant horizontal force generator to pull carts of different mass.
```

Still useful, but the new design changes its status.

It can demonstrate:

```text
same external action programme + bigger mass -> less motion-change
```

But if the device reading is used as `net-force`, then the lesson has smuggled in a force-sum certificate.

Possible role:

```text
Later controlled-force lab, after the net-force wall / force-sum bridge has been taught.
```

Or:

```text
NML2 demo only if described as a repeatable action source, not as direct net-force measurement.
```

---

# 15. Open design questions

## 15.1 Is E12 removed from the dictionary or only from the lesson?

Current best answer:

```text
Only remove/withhold it from the NML2 lesson for now.
```

Dictionary deletion is a deeper structural move and should be checked against the six-entry law-house requirements.

## 15.2 Can `net-force` have a negative wall?

Possible E12 candidate:

```text
net-force := the Newton-II force-accounting value required for a massive-particle's
inertial-acceleration; this entry does not specify how that value is produced
from force-contributions.
```

This may be better than a normal wall because it prevents the false intuition that `net-force` is directly measured.

## 15.3 Does this make NML2 too mysterious?

Maybe, but the mystery is productive.

NML2 should make the student feel:

```text
I can read the motion.
I can know the mass.
Newton II tells me a net-force value belongs here.
But I do not yet know how the world supplies that value.
```

That is exactly the bridge to force-sum.

## 15.4 Does inertial-mass need its own strong wall?

Probably yes.

If `net-force` is withheld, `inertial-mass` must carry more of the lesson’s intuitive load:

```text
mass as resistance to motion-change
heavy things hard to move sideways
very massive things move little
```

This may be the actual pedagogical heart of NML2.

---

## 16. Current working conclusion

NML2 should probably be redesigned around this claim:

```text
Net-force is not yet a residual object for the student.
It is a hidden accounting value exposed by the Newton-II triplet.
```

Therefore:

```text
Do not teach net-force by newton meter.
Do not teach net-force by total force.
Do not teach force addition.
Do not let zero acceleration become “no forces.”
```

Instead:

```text
Teach motion-change reading from NML1.
Teach mass as resistance to motion-change.
Use mass and motion to infer the demanded net-force value.
Leave the production of that value as the explicit mystery for NML3.
```

Final compact version:

```text
NML2: mass and path reveal the net-force slot.
NML3: force-sum explains how the slot is filled.
```
