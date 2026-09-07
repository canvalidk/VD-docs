# NML3 Entry-to-Lesson Bridge

**Status:** working bridge, d1  
**Project:** VD Newton / NML3  
**Purpose:** turn the current force-sum constraints into entry packets, a content specification, and then a timed lesson draft without silently inventing the missing warrant or closure machinery.

---

## 0. Diagnosis

The NML3 work has not stalled at the level of ideas. It has already established most of the **law contract**:

- one correct force account for one fixed target and context;
- independently warranted force members;
- acting-object-instance identity keys;
- no duplicate key admission;
- a distinction between force-instance identity and vector value;
- positive generation versus independent closure;
- the inability of a matching partial sum to establish completeness;
- the empty-account and cancelling-nonempty-account distinction; and
- the final all-and-only vector-sum relation.

What is missing is the operational middle layer:

```text
conceptual constraints
    -> abstract trace/state machine
    -> content specification
    -> exercise and evaluator bank
    -> timed lesson plan
    -> final residual wording
```

The current `nm_l3_lesson_draft.md` jumps from conceptual notes directly to seven lesson sections. That is why the writing process still feels vague.

---

## 1. The route that worked in NML1 and NML2

The previous lessons did not really follow a simple linear route from finished entries to prose.

They followed something closer to:

```text
law-house or entry commitments
    -> problem the law solves
    -> runnable student trace
    -> supplied inputs and explicit debts
    -> distinctions and forbidden inferences
    -> signature questions and failure cases
    -> content authority
    -> timed classroom sequence
    -> refined entry wording
```

NML1 found the path-problem, the `influence` handle, the Newton-I diagnostic trace, and the puck question.

NML2.1 found the ownership problem, the addressed Newton-II trace, the one-row discipline, and the mass-reuse burn. Its lesson plan then treated the content document as the canonical authority.

NML3 now needs the equivalent of those intermediate objects.

---

## 2. Provisional NML3 identity

### 2.1 Working lesson title

```text
NML3: Account Before Addition
The Force-Account Problem Behind the Force Sum
```

### 2.2 One-sentence thesis

> **A material object's net force is not obtained by inventing vectors that add correctly; it is obtained by closing a uniquely keyed force account and then summing the vector values of all and only its warranted members.**

### 2.3 Student-facing handle

```text
Earn the members.
Use each source key once.
Prove there are no more.
Then add.
```

Compressed:

```text
ACCOUNT BEFORE SUM
```

### 2.4 Signature question

> A partial force account already sums to the independently measured net force, but one acting-object candidate has not been ruled in or out. May the account be closed?

Expected answer:

> No. A zero residual does not prove exhaustion. Omitted warranted members may have zero resultant. Closure needs an independent no-further-member determination.

### 2.5 Burn / halt case

```text
all admitted members are sound
current partial sum matches measured net force
one candidate remains unresolved
no exhaustive closer witness
    -> HALT: force account remains open
```

This is the NML3 equivalent of NML2.1's expired mass-address halt.

---

## 3. The first structural repair: assign the two walls to the two winter words

The force-sum triplet has:

```text
November word:
    net-force-material-object

Winter word A:
    interacting-forces-set

Winter word B:
    contributing-force / warranted-force / final force-member headword
```

A six-entry law requires one outward wall for each winter word. The current labels describe two IFS operations, but they do not yet make the wall-headword assignment explicit.

The clean assignment is:

```text
E16  force-member wall
     outward job: admission/generation of one independently warranted,
     uniquely keyed member

E17  interacting-forces-set wall
     outward job: independent exhaustion/closure of the whole account
```

So the functional descriptions remain:

```text
E16  generator wall
E17  closer wall
```

but their headword ownership becomes:

```text
E16  wall of the force-member winter word
E17  wall of the interacting-forces-set winter word
```

This matches the logical division:

```text
only warranted members  -> E16 admission wall
all warranted members   -> E17 closure wall
```

---

## 4. The abstract force-account machine

Before writing entry prose, write the object and state that the entries must cause an interpreter to construct.

### 4.1 Fixed accounting context

Use one provisional context token:

```text
C = fixed target, frame, time/interval, state, and physical conditions
```

Then write:

```text
IFS(M | C)
F_net(M | C)
W_A(M | C)
```

This preserves same-context discipline without prematurely deciding the final surface notation for every qualifier.

### 4.2 Force-member witness sheet

Each admitted member should carry at least:

```text
FORCE-MEMBER RECORD
  member key:
      one acting-object-instance identity

  target:
      material object M

  context:
      C

  vector value or vector rule:
      vec(W_A)

  membership warrant:
      provenance showing that membership was earned independently of
      agreement with F_net

  role:
      unbound in NML3; later refined as action or reaction
```

Invariants:

```text
same key rediscovered
    -> same potential member; no second admission

different keys, equal vector values
    -> distinct members may both remain

same target, different keys
    -> distinct members may both remain

same key, different force-role label
    -> not a second member
```

### 4.3 IFS witness sheet

```text
INTERACTING-FORCES-SET RECORD
  owner / target:
      material object M

  context:
      C

  admitted-member map:
      key -> force-member record

  generation trace:
      ordered history of discoveries

  candidate-domain status:
      bounded / unbounded / supplied / unresolved

  exclusion or discharge records:
      why unadmitted candidates do not key members

  closure status:
      open / closed

  closer witness:
      independent no-further-member determination

  resultant:
      available as net force only after closure
```

The generation trace may be ordered while the completed IFS remains an unordered set.

### 4.4 Minimal state partition

For a finite first-pass candidate domain `D_C`, use:

```text
ADMITTED   keys that have produced warranted members
EXCLUDED   keys independently determined not to produce members
UNRESOLVED keys not yet discharged either way
```

The completed mathematical set is the set of admitted member records. The other columns belong to the trace and closer evidence, not to IFS membership.

### 4.5 Transitions

#### Generate one member

```text
select unresolved key A
obtain independent membership warrant
confirm A is not already an admitted key
construct W_A with target, context, vector value, and provenance
move A -> ADMITTED
account remains open
```

The licensed conclusion after any finite number of successes is only:

```text
current admitted members are a warranted subset of IFS(M | C)
```

#### Discharge a nonmember candidate

```text
select unresolved key A
obtain an independent exclusion determination
move A -> EXCLUDED
account remains open unless closure conditions are now met
```

#### Close

For the finite first-pass architecture:

```text
candidate domain is warranted as exhaustive
UNRESOLVED is empty
all admitted keys are unique and warranted
    -> account closes
```

A general exclusion argument may replace literal enumeration, but simple search failure may not.

#### Sum

Only after closure:

```text
F_net(M | C)
    = sum over admitted W in IFS(M | C) of vec(W)
```

For a closed empty account:

```text
IFS(M | C) = empty set
F_net(M | C) = zero vector
```

For a closed nonempty cancelling account:

```text
IFS(M | C) is nonempty
sum vec(W) = zero vector
F_net(M | C) = zero vector
```

### 4.6 Partial sums

A partial vector sum may be calculated as a diagnostic:

```text
P(S) = sum of currently admitted member vectors
```

but it is not yet licensed as the complete force-sum result.

Residual test:

```text
r = measured F_net - P(S)

r != 0
    -> current account cannot already be the correct complete account,
       assuming the measurements and current member values are correct

r = 0
    -> algebraic agreement only
    -/-> closure
```

---

## 5. The honest NML3 lesson boundary

NML3 should consume some structured inputs rather than pretending to derive all later physics at once.

### 5.1 Supplied or provisionally available to NML3

```text
a target material object M
an accounting context C
acting-object-instance candidate keys, or a candidate-domain witness
membership-warrant or exclusion evidence when a candidate is examined
the vector value or vector rule of an admitted member
an independent closer witness when closure is claimed
```

### 5.2 NML3 teaches

```text
why a force account is needed
why vector decomposition cannot establish membership
how one member is admitted without duplicate keys
why equal vectors can belong to distinct members
why generation does not establish completeness
what closure must establish
why matching F_net cannot be the stopping rule
how empty and nonempty zero-resultant accounts differ
why the sum is taken only after closure
what correct halt states look like
```

