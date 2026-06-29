# Acting-object architecture — consolidation after the QPT session

This summarises where the architecture landed after going through QPT and compositional modeling carefully and pushing back on what does and doesn't transfer. Several positions in the earlier deep-dive doc (`qpt_envisioner_dispatch_deep_dive.md`) were corrected by working through specific cases. This document captures the corrected picture, not the survey.

## Scenarios are mechanical-compositions

There is no scenario-object layer in the VD. The scenario is not "a set of objects plus forces between them" — it is the list of acting-objects appearing in the mechanical-compositions of the particles, and nothing else. The "object" as a unifying entity is a residual-layer artifact, not an architectural primitive.

This sharpens what mechanical-composition is doing. It is not passive bookkeeping that lists which forces happen to act on a particle. It is the structural specification through which the scenario itself is declared. The trace's question "what acting-objects are in particle A's mechanical-composition?" is not a query against a prior object inventory — there is no prior object inventory. The mechanical-composition is the inventory.

This explains why mechanical-composition has to be law-rank rather than a property: it is the construct through which scenarios exist at all. The scenario does not exist independently of mechanical-composition; mechanical-composition is how it is declared.

The structure is mutually recursive at the scenario level. Particles are defined by their mechanical-compositions. Mechanical-compositions are populated by acting-object instances. Acting-object instances have participants slots filled by particles, which are themselves defined by their mechanical-compositions. No external grounding layer.

This is a stronger architectural commitment than QPT or CM make. Both presume a scenario-object layer because their process specifications have no structural counterpart to mechanical-composition. The VD does not need that layer because it has mechanical-composition.

## Producer vs constraint — uniform fragment shape

The earlier deep-dive proposed bifurcating acting-objects into producers (springs, gravity, friction) and constraints (normal forces, tension, rigid-body internals). This bifurcation is not needed.

The VD's trace halts at "the called idea is fully defined," not at "the numerical value is computed." If the question is what F_net is, the answer is the equation — even when the equation contains symbols whose values require further work to compute. Force attribution means producing the equation with each term tagged to its source acting-object. That is what the program completes, and nothing more.

This means producer and constraint acting-objects fit the same fragment shape. The difference is in the content of R, not its structure:

- A spring's R is `F = −k · x`, a closed-form expression in constructs and parameters.
- A contact's R is `F = C`, a fresh symbol indexed to this instance.

Both are valid canonical-force rules. The trace machinery handles them uniformly: fire the rule, attribute the contribution, add to the sum.

Lazy demand-driven evaluation handles the difference between producer and constraint cases natively. Producer acting-objects route demand inward — to the construct's definitional law (equilibrium-point) and the parameter's value (k). Constraint acting-objects route demand sideways — to the other body's F_net, because the construct's definitional law (no-penetration on the contact-surface) references the other body's motion.

For a constrained multi-body scenario, the program output is a coupled symbolic system rather than a single equation. For an Atwood machine: two F_net equations plus the inextensibility constraint, with the tension symbol T appearing on both. The trace produces all three; downstream solving produces numerical T and accelerations.

The QPT views/processes distinction would have been the answer if force attribution required producing numerical force values for everything. It does not. The lazy evaluator already covers what views/processes were for.

## Constructs and parameters defined from the canonical-force

An acting-object instance carries three kinds of binding:

- **Slots** — the abstract acting-object properties (activation-condition, canonical-force, paired-particle). Filled by dispatch through meta-typing.
- **Constructs** — spatial-valued properties of the acting-object whose meaning is locked by a definitional law tying them to a slot. Equilibrium-point for springs, contact-surface for normal forces, source-point for gravity.
- **Parameters** — atomic, scalar-valued. Spring constant k, friction coefficient μ, gravitational constant G.

What determines the constructs and parameters of an acting-object type is its canonical-force formula. The formula references certain quantities, and those references generate the requirements: each construct or parameter mentioned in the canonical-force must be available to the instance.

For a spring with `F = −k · x`:

- `k` is referenced as a scalar — therefore a parameter.
- `x` is referenced as displacement-from-equilibrium, which expands to a relation between endpoint and equilibrium-point — therefore endpoint and equilibrium-point are constructs.

