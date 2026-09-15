# Sketch — The Constitutive Asymmetry of Action and Reaction

**Status:** SKETCH / capture draft. Not presentable. Not yet a note.
**Date:** 13 August 2026
**Project:** VD Newton
**Purpose of this file:** pull the §7 finding out of `FORCE_SUM_IFS_ABSTRACTION_BOUNDARY_DISCOVERY_NOTE.md` and capture everything that might belong to it as a standalone note, before any of it is shaped.

**Provenance marking used throughout:**

- `[SOURCED]` — already stated in an existing project document; citation given.
- `[EXTENDED]` — a consequence of sourced material, drawn out here for the first time.
- `[RAISED]` — Claude-raised question or stress case, not previously in the corpus. Treat as a prompt, not a finding.

---

# Part 0 — What this note is, in one paragraph

Standard Newtonian notation writes the third law as $\mathbf F_{12}=-\mathbf F_{21}$ and treats action and reaction as two labels for a symmetric pair differing only in sign. That picture is incomplete. Given an interaction *and* a constitutive law, the pair relation still does not determine which participant receives which force. The missing datum is which participant carries the constitutive mechanism. Once that is supplied, the two forces turn out to have different construction histories: one is computed from constitutive state, the other is obtained by negating the first. They are therefore not interchangeable, and "action" and "reaction" are not arbitrary names for $+\mathbf F$ and $-\mathbf F$.

---

# Part I — Motivation

## 1. Why this needs to be its own note

`[SOURCED]` It surfaced inside the Force-Sum discovery note (§7) but was explicitly parked there: *"This result remains important for the later excavation of IFS member structure. However, it is not yet part of the newly isolated Force-Sum law itself."* The discovery note's own §14–15 abstraction boundary makes the parking mandatory — Force-Sum is polymorphic over the member type and must not know about acting objects or action/reaction provenance. So the finding cannot live there without violating the boundary that note establishes.

`[SOURCED]` It is load-bearing for at least three other places, none of which currently own it:

- `NML3_OPEN_PROBLEM_IMPRESSED_FORCE_IDENTITY_ACTION_REACTION_EXCLUSIVITY.md` §27 flags exactly this structure as *"strongly suggested"* and adds *"its exact type representation remains open."* §14 of the same file needs it to determine cross-target pairing.
- The `V(f)` wall (discovery note §21) will branch on it: *"constitutive evaluation versus negation of a paired action value."*
- `VD_ACTING_OBJECT_INVENTORY_WORKING_NOTE.md` §2 already gives every concrete acting object two separate slots, `action-force` and `reaction-force`, without saying why they are two slots rather than one signed slot.

`[EXTENDED]` That last one is the strongest argument for the note existing. The inventory's working picture already presupposes the asymmetry. This note would supply its justification retroactively.

## 2. Why it is interesting outside the VD

`[RAISED]` The claim is not VD-internal bookkeeping. It is that a standard piece of notation is underdetermined in a way that is not usually remarked on. Textbook presentations routinely say "action and reaction are equal and opposite, and which one you call which is arbitrary." The finding says the second half of that sentence is false whenever a constitutive law is involved: one of them is derived *from* the other, and the direction of derivation is fixed by where the mechanism sits. That is a claim with an audience beyond the dictionary.

`[RAISED]` It may also connect to why the third law is stated as a *law* rather than as a definition. See Part V.

## 3. Goal of the eventual note

Capture, in order of decreasing confidence:

1. That the pair relation plus a constitutive law is insufficient to assign forces to targets. (Confident; demonstrated.)
2. That the missing datum is the identity of the constitutive participant. (Confident.)
3. That this induces an asymmetry of construction history. (Confident.)
4. That the asymmetry is what justifies two slots rather than one signed slot. (Likely.)
5. What that means for the type representation of a force occurrence. (Open.)
6. Whether the asymmetry is universal across acting-object types. (Open — see Part VI, this is the crux.)

---

# Part II — The core argument, restated

## 4. The setup

`[SOURCED]` (discovery note §7) Take two participants and the standard pair relation:

$$
\mathbf F_{12}=-\mathbf F_{21}.
$$

This successfully does two things: it distinguishes two force occurrences, and it relates their values. Now add a constitutive law, say Hookean:

$$
\mathbf F_{\mathrm{spring}}=-k\mathbf x.
$$

## 5. The gap

