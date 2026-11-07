# Hypothesis Sets from Traces

## How the paper, the trace and the prediction-set records might fit, tried once on the Atwood trace

**Status:** record. **PROVISIONAL AND UNCHECKED.** Claude-authored at the
user's request, 2026-11-05, from that evening's conversation in VD-docs. The
user's statements are marked *(stated)*. Everything else is *(analysis)*: it is
not ruled, and none of it has been checked by anyone but its author. Most of it
is a proposal about how existing records connect. Where a claim was checked
against a file, the check is named. Where it was not, assume it was not.
**Branch:** Theory. Newton is the worked case.

**What prompted it.**

> Do you see it, or are you just noticing that they look like they gotto fit.
> Cause that's where I'm at. *(stated)*

> This is the first time I don't know if there are more ideas you can naturally
> continue this with. Why don't you develop it slightly (look for more natural
> corrections), then write a record on what you have, with 'provisional',
> 'unchecked' or some other disclaimer. *(stated)*

**Parents (read against):**

- `Theory/_note_hypothesis_set_paper/hypothesis_set_paper_d4.md` (§§3–4 read
  in full for this record; the rest not reread)
- `Theory/theory_logical_structure/THEORY_LOGICAL_STRUCTURE_2026-11-05.md`
- `Theory/nobody_made_a_mistake/nobody_made_a_mistake_meaningful_substitutions.md`
  (§§2–11 read)
- `Theory/prediction_sets_as_disjunctions/prediction_sets_as_disjunctions_neptune_and_vulcan.md`
- `Theory/how_balls_turn_green_or_red/how_balls_turn_green_or_red_2026-11-01.md`
- `Theory/theory_immutable_object_and_id/WHY_A_THEORY_NEEDS_AN_IMMUTABLE_OBJECT_AND_UNIQUE_ID_2026-09-08.md`
- `Theory/vd_trace_level2_v3.md` (the Atwood trace: demand tree, human
  response to the diagnostic, final input taxonomy read)
- `Newton-analysis/_dscn_haze/` (the 09-09 tolerance discovery and the 09-12
  car record, as summarised in the catalog; not reread)
- `Newton-analysis/criticism_history/NML3_REMAINDER_TRIPLET_AND_ACTING_OBJECT_DISCOVERY_PROPOSAL_2026-09-09.md`

---

## 0. Short version

*(analysis)* The claimed fit: **a trace in a dated dictionary generates the
hypothesis set of its prediction.** Sort every step of the trace into one of
three kinds. Entry applications are the theory and contribute no member.
Supplied premises contribute one commitment member each. Meaningful
substitutions contribute one mistake member each. The paper's verdict rule then
runs over that set.

Tried once, on the Atwood trace, the fit **survives in outline and breaks in
detail**. It breaks in seven places, which are the corrections of §5. The four
most consequential:

1. **A trace records what was *used*; the paper's set is what was *needed*.**
   A generator that lists every used premise makes false acquittals possible.
   This mirrors the paper's point that an unlisted needed premise makes false
   convictions possible.
2. **A trial has two derivations, not one:** the trace to the prediction, and
   the reduction from the scene to the observed value. The trace generates only
   the first half of the set.
3. **Approximation members share one budget.** Their stated limits have to be a
   partition of the haze allowance set by the tolerance ε. If each is tested
   against the full ε, the disjunction the set relies on is no longer entailed.
4. **The dictionary does not abolish the line between T and commitment; it
   moves it into the entry cut.** In the current dictionary the gravity law is
   supplied at a wall, so it is a member, not part of T.

So the answer to the question that prompted this record is: **one connection
is a structure, not a resemblance.** It can be stated precisely enough to be
tried and to fail, and it failed in identifiable places. The rest (§6) is still
resemblance.

---

## 1. The pieces

