# The VD Law-House Foundation

**Status:** consolidated working orientation note  
**Project:** VD Newton / Design 3  
**Date:** 25 August 2026

## Purpose

This note records the current law-house rules needed for VD Newton work. It separates two questions that are easy to conflate:

1. **What makes a structure a VD law at all?**
2. **What additional entries make that law usable within the dictionary?**

The core answer is:

> A physical law is an irreducible three-headword triplet represented by a directed hypercycle. The triplet is embedded in a six-entry law-house that grounds all three headwords in the rest of the dictionary.

The triplet is the formal law. The six-entry house is the complete functional unit.

---

# Part I — Basic Notation

## 1. Entries, headwords, and entry-owned residues

A VD is an append-only log of entries. Write an entry schematically as

$$
E_n:\qquad A := \operatorname{Res}_n(B,C).
$$

Here:

- $E_n$ is entry $n$;
- $A$ is the entry's headword;
- $B$ and $C$ are the two law headwords exposed inside its definiens;
- $\operatorname{Res}_n$ is the residue belonging specifically to entry $n$.

The entry index is load-bearing. There is no single free-floating residue called merely $\operatorname{Res}$. Every entry—triplet, chimney, wall, or otherwise—has its own residual position, and every residue occurs at a particular entry-position and performs the role required there. The triplet notation above simply makes the law-headword inputs explicit.

Two related notations are useful:

$$
\operatorname{Res}_9()
$$

refers to **the residue belonging to entry $E_9$**, with its inputs suppressed, while

$$
\operatorname{Res}_9(B,C)
$$

shows that same entry-owned residue together with the two headword-accessible inputs exposed at that entry.

This distinction will matter whenever we ask what a particular residue must contain, what operation it must induce, or whether its wording imports undeclared machinery.

### Residual string and residue handle

It is useful to keep two levels distinct:

- the **residual string** is the wording left in an entry after recognised headwords are removed;
- $\operatorname{Res}_n()$ is the entry-indexed operational handle or idealised residue that this wording is intended to realise in a disciplined interpreter.

The written string is the visible stimulant. The indexed residue names the role that the string must successfully perform at that entry.

---

## 2. Triplet dependencies are hypergraph dependencies

Suppose a law has three headwords $A$, $B$, and $C$, occurring at entries $E_i$, $E_j$, and $E_k$:

$$
E_i:\qquad A := \operatorname{Res}_i(B,C),
$$

$$
E_j:\qquad B := \operatorname{Res}_j(A,C),
$$

$$
E_k:\qquad C := \operatorname{Res}_k(A,B).
$$

The proper dependency structure is:

$$
A \longrightarrow (B,C),
$$

$$
B \longrightarrow (A,C),
$$

$$
C \longrightarrow (A,B).
$$

These are three **directed hyperedges**. Each headword depends jointly on a pair of daughter headwords.

The parentheses are important. They retain the fact that $B$ and $C$ are exposed together at the $A$-corner. They do not assert that the $A$-entry contains two separable dependencies that can safely be handled independently.

A conventional directed graph may project

$$
A \longrightarrow (B,C)
$$

into

$$
A\to B,
\qquad
A\to C,
$$

but this projection is **lossy**. It preserves some reachability information while erasing the jointness of the two daughters inside one entry and one residue. Treating the projection as the full structure can cause subtle mistakes, including:

- evaluating one daughter as though the other were optional;
- treating one entry as two independent definitions;
- losing the fact that one indexed residue composes the two daughter exposures;
- confusing pairwise connectivity with the actual law-corner;
- inferring relations that exist only in the reduced graph, not in the authored entry.

Accordingly:

> The VD law network is fundamentally a directed hypergraph. Any ordinary pairwise dependency graph is a derived inspection view, not the authoritative form.

If the positions of the daughters matter to the residue, $(B,C)$ should be read as an ordered pair rather than an unordered set.

---

# Part II — What Makes a VD Law

## 3. A law is a minimal three-headword hypercycle

The three hyperedges

