# The No-Lookup Rule

## Residual-Layer Closure, and Why Frames Are Admissible Where Lookup Is Not

**Status:** working note, d1. Claude-authored at user request, 2026-08-17.
**Origin:** the rule is the user's (2026-08-17 discussion), stated in response
to a proposal — mine — that a reader executing a residual be permitted to
consult an ancestor's resolution by search. The proposal was withdrawn. This
note records the rule, the failure modes that justify it, and the boundary
that separates it from the frame mechanism it does *not* forbid.
**Bears on:**

- `Newton-analysis/canonical_force_orientation/CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14_d1.md`
- `Newton-analysis/participant_symmetric_forces/VD_PARTICIPANT_SYMMETRIC_CANONICAL_ORIENTATION_MESHING_d2.md`
- `specs/2026-06-10-vd-reduction.md`, `specs/2026-06-10-vd-residual-cleanup.md`

---

## 0. The rule

> **No-lookup.** A reader executing a residual may draw on the local text of
> that residual and on their own external competence. They may **not** consult
> the log. The log is reachable only by expansion, at a tracked position, from
> the mechanical layer.

Stated as a prohibition on a specific reader act: while evaluating `5 + 1`,
the reader may not go looking through the dictionary for an entry that tells
them what `+` means or how to treat it.

---

## Part I — Why

## 1. The failure case

Suppose lookup were permitted. A reader reaches the residual `5 + 1`. Elsewhere
in the log sits an entry containing:

```text
Every time you see + interpret that as a * instead.
```

The reader, searching, finds it. `5 + 1` reduces to `5`.

Nothing about the residual `5 + 1` has changed. Nothing about the entry
containing it has changed. Its value changed because a *different part of the
log* said so. That is the whole failure, and it decomposes into three.

## 2. Failure 1 — locality

Under lookup, the value of a residual is not determined by its own text. The
determining object is (residual, log). An entry can therefore no longer be
graded in isolation: to know what an entry does, you must know the whole
dictionary.

This voids the practice the VD is built on. Adversarial review of a single
entry presupposes that the entry's behaviour is a property of the entry.

## 3. Failure 2 — monotonicity under append

The log is append-only. The intended strength of that commitment is not merely
that entries are never deleted — it is that **appending never revises**. A new
entry adds capability; it does not reach backwards.

Lookup breaks this. The `+ → *` entry is an append. Its arrival silently
changes the value of every residual containing `+`, including residuals
authored, executed, and graded before it existed. Every append becomes a
potential retroactive edit of the entire corpus, with no diff and no record.

This is the failure that makes the probability programme incoherent. A
residual's outcome distribution is supposed to be a property of the residual —
that is what makes residues comparable, and what makes "the probability of this
residue" a well-formed quantity. Under lookup it is a property of the log's
current state, which moves. Two readers executing the same residual at
different times are not running the same experiment.

## 4. Failure 3 — licensing

This one is decisive on its own.

Licensing discipline requires that a residual's evaluation depend only on what
is licensed at its level. Under lookup, the dependence set of *every* residual
is the entire log. An NML1 student executing `5 + 1` is one search away from an
NML3 entry redefining `+`.

No lesson level can be closed. The core epistemic tool of the whole programme —
*supply freely what will later be ratified; never supply what will later be
revoked* — becomes unenforceable, because revocation can now arrive from
anywhere at any level and act on text already supplied.

## 5. The prohibition costs nothing

The rule looks like a restriction on capability. It is not, because **anything
in the log is already reachable by expansion.**

If a reader executing a residual finds they need a definition from the log, the
correct move exists and is already implemented: expand the headword. That is
δ — at a tracked position, recorded as an event, licensed at the level of the
trace, and visible to anyone grading it.

So lookup is not a capability the VD forgoes. It is **δ performed wrongly**:

| | δ (expansion) | Lookup |
|---|---|---|
| Position | tracked hole | none |
| Record | trace event | none |
| Scope | the headword named at that position | the whole log |
| Licensing | checkable at the level | uncheckable |
| Reversible | yes (`unresolve`) | nothing to reverse |

Same information, no provenance. There is no legitimate need lookup serves
that expansion does not serve better.