The constructs are not geometric primitives. The equilibrium-point is not "the rest position in space" treated as an independent geometric fact. It is defined by a definitional law that says: equilibrium-point is the point at which, if the endpoint were there, the canonical-force would vanish. The construct gets its meaning from the force-zero state, not from any external geometric primitive.

This is why constructs earn law-rank treatment while parameters do not. A parameter is a value that could vary across instances without anything structural changing. A construct cannot — its meaning *is* the definitional lock to a slot's behavior, and that lock is law-rank.

Constructs are spatial-valued and transform with the acting-object's pose. As a spring moves and rotates, its equilibrium-point moves with it; the construct attaches to the spring's own frame, not to a global frame. This means trace-time queries about the construct have to resolve frames against the scenario frame. This already matters within Newtonian mechanics (a spring on a rotating turntable has an equilibrium-point that moves in the lab frame) and foreshapes what GR will eventually formalise.

Parameters have no transformation behavior. They are atomic scalars set per-instance.

## Minimal instantiation lets acting-objects superpose without interference

When an acting-object instance is created, it carries only the data its R component demands — nothing more. A spring acting-object instance carries equilibrium-point, k, endpoints, and slot bindings. That is all, because that is everything the spring's canonical-force rule references.

If the same physical entity is also charged, a separate electromagnetic acting-object instance is created. It carries charge, position, and slot bindings. Different data set. The two instances coexist on the same particle's mechanical-composition without sharing or duplicating anything.

This is why no scenario-object layer is needed. The duplication problem that motivates QPT's object-vs-process separation does not arise in the VD, because lazy instantiation prevents it from arising. Each acting-object instance is minimally instantiated against its own R; the data sets across acting-objects of different types do not overlap.

The consequence for superposition: acting-objects of different types can be placed together on the same particle's mechanical-composition without architectural friction. They contribute independently to the force sum, they reference disjoint construct and parameter data, and the lazy evaluator processes each one in turn without any of them needing to know about the others.

The conceptual notion of "the physical spring as a unified entity" does not need an architectural representation. It is the union of all acting-object instances that the human has declared as belonging to the same entity, plus their constructs and parameters. The unity lives in the human's mind and at the residual layer; the architecture does not model it.

## Slot-typing syntax and fixed arity

The narrowly borrowable piece from QPT for instantiation is the slot-typing pattern. QPT writes process Individuals fields like `(src an object, Has-Quantity(src, heat); dst an object, Has-Quantity(dst, heat))` — slot name, type predicate, relational constraints. This pattern transfers to acting-object Individuals fields: a spring's slots are two endpoints, each requiring a particle-typed value; a friction acting-object's slots are one particle and one surface; and so on.

Slot arity is fixed per acting-object type. A spring is always two-particle. Gravity is always two-particle. Friction is always one-particle-and-one-surface. There is no variable-arity acting-object in the current architecture. If one is ever needed, it is an architectural extension, not a parameterisation of existing types.

The instantiation check at declaration time is therefore a small, syntactic operation: when the human declares a new acting-object on a particle's mechanical-composition, the engine checks that the slot fillers are type-compatible with the acting-object's Individuals spec. There is no search, no enumeration, no hypothetical binding generation. QPT's full pattern-matching machinery is overkill for this.

One discipline the VD enforces that QPT does not: type predicates on slots are themselves headwords in the dictionary. When a spring's Individuals spec says the endpoints must be particles, "particle" is a headword with its own definition and law-house. The type-check at declaration is therefore a dictionary lookup — does the entity offered for this slot satisfy the definition of "particle"? — not an engine-level primitive. The instantiation machinery is itself defined within the dictionary, consistent with the wall principle and the rest of the architecture.

## What this leaves to do

These commitments are now explicit. The next concrete test is the spring rewrite — a quadruple-shaped entry-cluster with the participants slots, the equilibrium-point definitional law, and the canonical-force rule, deployed on a one-spring scenario where the trace constructs an instance, populates its constructs and parameters, fires its R, and contributes to the force sum on each endpoint particle. If the wall principle holds end-to-end and the audit tools still pass, the architecture survives its first stress test.

Two things to confirm in that test: that the construct's definitional law (equilibrium-point's no-force-state lock) sits cleanly in the spring's law-house, and that the trace correctly distinguishes the slot bindings (filled by dispatch) from the construct bindings (filled by the construct law) from the parameter bindings (atomic) — all three landing at walls, none at triplet entries.