| Record | What it supplies to the fit |
|---|---|
| Hypothesis-set paper, d4 | The set H = {p, ¬A₁, …, ¬Aₙ}; the verdict rule (acquit when any member holds, convict when all are rejected, otherwise undecided); membership by what the derivation *needs*, to within ε; the question in §8, *what generates a theory's sets?* |
| Theory Logical Structure | The trace from a starting statement, "including the point where any extra premise enters"; the dated dictionary D and the relation P ⊢_D Q |
| Nobody made a mistake | One mistake member per meaningful substitution the trace records; the families table of §11 (mistakes; inputs and fidelity; missing objects and closure; frame and approximation) |
| Prediction sets as disjunctions | The colouring rule; Neptune green, Vulcan red; the external-body worry answered by moments |
| How balls turn green or red | The urn; a corrected trace is a new ball |
| Immutable object and ID (09-08) | The verdicts accumulate on one fixed, identified D |
| Haze | The tolerance ε, the special zero Z_ε, the allowance on what the account left out |
| Remainder-triplet proposal | "A new acting object is one which, if impressed on an object, drives the remainder to zero" *(stated, 2026-09-09)* |

---

## 2. The claimed fit

*(analysis)* Fix a dated dictionary D, a starting statement S and a trace from
S to a prediction p. Every recorded step is one of three kinds.

| Step kind | Example (Atwood) | Contributes |
|---|---|---|
| **1. Entry application.** A headword is expanded by D's own entry. | E21: inertial acceleration = net force / inertial mass | Nothing. It *is* T. |
| **2. Supplied premise.** Something D does not supply enters at a wall: a recognition, a modelling choice, an empirical value, a closure-forced constraint, or S itself. | "Lab frame is inertial-frame"; "IFS(m₁) = {gravity, tension}" | One commitment member ¬Aᵢ. |
| **3. Meaningful substitution.** A recorded replacement at the level of the residue. | `8a = 19.6` → `a = 2.45` | One mistake member: "what is meant by the left side differs from what is meant by the right". |

Then

```text
H(trace) = {p} ∪ {¬b : b a kind-2 step} ∪ {"c went wrong" : c a kind-3 step}
```

**Why the three member kinds behave differently.** This part checks out
against d4 §3. Kind-3 members are claims about the derivation, not the world:
whether S, b₁, …, bₖ ⊢_D p really holds. d4 says these members make the whole
disjunction "true whenever T is true" rather than entailed by T, and that a
found mistake acquits T, with the corrected derivation a new trial. In the VD,
a kind-3 member is closed by checking D (re-probing the residue, confluence),
not by looking at the world. Kind-2 members and p are closed empirically. So
the three step kinds of the trace line up with the two kinds of member the
paper already distinguishes: object-language commitments and step
correctness. That alignment is the core of the fit.

**What it would answer.** d4 §8 asks what generates a theory's sets. On this
reading the answer is *the dictionary's traces*. And d4 §4 concedes that where
T ends is "a residual convention". On this reading the dictionary settles it:
entry means T, everything else means commitment. §5, C5 qualifies this.

---

## 3. One run: the Atwood trace

*(analysis; checked against `vd_trace_level2_v3.md`, its demand tree, its
human response to the diagnostic and its final input taxonomy)*

Reading the set off mechanically, by step kind:

- **Kind 1, no members.** E21, E23, E24, E25, E31–E37, and E38–E44 for the
  closure diagnostic.
- **Kind 2, 17 recorded inputs.** Seven recognitions (two point particles, the
  frame, four acting objects). Three modelling choices (the two interaction
  sets, S = {m₁, m₂}). Three empirical inputs (F = −mg, two pairings). Four
  closure-forced inputs (Earth's acceleration negligible, equal tensions,
  kinematic coupling, wall stationary).
- **Kind 3, 10 recorded substitutions.** These are listed in Nobody made a
  mistake §7.

Set against what a physicist would write for this prediction in d4's style,
four things show up.

1. **The trace's own input table omits two inputs its demand tree records.**
   The demand tree has `inertial-mass(m₁) → human: 3 kg (given)`, and likewise
   5 kg for m₂. The 17-row taxonomy does not list either. Read mechanically,
   the demand tree catches inputs the hand-made table dropped. The value of g,
   folded into row 11, is a third. *(This is a small instance of the trace
   checking its reader, the effect Theory Logical Structure describes.)*
