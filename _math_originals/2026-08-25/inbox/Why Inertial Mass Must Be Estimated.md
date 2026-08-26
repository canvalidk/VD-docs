# Why Inertial Mass Must Be Estimated

**Status:** working draft  
**Project:** VD Newton / Newton-II analysis  
**Scope:** why an **empirical determination** of inertial mass from net-force and inertial-acceleration must be an estimation procedure. This does not deny that explicitly exact, compatible textbook inputs permit exact checked recovery.

---

## 0. Thesis

Newton's Second Law joins three addressed quantities belonging to one material object, over the same relevant interval and in the same inertial frame:

\[
\mathbf F_{\mathrm{net}}[A]=m[A]\mathbf a[A],
\qquad m[A]>0.
\]

At first sight, the law appears algebraically symmetric. Any two quantities seem to determine the third:

\[
\mathbf a=\frac{1}{m}\mathbf F_{\mathrm{net}},
\qquad
\mathbf F_{\mathrm{net}}=m\mathbf a,
\qquad
m=\frac{\mathbf F_{\mathrm{net}}}{\mathbf a}.
\]

The third expression is deceptive. Division of one vector by another is not defined. More importantly, the mass corner is structurally different from the other two corners. The ordinary types of a positive scalar and a vector are enough to guarantee the acceleration and net-force operations, but the ordinary types of two vectors do not guarantee that any positive scalar relates their values.

For explicitly exact inputs, inertial-mass recovery is therefore a **checked** operation. For empirical inputs, the problem is stronger. Net-force and inertial-acceleration must remain independently identifiable quantities, yet independently produced measurement results do not generally form an exact Newton-II pair. Newton II also does not uniquely specify how an imperfect pair should be moved onto its exact relation.

Therefore:

> **When inertial mass is determined from empirical net-force and inertial-acceleration results, it must be estimated by a declared joint estimation policy. The reconciliation of the two channels is part of the mass determination itself, not a preprocessing operation that redefines either input.**

---

## 1. Newton II as a six-entry law-house

Use the following local numbering for the Newton-II house:

```text
1. inertial-acceleration := Res_1(...)
2. inertial-acceleration := Res_2(net-force, inertial-mass)
3. net-force             := Res_3(inertial-acceleration, inertial-mass)
4. inertial-mass         := Res_4(inertial-acceleration, net-force)
5. net-force             := Res_5(...)
6. inertial-mass         := Res_6(...)
```

Entry 1 is the chimney. Entries 2–4 are the Newton-II triplet. Entries 5–6 are the two walls.

The present argument is primarily about the three inward-facing triplet residuals:

\[
\mathbf a
:=
\operatorname{Res}_2(\mathbf F_{\mathrm{net}},m),
\]

\[
\mathbf F_{\mathrm{net}}
:=
\operatorname{Res}_3(\mathbf a,m),
\]

\[
m
:=
\operatorname{Res}_4(\mathbf a,\mathbf F_{\mathrm{net}}).
\]

The question is not merely whether all three residuals can be written as algebraic rearrangements of one equation. The VD asks what operation each residual must actually cause a disciplined interpreter to perform when that headword is demanded.

---

## 2. Newton II is an addressed relation

Before comparing the three operations, the inputs must be correctly addressed.

For one material object `A`, Newton II relates:

```text
m[A]
a[A]
F_net[A]
```

The quantities must refer to:

- the same material object;
- the same relevant time or interval;
- the same inertial-frame-qualified account.

Thus

\[
\mathbf F_{\mathrm{net}}[A]
=
m[A]\mathbf a[A]
\]

is not merely a relation among one scalar and two vectors with suitable units. A calculation can be dimensionally and arithmetically correct while still failing to be a Newton-II calculation because the values belong to different targets, intervals, or frames.

This addressed structure will be assumed throughout the argument.

---

## 3. Two corners are total; the mass corner is not

### 3.1 Net-force determination

Given a positive inertial mass and an inertial-acceleration vector,

\[
\operatorname{NetForce}:
\mathrm{PositiveMass}
\times
\mathrm{AccelerationVector}
\to
\mathrm{ForceVector},
\]

\[
(m,\mathbf a)
\mapsto
m\mathbf a.
\]

