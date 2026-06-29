# The envisioner — going deeper, with the dispatch problem in the crosshairs

Yesterday's brief was a sketch. This is the read of the primary sources: Forbus's 1984 *Qualitative Process Theory* paper, and Falkenhainer & Forbus's 1991 *Compositional Modeling* paper, which generalises QPT in ways that turn out to be more directly useful for the VD's dispatch problem than the original envisioner.

## Diagnosis: what the VD's dispatch problem actually is

Restating it cleanly. The VD has:

- A static type infrastructure: abstract acting-object headwords (E34–E36), concrete acting-object types (spring, gravity, friction), and a meta-typing law that connects them.
- A force-sum chain (E24–E26) that integrates contributions.
- An open question of how, at trace time, a particular acting-object slot resolves to a concrete force value.

Yesterday's session converged on a partial answer at the dictionary level: the entry defining each concrete type (e.g. spring) must contain the abstract slot headwords paired with the concrete slot headwords, so that the tokeniser already creates the dependency edges at classification time. Good as far as it goes.

What that answer doesn't address:

1. **The runtime object.** Given a scenario with a spring connecting particles A and B, what *is* the thing the trace is reasoning about? Is it the headword `spring`? An instance? A binding?
2. **Candidate generation.** When the trace is at the force-sum step for particle A, how does it know there's a spring acting-object to consider in the first place?
3. **The activation phase, decoupled from dispatch.** "Is this acting-object currently producing force?" is a different question from "is this acting-object in the model at all?" — and the current architecture conflates them.

These are exactly the three things QPT and compositional modeling have crisp machinery for. The breakthrough framing isn't "QPT solves dispatch"; it's that **dispatch is a phase with internal structure, and the missing primitive is the runtime instance**.

## The PI as a first-class object

Forbus 1984 introduces a distinction that the VD currently lacks. For every collection of scenario objects that satisfies the `Individuals` field of a process specification, there is a **process instance (PI)**. The PI is a first-class object. It carries:

- A reference to its template (which process specification it instantiates).
- Bindings of template parameters to specific scenario objects.
- A `Status` field, taking values `Active` or `Inactive`, determined exactly by the conjunction of preconditions and quantity conditions.