### 5.3 Deferred

```text
how raw scenes produce acting-object candidates
how a concrete activation condition is tested
how concrete force laws produce vector values
how action/reaction roles are assigned
how reciprocal forces are represented across target IFSs
how mechanical-system closure is tested
how continuum or infinite force accounts are represented
```

This follows the precedent of NML2.1: consume a structured object now, expose the debt, and let the later block explain how that object is produced.

---

## 6. Proposed NML3 content-specification spine

The next canonical document should be:

```text
NML3_CONTENT_SPECIFICATION_d1.md
```

Recommended sections:

### 0. Status, purpose, and stopping point

- NML2 handoff: `F_net` was supplied or inferred but physically opaque.
- NML3 question: how does that slot acquire a complete physical force account?
- Explicit later debts.

### 1. One-sentence thesis and complete student route

```text
opaque net-force demand
    -> fix target and context
    -> open force-account ledger
    -> examine candidate source keys one at a time
    -> admit independently warranted unique members
    -> discharge or retain unresolved candidates
    -> obtain independent exhaustion witness
    -> close IFS
    -> map members to vector values
    -> vector-sum
    -> return net force
```

### 2. Four items that must not be collapsed

```text
material object
a force-instance
its vector value
the warrant for membership
```

### 3. Force account versus vector decomposition

- forward map is many-to-one;
- term count does not imply interaction count;
- arbitrary halves and cancelling pairs are algebraically valid but physically unwarranted.

### 4. The context-indexed correct IFS

- one target and fixed conditions;
- one correct membership fact;
- ordering and notation do not change set membership;
- discovery order belongs to the trace, not to the set.

### 5. Force-member identity

- acting-object-instance key;
- target is owner, not key;
- equal vector values versus duplicate identity;
- role labels do not create new members.

### 6. The generator

- one positive member at a time;
- duplicate check;
- provenance record;
- repeated success gives only a subset;
- no intrinsic final member.

### 7. The closer

- universal/exhaustiveness question;
- candidate-domain certificate or general exclusion argument;
- search failure is not proof of absence;
- initial-state closure for the empty account.

### 8. Partial sums and the residual asymmetry

- partial sum may be used diagnostically;
- mismatch can defeat completeness;
- match cannot establish completeness;
- no invented residual force.

### 9. Sum after closure

- map member identity to vector value;
- add all and only members;
- order independence;
- first-addition zero is an accumulator identity, not a force member;
- termination marker is not a summand.

### 10. Zero cases

```text
closed empty IFS -> zero net force
zero net force -/-> empty IFS
closed nonempty cancelling IFS -> zero net force
no generated member + no closer witness -> unknown/open, not empty
```

### 11. Mismatch and contradiction handling

If an independently warranted and independently closed account fails to reproduce independently measured net force:

```text
check context
check measurement
check member warrants
check vector values
check closer witness

never invent a residual member merely to balance the equation
```

### 12. Finite-account boundary

The present generator/closer trace terminates at a finite `K`. Therefore the first implementation should either:

```text
A. explicitly restrict NML3 to finite effective force accounts; or
B. add a separate infinite-account/convergence architecture.
```

For the first lesson, A is the clean boundary.

### 13. Exercise, evaluator, and misconception bank

Use the cases in Section 8 below.

### 14. Handoff to later blocks

- acting-object candidate origination;
- activation conditions and concrete force values;
- action/reaction refinement;
- mechanical closure;
- continuum aggregation.

---

## 7. Provisional lesson architecture

Do not time this until the content specification and exercise bank are stable. The conceptual sequence should nevertheless be:

### Segment 1 — The decomposition trap

Opening question:

> An object's net force is `10 N` right. May we write two `5 N` right arrows and call them two forces?

Install:

```text
valid vector decomposition
is not yet
valid force account
```

### Segment 2 — Build the force-account ledger

Introduce:

```text
target/context card
candidate source key
force-member card
warrant/provenance slot
vector-value slot
```

### Segment 3 — Identity before arithmetic

Sorting drills:

```text
same key, same vector -> duplicate
same key, other role -> duplicate proposal
new key, same vector -> distinct member
same target, new key -> possible distinct member
```

