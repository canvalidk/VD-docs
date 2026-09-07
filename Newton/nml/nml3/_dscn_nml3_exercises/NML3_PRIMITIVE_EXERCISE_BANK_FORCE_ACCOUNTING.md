# NML3 Primitive Exercise Bank — Force-Account Membership, Closure, and Summation

**Status:** working exercise-bank note  
**Project:** VD Newton / NML3  
**Purpose:** identify primitive exercises that install the force-account operations before concrete acting-object existence conditions are taught  
**Primary audience:** introductory university mechanics, with many exercises adaptable downward

---

## 0. Central teaching boundary

NML3 does not yet need to teach the concrete physical conditions under which springs, gravitational mechanisms, contacts, strings, fluids, and other acting objects produce force contributions.

It needs to prepare the machinery that will consume those conditions once later entries supply them.

For a fixed target material object `M` and accounting context `C`, use:

$$
\operatorname{IFS}(M\mid C)
$$

for the interacting-forces-set, and let `A`, `B`, `C`, ... label contributing-force records. Their vector values are written:

$$
\operatorname{vec}(A),\quad
\operatorname{vec}(B),\quad
\operatorname{vec}(C),\ldots
$$

The structural definition is:

$$
A\text{ is a contributing-force for }M\mid C
\quad\Longleftrightarrow\quad
A\in\operatorname{IFS}(M\mid C).
$$

Later redefinitions of `contributing-force` will provide increasingly concrete existence or admission rules for membership in the IFS. In these primitive exercises, those later rules are not derived. Instead, the exercise supplies one of the following:

```text
A. the complete IFS directly; or

B. candidate keys together with supplied existence-condition results,
   exclusion results, and closure information.
```

The student then practises what follows from those supplied facts.

The central order is:

```text
membership or existence fact
    -> contributing-force record
    -> vector value or vector rule
    -> closed IFS
    -> vector sum
    -> net force
```

The prohibited reverse order is:

```text
net force
    -> residual or decomposition
    -> invented contributing-force
```

A compact handle for the whole bank is:

```text
MEMBERSHIP FIRST.
VALUES SECOND.
CLOSURE BEFORE NET FORCE.
```

---

## 1. What “primitive exercise” means here

A primitive exercise should isolate one logical or operational move. It should not require the student to solve a whole physical scene, identify an acting object, derive a force law, and calculate a resultant all at once.

A good primitive exercise normally asks the student to perform only one of these actions:

```text
select the members of a supplied IFS
look up the vector values of those members
form a symbolic force-sum expression
calculate a closed-account resultant
recover the value of an already-known member
reject a duplicate key
preserve distinct equal-valued members
classify an account as open or closed
route supplied existence-condition results
calculate a residual without inventing a member
halt when closure or value information is insufficient
```

The advantage of primitive exercises is diagnostic clarity. When a student fails, the teacher can see whether the problem concerns:

```text
membership
identity
value qualification
target/context indexing
closure
vector addition
or illegitimate reverse inference
```

rather than receiving one undifferentiated wrong free-body diagram.

---

## 2. Recommended standard sheet anatomy

Most exercises in this bank can use the same visual grammar. Repetition of the layout should help install the trace.

### 2.1 Account header

Every sheet begins with:

```text
TARGET MATERIAL OBJECT:  M
ACCOUNTING CONTEXT:      C
```

For early sheets, `C` may be a simple label such as:

```text
C1 = this target, this instant, this model
```

More advanced sheets may expose time, interval, frame, or state explicitly.

### 2.2 Force-record bank

A separate table provides force records and their vector values.

| Force record | Vector value | Value status |
|---|---:|---|
| `A` | `10 N right` | known |
| `B` | `5 N left` | known |
| `C` | `vec(C)` | unqualified |
| `D` | `12 N right` | known |

The bank should deliberately contain records that are not members of the active IFS in some exercises. This prevents the student from treating “appears on the page” as “belongs in the sum.”

### 2.3 Membership or ledger panel

One of the following is supplied.

**Closed-set form:**

```text
IFS(M | C) = {A, B, C, E}
ACCOUNT STATUS: CLOSED
NO FURTHER MEMBERS: SUPPLIED
```

**Partial-set form:**

```text
{A, B, C} ⊆ IFS(M | C)
ACCOUNT STATUS: OPEN
```

**Ledger form:**

| Candidate key | Existence/admission result | Ledger destination |
|---|---|---|
| `a` | satisfied | admitted |
| `b` | failed | excluded |
| `c` | unresolved | unresolved |

### 2.4 Task box

The task should be specific:

```text
FORM THE FORCE-SUM EXPRESSION.
CALCULATE THE NET FORCE.
RECOVER vec(E).
CLASSIFY THE ACCOUNT.
CALCULATE THE RESIDUAL, BUT DO NOT NAME A NEW FORCE.
```

### 2.5 Required status line

Every answer box should include a status line:

```text
RESULT STATUS:
[ ] numerical vector
[ ] symbolic vector expression
[ ] member value recovered
[ ] underdetermined relation only
[ ] residual only — not a force member
[ ] account open — halt
[ ] contradiction / audit required
```

This prevents all non-numerical outputs from being treated as failures.

