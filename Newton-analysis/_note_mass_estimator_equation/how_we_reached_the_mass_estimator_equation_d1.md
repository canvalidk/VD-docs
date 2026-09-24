# How we reached the mass estimator equation

**Note:** `_note_mass_estimator_equation`, draft d1, 2026-09-23. Written by
Claude at the user's request, from the story laid out in conversation that day.

**What this is.** The story of how the estimator was reached, told once and in
order: from "m = F/a is not an operation" to the equation specified on
21 September. Each step says which of our records it comes from. Wherever a
step borrows from the literature, it says exactly what is taken and where it
sits in the paper. Every paper cited was read against the claim on 2026-09-23;
the few that were not are marked. The papers are in
`../_dscn_mass_estimator/papers/`.

**What this is not.** It is not a literature review, and it does not argue
priority. It also leaves out the parameter findings of 2026-09-23 (the fitted
prior tilt λ, the reduction of the default weighting to a single exponent,
switch rules and the update rule). Those come after the equation, and are
recorded in `mass_estimator_regimes_priors_and_updating_2026-09-23.md`.

**Direction.** Not yet ruled by the user.

---

## 1. The problem: $m=\mathbf F/\mathbf a$ is not an operation

Newton II, $\mathbf F=m\mathbf a$ with $m>0$, gives two well-defined
operations: multiply a vector by a positive scalar, or divide a vector by one.
The third rearrangement, $m=\mathbf F/\mathbf a$, asks us to divide one vector
by another. That operation does not exist.

Every familiar repair fails once real measurements are used:

- **Divide the magnitudes.** $\widetilde{\mathbf F}=(10,0)\,\mathrm N$ and
  $\widetilde{\mathbf a}=(0,5)\,\mathrm{m\,s^{-2}}$ give
  $|\widetilde{\mathbf F}|/|\widetilde{\mathbf a}|=2\,\mathrm{kg}$. But no
  scalar turns $(0,5)$ into $(10,0)$, so the number does not satisfy the law it
  was read from.
- **Use dot products.** Dotting with $\mathbf a$ gives
  $m_a=\mathbf F\cdot\mathbf a/\mathbf a\cdot\mathbf a$; dotting with
  $\mathbf F$ gives $m_F=\mathbf F\cdot\mathbf F/\mathbf F\cdot\mathbf a$. For
  $(2,1)\,\mathrm N$ and $(1,0)\,\mathrm{m\,s^{-2}}$ these give $2\,\mathrm{kg}$
  and $2.5\,\mathrm{kg}$, and the magnitude quotient gives $\sqrt5\,\mathrm{kg}$.
  Newton II does not say which vector to dot with. At a right angle one formula
  returns zero and the other divides by zero; past a right angle both are
  negative.
- **Measured zeros.** If both readings are zero, every positive mass satisfies
  $\mathbf 0=m\mathbf 0$. The quotient asks for $0/0$.

The general form of the difficulty (`vector_division_inertial_mass_measurement_d1.md`
§3): any rotation-invariant rule built from the two measured vectors (and reflection-invariant, in two dimensions) has the form

$$
\widehat m=\frac{|\widetilde{\mathbf F}|}{|\widetilde{\mathbf a}|}\,g(\cos\theta),
$$

and the exact law fixes only $g(1)=1$. Away from perfect alignment, choosing $g$
means choosing which errors are more plausible. So the question is a
measurement question: what determines mass from the force and acceleration
evidence we can actually supply?

*Records:* `../_note_why_mass_estimation/mass_estimation_introduction_candidate_2026-09-06.md`
(the working introduction, revised 6 September, no draft number assigned; §§1–5, where the examples come from);
`vector_division_inertial_mass_measurement_d1.md` (26 July, §§2–3).

## 2. First answer: fit the nearest compatible pair

The standard move is errors-in-variables fitting. Assume both readings are
wrong. Introduce unknown true vectors that satisfy the law exactly,
$\mathbf F^*=m\mathbf a^*$. Choose the mass whose true pair needs the smallest
correction, each correction measured in units of its own uncertainty.

For one trial with isotropic errors, minimising over the latent acceleration
leaves a profile in $m$ (spec d1 §7):

$$
Q_{\rm prof}(m)=\frac{p^2+m^2q^2-2ms}{\sigma_F^2+m^2\sigma_a^2},
\qquad p=|\widetilde{\mathbf F}|,\ q=|\widetilde{\mathbf a}|,\ s=\widetilde{\mathbf F}\cdot\widetilde{\mathbf a}.
$$

Its stationary points solve a quadratic, which is the Deming slope for a line
through the origin (`why_the_estimator_is_the_definition.md` §2, 1 August).

**What we take from the literature.**