`[SOURCED]` The two statements together do not tell us whether

$$
\mathbf F_{\mathrm{spring}}=\mathbf F_{12}
\qquad\text{or}\qquad
\mathbf F_{\mathrm{spring}}=\mathbf F_{21}.
$$

Both assignments satisfy the pair relation. So even after (1) identifying the interaction pair, (2) knowing the two values are negatives, and (3) knowing the constitutive output, the forces on the two targets remain unassigned.

`[EXTENDED]` Worth stating sharply in the eventual note: the pair relation is a constraint on a pair of values, not an assignment of values to targets. It has the same defect, one level down, that the aggregate constraint had in the Design 2.1 bug — it constrains a completed structure without determining its parts. This is the same disease twice, and saying so links this note to the aggregate/member finding.

## 6. The missing datum

`[SOURCED]`

> Which participant is the spring, or constitutive acting object?

Once the spring object is identified, its constitutive state supplies the law's value. That value applies to the **non-spring** participant. The negated value applies back to the particular spring object whose constitutive information generated the action.

## 7. The resulting asymmetry

`[SOURCED]` (discovery note §7, verbatim structure)

```text
action force:
acting-object state
  -> constitutive law
  -> force value applied to the non-acting participant

reaction force:
already-constructed action force
  -> negation
  -> force value applied to the acting object
```

Two differences fall out, and the eventual note should keep them distinct because they are logically separate:

- **Different construction history.** The action is computed; the reaction is derived from the computed action.
- **Different target restriction.** The action lands on the non-acting participant; the reaction lands on the acting object specifically.

`[EXTENDED]` A third difference may follow but is not yet argued: **different failure modes.** If constitutive state is unavailable, the action is undefined and the reaction is undefined *for a different reason* — it has nothing to negate. Worth checking whether that distinction does any work.

---

# Part III — What the asymmetry buys

## 8. It explains the two slots in the acting-object picture

`[SOURCED]` The inventory (§2) gives a concrete acting object this shape:

```text
concrete acting-object
    |
    +-- participants
    +-- activation condition
    +-- parameters / modelling regime
    +-- action-force
    +-- reaction-force
    +-- force-accounting target(s)
```

`[EXTENDED]` If action and reaction were merely $\pm\mathbf F$, one slot plus a sign convention would do. Two slots are justified precisely because the two are produced by different routes and land on differently-specified targets. This note supplies that justification.

## 9. It gives the `V(f)` wall its branch structure

`[SOURCED]` The discovery note §21 says the value entry *"may branch according to the member's nature"* and names the branch as constitutive evaluation versus negation of a paired action value — while Force-Sum needs only the common interface $V(f)\in\mathbb V_F$.

`[EXTENDED]` So the asymmetry is invisible at the Force-Sum level and structural at the wall level. That is a clean demonstration that the abstraction boundary in discovery §14 was drawn in the right place: a genuinely important physical asymmetry sits entirely behind the interface without disturbing the law that consumes it. The eventual note might use this as its closing argument, since it validates the boundary rather than straining it.

## 10. It constrains cross-target pairing

`[SOURCED]` NML3 open problem §14: the action/reaction pair lives *across* target accounts, not twice inside one target's IFS —

$$
W(A,M,C)\in\operatorname{IFS}(M\mid C),
\qquad
W(A,N,C)\in\operatorname{IFS}(N\mid C),
$$

with the constraint that the pair *"must not be represented by inserting both action and reaction as separate members of the same target's IFS under one acting-object identity."*

`[EXTENDED]` The construction-history asymmetry gives a reason for that constraint rather than merely stipulating it. The action and the reaction have *different targets by construction* — the action goes to the non-acting participant, the reaction to the acting object. Two members of one target's IFS under one acting-object identity would require both to land on the same target, which the construction rule forbids. So NML3's exclusivity condition (§13) may be derivable rather than imposed.

`[EXTENDED]` This looks like the single most useful downstream consequence, and it is exactly what NML3 §20 asked for: the constraint *"should follow from the object model rather than from an evaluator patch."* Flag prominently.

## 11. It sits well with $f\neq V(f)$

`[SOURCED]` The discovery note (§11, §23.4) separates a force occurrence from its value.

`[EXTENDED]` That separation is what lets the reaction be **identity-independent but value-derived**. The reaction is a distinct occurrence — distinct target, distinct membership, its own identity — while its *value* is obtained by a shortcut from the action's value. Identity and value-derivation come apart cleanly. Without $f\neq V(f)$ this would be hard to state without making the reaction sound like a mere sign flip of the action.