The same machinery applies to **view instances (VIs)** for the parallel notion of individual views (Forbus's stative configurations — more on these below).

This is the missing primitive in the VD. Right now, the trace can talk about the headword `spring` and the entries that define it, but it has no way of referring to "this particular spring instance, between particles A and B, in the current scenario, currently active." Once you add that primitive, dispatch dissolves into three well-defined sub-problems:

1. **Candidate generation.** For each acting-object library entry, and each scenario-object tuple compatible with its `Individuals` condition, generate a candidate instance.
2. **Activation.** Evaluate the candidate's operating conditions against scenario state. Active candidates remain; inactive ones reduce to `ao₀` (which we already have for free-particle grounding — its role here is exactly the "no contribution" terminator).
3. **Composition.** Active instances contribute their canonical-force as a direct influence on the per-particle force sum.

The two-tier picture: the **library** holds typed templates (the dictionary); the **trace** holds instances (the runtime). This is what's structurally absent.

## The model-fragment quadruple — and how it lands on VD walls

Falkenhainer & Forbus 1991 generalises Forbus's process specification into a **model fragment**: a quadruple `(I, A, O, R)`, with the logical reading

```
I ∧ A ∧ O → R
```

where:

- **I = Individuals.** The structural configuration of objects to which the model applies. (E.g., "two containers connected by a pipe.")
- **A = Assumptions.** Modeling commitments — abstractions, approximations, perspective, granularity. ("Frictionless flow." "Rigid body." "Point particle.")
- **O = Operating conditions.** The behavioural scope. Inequalities on quantity values; conditions on the activity of other fragments.
- **R = Relations.** The constraints imposed when the fragment fires — qualitative proportionalities, direct influences, equations.

This is the cleanest available structure for VD acting-object entries, and it lands surprisingly well on the wall principle.

For a spring acting-object, the quadruple would be:

- **I** — two particles (the participants).
- **A** — modeling assumptions: ideal Hooke's law, no internal damping, point-attachment.
- **O** — operating conditions: extension `≠ 0` (or whatever determines that the spring is currently producing force).
- **R** — `canonical-force = −k · extension`.

Now the wall mapping. The VD's discipline is "human inputs land at walls." Look at where each quadruple component sits:

- **I** is human input — the scenario specifies which particles. Lands at the participants wall (currently we have this implicitly through the action-reaction `paired-particle` slot, but it's not cleanly factored as "what are the participants of this acting-object?").
- **A** is human input — the modeller decides whether to treat the body as rigid or elastic, whether to invoke ideal Hooke's law. Lands at modeling-assumption walls. **These walls are currently missing or implicit.** This is the first concrete architectural prediction this analysis makes for the VD.
- **O** is also human input at the entry level (the human authors the activation-condition formula), but the trace evaluates it. Lands at the activation-condition wall — the wall we already have, just renamed and with a sharper distinction from A.
- **R** is the canonical-force rule — also human-authored, evaluated at trace time. Lands at the canonical-force wall — also already present, structurally.

The thing to stare at: the VD currently has a single "activation-condition" wall that's doing double duty. It's holding both the modeling assumption ("this is a spring at all, in this model") and the operating condition ("this spring is currently extended"). The QPT/compositional-modeling distinction says these are different *kinds* of walls.

This matters because the trace treats them differently. Modeling assumptions (A) are checked once at instantiation: if the assumption fails, the candidate is never generated. Operating conditions (O) are checked at each activation step: a spring is in the model throughout, but its instantaneous force can be zero. Conflating them confuses what the trace evaluates and when.

## The simplifying-assumption / operating-condition split, in detail

Falkenhainer & Forbus subdivide simplifying assumptions (`A`) into three categories. Each has a likely VD counterpart:

- **Ontology assumptions** — the choice of representational primitives (Lagrangian vs. Eulerian, particle vs. control volume). For the VD: "point particle ontology", "Newtonian (not relativistic) frame", "instantaneous action-at-a-distance allowed". These are *global* — they apply to the whole scenario, not to specific objects. The VD has these implicitly. Making them explicit would surface ontological choices currently hidden.
- **Grain assumptions** — which objects are considered. ("Consider the spring", "consider the pulley", "treat the string-pulley assembly as a single black box".) For the VD: when you treat a string-pulley system as one acting-object rather than separately modelling string and pulley, that's a grain assumption.
- **Approximations and abstractions** — frictionless, incompressible, inelastic, ideal. The VD's parallels are obvious: "massless string", "frictionless pulley", "ideal spring".

Operating conditions (`O`), separately, fall into:

- Local restrictions on quantity values (inequalities).
- Operating modes (named collections of restrictions — like "transistor in saturation mode").
- Steady-state assumptions and other behavioural scoping.

The VD's activation-conditions live almost entirely in this second category. Force activation conditions are `O`, not `A`.

A useful test for the VD: take any current entry's "activation-condition" and ask — does this restrict *when* the model fires (O), or does it restrict *whether the model is appropriate at all* (A)? For most acting-objects, current entries conflate these.

## Direct vs. indirect influences — a logical discipline worth importing

Forbus 1984 specifies that influences come in two kinds:

- **Direct** — `I+(Q, n)` and `I−(Q, n)`. Processes are the only source of direct influences. If a quantity is directly influenced, its derivative equals the sum of all direct influences on it.
- **Indirect** — qualitative proportionalities `Q1 ∝Q+ Q2`, propagating change through mediating quantities.

And the discipline:

> Importantly, we assume that no quantity is both directly and indirectly influenced at once. A domain physics that allows a quantity to be both directly and indirectly influenced at the same time is considered to be inconsistent.

This is a logical lock. Apply it to the VD's Newton II house.

In Newton II, `acceleration = (sum of forces) / mass`. Acceleration is computed as a function of force and mass. In QPT vocabulary: `acceleration ∝Q+ force` and `acceleration ∝Q− mass`. So acceleration is *indirectly influenced* by force-and-mass.

Now, can anything else *directly influence* acceleration? In the current VD, no — Newton II is the only path. Good. The discipline holds, and the architecture is consistent on this point.

But the discipline also tells you: if you ever wrote a constraint that *directly* set the acceleration (e.g. "the bead's acceleration is zero on this constraint surface"), you'd have a contradiction with Newton II's indirect specification. The resolution must be that constraint forces emerge from the constraint and feed back through the force sum — they don't directly set acceleration. This is exactly what real Lagrangian mechanics does. The VD doesn't currently have constraints, but when it does, the discipline tells you how to write them: as direct influences on the force sum, never as direct setters of acceleration.

This is the kind of formal commitment the VD has been missing — a logical reason for one architectural choice over another, not a stylistic preference.

## Views vs. Processes — the next architectural extension

QPT distinguishes two kinds of model fragments:

- **Processes** are active. They directly influence quantities. Heat-flow, fluid-flow, boiling.
- **Individual views (VIs)** are stative. They license inferences (the existence of a piece-of-stuff in a container; the configuration of a mechanism) without producing direct change.

In the VD, every acting-object is currently process-shaped: it has an activation-condition and a canonical-force rule. But several of the things we've been struggling to fit cleanly into this shape are stative:

- **Normal force.** A surface in contact with a particle doesn't have a closed-form force rule. The force value is whatever is needed to enforce the no-penetration constraint.
- **Tension in an inextensible string.** Same structure: force is whatever satisfies the constraint that the string length doesn't change.
- **Rigid-body internal forces.** Whatever holds two parts of a rigid body together.

These are constraint-licensers, not force-producers. They behave like QPT views, not QPT processes. The VD's "string-pulley assembly as one acting-object" awkwardness, noted in the Atwood trace, is a symptom of trying to make a constraint-licenser fit a process shape.

A proposed two-tier acting-object architecture:

- **Producer acting-objects** — springs, gravity, friction, applied forces. Have closed-form force rules. Quadruple-shaped.
- **Constraint acting-objects** — normal forces, tension, rigid-body internals. Force value emerges from solving the constraint. Different quadruple structure: `R` is a constraint equation, not a force rule, and the force value is a Lagrange-multiplier-like quantity computed at trace time.

This is a real architectural extension, not a notational one. It's also the kind of thing where stress-testing on the Atwood machine and inclined-plane problems would surface the structural difference clearly.

## What still doesn't translate (kept short, yesterday's brief covered this)

- QPT has no chimney/triplet/wall structure. The law-as-house architecture is pure VD.
- QPT's envisioner is total (enumerate all active processes). The VD's trace is lazy. The instance-level primitive (PI) translates fine, but candidate generation in the VD is demand-driven by the goal expression, not exhaustive.
- QPT doesn't formalise the residual/poetic layer. The library is treated as authoritative.
- Compositional modeling treats model fragments as facts to be combined. The VD treats entries as definitions to be tokenised and reasoned about as a graph. The two-tier picture (library + instances) coexists with the dictionary-graph picture; instances live alongside, not inside, the dictionary.

## Concrete proposals to test

Four things, in roughly increasing radicalness:

**1. Add an `ActingObjectInstance` primitive to the engine.** A triple `(template_ref, bindings, status)`. Have the trace machinery construct one explicitly when traversing the force-sum step. Verify the wall principle is preserved — the human inputs at instantiation are scenario-bindings (which lands at the participants wall) and assumption-checks (at modeling-assumption walls); the activation evaluation is mechanical.

**2. Rewrite one concrete acting-object — spring is the cleanest test case — as a quadruple-shaped entry-cluster.** Specifically:
- A "participants" wall entry: which particles is this spring attached to?
- A "modeling-assumption" wall entry (new): assumption `ideal-Hooke`.
- An "activation-condition_spring" wall entry: extension is defined and nonzero.
- A "canonical-force_spring" wall entry: F = −k · extension.

Then check whether the audit tools still pass, whether the trace can run on a one-spring scenario, and whether the wall principle is preserved end to end.

**3. Apply Forbus's no-double-influence discipline to the existing Newton II house and to any new constraint laws.** Specifically: write down which quantities are directly influenced (by which acting-objects), which are indirectly influenced (by which qualitative proportionalities), and check no quantity appears in both lists. This is a formal audit, not a refactor.

**4. Sketch a constraint acting-object class — start with normal force on a flat surface — and see whether the producer/constraint two-tier extension is forced by the scenario, or whether producer acting-objects can absorb constraints with enough cleverness.** Prediction (weak): the two-tier split is forced; constraints don't reduce to producers without representational distortion.

---

The dispatch problem looked like a single architectural gap. Reading the primary sources, it's three sub-problems with a missing primitive (the instance) and a missing structural distinction (modeling assumption vs. operating condition). Both have crisp, forty-year-old answers in QPT and compositional modeling — and the answers respect the VD's wall principle better than the existing single-wall approach to activation.

The proposal to test next, if we're pursuing this, is the spring-as-quadruple rewrite. That's a one-acting-object change with predictable, auditable consequences, and it'll either confirm the structural import is clean or surface exactly where it isn't.

## Reading list (refined)

Forbus 1984 — *Qualitative Process Theory* — Sections 2.5, 3.1, 3.2 on individual views, process specifications, and influences. Skip the boiling and oscillator examples.

Falkenhainer & Forbus 1991 — *Compositional Modeling* — Sections 2.1, 2.3.1, 2.3.2 on model fragments, simplifying assumptions, operating assumptions. The thermodynamics example in §4 is illustrative but not load-bearing.

Bobrow et al. 1996 — *A Compositional Modeling Language* — only if you want to see the syntactic synthesis the QR community settled on. Useful as a reference language for the VD's library specification, not load-bearing for the dispatch question.
