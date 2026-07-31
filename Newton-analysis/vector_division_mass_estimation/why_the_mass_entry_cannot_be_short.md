# Why the Mass Entry Cannot Be a Short Scalar Definition

An account of how I was convinced, written at Can's request. This is not a
reconstruction of his argument, which he is still working out. It is the sequence
that actually moved me, including the positions I defended too long and the two
places where I made the entry worse while believing I had improved it.

Filed to inbox for sorting. Grounded in E10 (`inertial-mass-material-object`) but
the load-bearing parts are general.

---

## 1. The position I was defending

For most of this work I held that E10 should read:

```text
For one material-object, the positive scalar that multiplies its
inertial-acceleration-material-object to give its net-force-material-object.
```

Fourteen words, no conditions, no procedure. I defended it four ways, and none of
the four was stupid, which is why it took so long to dislodge.

- **Definitions state what a thing is; procedures are trace matters.** The entry
  says which scalar; the evaluator finds it.
- **Constants of proportionality are conventionally implicit.** The `k` in
  `F = -kx`, resistivity, the gas constant. The house does it too — the Hookean
  entries define their constants relationally, never as quotients.
- **The definite article does elegant work.** `the` presupposes existence and
  uniqueness, so every boundary case is a failure of the description and none of
  them needs writing. Six behaviours from two words.
- **Load belongs on edges, not in residual.** Procedure text is residual, and the
  entry-writing guide says to move load the other way.

What was wrong with each, in the end:

- VD entries are not definitions in the lexicographic sense. The guide is explicit
  — an entry is *"a compact behavioural trigger placed where the trace needs the
  interpreter to perform an operation."* I was optimising a different object than
  the one I was writing.
- Convention is precedent, not criterion. That physics defines proportionality
  constants implicitly says what physicists do, not what maximises the probability
  of a correct trace.
- The definite description's logical work is real, but its *trigger* is weak.
  Presupposition failure is something readers accommodate rather than halt on.
  `0/0` is a klaxon installed in primary school; a failed definite description is
  a raised eyebrow.
- The guide asks for minimal *unbacked* residual, not minimal residual. Stock
  arithmetic is backed. That objection was never as strong as I made it.

---

## 2. What actually convinced me was not any single objection

Each objection arrived separately, and each one I absorbed with a patch. The
patches are the evidence.

```text
objection                            my patch                    where it landed
-----------------------------------  --------------------------  ---------------
inversion at every use               state the quotient          IRIL
measurement never gives exact align  declare a tolerance         IRIL
|F|/|a| is one estimator of many     declare a measurement model IRIL
students get no hint of complexity   glosses, a burn activity    packet + lesson
the reader needs the procedure       route it                    E12
```

Five times I moved something out of the entry. Every individual move was locally
defensible. The pattern is what broke the position: **if the entry is correct and
everything the reader actually needs is somewhere else, the entry is not doing its
job.** An entry whose accompanying apparatus has to carry the tolerance, the
estimator, the procedure, the hint and the handoff is not a compact behavioural
trigger. It is a true sentence with a support system.

The guide names this exact failure, and I walked into it while quoting the guide:

> If the intended reactions to a figure must be documented in packet notes for
> anyone to see them, that is the proof the machinery exists — it just lives where
> no audit can reach it.

The IRIL records what the residual *imparts*. A determination step the string does
not trigger is not imparted logic. Putting it there was not a division of labour;
it was a place to hide something the entry had failed to do.

---

## 3. The hinge: brevity at the other two corners is borrowed, not earned

This is the step that reorganised everything for me, and it came from the
type-theoretic reading.

Two corners of Newton II are **total** operations:

```text
PositiveMass  × AccelerationVector -> ForceVector          (total)
ForceVector   × PositiveMass       -> AccelerationVector   (total)
ForceVector   × AccelerationVector -> checked result       (not total)
```

E8 and E9 can be bare expressions because **their preconditions are discharged
upstream, by the types, before the entry is ever read.** A positive scalar and a
vector always admit a product. The entry inherits a guarantee it did not have to
establish, and its shortness is that inherited guarantee showing up as absence.

E10 has nothing to inherit. Its precondition is *value-level*: whether some
positive `m` exists depends on a relation between the two supplied values, and no
type in play encodes that. `ForceVector × AccelerationVector` is a perfectly
well-formed input that may simply not admit an answer.

So the check has nowhere else to live. If the entry does not carry it, nothing
does — not the type system, not the upstream entries, not the demand that produced
the trace.

I had read E8's and E9's brevity as a *standard* that E10 was failing to meet, and
I kept trying to get E10 closer to it. That was backwards. Their brevity is a
subsidy. E10 pays full price because it is the only corner not receiving one.

---

## 4. The asymmetry is real, and three independent routes find it

