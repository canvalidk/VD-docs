# The Handle–Stimulant Spine

## Version 0.1

### Core thesis

A system does not begin with meanings, definitions, laws, or settled symbols. It begins with targets that can be affected.

A **stimulant** is what is put into, presented to, or impressed upon a target: an electrical signal, a light pattern, a sound, a tactile mark, a pressure event, a chemical trace, or any other causal presentation.

A **handle** is the repeatable form by which that stimulant is picked out, routed, called, or made usable inside a procedure: an opcode, glyph, word, symbol, address, gesture-form, diagrammatic mark, or other operational sign.

The handle is not identical with the stimulant. A stimulant affects the target. A handle gives the procedure something to grab.

Meaning, lawhood, proof-use, and admission arise when handles produce stable dossiers under disciplined probing, and when those dossiers match across targets within a declared budget.

In compressed form:

> A stimulant affects.  
> A handle routes.  
> A dossier records.  
> Discipline stabilizes.  
> A budget licenses.  
> Admission names.

---

## 1. The problem

Suppose two systems appear to use the same operation.

One human reads the glyph `×`. Another hears the word “times.” A computer executes a multiplication opcode. A machine receives a voltage pattern. A child sees grouped objects. A proof assistant applies a formal rule.

There is no single visible object shared by all of these cases. The light, sound, voltage, ink, instruction, and internal state-transition are different stimulants. Nor can we assume in advance that all of these systems possess the same meaning.

The question is therefore:

> How can different targets be treated as using the same thing when neither their stimulants nor their internal procedures are literally the same?

The answer requires an intermediate object.

That object is the **handle**.

A handle is not a metaphysical meaning. It is not merely a surface symbol. It is not the raw causal event that strikes the target. It is the operable form by which a target-relative procedure is entered, called, or routed.

The same handle may be realised by different stimulants. The same stimulant may fail to install the same handle in different targets. Different handles may converge on the same procedural role.

So the first rule is:

> Do not identify use by surface form alone. Identify use by disciplined handle-behaviour.

---

## 2. Stimulants

A **stimulant** is a concrete presentation to a target.

Examples:

- photons from a written glyph;
- an acoustic waveform;
- a voltage transition;
- a tactile raised mark;
- a chemical signal;
- a pattern of pixels;
- a muscular gesture seen by another agent;
- a sequence of bits entering a machine.

A stimulant is causal before it is semantic. It can affect a target even when it is not understood by that target.

This distinction matters because the same handle can be carried by many stimulants. The glyph `+` can be printed in ink, displayed on a screen, scratched into wood, spoken as “plus,” encoded as Unicode, or represented internally as a formal token. The physical presentations differ. What we care about is whether they route the relevant procedure in the target.

A stimulant is therefore not yet a meaning. It is the material occasion for possible handle-use.

---

## 3. Handles

A **handle** is a repeatable operational form that a procedure can grab.

Examples:

- a glyph such as `+`, `×`, or `=`;
- an opcode such as `ADD` or `MUL`;
- a word such as “and,” “times,” or “force”;
- a diagrammatic mark;
- a formal token in a proof system;
- a command name;
- a headword in a vocabulary;
- a gesture-form;
- a label used to call a subroutine;
- an address used to retrieve or route an operation.

A handle is not defined by its visible shape alone. It is defined by what happens when a disciplined target is probed through it.

Thus, two visually identical inscriptions may be different handles if they route different procedures. Conversely, two visually different forms may count as matching handles if their dossiers converge under the relevant probes.

A handle is therefore target-relative at first. The glyph `×` for one reader, the opcode `MUL` for a CPU, and the spoken word “times” for another reader are not literally the same local object. But they may become admissibly equivalent if their disciplined dossiers match within budget.

This gives the central claim:

> A handle is individuated by disciplined procedural role, not by surface appearance.

---

## 4. Probes

A **probe** is a controlled attempt to learn what a handle does in a target.

A probe presents stimulants under conditions and observes what the target does with the associated handle.

For example, if the candidate handle is multiplication, probes might include:

- simple cases: `3 × 4`, `2 × 5`;
- identity cases: `n × 1`;
- zero cases: `n × 0`;
- commutation checks: `a × b` versus `b × a`;
- distributive contexts: `a × (b + c)`;
- word-to-symbol translation;
- symbol-to-action translation;
- error correction and repair behaviour;
- use inside a larger proof or calculation.

The point of probing is not merely to see whether a target produces one correct answer. The point is to build a record of how the handle behaves across contexts.

A single response is not enough. A handle is known through a pattern.

---

## 5. Dossiers

A **dossier** is the accumulated record of a handle’s behaviour under probes.

It may include:

- ordinary responses;
- boundary responses;
- failures;
- repairs;
- translations into other handles;
- compositional behaviour;
- counterfactual stability;
- behaviour under distraction, noise, or altered presentation;
- behaviour across time;
- interaction with neighbouring handles.

