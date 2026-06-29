# Design Note: Two `inertial-acceleration` Entries, Differentiated by Relation to the Second Law

## Status

Resolved design decision. Supersedes the earlier "headword collision" bug report,
whose framing (domain routing, photon contradiction, polymorphic dispatch) is
retracted. See **Retraction** below.

---

## 1. The finding

The Newton instance needs **two** `inertial-acceleration` entries, not one. They are
distinguished not by what kind of object exhibits them, and not by frame, but by a
single difference in definitional content:

```text
free-particle inertial-acceleration:
  read from the particle-trajectory; stands in no relation to net-force.

massive-particle inertial-acceleration:
  read from the particle-trajectory AND equal to net-force / inertial-mass.
```

The second entry carries one definitional commitment the first lacks: an edge into
the Newton II triplet. The free-particle acceleration has no such edge. That single
structural difference is the whole reason they are two headwords rather than one.

They are only contingently equal in value. For a massive Newtonian particle the
trajectory-read acceleration and the F/m quantity land on the same number — but that
coincidence is a *result* of Newtonian mechanics, not a definitional identity. The
dictionary names by definition, not by value, so it must keep them apart and let the
equality be earned in the massive case rather than assumed everywhere.

---

## 2. Why the differentiator is internal, not a domain tag

The distinguishing predicate — "is also equal to F/m" — is a property of the
*acceleration*, available by asking which entry you are in. It is **not** a property
of the witness object that must be inspected at trace time.

This matters because it means no domain machinery is required:

- No `massive-particle` *domain* needs to be defined in order to route the headword.
- No dispatcher keyed on properties of `x` is needed.
- No "most specific applicable domain" resolution rule is needed.

You never ask "is this object massive?" You ask "does this acceleration stand in the
Newton II relation?" — and that is answered by which entry the trace is expanding,
which is a fact about the graph, not about the particle.

This is the VD's native move: **distinguish by definitional role, not by witness
type.** It is also why the earlier domain-typed proposal was the wrong mechanism even
though it reached the right conclusion (two entries). Domain typing drags in
apparatus the definitional-role cut dissolves entirely.

---

## 3. The two entries

Provisional names; see Open Question 1 on naming.

```text
free-particle inertial-acceleration :=
The acceleration read from a free-particle's particle-trajectory when that
trajectory is described in an inertial-frame.
```

```text
massive-particle inertial-acceleration :=
The acceleration read from a massive-particle's particle-trajectory when that
trajectory is described in an inertial-frame, which for a massive-particle is
also the Newton II quantity equal to net-force divided by inertial-mass.
```

The relationship between them is **containment plus one commitment**, not disjoint
domains. The massive entry has all the content of the free entry (trajectory-read,
inertial-frame-qualified) and adds the Newton II edge. The free entry is the
weaker of the two; the massive entry strengthens it.

---

## 4. Append-only ordering falls out for free

Because the differentiator is the Newton II edge, the two entries sit naturally at
different points in the log, and the append-only rule is satisfied without
contrivance:

```text
Newton I block:
  free-particle inertial-acceleration is born here.
  No force vocabulary is in scope yet — none is needed, because this entry
  stands in no relation to net-force.

Newton II triplet:
  net-force and inertial-mass are born here as the winter words.
  massive-particle inertial-acceleration can now be stated, because F/m is
  finally available to supply the differentiating commitment.
```

The free-particle entry cannot accidentally reach into Newton II, because at the
point it is born the force vocabulary does not yet exist. The massive-particle
entry cannot be stated too early, because it requires terms the II triplet has not
yet introduced. The ordering constraint and the definitional cut agree.

This also means the Newton I lesson boundary is preserved and merely gains one entry:

```text
Newton I teaches:
  path, particle-trajectory, free-particle, inertial-frame, uniform-motion,
  free-particle inertial-acceleration.

Newton II teaches:
  net-force, inertial-mass, massive-particle inertial-acceleration.
```

---

## 5. What this does to the photon, and why the photon was never the point

