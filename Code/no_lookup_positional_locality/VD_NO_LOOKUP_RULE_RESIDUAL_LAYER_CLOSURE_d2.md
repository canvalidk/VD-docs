# The No-Lookup Rule

## Positional Locality of raw_meaning, and Why Arguments Are Admissible Where Memory Is Not

**Status:** working note, d2. Claude-authored at user request, 2026-08-17.
**Supersedes:** `VD_NO_LOOKUP_RULE_RESIDUAL_LAYER_CLOSURE_d1.md` (same day).
d1 stated the rule with the wrong discriminant — log-vs-trace instead of
positional — and consequently mislocated both the failure mode and the
boundary. See Part V for what changed and why.
**Origin:** the rule is the user's (2026-08-17 discussion), stated in
rejection of a lookup-based proposal I had made; the correction from
log-locality to positional locality is likewise the user's, in rejection of
the trace-memory scope d1 left open.
**Bears on:**

- `Newton-analysis/canonical_force_orientation/CANONICAL_FORCE_ORIENTATION_CONVENTION_DISCOVERY_2026-08-14_d1.md`
- `Newton-analysis/participant_symmetric_forces/VD_PARTICIPANT_SYMMETRIC_CANONICAL_ORIENTATION_MESHING_d2.md`
- `specs/2026-06-10-vd-reduction.md`, `specs/2026-06-10-vd-residual-cleanup.md`

---

## 0. The rule

> **Positional locality.** A residue is a handle for its own raw_meaning.
> Therefore
>
> $$\text{raw\_meaning}(R) \quad\text{— a function of } R \text{ alone.}$$
>
> A reader executing residual $R$ may draw on the local text of $R$ and on
> their own external competence. Their behaviour may not depend on text at any
> other position — not elsewhere in the log, and **not elsewhere in the same
> trace**.

Reaching outward for a datum is forbidden regardless of how far the reach goes.
The log is the flagrant case. Trace memory is the quiet one, and it is the same
violation.

---

## Part I — Why

## 1. The rule is about exercise, not access

Consider a reader with lookup enabled who never reads the material they could
look up. No residue is corrupted. Every probability remains trackable. The
capability was present and unexercised, and nothing broke.

So the rule was never about access. **It is about behavioural dependence on
text at another position.** What corrupts a residue is remembered material
altering execution — and the alteration being non-local.

This is the criterion, and everything below follows from it.

## 2. The handle argument

A residue is a handle for a raw_meaning. If executing $R$ requires text the
reader absorbed at position $P \neq R$, then

$$\text{raw\_meaning}(R, \text{context})$$

has a second argument, and $R$ does not determine what it handles. It is not a
handle. It is half of one, with the other half in the reader's head and no
record of which half.

Everything in §§3–5 is a symptom of that second argument. The failures differ
in visibility, not in kind.

## 3. Symptom — retroactive revision (log scope)

The flagrant case. A reader reaches `5 + 1`. Elsewhere in the log:

```text
Every time you see + interpret that as a * instead.
```

`5 + 1` reduces to `5`. Nothing about the residual changed; a different
position said so.

The log is append-only, and the intended strength of that commitment is that
**appending never revises**. Under lookup, the `+ → *` entry's arrival silently
changes the value of every residual containing `+`, including residuals
authored, executed and graded before it existed. Every append becomes a
potential retroactive edit of the whole corpus, with no diff.

Note what makes this case *easy*: the symptom is visible. d1 mistook this
symptom for the disease.

## 4. Symptom — non-local dependence with no symptom (trace scope)

A reader admits acting-object $ao_1$ at the IFS wall. Six steps later they
unfold `impressed-force` and use their memory of $ao_1$ to select the
operation.

Nothing appended to the log can reach this. No retroactive revision occurs. The
datum is trace-local and licensed at whatever level the trace runs. Every test
d1 proposed is passed.

And it is the same violation. Execution at the `impressed-force` position
depends on text at the IFS-wall position. $\text{raw\_meaning}$ has two
arguments. The residue is not a handle.

**Bounded memory is still memory.** "One step up" is a smaller second argument,
not the absence of one.

This case is worse than §3 precisely because it produces no symptom. It cannot
be caught by an append-monotonicity test, and it is the current status quo of
every Newton trace that passes a member down the pipeline.

## 5. Consequences of the second argument

Both scopes, once the second argument exists:

- **Entries stop being gradeable in isolation.** The determining object is
  (residual, context), so knowing what an entry does requires knowing what the
  reader read. Adversarial review of a single entry presupposes the opposite.
