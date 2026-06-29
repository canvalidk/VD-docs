# Newton I — Six-Entry Unit (Draft)

## Structure reminder
- **Chimney**: peripheral (kinematic) definition of the November word
- **Triplet**: three mutually-defining entries (November, Winter 1, Winter 2)
- **Wall 1**: peripheral definition of Winter 1 (outward-facing)
- **Wall 2**: peripheral definition of Winter 2 (outward-facing)

---

## Chimney

**E[c] uniform motion** := "A point particle is in uniform motion on an interval I
if its velocity is constant throughout I; i.e. ∀t₁, t₂ ∈ I, v(t₁) = v(t₂).
A point particle is in uniform motion at time t₀ if ∃ε > 0 such that it is in
uniform motion on (t₀ − ε, t₀ + ε)."

> **Note**: Pure kinematics. No physics. Computable from the trajectory alone.
> Merges the old E12/E13 into a single entry since the time-point version is
> just the local form of the interval version. Both variants are needed downstream
> (Newton I's triplet uses both), so housing them together avoids an unnecessary
> second pre-law entry.

---

## Triplet

**E[t1] uniform motion** := "The state of motion exhibited by a free particle
when described in an inertial frame. (Equivalently: uniform motion on any
interval of free motion in an inertial frame.)"

> **Role**: November (anchor). Previously defined by chimney.
> The chimney says *what* uniform motion looks like (constant velocity);
> the triplet says *when* it occurs (free + inertial).

**E[t2] inertial frame** := "A reference frame in which every free particle
exhibits uniform motion."

> **Role**: Winter 1. New term. Defined in terms of the other two triplet members.

**E[t3] free particle** := "A point particle that, when described in an inertial
frame, exhibits uniform motion."

> **Role**: Winter 2. New term. Defined in terms of the other two triplet members.

---

## Wall 1 (inertial frame)

**E[w1] inertial frame** := "Any reference frame in uniform motion relative to
an inertial frame is itself an inertial frame."

> **Note**: This is the Galilean closure property. It uses only "reference frame"
> (kinematic scaffold) and "uniform motion" / "inertial frame" (just defined).
> It gives downstream entries a way to *generate* new inertial frames from
> known ones — the operational handle they'll need.

---

## Wall 2 (free particle)

**E[w2] free particle** := "A point particle whose path is not being interfered
with by any external object."

> **Note**: Common-sense, pre-physics recognition criterion. No mention of
> inertial frame or uniform motion — that's the triplet's job. This wall faces
> outward: it tells the reader (and downstream entries) how to *recognise* a
> free particle using ordinary human judgment. The irreducible complexity of
> deciding "is anything interfering?" lives here as a recognition step (P-03).
> This is exactly the kind of entry that makes the VD honest about where
> human judgment enters.

---

# Discussion: Kinematic entries before and after Newton I

## Before Newton I (pure kinematics, residue-level)

These assume calculus and vector competence. They are notation-pinning, not physics.

Needed:
- time (t ∈ ℝ, ordering of events)
- reference frame (origin, axes, clock — the general concept, not yet inertial)
- position r(t)
- displacement Δr
- velocity v(t) = dr/dt
- speed ||v(t)||
- acceleration a(t) = d²r/dt² ← bare coordinate acceleration
- point particle (idealized, trajectory-only object)
- straight line (geometric primitive)
- trajectory (time-ordered curve)

Possibly not needed:
- path length (E9 in v0.2) — is anything downstream actually using this?

## After Newton I (between Newton I walls and Newton II chimney)

This is where "inertial acceleration" would live:

**E[ia] inertial acceleration** := "The acceleration of a point particle as
measured in an inertial frame."

> This is a non-law entry. It picks up "inertial frame" from Newton I's output
> and applies it to "acceleration" from the kinematic scaffold. It's the chimney
> for Newton II's November word. Any particle can have an inertial acceleration
> — not just free ones.

## Do we need "inertial position" or "inertial velocity"?

**Argument against**: Position and velocity are frame-dependent in ALL frames —
moving between inertial frames shifts them by a Galilean boost. But they don't
pick up *fictitious terms*. There's no "fictitious velocity" or "fictitious position"
the way there's fictitious acceleration (Coriolis, centrifugal). The distinction
between "coordinate X" and "inertial X" is physically sharp for acceleration
but merely conventional for position and velocity.

Put differently: two inertial frames disagree about r(t) and v(t) but agree
about a(t). Acceleration is the invariant under Galilean boosts; position and
velocity are not. So "inertial acceleration" is a physically distinguished quantity
in a way that "inertial position" is not.

**Argument for**: Consistency — if we're being rigorous about frame-qualification,
shouldn't we qualify everything? But this seems like over-definition (violates P-09:
interpretability is assumed). The reader can intuit "position in whatever inertial
frame we've chosen" without a separate entry.

**Tentative conclusion**: No inertial position or inertial velocity. Only inertial
acceleration gets its own entry because it's the only one where the inertial/
non-inertial distinction carries physical content (fictitious forces).
