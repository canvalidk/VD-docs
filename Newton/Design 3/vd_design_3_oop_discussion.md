# VD Newton Design 3 — OOP Choices Discussion

**Date:** 2026-04-10
**Status:** Discussion note — leads to a to-do item on entry-level invariant structure
**Pairs with:** `vd_design_3_todo.md`

---

## Context

This note documents an architectural choice made during the April 10 session about how acting-forces should relate to activation-conditions in the Design 3 entry structure. The choice sits alongside the entry change list in `vd_design_3_todo.md` and adds one new item to it. The discussion below records the reasoning that produced the item, so that the choice can be revisited if the trace reveals problems.

---

## The problem restated

In the v3 trace, the interacting-forces-set is populated by a flat human declaration — "gravity and tension act on m₁." The downstream machinery (E34–E37) then processes each force and exhibits its activation-condition, canonical-force, and paired-particle. But the *reason the force was in the set* is never traced. The declaration and the justification sit in separate regions of the trace, connected only by the physicist's intention.

Design 3's guiding principle says human inputs should land at wall entries, not triplet entries. That reroutes *where* the inputs land, but it doesn't by itself answer a deeper question: once the input has landed, what guarantees that the force being in the set and the activation-condition being met are the same commitment? The entry change list handles dispatch and peripheral homes. It doesn't yet handle the entailment structure.

## Three candidate structures

Three ways of relating force-membership to activation-condition were considered.

**Procedural gating.** The trace populates the IFS by running an unfold — for each candidate acting-object, check the activation-condition, and yield the canonical-force into the set if the condition passes. This is the FP set comprehension pattern. It's computationally honest and matches lazy evaluation cleanly. But it's still a *procedure*. The force being in the set is a consequence of a check that the trace ran. Someone could, in principle, assert the force without running the check — they'd be violating the procedure, but not contradicting the definitions themselves.

