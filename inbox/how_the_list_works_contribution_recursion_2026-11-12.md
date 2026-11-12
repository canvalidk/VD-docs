# How the List Works: the Contribution Recursion

## Building a set, going through it, and what can go wrong in each

**Status:** record. Claude-authored at the user's request ("do we have enough
ideas to make a full explanation of how the list works, separating iteration
completion from set construction completion etc. etc.?" ... "Yes go ahead."),
2026-11-12, from the conversations of 11 and 12 November (Claude session in the
VD Code project, linked to Can's computer). The user's statements are marked
*(stated)*, quoted as typed, with the time sent. Everything else is
*(analysis)*.
**Not an entry.** The entry wordings below are scratch, written to state the
mechanism and to exercise the engine. Entry decisions are VD-Newton's.
**Grades:** as in the 11 November decisions record. *Ruled*: he stated it as a
decision or correction. *Agreed*: stated or accepted without being framed as a
ruling. *Forced*: Claude's derivation from rows above it. *Proposed*: Claude's
suggestion, not accepted. *Open*: not settled.
**Branch:** the mechanism is general (any law that sums over members), which
points to Core or Code; the worked case is Force-Sum, which points to
Newton-analysis. Placement is the sorter's call.
**Companions (both in `inbox/`):**
`route_to_haze_regress_and_expansion_direction_2026-11-11.md` and
`contribution_law_and_force_sum_decisions_2026-11-11.md`. This record replaces
some rows of the second; §11 lists which.

---

## 0. Short version

1. There are two jobs. **Building the set** makes a claim about the physical
   system. **Going through the set** claims nothing. They are separate, and
   the first is finished before the second starts. *(Ruled)*
2. What the first job hands to the second is a **numbered list and its
   length**. Any numbering will do, provided it is the one the length counts.
   *(Ruled)*
3. The second job is **one definition** with a condition on a counter:

   ```text
   contribution_n :=  if length(interaction-set) > n,
                         the impressed force of member n, plus contribution_n+1
                      otherwise the zero vector
   ```

   (members numbered from 0). *(Ruled, in the corrected form)*
4. Net force starts it at n = 0, with haze added once, outside. *(Ruled for
   the start; haze is from the 11 November contribution law)*
5. There are **three ways for things to end**, and they are different in
   kind: the set is closed (a claim), the counter reaches the length
   (mechanical), a step is done wrongly (a mistake with its own
   meaning-identity element). *(Ruled for the first and third; the second is
   Forced)*
6. The engine as it stands **can run this**, with two qualifications found by
   running it on 12 November: the tail's argument cannot be written `n+1`, and
   the engine records the increment as a supplied input, not as arithmetic.
   *(Tested; §9)*

---

## 1. Two jobs, kept apart

> There are 2 halting conditions to distinguish. 'There are no more elements
> to be added to the interaction set.' This is where we make a claim about the
> physical system. That is different to, we expanded past the number of
> elements in the set. That is an error to be avoided. *(stated, 11 Nov 13:06)*

> The set is entirely given at this stage. Even though most students would
> produce the addition statement at the same time as the set. *(stated, 12 Nov
> 12:43)*

| | Building the set | Going through the set |
|---|---|---|
| What it does | Decides which interactions act on the body | Adds up what they supply |
| What it claims | That nothing more is to be added (at the stated tolerance; the rest is haze) | Nothing |
| When it ends | When that claim is made | When the counter reaches the length |
| What it hands on | A numbered list and its length | A vector |
| Where it lives | Not in Force-Sum. "Somewhere else" *(stated, 11 Nov)*; Claude's placement is at or behind the interaction-set's wall *(Proposed)* | In the contribution entry |

*Ruled:* the two are distinct, and the set is complete before the adding
starts. The second point replaces a suggestion of Claude's from 11 November
(that adding could begin while the set was still being built); see §11.

*(analysis)* His remark about students names the usual source of confusion. A
student writing "spring force plus weight" is building the set and adding in
one breath, so the two jobs look like one. The dictionary separates what the
student merges. The 7 September record made the same separation ("this
traversal is exhausted" against "these are all the relevant interactions").

The word "completeness" is not used for the first job's claim *(Ruled, 11 Nov
13:06)*.

---

## 2. What is handed over

> The numbering clearly doesn't matter as long as it matches that of the
> length function. *(stated, 12 Nov 12:43)*

The adding job receives two things:

- **a numbered list** of the interactions, each with one number;
- **its length**, a number.

*Ruled:* the numbering is free, on the one condition that it is the numbering
the length counts. *(analysis)* That condition is what makes "member n" and
"length > n" talk about the same thing. If the list has L members numbered
0 to L−1, the comparison `L > n` is true exactly when a member numbered n
exists.

Two things the numbering needs that are not decided here:

- **No repeats.** A list made from a set should hold each interaction once.
  Whether two descriptions pick out the same interaction is the identity
  question, which is unruled. *(Open)*
- **Who numbers them.** A choice with no physical content. The 11 November
  probe recorded such choices as non-world inputs. Where the choice lands is
  not decided. *(Open)*

The length is where the first job's physical claim turns into arithmetic. A
length that is too small silently drops members; that is a wrong claim about
the world, made earlier, and not a fault of the adding.

---

## 3. The entry

> Ok I figured it out I think. Contribution_n := if length(interaction_set)>
> n+1, (impressed force+ contribution_n+1) Else, (0,0,0). Its not 2
> definitions, its one. *(stated, 12 Nov 12:30)*

> well yeah obviously the corrected version. I had the right idea...
> *(stated, 12 Nov 12:43)*

*Ruled:* one definition with the condition inside it, and the comparison in
its corrected form. As first typed, the comparison was `> n+1`, which drops
the last member. Run on four cases (members numbered from 0):

| Scene | True sum | `length > n+1` | `length > n` |
|---|---|---|---|
| No members (free particle) | 0 | 0 | 0 |
| One spring | 10 | 0 | 10 |
| Spring and gravity | −48/5 | 10 | −48/5 |
| Three members | −33/5 | −48/5 | −33/5 |

The mechanism, with L = 2:

```text
contribution_0 :  2 > 0, so  member 0's force + contribution_1
contribution_1 :  2 > 1, so  member 1's force + contribution_2
contribution_2 :  2 > 2 is false, so  the zero vector
```

Three things about this form *(analysis)*:

- **The counter is the whole state.** Nothing else changes from one step to
  the next. "What is left" is not a set that shrinks; it is the number n.
- **It cannot run past the end by being followed.** At n = L the entry gives
  the zero vector and calls nothing further.
- **It has three headwords**: contribution, impressed-force, and
  interaction-set (through its length and its numbered members).

This replaces the option Claude had picked on 11 November (two entries for
contribution, chosen by the form of the argument). His form needs no rule for
choosing among a headword's definitions, and its argument is a plain number.

---

## 4. Where it starts

> Then the net_force is defined in terms of contribution_0 essentially and
> contribution_n is still the name of the function. So we would have to type
> net_force:= R(contribution_n where n = 0). That way the meaningful operation
> would carry it through. *(stated, 12 Nov 12:43)*

*Ruled:* the headword is `contribution_n`, a function of the counter, and the
net-force corner starts it at n = 0.

Two notes *(analysis)*:

- **Haze.** His line gives the contribution argument only ("essentially").
  Under the contribution law of 11 November (net-force, contribution and haze
  as one triplet), the corner reads net-force := R(haze, contribution_n where
  n = 0). Haze is added once, here, and never inside the recursion.
- **Two spellings of the start.** Both were tried in the engine (§9, test 5).
  Writing the call with the number in place gives `contribution_A_0` at once.
  Writing "contribution_n where n is 0" leaves `contribution_A_n` standing
  with the instruction beside it, and the reader supplies the 0. The second is
  his wording; it makes setting n a recorded act of the reader, which is what
  "the meaningful operation would carry it through" asks for. Which spelling
  the entry uses is not decided. *(Open)*

---

## 5. The zero

> the zero vector isn't exactly required and its not the correct base case.
> Now look partly we need a zero vector. This is because addition is a binary
> operation. *(stated, 11 Nov 12:20)*

- **What it is.** The value the entry gives when no member is left to add. It
  is a result, not a test. *(Ruled that it is not the base case as a value
  test; the rest is Forced)*
- **Why it is exact.** A list of one member must have that member's force as
  its contribution. So `contribution_1` for a one-member list must change
  nothing when added. Only the exact zero vector does that. *(Forced)*
- **Why it is not haze.** Haze is not an identity for addition, and under the
  contribution law it sits outside. *(Forced)*
- **Why a zero value cannot stop the adding.** Two members can cancel. A
  running sum of zero says nothing about whether members remain. The stop is
  the counter reaching the length. *(Forced; stated in the 9 September
  two-approaches record)*

The free particle is the check: length 0, so `contribution_0` is the zero
vector at once, and net force is haze alone.

---

## 6. Three ways for things to end

| | What it is | Kind | If wrong |
|---|---|---|---|
| **The set is closed** | "There are no more elements to be added" | A claim about the physical system *(Ruled)* | A wrong claim about the world. It sits in the hypothesis set as a commitment. |
| **The counter reaches the length** | `length > n` comes out false | Mechanical *(Forced)* | Cannot be wrong in itself; it is read off two numbers. |
| **A step is done wrongly** | The comparison is misjudged, the wrong branch taken, the wrong member picked, the counter moved wrongly | A mistake *(Ruled)* | A located error at a named step (§7). |

His two conditions are the first and third rows. The second is Claude's
addition: it is the legitimate stop, and it is what the 7 September record
calls the traversal being exhausted.

**Stopping early is not an error.**

> If n < length(interaction_set), no logical issues. *(stated, 11 Nov 12:44)*

*Ruled.* A line such as net-force = haze + member 0's force + contribution_1
is true with the tail standing. *(analysis)* It is true but not yet a
prediction. To get a number the tail must be expanded, or neglected with a
bound of its own. It may not be dropped into haze, which holds only what has
no key. *(Proposed, 11 November)*

**No error message in the theory.**

> are we allowed to just say, well we only claim that in the 'correct'
> expansion, do you get something coherent. *(stated, 11 Nov 12:56)*

*Agreed.* The dictionary claims coherence for the correct expansion only.
*(analysis)* "Correct" has to mean correct step by step, never "came out
right". In the one-definition form each step's correctness is a comparison of
two numbers and a move of the counter by one, so it can be checked without
looking at the answer.

---

## 7. Mistakes, and where each is charged

> And a failure to correctly do this, reaching an error, comes with its own
> meaningful substitution error! *(stated, 12 Nov 12:33)*

*Ruled.* By the 18 October record, each recorded substitution carries one
meaning-identity element. *(analysis)* One turn of the recursion has four:

1. judging `length > n`;
2. collapsing the condition to the branch that verdict selects;
3. picking member n from the list;
4. moving n to n+1.

A slip in any of them is a mistake at a known step. Found, it colours the
trial green and the rerun is a new trial (1 November rulings).

The two families of error are now separate in the books:

| Error | Family | Example |
|---|---|---|
| The set was closed too early, or holds something that does not act | Commitment (a claim about the world) | Length given as 1 when a second interaction acts |
| A step of the adding was done wrongly | Step (a substitution that did not preserve meaning) | Taking the adding branch when `2 > 2` is false |

On 11 November the hand-trace probe could not make this separation. The case
split had to be written as a reading, which the ledger counts on the theory
side, so a misjudged split was charged to the dictionary. In the
one-definition form the split is a comparison, which belongs with the steps.
The engine run of 12 November shows these elements being recorded (§9).

---

## 8. Each member once, in any order

- **Once.** The counter takes each value from 0 to L−1 one time, and each
  value names one member. So each member is added once, provided the list has
  no repeats (§2). No count of "how many so far" is kept beyond the counter
  itself. *(Forced)*
- **Any order.** A different numbering gives a different sequence of lines and
  the same sum, because vector addition is commutative and associative. This
  ought to be stated somewhere; it is used and written nowhere. *(Proposed)*
- **Finitely many.** The length is a number. Whether the physical system has
  more interactions than the list is the first job's business, and what lies
  outside the list is haze's. No claim is made about a total. *(Proposed, 11
  November; his question whether Newton holds "an infinite number of zeros"
  was left open)*

