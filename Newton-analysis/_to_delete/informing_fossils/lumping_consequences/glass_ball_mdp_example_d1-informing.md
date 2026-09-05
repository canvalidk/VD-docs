> **Informing copy - do not edit here.**
> **Home:** the `particle_and_mass_origins` discussion - `Newton-analysis/_dscn_particle_and_mass_origins/glass_ball_mdp_example_d1.md`.
> **Placed in** `lumping_consequences` (user instruction, 2026-09-05 — this settles the call that was pending since 09-03) because it is the discussion's one worked case of what a lumping judgment does and undoes: the count is an output of the audit, not of the nouns *glass*, *crack*, *shard* (§2, §14.1–14.2); a lost licence is not carried through — the scene is re-lumped and the return of redundancy creates a NEW target rather than restoring the old (§5, §14.3); a total does not determine a partition (§6, §14.5) — the value question handed off intact; and the division of labour in §1, lumping decides WHICH target may own a value, an MDP decides WHAT value, is this note's boundary stated in one sentence.
> **Live here:** §0–§6, §14.1–14.5, §15. **Not for this note:** Parts IV–IX — the mass-determining processes, the robot, density and weight routes, remainder, uncertainty: value territory. "MDP" is slated for renaming (nml2.2 review §16).
> **Caution:** the `M_A = M_B` deduction in §5 rests on n persistence certificates plus mass-locality that the notation hides (review §3); that is value-side and does not touch the licence-loss half, which is what this note reads it for.
> This is a read-only copy; refresh from home if the source changes.

---

# Glass Ball Example: Lumping Failure, MDP Choice, and Mass Reconstruction

**Status:** working conceptual note  
**Project:** VD Newton / NML2.2  
**Date:** 24 July 2026

## 0. Purpose

This example develops the relation between:

```text
lumping
mass addresses
mass-determining processes (MDPs)
mass additivity
density-based determination
weight-based determination
reconstruction after a lost licence
uncertainty carried into a Newton-II prediction
```

The example begins with a glass ball whose mass has already been determined:

$$
m[A]=M_A=1\ \mathrm{kg}.
$$

The ball hits a wall and a crack becomes visible. We assume excellent footage and complete coverage at the declared observational resolution.

The important restriction is that we have **not** been told how many pieces of glass there are, or how many material objects the scene should contain. That is an output of the lumping audit, not an input supplied by the word *glass* or by the appearance of a crack.

---

# Part I — The division of labour

## 1. Lumping and MDPs answer different questions

The construction has two separate stages:

```text
tracking + coverage + tolerance + redundancy
  -> determine the licensed material targets

licensed material target
  -> create a mass address
  -> use an MDP to bind a mass value to that address
```

Lumping answers:

> **Which target may own a mass value?**

An MDP answers:

> **What value belongs at that target's mass address?**

Therefore, whenever a lumping licence is lost, the old mass binding cannot simply be carried through the failure. The scene must first be re-lumped. Every newly licensed target that is to enter Newton II then needs a mass value supplied by an MDP.

The MDP need not always be a fresh direct measurement. It may be:

- a direct density–volume determination;
- a direct weight/gravity determination;
- a Newton-II determination;
- an assembly/additivity determination;
- a partition or remainder determination;
- a reconstruction from complete material accounting.

---

## 2. A crack is not a Newtonian object-counting rule

The word *glass* invites familiar material intuitions:

```text
glass is solid
a crack marks a split
mechanical attachment preserves one object
separate motion must have been caused by fracture
```

None of these intuitions is part of the lumping criterion.

The relevant question is only:

> **How many redundancy bundles do the completely covered tracks support at the chosen tolerance and over the chosen interval?**

Accordingly, neither implication is valid:

```text
crack observed
  -> several modelled material objects

several modelled material objects
  -> crack observed
```

A crack may appear while all tracks continue to support one target. A split into separately moving bundles may occur without any crack at all. The material could behave unlike familiar solid glass; it could even be liquid glass. None of that changes the Newtonian criterion.

