# Participant-Symmetric Canonical Orientation — Meshing Note

## Half-Weighted Gravity Signs, the Surviving Convention Wall, and σ(f) in the Trace

**Status:** working meshing note, d2. Claude-authored at user request,
2026-08-15, in VD-docs.
**Supersedes:** `VD_PARTICIPANT_SYMMETRIC_CANONICAL_ORIENTATION_MESHING_d1.md`
(same day; see Part VIII for what changed and why).
**Project:** VD Newton (Newton-analysis incubator)
**Parents:**

- `Newton-analysis/participant_symmetric_forces/VD_PARTICIPANT_SYMMETRIC_FORCES_OWNER_BLIND_ACTIVATION_AND_HALF_WEIGHTING_d2.md`
- `Newton-analysis/canonical_force_orientation/CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14_d1.md`
- `Newton-analysis/action_reaction_asymmetry/ACTION_REACTION_CONSTITUTIVE_ASYMMETRY_SKETCH_d1.md`

---

## 0. Purpose and one-paragraph result

The canonical-force orientation note establishes that $A=-R$ supplies
opposition but not orientation: a convention must select which member of the
pair is quoted as canonical, and the note's open question 4 asks how
symmetric mechanisms such as gravity supply that convention when neither
participant is a privileged constitutive carrier. The half-weighting note
establishes that participant-symmetric kinds are represented from both
participant-owned sides, each side carrying half the pair force.

This note meshes the two. The result, in two halves:

> **Discharged by ownership:** which representations exist (both), what
> anchors each (its owner), the pairing of members within each instance, and
> the weight ($\tfrac12$, fixed at design time by the closure theorem). No
> pair-ledger and no arbitrary *existence* choice survive.
>
> **Not discharged — the wall survives:** within each owned instance, which
> member is quoted (computed) and which is obtained by negation remains a
> two-way human choice. It leaves every target-side *value* unchanged but
> changes the *trace*, and the trace is what the VD grades. The convention is
> therefore a genuine runtime input in both acting-object branches, and
> $\sigma(f)$ appears in every trace as the per-occurrence shadow of the
> declared convention.

Under the **declared standard convention** (quote the action side; separation
unit vector oriented owner → non-owner):

$$A_{\text{gravity}} = -\frac{Gm_om_n}{2r^2}\,\hat{\mathbf r}
\qquad\text{(quoted; on the non-owner)}$$

$$R_{\text{gravity}} = +\frac{Gm_om_n}{2r^2}\,\hat{\mathbf r}
\qquad\text{(negated; on the owner)}$$

The minus sign belongs to the action **by declaration**, not by structural
necessity — the note recommends this declaration and says why, but the
recommendation is the content of a wall input, not a theorem.

---

# Part I — The two inputs

## 1. From the half-weighting note

For a participant-symmetric atomic kind $G$ (gravity, point-charge Coulomb,
closed-system magnetostatics):

- $\operatorname{Condition}_G$ inspects only the non-owner;
  $V_G(\text{owner},\text{non-owner})$ may inspect both.
- Same-kind reciprocity plus owner-blindness give the closure theorem:
  owner class $=$ target class, so **both** participants own an instance,
  $G_o$ and $G_n$, always.
- One physical pair interaction is therefore represented twice on each
  target, and each representation carries weight $\tfrac12$.

## 2. From the convention note

For one active binary interaction $i$ with participants $P(i)$, a convention
$C$ supplies a canonical recipient $c_C(i)\in P(i)$ and a canonical vector
$K_C(i)$, and the evaluator returns

$$
V_C(i,p)
=
\begin{cases}
K_C(i), & p=c_C(i),\\[4pt]
-K_C(i), & p\in P(i)\setminus\{c_C(i)\},\\[4pt]
\text{undefined}, & p\notin P(i).
\end{cases}
$$

An *independently named fixed* sign function $\sigma(f)$ was rejected as a
wall because a fixed piecewise function is not a runtime input; the working
principle is that **every wall exposes an input**. Open question 4 of that
note: what supplies the input for symmetric mechanisms? Open question 8: how
should a trace display convention provenance?

