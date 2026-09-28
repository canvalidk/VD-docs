# The mass estimator's lemmas: what we assume, what it gives, what is left

**2026-09-27.** Record, filed at the user's request, written by Claude from the
conversation of 27 September. His instruction: "We can imagine the Lemmas list as
a record of it's own. It won't be a note but a record. It'll be dated, and we can
imagine the changed versions go in as replacements."

**How this record changes.** Like any record: changes arrive as corrections or
supersessions under the usual rules, not as edits in place.

**What it covers.** The premises the estimator rests on, stated as short named
expressions; what follows from them; and what is still open. The equation being
pushed through is **ours26** (per-axis noise,
`ours26/ours26_per_axis_noise_2026-09-26.md`). ours25b is its case with one noise
pair for all axes. A result that holds only with one noise pair is marked
**[one pair]**.

**A ruling this list uses.** Newton III and later commitments may be used here:
"the mass estimation work doesn't need to care about commitment order so far. We
can consider that later. So we are totally fine with using Newton 3 and more."
(27 Sept.)

**Grades.** *bedrock*: denying it changes the problem. *strong*: a real premise,
well motivated. *medium*: plausible, narrower. *mild*: technical. *declared*:
chosen, not argued.

---

## 0. Notation

- Reading $i$, axis $k$: measured $\tilde F_{ik}$, $\tilde a_{ik}$; true
  $F^\ast_{ik}$, $a^\ast_{ik}$; noise SDs $\sigma_{F,ik}$, $\sigma_{a,ik}$.
- One noise pair: $\mathbf x_i=\tilde{\mathbf F}_i/\sigma_F$,
  $\mathbf y_i=\tilde{\mathbf a}_i/\sigma_a$, $s=\sigma_F/\sigma_a$,
  $m=s\tan\theta$.
- A candidate is a possible true pair. In noise units, reading $i$'s push is
  $\mathbf v_i$, with $\mathbf F^\ast_i/\sigma_F=\mathbf v_i\sin\theta$ and
  $\mathbf a^\ast_i/\sigma_a=\mathbf v_i\cos\theta$; $r^\ast_i=\lVert\mathbf v_i\rVert$
  for the true pair and $R^{\ast2}=\sum_i r^{\ast2}_i$.
- $R(X,Y)$: the readout, fed the law of the true sizes
  $X=\lVert\mathbf F^\ast\rVert$, $Y=\lVert\mathbf a^\ast\rVert$.
- $\pi$: the starting law of mass (the prior).

## 1. The premises

Numbering is kept from the conversation, so earlier references still work. L4
is narrowed and L14 is new (§4).

| | name | expression | grade |
|---|---|---|---|
| L1 | Newton II | $\mathbf F^\ast=m\,\mathbf a^\ast$, $m>0$; assumed, not tested (ruling of 7 Sept: no gate) | bedrock |
| L2 | Noisy type | every $\sigma>0$, so $\widehat m\in(0,\infty)$, never "undefined" | bedrock |
| L3 | No built-in scale | force units $\times\lambda$, acceleration units $\times\mu$ $\Rightarrow$ $\widehat m\times\lambda/\mu$. The one mass scale allowed in is the declared $\pi$, which transforms the same way (T20) | bedrock |
| L4 | Swap, law half | $\pi$ is unchanged by exchanging the channels: symmetric under $m/c\leftrightarrow c/m$, i.e. $\theta\leftrightarrow 90^\circ-\theta$ | strong |
| L5 | Lumping | $R(X_1+X_2,Y)=R(X_1,Y)+R(X_2,Y)$, on one shared law, common acceleration | strong |
| L6 | Magnitude-law readout (C3) | $R$ depends only on the law of $(X,Y)$; no second weighting (§4.2) | strong, load-bearing |
| L7 | Calibration | $R(f,\alpha)=f/\alpha$ on sure inputs; continuous at constants; defined on every positive law with finite means | mild |
| L8 | Axis splitting | a reading and its $d$ axes read as 1D readings give the same law and answer; strong form: one candidate has one size however its axes are grouped | strong |
| L9 | Isotropy | the push weight depends only on the push's length. In which units: open (§3.3) | strong |
| L10 | No push scale | the push weight has no width $\omega$ ($\omega\to\infty$) | strong for the point; implicated in the widths (§3.3) |
| L11 | Consistency | $\widehat m_N\to m$ whenever $R^{\ast2}\to\infty$ | strong |
| L12 | One joining rule | $\operatorname{size}(A\cup B)=\operatorname{size}(A)\oplus\operatorname{size}(B)$, one fixed $\oplus$ | medium |
| L13 | Gaussian noise | errors zero-mean Gaussian, independent across components, channels and readings, with known SDs | declared, never argued |
| L14 | Common force | $1/R(X,Y_1+Y_2)=1/R(X,Y_1)+1/R(X,Y_2)$: the reduced mass of an interacting pair (uses Newton III) | strong |

