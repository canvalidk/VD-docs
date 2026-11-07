# Why Triplets? Peirce, Lewis, and the House Count

## Sufficiency, minimality, orientation, and what a law-house over-determines

Status: record of a conversation, 1 November 2026 (Claude, chat session linked
to Can's computer). Written to `inbox/` at Can's request ("Yes I like it. Go
ahead.") and sorted the same session under the 2026-09-24 standing rule.

**Attribution.** Can's points are marked **[Can]**. Derivations, worked
examples, literature links and objections are Claude's, marked **[Claude]**.
Can endorsed the overall direction ("this is likely the best way to say why
triplet ... it is the minimal thing it can be broken down to") and asked for it
to be recorded *because it connects VD ideas to known ones*. The individual
results below were offered, not ruled on, unless the text says otherwise.

**Literature.** Every reference was checked on 2026-11-01 for existence and
bibliographic details, and most for the specific claim cited, but mostly
through abstracts, secondary sources and partial fetches rather than full
primary texts. The *Sources* section says what was checked for each. Treat the
attributions as good leads, not finished scholarship, before any outward use.

**Repo state read.** The working folder on Can's computer, 2026-11-01 (the
commit is not visible through the link): `Core/VD_LAW_HOUSE_FOUNDATION.md`,
`Core/vd_six_entry_structure.md`, `Core/degree_of_law_formal.md`,
`Core/VD rules.csv` and rule ledger v0.1.4, `Core/old VD development/VD__how_to_draft1.pdf`,
`Core/Current development/VD__how_to draft1.1.pdf`,
`Core/old VD development/VD_draft1_amendments.pdf`,
`Core/Current development/VD_draft1_amendments2.pdf`, both drafts in
`Theory/triplet_as_admission_event/`, and
`Theory/law_corners_and_the_orientation_trap/why_three_law_corners_2026-10-19.md`.

---

## 0. Summary

1. **Sufficiency.** Every theory can be written as a log of triplet laws, peripheral definitions and walls. The construction is mechanical (§2). So "can a theory be put in triplet form?" is a normal-form question, like 3-CNF, and cannot by itself falsify anything.
2. **Minimality.** Two-place relations cannot express a combination of two things into a third (§3). This is Peirce's reduction thesis. Law-house rules 9 and 10 are its two clauses. The known counter-results (binary encodings with hidden variables) work only by hiding a three-way junction, which law-house rule 21 already forbids.
3. **Orientation.** A ternary constraint can sit against the log in only four ways, and only one of them admits something new: exactly one old headword, two new (§4). This derives the November/winter rule rather than stipulating it.
4. **Forest.** Under R-LAW-01 the laws can never form a cycle. With R-LAW-05 (unique-November), every headword sits in at most two laws (§5). Checked against Newton v0.5.
5. **House count.** What a house over-determines is order-invariant where "newness" is not (§6). Walls are Lewis's uniqueness clause; the excess is the house's Ramsey content. The "is F = ma a definition?" debate becomes a wall count. A gap: the house has no slot for persistence across instances, which is where constants and persistent mass get their content (§7).

---

## 1. Where this came from

### 1.1 The Lewis comparison [Claude]

The session began with a summary of Lewis, *How to Define Theoretical Terms*
(1970). A theory $T$ introduces new terms $\tau_1 \ldots \tau_n$ jointly,
against old terms. "Old" means *understood before $T$*, not "observational".
Lewis writes the postulate $T(\tau_1,\ldots,\tau_n)$ and splits it in two:

- the **Ramsey sentence** $\exists x_1 \ldots x_n\, T(x_1,\ldots,x_n)$, which carries the empirical content;
- the **Carnap conditional**, which fixes meaning: if something realizes $T$, the terms name it.

He strengthens this to *unique* realization. If $T$ has no realizer or more
than one, the terms do not denote. Each term is then explicitly definable as
the corresponding component of the unique realizer.

The correspondence with the VD is close. Lewis's old/new is the VD's
previously-defined/new. The November word plays the role of an old term
*relative to one step of the log*. The winters are T-terms. The VD makes
Lewis's implicit authority, "the theory $T$", a named object with stages
($D^{(n)}$, December 2025 notation).

### 1.2 Meaning: where the two part [Can, Claude]

Claude raised a Newman-style objection: a triplet read referentially is
satisfied by many pairs, so what fixes the winters' meaning, and when?
**[Can]** answered that this is arguably the first problem the VD addresses,
and pointed to the oldest documents, the "Pundit/Punnet Square" of December
2025 (`VD__how_to_draft1.pdf` §4, `draft1.1` §4).

**[Claude]**, reading those documents:

- A **definition** is a string returned by a named dictionary. Two definitions are the same only if they match character for character.
- A **meaning** is the total change in world state caused by an utterance in context.
- The log is append-only, and lookup is a multi-map ($D^{(n)}[w]$, `VD_draft1_amendments2`).

So strings never change and meanings are never stored. The question "when is a
term's meaning fixed?" has no target. The Newman objection assumes the
referential semantics the VD rejects, and it does not apply.

**What survives.** A trace that consumes $B$ needs one of $B$'s active
definition strings, or a rule for using several. The December notation
deliberately postpones that choice function, $S^{(n)}(w)$.

### 1.3 The test, and the retraction [Can, Claude]

Claude proposed a formal test of the triplet hypothesis (d2 §10). Is a Ramsey
sentence equivalent to a chain of nested $\exists x_b\, x_c\, T_k(a_k,x_b,x_c)$,
with each $a_k$ already admitted? **[Can]** asked Claude to try it. §2 shows
the test as first stated always succeeds, so it has no bite. The earlier claim
that it was "worth more than the graph and Haskell arguments" is withdrawn in
that form. What it produced instead is §§3–7.

---

## 2. Sufficiency: every theory factors [Claude]

**Construction.**

1. **Flatten.** Break $T$ into atomic constraints of the form $u = f(v,w)$, naming intermediate subexpressions. The December 2025 draft already licenses this (§8.2: "a triplet decomposition exists in principle"), as does law-house rule 10.
2. **Admit in log order.** Start from the old vocabulary. Take any constraint that touches something already admitted:
   - **exactly one participant admitted:** a law; that participant is November, the other two are born as winters;
   - **two admitted:** the third is explicitly definable from them, so it is a peripheral entry;
   - **three admitted:** a wall, i.e. a consistency condition.
3. **Repeat** until every constraint is placed.

**Termination.** This finishes whenever every new term is connected to the old
vocabulary through some chain of constraints, which is Lewis's setting. A
component with no old term at all has no anchor. That case only arises for a
purely abstract structure with no handle on the world.

**Consequence.** "Every physics theory can be completely reconstructed in
triplet form" is true in this cheap sense for every theory. d2 §10's stronger
hypothesis needs something that could block the construction. §8 names the two
places where something could.

---

## 3. Minimality: why not two — Peirce's reduction thesis [Claude]

### 3.1 The projection argument

Take $S = \{(x,y,z) : z = x + y\}$ over the reals. Its projection onto any two
coordinates is all of $\mathbb R^2$: any two values are consistent with the
sum, because the third absorbs them.

Suppose a conjunction of one- and two-place constraints on $x, y, z$ (no
auxiliary variables) were satisfied exactly by $S$. Each constraint would have
to contain the projection of $S$ onto its own variables, i.e. everything. So
every constraint is trivial, the conjunction is $\mathbb R^3$, and that is not
$S$.

**The information in a sum lives only in the triple.**

The same holds for Newton II on positive magnitudes, $\alpha = f/m$. Any two of
$f$, $m$ and $\alpha$ are jointly unconstrained, so the corner relation is
genuinely three-place.

This is the precise form of what the six-entry note says informally ("the
daughter-to-daughter relation is emergent; no single entry states it"). It
also answers d2 §8's caution. A two-place relation *can* carry information
($y = 2x$ does), but it cannot carry a *combination*.

### 3.2 Two-place laws cannot admit

Line up a binary constraint against the log:

- **one old, one new:** the new term is defined (or merely bounded, see §8);
- **none old:** the constraint is unanchored.

Either way nothing irreducible is admitted. That is the exact content of
law-house rule 9 ("a two-term cycle collapses toward synonymy"). The collapse
is toward *definition*, of which synonymy is the special case.

### 3.3 This is Peirce's reduction thesis

The literature states Peirce's thesis as two clauses:

- **triadic irreducibility:** some triadic relations cannot be built from monadic and dyadic ones;
- **polyadic reducibility:** every relation of higher arity can be built from triadic ones.

(Koshkin 2024 gives this two-clause statement; Burch 1991 proved a version in
his Peircean Algebraic Logic; Hereth Correia & Pöschel 2006 proved it without
Burch's restriction.)

Law-house rule 9 is the first clause and rule 10 is the second. §2 and §3.1
are an elementary instance of each. As far as this session found, the VD's
triplet rule *is* Peirce's thesis, arrived at independently from the needs of
an auditable log.

### 3.4 The counter-position, and why rule 21 answers it

There is a well-known opposing result.

- **Löwenheim (1915)** reduced all relations to binary ones using set-theoretic pairing.
- In constraint programming, **every** constraint problem is equivalent to a binary one via the **hidden-variable encoding** (Rossi, Petrie & Dhar 1990). One auxiliary variable per constraint ranges over that constraint's satisfying tuples and is tied to each original variable by a two-place relation.

The answer from the Peirce literature (Koshkin 2024, §3): the hidden variable,
joined to three binary relations, *is* a triple junction,
$\exists t\,[P(t,x)\wedge Q(t,y)\wedge R(t,z)]$. It conceals a triad rather
than eliminating one. Peirce's name for the junction is teridentity, and
Hereth Correia & Pöschel (2006) proved it irreducible in their setting.

Dechter (1992, Thm 3.8 and §7) sharpens where the power comes from. Hidden
variables with only two values add nothing, while with three or more values
any relation decomposes. Binary sufficiency needs an auxiliary that can encode
a tuple.

**The VD premise to write down.** Minimality of three holds relative to an
interpreter whose primitives are two-input operations *and which may not
smuggle a pairing or junction*. Law-house rule 21 already demands exactly this:
"residual prose must not conceal undeclared conceptual devices". A hidden pair
variable is such a device.

**Remark [Claude, not checked against the literature].** The premise cannot be
weakened to "continuous constraints": a space-filling (Peano) curve is a
continuous map from $\mathbb R$ onto $\mathbb R^2$ and can play the hidden
variable. It can be weakened to differentiable ones. The image of a $C^1$ map
from $\mathbb R$ into $\mathbb R^2$ has measure zero, so it cannot encode
pairs.

### 3.5 A pointer, not an argument

Peirce tied triadicity to meaning: "a triadic relation is inexpressible by
means of dyadic relations alone" is a premise of his argument that meaning is
irreducible (CP 1.345). The VD's meaning work (DoM, handles, the
stimulus–interpreter–response picture) may have a Peircean reading worth a
separate look. Nothing here depends on it.

---

## 4. Orientation: why exactly one old [Claude]

A ternary constraint can be lined up against the log in only four ways:

| Already admitted | What the entry is |
|---|---|
| 0 | Unanchored; cannot be placed yet |
| 1 | **Admission**: something genuinely new enters (a law) |
| 2 | Explicit definition of the third (d2 §2.1's abbreviation) |
| 3 | Consistency check (a wall) |

Only one row admits anything. Law-house rules 5–6 (R-LAW-01's temporal clause)
state the one-old/two-new signature as a stipulation. Read with §3, it follows
from "a law is an admission" plus "combination needs three places". This is
the formal counterpart of d2 §§2–3, which reached the same pattern
semantically (candidate, admitted kind, differentiator).

---

## 5. Consequence: the laws form a forest [Claude]

**Claim.** Under R-LAW-01, the *law hypergraph* has no cycles. Its vertices are
headwords and its hyperedges are the law trios. Formally, its incidence graph
is a forest; in the database-theory vocabulary this is Berge-acyclicity (see
Fagin 1983 for the family of acyclicity notions).

**Proof.**
1. Go through laws in log order and look at the incidence graph (headword nodes, law nodes, an edge for each membership).
2. A law's winters are new, so they belong to no earlier law: any word in an earlier law was defined at its corner.
3. So each new law node joins exactly one existing headword node (its anchor) and two fresh headword nodes.
4. Attaching a node to one existing node, plus two fresh leaves, never closes a cycle. $\square$

**With R-LAW-05 (unique-November, currently DUBIOUS):**
- every headword is a winter in at most one law and an anchor in at most one, so it **sits in at most two laws**;
- each component is a tree in which every law node has two children.

**Check against Newton v0.5** (law list in `degree_of_law_formal.md`):
- **Newton II, Force Sum, Action–Reaction and Acting Object** form a single path, sharing net-force, acting-force and canonical-force$_{ao}$ in turn;
- **Newton I, Closure and Meta-typing** share no headword with any other law;
- **no headword is in three laws.**

Consistent. The Design 3 ledger was not checked.

**Degree of law.** Degree is at least depth in this forest, and can exceed it,
because degree also follows chimney dependencies. Newton II has degree 2 but
depth 1: its chimney reaches Newton I's winters, though no law vertex is shared.

**What it implies.** A quantity that appears in many laws of a textbook theory
(mass in Newton II, gravitation, momentum, kinetic energy) can hold at most two
*law* roles. All other appearances go through peripheral entries. Where a
modeller wants a third law role, the quantity has to split into two headwords
plus an identification between them. That looks like the structural root of
the VD acting as an "equivalence-principle generator" (gravitational/inertial
mass, acting-force/interaction-candidate). **Not shown** is that every such case
arises this way.

---

## 6. The house count [Claude]

### 6.1 Counting

**Setting.** Scalars, generic position: the relevant Jacobians have full rank,
so counting gives the local dimension of the solution set. The November word
is known from its chimney. The two winters are the unknowns. The three triplet
entries count as **one** equation, since they are three readable orientations of
one relation (d2 §4).

| Walls | Equations | Unknowns | Excess | Lewis reading |
|---|---|---|---|---|
| 0 | 1 | 2 | $-1$ | Multiply realized, e.g. $B\to\lambda B,\ C\to C/\lambda$; terms do not denote |
| 1 | 2 | 2 | $0$ | The law is the definition of the unwalled winter |
| 2 | 3 | 2 | $+1$ | One consistency condition; the law has empirical content |

### 6.2 Readings

- **Walls are Lewis's uniqueness clause, made local.** The triplet alone never fixes its winters; the walls do.
- **The excess is the house's Ramsey content:** the number of independent empirical conditions the house imposes.
- **"Is F = ma a law or a definition?" becomes "how many independent walls does this house have?"** As reported in secondary sources, Mach grounds mass independently (inverse ratio of mutual accelerations) and Poincaré, in *Science and Hypothesis*, treats F = ma as a definition. Read that way, both are 1-wall readings with force as the unwalled winter. The "force read independently off a spring scale" view is the 2-wall reading, in which F = ma is testable.

### 6.3 Newton II with the estimator as mass's grounding

Take the case where mass's outward grounding is the estimator, which is built
from the law itself, so it adds no independent equation. With $N$ readings in
$d$ dimensions and one persistent mass:

- **the law gives** $Nd$ equations;
- **the force walls fix** the $Nd$ force components;
- **the only further unknown is** $m$.

That leaves $Nd - 1$ conditions:

- $d-1$ codirectionality conditions per reading, which matches the 2026-09-29 ruling that a $k$-dimensional reading imposes $k-1$ codirectionality conditions;
- plus agreement of the $N$ readings on one mass.

"The estimator is the definition of mass" therefore leaves Newton II empty only
for a **single one-dimensional reading**.

### 6.4 Order-invariance

Which entries count as "new" depends on log order (§8). The **global** excess
does not: equations minus unknowns over the whole theory. It is unchanged by
re-logging, so it is a candidate for the weak invariant `why_three_law_corners`
§9 item 9 asks for. It is necessary, not sufficient, for "same predictions".
Per-house excess *does* depend on how walls are allotted to houses.

### 6.5 Caveats

- For field quantities, read "one equation" as one per point.
- Excess counts dimension, not uniqueness. A nonlinear law with positive excess can still have several discrete solutions.
- Houses share equations across the log. The net-force wall of Newton II is also Force Sum's chimney, so global counts need care.

---

## 7. What the house can't see: persistence [Claude]

**Gravitation as an illustration.** Name $X := m_1 m_2 / r^2$ peripherally and
anchor the law there. The winters are $F_g$ and $G$.

- $F_g$ has a wall: it is measured as an acting force.
- $G$ has none.

So a single instance has excess $0$. The law's empirical content comes entirely
from $G$ being *the same across instances*: $N$ instances give $N-1$
conditions. Mass persistence across readings (§6.3, and the 2026-09-30 lemma)
works the same way.

Neither appears anywhere in the six-entry unit. **The house miscounts constants
and persistent properties.** Their content comes from re-identification across
instances, which is not an entry. Either the functional unit needs a slot for
persistence, or the trackability and lumping work is supplying it unnamed.
**Ruling owed** (§9 item 3): it decides whether six entries are the whole
functional unit.

---

## 8. Where the triplet hypothesis can still be falsified [Claude]

The construction of §2 can be blocked in two places, and only there can d2
§10 have teeth.

1. **What peripheral entries may be.** Suppose a peripheral entry may be a *partial* constraint: an inequality, or a relation that does not determine its headword. Then an irreducible term can be born singly, outside any law, and the triplet rule becomes optional. If peripheral entries must be **explicit definitions or residuals**, every irreducible term must be born as a winter. Then a term constrained only relationally by older vocabulary, and by no law, is the counterexample shape. Neither the December notation nor the law-house foundation settles this. `why_three_law_corners` §9 item 5 (the dossier escape hatch) is the same kind of risk at a different place.
2. **"New" is a position in the log, not irreducibility.** The acceleration wall, $a := d^2x/dt^2$, is an explicit definition; once logged, acceleration is reducible in Lewis's sense. It counted as new only because the law came first. So d2 §2's irreducibility test, read at the moment of admission, can be satisfied by choice of order. The law-house foundation accepts chronology as role-defining (§4 there), which is coherent. It means the order-invariant content has to be stated separately, and §6.4 offers the global excess as a candidate.

A reformulation of d2 §10 that could fail [Claude, offered]: *every irreducible
admission can be logged so that peripheral entries are explicit definitions or
residuals only, and no house has negative global excess once persistence is
counted.*

---

## 9. Open items

1. **Peripheral entries, ruling owed.** Explicit definitions and residuals only, or partial constraints allowed? This decides whether the triplet hypothesis is falsifiable at all (§8).
2. **The minimality premise, ruling owed.** Adopt "no residue may conceal a pairing or junction" explicitly as the premise of three-place minimality, as a reading of rule 21 (§3.4)?
3. **Persistence slot, ruling owed.** Does the functional unit need an entry for re-identification across instances, or does the trackability/lumping chain already supply it (§7)?
4. **Equivalence principles as forced splits.** Check the known VD equivalence-principle cases against §5. Do they all arise from a quantity needing a third law role?
5. **Design 3 forest check.** Run §5's check on the current Design 3 ledger.
6. **Unique-November** remains DUBIOUS (R-LAW-05). §5 gives a consequence of it (at most two laws per headword), not a justification. d2 §10 and `why_three` item 12 stand.
7. **The postponed choice function** $S^{(n)}(w)$ (§1.2): which of several active definition strings a trace consumes, and what decides.
8. **Peirce on meaning** (§3.5): worth a separate look against DoM and the handle work.
9. **Literature before outward use:** read Poincaré's chapter and Mach directly, and confirm the Löwenheim (1915) reference, which is cited here only via Koshkin.

---

## Relation to existing records

- `why_the_triplet_rule_is_needed_d2.md`: the semantic (admission) justification. This record is its formal counterpart. It answers d2 §8's caution with §3.1 and proposes a falsifiable form of d2 §10 in §8. Does not supersede or correct it.
- `why_three_law_corners_2026-10-19.md`: the empirical counterpart. §6.4 bears on its item 9, §8 parallels its item 5, and §5 bears on its item 12.
- `VD_LAW_HOUSE_FOUNDATION.md`: rules 9 and 10 are Peirce's two clauses (§3.3), rules 5–6 are derived in §4, and rule 21 supplies the minimality premise (§3.4).
- `degree_of_law_formal.md`: law list used for the §5 check; degree vs depth.
- `VD_draft1_amendments2.pdf` (December 2025 notation): origin of unique-November (R-LAW-05) and of multi-valued lookup (§1.2).
- `VD__how_to_draft1.pdf` / `draft1.1`: the Pundit/Punnet Square (§1.2).

---

## Sources

- D. Lewis, "How to Define Theoretical Terms", *Journal of Philosophy* 67(13) (1970) 427–446. Checked: bibliographic details (PhilArchive) and the unique-realization proposal via secondary accounts.
- D. Lewis, "Psychophysical and Theoretical Identifications", *Australasian Journal of Philosophy* 50(3) (1972) 249–258. Checked: details and O-term/T-term framing (first page).
- F. P. Ramsey, "Theories" (1929), in *The Foundations of Mathematics and Other Logical Essays* (1931). Not checked; from memory.
- C. S. Peirce, *Collected Papers* 1.345 and 3.423–424. Seen via secondary sources only.
- R. W. Burch, *A Peircean Reduction Thesis: The Foundations of Topological Logic*, Texas Tech University Press (1991). Checked via citing works.
- J. Hereth Correia and R. Pöschel, "The Teridentity and Peircean Algebraic Logic", ICCS 2006, LNCS 4068, Springer, 229–246, doi:10.1007/11787181_17. Checked: abstract.
- J. Hereth and R. Pöschel, "Peircean Algebraic Logic and Peirce's Reduction Thesis", *Semiotica* (2011), doi:10.1515/semi.2011.050. Checked: abstract.
- S. Koshkin, "Is Peirce's reduction thesis gerrymandered?", arXiv:2406.14058 (2024). Checked: the two-clause statement, and the reading of pairing and hidden-variable reductions as concealed triple junctions (§3).
- L. Löwenheim, "Über Möglichkeiten im Relativkalkül", *Mathematische Annalen* 76 (1915). Cited via Koshkin; not checked.
- F. Rossi, C. Petrie and V. Dhar, "On the equivalence of constraint satisfaction problems", ECAI 1990. Checked via secondary sources (hidden-variable encoding).
- U. Montanari, "Networks of constraints: fundamental properties and applications to picture processing", *Information Sciences* 7 (1974) 95–132. Checked: an n-ary constraint cannot always be represented exactly by a binary network.
- R. Dechter, "From local to global consistency", *Artificial Intelligence* 55 (1992) 87–107. Checked: Theorem 3.8 and §7 (hidden-variable domain size).
- R. Fagin, "Degrees of acyclicity for hypergraphs and relational database schemes", *Journal of the ACM* 30(3) (1983) 514–550. Checked: existence and abstract; the definition of Berge-acyclicity is from memory.
- C. Beeri, R. Fagin, D. Maier and M. Yannakakis, "On the desirability of acyclic database schemes", *Journal of the ACM* 30(3) (1983) 479–513. Checked: details.
- E. Mach, *Die Mechanik in ihrer Entwickelung* (1883); H. Poincaré, *La Science et l'Hypothèse* (1902). Positions on mass and F = ma seen via secondary sources only.