- *Golub & Van Loan (1980)* define total least squares as the smallest
  perturbation of the data that makes the system consistent (p. 2, eq. 1.4),
  "a nearest compatible" problem solved through the SVD (§2). For a single
  unknown with unit weights, it minimises perpendicular distance to a line
  through the origin (p. 7, Fig. 1). Our "nearest compatible pair" is this
  problem with the columns weighted by $1/\sigma_a$ and $1/\sigma_F$. Correlated
  noise goes beyond their diagonal weights. They also list where the fit breaks (pp. 5, 7): no solution when
  the line would be vertical, and no unique solution when singular values tie.
  In our variables (our translation), exactly orthogonal weighted readings give
  no solution ($m=\infty$) when the weighted force is the larger, $m=0$ when the
  weighted acceleration is, and no unique answer when they are equal.
- *Bartel, Stoudt & Possolo (2016)* propose exactly this kind of fit for force
  metrology. They fit the transducer response and the latent true applied
  forces together, instead of the ordinary least squares then in use, with
  Monte Carlo uncertainty (Metrologia 53, 965–980; model p. 7, eq. 3 p. 11).
  They are an example of this first stage, not of the next one.
- `vector_division_inertial_mass_measurement_d1.md` also cites York et al.
  (2004) and Boggs & Rogers (ODR) for this framework. Those two were not re-read for this draft.

**Why it was not the answer.**

- **The chosen root.** The quadratic has one positive and one negative root.
  The minimum of the fit is the root with the sign of
  $\widetilde{\mathbf F}\cdot\widetilde{\mathbf a}$. The same root rule is
  Lindley & El-Sayyad's for their posterior mode (eqs. 19–20, p. 196), which they
  identify with the maximum-likelihood fit (p. 197). With anti-aligned readings the best-fitting mass is negative, and
  the positive root is a *maximum* of the profile; restricted to positive
  masses, the best fit runs off to $m\to0$ or $m\to\infty$ (spec d1 §7). Our
  1 August record used the positive root. The 2 September audit found that on
  null trials that root is the profile maximum about half the time
  (`what_forces_the_chain_to_the_estimator.md`).
- **Measured zeros.** At $\widetilde{\mathbf F}=\widetilde{\mathbf a}=\mathbf0$,
  every positive mass has a perfect fit ($Q_{\min}(m)=0$ for all $m$). The fit
  cannot tell a mass supported by a large region of plausible true pairs from
  one supported by a sliver (`median_based_estimator_inertial_mass.md` §2).

## 3. Second answer: integrate over all compatible pairs

The 27 August record changed the question. Instead of asking which mass allows
the single best corrected pair, ask how much total support the measurement
model gives each mass. Integrate the Gaussian likelihood over every true pair
compatible with that mass, turn the result into a distribution over positive
mass, and report its median.

**What we take from the literature.** This is the Bayesian errors-in-variables
move:

- *Lindley & El-Sayyad (1968)*: a line through the origin, $\eta=\theta\xi$,
  with both coordinates observed with error. They show that joint maximum likelihood
  over the true values *and both unknown error variances* fails (p. 191); with
  the variance ratio known, which is our case, their posterior mode coincides
  with the usual fit (pp. 196–197). They "eliminate the incidental parameters"
  by integrating the true values out (p. 192, eq. 7).
- *Gull (1989)*: straight-line fitting with errors in both coordinates. He
  integrates the unknown true values out of the posterior analytically
  (pp. 511, 513–514).
- Both papers say that the prior on the true values decides the answer. Gull
  finds that a flat prior on them biases the slope (abstract; p. 516).
  Lindley & El-Sayyad report that a uniform prior on the true values gave
  asymmetric, and in one case inconsistent, results (p. 201). We meet the same
  issue in §7.

**What the median proposal itself admitted.** A median needs a full
distribution over mass, and so needs more than the readings and their
uncertainties: a model of which true accelerations and forces were plausible
(an excitation model), and a prior or permitted range for the mass. Uniform in
$m$ and uniform in $\log m$ are different assumptions (median record §§17–18).

**The rule the estimator had to obey.** The 29 August disagreement rule
separated two failures that $m=\text{undefined}$ used to hide:

- **No positive mass fits** (for example $F/0$, or anti-aligned readings):
  disagreement with Newton II. On measured data the estimator must repair it.
- **Every positive mass fits** (exact $0/0$): agreement without identification.
  The estimator must not manufacture a mass here.

*Records:* `median_based_estimator_inertial_mass.md` (27 August);
`disagreement_rule_mass_estimator_trace.md` (29 August).

## 4. Third answer: average, then divide

The 30 August working specification kept the integration but changed the
readout. Weight every compatible latent pair $(f\widehat{\mathbf u},\alpha\widehat{\mathbf u})$,
with $f,\alpha>0$ and a common direction $\widehat{\mathbf u}$, by