## 2. What they give

| | name | expression | from |
|---|---|---|---|
| T1 | Exact branch | $\sigma=0$: one mass, no mass, or every mass; "undefined" only at exact $0/0$ | L1 |
| T2 | Candidates | $\mathbf F^\ast=f\mathbf u$, $\mathbf a^\ast=\alpha\mathbf u$, $f,\alpha>0$ | L1 |
| T3 | Separation | $R(X,Y)=R(X,1)\,R(1,Y)$ | L5, L14, L7 |
| T4 | Ratio of means | $R=E[X]/E[Y]=E[\alpha m]/E[\alpha]$ | T3, L5, L14, L6, L7 |
| T5 | Swap, readout half | $R(Y,X)=1/R(X,Y)$ | T4 |
| T6 | Flat pushes | push weight $d^d\mathbf v$ per reading; per axis in that axis's own noise units | L8, L9, L10 |
| T7 | Prior once | nothing attached to a reading may depend on $m$; equivalently the $m$-dependent part of the push weighting cancels each reading's determinant factor | L11 |
| T8 | The law (ours26) | $p(m)\propto\pi(m)\exp\!\big[-\sum_{i,k}(\tilde F_{ik}-m\tilde a_{ik})^2/2(\sigma_{F,ik}^2+m^2\sigma_{a,ik}^2)\big]$ | L1, L13, T6, T7 |
| T9 | Stacked size | $\lVert\mathbf F^\ast\rVert=\big(\sum_i\lVert\mathbf F^\ast_i\rVert^2\big)^{1/2}$, per candidate, before averaging | L8, L12 |
| T10 | The readout (ours26) | $\widehat m=E\lVert\mathbf F^\ast\rVert/E\lVert\mathbf a^\ast\rVert=\int mA\,p\,dm\big/\!\int A\,p\,dm$, $A(m)=E[\lVert\mathbf a^\ast\rVert\,\vert\,m]$ | T4, T8, T9 |
| T11 | Sufficiency | the data enter only through $(P_g,Q_g,D_g,M_g)$ for each noise pair $g$. [one pair] $N$ readings in $d$ dims are one reading in $M=Nd$ | T8, T9 |
| T12 | Combination | per noise pair, $(C,T,M)_{A\cup B}=(C,T,M)_A+(C,T,M)_B$ | T11 |
| T13 | Totality for any proper $\pi$ | $A(m)=O(1/m)$ and $mA(m)$ bounded, so $\widehat m\in(0,\infty)$; totality does not select $\pi$ | T8, T10 |
| T14 | Zero readings give $s$ [one pair] | $\widehat m=s$ at zero readings, for any estimator of this type. With several pairs the zero-data law is $\pi$ and the readout is not its centre | L2, L3, L4 |
| T15 | Equal energies [one pair] | $P=Q\Rightarrow\widehat m=\text{median}=s$ | T11, T5, L4 |
| T16 | A tilt is an unseen reading [one pair] | $\lambda\sin2\theta\equiv$ one reading with $P=Q$, $D=2\lambda$ | T8 |
| T17 | Convergence | $\widehat m\to m$ as $R^{\ast2}\to\infty$ | T8, T7 |
| T18 | Width [one pair] | $\mathrm{Var}_{\rm true}/\mathrm{Var}_{\rm law}=1+M/R^{\ast2}$ | T8, L10, L13 |
| T19 | No mean, under the current $\pi$ | $E_p[m]=\infty$ for the half-Cauchy, so report the median, intervals and SD of $\ln m$. A lighter-tailed $\pi$ would change this | T8 |
| T20 | Mixed-instrument no-go | with two or more noise pairs these cannot all hold: each instrument alone defaults to its own ratio; zero readings leave the law unchanged (they do: $Q=0$, likelihood 1); arrival order does not matter. So $\pi$ is declared before data, as part of the specification | T8, T14 |

