# VD Design Note: The Dispatch Problem for Concrete Acting-Objects

**Date:** 2026-03-26
**Context:** Preparing to encode concrete acting-objects (gravity, springs, friction, etc.)
**Status:** Open design question — no solution chosen yet

---

## The Problem

The VD has a working abstract layer for acting-objects. The acting-object law (E34–E36) establishes the *shape* of an acting-object: it has an activation-condition and a canonical-force. Meta-typing (E28–E30) can confirm that any concrete object satisfying these features counts as an acting-object. Mechanical-composition (E37) assigns acting-objects to particles. Force-sum (E24–E26) integrates their contributions.

What's missing is the link between these layers. When the program trace encounters a specific acting-object — say a spring — it needs to know:

1. That this acting-object is a spring (classification)
2. That because it's a spring, its activation-condition is activation-condition_spring and its canonical-force is canonical-force_spring (dispatch)
3. That spring has additional attributes beyond the abstract interface — equilibrium-position, stiffness, etc. (extension)

Step 1 is handled by meta-typing. Step 3 is just additional entries. Step 2 is the gap. Nothing in the current architecture tells the trace *how to get from the abstract call to the concrete implementation*.

## Why This Gap Exists

The acting-object law says: "an acting-object is an object equipped with an activation-condition_acting-object and a canonical-force_acting-object." When the trace evaluates an acting-object, it decomposes it into these two components. But "activation-condition_acting-object" is the abstract headword — it names the *slot*, not the *content*. For a spring, the content is activation-condition_spring. For gravity, it's activation-condition_gravity. The abstract slot and the concrete filler are different headwords.

In a conventional programming language, this is the problem that virtual method tables (vtables) solve. A vtable is a lookup structure attached to each object that maps abstract method names to concrete implementations. When you call `object.getForce()`, the runtime doesn't look up the abstract definition of `getForce` — it looks at the object's vtable, finds the concrete implementation (e.g., `Spring.getForce`), and dispatches to that instead.

The VD has no vtable. When the trace encounters an acting-object's activation-condition, it resolves to E35 (the abstract definition), which says what activation-conditions *do* in general — but doesn't say what *this particular* activation-condition *is*. The trace has no instruction telling it to look for the spring-specific version.

## What the Trace Needs

Here is a concrete example. Suppose particle p has a spring acting-object S in its mechanical-composition. The trace is evaluating the force on p via the force-sum law.

**Current trace (abstract layer only):**

1. Force-sum (E24): net-force on p = sum of acting-forces in interacting-forces-set
2. For each acting-force → comes from an acting-object in p's mechanical-composition
3. For acting-object S: check activation-condition_acting-object (E35)
4. **STUCK**: E35 tells us that *if* a particle fulfills the condition, the canonical-force fires. But it doesn't tell us what the condition *is* for this specific acting-object.

**What we need the trace to do:**

1. Force-sum (E24): net-force on p = sum of acting-forces in interacting-forces-set
2. For each acting-force → comes from an acting-object in p's mechanical-composition
3. Recognise that acting-object S is a spring (meta-typing)
4. **DISPATCH**: because S is a spring, resolve activation-condition to activation-condition_spring and canonical-force to canonical-force_spring
5. Evaluate activation-condition_spring for p → checks whether p is connected to another particle by an elastic element with rest length L
6. Evaluate canonical-force_spring → F = -k(d - L) along the line between particles

Step 4 is the vtable lookup. Something must tell the trace: "this acting-object is a spring, therefore substitute the spring-specific headwords for the abstract ones."

## What Generates the Vtable Constraint

The constraint comes from wanting the VD to be a *complete* program — one that a trace can execute without the human importing unencoded physics knowledge. Currently, the human fills in step 4 by recognising "oh, this is a spring, so I use Hooke's law." That recognition is physics knowledge applied at runtime. If we want the VD to be self-sufficient, that dispatch must be encoded.

The constraint is specifically about the *relationship between abstract and concrete headwords*. It's not enough to define activation-condition_spring as a standalone entry. The trace also needs to know that when it's evaluating the activation-condition of a spring acting-object, activation-condition_spring is the entry to use. That "when X is of type Y, use Z" pattern is the dispatch.

## Architectural Options

### Option A: No new law — dispatch via entry convention