---

## 9. What was run

### 9.1 Hand-trace recorder, 11 November (older form)

A two-member trace (spring and gravity on one body) on
`claude/hand-trace-ledger`, with the recursion written the older way: two
entries, and the tail carrying "the remaining set". Files in `inbox/`:
`contribution_law_probe_trace.md`, `handtrace_probe_contribution_law.py`.

- The answer came out (−24/5 m/s²), partial lines checked as true, and both
  orders agreed.
- Three failures passed unnoticed: a step taken past the end gave −73/5 with
  every check passing; a member re-added under a re-spelled address was
  accepted; an invented member sat beside the closed-set claim unflagged.
- Cause: the remaining set was only text in an address.

The one-definition form has not been put through the recorder. The recorder
has no comparison step yet.

### 9.2 Arithmetic check of the comparison, 12 November

The table in §3.

### 9.3 Engine, 12 November

`codex/trace-workbench-record` at `d81e9d3` (parameterized headwords and the
prediction-set layer). Script in `inbox/`:
`engine_probe_contribution_recursion.py`. Scratch entries, members numbered
from 0.

| Test | Result |
|---|---|
| 1. A contribution entry that refers to contribution | Accepted. The dictionary graph drops the self-reference: it records edges to impressed-force and to the count only, with no loop. Law detection therefore does not see the recursion. |
| 2. Tail spelled `contribution_p_n+1` | Read as the call `contribution_p_n` followed by the literal text "+1". Expanding it re-enters the same call with the same n, again and again, with no notice. |
| 3. Tail spelled with a separate letter, `contribution_p_m ... where m is the number after n` | The tail stands as `contribution_A_m`. Rewriting it by a reduce is refused ("reduction takes non-headword prose only"). Supplying `contribution_A_1` by an inject works, and the next expansion comes out with n = 1 throughout. |
| 4. Whole run, two members, forces 10 and −98/5 | Completes with −48/5 newtons. |
| 5. Starting from a net-force entry | Both spellings of §4 work as described there. |