Every correctly typed input pair returns a force vector. Scalar multiplication is defined for every positive scalar and every acceleration vector.

This is a total operation.

### 3.2 Inertial-acceleration determination

Given a net-force vector and a positive inertial mass,

\[
\operatorname{Acceleration}:
\mathrm{ForceVector}
\times
\mathrm{PositiveMass}
\to
\mathrm{AccelerationVector},
\]

\[
(\mathbf F_{\mathrm{net}},m)
\mapsto
\frac{1}{m}\mathbf F_{\mathrm{net}}.
\]

Because `m > 0`, the reciprocal exists. Every correctly typed input pair returns an acceleration vector.

This is also a total operation.

### 3.3 The naïve mass operation

The apparently symmetric signature would be

\[
\operatorname{Mass}:
\mathrm{ForceVector}
\times
\mathrm{AccelerationVector}
\to
\mathrm{PositiveMass}.
\]

No such total function is supplied by Newton II.

The ordinary input types tell us that one value is a force vector and the other is an acceleration vector. They do not tell us that the particular values satisfy

\[
\exists m>0:
\mathbf F_{\mathrm{net}}=m\mathbf a.
\]

That missing condition is relational and value-level. It is not encoded in either vector type separately.

The mass corner is therefore structurally different:

```text
PositiveMass × AccelerationVector
    -> ForceVector                         total

ForceVector × PositiveMass
    -> AccelerationVector                  total

ForceVector × AccelerationVector
    -> checked MassRecoveryResult          not total as a bare mass readout
```

The brevity of the first two corners is not a standard that the mass corner has somehow failed to meet. Their brevity is subsidised by their input types. The mass corner receives no corresponding guarantee.

---

## 4. Exact mass recovery is a checked operation

A more honest exact signature is

\[
\operatorname{MassExact}:
\mathrm{ForceVector}
\times
\mathrm{AccelerationVector}
\to
\mathrm{MassRecoveryResult}.
\]

The result type must distinguish several cases.

### 4.1 Exact nonzero compatible pair

A positive scalar exists when the two exact nonzero vectors are codirectional:

\[
\mathbf a\neq\mathbf 0,
\qquad
\exists m>0:
\mathbf F_{\mathrm{net}}=m\mathbf a.
\]

Equivalently, there is a common unit direction \(\widehat{\mathbf u}\) such that

\[
\mathbf F_{\mathrm{net}}=F_{\parallel}\widehat{\mathbf u},
\qquad
\mathbf a=a_{\parallel}\widehat{\mathbf u},
\]

with

\[
F_{\parallel}>0,
\qquad
a_{\parallel}>0.
\]

Only after this relation has been established may the scalar be read:

\[
m
=
\frac{F_{\parallel}}{a_{\parallel}}
=
\frac{|\mathbf F_{\mathrm{net}}|}{|\mathbf a|}.
\]

The quotient of magnitudes is therefore a **readout of an already established positive-scalar relation**. It is not an operation that establishes the relation.

### 4.2 Exact zero-zero pair

If

\[
\mathbf F_{\mathrm{net}}=\mathbf 0,
\qquad
\mathbf a=\mathbf 0,
\]

then every finite positive mass satisfies Newton II:

\[
\mathbf 0=m\mathbf 0.
\]

The trial is compatible with positive inertial mass but does not determine its value.

### 4.3 Exactly one vector is zero

If

\[
\mathbf F_{\mathrm{net}}=\mathbf 0,
\qquad
\mathbf a\neq\mathbf 0,
\]

or

\[
\mathbf F_{\mathrm{net}}\neq\mathbf 0,
\qquad
\mathbf a=\mathbf 0,
\]

then no finite positive scalar satisfies the exact supplied relation.

### 4.4 Exact nonzero incompatible pair

If the exact nonzero vectors are not codirectional, then

\[
\nexists m>0:
\mathbf F_{\mathrm{net}}=m\mathbf a.
\]

This is an inconsistency among the exact premises. It is not a successful mass recovery.

A useful exact result type is therefore:

```text
ExactMass(m)
ZeroZeroUnderdetermined
ZeroNonzeroExactInconsistency
NoncodirectionalExactInconsistency
```

