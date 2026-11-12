# The OP Technique (Overlapping Problems)

**Status:** record. Markdown copy of the Claude doc "The OP Technique (Overlapping Problems)", written to `inbox/` at Can's request ("Also add the doc we built to the inbox", 12 November 2026, 15:45). Built in one session on 12 November 2026 (Claude app, VD folders project). The technique and its name are Can's. The wording, the worked tables, the historical write-ups and the comparisons with the literature are Claude's, and were offered, not ruled on, except where the text says so.
**Live copy:** https://claude.ai/artifact/SEPrGqbZJiTCQJswLZLHLk (this file is a copy of its text as it stood at the end of that session).
**Companion record:** `what_is_a_question_op_run_2026-11-12.md`, the first run of the technique on a question of Can's own.
**Not sorted.** Placement is the sorter's call.

Nov 12, 2026 · Can Valid

## What it is

The OP technique gets a firm answer out of two questions that block each other. Both questions stay fixed, and the work is to find a statement on which the pair seems to force an answer. Such a statement is called an **Aligning Statement**.

The move is old and the name is new. It was picked out of the *History of Philosophy Without Any Gaps* podcast and named Overlapping Problems, or OP, because it is OP.

It is a philosophy technique, not an exact mathematical tool. It is kept loose on purpose, so that it fits more cases.

## The setup

The technique needs three things.

- **A shared set of statements.** The interesting case is when the set holds all statements.
- **Two questions** that can be asked of any statement in the set.
- **Binary answers**, for now. Yes/no, doubt/don't doubt, true/false and similar variants all count, because each can be rewritten as a yes/no question.

Which side gets called "yes" is a free choice, so nothing depends on the labels.

When the set holds all statements, it also holds statements about the two questions themselves. Both questions can then be turned on those statements, and that is where the technique gets its reach.

## The attitude

The technique only asks what happens when answers are assigned. It never asks what the real answers are.

- It does not matter that doubt suggests truth comes in degrees.
- It does not matter that absolute truth values are hard to assign to many statements.
- The two questions do not even need to agree in principle.

So every statement starts with all four answer combinations open. The work is to see which combinations survive.

## The procedure

1. **Fix the two questions.** They do not move or get reworded during a run.
2. **Run statements through both questions** and notice how each one behaves. Statements fall into three kinds, sorted by feel.
3. **Look for the Aligning Statements.** This is the real work.

| Kind | How it behaves |
| --- | --- |
| Easy | Both answers can be assigned without trouble. |
| Interfering | The two answers get in each other's way. One cannot be settled without the other. |
| Aligning | The two questions together seem to force an answer. |

A statement is aligning as long as it seems to force an answer. One forced answer is enough; it does not have to pin both questions.

Easy and aligning are different. On an easy statement the answers *can* be assigned. On an aligning statement they *cannot be assigned otherwise*.

## Worked example: the doubt case

The classic run uses doubt and truth. It shows that "doubt everything" cannot be a secure position, without saying what truth is.

- **Question 1:** can this statement be doubted?
- **Question 2:** is this statement true?
- **Aligning Statement:** "It is possible to doubt every statement." Call it A.

A is the blanket "yes" to Question 1, written down as a statement. The set holds all statements, so A is in it, and both questions apply to A itself.

| Is A true? | Can A be doubted? | Verdict |
| --- | --- | --- |
| Yes | No | Dead. If A is true, every statement can be doubted, A included. |
| No | No | Dead. If A cannot be doubted, A is a counterexample to itself, so it is false. But once it is shown false, it is being doubted. |
| Yes | Yes | Survives. |
| No | Yes | Survives. |

What A forces:

- **Question 1 is forced to "yes".** A can be doubted, whichever way Question 2 goes. Supposing otherwise undoes itself.
- **Question 2 stays open, but both branches say something.** If A is true, the sceptic's own thesis is doubtable and can never be held as certain. If A is false, at least one statement cannot be doubted.
- **Either way, universal doubt is not a secure position.**

Question 1 is read here as "can" rather than "should", so that it matches the wording of A.

## Status: a trick, not a proof