What the run in test 4 shows:

- **The engine can carry the recursion today**, driven by hand: expand, read
  the count, supply the next call, and collapse on the way back up.
- **The increment is recorded as a supplied input.** The prediction layer
  lists, for each step, "The supplied response 'contribution_A_1' is
  appropriate for the demand 'contribution_A_m'". So moving the counter has
  its own element, as §7 requires, but it is filed with inputs and not with
  substitutions.
- **The collapse is recorded as meaning preservation.** For example: what is
  meant by "if 2 exceeds 2 then ... otherwise the zero vector" is the same as
  what is meant by "the zero vector, because 2 does not exceed 2". That is the
  element his 12:33 statement predicts.
- **The collapse happens on the way back, not on the way in.** A node can be
  reduced only when all its holes are resolved. So at each level the tail is
  expanded first and the condition is collapsed afterwards. At the last level
  the two unused holes had to be flattened (marked inert) before the node
  could be reduced to the zero vector. The reader still judges the condition
  on the way in, by choosing to expand or to flatten; the record of that
  judgement arrives later.
- **Nothing is checked.** Every element is listed as unchecked. The engine
  records that 2 was said not to exceed 2; it does not verify it.

So the answer to "would the engine have to change" is: it runs without change,
with the tail spelled as in test 3. Three things would need work for it to run
well: arithmetic in an argument (so that the entry can say n+1), a notice when
a call re-enters itself, and checking of the comparison.