---

# Part IV — Where the acting object actually sits

## 12. An unresolved tension between two framings

`[RAISED]` The discovery note §7 speaks as though the acting object is **one of the two participants** ("which participant is the spring"), and the reaction applies "back to the particular spring object."

The inventory §2 instead treats an acting object as a **mechanism** — `hookean-spring_acting-object`, `normal-contact_acting-object`, `gravity...` — which *has* participants. On that reading the mechanism may be a third thing, not either participant.

These two framings are not obviously compatible, and the eventual note has to pick one or show they coincide.

- If the acting object is a participant: the spring is a body, the reaction lands on it, and the story in §7 works as written.
- If the acting object is a mechanism with participants: "the reaction lands on the acting object" is ill-typed, because a mechanism is not a thing that can carry a force.

`[RAISED]` Candidate resolution: the mechanism has a distinguished participant that **carries the constitutive state** (the spring's length, the surface's stiffness), and the reaction lands on *that participant*, not on the mechanism. Then "acting object" is being used for two different things and the note should split the term. This may be a naming bug worth reporting separately.

## 13. The massless-mechanism case

`[RAISED]` A spring idealised as massless is a participant whose own force account must sum to zero. If the reaction lands on the spring and the spring is massless, the reaction has to be transmitted onward, and the "lands on the acting object" story needs a further step. Worth a stress test — this is where the participant-vs-mechanism question bites hardest.

---

# Part V — The status of the third law

## 14. Does the asymmetry make N3 analytic?

`[RAISED]` This may be the sharpest thing in the note, and it is not currently anywhere in the corpus.

If a reaction force is *constructed* by negating a computed action force, then "action and reaction are equal and opposite" is not something the world could falsify — it is how the reaction was built. The third law becomes a construction rule rather than an empirical claim.

Two ways out, and the note should record which is taken:

- **(a) Reaction independently determined.** Both forces are computed from constitutive information, and N3 asserts, empirically, that they come out equal and opposite. Then negation is a *theorem* about constitutive laws, not a construction route — and the asymmetry in §7 is a fact about convenient computation rather than about structure.
- **(b) Reaction defined by negation.** N3 is analytic, and its empirical content moves elsewhere — into the claim that force accounts built this way predict correctly, or into the claim that every interaction admits a constitutive description from exactly one side.

`[RAISED]` Option (b) relocates rather than removes the empirical content, which is probably the honest reading, but it needs saying out loud.

## 15. Connection to the irreducibility criterion

`[RAISED]` The project's operative test is whether a determination admits a shortcut. Negation *is* a shortcut: the reaction's value is obtainable without running the constitutive procedure a second time. By the project's own criterion that suggests the reaction's **value** is not an independent fact, while its **identity** — being a distinct occurrence on a distinct target, with its own membership in a different IFS — still is.

So the criterion cuts *between* identity and value on the reaction side. That is a nontrivial application and it may be the note's cleanest link to the project's foundations. It also means the asymmetry is not a defect to be smoothed away: it is the criterion doing its job.

---

# Part VI — The crux: is the asymmetry universal?

## 16. The symmetric-interaction problem

`[RAISED]` This is the case that could break the whole finding, and it should be confronted early in the eventual note rather than buried.

Gravitational attraction between two masses. Which is the constitutive acting object? Both masses carry the relevant state (their masses and separation). There is no obvious asymmetry, and nothing distinguishes a "computed" side from a "negated" side.

Three possible readings:

- **(i) The asymmetry is not universal.** It is a feature of *some* acting-object types — those with a distinguished constitutive carrier (spring, actuator, deformable contact) — and absent for others (gravity, and possibly electrostatics). Then the `V(f)` wall branches three ways, not two: constitutive-computed, negation-derived, and jointly-computed.
- **(ii) The mechanism is always a third thing.** For gravity the acting object is the gravitational mechanism, which produces *both* forces by constitutive evaluation from the joint state. Then neither force is a reaction-by-negation, and the §7 asymmetry is a special case arising when the mechanism's state is carried by one participant only.
- **(iii) The asymmetry is always present but sometimes invisible.** Both directions happen to be separately derivable and coincide with the negation, so negation is redundant but still available.