---

# Part II — The meshing: what ownership discharges, and what it does not

## 3. Per instance, there is a privileged anchor

The convention note is right that the *interaction* has no privileged
participant in the symmetric case. But under the participant-symmetric
architecture the interaction is never evaluated as a bare interaction; it is
evaluated through its two owned instances, and each **instance** has a
privileged side by type: the owner. The constitutive-asymmetry template maps
onto each owned instance with the owner in the carrier role.

This is a real structural discharge, but of a *narrower* item than d1
claimed. What ownership fixes:

```text
which representations exist        -> both (closure theorem)
what anchors each representation   -> its owner
which members belong to one instance -> the instance's action/reaction pair
the weight                          -> 1/2, design-time constant
```

No ledger of processed pairs, no arbitrary choice of which side gets a
representation. That elimination stands.

## 4. The two-way assignment survives inside each instance

What ownership does **not** fix: within one instance, which member is the
quoted (computed) one. Both assignments are admissible:

```text
Declaration 1 (action-quoted):
    quote  K  = the member on the non-owner  (spring analogue: F = -kx)
    derive -K = the member on the owner, by negation

Declaration 2 (reaction-quoted):
    quote  K' = the member on the owner      (spring analogue: F = +kx)
    derive -K' = the member on the non-owner, by negation
```

Every target-side value is identical under the two declarations. If that
were the whole story the choice would be idle. It is not the whole story,
because the two declarations produce **different traces**: a different
formula is quoted, the constitutive (or joint-state) computation lands on a
different member, and the negation step sits in a different place.

## 5. Why trace-difference makes it a wall

The VD's operative standard is behavioural: an entry is judged by the traces
it triggers, and a determination that admits no shortcut is treated as fact.
The complement also binds: **a choice that could have gone the other way,
must be held consistent across an account, and must be known by anyone
grading the trace, is a runtime human input.** The quoting orientation is
exactly such a choice — the arbitrariness is the proof of its conventional
status, and its trace-visibility is the proof that it cannot be silently
absorbed. By the principle that every wall exposes an input, it keeps its
wall.

So the impressed-force chimney's third corner — the canonical-orientation
convention — is present in **both** acting-object branches. The symmetric
branch is special only in this narrower sense: its target-side *values* are
convention-invariant (because both instances always exist and their halves
are equal per target), while its *traces* are not.

## 6. σ(f) rehabilitated as the trace-shadow of the declaration

The convention note's rejection of $\sigma(f)$ stands in its original scope:
a *fixed* sign function, hard-coded, is an implementation detail and earns no
wall. But once the convention is a declared runtime input, each force
occurrence in a trace carries a derived per-occurrence sign

$$
\sigma(f)=
\begin{cases}
+1, & f \text{ is the quoted member under the declared convention},\\
-1, & f \text{ is the negated member},
\end{cases}
\qquad
V(f)=\sigma(f)\,K,
$$

and $\sigma(f)$ **must appear in the trace**: it is how the trace displays
which member was computed and which was derived, i.e. it is the convention's
provenance mark. The wall exposes the declaration; $\sigma(f)$ is the
declaration's shadow on each member line. This answers the convention note's
open question 8: a trace displays convention provenance by tagging each
member with its $\sigma$ and citing the declaration that induced the
tagging. Two traces under opposite declarations are then mechanically
comparable — flip every $\sigma$ and the quoted/derived roles, and the
target-side values must match.

---

# Part III — Gravity, vectors figured out

## 7. Definitions

One gravity instance $G_o$: owner $o$, mass $m_o$, position $\mathbf r_o$;
non-owner $n$, mass $m_n$, position $\mathbf r_n$. Orient the separation
**owner → non-owner**:

$$
\mathbf r = \mathbf r_n - \mathbf r_o,
\qquad
r = \lVert\mathbf r\rVert,
\qquad
\hat{\mathbf r} = \mathbf r/r.
$$

