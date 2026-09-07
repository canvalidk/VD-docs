# NML3 Content Specification

**Status:** working synthesis, d1  
**Project:** VD Newton / NML3 — force-account construction  
**Scope:** teacher-facing content authority to sit between the NML3 force-sum entries and a timed lesson plan  
**Audience:** introductory university mechanics, adaptable downward only after the logical structure is preserved

---

## 0. Purpose and stopping point

NML2.1 taught students to use a net-force vector that was supplied or inferred through Newton II while deliberately leaving its physical provenance unexplained. NML3 opens that debt.

NML3 asks:

> **How does a material object's opaque net-force slot acquire a physically licensed and complete force account?**

The lesson is not primarily about the mechanics of vector addition. It establishes:

- which force-instances may enter the sum;
- what gives each member its identity;
- why arbitrary vector decompositions do not create physical forces;
- how members are admitted one at a time;
- why positive discovery does not establish completeness;
- what an independent closer must establish;
- when the account may be summed and identified with net force; and
- when the correct result is to halt because the account remains open.

This specification does **not** yet teach:

- concrete force laws;
- the empirical discovery of every acting-object candidate from an unstructured scene;
- detailed activation-condition tests;
- action/reaction pairing;
- mechanically closed systems;
- continuum or infinite force accounts; or
- force-law-specific calculations involving gravity, springs, friction, tension, pressure, surface tension, and similar mechanisms.

Those are later destinations. NML3 may use supplied candidate keys, warrant records, exclusion records, force-vector values, and closer witnesses to teach the structure of a correct account without pretending to have derived those later objects already.

---

## 1. One-sentence thesis

> **A material object's net force is not obtained by inventing vectors that add correctly; it is obtained by closing a uniquely keyed force account and then summing the vector values of all and only its warranted members.**

Student-facing:

```text
Earn the members.
Use each source key once.
Prove there are no more.
Then add.
```

Compressed handle:

```text
ACCOUNT BEFORE SUM
```

---

## 2. The complete NML3 route

The student should be able to run:

```text
NML2 net-force demand
    -> fix the target material object and accounting context
    -> open a force-account ledger
    -> inspect acting-object-instance candidate keys one at a time
    -> admit a candidate only when an independent membership warrant succeeds
    -> reject duplicate keys
    -> preserve distinct members even when their vector values are equal
    -> record exclusions or unresolved candidates
    -> keep the account open after every positive generation step
    -> obtain an independent no-further-member determination
    -> close the interacting-forces-set
    -> map each member to its vector value
    -> sum all and only those values
    -> identify the resultant as the target's net force
```

Halt route:

```text
membership warrant missing
candidate domain not exhaustive
candidate remains unresolved
closer witness missing
    -> HALT: force account remains open
```

---

## 3. Provisional terminology

The current formal working headword is `contributing-force`, but its final wording remains open because the word can sound as though appearing in the sum is sufficient for membership.

This content specification therefore uses:

```text
force-account member
warranted force member
force-instance
```

as explanatory phrases.

They refer to the same provisional role unless a later terminology decision distinguishes them.

Formal placeholders:

```text
IFS(M | C)  interacting-forces-set for target M in context C
W_A         force-account member keyed by acting-object instance A
vec(W_A)    vector value or vector rule carried by W_A
```

No final entry wording is selected here.

---

## 4. Fixed target and accounting context

Every membership and closure claim is indexed to one fixed account.

Use a provisional context record:

```text
C = target-relevant frame, time or interval, state, and physical conditions
```

Then:

```text
IFS(M | C)
F_net(M | C)
W_A(M | C)
```

must share the same target and context.

The same acting-object instance may participate in another force account at another time, state, target, or physical arrangement without duplicating a member of the first account.

The student should understand:

> **Set uniqueness and closure apply inside one fixed force-accounting context.**

---

## 5. Four things that must not be collapsed

### 5.1 Material object

The target material object `M` is the owner or target of the force account.

It is not the identity key of each force member. One material object may have several force members from several acting-object instances.

### 5.2 Force-instance

A force-instance `W_A` is one admitted member of the target's force account.

It has identity beyond its numerical vector value.

### 5.3 Vector value

`vec(W_A)` is the vector carried by the force-instance under the chosen representation.

Vectors may be added, decomposed, resolved into components, or rewritten. Those algebraic operations do not create, destroy, merge, or multiply force-instances.