---

## 10. Open

1. **Identity.** "No repeats" depends on what counts as one interaction.
2. **The numbering.** Who chooses it and where the choice lands.
3. **The first job.** Building the set is unwritten. This record describes it
   only by what it hands over and by the claim it owns.
4. **The spelling of the start** (§4) and **of the tail** (§9.3, tests 2
   and 3). The engine today forces a separate letter and a supplied call.
5. **The filing of the increment.** Supplied input (as the engine has it) or
   substitution (as §7 treats it).
6. **The graph drops the self-reference** (§9.3, test 1). Whether law
   detection should see a headword that calls itself is a Core question. It
   bears on whether this entry, impressed-force and interaction-set are
   detected as a triplet.
7. **The recorder.** No comparison step; the one-definition form is untested
   there.
8. **The tail of a partial line.** The rule "expand it or bound it" is
   proposed, not ruled.
9. **Commutativity.** Used, not written.
10. **Haze's wall**, from 11 November. It does not bear on the list.

---

## 11. What this changes in the 11 November decisions record

| Row there | Now |
|---|---|
| 3.5 (the tail carries the remaining set) | Replaced. The counter is the state (§3, §8). |
| 3.7 (adding may start before the set is closed) | Dropped. "The set is entirely given at this stage." *(Ruled)* |
| 4.2 (the base case is the empty remaining set) | Same content in counter terms: the counter has reached the length. |
| 4.7 (the check must be located in the entries; placement open) | Placed: inside the one definition. *(Ruled)* |
| 5.4 (reaching the end of a given set is mechanical) | Stands; it is the second row of §6. |
| §7, item 1 (how "the rest" is written; where the case split lives) | Settled in form (§3). What is left is spelling in the engine (§10, item 4). |
| §7, item 4 (who picks the next member) | The numbering does it, and the numbering is free. *(Ruled)* |
| Claude's pick of two entries | Withdrawn in favour of his one definition. |
| 6.2 (Force-Sum anchored on contribution) and the sentence heading §6 there | See below. |