**Proposal-based unfolding.** Candidates are proposed one at a time (by the human or by the dictionary's known acting-object types), each passes through the activation gate, and accepted candidates yield their canonical-forces. This is what the first sketch of the unfold looked like. Same problem as above — the link is procedural, not definitional. And it introduces an awkward `→ human: any more candidates?` termination step.

**Definitional entailment.** Membership in the IFS is *defined* such that it entails activation-condition satisfaction. Not "check, then insert" but "if in set, then satisfied, as a matter of what the words mean." A force being in the set without its activation-condition being met isn't an error — it's a contradiction in terms, structurally identical to asserting that an acting-force has no paired-particle. The trace doesn't check the condition; it *exhibits* it, in the same way it already exhibits the paired-particle.

The third option was chosen. The first two are procedurally correct but definitionally weak; they require discipline from the reader to stay valid. The third is self-enforcing — anyone who uses the VD's definitions inherits the entailment whether they notice it or not.

## Why the parallel to paired-particle is load-bearing

The paired-particle already sits in the position we want activation-condition to occupy. When the trace walks any acting-force through E34 → E37, it necessarily encounters the paired-particle as a definitional component of the acting-object. The paired-particle isn't checked and then attached — it's part of what an acting-object *is*. Denying it while asserting the acting-force is incoherent.

This gives Design 3 a template. Whatever structural role the paired-particle plays in the acting-object definition, the activation-condition should play the same role. They should both appear as definitional components, both be traced through when any acting-force is evaluated, and both be denied only at the cost of contradiction.

The symmetry is clean and intentional:

- **Force in set → paired-particle exists.** Looking *outward* at the interaction structure. Grounds the force in Newton III.
- **Force in set → activation-condition met.** Looking *inward* at the particle's properties. Grounds the force in the modelling context.

One rule pins the force to the external world (something must receive the reaction). The other pins it to the local situation (something must be happening here that triggers the mechanism). Together they close off the two ways the force could be "floating" — unconnected to any reaction source, or unmoored from any physical circumstance.

## What this means for the entries

The acting-object entry structure needs to make activation-condition a *component* of the acting-object in the same syntactic position as paired-particle. The trace for any canonical-force then routes:

```
canonical-force
  └─ of acting-object A
       ├─ paired-particle of A: (entailed, exhibited)
       └─ activation-condition of A: (entailed, exhibited)
            └─ satisfied by the bearer particle
```

Both components fall out of tracing the acting-object. Neither is a separate step.

This changes what the concrete force-type entries (item #6 in the entry change list) have to carry. The concrete canonical-force entry can't just supply the force law as empirical content — it has to supply it *as a component of an acting-object whose activation-condition is also specified*. The dispatch destination isn't one entry per concrete quantity (force law, condition, etc.), it's a concrete acting-object hub that packages all three components together. Spring force, spring activation condition, and spring paired-particle belong to the same concrete entry cluster, routed through the same dispatch.

This also has implications for the IFS wall (item #5). If the entailment holds definitionally, then the IFS wall can be written to make membership-entails-activation explicit at the peripheral level, rather than relying on the triplet to carry the whole burden. A reader arriving at the wall sees immediately: this set contains exactly the forces whose activation-conditions are met, by definition.

## Connection to the one-at-a-time model

The definitional-entailment choice doesn't replace the one-at-a-time evaluation model discussed on March 30 — it sits underneath it. One-at-a-time handles the *computational* honesty point: the IFS can't be built as a batch, it has to be populated incrementally through mechanical-composition. Definitional entailment handles the *structural* honesty point: whatever ends up in the IFS must have passed through the activation-gate as a matter of what membership means.

The two layer cleanly. Mechanical-composition populates one acting-object at a time (one-at-a-time model). Each acting-object brings its activation-condition with it as a definitional component (definitional entailment). The composition process can't insert an acting-object whose condition is unmet without generating a term-level contradiction.

## Where this could still go wrong

The main risk is that the entailment becomes circular or vacuous. If "the activation-condition is met" is defined as "the force is in the set," and vice versa, the entailment holds trivially and carries no content. To avoid this, the activation-condition entries have to carry *independent* content — a concrete, checkable statement about the particle's situation ("attached to spring and displaced from equilibrium") that could in principle be evaluated without reference to the IFS.

The concrete activation-condition entries (part of item #6 in the change list) are where this independence has to live. They need to be written so that the condition is a claim about the particle's physical circumstance, with a truth-value determined by the modelling context, not by whether the force happens to be in the set. The entailment then runs in one direction: force-in-set implies condition-met, and condition-met can be verified independently by examining the particle.

This is a wording constraint on the concrete activation-condition entries rather than a separate architectural item. But it should be kept in mind when those entries are drafted.

---

## To-do item (to be added to `vd_design_3_todo.md`)

**10. Acting-object component structure — activation-condition parity with paired-particle (NEW)**

*Current:* The v3 trace treats paired-particle as a definitional component of the acting-object (exhibited during E34 → E37 traversal), but treats activation-condition as a separate gated step. The two winter words of the acting-object law have asymmetric structural positions.

*Problem:* The asymmetry lets readers assert an acting-force on a particle without structurally committing to the activation-condition being met. The force-in-set ↔ condition-met relationship holds procedurally (because the trace happens to check it) but not definitionally (because the entry structure doesn't enforce it as a term-level entailment).

*Direction:* Restructure the acting-object entry cluster so that activation-condition occupies the same structural position as paired-particle — a definitional component of the acting-object, exhibited whenever any canonical-force is traced. The entailment "force in IFS → activation-condition satisfied" should hold as a tautology under the VD's definitions, not as a consequence of a procedural check. Denying the entailment while using VD terminology should produce a contradiction in terms, structurally identical to denying the paired-particle.

*Dependencies:*
- Requires item #3 (acting-object wall) to be written with activation-condition as a peripheral component, not just paired-particle.
- Constrains item #6 (concrete force entries): the concrete hub must package canonical-force, activation-condition, and paired-particle as co-components, not as independent slots.
- Constrains item #5 (IFS wall): the wall should make membership-entails-activation explicit at the peripheral level.
- Requires concrete activation-condition entries to carry independent checkable content, to prevent the entailment from becoming vacuous.

*Owner:* Open.
