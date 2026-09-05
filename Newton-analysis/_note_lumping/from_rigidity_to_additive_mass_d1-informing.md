> **Informing copy - do not edit here.**
> **Home:** the `particle_and_mass_origins` discussion - `Newton-analysis/_dscn_particle_and_mass_origins/rigidity_composition/from_rigidity_to_additive_mass_d1.md`.
> **Placed in** `lumping` (stocked 2026-09-03 under the name `mass_address_lumping`, renamed `lumping_conditions` the same day on the two-note decision, and `lumping` on 2026-09-05 when the one-note decision made the qualifier redundant) because it is the only place **rigidity in the dynamical sense** — shared acceleration, `a1 = a2 = A` — is set out (§3, §6). It stands downstream of this note (it is the derivation the account licence rests on), but the note has to tell this sense apart from the track senses — fixed distances (d2), fixed offset (d4), `ε_shape`/`ε_trans` (the review) — and nothing else states it.
> **Live here:** §3, §6, §9. **Not for this note:** §4–§5, §7–§8 — the derivation of `M = Σ mᵢ` and the centre of mass: the account licence this note disclaims.
> **Caution:** "rigidity" here is pure rigid translation with shared acceleration — d4's zero-tolerance translation case seen from the dynamics side, not distance preservation. Its d3 (`from_fma_rigidity_to_com_plain_math_d3`) makes the same rigidity contribution and is cited, not copied.
> This is a read-only copy; refresh from home if the source changes.

---

# From Rigidity to Additive Inertial Mass

## Purpose

This note gives the argument that a rigid composite body should have additive inertial mass:

```text
M = m1 + m2
```

The point is not to assume this at the start. The point is to derive it from the attempt to replace a rigidly co-moving composite by one Newton-II target.

The argument does not use momentum conservation.

The argument also does not begin by assuming that physical forces on the parts add up to a physical force on the whole.

It uses:

```text
F = ma for each part
rigidity as shared acceleration
representative adequacy: the one-point representative must cover all part-level inertial demands
```

---

## 1. Start with two massive parts

Let a body be made of two parts:

```text
part 1 has inertial mass m1
part 2 has inertial mass m2
```

For now, do not assume the mass of the combined body.

Let the proposed one-point representative have unknown inertial mass:

```text
M
```

The question is:

```text
What must M be if this one point is to represent both rigidly co-moving parts?
```

---

## 2. Apply F = ma to the parts

Each part is a Newton-II target in its own right.

For part 1:

```text
F1-account = m1 a1
```

For part 2:

```text
F2-account = m2 a2
```

Here `F1-account` and `F2-account` should be read carefully. They are not yet being added as physical external forces. They are the Newton-II force-accounts demanded by the part accelerations.

---

## 3. Add rigidity

For pure rigid translation, the parts move together.

That means they share one bulk acceleration:

```text
a1 = a2 = A
```

Substitute this into the two part-level Newton-II accounts:

```text
F1-account = m1 A
F2-account = m2 A
```

So rigidity turns the two separate part accelerations into one shared acceleration demand.

The parts differ only in their inertial coefficients:

```text
part 1 demands m1 A
part 2 demands m2 A
```

---

## 4. Introduce the one-point representative

Suppose the whole rigid composite can be represented by one Newton-II target.

Let its unknown inertial mass be `M`.

If that representative accelerates with the shared bulk acceleration `A`, then its Newton-II account is:

```text
F_rep-account = M A
```

The representative is supposed to stand for both parts at once.

Therefore it must cover both part-level inertial demands:

```text
M A = m1 A + m2 A
```

This is the key step.

It is not the physical force-sum law. It is a representative adequacy condition:

```text
A one-point representative of a composite must include every part's inertial demand under the shared motion it represents.
```

---

## 5. Derive the combined mass

From:

```text
M A = m1 A + m2 A
```

factor the right-hand side:

```text
M A = (m1 + m2) A
```

For an arbitrary nonzero shared acceleration `A`, the inertial coefficients must match:

```text
M = m1 + m2
```

So the mass of the representative is not assumed at the beginning.

It is derived as the inertial coefficient required for one point to stand in for both rigidly co-accelerated parts.

---

## 6. What rigidity contributed

Rigidity alone does not say:

```text
M = m1 + m2
```

Rigidity is kinematic. It says that the parts share the same translational acceleration:

```text
a1 = a2 = A
```

But once the parts share one acceleration, `F = ma` gives a clean comparison of their inertial demands:

```text
m1 A
m2 A
```

The representative mass `M` is then the coefficient that covers those demands together:

```text
M A = m1 A + m2 A
```

So the real derivation is:

```text
F = ma
+ rigidity
+ representative adequacy
= additive inertial mass
```

---

## 7. Generalisation to many parts

For many parts:

```text
m1, m2, m3, ..., mn
```

rigid translation gives:

```text
a1 = a2 = a3 = ... = an = A
```

Each part-level Newton-II account is:

```text
Fi-account = mi A
```

Let the one-point representative have inertial mass `M`.

Its account is:

```text
F_rep-account = M A
```

Representative adequacy requires:

```text
M A = m1 A + m2 A + m3 A + ... + mn A
```

Factor out `A`:

```text
M A = (m1 + m2 + m3 + ... + mn) A
```

Therefore:

```text
M = m1 + m2 + m3 + ... + mn
```

or:

```text
M = sum of all mi
```

---

## 8. Relation to the centre of mass

Once the representative mass has been earned as:

```text
M = m1 + m2
```

we can ask where the representative point should be placed.

Since the same part-masses are the inertial weights in the representative account, the natural representative position is the mass-weighted position:

```text
R_CM = (m1 r1 + m2 r2) / (m1 + m2)
```

For many parts:

```text
R_CM = (sum of mi ri) / (sum of mi)
```

This is the centre of mass.

So the order is:

```text
1. Rigidity gives shared acceleration.
2. F = ma gives part-level inertial demands.
3. Representative adequacy gives additive mass.
4. The same mass weights then motivate the centre-of-mass position.
```

The centre of mass is therefore not introduced as a magic average point. It is the point whose mass-weighted track can carry the one-point Newton-II account of the rigid body's bulk translation.

---

## 9. What has not been assumed

This argument does not assume at the beginning:

```text
M = m1 + m2
```

It does not begin with:

```text
F_total = F1 + F2
```

It does not use:

```text
momentum conservation
```

The only composition step is the representative adequacy condition:

```text
A one-point representative of a composite must cover all the part-level inertial demands of the composite under the shared motion being represented.
```

That is the explicit bridge from rigid co-motion to additive inertial mass.