Worth recording that this is not an artefact of one framing. Three unrelated
approaches land in the same place:

- **Algebraic.** `a = F/m` and `F = ma` are closed forms. `m = F/a` is not,
  because vector division is undefined.
- **Type-theoretic.** Two corners are total on their input types; the mass corner
  is checked, because ordinary vector types do not encode the value-level relation
  a positive mass requires.
- **Dimensional.** `F` and `a` are not dimensionally comparable — newtons against
  `m s⁻²`. Mass is not a ratio of like things but a conversion between unlike ones.
  This is why the intuitive escape route fails as well: *"how many times does `a`
  fit into `F`"* is quotition division, which compares like with like, and nothing
  here is like anything else.

When three routes with nothing in common agree, the odd corner is odd for a
structural reason and not a drafting one. That killed my hope that a cleverer
wording would restore symmetry. There is no such wording, and looking for one was
the wrong activity.

---

## 5. Why the check cannot be demoted to a precondition

The obvious economy is to fence the entry instead of extending it:

```text
For aligned net-force and acceleration vectors, the magnitude of the one
divided by the magnitude of the other.
```

A precondition says when the entry applies. It says nothing about what to do when
it does not. That is survivable if the failure branch is rare.

It is not rare. It is the normal case.

---

## 6. Precision makes the exception the rule

Measured vectors are never exactly codirectional. Sensor noise, calibration,
numerical differentiation of a trajectory, timing, frame error — exact alignment
has effectively measure zero in any real trial.

So an entry fenced by exact codirectionality is defined precisely on the set of
inputs that never occurs, and silent on every input that does. Its check fires
almost always, and its failure branch is empty.

That is worse than having no check. A check that always fires and says nothing
trains the reader to ignore it.

This is also where the two documents converge. The estimation problem is not a
detail hanging off the edge of the law — it is what using the law *is*, once the
inputs come from instruments rather than from a textbook.

---

## 7. And the empty branch is not merely empty — it points the wrong way

The last thing that convinced me is the one I caused.

Trying to strengthen the entry's boundary behaviour, I made it assert the
alignment:

```text
Therefore the two point the same way, and the scalar is ...
```

I described this as an upgrade: misalignment now contradicts an asserted fact
rather than quietly failing a presupposition. Louder trigger, better entry.

The trigger was louder and it pointed at the wrong action. An assertion about the
world, contradicted by data, evokes *the law fails here* — and from there,
**"therefore no mass."** The reader needed to arrive at *"these values are not yet
the quantities; estimate a codirectional pair first."*

So the fork the entry must resolve is:

```text
(A)  not codirectional -> no mass                        catastrophic
(B)  not codirectional -> estimate the pair, then read   correct
```

And the packet already forbade (A) in its anti-misread list, in as many words,
while the string evoked it. **A prohibition in the packet cannot repair a trigger
in the string.** That is the guide's central claim about where machinery lives, and
it is the sharpest possible demonstration that the entry — not its apparatus —
has to carry the route.

---

## 8. The honesty argument, which I think is Can's, stated as it reached me

A dictionary that defines mass in terms of net force and acceleration, but whose
definition holds only on inputs that measurement never produces, is not
simplifying. It is claiming a coverage it does not have.

For an ordinary textbook that is a venial sin, because prose around the equation
picks up the slack. For a document whose entire premise is that its commitments
are inspectable, it is the one sin that matters: the gap is invisible to audit,
because the entry is *true*. Nothing in it is wrong. It is only silent where the
work is.

Which is why "the entry must be longer" is not a concession to practicality. The
extra material is not scaffolding around the definition. It **is** the definition
of mass in terms of net force and acceleration — the rest was the definition of
mass in terms of an idealised pair that does not arise.

---

## 9. The diagnostic that would have caught this five moves earlier

Read the entry as the reader, holding realistic data, and ask what they do next.
Not: is this true?

Both of my mistakes survive the truth test and fail this one. Dropping `the vector`
at E9 was right, but I reached it by asking whether the type was derivable, not by
asking what the reader does. Asserting codirectionality at E10 was wrong, and it
was wrong in a way the truth test cannot see, because the assertion is true.

The corollary, which I would put in the entry-writing guide: **an entry improved as
a statement can be degraded as a stimulus, and the second is the one being
optimised.**

---

## 10. What remains unresolved

- The right wording. The current draft resolves the fork with "reconciled to a
  codirectional pair", which is vague exactly where it must not be.
- The division of labour with E12. E10 must trigger the handoff; E12 carries the
  estimation machinery. That boundary is right, but E10's routing language is not
  yet written.
- The headword suffixes, which have stopped being cosmetic. Any sentence naming
  both daughters twice runs long enough that the tempting compressions —
  `the former`, `the net-force magnitude` — silently convert headword edges into
  residual anaphora. The tax is now driving a structural defect, not just length.
