# Kinematic Scaffold — Pre-Newton I Entries (Draft v2)

## Source reference

The concepts defined below are standard in introductory classical mechanics.
Principal references:

- **Kleppner, D. & Kolenkow, R.** *An Introduction to Mechanics* (2nd ed., Cambridge University Press, 2014).
- **Taylor, J.R.** *Classical Mechanics* (University Science Books, 2005).

The definitions have been reworded to respect VD entry-log dependency order:
each entry uses only residue (calculus, vectors, set theory, common sense) and
headwords that appear earlier in the log. The conceptual content is faithful to
the source material; the phrasing is ours.

## Assumptions (residue)

The reader is assumed competent with: real analysis (limits, derivatives,
integrals), vector algebra in ℝ³ (addition, scalar multiplication, dot product,
norms), and standard set-theoretic notation. These are not defined in the VD;
they are residue.

---

## Entries

**E1 time** := "A real parameter t ∈ ℝ used to order events; differences
Δt = t₂ − t₁ are durations."

> No headword dependencies. Pure residue.

---

**E2 reference frame** := "A convention for assigning spatial coordinates and
a time coordinate to events: an origin, a set of basis vectors, and a clock."

> References: time (E1).

---

**E3 point particle** := "An idealised object whose spatial extent and internal
structure are neglected."

> No headword dependencies. Residue-level recognition: the reader already
> knows what "a small thing you're tracking" means. What a point particle
> *has* (position, trajectory, etc.) is built up by later entries that reference
> this one — not packed in here. Full class formalisation comes when the
> meta-typing triplet fires.

---

**E4 position** := "The location of a point particle at time t in a reference
frame, represented by a vector r(t) ∈ ℝ³."

> References: point particle (E3), time (E1), reference frame (E2).

---

**E5 displacement** := "The change in position: Δr = r(t₂) − r(t₁)."

> References: position (E4).

---

**E6 velocity** := "v(t) = dr/dt."

> References: position (E4), time (E1) — via the derivative.

---

**E7 speed** := "v(t) = ‖v(t)‖."

> References: velocity (E6).

---

**E8 acceleration** := "a(t) = dv/dt = d²r/dt²."

> References: velocity (E6), time (E1). This is bare coordinate acceleration —
> a property of r(t) in whatever reference frame is being used. No physics.

---

**E9 trajectory** := "The time-ordered set of positions {r(t) : t ∈ I} of a
point particle over some interval I ⊆ ℝ."

> References: position (E4), point particle (E3), time (E1). Placed after
> velocity and acceleration because, while it doesn't reference them, it is
> conceptually the object that velocity and acceleration are derived from.
> Keeping it here avoids giving the impression that trajectory depends on
> velocity — it doesn't. Either ordering is valid; this one reads more
> naturally.

---

**E10 straight line** := "A set of points {r₀ + λû : λ ∈ ℝ} for fixed
r₀ ∈ ℝ³ and nonzero direction û ∈ ℝ³."

> No headword dependencies. Pure geometric residue. Needed for the
> uniform motion chimney (uniform motion on I implies the trajectory
> is a straight line or a point).

---

**E11 path length** := "The arc length of a trajectory from t₁ to t₂:
s = ∫_{t₁}^{t₂} ‖v(t)‖ dt."

> References: trajectory (E9), velocity (E6), time (E1). Not used by any
> law triplet. Included for completeness and downstream worked examples.
> First candidate to cut if a leaner scaffold is preferred.

---

**E12 relative position** := "For two point particles in the same reference
frame, the relative position is r₁₂(t) = r₂(t) − r₁(t)."

> References: point particle (E3), reference frame (E2), position (E4).
> Included because interaction laws downstream (gravity, springs) are
> functions of relative position.

---

**E13 relative velocity** := "For two point particles in the same reference
frame, the relative velocity is v₁₂(t) = v₂(t) − v₁(t) = dr₁₂/dt."

> References: point particle (E3), reference frame (E2), velocity (E6),
> relative position (E12). Included for downstream use — friction activation
> conditions depend on relative tangential velocity.

---

## Dependency audit

Every entry references only residue and earlier headwords:

| Entry | References (headwords only) |
|-------|---------------------------|
| E1  time               | — (residue) |
| E2  reference frame     | E1 |
| E3  point particle      | — (residue) |
| E4  position            | E1, E2, E3 |
| E5  displacement        | E4 |
| E6  velocity            | E1, E4 |
| E7  speed               | E6 |
| E8  acceleration        | E1, E6 |
| E9  trajectory          | E1, E3, E4 |
| E10 straight line       | — (residue) |
| E11 path length         | E1, E6, E9 |
| E12 relative position   | E2, E3, E4 |
| E13 relative velocity   | E2, E3, E6, E12 |

No forward references. No cycles. All non-law.

---

## What follows

- E14: uniform motion (chimney)
- E15: uniform motion (triplet — November)
- E16: inertial frame (triplet — Winter 1)
- E17: free particle (triplet — Winter 2)
- E18: inertial frame (wall)
- E19: free particle (wall)
- E20: inertial acceleration (chimney for Newton II)
