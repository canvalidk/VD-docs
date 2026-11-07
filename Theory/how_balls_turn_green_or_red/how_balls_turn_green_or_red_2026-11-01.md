# How Balls Turn Green or Red, and Why Theories Feel Absolutely True

## A formal model of the urn, the colouring rule, and the in-hand window

**Status:** record. Claude-authored at the user's request, 2026-11-01, from
that day's message. Written to Claude's scratchpad, not to the VD folder,
because another session was working there. Intended home: `Theory/`, beside
the disjunction record. The user's statements are marked *(stated)*;
everything else is *(analysis)* and is not ruled. Each analysis claim is
tagged **proved**, **sketched** or **open**.

**Parents (read against):**

- `inbox/prediction_sets_as_disjunctions_neptune_and_vulcan.md` (the
  colouring rule, §1)
- `inbox/nobody_made_a_mistake_meaningful_substitutions.md` (the mistake
  family, §11)
- `Theory/witness_sheets/witness_sheets.md` (the fidelity element)
- `Theory/theories_and_belief/theories_and_belief.md`
- `Theory/best/alpha_and_the_one_draft.md` (the catalogue α)
- `Theory/actually_there_prediction_sets/prediction_sets.md`

**This record adds the urn layer**, which until now lived only in the
conversation of 2026-10-16. It keeps the disjunction record's colouring rule
and adds the rerun: a corrected trace is a new ball (§3, D10; §6).

**Revised the same day**, after the user's correction. The first version
proposed a clause in which a held auxiliary item corrects the trace and the
corrected trace colours the ball. That clause is withdrawn (§3).

---

## 0. Short version

> a theory can be tested against any situation, and it accumulates belief
> just like any other simple idea. The thing that makes it feel more robust
> than mere advice is that people can reproduce the situations that gave it
> belief to arbitrarily drive up or down its belief. *(stated)*

> At the same time, the theory can be absolutely wrong, outside its domain.
> Each time we look at time dilation we think, Newton is wrong. *(stated)*

> The period of time between a major hypothesis vs all hypothesis of the
> theory being rejected is the time period we experience as 'wow that's a
> major result, scientists will now go back through all the measurements and
> reason to make sure this is not a mistake and verify/reproduce the
> results.' *(stated)*

The model below states each of these as a definition or a proposition
*(analysis)*. The results are:

1. **The prediction set is exactly what the theory says without its
   auxiliaries** (Prop. 1, proved). "Theory fails" cannot be an item.
2. **A correct theory still draws red balls**, at a rate of at most the
   point test's α (Prop. 2, proved). So "reliable" has to mean "green at
   least 1 − ε of the time" for some ε larger than that α.
3. **Belief on a reproducible class can be pushed to any level short of
   certainty in finitely many draws, and never to certainty** (Prop. 3,
   proved). "Absolute truth" is the limit of this process. The limit is well
   defined, but no belief record ever reaches it. "Absolutely wrong" is the
   mirror image.
4. **Universal belief goes to zero once one reproducible class is red, and
   belief in every other class is untouched** (Prop. 4, proved for
   independent urns).
5. **The in-hand window lasts as long as the slowest item test.** For n items
   tested in parallel it grows like ln n (Prop. 5, proved under stated
   assumptions). Belief does not move in the window, while activity peaks.
6. **A false red ball has probability at most the α of the true item,
   whatever the size of the set. False greens grow with the size of the set**
   (Prop. 6, proved). This corrects open question 4 of the disjunction
   record.
7. **A first red ball works mostly as a pointer.** In an established class
   it barely moves belief. In a new class it opens an urn, and reproduction
   then empties it (Prop. 7, proved).
8. **Re-certifying a blow after a found mistake takes a second window.** The
   rerun has to be set up and run, and then every item of the new ball's set
   has to be rejected (Prop. 8, proved).

