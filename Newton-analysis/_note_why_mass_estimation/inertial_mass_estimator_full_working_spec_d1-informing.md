> **Informing copy — do not edit here.**
> **Home:** the `mass_estimator` discussion — `Newton-analysis/_dscn_mass_estimator/inertial_mass_estimator_full_working_spec_d1.md`.
> Placed in `why_mass_estimation` because §34 is written straight at this note's subject: what the Newton-II mass entry must make the interpreter do. It supplies the fuller evaluator contract — weight the plausible underlying positive-codirectional pairs under the declared measurement policy; reject the Newton-II-constrained account if even the best pair is implausible; otherwise return the ratio of the mean compatible magnitudes with its reciprocal inverse-mass readout, uncertainty, residual, policy and provenance — alongside the shortest lesson-facing handoff, and it draws the line the entry need not cross (Gaussian integration, quadrature, goodness-of-fit calibration stay external competence). §32's settled/§33's policy split is the other reason it is here: it tells the next draft which requirements it may assert as forced and which are this estimator's choices. It was written partly from this workbench — its Source basis names all four drafts of this note. This is a read-only copy; refresh from home if the source changes.

---

# The Full Inertial-Mass Estimator

## A reciprocal-symmetric joint estimator with an absolute Newton-II compatibility test

**Status:** working synthesis, d1  
**Project:** VD Newton / inertial-mass estimation  
**Purpose:** collect the complete current estimator in one place: the exact branch, the empirical compatible-pair estimator, the rejection gate, reciprocal equivalence under `m` and `mu = 1/m`, the zero and non-codirectional cases, the preservation requirements, and the ways repeated trials make Newton II testable.

---

## 1. Thesis

Newton II relates one material object's true net force, true inertial acceleration, and positive inertial mass:

$$
\mathbf F^*=m\mathbf a^*,
\qquad m>0.
$$

Equivalently, with inverse mass

$$
\mu=\frac1m,
\qquad \mu>0,
$$

we may write

$$
\mathbf a^*=\mu\mathbf F^*,
$$

or

$$
\mathbf F^*=\frac1\mu\mathbf a^*.
$$

An empirical experiment does not normally supply the exact latent vectors $\mathbf F^*$ and $\mathbf a^*$. It supplies independent measurement results

$$
\widetilde{\mathbf F},
\qquad
\widetilde{\mathbf a},
$$

with uncertainty, provenance, and a declared measurement model.

The full mass-determination operation must therefore do two logically separate things:

1. **Estimate:** among Newton-II-compatible latent force–acceleration pairs, what positive scalar is supported by the measurements?
2. **Test compatibility:** is even the best Newton-II-compatible explanation plausible under the stated uncertainties?

The result is not always a mass number. It may instead be exact non-identification, exact contradiction, or empirical rejection.

The governing structure is:

```text
exact law-compatible inputs with unique identification
    -> return exact mass

exact law-compatible inputs without identification
    -> mass undefined from this trial

empirical measurements whose best Newton-II fit is plausible
    -> return an estimate with uncertainty and fit standing

empirical measurements whose best Newton-II fit is implausible
    -> REJECT the Newton-II-constrained account for the trial
```

The estimator described here is **not** the old positive stationary root, **not** a magnitude ratio applied to measured vectors, and **not** the posterior-median estimator. Its central readout is the ratio of the likelihood-weighted mean **positive latent magnitudes** over all plausible Newton-II-compatible pairs.

---

## 2. The operation is addressed

Before any estimation, all quantities must belong to the same Newton-II account:

```text
same material object
same relevant time or interval
same inertial-frame-qualified description
```

For material object `A`:

$$
\widetilde{\mathbf F}[A],
\qquad
\widetilde{\mathbf a}[A],
\qquad
m[A].
$$

A calculation can have correct arithmetic and units while still being invalid because it uses the force of one object, the acceleration of another, different intervals, or different frames.

The force and acceleration channels must also possess sufficiently independent provenance. If acceleration was calculated from the same force and an already assumed mass, then using that force and acceleration to “measure” the mass merely returns what was assumed. The same circularity occurs if the force was constructed from the demanded mass and acceleration.

The provenance test is:

```text
Did either input already depend on the demanded mass,
or on the other input through this same use of Newton II?
```

If yes, the operation may perform a consistency restatement, but it is not an independent empirical mass determination.

---

## 3. Exact and empirical inputs are different branches

The first branch condition is not whether the displayed vectors happen to align. It is whether the inputs are stipulated exact quantities or empirical measurement results.

```text
explicitly exact/supplied vectors
    -> checked exact recovery

empirical measurements with uncertainty
    -> joint estimation and compatibility testing
```

An empirical pair does not become exact merely because rounding makes the arrows appear codirectional.

---

# Part I — The exact branch

