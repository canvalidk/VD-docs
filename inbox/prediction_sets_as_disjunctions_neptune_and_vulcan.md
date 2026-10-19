# Prediction Sets as Disjunctions

## Neptune, Vulcan, and Where Newton's Information Comes From

**Status:** record. Claude-authored at the user's request, 2026-10-16, from
that day's conversation in VD-docs. Records the idea as far as it was
developed. The user's own statements are marked *(stated)*; everything else is
marked *(analysis)* and is not ruled.
**Branch:** Theory. Newton is the worked case. The idea applies to any VD
theory instance.
**Parents (read against):**

- `Theory/actually_there_prediction_sets/prediction_sets.md`
- `Theory/actually_there_prediction_sets/actually_there_prediction_sets_synthesis (2).md`
- `Theory/witness_sheets/witness_sheets.md`
- `Theory/theories_and_belief/theories_and_belief.md`
- `Theory/best/alpha_and_the_one_draft.md`
- `Newton-analysis/criticism_history/VD_TYPED_CLOSURE_FAILURE_DEDUCTION_RESIDUAL_TAXONOMY_d1.md`
- `Newton-analysis/_dscn_haze/HAZE_AND_THE_LANGUAGE_OF_APPROXIMATION_2026-09-13.md`

**This record changes how those notes tell Neptune.** They tell it as a failed
point prediction that was rescued. Here it is a prediction that never failed.
Section 8 lists what changes. Nothing is edited in place.

---

## 0. Short version

Newton does not predict "Uranus will be at x". It predicts a disjunction: *x,
or someone made a mistake, or an external body is pulling or pushing, or …*.
That disjunction is the **prediction set**. A failed observation counts against
the theory, as a red ball, only when **every** item of the set has been
rejected, and the rejections are made by hypothesis tests. Neptune was
therefore green. It only looked red to a reading of Newton without prediction
sets. Vulcan was red.

The obvious worry is that "an external body" can absorb any discrepancy. It
cannot, because **Newton applies strictly to moments in time**. At any one
moment Newton allows every possible external force. But the body must be one
body, the same at every moment, and its own motion must also obey Newton. The
residuals across all the moments of Uranus's orbit therefore constrain it,
jointly. That is honest about where the information came from. The theory
supplied the form of the item; decades of observed moments supplied its
content. What came out sharp (where to look) and what came out loose (how far
away) follows exactly where those moments carried information.

Vulcan used the same item, licensed by the same theory, and its content was
missing. Mercury's anomaly is a slow drift accumulated over many orbits. It
carries no time signature that would localise one moving body, so the item
pointed nowhere definite, and the searches rejected it.

---

## 1. The prediction set is the prediction

> The idea is that we can't decide if we have a red ball until every element
> of the prediction set is checked. Each element is a hypothesis, and only if
> every element of the set is rejected will the theory get a red ball against
> it. *(stated)*

> What connects elements of the prediction set are OR statements. The orbit
> will be this OR someone made a mistake OR there is an external body pulling
> or pushing. *(stated)*

Written out:

```text
Newton predicts:
     position(Uranus, t) = x(t)
  OR the calculation or the inputs contain a mistake
  OR an external body is acting on Uranus
  OR the frame is not inertial
  OR an approximation in the model broke
  OR ...                      (every item the theory's structure generates)
```

**A ball has three states** *(analysis, following the stated rule)*:

- **green:** some item holds. The point prediction matched, the mistake was
  found, or the body was found;
- **red:** every item has been rejected;
- **in hand:** some item is still open. The belief tally does not move yet.

**"Theory fails" is not an item.** It is what happens when every item is
rejected *(analysis)*. This answers the standing objection that a prediction
set containing "theory fails" covers every outcome and so predicts nothing.
The set has content: it rules out the conjunction "the orbit misses, and there
was no mistake, and no external body, and the frame was fine, and …".

**Rejections are made by hypothesis tests.**

> Well we can apply belief to anything before it happens. But the relevant
> part is that the relevant rejections are made by the hypothesis test.
> *(stated)*

So two layers are kept apart *(analysis)*:

- **The test layer colours the ball.** Each item gets a hypothesis test with a
  declared significance level. The ball is red only when every item has been
  rejected at its level.
- **The belief layer counts coloured balls.** Bayesian belief in the theory
  moves on green and red draws, not on items that are still open.