> I no longer think its up for grabs. That was because I forgot the reasoning
> from long ago. *(stated, 12 Nov 12:43)*

This withdraws his 11 November sentence that the law's form "is still up for
grabs". *(analysis)* Claude reads it together with §4: contribution is the
function that is expanded, over impressed forces and the interaction-set, and
net-force starts it. That is the re-anchored form of row 6.2. He did not say
which earlier reasoning he meant; the 14 August abstraction-boundary note is
the likely one. The grade is **Agreed**, not Ruled, because the reading is
Claude's. The 26 August naming decision still needs its own replacement record
before any entry changes.

---

## 12. Beyond forces

*(analysis; nothing here is tested.)* Nothing in §§1 to 8 uses what a force
is. The same shape should serve any law that sums over members: one job builds
a numbered list and makes the claim that it is closed, the other is a single
definition with a counter, a comparison against the length, and a zero for the
empty case. Candidates in the Newton material are sums over the parts of a
system and over lumped bodies. Each would need its own zero (the identity of
whatever is being added) and its own account of what the first job claims.

---

## Provenance

- **Conversations:** 11 November 2026, about 11:30 to 16:30, and 12 November
  2026, 12:30 to 12:45, local time. Same session.
- **Stated:** every quotation above, as typed, with its time.
- **Analysis (Claude):** everything not quoted, the grades, and all of §9.
- **Run for this record:** the comparison table (§3); the engine probe
  (§9.3). The hand-trace probe (§9.1) was run on 11 November.
- **Read:** the companion records; `NML3_MEMBERSHIP_AND_SUMMATION_LOOPS_2026-09-07.md`
  and `NML3_INTERMEDIATE_EXPRESSION_TWO_APPROACHES_2026-09-09.md` (VD-Newton,
  `pass to VD-docs/`); `specs/2026-09-01-vd-parameterized-headwords.md` and
  `repl.py` on the engine branch.
- **Not read:** `NEWTON_ENTRY_STRUCTURE_SYNTHESIS_2026-11-08.md`, still not on
  GitHub. If it settles any point above, it governs.
- **Not checked by anyone:** nothing here has been reviewed. The engine probe
  uses scratch entries and is driven by hand; it shows what the engine accepts
  and records, not that any entry is right.
