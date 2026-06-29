# Unfolding Forces In: How the VD Trace Should Handle Acting Objects

## The problem with the current trace

In the current VD trace (v3), there's a moment that looks clean but is actually a cheat. When the evaluator needs the interacting-forces-set for a particle — the list of all forces acting on it — the trace does this:

```
POPULATE  interacting-forces-set(m₁, t)
  → human:    What acting-forces act on m₁?
  response := { F_gravity_1, F_tension_1 }
```

The human hands over the complete set in one go. Two forces, fully named, dropped into the trace as a finished package. After that, the trace does excellent work — it walks each force through the acting-object architecture (E34–E37), checks activation conditions, extracts canonical forces and paired particles. But the *reason those forces were in the set in the first place* is never traced. The insertion and the justification are disconnected moments.

This matters. The VD exists to make definitional commitments explicit and traceable. If the single most important modelling decision in a mechanics problem — *what forces act on this particle?* — enters the trace as an unstructured human declaration, the formalism is looking away at exactly the moment it should be paying the most attention.

## An analogy from functional programming

In a functional programming language like Haskell, there's a useful distinction between two ways of producing a list.

The first is to declare it outright: `forces = [gravity, tension]`. This is what the current trace does. The list appears, fully formed, because someone said so.

The second is to *derive* it from a rule. You define a condition, run it against a pool of candidates, and the list assembles itself from whatever passes:

```haskell
forces = [ canonicalForce a | a <- candidateActingObjects
                             , activationConditionMet a particle ]
```

This is a *set comprehension*. The list isn't declared — it's the output of a filtering process. Each element is in the list *because* it satisfied the condition. There's no way for an element to be present without the condition having been met, and no way for the condition to be met without the element appearing. The two facts are the same fact.

In Haskell's lazy evaluation model, this list doesn't even get computed all at once. It *unfolds* — each element is produced on demand, one at a time, only when something downstream needs it. The list at any given moment is partly realised (the elements computed so far) and partly a suspended computation (the remaining candidates that haven't been checked yet). The process of building the list *is* the process of checking conditions. They aren't separate steps.

## What the VD trace should do instead

The insight is that the interacting-forces-set shouldn't be a container that the human fills. It should be *defined* in a way that makes the activation condition structurally inseparable from membership.

Not: "here are the forces, and by the way, their conditions are met." Rather: the force being in the set and the condition being met are the same statement. You can't assert one without the other. Having one without the other isn't wrong — it's *incoherent*, a violation of what those words mean.

This is already how the paired-particle works in the current VD. If you trace any acting-force back through the definitions, you inevitably hit its paired particle — the particle that receives the reaction force. The paired particle isn't a separate piece of information that gets attached to the force after the fact. It's a definitional component of the acting-object. Saying "this force exists but has no paired particle" isn't a claim that might be false. It's a sentence that fails to mean anything, given how "acting-force" is defined.

The activation condition should sit in exactly the same structural position.

## The shape of the entailment

When the trace walks through any acting-force, the definition chain currently goes:

```
"F_spring acts on m₁"
  └─ F_spring is the canonical-force of acting-object A          [E36]
       └─ acting-object A is: spring-contact-m₁                  [E34]
            └─ A has a paired-particle: the anchor point          [E37]
```

The paired particle shows up as a demanded dependency of the acting-object definition. You can't fully evaluate the force without encountering it. It's not checked — it's *exhibited*. The trace reveals it as something that was always there, entailed by the definitions.

The activation condition should work the same way:

```
"F_spring acts on m₁"
  └─ F_spring is the canonical-force of acting-object A          [E36]
       └─ acting-object A is: spring-contact-m₁                  [E34]
            ├─ A has a paired-particle: the anchor point          [E37]
            └─ A has an activation-condition:                     [E35]
                 "m₁ is attached to the spring and displaced
                  from equilibrium"
                 └─ m₁ satisfies this                (entailed)
```

The condition being satisfied isn't a gate that the force passes through on its way into the set. It's a *consequence* of the force being in the set. If you trace the definitions, you find it. It was always already there. The trace just makes it visible.

## What "entailed" means here

This is a specific and important sense of entailment. It's not that Newtonian mechanics tells you the condition must be met. It's that the *definitions you chose to use* tell you that.

If someone says "the spring canonical force acts on m₁, but m₁ isn't attached to the spring," they haven't made a physical error. They've made a *linguistic* one — a contradiction in terms, like saying "this bachelor is married." The VD defines the acting-force-from-a-spring as the thing that exists when the spring activation condition is met. If you use those words as the dictionary defines them, and then deny the condition, you haven't disagreed with Newton. You've disagreed with yourself.

This is important because it locates the authority correctly. The entailment doesn't come from nature or from physics. It comes from the dictionary. It holds for anyone who gives the dictionary authority over what those words mean — anyone who uses "acting-force" and "activation-condition" as the VD defines them. If you define those terms differently, you aren't bound by the entailment. But then you're speaking a different language, and the trace won't apply to you.

The VD doesn't tell you what's true about the world. It tells you what you've committed to by using these words in these ways.

## The computational honesty point

There's a second, more practical reason this matters. Even when the human *thinks* they're declaring the interacting-forces-set as a package — "gravity and tension act on m₁" — they're actually making two separate judgements. They're recognising that the gravitational activation condition is met (m₁ has mass, is in Earth's field) and separately recognising that the string-contact activation condition is met (m₁ is attached to the string). These are different checks with different content.

The current trace compresses this into a single declaration. This is an instance of what the VD framework calls "lossy readout" — the human's verbal shorthand serialises a structured, multi-step process into a flat statement, and information is lost in the compression. You can't tell, from the declaration alone, *why* those two forces and not others. The reasons are in the physicist's head, not in the trace.

The unfold — or the set comprehension, however you want to frame it — decompresses this. Each force enters the set through its own activation gate, and the trace records each gate separately. The individual judgements become visible, attributable, and auditable.

## What this means for design 3

The change is narrow in scope but deep in consequence. The interacting-forces-set entry (E25) needs to be redefined so that membership *is* activation-condition satisfaction, not a separate fact about it. The trace doesn't need a new procedure for "checking conditions before inserting forces." It needs the definitions chained so that tracing any force back through the entries *necessarily* passes through its activation condition.

The force doesn't enter the set and then you discover the condition was met. The force being in the set and the condition being met are revealed, by the trace, to be the same definitional commitment — a tautology made visible.
