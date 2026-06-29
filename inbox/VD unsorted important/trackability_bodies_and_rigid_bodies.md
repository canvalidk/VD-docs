# Trackability, Bodies, and Rigid Bodies

## Purpose

This short note introduces `trackability` as the bridge between physical bodies and point-particle trajectories.

The point is to avoid treating a point-particle as if it were automatically a tiny physical body.

Instead:

```text
point-particle = mathematical track-carrier
physical body = extended thing whose motion must first become trackable
```

---

## 1. The problem

Newtonian mechanics uses trajectories.

A point-particle can have a trajectory:

```text
r(t)
```

But an ordinary physical body is not a mathematical point.

It has extent, shape, surface, orientation, and possibly internal motion.

So before a physical body can be described by point-particle language, we need a bridge:

```text
How does a body supply something trajectory-like?
```

That bridge is trackability.

---

## 2. Trackability

Trackability is the assumption that selected points of a physical body can be re-identified through time in a reference frame.

In simple words:

```text
we can keep watching the same point on the body as time passes
```

A better technical phrasing:

```text
trackability :=
A physical body is trackable when selected points on it can be re-identified through time in a reference-frame, so that each selected point generates a track.
```

The key is continued re-identification.

It is not enough to see a point once. A track requires the same selected point to be followed across many times.

---

## 3. Tracks

Once a point on a body is trackable, it generates a track:

```text
selected point on body
  -> position at time t
  -> position at later time
  -> time-indexed track
```

In mathematical mechanics, that track can be represented as a trajectory:

```text
r(t)
```

So trackability allows this move:

```text
physical body
  -> selected trackable point
  -> trajectory
  -> point-particle description
```

A point-particle is then not the physical body itself.

It is the mathematical carrier of a track associated with the body.

---

## 4. A body has many possible tracks

An extended body does not usually supply just one track.

It supplies many possible tracks:

```text
track of point A
track of point B
track of point C
...
```

So the motion of a body is first available as a family of tracks.

This matters because different points of the same body can move differently.

For example:

```text
a spinning body has different point-tracks around its centre
an elastic body can deform, so distances between point-tracks can change
a fluid-like body may not preserve stable identifiable points in the same way
```

Trackability therefore does not yet imply rigidity.

It only says that there are tracks available to be followed.

---

## 5. Rigid bodies

A rigid body is a special kind of trackable body.

For a rigid body, the tracked points keep fixed distances from one another.

In simple words:

```text
the body may move, but its tracked points stay locked together
```

Technical phrasing:

```text
rigid-body :=
A trackable body whose selected point-tracks preserve fixed mutual distances over the motion interval being modelled.
```

So rigidity adds a constraint to the family of tracks:

```text
trackability gives tracks
rigidity constrains the tracks
```

For pure rigid translation, the tracked points all share the same acceleration:

```text
a1 = a2 = ... = A
```

For rotation, the distances remain fixed, but different tracked points can have different accelerations.

---

## 6. Point-particle representatives

Once a body is trackable, a modeller may choose one track to stand for the body in a simplified problem.

This gives a point-particle representative:

```text
point-particle representative :=
A point-particle whose trajectory is used to stand for a selected body-track, or for a constructed representative track of a body, when the body's extent and internal track differences are being neglected for the modelling question.
```

This is the crucial modelling move:

```text
body motion is many-track motion
point-particle motion is one-track motion
```

A body can be treated as a point-particle only when the modelling question permits one track to represent the relevant motion of the body.

---

## 7. Centre of mass as a later representative track

For a rigid body, many tracks are available.

The centre of mass is not just any one of them.

It is the mass-weighted representative track that can carry the body's bulk Newton-II account.

In short:

```text
trackability lets the body supply tracks
rigidity locks the tracks together
mass-weighting selects the centre-of-mass representative track for bulk translation
```

So the centre of mass belongs later in the structure.

Before asking why the centre of mass represents a body, we first need the idea that the body has tracks at all.

That prior idea is trackability.

---

## 8. Relation to NML2

NML2 should not begin with the vague phrase:

```text
an object moves
```

It should make the target question visible:

```text
Which thing are we tracking?
```

Then the Newton-II route can be understood as:

```text
1. Choose the target whose track is being read.
2. Read its motion-change from the track.
3. Attach a mass-side value to that same target.
4. Expose the net-force slot demanded by Newton II.
```

Trackability explains why step 1 is possible.

It says:

```text
physical bodies can supply tracks that point-particles can carry mathematically
```

That is the bridge from bodies to point-particle mechanics.

---

## 9. Compact summary

```text
Trackability:
  selected points on a body can be re-identified through time.

Track:
  the trajectory generated by following such a selected point.

Body motion:
  a family of tracks supplied by the body.

Rigid body:
  a trackable body whose tracks preserve fixed mutual distances.

Point-particle representative:
  one mathematical track-carrier used to stand for the body, when the modelling question permits it.

Centre of mass:
  the later mass-weighted representative track for bulk rigid-body translation.
```
