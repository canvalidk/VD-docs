# Degree of Law: Formal Definition and Pseudocode

**Date:** 2026-03-10
**Rule:** R-LAW-07
**Status:** Implemented and verified on Newton v0.5

---

## Setting

Let D be a VD instance with dependency graph G = (V, E) where:
- V = HD, the set of unique headwords
- E = {(w, u) : some entry with headword w references u in its definition}

Let L be the set of recognised laws in D. Each law L ∈ L is a triple:
- L.anchor ∈ V (the November word)
- L.cyclic = {C₁, C₂} ⊂ V (the two Winter words)
- L.trio = {L.anchor} ∪ L.cyclic

---

## Intuition

The degree of a law measures how many layers of prior law structure its anchor concept stands on. A law whose anchor depends on no other law's cyclic terms is degree 1 — it's a base-level commitment. A law whose anchor depends (through the non-cyclic part of the graph) on the cyclic terms of a degree-k law is at least degree k+1.

The critical subtlety: we must not walk through the law's own cyclic nodes when computing what the anchor depends on. Without this restriction, the walk follows the law's own triplet edges outward and reaches all downstream laws, making every degree near-maximal.

---

## Definition

**Pruned descendants.** For a law L with anchor A and cyclic set {C₁, C₂}, define:

    G_L = G with nodes C₁ and C₂ removed (and all their incident edges)

    Dep(L) = { v ∈ V : v is reachable from A in G_L }

This is the set of headwords the anchor can reach without passing through its own cyclic terms.

**Cyclic pool.** Define the global cyclic pool:

    CYC = ⋃_{L ∈ L} L.cyclic

**Overlap.** For law L:

    Overlap(L) = Dep(L) ∩ CYC

These are the cyclic terms of other laws that are reachable from L's anchor through non-cyclic paths.