The dossier is what replaces the fantasy that the handle’s meaning is visible on its face.

Instead of asking:

> What does this mark really mean by itself?

we ask:

> What dossier does this handle produce when a disciplined target is probed?

The dossier is not yet the definition. It is the evidence from which admissible definition becomes possible.

---

## 6. Discipline

A target is **disciplined** when its responses are stable enough for a dossier to converge.

Discipline may come from training, formal rules, machine architecture, biological regularity, social correction, proof norms, experimental controls, or repeated use.

Without discipline, the dossier remains noisy. A handle may appear to do one thing in one case and another thing in another case. In that condition, the system cannot safely admit a stable meaning, law, or operation.

Discipline is not perfection. A disciplined target can still err. What matters is that the errors have a shape: they can be detected, bounded, corrected, or explained.

This makes discipline a precondition for comparison.

> Undisciplined handles do not yet have stable dossiers. Stable dossiers are required before handle-matching can begin.

---

## 7. Budgets

A **budget** is the permitted tolerance for mismatch.

No real comparison is infinite. A human, a CPU, a proof assistant, and a child may converge on multiplication while differing in speed, notation, failure modes, representational limits, memory, overflow behaviour, or explanation style.

If exact identity is required at every level, almost nothing matches. If no constraint is required, everything matches too easily.

So admission requires a budget.

A budget says which differences matter for the present purpose.

Examples:

- For school arithmetic, slow calculation may be acceptable but systematic failure on zero is not.
- For machine arithmetic, fixed-width overflow may be acceptable only if explicitly modelled.
- For proof, empirical success may not be enough; rule-governed derivability matters.
- For translation, surface differences may be irrelevant while inferential role matters.

A budget is therefore not a weakness. It is the declared condition under which comparison becomes meaningful.

---

## 8. Handle-matching

Two handles match when their disciplined dossiers align within budget.

Let one target use handle `h₁` and another target use handle `h₂`.

We do not ask whether `h₁` and `h₂` look the same. We ask whether the dossiers produced by `h₁` and `h₂` under suitable probes converge closely enough for the intended use.

This relation is budget-relative:

> `h₁` and `h₂` match for purpose `P` under discipline `D` and budget `B`.

That qualification is essential. It prevents a false absolutism. Handles can match for one purpose and fail to match for another.

For example, a child’s multiplication handle may match an adult’s for small whole-number arithmetic, but not for algebraic manipulation. A CPU multiplication opcode may match mathematical multiplication over a bounded integer range, but diverge when overflow matters.

The match is real, but scoped.

---

## 9. Admission

**Admission** is the act of allowing a matched handle, object, rule, or law to enter the system as usable.

A handle is admitted when:

1. it has a dossier;
2. the dossier is stable under discipline;
3. the dossier matches relevant other dossiers within budget;
4. the remaining failures are either outside scope or explicitly recorded;
5. the system can now use the handle predictively, inferentially, or normatively.

Admission does not mean metaphysical certainty. It means the system has enough disciplined convergence to proceed.

Once admitted, a handle can receive a name, a definition, a law-entry, or a place in a catalogue.

This reverses the usual picture.

Definitions do not come first. Admission comes first. Definitions are compact public records of admitted handle-use.

---

## 10. Definitions downstream of handles

A definition is often treated as if it installs meaning from above.

In this spine, a definition is downstream. It records, compresses, or orients an already disciplined handle-dossier.

This is why definitions can fail even when their words are formally correct. A definition may not load the right handle in the target. It may not generate the intended dossier. It may describe a structure without installing usable behaviour.

So a definition has two jobs:

1. **audit job**: state the formal conditions of admission;
2. **loading job**: cause the target to route the right handle.

A definition that satisfies the audit job but fails the loading job may be technically correct but practically inert.

A definition that satisfies the loading job but fails the audit job may be useful but unsafe.

A good definition does both.

---

## 11. Raw meaning

Raw meaning is not an occult object behind the handle.

Raw meaning is the convergent content of a disciplined dossier before it has been fully compressed into a formal definition.

It is what the target has learned to do with the handle.

For example, the raw meaning of a multiplication handle is not merely the word “multiplication” and not merely one equation. It includes the pattern of use: grouping, repeated addition where appropriate, scaling, area, arrays, algebraic interaction, identity, zero, distributivity, and correction of common misuses.

Formal definition can later isolate one structure. But the living handle often carries more operational orientation than the final definition states.

This explains why informal wording, examples, and “poetic” phrases can matter. They may help install the right handle before the audit definition is fully available.

---

## 12. Laws as higher-order admitted handles

A law is not merely a sentence that happens to be true. A law is a higher-order handle admitted into a system because it stabilizes a pattern of lower-order handles.

