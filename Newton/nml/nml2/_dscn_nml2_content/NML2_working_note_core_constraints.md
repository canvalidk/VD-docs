# NML2 Working Note: E8–E13, One Force, One Mass, One Motion-Change

**Status:** working design note  
**Project:** VD Newton / Newtonian Mechanics Lesson 2  
**Core entry range:** E8–E13, with E7 as prerequisite and E14+ deferred

---

## 1. Purpose of NML2

NML2 should begin where NML1 ended.

NML1 installed the ability to read motion-change from a path or trajectory. In VD terms, that is the E7 motion-sheet getter:

```text
path / trajectory in inertial-frame
  -> read acceleration / motion-change
```

NML2 opens the Newton-II-side sheet for a massive target:

```text
motion-change already read
  -> target is treated as massive
  -> relate path-reading, scale-reading, and newton-meter-reading
```

The lesson should not present `F = ma` as a formula that creates acceleration from nowhere. It should present the Newton-II relation as a bridge between three already distinguishable readings:

```text
path-reading         -> how the motion changes
scale-reading        -> how much massive target is being moved
newton-meter-reading -> how strong the one applied pull/push is
```

Young-learner sentence:

```text
The path changes more when the pull number is bigger, and less when the scale number is bigger.
```

Teacher-facing sentence:

```text
NML2 installs the relation among massive-particle inertial-acceleration, net-force, and inertial-mass, without yet teaching force addition.
```

---

## 2. Settled VD scope

The current Design 2.1 structure gives the scope clearly:

```text
E7  inertial-acceleration_point-particle
    acceleration read from trajectory in an inertial-frame;
    stands in no relation to net-force.

E8  Newton II chimney;
    massive-particle inertial-acceleration.

E9  Newton II triplet;
    for a massive-particle, acceleration is net-force divided by inertial-mass.

E10 net-force winter entry.

E11 inertial-mass winter entry.

E12 net-force wall.

E13 inertial-mass wall.
```

So the central NML2 unit is:

```text
massive-particle inertial-acceleration
net-force
inertial-mass
```

or, in the familiar algebraic surface form:

$$
F_{\text{net}} = ma
$$

But the lesson should first make the three physical readings vivid before relying on the algebraic names.

---

## 3. The major constraint: no adding forces yet

NML2 may engage with force, but it may not yet teach **force addition**.

That means NML2 must avoid examples where the student has to assemble:

$$
F_{\text{net}} = F_1 + F_2 + F_3 + \cdots
$$

So the following are not good core NML2 examples:

```text
weight + normal
push + friction
gravity + tension
slope component + normal
spring + friction
balanced force diagrams
```

Those examples open E14 onward: force-sum, interacting-forces-set, attached-force, and eventually acting-objects.

NML2 should instead use situations that can be treated as:

```text
one massive target
one relevant force-accounting value
one motion-change read from the path
```

In other words:

$$
F_{\text{net}} = F_{\text{one applied value}}
$$

This is not a claim that the world contains no other interactions. It is a lesson-boundary decision: NML2 opens the Newton-II relation before opening the machinery that explains where the net-force value came from.

---

## 4. Scales and newton meters are allowed, but as black boxes

Scales and newton meters are still on the table.

The restriction is not:

```text
Do not use measuring devices.
```

The restriction is:

```text
Do not explain the measuring device by adding forces yet.
```

### 4.1 Scale

A scale can be used as a black-box **mass-reading device**:

```text
This tells us the scale number for the target.
```

But NML2 should not motivate scales through gravity, because that immediately opens:

```text
Earth pulls object down.
Scale/table pushes object up.
The object is stationary.
The forces balance.
Weight = mg.
Normal reaction.
```

That is force addition and equilibrium. It belongs later.

So in NML2, the scale is allowed only in this role:

```text
The scale gives the mass-side reading for the target.
```

Not yet:

```text
The scale works because weight and normal force balance.
```

### 4.2 Newton meter

A newton meter can be used as a black-box **force-reading device**:

```text
This tells us the pull-number applied to the target.
```

The lesson does not yet ask:

```text
What internal spring force makes the newton meter work?
What reaction force acts on the hand?
What other forces act on the cart?
```

