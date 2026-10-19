# Witness Sheets

## What a Witness Sheet Is, Where It Sits, and What It Adds to the Prediction Set

**Status:** record. Claude-authored at the user's request, 2026-10-06, from that
day's conversation in VD-docs. Records the idea as far as it is developed so
far, in his words where it was stated and marked as analysis where it was not.
**Branch:** Theory. The idea is about any VD theory instance, with Newton as
the worked case.
**Parents (read against):**

- `Theory/actually_there_prediction_sets/IT_IS_ACTUALLY_THERE.md`
- `Theory/actually_there_prediction_sets/actually_there_prediction_sets_synthesis (2).md`
- `Theory/actually_there_prediction_sets/prediction_sets.md`
- `Theory/randomness_declarative_boundary/randomness_declarative_boundary.md`
- `Newton/Design 3/vd_design_3_trace_architecture (1).md`
- `Code/no_lookup_positional_locality/VD_NO_LOOKUP_RULE_RESIDUAL_LAYER_CLOSURE_d2.md`

**This record revises how those notes use the term.** Several of them call
witness sheets "trace-side records" and have the trace "open/consult" a sheet.
That is not the idea. Section 9 lists what changes.

---

## 0. Short version

Every object in a scene has a **witness sheet**. A witness sheet is testimony
about the scene: it sits between the scene and the trace, one layer beyond
the trace's inputs. The trace never depends on how a sheet is structured.
Whoever answers the trace's walls gets the answers from the sheets instead of
from the scene.

The name is the idea. A good witness makes it as though you had been at the
crime scene and watched it yourself. **If every witness sheet were perfectly
kept, you would never have to observe the scene again.**

A sheet does not need to be organised. The block of text in front of an
ordinary Newtonian mechanics question works perfectly well as a witness
sheet. Because a sheet is a piece of information standing between the scene
and the trace, **it can itself be flawed**.

The entries decide everything a sheet implies, so what a sheet implies
becomes what the theory implies. That adds **one element to every prediction
set: the witness sheets accurately describe the scene.** A second element,
"the witness sheets are incoherent", is real, but its form must come from the
entries and cannot be written down yet.

---

## 1. One sheet per object

> Each object has a witness sheet for it. *(stated)*

A sheet is attached to an object of the scene, not to a trace and not to a
demand. A trace may draw on many sheets, and a sheet may serve many traces.

What a sheet records is whatever has been witnessed about its object: what it
is, where it is, how it moves, what it is attached to, what was measured on
it. The sheet is not built for a particular question. Its value is that it
was kept before anyone knew which questions would be asked. This is the
forensic point of the analogy: a witness records the scene first, and the
investigator asks questions afterwards.

---

## 2. Where the sheet sits: the periphery

> The witness sheets exist one layer beyond the "inputs". So think, a
> periphery of a computer. A device that is part of the "computer" physically
> but would be considered as inputs to it. *(stated)*

The layers, from the world inward:

```text
scene          the world itself
  |
witness sheets testimony about the scene, one sheet per object
  |
walls          where the trace demands an input and a reader supplies it
  |
trace          demand-driven evaluation over the dictionary
  |
entries        the dictionary (the theory instance)
```

The peripheral analogy is exact in one respect: a keyboard, a disk or a
sensor is physically part of the computer, but the CPU treats what comes
through it as input. Witness sheets belong to the VD in the same way. They are
part of the apparatus, but the trace treats what comes through them as input.

> The trace doesn't depend on the witness sheet structure. *(stated)*

The trace's contact points with the outside are unchanged: walls (a reader
supplies a value the mechanism demands), expansion, and argument delivery.
Witness sheets add no new contact point. When a wall asks "is m1 a
point-particle?" or "what acting-objects are on p?", the reader answers from
the sheet instead of from the scene. Nothing in the trace reads a sheet.

**Consequence (analysis).** The no-lookup rule (positional locality) is not
touched. That rule governs behaviour that depends on text at other positions
*of the log or of the trace*. A sheet is in neither. Answering a wall from a
sheet is what a wall is for: a reader supplying a value from outside the
dictionary. Whether the reader looks at the scene or at a record of the scene
is invisible to the trace.

---

## 3. A sheet need not be organised

> A witness sheet doesn't need to be organized. A common newtonian mechanics
> question often is preceded by a block of text that can perfectly function
> as a witness sheet. A piece of info that sits between the scene and the
> trace that can itself be flawed. *(stated)*

