# VD Acting-Object Ownership Fix

**Date:** 2026-03-26
**Resolves:** Acting-object ownership bug (reported 2026-03-06)
**Affects:** E37 (replaced), new entry inserted between E36 and E37
**Status:** Verified against all four Cases

---

## Problem

The old E37 defined acting-objects as standalone entities that "carry" a paired-particle. The ownership arrow pointed from acting-object to particle (push model). This meant forces firing into a mechanical system S from external sources (Case 3: source outside S, target inside S) were not traceable from inside S — only visible as orphaned symptoms on particles in S.

## Fix

Two replacement entries invert the ownership so that particles *have* acting-objects (composition), with paired-particle defined as a back-reference derived from that composition.

### RE36.5 — New entry (mechanical-composition\_point-particle)

Inserted between E36 and E37.

> "The mechanical-composition\_point-particle of a point-particle is the set of acting-object|s that the point-particle has. When a point-particle serves as the representative, or centre of mass, of a body, all acting-object|s of that body are included in the mechanical-composition\_point-particle of that point-particle."

### RE37 — Replaces E37 (paired-particle\_acting-object)

> "The paired-particle\_acting-object of an acting-object is the point-particle whose mechanical-composition\_point-particle includes that acting-object. The acting-object is modelled as located at the position of its paired-particle\_acting-object."

### Old E37 (superseded)

> "Each acting-object carries an associated particle, called its paired-particle\_acting-object. The acting-object is considered to be located at the position of its paired-particle\_acting-object. The particle may act as the object's centre of mass."

---

## Entries unchanged

- **E34–E36** (acting-object triplet): No reference to paired-particle or ownership. Clean.
- **E39** (interaction-candidate chimney): Already defines candidates from the particle side. Clean.
- **E40–E42** (closure triplet): No changes needed.
- **E43** (interaction-pair wall): References paired-particle\_acting-object but only uses the back-reference, which still means the same thing under the new model.
- **E44** (mechanically-closed-system residual): No changes needed.

---

## Verification: Four Cases

**Setup.** Two particles p and q. One acting-object A in q's mechanical-composition (so q is A's paired-particle). p fulfills A's activation-condition. Canonical force from A acts on p; reaction force acts on q. S is the mechanical system under analysis.

### Case 1 — p ∈ S, q ∈ S (both inside)

- E39: canonical force on p is a candidate (p ∈ S). Reaction force on q is a candidate (q ∈ S).
- E43: both candidates correspond to same acting-object A, one canonical, one reaction. They pair.
- E42: all candidates paired → **closure passes.** ✓

### Case 2 — p ∈ S, q ∉ S (target inside, source outside)

- E39: canonical force on p is a candidate (p ∈ S). Reaction force on q is NOT a candidate (q ∉ S).
- E43: canonical force candidate has no matching reaction in the candidate pool.
- E42: orphaned candidate → **closure fails.** ✓

### Case 3 — p ∉ S, q ∈ S (source inside, target outside)

- E39: reaction force on q is a candidate (q ∈ S). Canonical force on p is NOT a candidate (p ∉ S).
- E43: reaction force candidate has no matching canonical in the candidate pool.
- E42: orphaned candidate → **closure fails.** ✓

### Case 4 — p ∉ S, q ∉ S (both outside)

- E39: no candidates generated from this interaction.
- E42: no candidates, nothing to fail → **closure unaffected.** ✓

---

## Design notes

- **Exclusivity** (each acting-object belongs to exactly one particle) is carried by the definite article "the" in RE37 ("the point-particle whose..."), not by an imperative constraint.
- **Co-location** is flagged as a modelling convention ("modelled as located at") rather than a physical fact, reflecting that COM may not coincide with the physical body (e.g., a donut, a boomerang).
- **Dependency direction** is clean: RE37 depends on RE36.5, not the reverse. No circular glue.
- The bug report's concern about "two fundamentally different detection mechanisms" for Cases 2 and 3 dissolves because E39 defines candidates from the particle side. Both cases fail symmetrically through the same pairing mechanism.