### 5.4 Warrant

A warrant is the evidential or theoretical licence for admitting a candidate force-instance to the account.

The warrant is not:

- another material object;
- another force vector;
- the force-instance itself; or
- the fact that adding the candidate improves agreement with measured net force.

The basic separation is:

```text
material object
!= force-instance
!= vector value
!= membership warrant
```

---

## 6. The force account is prior to the sum

The familiar force-sum direction is:

```text
independently warranted members
    -> take member vector values
    -> add those values
    -> obtain net force
```

It is not:

```text
start from net force
    -> choose convenient summands
    -> call the summands physical forces
```

A net-force vector admits indefinitely many vector decompositions:

```text
F_net = A + B
      = C + D + E
      = 1/2 F_net + 1/2 F_net
      = (F_net + X) + (-X)
```

The algebraic validity of these expressions establishes no interaction count and no force membership.

The student should be able to state:

> **The number of written vector terms does not determine the number of physical force-instances.**

The forward map from complete force accounts to resultants is many-to-one. Therefore the resultant cannot be inverted algebraically to recover a unique force account.

---

## 7. The correct interacting-forces-set

For one target and fixed context, NML3 commits to one correct IFS membership fact, up to harmless changes in notation, coordinate representation, and discovery order.

The IFS is not a set of bare vector values. A bare value-set would collapse distinct equal-valued force-instances.

The IFS must preserve at least:

```text
member identity key
target
context
vector value or rule
membership provenance
later force-role refinement slot
```

The set is unordered. The generation trace may be ordered.

Different generation orders may produce the same completed IFS and net force.

There is no intrinsic final force in the set. “Final force” means only the last member discovered in one trace before closure succeeds.

---

## 8. Force-member identity

### 8.1 Acting-object-instance key

Each force-account member is keyed by exactly one acting-object instance.

For a fixed IFS:

$$
\operatorname{key}(W_i)=\operatorname{key}(W_j)
\Longrightarrow W_i=W_j.
$$

Consequences:

```text
same acting-object instance rediscovered
    -> duplicate; no second member

same acting-object instance proposed under another force-role label
    -> same key; no second member

same target, different acting-object instances
    -> different keys; may be different members

different keys, equal vector values
    -> different members remain
```

### 8.2 Material object is not the key

If the target material object were used as the member key, every legitimate force on that target would collapse into one set member.

Therefore:

```text
material object -> owner/target of IFS
acting-object instance -> key of one IFS member
```

### 8.3 Force count

For a fixed account, IFS cardinality is acting-object-key cardinality.

It is not determined by:

- the number of written terms;
- the number of distinct vector values;
- the number of named force-law types;
- the number of material objects mentioned in prose; or
- the number of coordinate components.

---

## 9. Minimum membership-warrant interface

NML3 does not need to pretend that one universal concrete experiment has already been written for every force type. It must nevertheless specify what a valid membership procedure cannot omit.

A candidate force may be admitted only when its warrant satisfies at least:

### 9.1 Independence from the sum

The candidate does not become a member because including it makes the equation balance.

### 9.2 Physical attachment

The warrant connects the candidate to the target and a relevant acting-object instance or interaction condition.

A familiar algebraic shape such as `-kx` does not, by shape alone, identify the spring as the source.

### 9.3 Identity preservation

The warrant supplies or preserves the acting-object-instance key so duplicate rediscovery can be distinguished from a different equal-valued force.

### 9.4 Context preservation

The warrant is for the same target and accounting context as the IFS.

### 9.5 Traceability

The trace records the supplied observations, interventions, conditions, source, admission rule, and uncertainty or grade relevant to the membership claim.

### 9.6 Revisability

A later evidential revision may change the currently warranted account. This does not make arbitrary decompositions legitimate.

The concrete implementation of these constraints belongs partly to later acting-object and force-law work. In NML3, missing warrant information remains visible as missing input or an unresolved candidate.

---

## 10. The generator

### 10.1 Positive role

The generator answers:

> **Does this candidate acting-object instance key a warranted force member for this target and context?**

A successful step:

```text
candidate key A
+ membership warrant
+ matching target/context
+ unique-key check
+ vector value or rule
    -> admit W_A
```

### 10.2 Successor structure

Schematically:

$$
R(N)=\{W_N\}\cup R(N+1).
$$