Those are later branches.

The NML2-safe device sentence is:

```text
The newton meter supplies the one force-accounting reading for this trial.
```

---

## 5. The three readings students must connect

The student should be trained to relate three observable surfaces before being prompted with the technical words.

| Lesson surface | Later formal word | What the student sees |
|---|---|---|
| Path / motion track | acceleration | How quickly the motion changes over the same time interval. |
| Scale reading | inertial mass | The mass-side number for the target. |
| Newton meter reading | net force | The one applied force-accounting number. |

Desired unprompted behaviour:

```text
Student sees path-change, scale number, and pull-meter number
  -> spontaneously relates them
  -> without needing to be first told: mass, acceleration, force
```

Example child-facing prompts:

```text
Same pull number. Same time. Bigger scale number.
What happens to the path-change?
```

Expected answer:

```text
The path changes less.
```

Another:

```text
Same scale number. Same time. Bigger pull number.
What happens to the path-change?
```

Expected answer:

```text
The path changes more.
```

Another:

```text
Same pull number. Same time. Half as much path-change.
What probably changed on the scale?
```

Expected answer:

```text
The scale number was bigger, probably doubled in the ideal case.
```

---

## 6. The three exam-question forms of `F = ma`

There are three standard rearrangements, and NML2 should connect each to one physical question.

### 6.1 Find the newton-meter reading

Given:

```text
scale reading
path-change reading
```

Ask:

```text
What newton-meter reading would account for this?
```

Formula:

$$
F_{\text{net}} = ma
$$

Physical form:

```text
For the same path-change, a bigger scale number requires a bigger pull number.
```

---

### 6.2 Find the path-change reading

Given:

```text
newton-meter reading
scale reading
```

Ask:

```text
What path-change should appear over the same time interval?
```

Formula:

$$
a = \frac{F_{\text{net}}}{m}
$$

Physical form:

```text
For the same pull number, a bigger scale number gives less path-change.
```

---

### 6.3 Find the scale reading

Given:

```text
newton-meter reading
path-change reading
```

Ask:

```text
What scale reading would make those two readings fit?
```

Formula:

$$
m = \frac{F_{\text{net}}}{a}
$$

Physical form:

```text
If the same pull gives less path-change, the target has a bigger mass-side reading.
```

Important boundary:

$$
m = \frac{F_{\text{net}}}{a}
$$

only works as a mass-finding route when the path-change reading is not zero.

If

$$
a = 0
$$

then the mass cannot be found by dividing by zero. This leads into the critical zero-acceleration question.

---

## 7. Critical question: what if the massive particle has zero acceleration?

NML2 must include this question explicitly:

```text
If a massive particle has zero acceleration, what does that mean?
```

Answer:

```text
The net force on the particle is zero.
```

In formula form:

$$
F_{\text{net}} = ma
$$

If

$$
a = 0
$$

and the particle has a finite nonzero mass, then

$$
F_{\text{net}} = 0
$$

But the lesson must avoid a common overclaim.

Correct:

```text
Zero acceleration means zero net force.
```

Not yet licensed:

```text
Zero acceleration means no forces exist.
```

The difference matters because later force-sum will show that multiple force-contributions can combine to a zero net-force value. But NML2 is not yet teaching that mechanism.

So the NML2-safe wording is:

```text
If the motion-change reading is zero, the one net-force accounting value is zero.
```

This also protects the Newton I/NML1 distinction:

```text
zero acceleration / uniform motion does not automatically mean free-particle
```

A stationary object or steadily moving object can have zero net force without being free in the NML1 sense.

---

## 8. Equal time interval is essential

To show mass as resistance to motion-change, the force must be applied for the same time interval.

The observable relation is:

$$
a = \frac{\Delta v}{\Delta t}
$$

So if the same force acts for the same time:

$$
\Delta v = \frac{F \Delta t}{m}
$$

Then doubling the mass gives half the velocity-change:

$$
m \to 2m
$$

$$
\Delta v \to \frac{1}{2}\Delta v
$$

Young-learner sentence:

```text
Same pull. Same time. Heavier target gains less speed.
```

This is probably the cleanest physical route into inertial mass.

---

## 9. Earth is very massive and so moves very little

