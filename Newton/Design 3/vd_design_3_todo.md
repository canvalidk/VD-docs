# VD Newton Design 3 — Entry Change List

**Date:** 2026-04-01
**Status:** Working document — entries agreed for change, with rationale and direction

---

## Guiding Principle

Human inputs should land at wall/peripheral/scaffold entries, not at triplet entries. Every place where the current trace forces a human input at a triplet entry indicates either a missing wall or an underwritten one. Design 3 fixes these.

---

## 1. E18 — Inertial-frame wall (REWRITE)

**Current:** "A reference-frame standard for Newtonian analysis of motion; historically, a Galilean reference frame."

**Problem:** Too thin. Carries no operational content. The trace bypasses it and goes to E16 (triplet) for the recognition check, which incorrectly triggers meta-typing and generates sub-demands for free-particle and uniform-motion. The wall should be where the physicist's frame commitment lands.

**Why it matters:** Newton I is the soundness guarantee for the entire downstream pipeline. Working in an inertial frame ensures that every observed acceleration corresponds to a real force from a real source, which is what makes closure sound. E18 needs to carry this protective role — the physicist reads it and understands that if their frame doesn't have this property, force-accounting will hallucinate objects (fictitious forces).

**Direction:** Rewrite to carry the operational meaning. Something that conveys: a reference-frame in which observed accelerations correspond to real forces from identifiable sources. The frame commitment is a modelling decision at the wall, not a classification via meta-typing.

**Owner:** Can (has specific wording in mind)

---

## 2. E20 — Inertial-acceleration chimney (SUBTLE CHANGE)

**Current:** "The acceleration of a point-particle as measured in an inertial-frame."

**Problem:** Doesn't signal the gap between itself and E8 (raw acceleration). Easy to read as "just acceleration with a frame label" rather than understanding that raw acceleration in a non-inertial frame includes fictitious contributions that don't correspond to real forces.

**Direction:** Subtle wording change to make the distinction from E8 load-bearing. Needs to convey that inertial-acceleration is the quantity you're allowed to feed into Newton II, without overloading the chimney's job.

**Owner:** Can (has specific wording in mind)

---

## 3. Acting-object wall (NEW ENTRY)

**Current:** Missing entirely. The acting-object law's winter words (acting-object, activation-condition_acting-object) have no wall entries.

**Problem:** Recognition inputs #4–7 in the Atwood trace land at E34 (triplet). Meta-typing looks up class-specific-features and finds only the triplet definition. The human checks "does this have an activation-condition and canonical-force?" — which is the triplet's inward-facing characterisation, not a standalone recognition criterion.

**Direction:** Add a wall entry for acting-object that gives the peripheral, standalone meaning. Something that captures what an acting-object IS in intuitive terms (a reusable force-producing mechanism possessed by a particle) without restating the triplet's internal slots. The wall carries the recognition; the triplet carries the computation.

---

## 4. Activation-condition_acting-object wall (NEW ENTRY)

**Current:** Missing. No wall exists for the second winter word of the acting-object law.

**Problem:** In the trace, the human supplies concrete activation conditions ("m₁ has nonzero mass and is in Earth's gravitational field") at E35 (triplet). But E35 only says what activation-conditions DO in general. The concrete content comes from the specific force type.