$$
w\propto e^{-Q/2}\,\rho,\qquad
Q=(\mathbf y-\mathbf x)^T\Sigma^{-1}(\mathbf y-\mathbf x),
$$

where $\rho$ is a declared measure: flat in the two magnitudes and uniform in
direction. Then average each magnitude and divide:

$$
\widehat m=\frac{\overline f}{\overline\alpha}.
$$

It is not the mean of $f/\alpha$, which is infinite (§5), and not the median.
The specification also said plainly that its policy, meaning the Gaussian
model, the correlations and the measure, is "not dictated uniquely by Newton
II" (spec d1 §9).

**Why average-then-divide, and not the median.** The specification's own
reason (§11, reciprocal invariance: using $m$ or $\mu=1/m$ gives the same
answer) turned out to select nothing. The median of the induced mass, every
quantile, the geometric mean and the old profile root are all reciprocal
invariant (`what_forces_the_ratio_of_means_readout.md`, 2 September, §2). What
does select it is composition:

- **(L) Lumping.** Glue two bodies together so they share an acceleration; the
  forces add, so the masses add. The readout must be linear on the force side.
- **(R) Common force.** Let one force act on two bodies, as the two members of
  an interaction pair do; the accelerations add, so the inverse masses add
  (the reduced mass). The readout must be linear on the acceleration side.

Each law kills what the other lets through. Lumping alone admits every readout
$E[f\,\varphi(\alpha)]/E[\alpha\,\varphi(\alpha)]$, including least squares of
$F$ on $a$. The common-force law alone admits the mirror family. Only
$E[f]/E[\alpha]$ satisfies both (2 September). The 6 September record proves
it as a theorem: for any readout determined by the joint law of the positive
magnitudes, force composition (C1), inverse-mass composition (C2), dependence
only on that magnitude law (C3), exactness on point masses (C4) and a
continuity condition (C5) force $R=E[f]/E[\alpha]$
(`mass_readout_composition_uniqueness_2026-09-06.md`).

**What this rests on.** Two premises, and they are ours, not statistics':

