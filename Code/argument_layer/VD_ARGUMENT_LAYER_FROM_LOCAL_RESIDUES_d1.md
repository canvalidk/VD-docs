# The Argument Layer

## Why Positional Locality Forces Arity Into the Interpreter

**Status:** working note, d1. Claude-authored at user request, 2026-08-17.
**Parents:**

- `VD_NO_LOOKUP_RULE_RESIDUAL_LAYER_CLOSURE_d2.md` (positional locality; pull vs. push)
- `Newton-analysis/participant_symmetric_forces/VD_PARTICIPANT_SYMMETRIC_CANONICAL_ORIENTATION_MESHING_d2.md` (the `V(f)` case)
- `specs/2026-06-10-vd-reduction.md`, `specs/2026-06-10-vd-residual-cleanup.md`

**Claim.** Positional locality is not a hygiene rule. It is a constraint on
what the interpreter must compute. Given it, argument delivery cannot be left
to notation, convention, or the reader — it must be a mechanical-layer
operation. This note derives that, specifies the layer, and records the
λ-calculus identification that fixes its shape.

**Priority note.** Local determination outranks minimality of the VD's
primitives. Where this note adds machinery, the justification is always that
locality fails without it — not that the addition is elegant.

---

## Part I — The derivation

## 1. The premise

From the parent note:

> A residue is a handle for its own raw_meaning. Therefore
> $\text{raw\_meaning}(R)$ is a function of $R$ alone. A reader executing $R$
> may use the local text of $R$ and their own external competence, and nothing
> at any other position — not in the log, not earlier in the same trace.

The criterion is behavioural dependence on non-local text, not access to it.
A reader with lookup enabled who reads nothing corrupts no residue.

## 2. The case that forces the issue

`impressed-force` — `V(f)` in the meshing note — is the first VD headword whose
*unfolding depends on an argument's value*. Which operation the reader performs
(quoted or negated, which instance, which target) is not determined by the
headword.

Earlier object-dependences were safe in two ways, neither available here:

| Form | Why δ succeeded blind |
|---|---|
| `net-force(t)` | parameter treated as decoration; never consulted |
| `inertial-acceleration_point-particle` | argument monomorphised into the name |

Member and kind monomorphise (`action-force_gravity`). **Instance cannot** —
instances are generated at trace time, and per meshing §13 instance identity is
exactly what distinguishes two equal-valued gravity members on one target.

So a datum must reach the unfolding site. The question is by what route.

## 3. Elimination

| Route | Direction | Status |
|---|---|---|
| Consult the log | pull | forbidden — retroactive revision, licensing collapse |
| Recall an earlier trace position | pull | forbidden — same violation, no symptom |
| Read the resolution one position up | pull, bounded | forbidden — bounded memory is memory |
| Re-supply at a second wall | — | rejected — duplicate input, unauditable agreement |
| Monomorphise into the headword | push, authoring-time | admissible; cannot hold instances |
| **Deliver as an argument** | **push, trace-time** | **admissible** |

Pull has the reader reach outward, so the site does not determine execution.
Push places the datum **at** the site before execution.

**The delivered argument becomes part of the handle.** The residual is not
`V(f)` with a dangling `f`; the handle is `V` *at* the delivered value, present
in the local text. Nothing is remembered because nothing is absent. Argument
delivery does not relocate the violation — it is the only route that restores
locality.

## 4. Why the reader cannot be trusted with it

Delivery could in principle be a convention: authors write arguments into
entries by hand, readers thread them through by attention.

That fails for the reason §3 forbids memory. If the reader supplies the
argument at the unfolding site from their recollection of the trace, execution
depends on a position other than the site — no matter that the datum is
correct. The datum must be **in the text**, and only the interpreter can put it
there, because only the interpreter knows the position.

Hence: mechanical layer.

## 5. What the interpreter must therefore compute

1. **Declaration.** Which parameters a headword takes, and their domains.
2. **Delivery.** Given a value at a call site, produce the instantiated
   residual with every occurrence of the slot filled.
3. **Propagation.** Slot occurrences inside the body are the delivery sites for
   the children. The datum threads down by being written, position by position.
4. **Gating.** Reduction is unavailable while parameters remain unbound.
5. **Recording.** Delivery is a trace event with provenance, like `expand`.