---

## 3. Answer vocabulary to install

Students should become comfortable returning these different answer-types:

```text
closed-account net force
symbolic closed-account sum
known-member vector value
known component of a member vector
combined value of several unknown members
residual vector of a partial account
open-account halt
closed-account contradiction
closed empty-set result
```

These are not interchangeable.

Particularly important distinctions are:

```text
unknown vector value of a known member
    !=
unresolved membership of a candidate

residual vector
    !=
contributing-force

zero net force
    !=
empty IFS

no member discovered
    !=
closed empty IFS
```

---

# Part I — Consuming a supplied closed IFS

## Primitive Exercise 1 — Closed-account forward sum

### Primitive operation

Use a supplied complete IFS to select the force records whose vector values must be added.

### Possible sheet

```text
TARGET: M
CONTEXT: C1

FORCE-RECORD BANK
A = 10 N right
B = 5 N left
C = 3 N right
D = 12 N right
E = 2 N left

IFS(M | C1) = {A, B, C, E}
ACCOUNT STATUS: CLOSED

TASK:
Calculate F_net(M | C1).
```

### Expected response

Taking right as positive:

$$
\mathbf F_{\mathrm{net}}
=
\operatorname{vec}(A)
+
\operatorname{vec}(B)
+
\operatorname{vec}(C)
+
\operatorname{vec}(E)
$$

$$
=
10-5+3-2
=
6\ \mathrm N\text{ right}.
$$

`D` is ignored even though its value is available.

### Symbolic variant

Some member values are deliberately unqualified:

```text
A = 10 N right
B = 5 N left
C = vec(C)
E = vec(E)
```

Then the correct answer is:

$$
\mathbf F_{\mathrm{net}}
=
5\ \mathrm N\text{ right}
+
\operatorname{vec}(C)
+
\operatorname{vec}(E).
$$

The student has completed the force-sum operation even though no final numerical vector is available.

### Key instilled behaviour

The student looks at the IFS before looking for numbers to add.

### Key instilled logic

```text
The IFS determines the domain of the sum.
The force-record bank supplies values for members in that domain.
A visible force value outside the IFS does not enter the sum.
```

### Diagnostic wrong answers

- Adding `D`: the student is treating the page as the account.
- Omitting `C` or `E` because their values are unknown: the student is confusing member existence with value qualification.
- Refusing to produce a symbolic expression: the student thinks only numerical termination counts as an answer.

---

## Primitive Exercise 2 — Recover the value of one already-known member

### Primitive operation

Use the net force and the known values of all other members to recover the vector value of one contributing-force whose membership is already established.

### Possible sheet

```text
TARGET: M
CONTEXT: C1

IFS(M | C1) = {A, B, C, E}
ACCOUNT STATUS: CLOSED
NO FURTHER MEMBERS: SUPPLIED

F_net(M | C1) = 20 N right

A = 10 N right
B = 5 N right
C = 2 N left
E = member confirmed; vector value unknown

TASK:
Determine vec(E).
```

### Expected response

$$
\operatorname{vec}(E)
=
\mathbf F_{\mathrm{net}}
-
\big(
\operatorname{vec}(A)
+
\operatorname{vec}(B)
+
\operatorname{vec}(C)
\big)
$$

$$
=20-(10+5-2)
=7\ \mathrm N\text{ right}.
$$

### Key instilled behaviour

The student checks that `E` is already a member and that the IFS is complete before using the residual to qualify `E`.

### Key instilled logic

```text
Membership can license value recovery.
Value recovery does not license membership.
```

The calculation does not discover that `E` exists. It discovers the vector value carried by the already-existing member `E`.

### Paired contrast

Give the same numerical data but replace:

```text
IFS(M | C1) = {A, B, C, E}
ACCOUNT STATUS: CLOSED
```

with:

```text
{A, B, C} ⊆ IFS(M | C1)
ACCOUNT STATUS: OPEN
```

Now `7 N right` may be calculated as a residual, but it cannot be identified as `vec(E)` or as the magnitude of one contributing-force.

### Diagnostic wrong answers

- “A new 7 N force exists”: the student has converted value recovery into member creation.
- Solving for `E` when the account is open: the student has ignored possible omitted members.
- Reporting only `7 N` with no direction: the student has changed a vector recovery into a magnitude-only answer.

---

## Primitive Exercise 3 — Membership filter before arithmetic

### Primitive operation

Separate force records that belong to the active IFS from force records that merely appear in the information bank.

### Possible sheet

The page contains a large bank:

| Record | Value | In `IFS(M|C)`? |
|---|---:|---|
| `A` | `4 N right` | student fills |
| `B` | `7 N left` | student fills |
| `C` | `2 N up` | student fills |
| `D` | `9 N down` | student fills |
| `E` | `3 N right` | student fills |

A separate card states:

```text
IFS(M | C) = {B, C, E}
```

The first task is only:

```text
Mark the members. Do not add yet.
```

A second line then asks for the sum.

### Expected response

The student marks `B`, `C`, and `E`, then writes:

$$
\mathbf F_{\mathrm{net}}
=
\operatorname{vec}(B)
+
\operatorname{vec}(C)
+
\operatorname{vec}(E).
$$