There is no required layout, no table of slots, no schema the sheet must
follow. Prose works. The standard exam preamble:

```text
Two masses m1 = 3 kg and m2 = 5 kg are connected by a massless, inextensible
string over a frictionless pulley.
```

is a witness sheet for m1, m2, the string and the pulley (several sheets run
together in one paragraph). It is parsed by the reader at the walls, using
the reader's own competence, exactly as a witness statement is read by an
investigator.

**Observation (analysis).** One unorganised sheet routinely mixes kinds of
line that the actually-there notes already distinguish as different ways a
commitment can enter:

```text
"3 kg"                       measurement / input
"connected ... over a pulley" observation of the scene's arrangement
"massless, inextensible"      modelling decision / approximation
"frictionless"               modelling decision / approximation
```

No real eyewitness writes "massless string"; exam text does all the time.
The sheet does not have to separate these, but when a prediction fails they
point to different places to look.

---

## 4. The entries define what a sheet implies

> It is up to the entries to define fully what the implications of the
> witness sheet are and thus, the implications of the witness sheet become
> implications of the theory. *(stated, in reply to: do the meta-object
> entries also define what a complete sheet for an object is? — answer yes)*

Two consequences follow.

**Completeness is definable.** If the entries say what an object of a given
kind has, then a sheet is *complete* for that object when it fills everything
its kind requires. "If all the witness sheets were fully well kept you would
not have to observe the scene again" becomes a checkable condition, not only
an ideal: a sheet is well kept when it answers every wall demand the theory
could make of an object of that kind, and answers it correctly.

**Correctness is defined by the entries.**

> Cause being correct is defined by the entries. The entries can force any
> properties on the witness sheet it wants. *(stated)*

Whether a sheet is coherent is a property of the pair (sheet, theory), not of
the sheet alone. The same text can be incoherent under one theory and
coherent under another (see the worked example in section 6).

---

## 5. Two forms of "actually there"

This separates two things the earlier notes ran together.

### 5.1 Reachability — built in now

> The actually there feature of the VD applies directly to say F = ma. If you
> have F, m and a must exist via being reachable. *(stated)*

The dependency graph already forces existence. If a trace has a net force,
the triplet that defines it makes inertial-mass and inertial-acceleration
reachable, and what is reachable must exist for the trace to be coherent. No
witness sheet is involved. This is what the earlier notes called
**entry-forced**, and the entries as written already deliver it.

The cup/Earth case is reachability: the force on the cup reaches its acting
object, and through it a source participant. The trace forces Earth even if
the sheet never mentions it. (Analysis: so the trace can *expose holes in
the testimony*. When reachability forces a commitment the sheets are silent
on, the wall demand it produces has nothing to answer it with.)

### 5.2 Membership — not built yet

> The idea that the witness sheet commits you to additional "actually there"
> ideas would be an additional feature of the VD that needs to be put in.
> Thus so far, it isn't built in fully and the "meta-object" entries are
> supposed to accomplish that. *(stated)*

Once an object is committed to a kind (the cup is a material object),
everything an object of that kind has exists for that object, whether or not
any demanded headword reaches it. The cup has a velocity even if the
question never asked about motion. This is forced by **kind membership**, not
by graph reachability.

The earlier term "witness-sheet-forced" is therefore a misnomer. The forcing
will come from the **meta-object entries**. The sheet is where the answers to
the resulting demands are written down; it forces nothing itself.

```text
reachability   demanded headword -> entries -> reachable headwords exist
               (built in: E-structure as it stands)

membership     object committed to kind K -> meta-object entries
               -> everything a K has exists for this object
               (to be built: the meta-object entries' job)
```

---

## 6. How a sheet fails

### 6.1 Unfaithful and incoherent

A sheet can fail in two different ways (the split is analysis; both halves
are his):

- **Unfaithful:** the sheet disagrees with the scene. It misrecorded
  something, or left something out.
- **Incoherent:** the sheet disagrees with itself, judged through the
  entries.

> Yes it can all be incoherent. *(stated)*

Incoherence can sit inside one sheet, across several sheets, or across the
whole set for a scene. A stipulated sheet with no scene behind it (an exam
preamble) cannot be unfaithful, since the scene is whatever the sheet says,
but it can still be incoherent:

> A witness sheet can be wrong. Say, for example: "a particle accelerated
> with 5 m/s for 5 seconds. Its velocity is now 1/2 of what it was 3 seconds
> ago." They can be incoherent. *(stated)*

The two failures behave differently (analysis):

- **The theory can catch incoherence from inside.** Since the entries fix
  what a sheet implies, a trace can derive a contradiction from the sheet
  alone, before any prediction is made.
- **Unfaithfulness cannot be caught from inside.** It shows up only as a
  failed prediction, or when someone looks at the scene again.

### 6.2 The worked example, read through the entries

The example also shows that incoherence depends on the theory reading the
sheet (analysis, raised in the exchange, not contested):

- **"5 m/s" is not an acceleration.** Read strictly, the sheet puts a value
  of the wrong type into a slot. That is a third kind of defect, an
  ill-typed sheet, and it is caught before any arithmetic.
- **Read in ordinary language** ("accelerated" means sped up), the sheet
  contradicts itself: speeding up for five seconds cannot halve the
  velocity.
- **Read through the entries** (acceleration is a vector), it does not. A
  constant 5 m/s² directed against the motion gives v(5) = v(2) / 2 when
  the speed at t = 2 s was 30 m/s.

The same text is incoherent in everyday language and coherent in Newtonian
mechanics. This is what "correctness is defined by the entries" means in
practice.

### 6.3 Reading error

A faithful sheet can still be misread at a wall. That failure belongs to the
reader, not the sheet, and is what the existing prediction-set element
"the inputs were wrong" now narrows to.

---

## 7. What sheets add to the prediction set

> Essentially this gives us 1 extra element on the prediction set. The
> witness sheets accurately describe the scene. And the prediction set
> element about the witness sheet being incoherent might come from the
> entries so I can't know that one's form yet. *(stated)*

### 7.1 The fidelity element

Added to every prediction set:

```text
The witness sheets accurately describe the scene.
```

**It replaces part of an old element (analysis).** The old list had "the
inputs or measurements were wrong". With sheets one layer further out, that
splits:

```text
sheet unfaithful to the scene      -> the new fidelity element
faithful sheet misread at a wall   -> the old input element, narrowed
instrument behind the testimony    -> measurement, as before
```

**It is the only element the entries cannot generate (analysis, not ruled).**
Every other element comes from the trace's own commitments, so its form
depends on the theory. Fidelity is about the relation between sheet and
scene, and the entries never see the scene. So it should have the same form
in every theory's prediction set. If so, every prediction set has exactly
one theory-independent element, and it lives at the periphery.

**Stipulated sheets remove it (analysis).** An exam question has no scene
behind its sheet, so the fidelity element cannot fail. In a lab it always
can. This may be part of why textbook Newton feels airtight: one element of
the prediction set has been removed by fiat.

### 7.2 The incoherence element

Its form comes from the entries and is not yet known. Coherence is defined by
the entries, which can force any properties on a sheet, so what counts as an
incoherent sheet, and how the trace reports one, waits on the meta-object
entries.

**Open (raised, not ruled).** If correctness is defined by the entries, an
incoherent sheet may not be a separate element at all. It may be a symptom
shared by two elements already present: either the sheet is unfaithful, or
the entries are wrong. A faithful record of a real scene, read through the
wrong theory, will look incoherent (a faithful record of Mercury's
perihelion is a sheet the Newtonian entries cannot make consistent). Which
element takes the blame then depends on which you trust more, the sheet or
the theory. Whether incoherence is its own element or a test that splits
blame between fidelity and theory failure is undecided.

---

## 8. Redundancy (analysis)

A sheet that gives exactly what the trace needs cannot be shown incoherent:
nothing on it is checked against anything else. Contradiction becomes
possible only once a sheet says more than the trace uses (the worked example
is over-determined: acceleration, duration and a velocity ratio).

So redundancy cuts both ways. It is what lets a sheet be wrong in a
detectable way, and it is also what the mass-identification pipeline uses as
evidence, since redundancy fills the validity interval of a mass binding. A
sheet with exactly enough data can never be shown wrong from inside, which is
not the same as being right.

---

## 9. What this changes in earlier records

Nothing below is edited in place. These are the readings this record
replaces.