Each concrete acting-object type gets entries that explicitly state the mapping. For example:

> "A spring is an acting-object. The activation-condition_acting-object of a spring is activation-condition_spring. The canonical-force_acting-object of a spring is canonical-force_spring."

This is the simplest approach. The dispatch is encoded directly in the definition of "spring" — when you look up what a spring is, the definition tells you where to find its activation-condition and canonical-force. No new law needed; meta-typing confirms the IS-A relationship; the entry itself carries the vtable.

**Advantages:** Simple. No new structural machinery. Each concrete type is self-documenting.

**Disadvantages:** The dispatch pattern repeats for every concrete type. There's nothing in the architecture that *requires* concrete types to provide this mapping — it's a convention, not a structural guarantee. The trace must know to look for this pattern in the definition.

### Option B: A new "type-dispatch" law

Introduce a law that formalises the relationship between an abstract class, a concrete subtype, and the specialised features. Something like a trio: {raw-class, concrete-subtype, specialised-features} — where the law says that when something is classified as a concrete-subtype, the abstract slots resolve to the specialised-features.

This would give the dispatch pattern structural force: the law would tell the trace *in general* how to handle the abstract-to-concrete resolution, and each concrete type would just instantiate the law.

**Advantages:** The dispatch pattern is encoded once at the law level. Every concrete type follows the same structural pattern. The trace has a single rule for resolution.

**Disadvantages:** It's a new law, which means a 3-cycle, which means genuine mutual undefinability between three concepts. Do these three concepts actually require each other? Or is this forcing a law where plain entries would do? The VD should only have laws where circularity is genuine.

### Option C: Extend meta-typing to carry dispatch

Meta-typing already handles classification: "is X an instance-of C?" Perhaps it could be extended (or its wall entries enriched) to also carry: "and if so, which specialised features does X have?" This would make dispatch a consequence of classification rather than a separate mechanism.

Concretely, the meta-typing wall entries (currently missing) could say something like: when an object is recognised as an instance-of a raw-class C, its class-specific-features resolve to the features of C. For a spring, the class-specific-features include the specific activation-condition and canonical-force.

**Advantages:** Reuses existing machinery. Classification and dispatch happen in the same step. No new law.

**Disadvantages:** Meta-typing is currently about recognition ("does X have the features of C?"), not about resolution ("given that X is a C, where are X's features?"). Adding dispatch might overload the law beyond its natural scope.

### Option D: Extend the acting-object law itself

Perhaps the acting-object law's wall entries (currently missing) could carry the dispatch. The wall for acting-object could say: "an acting-object of a given type resolves its activation-condition and canonical-force to the type-specific versions."

**Advantages:** Puts the dispatch exactly where it's needed — in the acting-object architecture.

**Disadvantages:** This is acting-object-specific. If other abstract classes also need dispatch (which they might, eventually), this doesn't generalise.

## The Deeper Question: Is the Circularity Real?

The key test for whether we need a new law is: are there three concepts in the dispatch pattern that genuinely cannot be defined without each other?

In the acting-object law, the circularity is real: you can't say what an acting-object IS without mentioning activation-condition and canonical-force, and you can't say what those ARE without mentioning acting-object. They're born together.

For dispatch, the question is: can you define "concrete subtype" without "specialised features" and vice versa? Or can you define them independently and just *associate* them?

If a spring can be fully defined as "an acting-object with these specific features" — without circularity — then no law is needed. If the concepts of "being a spring," "having spring-specific activation conditions," and "having a spring-specific force law" are genuinely mutually defining — where none of the three can be explained without the other two — then a law is warranted.

This question should be answered by attempting to write the concrete entries and seeing whether the definitions naturally close into a cycle or can be laid down sequentially.

## Recommended Next Step

Try Option A first: write concrete entries for a simple case (near-Earth gravity or a spring) as plain entries with explicit dispatch in the definition. If the trace can execute cleanly — abstract law decomposes into abstract slots, dispatch resolves to concrete slots, concrete entries evaluate — then no new law is needed and meta-typing plus entry convention handles inheritance.

If the trace gets stuck — if there's a point where the human must intervene to do the dispatch because no entry tells the trace what to do — then we know the gap is real and can decide between Options B, C, and D with concrete evidence about where the architecture breaks.