- **Residues stop being comparable.** A residue's outcome distribution is
  supposed to be a property of the residue — that is what makes "the
  probability of this residue" well-formed. With a second argument it is a
  property of a (residue, context) pair. Two readers executing the same
  residual under different histories are not running the same experiment.
- **Levels stop being closable.** Licensing requires that a residual's
  dependence set be finite and level-bounded. Under log scope the dependence
  set is the whole dictionary; under trace scope it is the whole trace prefix.
  Neither is checkable, and *supply freely what will later be ratified; never
  supply what will later be revoked* becomes unenforceable.

## 6. Lookup is δ done wrongly

The prohibition on log access costs nothing, because **anything in the log is
already reachable by expansion.**

| | δ (expansion) | Lookup |
|---|---|---|
| Position | tracked hole | none |
| Record | trace event | none |
| Scope | the headword named at that position | the whole log |
| Licensing | checkable at the level | uncheckable |
| Reversible | yes (`unresolve`) | nothing to reverse |

Same information, no provenance. There is no legitimate need lookup serves that
expansion does not serve better.

The trace-scope case has no equivalent escape — nothing existing legalises
reading an earlier position — which is why it needs a mechanism rather than a
prohibition. Part III.

---

## Part II — Placement in the architecture

## 7. The wall is two-way

The VD already holds the converse rule:

> The mechanical layer never consults the reader's judgment. Tokenisation,
> dependency graphs, cycle detection, audits and degree computation run without
> asking anyone anything.

Positional locality is the same wall from the other side:

```text
mechanical layer  --/-->  reader's judgment       (long-standing; e.g. "no
                                                   equivalence checking" —
                                                   reduction spec §10)

reader's judgment --/-->  text at other positions (this note; log AND trace)
```

Both crossings are forbidden symmetrically. The mechanical layer must not
import judgment or its audits stop being audits. The residual layer must not
import non-local text or its residues stop being handles.

Contact happens at exactly three designed interfaces: **walls** (reader supplies
a value the mechanism demands), **expansion** (mechanism unfolds a name the
reader requests), and **argument delivery** (mechanism places a datum at the
site before execution — Part III). Nothing else crosses.

## 8. What the residual layer may use

Positively stated, and this is the list d1 got wrong by omission:

- the **local text** of the residual, including latents;
- the reader's own **external competence** — arithmetic, vector algebra,
  physical intuition, ordinary language;
- **arguments delivered to that position** (§§10–12).

Not permitted: the log; earlier positions in the same trace; the reader's
memory of either.

The second item is the point of the residual layer — it is where the
interpretive bridge lives, and its content is the reader's, not the
dictionary's. It is also the one remaining unbounded scope; see §17.5.

## 9. The rule generalises guards already implemented

Not a new species of restriction. Two implemented guards are instances of it,
and recognising them as such is better evidence for the rule than any argument
here.

**Headword scan on reduced and cleaned text.** Human-supplied text is scanned
and an unescaped headword token rejected — `reduction spec §5`, `cleanup
spec §3`. Rationale at the time: a headword-shaped string in the render must
*be* a tracked reference. Read under this note: the residual layer is being
prevented from creating an untracked dependence on another position.

**Order-0 by fiat.** Reduced text is never `analyse`d; no holes spawn from it;
the graph cannot grow through the backwards pass — `reduction spec §2`. Read
under this note: human-supplied text may not open new non-local references at
all.

Both were justified locally. They are the same rule applied to the two surfaces
where human text enters. This note states the general form and extends it from
the reader's *text* to the reader's *behaviour*.

---

## Part III — The boundary: arguments are not memory

## 10. Why the question arises

`impressed-force` — the third corner of the candidate Force-Sum triplet — is
the first VD headword that is a **function of an argument the reader must
hold**. Earlier dependences were safe in two ways:

- `net-force(t)` — the parameter is decoration; δ succeeds without consulting
  it;
- `inertial-acceleration_point-particle` — the argument is monomorphised into
  the name; δ succeeds by identity.

`V(f)` is neither. Which operation the reader performs — quoted or negated,
which instance, which target — depends on $f$'s value. Member and kind
monomorphise (`action-force_gravity`); **instance cannot**, because instances
are trace-generated, and per the meshing note §13 instance identity is exactly
what distinguishes two equal-valued gravity members on one target.

So a residue of $f$ must reach the unfolding site. Every candidate mechanism is
now excluded except one.

## 11. The discriminant: pull versus push

