# Typed Closure-Failure Deduction and the Residual Taxonomy

## What an Open System's Residual Forces Say About What Exists Outside It

**Status:** working discussion note, d1. Claude-authored at user request,
2026-08-15, in VD-docs.
**Project:** VD Newton (Newton-analysis incubator), with a theory-side
hand-off.
**Theory-side parent:**
`Theory/actually_there_prediction_sets/IT_IS_ACTUALLY_THERE.md` — this note
develops that note's mechanical-closure section.
**Mechanics-side parents:**

- `Newton-analysis/participant_symmetric_canonical_orientation/VD_PARTICIPANT_SYMMETRIC_CANONICAL_ORIENTATION_MESHING_d2.md`
  (member-named force laws, Part IX; per-target value degeneracy, §§11–12)
- `Newton-analysis/participant_symmetric_forces/VD_PARTICIPANT_SYMMETRIC_FORCES_OWNER_BLIND_ACTIVATION_AND_HALF_WEIGHTING_d2.md`
  (closure theorem, same-kind reciprocity, half-weighting)
- `Newton-analysis/action_reaction_asymmetry/ACTION_REACTION_CONSTITUTIVE_ASYMMETRY_SKETCH_d1.md`
  (carrier datum, computed/negated construction histories)
- `Newton-analysis/canonical_force_orientation/CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14_d1.md`
  (structural closure condition §6; external-cancellation test §9.4)

**Presumption, stated up front:** this note presumes a more fully encoded
Newtonian mechanics than currently exists in entries — Newton III in place,
member-named force laws (`action-force_kind` / `reaction-force_kind`) as the
taught forms, and the Design 3 witness vocabulary (witness sheets,
acting-object witnesses) available to traces. Where the entries do not yet
exist, the reasoning is run against their intended shape.

---

## 0. Purpose and one-paragraph result

When a system fails to close — a member's force account carries a residual
that its internal inventory cannot pay — the member-named force laws turn
that failure into an instrument. The residual can be fitted against the
member laws of a hypothesized kind, and the outcome is a **typed** deduction
about what exists outside the system: not "something pulls," but *which
role* the external thing occupies in *which acting-object structure*. The
two acting-object branches behave differently under this instrument, and the
difference is itself measurable: **asymmetric (constitutive-carrier) kinds
yield residuals in single-member form and support two distinct external
deductions; participant-symmetric kinds yield residuals only in paired-sum
form and support exactly one, merged deduction.** The historical
instantiations are not hypothetical: Neptune is the schema's worked witness
case, Vulcan its worked halt case, and dark matter its live undecided case.

---

# Part I — The instrument

## 1. Setup

Select a system $S$. Build the force account of a member particle $p$ from
the acting-objects whose witnesses lie inside $S$. Suppose the account fails
to close: the observed kinematics of $p$ (via Newton II) demand a net force
that the internal inventory does not supply. Call the shortfall the
**residual** on $p$:

$$
\mathbf F_{\text{res}}(p)
=
\mathbf F_{\text{net}}^{\text{observed}}(p)
-
\sum_{f\in\operatorname{IFS}_{\text{internal}}(p)}V(f).
$$

## 2. The procedure

```text
1. Map the residual FIELD: measure F_res(p) as a function of p's
   configuration (position, extension against candidate anchors, time).
2. Hypothesize a force KIND whose value law fits the field's form.
3. Classify the residual against the kind's MEMBER laws:
   does it match action-force_kind or reaction-force_kind,
   given the fitted configuration?
4. Read off the typed deduction: which role the external witness fills.
```

Step 3 is the step that did not exist before member-named laws. An
underspecified $F=-kx$ cannot classify a residual, because it does not say
which member it quotes or who receives it. The member-named forms make the
classification well-posed — where the branch permits it at all, which is the
subject of this note.

## 3. What the deduction is not

Two boundaries, both inherited from the convention note §6 and test §9.4:

- **Closure is constituted structurally, diagnosed evidentially.** Whether
  $S$ is interaction-closed is a structural fact about participant
  incidences, not a fact about vector values. The residual instrument runs
  the *inference* direction: values in evidence of missing structure. That
  is abduction, not definition, and the two must not be conflated.
- **The instrument runs one way.** A nonzero residual licenses deduction; a
  zero residual licenses nothing. Two external interactions may cancel on
  every member of $S$ (the external-cancellation test), so
  $\mathbf F_{\text{res}}=0$ does not certify closure. Neptune-style
  deduction can miss cancelling pairs by construction.

---

# Part II — The asymmetric branch: the spring, worked

## 4. Two member laws, discriminable per configuration

Hypothesize spring-kind for the residual on $p$. The member laws land on
different targets with different value patterns relative to the measurable
constitutive state (the extension):

```text
action-force_spring   -> on the attached body: restoring pattern (-kx)
reaction-force_spring -> on the carrier: outward pattern (+kx)
```

Fit $k$ and the anchor geometry from the residual field. Exactly one member
law fits, and the two outcomes are **distinct logical deductions**:

**Residual matches `action-force_spring`.** Then $p$ is the attached body,
and the carrier is not in $S$:

> There must be a spring outside the system, attached to $p$.

**Residual matches `reaction-force_spring`.** Then $p$ is (or carries) the
constitutive mechanism, and the action side is landing beyond the boundary:

> $p$'s own spring is real and engaged; an object we did not notice must be
> connected to it, outside the system, receiving the action.

## 5. What the typing buys

In `IT_IS_ACTUALLY_THERE` vocabulary, the witness-sheet-forced external
commitment now arrives **typed**: not "a participant exists outside $S$" but
*which slot of which acting-object witness it fills* — carrier slot in the
first case, attached-participant slot in the second. The two deductions
demand different witness sheets, predict different further slots (the
carrier has constitutive state to measure; the attached body has its own
account to close), and are separately falsifiable. σ, the quoted/negated
mark, is here **residual-measurable**: an open-system observer can determine
from values which member they are seeing.

---

# Part III — The symmetric branch: gravity, worked

## 6. The discrimination step fails, necessarily

Run the identical procedure on a gravity-kind residual. The member laws are,
per target, **value-degenerate**: the two members landing on any one target
are equal vectors (meshing note §§11–12). On $p$, the action of an external
owner's instance and the reaction of $p$'s own instance both take the value

$$
\frac{Gm_pm_q}{2r^2}\,\hat{\mathbf r}_{p\to q}.
$$

So step 3 has no answer from values. σ is value-invisible in the symmetric
branch, and that abstract point cashes out here as a hard deduction limit:
**open-system residual analysis can never determine the member split for a
participant-symmetric force.**

## 7. The pure-member hypotheses are not merely indistinguishable — they are inadmissible

The closure theorem forbids both single-member readings:

- *residual $=$ action only* would mean an external owner acts on $p$ while
  $p$ fails to own gravity back — violating same-kind reciprocity;
- *residual $=$ reaction only* would mean $p$'s instance acts outward with
  nothing acting back — the mirror violation.

The only structurally permitted gravity residual from a single external
participant is the **paired sum**:

$$
\mathbf F_{\text{res}}(p)
=
\underbrace{\tfrac12\mathbf F_{\text{pair}}}_{\text{action of }G_q\text{ on }p}
+
\underbrace{\tfrac12\mathbf F_{\text{pair}}}_{\text{reaction of }G_p\text{ on }p}
=
\frac{Gm_pm_q}{r^2}\,\hat{\mathbf r}_{p\to q}.
$$

## 8. The two deductions merge

For the spring, "the mechanism is outside" and "an unnoticed receiver is
outside" were different conclusions. For gravity they are **one**
conclusion, because the external thing necessarily occupies both roles:

> There must be a massive participant outside the system — which is at once
> an owner of gravity acting on $p$, and the receiver of the action of
> $p$'s own gravity instance.

And the second half of that sentence is a forced commitment with no spring
analogue: closure failure under a symmetric kind commits the trace to the
proposition that **$p$'s own `action-force_gravity` is landing outside $S$
right now**. That is the cup-on-Earth commitment of
`IT_IS_ACTUALLY_THERE`, no longer recited from Newton III but derived from
the residual, in its exact halved-architecture form.

---

# Part IV — The residual taxonomy

## 9. The taxonomy

```text
asymmetric (constitutive-carrier) kind:
    residuals occur in SINGLE-MEMBER form
    sigma is residual-measurable
    two distinct typed deductions (carrier outside / receiver outside)

participant-symmetric kind:
    residuals occur ONLY in PAIRED-SUM form
    sigma is residual-unmeasurable (value-degenerate per target)
    one merged typed deduction (participant outside, both roles)
    plus a forced outward commitment (own action lands outside)
```

## 10. The degeneracy is diagnostic

A half-strength gravity-kind residual — one matching exactly a single member
value — is structurally impossible under participant symmetry. Measuring one
would falsify the branch classification for that kind: it would reveal a
directed source-species mechanism (red–blue physics) masquerading as a
symmetric force, or new physics outright.

This gives the branch classification an **empirical signature**, which bears
on the meshing note's open question 2 (the locally decidable mark licensing
the ½ vs. 1 weight): the branches are distinguishable *from outside an open
system* by which residual forms occur. This is a measurement-side route to
the classification; the entry-side mark (decidability from the kind's own
definition) remains open, and the two should eventually agree — the entry
mark predicting the residual signature is exactly the kind of
falsifiable-in-principle link the framework favours.

## 11. Which questions are well-posed, known in advance

The question "is the mechanism outside, or is an unnoticed receiver
outside?" is well-posed for the asymmetric branch and **ill-posed** for the
symmetric branch — and the VD tells you which, in advance, from the
headword's branch. Standard notation cannot state the question, let alone
sort its answerability by force kind.

---

# Part V — Historical instantiations

## 12. Neptune — the worked witness case

