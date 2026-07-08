# Norton's Dome: A VD Resolution

**Status:** rough explanation, v0 — whiteboard grade throughout.
Nothing here is encoded as entries yet; every claim below is a
candidate for encoding and should be treated as smuggle-suspect until
it survives that pass.
**Project:** VD Newton / admissibility rules, domain gate
**Date:** 2026-07-05
**Provenance:** conversation-derived. Standing literature: Norton
(2003), Malament, Korolev, Fletcher on the dome; Born, Gisin/Del Santo
on finite-information classicality; Werndl on observational
equivalence. The discursive points below mostly exist in that
literature; the structural claims (certificate taxonomy, address
assignments, constitutional trichotomy) are the VD contribution.

---

## 0. The scenario

A point ball rests at the apex of a frictionless dome shaped so that
the tangential force at arc-distance `s` from the apex is

```text
F(s) = m·k·s^(1/2)
```

Newton's second law then admits, from the initial condition
`(s, ṡ) = (0, 0)`, the eternal-rest solution **and** a two-parameter
family of spontaneous excitations:

```text
s(t) = 0                      for all t
s(t) = C·(t − T)^4            for t ≥ T, any T, any direction φ₀
```

No force acts at the moment of excitation; nothing selects T or φ₀.
The standard gloss: Newtonian mechanics is indeterministic.

The resolution is not one move but a stack of them, each at a
different address. That the addresses are different **is** the
resolution.

---

## 1. What is not violated (clearing the ground)

**Newton II.** Holds pointwise on every branch. Once `s > 0` a real
tangential force pays for every unit of momentum. The pathology is in
the *uniqueness theory* of the equation, not in the equation.

**Newton I.** Never engaged. The ball is not a free particle — see §2.

**Momentum.** Exact on every branch. Two-body treatment (dome mass M
free on a frictionless floor): the dome's position X is cyclic, its
Euler–Lagrange equation *is* momentum conservation, and the reduced
equation of motion is

```text
s̈ = ((M+m)/M) · k·s^(1/2)
```

Finite M rescales the coefficient and touches nothing else. The
non-Lipschitz germ survives every M > 0; the indeterminism does not
lean on M → ∞. The knife-edge is in phase space, not parameter space.

**Angular momentum.** L_z conserved and zero; forbids spontaneous
spiralling; forces excitation to be purely radial. Conservation here
*shapes* the solution family rather than failing to.

**Energy.** The profile is tuned so the height drop pays the kinetic
bill order by order: `r ∝ (t−T)^4` gives `v² ∝ (t−T)^6 ∝ y`.

**The structural fact under all four:** every conserved charge is zero
on every branch. The entire solution family lives on a single level
set `(E, P, L) = (0, 0, 0)`. Conservation laws are first integrals —
they stratify solution space and confine trajectories to leaves; they
are constitutionally incapable of distinguishing trajectories *within*
a leaf. The dome's degeneracy is intra-leaf by construction. Asking
momentum conservation to rule out spontaneous excitation is asking a
constant of motion to do a uniqueness theorem's job.

Sharper: the excitation parameters (T, φ₀) are exactly the elements of
the symmetry group fixing the initial state (time translation,
rotation about the axis). The solution family is a **group orbit** —
classical spontaneous symmetry breaking. Noether charges are built
from those very symmetries, so the degeneracy directions are precisely
the directions the charges cannot see. The indeterminism hides in the
only place conservation laws can't look: the interior of their own
level sets, along the orbits of their own generating group.

---

## 2. The certificate taxonomy (the Newton-I move)

The load-bearing distinction, syntactic vs semantic:

```text
free particle        interaction list is EMPTY
                     a property of the ledger; decidable by
                     inspection, no arithmetic

balanced particle    interaction list is nonempty; the SUM of the
                     entries evaluates to zero at this configuration
                     a property of an evaluation
```

Empty sum vs cancelling sum. Norton's ball is the second kind —
enrolled ({normal, weight}), permanently subject to NIII bookkeeping —
and never earns the first certificate.

Why this has teeth: a free particle's force function is zero *as a
function* — trivially Lipschitz — so Picard–Lindelöf applies and rest
is the unique solution. The free-particle certificate carries a
uniqueness **guarantee** for free. An enrolled-balanced particle has
zero as a *value*; uniqueness is now **contingent** on the germ of the
force function at the rest point:

```text
bowl bottom    F ∝ −s          Lipschitz      unique     (tame)
dome apex      F ∝ +s^(1/2)    non-Lipschitz  non-unique (pathological)
```

The enrolled-balanced category contains both; the Lipschitz condition
is the separate rule that decides its members. Two-tiered structure:
losing the free-particle certificate makes uniqueness contingent; the
non-Lipschitz germ cashes the contingency.

This slots directly into the Nothing-path branching: evaluation
branches on the interaction *list* (empty → NI triplet, categorical),
never on the force *value* (nonempty → NII evaluation, even when the
sum is zero at an instant). A formalism that branched on the value
could not *state* the distinction and could not express why one case
is guaranteed and the other isn't. It also dissolves the old ambiguity
in Newton I: "no forces act" and "zero net force" are usually treated
as interchangeable; the dome is where they come apart.