| Mechanism | Direction | Verdict |
|---|---|---|
| Consult the log | pull | forbidden (§3) |
| Recall an earlier trace position | pull | forbidden (§4) |
| Read the resolution one position up | pull, bounded | forbidden — bounded memory is memory |
| Re-supply at a second wall | — | rejected (§13) |
| Monomorphise into the headword | push, authoring-time | admissible, but cannot hold instances |
| **Deliver as an argument** | **push, trace-time** | **admissible** |

Pull mechanisms have the reader reach outward from the site, so the site does
not determine execution. Push mechanisms place the datum **at** the site before
execution begins.

The consequence is the whole point: **a delivered argument becomes part of the
handle.** The residual is not `V(f)` with a dangling $f$; the handle is $V$ *at*
$a$, with $a$ present in the local text. Nothing is remembered because nothing
is absent. $\text{raw\_meaning}$ has one argument again — a larger one, and
still one.

Arguments are therefore not a relocation of the violation. They are the only
mechanism that **restores** positional locality rather than shrinking the
breach.

## 12. Arguments and monomorphisation are one operation

Both partition the residue space, and each partition cell is a handle with its
own raw_meaning and its own distribution:

```text
finite domain, known at authoring time  -> put it in the name
    action-force_gravity, action-force_spring
    (separate handles, separate residues, already implemented via underscore)

domain generated at trace time          -> deliver it as an argument
    impressed-force at (instance, target)
    (separate handle per argument value; residue tracked per cell)
```

So the probability object is never $P(\text{residue of } V)$. It is
$P(\text{residue of } V \text{ at } a)$. Monomorphisation is partial evaluation
at authoring time; argument delivery is the same partition where the domain
cannot be enumerated in advance. One mechanism, two regimes.

## 13. Rejected alternative: re-supply at a second wall

The option needing no code: have the reader state the instance again at the
`impressed-force` site.

Rejected. The same datum enters twice with nothing checking the two mentions
agree — an unauditable coreference error with a human in the middle, which is
the error class this corpus can least afford, given that the canonical-
orientation result turns entirely on getting member/recipient pairing right.

Note the shape: this is **not** a wall. Passing the instance is not a human
judgment; it is bookkeeping the trace already holds and currently drops.
Walling it would place a judgment demand where no judgment exists — the mirror
of the error the convention note §14 diagnoses in the other direction.

## 14. Delivery semantics, storage freedom

Push describes what the reader sees, not how it is stored. Store the binding on
the `Demand` node; have the **render** compose it into the text at that
position. The reader receives a self-contained site; the stored `Definiens`
stays immutable and shared, preserving the Phase-3 commitment. Serialisation is
`(path, param, value)` — the address-keyed shape reduction spec §8 already
established.

The frame-versus-substitution question is about storage and is orthogonal to
push-versus-pull.

## 15. The condition, or lookup returns by the back door

> **The parameter sigil must be a tokeniser primitive, never a headword.**

If a parameter name could be defined in the log, an entry could redefine what
parameters mean and the `+ → *` failure reappears one level down — inside the
mechanism rather than in a residual. The sigil must be recognised by the
tokeniser and definable by no one.

This also keeps it distinct from the hyphen-as-reference prototype, which marks
the opposite thing: an opt-in reference *into* the log. Two sigils, two
directions, and they must not be confusable.

---

## Part IV — Consequences

## 16. What positional locality implies elsewhere

- **Entry grading stays local.** An entry's behaviour is a property of its text
  plus its declared parameters. Reviewable in isolation, which adversarial
  review presupposes.
- **Append stays safe.** Authoring NML2.1 entries cannot retroactively alter
  NML1 residuals — required for demand-driven sequencing to be sound rather
  than merely intended.
- **Residues become comparable objects.** Each (handle, argument value) cell
  has a distribution that is a property of the cell. Precondition for the
  probability programme, not a refinement of it.
- **Levels become closable.** A residual's dependence set is its own text plus
  its delivered arguments. Finite, and checkable against a level.
- **Existing Newton traces are suspect.** Any trace that passes a member down
  the pipeline by reader memory is in violation. §4 is not a hypothetical.

## 17. Open questions

1. **Sigil form.** What marks a parameter, and how does the tokeniser
   distinguish it from the hyphen-reference convention and from ordinary
   punctuation? (§15.)
2. **Parameter list for `impressed-force`.** Instance is required. Target is
   also required: d1 reasoned that one trace builds one account so the target
   is a trace-level constant, but a constant the reader carries across the
   trace and consults at each site is exactly §4's violation. So
   `{instance, target}`, pending a hand-run trace to confirm nothing further
   is needed.