### Key instilled behaviour

The student performs an explicit domain-selection step before vector manipulation.

### Key instilled logic

```text
Value availability is not a membership condition.
The sum ranges over members, not over every vector in sight.
```

### Sheet-design note

This exercise works well with detachable cards. Students physically move member cards into an `ADD` box and leave nonmembers in the bank. The physical separation makes the domain restriction visible.

---

## Primitive Exercise 4 — Net force alone does not recover the IFS

### Primitive operation

Refuse to infer force membership from a resultant vector or one of its algebraic decompositions.

### Possible sheet

```text
F_net(M | C) = 10 N right

Candidate written decompositions:
1. 10 N right
2. 5 N right + 5 N right
3. 15 N right + 5 N left
4. 100 N right + 90 N left

TASK A:
Mark every line that is valid vector arithmetic.

TASK B:
Mark every line that has thereby been established as the physical IFS.
```

### Expected response

All four may be valid vector decompositions. None is established as the IFS from the net-force value alone.

### Key instilled behaviour

The student separates “is a correct vector identity” from “names the contributing-force members.”

### Key instilled logic

The forward map from force accounts to resultant vectors is many-to-one. Therefore:

$$
\mathbf F_{\mathrm{net}}
\not\Longrightarrow
\operatorname{IFS}.
$$

### Diagnostic wrong answer

Selecting `5 N + 5 N` as “most natural” still fails. Natural-looking decomposition is not an existence condition.

---

## Primitive Exercise 5 — Membership known versus value known

### Primitive operation

Keep separate the existence or membership status of a contributing-force and the qualification status of its vector value.

### Possible sheet

| Record or candidate | Membership status | Vector-value status |
|---|---|---|
| `A` | member | `5 N right` |
| `B` | member | unknown |
| `C` | unresolved candidate | `4 N left` supplied as its value **if admitted** |
| `D` | excluded | `9 N right` |

Tasks:

```text
1. Which symbols belong in the current admitted-member partial-sum expression?
2. Which values can be substituted now?
3. Is the account closed?
```

### Expected response

- `A` and `B` belong in the current admitted-member partial-sum expression.
- `A` can be numerically substituted.
- `B` remains as `vec(B)`.
- `C` is not admitted merely because a possible vector value is written beside it.
- `D` does not enter.
- The account remains open because `C` is unresolved.

### Key instilled behaviour

The student reads two independent columns rather than collapsing them.

### Key instilled logic

```text
Known membership + unknown value
    -> member remains in the account symbolically.

Known value + unresolved membership
    -> value does not enter the account.
```

This is one of the most important primitive distinctions in NML3.

---

## Primitive Exercise 6 — Duplicate-key rejection

### Primitive operation

Construct a set from an ordered discovery log while admitting one contributing-force at most once for one acting-object key in one target/context account.

### Possible sheet

```text
DISCOVERY LOG FOR M | C
1. key a -> contributing-force A
2. key b -> contributing-force B
3. key a -> A rediscovered
4. key c -> contributing-force C
5. key a -> same source under a new handwritten label A'

VECTOR VALUES
A = 4 N right
B = 3 N right
C = 2 N left

TASK:
Construct IFS(M | C), state its cardinality, and calculate the sum.
```

### Expected response

$$
\operatorname{IFS}(M|C)=\{A,B,C\}
$$

with cardinality `3`, and:

$$
\mathbf F_{\mathrm{net}}=4+3-2=5\ \mathrm N\text{ right}.
$$

### Key instilled behaviour

The student checks acting-object keys rather than counting presentations, labels, or repeated lines.

### Key instilled logic

```text
One acting-object instance
+ one target/context
-> zero or one contributing-force member.
```

Rediscovery is trace information, not new set membership.

### Diagnostic wrong answers

- `{A,B,A,C,A'}`: presentation count has replaced key identity.
- Adding `A` three times: the student treats the discovery log as a sum expression.

---

## Primitive Exercise 7 — Distinct equal-valued members remain distinct

### Primitive operation

Retain two contributing-force members when their acting-object keys differ even though their vector values are equal.

### Possible sheet

```text
IFS(M | C) = {A, B}
key(A) = a
key(B) = b
where a != b

vec(A) = 5 N right
vec(B) = 5 N right
```

Tasks:

```text
1. How many contributing-forces are in the IFS?
2. What is the net force?
3. May the two members be replaced by one member because their values match?
```

### Expected response

There are two members. The net force is `10 N right`. They may not be merged as members.

### Key instilled behaviour

The student counts keyed records, not distinct numerical values.

### Key instilled logic

$$
A\neq B
\quad\text{while}\quad
\operatorname{vec}(A)=\operatorname{vec}(B)
$$

is perfectly coherent.

The IFS is not a set of bare vector values.

---

## Primitive Exercise 8 — Discovery order does not order the set

### Primitive operation

Recognise different generation orders as traces of the same completed IFS.

### Possible sheet

Two groups receive the same force records but different discovery logs:

```text
GROUP 1: A, B, C, E
GROUP 2: E, C, A, B
```

Both receive a valid closer witness.

Tasks:

```text
1. Write each completed IFS.
2. Calculate each net force.
3. Is either force intrinsically the “last force” in the set?
```