Three certificate types, three jobs:

```text
free-particle    (empty list)      GUARANTEES uniqueness, axiomatically
Lipschitz        (germ regularity) DECIDES uniqueness, contingently
conservation     (Noether charges) STRATIFIES the solution set;
                                   certifies consistency; cannot
                                   select within a stratum
```

The dome is the scenario where the first two fail and the third,
working perfectly, catches nothing — because there is nothing of its
type to catch.

---

## 3. Where the pathology lives (and where it doesn't)

**Not in contact forces.** Strip the dome: a particle on a line in
field `F(x) = mk·|x|^(1/2)·sign(x)` has the identical germ and
identical non-uniqueness with no contact anywhere. The ODE doesn't
know it came from a constraint problem.

**Conservation of pathology.** Try to source that field physically
(Poisson): `ρ ∝ ∇²V ∝ −|x|^(−1/2)` — divergent source density at the
rest point. Same exponent as the dome's apex curvature
`d²h/dr² ∝ r^(−1/2)`. Removing the contact force migrates the
singularity from constraint geometry to source density; it never
eliminates it. Smooth, bounded sources produce analytic (hence
Lipschitz) potentials at the field point: a non-Lipschitz germ must be
*paid for* with a singularity somewhere upstream.

**Trichotomy of origins:**

```text
singular geometry       dome (apex curvature)          unbuildable
singular sources        field version (divergent ρ)    unbuildable
lossy coarse-graining   Torricelli ḣ = −k√h;           buildable —
                        Coulomb friction ∝ −sign(v)    singularity is
                                                       in the
                                                       DESCRIPTION,
                                                       not in matter
```

Only the third is realizable, because only the third locates the
singularity in the reduced description. Finite-time arrival at
equilibrium (draining bucket, stopping puck) is logically equivalent
to non-uniqueness of the time-reversed problem. Determinism holds at
the fundamental description level and can be *lost in translation* to
effective laws — the lossy-readout diagnosis, with a uniqueness
certificate as the dropped node.

**VD address assignment.** The Lipschitz rule attaches to the *force
entry's germ at equilibria*, agnostic to mechanism — NOT to any
interaction-candidate category (the dome and its field twin have
disjoint interaction inventories and the identical pathology).
Status-tier note: plausibly LOCKED for fundamental force entries
(smooth-source theorem above), DUBIOUS-at-best for effective ones —
so the ledger must *mark* coarse-grained entries; the marking is
load-bearing for whether the uniqueness guarantee survives.

---

## 4. The tolerance floor (the trackability move)

Two distinct walls, not to be conflated:

```text
domain gate      trackability — re-identification of points through
                 time. The dome PASSES this: one ball, the block case,
                 every branch a perfectly good track. Fails at
                 identical particles (QM boundary).

Lipschitz rule   regularity of the force germ. The dome FAILS this.
                 Dynamics territory (NML3), not the gate.
```

But the trackability layer touches the dome through the **continuum
surplus**: tracks in the formalism are real-valued curves carrying
infinite information; every actual tracking procedure — any cameras,
any densification — delivers finitely many bits. The tolerance floor
is permanent (resolution residue). The formalism's determinism claim
is conditional on continuum-precision initial data that no finite-
information procedure certifies (Born's old point; Gisin/Del Santo's
program). Chaos makes every generic system dome-like beyond its
Lyapunov horizon; the dome is the degenerate limit — non-Lipschitz as
"infinite Lyapunov exponent at a point," divergence in zero time.

**Verdict at this wall:** the dome's premise, `(s, ṡ) = (0, 0)`
exactly, is **not a certifiable wall input**. It lives strictly below
every tolerance floor, where the framework's own rule says claims are
meaningless. The pathology is not caused by the trackability layer; it
is *quarantined* by it. NM never issues a wrong prediction here — it
issues no scoreable prediction at all, on an input no one can prepare.

---

## 5. Quantization cures it (the QM move, correctly aimed)

The potential `V ∝ −|x|^(3/2)` is continuous and bounded below by
`−c(1+x²)`, so the Schrödinger operator is essentially self-adjoint
(Faris–Lavine): **unique unitary evolution**, every initial state, no
branching, no T. Quantum evolution is *more* deterministic than the
classical dome. The Lipschitz pathology does not survive quantization,
because Schrödinger dynamics is linear and indifferent to the
regularity of ∇V in the way Newtonian characteristics are not.

Structural mismatch with quantum chance: QM's indeterminism comes with
a measure (Born rule); the dome's solution family carries **no measure
at all** — no probability over T, over φ₀, or over excitation vs rest.
A branching without a measure is not proto-quantum; it is not the same
kind of object.