| Earlier claim | Where | Reading now |
|---|---|---|
| "Witness sheets are trace-side records." | `IT_IS_ACTUALLY_THERE`, Type 2 | Sheets are peripheral: testimony about the scene, outside the trace. The trace does not depend on them. |
| Forcing chains begin "open/consult witness sheet for x". | `IT_IS_ACTUALLY_THERE`; synthesis §5.2 | Nothing in the trace consults a sheet. The forcing comes from the entries: reachability now, membership once the meta-object entries exist. The reader consults the sheet at walls. |
| "Witness schema imports further demandable slots." | synthesis §5.2 | That is the meta-object entries' job (membership). The sheet need not have a schema; it need not be organised. |
| "Witness-sheet-forced actually-there commitments." | both actually-there notes | Misnomer. Kind-membership forcing by meta-object entries, not yet built. |
| "Entry-forced." | both actually-there notes | Stands, now named reachability: built in, as F = ma already shows. |
| "Slot licensed ≠ slot value known ≠ demanded ≠ measured." | synthesis §5.2 | Stands. Licensing is the entries'; the value is on the sheet or not. |
| Random outcome "may be bound on a sheet for reuse". | `randomness_declarative_boundary` | Compatible. An observed outcome is written on a sheet like any observation; whether it was object-backed or random is decided by what the entries say forced it, not by the sheet. |
| "Bad inputs are tied to witness sheets, walls, and model inputs." | `prediction_sets` | Splits into the fidelity element (sheet vs scene) and the narrowed input element (misreading at a wall). |

**Terminology collision, flagged, not resolved.** The NML3 bridge
(`Newton/nml/nml3/_dscn_nml3_content/NML3_ENTRY_TO_LESSON_BRIDGE_d1.md` §§4.2–4.3)
calls its force-member and interacting-forces-set records "witness sheets".
Those records hold trace-side accounting state (closure status, generation
trace, admitted members), which is exactly what a witness sheet in this
record's sense is *not*. The same notes also use "closer witness" for
evidence of a universal claim (no further member), a different sense again.
Whether those NML3 records should be renamed is a ruling owed.

---

## 10. Open questions

1. **The form of the incoherence element**, which waits on the meta-object
   entries (stated as unknowable for now).
2. **Incoherence as its own element or as a blame-splitting test** between
   fidelity and theory failure (section 7.2).
3. **Is the fidelity element really theory-independent?** Proposed in
   section 7.1, not ruled.
4. **The meta-object entries themselves:** what they say a kind has, and how
   a kind commitment is made at a wall.
5. **Which objects get sheets.** "Each object has a witness sheet", but the
   witness decides how to cut the scene into objects. The cup/Earth case
   shows the trace can force an object that has no sheet. Is that always a
   fidelity failure (an omission), or a separate thing?
6. **Sheets across time.** Traces are per moment and stateless. Sheets sit
   outside the trace, so nothing stops a sheet outlasting one trace; the
   mass pipeline's validity interval is a licence for a sheet entry to keep
   serving later traces. How that licence is stated is open.
7. **Renaming the NML3 "witness sheet" records** (section 9).

---

## Provenance

The idea is the user's, stated 2026-10-06 in five messages: one sheet per
object; the trace does not depend on sheet structure; reachability
(F = ma) as the built-in form of actually-there, with kind-forced
commitments left to the future meta-object entries; the periphery analogy;
the witness analogy and the well-kept condition; sheets need not be
organised, an exam preamble works as one, and a sheet can be flawed; the
entries fully define a sheet's implications, which become the theory's;
any sheet or set of sheets can be incoherent, with correctness defined by the
entries; the one extra prediction-set element (sheets accurately describe
the scene), and the incoherence element whose form must come from the
entries.

Analysis that arose in the exchange and is marked as such above: the
no-lookup rule being untouched (§2); the line kinds mixed on one sheet (§3);
completeness as a checkable condition (§4, which he confirmed); "trace
exposes holes in the testimony" (§5.1); the unfaithful/incoherent split and
its catch-from-inside asymmetry (§6.1); the reading of the worked example
(§6.2); the split of the old input element, the theory-independence claim
and the exam-sheet point (§7.1); the incoherence-as-disjunction question
(§7.2); redundancy (§8); the revision table and the NML3 collision (§9).

An earlier reading in the same conversation, that sheets are a mechanism-side
store from which arguments are pushed into trace sites, was wrong and was
corrected by the user; it is not part of the idea and is recorded here only
so it is not reintroduced.