### Expected response

Both completed sets are:

$$
\{A,B,C,E\}.
$$

Both sums agree. The last discovered member is a fact about one trace, not an intrinsic final element of the set.

### Key instilled behaviour

The student records discovery order separately from membership.

### Key instilled logic

```text
Generation is ordered.
The completed IFS is not.
```

---

## Primitive Exercise 9 — Cancellation does not delete membership

### Primitive operation

Simplify the vector sum without simplifying the IFS membership record.

### Possible sheet

```text
IFS(M | C) = {A, B, C}
A = 10 N right
B = 10 N left
C = 3 N up
ACCOUNT STATUS: CLOSED
```

Tasks:

```text
1. Calculate F_net.
2. Rewrite the IFS after the calculation.
3. State the force count.
```

### Expected response

$$
\mathbf F_{\mathrm{net}}=3\ \mathrm N\text{ up}.
$$

The IFS remains:

$$
\{A,B,C\},
$$

with three members.

### Key instilled behaviour

The student simplifies vector values while preserving the member ledger.

### Key instilled logic

Cancellation occurs after mapping members to vectors. It does not act backward to erase contributing-force existence.

### Strong zero variant

Use four nonzero members whose total is zero. Ask:

```text
How many forces exist in the closed account?
What is the net force?
```

The answers may be `four` and `zero` simultaneously.

---

## Primitive Exercise 10 — Closed empty IFS

### Primitive operation

Evaluate the empty force sum when emptiness has been independently supplied or certified.

### Possible sheet

```text
TARGET: M
CONTEXT: C
IFS(M | C) = {}
ACCOUNT STATUS: CLOSED
CLOSER WITNESS: VALID AT INITIAL STATE
```

The page may also show several force records belonging to other target accounts as distractors.

### Expected response

$$
\mathbf F_{\mathrm{net}}(M|C)=\mathbf 0.
$$

### Key instilled behaviour

The student treats the empty account as a successful case rather than a failed attempt to begin addition.

### Key instilled logic

```text
closed empty IFS
-> empty vector sum
-> zero net force
```

The zero vector is the result, not an IFS member.

---

## Primitive Exercise 11 — Same resultant, different force accounts

### Primitive operation

Compare closed accounts that produce the same net-force vector while retaining different membership facts.

### Possible sheet

```text
ACCOUNT P
IFS(P | C) = {A}
A = 10 N right

ACCOUNT Q
IFS(Q | C) = {B, C}
B = 15 N right
C = 5 N left
```

Tasks:

```text
1. Calculate both net forces.
2. Are the IFSs equal?
3. Does equality of net force imply equality of member count or source keys?
```

### Expected response

Both net forces are `10 N right`. The IFSs are not equal and have different cardinalities and keys.

### Key instilled behaviour

The student keeps the resultant and its physical account as different information products.

### Key instilled logic

```text
same resultant
-/->
same force account
```

This is the forward many-to-one structure in an elementary form.

---

# Part II — Residuals, inverse calculations, and correct halts

## Primitive Exercise 12 — Open-account residual is not a force

### Primitive operation

Calculate a residual from a sound partial account without converting it into a contributing-force.

### Possible sheet

```text
KNOWN MEMBERS
{A, B} ⊆ IFS(M | C)
ACCOUNT STATUS: OPEN

A = 6 N right
B = 2 N left
F_net(M | C) = 10 N right
```

Task:

```text
Calculate the residual r.
Then state exactly what r does and does not establish.
```

### Expected response

$$
\mathbf r
=
\mathbf F_{\mathrm{net}}
-
\big(\operatorname{vec}(A)+\operatorname{vec}(B)\big)
$$

$$
=10-(6-2)
=6\ \mathrm N\text{ right}.
$$

The student should write:

```text
r is the unaccounted resultant relative to this partial account.
It is not thereby the vector, magnitude, identity, or existence proof
of one contributing-force.
```

### Key instilled behaviour

The student labels the result `residual`, not `force C`.

### Key instilled logic

The residual might be:

```text
the vector sum of several omitted members
one omitted member, if that fact is independently established
an indication that a supplied value or context is wrong
```

The algebra alone does not decide among these possibilities.

---

## Primitive Exercise 13 — Matching partial sum cannot close the account

### Primitive operation

Refuse to infer completeness from zero residual.

### Possible sheet

```text
KNOWN MEMBERS
{A, B} ⊆ IFS(M | C)

A = 6 N right
B = 4 N right
F_net(M | C) = 10 N right

CANDIDATE KEY c: UNRESOLVED
ACCOUNT STATUS: OPEN
```

Tasks:

```text
1. Calculate the partial sum.
2. Calculate the residual.
3. May the account be closed?
```

### Expected response

The partial sum is `10 N right` and the residual is zero. The account may not be closed.

### Key instilled behaviour

The student looks at the unresolved and closure panels after seeing a perfect numerical match.

### Key instilled logic

An omitted nonempty collection may have zero resultant. Therefore:

```text
mismatch can defeat completeness
match cannot establish completeness
```

### Sheet-design trick

Place the “unresolved candidate” box below the arithmetic so students are tempted to stop early. Full credit requires returning to the ledger after the match.