3. **Which existing entries already require delivery?** The Newton set was
   authored assuming all dependences were ignorable or monomorphised. Any entry
   whose residual silently expects trace-generated data is currently running on
   reader memory. An audit could find these: look for residuals whose claimed
   reduction is unreachable from local text plus external competence.
4. **Is the argument list itself level-licensed?** Delivering `{instance,
   target}` presupposes those concepts are licensed where the entry is used. If
   an NML2 entry needs an NML3 argument, that is a licensing violation
   expressed through arity — a new failure mode worth naming.
5. **Is external competence bounded?** The rule permits the reader's own
   knowledge without limit. `5 + 1` presumes arithmetic; a residual could
   presume much more. Whether the residual layer needs a *licensed competence
   set* per level is not settled here. It is the remaining unbounded scope:
   positional locality closes the log and the trace, and leaves the reader's
   head open.
6. **Enforcement.** Positional locality constrains behaviour, not artifacts, so
   no audit detects a violation directly — and per §4 the trace-scope case has
   no symptom at all. The §17.3 signal (claimed reduction unreachable from
   local material) is the only indirect handle identified so far.

---

## 18. Compact statement

A residue is a handle for its own raw_meaning, so raw_meaning must be a
function of the residue alone. Any dependence on text at another position gives
it a second argument and destroys the handle — whether that position is in the
log or earlier in the same trace, and whether or not the dependence leaves a
visible symptom.

Everything the reader legitimately needs from the log is available by
expansion, which records what lookup would hide. Everything the reader
legitimately needs from the trace must be **delivered to the site** as an
argument, which makes it part of the handle rather than part of the reader.

That is what makes residues countable, comparable, and licensable at all.

---

## Part V — What changed from d1

## 19. The wrong discriminant, and the argument that replaced it

d1 stated the rule as **log-locality**: the reader may not consult the log, but
may read the trace's own history. Part III of d1 then defended a "frame"
mechanism on exactly that basis, with append-monotonicity as the test, and
proposed a cheaper "depth-1 positional access" variant — read the resolution of
the position you were expanded into.

The user's correction (2026-08-17): consider a reader with lookup enabled who
never reads what they look up. Nothing is corrupted. The rule therefore
concerns behavioural dependence on non-local text, not access to it — and by
that criterion remembering earlier trace text is *mathematically equivalent to
lookup*, because a residue is a handle for its raw_meaning and remembering
gives raw_meaning a second argument.

Specific retractions and repairs:

- d1 §0 (the rule, as a prohibition on consulting the log) — **replaced** by
  positional locality over all positions (§0).
- d1 §§2–4 (three co-equal failure modes: locality, monotonicity, licensing) —
  **restructured**: the disease is the second argument (§2); the three are
  symptoms differing in visibility (§§3–5). Append-sensitivity is demoted from
  criterion to symptom, and explicitly noted as the symptom that misled d1.
- d1 §7 (what the residual layer may use) — **corrected**: d1 listed local text
  and external competence, silently omitting trace memory, which is therefore
  neither permitted nor excluded. d2 excludes it by name (§8).
- d1 §10 (frame/lookup discriminated by append-monotonicity) — **withdrawn**;
  replaced by pull-versus-push (§11). Monotonicity cannot discriminate, because
  trace memory passes it.
- d1's "depth-1 positional access" as the cheap starting mechanism —
  **withdrawn**: bounded memory is memory (§11).
- d1's treatment of target as a trace-level constant needing no delivery —
  **withdrawn** (§17.2); a constant carried across the trace is the §4
  violation.
- d1 §13's list of implications — **retained**, plus the finding that existing
  Newton traces are in violation (§16).
- New: arguments as *restoration* of locality rather than a permitted breach
  (§11); the identification of monomorphisation and argument delivery as one
  partition operation over the residue space (§12); delivery-versus-storage
  separation (§14); the argument-list licensing question (§17.4).

---

## Provenance

The rule and its correction are both the user's, stated 2026-08-17 in rejection
of two successive proposals of mine (lookup, then bounded trace access). The
symptom decomposition (§§2–5), the lookup-as-degraded-δ comparison (§6), the
two-way wall framing (§7), the identification of the implemented headword-scan
and order-0 guards as instances of the same rule (§9), the pull/push
discriminant (§11), and the monomorphisation-as-partition reading (§12) are
analysis added here. No entry wording is proposed. No file in VD-Newton was
read for or edited by this note. The parameter list of §17.2 remains open
pending a hand-run gravity trace.
