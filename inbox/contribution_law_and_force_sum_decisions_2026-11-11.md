# The Contribution Law and the Force-Sum Recursion: What Was Decided on 11 November, and How Firmly

**Status:** record. Claude-authored at the user's request ("Yes make a record
on all the things we decided on (hedging certainty so there is no future
confusion.)"), 2026-11-11, from that day's conversation (Claude session in the
VD Code project, linked to Can's computer, about 11:30 to 13:15). The user's
statements are marked *(stated)*, quoted as typed, with the time they were
sent.
**Not an entry.** Nothing here is entry wording, and nothing here changes the
ratified Force-Sum names. Entry decisions are VD-Newton's.
**Branch:** this record proposes changes to the Force-Sum house, so by the
sorting test it is probably a criticism (`criticises: [force_sum]`). Placement
is the sorter's call.
**Companion:** `route_to_haze_regress_and_expansion_direction_2026-11-11.md`
(same day, in `inbox/`). That record gives the arguments for haze and for the
direction of expansion. This one lists the decisions and grades them.

---

## How to read the grades

Every row carries one grade. The grade says how much weight the row can bear.

| Grade | Meaning |
|---|---|
| **Ruled** | He stated it as a decision or as a correction. His words are quoted. |
| **Agreed** | He stated it or accepted it in conversation without framing it as a ruling. It is the working position. |
| **Forced** | Claude's derivation from rows graded above it. It holds if those rows hold and the argument is sound. Not ruled, and not checked by anyone else. |
| **Proposed** | Claude's suggestion. He has not accepted it. |
| **Open** | Raised and not settled. |
| **Withdrawn** | Said by Claude during the conversation and retracted. Listed so it is not reintroduced. |

Nothing below has been tried in a trace or in code.

---

## 1. Standing position

| # | Statement | Grade | Basis |
|---|---|---|---|
| 1.1 | The Newton entries up to the Force-Sum law are in good shape. | Ruled | "Everything we have until the Force-Sum law is pretty good." *(stated, 11:31)* |
| 1.2 | Force-Sum goes forward in the haze-and-contributions version. | Ruled | "And we'll use the haze and contributions version." *(stated, 11:31)* |
| 1.3 | One line upstream needs changing: E11 says there are "exactly two ways" to obtain net force, and haze plus contribution is a third or replaces one. | Proposed | Claude's reading of `DESIGN_2_1_DRAFT_1_ENTRIES.md`. The tension was already an open item in the hand-traced Atwood recording. It qualifies 1.1; he has not responded to it. |

---

## 2. The contribution law

| # | Statement | Grade | Basis |
|---|---|---|---|
| 2.1 | Net-force, contribution and haze form a triplet, the contribution law. Any two determine the third. | Ruled | "you agree how picking a haze and a net_force determines contribution, and vice versa and versa. Constituting a triplet? The contribution law? You like the decision? you comfortable with the direction?" *(stated, 12:11)*. He calls it "the decision". The corner wordings are not written. |
| 2.2 | Net-force is the November word. Contribution and haze are the winters, born together. | Forced | From 2.1 and law-house rules 5 and 6: net-force already has its Newton II entries, and the other two do not exist before this law. |
| 2.3 | On values alone the triplet is the free decomposition. It is a law only if haze has a wall of its own. If contribution is keyed and haze is only the leftover, haze is a definition. | Proposed | Claude, 12:11. Rests on §6 of the 1 November triplet record, which was offered and not ruled. |
| 2.4 | The tolerance is a human input, so it lands at haze's wall and not in a triplet corner. | Forced | From the wall-landing discipline (ratified, Design 3). |
| 2.5 | What haze's wall says: a bound only, a distribution, or a bound together with a bar on reproducible structure. | Open | The companion record argues for the third. He has not ruled. |
| 2.6 | Whether haze is a headword (as in 2.1) or the content of the closer wall under the 26 August names. | Agreed, in favour of the headword | 2.1 makes haze a triplet word. The alternative was listed by Claude and not taken up. No decision record replaces the 26 August one yet (see §5). |

---

## 3. The expansion