---

## Primitive Exercise 14 — Several known members with unknown values

### Primitive operation

Recover only the combined value that the available equation determines.

### Possible sheet

```text
IFS(M | C) = {A, B, C}
ACCOUNT STATUS: CLOSED

F_net = 10 N right
A = 3 N right
B = member; value unknown
C = member; value unknown
```

### Expected response

$$
\operatorname{vec}(B)+\operatorname{vec}(C)
=
7\ \mathrm N\text{ right}.
$$

Neither `vec(B)` nor `vec(C)` is individually determined.

### Key instilled behaviour

The student stops at the strongest licensed relation instead of inventing an equal split or another arbitrary allocation.

### Key instilled logic

```text
One resultant equation can determine the sum of several unknown member values
without determining the members separately.
```

### Useful trap variants

Offer tempting answers:

```text
B = 3.5 N right, C = 3.5 N right
B = 7 N right, C = 0
B = 10 N right, C = 3 N left
```

All may satisfy the equation. None is selected without further information.

---

## Primitive Exercise 15 — Recover only a component, not the full vector

### Primitive operation

Use a closed component equation to determine one component of a known member while refusing to infer its full vector or magnitude.

### Possible sheet

```text
IFS(M | C) = {A, B}
ACCOUNT STATUS: CLOSED

F_net,x = +10 N
A_x = +4 N
B is a confirmed member; full vector unknown
```

### Expected response

$$
B_x=+6\ \mathrm N.
$$

The student must not conclude:

$$
\operatorname{vec}(B)=6\ \mathrm N\text{ right}
$$

or:

$$
|\operatorname{vec}(B)|=6\ \mathrm N.
$$

`B` may possess a nonzero `y`-component.

### Key instilled behaviour

The student preserves the type and scope of the recovered information.

### Key instilled logic

```text
component recovery
-> one component of a known member
-/-> full member vector
-/-> member magnitude
```

This is the component analogue of the valid missing-member-value exercise.

---

## Primitive Exercise 16 — Components are not additional force members

### Primitive operation

Decompose one member vector into coordinate components without multiplying the number of contributing-forces.

### Possible sheet

```text
IFS(M | C) = {A}
ACCOUNT STATUS: CLOSED
vec(A) = (3, 4) N
```

Tasks:

```text
1. Write A using x- and y-components.
2. Calculate F_net.
3. State the number of contributing-forces.
```

### Expected response

$$
\operatorname{vec}(A)
=
(3,0)\ \mathrm N+(0,4)\ \mathrm N,
$$

and:

$$
\mathbf F_{\mathrm{net}}=(3,4)\ \mathrm N.
$$

The IFS still contains one contributing-force.

### Key instilled behaviour

The student separates representational decomposition from force-account membership.

### Key instilled logic

Coordinate components are parts of a vector representation, not automatically force-instances with new acting-object keys.

---

## Primitive Exercise 17 — Closed-account mismatch: audit, do not invent

### Primitive operation

Respond to a contradiction between an independently closed account and an independently supplied net force.

### Possible sheet

```text
IFS(M | C) = {A, B}
ACCOUNT STATUS: CLOSED
CLOSER WITNESS: VALID

A = 4 N right
B = 3 N right

INDEPENDENT NET-FORCE VALUE:
F_net(M | C) = 10 N right
```

Tasks:

```text
1. Calculate the force-account sum.
2. Compare it with the independent net-force value.
3. Choose the correct response:
   a. add a new 3 N member
   b. report contradiction and audit
   c. change the IFS silently
```

### Expected response

The account sum is `7 N right`, which conflicts with the supplied net force. The correct response is contradiction or diagnostic audit.

Possible audit targets can be printed as checkboxes:

```text
[ ] target/context mismatch
[ ] net-force measurement or inference
[ ] member vector value
[ ] member existence/admission result
[ ] candidate-domain exhaustiveness
[ ] closer witness
```

### Key instilled behaviour

The student refuses to use a residual vector as an emergency membership rule.

### Key instilled logic

Once the account is independently warranted and closed, there is no free residual member `R`. A mismatch means at least one substantive record is wrong or mis-scoped.

---

## Primitive Exercise 18 — Closed versus open form of the same algebra

### Primitive operation

See that identical numerical data can license value recovery in one account and only a residual in another.

### Possible paired sheet

**Panel A:**

```text
IFS(M | C) = {A, B, E}
ACCOUNT STATUS: CLOSED
E is a confirmed member; value unknown
```

**Panel B:**

```text
{A, B} ⊆ IFS(M | C)
ACCOUNT STATUS: OPEN
No member E has been established
```

Both panels give:

```text
F_net = 12 N right
A = 5 N right
B = 3 N right
```

### Expected response

Panel A:

$$
\operatorname{vec}(E)=4\ \mathrm N\text{ right}.
$$

Panel B:

$$
\mathbf r=4\ \mathrm N\text{ right},
$$

but no `E` may be created.

### Key instilled behaviour

The student checks account status and member identity before reusing the same subtraction procedure.

### Key instilled logic

The algebraic operation is the same. Its interpretation depends on independently supplied membership and closure facts.

