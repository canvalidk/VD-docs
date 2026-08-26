# From Tracks to Particles: Rigidity as the Lumping Criterion

**Status:** working design note
**Project:** VD Newton / Newtonian Mechanics Lesson sequencing
**Position:** NML1 → NML2 hinge, following trackability

---

## Purpose

This note answers a question that the trackability material leaves open:

```text
A body supplies many possible tracks.
How many tracks should we actually use to describe it?
```

Trackability tells us that selected points on a body can be re-identified through
time, each generating a track. It tells us the body offers a *family* of tracks.
It does not tell us how many of those tracks a problem needs, or what mass each one
carries.

The claim of this note is that **rigidity — redefined as an observed feature of
tracks rather than a property of solids — is the criterion that answers both
questions at once.** It decides how many particles a problem needs, and it decides
how much mass each particle carries.

---

## 0. The ground: the material in the real world is trackable

Before any of this, one fact has to hold, and it is the fact the entire trajectory
formalism quietly stands on: **the material in the real world is trackable.** Points
on real bodies can be re-identified through time. This is not a result of Newtonian
mechanics; it is the precondition that lets Newtonian mechanics describe the world at
all. Every trajectory `r(t)` ever written for a physical body is silently cashing
this fact — it is the trajectory *of* something only because some material point was
followable from one moment to the next. Strip trackability away and you do not get
worse mechanics, you get no mechanics, because there is nothing for a trajectory to
be the trajectory of. So the dependency runs one way: Newtonian mechanics can be used
to describe the world *because* the material of the world is trackable — not the
reverse. This also fixes the place of the centre of mass. The centre of mass is not
the special point that gives the body its trajectory; trackability is a property of
*all* material points, and the centre of mass is simply one of them that happens to
be trackable too, distinguished later for a mass-weighting reason, never for being
the source of trajectory-hood. The centre of mass is a tenant of this grip on
reality, not its foundation.

---

## 1. The tap: why one track?

Consider water flowing from a tap in a steady stream.

We routinely represent that stream with a single track — one trajectory standing in
for the whole flow.

But this is a choice, and it deserves justification. We could equally describe the
stream with one hundred tracks:

```text
100 tracks, each carrying 1/100 of the flow's material.
```

Nothing forces us to use one rather than one hundred. So why is the single-track
description legitimate?

The answer is in the tracks themselves. If we *did* lay down a hundred tracks across
the stream, we would notice something:

```text
the hundred tracks move together
they keep fixed distances from one another
they flow uniformly, as one
```

Because the tracks travel as a locked-together family, the extra ninety-nine carry
no information the first one lacks. Any one of them already reports the motion of all
of them. So we are entitled to collapse the hundred down to one — not because the
water is "simple," but because the tracks are **mutually rigid**.

This is the justification that was missing. The single-track description of the tap
is licensed by an observed feature of the tracks: they preserve fixed mutual
distances as they move.

---

## 2. Rigidity, redefined

The ordinary meaning of "rigid" is a property of hard solids — a brick is rigid, a
sponge is not.

For this purpose we redefine it as a feature of tracks:

```text
rigidity (track sense) :=
A collection of tracks is mutually rigid when the tracks preserve fixed mutual
distances over the modelling interval being considered.
```

Under this definition, rigidity is not something a material *has*. It is something
a family of tracks *does*, observed over the interval we care about.

This redefinition is what lets the same idea cover the tap. Tap water is not a solid.
But over a short interval, the tracks across a steady stream do preserve their mutual
distances — so the stream's tracks are mutually rigid in the track sense, even though
the water is a fluid. The familiar solid case (a brick, whose tracks obviously stay
locked together) becomes just the most obvious instance of a more general condition.

---

## 3. The lumping move

Once rigidity is a feature of tracks, it does work. It becomes the rule for
collapsing many tracks into few:

```text
tracks that are mutually rigid carry redundant information
so they can be represented by a single track
that single track becomes one particle
```