## 4. Exact compatibility set

For exact supplied vectors, define

$$
\mathcal C(\mathbf F,\mathbf a)
=
\{m>0:\mathbf F=m\mathbf a\}.
$$

Exactly three structures can occur.

### 4.1 One compatible mass

If $\mathbf F$ and $\mathbf a$ are both nonzero and codirectional, then

$$
\mathcal C(\mathbf F,\mathbf a)=\{m_0\},
$$

where

$$
\boxed{
 m_0=\frac{|\mathbf F|}{|\mathbf a|}
}.
$$

The direction relation is checked first. The magnitude quotient only reads the scalar after the vector relation has been established.

### 4.2 Every positive mass is compatible

If

$$
\mathbf F=\mathbf0,
\qquad
\mathbf a=\mathbf0,
$$

then

$$
\mathbf0=m\mathbf0
$$

for every $m>0$. Therefore

$$
\mathcal C(\mathbf0,\mathbf0)=(0,\infty).
$$

Newton II agrees with the trial, but the trial selects no mass:

$$
\boxed{
 m\text{ is undefined from this trial.}
}
$$

This is **agreement without identification**, not disagreement with Newton II.

### 4.3 No positive mass is compatible

If exactly one vector is zero, or the two nonzero vectors are not codirectional, then

$$
\mathcal C(\mathbf F,\mathbf a)=\varnothing.
$$

For exact stipulated inputs, the correct result is an exact contradiction:

```text
ExactNewtonIIContradiction
```

The estimator is not licensed to rewrite exact premises.

---

## 5. Exact result type

```text
ExactMassRecoveryResult :=
    ExactMass(m)
  | ExactMassNotIdentified
  | ExactNewtonIIContradiction
```

`ExactMassNotIdentified` and `ExactNewtonIIContradiction` are fundamentally different outputs.

---

# Part II — Why empirical determination needs a joint estimator

## 6. Measurements and latent quantities must remain distinct

The experiment produces measurement results such as

$$
(\widetilde{\mathbf F},\Sigma_F,P_F),
\qquad
(\widetilde{\mathbf a},\Sigma_a,P_a),
$$

where the covariance or uncertainty descriptions are represented schematically by $\Sigma_F$ and $\Sigma_a$, and the provenance records by $P_F$ and $P_a$.

The estimator then considers latent Newtonian quantities

$$
\mathbf F^*,
\qquad
\mathbf a^*,
$$

constrained by

$$
\mathbf F^*=m\mathbf a^*.
$$

The starred quantities are not what either independent measurement “really meant all along.” They are joint, model-constrained estimates produced from both channels.

The architecture is:

```text
force-side observations
    -> independent measured-force result

trajectory/acceleration-side observations
    -> independent measured-acceleration result

both independent results
    -> joint Newton-II-constrained latent-pair estimator
```

Reconciliation cannot be moved upstream by silently rewriting the measured force or measured acceleration. Doing so would make one quantity depend on the other and would damage the operability of the other two Newton-II corners.

---

## 7. Why the old best-point estimator is not the final mass readout

A standard errors-in-variables fit asks which single corrected latent pair lies closest to the measurements while obeying Newton II. Under independent Gaussian errors, a profile objective can be written as

$$
Q(m,\mathbf a^*)
=
(\widetilde{\mathbf F}-m\mathbf a^*)^T
\Sigma_F^{-1}
(\widetilde{\mathbf F}-m\mathbf a^*)
+
(\widetilde{\mathbf a}-\mathbf a^*)^T
\Sigma_a^{-1}
(\widetilde{\mathbf a}-\mathbf a^*).
$$

This is useful for finding the smallest possible discrepancy, but the positive stationary root is not automatically the mass estimate.

In the isotropic one-trial case, after minimizing over the latent acceleration,

$$
Q_{\mathrm{prof}}(m)
=
\frac{
 p^2+m^2q^2-2ms
}{
 \sigma_F^2+m^2\sigma_a^2
},
$$

where

$$
p=|\widetilde{\mathbf F}|,
\qquad
q=|\widetilde{\mathbf a}|,
\qquad
s=\widetilde{\mathbf F}\cdot\widetilde{\mathbf a}.
$$

For anti-aligned data, the positive stationary root can be a **maximum**, not a minimum. Boundary cases may have their best fit as $m\to0^+$ or $m\to\infty$. Therefore:

> The profile fit remains valuable for the absolute compatibility test, but its positive stationary root is not the general point estimator.

---

# Part III — The compatible-pair mean estimator

## 8. Parameter-free description of the compatible pairs

A Newton-II-compatible latent pair can be written using one common unit direction $\widehat{\mathbf u}$ and two nonnegative magnitudes:

$$
\mathbf F^*=f\widehat{\mathbf u},
\qquad
\mathbf a^*=\alpha\widehat{\mathbf u},
$$