> the trace is fixed, and once a mistake is found, the ball turns green. This
> is if the theory made an explicit hypothesis in its set that said [... OR
> somebody made a mistake here OR ...] but that doesn't stop anybody from
> rerunning the trace with the corrected form and redoing the experiment.
> Which causes a real time delay between the mistake being found and the
> experiment being re-certified and re-certified as a blow at the theory
> itself. *(stated)*

**The trace is fixed** *(stated)*. Once a held or rejected item settles a
ball, the ball keeps its colour. A found mistake turns it green, because the
set said "… OR somebody made a mistake here …". Rerunning with the corrected
trace and redoing the experiment draws a new ball (D10). The time until that
ball can count as a blow is the second window (§6).

---

## 1. Objects

**D1. Theory instance.** $T$: a named dictionary at a stage.

**D2. Situation class.** $\sigma$: a setup that can be instanced again, such
as a cart on a track, a muon in a storage ring, or a block on an incline. An
instance is $s \in \sigma$, and its witness sheets are $W(s)$. The class is
**reproducible** if any agent can produce a fresh instance at finite cost.
Uranus's orbit is not reproducible on demand; a cart on a track is. A class
that can't be reproduced still yields balls. They just can't be called up at
will. How situations are grouped into classes is open (§9).

**D3. Trace.** $\tau = \mathrm{trace}(T, W(s), q)$ for a question $q$. Its
**commitments** $C(\tau) = \{A_1,\dots,A_n\}$ are every input the trace
records, namely:

- recognitions;
- bindings;
- populated sets;
- closure answers;
- every meaningful substitution;
- the fidelity commitment $A_W$: "the witness sheets describe the scene".

The trace's point prediction is $p_\tau$, with its allowance. If the trace
halts there is no $p_\tau$, and no ball.

**D4. Prediction set.**

$$
\Pi(\tau) \;=\; \{p_\tau\} \;\cup\; \{\neg A : A \in C(\tau)\}.
$$

**Prop. 1 (proved).** If the trace is a derivation, that is
$T \wedge A_1 \wedge \dots \wedge A_n \vdash p_\tau$, then

$$
T \;\vdash\; p_\tau \vee \neg A_1 \vee \dots \vee \neg A_n .
$$

*Proof.* By the deduction theorem,
$T \vdash (A_1 \wedge \dots \wedge A_n) \rightarrow p_\tau$. Rewrite the
conditional as a disjunction and apply De Morgan. ∎

Consequences:

- **The prediction set is what $T$ says without the auxiliaries.** "Theory
  fails" cannot be an item, because it is not a disjunct of anything $T$
  entails. This agrees with the disjunction record, §1.
- **The set excludes exactly one region:**
  $\neg p_\tau \wedge A_1 \wedge \dots \wedge A_n$. That region is the
  theory's empirical content for this situation.
- **One rule generates every family.** Each family in the §11 table of the
  "nobody made a mistake" record is one kind of commitment in $C(\tau)$,
  negated:
  - mistakes come from substitutions;
  - inputs and fidelity come from bindings and $A_W$;
  - missing objects come from populated interacting-forces sets. Neptune's
    item is the negation of "the forces on Uranus are those of the Sun and
    the known planets";
  - frame and approximation come from recognition inputs.

  So the generator is: walk $C(\tau)$ and negate each commitment.
  *Sketched*: the sorting of $C(\tau)$ into kinds has not been checked
  against every entry.

---

## 2. Item decisions

> Each prediction is independently a hypothesis that needs to be held or
> rejected via the usually sophisticated ways. *(stated)*

**D5.** Each item $i \in \Pi(\tau)$ has a decision
$\delta_i(t) \in \{\text{open}, \text{held}, \text{rejected}\}$. It is made by
whatever procedure the field uses for that kind of claim. The only property
of the procedure the model uses is its error rates:

$$
P(\delta_i = \text{rejected} \mid i \text{ true}) \le \alpha_i,
\qquad
P(\delta_i = \text{held} \mid i \text{ false}) \le \beta_i .
$$

