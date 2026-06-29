# VD Newton Design 3 — Entity Identity and Meta-Typing

**Date:** 2026-04-10
**Status:** Discussion document — architectural decisions on how VD entities carry identity, with a todo item at the end

---

## Guiding Principle

Every VD entity — particle, acting-object, force — must be distinguishable as *this one here* independently of its properties. The distinguishability must be visible, countable, and supplied by the user rather than by background machinery, because the VD is a representation of the prediction-generating procedure as a human actually runs it, and any identity-tracking the evaluator performs that a human wouldn't is a failure of representation.

---

## 1. Statelessness at the Dictionary Level

The Newton case study doesn't need the dictionary to talk about change-over-time. Each application of the Newton triplets is a self-contained trace over the state of the world at one moment. If the trace needs to address a later moment, it is re-run from scratch against fresh inputs. The dictionary never has to carry "the same velocity changing" because it never talks about two moments in the same breath.

This is an architectural commitment, not a convenience. It means the VD is stateless at the dictionary level, and any appearance of state — "the velocity changed" — lives outside the dictionary, at whatever layer is stitching successive traces into a time-evolution. The dictionary's job is to say, at each moment, what the definitional commitments are; the time-evolution is a separate apparatus that feeds the dictionary fresh inputs each tick.

**Consequence:** the evaluator has no need for mutable entities. Every instance is immutable once declared by the model. Properties don't update in place; a new trace is run against a new state. This eliminates whole categories of machinery the framework would otherwise have to carry.

---

## 2. Haecceity as a Uniform Rule

The meta-typing layer commits to a single rule applied across all VD entities: every referenced entity has a distinction between its definitional content and its identity as a this-one-here. Particle1 ≠ Particle2 even when their properties are identical. This is the same rule that makes Spring1 ≠ Spring2, and the same rule that (derivatively) makes Force1 ≠ Force2.

The rule is uniform on purpose. A framework that handles identity the same way it handles recognition inputs — as a general principle applied across otherwise-different contexts — has a structural economy that a framework with three separate instantiation stories does not.

**Open subpoint:** force identity is probably inherited from the pairing (acting-object-instance × particle-instance) rather than being a primitive. A force exists as long as its pairing does, and its identity is derived from the identities of the things it relates. This keeps the uniform rule intact while acknowledging that forces are ontologically downstream. To be confirmed when the acting-object refactor lands.

---

## 3. Haskell Options Considered

The evaluator will eventually be a Haskell (or Haskell-adjacent) library. The question of *how* entities carry identity at the implementation level was explored, because the implementation choice either preserves or obscures the haecceity ledger that the meta-typing rule is trying to make countable.

**IORef / mutable references.** Rejected. IORef bundles identity and mutation into a single primitive — you cannot have one without the other. For a stateless dictionary this imports mutation that isn't needed, and worse, it makes every act of identity-creation look like an implementation detail ("oh, they used mutable references, that's just how Haskell simulations work") rather than an ontological commitment. The commitment becomes invisible again, which is exactly the failure mode the VD exists to prevent.

**Phantom types / type-level tags.** Rejected for this purpose. Good for a fixed small number of named instances, awkward for "arbitrarily many entities created as the model demands," because type-level identity doesn't let you put the instances in a list and iterate over them uniformly.

**State monad.** Considered, rejected. Imports state-threading machinery the stateless dictionary doesn't need.

**Data.Unique.** Initially attractive — opaque tokens, guaranteed unique by construction, lightweight. Rejected on the no-background-processes constraint (see §4).

**Records with explicit ID fields.** Adopted. Each entity type carries an identity field (a plain string: "p1", "r1", "F1") alongside its definitional content. Equality is defined on the ID field, not on content. Everything stays pure; there is no IO anywhere in the framework; identity is a syntactically visible feature of every entity that can be audited by inspecting the model.

---

## 4. The No-Background-Processes Constraint

The choice between Data.Unique and plain-string IDs turned on a constraint that deserves its own section, because it's load-bearing for the entire research program.

The VD is not just a specification that *could* be run by a machine — it is a specification that a *human* runs by tracing through entries with pen and paper. Every step the evaluator performs has to correspond to something the human trace performs. Any machinery the evaluator relies on that the human trace cannot reproduce is a failure of representation: the framework stops describing physics-as-practiced and starts describing some idealised alternative to the practice.

Data.Unique generates opaque tokens via a background counter managed by the standard library. A human tracing by hand has no such counter. Even if the tokens never surface in user-facing output, their *existence in the evaluator* is a commitment the human version cannot mirror. The same objection kills parse-time uniqueness checking ("the tool flags collisions"), automatic ID generation ("the evaluator hands out fresh names"), and any other form of identity-management the user does not perform themselves.

The constraint forces the identity scheme to be the one the practice already uses: the user writes "p1" and "p2" in the model, the evaluator treats them as distinct because the strings differ, and if the user writes "p1" twice they have made a modelling error the same way they would if they wrote F = ma². The evaluator does not correct it; the trace produces whatever contradiction the double-declaration entails, which is the correct behaviour for a framework whose job is to make definitional commitments visible.

This is more consistent with the haecceity-auditing goal, not less. The count of identity commitments in a model is literally the count of distinct ID strings that appear in it, visible by reading the model. There is no tool-mediated step between "what the model says" and "how many commitments it makes." The ledger is the model itself.

---

## 5. Meta-Typing as a User-Followed Rule

The meta-typing "law" is not a rule the evaluator enforces. It is a rule the *user* follows when writing the model, and the evaluator's behaviour is the mechanical consequence of the user having followed it. This matches the rest of the VD's character, where rules are things a careful reader applies rather than things a compiler checks.

Stated as a draft rule for the ledger: *Every VD entity must be introduced by the model with a distinct identity token. Entities are equal iff their identity tokens are equal. Identity tokens are supplied by the user at declaration; the evaluator never generates them.*

The three-layer structure discussed earlier — dictionary handles class refinement (acting-object → spring), meta-typing handles instantiation (spring → Spring1), data-paragraph certifies instantiation — sits underneath this rule. The rule says what identity is; the three layers say where it comes from and how it gets certified.

---

## 6. Consequences for the Evaluator Sketch

Several commitments fall out cleanly from the decisions above:

- The evaluator can be written in pure Haskell with no IO, no state monad, no mutable references.
- Entities are plain records. Identity is a string field. Equality is string equality on that field.
- A typeclass (`HasIdentity` or similar) gives one uniform place where the meta-typing rule lives in the code — any type that wants to be a VD entity must declare how to read its identity token — so the framework can be written against the typeclass rather than against specific entity types.
- The evaluator re-runs from scratch for each moment of interest. There is no persistent simulation state inside the evaluator; persistence lives entirely in whatever layer is calling the evaluator repeatedly with updated inputs.
- The user is responsible for not reusing identity tokens within a single model. The evaluator does not check this. If a reader wants to verify uniqueness, they read the model.

---

## Summary — Todo Item

| Entry | Action | Reason |
|-------|--------|--------|
| New rule: **meta-typing identity rule** | Add to rule ledger | States that every VD entity is introduced with a user-supplied identity token, equality is token-equality, and the evaluator does not generate tokens. Foundational for the evaluator sketch and for the haecceity-auditing use of the framework. |

**Depends on:** nothing upstream — this rule can be added independently of the acting-object refactor.

**Enables:** the evaluator sketch (once the Newton entries stabilise), and the formal statement of any claim that counts haecceity commitments across a model.

**Open question deferred:** whether force identity is primitive or derived from pairing. Best settled when the acting-object refactor lands, because that refactor determines what the pairing structure looks like.