with

$$
f\geq0,
\qquad
\alpha\geq0.
$$

Whenever $f>0$ and $\alpha>0$,

$$
m=\frac f\alpha,
\qquad
\mu=\frac\alpha f.
$$

This representation enforces positive codirectionality without choosing in advance whether mass or inverse mass is the preferred parameter.

The strict finite-mass relation occupies the interior $f>0$, $\alpha>0$. The boundary values $f=0$ or $\alpha=0$ are useful as limiting cases for compatibility testing. Under a continuous empirical uncertainty model they carry zero integration measure, but the best fit may approach them.

---

## 9. Measurement weight over compatible latent pairs

Combine the measured vectors into

$$
\mathbf y
=
\begin{bmatrix}
\widetilde{\mathbf F}\\
\widetilde{\mathbf a}
\end{bmatrix},
$$

and a candidate compatible latent pair into

$$
\mathbf x(f,\alpha,\widehat{\mathbf u})
=
\begin{bmatrix}
f\widehat{\mathbf u}\\
\alpha\widehat{\mathbf u}
\end{bmatrix}.
$$

Let $\Sigma$ be the full measurement covariance. It may be block diagonal when force and acceleration errors are independent, or may contain declared cross-correlations.

The uncertainty-normalized discrepancy is

$$
Q(f,\alpha,\widehat{\mathbf u})
=
(\mathbf y-\mathbf x)^T
\Sigma^{-1}
(\mathbf y-\mathbf x).
$$

For a Gaussian measurement policy, assign support weight

$$
w(f,\alpha,\widehat{\mathbf u})
\propto
\exp\!\left[-\frac12Q(f,\alpha,\widehat{\mathbf u})\right]
\rho_{\Pi}(f,\alpha,\widehat{\mathbf u}),
$$

where $\rho_{\Pi}$ is the declared latent-pair measure or experimental weighting supplied by policy $\Pi$.

The current interactive implementation uses the simplest policy:

```text
isotropic independent Gaussian uncertainties
uniform direction measure
flat measure over positive latent force and acceleration magnitudes
```

That policy is not dictated uniquely by Newton II. The uncertainty model, correlation structure, and latent-pair measure are additional estimator inputs and must be recorded.

Normalize the support:

$$
Z
=
\int w(f,\alpha,\widehat{\mathbf u})
\,df\,d\alpha\,d\Omega.
$$

---

## 10. The central readout

Compute the support-weighted mean **positive magnitudes**:

$$
\overline f
=
\frac1Z
\int
f\,w(f,\alpha,\widehat{\mathbf u})
\,df\,d\alpha\,d\Omega,
$$

$$
\overline\alpha
=
\frac1Z
\int
\alpha\,w(f,\alpha,\widehat{\mathbf u})
\,df\,d\alpha\,d\Omega.
$$

Then define

$$
\boxed{
\widehat m
=
\frac{\overline f}{\overline\alpha}
}
$$

and

$$
\boxed{
\widehat\mu
=
\frac{\overline\alpha}{\overline f}.
}
$$

Therefore

$$
\boxed{
\widehat\mu=\frac1{\widehat m}
}
$$

exactly, apart from numerical integration error.

This estimator does **not** calculate

$$
E\!\left[\frac f\alpha\right]
$$

and does not calculate the posterior mean of $m$. It calculates the ratio of the mean compatible magnitudes.

That distinction matters because the induced ratio $f/\alpha$ can possess a very long high-mass tail when $\alpha$ approaches zero. The mean of the ratio may fail to exist even though $\overline f$ and $\overline\alpha$ both exist. Under positive finite Gaussian uncertainties, the magnitude integrals have truncated-Gaussian tails, so their first moments are finite and positive.

---

## 11. Why the reciprocal form is a hard requirement

The two equations

$$
\mathbf F^*=m\mathbf a^*
$$

and

$$
\mathbf F^*=\frac1\mu\mathbf a^*,
\qquad \mu=\frac1m,
$$

describe the same physical compatible pairs. Choosing the symbol $m$ or $\mu$ must not alter the inference.

The estimator therefore has the following invariance rule:

```text
finite m estimate m_hat
    <-> finite inverse-mass estimate mu_hat = 1/m_hat

lower bound m > L
    <-> upper bound mu < 1/L

upper bound m < U
    <-> lower bound mu > 1/U

mass non-identification
    <-> inverse-mass non-identification

poor Newton-II compatibility
    <-> the same poor compatibility
```

The present compatible-pair mean estimator passes this test because it does not put an independent prior or averaging rule directly on either $m$ or $\mu$. Both are read from the same latent-pair support.

This also explains why independently choosing “uniform in $m$” and “uniform in $\mu$” would be unacceptable: those are different policies and can produce different inferences from the same experiment.

