# A Rewrite-Theoretic Reading of the Valid Dictionary, Part I: The Acyclic Fragment

*Scope note.* This note covers **only** the acyclic part of a VD — the entries above (or beside) the law triplets, where definitional unfolding terminates. Law triplets, equivalence principles, and the status-tier interaction are deferred. The goal is modest: define a reduction relation `⟶` on VD entries, state the diamond property, and prove confluence for this fragment. Nothing here should be read as a claim about VD as a whole.

---

## 1. Setup

Let a **VD fragment** `D` be a finite set of entries `E₁, …, Eₙ`, where each entry has:

- a **headword** `h(Eᵢ)`,
- a **definiens** `d(Eᵢ)`, which is a finite expression built from headwords of *previously defined* entries and **residue tokens** `γ ∈ Γ` (the grounded, irreducible symbols),
- a dependency set `deps(Eᵢ) ⊆ {h(E₁), …, h(Eᵢ₋₁)}`.

The **acyclicity assumption** for this note: the directed graph with an edge `h(Eᵢ) → h(Eⱼ)` whenever `h(Eⱼ) ∈ deps(Eᵢ)` is a DAG. (This is exactly the regime where no triplet has yet been introduced.)

A **term** `t` over `D` is any expression built from headwords and residues by the same formation rules used in definientia. Let `T(D)` be the set of such terms.

## 2. The reduction relation

Define `⟶ ⊆ T(D) × T(D)` as the smallest relation closed under context such that, for every entry `E` with `h(E) = H` and `d(E) = δ`,

> `H ⟶ δ`

i.e. a single reduction step replaces *one* occurrence of a defined headword by its definiens. Write `⟶*` for the reflexive-transitive closure.

A term is in **normal form** if it contains no defined headwords — equivalently, it consists only of residue tokens and the formation operators over them. Call such a term a **residue expression**.

## 3. Termination

**Lemma 1 (Termination).** *Every reduction sequence from a term `t ∈ T(D)` terminates.*

*Proof.* Assign to each headword `H` its **height** `ht(H)` in the dependency DAG: residues have height 0, and `ht(H) = 1 + max{ht(H′) : H′ ∈ deps(E_H)}`. Extend to terms by `ht(t) = ` the multiset of heights of headword occurrences in `t`, ordered by the multiset extension of `<` on ℕ. Each `⟶` step replaces one headword `H` by an expression whose headwords all have strictly smaller height, so the multiset strictly decreases. The multiset order on ℕ is well-founded (Dershowitz–Manna), so no infinite chain exists. ∎

## 4. The diamond property

**Lemma 2 (Local confluence / weak diamond).** *If `t ⟶ u` and `t ⟶ v`, then there exists `w` with `u ⟶* w` and `v ⟶* w`.*

*Proof.* The two steps unfold occurrences of headwords `H₁` and `H₂` at positions `p₁` and `p₂` in `t`. Three cases:

1. **Disjoint positions.** `p₁` and `p₂` lie in disjoint subterms. Then unfolding one does not affect the other; performing the remaining step on each side yields the same `w`.
2. **Same position, same headword.** Then `H₁ = H₂` and `u = v`; take `w = u`.
3. **Nested positions.** Say `p₁` is a prefix of `p₂`, so `H₂` occurs *inside* the subterm at `p₁`. Unfolding `H₁` first replaces that subterm by `δ₁ = d(E_{H₁})`; the occurrence of `H₂` is preserved (possibly duplicated, if `H₁`'s definiens uses its argument positions multiple times — but in pure definitional unfolding there are no argument positions, so duplication does not arise here). Unfold all resulting occurrences of `H₂` in `δ₁` to obtain `w`. From the other side, unfold `H₂` first, then `H₁`; the same `w` results.

The "no argument positions" remark matters: VD entries are *definitions*, not function abstractions, so headwords have no bound variables to substitute into. This makes the rewrite system **orthogonal** in the technical sense — no rule overlaps with another, and no rule's left-hand side has repeated variables. ∎

## 5. Confluence

**Theorem (Church–Rosser for the acyclic fragment).** *The relation `⟶*` on `T(D)` is confluent: if `t ⟶* u` and `t ⟶* v`, then there exists `w` with `u ⟶* w` and `v ⟶* w`. Moreover, every term has a unique normal form, which is a residue expression.*

*Proof.* Termination (Lemma 1) plus local confluence (Lemma 2) gives confluence by **Newman's Lemma**. Uniqueness of normal forms is immediate from confluence: if `u` and `v` are both normal forms of `t`, the common reduct `w` must equal both. Existence of a normal form follows from termination: any maximal reduction sequence ends in an irreducible term, which by definition contains no defined headwords and is therefore a residue expression. ∎

## 6. What this buys us

Three things, no more:

1. **Residue grounding is well-defined on the acyclic fragment.** For any headword `H` above the law layer, "the residue expression of `H`" is a unique object, independent of the order in which intermediate definitions are unfolded. This is the formal content of the intuition that because-trees compress to a definite ground.

2. **Order-independence of definitional reading.** A reader who unfolds `inertial frame` before `uniform motion` and a reader who does the reverse arrive at the same residue expression. This is reassuring but unsurprising; it is the part of VD that "behaves like ordinary mathematics."

3. **A baseline against which the law layer looks anomalous.** Because confluence is so cheap on the acyclic fragment, whatever happens at the triplet layer is a genuine departure, not a generic feature of definitional systems. This sharpens the question deferred to Part II.

## 7. What this does *not* show

- Nothing about triplets. The termination proof breaks the moment a 3-cycle is admitted, because height is no longer well-defined on the cyclic component.
- Nothing about status tiers. All entries here are treated uniformly; LOCKED/DUBIOUS/BENCH play no role.
- Nothing about equivalence principles. Two headwords with different residue expressions are, in this fragment, simply distinct. The interesting case where they are empirically identified is outside scope.
- Nothing about *which* definitional systems are VDs. The proof goes through for any acyclic definitional system over a residue alphabet; it does not use anything specific to physics.

## 8. Open questions for Part II

- What is the right `⟶` for triplets? The naive extension gives a non-normalizing term in the style of the untyped λ-calculus' `Ω`, which is consistent with Church–Rosser but trivializes it.
- Does the chimney / triplet / walls structure correspond to anything in the rewrite system, or is it orthogonal to it?
- Should DUBIOUS entries license only conditional rewrites? If so, conditional rewriting has its own confluence theory and the analysis becomes more delicate.

---

*End of Part I.*