- *The estimator is the definition.* On measured data, the estimator is what
  "mass" means, so it must compose as mass composes elsewhere in the
  dictionary. Otherwise the mass entry and the lumping entry define different
  words (`why_the_estimator_is_the_definition.md`; 2 September, "On the
  premise"). A statistician can reply that the estimate of a sum need not be
  the sum of the estimates. Under the natural symmetric loss
  $(\log\widehat m-\log m)^2$ the best readout is the geometric mean, which
  fails both composition laws. Composition is the only argument that
  separates the candidates.
- *Inverse mass adds under a common force.* The records take this, like
  lumping, as a commitment the dictionary already makes at other entries
  (2 September: "its inverse adds under common force"; the chain audit's S10).
  It fits the 7 September steering that force and acceleration are to be
  treated symmetrically as sources of information. In the 23 September
  conversation the same premise was put as "$1/m$ has the same standing as
  $m$".

The definition premise is not independent of the weighting either. The
2 September chain audit found that the 1 August argument survives only with
the current estimator, and then rests on the flat latent measure, which §7
shows is a declared choice (`what_forces_the_chain_to_the_estimator.md` §5).

The theorem's own premises also matter: C3 (a readout using direction or
residual information would fall outside it) and its domain (all joint laws of
strictly positive magnitudes with finite means, which is broader than the
Gaussian posteriors actually used).

**What we take from the literature.**

- *The point is a biased mean.* $\widehat m=E_P[\alpha M]/E_P[\alpha]$ with
  $M=f/\alpha$. In the terms of Arratia, Goldstein & Kochman, $\widehat m$ is
  the mean of $M$ under the joint law biased by its coordinate $\alpha$,
  $dP^{(\alpha)}/dP=\alpha/E_P[\alpha]$ (§2.3, eqs. 19–21). Under that law the
  $\alpha$-marginal is the size-biased law of $\alpha$. The weight $\alpha$ is
  exactly what cancels the $1/\alpha$ that makes $E[M]$ infinite; pairs in which
  the object barely accelerates count for little.
- *The known-direction case is two Katz estimates.* If the direction is known
  exactly and the force and acceleration errors are independent, the channels
  separate. Under a flat weight on $f>0$ and a Gaussian
  reading $x_F$, the posterior mean is
  $x_F+\sigma_F\,\phi(x_F/\sigma_F)/\Phi(x_F/\sigma_F)$, and similarly for
  $\alpha$. Katz (1961) gives this estimator for a unit-variance normal mean
  known to be non-negative, $x+\phi(x)/\Phi(x)$ (p. 139). He obtains it as the
  limit of Bayes rules under exponential priors of growing scale (p. 137) and
  proves it admissible (Theorem 1, p. 138) and minimax (p. 139) under squared
  error, and always positive (Lemma 1, p. 139). Those properties are for each
  channel's mean separately. Nothing in Katz carries them over to the ratio.

**Newton II is a premise, not a hypothesis under test.** The 30 August
specification also carried a rejection gate that tested Newton II against the
data. On 7 September the user ruled that the investigation asks what must be
true if the law is correct. Anti-aligned readings can then only arise from
error, and the estimator reconciles them conditionally rather than rejecting
them. The same record keeps a distinction: the construction gives less
erroneous pairs more weight, but its scalar is not the single least-error
reconciliation. In the symmetric anti-aligned example the point is 1, while
the least discrepancy (6) is approached by sending one channel to zero
(`mass_estimator_law_assumed_correct_steering_2026-09-07.md`).

## 5. The equation

Specified on 21 September (`mass_estimator_equation/README.md`):

$$
\widehat m(\widetilde{\mathbf F},\widetilde{\mathbf a},\Sigma)
=\frac{E_P[f]}{E_P[\alpha]}
=\frac{\displaystyle\int_{\mathcal C} f\,e^{-Q/2}\,d\nu}
        {\displaystyle\int_{\mathcal C}\alpha\,e^{-Q/2}\,d\nu},
\qquad
\mathcal C=(0,\infty)^2\times S^{d-1},\quad d\nu=df\,d\alpha\,d\Omega(\mathbf u).
$$

- **Uncertainty** comes from the same law. Report the equal-tail quantiles of
  $M=f/\alpha$ and the standard deviation of $\log M$. The ordinary mean and
  second moment of $M$ diverge for every finite dataset, so an ordinary SD is
  undefined and "mass ± SD" is not available.
- **The promise** is conditional: a 95% interval holds 95% of the declared law.
  It is not a repeated-experiment confidence guarantee (§8 explains why it
  cannot be).
- **At measured zero-zero** with independent isotropic errors,
  $\widehat m=\sigma_F/\sigma_a$ and $M/(\sigma_F/\sigma_a)$ is half-Cauchy. The
  95% interval is about $[0.039,\,25.45]$ times $\sigma_F/\sigma_a$, and the log
  standard deviation is $\pi/2$. That answer describes the instruments, not the
  object.
- **Exact inputs** are a separate branch outside the function. Exact
  nonzero codirectional vectors give their ratio; exact zero-zero identifies no mass;
  other exact pairs contradict positive-mass Newton II.

## 6. Where the equation sits: in one dimension it is Fieller's problem

On one known axis, a noisy $F$ and a noisy $a$ with known uncertainties give
exactly the classical problem of the ratio of two normal means.

**What we take from the literature.**

- *Fieller (1954)* inverts the pivot $(y-\alpha x)/(v_{yy}-2\alpha v_{xy}+\alpha^2v_{xx})^{1/2}$
  into a quadratic inequality in the ratio (§3, p. 176, eq. 5). The resulting
  range is a finite interval when the denominator is significant, and otherwise
  an unbounded set: the complement of an interval, or the whole line (§5,
  p. 177; table p. 180). He regards an unbounded range, when the denominator is
  not significant, as what we should intuitively expect, and the whole-line case
  as saying that the data are consistent with every value (§5, p. 177). He credits
  the pivot to his 1940 paper and writes in fiducial language; the 1954 paper
  treats estimated variances ($t$).
- *With known variances* (our case) the set is unbounded exactly when the
  observed acceleration is not significant at the same level:
  $|\widetilde a|/\sigma_a\le1.96$ for a 95% set (Fieller §§4–5,
  pp. 176–177; Franz 2007, p. 9; with known $\sigma$ the $t$ quantile becomes
  the normal one: Koschat p. 464, Franz p. 7). The force reading only decides which unbounded shape
  appears.
- *Koschat (1987)* proves two things. No procedure with a positive coverage
  guarantee can always return bounded intervals (Proposition 1, p. 463). And
  within the natural class of intervals centred on the observed direction whose
  width shrinks as the data vector lengthens, Fieller's is the unique one with
  exact coverage (Theorem, p. 467). He notes other exact procedures exist
  outside that class, which he calls worthless in practice (pp. 467–468).
- *The usual point* is the plain ratio of the readings (Franz 2007, p. 6;
  von Luxburg & Franz, §1.1). It has no finite mean, and usually no finite
  variance (Franz pp. 4, 7; von Luxburg & Franz pp. 3, 14). The delta method
  never gives unbounded limits and fails when the denominator is near zero
  (Franz pp. 10–11).
- *Liseo (2003)* reviews the Bayesian side. His model is two independent
  normal means with equal known variance and ratio $\theta=\omega_1/\omega_2$
  (§1). His eq. (10) is the Jeffreys prior, $\propto|\omega_2|$ in
  $(\theta,\omega_2)$ coordinates (p. 137). By that Jacobian it is the flat prior
  on the two means; that identification is ours, not his wording. Its
  marginal posterior for $\theta$ is his eq. (12) (p. 138): a Cauchy-like
  $1/(1+\theta^2)$ factor times a bracket in $\phi$ and $\Phi$. He notes the
  thick, Cauchy-like tails (p. 138), and that posterior sets are finite but can
  have poor coverage at fixed sample size (pp. 134, 138).

**The one-dimensional identity.** Our 1D law, with the two directions $\pm1$
each weighted ½, is flat on both same-sign quadrants of the two means.
Liseo's eq. (12) restricted to $\theta>0$ is exactly that
(`literature_review/mass_candidate_liseo_evidence_2026-09-08.md`; re-checked
numerically 2026-09-23). Two details matter:

- Liseo assumes equal variances. Our unequal $\sigma_F,\sigma_a$ need each axis
  rescaled by its own $\sigma$, which leaves a flat prior flat.
- A flat prior on the positive quadrant alone, with a fixed sign, gives a
  slightly different density, $1+s\,\Phi(s)/\phi(s)$ in the bracket. The
  difference is visible only at low signal-to-noise.

So, in one dimension, **our probability law is Liseo's flat (Jeffreys) posterior
restricted to positive mass**. Its infinite mean is our consequence of the
Cauchy-like tail; Liseo does not state it.

**What the equation adds beyond one-dimensional Fieller.**

1. **Positivity.** Mass is positive, so the law is conditioned on the
   same-sign event.
2. **Vectors with an unknown common direction.** Fieller's problem has no
   direction. In two or three dimensions the question becomes the ratio of the
   lengths of two noisy vectors that must be parallel. This is also where the
   choice of weighting stops being innocent (§7).
3. **The point.** Fieller's literature reports intervals and posteriors; its
   point is the plain ratio. $E[f]/E[\alpha]$ is not in Liseo, and the
   literature search did not find it elsewhere. Its justification is
   composition, which a generic ratio of two means does not have.
4. **Equal treatment of the channels.** Fieller's problem singles out the
   denominator: a weak denominator breaks it and a weak numerator does not. The
   common-force law removes that asymmetry.

## 7. The weighting is not forced

The composition theorem starts from a law. It does not choose one. Newton II
and Gaussian errors leave the weighting $\rho$ open, and the lab spent
15 September mapping that freedom (VD-Newton, `investigation/`):

- **Gaussianity does not choose it** (contribution 2,
  `gaussian_conditioning.md`). In more than one dimension, exactly parallel
  vectors have probability zero under the noise. You must say how you approach
  "parallel", and different approaches give different laws and different
  points.
- **The flat weighting has a concrete meaning** (contribution 6,
  `why_flat_conditioning.md`). It is the limit of Gaussian conditioning on a
  small cross product $|\mathbf F\times\mathbf a|$, the area the two vectors
  span. That rule follows if the mismatch must add up on the force side, treat
  the two channels symmetrically, and have a constant tolerance. Those are
  extra requirements, not yet warranted.
- **Each rival has its own reason** (contribution 7, `operational_warrant.md`).
  Area conditioning preserves additive balance error. The tube measure scales
  the discrepancy by the local Gaussian error. The sampling covariance gives a
  third rule. None is selected.
- **The tube measure is Jeffreys' rule** (contribution 3,
  `weighting_and_calibration.md` §1). For the compatible-pair model the joint
  Jeffreys prior, $\sqrt{\det I}$, is the compatible-surface volume in the noise
  metric. For independent isotropic errors it is $(f^2/\sigma_F^2+\alpha^2/\sigma_a^2)^{(d-1)/2}$ times the flat
  weighting. In one dimension the extra factor is 1. Jeffreys and flat agree
  there, which is Liseo's eq. (10); the fork opens only for vectors.