---

## 12. Uncertainty on the returned mass

A point estimate is not the full result.

Two suitable routes for uncertainty are:

1. **Induced-ratio quantiles.** Push the same normalized latent-pair support through

   $$
   m=\frac f\alpha
   $$

   and report quantiles or a highest-support interval. The mean of this ratio need not exist, but finite quantiles generally can.

2. **Measurement-model resampling.** Repeatedly simulate or bootstrap measurement results under the declared model, rerun the complete estimator, and report the sampling distribution of $\widehat m$.

Whichever route is used, the inverse-mass interval must be the reciprocal transformation of the mass interval. If

$$
 m\in[L,U],
$$

then

$$
 \mu\in\left[\frac1U,\frac1L\right].
$$

One must not construct unrelated intervals independently in the two parameterizations.

The output should also classify its standing, for example:

```text
strongly identified
weakly identified
boundary-dominated
apparatus-dominated
```

A finite point value can coexist with an extremely broad interval. The interval and standing say whether the number is mainly an object determination or mainly a statement about what the apparatus cannot resolve.

---

# Part IV — The absolute compatibility and rejection gate

## 13. Best possible Newton-II fit

The normalized compatible-pair weight can always be normalized when the measurement model has nonzero tails. That fact alone must not force the operation to report a mass.

First calculate the smallest discrepancy achievable by **any** positive-codirectional latent pair:

$$
\boxed{
Q_{\min}
=
\inf_{
 f\geq0,
 \alpha\geq0,
 \widehat{\mathbf u}
}
Q(f,\alpha,\widehat{\mathbf u}).
}
$$

This asks:

> Does any positive-mass Newton-II relation make the measurements plausibly compatible with the law under the stated uncertainty model?

Then compare $Q_{\min}$ with a declared acceptance threshold $Q_{\mathrm{crit}}$.

```text
Q_min <= Q_crit
    -> compatible enough to report the empirical mass estimate

Q_min > Q_crit
    -> REJECT the Newton-II-constrained account for this trial
```

The rejection gate dominates the mass readout. A conditional number may still be calculated internally for diagnostics, but it is not the returned mass once the model is rejected.

---

## 14. “Impossible” versus “statistically incompatible”

With hard bounded uncertainties, literal impossibility is possible. If the force and acceleration uncertainty regions do not intersect the Newton-II-compatible set, then no permitted latent pair exists.

With Gaussian uncertainties, every finite correction has nonzero tail probability. Therefore “impossible” is normally too strong. The correct statement is:

> The measurements are statistically incompatible with $\mathbf F=m\mathbf a$ beyond the declared threshold under the stated measurement model.

The threshold is part of policy. A production implementation should calibrate it for dimension, fitted degrees of freedom, boundary effects, and the desired false-rejection rate, often by simulation. The interactive playground's default $Q_{\mathrm{crit}}=9$ is a visible heuristic, not a universal theorem.

---

## 15. What rejection is evidence against

A failed fit initially places pressure on the complete experimental account:

```text
Newton II
+ measurement-error model
+ force accounting
+ inertial-frame commitment
+ object and interval addressing
+ calibration
+ same-object/mass-persistence assumptions where used
```

A rejection is not automatically proof that Newton II alone failed. The wrong object may have been addressed, the force account may be incomplete, the frame may be non-inertial, or an instrument may be miscalibrated.

But once those alternative premises are independently secured, persistent rejection is evidence against

$$
\mathbf F=m\mathbf a.
$$

The estimator therefore does not make Newton II unfalsifiable. It separates ordinary measurement disagreement from disagreement too large to be credibly attributed to the declared uncertainties.

---

# Part V — Behaviour on the important cases

## 16. Strong nonzero codirectional measurements

Suppose the measurements are strongly aligned and precise:

$$
\widetilde{\mathbf F}\approx50\widehat{\mathbf u},
\qquad
\widetilde{\mathbf a}\approx10\widehat{\mathbf u}.
$$

Then the compatible-pair support is concentrated near

$$
f\approx50,
\qquad
\alpha\approx10,
$$

so

$$
\widehat m\approx5.
$$

As uncertainty shrinks, the estimator approaches the exact Newton-II magnitude ratio.

---

## 17. Measured force zero, acceleration nonzero

Take

$$
\widetilde F=0,
\qquad
\widetilde a=10,
$$

with nonzero force uncertainty.

The reading $\widetilde F=0$ does not assert that the latent force is exactly zero. It says that the instrument did not resolve a force away from zero. The compatible-pair support therefore contains small positive force magnitudes aligned with the clearly nonzero acceleration.

Thus

$$
\overline f>0,
\qquad
\overline\alpha\approx10,
$$

and