Uranus's account fails to close: a residual survives after the Sun and known
planets are subtracted. The residual *field* — decades of positional data —
fits gravity-kind. The symmetric branch then forces the merged deduction: a
full participant, owner and receiver at once. The receiver half did real
inferential work: the hypothesized body had to itself move under the Sun's
gravity for the residual's time-dependence to come out right, so Le Verrier
(and Adams) fitted a complete witness sheet — mass, orbit, position on a
given night — not a static tug. Galle found the witness within a degree of
the demanded slot (1846). *It is actually there* as a literal observing-run
instruction.

## 13. Vulcan — the worked halt case

Mercury's perihelion: same closure failure, same gravity-kind hypothesis,
same schema, run by the same man. This time **no admissible witness sheet
existed** — no mass-position assignment matched the residual without
contradicting other observations. The honest trace verdict was: *no witness
can fill this slot; halt at theory boundary.* The residual was eventually
paid by changing the entry (general relativity), not the inventory. In
`IT_IS_ACTUALLY_THERE` terms, Vulcan was an unlicensed import: the residual
was real, but the forcing path from residual to object never completed, and
the discipline of demanding the completed path is exactly what separates the
two cases. Same inference; one returns a planet, the other returns the edge
of Newtonian mechanics — and the schema itself grades which verdict applies.

## 14. Dark matter — the live undecided case

Galactic rotation curves: closure failure at galactic scale, gravity-kind
hypothesis, and a standing dispute over which forcing path the residual
licenses — *fill the witness* (dark matter: Neptune again) or *modify the
entry* (modified gravity: Mercury again). The typed-deduction framing states
the dispute more cleanly than most of the literature: it is a disagreement
about whether an admissible witness sheet exists, and both programmes are
attempts to complete their respective forcing paths. The schema does not
decide the case; it says precisely what deciding it would consist of.

---

# Part VI — What this adds to IT_IS_ACTUALLY_THERE

## 15. Three upgrades to the closure section

1. **Typed external witnesses.** "An external witness is actually part of
   the accountable force structure" becomes: an external witness *in a
   specified role of a specified acting-object kind*, with a predicted
   witness sheet, separately falsifiable per role.
2. **Stronger entry-forcing for symmetric kinds.** For the symmetric branch
   the entry structure forces more: the external witness is committed to
   *both* roles, and the trace is additionally committed to its own member's
   action landing outside the system. The cup/Earth example was already
   two-layer (entry-forced + witness-sheet-forced); the halved architecture
   makes the layers exact.
3. **A third verdict.** The working rule's paths (entry-forced,
   witness-sheet-forced, input, unlicensed import) gain the halt verdict as
   a first-class outcome: *the residual is real and no admissible witness
   exists* — closure failure as evidence against the entry rather than for
   an object. Vulcan shows the verdict is reachable in practice and that
   reaching it honestly is a success of the method, not a failure.

## 16. Extended working rule

```text
A closure-failure commitment is licensed only when the trace can show:
  residual field
  -> kind hypothesis (value-law fit)
  -> member classification (or its principled impossibility, symmetric branch)
  -> completed witness sheet for the typed external role(s)

If the witness sheet cannot be completed admissibly, the verdict is a halt
at the theory boundary, and the residual stands as evidence against the
entry structure — never smuggle the object in anyway.

A zero residual licenses nothing (external cancellation).
```

---

## 17. Open questions

1. State and prove the admissible-residual-forms result per branch as a
   theorem (single-member forms for constitutive kinds; paired-sum forms
   for symmetric kinds), including mixed inventories.
2. Superposition: with several external witnesses, the residual is a sum of
   admissible forms. Neptune worked because the known inventory was
   subtracted first. What are the identifiability conditions — when can a
   residual field be uniquely decomposed into external witness sheets?
3. Noise and estimation: the member classification for the asymmetric
   branch is a hypothesis test. What does the test look like when the
   constitutive state (e.g. extension) is itself estimated?
4. Does the entry-side branch mark (meshing note q2), once settled, provably
   predict the residual signature of §10?
5. The n-participant generalization, again (convention note q5): what do
   residual forms look like for mechanisms that are not binary?
6. Theory-side: how should the halt verdict be recorded in a trace so that
   Vulcan-type cases are distinguishable from not-yet-completed
   Neptune-type cases while investigation is still open (the dark-matter
   state)?

---

## Provenance and scope

Authored 2026-08-15 in VD-docs from the same day's working discussion. The
deduction schema (residual → kind fit → member classification → typed
external conclusion) and the spring case are the user's, as is the Neptune
identification ("hence, Neptune"); the degeneracy/merger analysis for the
symmetric branch, the inadmissibility argument, the residual taxonomy, and
the Vulcan / dark-matter framings arose in the exchange and are recorded
here for the first time. This note presumes entries that do not yet exist
(see the presumption paragraph in the header); it proposes no entry wording
and selects no headwords. The historical cases are used as structural
instantiations, not as history of science — dates and attributions are
standard textbook fare and carry no load. Math written in `$`/`$$` form
from the start.