**No free parameters.**

> There are only free parameters if you include them additionally.
> *(stated)*

The external-body item is not "some body, with a mass and an orbit fitted to
taste". It is the claim that *a body exists which, under Newton, produces this
residual*. Newton plus the record fix what that body must be (§3). Le
Verrier's calculation was the work of testing the item, not a price paid by the
theory.

---

## 2. Newton applies strictly to moments

> Notice that Newton applies strictly to moments in time. *(stated)*

Newton II relates the net force on a particle *at time t* to its inertial
acceleration *at time t*. The VD writes it that way:

- the Atwood trace demands `net-force(m₁, t)` and
  `interacting-forces-set(m₁, t)` (`Theory/vd_trace_level2_v3.md`);
- the witness-sheet record notes that "Traces are per moment and stateless"
  (`Theory/witness_sheets/witness_sheets.md` §10, item 6).

**At a single moment the external-body item is almost empty** *(analysis)*.
The residual at that moment is one vector: observed acceleration minus what the
known bodies supply. Any acting object whose force at t equals that vector
would do. For gravity even that vector does not separate mass from distance:
a body of mass M at distance r pulls exactly like a body of mass M/4 at r/2.

> So while Newton would allow for the possibility of every potential external
> force. The full information constrain it. *(stated)*

This is the right description of a single moment. The prediction set's
external item is licensed by the theory at every moment. At any one moment it
would absorb anything.

---

## 3. What ties the moments together

The item becomes definite only through what holds *across* moments
*(analysis)*:

1. **One body.** The residuals at different moments must come from the same
   external object. That a body is the same body from one moment to the next
   is itself a commitment. `what_the_vd_is.md` makes the general point: a
   practitioner's commitment to "the identity of a particle across time" must
   appear somewhere. The trackability and persistence work
   (`Newton-analysis/_dscn_particle_and_mass_origins/`) is where the VD
   handles re-identification.
2. **Its own motion is Newtonian.** The hypothesised body is a particle with
   its own force account, dominated by the Sun. Its trajectory is therefore not
   arbitrary. It belongs to a small family: an orbit plus a mass.
3. **Its pull at every moment follows from 1 and 2.** One member of that
   family fixes the predicted residual on Uranus at every moment of the
   record.

So the item is a claim about **the whole record of moments at once**: some
member of a small, Newton-generated family reproduces every observed residual
within its allowance. That is a definite and rejectable claim. It is not "a
force appeared at t".

**Where the information came from.**

> So the data Neptune is being fitted to are all the moments across the
> orbit. … Which is honest to where the information is coming from for
> Neptune. *(stated)*

The theory supplied the *form* of the item: a body, its Newtonian motion, its
Newtonian pull. The observed moments supplied its *content*. Whatever the
moments constrained tightly came out sharp. Whatever they constrained loosely
came out loose. Nothing in the result is more precise than the moments that
produced it.

---

## 4. Neptune, worked through

The history below is the standard account. Items marked † were checked against
secondary sources on 2026-10-16 (see Provenance); the rest is unchecked.

**The record.** Uranus's positions ran from the 1781 discovery back through
pre-discovery sightings recorded as stars, up to the 1840s. Tables built in
1821 no longer fitted the observations.† The standard account says Uranus ran
ahead of the tables before about 1822 and fell behind after. The residual
changed sign as Uranus passed the unseen body.

**The items, taken in turn** *(analysis, using the stated rule)*:

| Item | How it was tested | Result |
|---|---|---|
| a mistake in the calculation or the old observations | the theory recomputed, observations re-reduced | rejected |
| the known planets mis-modelled | Le Verrier showed Jupiter and Saturn could not explain the residual whatever their masses† | rejected |
| an external body | compute the one Newtonian body that reproduces the residual at every moment; it predicts a direction for 1846 | open, then tested |

**The test.** On 23 September 1846, Galle and d'Arrest found the planet within
about 1° of Le Verrier's predicted position. Adams's prediction was about 12°
off.† The external-body item survived a test that could have rejected it. The
ball is **green**. It was never red; it only looked red to a reading in which
Newton predicted the bare point x.

**What the moments determined, and what they did not** *(analysis)*.
- **Sharp: the direction.** The residual record was most informative around
  the years when Uranus passed closest to the unseen body, and that pins down
  roughly where the body was.