This form contains a successor request after every successful member. It has no internal final-member case.

After any finite number of successful steps, the licensed conclusion is:

$$
\{W_0,\ldots,W_n\}
\subseteq
\operatorname{IFS}(M|C),
$$

not equality.

### 10.3 Duplicate check

The generator checks acting-object-instance keys, not:

- vector equality;
- target equality;
- force-law name;
- written symbol; or
- force-role label.

### 10.4 Discovery order

The generator records one discovery order. That order does not impose an order on the completed set.

### 10.5 Generator failure is not empty closure

No generated member may mean:

- the true IFS is empty;
- the search is incomplete;
- the warrant procedure failed;
- the candidate domain is missing; or
- the current candidates were excluded.

Only the closer can distinguish successful empty closure from unsuccessful generation.

---

## 11. The closer

### 11.1 Different logical question

The closer answers:

> **Does any eligible, not-yet-admitted force member remain?**

Generation is positive or existential:

$$
\exists A\;\operatorname{eligible}(A).
$$

Closure is a universal negative:

$$
\neg\exists A\;
\big(
\operatorname{eligible}(A)
\land
A\notin\operatorname{keys}(S)
\big).
$$

Repeated existential witnesses do not entail universal exhaustion.

### 11.2 Independent base case

The closer supplies the base case absent from the generator:

$$
R(K)=\varnothing.
$$

This is not another generated force member and does not appear as a summand.

### 11.3 Candidate-domain requirement

For the finite first-pass architecture, closure requires either:

- an exhaustively bounded acting-object candidate domain in which every candidate has been admitted or independently excluded; or
- a general exclusion argument that rules out all remaining candidates.

Merely asking for another candidate and receiving none is not proof of absence unless the search procedure itself is warranted as exhaustive.

### 11.4 Empty account

The empty IFS is the case in which the closer succeeds at the initial state before any positive member is generated.

### 11.5 New member after closure

If a new warranted member is discovered under supposedly unchanged target and conditions, then:

- the previous closer was invalid; or
- the contexts were not actually identical.

A correctly closed account is not harmlessly extended under unchanged conditions.

---

## 12. A concrete force-account ledger

For the first finite implementation, the student may use:

```text
FORCE ACCOUNT: target M, context C

ADMITTED
  key | member record | vector value | warrant provenance

EXCLUDED
  key | exclusion determination

UNRESOLVED
  key | missing determination

CANDIDATE DOMAIN
  exhaustive? yes / no / unknown

ACCOUNT STATUS
  open / closed

CLOSER WITNESS
  supplied / missing
```

The completed IFS is the set of admitted member records. The excluded and unresolved columns are trace evidence, not set members.

Closure in the finite first-pass model requires:

```text
candidate domain certified exhaustive
UNRESOLVED empty
all admitted members warranted
all admitted keys unique
```

---

## 13. Partial sums and residual testing

For a sound partial account `S`, define the partial resultant:

$$
P(S)=\sum_{W\in S}\operatorname{vec}(W).
$$

This may be calculated before closure as a diagnostic. It is not yet the force-sum result of the complete account.

Define:

$$
\mathbf r
=
\mathbf F_{\mathrm{net}}
-
P(S).
$$

Assuming the net-force value and current member vector values are correct:

```text
r != 0
    -> S cannot already be the complete correct IFS

r = 0
    -> algebraic agreement only
    -/-> closure
```

Why zero residual is insufficient:

There may be an omitted nonempty warranted collection `C` such that:

$$
\sum_{W\in C}\operatorname{vec}(W)=\mathbf 0.
$$

The omitted members are invisible to the resultant.

Student-facing handle:

```text
MISMATCH CAN DEFEAT.
MATCH CANNOT CLOSE.
```

---

## 14. Sum after closure

Only after independent closure may the law identify:

$$
\boxed{
\mathbf F_{\mathrm{net}}(M|C)
=
\sum_{W\in\operatorname{IFS}(M|C)}
\operatorname{vec}(W)
}
$$

The equation must be read in this order:

```text
warrant members independently
-> form and close the correct IFS
-> map members to vectors
-> add all and only those vectors
-> identify the resultant as net force
```

### 14.1 Binary-addition initiator

Operational accumulation may begin at the zero vector:

```text
0 + vec(W_1) + vec(W_2) + ...
```