The crack is a visible scene feature. It matters only insofar as it is accompanied by track behaviour relevant to the declared lumping tolerance.

---

# Part II — Initial state

## 3. Before impact

Complete coverage and the redundancy audit license one target:

```text
TARGET ADDRESS
  A

MASS ADDRESS
  m[A]

BOUND VALUE
  m[A] = M_A = 1 kg
```

The value `1 kg` has provenance from an earlier MDP, although the present example need not specify which one.

The current licence may be represented schematically as:

$$
\operatorname{valid}(A;\varepsilon,[t_0,t_1],Q).
$$

As long as that licence continues, the value at `m[A]` may be reused.

---

# Part III — What happens after impact?

## 4. Case A — The one-target licence is never lost

Suppose the crack appears, but the completely covered tracks continue to form one redundancy bundle at the chosen tolerance.

Then:

```text
A remains licensed
m[A] remains the relevant mass address
m[A] = 1 kg remains reusable
no new MDP is demanded
```

The result does **not** depend on whether the crack is partial, whether two regions are mechanically joined, or whether the material fits ordinary expectations about glass. Those facts are not the operational criterion.

The only relevant statement is:

```text
one covered redundancy bundle persists
-> one target licence persists
```

---

## 5. Case B — The old licence is lost, but all material later forms one new bundle

Now suppose the original one-target licence genuinely fails. During or after impact, the completely covered tracks no longer support target `A` as one bundle.

### 5.1 First re-lump the scattered material

The footage is used to identify the new redundancy bundles:

$$
P_1,P_2,\ldots,P_n.
$$

These are not presupposed pieces. They are the outputs of the post-failure lumping audit.

Each receives a mass address:

$$
m[P_1]=m_1,\quad m[P_2]=m_2,\quad\ldots,\quad m[P_n]=m_n.
$$

At first, the individual values may all be unknown.

### 5.2 First additivity MDP: partition of the old target

Complete coverage establishes that these post-event targets collectively account for all the material formerly represented by `A`, with no above-resolution material missing and no additional material included.

A licensed additivity/partition MDP therefore gives:

$$
M_A=m_1+m_2+\cdots+m_n.
$$

Because $M_A=1\ \mathrm{kg}$,

$$
1\ \mathrm{kg}=m_1+m_2+\cdots+m_n.
$$

This equation fixes the total. It does **not** determine the individual values $m_i$.

### 5.3 The scattered targets later come together

Suppose all the tracked targets $P_1,\ldots,P_n$ later become redundant with one another and are lumped into a new target:

```text
new target address: B
new mass address:   m[B]
```

The return of one-bundle redundancy creates `B`. It does not automatically restore `A`, because the original licence was lost.

### 5.4 Second additivity MDP: assembly of the new target

Because `B` is formed from the same completely accounted-for family $P_1,\ldots,P_n$, an assembly/additivity MDP gives:

$$
M_B=m_1+m_2+\cdots+m_n.
$$

Now the two MDP outputs can be compared:

$$
M_A=m_1+m_2+\cdots+m_n,
$$

$$
M_B=m_1+m_2+\cdots+m_n.
$$

Therefore:

$$
M_A=M_B.
$$

Since $M_A=1\ \mathrm{kg}$,

$$
\boxed{M_B=1\ \mathrm{kg}}.
$$

### 5.5 What has been recovered

The familiar intuition that the mass number may be used again has been recovered, but not by saying:

```text
“It is obviously the same ball.”
```

The number is re-derived through the following route:

```text
A loses its licence
-> identify every new redundancy bundle
-> account for all former material
-> M_A = sum of the new target masses
-> the same target family later forms B
-> M_B = the same sum
-> deduce M_A = M_B
```

The value is therefore **reconstructed for a new address**, not continuously carried through a period in which the old address was unlicensed.

### 5.6 When the reconstruction fails

The deduction fails if, for example:

```text
one former target is missing
an untracked offshoot escaped
new material joined the family
coverage was insufficient
lineage between the two families is uncertain
additivity is not licensed to the required precision
```

In any of those cases, `m[B] = 1 kg` cannot be concluded by this route.

---

## 6. Case C — The post-impact scene continues to contain several targets

Suppose the track audit licenses several continuing bundles:

$$
P_1,P_2,\ldots,P_n.
$$

Then the old address `A` has expired and the new mass addresses are initially unbound:

$$
m[P_1],m[P_2],\ldots,m[P_n].
$$

Complete material accounting and additivity give:

$$
\sum_{i=1}^{n}m[P_i]=1\ \mathrm{kg}.
$$

This does not determine the partition.

For two targets, `S` and `R`,

$$
m[S]+m[R]=1\ \mathrm{kg}.
$$

One further independent mass determination is required before either individual value can be obtained by subtraction.

---

# Part IV — The very fast robot

## 7. Setup

Let the post-impact lumping audit license two targets:

```text
S = the target the robot will scoop
R = the remaining flying target
```

Additivity supplies:

$$
M_A=m[S]+m[R].
$$

Since $M_A=1\ \mathrm{kg}$,

$$
1\ \mathrm{kg}=m[S]+m[R].
$$

The robot scoops `S` while `R` continues moving.

Disturbing `S` does not automatically invalidate `R`. Once `S` and `R` are separately licensed targets, each has its own target history and Newton-II account. The robot's action on `S` matters to `R` only if it also changes `R`'s force account, material content, trackability, or target licence.

The robot now needs one direct MDP for `S`. After that, a remainder MDP can determine `R`.

---

# Part V — Density MDP for the scooped target

## 8. Density–volume route

The robot measures the volume of `S` and supplies a density model:

$$
\rho=\frac{m}{V}.
$$

Therefore:

$$
\boxed{m[S]=\rho_S V_S}.
$$

This MDP depends on two kinds of input:

```text
measured geometry/volume of S
licensed density model for the material in S
```

### 8.1 Characteristic assumptions and failure modes

The route may fail or become inaccurate because of:

```text
uncertain density
spatially non-uniform density
wrong material or phase identification
temperature or pressure dependence
voids, bubbles, porosity, or inclusions
volume-measurement error
material exchange during the test
loss or replacement of the target address
```

The example must not silently assume familiar solid glass. The density model must fit the material actually tracked as `S`.

### 8.2 Uncertainty

If the density and volume uncertainties are independent and sufficiently small, then approximately:

$$
\left(\frac{u(m[S])}{m[S]}\right)^2
\approx
\left(\frac{u(\rho_S)}{\rho_S}\right)^2
+
\left(\frac{u(V_S)}{V_S}\right)^2.
$$

There may also be model uncertainty not captured by the two numerical terms, especially uncertainty about whether one density value adequately represents the target.

---

# Part VI — Weight/gravity MDP for the scooped target

## 9. Weight route

Alternatively, the robot determines the gravitational force on `S` and uses:

$$
F_g=m_g g.
$$

Thus:

$$
\boxed{m_g[S]=\frac{F_g[S]}{g}}.
$$

To use this value as the inertial mass in Newton II, the gravitational–inertial mass link must be licensed for the present model.

### 9.1 What must actually be measured

The force in the equation must be the gravitational force, or a sensor reading from which the gravitational force can be correctly reconstructed.

A scale-like sensor on an accelerating robot may report a support force or apparent weight rather than simply $mg$. Therefore the robot must either:

```text
perform the test in a suitable controlled state
or
correct for the robot's acceleration and other forces
```

### 9.2 Characteristic assumptions and failure modes

The route may fail or become inaccurate because of:

```text
uncertain local g
uncertain force measurement
robot acceleration or vibration
other forces included in the sensor reading
incorrect direction resolution
an unlicensed gravitational-to-inertial mass identification
material exchange or target-address failure during the test
```