This exercise may be the cleanest direct comparison in the whole bank.

---

# Part III — Preparing for future existence/admission rules

## Primitive Exercise 19 — Route supplied existence-condition results

### Primitive operation

Treat a supplied condition result as determining whether the corresponding contributing-force exists and belongs to the IFS, without teaching the physical content of the condition.

### Possible sheet

```text
TARGET: M
CONTEXT: C
CANDIDATE DOMAIN: {a, b, c, d}
DOMAIN STATUS: EXHAUSTIVE

SUPPLIED EXISTENCE-CONDITION RESULTS
candidate a: SATISFIED
candidate b: FAILED
candidate c: SATISFIED
candidate d: UNRESOLVED
```

The sheet explains:

```text
If the result for key x is SATISFIED,
contributing-force W_x exists for this account.
```

Tasks:

```text
1. Move each key to ADMITTED, EXCLUDED, or UNRESOLVED.
2. Write the currently admitted member set.
3. State whether the account is closed.
```

### Expected response

```text
ADMITTED:   W_a, W_c
EXCLUDED:   b
UNRESOLVED: d
```

The currently admitted set is:

$$
\{W_a,W_c\},
$$

but the account remains open because `d` is unresolved.

### Key instilled behaviour

The student understands how later rules will plug into the IFS machinery while not pretending to know those rules yet.

### Key instilled logic

```text
existence condition satisfied
-> contributing-force exists
-> member of IFS

existence condition failed
-> no contributing-force from that key in this account

existence condition unresolved
-> no membership verdict
-> account cannot close
```

The trace may call this “admission,” but the physical logic is existence plus membership, not bureaucratic permission granted after the force already exists.

---

## Primitive Exercise 20 — Exhaustive-domain closure audit

### Primitive operation

Close an IFS only when the supplied candidate domain is exhaustive and every candidate has been resolved.

### Possible sheet

Give three small ledgers.

**Ledger A**

```text
DOMAIN EXHAUSTIVE: YES
all candidates: SATISFIED or FAILED
UNRESOLVED: none
```

**Ledger B**

```text
DOMAIN EXHAUSTIVE: YES
one candidate: UNRESOLVED
```

**Ledger C**

```text
DOMAIN EXHAUSTIVE: UNKNOWN
all listed candidates: SATISFIED or FAILED
```

Task:

```text
Mark CLOSED or OPEN and give the reason.
```

### Expected response

- Ledger A: closed.
- Ledger B: open because an existence determination is unresolved.
- Ledger C: open because the candidate domain is not certified exhaustive.

### Key instilled behaviour

The student audits both the rows and the domain header.

### Key instilled logic

```text
all listed candidates resolved
is not enough unless
all eligible candidates are represented or generally excluded.
```

Closure is a universal exhaustion claim, not the end of a finite-looking list.

---

## Primitive Exercise 21 — Closed empty by exclusion versus no successful discovery

### Primitive operation

Distinguish a successfully empty IFS from an open account with no admitted members.

### Possible three-panel sheet

**Panel A — closed empty**

```text
candidate domain exhaustive
A failed
B failed
C failed
unresolved none
closer succeeds
```

**Panel B — open no discovery**

```text
candidate domain unknown
no members admitted
no exclusions recorded
closer missing
```

**Panel C — open unresolved**

```text
candidate domain exhaustive
A failed
B unresolved
no members admitted
```

Tasks:

```text
1. Which panel licenses IFS = {}?
2. Which panel licenses F_net = 0?
3. Which panels require a halt?
```

### Expected response

Only Panel A licenses the closed empty IFS and therefore zero net force. Panels B and C remain open.

### Key instilled behaviour

The student looks for a positive absence determination rather than treating blankness as emptiness.

### Key instilled logic

```text
no member admitted
-/->
no contributing-force exists
```

The closer, not failed generation, establishes the empty case.

---

## Primitive Exercise 22 — One acting object may contribute once to each of several target accounts

### Primitive operation

Apply uniqueness locally to one fixed target/context account rather than globally across all accounts.

### Possible sheet

```text
ACTING-OBJECT KEY: g

TARGET M ACCOUNT
W_g(M | C) exists once
vec(W_g(M | C)) = 4 N down

TARGET N ACCOUNT
W_g(N | C) exists once
vec(W_g(N | C)) = 7 N down
```

Tasks:

```text
1. May g appear once in IFS(M | C)?
2. May g also appear once in IFS(N | C)?
3. May g appear twice in IFS(M | C) under two labels?
```

### Expected response

Yes, yes, no.

### Key instilled behaviour

The student indexes uniqueness to the account owner and context.

### Key instilled logic

```text
same acting-object instance
+ different target accounts
-> one contributing-force realization in each account may exist

same acting-object instance
+ same target/context account
-> not two contributing-force members
```

This prevents the slogan “one acting object, one force” from being misread as “one force anywhere in the universe.”

---

## Primitive Exercise 23 — Target and context filter

### Primitive operation

Use only force records qualified for the same target and accounting context as the active IFS.

### Possible sheet