For example, a law may connect handles for force, mass, and acceleration. It does not merely mention these terms. It disciplines their joint use. It tells the target how changes in one handle should constrain the others.

A law therefore has its own dossier:

- where it works;
- where it fails;
- what it predicts;
- what it licenses;
- what it forbids;
- what neighbouring handles it coordinates;
- what residual cases remain outside it.

A law is admitted when this higher-order dossier is stable enough under the system’s budget.

Thus, the same machinery applies at multiple levels:

- handles for terms;
- handles for operations;
- handles for definitions;
- handles for laws;
- handles for entire modelling regimes.

---

## 13. Catalogue and remainder

Any catalogue admits some handles and leaves others outside.

The outside is not necessarily empty. It is the system’s **remainder**: what has not yet been admitted, distinguished, disciplined, or made usable.

The remainder is not automatically meaningless. It is simply not yet available as an admitted handle inside the catalogue.

When a new handle is admitted, the catalogue changes and the remainder changes with it.

Admission therefore has a before-and-after structure:

> remainder-before → admitted handle → remainder-after

This is why admission is not just adding an item to a list. It reorganizes the boundary between what the system can use and what it cannot yet use.

---

## 14. Failure modes

The handle-stimulant distinction prevents several failures.

### 14.1 Stimulant-collapse

This occurs when the physical presentation is mistaken for the handle.

Example: assuming that because two targets receive the same glyph, they must be using the same handle.

But one target may read `×` as multiplication, another as a letter, another as decoration, another as an error, and another not at all.

### 14.2 Surface-handle collapse

This occurs when two handles are treated as the same because they look or sound alike.

Example: the same word may route different procedures in different disciplines.

### 14.3 Hidden convergence failure

This occurs when different-looking handles are rejected too quickly, even though their dossiers converge.

Example: an opcode, a spoken word, and a written glyph may all route the same operation within the relevant budget.

### 14.4 Undisciplined dossier failure

This occurs when a handle is admitted before the target’s responses have stabilized.

Example: a learner sometimes treats multiplication as repeated addition, sometimes as concatenation, sometimes as exponentiation, and sometimes as arbitrary symbol-pushing.

### 14.5 Budget failure

This occurs when the tolerance for mismatch is left implicit.

Example: CPU integer multiplication may be accepted as mathematical multiplication until overflow matters. The failure was not in the handle alone, but in the unstated budget.

### 14.6 Reference-monopoly failure

This occurs when one interpreter is treated as the absolute source of meaning rather than as one disciplined target among others.

The better method is not to enthrone one interpreter, but to compare dossiers under explicit discipline and budget.

---

## 15. The multiplication example

Consider four cases:

1. A human sees `3 × 4`.
2. Another human hears “three times four.”
3. A CPU executes a multiplication opcode.
4. A child arranges three groups of four objects.

The stimulants differ:

- light from glyphs;
- sound waves;
- voltage patterns;
- visible objects and gestures.

The handles differ:

- the glyph `×`;
- the word “times”;
- the opcode `MUL`;
- the grouping action.

The targets differ:

- trained reader;
- listener;
- machine;
- child.

Yet we may admit these as converging on multiplication if their dossiers match within the relevant budget.

We test not merely whether each target says “12.” We test whether the handle behaves correctly across a family of probes: identity, zero, grouping, scaling, distributivity, error correction, and interaction with neighbouring operations.

Only after that convergence do we safely say:

> These different handles are admissible variants of the same operation for this purpose.

The word “multiplication” then names the admitted convergence. It does not magically precede the convergence.

---

## 16. The general route

The spine can now be stated as a route:

1. A target is exposed to stimulants.
2. Some stimulant-patterns become usable through handles.
3. Handles are probed.
4. Probes generate dossiers.
5. Discipline stabilizes dossiers.
6. Dossiers are compared across targets.
7. A budget determines acceptable mismatch.
8. Matching handles are admitted.
9. Admitted handles receive names, definitions, laws, or catalogue positions.
10. Each admission changes the remainder of what is not yet admitted.

This route applies to symbols, operations, definitions, laws, models, and theoretical objects.

---

## 17. Final formulation

A handle is the procedural grip by which a target makes a stimulant usable.

A handle is not self-interpreting. It earns its identity through disciplined dossier-behaviour.

A definition is not the origin of meaning. It is the compressed public form of an admitted handle-dossier.

A law is not merely a sentence. It is a higher-order handle that disciplines relations among lower-order handles.

A catalogue is not a mirror of reality. It is the current set of admitted handles, with a remainder left outside.

The foundational question is therefore not:

> What does this symbol mean in itself?

but:

> What stimulant installs this handle, what dossier does the handle produce under discipline, what budget licenses its match with other handles, and what admission follows?