NML2 may need a small bridge sentence about Earth.

Students may wonder why, when an object is pulled or pushed, the source of the pull does not visibly move. We should not open Newton III fully yet, but we can use the mass idea already being installed.

NML2-safe version:

```text
Very massive things show very small motion-change under the same size of interaction. Earth is so massive that its motion-change is usually too small to notice.
```

This can help students understand why everyday mechanics often watches the smaller target and treats Earth or the room as effectively unmoving.

Forbidden expansion for NML2:

```text
Every force has an equal and opposite force.
Now compute Earth's acceleration from the reaction force.
```

That belongs to Newton III.

Allowed bridge:

```text
The same mass-idea explains why enormous things barely change path.
```

This line prepares the later third-law lesson without opening it.

---

## 10. Likely physical lesson object

The cleanest NML2 experiment would be:

```text
low-friction cart
mass measured by scale
horizontal pull measured by newton meter
pull applied for fixed time interval
path / velocity-change recorded
```

Ideal comparison:

```text
Trial A:
  scale number = m
  pull number = F
  time = Δt

Trial B:
  scale number = 2m
  pull number = F
  time = Δt
```

Prediction:

$$
\Delta v_B = \frac{1}{2}\Delta v_A
$$

The teacher does not need to explain all background forces. The active horizontal model is:

```text
one target
one pull reading
one path-change
```

---

## 11. Speculative / unresolved design decisions

### 11.1 Apparatus choice

The ideal apparatus is a black-box constant-force puller.

Possible implementations:

```text
feedback-controlled cart puller
constant-force spring / negator spring
newton meter with teacher-controlled pull
low-friction cart and force sensor
simulation paired with physical demo
```

Fan carts are probably not ideal for the core proof object, because fan thrust can depend on the cart's speed through the air. They may still be useful qualitatively.

Hanging balls hit sideways are useful for inertial-mass intuition, but they are closer to impulse than force-over-time unless the hit is tightly controlled.

### 11.2 How much algebra?

The lesson should probably begin with reading surfaces:

```text
path reading
scale reading
newton-meter reading
```

Then it can introduce the technical names:

```text
acceleration
mass
force
```

Then the formula:

$$
F_{\text{net}} = ma
$$

The formula should arrive as a compression of an already-installed relationship, not as the first object.

### 11.3 Whether to include centre of mass

Centre of mass should probably not be active in the NML2 core.

Possible light note:

```text
For an extended object, introductory physics often picks one point to track as the object's motion point.
```

But full centre-of-mass dynamics opens extended bodies, systems, internal forces, and later momentum reasoning. That is probably too much for E8–E13.

### 11.4 Whether to include density

Density should not be active in the NML2 core.

Possible light note:

```text
Sometimes a scale number can be found from material amount or density, but this lesson treats the scale reading as already supplied.
```

### 11.5 Whether to mention Newton's original momentum formulation

Newton's original Second Law is closer to change of quantity of motion than the modern fixed-mass `F = ma` form. This is important for the theory note, but probably not for the main child-facing NML2 lesson.

Possible teacher note:

```text
NML2 teaches the modern fixed-mass massive-particle route. Momentum and variable-mass/open-system cases are outside this lesson.
```

---

## 12. Boundary to NML3

NML2 answers:

```text
Given one net-force value and one mass value, what acceleration should be read?
```

NML3 should ask:

```text
Where did the net-force value come from?
```

That opens:

```text
force-sum
interacting-forces-set
attached-force
force diagrams
balanced force-contributions
normal force
friction
tension
springs
acting-objects
```

So the NML2/NML3 split is:

```text
NML2:
  one mass, one net-force value, one acceleration

NML3:
  many force-contributions, one net-force value
```

---

## 13. Working thesis

NML2 is not a general lesson on forces.

It is the installation of the Newton-II relation as a three-way bridge among:

```text
path-change reading
scale reading
newton-meter reading
```

The target installed behaviour is:

```text
Same pull, same time, bigger scale number -> less path-change.
Same scale number, same time, bigger pull -> more path-change.
Zero path-change -> zero net-force reading.
```

Only after that bridge is stable should later lessons ask how several forces combine to produce the one net-force value.