$$
\boxed{
\widehat m>0\text{ and small.}
}
$$

In the simplest one-dimensional limiting picture, if the acceleration is effectively exact and the force reading is $0\pm\sigma_F$, the positive latent force has a half-normal mean:

$$
\overline f
=
\sigma_F\sqrt{\frac2\pi}.
$$

Then

$$
\boxed{
\widehat m
\approx
\frac{\sigma_F}{10}
\sqrt{\frac2\pi}.
}
$$

This captures the intended interpretation:

> There is appreciable acceleration, while the required force is small enough to lie near or below the force instrument's resolution; therefore the supported mass is small.

With an unrestricted domain $m>0$ and a continuous nonzero uncertainty model, this free-mass trial can approach an exact fit as $m\to0^+$, so its single-trial free-mass score need not reject. Rejection becomes possible if the inputs are exact, a previously established mass or mass range excludes the small-mass regime, hard bounds exclude the required latent force, or repeated trials fail to support one common mass.

---

## 18. Measured force nonzero, acceleration zero

Take

$$
\widetilde F=50,
\qquad
\widetilde a=0,
$$

with nonzero acceleration uncertainty.

The zero acceleration reading permits small positive latent accelerations below or near the acceleration instrument's resolution. Therefore

$$
\overline f\approx50,
\qquad
\overline\alpha>0\text{ but small},
$$

so

$$
\boxed{
\widehat m\text{ is finite and large.}
}
$$

In the corresponding one-dimensional limiting picture,

$$
\overline\alpha
=
\sigma_a\sqrt{\frac2\pi},
$$

and therefore

$$
\boxed{
\widehat m
\approx
\frac{50}{\sigma_a\sqrt{2/\pi}}.
}
$$

This does not mean the experiment determined the mass sharply. The upper tail may be very broad. The result may be mainly a lower-bound or “heavy relative to this apparatus” statement.

With an unrestricted domain $m>0$ and a continuous nonzero uncertainty model, this free-mass trial can approach an exact fit as $m\to\infty$, so its single-trial free-mass score need not reject. Rejection becomes possible if the inputs are exact, a previously established mass or mass range excludes the high-mass regime, hard bounds exclude the required latent acceleration, or repeated trials fail to support one common mass.

---

## 19. Other non-codirectional measured vectors

Non-codirectionality of the displayed central values does not by itself decide the result.

The estimator considers all common directions and asks which latent codirectional pairs are supported by the two uncertainty models.

```text
small directional disagreement relative to uncertainty
    -> finite mass estimate, often well supported

large directional disagreement but large uncertainty
    -> finite but broad estimate may remain possible

large directional disagreement relative to tight uncertainty
    -> rejection
```

Thus an acute angle, a right angle, or even an obtuse angle is not by itself a hard empirical branch. The absolute compatibility score decides whether the required corrections are credible.

---

## 20. The anti-aligned stress test

Consider the playground example

$$
\widetilde{\mathbf F}=(-10,0),
\qquad
\widetilde{\mathbf a}=(10,0),
$$

with

$$
\sigma_F=\sigma_a=2.
$$

The measured vectors point in exactly opposite directions. A positive-mass Newton-II pair must point in one common direction.

The cheapest reconciliation is to preserve one channel and move the other to the zero boundary. Either move costs five standard deviations:

$$
Q_{\min}
=
\left(\frac{10}{2}\right)^2
=25.
$$

With the playground threshold

$$
Q_{\mathrm{crit}}=9,
$$

we have

$$
25>9,
$$

so the result is

$$
\boxed{
\text{REJECT.}
}
$$

A normalized compatible-pair calculation may, by symmetry, internally produce a conditional central value near $1\,\mathrm{kg}$. That number is not the mass result. It is what the conditional averaging rule says **after forcing the rejected model to be true**. The rejection gate suppresses it.

This case demonstrates why a normalized distribution or average over compatible states cannot replace the absolute goodness-of-fit test.

---

## 21. Measured zero-zero versus exact zero-zero

These cases must remain separate.

### Exact zero-zero

If the inputs are explicitly exact,

$$
\mathbf F=\mathbf0,
\qquad
\mathbf a=\mathbf0,
$$

then every $m>0$ fits and the trial does not identify mass:

```text
ExactMassNotIdentified
```

### Empirical zero-zero with nonzero uncertainties

If the instrument outputs are

$$
\widetilde{\mathbf F}=\mathbf0,
\qquad
\widetilde{\mathbf a}=\mathbf0,
$$

but $\Sigma_F$ and $\Sigma_a$ are nonzero, the empirical compatible-pair support includes neighboring positive latent magnitudes. Under the symmetric isotropic policy used by the current playground,

$$
\overline f\propto\sigma_F,
\qquad
\overline\alpha\propto\sigma_a,
$$

so approximately

