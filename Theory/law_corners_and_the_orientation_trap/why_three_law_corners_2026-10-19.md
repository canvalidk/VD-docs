# Why Three?

## Unequal statements of one law, law corners, and the orientation trap

Status: record of a conversation, 19 October 2026 (Claude app, mobile, then
Claude Cowork). Written to `inbox/` at Can's request ("Yes will you rewrite it
please") and sorted the same session.

**Supersedes** `law_corners_and_the_orientation_trap_2026-10-19.md` (same day),
wholesale. The successor test reads it as a supersession, not a draft: the
earlier record explained why one law has *three equivalent* statements and
treated their non-equivalence as an open item. Can's correction: that has the
emphasis backwards. The statements are **not** equivalent, and the real
question is why physics counts them as one law anyway. Everything of value in
the earlier record is carried over here, so it need not be consulted.

Repo state read for the earlier record: `canvalidk/VD-docs@b013b99`, namely
`Core/VD_LAW_HOUSE_FOUNDATION.md`, `Core/degree_of_law_formal.md`,
`Theory/triplet_as_admission_event/` (both drafts), and the law sections of
`Theory/_note_theories_as_haskell/vd_haskell_essay_d2.md` and
`Theory/Orientational/why_this_project_is_worth_your_time.md`.

**Attribution.** Can's points are marked **[Can]**. Worked mappings, examples,
formulations and objections are Claude's, marked **[Claude]**, and were
offered, not ruled on, unless the text says Can confirmed them. Literature
references have **not** been checked against primary sources.

---

## 1. The question nobody had a place to put

**[Can]** The second law of thermodynamics has several standard statements.
The third law has three. They are not all exactly the same. Anyone can see
that there are three; the nerve is in asking *why three*. From the answer's
side there now seems to be a possible story. From the mystery's side it is
crazy even to imagine that the question has a solution.

**[Claude]** Why it is crazy: before the answer exists, there is no *kind* of
answer the question could have.

- Physics does not care how many ways a law is phrased.
- History says Nernst, then Planck, then the unattainability people; three is
  an accident of who showed up.
- Logic says equivalent statements are one statement, and these are not even
  equivalent.

Each field gives the same reply: the count is noise. So asking "why three?"
means treating a number found in textbooks as *data*, the way "three
generations of fermions" was eventually treated as owed an explanation. That
is only possible once you suspect a theory exists in which the number of
statements of a law is a predicted quantity. **The question and the answer
arrive together.** From inside the answer it looks obvious; from outside it
looks like numerology. That asymmetry is the signature of the find.

## 2. The facts: the statements are not equivalent [Claude]

*Unverified against primary sources.*

**Third law.**

| Statement | Content | Relation to the others |
|---|---|---|
| Nernst | entropy *changes* of all processes vanish as $T\to 0$ | the weakest; differences only |
| Planck | entropy itself goes to zero as $T\to 0$ for a perfect crystal | strictly stronger than Nernst: fixes the constant's *value*, not just its sameness |
| Unattainability | no finite sequence of processes reaches $T = 0$ | equivalence with Nernst disputed for about a century; Masanes & Oppenheim (2017) derived it under quantum-information assumptions |

**Second law.**

| Statement | Content | Relation |
|---|---|---|
| Clausius | heat does not flow spontaneously from cold to hot | proved equivalent to Kelvin–Planck by the standard composite-engine argument |
| Kelvin–Planck | no cyclic engine turns heat from one reservoir entirely into work | as above |
| Carathéodory | near any state there are states not reachable adiabatically | a different kind of statement; needs extra assumptions to recover the others |
| Entropy increase | the entropy of an isolated system never decreases | standard, and not one of the three |
| Carnot's theorem | no engine between two reservoirs beats the reversible one | standard, and not one of the three |

Every textbook still calls each set "the second law" and "the third law".

## 3. Thesis: a law is its house, not one proposition