This is the **lumping move**: replace a bundle of mutually-rigid tracks with one
representative track, and treat that representative as a single particle.

The tap is one particle because all its tracks form a single mutually-rigid bundle.
There is nothing to distinguish them dynamically, so one stands for all.

---

## 4. The splatter: why many particles?

Now let the tap water fall and hit the floor, splitting into a spray that scatters
outward.

We can no longer use one track. The question returns in a sharper form:

```text
How many tracks should we use to describe the splatter?
```

The lumping move answers it. The procedure is:

```text
1. Lay down many tracks across the splattering water.
2. Identify which tracks remain mutually rigid with one another.
3. Each maximal bundle of mutually-rigid tracks becomes one particle.
```

Before the splash, every track belonged to one bundle — one particle. The splash
*breaks* that single bundle apart. Tracks that flew off to the left no longer
preserve their distances to tracks that flew off to the right. They are no longer
mutually rigid. So they fall into separate bundles, and each separate bundle is a
separate particle.

The number of particles is therefore not handed to us by the problem. It is **read
off the tracks** using rigidity as the criterion:

```text
one rigid bundle before the splash    -> one particle
several rigid bundles after the splash -> several particles
```

The splash is the event that converts one particle into many, because it is the
event that breaks one rigid bundle into several.

---

## 5. The mass each particle carries

The same criterion that fixes the *count* also fixes the *mass*.

A track, on its own, is just a geometric line through space and time. It carries no
mass by itself. What gives a track a mass is the **material that moves rigidly with
it**:

```text
a particle's mass = the mass of the material that stays mutually rigid
                    with that particle's track bundle
```

For the tap, this is the whole flow: all the water moves rigidly with the one bundle,
so the one particle carries the whole mass.

For the splatter, the incoming material has divided. Each outgoing bundle stays rigid
with its own portion of the water, and each particle carries the mass of *its*
portion:

```text
incoming water of mass M
  -> splits into bundles
  -> each bundle's particle carries the mass of the water moving rigidly with it
```

So rigidity does double duty. It is the criterion for how many particles we need,
and — through the material each bundle stays rigid with — it is also the criterion
for how much mass each particle gets.

---

## 6. Why this matters for the lesson sequence

This completes the bridge from trackability to mechanics that the earlier material
started.

Trackability said: a body supplies tracks. But a bare track is not yet usable in
mechanics — to read motion-change on it and eventually account for that change, we
need to know two things the track alone does not tell us: how many tracks to use, and
how much material each one represents.

Rigidity-as-track-feature supplies both:

```text
trackability:  a body offers a family of tracks
rigidity:      mutually-rigid tracks lump into one particle (the count)
               each particle carries the mass it stays rigid with (the mass)
```

The progression for the student is then:

```text
1. A body supplies many possible tracks. (trackability)
2. Tracks that move rigidly together can be represented by one. (lumping)
3. That representative is a particle, carrying the mass it stays rigid with.
4. When an event breaks the rigid bundle apart, one particle becomes many,
   and the mass divides among them along the new bundles.
```

The tap and the splatter are the two anchoring examples:

```text
tap:      one rigid bundle  -> one particle  -> whole mass on one track
splatter: many rigid bundles -> many particles -> mass divided along the bundles
```

---

## 7. Compact summary

```text
Trackability:
  a body supplies a family of tracks.

Rigidity (track sense):
  a collection of tracks is mutually rigid when it preserves fixed mutual
  distances over the modelling interval.

Lumping move:
  a bundle of mutually-rigid tracks is represented by one track = one particle.

Particle count:
  partition the tracks into maximal mutually-rigid bundles; each bundle is a particle.

Particle mass:
  each particle carries the mass of the material that moves rigidly with its bundle.

Tap:
  all tracks form one rigid bundle -> one particle -> whole mass.

Splatter:
  the splash breaks the bundle apart -> many particles -> mass divided along bundles.
```