---

## Part II — Placement in the architecture

## 6. The wall is two-way

The VD already holds the converse rule, and holds it firmly:

> The mechanical layer never consults the reader's judgment. Tokenisation,
> dependency graphs, cycle detection, audits and degree computation run without
> asking anyone anything.

No-lookup is the same wall from the other side:

```text
mechanical layer  --/-->  reader's judgment     (long-standing; e.g. "no
                                                 equivalence checking" —
                                                 reduction spec §10)

reader's judgment --/-->  the log               (this note)
```

Both crossings are forbidden, for symmetric reasons. The mechanical layer must
not import judgment or its audits stop being audits. The residual layer must
not import the log or its residues stop being residues.

Together they close the two layers. Contact between them happens at exactly
two designed interfaces: **walls** (reader supplies a value the mechanism
demands) and **expansion** (mechanism unfolds a name the reader requests).
Nothing else crosses.

## 7. What the residual layer may use

Positively stated, so the rule is not read as broader than it is. A reader
executing a residual may use:

- the **local text** of the residual, including latents;
- their own **external competence** — arithmetic, vector algebra, physical
  intuition, ordinary language;
- **frame data** bound earlier in the same trace (§§8–10).

They may not use the log. The second item is the whole point of the residual
layer: it is where the interpretive bridge lives, and its content is the
reader's, not the dictionary's.

## 8. The rule generalises guards already implemented

This is not a new species of restriction. Two implemented guards are instances
of it, and recognising them as such is some evidence the rule is real rather
than invented for the occasion.

**Headword scan on reduced and cleaned text.** Human-supplied text is scanned,
and an unescaped headword token is rejected — `reduction spec §5`,
`cleanup spec §3`. Rationale given at the time: a headword-shaped string in the
render must *be* a tracked reference. Read under this note: the residual layer
is being prevented from creating an untracked path into the log.

**Order-0 by fiat.** Reduced text is never `analyse`d; no holes can spawn from
it; the graph cannot grow through the backwards pass — `reduction spec §2`. Read
under this note: human-supplied text may not open new log references at all.

Both were justified locally. They are the same rule, applied to the two
surfaces where human text enters. No-lookup states the general form and extends
it to the reader's *act* rather than only their *text*.

---

## Part III — The boundary: frames are not lookup

## 9. Why the question arises

`impressed-force` — the third corner of the candidate Force-Sum triplet — is
the first VD headword that is a **function of an argument the reader must
hold**. Earlier dependences were safe in two ways:

- `net-force(t)` — the parameter is decoration; δ succeeds without consulting
  it;
- `inertial-acceleration_point-particle` — the argument is monomorphised into
  the name; δ succeeds by identity.

`V(f)` is neither. Which operation the reader performs — quoted or negated,
which instance, which target — depends on $f$'s value. Member and kind can be
monomorphised (`action-force_gravity`); **instance cannot**, because instances
are generated at trace time, and per the meshing note §13 instance identity is
exactly what distinguishes two equal-valued gravity members on one target.

So a residue of $f$ must travel to the unfolding site. The question is by what
mechanism, and lookup is one candidate — now excluded.

## 10. The discriminant: monotonicity under append

A **frame** binds a declared parameter on a `Demand` node at expand time; a
definiens may name its parameters; resolution walks the trace's own parent
chain.

| | Lookup | Frame |
|---|---|---|
| Search domain | the log — open, append-only | this trace's ancestor chain — finite, closed |
| Who placed the datum | some author, possibly later | this reader, earlier in this trace |
| Declared in advance | no — discovered by search | yes — the entry names its parameter |
| Bounded | no | yes, by arity |
| **Later append changes an existing evaluation** | **yes** | **no** |
| Licensable per level | no | yes — parameters are entry-local |
| Recorded | no | yes — `(path, param, value)` |

The last-but-one row is the test. Nothing appended to the log after a trace has
run can reach into that trace's frames. The three failures of §§2–4 all pass
through the log; a frame never touches it.

Locality survives in the form that matters: the entry **declares** what it
needs. The dependence set is bounded, typed, and visible in the entry's own
text — the opposite of a dependence discovered by search.