---

## 5. Vector division is not defined

The school-level rearrangement

\[
m=\frac{F}{a}
\]

is harmless only after the problem has been reduced to one scalar direction. Written with full vectors,

\[
m=\frac{\mathbf F}{\mathbf a}
\]

is not a defined vector operation.

A scalar may multiply a vector. A nonzero scalar may divide a vector. But one vector cannot generally divide another to return a scalar.

For example, suppose

\[
\mathbf F=(10,0),
\qquad
\mathbf a=(4,3).
\]

No scalar \(m\) satisfies

\[
(10,0)=m(4,3).
\]

Nevertheless, several scalar expressions can be formed:

\[
\frac{|\mathbf F|}{|\mathbf a|}=2,
\]

\[
\frac{\mathbf a\cdot\mathbf F}{\mathbf a\cdot\mathbf a}=1.6,
\]

\[
\frac{\mathbf F\cdot\mathbf F}{\mathbf F\cdot\mathbf a}=2.5.
\]

These are not three notations for vector division. They are different scalar estimators, each arising from a different decision about how the pair should be reconciled.

This becomes decisive once the inputs are empirical.

---

## 6. Exact quantities, measurements, and latent estimates must be distinguished

The empirical argument requires three levels that earlier formulations can easily collapse.

### 6.1 Observations

Observations are instrument outputs and records before they have been assigned as final Newton-II quantities. Examples include:

- load-cell or deformation readings;
- field and calibration records;
- time-indexed position samples;
- accelerometer outputs;
- timestamps, frame markers, and instrument-state records.

### 6.2 Independent measurement results

A force-side measurement procedure uses its observations, instrument model, calibration, target assignment, and uncertainty account to produce something like

\[
(\widetilde{\mathbf F},\Sigma_F,P_F).
\]

An acceleration-side procedure independently uses trajectory or accelerometer observations to produce

\[
(\widetilde{\mathbf a},\Sigma_a,P_a).
\]

Here:

- the tildes mark measured estimates;
- \(\Sigma_F\) and \(\Sigma_a\) represent uncertainty information;
- \(P_F\) and \(P_a\) represent provenance.

These are legitimate measurement results even when their central vector estimates are not codirectional.

### 6.3 Joint Newton-II-constrained latent estimates

A later joint procedure may infer latent values

\[
\mathbf F^*,
\qquad
\mathbf a^*,
\qquad
m,
\]

subject to

\[
\mathbf F^*=m\mathbf a^*,
\qquad
m>0.
\]

The starred vectors are not what either independent measurement “meant all along.” They are model-constrained estimates produced jointly from the two measurement results.

Thus:

```text
observations
    -> independent measurement results
    -> joint Newton-II-constrained latent estimates
```

The independent measurements and the latent fitted quantities are different objects and must not be silently identified.

---

## 7. Why the two measurement channels must remain independent

The need for independent channels is not an optional philosophy of good experiments. It follows from the operability of the Newton-II triplet itself.

### 7.1 What the acceleration corner requires

The acceleration residual consumes net-force and inertial-mass:

\[
\mathbf a
=
\operatorname{Res}_2(\mathbf F_{\mathrm{net}},m).
\]

For this operation to be usable, net-force must be identifiable without first requiring the acceleration that the operation is supposed to return.

### 7.2 What the net-force corner requires

The net-force residual consumes inertial-acceleration and inertial-mass:

\[
\mathbf F_{\mathrm{net}}
=
\operatorname{Res}_3(\mathbf a,m).
\]

For this operation to be usable, inertial-acceleration must be identifiable without first requiring the net-force that the operation is supposed to return.

### 7.3 The empirical routes satisfy this requirement

In practice, the channels can be genuinely separate:

```text
force-side observations
    -> force-side measurement procedure
    -> measured net-force result
```

```text
trajectory observations
    -> acceleration-side measurement procedure
    -> measured inertial-acceleration result
```

The force-side result need not inspect the trajectory merely to qualify as a force measurement. The acceleration-side result need not inspect force data merely to qualify as an acceleration measurement.

This independence is what allows the two results to provide empirical content when they are later compared under Newton II.

---