The technique is no stronger than starting an axiomatic system by assuming a statement to be true. It only feels stronger.

In the doubt case, the forcing did not come from A alone. Each "dead" verdict used a rule that was never listed:

1. A applies to itself, and "true" means things are as A says.
2. An assignment may not contradict itself.
3. The two questions are linked: once a statement is shown false, it is being doubted.

Drop the third rule and the second row of the table survives. The assumptions are paid for by agreeing to ask the two questions at all.

That is also why the trick is so convincing. Nobody in the conversation can refuse those assumptions without leaving the conversation.

So OP does not solve the primary leap of faith, also known as Descartes's problem or the language problem. That problem is likely unsolvable. OP is still an extremely effective trick.

## Deliberately left open

Three things are undecided on purpose.

- **What makes two questions overlap.** The technique does not need to know yet.
- **Questions with more than two answers.** Only binary questions are considered for now.
- **How formal to make it.** The types can be worked out, but not at the cost of theory production.

## Historical uses, by question pair

Each group below is one pair of questions. Inside a group, different people found different Aligning Statements, and the contrast between them is the point. Pairs are kept apart unless they are clearly the same question. The first six are the well-known cases, and the last four are the harder ones.

### Can it be known? / Is it true?

Two Aligning Statements: the sceptic's own thesis, "nothing can be known", and Fitch's unknown truth.