The zero vector is the identity element of vector addition. It is not a force-account member.

The exposed nonempty physical account should be displayed as:

```text
vec(W_1) + vec(W_2) + ... + vec(W_n)
```

not as though zero were another force.

### 14.2 Termination marker

The closer signal is not a force and does not appear as the final summand.

### 14.3 Order independence

Different discovery orders yield the same sum when they produce the same closed finite set.

---

## 15. Zero cases

Students must distinguish all four cases.

### 15.1 Closed empty IFS

$$
\operatorname{IFS}(M|C)=\varnothing
\Longrightarrow
\mathbf F_{\mathrm{net}}(M|C)=\mathbf 0.
$$

### 15.2 Zero net force does not imply empty IFS

$$
\mathbf F_{\mathrm{net}}(M|C)=\mathbf 0
\not\Longrightarrow
\operatorname{IFS}(M|C)=\varnothing.
$$

### 15.3 Closed nonempty cancelling IFS

A nonempty set of warranted members may sum to zero.

Cancellation occurs only after members are mapped to vector values. It does not delete membership.

### 15.4 No member discovered, no closer witness

This is an open or failed account, not a successfully empty IFS.

---

## 16. Component and scalar equations are weaker

Agreement in one coordinate component does not establish closure of the full vector account.

Additional warranted forces may:

- have zero projection on that axis; or
- possess projections that cancel.

Therefore:

```text
component agreement
    -/-> full IFS closure
```

A component lesson may use a closed full account and then project it. It may not use projected agreement to infer the full membership account.

---

## 17. Mismatch after independent closure

Suppose:

- every member is independently warranted;
- the account is independently closed; and
- its sum does not agree with an independently measured or Newton-II-inferred net force.

The mismatch cannot be repaired by inventing a residual force.

At least one substantive element is wrong or mis-scoped:

```text
target/context
net-force measurement or inference
member warrant
member vector value
candidate-domain claim
closer witness
```

The correct output is a contradiction or diagnostic failure until one of those items is repaired.

---

## 18. Finite-account boundary

The present generator/closer architecture reaches a finite index `K` with:

$$
R(K)=\varnothing.
$$

This commits the first implementation to finite effective force accounts.

If infinite IFSs are later permitted, additional machinery is required for:

- infinite summation;
- convergence;
- enumeration-order independence; and
- the meaning of closure for an infinite domain.

NML3 d1 therefore uses:

> **finite, exhaustively closable effective force accounts**

as its explicit domain.

Continuum interactions require later aggregation or convergence machinery rather than silent inclusion.

---

## 19. Required learning outcomes

By the end of NML3, students should be able to:

1. Explain why force summation is not merely vector addition.
2. Distinguish a material object, force-instance, vector value, and membership warrant.
3. Explain why arbitrary decomposition of `F_net` cannot identify physical force members.
4. State that one correct IFS is intended for one fixed target and context.
5. Identify the acting-object instance as the member key and the material object as account owner/target.
6. Reject duplicate admission of the same key.
7. Preserve two distinct equal-valued members when their keys differ.
8. Explain why changing action/reaction labels does not create a second member under the same key.
9. Run one positive generator step.
10. Explain why repeated generation establishes only a subset.
11. Distinguish generation from closure.
12. Explain why search failure is not proof of absence.
13. Explain why a matching partial sum cannot close the account.
14. Use nonzero residual disagreement only as a defeater, not use zero residual agreement as proof.
15. Distinguish a closed empty IFS from a nonempty cancelling IFS.
16. Treat the zero accumulator and closer signal as nonmembers.
17. Sum member vector values only after closure.
18. Halt when a warrant, candidate-domain certificate, or closer witness is missing.
19. Reject an invented residual force used only to repair a mismatch.
20. State the finite-account boundary of the present architecture.

---

## 20. Installed student trace

The target behaviour is:

```text
What material object and context are active?
What is the acting-object-instance key of this candidate?
What independently warrants its membership?
Has that key already been admitted?
What vector value or rule does the admitted member carry?
Which candidate keys remain unresolved?
What proves that the candidate domain is exhaustive?
Has the no-further-member closer succeeded?
Only then: what is the vector sum of all member values?
```

Youngest compressed form compatible with the logic:

```text
Whose account?
Which source card?
Why does it belong?
Have we counted that source already?
Are any source cards unresolved?
What proves there are no more?
Now add.
```