The $\alpha_i$ are the item-test levels. They are not the catalogue α of
`alpha_and_the_one`; the two significance levels have different jobs
*(stated, 2026-10-16)*.

**What "held" means for each kind of item** *(analysis)*:

- For the point item, held means the observation lies within the allowance.
- For $\neg A$, held means $A$ was rejected: the mistake was found, the body
  was seen, or the sheet was shown to be unfaithful.
- $\neg A$ rejected means $A$ was upheld: the recomputation agreed, or the
  search came up empty at its detection limit.

---

## 3. The colouring rule

**D6.** The colour of the ball drawn with the fixed trace $\tau$, at time
$t$:

1. **Green**, if some item of $\Pi(\tau)$ is held: the point item, or any
   $\neg A$.
2. **Red**, if every item of $\Pi(\tau)$ is rejected.
3. **In hand**, otherwise.

This is the disjunction record's rule, §1. **The trace is fixed** *(stated)*.
A ball's set is the one its trace generated, and once the ball is green or
red it keeps that colour (decisions that get revised are open question 5).

**Why a found mistake is green** *(stated)*. The set explicitly said
"… OR somebody made a mistake here OR …". When that item holds, the
prediction as stated was right.

**What this means:**

- **Neptune.** $\neg$(forces set complete) held at Galle's sighting: green.
  Rerunning with Neptune in the trace is a new ball.
- **A found arithmetic slip.** Green. Nothing stops anyone from rerunning
  the corrected trace and redoing the experiment, but that is a new ball
  (D10).
- **A lucky match.** The point item held, and a mistake turns up later.
  Both are held items, so the ball stays green. A rerun is a new ball.