**What we take from the literature.**

- *Sun & Berger (2008)* show that Jeffreys and reference priors typically
  depend on the stopping rule. Jeffreys' prior picks up a factor from the
  expected sample size (pp. 19–22, eqs. 2.1–2.2). We cite them only for the
  general point that Jeffreys' rule uses the whole experiment's Fisher
  information, so it depends on the design. They do not discuss noise ratios or
  dimension, or state a clash with updating; that clash is our own concern
  (`joint_inference_and_uncertainty.md`).
- *Berger, Liseo & Wolpert (1999)* place Fieller's problem among the
  Gleser–Hwang class of hard problems, which they say are "simply not amenable
  to any 'objective' analysis" (pp. 7, 15–17). For those problems prior
  information matters, and reference-prior analyses are "arguably the best"
  default candidates. That is the literature's own statement that this choice cannot
  be proven away by the model alone. Their Example 5 (pp. 9–10) shows a flat
  prior on a vector mean implies an unreasonable prior on its length, and
  recommends a uniform prior on direction instead. That is the same shape as
  our construction: weight on the magnitudes, uniform on direction.
- *Gull* and *Lindley & El-Sayyad* (§3) had already found, for lines, that the
  prior on the true values decides the answer. Our one-dimensional law is a
  flat prior on the true values, the class their warnings concern; whether
  those warnings bite for a single pair is not settled here.

