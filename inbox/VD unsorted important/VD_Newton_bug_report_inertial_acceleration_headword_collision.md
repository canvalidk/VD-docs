# Bug Report: `inertial-acceleration` Headword Collision Between Newton I and Newton II Routes

## Status

Open / unresolved.

## Summary

The current Design 2.1 / Design 3 transition appears to contain a domain-routing bug around the headword `inertial-acceleration`.

The problem is that `inertial-acceleration` is currently being used for two different roles:

1. A **kinematic / frame-qualified acceleration** route:

   ```text
   acceleration of a point-particle trajectory described in an inertial-frame
   ```

2. A **Newton II / force-accounting acceleration** route:

   ```text
   acceleration related to net-force and inertial-mass
   ```

These routes coincide for ordinary massive Newtonian particles, but they do not coincide for massless free-particle path-cases such as photons.

This creates a contradiction if a photon is allowed through the Newton I path route and then later queried through the Newton II acceleration route.

---

## Minimal Reproduction

Assume the current Newton I branch allows a photon to be treated as a free-particle or free-body for path questions.

Then the following route is permitted:

```text
photon is a free-particle
free-particle + inertial-frame -> uniform-motion
uniform-motion -> constant velocity
constant velocity -> acceleration = 0
E7 inertial-acceleration := acceleration in an inertial-frame
therefore inertial-acceleration(photon) = 0
```

But if the same headword is later expanded through Newton II:

```text
E8 inertial-acceleration := net-force / inertial-mass
```

then for a photon:

```text
inertial-mass(photon) is undefined
```

or, if photons are treated as point-particles with zero mass:

```text
inertial-acceleration(photon) = 0 / 0
```

So the same headword produces:

```text
inertial-acceleration(photon) = 0
```

and also:

```text
inertial-acceleration(photon) = undefined
```

This yields the contradiction:

```text
0 = undefined
```

---

## Expected Behaviour

The VD should not allow the same headword to produce both a value and an undefined referent for the same object under different expansion routes.

Instead, the system should distinguish:

```text
kinematic/frame acceleration route
```

from:

```text
Newton-II force-accounting acceleration route
```

The photon should be allowed to route through the Newton I path branch, but should not be silently admitted into the Newton II massive-particle force-accounting branch.

Expected behaviour:

```text
inertial-acceleration_point-particle(photon) = 0
```

if this is defined as the frame-qualified kinematic acceleration of a point-particle trajectory.

But:

```text
inertial-acceleration_massive-particle(photon) = domain boundary / undefined referent
```

because the photon is not in the massive-particle / inertial-mass domain.

No contradiction should be produced, because these are different typed headwords.

---

## Actual Behaviour

The current untyped or under-typed use of `inertial-acceleration` risks collapsing two distinct routes into one headword:

```text
inertial-acceleration
```

This makes the dictionary equate:

```text
acceleration of a trajectory in an inertial-frame
```

with:

```text
Newton-II acceleration related to net-force and inertial-mass
```

These are equivalent only inside the massive-particle Newtonian domain.

Outside that domain, especially for massless path-cases, the equivalence fails.

---

## Root Cause

The root cause is a headword collision caused by insufficient domain typing.

The VD currently treats `inertial-acceleration` as though it can serve both as:

```text
E7: outward / wall-facing / chimney-style kinematic bridge
```

and:

```text
E8: inward / triplet-facing Newton II law corner
```

without distinguishing the object domain.

But the Newton I branch can apply to point-particle path-cases more broadly than the Newton II branch can apply to force-accounting particles.

In other words:

```text
Newton I route:
  point-particle / free-particle / massless-free-particle path reasoning

Newton II route:
  massive-particle / inertial-mass / net-force reasoning
```

These are not the same domain.

---

## Proposed Fix

Introduce typed headwords that separate the two routes.

Suggested structure:

```text
E7 inertial-acceleration_point-particle :=
The acceleration read from a point-particle's particle-trajectory when that
trajectory is described in an inertial-frame.
```

```text
E8 inertial-acceleration_massive-particle :=
The inertial-acceleration_point-particle of a point-particle when that
point-particle is admitted to the massive-particle / Newton-II force-accounting
domain.
```

