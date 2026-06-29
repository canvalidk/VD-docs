# VD Design 3 — Trace Architecture for Force Evaluation

**Date:** 2026-04-16
**Status:** Working design note — captures the intended trace structure for Design 3
**Context:** Preparing to rewrite E25 and add supporting entries so the force-evaluation pipeline runs with less human assistance

---

## 1. Acting-Forces Are Functions, Not Values

An acting-object is not a force waiting to be evaluated. It is a function — a callable that, when invoked against a particle's state, produces a force. When the trace asks "is there another acting-object on p?" and the human says yes, what enters the trace is this callable. It has no committed force-value, no magnitude, no direction. It carries the *capability* to produce a force; the actual force is the result of running it.

This distinction matters because it changes when information commits. The acting-object enters the trace as an unevaluated function. Its type (gravity, spring, contact) is not yet determined. Its activation-condition has not been checked. Its canonical-force has not been computed. All of that happens later, when the trace demands it — not at the moment the acting-object is handed over.

An acting-force, similarly, is a function. When the acting-object's activation-condition fires and its canonical-force is invoked, what arrives is an acting-force — but this too is a callable, not a vector. It enters the action-reaction structure (E31–E33) as something whose concrete content will be determined by the acting-object that produced it. The acting-force is a handle pointing back to its source; its value comes from resolving that source.

---

## 2. Both Paths Get Stuck at the Same Point

Once an acting-force f enters the trace, E31 classifies it: f is either a canonical-force_acting-object or a reaction-force_acting-object.