`[RAISED]` Reading (ii) looks most consistent with the inventory's mechanism-centred treatment, and it would make §7's spring case an instance rather than the general rule. If that is right, the eventual note's title claim needs weakening from "action and reaction are asymmetric" to something like "some acting objects have a distinguished constitutive carrier, and where they do, the pair is asymmetric."

That is a smaller claim but a defensible one, and getting it right early avoids building the `V(f)` wall on an over-general premise.

## 17. Known limits of pairing

`[RAISED]` The third law fails outright for electromagnetic forces between moving charges — momentum goes into the field, and there is no instantaneous equal-and-opposite partner. The inventory already anticipates this territory at §3.10 (radiation and field-momentum extensions). Any pairing law written here should be scoped so that it does not silently claim universality it cannot have.

---

# Part VII — Stress tests to run

`[RAISED]` All of these; the eventual note should work at least the first four.

1. **Hookean spring between two blocks.** The canonical case. Confirms the base story.
2. **Gravity between two masses.** The symmetric case. Decides Part VI.
3. **Normal contact between two surfaces.** Both deform; is there a distinguished carrier? Note that the inventory (§5.2) already rules `normal-force` out as an acting object and assigns it to `normal-contact_acting-object`, so the mechanism reading is already preferred here.
4. **Massless spring.** Tests §13 — where does the reaction land when the carrier has no account of its own?
5. **Rocket / imposed actuator** (inventory §3.8). The actuator plainly supplies the value; this should be the *most* asymmetric case and a good positive control.
6. **Two charges with retardation.** Expected to break pairing; a scoping test, not a design test.
7. **Fluid drag on a body** (inventory §3.6). Many participants, or a continuum — does the two-participant framing survive at all?
8. **Friction** (inventory §5.3). Ruled out as an acting object; the mechanism is the contact. Does the constitutive carrier notion apply when the law is non-smooth and history-dependent?

---

# Part VIII — Terminology

`[SOURCED]` `NML3_FORCE_SUM_VOCABULARY_RESERVOIR.md` §1 already banks the relevant candidates: agent, receiver, participant, relatum, source object, acting object, exert, impress, applied to, force due to, provenance.

`[EXTENDED]` The finding suggests the historical pair "action / reaction" may be actively misleading, because both words describe *what the force does* rather than *how it was constructed*. Candidates worth testing against the reservoir's five-question probe:

- constitutive force / derived force
- computed force / negated force
- primary / paired
- carrier-side / recipient-side

`[SOURCED]` Per the NML3 open problem §22 and the reservoir §21, **no naming decision should be taken here.** Resolve the structure first, then pick words. This note should explicitly refuse to name.

---

# Part IX — What this note is NOT

To keep the boundary clean, and mirroring the discipline of the discovery note:

- Not the Force-Sum law. That is settled and abstract over the member type.
- Not the IFS construction / membership law. This note may *constrain* it — see §10 — but does not write it.
- Not the acting-object inventory. That exists.
- Not a naming pass.
- Not a resolution of impressed-force identity. That is the NML3 open problem; this note supplies one input to it.

---

# Part X — Open questions, consolidated

1. Is the acting object a participant or a mechanism, and does the reaction land on the mechanism's distinguished carrier? (Part IV — blocking.)
2. Is the constitutive asymmetry universal, type-dependent, or an artefact of one-sided state? (Part VI — blocking, and the biggest risk to the note.)
3. If reaction is defined by negation, where does the third law's empirical content go? (Part V.)
4. Does role — action or reaction — belong to the force occurrence, to the acting object, or to the pairing relation? (NML3 §13 vs §14; still open there.)
5. Does the identity/value split of Part §11 survive contact with the NML3 identity problem, or does construction history need to enter identity after all?
6. Can the exclusivity condition really be *derived* from construction history, as §10 suggests, or does it still need stipulating?
7. What primitive student exercise would expose a wrong answer here? (NML3 §21 asks this of its own problem; it applies equally.)
8. How does the story scale past two participants?

---

# Part XI — Method note

`[SOURCED]` The discovery note §29 ("hand on the wall") lists *"the missing action/reaction assignment datum"* as one of six cracks the method exposed.

`[EXTENDED]` Worth recording that this finding was produced the same way as the others: by refusing to accept $\mathbf F_{12}=-\mathbf F_{21}$ as self-evidently complete and asking what it actually determines. The eventual note is a second worked instance of the method, and could cite itself as such.
