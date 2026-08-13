# NML3 Open Problem — Impressed-Force Identity and Action/Reaction Exclusivity

**Status:** open conceptual and representation problem  
**Project:** VD Newton / NML3  
**Topic:** impressed-force identity, acting-object keys, IFS membership, and action/reaction exclusivity  
**Date:** 2026-08-12

---

## 0. Purpose

NML3 is converging on the idea that a target material object's net force is obtained by summing the vector values of the impressed-force members of that target's interacting-forces-set (IFS).

A remaining structural problem must be solved before the force-sum and action/reaction blocks can be considered stable:

> **How should impressed-force identity be represented so that one acting-object can act on one target material object through exactly one force role — action or reaction — without allowing duplicate membership, while still allowing the same acting-object to participate in force accounts for multiple targets?**

This is not merely a naming issue.

The answer determines:

- what one impressed-force **is**;
- how two impressed-forces are distinguished;
- how duplicate admission is prevented;
- how action/reaction roles attach to force members;
- how an acting-object can participate in more than one target account;
- what information the IFS must store or inherit;
- whether `impressed-force` should be represented as a standalone kind, an acting-object attribute, a relation, or some keyed record;
- and what later entries must redefine in order to turn acting-object conditions into IFS membership.

The present note records the problem without selecting a final solution.

---

## 1. Current accepted force-sum commitments

### 1.1 One target has one force account in one fixed accounting context

Write:

$$
\operatorname{IFS}(M\mid C),
$$

where `M` is the target material object and `C` is the relevant force-accounting context.

The completed IFS contains the impressed-force members whose vector values are summed to produce the target's net force:

$$
\mathbf F_{\mathrm{net}}(M\mid C)
=
\sum_{W\in\operatorname{IFS}(M\mid C)}
\operatorname{vec}(W).
$$

### 1.2 Impressed-force membership is prior to summation

A vector is not an impressed-force merely because it can be written as a summand of the net force.

```text
impressed-force membership
    -> vector value
    -> force sum
    -> net force
```

not:

```text
net force
    -> arbitrary vector decomposition
    -> physical force membership
```

### 1.3 Later existence conditions are IFS admission conditions

`impressed-force` is intended to be defined extensionally through IFS membership.

Schematically:

$$
W \text{ is an impressed-force for } (M,C)
\iff
W\in\operatorname{IFS}(M\mid C).
$$

Later redefinitions of `impressed-force`, and later acting-object machinery, are expected to specify the physical conditions under which such membership exists.

Therefore:

```text
acting-object / interaction conditions obtain
    -> corresponding impressed-force exists
    -> corresponding member belongs to the target IFS
```

The trace may describe this as **admission**, but physically the same conditions are existence conditions for the impressed-force member.

### 1.4 One acting-object cannot act twice on the same target account

The current intended rule is:

> For one fixed target material object and force-accounting context, one acting-object instance may give rise to zero or one impressed-force member.

It must not produce two separate impressed-force members on the same target merely because:

- its vector is represented twice;
- its vector is decomposed;
- it is rediscovered;
- it is given two labels;
- or it is described once as action and again as reaction.

### 1.5 The same acting-object may participate in more than one target account

The previous rule does **not** mean:

```text
one acting-object
-> one impressed-force globally
```

A single acting-object may act on multiple material objects.

Therefore an acting-object `A` may be relevant to:

$$
\operatorname{IFS}(M_1\mid C_1),
$$

$$
\operatorname{IFS}(M_2\mid C_2),
$$

and so on.

The resulting impressed-force members must not be collapsed merely because they share the same acting-object identity.

---

## 2. The central action/reaction requirement

For one acting-object and one target material object, the target-side impressed-force must occupy **exactly one** of the available force roles:

```text
action-force
or
reaction-force
```

not both.

The target account must therefore make this impossible:

```text
same acting-object A
same target M
same accounting context C

-> impressed-force #1 labelled action
-> impressed-force #2 labelled reaction
```

when both records refer to the same acting-object-to-target relation.

Changing the role label must not manufacture a second member.

A future valid representation must support a rule of the form:

$$
\text{same acting-object}
+
\text{same target}
+
\text{same context}
\Longrightarrow
\text{one impressed-force identity}.
$$

The action/reaction status must refine that member rather than duplicate it.

---

## 3. Why acting-object identity appears to be needed

Suppose a target account contains two physical force members whose vector values are numerically equal:

$$
\operatorname{vec}(W_1)
=
\operatorname{vec}(W_2).
$$

The set must still preserve both if they arise from two distinct acting-objects.

Therefore vector value cannot determine impressed-force identity.

This motivates using acting-object identity as a key. Within one fixed IFS, the intended rule is approximately:

$$
A_i=A_j
\Longrightarrow
W_i=W_j.
$$

Different acting-object identities may support different members even when their vector values agree.

This would make duplicate detection simple:

```text
same acting-object key
-> same impressed-force member
-> do not add another member
```

---

## 4. The Alice problem

A mathematical set does not lose distinct people merely because they share a name. The problem appears only if the representation stores insufficient identity information.

If two different students are both represented only by the string:

```text
"Alice"
```

then:

$$
\{\text{"Alice"},\text{"Alice"}\}
=
\{\text{"Alice"}\}.
$$

The set has not failed. The representation has discarded the information needed to distinguish the two students.

The analogous danger is an `impressed-force` representation that preserves only:

- a vector value;
- a generic label;
- or some other non-unique field.

The final design must therefore answer:

> **What information makes two impressed-force instances the same or different object?**

---

## 5. Why `impressed-force_acting-object` is tempting

A headword such as:

```text
impressed-force_acting-object
```

looks attractive because it visibly binds force identity to acting-object identity.

It appears to support:

```text
acting-object identity
-> impressed-force identity
```

and would make action/reaction exclusivity easy to express:

```text
one acting-object
-> one impressed-force slot
-> slot receives action OR reaction status
```

However, this creates a serious problem.

---

## 6. Why `impressed-force_acting-object` may encode the wrong ownership claim

Within the current VD naming conventions, a form such as:

```text
X_acting-object
```

naturally suggests that `X` is an attribute, slot, or value **of the acting-object**.

If the headword is:

```text
impressed-force_acting-object
```

the residual implication may become:

> each acting-object has one impressed-force.

That is too strong.

The intended physics is:

```text
one acting-object
may impress forces on multiple target material objects
```

So the map:

$$
A\mapsto W
$$

cannot in general be single-valued globally.

The same acting-object may be associated with:

$$
W(A,M_1,C_1),
$$

$$
W(A,M_2,C_2),
$$

and further impressed-force instances.

Therefore making impressed-force a simple acting-object attribute risks turning a target-relative relation into a single stored property.

---

## 7. Local identity versus global identity

### 7.1 Inside one fixed IFS

Inside:

$$
\operatorname{IFS}(M\mid C),
$$

the target `M` and context `C` are already fixed.

Therefore acting-object identity **may be sufficient locally** to distinguish members:

$$
W_A \in \operatorname{IFS}(M\mid C).
$$

Within this account:

```text
same acting-object A
-> same member W_A
```

### 7.2 Across different IFSs

Globally, acting-object identity alone is insufficient.

The same acting-object may appear relative to different targets.

So:

$$
W(A,M_1,C_1)
$$

and:

$$
W(A,M_2,C_2)
$$

must be distinguishable even when the acting-object component `A` is the same.

This suggests that global impressed-force identity may require something like:

$$
(\text{acting-object},\text{target},\text{context})
$$

or equivalently:

$$
(\text{acting-object},\text{IFS identity}).
$$

This remains open.

---

## 8. Candidate representation A — relationally keyed impressed-force

One possible architecture is:

$$
W(A,M,C).
$$

Then:

```text
kind:
    impressed-force

identity:
    acting-object A
    target M
    accounting context C
```

### Potential advantage

It separates:

```text
what kind of thing?
    impressed-force

which instance?
    acting-object + target/context
```

### Open concern

It is not yet established that `(acting-object, target, context)` is the correct or minimal global identity criterion.

---

## 9. Candidate representation B — IFS identity plus acting-object identity

A more account-native representation is:

$$
W(\operatorname{IFS}(M\mid C),A).
$$

The member identity becomes:

```text
this force account
+
this acting-object
```

The local key inside the set remains the acting-object.

### Potential advantage

It captures target-relative force identity without pretending that an acting-object owns one impressed-force attribute.

### Open concern

It may make physical force identity depend too directly on the bookkeeping object `IFS`, when the physical relation might need to be definable before collection into the set.

---

## 10. Candidate representation C — a relational instance as primary

Another possibility is that one impressed-force is fundamentally a relation or relational instance connecting:

```text
acting-object
target material object
force role
context
```

The IFS then queries all such instances whose target equals `M`.

Schematically:

```text
SELECT impressed-force instances
WHERE target = M
AND existence conditions hold
```

### Potential advantage

The action/reaction role could refine one relational record rather than create separate members.

### Open concern

This may prematurely require `interaction` or an `impressed-force relation` to be a first-class stored object.

Nothing yet proves that the data must be stored interaction-first rather than object-first.

---

## 11. Storage architecture is not yet physics

The force-sum calculation requires a query equivalent to:

```text
find all impressed-force members
whose target is M
under context C
```

That requirement does **not** determine where the information is stored.

Possible implementations include:

### Interaction-centred storage

```text
interaction / acting-object record
    participant A
    participant B
    conditions
    force-side information
```

### Object-centred storage

```text
material object M
    acting-object / interaction references
```

### Bidirectional or indexed storage

Both sides may retain references or indexes.

NML3 should not accidentally convert one database representation into an ontological law.

The physics commitment appears weaker:

> The theory must be capable of recovering every and only impressed-force member relevant to the selected target account.

---

## 12. The role of set identity

A mathematical set is determined by its members:

$$
S=T
\iff
\forall x\,
(x\in S\leftrightarrow x\in T).
$$

But set theory does not itself supply the identity criterion for complex member objects.

NML3 therefore needs two layers:

```text
set semantics:
    duplicates collapse because identical members occur only once

member semantics:
    what makes two impressed-force instances identical?
```

The present open problem belongs primarily to the second layer.

---

## 13. The action/reaction exclusivity condition

Whatever representation is chosen must support this invariant:

```text
same acting-object
same target
same context
-> one impressed-force member
-> action OR reaction
```

Changing the force-role description must not create a second member.

A possible abstract condition is:

$$
\operatorname{role}(W)
\in
\{\text{action},\text{reaction}\}.
$$

More importantly:

```text
changing role description
-/-> new impressed-force member
```

---

## 14. Cross-target action/reaction pairing

The action/reaction pair is expected to live across target accounts rather than twice inside one target IFS.

Schematically:

```text
acting-object A
    -> impressed-force on M
    -> impressed-force on N
```

For example:

$$
W(A,M,C)\in\operatorname{IFS}(M\mid C)
$$

and:

$$
W(A,N,C)\in\operatorname{IFS}(N\mid C).
$$

The later action/reaction law must determine how these target-side force instances are paired and which role each occupies.

The NML3 constraint is:

> The pair must not be represented by inserting both action and reaction as separate members of the same target's IFS under one acting-object identity.

---

## 15. Required behavior of a successful solution

A final representation should satisfy all of the following.

### 15.1 Duplicate prevention

```text
same acting-object rediscovered
-> same impressed-force member
-> no duplicate IFS entry
```

### 15.2 Equal-valued distinct forces remain distinct

```text
different acting-objects
+ same target
+ equal force vectors
-> two different impressed-force members
```

### 15.3 Same acting-object may act on multiple targets

```text
same acting-object
+ target M1
-> impressed-force instance 1

same acting-object
+ target M2
-> impressed-force instance 2
```

These must not collapse globally.

### 15.4 Action/reaction is exclusive per target-side member

```text
same acting-object
same target
same context
-> one impressed-force member
-> action OR reaction
```

### 15.5 Role relabelling does not create membership

A force cannot be counted twice merely because the same force is later described under another role label.

### 15.6 Vector decomposition does not create identity

Breaking one impressed-force vector into components must not create additional impressed-force members.

### 15.7 Storage direction remains implementation-neutral unless later theory forces otherwise

The representation should not imply without argument that:

```text
acting-object owns force data
```

or:

```text
interaction owns all participant data
```

if the physics requires only that the relevant member can be recovered.

### 15.8 Future existence conditions must route cleanly into membership

When later acting-object conditions are supplied, they must determine whether the corresponding impressed-force instance exists in the target account.

---

## 16. Stress tests

### Test A — duplicate rediscovery

One spring acting-object `A` is encountered twice while constructing the same target IFS.

Expected:

```text
one impressed-force member
```

### Test B — same acting-object, two targets

One acting-object participates with `M1` and `M2`.

Expected:

```text
one target-side impressed-force in IFS(M1)
one target-side impressed-force in IFS(M2)
```

The two must remain distinguishable globally.

### Test C — action/reaction relabelling

The same target-side force is first described as action and later presented as reaction.

Expected:

```text
role inconsistency or correction
```

not:

```text
second member
```

### Test D — legitimate pair across targets

One acting-object connects `M1` and `M2`.

Expected:

```text
one impressed-force in IFS(M1)
one impressed-force in IFS(M2)
paired across accounts
```

### Test E — equal vectors from different acting-objects

Two different acting-objects produce equal vectors on one target.

Expected:

```text
two distinct impressed-force members
```

### Test F — one vector resolved into components

One impressed-force vector is represented by x and y components.

Expected:

```text
one impressed-force member
two coordinate components
```

not two members.

### Test G — context change

The same acting-object and target are considered under a different time/state/context.

The design must decide whether this is:

```text
same continuing impressed-force with changed state
```