### Segment 4 — Generate one at a time

Students process candidate cards and build an open account.

Keep the current partial sum visible but labelled:

```text
partial resultant — not yet complete net-force reconstruction
```

### Segment 5 — The matching-sum trap

Current members already reproduce the measured net force.

Reveal an unresolved candidate or possible cancelling pair.

Install:

```text
MATCHING IS NOT CLOSURE
```

### Segment 6 — Close independently

Use an exhaustive candidate board:

```text
ADMITTED | EXCLUDED | UNRESOLVED
```

Closure succeeds only when the candidate domain is exhaustive and `UNRESOLVED` is empty.

### Segment 7 — Sum the closed account

Map member cards to vectors and add.

Explicitly distinguish:

```text
zero accumulator
force members
closure signal
```

### Segment 8 — Empty and cancelling accounts

Contrast:

```text
closed empty account -> 0
closed nonempty cancelling account -> 0
open account with no discovered member -> not yet 0 by closure
```

### Segment 9 — Exit trace and burn

Use the signature unresolved-candidate question.

Expected final student trace:

```text
fix target/context
-> admit warranted unique force members
-> do not infer membership from the sum
-> do not infer completeness from a match
-> close independently
-> add all member vectors
-> return net force
-> halt if closure remains unresolved
```

---

## 8. Required exercise and evaluator contrasts

### 8.1 Arbitrary half decomposition

```text
F_net = 1/2 F_net + 1/2 F_net
```

Result:

```text
valid algebra
no force membership warrants
not an IFS
```

### 8.2 Invented cancelling pair

```text
F_net = (F_net + A) + (-A)
```

Result:

```text
valid algebra
no extra physical members earned
```

### 8.3 Duplicate key

```text
same acting-object-instance key presented twice
```

Result:

```text
one member only
no second vector contribution
```

### 8.4 Equal vectors, different keys

```text
A1 != A2
vec(W_A1) = vec(W_A2)
```

Result:

```text
two distinct members remain
```

### 8.5 Action/reaction relabelling

```text
same key proposed once as action and once as reaction
```

Result:

```text
same potential member
later role refinement cannot duplicate it
```

### 8.6 Matching partial sum without closer

```text
all current members warranted
partial sum = measured F_net
no no-further-member witness
```

Result:

```text
sound partial account
closure fails
```

### 8.7 Nonzero residual

```text
partial sum != measured F_net
```

Result:

```text
current account cannot be the complete correct account under the stated
measurement and value assumptions
```

### 8.8 Closed empty account

```text
no admitted member
all candidates exhaustively excluded
```

Result:

```text
IFS = empty set
F_net = zero vector
```

### 8.9 Nonempty equilibrium account

```text
two or more warranted members
vector sum = zero
account closed
```

Result:

```text
F_net = zero
IFS is not empty
```

### 8.10 Search failure without exhaustiveness

```text
ask for another candidate
none immediately supplied
search method not certified exhaustive
```

Result:

```text
open account
not an empty-set or closure proof
```

### 8.11 Scalar/component agreement

```text
x-components reproduce measured x net force
```

Result:

```text
full vector closure not established
```

### 8.12 Closed-account mismatch

```text
account independently warranted and closed
sum does not equal independently measured F_net
```

Result:

```text
diagnostic contradiction or scoping failure
no invented residual force
```

---

## 9. Entry-packet targets

Do not write polished entry sentences first. Fill IRIL, IRIE, witness slots, boundaries, and tests.

### E14 — `interacting-forces-set` triplet corner

```text
Plain purpose:
  Admit one correct context-indexed force account as distinct from arbitrary
  sum-equivalent vector collections.

IRIL allowed:
  IFS membership is prior to the resultant.
  IFS contains all and only force-member instances of the law.

IRIL blocked:
  arbitrary vector decomposition
  human-supplied flat list without admission/closure trace

IRIE:
  reader asks what licenses the collection before adding
```

### E15 — force-member triplet corner

