# Bug Report: `forceful-inertial-acceleration` Domain Leak in the Photon Case

## Status

Open / unresolved.

This rewrite assumes the Design 3 headword split has already been introduced:

```text
free-inertial-acceleration
forceful-inertial-acceleration
```

So this is no longer primarily a bug about the old untyped headword:

```text
inertial-acceleration
```

The remaining bug is subtler. It occurs when a massless free-particle path-case, especially a photon, is accidentally admitted into the `forceful-inertial-acceleration` branch.

---

## Summary

Newtonian mechanics contains two different acceleration branches that must not be silently collapsed.

### Branch 1: free branch

```text
free-inertial-acceleration :=
  the acceleration obtained by differentiating the velocity read from the
  trajectory of a free-particle described in an inertial-frame.
```

For a free-particle in an inertial-frame, Newton I gives:

```text
free-particle + inertial-frame -> uniform-motion
uniform-motion -> constant velocity
constant velocity -> acceleration = 0
```

So:

```text
free-inertial-acceleration(free-particle) = 0
```

This branch may include massless free-particle path-cases, such as photons, if the VD allows photons to be treated as free-particles for path reasoning.

### Branch 2: forceful branch

```text
forceful-inertial-acceleration :=
  the acceleration of a massive particle in the Newton-II force-accounting domain.
```

Inside this branch, there are two routes that are supposed to coincide.

#### Route 2A: forceful trajectory route

```text
forceful-inertial-acceleration_trajectory :=
  the acceleration obtained by differentiating the velocity read from the
  trajectory of a massive particle described in an inertial-frame.
```

#### Route 2B: forceful Newton-II route

```text
forceful-inertial-acceleration_Newton-II :=
  net-force / inertial-mass
```

or:

```text
a = F_net / m
```

For ordinary massive Newtonian particles, these two routes are intended to agree:

```text
forceful-inertial-acceleration_trajectory(x)
  = forceful-inertial-acceleration_Newton-II(x)
```

but only when:

```text
x is a massive-particle
m(x) is defined
m(x) != 0
```

The bug occurs when a photon is allowed to enter this forceful branch.

---

## Minimal Reproduction: The `0 / 0` Case

This note focuses on the free-photon `0 / 0` case, not the gravitational `F / 0` case.

Assume:

```text
photon is a massless free-particle path-case
```

and:

```text
photon is described in an inertial-frame
```

Then the free branch permits:

```text
photon is a free-particle
free-particle + inertial-frame -> uniform-motion
uniform-motion -> constant velocity
constant velocity -> acceleration = 0
```

So:

```text
free-inertial-acceleration(photon) = 0
```

So far, there is no contradiction.

The bug appears only if the same photon is then admitted into the forceful branch and queried as though it has a forceful-inertial-acceleration.

Because the photon has a trajectory, the trajectory-style route may try to return:

```text
forceful-inertial-acceleration_trajectory(photon) = 0
```

This value is inherited from the path/free-motion reasoning.

But the Newton-II route asks for:

```text
forceful-inertial-acceleration_Newton-II(photon)
  = F_net(photon) / m(photon)
```

For a free photon in the `0 / 0` case:

```text
F_net(photon) = 0
m(photon) = 0
```

So the Newton-II route returns:

```text
forceful-inertial-acceleration_Newton-II(photon) = 0 / 0
```

which is undefined / indeterminate.

Therefore the illegally admitted photon produces:

```text
forceful-inertial-acceleration(photon) = 0
```

by the trajectory-style route, but:

```text
forceful-inertial-acceleration(photon) = undefined
```

by the Newton-II route.

If these are treated as the same headword without route typing, the VD has effectively produced:

```text
0 = undefined
```

or, more carefully:

```text
the same queried headword has been assigned both a value and a non-value.
```

That is the bug.

---

## What the Bug Is Not

This is not a claim that physics literally proves:

```text
0 = undefined
```

It is a VD routing failure.

The system has accidentally sent a massless free-particle path-case into a branch whose hidden domain is:

```text
massive-particle with defined nonzero inertial-mass
```

So the contradiction is not in reality. The contradiction is in the dictionary routing.

The photon is admissible as:

```text
massless free-particle path-case
```

but not as:

```text
Newton-II force-accounting massive-particle
```

unless an explicit modelling choice has been made to treat it as a massive corpuscle, which is not the massless photon case.

---

## Expected Behaviour

The VD should allow:

```text
free-inertial-acceleration(photon) = 0
```

when the photon is being used in the free branch as a free-particle trajectory case.

But the VD should not allow:

```text
forceful-inertial-acceleration(photon)
```

unless the photon has first passed the domain test for the forceful branch.

The forceful branch domain test should require something like:

```text
x is a massive-particle
inertial-mass(x) is defined
inertial-mass(x) != 0
```

For a photon:

```text
m(photon) = 0
```

or:

```text
inertial-mass(photon) is not a Newton-II massive-particle referent
```

Therefore the expected result is:

```text
forceful-inertial-acceleration(photon) = domain boundary
```

not:

```text
0
```

and not:

```text
0 / 0
```

The dispatcher should stop before either route tries to produce a value.

---

## Actual Behaviour

The unsafe behaviour is:

```text
photon -> free-particle path reasoning
photon -> acceleration from trajectory = 0
```

followed by:

```text
same photon -> forceful-inertial-acceleration query
```

followed by both:

```text
trajectory route -> 0
Newton-II route -> 0 / 0
```

This lets the photon borrow a value from the free branch while also being queried inside the massive-particle force-accounting branch.

The result is a branch collision:

```text
free branch output leaks into forceful branch query
```

and:

```text
forceful branch Newton-II route rejects the same object by producing 0 / 0
```

So the actual bug is not merely a naming bug. It is a domain-routing bug caused by a partially repaired naming system.

The old bug was:

```text
inertial-acceleration
```

being used for too many things.

The new bug is:

```text
forceful-inertial-acceleration
```

still containing two routes whose agreement silently assumes the massive-particle domain.

---

## Root Cause

The root cause is that `forceful-inertial-acceleration` is itself internally overloaded.

It names both:

```text
1. the acceleration read from the trajectory of a massive particle
```

and:

```text
2. the acceleration computed by net-force / inertial-mass
```

These two are equivalent only under the Newton-II admissibility condition:

```text
massive-particle + defined nonzero inertial-mass
```

For a normal massive particle:

```text
F_net = 0
m != 0
```

so:

```text
a = F_net / m = 0 / m = 0
```

and the trajectory route agrees:

```text
dv/dt = 0
```

No bug appears.

For a photon:

```text
F_net = 0
m = 0
```

so the Newton-II route becomes:

```text
a = 0 / 0
```

while the trajectory/free-motion route still tries to say:

```text
dv/dt = 0
```

The equality between the two routes has failed because its hidden type assumption was violated.

---

## Proposed Fix

Keep the implemented headword split:

```text
free-inertial-acceleration
forceful-inertial-acceleration
```

but add an explicit domain gate before `forceful-inertial-acceleration` can be queried.

Suggested rule:

```text
A query for forceful-inertial-acceleration(x) is valid only if x is admitted into
Newton-II force-accounting.
```

Newton-II force-accounting admission requires:

```text
x is a massive-particle
inertial-mass(x) is defined
inertial-mass(x) != 0
```

Then:

```text
forceful-inertial-acceleration(x)
```

may be computed by either route:

```text
trajectory route: dv/dt from the massive-particle trajectory
Newton-II route: F_net / m
```

and Newton II asserts their equality.

But if:

```text
x = photon
```

then:

```text
forceful-inertial-acceleration(photon)
```

must halt at:

```text
domain boundary
```

before either route returns a value.

---

## Recommended Entry Shape

### E7: `free-inertial-acceleration`

```text
free-inertial-acceleration :=
The acceleration obtained by differentiating the velocity read from the trajectory
of a free-particle described in an inertial-frame.
```

Allowed domain:

```text
free-particle path-cases
```

This may include:

```text
massive free-particles
massless free-particles, such as photons, if admitted by the VD
```

Newton I result:

```text
free-particle + inertial-frame -> free-inertial-acceleration = 0
```

### E8: `Newton-II-admissible-particle`

```text
Newton-II-admissible-particle :=
A point-particle admitted into the Newton-II force-accounting domain, for which
inertial-mass is defined and nonzero.
```

This is a domain bridge, not an acceleration headword.

It exists to prevent massless free-particle path-cases from being silently cast into the forceful branch.

### E9: `forceful-inertial-acceleration`

```text
forceful-inertial-acceleration :=
The acceleration of a Newton-II-admissible-particle, equivalently readable from
its massive-particle trajectory in an inertial-frame and computable from net-force
divided by inertial-mass.
```

Internal route equality:

```text
forceful-inertial-acceleration_trajectory(x)
  = forceful-inertial-acceleration_Newton-II(x)
```

provided:

```text
x is Newton-II-admissible
```

Newton-II formula:

```text
forceful-inertial-acceleration(x) = F_net(x) / m(x)
```