The full ordinary pair force on the non-owner is the textbook form:

$$
\mathbf F_{o\to n}
=
-\frac{Gm_om_n}{r^2}\,\hat{\mathbf r}
=
Gm_om_n\,
\frac{\mathbf r_o-\mathbf r_n}{\lVert\mathbf r_o-\mathbf r_n\rVert^3},
$$

minus because attraction pulls $n$ back toward $o$.

## 8. The two members under the declared standard convention

Declaration 1 (action-quoted) is adopted as the standard:

$$
\boxed{
A_{\text{gravity}}
=
V(\operatorname{action}(G_o,n))
=
-\frac{Gm_om_n}{2r^2}\,\hat{\mathbf r},
\qquad \sigma=+1
\quad\text{(quoted; on the non-owner)}
}
$$

$$
\boxed{
R_{\text{gravity}}
=
V(\operatorname{reaction}(G_o,o))
=
+\frac{Gm_om_n}{2r^2}\,\hat{\mathbf r},
\qquad \sigma=-1
\quad\text{(negated; on the owner)}
}
$$

In absolute positions:

$$
A_{\text{gravity}}
=
\frac{Gm_om_n}{2}\,
\frac{\mathbf r_o-\mathbf r_n}{\lVert\mathbf r_o-\mathbf r_n\rVert^3},
\qquad
R_{\text{gravity}} = -A_{\text{gravity}}.
$$

Under Declaration 2 the same two vectors appear with quoted/derived roles
and $\sigma$ tags exchanged; all four target-side values in §11 are
unchanged.

## 9. Why the standard declaration is recommended

Three reasons — now offered as grounds for a *declaration*, not as a proof:

1. **Template fit.** The action is the constitutively computed member of the
   asymmetry sketch's template and lands on the non-owner; attraction pulls
   the non-owner toward the owner, the $-\hat{\mathbf r}$ direction under
   owner-anchored orientation.
2. **Textbook continuity.** The owner occupies the source role, so the quoted
   canonical formula is the familiar $-({Gm_1m_2}/{r^2})\,\hat{\mathbf r}$
   with $\hat{\mathbf r}$ source → test mass — halved. Nothing about the
   quoted form has to be relearned.