```text
E9 inertial-acceleration_massive-particle :=
For a massive-particle, inertial-acceleration_massive-particle is the Newton II
quantity related to net-force and inertial-mass.
```

Under this fix:

```text
E7 = kinematic / frame-qualified / point-particle-facing
E8 = wall-facing bridge into massive-particle domain
E9 = triplet-facing Newton II entry
```

This pushes the Newton II triplet entry down by one slot and adds an intermediate domain-specialisation entry.

---

## Why This Fix Works

The proposed split prevents the photon route from reaching Newton II accidentally.

For a photon:

```text
photon -> free-particle path-case
photon -> point-particle trajectory route
photon -> inertial-acceleration_point-particle = 0
```

But:

```text
photon -> inertial-acceleration_massive-particle
```

halts at a domain boundary, because the photon is not a massive-particle and has no inertial-mass referent in the Newton II route.

So the VD returns:

```text
inertial-acceleration_point-particle(photon) = 0
```

and:

```text
inertial-acceleration_massive-particle(photon) = undefined / not applicable
```

These are not contradictory because they are different typed headwords.

---

## Design Implication

This appears to be the first clear case where the Newton VD needs something like polymorphic headword resolution.

Previously, the relation between point-particles and massive-particles could be treated mostly as inheritance:

```text
massive-particle inherits point-particle kinematic slots
```

But this bug shows that inheritance alone is not enough.

The same ordinary-language query:

```text
What is the inertial acceleration?
```

may need to resolve to different typed headwords depending on the witness domain:

```text
inertial-acceleration_point-particle
inertial-acceleration_massive-particle
```

This suggests a future need for an explicit polymorphic query-normalisation rule:

```text
Given a query H(x), choose the most specific typed headword H_T(x)
whose domain T is satisfied by x.
```

Possible resolution rule:

```text
If no typed headword applies:
  return domain boundary.

If exactly one typed headword applies:
  use it.

If multiple typed headwords apply:
  choose the most specific applicable domain.

If multiple incomparable typed headwords apply:
  return ambiguity or require model choice.
```

---

## NML1 Consequence

NML1 can still teach E7, but only as the point-particle / trajectory-facing entry:

```text
inertial-acceleration_point-particle :=
acceleration read from a point-particle trajectory in an inertial-frame
```

NML1 should not yet teach the massive-particle Newton II route.

So the lesson boundary becomes:

```text
NML1 teaches:
  path
  trajectory
  free-particle
  inertial-frame
  uniform-motion
  inertial-acceleration_point-particle

NML2 teaches:
  inertial-acceleration_massive-particle
  net-force
  inertial-mass
  Newton II
```

This preserves the existing NML1 boundary before force while still letting the lesson add one more entry.

---

## Open Questions

1. Should `inertial-acceleration_point-particle` be called exactly that, or should it use a less Newton-II-sounding name such as:

   ```text
   inertial-frame-acceleration_particle-trajectory
   ```

2. Should `massive-particle` be introduced before Newton II, or should the VD use a neutral pre-Newton-II domain name such as:

   ```text
   force-accounting-particle
   ```

3. If `massive-particle` is introduced before Newton II, how do we avoid defining it using `inertial-mass` before `inertial-mass` is born in the Newton II triplet?

4. Should there be a general VD rule for polymorphic headword resolution, or should typed headwords remain explicit with no dispatcher?

5. Does `uniform-motion -> acceleration = 0` apply to all point-particle trajectories, or only to trajectories for which the acceleration headword is explicitly defined?

---

## Current Best Judgment

The contradiction should not be patched by simply changing E7 to:

```text
inertial-acceleration :=
acceleration of a massive point-particle in an inertial-frame
```

That would avoid the contradiction, but it would lose the useful NML1 kinematic bridge.

A better fix is to split the headword domain:

```text
inertial-acceleration_point-particle
```

for the NML1 / Newton I / path route, and:

```text
inertial-acceleration_massive-particle
```

for the NML2 / Newton II / force-accounting route.

This preserves both insights:

```text
Newton I can discuss path behaviour for massless free-particle cases.
Newton II should only compute acceleration in the massive-particle force-accounting domain.
```