---

## 21. Signature questions

### 21.1 Decomposition question

> `F_net = 10 N` right. Is `5 N + 5 N` automatically a two-force account?

Expected:

> No. It is a valid vector decomposition. Two independently warranted force-instances are required before it becomes a two-member force account.

### 21.2 Duplicate question

> The same acting-object instance is rediscovered with the same vector. Is another member added?

Expected:

> No. The acting-object-instance key is already present.

### 21.3 Equal-value question

> Two different acting-object-instance keys carry equal vectors. Does the set collapse them?

Expected:

> No. Force identity is keyed identity, not vector-value identity.

### 21.4 Matching-sum question

> The current partial sum equals measured net force. May generation stop?

Expected:

> Not on that basis. Omitted warranted members may cancel. Closure requires an independent no-further-member determination.

### 21.5 Empty-account question

> No member has been generated. Is the IFS empty?

Expected:

> Only if the closer succeeds at the initial state. Failed discovery alone does not establish emptiness.

### 21.6 Zero-net-force question

> The net force is zero. Are there no force members?

Expected:

> Not necessarily. A nonempty closed IFS may have zero resultant.

### 21.7 Mismatch question

> A closed warranted account does not reproduce independently measured net force. May a residual force be inserted?

Expected:

> No. The mismatch shows that a measurement, value, warrant, closure claim, or context is wrong or mis-scoped.

---

## 22. Exercise and evaluator bank

### 22.1 Valid algebra, invalid account

Sort expressions into:

```text
vector identity only
sound partial force account
closed force account
```

Include arbitrary halves and invented cancelling pairs.

### 22.2 Key-sort cards

Give cards varying:

- acting-object key;
- target;
- vector value;
- role label; and
- context.

Ask whether the card is:

```text
new member
duplicate
wrong target/context
same member under later role refinement
```

### 22.3 Account ledger activity

Students move candidate cards among:

```text
ADMITTED | EXCLUDED | UNRESOLVED
```

They may close only when the domain is certified exhaustive and unresolved is empty.

### 22.4 Matching-sum trap

Supply an unresolved candidate after the partial sum has already matched `F_net`.

Full credit requires refusal to close.

### 22.5 Empty versus equilibrium

Compare:

```text
closed empty account
closed two-member cancelling account
open account with no successful generation
```

All may display zero or no current resultant, but only the first two are complete force accounts.

### 22.6 Residual asymmetry

Give several partial accounts and measured net forces. Students classify:

```text
residual nonzero -> current account not complete under assumptions
residual zero -> closure still unproved
```

### 22.7 Component trap

Give an account whose x-components match while an unresolved y-directed candidate remains.

### 22.8 Closed mismatch

Require students to audit the substantive records rather than invent a balancing term.

### 22.9 Discovery-order comparison

Two groups generate the same members in different orders. Students verify that the completed set and sum agree.

### 22.10 Correct halt

Withhold:

- a member warrant;
- an exclusion determination;
- the exhaustiveness certificate; or
- the closer witness.

Students must return the appropriate open-account halt rather than guess.

---

## 23. Common misconceptions and repairs

### 23.1 “Any correct decomposition is a possible force list”

Repair:

> Algebra licenses a vector expression. Independent warrants license physical members.

### 23.2 “One written term means one interaction”

Repair:

> Term count is representational. Force count is keyed membership count.

### 23.3 “Equal vectors are the same force”

Repair:

> Different acting-object keys may carry equal vector values.

### 23.4 “The same force can be counted once as action and once as reaction”

Repair:

> Within one fixed target's IFS, the same acting-object key cannot be admitted twice under different role labels.

### 23.5 “A set cannot be generated because generation is ordered”

Repair:

> Discovery order belongs to the trace. Membership belongs to the unordered completed set.

### 23.6 “The last force found is intrinsically the final force”

Repair:

> It is only the last discovery in one trace. The closer, not the member, establishes finality.

### 23.7 “Nothing else was found, so there is nothing else”

Repair:

> Search failure is not proof of absence unless the search is exhaustive.

### 23.8 “The forces already add to net force, so the account is complete”

Repair:

> Omitted forces may have zero resultant. Matching is not closure.

### 23.9 “Zero net force means no interactions”

Repair:

> Zero is compatible with an empty account or a nonempty cancelling account.