**[Can]** Each triplet entry is a *different statement of the law*. A law has
three corners, so it can be stated three ways, one oriented around each of its
headwords. A corner does not have to carry the law's whole information
content, but it can.

**[Claude, formulation; emphasis confirmed by Can]** Then the
non-equivalence is not an embarrassment for the triplet view. **It is the
evidence for it.** If a law were a single proposition, three unequal
statements would be three different laws. Physics does not treat them that
way. It counts unequal statements as one law, so it is already treating the
law's identity as the *house*, the triplet of headwords it relates, rather
than any one sentence, without having a word for doing so. Each standard
statement is the triplet's content read off at one corner, plus whatever that
corner borrows from the surroundings. Corners that borrow different amounts
come out unequal and still belong to one law.

**[Claude]** This is a second justification of the triplet rule, different in
kind from `why_the_triplet_rule_is_needed_d2.md`. That note's admission
argument says what an honest theory *should* record (one prior term plus two
co-admitted terms). This record observes what physics *does*: laws discovered
piecemeal by different people come with several unequal "formulations" that
are nevertheless one law. Laws written down once (Newton II, the first law)
come with one statement and a long argument about what it means. The corner
structure leaks into the historical record.

## 4. Worked corners [Claude]

### 4.1 Third law

November: `entropy` (from the second law, defined only up to a constant).
Winters: `absolute-entropy`, `absolute-zero`.

| Corner | Statement | What the corner adds |
|---|---|---|
| entropy | **Nernst**: entropy changes vanish as $T\to 0$ | stated in the old currency, differences only, so it carries least |
| absolute entropy | **Planck**: entropy goes to zero as $T\to 0$ | entropy gets a zero, the suspected-iron → iron move: entropy-up-to-a-constant becomes absolute entropy |
| absolute zero | **Unattainability**: $T = 0$ is not reached in finitely many steps | absolute zero gets its role as an unreachable limit |

The ordering of strength tracks the corners: the November corner, stated in
pre-existing vocabulary, can say least; the corner that *births* a quantity
(absolute entropy) says most. This is the unequal-content pattern §3 predicts.

### 4.2 Second law