**D10. The rerun** *(stated; formalised here)*. Suppose some $\neg A_k$ held.
Let $\tau'$ be $\tau$ with $A_k$ replaced by what the holding established:
the corrected substitution, the added body, or the corrected sheet. Redoing
the experiment gives a new instance $s' \in \sigma$ and a new ball $b'$ with
set $\Pi(\tau')$, coloured by D6 on its own. If $p_{\tau'}$ misses and every
item of $\Pi(\tau')$ is rejected, $b'$ is red: the experiment has been
"re-certified as a blow at the theory itself" *(stated)*. The time this takes
is the subject of §6.

**Withdrawn.** The first version of this record had a correction clause: a
held auxiliary item corrected the trace, and the corrected trace coloured the
original ball. That conflated the original ball with the rerun. It is
recorded here so it is not reintroduced.

**Worked case: OPERA, 2011–12** *(history from memory, not checked against
sources)*:

- Relativity's point item (neutrinos are not faster than light) was
  rejected at about 6σ, and the ball went into hand (September 2011).
- In early 2012 the apparatus item held: a badly connected optical fibre in
  the timing chain. The ball turned green.
- The corrected runs (OPERA's own rerun, and ICARUS) were new balls, and
  they agreed with $c$: green.
- Belief in relativity did not move while the first ball was in hand. That is
  what the model predicts, since balls in hand carry no weight.

---

## 4. The urn

> it accumulates belief just like any other simple idea *(stated)*

The belief model is the user's *(stated, 2026-10-16)*:

- belief is Bayesian;
- each draw is a ball, green or red;
- experiments can be targeted at a theory's weak domains.

**D7.** For each situation class $\sigma$, let $\theta_\sigma$ be the
long-run fraction of green balls among the coloured draws from $\sigma$.
Belief about $\theta_\sigma$ is $\mathrm{Beta}(a_\sigma, b_\sigma)$:

- a green ball adds 1 to $a$;
- a red ball adds 1 to $b$;
- a ball in hand adds nothing.

Equivalently, the believer keeps a Pólya urn, with
$P(\text{next ball green}) = a/(a+b)$. This is Laplace's rule of succession.
Every coloured ball counts once, whichever item settled it.

**Prop. 2: the ceiling (proved, under D5–D6).** Suppose $T$ is right about
$\sigma$ and its traces are faithful. The only true item is then $p_\tau$, so
a red ball needs the point test to reject falsely:

$$
P(\text{red}) \;=\; \alpha_p \cdot P(\text{every } \neg A \text{ rejected}) \;\le\; \alpha_p .
$$

So a correct theory still draws red balls: flukes that get past the point
test and survive every check. "Reliable" therefore has to mean
$\theta_\sigma \ge 1 - \varepsilon$ with $\varepsilon > \alpha_p$. The point
test's level sets how close to 1 a perfect theory's record can get. At 5σ
that is about $3 \times 10^{-7}$; at 2σ, about 5%.

**Prop. 3: belief on tap (proved).** Start from a uniform prior. Then:

$$
\text{after } n \text{ greens:}\quad P(\theta_\sigma \ge 1-\varepsilon) = 1-(1-\varepsilon)^{n+1},
$$

$$
\text{after } m \text{ reds:}\quad P(\theta_\sigma \le \varepsilon) = 1-(1-\varepsilon)^{m+1}.
$$

More generally, the Beta–Bernoulli posterior concentrates on the true
$\theta_\sigma$. So on a reproducible class, $P(\theta \ge 1-\varepsilon)$
goes to 1 if $\theta > 1-\varepsilon$, and to 0 if $\theta < 1-\varepsilon$.

- **Any confidence level $1-\eta$ short of certainty is reachable in
  finitely many draws:**
  $n \ge \ln\eta / \ln(1-\varepsilon) - 1$.
  - $\varepsilon = \eta = 0.01$: 458 draws.
  - $\varepsilon = 10^{-3}$, $\eta = 10^{-6}$: 13,808 draws.
- **No finite record reaches certainty**, since $(1-\varepsilon)^{n+1} > 0$
  for every $n$.

---

## 5. "Absolute truth" and "absolutely wrong"

> This produces the attitude that scientists already have towards their
> theories, a representation of 'absolute truth' separate from religious,
> personal truths, seemingly more reliable. This is of course merely an
> attitude in the sense that scientists won't be able to give a
> mathematically precise sense definition of 'absolute truth'. *(stated)*

**D8. Domain and anti-domain**, at confidence $1-\eta$:

$$
\mathrm{Dom}(T) = \{\sigma : P(\theta_\sigma \ge 1-\varepsilon) \ge 1-\eta\},
\qquad
\mathrm{Anti}(T) = \{\sigma : P(\theta_\sigma \le \varepsilon) \ge 1-\eta\}.
$$

Both sets are outputs of the urns, not inputs, and both grow as classes are
reproduced.

**Reading** *(analysis)*:

- **The attitude.** "$T$ is absolutely true in $\sigma$" means two things:
  - $\sigma \in \mathrm{Dom}(T)$ for a small $\eta$;
  - $\sigma$ is reproducible, so anyone can make $\eta$ smaller at finite
    cost. Belief is on tap.

  "Absolute" names the limit $\eta \to 0$. Prop. 3 shows the limit exists,
  but no record attains it. That is why nobody can define absolute truth as
  a property: it is not the state of any belief record, but the direction
  reproduction moves in. The model describes the attitude precisely without
  making absolute truth a property of the theory. *Proved* as a statement
  about the model; *sketched* as a reading of the attitude.
- **"Absolutely wrong" is the mirror image:** $\sigma \in \mathrm{Anti}(T)$
  on a reproducible class. With time dilation, muon lifetimes and clocks
  flown on aircraft can be measured again and again, and every Newtonian
  ball comes out red. Each look is a fresh red draw. "Each time we look at
  time dilation we think, Newton is wrong" *(stated)* is Prop. 3 applied to
  red balls.
- **Both hold at once.** $\mathrm{Dom}(\text{Newton})$ contains the cart on
  the track and $\mathrm{Anti}(\text{Newton})$ contains muons in a storage
  ring. There is no contradiction, because there is one urn per class.
- **Advice and personal truth** use the same urn and the same updates. They
  differ in three ways *(sketched)*:
  1. Their situations can't be re-instanced at will (you can't rerun last
     winter). Each class gets few balls, and its posterior stays near the
     prior.
  2. They have no prediction set, so nothing turns a failure red. The tally
     is whatever the holder makes it.
  3. The draws are private, so nobody else's balls enter the urn.

  A public, reproducible class pools everyone's draws into one urn. In this
  model, that is the formal difference between "absolute" and "personal".

**Prop. 4: universality (proved for independent urns).**

$$
U(T) = P(\forall \sigma:\ \theta_\sigma \ge 1-\varepsilon) \;\le\; \min_\sigma P(\theta_\sigma \ge 1-\varepsilon).
$$

One reproducible class in $\mathrm{Anti}(T)$ drives $U(T)$ to 0. With
independent urns, belief in every other class is unchanged. "Newton is wrong"
(about $U$) and "Newton is right here" (about $\mathrm{Dom}$) are both true
of one belief state.

With a hierarchical model, classes share a population distribution with
covariates such as $v/c$. Then red balls in one class lower belief in nearby
untried classes, and that is how a domain boundary would be learned *(open)*.

**Prop. 7: a first red ball is a pointer (proved, arithmetic).**

- **In an established class, one red barely moves belief.** Going from
  $\mathrm{Beta}(10^6+1, 1)$ to $\mathrm{Beta}(10^6+1, 2)$ moves the mean
  from 0.999999 to 0.999998.
- **In a new class it moves belief a lot.** Starting from a uniform prior,
  $P(\theta \ge 0.99)$ is $10^{-4}$ after one red and $10^{-8}$ after three.

So a red ball's weight depends on which class it lands in. Its main effect
is to point at a class worth reproducing. This is why anomalies in new
regimes matter more than anomalies in well-trodden ones.

---

## 6. The in-hand window

> The period of time between a major hypothesis vs all hypothesis of the
> theory being rejected is the time period we experience as 'wow that's a
> major result …' *(stated)*

**D9.** Let the point item be rejected at $t_0$, and let $T_i$ be the time
until item $i$ is decided. The window is

$$
W = \min\big(T_{\text{hold}},\ \max_i T_i\big),
$$

where $T_{\text{hold}}$ is the first time some auxiliary item is held, at
which point the ball turns green. If every auxiliary item is rejected, the
ball turns red at $t_0 + \max_i T_i$.

**Prop. 5: length of the window (proved, under the stated assumptions).**
Suppose the $n$ auxiliary items are tested in parallel, with independent
exponential times of rate $\lambda$. Then

$$
E\big[\max_i T_i\big] = \frac{H_n}{\lambda} \approx \frac{\ln n + 0.58}{\lambda},
$$

or $n/\lambda$ if the items are tested one after another. Simulation at rate
1: $n = 5 \to 2.28$; $20 \to 3.60$; $100 \to 5.19$; $1000 \to 7.49$. In
practice the window is set by the slowest item, as with Vulcan's ~55 years of
searches.

**Consequences** *(analysis)*:

- **A theory with a richer trace takes longer to reject.** More commitments
  means more items to close. Established theories fail slowly because closing
  the set takes time, not because of error rates.
- **Belief does not move during the window**, because balls in hand carry no
  weight. What happens is the item tests:
  - re-deriving (the mistake family);
  - re-measuring and inspecting the apparatus (fidelity);
  - searching (missing objects);
  - reproducing.
- **Reproduction does two jobs.** It tests the mistake and fidelity items for
  the original ball: an independent rerun that also misses makes "the
  original was a mistake" unlikely. It also draws new balls from $\sigma$.
  That is why the window is when everyone reproduces.

### The rerun window

**Prop. 8 (proved, by D6, D9 and D10).** Suppose the first ball's window
ends at $t_1 = t_0 + T_{\text{hold}}$ because a mistake item is held, so the
ball turns green. Let $R$ be the time needed to rerun: correct the trace, then
set up and redo the experiment. If the new ball's point item misses, its own
window runs, with item times $T'_i$. A blow at the theory therefore arrives
no earlier than

$$
t_0 + T_{\text{hold}} + R + \max_i T'_i .
$$

**Consequences** *(analysis)*:

- **A real anomaly first blamed on a mistake reaches the theory later.** It
  is delayed by $R$ plus a whole second window. Each further mistake found
  along the way adds another $R$ and another window.
- **Belief can rise during the rerun window.** The first ball is green and
  the new one is not yet coloured. So in the urn, the theory has gained a
  green ball, and nothing yet counts against it.
- **A blow is a red ball on a rerun.** "Re-certified as a blow at the theory
  itself" *(stated)* means the corrected trace, run on a redone experiment,
  missed, and every item of its own set was rejected.

---

## 7. Errors of colouring

**Prop. 6 (proved).**

**(a) False red.** If some item $j$ is true, a red ball requires rejecting
$j$, so $P(\text{red}) \le \alpha_j$. Hence

$$
P(\text{false red}) \;\le\; \min_{j \text{ true}} \alpha_j ,
$$

whatever the size of the set. When $T$ is right and the trace faithful, this
is Prop. 2. Simulation with $\alpha_p = 0.05$ and $\beta = 0.02$:

| auxiliary items | false-red rate |
|---|---|
| 1 | 0.049 |
| 10 | 0.042 |
| 50 | 0.019 |

**(b) False green.** If every item is false, the union bound gives

$$
P(\text{green}) \;\le\; \sum_i \beta_i .
$$

Simulation with $\beta = 0.01$:

| items | false-green rate |
|---|---|
| 10 | 0.096 |
| 100 | 0.63 |

**This corrects open question 4 of the disjunction record**, which says a red
ball's error rate "can approach n·α". The multiplicity lands on green, not on
red. The record's conclusion still stands ("a large, well-generated prediction
set is hard to colour red by accident"); (a) gives the reason.

Because a held auxiliary item turns the ball green directly, false greens
from the mistake family are real: a mistake that wasn't one, believed found,
gives a green ball. The rerun is where this gets caught. The corrected trace
carries the false correction as one of its own commitments, so the false
correction is an item in the new ball's set.

---

## 8. What this changes in earlier records

Nothing is edited in place. These are the readings this record proposes.

| Earlier claim | Where | Reading now |
|---|---|---|
| Green: "some item holds" | disjunction record §1 | Stands, for every item, auxiliary ones included; the trace is fixed (user, 2026-11-01). A rerun with the corrected trace is a new ball (D10) |
| A red ball's error "can approach n·α" | disjunction record, open Q4 | Replaced by Prop. 6: at most the α of the true item; multiplicity affects green |
| Completeness and generation of the set | disjunction record, open Q5 | Prop. 1 plus the generator rule: negate each commitment in $C(\tau)$ |
| A found mistake: green, or credited elsewhere? | "nobody made a mistake", open Q4 | Green (user, 2026-11-01). A rerun with the corrected trace and a redone experiment is a new ball, after a real delay (D10, Prop. 8). The dossier credit in §8 item 4 there is a separate matter and is unaffected |
| The belief layer (urn) is in no file | disjunction record §7 table | This record |

---

## 9. Open questions

1. **How situation classes are individuated.** There is one urn per class,
   so the number of urns matters as much as the counts in them. A candidate
   *(speculation)*: the classes are what the catalogue α admits. That would
   be one place where the two significance levels meet.
2. **Items that span moments.** Per-moment traces can't state "one body at
   every moment" (disjunction record, Q1). The model treats Uranus's orbit as
   one draw with one trace, so a trace over time is needed.
3. **Hierarchical urns.** How does belief carry over to untried classes?
   This is `theories_and_belief`'s "belief at inputs nobody has tried".
4. **The rerun's class.** Is a redone experiment always an instance of the
   same class $\sigma$, or can the correction change which class it belongs
   to (an added body, a corrected sheet)?
5. **Revised decisions.** The model treats item decisions as final, but real
   decisions get revisited.
6. **Correlated item tests.** Shared apparatus breaks the independence used
   in Prop. 5's simulation and in the product in Prop. 6(a).
7. **A weak point test colours green cheaply.** If the allowance is so wide
   that the point test could not have rejected, a held point item tells
   nothing. Should "held" carry a power condition? The haze and allowance
   notes are the place to look.

---

## Formal handles *(analysis; not checked against primary sources)*

- **Beta–Bernoulli updating, Laplace's rule of succession, the Pólya urn:**
  the standard machinery under D7 and Prop. 3.
- **Prop. 1** is the standard form of the Duhem–Quine point: a theory meets
  observation only together with its auxiliaries. What the VD adds is that
  the auxiliaries are read off a trace, so they are finite and fixed before
  the test.
- **Lakatos (1970)** tells an imaginary-planet story with the same shape as
  Neptune.
- **Dorling (1979) and Strevens (2001)** treat auxiliary blame in Bayesian
  terms by putting priors on the auxiliaries. This model differs on purpose:
  colouring is done by item tests, and belief counts only coloured balls
  *(stated, 2026-10-16)*.

---

## Provenance

**The idea is the user's**, stated in the message of 2026-11-01:

- a theory can be tested against any situation and accumulates belief like
  any simple idea;
- reproducing the situations lets people drive belief up or down at will,
  which produces the "absolute truth" attitude, separate from religious and
  personal truths;
- that attitude has no mathematically precise definition;
- a theory can be absolutely wrong outside its domain (time dilation);
- a ball is red when every item of the prediction set is rejected, each item
  being a hypothesis held or rejected by the field's usual methods;
- the window between rejecting the major hypothesis and rejecting all of
  them is the "major result, check and reproduce" period.

The user's correction, later the same day:

- the trace is fixed;
- once a mistake is found, the ball turns green, because the set explicitly
  said "… OR somebody made a mistake here OR …";
- rerunning with the corrected trace and redoing the experiment is still
  possible;
- there is a real delay between finding the mistake and re-certifying the
  experiment as a blow at the theory.

The belief model was stated earlier, on 2026-10-16: Bayesian belief, an urn
of green and red balls, targeted experiments, colouring by hypothesis tests,
and two distinct significance levels.

**Analysis that arose in writing this record:**

- the definitions D1–D10 (D10 formalises the user's rerun);
- Props. 1–8;
- the correction clause of the first version, withdrawn after the user's
  correction;
- the domain and anti-domain sets, and the reading of the attitude as a
  limit;
- the three-way difference from advice;
- the OPERA example;
- the correction to open question 4;
- the open questions;
- the simulations.

**Checks.** The script
`C:\Users\canva\AppData\Local\Temp\claude\C--Users-canva--claude-spares-spare-rtQFxg\c76f2391-3ca1-45e7-abf9-19613079ce34\scratchpad\checks\colouring_checks.py`
(run 2026-11-01 with `py -3 -I`) checks:

- the closed form of Prop. 3 against Beta sampling (0.9514 against 0.9513 at
  $n = 300$, $\varepsilon = 0.01$);
- the draw counts in Prop. 3;
- the arithmetic of Prop. 7;
- $H_n$ against simulated maxima for Prop. 5;
- the false-red and false-green rates of Prop. 6.

**Placement.** `inbox/` for sorting; probably `Theory/`, beside the
disjunction record and `witness_sheets/`. Whether it binds to the disjunction
record as a correction is the sorter's call.