Items 2–3 are the layer proper. The rest is bookkeeping around it.

---

## Part II — Shape

## 6. Arity is declared by the domain headword

The notation carries the declaration:

```
net-force(point-particle) := ...
inertial-acceleration(point-particle) := ...
impressed-force(interaction-instance, point-particle) := ...
```

The slot name **is** the domain headword. Three consequences:

- No new declaration syntax. The parameter list is written where a reader
  already expects it.
- Admission is type-checked by machinery already authored: `p1` may be
  delivered to `(point-particle)` iff `p1` is `instance-of point-particle` —
  the meta-typing triplet E28–E30, which has had no consumer until now.
- The domain is static, so the dependency edge runs to the *domain* headword,
  not to the delivered value. The graph never moves at trace time.

That last point is what keeps the mechanical layer intact: law detection, cycle
detection, house structure and degree computation are untouched, because the
edge set is fixed in the log.

## 7. Uniformity: the bare headword *is* the parameterised headword

```
inertial-acceleration  =  inertial-acceleration(point-particle)
```

There is no unparameterised fallback. Every object-dependent headword carries
its arity always.

This is what makes propagation automatic rather than per-entry opt-in. The
interpreter substitutes wherever a slot appears, in every entry, without anyone
declaring which entries participate.

It also retires two earlier devices:

- `inertial-acceleration_point-particle` can drop the underscore; the parameter
  carries what the name was carrying.
- "Ignorable dependence" is not a category. Either the headword depends on the
  object — declare it — or it does not, and no slot exists.

## 8. Coreference falls out

```
net-force(point-particle) := inertial-acceleration(point-particle) * inertial-mass(point-particle)
```

One slot, one delivery, every occurrence filled. `inertial-acceleration(p1) *
inertial-mass(p2)` is **unwritable**. Index-matching needs no audit because the
error has no expression.

## 9. Arity is per headword, not per definition

A headword carries multiple coexisting definitions; the binder is shared across
them. Two definitions wanting different parameter lists is not a feature to
support — it is the formalism reporting that one name is doing two jobs. Same
diagnostic value as the additivity and MDP collisions.

## 10. Open parameters are a legitimate state

Closure is a **degree**, not a gate on presentation.

| Form | Status | Reader's correct act |
|---|---|---|
| `net-force(point-particle)` | entry, open | none — this awaits an instance |
| `net-force(p1)` | instantiation, closed | may reduce |

`net-force(point-particle)` presented to a reader is not underdetermined: the
reader knows exactly what to do, namely wait. The open slot is *information*,
not absence. And a reader who attempts execution cannot succeed, so nothing is
recorded from a state the site did not warrant — the failure is loud.

The criterion is **determined by what is present**, not *closed*. An unbound
slot determines its own state. This distinguishes:

- open, not executed — fine (the entry as authored);
- closed, executed — fine (the instantiation);
- **closed-looking, executed using a remote datum — the violation.**

Reduction therefore gains a second precondition alongside `is_resolved`: no
open parameters. Same structure as the existing gate.

## 11. Argument values: closed, not order-0

An earlier draft required delivered arguments to be order-0 text. **Withdrawn.**
Headwords are constants, not free variables — the opening λ-term of this
discussion was closed *with* `+`, `1`, `5` in it. Headword-valued arguments do
not open a site.

The real condition is that a delivered value be **closed**: headwords
permitted, unbound parameters not. Substituting a closed term into any context
is always safe, which is why capture discipline never becomes necessary
(§16).

Two parameter kinds follow:

| Kind | Value | Delivery | Verified by |
|---|---|---|---|
| headword-valued | an entry name | creates a hole, expandable | `instance-of` (E28–E30) |
| instance-valued | scene object | order-0 text, no hole | nothing — ground data |

`impressed-force(interaction-instance, point-particle)` is instance-valued in
both slots, which is why order-0 looked sufficient. It was sufficient for that
entry and wrong as a general rule. Headword-valued arguments are required for
the one law that resists monomorphisation: the Newton III pairing law, which
quantifies over kind.

## 12. Dispatch is a headword-valued argument

`action-force` with `kind` delivered *is* dispatch. The abstract slot resolves
to the concrete entry by the delivered headword; the resolution is δ on that
headword; the static domain edge is the type; `instance-of` is the type check.