provided:

```text
m(x) is defined
m(x) != 0
```

---

## Why This Fix Works

For a photon in the free branch:

```text
photon -> free-particle
free-particle + inertial-frame -> uniform-motion
uniform-motion -> free-inertial-acceleration(photon) = 0
```

This is allowed.

But:

```text
photon -> Newton-II-admissible-particle
```

fails, because:

```text
m(photon) = 0
```

or:

```text
photon has no massive-particle inertial-mass referent
```

Therefore:

```text
forceful-inertial-acceleration(photon)
```

returns:

```text
domain boundary
```

rather than:

```text
0
```

or:

```text
0 / 0
```

So the VD no longer produces:

```text
0 = undefined
```

because the two outputs are no longer allowed to be outputs of the same valid query.

---

## Design Implication

The important design lesson is that the split:

```text
free-inertial-acceleration
forceful-inertial-acceleration
```

is necessary but not sufficient.

The `forceful-inertial-acceleration` headword still needs an explicit domain gate, because it contains two sub-routes:

```text
trajectory route
Newton-II route
```

and their equality is not type-free.

It holds only inside the massive-particle / Newton-II-admissible domain.

This is probably the first clear case where the Newton VD needs a formal routing rule of the following kind:

```text
Given a query H(x), first test whether x satisfies the domain of H.

If the domain test passes:
  evaluate H(x).

If the domain test fails:
  return domain boundary.

Do not evaluate sub-routes of H before the domain test passes.
```

This is stronger than ordinary inheritance.

Inheritance says:

```text
massive-particle inherits point-particle trajectory slots
```

But this bug shows that the reverse is not true:

```text
point-particle trajectory-bearer does not automatically inherit massive-particle
force-accounting slots
```

So the VD needs controlled branch admission, not just inheritance.

---

## NML1 / NML2 Consequence

NML1 can teach:

```text
free-inertial-acceleration
```

as a path-facing idea:

```text
free-inertial-acceleration :=
acceleration read from the trajectory of a free-particle in an inertial-frame.
```

NML1 should not yet teach:

```text
forceful-inertial-acceleration = F_net / m
```

because that belongs to the Newton-II force-accounting branch.

So the lesson boundary becomes:

```text
NML1 teaches:
  path
  trajectory
  point-particle
  free-particle
  inertial-frame
  uniform-motion
  free-inertial-acceleration
```

```text
NML2 teaches:
  Newton-II-admissible-particle
  massive-particle
  net-force
  inertial-mass
  forceful-inertial-acceleration
  forceful-inertial-acceleration = F_net / m
```

This keeps the NML1 boundary clean while preserving the photon/free-particle path-case.

---

## Open Questions

1. Should `Newton-II-admissible-particle` be the actual bridge headword, or should the VD use a less formal name such as:

   ```text
   force-accounting-particle
   ```

2. Should `forceful-inertial-acceleration` explicitly include two labelled sub-routes in the entry, or should one route be treated as the definition and the other as the Newton-II law relation?

3. Should a photon have:

   ```text
   inertial-mass(photon) = 0
   ```

   or should the VD say:

   ```text
   inertial-mass(photon) is not a Newton-II massive-particle referent
   ```

   The second wording may avoid accidentally making `0 / 0` look like a valid calculation rather than a failed domain query.

4. Should `free-inertial-acceleration(photon) = 0` be taught as a Newton I result, or as a VD-specific extension of Newton I to massless free-particle path-cases?

5. Should the dispatcher return:

   ```text
   undefined
   ```

   or:

   ```text
   domain boundary
   ```

   when `forceful-inertial-acceleration(photon)` is queried?

   Current preference: return `domain boundary`, because the calculation should not begin.

---

## Current Best Judgment

The bug is best described as:

```text
A massless free-particle path-case is illegally admitted into the forceful branch.
```

Once admitted, the photon can produce:

```text
0
```

from the trajectory/free-motion route, while the Newton-II route produces:

```text
0 / 0
```

So the apparent contradiction:

```text
0 = undefined
```

is not a physical result. It is a dictionary-routing error.

The correct repair is not to remove photons from the free branch. The correct repair is to prevent photons from entering the forceful branch unless a separate modelling choice explicitly changes their domain status.

Final rule:

```text
free-inertial-acceleration(photon) may be defined.
forceful-inertial-acceleration(photon) must halt at domain boundary.
```

That preserves both insights:

```text
Newton I / NML1 can discuss massless free-particle path behaviour.
Newton II / NML2 can compute forceful acceleration only for massive-particle
force-accounting cases.
```