2. **The trace used a premise it never recorded.** The human response to the
   diagnostic derives equal tensions "by symmetry of the frictionless pulley".
   "Frictionless pulley" is not an input row, and neither is the pulley's
   inertia, which is not mentioned at all. A mechanical reading of the recorded
   inputs misses both. A reading of the prose catches one. So **membership
   depends on recording grain**, for premises exactly as Nobody made a mistake
   §7 found for substitutions. A premise is a member only if the trace records
   it as a premise.
3. **The observation side is absent.** The trace ends at a = 2.45 m/s². The
   members that say the measured acceleration was wrong (timing, distance, the
   reduction from the scene to a number) are not in it and cannot be. d4's
   Jupiter set has a block of these: its §5, seen in passing and not reread,
   says "the observed side uses those behind ¬A₁₀ to ¬A₁₂ and ¬A₁₄". See C2.
4. **The four closure-forced inputs are all approximations, and they share
   one tolerance.** Earth's recoil is "negligible", the string is "massless"
   and "inextensible", and the wall "doesn't accelerate". Each is true only to
   within some size, and their effects on a add up. See C3.

Verdict of the run *(analysis)*: the three-kind sort reproduces the paper's
member kinds and finds members the hand list missed (item 1). It also misses
members (items 2 and 3) and mis-states others (item 4). That is a structure
that can fail, not a resemblance. But it is not yet a generator.

---

## 4. Where haze and the remainder enter

*(analysis)*

- **The closure member is where haze lives.** d4's Jupiter set has a
  force-completeness commitment (the only appreciable forces are those
  counted). In VD terms it is the modelling input "IFS(m₁) = {gravity,
  tension}", and in the Atwood case the closure-forced approximations too.
  Haze is this commitment made tolerance-indexed: the account C plus Z_ε, the
  unaccounted part within an allowance. The 09-13 reading of haze as "the
  closer" says the same from the other side.
- **The remainder-triplet statement is Le Verrier's move.** "A new acting
  object is one which, if impressed on an object, drives the remainder to
  zero" *(stated, 2026-09-09)* describes the 31 August 1846 derivation almost
  word for word: find the one body that reproduces the residual.
- **But it constructs the *test*, not the member** (C4).

---

## 5. Corrections found while developing it

Each correction is *(analysis)*. Each corrects the fit of §2, or something said
in conversation earlier the same evening.

### C1. Used is not needed: over-generation causes false acquittals

d4 §4 makes a commitment a member only if the derivation *needs* it: "A premise
used but not needed is not a member." A trace records what was *used*. So
H(trace) is an upper bound on d4's set, not the set.

This matters for the verdict, not just for tidiness. d4 argues that an
unconceived (missing) member "cannot cause a false acquittal, since an
acquittal needs a held member, and a held member is on the list; it can cause a
false conviction". The mirror case is new. **A used-but-unneeded premise on the
list *can* cause a false acquittal:** if it happens to be false, it holds, and
the rule acquits T on a trial whose prediction never depended on it.

Taken together: listing too few members makes false convictions possible, and
listing too many makes false acquittals possible. A generator has to aim for
exactly the needed set.

How close a trace can get mechanically: the trace's dependency graph shows
which premises flow into p (the provenance cone). Flowing into p is necessary
for need, but not sufficient. Sufficiency is d4's countermodel test, which is
not mechanical. So the trace yields an upper bound that is tighter than "used"
and still not exact.

### C2. A trial has two derivations

The prediction trace gives the T side of the set. Whether p "held" is decided
by a second derivation, from the scene to an observed value, with members of
its own: input fidelity, instrument readings, the reduction chain. In VD terms
that is the witness sheet and the fidelity family of Nobody made a mistake
§11. So:

```text
H(trial) = H(prediction trace) ∪ H(observation reduction)
```

