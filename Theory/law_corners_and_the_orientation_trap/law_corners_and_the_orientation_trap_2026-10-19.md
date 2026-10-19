# Law Corners and the Orientation Trap

## Why laws come with several "equivalent" statements, why they feel mysterious, and why philosophers argue about which statement is the right one

Status: record of a conversation, 19 October 2026 (Claude app, mobile).
Written to `inbox/` at Can's request ("Ye go for it") and sorted the same session.

Repo state read: `canvalidk/VD-docs@b013b99` — `Core/VD_LAW_HOUSE_FOUNDATION.md`,
`Core/degree_of_law_formal.md`, `Theory/triplet_as_admission_event/` (both drafts),
and the law sections of `Theory/_note_theories_as_haskell/vd_haskell_essay_d2.md`
and `Theory/Orientational/why_this_project_is_worth_your_time.md`.

**Attribution.** The argument's spine is Can's, stated in the conversation and
marked **[Can]**. Worked mappings, examples and objections were supplied by
Claude in discussion and are marked **[Claude]**. Claude's mappings were
offered, not ruled on: none of them is a decision. Literature references have
**not** been checked against primary sources.

---

## 1. Thesis

**[Can]** Each triplet entry is a *different statement of the law*. A law has
three corners, so a law can be stated three ways, one oriented around each of
its headwords. A corner does not have to carry the law's whole information
content — but it can.

**[Can]** This explains a fact any curious student runs into: the third law of
thermodynamics has three standard statements. The naive question — *why three
statements if they mean the same thing?* — has a VD answer: they are the three
corners of one triplet.

**[Claude, assessment]** This is a second justification of the triplet rule,
different in kind from the one in `why_the_triplet_rule_is_needed_d2.md`. That
note's admission argument says what an honest theory *should* record (one prior
term plus two co-admitted terms). This record observes what physics *does*: laws
discovered piecemeal by different people come with three separately found
"equivalent" formulations, and laws written down once (Newton II, the first law)
come with one statement and a long argument about what it means. The corner
structure leaks into the historical record.

---

## 2. Worked corners [Claude]

### 2.1 Newton II

November: `inertial-acceleration` (chimney via Newton I). Winters: `net-force`,
`inertial-mass` — the Newton v0.5 assignment worked in `degree_of_law_formal.md`.

