# The Atwood Set, Read off the v3 Trace and Compared with the Hand Set

## Step 2 of the test proposed in `hypothesis_sets_from_traces` §7

**Status:** record. Claude-authored on 8 November 2026, at Can's request
("Next, read the set off the old v3 trace and compare it with the hand set? go
ahead"), in the Claude Code session that wrote the hand set. Everything here
is analysis: none of it is ruled, and nobody but its author has checked it.
Can's ruling on haze and on members is needed before any of it binds.

**Inputs, fixed by hash:**

| File | SHA-256 | Role |
|---|---|---|
| `inbox/atwood_hypothesis_set_by_hand_2026-11-07.md` | `f282b2a7f45d5f9b82e28e12ac531c6bca05c3f514a244f66351fe9c690b1b23` | the hand set; checked unchanged before the trace was opened |
| `Theory/vd_trace_level2_v3.md` (file dated 22 Mar 2026) | `0ae6b94393e0ea7812ab4269921119add7b75f8eed8b45e8088b709abb4e8ae4` | the trace, opened for the first time in this session after the hash check |

**The rule applied.** The three-kind sort of `hypothesis_sets_from_traces` §2:
- an entry application contributes no member;
- a supplied premise (every "→ human") contributes one commitment member;
- a recorded substitution contributes one mistake member.

Members are compared by their tests, as d4 §4 counts them.

---

## 0. Short version

1. **The sort works mechanically.** The trace's inputs and arithmetic fall into
   the paper's two member kinds without judgement. The world members largely
   correspond: 10 of the hand set's 12 derivation members appear in some form.
2. **The set it yields is not the needed set.** It is too big, too small and
   limitless at once:
   - **Too big.** About half the trace's inputs are not needed for p: source
     attributions, activation conditions, paired particles, and the choice of
     S. The two point-particle inputs are literally false: read as
     members ("m₁ is not a point-particle"), they always hold, so the verdict
     rule would acquit T on every trial.
   - **Too small.** It has no persistence member, no pulley-inertia member, no
     mass-identity member (which its own cut requires), and no measurement
     members at all.
   - **Limitless.** No approximation in the trace carries a size.
3. **Three members are folded into single answers,** present only inside a
   supplied value: the value of g, the vertical direction of the strings, and
   the identity of the mass in the weight with the mass in m a.
4. **The closure diagnostic found the right leak.** It pointed at the
   string-pulley assembly. The member was lost later, in the human response,
   which modelled the string but not the pulley.
5. **The trace names no dictionary edition,** so its claims cannot carry the
   "according to D" suffix.

**Verdict on the 5 November claim.** A trace generates a structure of the right
kind. The old trace does not generate the set. Its failures land on the
corrections C1, C2, C3 and C5 of the 5 November record. Every one is
confirmed, and two are sharpened (§4).

---

## 1. The mechanical read

### 1.1 Supplied premises (kind 2)

The body has about 31 explicit supplied premises. Expanding the second block's
chain, which the trace compresses as "the same structure", gives about 36. The
trace's own 17-row input table groups or omits the rest:
- the two masses;
- four activation conditions and their satisfactions;
- the two tension values "+T ŷ";
- a paired particle that appears only in the demand tree.

Grouped by test:

| Group | The trace's supplied premises | Count |
|---|---|---|
| G1 | m₁ and m₂ are point-particles ("the block's size is negligible for this problem") | 2 |
| G2 | the lab frame is inertial ("approximately; modelling commitment") | 1 |
| G3 | the wall does not accelerate (demand tree only) | 1 |
| G4 | the Earth's acceleration is negligible, ≈ 10⁻²³ m/s² | 1 |
| G5 | the inertial masses are 3 kg and 5 kg (body and demand tree only, not the table) | 2 |
| G6 | each block's interacting-forces set is {gravity, tension} | 2 |
| G7 | the gravity values are −m₁g ŷ = −29.4 N ŷ and −49.0 N ŷ ("empirical: gravitational force law") | 2 |
| G8 | the tension values are +T ŷ, with T unknown | 2 |
| G9 | the string is massless, so the tensions are equal ("by symmetry of the frictionless pulley") | 1 |
| G10 | the string is inextensible, so a₁ = −a₂ | 1 |
| G11 | the source of each force: what acting-object produces it, and that it is one | 4 to 8 |
| G12 | each acting-object's activation condition, and that the block satisfies it | 4 explicit, 8 with m₂ |
| G13 | the paired particles: Earth for the gravity forces, string-pulley for the tension forces | 3 explicit, 4 with m₂ |
| G14 | the diagnostic system S = {m₁, m₂} | 1 |

Not counted: the sign and axis conventions ("origin at pulley, y up"; "a = a₁
positive upward"). They are choices, not claims. Also not counted: the
decision to apply Newton II to each block. The trace's own finding 5 notes
that no entry prescribes it.

### 1.2 Recorded substitutions (kind 3)

At full grain there are about 12:
1. −m₁g = −29.4 N
2. −m₂g = −49.0 N
3. the two force sums
4. the two blocked forms (T − 29.4)/3 and (T − 49.0)/5
5. the two thunks rewritten as 3a = T − 29.4 and 5(−a) = T − 49.0
6. the two rearrangements for T
7. 3a + 29.4 = 49.0 − 5a, giving 8a = 19.6
8. a = 2.45
9. T = 36.75
10. (m₁ + m₂)g / M_Earth ≈ 10⁻²³

`nobody_made_a_mistake` §7 counted 10. The difference is grain.

---

## 2. Each hand member against the trace

| Hand member | In the trace? | Where, and how |
|---|---|---|
| ¬A1 local g | **folded** | only inside G7's numbers; g's value is never stated as an input |
| ¬A2 frame and support | **yes, split three ways** | G2 frame, G3 wall, G4 Earth's recoil (the hand set has it inside ¬A2) |
| ¬A3, ¬A4 masses | **yes** | G5; outside the input table |
| ¬A5 the blocks run are the blocks weighed; constant mass | **absent** | — |
| ¬A6 pulley inertia | **absent** | the exercise and the prose say nothing of it |
| ¬A7 pulley friction | **prose only** | the exercise statement, and "by symmetry of the frictionless pulley" inside G9; not a recorded input |
| ¬A8 string mass | **yes** | G9, "massless" |
| ¬A9 string length constant | **yes** | G10; G12's "m₁ is attached to the string" is its extreme case |
| ¬A10 force completeness | **yes, without versions** | G6 |
| ¬A11 vertical motion | **folded** | only in G8's direction ŷ, and partly in G1 |
| ¬A12 mass in the weight = mass in m a (cut-dependent) | **absent, though the cut requires it** | gravity enters as an empirical value at E36, so on the hand set's §6 this is a member; the trace silently uses the inertial mass in −m₁g |
| ¬A13 arithmetic | **yes, by another route** | §1.2; about 12 against the hand set's 6 steps |
| ¬B1–¬B5 measurement | **absent** | the exercise asks only to "find"; the trace has no measurement side |
| Limits on every approximation | **absent** | "negligible", "approximately", "massless", "inextensible", "doesn't accelerate" carry no size |

**Count.**
- **Hand derivation members present in some form:** 10 of 12.
- **Present as recorded members:** 7. These are ¬A2, ¬A3, ¬A4, ¬A8, ¬A9,
  ¬A10 and ¬A13, and two of them, the masses, sit outside the trace's own
  table.
- **Present only folded or in prose:** 3 (¬A1, ¬A7, ¬A11).
- **Absent:** 2 (¬A5, ¬A6), plus ¬A12, which the cut requires.
- **Measurement members:** 0 of 5.

## 3. Each trace group against the hand set

| Group | Hand counterpart | Reading |
|---|---|---|
| G2, G3, G4 | ¬A2 | match, regrouped |
| G5 | ¬A3, ¬A4 | match |
| G6 | ¬A10 | match |
| G7 | ¬A1, ¬A12 | match, folded |
| G8 | ¬A11 | match, folded |
| G9 | ¬A8; ¬A7 in prose | partial match |
| G10 | ¬A9 | match |
| G1 | parts of ¬A11, of ¬A10's drag version, and of ¬B4 | needed only in a weakened form (§4.1) |
| G11, G12, G13 | none | **used, not needed for p**: with the force values supplied, their failure leaves p unchanged. They matter for other consequences, such as where reactions land. |
| G14 | none | **not a claim**: a choice of diagnostic route |

**Needed members the trace found and the hand set missed: none.** This is
weak evidence. The hand set was written knowing the trace's input categories
(see its blindness note).

---

## 4. What this says about the 5 November corrections

### 4.1 C1, used is not needed: confirmed, and sharpened

About half the trace's individual inputs are not needed for p (G11–G14).
That is the over-generation C1 predicted.

**The sharper finding is G1.** "m₁ is a point-particle", read as a member,
says the block has no extent. It plainly has extent: a 3 kg block is several centimetres
across. So the member
"m₁ is not a point-particle" is held on every trial, and the verdict rule
acquits T every time.

What the derivation needs is weaker: the block's extent does not matter at
ε. That is an approximation member with a limit, and the trace's own gloss
("negligible for this problem") is reaching for it.

**So recognitions of idealisations, recorded as YES, cannot be members as
they stand.** Their needed form is an approximation with a size. Any
generator has to make that conversion.

### 4.2 C2, two derivations: confirmed

There are no measurement members at all. The hand set's §4 is wholly outside
the trace, as C2 expected.

### 4.3 C3, shared budget: confirmed

Six of the trace's groups are approximations: G1, G2, G3, G4, G9 and G10.
None has a size, so the budget can be neither divided nor checked.

On the hand set's numbers, the member most likely to break p in a real run is
pulley inertia, where a 24 g disc pulley already exceeds its share. The trace
does not list it.

### 4.4 C5, the cut moves the line: confirmed, and sharpened

Gravity enters at a wall, as an empirical value. So the identity of the mass
in the weight with the mass in m a is not part of T, and it has to be a
member. The trace uses it without recording it.

The cut does more than move members out of T. It creates members, and the
trace has to record those too.

### 4.5 Recording grain applies to premises too

`hypothesis_sets_from_traces` §3, item 2 found one unrecorded premise. This
run finds three members folded into single answers:
- g, inside −29.4 N;
- the strings' vertical direction, inside +T ŷ;
- the mass identity, inside −m₁g.

A member exists only if the trace records it as a premise. `nobody_made_a_mistake`
§7 found the same for substitutions.

### 4.6 Where the pulley member was lost

The closure diagnostic did its job. It reported that the tension reactions
land on the string-pulley assembly, outside S. The loss happened in the human
response to that leak:
- the string's mass was modelled;
- the string's inextensibility was modelled;
- the pulley's friction was assumed in passing;
- the pulley's inertia was never mentioned.

**Proposed discipline** *(analysis)*. Answering a leak means listing every
property of the external object that enters the internal equations: its mass,
its inertia, its friction, its motion. Each one is either a member with a
limit, or a reason it does not enter. Read this way, a haze allowance is what
a leak's response has to bound.

### 4.7 The edition is unnamed

The trace cites entries E3–E44 of a Newton dictionary but does not say which
version. So its claims cannot be written in the "according to D" form that
`THEORY_LOGICAL_STRUCTURE` §6 asks for. Future traces should name their
edition in the first line.

---

## 5. What this does not show

- **The hand set is not fully blind.** Its absences of ¬A6 and ¬A7 were partly
  expected from earlier summaries.
- **Findings new on opening the trace:**
  - the three folded members;
  - G1's automatic acquittal;
  - the count of unneeded inputs;
  - the unnamed edition;
  - the diagnostic's correct pointing at the pulley.
- **One trace, one prediction, an old edition.** The tension prediction,
  36.75 N, was not compared.
- **Need was judged by hand,** with the countermodel test of d4 §4. A
  mechanical cut by provenance cone, as C1 suggests, was not tried.

## 6. Next

**Step 3.** Force the trace through the current entries. Record every
interpretation of an unfinished entry as a supplied premise. Then read the set
off again and compare it with the same hand set (hash above).

**What C5 and this record predict for that run:**
- a gravity headword would turn G7 into entry applications;
- it would add the commitments `THEORY_LOGICAL_STRUCTURE` found missing;
- it would make ¬A12 part of T;
- the leak responses would still need the §4.6 discipline;
- the measurement side would still be absent.

## Provenance

- **Stated (Can's):** the request; the test design, through
  `hypothesis_sets_from_traces` §7.
- **Analysis (Claude's):** everything else.
- **Read for this record:**
  - the trace, in full;
  - the hand set, in full (its author's);
  - `hypothesis_sets_from_traces_2026-11-05.md`;
  - `nobody_made_a_mistake` §7;
  - d4 §§3–5.
- **Placement:** `inbox/` for sorting, beside the hand set. Both belong next
  to `hypothesis_sets_from_traces` in `Theory/`.
