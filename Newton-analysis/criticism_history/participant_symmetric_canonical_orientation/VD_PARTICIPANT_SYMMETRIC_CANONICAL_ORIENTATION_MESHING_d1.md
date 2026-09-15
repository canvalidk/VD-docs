# Participant-Symmetric Canonical Orientation — Meshing Note

## Half-Weighted Gravity Signs under the Canonical-Force Orientation Convention

**Status:** working meshing note, d1. Claude-authored at user request,
2026-08-15, in VD-docs.
**Project:** VD Newton (Newton-analysis incubator)
**Parents:**

- `Newton-analysis/participant_symmetric_forces/VD_PARTICIPANT_SYMMETRIC_FORCES_OWNER_BLIND_ACTIVATION_AND_HALF_WEIGHTING_d2.md`
- `Newton-analysis/canonical_force_orientation/CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14_d1.md`
- `Newton-analysis/action_reaction_asymmetry/ACTION_REACTION_CONSTITUTIVE_ASYMMETRY_SKETCH_d1.md`

---

## 0. Purpose and one-paragraph result

The canonical-force orientation note establishes that $A=-R$ supplies
opposition but not orientation: a convention must select the canonical
recipient and the canonical vector, and the note's open question 4 asks how
symmetric mechanisms such as gravity are to supply that convention when
neither participant is a privileged constitutive carrier. The half-weighting
note establishes that participant-symmetric kinds are represented from both
participant-owned sides, each side carrying half the pair force.

This note meshes the two. The result:

> **For the participant-symmetric branch, the canonical recipient is supplied
> structurally, per owned instance: it is the non-owner. No human runtime
> choice is needed at the evaluation level. With the separation unit vector
> oriented owner → non-owner, the action member of the owned gravity instance
> is**
>
> $$A_{\text{gravity}} = -\frac{Gm_om_n}{2r^2}\,\hat{\mathbf r}$$
>
> **and the reaction member is**
>
> $$R_{\text{gravity}} = +\frac{Gm_om_n}{2r^2}\,\hat{\mathbf r}.$$
>
> **The minus sign belongs to the action.** The target-side values are
> convention-free: every gravity member in any target's account points from
> the target toward the other participant with magnitude $Gm_om_n/2r^2$.

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

A fixed sign function $\sigma(f)$ was rejected because it is not a runtime
input; the working principle is that **every wall exposes an input**. Open
question 4 of that note: what supplies the input for symmetric mechanisms,
where no participant is a privileged constitutive carrier?

---

# Part II — The meshing: ownership discharges the orientation input

## 3. Per instance, there is a privileged side

The convention note is right that the *interaction* has no privileged
participant in the symmetric case. But under the participant-symmetric
architecture, the interaction is never evaluated as a bare interaction. It is
evaluated through its two owned instances, and each **instance** has a
privileged side by type: the owner.

The constitutive-asymmetry template — action computed, landing on the
non-acting participant; reaction obtained by negation, landing back on the
carrier — maps onto each owned instance with the owner in the carrier role.
This fixes, structurally:

$$
c(G_o) = n,
\qquad
K(G_o) = \tfrac12\,\mathbf F_{o\to n}.
$$

The evaluator branch of the convention note then runs unchanged per instance:
canonical vector to the non-owner, its negative to the owner, undefined for
nonparticipants.

## 4. Why no runtime convention survives at the evaluation level

For a constitutive mechanism, choosing the canonical recipient is a genuine
choice between two representations, only one of which will be used. For a
participant-symmetric kind, **both** owner-anchored representations always
exist — that is the content of the closure theorem — so there is nothing to
choose between. The two per-instance orientations are both present, each at
half weight, and their union is orientation-neutral.

This is the same maneuver that eliminated the pair-ledger: where the
conventional algorithm demands a choice (which side is source) and a memory
(which pairs are done), the VD refuses the choice by firing both sides,
halved. Here it refuses the orientation choice the same way. The demanded
datum — which participant is canonical — does not exist for this branch, and
an algorithm that requires it is requiring a non-fact. The architecture that
requires no such datum is the one that fits.