November: `heat` (the first law's wall). Winters: `thermodynamic-temperature`,
`entropy`, co-born in $\delta Q_{\mathrm{rev}} = T\,dS$.

| Corner | Statement |
|---|---|
| heat | **Clausius**: heat does not flow spontaneously from cold to hot |
| temperature | **Kelvin–Planck**: no cyclic engine turns heat from one reservoir entirely into work (Kelvin's absolute scale was built from the same Carnot reasoning) |
| entropy | **Carathéodory**: adiabatic inaccessibility, which is what proves entropy exists |

**Co-birth in the mathematics.** Carathéodory's theorem gives $\delta Q$ an
integrating factor, and an integrating factor arrives *paired with its
potential*. Entropy cannot be had without simultaneously having a temperature
that turns $\delta Q$ into $dS$. That is co-birth in the mathematics of
thermodynamics, decades before the VD, not imposed by it.

**Weakest mapping.** Kelvin–Planck is about engines; it is Kelvin's scale
construction, from the same reasoning, that defines $T$. The temperature
corner may be the scale construction rather than the engine statement.

### 4.3 Newton II

November: `inertial-acceleration` (chimney via Newton I). Winters: `net-force`,
`inertial-mass`, the Newton v0.5 assignment worked in `degree_of_law_formal.md`.

| Corner | Statement | Algebraic face | What it licenses |
|---|---|---|---|
| acceleration | Inertial acceleration is what a net force produces in a body: more for more force, less for more inertial mass. | $a = F/m$ | predicting motion |
| force | Net force is what it takes to give a body of a given inertial mass a given inertial acceleration. | $F = ma$ | attributing a cause to motion |
| mass | Inertial mass is how much net force a body needs per unit of inertial acceleration. | $m = F/a$ | reading mass off force–acceleration data (the estimator's corner) |

For an equation-shaped law every corner written as a formula carries the whole
law algebraically. The corners then differ not in information but in what
their residues *license*: predict, attribute, read off.

### 4.4 First law

November: `work` (grounded in mechanics as $\int \mathbf F\cdot d\mathbf x$).
Winters: `internal-energy`, `heat`.

| Corner | Statement | Algebraic face |
|---|---|---|
| work | The work a system does is the internal energy it gives up beyond what it takes in as heat. | $\delta W = \delta Q - dU$ |
| internal energy | Internal energy is a state quantity that rises by the heat taken in and falls by the work done. | $dU = \delta Q - \delta W$ |
| heat | Heat is the change in a system's internal energy not accounted for as work. | $\delta Q = dU + \delta W$ (Born's definition) |

Heat counts as a winter word although the word is old: its role *as an energy
transfer* is born here, as `melting-point-of-iron` is born with `iron`. The
$d$-versus-$\delta$ notation already marks which corner is the state function.

### 4.5 The houses chain

```text
First law    November: work      → winters: internal energy, heat
             heat's wall      = second law's chimney
Second law   November: heat      → winters: temperature, entropy
             entropy's wall   = third law's chimney
Third law    November: entropy   → winters: absolute entropy, absolute zero
```

The same degree ladder (1, 2, 3, …) as Newton I → Newton II → Force Sum in
`degree_of_law_formal.md`, and the house-overlap structure of
`VD_LAW_HOUSE_FOUNDATION.md` §13.

## 5. What would make the pattern real [Claude]

**P1. Sorting by headword.** Wherever a law has several unequal statements,
they should sort by the headword each is built around, at most one family per
corner.

**P2. Differences live in the borrowings.** The gap between two statements of
one law should be locatable in what each corner borrows from the surroundings
(chimney, walls, background vocabulary), not in the triplet's core.

**The hinge: the second law has more than three statements.** The third law
is clean. The second law is not: entropy increase and Carnot's theorem are
standard statements beyond the three corners. The honest claim is therefore
not "the second law has three statements" but **"the second law has three
corner statements, and the others reduce to a corner plus a wall."** If the
reduction works (entropy increase looks like the entropy corner plus the
isolated-system wall; Carnot's theorem like the temperature corner plus the
reversible-engine wall), the pattern is real. If an extra statement resists
reduction, the three that fit were selected. This is the test the nerve of the
question exposes it to: the same instinct that makes "why three?" askable
makes "three" easy to see where it is not.

**The membership test.** If a law's identity is its house, something must stop
every true sentence mentioning entropy and temperature from counting as "a
statement of the second law". Candidate: a statement belongs to a law iff it
is the triplet's content read off at one corner plus only what that corner may
legally borrow (by the chimney < triplet < walls chronology, §7). Without such
a test, "same law" degrades into "same topic".

**Forward prediction.** Take a law that famously has one statement, write its
two missing corners, then search the literature for whether they already exist
as "alternative formulations" carrying odd foundational baggage. Repeated hits
would be strong evidence; corners that are nonexistent or nonsensical would be
informative too.

**Selection effect.** Claude produced the thermodynamic mappings quickly and
found they fit; that is when to trust them least. The decisive check is to
type one law's three corners cold and confirm that the joint content of the
three residues is the law and nothing more.

## 6. Mystery is a dropped node

**[Can]** Some statements are triplets nobody notices. "Energy is conserved"
feels mysterious because we don't say the full thing. It is like saying
"$F = m$ times stuff", which would also feel mysterious. Say the full thing
("energy is constant in an energetically closed system") and it feels obvious.
This is the lossy-readout diagnosis of the Haskell essay, used as a working
tool.

**[Claude]** Energy conservation as a triplet. November: `energy`; winters:
`energy-transfer`, `energetically-closed-system`.

1. *Energy corner:* a system's energy changes only by energy transferred across its boundary.
2. *Transfer corner:* energy transfer is whatever changes a system's energy from outside, through its boundary.
3. *Closed-system corner:* an energetically closed system is one with no energy transfer across its boundary.

Jointly, "energy is constant in an energetically closed system" reads like "a
bachelor has no wife". The mystery is **located, not destroyed**: the empirical
bite sits in claims belonging to the walls and the prediction set, namely that
*closed systems exist* (boundaries blocking every kind of transfer can be
built, at least approximately) and that *one scalar suffices* (work, heat and
radiation are bookkeeping in one currency: Joule, not logic). That is where the
VD says empirical content should live.

Other cases: *momentum is conserved* + "in a mechanically closed system" (the
Closure law); *charge is conserved* + "it changes only by current through the
boundary" (the continuity equation *is* the full statement); *entropy
increases* + "in an isolated system" still feels mysterious. Either a node is
still missing or this is a genuine brute fact. Candidate missing node: the
coarse-graining, where the lumping-horizon result (Newton-analysis,
`_dscn_lumping_consequences`) may be the missing headword.

## 7. The orientation trap

**[Can]** There is a real choice of which corner to state first.
Mathematicians treat the other two as simple theorems of the first, which
neglects the asymmetry of information between the corners. That asymmetry,
together with the fact that the choice must be made and that it affects *not
the law itself but everything surrounding it*, is a deadly trap for the
philosopher:

> No, this is the right statement. No, that one is. If you use that one, this
> over there breaks. No, you can fix that over there by changing it like this.
> But you can't do that — that would be circular.

**[Claude] The trap runs on the non-equivalence.** If the corners were truly
equivalent, choosing which to state first would be taste and nobody would
fight about it. They fight because the corners carry unequal content, and each
choice changes what the surrounding entries have to supply. §2's facts are the
fuel; §3's thesis says why the fight cannot be settled by finding "the" law.

**[Claude] The mechanism.** "Corner 2 is a theorem of corner 1" is never quite
true: the derivation borrows from the surroundings. What holds is

$$
\text{corner}_1 + S_1 \vdash \text{corner}_2,\ \text{corner}_3 ,
$$

and a different choice of first corner needs a different $S$. The information
asymmetry does not vanish; it moves into whatever the derivation silently
borrowed. Hence "if you use that one, this over there breaks" is literally
true: the load moved over there.

**[Claude] The legal direction of the cycle.** The law-house chronology
(chimney $<$ triplet $<$ walls) makes the cycle legal in exactly one direction:
a wall may use the law, since walls come after the triplet; the chimney may
not. The circularity charge is right when "over there" is the chimney and
wrong when it is a wall. Linear axiomatics cannot express the difference (to it
every backward dependence is circular), so both sides of the debate get to be
right in turn, indefinitely.

**[Claude] Instances.**

- Newton II: definition of force (Poincaré) or empirical law? Mass first via acceleration ratios (Mach)? One triplet, three choices of anchor.
- Second law: Planck's objection to Carathéodory's axiomatics as unphysical, and the reverse view of Clausius/Kelvin as engine talk.
- Outside physics: the axiom of choice, Zorn's lemma and the well-ordering theorem, equivalent over ZF and felt as wildly unequal (the joke attributed to Jerry Bona: the first obviously true, the last obviously false, and who can tell about Zorn's lemma).

**[Claude] What the VD does to the debate.** November is not freely chosen; it
is whatever the log already held. "Which statement is right?" becomes "what
vocabulary were you assuming before this law?", a question with an answer per
log.

## 8. Alternative logs

**[Can]** One can imagine a version of Newton that begins with spring
constants and derives space and time relative to them, and all sorts of highly
unintuitive versions: wave function first instead of observables first.
Seeing exactly how these laws fit requires prying the well-typed VD versions
out of their meanings, which is surprisingly hard.

**[Claude]**

- **The reordered log already exists.** Since the 2019 SI redefinition, the kilogram is fixed from Planck's constant, the second from the caesium hyperfine frequency, the metre from $c$: constants first, base units derived. A spring-first Newton is the same move with a cruder oscillator; any clock is a stiffness-and-inertia device.
- **A sorting test for foundations debates.** A theory is roughly a set of law houses and a foundational position is a chosen log order. *Same houses, different order* is an orientation dispute with no content at stake (wave-function-first vs observables-first, Mach vs Poincaré on mass, relational vs absolute space). *Extra houses* is a genuine content difference (Bohmian particle positions plus a guidance law), and then the triplet rule's idle-ontology audit applies.
- **Why one order feels intuitive.** Entries are judged as triggers, by the probability that a reader performs the correct procedure, not as statements judged for accuracy. Observables-first feels natural because a human reader's oldest chimneys are perceptual; a wave-function-first log is not wrong, but its first residues have no installed reactions until a lesson installs them.

## 9. Open items

1. **Tension with the law-house rule, ruling owed.** `VD_LAW_HOUSE_FOUNDATION.md` rule 8 says no one corner should encode the whole daughter–daughter relationship, and §5 there asks "would this one entry already communicate the whole law?". Can's statement is that a corner need not carry the full content but *can*. Either rule 8 is a writing guideline rather than a lawhood criterion, or it is amended. §4.3's reading (corners differ in what they license, not in information) is Claude's suggestion.
2. **Different corner vs more content.** §3 lets corners carry unequal content; the audit then needs a test telling *a different corner* apart from *a stronger law*. Planck vs Nernst is the test case: is Planck the absolute-entropy corner, or a stronger third law?
3. **The hinge (§5).** Do entropy increase and Carnot's theorem reduce to a corner plus a wall?
4. **The membership test (§5)** is a candidate, not a rule.
5. **The dossier escape hatch.** "A participant may be a structured dossier" (d2 §6) is legitimate but could absorb any counterexample; the rule stays falsifiable only if the dossier move is sometimes *refused*.
6. **"Feels obvious" as the success criterion.** A full statement can feel obvious because it is tautological or because the hard part was pushed into a headword's wall. The audit must check the walls, not the vibe.
7. **Energy and symmetry, ruling owed.** Noether ties energy conservation to time-translation symmetry, and in general relativity a well-defined total energy often does not exist. The symmetry is either a hidden node or lives in the "closed systems exist" wall.
8. **Log order relocates the choice rather than abolishing it.** "Which statement?" becomes "which log?", and an argument is needed that some orders are forced (by pedagogy, or by what is observable first).
9. **The invariant may not survive reordering.** "Exactly one old, two new" depends on chronology, so a different log may force a different *grouping* into triplets, not only different anchors; "same houses" would then need a weaker invariant (same hypergraph up to re-factorisation, or same predictions).
10. **Spring-first Newton** needs a check that the first oscillator's period is not measured against a smuggled time; the SI dodges this by declaring the caesium frequency a definition: legitimate chimney or stipulated primitive?
11. **"Interpretation = log order" needs a counterexample hunt.** Collapse theories change the dynamics, so they are added houses, not reorderings; the claim needs every interpretation classified, not the convenient ones.
12. **Unique-November** remains unjustified (d2 §10); nothing here bears on it.

---

## Relation to existing records

- `law_corners_and_the_orientation_trap_2026-10-19.md`: **superseded** by this record, wholesale (thesis changed; all content carried over).
- `why_the_triplet_rule_is_needed_d2.md`: the semantic (admission) justification; this record is its empirical counterpart. Does not supersede or correct it.
- `VD_LAW_HOUSE_FOUNDATION.md`: chimney/wall chronology used in §7; rule 8 tension in §9 item 1.
- `degree_of_law_formal.md`: the degree ladder that §4.5 extends to thermodynamics.
- `vd_haskell_essay_d2.md`, `why_this_project_is_worth_your_time.md`: the lossy-readout diagnosis applied in §6.