What genuinely points at QM is the **floor, not the indeterminism**:
the procedural tolerance floor (tracker noise) is promoted to a floor
supplied by nature (ℏ; phase-space cells; finitely many
distinguishable states per bounded region). The dome's initial
condition — exact position AND exact zero momentum — is not merely
uncertifiable in QM; it is *forbidden*. And ψ does not supply the
missing sub-floor track information (on the information axis it is
heavier, not lighter, than the tracks it replaces); it declares the
missing information **nonexistent**. QM's two verdicts on the dome:

```text
knife-edge question    "exactly at rest exactly at the apex —
                       when does it leave?"
                       → DISSOLUTION (the premise names no state)

floored question       "wavepacket localized near the apex within
                       Δx·Δp ~ ℏ — where at time t?"
                       → BORN MEASURE (unique, scorable)
```

---

## 6. The constitutional reading

Science's canonization mechanism — selection on realized predictive
success — cannot elevate a theory-region that issues no scorable
output. Precisely:

**The canon selects for scorability, not for determinism.** A scorable
output is a probability measure over outcomes; determinism is the
special case of the delta measure. QM was canonized *while asserting
indeterminism* because the Born rule norms; the dome offers a
possibility set with no measure — the constitutional defect is not
"fails to determine" but "fails to norm." A theory may say *chance*;
it may not say *shrug*.

**But the dome is selection-invisible.** Its premise is unpreparable
(sub-floor, ℏ-forbidden), so no trial, no scoring event, no selection
pressure — the mutation is fitness-neutral. The empirical chamber
alone would never expose it. The constitution therefore has a second
chamber: **admissibility norms** (well-posedness, regularity,
Hadamard), enforced a priori, filtering theories before they reach
scoring. The Lipschitz condition is such a provision — enforced for
centuries, written down never.

**The VD, in this vocabulary, is an explicit constitution**: the rule
ledger is canonization machinery made mechanical; admissibility rules
are the a priori chamber; the residue system prices what the empirical
chamber can and cannot see. The dome then gets the constitutionally
correct treatment — barred by an explicit admissibility entry rather
than surviving indefinitely in the empirical chamber's blind spot.
That the informal constitution enforced this rule invisibly and the VD
forces it onto the books is the publication sentence.

**Completed-inquiry output trichotomy** (mirroring §2's certificate
trichotomy one level up — recurrence noted, unexplained, chase it):

```text
delta measure     deterministic answer
proper measure    probabilistic answer (Born-style)
dissolution       ill-posed question; premise rejected
```

**Horizon fact.** Even the completed constitution pins the canon only
up to sub-floor equivalence (Werndl: deterministic and indeterministic
descriptions can be observationally equivalent). "Is nature really
deterministic beneath the floor" is not unanswered but *unaskable in
the canon's language* — the resolution residue, promoted to the
constitutional level. Determinism was never a canonizable claim; only
scorability was, and the delta measures were an accident of which
questions sat above the floor.

---

## 7. The resolution, compactly

```text
NI          not engaged: the ball is enrolled-balanced, not free.
            Empty list ≠ cancelling sum; branch on the list.
NII         holds pointwise on every branch; pathology is in the
            uniqueness theory, not the law.
P, L, E     exact on every branch; all charges zero; the whole family
            sits on one level set. Conservation stratifies, never
            selects. Degeneracy = orbit of the stabilizer group =
            exactly what Noether charges cannot see.
Lipschitz   the unwritten admissibility rule; attaches to the force
            germ at equilibria, not to any interaction category.
            Non-Lipschitz germs must be paid for: singular geometry,
            singular sources, or coarse-graining — only the last
            buildable.
Floor       the premise is sub-tolerance, hence not a certifiable
            wall input; quarantined, not caused, by trackability.
            Chaos generalizes; the dome is the zero-time limit.
QM          promotes the floor to nature (ℏ), forbids the premise,
            evolves uniquely (essential self-adjointness), answers
            the floored question with a measure and the knife-edge
            question with dissolution.
Canon       selects scorability, not determinism; the dome is
            selection-invisible, so it is barred by the a priori
            chamber — the admissibility rule the VD makes explicit.
```

Norton's dome is not a counterexample to determinism *in* Newtonian
mechanics; it is a counterexample to the claim that Newtonian
mechanics ever wrote down all of its own rules. The VD's job is to be
the place where they get written down.

---

## 8. Edits owed (not performed here)

```text
rule ledger      new entry: Lipschitz admissibility on force-entry
                 germs at equilibria. Tier: LOCKED for fundamental
                 entries, DUBIOUS for effective/coarse-grained ones;
                 requires a coarse-grained marker on force entries.

domain gate §0   second failure clause: precision floored always,
                 provenance upgrading procedural → natural (ℏ) at the
                 quantum boundary. Distinct in character from the
                 re-identification clause; same address.

tolerance §1     third source line: "from nature, at the boundary of
                 the domain."

encoding pass    the whole note is whiteboard-grade until the dome is
                 encoded as entries and the branch structure (empty
                 list vs cancelling sum) is verified to produce §7
                 mechanically. The VD's own standard: whiteboard
                 arguments are where assumptions get smuggled.
```
