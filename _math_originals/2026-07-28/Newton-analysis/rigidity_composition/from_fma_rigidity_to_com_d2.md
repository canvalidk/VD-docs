# From \(F=ma\) and Rigidity to the Centre-of-Mass Representative

## Purpose

This note presents the argument that a rigid composite body can be represented, for translational motion, by its centre of mass. The route begins from Newton’s second law for the parts and adds the rigidity condition.

The aim is not to assume immediately that a composite body “just has” one mass at one point. The aim is to show how that point-particle representative is earned.

---

## 1. Setup: Two Parts Forming One Rigid Body

Let a body \(B\) be made of two rigidly connected parts:

\[
m_1,\qquad m_2.
\]

Let their positions be

\[
\mathbf r_1(t),\qquad \mathbf r_2(t).
\]

The total mass is

\[
M=m_1+m_2.
\]

Suppose a total external force \(\mathbf K\) is applied to the rigid composite.

We want to know why the body’s translational motion can be represented by a single point: its centre of mass.

---

## 2. Replace One Body-Force by a Distributed Force Account

Instead of saying only

\[
\mathbf K \text{ acts on body } B,
\]

we distribute the force over the two parts:

\[
\mathbf K_1,\qquad \mathbf K_2,
\]

with

\[
\mathbf K_1+\mathbf K_2=\mathbf K.
\]

For pure translation of a rigid body, the natural mass-proportional distribution is

\[
\mathbf K_1=\frac{m_1}{M}\mathbf K,
\]

\[
\mathbf K_2=\frac{m_2}{M}\mathbf K.
\]

This says: the heavier part receives a larger share of the equivalent translational force-account.

---

## 3. Apply \(F=ma\) to Each Part

By Newton’s second law,

\[
\mathbf K_1=m_1\mathbf a_1,
\]

\[
\mathbf K_2=m_2\mathbf a_2.
\]

Substitute the mass-proportional force shares:

\[
m_1\mathbf a_1=\frac{m_1}{M}\mathbf K,
\]

so

\[
\mathbf a_1=\frac{\mathbf K}{M}.
\]

Likewise,

\[
m_2\mathbf a_2=\frac{m_2}{M}\mathbf K,
\]

so

\[
\mathbf a_2=\frac{\mathbf K}{M}.
\]

Therefore,

\[
\mathbf a_1=\mathbf a_2.
\]

The two parts receive the same acceleration.

---

## 4. Rigidity Supplies the Shared-Motion Constraint

A rigid body is not merely a selected collection of parts. Its parts travel together.

For pure translation, rigidity means:

\[
\mathbf a_1=\mathbf a_2=\mathbf A.
\]

The distributed force-account above is compatible with this rigidity condition, because each part receives the same acceleration:

\[
\mathbf A=\frac{\mathbf K}{M}.
\]

So the rigid body has one bulk translational acceleration.

---

## 5. Define the Centre of Mass

The centre of mass of the two-part body is

\[
\mathbf R_{\rm CM}
=
\frac{m_1\mathbf r_1+m_2\mathbf r_2}{m_1+m_2}.
\]

Using \(M=m_1+m_2\), this becomes

\[
\mathbf R_{\rm CM}
=
\frac{m_1\mathbf r_1+m_2\mathbf r_2}{M}.
\]

Differentiate twice:

\[
\mathbf a_{\rm CM}
=
\frac{m_1\mathbf a_1+m_2\mathbf a_2}{M}.
\]

Because the body is rigidly translating,

\[
\mathbf a_1=\mathbf a_2=\mathbf A.
\]

So

\[
\mathbf a_{\rm CM}
=
\frac{m_1\mathbf A+m_2\mathbf A}{M}.
\]

Factor out \(\mathbf A\):

\[
\mathbf a_{\rm CM}
=
\frac{(m_1+m_2)\mathbf A}{M}.
\]

Since \(M=m_1+m_2\),

\[
\mathbf a_{\rm CM}=\mathbf A.
\]

So the centre of mass has the same acceleration as the rigid body’s bulk translational motion.

---

## 6. The Result

Since

\[
\mathbf A=\frac{\mathbf K}{M},
\]

and

\[
\mathbf a_{\rm CM}=\mathbf A,
\]

we get

\[
\boxed{
\mathbf a_{\rm CM}=\frac{\mathbf K}{M}
}
\]

or equivalently,

\[
\boxed{
\mathbf K=M\mathbf a_{\rm CM}.
}
\]

Thus the rigid body behaves translationally as if the total external force \(\mathbf K\) acts on a single representative point carrying the total mass \(M\).

That representative point is the centre of mass.

---

## 7. What Was Actually Shown

The argument does **not** show that the centre of mass is literally the whole rigid body.

The centre of mass has no size, shape, orientation, or rotation.

What the argument shows is narrower:

\[
\text{For translation, the centre of mass carries the same acceleration as the rigid body's bulk motion.}
\]

So the centre of mass is a **translational representative**.

It lets a rigid body be treated as one massive particle when the question concerns bulk motion.

---

## 8. Generalisation to Many Parts

For a rigid body made of many parts \(m_i\), with total mass

\[
M=\sum_i m_i,
\]

the centre of mass is

\[
\mathbf R_{\rm CM}
=
\frac{1}{M}\sum_i m_i\mathbf r_i.
\]

Differentiate twice:

\[
\mathbf a_{\rm CM}
=
\frac{1}{M}\sum_i m_i\mathbf a_i.
\]

For pure rigid translation,

\[
\mathbf a_i=\mathbf A
\]

for every part. Therefore,

\[
\mathbf a_{\rm CM}
=
\frac{1}{M}\sum_i m_i\mathbf A
=
\frac{\mathbf A}{M}\sum_i m_i
=
\mathbf A.
\]

So again,

\[
\mathbf a_{\rm CM}=\mathbf A.
\]

If the total applied force is \(\mathbf K\), and the equivalent translational force distribution is

\[
\mathbf K_i=\frac{m_i}{M}\mathbf K,
\]

then each part receives acceleration

\[
\mathbf a_i=\frac{\mathbf K_i}{m_i}
=
\frac{\mathbf K}{M}.
\]

So the whole rigid body translates with

\[
\mathbf a_{\rm CM}=\frac{\mathbf K}{M}.
\]

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

\[
\boldsymbol\tau
=
(\mathbf r_{\rm applied}-\mathbf R_{\rm CM})\times \mathbf K.
\]

So:

```text
same total force -> same centre-of-mass acceleration
same torque -> same rotational behaviour
```

The centre of mass is therefore enough for translational motion, but not enough for the full rigid-body state.