| Record | Target | Context | Value |
|---|---|---|---:|
| `A` | `M` | `C1` | `4 N right` |
| `A` | `N` | `C1` | `7 N right` |
| `B` | `M` | `C2` | `2 N left` |
| `C` | `M` | `C1` | `3 N right` |

Active account:

```text
IFS(M | C1) = {A, C}
```

### Expected response

Use `A` qualified for `M|C1` and `C` qualified for `M|C1`. The net force is `7 N right`.

### Key instilled behaviour

The student reads the target/context columns before copying a value.

### Key instilled logic

A force label or source key is not globally value-complete. Its contribution is qualified by the target and accounting context.

### Useful extension

Give the same acting-object key in two times or states. Ask whether this is duplication. It is not duplication inside one account if the contexts differ; it is participation in different accounts.

---

## Primitive Exercise 24 — New member after purported closure

### Primitive operation

Diagnose what follows when a new contributing-force is established after an account was said to be closed.

### Possible sheet

```text
Earlier record:
IFS(M | C1) = {A, B}
STATUS: CLOSED

Later finding:
W_c(M | C1) is established under the same target and unchanged context.
```

Task:

```text
Choose the licensed conclusion:
1. harmlessly extend the correctly closed IFS
2. previous closer was invalid
3. the context must actually have changed
4. either 2 or 3
```

### Expected response

Either the previous closer was invalid or the contexts were not genuinely identical.

### Key instilled behaviour

The student treats closure as a substantive claim that can be defeated, not as a decorative label.

### Key instilled logic

A correctly closed account under unchanged conditions is not silently extendable.

---

# Part IV — Control symbols, cardinality, and trace hygiene

## Primitive Exercise 25 — Zero accumulator and closer signal are nonmembers

### Primitive operation

Separate operational control items from contributing-force members.

### Possible sheet

```text
ACCUMULATION TRACE
START: 0
ADD A
ADD B
CLOSER: NO FURTHER MEMBERS
```

Tasks:

```text
1. Write the IFS.
2. Write the exposed physical sum.
3. State the member count.
4. Does 0 or NO FURTHER MEMBERS belong to the IFS?
```

### Expected response

$$
\operatorname{IFS}(M|C)=\{A,B\}
$$

and:

$$
\mathbf F_{\mathrm{net}}
=
\operatorname{vec}(A)+\operatorname{vec}(B).
$$

There are two members. Neither the zero accumulator nor the closer signal is a contributing-force.

### Key instilled behaviour

The student reads the execution trace without converting control tokens into physical terms.

### Key instilled logic

```text
0 is the identity element of vector addition.
The closer is a termination witness.
Neither is a member of the force account.
```

---

## Primitive Exercise 26 — Count forces from keys, not from written terms or distinct values

### Primitive operation

Determine IFS cardinality from unique acting-object keys.

### Possible sheet

```text
IFS(M | C) = {A, B, C}

vec(A) = (3, 4) N
vec(B) = (3, 4) N
vec(C) = (-6, -8) N
```

A student expands all components:

$$
(3,0)+(0,4)+(3,0)+(0,4)+(-6,0)+(0,-8).
$$

Tasks:

```text
1. How many written vector terms appear after component expansion?
2. How many distinct vector values appear before expansion?
3. How many contributing-force members exist?
4. What is the net force?
```

### Expected response

- Six component terms are written.
- Two distinct bare vector values appear.
- Three contributing-force members exist.
- The net force is zero.

### Key instilled behaviour

The student returns to the key set when asked “how many forces?”

### Key instilled logic

Force count is not:

```text
written-term count
distinct-vector-value count
component count
or non-cancelling-term count
```

It is keyed IFS cardinality.

---

## Primitive Exercise 27 — Sort the four non-collapsible item types

### Primitive operation

Distinguish the target material object, contributing-force record, vector value, and existence/warrant record.

### Possible sheet

Give mixed cards:

```text
M
A
5 N right
“condition for key a satisfied”
C1
B
3 N left
“candidate b unresolved”
```

Students place them under:

```text
TARGET / CONTEXT
CONTRIBUTING-FORCE MEMBER
VECTOR VALUE
EXISTENCE OR ADMISSION RECORD
```

### Expected response

The target/context identifies the account. `A` and `B`, when admitted, are member records. `5 N right` and `3 N left` are vector values. The condition-result sentences are the records that establish, exclude, or leave unresolved membership.

### Key instilled behaviour

The student refuses category substitutions such as calling a vector value an acting object or calling a warrant another force.

### Key instilled logic

```text
material object
!= contributing-force
!= vector value
!= existence/admission determination
```

This exercise is less computational than the others, but it is primitive because every later calculation depends on the distinction.

---

# Part V — Suggested worksheet sequences

## 4.1 Minimal first sequence

A compact first sequence could be:

```text
1. Membership filter
2. Closed-account forward sum
3. Symbolic closed-account sum
4. Duplicate-key rejection
5. Distinct equal-valued members
6. Cancellation does not delete membership
7. Closed empty account
8. Net force alone does not recover the IFS
9. Recover one known member's value
10. Open residual is not a force
11. Matching partial sum cannot close
12. Supplied existence-condition routing
13. Exhaustive-domain closure audit
```

This sequence moves from direct use toward the deeper generator/closer distinction.

## 4.2 Paired contrast sheets