### 23.10 “Cancellation removes the forces”

Repair:

> Cancellation occurs among vector values after membership is fixed.

### 23.11 “A missing residual can be called an unknown force”

Repair:

> A residual vector is not a membership warrant. Investigate the failed account instead.

---

## 24. Criteria of instillment

### 24.1 Basic criteria

| Criterion | Evidence |
|---|---|
| Account-first attention | Student asks for membership grounds before adding vectors. |
| Identity discipline | Student checks acting-object keys rather than vector equality. |
| Duplicate discipline | Student refuses a second member under the same key. |
| Equal-value discipline | Student retains distinct equal-valued members under different keys. |
| Provenance restraint | Student does not infer force members from algebraic fit. |
| Open-account discipline | Student treats positive generation as partial. |
| Closure discipline | Student asks what proves no member remains. |
| Residual asymmetry | Student uses mismatch as a defeater and refuses to use agreement as proof. |
| Zero discipline | Student distinguishes empty zero from cancelling zero. |
| Sum-order discipline | Student adds only after closure. |
| Halt discipline | Student stops when a warrant or closer witness is missing. |

### 24.2 Strong criteria

A stronger installation has occurred when the student spontaneously asks:

```text
What fixes the target and context?
What is the candidate source key?
What independently warrants membership?
Has this key already appeared?
Which candidates remain unresolved?
What proves the candidate domain is exhaustive?
What is the closer witness?
Only then, what is the resultant?
```

### 24.3 Longitudinal criteria

Later lessons should reveal whether the student:

- treats action/reaction as refinement of already keyed members rather than duplication;
- uses acting-object activation conditions to supply warrants rather than invent forces;
- recognises mechanically closed systems as a different closure question from IFS closure;
- handles concrete force laws as value-producing machinery for admitted members; and
- does not collapse continuum aggregation into an unexplained infinite list.

---

## 25. Provisional lesson sequence

The content can provisionally be taught as:

```text
1. NML2 handoff: where does the opaque net-force vector come from?
2. Decomposition trap: correct arithmetic does not create interactions.
3. Force-account ledger and the four non-collapsible items.
4. Member identity: one acting-object key, one member.
5. Equal vectors versus duplicate members.
6. One-at-a-time positive generation.
7. Matching partial sum trap.
8. Independent closure and exhaustive candidate discharge.
9. Sum after closure.
10. Empty account versus cancelling equilibrium.
11. Closed-account mismatch and no invented residual force.
12. Exit trace and unresolved-candidate burn.
```

The present material may become one long university lesson or two lessons:

```text
NML3.1  Membership before summation
NML3.2  Generation, closure, and the right to stop
```

That split should be decided only after the exercise bank is tested against timing.

---

## 26. Explicit later destinations

### Action-reaction block

Determines how an already admitted member is classified and how reciprocal sides are represented across target force accounts without duplicating a key within one IFS.

### Acting-object block

Supplies concrete acting-object structure, activation conditions, participant slots, and force-value rules.

### Mechanical-closure block

Tests whether interaction candidates of a selected mechanical system are internally paired. This is not the same question as whether one target's IFS is complete.

### Concrete force-law clusters

Supply executable value rules and empirical warrant procedures for gravity, springs, contact, strings, pressure, surface tension, and other acting-object types.

### Continuum/infinite extension

Supplies aggregation, convergence, and enumeration-independence machinery when a finite effective account is inadequate.

---

## 27. Entry-facing consequences

The two winter walls should be assigned explicitly:

```text
E16  force-member wall
     one-at-a-time independently warranted admission and duplicate-key control

E17  interacting-forces-set wall
     independent no-further-member closure, including initial empty closure
```

The entry-writing order should be:

```text
E14 and E15 triplet packets together
-> E16 and E17 wall packets from the trace machine
-> E13 net-force triplet packet last
```

Final residual wording must be audited against the behaviours and anti-habits in this specification.

---

## 28. Working summary

NML3 installs one central reversal of textbook habit:

```text
Do not begin by writing a force list and asking whether it adds correctly.
Begin by asking what earns membership and what earns closure.
```

The final force sum is small:

```text
add the vectors
```

The larger theoretical and pedagogical achievement is:

```text
which forces belong
why each belongs
why none is duplicated
why none is omitted
why the account is allowed to stop
```

Only after those questions are answered does the complete account produce the material object's net force.