$$
A \longrightarrow (B,C),
\qquad
B \longrightarrow (A,C),
\qquad
C \longrightarrow (A,B)
$$

form a minimal three-headword cycle. This is the **triplet**.

No member can be removed while preserving the same irreducible structure. Each corner requires the other two headwords, and the three entry-owned residues jointly establish the law.

A two-term cycle is not enough. In the present VD analysis, a structure of the form

$$
A \leftrightarrow B
$$

collapses toward a synonym pair: each term merely returns the other, with no third position available to carry non-trivial relational structure.

If an apparent law contains four or more irreducibly entangled terms, the working rule is not to enlarge the primitive law shape. Instead, look for a decomposition into overlapping triplets. This usually requires discovering an intermediate headword that has been doing conceptual work without yet being named.

Thus:

- an apparent two-term law suggests a hidden third term;
- an apparent four-or-more-term law suggests a factorisation into overlapping triplets;
- the unnamed mediator or intermediate is often the conceptual discovery produced by the analysis.

---

## 4. Exactly one headword is old and two are new

A valid triplet is temporally asymmetric when introduced into the append-only log.

Exactly **one** of its headwords must already have a prior definition. This is the **November word**, also called the **anchor**.

Exactly **two** must not yet have been defined. These are the **winter words**. They are born in the law.

If $A$ is the November word, then immediately before the triplet is introduced:

$$
A=\text{already available},
\qquad
B=\text{new},
\qquad
C=\text{new}.
$$

The triplet then locks all three together.

“November” and “winter” are not semantic labels assigned after the fact. They are identified by chronology:

- whichever headword already had an entry is November;
- whichever two did not are winters.

The roles therefore fall out of the log rather than being freely decorated onto an already completed triangle.

The compact temporal signature of a law is:

$$
\boxed{\text{one old concept}+\text{two newly born concepts}}.
$$

---

## 5. Every corner must genuinely require both daughters

At the $A$-corner, entry $E_i$ must characterise $A$ using $B$ and $C$ together:

$$
A := \operatorname{Res}_i(B,C).
$$

Likewise:

$$
B := \operatorname{Res}_j(A,C),
$$

$$
C := \operatorname{Res}_k(A,B).
$$

The hyperedge at each corner is therefore atomic at the level of law structure. The corner does not merely point separately at two unrelated headwords; its indexed residue must make their joint exposure bear on the headword being defined.

There is also a stronger writing rule:

> No one corner should state the whole law by itself.

The $A$-entry should tell us how $B$ and $C$ bear on $A$. It should not completely state the relation between $B$ and $C$ in a way that makes the $B$- and $C$-corners redundant.

The same restriction applies cyclically at the other two corners.

The complete relation among the three headwords should emerge from the **intersection of the three indexed residues**:

$$
\operatorname{Res}_i(B,C),
\qquad
\operatorname{Res}_j(A,C),
\qquad
\operatorname{Res}_k(A,B).
$$

Each corner is deliberately incomplete. That incompleteness is not a defect; it is what preserves the irreducibility of the triplet.

A useful audit question is:

> If the other two triplet entries vanished, would this one entry already communicate the whole law?

If yes, that corner has probably swallowed work that belongs to the other two residues.

---

## 6. Triplet definitions face inward

The three law entries are **inward-facing**. Their primary job is to establish each headword's role inside the law.

For example,

$$
A := \operatorname{Res}_i(B,C)
$$

should tell us how $B$ and $C$ jointly characterise $A$ within this triplet. It should not try to connect $A$ to every surrounding concept in the broader theory.

The entry-writing rule is:

> A triplet entry should perform law-internal work. Peripheral dictionary grounding belongs outside the triplet.

In the strict form of the rule, the triplet entry speaks through the other two law headwords. Reaching outward to unrelated vocabulary risks importing peripheral work into the law core, hiding assumptions, and weakening the three-cornered structure.

---

# Part III — Why a Law Needs Six Entries

## 7. Every law headword needs an inward and an outward definition