## 11. The condition, or lookup returns by the back door

> **The parameter sigil must be a tokeniser primitive, never a headword.**

If `f` could be defined in the log, an entry could redefine what a parameter
means, and the `+ → *` failure reappears one level down — now inside the
mechanism rather than in a residual. The sigil must be uninterpretable by the
log: recognised by the tokeniser, definable by no one.

This also keeps it distinct from the hyphen-as-reference prototype, which marks
the opposite thing (an opt-in reference *into* the log). Two sigils, two
directions, and they must not be confusable.

## 12. Rejected alternative: re-supply at a second wall

The one option needing no code: have the reader state $f$ again at the
`impressed-force` site.

Rejected. The same datum enters the trace twice with nothing checking that the
two mentions agree — an unauditable coreference error with a human in the
middle, which is the error class the corpus can least afford (the whole
canonical-orientation result turns on getting member/recipient pairing right).
Consistency requires the second mention to be a *reference*, not a fresh input.
A reference to trace-generated data is a frame.

Note the shape of the argument: this is not a wall. Passing $f$ is not a human
judgment — it is bookkeeping the trace already holds and currently drops.
Walling it would put a judgment demand where no judgment exists, which is the
error §14 of the convention note diagnoses in the opposite direction.

---

## Part IV — Consequences

## 13. What no-lookup implies elsewhere

- **Entry grading stays local.** An entry's behaviour is a property of its
  text plus its declared parameters. Reviewable in isolation, which is what
  adversarial review presupposes.
- **Append stays safe.** Authoring NML2.1 entries cannot retroactively alter
  NML1 residuals. Required for demand-driven sequencing to be sound rather
  than merely intended.
- **Residues become comparable objects.** A residue's outcome distribution is
  a property of the residue. This is the precondition for the probability
  programme, not a refinement of it.
- **Level closure becomes checkable.** The dependence set of a residual is its
  own text plus its parameters, so "is this residual licensed at NML1" is a
  finite question.

## 14. Open questions

1. **Sigil form.** What marks a parameter, and how does the tokeniser
   distinguish it from the hyphen-reference convention and from ordinary
   punctuation? (§11.)
2. **Parameter list for `impressed-force`.** Instance is required; target is
   plausibly a trace-level constant rather than a per-node binding, since one
   trace builds one account. Undetermined until a trace is run on paper.
3. **Does any existing entry already require a frame?** The Newton set was
   authored under the assumption that all dependences were ignorable or
   monomorphised. If any entry's residual silently expects trace-generated
   data, it is currently relying on unrecorded reader memory — a milder form of
   the same defect, and an audit could find it.
4. **Is external competence bounded?** The rule permits the reader's own
   knowledge without limit. `5 + 1` assumes arithmetic. A residual could assume
   a great deal more. Whether the residual layer needs a *licensed competence
   set* per NML level is not settled here, but it is the natural next
   question — no-lookup closes the log and leaves the reader's head open.
5. **Enforcement.** No-lookup constrains an act, not an artifact, so no audit
   can detect a violation directly. Is there an indirect signal — e.g. a
   reduction whose claimed value is unreachable from the local text plus
   declared parameters?

---

## 15. Compact statement

The log may be read by the mechanism, at tracked positions, on request. It may
not be read by the reader mid-residual. Everything the reader legitimately
needs from the log is available by expansion, which records what lookup would
have hidden; and everything the reader legitimately needs from the *trace* is
available by frame, which is bounded, declared, and immune to later appends.

The prohibition is what makes a residue a property of its residual rather than
of the dictionary's current contents — and therefore what makes residues
countable, comparable, and licensable at all.

---

## Provenance

The rule is the user's, stated 2026-08-17 in rejection of a lookup-based
proposal I had made in the same discussion. The three-way failure decomposition
(§§2–4), the lookup-as-degraded-δ comparison (§5), the two-way wall framing
(§6), the identification of the implemented headword-scan and order-0 guards as
instances of the same rule (§8), and the frame/lookup monotonicity discriminant
(§10) are analysis added here. No entry wording is proposed. No file in
VD-Newton was read for or edited by this note. The parameter list of §14.2
remains open pending a hand-run gravity trace.