The earlier claim (in conversation) that the trace "gives you the hypothesis
set" is withdrawn. It gives one of two halves. Whether the second half is also
a trace in some dictionary (a dictionary of instruments) is open.

### C3. Approximation members share one budget

This is the correction with the most content, and the least checked.

The disjunction p ∨ ¬A₁ ∨ … ∨ ¬Aₙ is entailed only if T together with all the
Aᵢ yields p *to within ε*. Suppose several members are approximations, of the
form "effect i is below δᵢ" (Earth's recoil, string mass, pulley friction,
drag). To first order their effects on p add, so the entailment needs

```text
δ₁ + δ₂ + … + δₖ  ≤  allowance(ε)
```

(or the corresponding bound in whatever norm the haze adequacy condition
uses). Testing each approximation member against the full ε breaks the
entailment. Four effects each just under ε can together move p by far more
than ε. Every member is then rejected, the prediction fails, and the rule
convicts T, though T was never at fault.

What follows, if this is right:

- The **stated limits** of d4's approximation members are not chosen one by
  one. They are a **partition of the haze allowance**, which is fixed by the
  asker's ε. That answers the question raised in conversation, whether ε and
  d4's stated limits are the same thing: ε fixes the allowance, and the limits
  divide it.
- d4's argument that regrouping members does not change the verdict (strong
  Kleene composition) still holds for presence-or-absence members. For bounded
  members it holds only if the regrouped member carries the summed bound.
- Haze's single aggregate member, "the unaccounted contribution H_C is within
  allowance", is the safe form. It is one member with one test, so the budget
  cannot be double-spent.
- The Atwood trace's closure-forced inputs show the problem directly. They
  arrive together from one diagnostic, unquantified ("negligible",
  "massless"), so no partition is stated.

Unchecked: whether d4's notes (not reread) already handle bounded members; the
first-order additivity; whether "allowance" is the right haze object (09-12
car record, h_allowed versus h_required).

### C4. The remainder builds the test of the closure member, not the member

In conversation it was said that inverting the remainder generates Neptune's
search member. That is wrong as stated. d4 fixes the set before the test, and
its closure member is existential: some body acting was left out. That member
was in Bouvard's set all along. What the residual supplies afterwards is the
**test** for it, the place to look. d4 says as much: "the derivation fixes the
form of the test … the search fixes how far it reaches."

So the remainder-triplet statement is a candidate rule for constructing the
closure member's test from the residual. Building that test needs a concrete
force law to invert. Theory Logical Structure found that the current dictionary
has no gravity headword. **So what the missing headword blocks is the
construction of the test, not the generation of the member.** That is a
narrower claim than the one made in conversation, and it is still checkable.

### C5. The T/commitment line moves into the entry cut; it does not vanish

d4 takes T to be Newton's laws of motion *and gravitation*. In the Atwood
trace, F = −mg is row 11, an **empirical input** supplied at E36's wall. So in
the current dictionary the gravity law is a commitment member, not part of T.
The dictionary does make the line non-conventional *given D*: entry means T.
But which D, meaning which entry cut, is still a choice. It is the choice the
Criticism History argues about. Lakatos's convention has been relocated into
the cut, not removed. The claim in conversation that it "stops being one" is
withdrawn in that strong form.

A further consequence: **supplying a law at a wall shrinks the set.** A
supplied value "F = −29.4 N" brings one member: the value is right. A gravity
*headword* would bring the commitments Theory Logical Structure looked for and
did not find (B is massive, B feels the reciprocal force). Those would be
members of other trials and consequences checkable by trace. A dictionary that
supplies laws as values at walls makes trials that test less.

### C6. Case splits do not break the set

The worry raised in conversation, that a trace by cases or by contradiction
(Theory Logical Structure, row 3) might need one set per branch, dissolves for
the set itself. By the deduction theorem, T ⊢ (A₁ ∧ … ∧ Aₙ) → p over all
premises used anywhere in the proof, whatever its shape. So H is the union over
the whole proof tree. What remains open is whether the trace language can
*express* those proofs at all, and whether the need-pruning of C1 can be done
branch by branch. That question is about Code, not about the set.