- **Loose: the distance and the mass.** For a pull seen from far away these
  trade off against each other, and the record did not separate them well. The
  usual accounts put the distance assumed in the predictions near 36 AU,
  against Neptune's actual 30 or so (not checked here).

**What the find confirmed.** It confirmed the existence item and the predicted
direction. It did not confirm the fitted orbit size. This fits the production
path rule in the synthesis: credit flows only to what the tested prediction
actually depended on *(analysis)*.

**Afterwards, two separate significance levels apply** *(stated that they are
distinct; analysis on how they apply here)*:
- the item tests coloured the ball;
- Neptune's entry into the catalogue of planets is an admission under the α of
  `alpha_and_the_one_draft.md`.

> They are both significance levels, but the alpha note's prediction sets
> determine the number of things that exist. The number of inputs might be
> related to that but its unclear right now how. *(stated)*

Read here as: the alpha note's significance level fixes how many things the
catalogue admits. That reading is this record's, not a ruling.

---

## 5. Vulcan, worked through

**The record.** In 1859 Le Verrier reported an unexplained advance of
Mercury's perihelion, about 38″ per century. The modern value is about 43″.†

**What these moments contain** *(analysis)*. The anomaly is a secular drift: a
slow rotation of the orbit, built up over many revolutions. It has no time
signature that a single moving body leaves, like Uranus's residual changing
sign as it passed Neptune. So the external-body item had no content that
pointed anywhere definite. Many arrangements give the same drift: a planet
inside Mercury's orbit, a ring of small bodies, or diffuse matter near the Sun.
Le Verrier himself allowed either a planet or a ring of debris.†

**The items, taken in turn:**

| Item | How it was tested | Result |
|---|---|---|
| an intra-Mercurial planet | searches for transits and at solar eclipses, for roughly 55 years after Lescarbault's 1859 claim of a transit† | rejected |
| a ring or belt of small bodies | the same searches, plus the requirement not to disturb other planets | rejected (not checked here in detail) |
| diffuse matter (the zodiacal-light material) | Seeliger examined whether any distribution of it could explain the advance without causing other anomalies in the inner planets† | not sustained (the outcome is not checked here) |

When every item is rejected, the ball is **red** against Newton for that
domain. Proposals to change the force law itself (for example Hall's 1894
exponent, not checked here) are not items of Newton's prediction set. They are
different theories. General relativity (1915) accounted for the advance
without any perturbing body.†

**Why the same item behaved differently** *(analysis)*. In both cases the
item came from the same place in the theory. In both cases it was tested the
same way. The outcomes differed because of what the moments contained:

- Uranus's record gave the item a definite content: a direction to look in.
- Mercury's record gave it almost none, and each definite version of it failed
  its test.

No one's judgement separated the two cases. The record did. This is why the
external-body item is not an ad hoc escape: it costs nothing to *state*, but it
has to *pass a test* whose content the record fixes.

**Red is domain-bounded** *(analysis)*. The red ball counts against Newton
near the Sun, at that precision. Predictions whose allowances are far larger
than 43″ per century, such as orbits elsewhere or engineering, are untouched.
Belief in Newton as a universal theory drops; belief in Newton inside its
allowances does not.

---

## 6. Why this was never obvious

*(analysis)*

- **Every telling in the VD files treats Neptune as a rescue.** That includes
  `prediction_sets.md`, the synthesis §12, the typed-closure note §§12–13, and
  the haze note §3. Each starts from a failed point prediction and shows a
  licensed way out. That framing invites the obvious objection: if any miss
  can be blamed on an unseen body, the theory risks nothing. Reading the set
  as a disjunction removes the "failed" step.
- **The objection is answered by time, and that answer is written nowhere.**
  The item is nearly empty at one moment and nearly rigid across many. Newton
  is a per-moment law, but the body it posits must persist and must obey the
  same law. This is what makes the external-body item a test rather than an
  excuse, and no file says it.
- **The typed-closure note came closest.** Its procedure begins "Map the
  residual FIELD: measure F_res(p) as a function of p's configuration
  (position, extension against candidate anchors, time)". It also says the
  hypothesised body "had to itself move under the Sun's gravity for the
  residual's time-dependence to come out right". Those are the two ingredients
  of §3. The note does not draw the conclusion that the item gets its content
  from the record of moments.