$$
\widehat m
\sim
\frac{\sigma_F}{\sigma_a}.
$$

This is an apparatus-dominated, low-information readout and should be labelled as such. It is not the exact-law conclusion and does not show that the object's mass equals the apparatus scale.

The disagreement rule alone does not require this stronger zero-zero inference, because the central values already agree with Newton II. It is a consequence of running the full empirical compatible-pair integration on all measurement results. The exact zero-zero boundary remains non-identifying.

---

# Part VI — Why the median estimator is no longer the core operation

## 22. What the posterior-median proposal added

The earlier median proposal integrated support over latent states, introduced an excitation model and a prior over positive mass, constructed a distribution $p(m\mid\text{data})$, and returned its median.

That proposal correctly exposed several facts:

- one best latent point does not exhaust the available uncertainty information;
- zero readings may still carry model-dependent information;
- nonzero force with unresolved acceleration favours large mass;
- nonzero acceleration with unresolved force favours small mass;
- anti-aligned measurements should produce a compatibility warning rather than a negative mass;
- several trials should share one mass.

Those insights survive.

---

## 23. Why the median is not needed for the present estimator

The compatible-pair mean estimator already gives finite positive readouts for measured

$$
\widetilde F=0,\ \widetilde a\neq0
$$

and

$$
\widetilde F\neq0,\ \widetilde a=0
$$

without taking a posterior median over mass.

The median proposal also requires stronger additional inputs:

```text
experimental excitation or latent-state model
mass prior or permitted mass range
choice of parameterization for that prior
```

Low-information results can depend strongly on those choices.

Most importantly, any normalized mass distribution can still be manufactured even when **every** mass fits badly in absolute terms. Therefore a posterior median cannot replace the rejection gate.

The current estimator instead:

```text
integrates over compatible latent force and acceleration magnitudes
uses their mean magnitudes for the reciprocal-safe point readout
uses an independent absolute compatibility test
```

A richer Bayesian or excitation-model analysis may still be added downstream, but it is no longer the core estimator and must inherit the same rejection and reciprocal-invariance requirements.

---

# Part VII — How Newton II remains falsifiable

## 24. Why a weak first experiment need not falsify anything

If the object's mass is unknown and a trial contains low-confidence information, the estimator may return

```text
a mass estimate with a very wide interval
```

rather than a rejection.

That does not make Newton II unfalsifiable. It means the experiment had too little information to test the relation strongly. A theory is not required to be sharply tested by an apparatus that cannot resolve the relevant quantities.

There are three distinct testing levels.

---

## 25. Level 1 — Can any mass fit this single trial?

Define the free-mass compatibility score

$$
Q_{\min}
=
\inf_{m>0}
Q_{\min}(m),
$$

where $Q_{\min}(m)$ is the smallest discrepancy at fixed candidate mass.

If even the best mass gives an implausible score, reject the Newton-II-constrained account for that trial.

This is the anti-aligned stress-test route.

---

## 26. Level 2 — Does a previously known mass fit this trial?

Suppose a prior independent experiment has established

$$
m=m_0
$$

with small uncertainty.

The new trial must not be allowed to choose an unrelated mass merely because another value would reconcile its force and acceleration. Instead evaluate the fixed-mass score

$$
\boxed{
Q_{\min}(m_0)
=
\inf_{\mathbf a^*}
Q(m_0,\mathbf a^*)
}
$$

or the equivalent $\mu_0=1/m_0$ form.

If the known mass lies outside the regime supported by the new measurement, then the new trial conflicts with

```text
Newton II
+ the established mass
+ the other experimental premises
```

This is a stronger test than freely estimating mass from scratch.

---

## 27. Level 3 — Does one common mass fit repeated trials?

For repeated independent trials $i=1,\ldots,N$ on the same material object, Newton II requires one common mass:

$$
\mathbf F_i^*=m\mathbf a_i^*.
$$

Each trial has a fixed-mass profile score $Q_i(m)$. The common-mass score is

$$
\boxed{
Q_{\mathrm{joint}}(m)
=
\sum_{i=1}^N Q_i(m).
}
$$

Then ask whether

$$
\min_{m>0}Q_{\mathrm{joint}}(m)
$$

is plausible.

Two trials may each fit Newton II beautifully with their own independently chosen masses while no **single** mass fits both. In that case the joint Newton-II/common-mass account fails.

Example:

```text
Trial 1:  m = 5.00 +/- 0.05 kg
Trial 2:  m = 8.00 +/- 0.05 kg
```

Each trial may possess a good latent codirectional pair, but the same material object cannot simultaneously possess both masses under the unchanged-mass account.

This is the central falsifiability point:

> Estimating a free mass from one trial mainly determines the parameter. Holding that mass fixed across independent trials tests Newton II.

---