**Status.** The flat weighting is a declared choice with a partial warrant
(area conditioning), not a consequence of the law. Which default to use when
nothing is known about the object is open. The 2026-09-23 work on that
question is not part of this draft.

## 8. The limit: no always-finite interval can guarantee coverage

Our lab proved this in its own terms, before we located the general result
(contribution 3,
`weighting_and_calibration.md` §4). At true zero excitation, $\mathbf a^*=\mathbf0$
and $\mathbf F^*=\mathbf0$, so the sampling law of the readings is the same for
every mass. A finite interval therefore misses large enough masses almost
always. Letting the excitation shrink towards zero while the mass grows, the
sampling laws converge to the null law in total variation, so no finite
interval keeps a positive coverage guarantee over all masses and all nonzero
excitations. The record is careful about what this does not claim. It does
not claim that every fixed mass undercovers. It does not apply unchanged to a
bounded mass range or a declared minimum excitation (Gleser & Hwang's
Theorem 3, p. 1359, shows bounded ranges carry their own, weaker obstruction).
And it does not forbid a conditional credible interval.

**What we take from the literature.**

- *Gleser & Hwang (1987)*, Theorem 1 (p. 1353), is the general result. Its
  conditions: the parameter of interest is unbounded; as a nuisance parameter
  approaches some limit point, the distribution of the data tends to one that
  does not depend on the parameter of interest; and all parameter values share
  the same support. Its conclusion: every confidence set with positive
  confidence level is infinite with positive probability at every parameter
  value, and a set that is finite with probability one has confidence level
  (infimum coverage) zero. It covers errors-in-variables models, including the
  general nonlinear case (§3.1) and ratios of regression coefficients (§3.3).
  Our problem fits §3.1, with force $=m\times$ true acceleration and weak
  excitation as the limit. This needs both channels to be noisy and the mass to
  be unbounded. Their §5 (p. 1361) adds that excluding the non-identified point
  itself does not help; nearness is enough. Our lab's proof is a special case
  of this theorem.
- *Koschat (1987)*, Proposition 1, states the ratio-of-means version directly
  (§6 above).
- *Dufour (1997)* generalises the result to locally almost unidentified models.
  It was cited from its abstract only and not read for this draft.

**Where each method sits.**

| Method | Always finite? | Guaranteed coverage? | Source |
|---|---|---|---|
| Fieller | no | yes, exact | Fieller 1954; Koschat 1987 |
| Vector analogue: conditional likelihood-ratio set | no (bounded, one-sided, two rays, whole domain, or empty) | yes, exact under the stated Gaussian model | lab contribution 5, `conditional_uncertainty_and_design.md` §§2–3 |
| Penalised Fieller | yes, when its penalty $\lambda\ge t^2_\alpha/4$ | no | Wang et al. 2021 |
| This equation's interval | yes | no; it promises conditional probability | equation README |

For penalised Fieller: Theorem 1 (§2.5, p. 1358) gives boundedness. The
authors say it "is not an exact method" (p. 1366). In their Table 1 (p. 1361;
$n=20$, bivariate normal, 95%, a weak denominator whose test has power 0.20)
its coverage is 83.71%. Fieller's coverage there is 95.04%, but 79.97% of
Fieller's sets are unbounded. The same table's parametric bootstrap stays
bounded and covers 95.85% at that setting, with a median width of 61.97, so a
single table does not show every bounded method failing. That rests on the
theorems.

**The same limit in our own numbers.** At zero excitation, our flat law's
nominal 95% interval covers the true mass 99.71% of the time when the mass is
$\sigma_F/\sigma_a$, but 6.93% when it is 64 times smaller and 7.26% when it is
64 times larger (VD-Newton `investigation/README.md`, null reuse diagnostic,
10,000 trials, Monte Carlo errors 0.05–0.26 points; the three masses reuse the
same null trials, so they are not independent confirmations). Coverage near the
instrument scale hides failure elsewhere.

**Why this is physics, not a defect.** At zero excitation the readings carry
no information about mass: an object that is neither pushed nor accelerating
reveals nothing about its inertia. Any finite answer there must come from
somewhere other than the object, and ours comes from the instruments,
$\sigma_F/\sigma_a$. The partial cases still carry information. With the force and
direction known and a weak acceleration reading, the flat law's 95% lower bound
on mass covers the true mass at least 95% of the time, while the point itself
falls towards zero relative to the true mass (lab contribution 8,
`weak_acceleration_information.md`, findings 1–2). The information is
one-sided: a lower bound on mass with no useful upper bound. That is the
same shape as Fieller's unbounded ranges, which include infinitely large
values (§5, p. 177).