The triplet is necessary, but it is not the complete operational unit.

Each of the three law headwords ultimately needs two definitions:

1. an **inward-facing triplet definition**, which gives its place inside the law;
2. an **outward-facing peripheral definition**, which connects it to the rest of the dictionary.

Therefore:

$$
3\text{ headwords}\times 2\text{ definitions per headword}=6\text{ entries}.
$$

This six-entry structure is the **law-house**.

The two definitions of a headword are not competitors. They perform different tasks.

---

## 8. The November word receives its peripheral definition first: the chimney

Because the November word must already exist before the triplet, its outward-facing definition must occur earlier in the log.

If $A$ is November, its prior peripheral entry is:

$$
E_a:\qquad A := \operatorname{Def}_a(\ldots),
$$

with

$$
a<i.
$$

This earlier entry is the **chimney**.

Its job is to connect $A$ to vocabulary already available in the dictionary. Later, $A$ is redefined inwardly at its triplet corner:

$$
E_i:\qquad A := \operatorname{Res}_i(B,C).
$$

The November word therefore has:

1. a chimney definition — outward-facing and earlier;
2. a triplet definition — inward-facing and law-internal.

---

## 9. The winter words receive peripheral definitions afterwards: the walls

The winter words cannot receive peripheral definitions before the triplet. If they did, they would already exist and would no longer be winters.

They are first introduced at their triplet corners:

$$
E_j:\qquad B := \operatorname{Res}_j(A,C),
$$

$$
E_k:\qquad C := \operatorname{Res}_k(A,B).
$$

Only after the triplet may they receive outward-facing definitions:

$$
E_p:\qquad B := \operatorname{Def}_p(\ldots),
$$

$$
E_q:\qquad C := \operatorname{Def}_q(\ldots).
$$

These later entries are the **walls**.

Each winter word therefore has:

1. a triplet birth — inward-facing;
2. a wall grounding — outward-facing and later.

The walls make the newly born concepts usable elsewhere in the dictionary without requiring every later use to reopen the law's internal hypercycle.

---

## 10. The complete six-entry house

The abstract structure is:

$$
\boxed{
\begin{array}{rll}
E_a:&A := \operatorname{Def}_a(\ldots)&\text{chimney: peripheral November definition}\\[1mm]
E_i:&A := \operatorname{Res}_i(B,C)&\text{November triplet corner}\\
E_j:&B := \operatorname{Res}_j(A,C)&\text{winter triplet corner}\\
E_k:&C := \operatorname{Res}_k(A,B)&\text{winter triplet corner}\\[1mm]
E_p:&B := \operatorname{Def}_p(\ldots)&\text{wall: peripheral winter definition}\\
E_q:&C := \operatorname{Def}_q(\ldots)&\text{wall: peripheral winter definition}
\end{array}}
$$

subject to:

$$
a<i<j<k,\qquad k<p,\qquad k<q.
$$

The order of $p$ and $q$ relative to one another need not matter unless a later dependency imposes a further constraint. The notation $\operatorname{Def}_n(\ldots)$ is role-shorthand for an outward-facing definition; it does **not** imply that peripheral entries lack residues. Entry $E_a$, for example, still has its own $\operatorname{Res}_a()$.

An architectural mnemonic is:

```text
                 E_a: A := Def_a(...)
                         chimney
                            |
                            v
               E_i: A := Res_i(B,C)
               E_j: B := Res_j(A,C)
               E_k: C := Res_k(A,B)
                    triplet law-core
                      /           \
                     v             v
        E_p: B := Def_p(...)   E_q: C := Def_q(...)
                 wall                  wall
```

This picture is a mnemonic for entry roles and chronology. It is **not** a replacement for the authoritative hypergraph representation of the triplet.

The complete unit is called the **house with a chimney**.

---

## 11. Peripheral and triplet definitions perform complementary jobs

When a headword has two definitions, the dictionary is not saying:

> Choose whichever definition you prefer.

The two entries are complementary.

The structurally secure distinction is:

| Entry role | Primary job |
|---|---|
| Chimney | Grounds the November word outwardly in earlier dictionary content. |
| Triplet corner | Establishes the headword's inward-facing role in the law. |
| Wall | Grounds a winter word outwardly so it can participate in later dictionary work. |

Trace and evaluator work has suggested a rough computational reading:

- a chimney may supply recognition hooks, type information, or preconditions;
- a triplet corner may supply the law-internal transformation or constraint;
- a wall may supply externally usable grounding for a newly created concept.

That computational mapping is useful, but it should not be overstated as a fully settled implementation law. The firm point is structural: the entries are deliberately different views of one headword, not ambiguous duplicates.

---

# Part IV — Chronology, Adjacency, and Overlap

## 12. The ordering follows from the append-only log

The abstract chronological requirement is:

$$
\operatorname{chimney}(A)
<
\operatorname{triplet}(A,B,C)
<
\operatorname{walls}(B,C).
$$

More explicitly:

$$
a<i<j<k,\qquad k<p,\qquad k<q.
$$

The chimney must precede the triplet because $A$ must already exist. The walls must follow the triplet because $B$ and $C$ must be born there.

The three triplet entries must occur in log order, but they need not be literally adjacent in the abstract VD criterion. Other entries may intervene.

Accordingly:

> The directed hypergraph together with the chronology identifies the law; adjacency alone does not.

The current Newton Design 3 ledger adopts a stronger layout convention for clarity:

```text
chimney
triplet corner 1
triplet corner 2
triplet corner 3
wall 1
wall 2
```

This sequential six-slot layout makes houses easier to inspect and audit. It is a Design 3 authoring convention, not part of the minimal abstract criterion of lawhood.

The distinction is therefore:

- **VD law rule:** satisfy the chronological inequalities and hypercycle structure;
- **current Newton Design 3 convention:** keep each six-entry house sequential.

---

## 13. Houses can overlap

A wall from one law is an established outward-facing definition. That headword is therefore available to become the November anchor of a later law.

Schematically:

```text
Law 1:
    ...
    E_p: B := Def_p(...)      wall of Law 1

Law 2:
    E_p: B := Def_p(...)      already-available grounding for B
    ...
    E_r: B := Res_r(D,E)      November corner of Law 2
```

The same peripheral grounding can therefore do double structural duty:

- it is the wall that completes the earlier house;
- it supplies the prior definition required for the later house's November word.

This is why a mature VD theory looks like a network of interlocking houses rather than a row of isolated six-entry boxes.

A wall does not merely terminate one law. It can become an attachment point for later law structure.

---

# Part V — Residual Wording as Operational Machinery

## 14. A residue is not leftover decoration

The notation $\operatorname{Res}_n$ does not mean “irrelevant prose remaining after headword extraction.”

At the token level, an engine may mechanically obtain a residual string by removing recognised headwords from the definiens. But the remaining wording is expected to do operational work. It is the handle that routes a disciplined interpreter toward the operation required at entry $E_n$.

For a triplet corner such as

$$
E_i:\qquad A := \operatorname{Res}_i(B,C),
$$

the law is not fully specified by recording only that $A$ has access to $B$ and $C$. The wording realising $\operatorname{Res}_i()$ must cause the interpreter to make the intended use of those two headwords.

This is another reason the pairwise graph projection is insufficient. The hyperedge records that the two daughters are jointly exposed. The indexed residue records the authored operational position at which their relationship is taken up.

---

## 15. Residues must not hide undeclared concepts

Residual wording is load-bearing but only partly visible to structural audits. This creates a strict authoring obligation.

> If a residual phrase performs real conceptual work, the reaction it relies on must already be installed in the intended interpreter, or the concept must be promoted to an auditable headword.

Acceptable support may come from:

- ordinary grammar;
- stable general-language idioms used only at their installed strength;
- established scientific or cultural usage;
- stock formulas;
- lesson-installed handles;
- previously defined VD headwords.