### 9.3 Uncertainty

If the force and local gravitational-field uncertainties are independent and sufficiently small, then approximately:

$$
\left(\frac{u(m_g[S])}{m_g[S]}\right)^2
\approx
\left(\frac{u(F_g[S])}{F_g[S]}\right)^2
+
\left(\frac{u(g)}{g}\right)^2.
$$

The density and weight routes can therefore bind values to the same target address while carrying different uncertainty budgets and different characteristic failure modes.

---

# Part VII — Remainder MDP for the flying target

## 10. Determine the mass of `R`

Once a direct MDP has bound a value to `m[S]`, the additivity relation becomes sufficient to determine `m[R]`:

$$
M_A=m[S]+m[R].
$$

Therefore:

$$
\boxed{m[R]=M_A-m[S]}.
$$

Since $M_A=1\ \mathrm{kg}$,

$$
\boxed{m[R]=1\ \mathrm{kg}-m[S]}.
$$

This is a **remainder MDP**. It is distinct from the direct MDP performed on `S`.

The complete chain is:

```text
split A into S and R
-> additivity: M_A = m[S] + m[R]
-> direct MDP on S
-> bind m[S]
-> remainder MDP
-> bind m[R] = M_A - m[S]
```

### 10.1 Uncertainty inherited by the remainder

If the uncertainties in $M_A$ and $m[S]$ are independent, then:

$$
u(m[R])^2
\approx
u(M_A)^2+u(m[S])^2.
$$

Thus the chosen direct MDP for `S` affects the quality of the mass binding obtained for `R`.

---

# Part VIII — Newton-II prediction for the other target

## 11. Predicting `R` while the robot tests `S`

Once the remainder MDP has supplied `m[R]`, Newton II may be applied to `R`, provided:

```text
R remains a licensed massive target
the reference frame is licensed as inertial
the net-force account for R is available
the prediction is made for the relevant interval
no later split, merge, or material exchange invalidates R
```

Then:

$$
\mathbf a[R]
=
\frac{\mathbf F_{\mathrm{net}}[R]}{m[R]}.
$$

Substituting the remainder determination:

$$
\boxed{
\mathbf a[R]
=
\frac{\mathbf F_{\mathrm{net}}[R]}
{M_A-m[S]}
}.
$$

For the density route:

$$
\boxed{
\mathbf a[R]
=
\frac{\mathbf F_{\mathrm{net}}[R]}
{M_A-\rho_SV_S}
}.
$$

For the weight route:

$$
\boxed{
\mathbf a[R]
=
\frac{\mathbf F_{\mathrm{net}}[R]}
{M_A-F_g[S]/g}
}.
$$

The final acceleration prediction therefore preserves the provenance of the mass determination performed on the other target.

### 11.1 Meaning of “act fast enough”

The robot's speed matters because the answer must be produced while it is still useful and while the relevant licences remain valid. It must complete the MDP before:

```text
R reaches the event being predicted
R loses its present target licence
R undergoes another split or merge
R's force account changes in an unmodelled way
coverage or tracking of R fails
```

The time pressure is therefore a prediction deadline, not a special principle of mass determination.

---

# Part IX — Comparing the two direct MDPs

## 12. Density versus weight

| Feature | Density MDP | Weight/gravity MDP |
|---|---|---|
| Core equation | $m=\rho V$ | $m_g=F_g/g$ |
| Main measured input | Volume | Gravitational force or a corrected sensor reading |
| Main supplied/model input | Density | Local gravitational field $g$ |
| Typical uncertainty sources | $\rho$, $V$, uniformity, phase, voids | $F_g$, $g$, robot acceleration, other forces |
| Directly determines | Density-model mass | Gravitational mass |
| Extra bridge for Newton II | Density/stuff mass must be licensed as inertial mass | Gravitational mass must be licensed as inertial mass |
| Characteristic failure | Wrong density model | Apparent weight mistaken for gravitational force |
| Downstream effect | Uncertainty enters the remainder mass of `R` | Uncertainty enters the remainder mass of `R` |