| # | Statement | Grade | Basis |
|---|---|---|---|
| 3.1 | Contribution is the side that expands. Haze does not expand inside a trace. | Ruled | First a lean: "im leaning towards contribution being expanded" *(stated, 11:54)*. Then: "Okay then the next two entries seem to be decisded. We have, contribution_n = contribution_n+1 + acting_force." *(stated, 12:15)*. Note his word "seem". The three supporting arguments are Claude's and are in the companion record. |
| 3.2 | The step: a contribution is one impressed force plus the remaining contribution. | Ruled | Same statement, 12:15. |
| 3.3 | The force in the step is `impressed-force`, the name ratified on 12 August. | Ruled | "oh yeah that's right impressed force." *(stated, 12:20)* |
| 3.4 | The number of expansion steps need not equal the number of members. Stopping early leaves a true sentence. | Ruled | "they don't need to match. This is because we already have contribution_n+1 in place. So if someone doesn't expand every element in the list, that's fine. If n < length(interaction_set), no logical issues." *(stated, 12:44)* |
| 3.5 | Nothing is added twice, because the remaining contribution carries the remaining set, and taking a member out shrinks it. The guarantee is that state, not a count. | Forced | Claude, 12:44, as the reason behind 3.4. Needs the remaining set to be an argument of the tail, which is not yet representable (§7, item 1). |
| 3.6 | A partial line is true but is not a prediction. The tail must be expanded, or neglected with a bound of its own. It may not be dropped into haze, which is for the unkeyed. | Proposed | Claude, 12:44. Follows the 13 September table's separation of named-and-neglected from haze. Not ruled. |
| 3.7 | Expansion can start before the set is closed, with the tail read as "the contribution of the remaining interactions". | Proposed | Claude, 12:44. Matches the "lazy producer and consumer" row of the 7 September record. Not ruled. |

---

## 4. The base case and the zero

| # | Statement | Grade | Basis |
|---|---|---|---|
| 4.1 | The value (0,0,0) is not the base case. A zero is still needed, because addition is a binary operation. | Ruled | "the zero vector isn't exactly required and its not the correct base case. Now look partly we need a zero vector. This is because addition is a binary operation. so we either need a zero at the start or the end or both you see?" *(stated, 12:20)*. This replaces his 12:15 suggestion "probably contribution_n = (0,0,0) or similar". |
| 4.2 | The base case is the empty remaining set. The zero vector is what the sum assigns to it. | Forced | Claude, 12:20. A remaining set that is not empty can still sum to zero, so a zero value cannot be the stopping condition. Stated in the 9 September two-approaches record. He went on from it without objecting; he did not rule on it. |
| 4.3 | That zero is the exact zero vector, with no freedom. | Forced | Claude, 12:47. A set of one interaction must have that interaction's impressed force as its contribution, so the empty set's contribution must change nothing when added. It cannot be haze, which is not an identity for addition. Depends on 2.1 keeping contribution free of haze. |
| 4.4 | Zero at the end, at the start, or both: a right fold, a left fold with an accumulator, or the invariant "net = accumulated + remaining". | Forced | Claude, 12:20. All three are in the 7 and 9 September records. |
| 4.5 | The sum may be taken in any order because vector addition is commutative as well as associative. This should be stated somewhere. | Proposed | Claude, 12:20. |
| 4.6 | The base case has to be checked at every step. | Ruled | "Oh of course, a computer would have to check the base case every iteration to see if it was met!" *(stated, 13:00)* |
| 4.7 | The check has to be located in the entries, and there are several ways to do it. | Ruled as a requirement; the placement is Open | "We actually need to locate this check somewhere in the entries. There are many ways to do this right?" *(stated, 13:02)*. See §7, item 1. |

---

## 5. Halting: three situations kept apart

| # | Statement | Grade | Basis |
|---|---|---|---|
| 5.1 | Two halting conditions are different. "There are no more elements to be added to the interaction set" is a claim about the physical system. "We expanded past the number of elements in the set" is an error to be avoided. | Ruled | "I don't think that's right. I think completeness exists somewhere else. Calling it completeness gives us many other philosophical problems. There are 2 halting conditions to distinguish. 'There are no more elements to be added to the interaction set.' This is where we make a claim about the physical system. That is different to, we expanded past the number of elements in the set. That is an error to be avoided." *(stated, 13:06)*. A correction of Claude. |
| 5.2 | The physical claim is not made inside the expansion. It "exists somewhere else". | Ruled | Same statement. He did not say where. |
| 5.3 | The word "completeness" is not to be used for the physical claim. | Ruled | Same statement. |
| 5.4 | A third situation sits between the two: reaching the end of a set one was handed. It is a fact about the list, it is the legitimate stop, and it claims nothing. | Forced | Claude, 13:06, as the middle row of a table he did not comment on. It is the 7 September record's "this traversal is exhausted". He named two conditions; this third is Claude's addition. |
| 5.5 | The physical claim lives where the set is built: on the membership side, at or behind the interaction-set's wall. | Proposed | Claude, 13:06. He said "somewhere else" and no more. |
| 5.6 | The Force-Sum expansion therefore contains no human input. It is pure entry application. | Forced | From 5.1, 5.2 and 5.4. Fits "triplet entries entail; wall entries identify". If it holds, the expansion adds no commitment members to a hypothesis set. |
| 5.7 | Going past the end needs no error message in the theory. Only the correct expansion is claimed to be coherent. | Agreed | His proposal: "are we allowed to just say, well we only claim that in the 'correct' expansion, do you get something coherent." *(stated, 12:56)*. Claude agreed, with the condition in 5.8. |
| 5.8 | "Correct" must be defined step by step (each member taken really is in the remaining set), never by the result. | Proposed | Claude, 12:56. Without it, 5.7 is the Major Logical Failure. Not ruled. |
| 5.9 | In code, going past the end is a refusal. That is where an error message belongs. | Proposed | Claude, 12:56. |