(Physicists meet a relative of this in Feldman & Cousins (1998), who construct
intervals with exact coverage for a Gaussian mean bounded by a physical limit,
such as a mass that cannot be negative, that are never empty or unphysical.
Their problem is a boundary, not a ratio, and they give no infinite intervals.
Cited only as a familiar reference point for a physics audience.)

## 9. The story in one table

| Step | Status | From |
|---|---|---|
| Candidates are same-direction pairs with $f,\alpha>0$ | forced by Newton II with $m>0$ | working introduction; spec d1 |
| Integrate over the candidates rather than fit one | the Bayesian errors-in-variables move | median record; Lindley & El-Sayyad; Gull |
| Average, then divide | forced, given composition (L) and (R), C3 and the theorem's domain | 2 and 6 September records |
| Composition applies at all | VD premise: the estimator is the definition | 1 August; 2 September |
| The common-force law applies | VD commitment: inverse mass adds under a common force ($1/m$ has the same standing as $m$) | 2 September records; 7 September steering |
| Newton II is assumed, not tested | ruling, 7 September | steering record |
| Gaussian noise with known $\Sigma$ | declared input | spec d1 §9; equation README |
| Flat magnitudes, uniform direction | declared choice with a partial warrant | lab contributions 2, 3, 6, 7 |
| 1D law = Liseo's flat posterior, positive part | known | Liseo 2003 eq. (12) |
| Intervals are conditional, not guaranteed | forced by the Gleser–Hwang theorem for any always-finite interval | Gleser & Hwang 1987; Koschat 1987; lab contribution 3 |

**Possibly new**, as far as the searches went: the composition-forced point,
precisely the ratio of the posterior means of the *positive magnitudes* under
the same-sign restriction. (Under Liseo's unrestricted flat prior the ratio of
the posterior means of the two signed means is just the plain ratio of the
readings, so it is the positivity that makes the point different.) Also the
equal treatment of force and acceleration that goes with it, and the vector
problem with its open weighting question. **Not new:** the
one-dimensional law, the impossibility of guaranteed finite intervals, and the
dependence of default priors on design.

## 10. What this draft leaves out, and what is still open

**Left out by instruction.** The 2026-09-23 parameter findings: the tilt λ as
a prior on how balanced the two channels are; the argument that
order-independent updating across instruments reduces the default weighting
to $(f\alpha)^k$; switch rules; the update-rule reading. See
`mass_estimator_regimes_priors_and_updating_2026-09-23.md` and the
conversation of that day.

**Open.**

- The C3 premise: whether any composing readout can use more than the
  magnitude law.
- The three requirements behind the flat weighting (force-side additivity,
  channel symmetry, constant tolerance) are not yet warranted.
- The noise model is declared. Calibration uncertainty and non-Gaussian noise
  are untested.
- Several readings of one mass need a declared joint model.
- There is no real dataset that the user took or analysed himself.

---

## References

"Read" means the paper was read against the claim made here on 2026-09-23.
PDFs are in `../_dscn_mass_estimator/papers/` unless marked otherwise.