Several primitives are strongest when printed side by side with identical arithmetic and different account information.

### Pair A — valid missing-member recovery versus invalid invented force

```text
CLOSED IFS with E already a member
versus
OPEN partial account with no E established
```

### Pair B — closed empty versus no discovery

```text
exhaustive domain + all exclusions
versus
blank admitted list + missing closer
```

### Pair C — equal values versus duplicate key

```text
different keys, same vector -> two members
versus
same key, repeated presentation -> one member
```

### Pair D — full-vector recovery versus component recovery

```text
full vector equation -> full member vector
versus
one component equation -> one member component only
```

### Pair E — mismatch versus match

```text
nonzero residual -> current account defeated as complete
zero residual -> current account still not proven complete
```

These paired sheets are useful because the arithmetic stays nearly fixed while the legal interpretation changes.

---

## 5. Evaluator codes

A teacher or automated evaluator could classify responses with short codes.

| Code | Meaning |
|---|---|
| `M-SUM` | Correctly summed all and only supplied closed-account members |
| `M-SYM` | Correct symbolic sum returned where values were unqualified |
| `M-REC` | Correctly recovered value of an already-known member |
| `M-COMP` | Correctly recovered only the licensed component |
| `M-DUP` | Duplicate key correctly rejected |
| `M-EQV` | Distinct equal-valued members correctly retained |
| `C-OPEN` | Account correctly left open |
| `C-CLOSE` | Closure correctly recognised from exhaustive resolved domain |
| `R-ONLY` | Residual calculated but not converted into a force member |
| `R-ZERO` | Zero residual correctly refused as a closure witness |
| `H-UNDET` | Underdetermined relation returned without arbitrary split |
| `X-AUDIT` | Closed mismatch correctly returned as contradiction/audit |
| `T-INDEX` | Target/context qualification preserved |
| `CTRL` | Zero accumulator and closer signal correctly treated as nonmembers |

Common failure codes could be:

| Code | Failure |
|---|---|
| `F-PAGE` | Added every force value appearing on the page |
| `F-INVENT` | Converted residual/decomposition into a new member |
| `F-DROP` | Dropped a known member because its value was unknown or cancelled |
| `F-MERGE` | Merged different keys because vector values were equal |
| `F-DUP` | Counted one key more than once |
| `F-MATCHCLOSE` | Used numerical agreement as the closer |
| `F-BLANKEMPTY` | Treated no successful generation as closed emptiness |
| `F-COMPONENT` | Promoted a component to a separate physical force or full vector |
| `F-CONTROL` | Counted zero or the closer signal as a member |

---

## 6. Criteria of instillment

A student has begun to acquire the NML3 force-account reaction when they spontaneously ask:

```text
What is the target account?
Is this the complete IFS or only a known subset?
Does this label name a member or only a candidate?
Is the member's vector value known?
Has this acting-object key already appeared?
Are these equal vectors from different keys?
Is the candidate domain exhaustive?
Are any existence conditions unresolved?
Am I calculating a member value or merely a residual?
Does this equation determine a full vector, one component, or only a sum?
```

Strong installation is visible when the student does the following without prompting:

```text
keeps a known member in the expression when its value is unknown;
keeps a supplied vector out of the expression when membership is unresolved;
rejects duplicate rediscovery;
retains distinct equal-valued members;
refuses to close on a matching sum;
uses a residual to recover a value only after membership and closure are supplied;
returns a symbolic relation or halt rather than inventing data;
and treats later existence-condition rules as implementations of IFS membership.
```

---

## 7. What these exercises deliberately do not teach

These sheets do not yet ask the student to determine:

```text
whether a spring is active
whether contact exists
whether friction is static or kinetic
whether a gravitational model applies
whether a string is taut
whether pressure or surface tension contributes
which physical observations warrant those conclusions
```

Instead, they prepare the consequences of those later determinations.

Once later entries say:

```text
acting-object key a satisfies its contributing-force existence conditions
```

NML3 has already installed what happens next:

```text
W_a exists as a contributing-force
-> W_a is a member of IFS(M | C)
-> the key may occur once in that account
-> its vector value or rule is demanded
-> unresolved candidates prevent closure
-> after closure, all and only member vectors are summed
```

That is the socket these primitive exercises are designed to build.

---

## 8. Compact summary

The primitive exercise bank is organised around five independent questions:

```text
1. MEMBERSHIP
   Which contributing-force records exist in this IFS?

2. IDENTITY
   Which presentations share one acting-object key, and which are distinct?

3. VALUE
   What vector value or symbolic rule does each known member carry?

4. CLOSURE
   What establishes that no further member remains?

5. SUM
   What is the vector sum of all and only the closed-account members?
```

The two central inverse rules are:

```text
A residual may qualify an already-known sole missing member
when the IFS is complete.

A residual may not create or identify a contributing-force
when membership or closure is missing.
```

The final student-facing handle is:

```text
KNOW THE MEMBER.
KNOW THE ACCOUNT IS COMPLETE.
THEN A RESIDUAL MAY TELL YOU ITS VALUE.

WITHOUT THOSE FACTS,
A RESIDUAL IS ONLY A RESIDUAL.
```