Consequence of T20: ours26's `first_reading_geometric` centre depends on arrival
order, and L3's "nothing else goes in" holds only with $\pi$ counted as a
declared input.

## 3. What is left

### 3.1 The starting law $\pi$

- **Forced:** symmetric (L4), counted once (T7), declared before data (T20),
  unit-covariant (L3), the same for a reading and its axes (L8). With one noise
  pair, centred on $s$ (T14).
- **Open:** its shape; with several noise pairs, also its centre.
- **Current:** uniform in the angle at centre $c$, $\pi(m)=c/(c^2+m^2)$.
- **The shape matters.** Every $\pi_c(m)=m^{-1}g(\ln(m/c))$ with $g$ even
  satisfies the forced parts. For $\tilde F=1$, $\tilde a=0$,
  $\sigma_F=\sigma_a=c=1$ (1D): half-Cauchy 1.33213; lognormal with log-SD 0.3,
  1 and 2: 1.03539, 1.23185, 1.48048. (From the 27 Sept completion message;
  reproduced by Claude to every digit.)
- **Candidate: uniform arc length.**
  $\pi_{\rm arc}(m)\propto\big(\sum_k(s_k/(s_k^2+m^2))^2\big)^{1/2}$, the
  speed of the curve $\theta_k(m)=\arctan(m/s_k)$. Proper, unit-covariant,
  reciprocal, and the half-Cauchy when all ratios agree. A reason to prefer it
  to summed angular speeds (Claude, 27 Sept, algebra only): with the push
  $v_k$ held fixed, axis $k$ carries Fisher information $v_k^2$ about
  $\theta_k$, whatever $\theta_k$ is; informations add over axes, so
  $\sqrt{I(m)}=\big(\sum_kv_k^2(d\theta_k/dm)^2\big)^{1/2}$, which is arc length
  when the pushes are equal on every axis **in noise units**. That last clause
  is the units fork of §3.3. Under T20 the instrument set must be declared up
  front.

### 3.2 C3's justification

L6 is what closes the direction-weighting hole (§4.2). The argument for it so
far: a weight $h(\mathbf u)$ built from $E[\mathbf u]$ depends on the data, so
it reweights the law a second time with the same readings. That is an
argument, not a proof.

### 3.3 Coverage, $\omega$ and the units of isotropy

See `ours26/README.md`: the two coverage failures, the reading of L10 as
"$\omega$ unknown and learned", and the fork over which units L9 holds in.

### 3.4 Other open items

- L13 is declared, never argued. A general form with a full covariance
  $\Sigma$ exists: $Q(m)=r_m^\top V_m^{-1}r_m$, $r_m=\tilde{\mathbf F}-m\tilde{\mathbf a}$,
  $V_m=\Sigma_{FF}-m(\Sigma_{Fa}+\Sigma_{aF})+m^2\Sigma_{aa}$ (completion
  message; its conditional mean checked against ours26 by Claude). With
  correlated axes, the L8 argument for T6 has to be restated.