| Reference | Used in | Read |
|---|---|---|
| Arratia, R., Goldstein, L. & Kochman, F. (2019). Size bias for one and all. *Probability Surveys* 16, 1–61. doi:10.1214/13-PS221; arXiv:1308.2729 (v3 read; the journal version was not confirmed at the publisher). | §4 | yes |
| Bartel, T. W., Stoudt, S. & Possolo, A. (2016). Force calibrations using errors-in-variables regression and Monte Carlo uncertainty evaluations. *Metrologia* 53, 965–980 (NIST author manuscript). | §2 | yes |
| Berger, J. O., Liseo, B. & Wolpert, R. L. (1999). Integrated likelihood methods for eliminating nuisance parameters. *Statistical Science* 14(1), 1–28. | §7 | yes |
| Boggs, P. T. & Rogers, J. E. Orthogonal distance regression (NIST). Cited by `vector_division_inertial_mass_measurement_d1.md`. | §2 | no |
| Dufour, J.-M. (1997). Some impossibility theorems in econometrics with applications to structural and dynamic models. *Econometrica* 65(6), 1365–1388. Not in `papers/`. | §8 | abstract only |
| Feldman, G. J. & Cousins, R. D. (1998). Unified approach to the classical statistical analysis of small signals. *Phys. Rev. D* 57, 3873. arXiv:physics/9711021. | §8 | yes |
| Fieller, E. C. (1954). Some problems in interval estimation. *JRSS B* 16(2), 175–185. | §6, §8 | yes |
| Franz, V. H. (2007). Ratios: a short guide to confidence limits and proper use. arXiv:0710.2024. | §6 | yes |
| Gleser, L. J. & Hwang, J. T. (1987). The nonexistence of 100(1−α)% confidence sets of finite expected diameter in errors-in-variables and related models. *Annals of Statistics* 15(4), 1351–1362. | §8 | yes |
| Golub, G. H. & Van Loan, C. F. (1980). An analysis of the total least squares problem. *SIAM J. Numer. Anal.* 17, 883–893 (Cornell TR 80-411 version read). | §2 | yes |
| Gull, S. F. (1989). Bayesian data analysis: straight-line fitting. In J. Skilling (ed.), *Maximum Entropy and Bayesian Methods*, 511–518. Kluwer. | §3, §7 | yes |
| Katz, M. W. (1961). Admissible and minimax estimates of parameters in truncated spaces. *Annals of Mathematical Statistics* 32(1), 136–142. doi:10.1214/aoms/1177705146. | §4 | yes |
| Koschat, M. A. (1987). A characterization of the Fieller solution. *Annals of Statistics* 15(1), 462–468. (Mis-dated 1981 by Wang et al. 2021.) | §6, §8 | yes |
| Lindley, D. V. & El-Sayyad, G. M. (1968). The Bayesian estimation of a linear functional relationship. *JRSS B* 30(1), 190–202. | §2, §3, §7 | yes |
| Liseo, B. (2003). Bayesian and conditional frequentist analyses of the Fieller's problem. A critical review. *METRON* LXI(1), 133–150. | §6, §7 | yes |
| Sun, D. & Berger, J. O. (2008). Objective Bayesian analysis under sequential experimentation. *IMS Collections* 3, 19–32. doi:10.1214/074921708000000020; arXiv:0805.3064. | §7 | yes |
| von Luxburg, U. & Franz, V. H. A geometric approach to confidence sets for ratios: Fieller's theorem, generalizations, and bootstrap. arXiv:0711.0198 (2007; journal version not checked). | §6 | yes |
| Wang, P., Xu, S., Wang, Y.-X., Wu, B., Fung, W. K., Gao, G., Liang, Z. & Liu, N. (2021). Penalized Fieller's confidence interval for the ratio of bivariate normal means. *Biometrics* 77, 1355–1368. doi:10.1111/biom.13363. | §8 | yes |
| York, D., Evensen, N. M., López Martínez, M. & De Basabe Delgado, J. (2004). Unified equations for the slope, intercept, and standard errors of the best straight line. *Am. J. Phys.* 72, 367–375. Cited by `vector_division_inertial_mass_measurement_d1.md`. | §2 | no |

**Our own records**, in the order the story uses them. Dates are the files'
dates as catalogued (several files do not print their own date). VD-docs paths are
relative to `Newton-analysis/`; lab files are in VD-Newton
`03_trace_and_evaluator/mass_estimator/investigation/`.

| Record | Date | Used in |
|---|---|---|
| `_note_why_mass_estimation/mass_estimation_introduction_candidate_2026-09-06.md` (working introduction) | 6 Sep | §1 |
| `_dscn_mass_estimator/vector_division_inertial_mass_measurement_d1.md` | 26 Jul | §§1–2 |
| `_dscn_mass_estimator/why_the_estimator_is_the_definition.md` | 1 Aug | §§2, 4 |
| `_dscn_mass_estimator/median_based_estimator_inertial_mass.md` | 27 Aug | §§2–3 |
| `_dscn_mass_estimator/disagreement_rule_mass_estimator_trace.md` | 29 Aug | §3 |
| `_dscn_mass_estimator/inertial_mass_estimator_full_working_spec_d1.md` | 30 Aug | §§2, 4 |
| `_dscn_mass_estimator/what_forces_the_ratio_of_means_readout.md` | 2 Sep | §4 |
| `_dscn_mass_estimator/what_forces_the_chain_to_the_estimator.md` | 2 Sep | §2 |
| `_dscn_mass_estimator/mass_readout_composition_uniqueness_2026-09-06.md` | 6 Sep | §4 |
| `_dscn_mass_estimator/mass_estimator_law_assumed_correct_steering_2026-09-07.md` | 7 Sep | §4 |
| `_dscn_mass_estimator/literature_review/mass_candidate_liseo_evidence_2026-09-08.md` | 8 Sep | §6 |
| Lab contributions 2–8: `gaussian_conditioning.md`, `weighting_and_calibration.md`, `joint_inference_and_uncertainty.md`, `conditional_uncertainty_and_design.md`, `why_flat_conditioning.md`, `operational_warrant.md`, `weak_acceleration_information.md` | 15 Sep | §§7–8 |
| Lab `investigation/README.md` (null reuse diagnostic) | 21 Sep | §8 |
| `_dscn_mass_estimator/mass_estimator_equation/README.md` | 21 Sep | §5 |