Under the two-entry cut there is no contradiction to resolve, because there was
never a single value that came out two ways.

A photon, if a human modeller admits it as a free-particle in the Newtonian instance
(itself a wall-level modelling decision, not an automatic trace step), has a
trajectory and therefore a `free-particle inertial-acceleration`. That entry stands
in no relation to net-force, so nothing about mass is invoked and nothing is
undefined.

The photon never reaches `massive-particle inertial-acceleration`, because that
entry is a statement about massive-particles and the photon is not one. There is no
F/m computation to attempt, so no `0/0` and no "undefined." Newton II simply has no
satisfying assignment for the photon — the law does not apply, which is the correct
outcome, not a fault.

The earlier report's `0 = undefined` arose only from forcing one headword to serve
both roles and then running a massless case through the merged entry. With two
entries the question never forms. The genuine witness for the distinction is the
**ordinary massive particle**, where the equality of the trajectory acceleration and
F/m is a Newtonian result the dictionary should make you earn. The photon is a
dramatic illustration at best and a red herring at worst.

---

## 6. Retraction of the earlier bug report

The prior note, *Bug Report: `inertial-acceleration` Headword Collision Between
Newton I and Newton II Routes*, reached the correct conclusion — two entries — by an
incorrect mechanism. For the record, the following parts of it are withdrawn:

- **The "routing bug" framing.** There is no routing bug. There is a definitional
  distinction the single-entry dictionary failed to record.

- **The photon contradiction as the motivating case.** The contradiction was an
  artifact of the merged entry, not evidence of a routing failure. The motivating
  case is the ordinary massive particle.

- **The `_point-particle` / `_massive-particle` headword encoding.** This encodes a
  *domain* into the headword string. The correct cut is by relation-to-the-second-law,
  not by object domain.

- **The E7 / E8 / E9 three-entry structure with an intermediate "bridge" entry.**
  The bridge entry (E8) did no work that the triplet-facing entry did not, and as
  written it duplicated the massive headword, reintroducing the very collision one
  level down. There are two entries, not three.

- **The polymorphic query-normalisation rule** ("choose the most specific typed
  headword whose domain `T` is satisfied by `x`"). This is multiple dispatch keyed on
  the witness, placed upstream of the wall. It contradicts the standing principle
  that dispatch is residual, and the definitional-role cut makes it unnecessary.

- **Open questions 2 and 3** (whether to introduce `massive-particle` before Newton II,
  how to define it without `inertial-mass`). These exist only if the differentiator is
  a domain. It is not, so they dissolve.

What survives from the original is the one-line finding and the recognition that the
kinematic and dynamical accelerations are structurally distinct — which is the same
distinction already recorded elsewhere as raw-vs-inertial acceleration, here
reappearing at the free-vs-massive layer.

---

## 7. Open questions

1. **Naming.** "free-particle inertial-acceleration" and "massive-particle
   inertial-acceleration" are functional but verbose. The word "inertial" in the free
   case is arguably misleading, since that acceleration's only qualification is the
   frame, not any relation to inertia. A candidate for the free case is
   `inertial-frame-acceleration_particle-trajectory`; clunkier, but it removes the
   Newton II connotation that helped create the original confusion. Open whether the
   shared stem `inertial-acceleration` should be kept for readability at the cost of
   that connotation.

2. **`uniform-motion -> acceleration = 0` scope.** This should fire only where the
   acceleration headword is defined over the trajectory in question. Where the entry
   has not yet been born for a route, "= 0" is a category error rather than a true
   statement. Worth confirming this is enforced, as it independently closes off the
   spurious `free-particle inertial-acceleration(photon) = 0` step in any route where
   the entry is not in scope.

3. **Six-entry placement.** Confirm how the two entries distribute across the
   chimney/triplet/wall structure of the Newton II house. The
   `massive-particle inertial-acceleration` entry's relation to the Newton II triplet
   corner (triplet-facing vs wall-facing) should be pinned down so the headword does
   not collapse two structural roles — the degree-contamination pattern this note is
   otherwise careful to avoid.