| Corner | Statement | Algebraic face | What it licenses |
|---|---|---|---|
| acceleration | Inertial acceleration is what a net force produces in a body: more for more force, less for more inertial mass. | $a = F/m$ | predicting motion |
| force | Net force is what it takes to give a body of a given inertial mass a given inertial acceleration. | $F = ma$ | attributing a cause to motion |
| mass | Inertial mass is how much net force a body needs per unit of inertial acceleration. | $m = F/a$ | reading mass off force–acceleration data (the estimator's corner) |

### 2.2 First law

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

### 2.3 Third law

November: `entropy` (from the second law, defined only up to a constant).
Winters: `absolute-entropy`, `absolute-zero`.

| Corner | Standard statement |
|---|---|
| entropy | **Nernst**: entropy *changes* of all processes vanish as $T\to 0$ — stated in the old currency, differences only. |
| absolute entropy | **Planck**: entropy itself goes to zero as $T\to 0$ for a perfect crystal — entropy gets a zero; the suspected-iron → iron move, entropy-up-to-a-constant → absolute entropy. |
| absolute zero | **Unattainability**: no finite sequence of processes reaches $T = 0$ — absolute zero gets its role as an unreachable limit. |

### 2.4 Second law

November: `heat` (the first law's wall). Winters: `thermodynamic-temperature`,
`entropy`, co-born in $\delta Q_{\mathrm{rev}} = T\,dS$.

| Corner | Standard statement |
|---|---|
| heat | **Clausius**: heat does not flow spontaneously from cold to hot. |
| temperature | **Kelvin–Planck**: no cyclic engine turns heat from one reservoir entirely into work (Kelvin's absolute scale was built from the same Carnot reasoning). |
| entropy | **Carathéodory**: near any state there are states not reachable adiabatically — which is what proves entropy exists. |

**The strongest evidence found in the conversation.** Carathéodory's theorem
gives $\delta Q$ an integrating factor, and an integrating factor arrives
*paired with its potential*. Entropy cannot be had without simultaneously having
a temperature that turns $\delta Q$ into $dS$. That is co-birth in the mathematics
of thermodynamics, decades before the VD, not imposed by it.

### 2.5 The houses chain

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

---

## 3. Mystery is a dropped node

**[Can]** Some statements are triplets nobody notices. "Energy is conserved"
feels mysterious because we don't say the full thing — it is like saying
"$F = m$ times stuff", which would also feel mysterious. Say the full thing
("energy is constant in an energetically closed system") and it feels obvious.
This is the lossy-readout diagnosis already in the Haskell essay, applied as a
working tool.

**[Claude]** Energy conservation as a triplet — November: `energy`; winters:
`energy-transfer`, `energetically-closed-system`.

1. *Energy corner:* a system's energy changes only by energy transferred across its boundary.
2. *Transfer corner:* energy transfer is whatever changes a system's energy from outside, through its boundary.
3. *Closed-system corner:* an energetically closed system is one with no energy transfer across its boundary.

Jointly, "energy is constant in an energetically closed system" reads like "a
bachelor has no wife".

**[Claude] The mystery is located, not destroyed.** With the core transparent,
the empirical bite sits in two claims that belong to the walls and the
prediction set, not to the law:

- *closed systems exist* — boundaries blocking every kind of transfer can be built, at least approximately;
- *one scalar suffices* — work, heat and radiation are bookkeeping in one currency (Joule, not logic).

That is where the VD says empirical content should live, so the dissolved
mystery is a prediction confirmed.

**[Claude] Other cases.**

- *Momentum is conserved* + "in a mechanically closed system" — the Closure law (interaction candidate, interaction pair, mechanically closed system).
- *Charge is conserved* + "it changes only by current through the boundary" — the continuity equation *is* the full statement.
- *Entropy increases* + "in an isolated system" still feels mysterious. Either a node is still missing or this is a genuine brute fact. Candidate missing node: the coarse-graining — which states are lumped together — where the lumping-horizon result (Newton-analysis, `_dscn_lumping_consequences`) may be the missing headword.

---

## 4. The orientation trap

**[Can]** There is a real choice of which corner to state first. Mathematicians
treat the other two as simple theorems of the first, which neglects the
asymmetry of information between the corners. That asymmetry, combined with the
fact that the choice must be made and that it affects *not the law itself but
everything surrounding it*, is a deadly trap for the philosopher:

> No, this is the right statement. No, that one is. If you use that one, this
> over there breaks. No, you can fix that over there by changing it like this.
> But you can't do that — that would be circular.

**[Claude] The mechanism.** "Corner 2 is a theorem of corner 1" is never quite
true: the derivation borrows from the surroundings (chimney, walls, background
vocabulary). What holds is

$$
\text{corner}_1 + S_1 \vdash \text{corner}_2,\ \text{corner}_3 ,
$$

and a different choice of axiom needs a different $S$. The information
asymmetry does not vanish; it moves into whatever the derivation silently
borrowed. Hence "if you use that one, this over there breaks" is literally true
— the load moved over there.

**[Claude] The legal direction of the cycle.** The law-house chronology
(chimney $<$ triplet $<$ walls) makes the cycle legal in exactly one direction:
a wall may use the law, since walls come after the triplet; the chimney may not.
The circularity charge is right when "over there" is the chimney and wrong when
it is a wall. Linear axiomatics cannot express the difference — to it every
backward dependence is circular — so both sides of the debate get to be right
in turn, indefinitely.

**[Claude] Instances of the trap.**

- Newton II: definition of force (Poincaré) or empirical law? Mass first via acceleration ratios (Mach)? One triplet, three choices of anchor.
- Second law: Planck's objection to Carathéodory's axiomatics as unphysical, and the reverse view of Clausius/Kelvin as engine talk — an orientation fight.
- Outside physics: the axiom of choice, Zorn's lemma and the well-ordering theorem — equivalent over ZF, felt as wildly unequal (the joke attributed to Jerry Bona: the first obviously true, the last obviously false, and who can tell about Zorn's lemma). Three statements, logically one, unequal in felt content.

**[Claude] What the VD does to the debate.** November is not freely chosen; it is
whatever the log already held. "Which statement is right?" becomes "what
vocabulary were you assuming before this law?" — a question with an answer per
log.

---

## 5. Alternative logs

**[Can]** One can imagine a version of Newton that begins with spring constants
and derives space and time relative to them, and all sorts of highly
unintuitive versions — wave function first instead of observables first.

**[Claude]**

- **The reordered log already exists.** Since the 2019 SI redefinition, the kilogram is fixed from Planck's constant, the second from the caesium hyperfine frequency, the metre from $c$: constants first, base units derived. A spring-first Newton is the same move with a cruder oscillator; any clock is a stiffness-and-inertia device.
- **A sorting test for foundations debates.** On this picture a theory is roughly a set of law houses and a foundational position is a chosen log order. *Same houses, different order* is an orientation dispute with no content at stake (wave-function-first vs observables-first, Mach vs Poincaré on mass, relational vs absolute space). *Extra houses* is a genuine difference in content (Bohmian particle positions plus a guidance law), and then the triplet rule's idle-ontology audit applies: does removing the house change any inference, classification or licensed operation?
- **Why one order feels intuitive.** Entries are judged as triggers, by the probability that a reader performs the correct procedure (the E10 packet's settled reading), not as statements judged for accuracy. Observables-first feels natural because a human reader's oldest chimneys are perceptual; a wave-function-first log is not wrong, but its first residues have no installed reactions, so they count as undeclared machinery until a lesson installs them.

**[Can]** Seeing exactly how these laws fit requires prying the well-typed VD
versions out of their meanings, which is surprisingly hard.

---

## 6. Open items and pressure points

1. **Tension with the law-house rule, ruling owed.** `VD_LAW_HOUSE_FOUNDATION.md` rule 8 says no one corner should encode the whole daughter–daughter relationship, and §5 gives the audit question "would this one entry already communicate the whole law?". Can's statement here is that a corner does not have to carry the info content but *can*. Either rule 8 is a writing guideline rather than a lawhood criterion, or it is amended. For equation-shaped laws every corner written as a formula carries the whole law algebraically, so the rule cannot be about information content; Claude's suggested reading is that corners differ in what their residues *license* (predict, attribute, read off).
2. **The three third-law statements are not strictly equivalent.** Planck's is stronger than Nernst's (it fixes the constant's value, not just its sameness), and the Nernst–unattainability equivalence was long disputed (Masanes & Oppenheim, 2017, derived unattainability under quantum-information assumptions). Consistent with item 1's "can carry unequal content", but "they mean the same thing" was always partly false — and the audit needs a test telling *a different corner* apart from *more content*.
3. **Kelvin–Planck → temperature corner is the weakest mapping.** The statement is about engines; it is Kelvin's scale construction, from the same reasoning, that defines $T$.
4. **The second law has more than three folk statements** (entropy increase, Carnot's theorem). Test: do the extras reduce to a corner plus a wall, or is one of them a compressed second law?
5. **Selection effect on the mappings.** Claude produced the thermodynamic mappings quickly and found they fit; that is when to trust them least. The decisive test is to type one law's three corners cold and check that the intersection of the three residues is the law and nothing more.
6. **Forward prediction, proposed.** Take a law that famously has one statement, write its two missing corners, then search the literature for whether they already exist as "alternative formulations" carrying odd foundational baggage. Repeated hits would be strong evidence; non-existent or nonsensical corners would be informative too.
7. **The dossier escape hatch.** "A participant may be a structured dossier" (d2 §6) is legitimate but could absorb any counterexample; the rule stays falsifiable only if the dossier move is sometimes *refused*.
8. **"Feels obvious" as the success criterion.** A full statement can feel obvious because it is tautological or because the hard part was pushed into a headword's wall. The audit must check the walls, not the vibe.
9. **Energy and symmetry.** Noether ties energy conservation to time-translation symmetry, and in general relativity a well-defined total energy often does not exist. The symmetry is either a hidden node or lives in the "closed systems exist" wall; ruling owed.
10. **Log order relocates the choice rather than abolishing it.** Two logs are two dictionaries; "which statement?" becomes "which log?", and an argument is needed that some orders are forced (by pedagogy, or by what is observable first).
11. **The invariant may not survive reordering.** "Exactly one old, two new" depends on chronology, so a different log may force a different *grouping* into triplets, not only different anchors; "same houses" would then need a weaker invariant (same hypergraph up to re-factorisation, or same predictions).
12. **Spring-first Newton** needs a check that the first oscillator's period is not measured against a smuggled time; the SI dodges this by declaring the caesium frequency a definition — legitimate chimney or stipulated primitive?
13. **"Interpretation = log order" needs a counterexample hunt.** Collapse theories change the dynamics, so they are added houses, not reorderings; the claim needs every interpretation classified, not the convenient ones.
14. **Unique-November** remains unjustified (d2 §10); nothing here bears on it.

---

## Relation to existing records

- `why_the_triplet_rule_is_needed_d2.md` — the semantic (admission) justification; this record is its empirical counterpart. Does not supersede or correct it.
- `VD_LAW_HOUSE_FOUNDATION.md` — chimney/wall chronology used in §4; rule 8 tension in §6 item 1.
- `degree_of_law_formal.md` — the degree ladder that §2.5 extends to thermodynamics.
- `vd_haskell_essay_d2.md`, `why_this_project_is_worth_your_time.md` — the lossy-serialisation diagnosis applied in §3.