### C7. Editions: which balls carry over

The knot left in conversation was this: verdicts accumulate on an immutable D,
but D gets new editions. Proposed rule for when a verdict on a trace in D
carries over to an edition D′:

- (a) every entry the trace applies is unchanged in D′, **and**
- (b) no premise the trace supplied at a wall is supplied by an entry of D′.

Condition (b) is needed because adding a headword can absorb a member into T.
Take an Atwood trial acquitted because the supplied gravity value was wrong
(a held member). In D′, with a gravity headword, that member is part of T, so
the same evidence would *convict*. Adding the headword can therefore turn past
acquittals into convictions. So editions do not simply inherit urns, and they
do not simply restart them. Inheritance is per trace and depends on which
entries and walls the trace touched.

This also answers the identity question of the 09-08 record from one side.
What the urn tracks is not one immutable object for ever. It is the set of
traces whose entries and walls have stayed fixed. Unchecked; not argued
against the urn model of How balls turn green or red.

---

## 6. What is still resemblance

*(analysis)* Each of these looked like it fitted and was not shown to.

1. **Mistake members and "meanings fixed".** d4 holds "logic and the meanings
   of terms" fixed and counts arithmetic as a member. In the VD, the meaning of
   a residue is exactly what a mistake member tests ("what is meant by `5 + 6`
   is what is meant by `11`"), and the wording of an entry can be indicted by
   its dossier (Nobody made a mistake §8.5). So the VD seems to open a member
   that d4 closes by fiat. Whether that is a correction to d4 or a different
   scope is not settled.
2. **Haze inside T or among the members.** If F_net = C + Z_ε is written into
   the Force-Sum entry (the remainder-triplet route), the closure commitment
   becomes part of T in tolerance-indexed form. It is unclear whether that
   moves the closure member out of H or just restates it. It looks like the
   same commitment either way, but that was not worked through.
3. **The found-mistake question.** Nobody made a mistake §10.4 left open
   whether a found mistake colours the ball green. d4, with the user's ruling
   of 2026-11-01, answers it: a found mistake acquits T, and the corrected
   derivation is a new trial. This is recorded here as answered elsewhere, not
   as a result of this record.
4. **The dated suffix and the urn.** P ⊢_D Q is permanent and mathematical.
   The urn is empirical and grows. Whether C7 is the whole relation between
   them, or whether a second object is needed (a lineage of editions), is open.

---

## 7. The next test

*(analysis)* The run of §3 compared a mechanical reading against intuition.
The decisive version: **write the d4-style set for the Atwood prediction by
hand first, independently, then read the set off the trace and compare row by
row.** Count members the trace finds and the hand missed, members the hand
finds and the trace missed, and members the trace lists that are not needed
(C1). A second run on a trace that uses a law headword rather than a value at a
wall would show what C5 predicts: more members, and a richer test.

---

## Provenance

- **Conversation:** 2026-11-05, VD-docs (Claude session linked to Can's
  computer). This followed the sorting of THEORY_LOGICAL_STRUCTURE and Claude's
  reading of it.
- **Stated** (the user's words): the two quotations at the top; the
  remainder-triplet statement quoted in §4 (from the 2026-09-09 record); the
  2026-11-01 found-mistake ruling, as recorded in d4 and its revision log.
- **Analysis** (Claude): everything else, including the three-kind mapping,
  the Atwood run, all seven corrections, §6 and §7.
- **What was read for this record:** d4 §§3–4; Theory Logical Structure in
  full; Nobody made a mistake §§2–11; the Atwood trace's demand tree, its
  diagnostic response and its input taxonomy.
- **What was NOT read:** d4's notes and §§5–8; the haze records themselves
  (only their catalog summaries); the urn record's propositions.
- **Not checked by anyone:** nothing here has been reviewed.
- **Placement:** Theory, own folder, beside Theory Logical Structure. It
  scopes several records and binds to none. It may be a candidate input to the
  hypothesis-set paper's §8, which is his call.