Neither route is simply “the mass measurement.” Each is a distinct MDP with its own evidence, assumptions, uncertainty, and failure conditions.

---

# Part X — Complete trace

## 13. Integrated route

```text
1. Original covered bundle is lumped as target A.
2. An earlier MDP has bound m[A] = M_A = 1 kg.
3. A hits the wall and a crack appears.
4. Ignore ordinary glass intuition when counting targets.
5. Audit the completely covered tracks at the chosen tolerance.

6A. If one bundle persists:
      A remains licensed.
      Reuse m[A] = 1 kg.
      No new MDP.

6B. If A's licence fails:
      Re-lump the scene into P1, ..., Pn.
      Create m[P1], ..., m[Pn].
      Use additivity:
        M_A = m1 + ... + mn.

7B. If exactly the same accounted-for family later forms one new bundle B:
      Create target B and mass address m[B].
      Use additivity again:
        M_B = m1 + ... + mn.
      Deduce:
        M_B = M_A = 1 kg.

6C. If several targets remain:
      Additivity fixes only their total.
      Individual masses remain underdetermined.

8. In the two-target robot case, label them S and R.
9. Additivity gives:
      M_A = m[S] + m[R].
10. Robot scoops S and performs one direct MDP:
      density route: m[S] = rho_S V_S
      or
      weight route:  m[S] = F_g[S] / g.
11. Use the remainder MDP:
      m[R] = M_A - m[S].
12. Apply Newton II to R while its licences remain valid:
      a[R] = F_net[R] / (M_A - m[S]).
13. Carry the uncertainty and provenance of the chosen MDP into the prediction.
```

---

# Part XI — Main lessons

## 14. What the glass-ball example establishes

### 14.1 Object count is an output

The number of material objects is determined by covered, tolerance-indexed track redundancy. It is not supplied by the nouns *ball*, *glass*, *crack*, *shard*, or *piece*.

### 14.2 A crack is neither necessary nor sufficient for a split

A crack can occur without loss of the one-target licence. A split into several modelled targets can occur without a crack.

### 14.3 Loss of a licence removes permission to reuse the old binding

When `A` fails, the historical value `1 kg` still exists as a record, but it cannot be attached to a new present target merely by intuition.

### 14.4 Additivity can reconstruct a new binding

When all former material is accounted for and the same family later forms `B`, two additivity equations yield:

$$
M_A=M_B.
$$

The familiar result is recovered as a deduction.

### 14.5 A total does not determine a partition

From:

$$
M_A=m[S]+m[R],
$$

neither $m[S]$ nor $m[R]$ is individually known. One further independent MDP is required.

### 14.6 One direct MDP can determine another target by remainder

After determining `m[S]`, the mass of `R` follows from:

$$
m[R]=M_A-m[S].
$$

### 14.7 MDP choice changes the epistemic quality of the answer

Density and weight can target the same mass address while contributing different uncertainty budgets, assumptions, and failure modes.

### 14.8 A Newton-II prediction inherits MDP provenance

The predicted acceleration of `R` depends on how `m[S]` was determined:

$$
\mathbf a[R]
=
\frac{\mathbf F_{\mathrm{net}}[R]}
{M_A-m_{\mathrm{MDP}}[S]}.
$$

The mass value is therefore not a context-free number. It is an addressed value with a derivation history.

---

# 15. Compact conclusion

The glass-ball example replaces a familiar but unexamined intuition—“the same material still has the same mass”—with an explicit Newtonian reconstruction:

```text
track the material
-> determine when the old lumping licence fails
-> re-lump the post-failure scene
-> create new mass addresses
-> relate them by additivity
-> perform one direct MDP where required
-> determine remaining masses by assembly or remainder
-> carry uncertainty and provenance into Newton II
```

The result is not scepticism about ordinary mass reuse. It is an explanation of how that reuse is earned.
