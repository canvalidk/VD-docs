> **Informing copy — do not edit here.**
> **Home note:** `photon_frame_certification`, draft `d3` — `Newton-analysis/photon_frame_certification/photon_frame_certifier_and_gravity_d3.md`.
> Placed in `nml2.1` (informs `nml2_1_lesson`): the lesson assumes inertial-frame certification is solved (frame-qualified triplet, supplied frames); this note is the frame-certification account. This is a read-only copy; refresh from the home note if the source changes.

---

# Why a Usable Newtonian Mechanics Can't Carry Gravity as a Force

## What this note claims

A precise, bounded claim — not the grand one.

> If you want Newtonian mechanics to work as a *predictive instrument* — a system
> that can look at an unexplained motion and infer "there must be a force-source you
> haven't accounted for yet" — then you are forced into a specific setup. And in that
> setup, treating gravity as a force produces an internal error. So: **a Newtonian
> mechanics that is actually usable as a force-detector cannot carry gravity as one of
> its forces.**

This is *not* the claim "gravity is not a force, full stop." That stronger claim is
true for other, deeper reasons (see the last section). What's interesting here is that
a much narrower version of it can be forced out of Newton's *own* internal structure,
without appealing to relativity at all.

The argument has three moving parts. Each one is individually unremarkable. The point
is how they lock together.

---

## Part 1: Newton's predictive power depends on being in the right kind of frame

The useful thing Newtonian mechanics does is *force accounting*. You add up the forces
on an object, and the leftover — the acceleration that the forces don't explain —
tells you something real is missing from your list. This is how you discover hidden
things. Neptune was found this way: Uranus accelerated in a way the known planets
couldn't explain, so there had to be another mass out there.

But this trick only works if you are in an **inertial frame** — roughly, a
non-accelerating, non-rotating point of view.

Why? Because in an accelerating or rotating frame, objects *appear* to be pushed around
by forces that aren't really there. On a spinning merry-go-round you feel flung
outward, but nothing is pushing you — it's the frame doing it. These are called
**fictitious forces**. If you run the force-accounting trick in such a frame, the
leftover acceleration doesn't mean "a hidden object is out there." It might just mean
"my frame is spinning." The detector gives you false positives. It hallucinates causes.

So the rule is: **force-accounting only gives trustworthy answers in an inertial
frame.** Get the frame wrong and every "discovery" is suspect.

This means that *before* you can use Newton to detect hidden things, you must somehow
establish that you're in an inertial frame.

---

## Part 2: Establishing the frame is harder than it looks — the look-alike problem

How do you check that your frame is inertial? The textbook answer: find an object that
has no forces on it (a "free particle"), and check that it moves in a straight line at
constant speed. If it does, your frame is inertial.

Here's the trap. A free particle moving at constant velocity looks **exactly the same**
as an object you're watching from a frame that is itself accelerating along with it.
"Moving uniformly" cannot, by itself, tell apart:

- a genuinely force-free object seen from a genuinely inertial frame, and
- an object seen from a whole *family* of accelerating frames that happen to move along
  with it.

Call these the look-alike frames. From inside the system, uniform motion alone can't
distinguish the real inertial frame from its accelerating look-alikes.

So you need to certify some object as *genuinely* free — not just apparently uniform —
to break the tie.

**And here is the circularity.** Suppose you pick an ordinary massive object — a ball,
a planet — and declare it free because "I've added up all the forces on it and they
cancel." But the whole reason you built this machine was to *detect forces you haven't
accounted for yet*. An object that looks force-free might simply be one whose hidden
force you haven't found — which is precisely the thing the detector is supposed to find
later. So certifying your frame with a massive object means **assuming there are no
hidden forces in order to build the instrument whose entire job is to find hidden
forces.** That's circular. You've assumed the answer to build the question-asker.

So:

- Certify the frame with a massive body → circular. Can't distinguish the real inertial
  frame from its look-alikes.
- Certify with nothing → no inertial frame established → the detector's outputs are
  meaningless.

Both branches are dead. The detector never gets off the ground.

---

## Part 3: The photon is the one escape — and it's a poisoned one

There is exactly one kind of object that breaks the circularity.

A **photon** — a particle of light — can be asserted to be free *without* first doing
the force-accounting that assumes the frame. You don't certify a photon as free by
saying "I added up its forces and they cancel" (the circular route). You assert its
freedom on independent grounds. That makes the photon the **only candidate that can
certify an inertial frame without smuggling in the very no-hidden-forces assumption the
detector exists to test.**

So if you want a *usable* Newtonian detector, you are essentially forced to admit the
photon as your reference free particle. It's not an optional, exotic choice a careless
modeller might make. It's the thing that rescues the whole enterprise from
circularity. Decline it, and you're back in Part 2 with no non-circular way to pin the
frame.

