# Theories, belief, and what a theory might be

Working notes from a conversation on 21–22 September 2026. The argument is Can's; the restatements, literature hooks and objections were supplied in discussion and are marked as such. None of the references have been checked against primary sources yet.

---

## 1. Belief flows to generators, not to hypotheses

A theory emits hypotheses. A hypothesis is a string: "the cart will stop here."

When the cart stops there, the hypothesis was correct, but it gains nothing. It is now a sentence about the past, with nothing to say about tomorrow. Whatever carries forward has to live in the thing that produced it. Confirmation does not reward the hypothesis; it flows *through* the hypothesis back to its source, and the source issues the next prediction.

So the mechanism of science has an understated second half: not "hypothesis → test," but "hypothesis → test → credit returned to the generator." That back-flow is the part nobody writes down.

**Formal handle.** This is not a Markov chain over events. Yesterday's cart and tomorrow's cart never touch; they connect only through the theory. The structure is a fork (theory → prediction 1, theory → prediction 2): predictions are conditionally independent given the theory (Reichenbach's screening-off). Two Markov facts hide inside it: belief in the theory updates as a Markov process, and the whole thing is a hidden Markov model whose hidden state never changes. De Finetti's representation theorem says almost exactly this sentence: treat observations as exchangeable and you are committed to a fixed hidden parameter through which all learning about the future passes.

## 2. A theory is a function, not a track record

Induction, on this picture, is itself a generator, and a degenerate one. Its signature is `history → string`: it hands back what it was last given. A real theory has signature `(question, situation) → string`.

The two can agree on every output produced so far and still be different functions. You only believe iron will melt at the same temperature again because the theory says the relevant inputs are unchanged, and *judging that the situation is unchanged is itself something the theory does*. Bare induction cannot see that the situation changed. Ask it "when will the cart stop?" and it returns "the melting point of iron is 1500," because that is the last string it holds. Well-formed output, no connection to the question, and no way to notice.

This explains the apparent success of induction. It is only ever scored on trials where the question is repeated and the world has not moved. On that subset, "say the last thing again" coincides with the right answer every time. Its record is a fact about the exam, not the candidate.

**Formal handles.** Extensional versus intensional equality of functions. Lookup table versus rule: induction is a partial function defined only on visited situations; a theory is a total one over its declared scope. Goodman's new riddle (grue) is the same point: past agreement cannot separate hypotheses that diverge later. The meteorologists' persistence forecast is this object in professional use, and it is the baseline every real model is scored against.

**Consequence.** To believe a theory is to believe a particular function, including what it does on inputs nobody has tried yet.

## 3. Belief is enforced by exploitation

Once strings become reliable enough to steer behaviour, organisms come under selection for which strings they keep. Each string acquires a weight: belief.

The last ingredient is discipline. If you act on your strings *reliably*, then a string that makes you lose reliably is no longer a private inefficiency; it is a standing offer. Anyone who finds the losing input can bet against you repeatedly and take everything. So a reliably wrong string is not merely unhelpful but fatal, and it has to go. Pressure of that kind, applied long enough, looks like science.

**Formal handles.** This is the Dutch book argument (Ramsey 1926, de Finetti 1937): belief *is* the odds you would accept, and incoherent odds can be exploited for sure loss. Shafer and Vovk rebuilt probability on "no betting strategy gets rich against it." Popper's "we let our theories die in our stead"; Campbell's evolutionary epistemology.

Two structural observations. First, the scoreboard from §1 is not an extra mechanism: it is other players, and the back-flow of credit is a market. Second, exploitation only works against a *fixed* procedure. Committing to a fixed, public method buys trust and costs exposure: every input where it loses is now a hole someone can find. "Has no losing input anywhere" becomes a survival condition for a fixed method.

## 4. The fork: two ways to repair a failed string

When a string fails somewhere, two repairs are available.

- **A.** Rewrite the string so it is right, and go on following it faithfully.
- **B.** Leave the string alone and learn, as a matter of skill, when not to follow it.

Both close the hole a bookie could exploit. If survival is the only standard, selection is indifferent. The claim is that there is a higher standard by which A beats B.

B is how physics is mostly practised. The textbook says m = F/a; the competent experimentalist knows not to use it when the acceleration is lost in noise. That knowledge is real, reliable, and written nowhere. The literature of B: Polanyi on tacit knowledge, Kuhn on learning through exemplars, Collins on experiments that could not be replicated from the paper alone.

But under B the practitioner is running string *plus* judgement, and the judgement is also a function: given a situation it reliably says follow or don't. If experts handle every case consistently, a total procedure already exists. It is split in two, with half written and half living in heads, unversioned and unauditable. B is A with part of the code kept off the books.

## 5. The argument assembled

1. Belief flows to generators.
2. Generators are functions, believed at inputs not yet tried.
3. Fixed procedures persist only if they have no reliably losing input.
4. A failed string is rewritten, or kept with unwritten judgement.
5. Newtonian mechanics has persisted, including at inputs where its written text fails (m = F/a is undefined at 0/0, misleading in noise), and nobody bankrupts physicists there. So practitioners already execute something total and unexploitable at those inputs. It exists, because it is being run.
6. By (1), credit belongs to whatever generated the winning outputs, which was never the textbook alone.

**Conclusion.** "Newtonian mechanics," meaning the thing the evidence actually supports, is the complete function, of which the textbook is a partial transcription. "What is the correct text?" is then well-posed: the text which, followed faithfully with no judgement added, reproduces the practice. "What is mass?" asks for mass's entry in that text. The question is descriptive, not prescriptive: not what physicists should do, but what they have believed all along. The VD mass estimator is one candidate for one entry; the argument stands even if the candidate falls.

## 6. The possession argument

Objection raised in discussion: the estimator is built on F* = m a*, so it presupposes an exact mass, and at 0/0 it returns a sensor ratio that "fails to reach the Sun's real mass."

Can's reply: *how do you know?* Every mass anyone has ever held is a number with an uncertainty, produced by some procedure. Nobody has ever possessed an exact mass to hold an estimate against. "The Sun's mass is 2×10³⁰ kg" is one estimate compared with another and called the truth. The "real mass behind the estimates" is assumed, not accessible.

This landed. It also changes the reading of the 0/0 case: "50 kg with an unbounded compatibility set" and "2×10³⁰ kg, tightly" do not conflict; the second lies inside the first. The output was not wrong, it was uninformative, and it said so.

What it does not win: everyone has *claimed* exact masses (the argument is about possession, not claims); the estimator's own likelihood quantifies over true values, so the exact concept is still load-bearing inside the text as a bound variable; and "always a scalar plus uncertainty" does not say which one, so the demand that procedures cohere still has to do the work "true value" used to do.

**Agreed thesis.** Mass, as anyone has ever held it, is a scalar with an uncertainty. The exact m is a variable the theory quantifies over and that no trace ever contains. A definition that stops at the exact scalar is half a definition. Literature on Can's side: Bridgman, the GUM, van Fraassen, Chang.

## 7. What a theory might be like, on this picture

- A total function from (question, situation) to strings, believed at untried inputs.
- Written down in full, including the passage from noisy readings to the theory's quantities, because that passage is where practice currently keeps its unwritten half.
- Fixed before the data arrive, so that it can be relied on and therefore exploited, and therefore tested.
- Carrying the reader's "that's ridiculous" inside the method as a declared branch (the compatibility set, the `Nothing` return), not in the experimenter's head.
- Returning, for every quantity, an estimate with its uncertainty, because that is the only form in which any quantity has ever been held.

## 8. Standing objections (pressure list)

1. **Step 5 is the weak joint.** At 0/0 practitioners *abstain*, and abstention is unexploitable. Survival supports "the complete text says unidentified here" at least as well as a positive number. Deeper: there is no bookie who knows better at 0/0, so no selection pressure there at all. A gap can persist because it is harmless, not because it is secretly filled.
2. **Step 2 turns on the conclusion.** Any finite record of practice is matched by indefinitely many total functions that diverge on unmet cases (Kripke's Wittgenstein: plus versus quus). "The function they've been running all along" may have no fact of the matter. The defensible version is Carnap's explication, which is partly a proposal.
3. **Factorisation.** Practice keeps mechanics and error analysis as separate modules, and the same inference serves every quantity in every theory. Why does the noisy-data handling belong under "mass" rather than beside it?
4. **No text is judgement-free.** Applying any text to a situation takes judgement the text cannot contain (Carroll's tortoise, Wittgenstein on rules). "Followed faithfully with no judgement" names a direction, not a destination.
5. **Smaller items.** The scoreboard's trust in a generator is induction one level up, so induction is relocated, not demoted. "Hypotheses don't gain belief" holds for token predictions, not general ones. A bare point value at 0/0 is exactly the caricature of induction from §2, which is why the compatibility set must travel with it.

## 9. Two pieces of the unfinished argument

**Types.** m = F/a has type "exact reals, a ≠ 0." Experiments produce readings with uncertainty. The textbook contains no function from measurements to masses, so the text does not type-check against its own use. The gap is a type error, not a philosophical mood.

**Computation.** If practitioners execute something reliably, it is an effective procedure, so a finite program for it exists (Church–Turing). Step 5 is a non-constructive existence proof; the demand is for the witness. Nothing guarantees the witness is short, intelligible, or unique.

---

*What survives pressure:* belief attaches to text plus practice; the written text has a type-level hole; some filler exists. *What does not:* that the filler is unique, that finding it is pure description, that it lives inside "mass," or that it returns a number where practice abstains.