That is vtable structure, first-order. Dispatch has been the single item
blocking Design 3 entry, and it does not need new machinery beyond this layer.

---

## Part III — Identification: δ forwards, β backwards

## 13. The holes are the binder

A `Residual` with $n$ holes, keyed by original position, is an abstraction over
its holes:

```
λ□. latent₀ □₀ latent₁ □₁ … latentₙ
```

Positional, so **no names are needed — the positions are de Bruijn indices.**
This is why original-position keying gives stability for free, and why capture
cannot arise whatever is substituted. De Bruijn representation exists for
exactly that property; the VD arrived at it from "positions never shift."

The abstraction constructor was always present. It is not spelled `λ`.

## 14. The two passes are two reduction relations

**Forwards pass — δ.** `expand` unfolds a name into a hole; argument delivery
specialises a template. Neither computes: both **build the term**. A node after
expansion is a positional abstraction (its latents) applied to its children.
Expansion *forms* the application node.

**Backwards pass — β.** `reduce` contracts a node: operator latents plus value
children collapse to a value. `fold` is a post-order sweep — innermost-first,
i.e. **call-by-value**. The `is_resolved` gate is the CBV strictness
requirement: operands must be values before the operator applies. The spec's
own justification — that reducing `5 * {a}` is meaningless — is the argument
for strictness.

The turnaround at the settled frontier is the boundary between term
construction and term evaluation. δ at link time, β at run time — a staged
architecture, not an idiosyncrasy.

## 15. The identification predicts spec decisions already made

Evidence that this is structural rather than a resemblance. Each was justified
locally, in isolation, and each falls out of the reading:

| Decision | β reading |
|---|---|
| `unresolve` clears `reduced` up the ancestor chain | destroying a redex voids every contraction that consumed its value |
| a reduced node masks its descendants in all renders | a contracted redex is a value; values are opaque |
| reduced text is order-0 by fiat; graph cannot grow backwards | β contracts; spawning holes would admit non-termination |
| strong gate for reduce, provisional gate for cleanup | strict evaluation vs. cosmetic edits on unevaluated code |

## 16. Which fragment — and why it is not λ-calculus

Abstraction, bound occurrences, application and substitution are all present.
The fragment is nonetheless not λ-calculus, for three reasons:

1. **One binder, several bodies.** $\lambda x.B$ requires exactly one $B$; a VD
   headword has several definitions sharing one parameter list (§9). The object
   is $\lambda pp.\{B_1, B_2\}$ — not a λ-term but a **clause set with a shared
   head pattern**. Adding the binder did not dissolve the multiple-definitions
   obstruction; it sharpened it into the shape logic programming has and
   λ-calculus lacks.
2. **First-order.** A parameter's domain is a kind of object, not a function.
   No currying, no partial application, headwords are not values.
3. **No unification.** Delivery is a ground instance plus an `instance-of`
   check. No variable-to-variable binding, no backtracking. Weaker than Prolog;
   closer to parameterised templates with declared domains. Deterministic,
   terminating.

**Capture is unreachable.** Arguments are closed (§11), so no binder ever
appears inside an argument, so λ's substitution clause for abstractions never
fires. A formalism whose capture case cannot occur needs λ's *notation*, not
λ's *machinery* — and is spared the higher-order and non-termination hazards
that machinery brings.

## 17. Consequence worth acting on: confluence is an audit

β's central theorem is Church–Rosser — normal form is independent of reduction
order. The VD has a reduction machine whose contraction engine is a human, so
confluence is **not guaranteed and is therefore testable**.

> Fold the same trace twice under different orders. The root values must agree.
> Divergence localises a bad contraction to the node where the paths split.

This is the checker previously thought unbuildable. A checker over (render,
reduced) pairs would have to decide which arithmetic lies within its competence,
and there is no principled line. Confluence needs no competence at all: the
simulator evaluates nothing, compares two human reductions, and reports
disagreement.

It is also the consistency condition the probability programme requires. A
residue's distribution is meaningful only if residues compose consistently;
confluence is what "consistently" means. `fold`'s open question about scope
variants is therefore not a UX question — different fold scopes are different
reduction strategies, and comparing their results is the test.