**But the photon is massless.** And Newton's second law is

```text
acceleration = force / mass.
```

Divide by the mass of a photon and you get a meaningless expression — you're dividing
by zero. So the instant you also try to treat **gravity as a force acting on the
photon** (and gravity does act on light — light bends near massive objects), you ask
Newton to compute `gravitational force / 0`, and the whole framework errors out.

That's the collision:

- The photon is **load-bearing**: it's the only thing that makes Newton usable as a
  predictor.
- The photon is **lethal to gravity-as-a-force**: the moment gravity is treated as a
  force on it, the second law breaks.

The same single act — admitting the photon — both rescues the detector and destroys
gravity's status as a force *within* that detector. You can't keep one without the
other.

---

## Putting it together

1. To use Newton to discover hidden things, you must be in an inertial frame.
2. To establish an inertial frame non-circularly, you must certify a genuinely free
   particle — and a massive one won't do, because certifying it assumes away the very
   hidden forces the machine exists to find.
3. The photon is the unique non-circular certifier — so a usable Newton is *forced* to
   admit it.
4. But the photon is massless, and gravity acts on it, so treating gravity as a
   Newtonian force makes the second law divide by zero.

Therefore: **a Newtonian mechanics powerful enough to be used as a force-detector
cannot consistently carry gravity as a force.** Not by choice, but by the structure of
what it takes to make the detector work.

---

## What this is *not* (the honest boundary)

It's worth being scrupulous about what this argument does and doesn't show, because the
modest version is genuinely interesting and the overclaim would be easy to make.

**It is not a proof that "gravity is not a force."** The error above is really carried
by *massless + divide-by-mass*, not by anything special about gravity. Any force you
tried to apply to a massless particle via `F/m` would break the same way. Gravity dies
here only because it's the force that happens to act on the frame-certifier
unconditionally. So the honest conclusion is about **Newtonian mechanics' internal
reach**, not about gravity's ultimate nature.

**It is not a discovery that physicists missed.** That Newton can't handle light is old
news — it was settled empirically, and the 1919 eclipse measured the deflection that
confirmed Einstein over Newton. What's novel here is the *structural* diagnosis —
pinpointing the failure as a frame-certification problem internal to Newton — not the
fact of the failure.

One common framing of that old news deserves correcting, though, because it actually
*understates* the present argument. People often say "Newton predicts light should bend,
just by the wrong amount — half the true value." This is misleading. There is no clean
Newtonian prediction about light. The famous half-value is obtained only by treating the
photon as a tiny *massive* corpuscle: you compute its deflection via `force / mass`, the
mass cancels out of the answer, and only afterward do you notice the result doesn't
depend on the mass you assigned. That cancellation is the only thing standing between you
and the divide-by-zero. In other words, the half-value is produced by exactly the move
this whole argument forbids — putting the photon on the `force / mass` branch — and is
therefore not a Newtonian statement about light at all, but a symptom of the same
massless mismatch, dressed up as a finite number.

So the factor-of-two discrepancy and the divide-by-zero are not two separate facts. They
are the *same defect* seen two ways. Sloppy Newton hides the massless problem inside a
mass-cancellation and walks away with a finite-but-wrong number; careful Newton — Newton
that refuses to treat the frame-certifying free particle as a massive one — refuses the
cancellation and is handed an explicit error instead. The error is the honest version of
the wrong number. General relativity then recovers the full, correct deflection precisely
because it never routes through `force / mass` at all.

**The real reason gravity isn't a force is different and deeper.** In general relativity,
gravity is geometry. The decisive clue is the **equivalence principle**: everything
falls at the same rate regardless of its mass or composition. For every genuine force,
the resulting acceleration depends on a charge-to-mass ratio; for gravity it doesn't.
That universality is why gravity can be transformed away by switching to a freely-falling
frame — *no other force can be eliminated by choice of frame* — and why it's better
understood as the curvature of spacetime than as a push. A falling object isn't being
forced; it's coasting along the straightest available path through curved spacetime.
Light bends because it follows those paths too. Crucially, that account *also predicts
the right deflection number*, which the present argument does not attempt to do.

So the relationship is: the argument in this note finds, inside Newton's own bones, a
**structural shadow** of the equivalence principle — a place where Newton's framework
quietly refuses to carry gravity as a force once you make it powerful enough to be
useful. It is a negative consistency result about a superseded theory, not a positive
replacement for it. That's a smaller claim than "gravity isn't a force" — but it's true,
it stands on Newton's own terms, and it explains *why* the naive route fails rather than
merely asserting that it does.
