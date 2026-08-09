# E10 Entry Writing Pass — `inertial-mass-material-object`

Status: independent drafting pass against
`ENTRY_PACKET_E10_INERTIAL_MASS_MATERIAL_OBJECT_d5.md`.
Date: 2026-08-01. Second pass at this corner;
`E10_ENTRY_WRITING_PASS_2026-07-25.md` stays live and is load-bearing below —
its §4, §5 and §11 are all used here.

**Revised twice after review. The two revisions run the same way and it is worth
saying so at the top: this pass three times removed something from the string
because it was logically entailed, and each time the entry got tighter as a
statement and worse as a trigger. §3 (substitution) and §4 (the leading
conditional) are the corrections. What survives of the first draft is mostly its
cuts of other people's material, not its cuts of its own.**

```text
E8                 9 words
E9                 8 words
E10  7/25 pass    14 words
E10  this pass    42 words
E10  candidate A 137 words
```

---

## 1. The entry

```text
inertial-mass-material-object :=

For one material-object, the positive scalar that multiplies its
inertial-acceleration-material-object to give its net-force-material-object.
If the two are nonzero and codirectional, it is the net-force magnitude divided
by the acceleration magnitude. Otherwise they do not determine it; estimate them
and it together.
```

Sentence one is the 7/25 entry, unchanged, down to the word. Sentences two and
three are this pass's contribution: twenty-eight words, one conditional each.

---

## 2. Why the fourteen words are not enough

The 7/25 pass's §4 is the strongest argument in the corpus for this entry: the
definiens states **no conditions at all** and still produces every boundary
behaviour, because `the` is a definite description and its existence and
uniqueness failures *are* the boundary cases.

The table is exact. Run it with the column heading made explicit:

| Trial (values are **the object's own** F and a) | Positive scalars taking a to F | Status |
|---|---|---|
| a ≠ 0, F codirectional | exactly one | determined |
| a = 0, F = 0 | all | indeterminate |
| every other case | none | contradiction |

Now hand the reader two values off an experiment. Generically they are not
codirectional — and by the 7/25 pass's own §11.1 result, existence of the
positive scalar *is* the direction identity, so a mismatch of any size is an
existence failure.

The table returns **contradiction** for essentially every real trial. Read
literally and correctly, the fourteen words tell an experimenter their object has
no mass, and they do it silently, because a definite description that fails to
denote does not announce which presupposition broke.

---

## 3. The substitution test

An entry is not read in the abstract. It is **substituted into**, and what the
reader confronts is the result. So the test of a definiens is how it reads with
its slots filled:

```text
For one material-object, the positive scalar that multiplies (10,0,0) to give
(5,0,1). …
```

### 3.1 Substitution destroys provenance and preserves type

`(10,0,0)` does not say whether it was measured or given. That record lived in
the slot, not the filler. So a branch keyed to **provenance** cannot fire at the
moment it is needed.

Codirectionality is a property *of the values* and survives substitution intact.
A reader looking at `(10,0,0)` and `(5,0,1)` can see it. That is what makes it a
**type check** rather than a provenance check, and a type check is the only kind
an entry can perform on what it is holding.

d5's decision 1 — *"the branch selector is explicitly exact/supplied versus
empirically measured"* — therefore does not survive. It selected on metadata the
entry never sees. §7 records what becomes of decision 2.

> **An entry may only branch on what survives substitution.** Properties of the
> values survive. Facts about their provenance do not.

### 3.2 The same test undercuts siting the inversion in the IRIL

7/25 §5 identifies the real cost of the implicit form: E8 and E9 hand you a
computation, E10 hands you a puzzle, and the reader must solve for the scalar
every time. §5.3 moves the fix to the IRIL, *"somewhere it can be enforced"*.

That is right for an automated evaluator, which runs IRIL clauses as steps. It is
wrong for a human reader in NML2.1, who has the substituted string in front of
them and not the IRIL. Under substitution, *"the positive scalar that multiplies
(10,0,0) to give (5,0,0)"* still demands an inversion, and no clause the reader
is not looking at can discharge it.

So the substitution test cuts twice: against branching on provenance, and against
exporting the inversion. Both were attempts to keep the string short by relying
on something the reader cannot see at the moment they need it.

---

## 4. Why the explicit form goes back in, and why the `if` is what makes it work

The first draft of this pass cut the exact-branch computation as redundant with
sentence one. Every outcome *is* derivable from `the` and `positive`. That is a
statement-level fact and it is the wrong test. Derivable is not performed: a
reader who must derive the magnitude quotient from a definite description will
sometimes not, and the ones who do will pay §3.2's inversion cost on every use.

But 7/25 §5.3 rejected the guarded computation for a reason that still deserves
an answer:

> *"A trailing 'when both vectors are nonzero and point in the same direction'
> inside an entry string is a subordinate clause a reader can drop — and the
> packet's own anti-misread list names that exact failure."*

That objection is correct, and it is an objection to **trailing** placement, not
to the computation. Candidate C put the condition at the end:

```text
… the magnitude of its net-force divided by the magnitude of its
inertial-acceleration, when both vectors are nonzero and point in the same
direction.
```

Skim the tail and you still have a complete, grammatical, wrong instruction.

A **leading** conditional cannot be skimmed the same way:

```text
If the two are nonzero and codirectional, it is the net-force magnitude divided
by the acceleration magnitude.
```

Drop the `if` clause and what remains — *"it is the net-force magnitude divided
by the acceleration magnitude"* — is not a sentence the reader was given. The
condition is not attached to the instruction; it **governs** it. Grammar does the
enforcing, which is the same mechanism the E8 pass credits for `its` and the 7/25
pass credits for `the`: the constraint is enforced by what the reader must do to
parse, not described alongside it.

That is the whole difference between candidate C and sentence two, and it is why
this is not a reversal of 7/25 §5.3 so much as a repair of the placement it was
objecting to.

### 4.1 `nonzero` closes the case §11.5 names

7/25 §11.5 rejects the ratio as a *definition* on two grounds. Both are answered
here, and neither is waved away.

*"A cart at rest under zero net force has an inertial mass and has no such ratio.
`0/0` is not its mass."* — `nonzero` is in the conditional precisely for this.
Zero/zero fails the condition, falls to sentence three, and is told it does not
determine the scalar. Correct verdict, reached directly rather than through a
uniqueness failure the reader has to interpret.

*"Any two non-parallel vectors divide cleanly. A definition built on the ratio
would assign an inertial mass to values that violate the law."* — the ratio is
not the definition here. Sentence one is, and it still detects law violations by
failing to denote. Sentence two is a computation licensed under a stated
condition, reached only after that condition holds. This is 7/25 §5.4's own
prescription: *a second sentence alongside the relation, never in place of it.*

### 4.2 What sentence three still has to do

`Otherwise they do not determine it` is not redundant with the routing.

The reader arriving at non-codirectional values has, by §2, already formed *no
such scalar exists*, which slides into *this object has no mass*. Sentence three
corrects that verdict before instructing: these values **do not determine** the
scalar — a fact about the values, not about the object.

Dropping it leaves `Otherwise, estimate them and it together`, which reads as a
workaround for imprecise data rather than as the correct operation. The five
words are the difference between a reader who estimates and a reader who
estimates while still believing the trial showed something about the object.

`estimate them and it together`: `them` are the object's actual quantities, which
the values in hand estimate; `it` is the scalar; `together` carries d5's
governing correction that reconciliation is internal to the determination rather
than prior to it.

---

## 5. Two things still cut from candidate A

### 5.1 The retention requirements are the other theorem

> *"Retain the original measurements, their uncertainty and discrepancy, the
> policy, and their provenance."*

Correct, and not this entry's. d5 says so itself, under *What E10 is not required
to establish*: retention rests on the separate self-confirmation argument, and
conflating the two chains "is what lets evaluator requirements migrate into the
definitional core and inflate the entry." Candidate A is that migration, in the
packet that diagnoses it.

Note this is a different kind of cut from the ones §4 reverses. The exact
computation was cut for being *entailed* — a bad reason. Retention is cut for
belonging to *another argument* — a good one. Only the second kind survived
review.

**Disposition:** cut from the string; evaluator. §8 records the dependency.

### 5.2 The circularity clause is about standing, not about mass

> *"If either result already depended on the mass being sought or on the other
> result through this relation, the outcome is only a consistency restatement."*

An answer to *what is this result worth*, not to *what is inertial mass*.

**Disposition:** cut from the string; retained in the evaluator, where d5 already
puts it as `ConsistencyRestatement`.

---

## 6. The generator, stated once

Three times in this pass I removed a clause because what it said was already
entailed:

```text
codirectional      entailed by the relation   (§11.1 identity)      -> restored
the magnitude form entailed by the definite description             -> restored
the branch itself  the reader knows their own situation             -> replaced
```

Each removal made the entry a tighter statement and a worse trigger. The common
error is treating an entry as something that must be *true and non-redundant*,
when it is something that must *make a reader do the right thing*. Entailment is
not noticing; derivability is not performance; and a reader's situation is not
visible to the string once the values are in it.

This also qualifies the 7/25 §4 virtue. *"Parallelism is never mentioned"* is
true, elegant, and costs nothing on exact values, where the reader is meant to
conclude the trial is bad. On values off an experiment the same silence produces
the fork. Elegance conditional on the inputs being exact is not elegance for the
one corner whose inputs generally are not.

---

## 7. What this does to the packet's decisions

**d5 decision 1 does not survive.** The branch is nonzero-and-codirectional, not
exact-versus-measured, per §3.1. Its motivation was sound — it wanted a selector
the reader could evaluate at the node — but it picked one that substitution
erases.

**d5 decision 2 moves rather than dies.** *"Every empirical mass determination
takes the joint estimation branch, including an aligned displayed measurement
pair"* cannot be an entry rule, because the entry cannot see that a
displayed-aligned pair was measured. It survives as an **evaluator** rule, and
the evaluator does hold the provenance slot — d5's *slots read* lists
`exact/supplied versus empirical-measurement status` explicitly.

That relocation is not a loss. The content of decision 2 is *do not lose the
uncertainty*, which is a retention requirement, and §5.1 has already sent
retention to the evaluator. Decision 2 was on the wrong side of the same line.

**Decisions 3–12 are untouched.**

---

## 8. Requirements this creates

**This wording depends on an evaluator that implements retention**, because §5.1
removed the retention clause from the string. d5's evaluator does implement it —
`JointNewtonIIFitResult` carries all of it and an incomplete result is rejected.
If those fields are ever dropped, this entry becomes unsafe and must grow the
clause back.

**It depends on the evaluator keeping the provenance slot live**, per §7. The
entry has handed provenance back; something must still hold it.

**It issues an instruction the dictionary cannot discharge.** `estimate` names an
operation outside the VD's authority, on d5's differentiation precedent. E8 does
the same with differentiation.

**And it needs a ruling on whether anaphoric short forms substitute.** Sentence
two says `the net-force magnitude`, not `its net-force-material-object`'s. If
short anaphoric forms are not headword mentions — which is the reading this pass
assumes, and the same reading that lets `them` and `it` work — then they are not
substituted, and sentence two stays readable with values in place. If they are
substituted, sentence two becomes *"the (5,0,1) magnitude divided by the
(10,0,0) magnitude"*, which is still unambiguous but reads badly. Either way the
trace is correct; the ruling affects legibility and should be made.

---

## 9. Drafting record

```text
D1  [packet d4/d5 candidate A, 137 words]
```
Rejected per §5. Its first sentence is D7 of the 7/25 pass and is kept intact.
What follows is either an evaluator requirement or a *trailing*-conditional
version of what sentence two now does with a leading one.

```text
D2  For one material-object, the positive scalar that multiplies its
    inertial-acceleration-material-object to give its net-force-material-object.
```
The 7/25 entry alone. Rejected on §2: its own §4 table returns `contradiction` on
essentially every real trial. Not a defect the 7/25 pass could have found — the
observation/measurement distinction postdates it.

```text
D3  … Where these are measured rather than given, estimate them and the scalar
    together.
```
First draft of this pass. Rejected on §3.1: the selector keys on provenance,
which substitution destroys. Recorded because the reasoning that produced it is
the generator §6 names.

```text
D4  … Values that are not codirectional do not determine it; estimate them and
    it together.
```
Second draft. Right trigger, and it closes the fork. Rejected because it leaves
the inversion in place — a reader with codirectional values still has to solve
sentence one for the scalar, every time, and §3.2 shows the IRIL cannot take that
job for a human reader. Half the entry's uses were still a puzzle.

```text
D5  … the magnitude of its net-force divided by the magnitude of its
    inertial-acceleration, when both are nonzero and codirectional.
```
Candidate C of the 7/25 pass, restated. Rejected with that pass, §4: the
condition trails, so skimming it leaves a complete and wrong instruction. This is
the version that makes the leading/trailing distinction visible.

```text
D6  … If the two are codirectional, it is the net-force magnitude divided by the
    acceleration magnitude. Otherwise they do not determine it; estimate them and
    it together.
```
One word short. Without `nonzero`, a reader may treat `0/0` as passing the
condition and compute a ratio from it — precisely the case 7/25 §11.5 raises
against ratio forms.

```text
D7  For one material-object, the positive scalar that multiplies its
    inertial-acceleration-material-object to give its net-force-material-object.
    If the two are nonzero and codirectional, it is the net-force magnitude
    divided by the acceleration magnitude. Otherwise they do not determine it;
    estimate them and it together.                                    ← chosen
```

Substitution check, the primary test:

```text
For one material-object, the positive scalar that multiplies (10,0,0) to give
(5,0,0). If the two are nonzero and codirectional, it is the net-force magnitude
divided by the acceleration magnitude. Otherwise they do not determine it;
estimate them and it together.
```
→ codirectional, so `5/10 = 0.5`. No inversion performed.

```text
… that multiplies (10,0,0) to give (5,0,1). …
```
→ not codirectional, so they do not determine it; estimate. No fork.

```text
… that multiplies (0,0,0) to give (0,0,0). …
```
→ fails `nonzero`; they do not determine it. Correct, and reached directly.

Minimality check:

- drop `nonzero` → `0/0` computes a ratio; D6;
- drop `codirectional` → the ratio applies to values that violate the law;
- move either condition to the tail → skimmable; D5;
- drop `divided by …` → the inversion returns on every codirectional use; D4;
- drop `do not determine it` → estimation reads as a workaround; §4.2;
- drop `and it` → estimation becomes preprocessing; horn two of d5's dilemma;
- drop `together` → sequential reading returns.

Nothing is removable.

---

## 10. Residual provenance ledger — sentences two and three

Sentence one's ledger is unchanged from 7/25 §8.

| Phrase | Backing |
|---|---|
| `If` (leading) | Grammar-level conditional. Governs its clause rather than qualifying it, so it cannot be skimmed off the way candidate C's trailing `when` can. §4. |
| `the two` | Anaphora to the two possessives in sentence one. |
| `nonzero` | Closes `0/0`, the case 7/25 §11.5 raises against any ratio form. §4.1. |
| `codirectional` | The type condition of the operation, and the only branch that survives substitution. §3.1. Recovers the word 7/25 §4 and this pass's first draft both cut as entailed. |
| `the net-force magnitude divided by the acceleration magnitude` | The determination, stated forward so the reader does not invert. Named in full rather than by position — `the second divided by the first` would break silently if sentence one were ever reordered. |
| `Otherwise` | Routes the complement without restating the condition. |
| `they do not determine it` | Corrects the verdict sentence one produces on such values. A fact about the values, not about the object — the anti-fork clause. §4.2. |
| `estimate them` | The reference repair: what is estimated is the object's quantities, which the values in hand estimate. |
| `and it` | Mass is an output of the estimate, not a consequence drawn afterwards. |
| `together` | d5's governing correction in one word: reconciliation is internal to the determination, not prior to it. |

No row is backed by this writer's invention. `measured`, `given`, `policy`,
`provenance`, `uncertainty`, `residual` and `underlying` appear in no row because
they appear in no clause — §3, §5.

---

## 11. Checks

- sentence one untouched, so the §2 table survives entire — yes
- legible in substituted form — yes, §9, and this is the primary check
- the branch is inspectable without provenance — yes, §3.1
- no inversion demanded on the determining branch — yes, §4
- the condition governs rather than trails — yes, §4
- `0/0` cannot reach the ratio — yes, §4.1
- the reader's wrong verdict is corrected, not merely routed around — yes, §4.2
- the ratio supplements the relation and does not replace it, so law violations
  are still detected by sentence one failing to denote — yes, §4.1
- estimation sited inside the determination — yes, `together`
- no retention, policy, provenance or circularity language — yes, and the
  dependencies are in §8
- no scale, weight, gravitational mass, amount of matter, additivity, target
  construction, persistence or constancy — yes
- estimator neither named, chosen, nor taught — yes
- no numbered entry implied for the estimation capability — yes

---

## 12. Answers, and two new questions

**d5 Q1, final wording.** Answered: the entry above. Forty-two words against
candidate A's 137. The gap is not brevity for its own sake — every cut is either
another argument's material (§5) or a placement repair (§4).

**d5 Q2, headword suffixes.** Sentences two and three mention no suffixed
headword; they use `the two`, `them`, `it`, and the short forms `net-force` and
`acceleration`. The suffix cost stays concentrated in sentence one, 141
characters of it. The tax is paid per *mention*, and an entry can triple in
length without adding a single mention — which narrows where that argument has to
happen.

**d5 Q4, result vocabulary.** The natural vocabulary is in 7/25 §10 — existence
versus uniqueness failure — but sentence three now supplies a third verdict that
is neither: *does not determine*, which is what both failures mean once the
values are understood as estimates rather than as the quantities themselves.
That is probably the ratifiable name.

**d5 Q6 and Q7.** Untouched. Evaluator questions; neither should reach the string.

**New — the substitution rule belongs to Core.** §3.1 is not about mass. Any
entry that routes on a property of its inputs faces it, and any entry tempted to
route on provenance is making E10's mistake. The whole exact/measured
architecture in the d3–d5 line should be re-read against it: right about the
world, wrong about which layer can see it.

**New — leading versus trailing conditions is a house rule waiting to be
written.** §4 is not about mass either. Any entry with a domain restriction can
put it at the front or the back, and the two are not equivalent under skimming.
If that is right, it is a general entry-writing constraint and it should sit
beside the residual/auditable split in the E8 pass rather than being rediscovered
per corner.