## 8. Independent empirical results are not exact Newton-II pairs

Two independently produced empirical vector estimates, each with its own uncertainty and error sources, have no reason to land exactly on

\[
\mathbf F=m\mathbf a.
\]

Under ordinary continuous error models, exact codirectionality is a measure-zero event. More generally, even when displayed values happen to align after rounding, the results remain measurements with uncertainty. Rounded alignment does not transform them into explicitly exact Newton-II quantities.

Therefore the correct branch distinction is not:

```text
aligned pair
versus
misaligned pair
```

but:

```text
explicitly exact supplied pair
versus
empirical measurement results
```

Every empirical determination belongs to the second branch, whether or not the arrows appear aligned on the page.

---

## 9. Newton II does not uniquely specify the estimate

Once an empirical pair falls away from the exact-law relation, the law does not uniquely say how it should be corrected.

Suppose an estimator:

- uses only the two nonzero measured vectors;
- is invariant under rotation of the coordinate axes;
- has the dimensions of mass.

Then it must have the form

\[
\widehat m
=
\frac{|\widetilde{\mathbf F}|}{|\widetilde{\mathbf a}|}
\,g(\cos\theta),
\]

where \(\theta\) is the angle between the measured vectors and \(g\) is dimensionless.

Exact Newton II requires only

\[
g(1)=1.
\]

It does not determine \(g(c)\) for \(c\neq 1\).

Different familiar unconstrained procedures, or procedures considered before the positive-mass constraint is imposed, correspond to different choices:

\[
g(c)=1
\qquad
\text{magnitude ratio},
\]

\[
g(c)=c
\qquad
\text{minimise force residuals while holding acceleration fixed},
\]

\[
g(c)=\frac{1}{c}
\qquad
\text{minimise acceleration residuals while holding force fixed, where }c\neq0.
\]

These procedures answer different statistical questions. None is selected by the exact law alone.

Therefore:

> **The measured vector pair and Newton II do not determine a unique mass estimate. An estimation policy is additional input.**

The estimation policy expresses which corrections are plausible, how force and acceleration uncertainties are weighted, whether errors are correlated, and what loss or likelihood is being used.

---

## 10. Why reconciliation cannot be moved upstream

One might try to preserve a short exact mass definition by saying:

> First let metrology reconcile the force and acceleration. Then hand the compatible pair to the mass entry.

This deferral picture fails.

### 10.1 Horn one: the upstream process preserves the independent quantities

Suppose the upstream process returns the force and acceleration as their independent channels determined them.

Then the pair remains generically nonconforming. The exact mass readout still has nothing to apply to on the ordinary empirical domain.

The reconciliation has not been performed. The problem has only been renamed.

### 10.2 Horn two: the upstream process returns reconciled values as the force and acceleration

Suppose instead that the process adjusts the acceleration using the force direction, adjusts the force using the acceleration direction, or jointly adjusts both and then presents the adjusted values as the original Newton-II quantities.

Then the quantities consumed by the other two triplet corners are no longer independently identifiable:

- acceleration now partly depends on net-force;
- net-force now partly depends on acceleration.

The acceleration corner would consume a net-force already shaped by its own output. The net-force corner would consume an acceleration already shaped by its own output.

The reconciliation makes the mass corner appear clean by damaging the operability of the other two corners.

### 10.3 The apparent third route confirms the conclusion

A defender may reply:

> Keep the independent measurements unchanged, but let an upstream procedure produce a separate compatible starred pair.

That is coherent, but it is no longer preprocessing the meanings of net-force and inertial-acceleration. It is already performing the joint model-constrained operation from which mass is recovered.

The starred pair is an output of mass determination, not a cleaned version of either independent input.

Therefore there is no genuine third route. Either:

- the independent inputs remain unchanged and still require estimation; or
- a distinct latent compatible pair is jointly produced, which is precisely the estimation step internal to mass determination.

Hence:

\[
\boxed{
\text{reconciliation is constitutive of empirical mass determination.}
}
\]

---

## 11. The empirical mass operation

The empirical operation is not

\[
\mathrm{MeasuredForceVector}
\times
\mathrm{MeasuredAccelerationVector}
\to
\mathrm{PositiveMass}.
\]