A novel conceptual device hidden only in prose is undeclared machinery. The dependency hypergraph cannot inspect it, and a later trace cannot reliably attribute its effect.

For each entry, the right question is not merely:

> Is this sentence true?

It is also:

> What does the residual string cause the intended interpreter to do at this exact entry-position?

The indexed notation makes this audit precise. Instead of asking vaguely what “the residue” should contain, we can ask:

```text
What operation must Res_9() install?
Which reactions does Res_9() rely on?
Does the wording proposed for E9 reliably realise Res_9()?
Does Res_9() hide a concept that should become a headword?
How does Res_9(B,C) compose the two daughter exposures?
```

This will be especially important in arguments about what Newton II permits the interpreter to do with force, acceleration, and mass.

---

# Part VI — Consolidated Law-House Ruleset

The complete working ruleset is:

1. **A physical law is a minimal three-headword cycle in a directed hypergraph.**
2. **Each triplet corner is one directed hyperedge:** $A\to(B,C)$, not two authoritative single arrows $A\to B$ and $A\to C$.
3. **A pairwise dependency graph is only a lossy projection.** It must not replace the authored hypergraph.
4. **Every residue belongs to a particular entry.** $\operatorname{Res}_9()$ denotes the residue of $E_9$, whether that entry is a triplet corner or a peripheral entry.
5. **Exactly one triplet headword is previously defined.** This is the November word or anchor.
6. **Exactly two triplet headwords are new.** These are the winter words, born in the law.
7. **Each triplet entry faces inward and jointly requires the other two law headwords.**
8. **No one corner should encode the whole daughter–daughter relationship.** The complete law emerges across the three indexed residues.
9. **A two-term cycle collapses toward synonymy.** Apparent two-term laws should be searched for a hidden third term.
10. **Apparent four-or-more-term laws should be factored into overlapping triplets, usually by naming an intermediate concept.**
11. **Every law headword ultimately receives two definitions:** one inward-facing and one outward-facing.
12. **The November word's outward definition occurs before the triplet.** This is the chimney.
13. **The winter words' outward definitions occur after the triplet.** These are the walls.
14. **The complete functional law unit therefore contains six entries:** one chimney, three triplet corners, and two walls.
15. **Triplet and peripheral definitions are complementary, not competing.**
16. **Append-only chronology is load-bearing:** chimney before triplet, triplet before walls.
17. **Strict adjacency is not part of the abstract law criterion.** Hypergraph structure and chronology identify the law.
18. **Current Newton Design 3 nevertheless keeps each six-entry block sequential for clarity and mechanical inspection.**
19. **Houses can overlap.** A winter wall from one law may supply the prior grounding needed for that word to become November in a later law.
20. **Residual wording is operational machinery.** It must route a disciplined interpreter toward the intended operation.
21. **Residual prose must not conceal undeclared conceptual devices.** Promote load-bearing new concepts to headwords or compose the residue from already installed reactions.

---

# Final Compression

The most compact picture is:

$$
\boxed{
\text{outward grounding}
\longrightarrow
\underbrace{\text{irreducible three-headword hypercycle}}_{\text{law}}
\longrightarrow
\text{outward grounding}
}
$$

with the temporal asymmetry:

$$
\boxed{\text{one old concept}+\text{two newly born concepts}.}
$$

At the triplet level, the authoritative network is:

$$
\boxed{
A\to(B,C),
\qquad
B\to(A,C),
\qquad
C\to(A,B)
}
$$

and at the entry level, every operational corner is indexed:

$$
\boxed{
E_i:A:=\operatorname{Res}_i(B,C),
\quad
E_j:B:=\operatorname{Res}_j(A,C),
\quad
E_k:C:=\operatorname{Res}_k(A,B).
}
$$

This is the law-house foundation to use when analysing arguments such as **why mass must be estimated**. Newton II should not be treated as an ordinary algebraic equation whose symbols may be rearranged without regard to entry structure. The relevant question is which operations its particular triplet residues license, on which jointly exposed headwords, and under which outward grounding and input conditions.