---

## 6. The form of Force-Sum

His position at 12:36: "I think this laws form is still up for grabs." *(stated)*
Everything in this section is to be read under that sentence.

| # | Statement | Grade | Basis |
|---|---|---|---|
| 6.1 | The ratified Force-Sum triplet is net-force / impressed-force / interaction-set. | Ruled, 26 August | `NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md`. It stands until a decision replaces it. Nothing said on 11 November replaces it. |
| 6.2 | With net-force anchoring the contribution law, Force-Sum would anchor on contribution: contribution / impressed-force / interaction-set. The four type-boundary points of 26 August carry over unchanged. | Proposed | Claude, 12:11 and 12:26. Follows from 2.1 if unique-November holds (R-LAW-05, graded DUBIOUS in the ledger). He has not accepted it. It would need its own decision record. |
| 6.3 | The list is not a triplet. Finding the next member is not a triplet. The base case is not a triplet: it relates two things, and by law-house rule 9 that is a definition. | Agreed | He asked each time ("Which might technically be its own triplet?", 12:15; "but then is that a triplet?", 12:44) and referred back to it as settled ("I know we said the list wouldn't be a triplet", 12:36). The answers are Claude's. |
| 6.4 | The recursion's index is the interaction-set in disguise: the step and the stop cannot be stated without the set. So the recursion is the contribution corner of 6.2, not a new law. | Proposed | Claude, 12:15. Whether 6.2 is a law or only a definition of contribution was flagged by Claude as unchecked and stays unchecked. |
| 6.5 | Force-Sum does not construct the set and does not need to know what its members are. | Ruled, 14 August | The abstraction-boundary note, adopted in `07_design_2_1/CURRENT_STATE.md`. Used here; not new. |
| 6.6 | How many members there are is settled behind the set's wall, by a membership law. | Open | His question: "that makes me think that actually, the interaction set sits further behind? ... maybe that the number or elements is determined by a law? I'm confused a little..." *(stated, 12:36)*. Claude answered yes, on the model of §22 of the 14 August note. He then resolved his own worry a different way (3.4) and did not rule on this. |
| 6.7 | A causal order for the design decisions: identity, candidate universe, member rule, closing the set, value, aggregate, net force. | Proposed | Claude, 12:36, built on the 12 August bug report's pipeline. Not ruled. |
| 6.8 | If a member carries its kind, there is no separate routing step: the impressed force is the interaction applied to the target. | Proposed | Claude, 12:36. Leans on the ratified principle that acting-objects are callables. Not ruled for this cut. |
| 6.9 | Whether Newton holds that a body has infinitely many contributions, finitely many of them nonzero. | Open | His question, 12:52: "this is the classic list out of index error. But now it seems to matter ontologically." Claude's answer, not ruled: a zero with no interaction behind it is not a contribution; what is finite is the explicit account at a tolerance; no claim is made about the total (the 9 September candidate law; Logical Consequence 23). The remark about Seeliger's paradox was from memory and not checked. |

---

## 7. What is still missing before entry text

All Claude's assessment (13:10). He replied by asking for this record and did
not dispute the list.

1. **How "the rest" is written, and where the case split lives.** One decision.
   The entry needs a headword that takes the remaining set as an argument. The
   parameterized-headwords branch handles flat atomic arguments only, and the
   7 September record says an empty-or-element dispatcher is not established.
   Three placements were listed: a conditional inside the contribution corner;
   two entries for contribution, chosen by the form of the argument; a built-in
   fold in the engine. Claude's pick is the second, which needs a Core rule for
   choosing among several definitions of one headword. After 5.1 the split is
   mechanical whichever is chosen.