3. **Uniformity across branches.** The spring's standard quoting $F=-kx$ is
   action-quoted (the carrier's force on the body). Declaring action-quoted
   everywhere gives one rule for both architectures.

The opposite declaration is fully admissible — that admissibility is what
makes this a wall input — it is merely nonstandard on all three counts.

## 10. Coulomb, for contrast

Same structure; the sign is carried by the coupling product rather than by
the architecture:

$$
A_{\text{coulomb}}
=
+\frac{q_oq_n}{8\pi\varepsilon_0 r^2}\,\hat{\mathbf r},
\qquad
R_{\text{coulomb}} = -A_{\text{coulomb}}.
$$

Like charges ($q_oq_n>0$): the action pushes the non-owner away from the
owner, along $+\hat{\mathbf r}$. Unlike charges: signs flip and the form
matches gravity's. The declaration machinery is identical.

---

# Part IV — Verification

## 11. Totals per target

The other instance $G_n$ runs the same rule with roles exchanged
($\hat{\mathbf r}_{n\to o} = -\hat{\mathbf r}$):

| occurrence | lands on | $\sigma$ | value |
|---|---|---|---|
| action of $G_o$ | $n$ | $+1$ | $-\dfrac{Gm_om_n}{2r^2}\,\hat{\mathbf r}$ |
| reaction of $G_n$ | $n$ | $-1$ | $-\dfrac{Gm_om_n}{2r^2}\,\hat{\mathbf r}$ |
| action of $G_n$ | $o$ | $+1$ | $+\dfrac{Gm_om_n}{2r^2}\,\hat{\mathbf r}$ |
| reaction of $G_o$ | $o$ | $-1$ | $+\dfrac{Gm_om_n}{2r^2}\,\hat{\mathbf r}$ |

Sums: $-({Gm_om_n}/{r^2})\,\hat{\mathbf r}$ on $n$ and
$+({Gm_om_n}/{r^2})\,\hat{\mathbf r}$ on $o$ — the full textbook pair,
equal and opposite. ✓ Note each target receives one $\sigma=+1$ and one
$\sigma=-1$ member of equal vector value: the $\sigma$ column is invisible in
the sums and indispensable in the trace.

## 12. The value-level convention-free form

The table exposes something stronger than the totals: **the two members
landing on any one target are equal vectors.** A fully local,
declaration-free statement of every gravity member's *value* is therefore
available:

> Every gravity member in target $p$'s account has value
>
> $$\frac{Gm_om_n}{2r^2}\,\hat{\mathbf r}_{p\to q},$$
>
> where $q$ is the other participant: half strength, pointed at the other
> participant, and there are exactly two of them.

This is a statement about values only. The members' quoted/derived roles —
their $\sigma$ tags — are **value-invisible but trace-visible**, and the
trace-visibility is what keeps the convention wall standing (§5). d1's term
"evaluation-invisible" was too strong and is retired.

## 13. NML3 case instantiation

The two members on one target are **distinct force-instances with equal
vector values** — distinct because their acting-object-instance identities
differ ($G_o$ vs $G_n$). This physically instantiates the NML3 explication's
behavioural case "distinct equal-valued forces both remain" (and the open
problem's test E) in *every* gravitational pair, not as an exotic
possibility. Any identity scheme that collapses equal-valued members merges
the two halves into one and loses half the force. This is direct pressure on
NML3 open item 6 toward instance-carried identity.

## 14. Against the convention note's test battery

- **Convention reversal** (§9.1): flip the declaration (and/or the
  $\hat{\mathbf r}$ anchoring) — quoted/derived roles and every $\sigma$
  exchange, all four table values unchanged. Pass.
- **Equal-and-opposite underdetermination** (§9.2): given only $A=-R$, the
  evaluator must refuse to orient until a declaration is supplied. Under d1's
  reading this test was trivialized for the symmetric branch; under the
  corrected reading it applies with full force — the declaration is still a
  required input, and the evaluator's refusal is correct behaviour. Pass.
- **Interaction-before-value** (§9.3): admission of both instances uses only
  $\operatorname{Own}_G$ and $\operatorname{Condition}_G$; no value and no
  declaration are needed for membership. Pass.
- **Invalid target** (§9.5): a nonparticipant fails
  $\operatorname{Condition}_G$'s incidence and receives *undefined*, not
  $-K$. Pass.

---

# Part V — The wall, stated for both branches

## 15. One convention wall, two branches

```text
constitutive-carrier branch (spring, contact, actuator):
    one representation, full weight
    declaration selects quoted member    (F = -kx vs F = +kx)
    sigma(f) tags computed vs negated in the trace

participant-symmetric branch (gravity, Coulomb, closed magnetostatics):
    two representations, weight 1/2 each
    declaration selects quoted member within each instance
    sigma(f) tags computed vs negated in the trace
    additionally: target-side values are declaration-invariant
```

The wall input is the same kind of object in both branches — a human
declaration of quoting orientation — which restores the uniformity of the
impressed-force chimney: {impressed-force $V(f)$, canonical-force
acting-object, canonical-orientation convention} applies unmodified to the
symmetric branch. d1's claim that the third corner was structurally
discharged there is withdrawn.

## 16. Weight as a branch attribute

The evaluator needs one further datum per acting-object kind: which
architecture it belongs to, hence which weight applies. The weight is fixed
at design time by the closure theorem (multiplicity is exactly two for the
symmetric branch, always); it is not a runtime count and not
account-dependent. But the branch classification must be locally decidable
from the kind itself, or a trace could apply the wrong weight without
visible failure. This is the half-weighting note's open question 3 wearing
operational clothes — and it is a *classification* datum, not a
*convention* input: no admissible alternative exists once the kind is fixed,
so it earns no wall of its own.

That contrast is worth stating as a rule of thumb the two notes now share:

> **Arbitrariness diagnoses the wall.** Where two assignments are admissible
> and traces differ, there is a human input and it must be walled
> (declaration). Where the theorem fixes the datum, there is no input and no
> wall (weight).

---

# Part VI — The algorithmic rationale, recorded

## 17. Three algorithms

This argument arose in discussion (2026-08-15) and is not recorded
elsewhere; it belongs here because it is the *reason* the meshing comes out
clean.

**(a) Field/per-target (conventional).** Force on each target $=$ its
coupling $\times$ the fields of all *others*. Stateless — but reactions are
never constructed, so $A=-R$ degrades to an unrepresented coincidence; each
participant appears in two unrelated roles (source, receiver) with the
coincidence that one mass serves both left brute; and an explicit
$j\neq i$ self-exclusion clause is required.

**(b) Pair-based with N3 (conventional).** Enumerate pairs; per pair, choose
a source, compute the action, negate for the reaction. Keeps the pair
ontology — but demands an **arbitrary side choice** that corresponds to no
physical datum in the symmetric case, and a **ledger** of already-processed
pairs: global mutable state threaded through the trace, so the correctness of
any single admission depends on the history of the whole run.

**(c) Owner-uniform with halving (VD).** Iterate over all owned instances;
each fires its half-action on the non-owner and half-reaction on the owner,
unconditionally. Stateless like (a), pair-preserving like (b): $A=-R$ holds
per instance by construction, the source/receiver role collapse is the
closure theorem rather than a coincidence, and self-action is excluded by the
owner/non-owner typing rather than by a bolted-on clause.

The $\tfrac12$ is the entire price of having both virtues at once, and it is
a design-time constant, not bookkeeping.

## 18. The choices, sorted

The correction in this d2 sharpens what (c) does and does not eliminate from
(b). Algorithm (b) contains **two** choice-like elements: which side gets
the representation (plus the ledger enforcing once-only), and which side's
formula is quoted. Algorithm (c) eliminates the first *because it was never
a physical datum* — both sides fire, halved. It cannot eliminate the second,
because the second is a genuine representational freedom that any
trace-producing scheme must declare. The first was a non-fact posing as an
input; the second is an input. The VD's contribution is to tell them apart.

## 19. Consistency with the forward-only reading

The halved members are not the banned $\tfrac12\mathbf F_{\mathrm{net}} +
\tfrac12\mathbf F_{\mathrm{net}}$ decomposition. The banned move manufactures
*members* out of algebra on the resultant. Here membership is established
first — two instances, separately admitted through
$\operatorname{Own}_G$ and $\operatorname{Condition}_G$ — and the halving
happens inside the value procedure of already-warranted members. Membership
first, values second; the one-way direction of the NML3 explication is
preserved. The declaration likewise touches only the value/trace layer:
membership never depends on which member is quoted.

---

# Part VII — Reading guide: how the pieces fit across the corpus

*Written for readers (human or AI) coming to this line of work cold. Each
entry says what the note contributes and what to read it for. Custody note:
the Force-Sum discovery note lives in VD-Newton, not here; its surviving
local carrier is the constitutive-asymmetry sketch.*

## 20. The dependency chain

```text
aggregate/member correction (Design 2.1 bug, custody: VD-Newton)
    |
    v
Force-Sum abstraction: F_net = Σ_{f in IFS} V(f), with f ≠ V(f)
(Force-Sum discovery note, custody: VD-Newton)
    |
    +--> membership is prior to summation; decomposition ≠ membership;
    |    forward-only reading; generator/closer split
    |    [NML3_FORCE_SUM_FOUNDATIONAL_UNDERSTANDING_2026-08-02,
    |     NML3_WARRANTED_FORCE_ACCOUNT_FOUNDATIONAL_EXPLICATION_2026-08-05,
    |     NML3_FORCE_SUM_STEELMAN_2026-08-08]
    |
    +--> instance identity, duplicate prevention, action/reaction
    |    exclusivity, cross-target pairing
    |    [NML3_OPEN_PROBLEM_IMPRESSED_FORCE_IDENTITY_...]
    |
    +--> action and reaction have different construction histories;
    |    carrier datum; gravity as the universality crux (Part VI)
    |    [ACTION_REACTION_CONSTITUTIVE_ASYMMETRY_SKETCH_d1]
    |         |
    |         v
    |    two architectures: constitutive-carrier vs participant-symmetric;
    |    owner-blind activation + same-kind reciprocity -> closure theorem
    |    -> two owner-side representations -> half-weighting
    |    [VD_PARTICIPANT_SYMMETRIC_FORCES_..._d2]
    |
    +--> V(f) wall needs a runtime input; fixed sigma(f) rejected;
         canonical recipient + canonical vector; open q4: symmetric case?
         open q8: convention provenance in the trace?
         [CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14_d1]
              |
              v
         q4 SPLIT and answered: ownership discharges existence, anchoring,
         pairing and weight; the quoting declaration SURVIVES as the wall
         input in both branches; sigma(f) returns as the declaration's
         per-occurrence trace shadow (answering q8);
         A = -(Gmm/2r²)r̂ quoted, R = +(Gmm/2r²)r̂ negated,
         under the declared standard convention; values declaration-invariant
         [THIS NOTE, d2]
```

## 21. Per-note guide

**Force-Sum discovery note** *(VD-Newton custody; extraction survives in the
asymmetry sketch).* Source of the aggregate/member correction and the
$f\neq V(f)$ separation: the IFS holds identity-bearing occurrences, an
evaluator supplies vectors, and Force-Sum is polymorphic over the member
type. Read it for *why the sum consumes members it did not construct.*

**NML3 foundational note (2026-08-02).** States the five hurdles of building
a force account and the critical insight that vector decomposition never
creates membership — including the $\tfrac12\mathbf F_{\mathrm{net}}$
counterexample. Read it for *what the halved members must NOT be mistaken
for* (§19 above resolves the apparent collision).

**NML3 warranted-account explication (2026-08-05) + steel-man (2026-08-08).**
The four-way separation (object ≠ force-instance ≠ vector value ≠ warrant),
the forward-only reading, the generator/closer split, and membership earned
computationally from the non-invertibility of the sum. The steel-man flags
open item 6 — one interaction, one vs. several instances — as high-leverage.
Read them for *the membership machinery the halved members must pass
through*, and note that §13 above bears directly on item 6.

**NML3 open problem (impressed-force identity / exclusivity).** Where
instance identity, duplicate prevention, and the cross-target action/reaction
pairing constraints live, with the stress-test battery (test E = distinct
equal-valued forces). Read it for *the identity scheme the two half-members
must satisfy*; the halved picture makes test E the generic gravitational
case, not an edge case.

**Constitutive-asymmetry sketch (2026-08-13).** Action and reaction differ in
construction history (computed vs. negated), the missing datum is which
participant carries the constitutive mechanism, and Part VI raises gravity as
the case with no carrier. Read it for *the template that each owned instance
instantiates* — the owner sits in the carrier role — and for the crux the
half-weighting note answers. Note its computed/negated distinction is exactly
what $\sigma(f)$ marks in the trace.

**Participant-symmetric forces d2 (2026-08-13).** The owner-blind interface,
the closure theorem, the derivation of double representation, and the
half-weighting. Answers the sketch's Part VI: gravity does not break the
asymmetry; it reveals a second architecture. Read it for *why both halves
always exist and why ½ is forced.*

**Canonical-orientation convention note (2026-08-14).** $A=-R$ underdetermines
which member is canonical; a convention must supply recipient and vector; a
*fixed* $\sigma(f)$ is rejected because every wall exposes a genuine runtime
input. Read it for *the evaluator shape this note plugs the symmetric branch
into*. Its open q4 is split and answered here; its q8 is answered by the
$\sigma(f)$-as-trace-shadow construction.

**This note (d2, 2026-08-15).** The meshing, corrected: ownership discharges
representation existence, anchoring, pairing and weight — but the quoting
declaration survives as a wall input in both branches, because the two
admissible declarations produce different traces and the trace is what the
VD grades. $\sigma(f)$ returns as the declaration's per-occurrence shadow.
The action carries the minus sign under the declared standard convention;
target-side values are declaration-invariant and locally statable; the
statelessness rationale is recorded; the arbitrariness-diagnoses-the-wall
rule is stated. The Part IX addendum records the member-headword
resolution: force laws taught as `action-force_kind` / `reaction-force_kind`
absorb $\sigma$ into the name, discharging the declaration through the entry
authority.

## 22. The shape of the whole, in three sentences

Force-Sum consumes warranted, identity-bearing members and is blind to their
construction; everything interesting happens behind the $V(f)$ wall. Behind
that wall there are (at least) two acting-object architectures —
constitutive mechanisms, where one side carries the state, and
participant-symmetric fundamentals, where both sides own the same kind and
each pair interaction is represented twice at half weight — and one
convention wall spanning both: the human declaration of which member is
quoted, whose per-occurrence shadow $\sigma(f)$ every trace must carry. What
distinguishes the symmetric branch is not escape from that wall but
value-level invariance under it — which is why gravity, the case that
threatened all three parent notes, ends up confirming each of them.

---

# Part VIII — What changed from d1

## 23. The overclaim, and the argument that removed it

d1 claimed the convention wall's runtime input was **discharged
structurally** for the participant-symmetric branch, leaving "only
presentation." The user's correction (2026-08-15 discussion): the opposite
declaration — quote $F=+kx$, understand the quoted force as the
reaction-side member, negate for the action — is fully admissible, and that
admissibility is itself the proof of a surviving human input. d1 had
conflated *value*-invariance with *input*-absence. Since the two
declarations differ in the trace, and the VD's ontology is trace-behavioural,
the input is real and must be walled.

Specific retractions and repairs:

- §4 of d1 ("no runtime convention survives at the evaluation level") —
  **withdrawn**; replaced by the discharged/surviving split (§§3–5).
- "evaluation-invisible" (d1 §10) — **retired**; replaced by
  "value-invisible, trace-visible" (§12), which is what keeps the wall.
- d1 §12's reading of the underdetermination test ("input relocated") —
  **corrected**: the test applies with full force; the evaluator must refuse
  to orient until a declaration is supplied (§14).
- d1 §13 ("only presentation survives") — **corrected**: the quoting choice
  is the wall input itself, not epiphenomenal residue (§5).
- d1 §14/§21-q1 (whether the constitutive branch is also discharged) —
  **dissolved**: neither branch is discharged; one convention wall spans
  both (§15).
- d1's boxed signs — **retained**, but relabelled as the content of a
  declared standard convention rather than a structural necessity (§8).
- New: $\sigma(f)$ rehabilitated as the declaration's trace shadow,
  answering the convention note's q8 (§6); the
  arbitrariness-diagnoses-the-wall rule (§16); the two-choices sorting of
  the algorithmic rationale (§18).

---

# Part IX — Addendum (2026-08-15, later same day): member-named force laws

## 24. The user's presentation, recorded

The clearest statement of the whole result arrived after d2 was drafted, as a
pedagogical reformulation (user, 2026-08-15 discussion):

> Every time you learnt about a force, it was underspecified. You should
> have been simply told: `action-force_spring` $= -kx$,
> `action-force_gravity` $= \ldots$, `reaction-force_pressure` $= \ldots$

Every taught force law — $F=-kx$, $mg$, $PA$ — quotes one member of a pair
as if it were the whole mechanism, leaving the recipient and the quoted-side
choice for context to patch. The fully specified form names the member in
the headword. Then nothing is ambient: the name says which member the
formula evaluates, and therefore who receives it (action → non-owner /
non-carrier; reaction → owner / carrier). For the symmetric branch:

$$
\texttt{action-force\_gravity} = -\frac{Gm_om_n}{2r^2}\,\hat{\mathbf r},
\qquad
\texttt{reaction-force\_gravity} = +\frac{Gm_om_n}{2r^2}\,\hat{\mathbf r},
$$

instantiated twice per pair, once per owner.

## 25. What the member-headword shape settles

**Open question 1 (declaration supply point) — resolved in direction.** The
declaration is installed by the entry authority, per force kind, baked into
member-designating headwords. This is one of the supply points the
convention note's §5 explicitly anticipated ("an entry authority"). The wall
still exposes a human input; the input is supplied once, in the dictionary,
rather than redeclared per trace.

**Open question 3 ($\sigma$ display) — resolved in direction.** The
$\sigma$ tag is absorbed into the headword. A trace displays convention
provenance by *citation* — "applied `action-force_spring` to the block" —
and needs no $\sigma$ column. The name is the tag.

**Convergence with the inventory.** The acting-object inventory already
gives every concrete acting object separate `action-force` and
`reaction-force` slots, and the asymmetry sketch asked why two slots rather
than one signed slot. The member-headword shape is the answer read forward:
each slot deserves its own quoted formula, and the familiar taught formulas
were always one slot's content masquerading as the pair.

**The generalization.** The pair relation does not assign targets; $A=-R$
does not orient; $F=-kx$ does not name its recipient. One sentence covers
all three: **standard force notation systematically underspecifies the
member.** A student taught the member-named forms never meets the ambiguity;
the convention machinery becomes visible only at the good question — why
two entries per kind — where the answer is the constitutive asymmetry
itself.

**What stays free, harmlessly.** Which member is taught first. Under
member-named laws neither entry claims to be "the" force law, so ordering no
longer smuggles anything.

**Scope.** Direction recorded on user decision, 2026-08-15. Final headword
wording (whether `action`/`reaction` survive the vocabulary reservoir's
probe, or the computed/negated candidates replace them) remains entry-design
territory at source; this addendum records the *shape* — member-designating
names — not the words.

---

## 26. Open questions

1. ~~Where is the declaration supplied?~~ **Resolved in direction (§25):**
   by the entry authority, per force kind, in member-designating headwords.
2. What is the locally decidable mark of branch membership that licenses the
   ½ vs. 1 weight? (§16; half-weighting note q3.) *Partial progress
   2026-08-15: the branches have an empirical signature — asymmetric kinds
   yield single-member residuals, symmetric kinds only paired-sum residuals
   — so the classification is measurable from outside an open system. See
   `Newton-analysis/typed_closure_deduction/`, §10. The entry-side mark
   remains open.*
3. ~~How should the trace display $\sigma$?~~ **Resolved in direction
   (§25):** by member-name citation; no $\sigma$ column.
4. Does the value-invisibility of $\sigma$ in the symmetric branch bear on
   the convention note's q6 (whether `action`/`reaction` remain headwords,
   derived labels, or teacher vocabulary)?
5. How does the owner-anchored orientation interact with the NML3 identity
   representation candidates (relationally keyed vs. IFS-plus-acting-object
   keyed) in the open problem note §§8–10?
6. Beyond binary: does the per-instance structure survive for
   $n$-participant mechanisms, where the convention note's q5 already flags
   the generalization as open?

---

## Provenance and scope

Authored locally in VD-docs on 2026-08-15 from a working discussion of the
three parent notes; revised to d2 the same day after the user identified the
discharged-convention overclaim. No VD-Newton file was read for or edited by
this note; no entry wording is proposed; no headword is selected (the
vocabulary reservoir and the NML3 terminology decisions remain authoritative
at source). The algorithmic rationale of Part VI and the correction argument
of Part VIII record discussion-level arguments not previously in the corpus;
everything else is meshing, not new physics. Math written in `$`/`$$` form
from the start.