A more adequate signature is:

\[
\operatorname{JointNewtonIIFit}:
\mathrm{MeasuredForceResult}
\times
\mathrm{MeasuredAccelerationResult}
\times
\mathrm{EstimationPolicy}
\to
\mathrm{JointNewtonIIFitResult}.
\]

A full joint result may contain:

```text
JointNewtonIIFitResult(
    underlying_force = F*,
    underlying_acceleration = a*,
    inertial_mass = m,
    uncertainty,
    corrections_or_residual,
    goodness_of_fit,
    estimation_policy,
    measurement_provenance
)
```

subject to

\[
\mathbf F^*=m\mathbf a^*,
\qquad
m>0.
\]

Under a Gaussian errors-in-variables policy, for example, the procedure may minimise uncertainty-weighted corrections to both measured vectors. Other policies are possible. The present argument does not select one universal estimator.

The essential operation is:

```text
receive two independent measurement results
    -> retain both results and their uncertainty/provenance
    -> apply a declared joint estimation policy
    -> estimate a latent codirectional pair
    -> recover the positive scalar relating that pair
    -> report the estimate together with its standing
```

---

## 12. Why the discrepancy should remain visible

The latent outputs satisfy

\[
\mathbf F^*=m\mathbf a^*
\]

by construction. If the procedure returns only the fitted mass, or only the compatible starred pair, it can appear to confirm the same relation it imposed.

The empirical content lies partly in the discrepancy between

\[
(\widetilde{\mathbf F},\widetilde{\mathbf a})
\]

and

\[
(\mathbf F^*,\mathbf a^*).
\]

A residual, correction record, likelihood, or goodness-of-fit value answers questions such as:

- how far each measurement had to move;
- whether those corrections were credible under the declared uncertainties;
- whether the disagreement was mainly directional or scalar;
- whether the target, frame, interval, calibration, or force account may be wrong;
- whether repeated trials support one common scalar mass.

This retention claim is an important consequence of the joint-measurement architecture. It is conceptually distinct from the narrower theorem that estimation is required. The latter can be established even before the exact output record is settled.

---

## 13. Consequence for the three triplet residuals

The triplet residuals are not equally simple operations.

### `Res_2`: inertial-acceleration corner

A provisional operational abstraction is

\[
\operatorname{Res}_2(\mathbf F,m)
=
\frac{1}{m}\mathbf F.
\]

Its input types discharge the main algebraic precondition.

### `Res_3`: net-force corner

A provisional operational abstraction is

\[
\operatorname{Res}_3(\mathbf a,m)
=
m\mathbf a.
\]

Its input types also discharge the main algebraic precondition.

### `Res_4`: inertial-mass corner

`Res_4` cannot be represented honestly as vector division.

It must at least distinguish:

```text
explicitly exact inputs
    -> checked exact recovery or a non-mass result

empirical measurement results
    -> joint estimation under a declared policy
```

The residual need not teach the mathematics of errors-in-variables regression any more than an acceleration entry must teach numerical differentiation. The detailed estimator may remain external mathematical competence.

But the mass residual must route the interpreter correctly. It must not cause either of these reactions:

```text
not exactly codirectional -> the object has no mass
```

or

```text
measured vectors -> divide their magnitudes automatically
```

The minimum honest empirical route is:

> **Jointly estimate two underlying codirectional vectors, then recover the positive scalar relating them.**

Whether the final entry carries this as one definiens, a compact residual plus an evaluator contract, or another arrangement remains an entry-writing question. The conceptual route itself cannot be removed.

---

## 14. Compact theorem

### Theorem — empirical inertial-mass determination requires estimation

Let one material object's net-force and inertial-acceleration be independently identifiable quantities in a common inertial-frame-qualified account. Suppose inertial mass is a positive scalar constrained by

\[
\mathbf F_{\mathrm{net}}=m\mathbf a.
\]

Then an empirical determination of `m` from force-side and acceleration-side measurement results cannot, in general, be a total algebraic quotient of the two reported vectors. It requires a joint estimation policy.

### Proof

1. `net-force` and `inertial-acceleration` are vectors, while `inertial-mass` is a positive scalar.
2. The ordinary vector types do not guarantee that a supplied pair satisfies

   \[
   \exists m>0:\mathbf F=m\mathbf a.
   \]