**Canonical side.** f came from running ao's canonical-force, so f is a canonical-force_acting-object. E36 says the canonical-force is the acting-force that ao exerts on p. But the abstract slot `canonical-force_acting-object` tells us *that* f is ao's canonical-force — not *what* that force is. To get the actual force law (Hooke's law, gravitational inverse-square, etc.), the trace needs to know ao's concrete type. The trace is stuck here, waiting on dispatch.

**Reaction side.** E32/E33 say the reaction-force is the negative of the canonical-force, exerted on ao's paired-particle q (via E38). The negation is a structural operation, but it operates on f. Until f has content, −f has no content. The reaction side is stuck for exactly the same reason — both paths are waiting on the same missing piece.

**The single stuck point is ao's concrete identity.** Resolving the dispatch — determining *which kind* of acting-object ao is — simultaneously unblocks both the canonical-force (giving f a value) and the reaction-force (giving −f a value on q). Classification is dispatch: knowing what type of function ao is tells the trace which concrete activation-condition and canonical-force to invoke.

---

## 3. IFS Iteration Via Three Entries

The interacting-forces-set currently requires a single human input at the triplet entry E25: "what acting-forces act on p?" This is a modelling decision landing at a triplet, which violates the Design 3 wall principle. The fix distributes the iteration across three entries.

### E25 (triplet, rewritten)

**Role:** Defines what the IFS *is* — the set of acting-force elements whose vector sum gives the net-force on p at t. Preserves the 3-cycle edges to `acting-force` and `net-force`.

**What the trace reads:** IFS is a set. Its elements are acting-forces. The sum of those elements is the net-force. To compute the sum, the trace must obtain the elements.

### IFS wall 1 (new entry)

**Role:** The generator. States that there are as many acting-forces in the IFS as needed to capture all the mechanical interactions of the particle.

**What the trace reads:** A standing instruction to keep demanding acting-forces. Each demand produces a fresh acting-force slot. That slot is filled by invoking an acting-object from p's mechanical-composition through the full pipeline (E34 → E35 → E36 → E31). The wall re-fires after each acting-force is obtained: "as many as needed" means the trace loops back and asks again.

### IFS wall 2 (new entry)

**Role:** The terminator. States that if all the mechanical interactions have been considered, there won't be anything else in the list.

**What the trace reads:** A stopping condition. Once the human has reported all relevant acting-objects (and the last slot was filled by ao₀, the zero acting-object), this entry fires: nothing further will arrive. The loop closes. The sum is complete.

### How the three work together

1. E25 demands the sum of acting-forces in the IFS.
2. IFS wall 1 says there are as many as needed — the trace demands one.
3. An acting-object enters, the pipeline runs, an acting-force (with value) joins the set.
4. The trace returns to IFS wall 1 — still "as many as needed." Demands another.
5. Repeat until the human gives ao₀.
6. ao₀ runs through the pipeline, returns the zero vector.
7. IFS wall 2 fires: all interactions considered, nothing else in the list.
8. Loop closes. Sum is complete. Net-force has a value.

Human inputs in this loop are:
- "Here is the next acting-object" — modelling input, landing at the mechanical-composition wall (E37).
- "The next acting-object is ao₀" — the same kind of input, expressing "I've covered everything."

Both land at walls. The triplet entry E25 receives no direct human input.

---

## 4. The Zero Acting-Object (ao₀)

ao₀ is an acting-object whose activation-condition is universally satisfied and whose canonical-force is the zero vector. Its reaction-force is also zero. It is a structurally valid acting-object that contributes nothing to any computation.

### Why ao₀ is necessary

**Problem 1 — iteration termination.** Without ao₀, the "no more forces" answer requires the trace to backtrack out of a demand it has already entered. The trace asks "is there another acting-force?" and if the answer is no, the current acting-force demand must be unwound. ao₀ eliminates the backtrack: "no more forces" is expressed by giving ao₀ to the current slot. The demand completes normally (with zero), and the termination entry closes the loop.

**Problem 2 — the empty-set sum.** Net-force is defined as the sum of acting-forces in the IFS (E24). Nothing in the entries says this sum defaults to the zero vector when the set is empty. Nothing says net-force is a 3-vector by default. A free particle with no acting-objects would have an empty IFS, and the sum Σ{} is undefined within the trace. ao₀ prevents this: every particle has at least ao₀ in its mechanical-composition, so every IFS contains at least one element, and the sum is always well-defined.

**Problem 3 — free-particle acceleration.** A free particle's acceleration should be zero, computed through the normal Newton II pipeline. With ao₀, this works: the IFS contains {ao₀}, the sum is Σ{0} = 0, net-force = 0, and inertial-acceleration = 0/m = 0. The free-particle case runs through the full pipeline with no special handling. Zero acceleration is a *computed result*, not a default or an axiom.

### ao₀'s three roles

| Role | Mechanism |
|------|-----------|
| Iteration terminator | "No more forces" = give ao₀ to the current slot; trace completes normally |
| Empty-set preventer | Every IFS has ≥ 1 element; the sum is always well-defined |
| Free-particle grounding | a = 0 is computed via Newton II, not assumed |

All three roles fall out of a single structural move: one acting-object, zero canonical-force, universal activation-condition. ao₀ is not a hack or a special case — it is a legitimate acting-object that happens to contribute nothing. It can be invoked any number of times without affecting any result.

---

## 5. Summary of Design 3 Trace Flow

Starting from the goal `inertial-acceleration(p)`:

```
EVAL inertial-acceleration(p)                           [E21]
  │
  ├─ precondition: p is point-particle                  [E3, wall]
  ├─ precondition: frame is inertial-frame              [E18, wall]
  ├─ DEMAND inertial-mass(p)                            [E23, empirical]
  │
  └─ DEMAND net-force(p, t)                             [E24]
       │
       └─ DEMAND interacting-forces-set(p, t)           [E25, rewritten]
            │
            ├─ IFS wall 1: as many acting-forces as needed
            │
            ├─ ITERATION STEP 1:
            │   ├─ acting-object ao₁ enters             [E37, human modelling input]
            │   ├─ activation-condition check            [E35 → concrete entry]
            │   ├─ canonical-force evaluated             [E36 → concrete entry]
            │   ├─ acting-force f₁ enters               [E31]
            │   │   ├─ canonical side: f₁ = value       [dispatch resolves]
            │   │   └─ reaction side: −f₁ on q₁         [E32/E33, E38]
            │   └─ f₁ added to sum
            │
            ├─ ITERATION STEP 2:
            │   └─ (same structure, ao₂ → f₂)
            │
            ├─ ITERATION STEP k (termination):
            │   ├─ acting-object ao₀ enters             [human: "no more"]
            │   ├─ activation-condition: trivially YES
            │   ├─ canonical-force: zero vector
            │   ├─ acting-force f₀ = 0 enters
            │   └─ 0 added to sum (no effect)
            │
            └─ IFS wall 2: all interactions considered → list closed
       │
       └─ net-force = Σ{f₁, f₂, ..., 0} = Σ{f₁, f₂, ...}
  │
  └─ inertial-acceleration = net-force / inertial-mass
```

Every human input lands at a wall or scaffold entry. The triplet entries (E21, E24, E25) receive no direct human input — they provide computation rules that the trace executes mechanically. The iteration is self-contained within the entry structure, with ao₀ serving as the natural terminator.