---

## 7. The VD pieces, and where each enters

| Piece | Where it lives | Its role in the story *(analysis)* |
|---|---|---|
| Per-moment trace with attributed inputs | `Theory/vd_trace_level2_v3.md` | Produces the prediction at each moment and records every commitment the items deny |
| Force accounting through acting objects (reachability) | Design 3 notes; `witness_sheets.md` §5.1 | Every force needs a source, so an unexplained residual *generates* the external-body item. The theory's structure supplies the item; nobody invents it |
| Honesty rule | `prediction_sets.md` | Items must come from the theory's structure, so the disjunction is finite and every item can be rejected |
| Haze bound | `HAZE_AND_THE_LANGUAGE_OF_APPROXIMATION_2026-09-13.md` §3 | The residual exceeding the declared bound on omissions is what makes the external item live and not ignorable |
| Typed closure | `VD_TYPED_CLOSURE_..._d1.md` | Residual field, then kind fit, then typed external participant. It is the procedure for testing the external item |
| Identity across time | `_dscn_particle_and_mass_origins/` (trackability, persistence) | Licenses "the same body at every moment", which ties the moments together |
| Witness sheets | `witness_sheets.md` | A hypothesised body has no sheet. The item's test predicts the values a sheet would need; Galle's observation is what writes Neptune's sheet. This answers `witness_sheets.md` open question 5 for this case |
| "It is actually there" | `IT_IS_ACTUALLY_THERE.md` | Neptune is the cup and Earth at planetary scale. Uranus's reciprocal pull on Neptune is a forced commitment, negligible for Neptune's motion |
| Hypothesis tests | this record, §1 | Reject items; colour the ball |
| Belief layer (urn) | conversation of 2026-10-16 (not yet in any file) | Coloured balls update Bayesian belief. Mercury's ball stayed in hand for decades, and belief in Newton barely moved meanwhile |
| Production-path credit | synthesis §§1–2 | The find credits what the test actually tested: existence and direction, not the fitted distance |
| Allowances and domains | haze notes; synthesis §3 | A red ball is bounded to the domain and precision where it was drawn |
| Admission α | `alpha_and_the_one_draft.md` | Neptune entering the catalogue is a separate significance level from the item tests (§4) |

---

## 8. What this changes in earlier records

Nothing below is edited in place. These are the readings this record replaces.

| Earlier claim | Where | Reading now |
|---|---|---|
| Neptune shows that "historical 'failed predictions' of Newton were not failures of the full Newtonian prediction set"; "Uranus did not match the simple point prediction" | `prediction_sets.md`, Claim | Stands, sharpened: the prediction *was* the disjunction. Neptune was a green ball |
| Theory failure is "the remaining branch when licensed rescues close or become too costly" | synthesis §9 and §13 item 9 | "Too costly" is replaced: theory failure is not a branch. A ball is red when every item has been rejected by its hypothesis test |
| "A narrow prediction says: Uranus should be at position x at time t. Observation disagrees." The VD-style story then licenses a branch | synthesis §12 | Newton never predicted the bare x. The orbital discrepancy opens no rescue; it starts the item tests |
| Le Verrier "fitted a complete witness sheet — mass, orbit, position" | typed closure §12 | The fit produced predicted values for the slots, sharp in direction and loose in distance. Galle's observation wrote the sheet |
| Vulcan: "no admissible witness sheet existed"; "halt at theory boundary" | typed closure §13 | The items were rejected by their tests, so the ball is red. It is bounded to the domain |
| "The extra piece exceeded its bound, and a keyed member was added" | haze §3 | Compatible. Exceeding the haze bound is what makes the external item live; the item test then admits the member |
| A prediction set containing "theory fails" excludes no outcome | read-through of 2026-10-16 | Answered: "theory fails" is not an item, so the set excludes the conjunction of a miss with every item false |

---

## 9. Open questions

1. **How a trace states a constraint across moments.** Traces are per moment
   and stateless (`witness_sheets.md` §10, item 6). The external item's
   content comes from many moments at once. What entry or structure says "the
   same body, obeying the same law, at every moment"? Is it the persistence
   certificates of the mass pipeline, or something new?
