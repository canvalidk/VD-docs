# What Is a Question? A First Run of the OP Technique

## "Is it a question?" against "Does it have an answer?"

**Status:** record. Claude-authored at Can's request (Claude offered "I can write this run up as a record"; Can: "Sure yes please.", 12 November 2026, 15:45), from the conversation of 12 November 2026 (Claude app, VD folders project). Can's statements are marked *(stated)*, quoted as typed, with the time sent. Everything else is *(analysis)* and is Claude's.
**Grades:** *Ruled*: he stated it as a decision or correction. *Agreed*: stated or accepted without being framed as a ruling. *Forced*: Claude's derivation from rows above it. *Proposed*: Claude's suggestion, not accepted. *Open*: not settled.
**Companion record:** `op_technique_overlapping_problems_2026-11-12.md`, which explains the technique and its terms (Aligning Statement, easy, interfering, built opposite, claimed mirror).
**Not sorted.** The subject is the foundation of the VD (what counts as a question), which points to Theory or Core. Placement is the sorter's call.
**Not checked against the repo.** Section 6 raises a question about the VD's foundation from Claude's general knowledge of the project, not from a fresh read of the Authority Dictionary entries.

---

## 1. The target and the pair

*(stated, 15:33)* "oh yeah I was gonna ask: "What is a question?" and try to fit it into the shape."

The target is the technique's own primitive. OP is built out of questions and never says what one is, so this run is OP turned on itself. *(analysis)*

Claude offered three candidate second questions: does it have a truth value, does it have an answer, and does asking it already require knowing the answer. *(Proposed)*

*(stated, 15:36)* "Seemingly all of them are interesting. Lets start with, is it a question? Does it have an answer?"

So the run is:

- **Set:** sentences in general, not only statements.
- **Question 1:** is it a question?
- **Question 2:** does it have an answer?

"Has an answer" is read throughout as "has a correct answer". That reading is Claude's and was not ruled on. *(Open)*

The other two pairs were not run. *(Open)*

## 2. The sweep

*(analysis)*

- **Easy.** "Is it raining?" is a question and has an answer. "It is raining" is neither.
- **Interfering.** "What is the largest prime?" looks like a question, but whether it has an answer depends on whether "there isn't one" counts as an answer. "I wonder what time it is" is not a question in form, yet it has an answer. On these, each verdict waits on the other.

## 3. The Aligning Statements

The candidates are the questions that ask about their own answer. *(analysis, Forced)*

| Statement | Try "yes" | Try "no" | Forced |
| --- | --- | --- | --- |
| "Does this question have an answer?" | Consistent | "No" would itself be an answer, so it undoes itself | Yes |
| "Does this question have no answer?" | "Yes" would itself be an answer, so it undoes itself | Consistent | No |
| "Is the answer to this question no?" | Undoes itself | Undoes itself | Nothing survives |

A fourth statement, "Is the answer to this question yes?", accepts both answers, so nothing is forced.

## 4. What the run shows

*(analysis, Forced unless marked)*

1. **A question cannot ask its way out of having an answer.** The first two statements are both forced, and both end up answered. Asking whether you have an answer is already enough to have one.
2. **"Has an answer" behaves like provability, not like truth.** "Does this have an answer?" is forced to yes, the way Henkin's sentence is forced to provable. The truth version, "Is the answer to this question yes?", forces nothing. The difference is that a "no" still counts as an answer.
3. **The third statement is where the two questions overlap.** Nothing survives, so something in the setup has to give. It is the claimed-mirror shape: being a question and having an answer were supposed to match everywhere, and this is the item built where they cannot.

## 5. The fork

*(stated, 15:38)* "So "Is the answer to this question no?" not a question? or is it neither a question or a statement?"

*(stated, 15:41)* "so the idea is, if you accept its a question, you have to accept, not all questions have answers?"

Yes, and it runs both ways. *(Forced)*

- Accept that it is a question, and not all questions have answers.
- Insist that all questions have answers, and it is not a question.

"It is a question" and "every question has an answer" cannot both be held.

