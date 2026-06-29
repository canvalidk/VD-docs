# QPT Envisioner — what it is and the dispatch connection

## What it is

The envisioner is the reasoning engine at the heart of QPT. Given:

- a **scenario** (concrete objects and their initial state), and
- a **library of process specifications** (typed templates),

it produces which processes are currently active and the resulting qualitative behaviour (what quantities change, in which directions).

Processes in QPT are declared with:

- **participants**: parameter slots for objects
- **preconditions**: non-physical enabling (e.g. "valve is open")
- **quantity conditions**: predicates on continuous quantities (e.g. `T(src) > T(dst)`)
- **influences**: what the process does when active — direct (I+/I−, additive contributions to a derivative) or indirect (qualitative proportionalities through mediating quantities)

Canonical example — heat-flow:

```
process heat-flow(src, dst)
  preconditions:      heat-path(src, dst)
  quantity conditions: T(src) > T(dst)
  influences:         I+(heat(dst), flow-rate)
                      I−(heat(src), flow-rate)
```

## How dispatch actually happens

The envisioner handles the abstract-to-concrete transition in three steps:

**1. Instance generation.** Given the scenario's objects and the library's process templates, the envisioner binds parameters to objects to produce *process instances*. If `heat-flow(src, dst)` is in the library and the scenario has objects `cup` and `room`, candidate instances include `heat-flow(cup, room)` and `heat-flow(room, cup)`.

**2. Activation check.** Each candidate instance's preconditions and quantity conditions are evaluated against the scenario state. Instances whose conditions hold are marked *active*; the rest sit dormant.

**3. Influence composition.** Active instances' direct influences are summed per-quantity to produce net rates of change. Qualitative proportionalities propagate changes through mediating quantities.

The dispatch — going from "abstract typed process" to "concrete contribution" — happens at step 1. The library carries the types; the scenario carries the objects; binding produces the callable. Step 2 is what the VD calls activation-condition evaluation. Step 3 is the force/influence sum.

## Map to the VD's dispatch problem

Your problem: when an acting-object enters the trace as an abstract callable, how does it resolve to a concrete type-specific implementation?

The QPT-shaped answer:

- Maintain a **typed acting-object library** separate from the append-only dictionary. Each entry specifies participants, an activation-condition, and a force-production rule (or resolves to `ao₀` if inactive).
- At trace time, the scenario (a textbook problem, say) provides concrete objects; the library provides typed templates. **Binding is the dispatch step** — each template + object combination produces a candidate acting-object instance.
- Candidate instances carry their activation-condition from the library. The trace evaluates the condition; if it holds, the instance is active and produces its force via the library's rule.
- Instances whose activation fails reduce to `ao₀` and contribute nothing to the force sum.

So: the dispatch table is the library, the dispatch operation is parameter binding, and the activation check is the filter between "this type could apply" and "this type does apply."

## What translates, what doesn't

**Translates well:**

- Template-with-slots as the dispatch primitive
- Binding as the instantiation operation
- Activation condition as the gatekeeper between candidate and active
- Summation of contributions over active instances

**Doesn't translate:**

- QPT has no wall principle. In QPT, activation conditions and influences sit at the same representational level. The VD's insistence that activation-conditions live at wall entries, and that force-production rules live elsewhere, is VD-specific discipline you'd need to layer on top of anything borrowed from QPT.
- QPT's envisioner is typically total — enumerate all active processes and their behaviour. Your trace is lazy, goal-driven. You'd want per-instance evaluation demanded by the goal expression, not wholesale envisioning.
- QPT has no chimney/triplet/wall structure. The law-as-house architecture doesn't exist in QPT; processes are flat.
- QPT doesn't formalise the residual/poetic layer. The library is treated as authoritative, not as a compiled human judgment.

## What to read

For the envisioner specifically:

- **Forbus (1984), *Qualitative Process Theory*, *Artificial Intelligence* 24(1–3), 85–168.** Envisioner specified in the later sections.
- **Forbus & de Kleer (1993), *Building Problem Solvers*.** Implementation-level treatment — the chapters on envisioning and ATMS.

For the library-assembly question (closer to your wall-principle concerns):

- **Falkenhainer & Forbus (1991), *Compositional Modeling: Finding the Right Model for the Job*, *AI* 51(1–3), 95–143.** How process libraries get assembled and selected in practice. Probably the more useful paper for your dispatch work specifically.