- Repeated measurements of one unchanged pair are one push, not several. The
  law as written treats every reading as a new push; no tester world tests the
  other case.
- The weak form of L8 (only the answers agree): sketched, not checked.
- Real data.

## 4. Bookkeeping behind the statuses

### 4.1 The swap, split

The swap used to be one premise. It is now two things:

- **Readout half:** a theorem (T5), from lumping, common force and C3.
- **Law half:** a premise (L4) about $\pi$ only. The push part is already
  symmetric, because $\mathbf v$ is shared by both channels in noise units.

"Any two of lumping, common force and swap give the third" is lopsided:

| from | to | needs C3? |
|---|---|---|
| lumping + swap | common force | no: $1/R(X,Y_1+Y_2)=R(Y_1+Y_2,X)=R(Y_1,X)+R(Y_2,X)$ |
| common force + swap | lumping | no, the mirror |
| lumping + common force | swap | yes |

Common force is a premise here (L14), with its physics (reduced mass, Newton
III), under the ruling quoted at the top.

### 4.2 What C3 holds back

Readouts that weight candidates by direction, $\mathbf u$ the candidate's
direction and $\mathbf v=E[\mathbf u]$:

- $R_h=E[h\,f]/E[h\,\alpha]$, $h=1+(\mathbf u\cdot\mathbf v)^2$ (the 6 Sept
  counterexample, `mass_readout_composition_uniqueness_2026-09-06.md` §5);
- $R_{h_1h_2}=E[h_1f]/E[h_2\alpha]$, $h_1=1+(\mathbf u\cdot\mathbf v)^2$,
  $h_2=1+(\mathbf u\cdot\mathbf v)^4$ (27 Sept).

| constraint | rules out $h_1\ne h_2$? | rules out one $h$? |
|---|---|---|
| lumping, common force | no | no |
| calibration | only at $\mathbf u=\mathbf v$ | no |
| L3 (units) | no: direction has no units | no |
| swap | yes (1.33 instead of 1 on a random law) | no |
| C3 | yes | yes |

$R_h$ is the ratio of means under the reweighted law $h\,p$, so the hole is a
second weighting of the law, not a different readout. Axis splitting does not
obviously close it (the stacked direction survives regrouping; not checked
rigorously). Consistency does not ($h\to$ constant as the law concentrates).
Size on a random law: 0.12%. In principle unbounded, since $h$ can be any shape.

### 4.3 Why the ratio of means stays a theorem

As a premise it would be equivalent to {L5, L14, L6, L7}. It stays a theorem
because premises should be the obvious end; assuming it hides C3 instead of
naming it; uniqueness is the point (a remaining choice would be a rival
definition of mass); "ratio of means" alone does not say which sizes with many
readings (T9 does); and the derivation records that the readout rests on
Newtonian composition.

## 5. Sources and checks

- The chain: `../_note_mass_estimator_equation/the_mass_estimator_equation_d2.md`
  (its §3.1 premise table is the predecessor of §1 here) and the records it cites.
- ours26: `ours26/ours26_per_axis_noise_2026-09-26.md`. Combination:
  `the_combination_equation_is_exact_2026-09-26.md`. Composition theorem:
  `mass_readout_composition_uniqueness_2026-09-06.md`.
- The completion message of 27 Sept (VD-Newton, not filed): source of T13,
  T20, the log-symmetric table, the arc-length candidate and the general
  covariance form. Claude checked its algebra and reproduced its numbers.
- Checked by Claude on 27 Sept: the two-order identity (difference
  $-(ry-x)^2/[(r+x)(y+1)(ry+xy+y+1)]$, symbolic); the median and least-squares
  counterexamples to lumping and common force (exact fractions); the
  direction-weighted readouts against lumping, common force, calibration,
  units and swap (numerical); the prior table (quadrature). Not checked by
  computation: the Jeffreys argument in §3.1 (algebra only).