The case is stronger than "What is the largest prime?". There one can count "there isn't one" as the answer. Here the same move fails: if the answer is "neither", then the answer is not "no", so the correct reply to "is the answer no?" is "no", and the loop restarts. *(Forced)*

**Can's position.** *(stated, 15:43)* "well... I kinda built the whole VD on the assumption that every question has an answer, and everything else is just giberish. Nice to see that intuition be expressed cleanly here. Welp... that was easy. I basically found what I came for."

So Can takes the second branch: every question has an answer, and "Is the answer to this question no?" is gibberish. *(Agreed. He stated it as the VD's standing assumption, not as a new ruling.)*

**What that amounts to.** *(analysis)* The run does not derive "every question has an answer". It shows that the claim is one side of a forced choice, so it has the standing of an axiom. That matches Can's own verdict on the technique (a trick of axiom strength). What the run adds is where the axiom sits and what it costs:

- The Liar-question has to be gibberish, although it looks and behaves like a question.
- Being a question then means having an answer, so a question cannot be told from gibberish by its form.

**Claude's alternative, not adopted.** *(Proposed)* Keep it as a question with no answer, on three grounds: it was handled as a question in order to classify it; "neither question nor statement" needs a third bin defined only by failure; and its having no answer is itself the answer to the next question up. On that branch a question would be something that sets a test for responses (it fixes the candidates and the condition they must meet), and having an answer would mean that some candidate passes.

## 6. Open items

1. **Typed failure covers gaps, not revenge.** *(analysis)* The VD's typed failure cases are the move "having no answer is itself an answer, one level up", and they keep "What is the largest prime?" a question. That move does not work on the Liar-question, because offering "neither" restarts the loop. So self-referential cases have to be excluded by a rule about what is well-formed. *(Open: the rule is not stated.)*
2. **The foundation cycle.** *(analysis, flagged as a question)* If the VD's foundation is itself a deliberate self-referential cycle, the well-formedness rule has to let that cycle through while blocking the Liar-question. Not checked against the repo. *(Open)*
3. **The reading of "answer".** Correct answer, or any response? Not ruled. *(Open)*
4. **The other two pairs.** "Does it have a truth value?" and "Does asking it already require knowing the answer?" were proposed and not run. *(Open)*
5. **Missing Aligning Statements in the historical pairs.** *(stated, 15:45)* "We can explore the missing aligning statements later." The pairs with only one statement are Augustine's "mistaken" pair and the four harder pairs. *(Open)*

## 7. Parked list for the technique

Can works in two modes, and during generation Claude parks critiques for delivery afterwards. These were parked during the session and delivered at its end. All are Claude's. *(Proposed)*

1. **Looseness.** The technique is kept loose so that it fits more cases. A technique that fits everything explains nothing. It needs at least one case it refuses.
2. **Selection.** Claude chose the historical cases and did the fitting, and chose cases expected to fit. A fair test is to have someone else pick cases, including ones that look like OP and are not.
3. **"Seems to force" is by feel.** Mackie's distinction between "cannot be true" and "cannot be coherently asserted" is the available discipline. Can judged it a renaming. Claude's view is that it can be skipped when hunting for Aligning Statements and is needed when stating what one establishes.
4. **Does the second batch count?** Can's criterion is that a statement is aligning if it seems to force an answer. The harder cases force something out of the setup instead. They were written up as aligning without a ruling.
5. **"All statements" and Russell.** The technique's preferred set is all statements. Russell's case is a set of everything that contains an item which breaks the questions. The same may apply to the technique's own set.
6. **September's run.** On the mass estimator the technique pinned the centre and not the shape. Today's run worked on a philosophical target. Whether OP can do work on a quantitative problem is still unshown.
7. **Novelty.** The first batch and the status claim are in Mackie (1964). The second batch is unified by Lawvere (1969). The bridge between them and the sorting by pair and shape may be new. No systematic search has been done, and Priest's *Beyond the Limits of Thought* has not been read.
8. **Sourcing.** Most historical claims rest on encyclopedia entries, several of them read only in part.

One parked item is a conjecture, not a critique: two questions overlap when one is the standard (is it true, does it exist) and the other is the access (can it be doubted, proved, conceived). Can's ruling at the time was "we don't need to know yet".