2. **E11** (row 1.3).
3. **Haze's wall** (rows 2.3 to 2.5). It blocks the contribution law's wall
   only.
4. **Who picks the next member.** Any order gives the same sentence, so it can
   be a wall input. Left open by the 9 September algorithm record.

---

## 8. Withdrawn

Said by Claude on 11 November and retracted after the 13:06 correction.

| Withdrawn claim | Said at | Why |
|---|---|---|
| "Halting is a claim, not a default. 'No more members at this tolerance' is the completeness input." | 12:56 | Reaching the end of a given set claims nothing (5.4). The physical claim is made elsewhere (5.2). |
| The n + 1 answers to "is there another?" inside the expansion are n existential witnesses and one universal negative, so the generator and closer are one check asked every step. | 13:00 | Inside the expansion every answer is mechanical. The asymmetry of Logical Consequence 10 belongs to building the set. |
| The check splits into "a question to the world" and "a case split", with the question landing at the interaction-set's wall as part of the Force-Sum step. | 13:02 | The question to the world is not part of Force-Sum at all. Only the case split is. |
| The word "completeness" for the physical claim. | 12:56 to 13:02 | Row 5.3. |

One earlier statement stands and should not be read as withdrawn: the
companion record's §5 says that which interactions are explicit at a tolerance
is a modelling input that lands at a wall. That is about building the set, and
agrees with 5.2.

---

## 9. Relation to earlier records

| Record | Relation |
|---|---|
| `NML3_FORCE_SUM_TRIPLET_NAMING_DECISION_2026-08-26.md` | Stands (6.1). Row 6.2 proposes changing its first word. |
| `NML3_IMPRESSED_FORCE_TERMINOLOGY_DECISION_2026-08-12.md` | Confirmed in use (3.3). |
| `FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md` (14 August) | Its §15 and §22 are the basis of 6.5 and of Claude's answer in 6.6. |
| `DESIGN_2_1_BUG_REPORT_AGGREGATE_VS_MEMBER_CONSTRAINT.md` (12 August) | Its pipeline is the skeleton of 6.7. |
| `NML3_MEMBERSHIP_AND_SUMMATION_LOOPS_2026-09-07.md` and `NML3_INTERMEDIATE_EXPRESSION_TWO_APPROACHES_2026-09-09.md` (both in VD-Newton's `pass to VD-docs/`; not found in VD-docs) | They already contain 4.2, 4.4 and 5.4, and state them more fully. What 11 November adds: a headword for the tail (their `R(T)` was "working notation"), the anchor moving to contribution, and haze as what lies between "this traversal is exhausted" and "these are all the relevant interactions". |
| The haze records of 9 to 13 September | The companion record relates to these. Rows 2.5 and 3.6 depend on the 13 September table. |
| `triplet_minimality_and_house_count_2026-11-01.md` | Row 2.3 rests on its §6. Row 2.5 bears on its open item 1 (inequalities as peripheral entries). |
| Remainder-triplet proposal (9 September, fate open) | Its recursion is 3.2 under an older name. Row 2.1 gives the remainder a different home (contribution as a winter of a law anchored on net-force) from the one it proposed. Its fate is not ruled here. |

---

## Provenance

- **Conversation:** 2026-11-11, about 11:30 to 13:15 local time, Claude session
  in the VD Code project, linked to Can's computer.
- **Stated:** every quotation above, as typed, with its time.
- **One remark not placed in a row:** "Right and that was blocking our logic."
  *(stated, 12:26)*, said in reply to Claude's comparison of the day's results
  with the two September records. He did not say which point it referred to.
- **Analysis (Claude):** every row graded Forced or Proposed, the grades
  themselves, §7 and §8.
- **The grades are Claude's reading** of what he said. Where a row is graded
  Ruled on the strength of a question he asked ("You like the decision?") or a
  hedged phrase ("seem to be decisded"), the quotation is given so the grade
  can be checked against it. He should correct any grade that overstates him.
- **Read for this record:** the files named in §9; the companion record.
- **Not read:** `NEWTON_ENTRY_STRUCTURE_SYNTHESIS_2026-11-08.md` and
  `ATWOOD_WORKED_TRACE_2026-11-08.md`, which were not on GitHub. Their §5 and
  §8 bear on rows 1.3, 6.1 and 6.2. If the synthesis already settles any row,
  it governs.
- **Not checked by anyone:** nothing here has been reviewed, traced or run.