**Degree.** Defined recursively:

    deg(L) = 1                                          if Overlap(L) = ∅
    deg(L) = 1 + max { deg(L') : L' ∈ L,
                                  L' ≠ L,
                                  L'.cyclic ∩ Overlap(L) ≠ ∅ }   otherwise

---

## Pseudocode

```
function DEGREE(L, visited):
    // L       : a recognised law
    // visited : set of law identifiers (for cycle protection)

    if L.trio ∈ visited:
        return 1                              // cycle among laws; base case

    visited ← visited ∪ {L.trio}

    // Step 1: Build pruned graph
    G_L ← copy of G
    remove L.cyclic from G_L                  // remove C₁, C₂ and all their edges

    // Step 2: Compute reachable set from anchor
    Dep_L ← DESCENDANTS(G_L, L.anchor)        // all nodes reachable from A in G_L

    // Step 3: Find overlap with other laws' cyclic terms
    Overlap_L ← Dep_L ∩ CYC                   // CYC = union of all laws' cyclic terms

    if Overlap_L = ∅:
        return 1

    // Step 4: Recurse on overlapping laws
    d_max ← 0
    for each L' ∈ L where L' ≠ L:
        if L'.cyclic ∩ Overlap_L ≠ ∅:
            d ← DEGREE(L', copy of visited)
            d_max ← max(d_max, d)

    return 1 + d_max
```

Entry point: `DEGREE(L, ∅)` for each law L.

---

## Worked example: Newton v0.5

The dependency graph has the following law chain. Arrows show non-cyclic reachability (chimney edges):

```
Newton I          anchor: uniform-motion
  |                 cyclic: {free-particle, inertial-frame}
  |                 Dep reaches: scaffold only (time, point-particle, ...)
  |                 Overlap: ∅
  |                 degree = 1
  |
  v  (inertial-acceleration chimney E20 refs inertial-frame, which is Newton I cyclic)
  |
Newton II         anchor: inertial-acceleration
  |                 cyclic: {net-force, inertial-mass}
  |                 Dep reaches: acceleration, inertial-frame, free-particle, scaffold...
  |                 Overlap: {inertial-frame, free-particle} — both Newton I cyclic
  |                 degree = 1 + deg(Newton I) = 1 + 1 = 2
  |
  v  (net-force wall E24 is also Force Sum chimney)
  |
Force Sum         anchor: net-force
  |                 cyclic: {acting-force, interacting-forces-set}
  |                 Dep reaches: inertial-acceleration, inertial-mass, then Newton I terms
  |                 Overlap: {inertial-mass} — Newton II cyclic
  |                 degree = 1 + deg(Newton II) = 1 + 2 = 3
  |
  v  (acting-force wall E31 is also Action-Reaction chimney)
  |
Action-Reaction   anchor: acting-force
  |                 cyclic: {canonical-force_ao, reaction-force_ao}
  |                 Dep reaches: interacting-forces-set, net-force, then Newton II...
  |                 Overlap: {interacting-forces-set} — Force Sum cyclic
  |                 degree = 1 + deg(Force Sum) = 1 + 3 = 4
  |
  v  (canonical-force_ao wall E36 is also Acting Object chimney)
  |
Acting Object     anchor: canonical-force_acting-object
  |                 cyclic: {acting-object, activation-condition_ao}
  |                 Dep reaches: acting-force, reaction-force_ao, then chain above...
  |                 Overlap: {acting-force, reaction-force_ao} — Action-Reaction cyclic
  |                 degree = 1 + deg(Action-Reaction) = 1 + 4 = 5
  |
  v  (interaction-candidate chimney E39 refs acting-force, interacting-forces-set)
  |
Closure           anchor: interaction-candidate
                    cyclic: {interaction-pair, mechanically-closed-system}
                    Dep reaches: acting-force, interacting-forces-set,
                      then through acting-force → canonical-force_ao,
                      reaction-force_ao, acting-object, activation-condition_ao,
                      and further up: net-force, inertial-mass, inertial-frame...
                    Overlap includes cyclic terms of ALL five prior laws
                    degree = 1 + max(deg(Acting Obj), ...) = 1 + 5 = 6
```

The detailed trace below confirms this by walking through Dep(Closure) node by node.

---

## Detailed trace: Closure

Closure: anchor = interaction-candidate, cyclic = {interaction-pair, mechanically-closed-system}

G_Closure = G minus {interaction-pair, mechanically-closed-system}

From interaction-candidate (chimney E39), the definition references:
- acting-force (→ in Dep)
- interacting-forces-set (→ in Dep)
- mechanical-system (→ in Dep)

From acting-force we can reach (via its chimney E26 and other non-cyclic entries):
- interacting-forces-set, net-force

From interacting-forces-set we can reach:
- acting-force, net-force

From net-force (chimney E22) we reach:
- inertial-acceleration, inertial-mass

And so on up the chain. But critically, can we reach acting-object or activation-condition_ao? Those are Acting Object's cyclic terms. Acting Object's anchor is canonical-force_ao. Can we reach canonical-force_ao?

canonical-force_ao is a cyclic term of Action-Reaction. From acting-force, in the original graph acting-force → canonical-force_ao (via E31). But in G_Closure we only removed Closure's own cyclic terms, so this edge is still present.

So Dep(Closure) includes canonical-force_ao, which is Action-Reaction cyclic AND Acting Object anchor. From canonical-force_ao (as a node in G_Closure), can we reach acting-object or activation-condition_ao? Yes: canonical-force_ao → acting-object and canonical-force_ao → activation-condition_ao (via E36).

So Overlap(Closure) includes:
- acting-force (Force Sum cyclic)
- interacting-forces-set (Force Sum cyclic)  
- canonical-force_ao (Action-Reaction cyclic)
- reaction-force_ao (Action-Reaction cyclic)
- acting-object (Acting Object cyclic)
- activation-condition_ao (Acting Object cyclic)
- inertial-frame (Newton I cyclic)
- free-particle (Newton I cyclic)
- inertial-mass (Newton II cyclic)
- net-force (Newton II cyclic)

Laws with cyclic overlap:
- Newton I (degree 1)
- Newton II (degree 2)
- Force Sum (degree 3)
- Action-Reaction (degree 4)
- Acting Object (degree 5)

degree(Closure) = 1 + max(1, 2, 3, 4, 5) = 1 + 5 = 6. ✓

---

## Properties

**Well-foundedness.** The recursion terminates because:
1. The visited set prevents re-entry into the same law.
2. In a finite VD, L is finite, so the recursion tree is bounded.

**Base case.** A law whose anchor's pruned descendants include no other law's cyclic terms has degree 1. These are the foundational laws — their anchors are built from scaffold terms only.

**Monotonicity.** If law L' has cyclic terms in Dep(L), then deg(L) ≥ 1 + deg(L'). Longer dependency chains produce higher degrees.

**Independence.** Two laws with no shared reachability have independent degrees. Meta-typing (degree 1) is independent of the Newton chain because raw-class's pruned descendants never reach any other law's cyclic terms.

**The degree chain is the law dependency chain.** In a linear sequence of laws where each wall becomes the next chimney, the degrees form an arithmetic sequence 1, 2, 3, ... This is the Newton instance's structure (excluding Meta-typing).

---

## Complexity

For a VD with n entries, h unique headwords, and k laws:
- Graph copy and node removal: O(h + |E|)
- Descendant computation: O(h + |E|) per law
- Recursion: at most k levels deep, each level iterates k laws
- Total: O(k² · (h + |E|))

For the Newton instance (h=33, |E|≈60, k=7), this is negligible.