3. Therefore exact mass recovery is checked rather than total.
4. Force and acceleration must remain independently identifiable, because each is consumed as an input by another Newton-II triplet operation.
5. Independent empirical channels return measurement results with uncertainty, not exact law-conforming values.
6. Such results need not be exactly codirectional, and ordinary empirical work supplies no reason to expect exact conformity.
7. Newton II fixes the estimator only on the exact-law surface. It does not specify a unique extension away from that surface.
8. Any reconciliation that replaces the independent quantities before the triplet runs makes one or both quantities depend on the other and damages the operability of the other corners.
9. Therefore the independent measurement results must be retained while a joint policy estimates a separate latent compatible pair and the positive scalar relating it.

Hence empirical inertial mass must be estimated. \(\square\)

---

## 15. What this argument establishes

The argument establishes that:

1. the three Newton-II directions are not type-theoretically identical;
2. net-force and acceleration determination are total on their ordinary typed inputs;
3. exact inertial-mass recovery is checked;
4. vector division is not the mass operation;
5. exact codirectionality must be established before a magnitude quotient is used;
6. empirical force and acceleration results must remain distinct from jointly fitted latent values;
7. independently measured vectors do not automatically form an exact Newton-II pair;
8. Newton II does not uniquely determine how an off-law pair should be corrected;
9. an estimation policy is additional input;
10. reconciliation cannot be moved upstream while preserving the independent meanings required by the triplet;
11. estimation is therefore internal to empirical mass determination;
12. `Res_4` must route empirical inputs toward joint estimation rather than magnitude division or a no-mass conclusion.

---

## 16. What this argument does not yet establish

This draft deliberately does **not** assume the following stronger claims:

- that one particular statistical estimator is universally correct;
- that the estimator, rather than the exact Newton-II relation, is the metaphysical or final definition of inertial mass;
- that every null trial returns a meaningful positive point estimate;
- that a quantum lower bound on joint force/acceleration precision has been established;
- that the exact wording or final length of the inertial-mass triplet entry has been settled;
- that every field of a full joint-fit result must appear inside the triplet residual itself;
- that cross-trial persistence of the recovered scalar as a property of a material object has been proved here;
- that inertial mass has been identified with gravitational mass or material-amount mass.

These may be separate consequences or later arguments. They are not premises of the core proof.

---

## 17. Conclusion

The phrase “mass must be estimated” should not be understood as a generic reminder that experiments are noisy.

The necessity comes from the structure of Newton II itself.

The acceleration corner receives a vector and a positive scalar, so its operation is total. The net-force corner receives the same kinds of inputs in the opposite order, so its operation is total. The mass corner receives two vectors, and their ordinary types do not guarantee the positive-scalar relation required by the law.

Exact mass recovery must therefore check the relation before reading a scalar. Empirical determination goes further: force and acceleration must remain independently measured, their results do not generally lie exactly on the law, and the law does not specify a unique correction away from its exact surface. Attempting to reconcile the values before mass determination either leaves the problem untouched or contaminates the quantities required by the other two corners.

The only coherent route is:

```text
independent force measurement result
+ independent acceleration measurement result
+ declared estimation policy
    -> joint Newton-II-constrained latent pair
    -> positive scalar relating that pair
    -> inertial-mass estimate with stated standing
```

Therefore:

> **Empirical inertial mass is not obtained by dividing one measured vector by another. It is the positive scalar recovered through a joint estimate of the Newton-II-compatible relation between independently measured net-force and inertial-acceleration.**

---

## Source basis

This draft synthesises and refines the following project notes:

- `type_theoretic_analysis_newton_II_mass_recovery_d2.md`
- `vector_division_inertial_mass_measurement_d1.md`
- `why_reconciliation_cannot_be_upstream_of_E10.md`
- `why_the_mass_entry_cannot_be_short.md`
- `why_the_mass_entry_must_be_long_joint_measurement_d3.md`
- `NML2_1_CONTENT_d2.md`

The following note is treated as a stronger downstream proposal rather than as a premise of the core argument:

- `why_the_estimator_is_the_definition.md`