**Note:** This partly collapses into the dispatch problem (#7). The abstract wall says what an activation-condition is peripherally; the concrete content comes from dispatch destination entries. Both are needed.

**Direction:** Add a wall that characterises activation-conditions in standalone terms — the physical circumstance under which a force mechanism becomes active.

---

## 5. Interacting-forces-set wall (NEW ENTRY or RESTRUCTURE)

**Current:** E25 is the only definition of interacting-forces-set, and it's a triplet entry. No wall exists.

**Problem:** Modelling inputs #8–9 (IFS population) land at E25 (triplet).

**Depends on:** Whether we commit to the one-at-a-time model from the March 30 session. Under that model:

- Forces enter the IFS individually via mechanical-composition → activation-condition filtering, not as a batch.
- The batch population at E25 dissolves into a sequence of "is there another acting-object?" questions plus "probably no" closures.
- The IFS wall just says what the set IS peripherally, and nobody ever asks the human to populate it as a batch.
- The human inputs migrate to the acting-object / mechanical-composition level.

If the one-at-a-time model is adopted, the IFS wall exists but doesn't carry a human input directly — it becomes a structural entry that describes the collection, with the actual human inputs arriving through the composition chain.

**Direction:** Write a wall for IFS. Decide whether E25 (triplet) also needs rewriting to reflect the one-at-a-time evaluation logic.

---

## 6. Concrete force type entries (NEW ENTRIES — dispatch destinations)

**Current:** No concrete force entries exist. The trace gets stuck at E36 (triplet) and the human supplies empirical force law values there.

**Problem:** Empirical input #11 lands at a triplet entry because there's no dispatch path to a concrete entry. This is the central dispatch problem.

**Direction:** For each concrete force type used in the Newton instance, add peripheral entries:

- **Type hub entry** (e.g., `near-earth-gravity`): references both abstract and concrete slot headwords, carries the dispatch mapping. The trace arrives here via meta-typing classification of the acting-object.
- **Concrete canonical-force entry** (e.g., `canonical-force_near-earth-gravity`): carries the actual force law (F = −mg). This is where the empirical human input lands.
- **Concrete activation-condition entry** (e.g., `activation-condition_near-earth-gravity`): carries the specific condition. This is where the recognition check lands.

The type hub is the dispatch hub — one entry per concrete type that carries the structural burden. The other two are ordinary definitions carrying domain content.

**Depends on:** Resolution of the underscore/tokeniser question (whether underscores free their qualifier as a separately matchable headword, or whether dispatch is handled purely through explicit cross-references in the entry text).

---

## 7. Dispatch mechanism (ARCHITECTURAL DECISION)

**Current:** No dispatch exists. The trace hits abstract acting-object slots and gets stuck.

**Problem:** See #6. The abstract-to-concrete link is the primary architectural gap.

**Options explored (March 30 session):**

- **Option A (plain entry conventions):** The type hub entry explicitly mentions both abstract and concrete headwords. Dispatch falls out of the definition text. Derived from trace necessity.
- **Underscore rule change:** Tested — underscores free their qualifier as a separately matchable headword. Produced only 3 new edges but introduced circular law dependency between action-reaction and acting-object laws. Needs more work.

**Key insight from March 30:** The human supplies the type at the modelling-decision point (when populating mechanical-composition). Meta-typing has already visited the type definition during classification. If the type definition contains the abstract-to-concrete mapping, dispatch falls out of classification. No separate mechanism needed.

**Direction:** Try Option A first with a concrete example (near-earth gravity on the Atwood machine). If the trace executes cleanly, commit. If not, revisit.

---

## 8. Mechanical-composition and paired-particle (REVIEW)

**Current:** E37 (mechanical-composition_point-particle) and E38 (paired-particle_acting-object) were added/revised in v0.6 to fix the ownership inversion bug.

**Problem:** Under the one-at-a-time model, mechanical-composition becomes the entry where the human declares "this particle has these acting-objects." This is a modelling decision. The entry should be a wall-type entry where this input lands cleanly.

**Direction:** Review E37's wording to ensure it supports the one-at-a-time evaluation model. May need to explicitly convey that populating the composition is an iterative modelling process, not a batch declaration.

---

## 9. Closure-forced inputs (DEFERRED)

**Current:** Inputs #14–17 land at the closure failure diagnostic. They don't route to any wall entry — they come from the physicist modelling external objects.

**Problem:** Under the guiding principle, these should also be routable to walls. But the external objects (string, pulley, Earth) aren't in the dictionary, and the constraints (masslessness, inextensibility) come from modelling those objects.

**Direction:** Deferred. To be figured out after the core entry changes are done. Possible approaches: wall entries for concrete mechanism types (string, pulley) that carry the relevant constraints, or a structural acknowledgment that closure-forced inputs are a separate category.

---

## Summary — Entry Change Map

| Entry | Action | Reason |
|-------|--------|--------|
| E18 (inertial-frame wall) | Rewrite | Carry protective/operational role of Newton I |
| E20 (inertial-acceleration chimney) | Subtle change | Signal gap from raw acceleration |
| New: acting-object wall | Add | Recognition inputs need peripheral home |
| New: activation-condition wall | Add | Abstract standalone characterisation |
| New: IFS wall | Add | Peripheral definition of the set |
| New: concrete force entries | Add | Dispatch destinations for empirical inputs |
| E37 (mechanical-composition) | Review | Support one-at-a-time model |
| E25 (IFS triplet) | Possibly rewrite | Reflect one-at-a-time evaluation |
| Dispatch mechanism | Decide | Architectural prerequisite for concrete entries |
| Closure routing | Deferred | Determine how closure inputs reach walls |
