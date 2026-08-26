# From F = ma and Rigidity to the Centre-of-Mass Representative

## Purpose

This note presents the argument that a rigid composite body can be represented, for translational motion, by its centre of mass.

The route begins from Newton's second law for the parts and adds the rigidity condition.

The aim is not to assume immediately that a composite body "just has" one mass at one point. The aim is to show how that point-particle representative is earned.

---

## 1. Setup: Two Parts Forming One Rigid Body

Let a body B be made of two rigidly connected parts:

```text
mass of part 1 = m1
mass of part 2 = m2
```

Let their positions be:

```text
position of part 1 = r1(t)
position of part 2 = r2(t)
```

The total mass is:

```text
M = m1 + m2
```

Suppose a total external force K is applied to the rigid composite.

We want to know why the body's translational motion can be represented by a single point: its centre of mass.

---

## 2. Replace One Body-Force by a Distributed Force Account

Instead of saying only:

```text
K acts on body B
```

we distribute the force over the two parts:

```text
K1 acts on part 1
K2 acts on part 2
```

with:

```text
K1 + K2 = K
```

For pure translation of a rigid body, the natural mass-proportional distribution is:

```text
K1 = (m1 / M) K
K2 = (m2 / M) K
```

This says: the heavier part receives a larger share of the equivalent translational force-account.

---

## 3. Apply F = ma to Each Part

By Newton's second law:

```text
K1 = m1 a1
K2 = m2 a2
```

Substitute the mass-proportional force shares.

For part 1:

```text
m1 a1 = (m1 / M) K
```

Divide both sides by m1:

```text
a1 = K / M
```

For part 2:

```text
m2 a2 = (m2 / M) K
```

Divide both sides by m2:

```text
a2 = K / M
```

Therefore:

```text
a1 = a2
```

The two parts receive the same acceleration.

---

## 4. Rigidity Supplies the Shared-Motion Constraint

A rigid body is not merely a selected collection of parts. Its parts travel together.

For pure translation, rigidity means:

```text
a1 = a2 = A
```

where A is the shared bulk acceleration of the body.

The distributed force-account above is compatible with this rigidity condition, because each part receives the same acceleration:

```text
A = K / M
```

So the rigid body has one bulk translational acceleration.

---

## 5. Define the Centre of Mass

The centre of mass of the two-part body is:

```text
R_CM = (m1 r1 + m2 r2) / (m1 + m2)
```

Since:

```text
M = m1 + m2
```

we can write:

```text
R_CM = (m1 r1 + m2 r2) / M
```

Differentiate once with respect to time:

```text
v_CM = (m1 v1 + m2 v2) / M
```

Differentiate again with respect to time:

```text
a_CM = (m1 a1 + m2 a2) / M
```

Because the body is rigidly translating:

```text
a1 = a2 = A
```

So:

```text
a_CM = (m1 A + m2 A) / M
```

Factor out A:

```text
a_CM = ((m1 + m2) A) / M
```

Since:

```text
M = m1 + m2
```

we get:

```text
a_CM = A
```

So the centre of mass has the same acceleration as the rigid body's bulk translational motion.

---

## 6. The Result

Since:

```text
A = K / M
```

and:

```text
a_CM = A
```

we get:

```text
a_CM = K / M
```

Equivalently:

```text
K = M a_CM
```

Thus the rigid body behaves translationally as if the total external force K acts on a single representative point carrying the total mass M.

That representative point is the centre of mass.

---

## 7. What Was Actually Shown

The argument does **not** show that the centre of mass is literally the whole rigid body.

The centre of mass has no size, shape, orientation, or rotation.

What the argument shows is narrower:

```text
For translation, the centre of mass carries the same acceleration as the rigid body's bulk motion.
```

So the centre of mass is a **translational representative**.

It lets a rigid body be treated as one massive particle when the question concerns bulk motion.

---

## 8. Generalisation to Many Parts

For a rigid body made of many parts:

```text
m1, m2, m3, ..., mn
```

with total mass:

```text
M = sum of all mi
```

or more compactly:

```text
M = Σ mi
```

The centre of mass is:

```text
R_CM = (1 / M) Σ (mi ri)
```

Differentiate twice:

```text
a_CM = (1 / M) Σ (mi ai)
```

For pure rigid translation, every part has the same acceleration:

```text
ai = A for every part i
```

Therefore:

```text
a_CM = (1 / M) Σ (mi A)
```

Since A is the same for every part, factor it out:

```text
a_CM = (A / M) Σ mi
```

But:

```text
Σ mi = M
```

So:

```text
a_CM = (A / M) M
```

Therefore:

```text
a_CM = A
```

So again, the centre of mass has the same acceleration as the rigid body's bulk translational motion.

If the total applied force is K, and the equivalent translational force distribution is:

```text
Ki = (mi / M) K
```

then each part receives acceleration:

```text
ai = Ki / mi
```

Substitute Ki:

```text
ai = [(mi / M) K] / mi
```

Cancel mi:

```text
ai = K / M
```

So the whole rigid body translates with:

```text
a_CM = K / M
```

---

## 9. NML2 Interpretation

The conceptual route is:

```text
F = ma for each part
+ distributed force account
+ rigidity condition
+ mass-weighted centre-of-mass definition
= centre of mass behaves as the translational representative of the rigid body
```

The centre of mass is not automatically a body.

Rather:

```text
A selected system has a centre of mass.

A rigid body is a selected system whose parts travel together.

When the parts travel together, the centre-of-mass trajectory matches the body's bulk translational trajectory.

Therefore, for translational Newton-II accounting, the rigid body may be represented by a massive point-particle located at its centre of mass and carrying the total mass.
```

---

## 10. Important Limitation

The argument above concerns pure translation.

If the force is applied off-centre, the body may also rotate. Then the centre of mass still tracks the translational motion, but it does not capture the whole motion of the body.

For full rigid-body dynamics, one must also account for torque:

```text
torque = lever arm × force
```

More explicitly:

```text
tau = (r_applied - R_CM) × K
```

So:

```text
same total force -> same centre-of-mass acceleration
same torque      -> same rotational behaviour
```

The centre of mass is therefore enough for translational motion, but not enough for the full rigid-body state.