2. **Testing existence items.** "No such body exists" is rarely refuted
   outright. What test, at what significance level, rejects an item that says
   something exists? Was Vulcan rejected, or abandoned?
3. **The two significance levels.** The item-test level and the catalogue α
   are distinct *(stated)*. How the number of items relates to the number of
   things that exist is unclear *(stated)*.
4. **The error rate of a red ball** *(analysis)*. If each of n items is
   rejected at level α, the chance that a red ball is wrong (some item was true
   but falsely rejected) can approach n·α. A large, well-generated prediction
   set is hard to colour red by accident. Is that part of why established
   theories fail slowly?
5. **Completeness of the set.** The items should be generated from the trace's
   own record, so that the disjunction is finite and fixed before the test. No
   file does this yet; it is the trace-to-prediction-set step.
6. **Credit inside a green ball.** Neptune's find confirmed existence and
   direction, not distance. A rule is needed for which commitments a green
   ball credits.
7. **Dark matter.** On this reading, the galactic rotation-curve ball is still
   in hand: the external-matter item has not been rejected, and its content is
   disputed.

---

## Provenance

**The idea is the user's**, stated 2026-10-16 in four messages:

- the prediction set as an OR of items, with a red ball only when every item
  is rejected;
- Neptune green, looking red only without prediction sets, and Vulcan red;
- no free parameters unless added;
- rejections made by hypothesis tests, while belief can attach to anything
  beforehand;
- the two significance levels distinct, with their relation unclear;
- Newton applying strictly to moments, so that Neptune is fitted to all the
  moments of the orbit and the full information constrains the external force,
  which is honest about where the information came from.

The surrounding Bayesian-urn model is also the user's, stated in the same
conversation. Belief is Bayesian; experiments are targeted at a theory's weak
domains; replications are further draws; and the model is meant to explain the
timescales of acceptance and rejection. It is not yet written up in any file.

**Analysis that arose in writing this record**, marked as such above:

- the three ball states and the answer to the "covers every outcome" objection
  (§1);
- the near-emptiness of the item at one moment and the mass-distance
  degeneracy (§2);
- the three things that tie the moments together (§3);
- sharp direction against loose distance, and what the find credited (§4);
- secular drift with no time signature as the reason Vulcan's item had no
  content (§5);
- the reading of the earlier notes (§§6, 8);
- the table of pieces (§7);
- open questions 4–7.

**History.** The cases are used for their structure, but the account aims to
be right.

- Checked on 2026-10-16 against secondary sources (marked †):
  - Galle and d'Arrest found Neptune on 23 September 1846, within about 1° of
    Le Verrier's position and about 12° from Adams's;
  - Le Verrier showed Jupiter and Saturn could not account for the residual;
  - the 1821 tables failed;
  - Le Verrier's 1859 figure of about 38″ per century, and the modern figure of
    about 43″;
  - Le Verrier's planet-or-ring proposal;
  - the eclipse searches over about 55 years following Lescarbault's 1859
    claim;
  - Seeliger's examination of zodiacal-light matter;
  - general relativity's 1915 account.
- Not checked:
  - the pre-discovery sightings of Uranus recorded as stars;
  - Uranus running ahead of the tables before about 1822 and behind after;
  - the ~36 AU distance assumed in the predictions;
  - Hall's 1894 exponent;
  - the outcome of Seeliger's analysis;
  - the details of the ring hypothesis.
- Sources used:
  - Wikipedia, *Urbain Le Verrier* — https://en.wikipedia.org/wiki/Urbain_Le_Verrier
  - Astronomy.com, *Who discovered Neptune?* — https://www.astronomy.com/science/who-discovered-neptune
  - Astronomy.com, *Sept. 23, 1846: Johann Galle discovers Neptune* — https://www.astronomy.com/today-in-the-history-of-astronomy/sept-23-1846-johann-galle-discovers-neptune/
  - Wikipedia, *Vulcan (hypothetical planet)* — https://en.wikipedia.org/wiki/Vulcan_(hypothetical_planet)
  - Nature (1925), obituary of Seeliger — https://www.nature.com/articles/115309a0

**Placement.** This record sits in `inbox/` for sorting. It probably belongs
in `Theory/`, beside `actually_there_prediction_sets/` and
`witness_sheets/`. Whether it binds as a correction to the synthesis is a
sorter's call.