## 18. And a dial for later

With the backwards pass named as β, CBV becomes a choice. Lazy contraction would
license reducing a node with open holes when the holes cannot affect the result
— `0 * {a}` → `0`. Currently forbidden, correctly, at this stage. But it is the
door to short-circuit reasoning: a force term vanishing by symmetry need not
have its magnitude evaluated.

---

## Part IV — Cost, and what to build first

## 19. Cost

1. **Every object-dependent Newton headword gets an arity.** The tokeniser stops
   dropping arguments everywhere at once. This lands on the already-queued
   Newton rewrite, with a second reason and a wider scope.
2. **Arity is a physics claim.** `net-force(point-particle)` asserts the
   dependence set. Wrong arity is substantive error, not typo.
3. **A parameter sigil is needed**, and it must be a **tokeniser primitive,
   never a headword** — if a parameter name were definable in the log, an entry
   could redefine what parameters mean and reproduce the `+ → *` failure inside
   the mechanism. It must also stay distinct from the hyphen-as-reference
   convention, which marks the opposite direction (a reference *into* the log).
4. **Delivery interacts with cleanup.** `net-force(point-particle)` → "the
   net-force of the p1" — the article breaks because a latent written for a type
   name received an instance name. Handled by existing gap-wise latent editing,
   but the cleanup offer must fire **on delivery**, not only on settle.

## 20. Build order

1. Parameter representation and the delivery operation (§5.2–5.3), with slots
   inside latents so hole positions never shift.
2. The reduce gate extension (§10).
3. `instance-of` wiring for admission (§6).
4. Confluence comparison over two folds (§17) — independent of the rest, and
   the highest-value item per unit of work.
5. Sigil and tokeniser change **last**, so it can be settled together with the
   hyphen convention rather than in competition with it.

Nothing here requires Design 3 to land first. Items 1–4 are additive to the
current engine.

## 21. Open

1. **Provenance field.** Under §7's uniformity an unbound slot means "awaiting
   instance," full stop, and the delivered-vs-reader-supplied distinction may be
   unnecessary. Check against a real wall entry: if some wall's demand is an
   unbound *parameter* rather than a hole, provenance returns.
2. **Definition selection.** Two coexisting definitions of `net-force` means
   expansion is nondeterministic. Selection is an input that has never been
   named as one, and it is not a wall in the current taxonomy. It does not break
   locality — the choice precedes the residual's existence and `expand` records
   it — but it is unaccounted.
3. **Empirical/computational agreement.** If `net-force(p1)` has both a measured
   definition and `a(p1) × m(p1)`, their agreement is a substantive claim that
   can fail. Newton II's falsifiable content may sit in inter-clause agreement
   rather than in the triplet. Testable: find another headword with both
   definition kinds and check whether their agreement is also a law.
4. **Which existing entries already run on reader memory.** Any entry whose
   residual expects trace-generated data it does not declare. Signal: a claimed
   reduction unreachable from local text plus external competence.
5. **Argument-list licensing.** If an NML2 entry declares an NML3 domain, that
   is a licensing violation expressed through arity — a failure mode with no
   current detector.
6. **Where cleanup sits.** It edits latents on unevaluated code during the
   backwards phase, so it is neither δ nor β but a source-level rewrite of the
   operator template mid-evaluation. Either a third operation needing its own
   account, or β on latent structure — in which case the reduce/clean split is
   finer than "grammar fixes vs. equivalence collapse."
7. **Acting-objects and the first-order boundary.** If a delivered acting-object
   is a callable and the trace ever *invokes* it, the fragment is higher-order
   and §16 needs redoing. If the trace only *expands* it by name, first-order
   holds. The Design 3 flow reads as expansion; the callable language may be
   analogical, and this should be settled explicitly.

---

## Provenance

Positional locality, its correction from log-scope to position-scope, the
priority of local determination over minimality, the uniformity of
parameterisation (§7), the rejection of closure-as-gate (§10), and the
identification of the backwards pass as β (§14) are the user's. The elimination
table (§3), the mechanical-necessity argument (§4), the domain-edge construction
(§6), the coreference result (§8), the fragment classification (§16), and the
confluence audit (§17) are analysis added here. No entry wording is proposed. No
file in VD-Newton was read for or edited by this note.
