# Draft 3 of the hypothesis-set paper: how it is flawed

**Status:** record. Claude-authored at the user's request, 2026-11-01, from
that evening's review of d3 (claude.ai, VD folders project). The user's own
statements are marked *(stated)*; everything else is *(analysis)* and is not
ruled.
**Corrects:** `hypothesis_set_paper_d3.md`, in this folder. d3 stays current;
this record names what the next draft has to fix. Nothing is edited in place.
**Read against:**

- `inbox/prediction_sets_as_disjunctions_neptune_and_vulcan.md` (2026-10-16 record, the paper's conceptual parent; unsorted at the time of writing)
- `Theory/theories_and_belief/theories_and_belief.md`
- `Theory/actually_there_prediction_sets/`

---

## 0. Short version

The verdict rule is right. What d3 says about the rule is wrong.

d3 defines green as: some member of the hypothesis set held, so the
disjunction T actually entails was true on this trial. That is T *not losing*
belief. But d3 describes green throughout as T *gaining* belief: "counts for
T", "a trial in its favour", "the theory has gained a trial in its favour",
"the tally for T stands one higher", and §5 reads the urn as the theory's
reliability. Gaining belief in a theory and not losing it are different
mechanisms *(stated)*, and d3 runs them together.

## 1. The ruling *(stated, 2026-11-01)*

- A trial's set either holds or it doesn't. Green means the set held. A found mistake is green, not void.
- "We just have to accept the reality that gaining belief in a theory is simply a different mechanism than not losing belief in it."

## 2. How the conflation showed *(analysis)*

Two independent reviews the same evening (Claude's, and another model's that
he pasted in) both read green as positive support and attacked it on that
reading. A run with a known-broken commitment earns a green ball; OPERA's
loose connector makes special relativity one trial stronger; note 13 concedes
that large sets are "easy to decide for". Both reviews then proposed repairs
that weakened the rule: voiding any trial in which a commitment failed, or
relabelling green as "resolved without refutation" while conceding that the
urn no longer measures reliability. He rejected both.

Both reviews had smuggled back the bare-outcome reading that the paper's first
sentence rejects. T never claimed p; it claimed the disjunction, and when a
mistake is found the disjunction was true. Two careful readers falling into
the same hole is the evidence that the hole is in the prose, not in the rule.

## 3. What green means under the rule *(analysis)*

Green is an acquittal: the trial could have convicted T and did not. Not
guilty is not innocent, and finding the real culprit is the cleanest
acquittal there is. The urn then estimates θ, how often T's claims are true on
the class; equivalently, how often T is not at fault when something goes
wrong.

- θ = 1 for a true theory, by entailment, however careless its testers. §5's "absolutely true of the cart" becomes: when a cart experiment fails, the fault is never Newton's. "Absolutely wrong of the muon": it always is.
- OPERA's green is no paradox. Relativity was acquitted, and the tally standing one higher is simply true.
- The Bayesian rivals (Dorling, Strevens) apportion blame, which is the same quantity. The comparison becomes: blame assigned a little at once, against blame assigned only at closure.
- Neptune and OPERA are both green, but only Neptune involved a new risky claim (a planet near longitude L) that came true. The gain mechanism, not the urn, is what separates them, and it explains why only Neptune was felt as a triumph.

## 4. What d3 gets wrong as a result *(analysis)*

1. **Wording.** In §3 to §5, "counts for T", "in its favour", "gained a trial", "the tally for T stands one higher", "belief that T is reliable" and "the delay before belief moves" all read as gain. Replace them with not-at-fault or acquittal language, and state once that the urn measures belief not being lost.
2. **The gain mechanism is missing.** d3 never says how belief in a theory is gained. Name it, at least in a paragraph (severity; novel success, with Neptune as the worked case). Otherwise referees will either read greens as gains, as both reviews did, or say only half of belief has been modelled.
3. **θ is not a property of T alone when T is false.** A false T gives θ = m, the rate at which something else breaks first: each such mistake acquits T, and the corrected rerun then goes red. Greens cannot tell a true theory from a false one in careless hands; only reds discriminate. Genuine mistakes dilute the reds without hiding them, so the limit θ → 1 stays honest, but finite-sample statements do not. Note 12's "0.99 confidence that θ ≥ 0.99" is literally true of a false theory tested where something else breaks 99.5% of the time. Either build testing practice into the class, or say that reliability means reliability in the hands of the people who test the theory.
4. **The real threat is false acquittals:** a mistake wrongly believed found (d3's caveat 2; note 13 on large sets; Collins's experimenters' regress). Promote it from a caveat to the main threat.
5. **Title and abstract** promise a delay before belief moves. What d3 models is a delay before a verdict.

## 5. Parked: other objections from the same review, not settled here

Listed so that none is dropped. None is ruled.

- **The descriptive claim fails in the flagship case.** Newcomb's 1895 tables built Hall's altered exponent in (n = 2.0000001612, perihelion motions of the four inner planets augmented accordingly), and those tables were adopted in the national ephemerides from 1900, while the planet member was still open (Duncombe and Seidelmann, "Planetary theories and observational data"). Add Vulcan 1915, OPERA's theorists and the 750 GeV bump, all conceded in d3.
- **The argument against Bayesian movement.** "No definite likelihood" does not give zero movement; imprecise credence (Joyce 2010) gives an interval. The two models differ in the path: Bayes drifts down as members are ruled out, d3's model is flat and then steps. The history may favour drift.
- **"Fixed before the test" against §6 and the Bell list:** Stanford's problem of unconceived alternatives (*Exceeding Our Grasp*, 2006).
- **Missing literature.** Eliminative induction and inference: Earman 1992, ch. 7; Bird 2005 ("Abductive knowledge and Holmesian inference") and 2010 ("Eliminative abduction"); Forber 2011 ("Reconceiving eliminative inference"); McCoy 2021. Suspended judgment and inquiry: Friedman 2013, 2017, 2020.
- **§5:** the claim about how physicists talk is uncited; the paragraph on advice and personal truths is out of scope for a philosophy of science journal.
- **22 open [check] tags**, among them Popper 1974 p. 986 and Gapaillard 2015, which bears on "under a degree".
- **The strongest idea is in caveat four:** a rival's derivation can close Newton's open member through its own set ("no intra-Mercurial matter" as a commitment of general relativity's 43″). Candidate centrepiece for the next draft.
- **Withdrawn:** the "free green balls" objection was only a reductio under the misreading described in §2.