Seneca reports that the Academic sceptics claimed to know that nothing can be known, which is the thesis caught by itself ([SEP, Ancient Skepticism](https://plato.stanford.edu/entries/skepticism-ancient/), §3.1).

Sextus Empiricus accepted the turn instead of fighting it. His sceptical formulae apply to themselves and cancel themselves along with everything else, like a fire that burns its fuel and then itself (*Outlines* 1.14–15). He also compares them to a ladder thrown away after the climb (*M* 8.481).

The statement forces the knowledge question on itself: the thesis cannot be known either. Sextus used that forced answer to remain a sceptic.

**"p is true, and nobody knows it."** This is a second Aligning Statement for the same pair. Fitch published it in 1963, and the argument first reached him in 1945 from an anonymous referee, later identified as Alonzo Church ([SEP, Fitch's Paradox of Knowability](https://plato.stanford.edu/entries/fitch-paradox/), §1).

Take any truth p that nobody knows. If the whole statement were known, p would be known, and it would also be true that nobody knows p. So the statement cannot be known, even when it is true (§2).

The statement forces the knowledge question to "no". It also breaks a claimed mirror: if every truth could be known, every truth would already be known.

**The contrast.** The sceptic gives the blanket "no" to the knowledge question, and that answer undoes itself. Fitch's statement refutes the blanket "yes". So neither blanket answer to this question survives.

The hidden rules are on the table here: knowing a conjunction means knowing each part, and what is known is true.

### Could I be mistaken about it? / Is it true?

One Aligning Statement so far: Augustine's "if I am mistaken, I am".

Augustine wrote it against the Academic sceptics and their question "what if you are deceived?" ([*City of God* XI.26](https://logoslibrary.org/augustine/city/1126.html)). Being deceived requires existing, so the question hands him one truth: *si fallor, sum*.

The statement forces the truth question. This pair arose as a reply to the knowledge pair above, and it sits next to the doubt pair below. It is kept apart because "mistaken" and "doubted" are not clearly the same question.

### Can it be doubted? / Is it true?

Two Aligning Statements, and they pin opposite questions.

**"It is possible to doubt every statement."** This is the worked example above. It forces the doubt question and leaves truth open. No historical author has been attached to it in exactly this form yet.

**"I am, I exist."** Descartes reaches it in the Second Meditation (1641). Doubting his own existence requires thinking, so the statement holds whenever he puts it forward ([SEP, Descartes' Epistemology](https://plato.stanford.edu/archives/spr2023/entries/descartes-epistemology/), §4). It forces the truth question.

**The contrast.** Across these three pairs the uses run in opposite directions. Sextus used his statement to remain a sceptic, while Augustine and Descartes used theirs to get out of scepticism.

### Is it believed? / Is it true?

Two Aligning Statements: Protagoras's own thesis, and Moore's sentence about the rain.

On its face, the argument treats Protagoras as holding that all beliefs are true. In the *Theaetetus* (171a–b), Socrates asks both questions of that thesis itself. Someone believes "not all beliefs are true", so by the thesis that belief is true, so the thesis is false ([SEP, Plato on Knowledge in the *Theaetetus*](https://plato.stanford.edu/entries/plato-theaetetus/), §6.3).

Sextus Empiricus is thought to have given the argument its name, *peritrope*, a turning back on oneself ([Wikipedia, Peritrope](https://en.wikipedia.org/wiki/Peritrope)). Commentators still disagree about what it forces. Burnyeat, Denyer and Sedley reconstruct it as a valid refutation, while McDowell and Bostock see self-defeat rather than strict contradiction.

**Burnyeat's reading.** Taken at face value, the argument attacks "every judgment is true". Plato's Protagoras holds something subtler: every judgment is true *for* the person who makes it. With that qualifier kept, the argument seems to show only that the doctrine is false for his opponents ([Burnyeat, "Protagoras and Self-Refutation in Plato's *Theaetetus*"](https://www.jstor.org/stable/2183729), pp. 173–174).

Burnyeat argues that this result is not harmless. The doctrine claims to describe everyone's judgments, so if it fails for the opponents it fails as a theory, and Protagoras must then give it up for himself too (pp. 183–188).

Protagoras has one escape, which is to say the doctrine is true only for him. Burnyeat reads Plato's image of Protagoras popping his head up and running away as exactly that: a refusal to stay in the discussion (pp. 190–193). Even then he asserts something outright, because to assert anything is to assert it as true (p. 195).

This is the status section in a single case. The forcing rests on what asserting commits one to, and the only way out is to leave the conversation.

**The contrast.** This has the same shape as the sceptic's thesis: a blanket "yes" to the first question, written as a statement, with both questions then asked of it. The outcomes differ. Blanket doubt only loses its security, while blanket belief is forced to be false.

This run also shows its hidden rule plainly. It only works if someone actually disagrees with Protagoras.

**"It is raining, but I do not believe it."** This is a second Aligning Statement for the pair. Moore presented it to the Cambridge Moral Sciences Club in 1944, and Wittgenstein was greatly excited by it (["Wittgenstein and Moore's Paradox", Cambridge University Press](https://core-prod.cambridgecore.org/core/books/wittgenstein-scepticism-and-naturalism/wittgenstein-and-moores-paradox/01289866D62561EC6A567B3934494109)).

The sentence may well be true. But if I believe all of it, then I believe it is raining, and that makes its second half false. So it cannot be both believed and true.

Moore put the point in terms of asserting the sentence. It is read here in terms of believing it, to fit the pair.

**The contrast with Protagoras.** Protagoras claims that belief guarantees truth everywhere. Moore's sentence is a statement where believing it guarantees it is false. Plato refuted the blanket claim with the claim itself, and Moore's sentence refutes it with one remark about the weather.

The hidden rules here: believing a conjunction means believing each part, and the sentence has to be in the first person and the present tense.

### Can it be conceived? / Does it exist?

This pair shows the trick being caught almost as soon as it was played.

Anselm's *Proslogion* (1078) takes "a being than which no greater can be conceived". If it existed only in the understanding, a greater one could be conceived, namely one that also exists in reality. That is absurd, so the being exists in reality ([SEP, Ontological Arguments](https://plato.stanford.edu/archives/spr2006/entries/ontological-arguments/), §1).

Gaunilo, a Benedictine monk, replied soon after in his "Reply on Behalf of the Fool". He kept both questions and changed the statement to "that island than which no greater can be thought". The same steps then force the island to exist, which is absurd ([Encyclopedia.com, Gaunilo](https://www.encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/gaunilo-fl-11th-century)).

**The contrast.** Gaunilo did not attack a premise. He found a second Aligning Statement for the same pair and let the forced answer speak for itself.

The usual defence of Anselm is that a greatest conceivable island is incoherent, because a greater one can always be imagined. The SEP entry treats parodies like this as a real objection, and it concludes that none of the known ontological arguments should persuade a non-theist.

One stretch to note: the set here holds descriptions of things rather than statements.

### Is it provable? / Is it true?

In this pair the two Aligning Statements are mirror images, and the forced answers are not.

Gödel (1931) built a sentence that, loosely, "says of itself that it is not provable" in a formal system F. If F is consistent, F does not prove it. Read the right way, the sentence is then true, so it is true and unprovable ([SEP, Gödel's Incompleteness Theorems](https://plato.stanford.edu/entries/goedel-incompleteness/), §2.5).

Henkin asked the mirror question in 1952: what about a sentence that asserts its own provability? Löb answered in 1955 that it is provable. More generally, if F proves "if A is provable, then A", then F already proves A (same entry, §4.3).

**The contrast.** "I am not provable" comes out unprovable and true. "I am provable" comes out provable and true. Flipping the statement flipped only one of the two answers.

This is also the pair where the hidden rules got written down. Gödel's result needs F to be consistent. Kreisel (1953) pointed out that the answer to Henkin's question depends on how provability is expressed, and Löb's proof states the conditions it relies on.

The ancestor is the Liar, "this sentence is false". With truth on both sides no assignment survives, so nothing is forced. According to the SEP entry (§5), Gödel reached incompleteness after running into the Liar in 1930. Swapping one "true" for "provable" turned a paradox into a theorem.

### The harder cases: when no answer survives

In the pairs above, the Aligning Statement forces an answer to one of the two questions. In the four pairs below it does something stronger. No assignment survives at all, so the forced answer lands on the setup: something assumed to exist cannot exist.

These cases share a build. The second question is not given separately. It is made from the first, in one of two ways.

- **Built opposite.** Question 2 is defined to give the opposite of Question 1 (Cantor, Russell). The Aligning Statement is the very thing Question 2 defines, and it gets forced out of the set.
- **Claimed mirror.** Question 2 is claimed to agree with Question 1 everywhere (Tarski, Turing). An item is built on which the two must differ, so no such mirror exists.

Gödel's sentence above is the claimed-mirror kind as well. It breaks the claim that provability matches truth everywhere.

The sets change too. They hold list positions, sets, sentences and machines, not statements in general.

### Is the diagonal digit a 1? / Is the new sequence's digit a 1?

Cantor published this argument in 1891. Take any list that claims to hold every infinite sequence of 0s and 1s. Build a new sequence by flipping the n-th digit of the n-th sequence, for every n ([Wikipedia, Cantor's diagonal argument](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument)).

In OP terms, the set is the positions in the list. Question 1 asks about the n-th digit of the n-th sequence. Question 2 asks about the n-th digit of the new sequence, and it is built to give the opposite answer.

The Aligning Statement is the position where the new sequence would sit. There the two questions are one question, yet their answers must differ. So the new sequence has no position, and no such list is complete.

### Is it a member of itself? / Is it a member of R?

Russell found this around 1901 while studying Cantor's proof, and wrote to Frege about it on 16 June 1902 ([SEP, Russell's Paradox](https://plato.stanford.edu/entries/russell-paradox/), §2). He took Cantor's build and removed the list. The set is now all sets, and R is the set of all sets that are not members of themselves.

Most items are easy. The set of all teacups is not a teacup, so it is not a member of itself, and it is a member of R.

The Aligning Statement is R itself. "Is R a member of itself?" and "Is R a member of R?" are one question, and R's definition demands opposite answers. Either answer yields its opposite.

**The contrast.** Cantor's forced answer was welcome: the list is incomplete. Russell's was a crisis, because the thing forced out was a principle people relied on, that any condition picks out a set. Frege conceded in an appendix that his Basic Law V was false.

The repair makes Russell look like Cantor again. Under Zermelo's rule a set must be carved out of an existing set B. The Russell-style set carved from B exists, but it cannot be a member of B, so something is always missing from B (§3–4).

The SEP entry adds that the reasoning is pure logic (§5). Nothing can be related to exactly those things that are not related to themselves. That is the built-opposite build stated as a law.

### Is it true? / Does the truth predicate say so?

Suppose a language could define its own truth predicate: a formula that applies to exactly the true sentences of that language. That is a claimed mirror, where Question 2 always agrees with Question 1.

Tarski's theorem says no such predicate exists. The proof builds a Liar sentence out of the supposed predicate, one that says the predicate does not apply to it ([SEP, Gödel's Incompleteness Theorems](https://plato.stanford.edu/entries/goedel-incompleteness/), §4.1). On that sentence the two questions must disagree.

So defining truth for a language needs resources beyond that language ([SEP, Axiomatic Theories of Truth](https://plato.stanford.edu/entries/truth-axiomatic/), §1, citing Tarski 1935).

**The contrast.** The Aligning Statement is the Liar again. In the ancient version there was nothing to blame, so it stayed a paradox. Here there is an assumption to blame, so it became a theorem.

### Does it halt? / Does the decider say it halts?

Suppose a decider: a program that says correctly, for every program and input, whether that program halts. That is a claimed mirror again.

Build a program D that asks the decider about a program run on its own text, then does the opposite of the verdict. Now ask about D run on D. Whatever the decider says, D does the other thing, so no decider exists.

The attribution needs care. Turing's 1936 paper does not state the halting problem. It proves a related problem undecidable, the "circle-free" problem, by a diagonal argument like Cantor's. Hamkins and Nenu credit the clear statement of the halting problem to Martin Davis (1958) and the self-referential argument to Kleene (1952) ([Hamkins and Nenu, "Did Turing prove the undecidability of the halting problem?"](https://ar5iv.labs.arxiv.org/html/2407.00680)).

**The contrast.** This pair has the same shape as provable and true: a fact, and a mechanical verdict on that fact. Gödel's Aligning Statement talks about its own verdict. Turing's acts on it, because D reads the verdict and does the opposite.

### What the two batches show

Ten pairs so far. Four patterns run across them, followed by a note on prior art.

**Two kinds of forced answer.** In the first six pairs the Aligning Statement forces an answer about the statement. In the last four it forces something out of the setup: a list position, a set, a truth predicate, a decider. Fitch's statement does both at once.

**The hidden rule and the blamed assumption play the same role.** In the first batch, every run leaned on a rule from outside its statement:

- Being deceived requires existing, and doubting requires thinking.
- Someone actually disagrees with Protagoras.
- Existing in reality is greater than existing only in the understanding.
- The formal system is consistent.

In the second batch the outside rule is stated up front as an assumption, and the Aligning Statement refutes it. On this reading, a proof by contradiction is the trick run with its assumption on the table.

**Shapes of Aligning Statement recur across pairs.**

- **A blanket answer turned on itself:** "nothing can be known", "every statement can be doubted", "all beliefs are true".
- **Asking the first question supplies the second answer:** "if I am mistaken, I am" and "I am, I exist".
- **A statement about its own answer:** "I am not provable", "I am provable", and the Liar.
- **A truth that denies its own first answer:** "it is raining, but I do not believe it" and "p is true, and nobody knows it".
- **An item that does the opposite of its own verdict:** Cantor's new sequence, Russell's R, the program D.

So there may be two useful ways to sort the examples: by question pair, and by the shape of the Aligning Statement.

**Later statements answer earlier ones.** Augustine wrote against the Academics, Gaunilo against Anselm, and Henkin's question mirrors Gödel's sentence. Russell found his case while studying Cantor's.

**Prior art for the second batch.** Lawvere (1969) showed that Cantor's theorem, Russell's paradox, Tarski's theorem and Gödel's first theorem follow one diagonal scheme. Yanofsky (2003) restated the scheme in plain set terms and covers Turing's halting problem too ([Yanofsky, "A Universal Approach to Self-Referential Paradoxes, Incompleteness and Fixed Points"](https://arxiv.org/pdf/math/0305282)).

Yanofsky's moral is that "there will be trouble when things deal with their own properties". OP may turn out to be the loose, philosophical version of that scheme, one that also reaches the first batch.

## Neighbouring ideas

Existing work covers parts of the technique. None of the items below sorts cases by question pair. No systematic search for that sorting has been done yet, so its novelty is unverified.

- **Self-refutation, classified by mechanism.** Mackie (1964) separates pragmatic from absolute self-refutation. Castagnoli argues that the ancient arguments aimed to show a thesis untenable in debate, not to settle its truth value ([Castagnoli, "Everything is true, everything is false"](https://durham-repository.worktribe.com/OutputFile/1535396)). That matches the status section above.
- **Performative contradiction.** Habermas and Apel coined the term for a statement whose making presupposes what it denies. They credit Hintikka's 1962 paper on the cogito with the first elaboration ([Wikipedia, Performative contradiction](https://en.wikipedia.org/wiki/Performative_contradiction)). This is the shape where asking the first question supplies the second answer.
- **Priest's Inclosure Schema.** In *Beyond the Limits of Thought*, Priest claims that one schema captures all the paradoxes of self-reference. One objection is that the schema captures only form, so it cannot tell a paradox from a proof by contradiction ([M-Phi blog, "Two objections to Priest's Inclosure Schema"](https://m-phi.blogspot.com/2013/04/two-objections-to-priests-inclosure.html)). This document draws that same line between the Liar and Tarski.
- **Lawvere and Yanofsky.** The formal scheme for the second batch, described above.

### Closest neighbour: Mackie (1964)

Mackie's paper has now been read in full. It anticipates more of this document than the secondary accounts suggested, including the status claim.

**His frame.** Let d be any operator on statements: "I am saying that", "it can be proved that", "Smith believes that". Mackie studies the statement "nothing is d" and what happens when d is applied to it ([Mackie, "Self-Refutation: A Formal Analysis"](https://www.jstor.org/stable/2955461), pp. 193–197). In OP terms, d is the first question and truth is the second. He credits the technique to Prior (1961) and the topic to Passmore (1961).

He finds four types, sorted by the rule that links d to truth. These are this document's hidden rules, classified.

| Type | Rule on d | What follows | His example |
| --- | --- | --- | --- |
| Pragmatic | None; holds for any d | If d is applied to "nothing is d", then "nothing is d" is false | Writing "I am not writing" |
| Absolute, first kind | Truth-entailing: d holds only of truths | d cannot hold of "nothing is d" | "It can be proved that nothing can be proved" |
| Absolute, second kind | Strictly prefixable: d holds of every truth | "Nothing is d" is false | "There are no truths" |
| Operational | Weakly prefixable: asserting a statement commits one to asserting d of it | "Nothing is d" may be true, but cannot be coherently asserted | "I believe nothing" |

**What he already has.**

- **The cogito.** "I am not thinking" is operational: it cannot be coherently asserted, yet it may be true. Descartes went wrong by treating it as impossible outright (p. 198).
- **Conceiving and existing.** Berkeley's "a tree existing unconceived" gets the same verdict. Nobody can coherently assert of a named thing that it exists unconceived, but "some things exist unconceived" is fine (pp. 200–202).
- **A Fitch-like statement.** "There are truths I do not know" is fine. "That-x is a truth I do not know" cannot be coherently asserted (p. 200).
- **Scepticism.** "I know nothing" is operational on the ordinary sense of "know", and not self-refuting at all if "know" means "know for certain". "Nothing can be proved" can be coherently held (pp. 198–199).
- **Moore's sentence**, in a footnote (p. 196).
- **The status claim.** Self-refutation offers no special way to establish positive conclusions. The first absolute kind shows only that "we are merely avoiding logical contradictions". The interesting cases are operational, so they mark limits on what can be coherently asserted, not necessary truths (p. 203).

He also agrees with Passmore that arguing from self-refutation to positive conclusions is reminiscent of the ontological argument (p. 199).

**What he does not have.**

- The Liar, Gödel's sentence, or any of the diagonal cases.
- The blanket "yes" shape, such as "everything is true".
- Statements that affirm d of themselves, such as Henkin's.
- The comparison of rival Aligning Statements across history, such as Gaunilo against Anselm.

So the first batch of this document is largely Mackie's territory, status section included. What this document adds is narrower: the bridge from his cases to the second batch, the sorting by pair and by shape, and the line between paradox and theorem.

## Sources

Pages opened on 12 November 2026. The primary texts are cited through these pages, not read directly, except Augustine, Mackie and Burnyeat.

- [Ancient Skepticism](https://plato.stanford.edu/entries/skepticism-ancient/), Stanford Encyclopedia of Philosophy. Seneca on the Academics; Sextus on self-cancelling formulae.
- [Fitch's Paradox of Knowability](https://plato.stanford.edu/entries/fitch-paradox/), Stanford Encyclopedia of Philosophy.
- [Augustine, *City of God* XI.26](https://logoslibrary.org/augustine/city/1126.html), translated by Marcus Dods.
- [Descartes' Epistemology](https://plato.stanford.edu/archives/spr2023/entries/descartes-epistemology/), Stanford Encyclopedia of Philosophy, Spring 2023 archive.
- [Plato on Knowledge in the *Theaetetus*](https://plato.stanford.edu/entries/plato-theaetetus/), Stanford Encyclopedia of Philosophy.
- [Peritrope](https://en.wikipedia.org/wiki/Peritrope), Wikipedia. Used only for the name and its attribution to Sextus.
- ["Wittgenstein and Moore's Paradox"](https://core-prod.cambridgecore.org/core/books/wittgenstein-scepticism-and-naturalism/wittgenstein-and-moores-paradox/01289866D62561EC6A567B3934494109), chapter summary, Cambridge University Press.
- [Ontological Arguments](https://plato.stanford.edu/archives/spr2006/entries/ontological-arguments/), Stanford Encyclopedia of Philosophy, Spring 2006 archive.
- [Gaunilo](https://www.encyclopedia.com/humanities/encyclopedias-almanacs-transcripts-and-maps/gaunilo-fl-11th-century), Encyclopedia.com.
- [Gödel's Incompleteness Theorems](https://plato.stanford.edu/entries/goedel-incompleteness/), Stanford Encyclopedia of Philosophy. Also used for Tarski's theorem.
- [Cantor's diagonal argument](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument), Wikipedia.
- [Russell's Paradox](https://plato.stanford.edu/entries/russell-paradox/), Stanford Encyclopedia of Philosophy.
- [Axiomatic Theories of Truth](https://plato.stanford.edu/entries/truth-axiomatic/), Stanford Encyclopedia of Philosophy.
- [Hamkins and Nenu, "Did Turing prove the undecidability of the halting problem?"](https://ar5iv.labs.arxiv.org/html/2407.00680), arXiv 2407.00680.
- [Yanofsky, "A Universal Approach to Self-Referential Paradoxes, Incompleteness and Fixed Points"](https://arxiv.org/pdf/math/0305282), *Bulletin of Symbolic Logic* 9(3), 2003.
- [Castagnoli, "Everything is true, everything is false: self-refutation arguments from Democritus to Augustine"](https://durham-repository.worktribe.com/OutputFile/1535396), Durham repository copy. Pages 11–22 read directly.
- [Performative contradiction](https://en.wikipedia.org/wiki/Performative_contradiction), Wikipedia.
- ["Two objections to Priest's Inclosure Schema"](https://m-phi.blogspot.com/2013/04/two-objections-to-priests-inclosure.html), M-Phi blog, 2013.
- [Brandon, "Quantifiers and the Pursuit of Truth"](https://global.uwi.edu/sites/default/files/bnccde/epb/quantifiers.html), *Educational Philosophy and Theory* 14, 1982. Used for its account of Mackie (1964).
- [Mackie, "Self-Refutation: A Formal Analysis"](https://www.jstor.org/stable/2955461), *Philosophical Quarterly* 14 (1964), pp. 193–203. Read in full.
- [Burnyeat, "Protagoras and Self-Refutation in Plato's *Theaetetus*"](https://www.jstor.org/stable/2183729), *Philosophical Review* 85 (1976), pp. 172–195. Read in full.