## 28. Same-object and mass-reuse licence

Cross-trial incompatibility is evidential only if the same material object and the same mass binding persist.

Events such as

```text
splitting
merging
material loss or gain
continuous leakage or ejection
loss of target identity
```

can suspend the licence to reuse the earlier mass. If such an event occurred, a changed estimate need not be evidence against Newton II; the object or its mass address may have changed.

Therefore repeated-trial falsifiability depends on the material-object and mass-persistence account being secured rather than silently assumed.

---

# Part VIII — Required output and trace

## 29. The estimator is not a function into bare positive mass

The correct type is not

$$
\mathrm{MeasuredForceVector}
\times
\mathrm{MeasuredAccelerationVector}
\to
\mathrm{PositiveMass}.
$$

A fuller signature is

$$
\operatorname{MassFromForceAcceleration}:
\mathrm{ForceAccelerationInput}
\times
\mathrm{EstimationPolicy}
\to
\mathrm{MassDeterminationResult}.
$$

A suitable result type is:

```text
MassDeterminationResult :=
    ExactMass(
        m
    )

  | ExactMassNotIdentified(
        reason = zero-zero agreement
    )

  | ExactNewtonIIContradiction(
        supplied_force,
        supplied_acceleration,
        reason
    )

  | EmpiricalMassEstimate(
        m_hat,
        mu_hat,
        reciprocal_check,
        mass_interval,
        inverse_mass_interval,
        latent_mean_force_magnitude,
        latent_mean_acceleration_magnitude,
        compatible_support_summary,
        Q_min,
        compatibility_threshold,
        identification_standing,
        original_measurements,
        uncertainty_model,
        estimation_policy,
        provenance
    )

  | PoorModelCompatibility(
        Q_min,
        compatibility_threshold,
        best_available_correction,
        original_measurements,
        uncertainty_model,
        estimation_policy,
        provenance,
        possible_failed_premises
    )

  | EstimationRequired(
        reason = empirical inputs but no policy supplied
    )

  | InvalidInput(
        reason
    )
```

---

## 30. Why the discrepancy must survive

The latent outputs satisfy Newton II by construction. If the operation returns only the fitted mass or only the compatible latent pair, it can appear to confirm the very relation it imposed.

The empirical content lies partly in the discrepancy between

$$
(\widetilde{\mathbf F},\widetilde{\mathbf a})
$$

and the supported latent compatible states.

The result must therefore retain enough information to answer:

- how far the measured force had to move;
- how far the measured acceleration had to move;
- whether those corrections were credible under the stated uncertainties;
- whether disagreement was mainly directional or scalar;
- whether the fit is strongly or weakly identifying;
- whether a previously known mass lies inside the supported regime;
- whether repeated trials support one common mass;
- whether target, interval, frame, force account, calibration, or provenance may have failed.

The estimator should not install Newton II and then report the installed agreement as evidence. The residual and goodness of fit keep the law answerable to the measurements.

---

## 31. Full operational trace

```text
DEMAND:
    inertial-mass(A)

ADDRESS AUDIT:
    same material object?
    same interval/time?
    same inertial frame?
    independent enough provenance?

INPUT BRANCH:
    explicitly exact/supplied
        -> exact compatibility set
        -> ExactMass
           or ExactMassNotIdentified
           or ExactNewtonIIContradiction

    empirical measurements
        -> require uncertainty model and estimation policy
        -> preserve original measured force and acceleration
        -> construct Newton-II-compatible latent-pair support
        -> calculate absolute best-fit Q_min

COMPATIBILITY GATE:
    Q_min > Q_crit
        -> PoorModelCompatibility
        -> do not return the conditional mass as the answer

    Q_min <= Q_crit
        -> integrate compatible latent magnitudes
        -> compute mean latent force magnitude f_bar
        -> compute mean latent acceleration magnitude alpha_bar
        -> m_hat = f_bar / alpha_bar
        -> mu_hat = alpha_bar / f_bar
        -> verify mu_hat = 1/m_hat
        -> construct reciprocal uncertainty intervals
        -> classify identification standing
        -> retain residual, policy, uncertainty, and provenance
        -> EmpiricalMassEstimate

OPTIONAL TESTS:
    known mass available?
        -> evaluate fixed-mass compatibility

    repeated trials on same unchanged object?
        -> require one common mass
        -> evaluate joint compatibility
```

---

# Part IX — What is settled and what remains policy

## 32. Settled structural requirements

The following are now part of the estimator's required structure:

1. Force and acceleration are independently produced empirical inputs, not already reconciled values.
2. Exact and empirical inputs take different branches.
3. Exact nonzero codirectional values permit checked magnitude-ratio recovery.
4. Exact zero-zero agrees with Newton II but does not identify mass.
5. Exact one-zero or non-codirectional values contradict positive-mass Newton II.
6. Empirical disagreement invokes joint latent-pair estimation rather than vector division or “no mass.”
7. The estimator integrates over plausible positive-codirectional latent pairs rather than selecting the old positive stationary root.
8. The point readout is the ratio of mean compatible magnitudes, not the mean or median of the mass ratio.
9. The $m$ and $\mu=1/m$ implementations must be reciprocal relabellings of one inference.
10. Absolute model compatibility is tested separately from relative preference among masses.
11. Rejection suppresses the conditional mass readout.
12. Zero central readings with nonzero uncertainty can support finite small or large estimates.
13. Non-codirectional empirical readings may yield an estimate or rejection depending on their uncertainties.
14. Original measurements, uncertainty, residual, policy, and provenance remain in the result.
15. A known mass and a common mass across repeated trials provide stronger falsifiability tests than one free-mass fit.

---

## 33. Remaining estimator-policy choices

Newton II does not by itself settle every numerical detail. A production implementation still needs declared choices for:

- the force and acceleration uncertainty distributions;
- anisotropy and cross-correlation;
- the latent-pair measure $\rho_\Pi$;
- treatment of hard physical bounds;
- calibration of $Q_{\mathrm{crit}}$ or the model-checking significance level;
- the uncertainty-interval construction;
- numerical integration accuracy;
- common-mass multi-trial integration where a full support distribution, rather than only a joint profile test, is desired;
- criteria for labels such as `weakly identified`, `boundary-dominated`, or `apparatus-dominated`.

These are not defects hidden from the operation. They are explicit policy inputs whose values and provenance must be retained.

---

## 34. Consequence for the VD mass entry

The Newton-II inertial-mass entry need not teach Gaussian integration, covariance matrices, numerical quadrature, bootstrap intervals, or goodness-of-fit calibration. Those remain external mathematical and metrological competence.

But the entry must trigger the correct route. At minimum, it must cause the interpreter to distinguish:

```text
exact supplied pair
    -> checked exact recovery or exact non-mass result

empirical measurement results
    -> declared joint estimation
    -> absolute compatibility test
    -> mass estimate or rejection
```

The shortest honest lesson-facing handoff remains:

> **Jointly estimate underlying codirectional force and acceleration values, then recover the positive scalar relating them.**

The fuller evaluator contract is now:

> **Weight the plausible underlying positive-codirectional force–acceleration pairs under the declared measurement policy; reject the Newton-II-constrained account if even the best pair is implausible; otherwise return the ratio of the mean compatible magnitudes, together with its reciprocal inverse-mass readout, uncertainty, residual, policy, and provenance.**

---

## 35. Main conclusion

The complete estimator is not merely a rule for turning two noisy vectors into a positive number.

It is a routed empirical operation that:

1. preserves independently measured force and acceleration;
2. represents possible latent Newton-II-compatible states by a common direction and positive magnitudes;
3. weights those states by the declared uncertainty model;
4. separately checks whether the Newton-II model fits at all;
5. rejects when even the best reconciliation is implausible;
6. otherwise reads

   $$
   \widehat m=\frac{\overline f}{\overline\alpha};
   $$

7. returns

   $$
   \widehat\mu=\frac1{\widehat m}
   $$

   from the same calculation;
8. reports uncertainty and whether the result is object-dominated or apparatus-dominated;
9. preserves the discrepancy by which Newton II remains answerable to the evidence;
10. permits stronger falsification when a known or common mass fails in later independent trials.

The central governing rule is therefore:

$$
\boxed{
\begin{array}{ll}
\text{exact agreement and unique identification}
    &\to \text{exact mass},\\[2mm]
\text{exact agreement without identification}
    &\to \text{mass undefined from the trial},\\[2mm]
\text{empirical measurements with a plausible best fit}
    &\to \text{reciprocal-symmetric mass estimate},\\[2mm]
\text{empirical measurements with an implausible best fit}
    &\to \text{reject the Newton-II-constrained account}.
\end{array}
}
$$

---

## Source basis and relation to earlier notes

This synthesis draws together and updates the live arguments contained in:

- `why_inertial_mass_must_be_estimated.md`
- `why_mass_must_be_estimated_introduction_d2.md`
- `why_reconciliation_cannot_be_upstream_of_E10.md`
- `why_the_mass_entry_must_be_long_joint_measurement_d3.md`
- `disagreement_rule_mass_estimator_trace.md`
- `median_based_estimator_inertial_mass.md`
- `why_the_estimator_is_the_definition.md`
- `NML2_1_CONTENT_d2.md`

The compatible-pair mean readout, reciprocal-equivalence requirement, rejection-gate dominance, anti-aligned stress test, and fixed/common-mass falsifiability analysis are the new synthesis produced by the present estimator review.