or:

```text
different impressed-force instance
```

This may determine whether context belongs to force identity or only qualifies force state.

---

## 17. Subtle unresolved issue: whether context belongs to identity

The provisional global key:

$$
(\text{acting-object},\text{target},\text{context})
$$

may be too strong.

If the same spring continues acting on the same target through time while its vector changes, ordinary physical language may regard this as one continuing interaction rather than a new force-instance at every instant.

The final design must therefore distinguish:

```text
identity of a continuing impressed-force
```

from:

```text
state/value of that impressed-force at a selected context
```

It may turn out that:

$$
(\text{acting-object},\text{target})
$$

determines identity, while time/state/context qualifies its current value and existence.

Alternatively, context changes may create genuinely different force instances.

This must not be silently decided.

---

## 18. Subtle unresolved issue: acting-object identity may itself need refinement

The current architecture assumes one acting-object instance can act on one target through at most one impressed-force.

If later concrete acting-object work finds a legitimate case where one acting-object instance produces two independently countable target-side forces, then either:

1. the one-acting-object/one-force assumption is false; or
2. the acting-object was individuated too coarsely and should be split into distinct acting-object instances.

The current expectation is the second, but concrete force taxonomy should stress-test it.

---

## 19. Naming question

The terminology problem is therefore not merely:

```text
contributing-force
or
impressed-force
```

It is also:

```text
impressed-force
or
impressed-force_acting-object
or
impressed-force(A,M)
or
some other relationally explicit form
```

### `impressed-force`

Advantages:

- Newtonian historical provenance;
- target-facing residual meaning;
- does not by itself imply ownership by the acting-object;
- clean kind-name.

Risk:

- if identity is not represented separately, duplicate and cross-target distinctions may be lost.

### `impressed-force_acting-object`

Advantages:

- visibly associates force identity with acting-object structure.

Risk:

- may imply an acting-object owns one impressed-force attribute;
- may accidentally encode a globally single-valued map:

$$
A\mapsto W.
$$

That is presently believed false.

### `impressed-force(A,M)`

Advantages:

- makes relational identity explicit;
- permits one acting-object to produce target-distinct force instances.

Risk:

- may prematurely commit to a particular identity signature;
- context/time behavior remains unresolved.

No naming decision should be made until the underlying identity problem is solved.

---

## 20. What is actually being sought

We need a representation in which the following becomes structurally unavoidable:

```text
For one target force account:

one acting-object
-> zero or one impressed-force member

if the member exists:
-> exactly one action/reaction role

same acting-object + same target
-/-> two members

same acting-object + different target
-> may produce a different impressed-force member
```

This should follow from the object model rather than from an evaluator patch.

---

## 21. Open questions

1. What is the global identity criterion for one impressed-force?
2. Is acting-object identity sufficient only within a fixed IFS?
3. Does target identity belong directly to impressed-force identity?
4. Does IFS identity belong to impressed-force identity?
5. Does context belong to identity or merely qualify state/value?
6. Should action/reaction status be an attribute of the impressed-force member?
7. Can the same acting-object produce target-side forces under different contexts without identity confusion?
8. Should acting-object instances be defined finely enough that one acting-object-to-target pairing always yields at most one force?
9. Does the eventual representation require `interaction` to be a first-class object, or can it remain a relation/query over object-held information?
10. Which side owns the data: acting-object, target object, interaction relation, IFS member record, or some distributed representation?
11. Which of those are physics commitments and which are implementation choices?
12. What naming convention exposes the right residual meaning without falsely implying attribute ownership?
13. How should the action/reaction law pair two target-side impressed-force instances across distinct IFSs?
14. Can the key structure be derived from the six-entry law architecture rather than stipulated externally?
15. What primitive student exercise would expose an incorrect solution to this identity problem?

---

## 22. Provisional decision rule

Do not yet rename the formal member headword merely because `impressed-force` is historically and residually attractive.

First resolve:

```text
WHAT IS ONE IMPRESSED-FORCE INSTANCE?
```

Then:

```text
WHAT INFORMATION IDENTIFIES IT?
```

Then:

```text
WHERE DOES ACTION/REACTION STATUS LIVE?
```

Only after those questions are settled should the final headword form be selected.

---

## 23. Compact statement of the open problem

> **NML3 needs an impressed-force representation in which one acting-object can contribute at most one target-side force member to one fixed force account, with that member being exclusively action or reaction, while the same acting-object may still participate in other target accounts. Acting-object identity therefore appears necessary for local IFS member identity, but making `impressed-force` a simple acting-object attribute appears too strong. The unresolved task is to find the correct relational identity structure and naming convention without turning an implementation choice into physics.**