```text
Plain purpose:
  Admit the member-kind whose vector value may count in the complete IFS.

IRIL allowed:
  one member has force-instance identity beyond its vector value

IRIL blocked:
  summand status alone
  coordinate component as force member
  repeated written occurrence as repeated physical member

IRIE:
  reader separates member identity from vector representation
```

### E16 — force-member wall / generator

```text
Plain purpose:
  Make one member independently usable by recording a membership warrant,
  one identity key, the target/context, and vector value.

IRIL allowed:
  positive one-at-a-time admission
  duplicate rejection by key

IRIL blocked:
  membership inferred from net-force fit
  finality inferred from one or many successes

IRIE:
  admit for a reason; count each key once; keep account open
```

### E17 — IFS wall / closer

```text
Plain purpose:
  Make the completed collection independently usable by supplying the missing
  no-further-member base case.

IRIL allowed:
  closure from exhaustive candidate discharge or general exclusion
  empty closure at initial state

IRIL blocked:
  known count
  no immediately found next member
  zero residual
  matching measured net force

IRIE:
  ask what proves exhaustion; halt when closure is missing
```

### E13 — `net-force-material-object` triplet corner

Write last.

```text
Plain purpose:
  Identify the vector sum of the complete IFS's member values as the target's
  net force.

IRIL allowed:
  sum after closure
  empty sum = zero

IRIL blocked:
  backward decomposition as member discovery
  partial sum silently renamed net force

IRIE:
  build account first; then add
```

---

## 10. Remaining architectural decisions, now narrowed

### 10.1 Final force-member headword

For content and lesson drafting, use the neutral pedagogical phrase:

```text
force-account member
```

Keep the formal headword open among:

```text
contributing-force
warranted-force
another selected term
```

The final choice should be judged against the installed behaviour, not made before it.

### 10.2 `interacting-forces-set` versus list-like generation

Keep `interacting-forces-set` provisionally.

The apparent list behaviour belongs to the **ordered discovery trace**, not to the completed mathematical object. Different discovery orders can yield the same set.

### 10.3 Acting-object key before the acting-object block

The semantic constraint is settled, but the entry-order representation still needs an audit.

Options to evaluate in the E16 packet:

```text
A. carry an opaque source-instance key in a witness slot and let the later
   acting-object block refine its type;

B. introduce a prior scaffold headword for the key;

C. alter the entry order.
```

Do not silently mention a later headword in E16 if that creates a forward dependency.

### 10.4 Exact warrant mechanism

NML3 can specify the **interface and admissibility constraints** of a warrant while concrete acting-object and force-law blocks later instantiate it.

The trace must expose missing warrant evidence as a suspension or halt, never fill it from background habit.

### 10.5 Finite versus infinite accounts

Adopt finite effective force accounts for the first lesson and evaluator unless a separate convergence architecture is added.

### 10.6 Time and condition indexing

Use one context token `C` in the content specification. Expand it into final headword-visible qualifiers only during packet writing.

---

## 11. Immediate production order

```text
1. Ratify the provisional NML3 thesis and student trace.
2. Ratify E16 as the force-member/admission wall and E17 as the IFS/closure wall.
3. Draft the force-member and IFS witness sheets.
4. Decide the finite-account boundary for the first implementation.
5. Fill E14 and E15 entry packets together.
6. Fill E16 and E17 packets from the abstract state machine.
7. Write NML3_CONTENT_SPECIFICATION_d1.md.
8. Build the exercise/evaluator bank.
9. Decide whether the classroom material is one long lesson or NML3.1/NML3.2.
10. Draft the timed lesson.
11. Write E13 last.
12. Run residual-provenance and hidden-import audits on all five entries.
```

The important change is that entry wording and lesson wording are no longer treated as two independent acts. Both are implementations of the same trace contract and intended interpreter behaviour.

---

## 12. Compact working summary

The present NML3 notes already answer the central conceptual question:

```text
A correct force sum is the resultant of a correct force account,
not a decomposition selected because it works algebraically.
```

The next task is not free-form lesson prose. It is to make that claim runnable:

```text
force-member witness
+ IFS witness
+ generator transition
+ closer transition
+ halt states
+ evaluator contrasts
```

Once those are explicit, both the entries and the lesson should become much less vague.
