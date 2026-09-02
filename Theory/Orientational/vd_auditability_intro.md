# The VD Project, from the Auditability Angle

*An informal introduction. The point here is to motivate the project, not to derive anything.*

---

## The funnel

Think of a physical theory as a funnel. A pile of heterogeneous stuff goes in the top — numerical inputs, modelling decisions, assumptions you didn't know you were making, choices about what to ignore — and a prediction comes out the bottom. Something like *the acceleration will be 5 m/s²*.

Some of the objects that fall into that funnel are well-known. They have memorable names, and often a whole branch of mathematics devoted to inspecting them and checking that they behave. Force, mass, energy. You know them, the community knows them, and there are tools for verifying claims about them.

But other objects fall into the funnel too, and these don't have established names. Maybe they're too mundane to have been noticed. Maybe they're too subtle. Maybe they aren't mathematically recognised yet, or they're too vague as concepts to have been picked out cleanly. None of that stops them from participating in producing the prediction. They're in the funnel, doing work, just anonymous.

The operative idea behind the whole project: **in mathematics, to name something is to notice its existence.** An unnamed object can't be inspected, can't be checked, can't be combined with anything. Naming is the precondition for everything else.

So the VD — the Valid Dictionary — is the collection of intellectual tools built to systematically name the objects that go into making predictions, and to gather them all in one place where they're named and described.

## Why bother

Two payoffs, and they're worth keeping distinct.

**Reliability.** Once a previously-unrecognised object has a name, it becomes a *target*. The mathematical community can train its inspection machinery on it and check it for rigour. You can't audit what you can't point at; naming is what makes the pointing possible.

**Discovery.** Insights tend to hide in the *interactions* between mathematical objects, not in the objects themselves. If enough otherwise-overlooked objects get assembled in one place, their interactions might surface results that frontier research has been quietly stepping over for years. You only get that if the objects are all named and sitting together where their interactions can be seen.

Both payoffs run through naming. That's the bet.

## The three criteria

If that's the goal, the project has to be good at three things:

- **Perceptiveness** — actually noticing the unnamed objects in the first place, including the ones that are hard to notice *by their nature*.
- **Reliability** — making sure that what gets named is named correctly, and can be trusted to do what it claims.
- **Scale** — gathering enough objects that the interaction-effects become available, and doing it in a way the wider community can actually check.

## The four objections

The cleanest way to see what the infrastructure is *for* is to imagine handing the project to a skeptical physicist. They'll have four objections, and most of the existing machinery exists to answer one of them.

**1. How do you know the objects you've named are correct — that they verifiably produce the predictions, rather than being plausible-sounding inventions?**

**2. How do you notice the existence of objects that are, by their nature, hard to notice?**

**3. How do you do any of this while respecting the genuine diversity and vagueness in the boundaries between theories, without overgeneralising and flattening it all into a false universal?**

**4. How do you do all of this at scale, mechanically, in a way that stays — as promised — auditable to the wider community?**

## The tools that answer each

**Objection 1 — correctness — is answered by the trace and the dossier.** A trace runs the named objects all the way down to a concrete predicted number, with every dependency forced to be explicit. If the named objects are wrong or incomplete, the trace either fails to close or spits out the wrong value — so correctness is checked against a result, not against the author's say-so. The finer-grained version of the same answer is the dossier: a named object's content is `raw_meaning`, the convergent record of how a disciplined target actually behaves when you probe it. Constructions yield to records. That's verification.

**Objection 2 — perceptiveness — is answered by the residue derivation.** The trick is not to rely on noticing, because the hard-to-notice objects are exactly the ones intuition misses. Instead they get *derived into existence*: the residue argument shows that when you try to write down a general procedure for matching two unknown interpreters, the procedure is forced into a shape with parameter slots, and those slots are objects nobody posited. They fall out of structural necessity. So the answer to "how do you notice the un-noticeable?" is that you don't depend on perception at all — you let the structure manufacture the objects for you.

**Objection 3 — diversity without overgeneralising — is answered by the named-dictionary architecture itself.** This is the foundational one. A VD never makes a claim about meaning *simpliciter*. Every statement is indexed to a named dictionary — "the definition of *w* is δ" is ill-posed until it's read as "in dictionary *D*, *D(w) = δ*." So the framework structurally *cannot* overgeneralise across theories, because it has no vantage point from which to assert a theory-independent truth and no hidden background authority it could smuggle in to do the flattening. This is exactly why theories have to be built up from scratch: you can't ingest existing physics wholesale, because that would mean inheriting whatever concealed authority it was leaning on. You re-found each theory on the explicit baseline and log every commitment as an entry. The diversity at the boundaries is respected by refusing to give yourself any tool that could paper over it. The from-scratch requirement is the cost of answering this objection honestly, not just methodological tidiness.

**Objection 4 — auditable scale — is answered by Code and the append-only log.** The engine reads entries, builds the dependency graph, detects laws and houses, and runs traces — that's the scale leg, the mechanisation. The append-only discipline plus the fully-explicit, fully-attributed trace is what keeps the scaled-up output honest: anyone can walk a trace and see every commitment and every point of human input. Mechanisation buys scale without buying a black box.

---

*One thing worth noticing: objections 1 and 4 both lean on the trace, but for different properties of it — objection 1 on its truth-preservation (produces the right number or breaks), objection 4 on its transparency (shows all its work). The pieces cross-cut more than the one-objection-one-tool table suggests.*