$\sigma(f)$ stays rejected, and for a stronger reason than before: the sign
branch is now derived from the owner/non-owner typing of the instance, which
is a structural datum, not a supplied one and not a hidden implementation
detail.

---

# Part III — Gravity, vectors figured out

## 5. Definitions

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

## 6. The two members of the owned instance

$$
\boxed{
A_{\text{gravity}}
=
V(\operatorname{action}(G_o,n))
=
-\frac{Gm_om_n}{2r^2}\,\hat{\mathbf r}
\qquad\text{(on the non-owner)}
}
$$

$$
\boxed{
R_{\text{gravity}}
=
V(\operatorname{reaction}(G_o,o))
=
+\frac{Gm_om_n}{2r^2}\,\hat{\mathbf r}
\qquad\text{(on the owner)}
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

## 7. Why the minus belongs to the action

Three reasons, in decreasing order of weight:

1. **Template fit.** The action is the constitutively computed member and
   lands on the non-owner; attraction pulls the non-owner *toward* the owner,
   which is the $-\hat{\mathbf r}$ direction under owner-anchored
   orientation.
2. **Textbook continuity.** The owner occupies the source role, so the quoted
   canonical formula is exactly the familiar
   $-({Gm_1m_2}/{r^2})\,\hat{\mathbf r}$ with $\hat{\mathbf r}$ source →
   test mass — halved. Nothing about the quoted form has to be relearned.
3. **Convention-reversal admissibility.** The flip ($\hat{\mathbf r}$
   anchored non-owner → owner, $K$ negated) passes the convention note's
   reversal test — every target-side value invariant — so it is admissible
   but pointlessly nonstandard.

## 8. Coulomb, for contrast

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
matches gravity's. The canonical structure — action on the non-owner,
reaction by negation on the owner, half weight — is identical.

---

# Part IV — Verification

## 9. Totals per target

The other instance $G_n$ runs the same rule with roles exchanged
($\hat{\mathbf r}_{n\to o} = -\hat{\mathbf r}$):

| occurrence | lands on | value |
|---|---|---|
| action of $G_o$ | $n$ | $-\dfrac{Gm_om_n}{2r^2}\,\hat{\mathbf r}$ |
| reaction of $G_n$ | $n$ | $-\dfrac{Gm_om_n}{2r^2}\,\hat{\mathbf r}$ |
| action of $G_n$ | $o$ | $+\dfrac{Gm_om_n}{2r^2}\,\hat{\mathbf r}$ |
| reaction of $G_o$ | $o$ | $+\dfrac{Gm_om_n}{2r^2}\,\hat{\mathbf r}$ |

Sums: $-({Gm_om_n}/{r^2})\,\hat{\mathbf r}$ on $n$ and
$+({Gm_om_n}/{r^2})\,\hat{\mathbf r}$ on $o$ — the full textbook pair,
equal and opposite. ✓

## 10. The convention-free local form

The table exposes something stronger than the totals: **the two members
landing on any one target are equal vectors.** A fully local, orientation-free
statement of every gravity member is therefore available:

> Every gravity member in target $p$'s account has value
>
> $$\frac{Gm_om_n}{2r^2}\,\hat{\mathbf r}_{p\to q},$$
>
> where $q$ is the other participant: half strength, pointed at the other
> participant, and there are exactly two of them.

The action/reaction labels — which member is the other instance's action and
which is your own instance's reaction — never affect the value a target
receives. The values carry no convention residue at all. The labels remain
real (they carry instance identity and construction history) but they are
evaluation-invisible.

## 11. NML3 case instantiation

The two members on one target are **distinct force-instances with equal
vector values** — distinct because their acting-object-instance identities
differ ($G_o$ vs $G_n$). This physically instantiates the NML3 explication's
behavioural case "distinct equal-valued forces both remain" (and the open
problem's test E) in *every* gravitational pair, not as an exotic
possibility. Any identity scheme that collapses equal-valued members merges
the two halves into one and loses half the force. This is direct pressure on
NML3 open item 6 toward instance-carried identity.

## 12. Against the convention note's test battery

- **Convention reversal** (§9.1): flip $\hat{\mathbf r}$ anchoring and negate
  $K$ together — all four table entries unchanged. Pass.
- **Equal-and-opposite underdetermination** (§9.2): given only $A=-R$, the
  evaluator cannot orient; here orientation is supplied by ownership typing,
  which is exactly the "supplied convention" the test demands — supplied
  structurally rather than by a human. Pass, with the input relocated.
- **Interaction-before-value** (§9.3): admission of both instances uses only
  $\operatorname{Own}_G$ and $\operatorname{Condition}_G$; no value is
  needed. Pass.
- **Invalid target** (§9.5): a nonparticipant fails
  $\operatorname{Condition}_G$'s incidence and receives *undefined*, not
  $-K$. Pass.

---

# Part V — What survives as convention, and what is open

## 13. Surviving human freedom

Only presentation. Which $\hat{\mathbf r}$ a formula is written in, and which
of the two equal members a lesson displays first, are quoting choices; they
flip $A$ and $R$ jointly or reorder equal values, and leave every
target-side value fixed. The convention note's degree of freedom is real, but
for this branch it lives entirely on the quoting side of the wall.

## 14. The constitutive branch is untouched

For carrier-borne mechanisms (spring, contact, actuator) only one side owns
the constitutive state, only one representation exists, and it carries full
weight. There the canonical-recipient choice may retain genuine runtime
content — the Hooke $F=-kx$ vs $F=+kx$ freedom — or may be discharged by the
carrier the way ownership discharges it here. **This note takes no position**;
that is the convention note's open questions 2–3 restricted to the
constitutive branch.

## 15. Weight as a branch attribute

The evaluator now needs one datum per acting-object kind: which architecture
it belongs to, hence which weight applies —

```text
participant-symmetric branch  -> two representations -> weight 1/2
constitutive-carrier branch   -> one representation  -> weight 1
```

The weight is fixed at design time by the closure theorem (multiplicity is
exactly two for the symmetric branch, always); it is not a runtime count and
not account-dependent. But the branch classification must be locally
decidable from the kind itself, or a trace could apply the wrong weight
without visible failure. This is the half-weighting note's open question 3
wearing operational clothes.

---

# Part VI — The algorithmic rationale, recorded

## 16. Three algorithms

This argument arose in discussion (2026-08-15) and is not yet recorded
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

## 17. Consistency with the forward-only reading

The halved members are not the banned $\tfrac12\mathbf F_{\mathrm{net}} +
\tfrac12\mathbf F_{\mathrm{net}}$ decomposition. The banned move manufactures
*members* out of algebra on the resultant. Here membership is established
first — two instances, separately admitted through
$\operatorname{Own}_G$ and $\operatorname{Condition}_G$ — and the halving
happens inside the value procedure of already-warranted members. Membership
first, values second; the one-way direction of the NML3 explication is
preserved.

---

# Part VII — Reading guide: how the pieces fit across the corpus

*Written for readers (human or AI) coming to this line of work cold. Each
entry says what the note contributes and what to read it for. Custody note:
the Force-Sum discovery note lives in VD-Newton, not here; its surviving
local carrier is the constitutive-asymmetry sketch.*

## 18. The dependency chain

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
    +--> V(f) wall needs a runtime input; σ(f) rejected;
         canonical recipient + canonical vector; open q4: symmetric case?
         [CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14_d1]
              |
              v
         q4 discharged structurally for the symmetric branch:
         canonical recipient = non-owner, per instance;
         A = -(Gmm/2r²)r̂, R = +(Gmm/2r²)r̂; values convention-free
         [THIS NOTE]
```

## 19. Per-note guide

**Force-Sum discovery note** *(VD-Newton custody; extraction survives in the
asymmetry sketch).* Source of the aggregate/member correction and the
$f\neq V(f)$ separation: the IFS holds identity-bearing occurrences, an
evaluator supplies vectors, and Force-Sum is polymorphic over the member
type. Read it for *why the sum consumes members it did not construct.*

**NML3 foundational note (2026-08-02).** States the five hurdles of building
a force account and the critical insight that vector decomposition never
creates membership — including the $\tfrac12\mathbf F_{\mathrm{net}}$
counterexample. Read it for *what the halved members must NOT be mistaken
for* (§17 above resolves the apparent collision).

**NML3 warranted-account explication (2026-08-05) + steel-man (2026-08-08).**
The four-way separation (object ≠ force-instance ≠ vector value ≠ warrant),
the forward-only reading, the generator/closer split, and membership earned
computationally from the non-invertibility of the sum. The steel-man flags
open item 6 — one interaction, one vs. several instances — as
high-leverage. Read them for *the membership machinery the halved members
must pass through*, and note that §11 above bears directly on item 6.

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
half-weighting note answers.

**Participant-symmetric forces d2 (2026-08-13).** The owner-blind interface,
the closure theorem, the derivation of double representation, and the
half-weighting. Answers the sketch's Part VI: gravity does not break the
asymmetry; it reveals a second architecture. Read it for *why both halves
always exist and why ½ is forced.*

**Canonical-orientation convention note (2026-08-14).** $A=-R$ underdetermines
which member is canonical; a convention must supply recipient and vector;
$\sigma(f)$ is rejected because every wall exposes a genuine runtime input.
Read it for *the evaluator shape this note plugs the symmetric branch into*,
and for open question 4, which this note discharges.

**This note (2026-08-15).** The meshing: ownership supplies the canonical
recipient per instance, so the symmetric branch needs no runtime orientation
input; the action carries the minus sign under owner-anchored orientation;
target-side values are convention-free and locally statable; the statelessness
rationale is recorded; the surviving freedoms and the branch-classification
requirement are flagged.

## 20. The shape of the whole, in three sentences

Force-Sum consumes warranted, identity-bearing members and is blind to their
construction; everything interesting happens behind the $V(f)$ wall. Behind
that wall there are (at least) two acting-object architectures: constitutive
mechanisms, where one side carries the state and the reaction is a negation,
and participant-symmetric fundamentals, where both sides own the same kind
and each pair interaction is represented twice at half weight. The
orientation convention that the wall exposes as a runtime input for the first
architecture is discharged structurally by ownership in the second — which is
why gravity, the case that threatened both parent notes, ends up confirming
both.

---

## 21. Open questions

1. Should the constitutive-carrier branch's canonical recipient also be
   regarded as structurally discharged (carrier = owner role), leaving the
   quoting freedom as the only convention content there too? (§14; convention
   note qq. 2–3.)
2. What is the locally decidable mark of branch membership that licenses the
   ½ vs. 1 weight? (§15; half-weighting note q. 3.)
3. Does the evaluation-invisibility of the A/R labels (§10) bear on the
   convention note's q. 6 (whether `action`/`reaction` remain headwords,
   derived labels, or teacher vocabulary)?
4. How does the owner-anchored orientation interact with the NML3 identity
   representation candidates (relationally keyed vs. IFS-plus-acting-object
   keyed) in the open problem note §§8–10?
5. Beyond binary: does the per-instance discharge of orientation survive for
   $n$-participant mechanisms, where the convention note's q. 5 already
   flags the generalization as open?

---

## Provenance and scope

Authored locally in VD-docs on 2026-08-15 from a working discussion of the
three parent notes. No VD-Newton file was read for or edited by this note; no
entry wording is proposed; no headword is selected (the vocabulary reservoir
and the NML3 terminology decisions remain authoritative at source). The
algorithmic rationale of Part VI records a discussion-level argument not
previously in the corpus; everything else is meshing, not new physics. Math
written in `$`/`$$` form from the start.
