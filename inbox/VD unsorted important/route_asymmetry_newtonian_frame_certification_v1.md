# A Route-Asymmetry in Newtonian Frame Certification

**Status:** rough draft v1  
**Genre:** foundations / philosophy of mechanics note  
**Core claim:** If Newtonian mechanics is treated as correct, and if massless particles with measurable paths are admitted as possible path-objects, then such particles have a special capacity to certify inertial frames: unlike massive particles, they cannot be assigned hidden force-produced trajectories by Newton's force law.

---

## Abstract

Newtonian mechanics requires inertial frames before its force-accounting machinery can be trusted. But identifying the first inertial frame is not trivial. A massive body that appears to move uniformly in a candidate frame may be genuinely free, in which case the frame is plausibly inertial; but it may also be a forced body whose acceleration has been hidden by a frame chosen to move with it.

This note argues that massless particles occupy a different structural role. Newtonian mechanics has two distinct ways of assigning future paths: the free-particle route, where a free body in an inertial frame exhibits uniform motion, and the force route, where force determines acceleration through `a = F_net / m`, which then updates velocity and position. Massive particles can enter both routes. Massless particles cannot enter the force route, because `m = 0` makes the acceleration update undefined or underdetermined.

Therefore, if a massless particle is admitted at all, its Newtonian role is restricted to the free-particle path route. This blocks the hidden-force ambiguity that attaches to massive certifiers. The result is not a standard historical claim about Newton, nor a replacement for the usual affine-spacetime account of inertial structure. It is a conditional route-asymmetry: in Newtonian mechanics plus massless path-objects, massless particles are structurally better candidates for certifying the first inertial-frame family than massive particles.

---

## 1. The problem: inertial frames are easy after the first one

In Newtonian mechanics, once one inertial frame has been granted, the rest are easy. Every non-rotating frame moving at constant velocity relative to an inertial frame is also inertial. The inertial frames form a Galilean equivalence class.

So the real problem is not:

```text
Given one inertial frame, which other frames are inertial?
```

The real problem is:

```text
How does Newtonian mechanics earn the first inertial frame?
```

This is the frame-certification problem.

The usual textbook slogan is that an inertial frame is one in which free particles move uniformly in straight lines. But this definition is not automatically operational. To use it, one must already know which particles are genuinely free. And if "free" means "not acted on by forces," then determining whether a particle is free appears to require force-accounting. But force-accounting is trustworthy only after an inertial frame has been selected.

So there is a circular pressure:

```text
To run Newtonian force-accounting, we need an inertial frame.
To identify an inertial frame, we look for free particles.
To identify free particles, we seem to need force-accounting.
```

This is not a new problem. Standard treatments usually handle it by building inertial structure into Newtonian spacetime, by treating it as primitive background affine structure, or by approximating it empirically through the frame in which Newton's laws take their simplest and most successful form across many bodies.

This note does not try to replace those standard answers. It asks a narrower question:

> If we look inside the Newtonian path-assignment machinery, are all possible frame-certifiers structurally equal?

The answer, I will argue, is no. Massive and massless path-objects behave differently.

---

## 2. Co-moving is not co-inertial

Before stating the argument, one terminological distinction matters.

A frame that moves with a particle is **co-moving** with that particle.

A frame that is related to an inertial frame by a Galilean boost is **co-inertial** with that inertial frame.

These are not the same thing.

If a particle is genuinely free in an inertial frame, then a non-rotating frame moving uniformly with that particle is co-inertial. But if the particle is forced and accelerating, then a frame moving with it is merely co-moving. It may make the particle appear at rest, but it is not thereby inertial.

So the problem can be stated as:

```text
How do we distinguish a genuine co-inertial frame family
from a merely co-moving frame family built around a selected particle?
```

A single massive particle does not solve this problem by itself, because its apparent uniform motion can be produced in more than one way.

---

## 3. Newton has two routes for assigning future paths

Newtonian mechanics has two different methods for assigning a future path to a particle.

The first is the **free-particle route**:

```text
free particle + inertial frame -> uniform motion
```

This route says that if the particle is free and the frame is inertial, then the particle's velocity remains constant and its path is uniform: stationary or straight-line constant-speed motion.

In procedural form:

```text
current position + current velocity -> next position
velocity remains unchanged
therefore future path is uniform
```

The second is the **force route**:

```text
net force -> acceleration -> next velocity -> next position
```

In procedural form:

```text
a = F_net / m
v_next = v_current + a Δt
x_next = x_current + v_next Δt
```

This is the route by which Newtonian mechanics assigns curved or non-uniform motion. A force changes acceleration; acceleration changes velocity; velocity changes position.

The distinction matters because the two routes have different entry conditions.

The free-particle route requires a particle with a position and velocity whose free status is being considered in a candidate inertial frame.

The force route requires more. It requires the particle to have a mass value that can appear in the acceleration update:

```text
a = F_net / m
```

That requirement is harmless for ordinary massive particles. It is fatal for massless particles.

---

## 4. Massive particles can enter both routes

An ordinary massive particle can be admitted into both Newtonian path-assignment routes.

If it is free, Newton I assigns its future path:

```text
massive particle
+ free status
+ inertial frame
-> uniform motion
```

If it is not free, Newton II assigns its future path:

```text
massive particle
+ net force
+ inertial mass
-> acceleration
-> velocity update
-> position update
```

So a massive particle has two Newtonian path possibilities:

```text
free path:
  no relevant force influence -> uniform motion

force path:
  force accounted -> acceleration -> possibly curved or non-uniform motion
```

This creates the massive-certifier ambiguity.

Suppose a massive particle appears to move uniformly in a candidate frame. There are at least two broad interpretations.

First:

```text
The particle is genuinely free.
The frame is genuinely inertial.
Therefore the particle exhibits uniform motion.
```

Second:

```text
The particle is not genuinely free.
Its path is being produced by forces.
The chosen frame hides this by moving with the particle or otherwise absorbing the apparent acceleration into the frame description.
```

The second interpretation remains possible because massive particles can be assigned force-produced trajectories. The force route is open.

So the observation:

```text
massive particle appears uniform in frame F
```

does not uniquely imply:

```text
frame F is inertial
```

The particle may be a good practical clue. It may be part of a larger empirical procedure. But by itself it does not break the first-frame circularity.

---

## 5. Massless particles cannot enter the Newtonian force route

Now consider a massless particle:

```text
m = 0
```

The force route attempts to assign acceleration by:

```text
a = F_net / m
```

For a massless particle, this becomes:

```text
a = F_net / 0
```

If `F_net` is nonzero, the expression is undefined.

If `F_net = 0`, then the expression becomes:

```text
a = 0 / 0
```

which is also undefined. Equivalently, if Newton's second law is written as:

```text
F_net = m a
```

then for `m = 0` and `F_net = 0`, it becomes:

```text
0 = 0 · a
```

This does not determine `a`. Every acceleration satisfies it. So even in the zero-force case, the force route does not assign a unique future path.

Therefore, a massless particle is not excluded from Newtonian mechanics because it cannot have a position, velocity, or path. It is excluded from the **force path** because the force path assigns future position through an acceleration update, and the acceleration update cannot be performed when `m = 0`.

So the structure is:

```text
massless particle
-> force route
-> a = F_net / 0 or 0 / 0
-> acceleration update fails
-> velocity update fails
-> future path not assigned by force
```

This is the central asymmetry.

A massive particle can be secretly force-routed.

A massless particle cannot be secretly force-routed by Newton's force law.

---

## 6. If Newton is correct, massless particles cannot curve in inertial frames

Assume Newtonian mechanics is correct.

A massless particle cannot receive a force-produced acceleration, because the force route fails at `a = F_net / m`.

Therefore, Newtonian mechanics has no internal means to assign a curved or non-uniform trajectory to a massless particle in an inertial frame.

If the massless particle is admitted at all, it must be admitted through the free-particle route:

```text
massless particle
+ free path route
+ inertial frame
-> uniform motion
```

So, under this conditional reconstruction:

> If Newtonian mechanics is correct, and if photons are massless particles with measurable paths, then photons cannot curve in inertial frames.

If a photon appears to curve, Newtonian mechanics has only a few possible exits:

```text
1. The photon is not really massless.
2. The frame is not really inertial.
3. Newtonian mechanics is not correct for this case.
4. The photon is interacting with something outside the Newtonian force model.
```

But if the note assumes both Newtonian correctness and photon masslessness, then the Newtonian conclusion is:

```text
curving photon path -> non-inertial frame
```

This is the key step that gives photons their frame-certifying capacity.

---

## 7. The massless-certifier argument

We can now state the argument.

A massive particle used as a frame-certifier leaves open two explanations:

```text
A. It is genuinely free in an inertial frame.

B. It is forced, but the candidate frame hides the force-produced motion.
```

The second explanation is open because the massive particle can enter the force route.

A massless particle used as a frame-certifier does not leave open the same pair of explanations:

```text
A. It is on the free-particle route in an inertial frame.

B. It is forced, but the candidate frame hides the force-produced motion.
```

Option B fails inside Newtonian mechanics, because Newton cannot assign a force-produced trajectory to a massless particle.

Therefore, if a massless particle exhibits uniform motion in a candidate frame, its certifying status is stronger than that of a massive particle. The hidden-force explanation has been blocked by the type structure of the force law.

Compressed:

```text
Massive certifier:
  uniform appearance = genuine free motion OR hidden forced motion

Massless certifier:
  uniform appearance = genuine free motion only
  because hidden forced motion is not Newton-computable
```

This is not the claim that one photon path is enough to define all inertial structure. It is the claim that massless path-objects remove a particular ambiguity that massive path-objects cannot remove.

---

## 8. One photon is not enough

A single straight path does not certify a full inertial frame.

A coordinate system can be constructed around a single trajectory, making that trajectory appear simple. The standard historical point is that one free particle is insufficient to define an inertial system.

So the photon-certifier claim must be stated in terms of a family of photon path measurements.

The relevant empirical object is not:

```text
one photon moves straight
```

but something more like:

```text
free photon paths, emitted in many directions and at many locations,
exhibit uniform straight-line motion in the candidate frame.
```

This matters because a frame is not just a line. A frame includes spatial axes and a clock. To certify the frame, photon measurements must constrain not only spatial straightness but also temporal uniformity.

So a careful version of the claim is:

> A sufficiently rich family of free massless path measurements can certify an inertial-frame family more strongly than a corresponding family of massive-particle measurements, because the hidden force-route interpretation remains open for massive particles but not for massless particles.

The phrase "sufficiently rich" hides work. It includes enough directions, locations, and timing information to test whether the candidate coordinates support uniform free paths rather than merely one rectified trajectory.

---

## 9. What exactly do photons certify?

There is a subtle distinction between certifying **straightness of paths** and certifying a full **inertial frame**.

A spatial photon track can help identify straight lines. But Newtonian uniform motion also requires a time scale: the particle must move equal distances in equal times.

So photon paths alone, considered only as spatial curves, may certify something closer to a **projective** or straight-line structure. To certify a Newtonian inertial frame, one also needs clocks and timing conventions.

This introduces a possible refinement:

```text
Photon tracks without timing:
  help certify straight-path structure.

Photon tracks with timing:
  help certify uniform-motion structure.

A full inertial frame:
  requires spatial axes + clock + uniform free-path behaviour.
```

This point should be included because otherwise the note may appear to claim too much from "photon paths" alone.

The note should therefore say:

> I am not claiming that an isolated light ray, considered only as an unparameterised spatial curve, determines an inertial frame. The claim concerns photon measurements rich enough to test uniform motion: path plus timing.

This protects the argument from an obvious objection.

---

## 10. The role of light must not import special relativity

There is another danger. Once photons and frame-certification appear in the same note, readers may think the argument is secretly using special relativity.

It should not.

The claim here is not:

```text
The speed of light is invariant in all inertial frames.
```

That is a relativistic postulate, not a Newtonian one.

The Newtonian claim is only:

```text
A free massless path-object, if admitted into Newtonian mechanics,
cannot be assigned a force-produced acceleration by a = F_net / m.
Therefore its admissible Newtonian path route is the free route.
```

Under Galilean transformations, a photon's velocity would transform in the ordinary Galilean way. Its speed would not be invariant. That is fine for this argument. Nothing here requires Einstein synchronization or Lorentz transformations.

So the note should explicitly say:

> Photons are used here as massless path-objects, not as carriers of the special-relativistic light postulate. The argument does not assume invariant light speed. It assumes only masslessness and measurable path behaviour.

This is important because otherwise the reader will accuse the note of smuggling relativity into Newtonian mechanics.

---

## 11. The connection to gravity

The argument becomes especially interesting when gravity is reintroduced.

Newtonian gravity, applied to ordinary massive particles, fits naturally into the force route:

```text
massive particle
+ gravitational force
-> a = F_g / m
-> curved/non-uniform path
```

But if gravity is treated as an ordinary Newtonian force acting on photons, the route becomes:

```text
photon
+ gravitational force
-> a = F_g / 0
```

or, if the force is treated as zero because the photon has no mass:

```text
a = 0 / 0
```

Either way, Newtonian mechanics cannot assign the photon's gravitationally curved path through the ordinary force route.

So under the assumptions of this note:

```text
photon curves near a mass
```

cannot be interpreted as:

```text
gravity exerted an ordinary Newtonian force on the photon in an inertial frame
```

Instead, Newton must choose one of the following:

```text
1. The frame was not inertial.
2. The photon was not massless.
3. Gravity is not an ordinary force on photons.
4. Newtonian mechanics is not adequate for photons.
```

Historically and physically, of course, the later answer is general relativity: light bends because free light follows null geodesics in curved spacetime, not because an ordinary Newtonian force is divided by the photon's inertial mass.

But this note's point is weaker and more theory-internal:

> The same feature that makes photons attractive as inertial-frame certifiers -- their inability to enter the Newtonian force route -- also prevents Newtonian gravity from being cleanly applied to them as an ordinary force.

That is a useful bridge to a later note on gravity-as-force, but the present note should not depend on it.

---

## 12. Relation to the standard solution

The standard answer to the inertial-frame problem is not "use photons."

The standard answer is closer to this:

```text
Newtonian spacetime has inertial/affine structure built into it,
or inertial frames are approximated empirically by the frames in which
the laws take their simplest and most successful form across many bodies.
```

Newton himself used absolute space, with the fixed stars serving as a practical approximation. Modern presentations often replace that with background spacetime structure or with operational definitions involving many bodies.

So this note should not present itself as the orthodox solution.

The contribution is narrower:

> Given the Newtonian distinction between free path-assignment and force path-assignment, massive and massless certifiers are not equivalent. Massive particles leave open a hidden force-route interpretation. Massless particles do not.

That is the route-asymmetry.

This can coexist with the standard answer. The standard answer tells us how inertial frames are usually understood. This note identifies a structural difference between two possible kinds of certifier.

---

## 13. Objections and replies

### Objection 1: Newtonian mechanics is a theory of massive particles, so massless particles are outside its domain.

Correct. This note is conditional.

It does not say:

```text
Historical Newtonian mechanics already contains photons as massless particles.
```

It says:

```text
If a massless particle with a measurable path is admitted as a boundary object,
then Newton's route-structure gives it a special certifying role.
```

The point is not historical exegesis. It is a structural test.

### Objection 2: If the force is zero, then the photon can just keep moving uniformly.

Yes, but that is the free route, not the force route.

The force route asks for acceleration by:

```text
a = F_net / m
```

For `F_net = 0` and `m = 0`, this becomes `0/0`, which does not determine acceleration. If we decide the particle keeps moving uniformly, that decision is supplied by Newton I, not Newton II.

So the force route still fails as a path-assigning method for massless particles.

### Objection 3: Maybe the massless particle has a force law other than `F = ma`.

Then we have left ordinary Newtonian force-accounting.

That may be a good thing physically. But it confirms the note's point: the ordinary Newtonian force route cannot do the job.

### Objection 4: Real photons do curve gravitationally.

Yes. That is one of the reasons Newtonian mechanics fails for light and gravity.

The argument is not trying to deny light bending. It says that if Newtonian mechanics plus photon masslessness is held fixed, then Newton cannot explain photon curvature through the ordinary force route. The actual bending of light therefore marks a boundary of Newtonian mechanics, or of gravity-as-force, or both.

### Objection 5: A single photon trajectory can always be made straight by choosing coordinates.

Yes. That is why the certifier must be a family of photon measurements, not one trajectory.

This is already familiar from the historical inertial-frame problem: one free particle is not enough.

### Objection 6: Photon measurements require clocks, synchronization, and optics, which may smuggle in extra structure.

Yes. A complete operational account would need to state what timing and synchronization conventions are allowed.

The present note only establishes a route-asymmetry. It does not by itself provide a full metrology of inertial frames.

---

## 14. Main conclusion

The co-inertial frame problem asks how Newtonian mechanics earns its first inertial-frame family.

Massive particles are ambiguous certifiers because they can enter both Newtonian path-assignment routes. Their apparent uniform motion may be genuine free motion in an inertial frame, or it may be forced motion hidden by a co-moving frame.

Massless particles are different. They can be admitted as path-objects, but they cannot be assigned force-produced trajectories by Newton's `a = F_net / m` route. With `m = 0`, the acceleration update is undefined or underdetermined. Therefore the hidden-force alternative is closed.

So the central result is:

> In Newtonian mechanics plus massless path-objects, massless particles have a distinctive frame-certifying capacity. They can occupy the free-particle path route without leaving open the hidden force-route explanation that undermines massive certifiers.

This does not replace the standard account of inertial structure. But it exposes a clean asymmetry in the logic of frame certification.

---

## 15. Additional comments to consider

### 15.1 The distinction between "free" and "force-balanced"

A massive body can exhibit uniform motion while still being under forces, provided the net force is zero. A block resting on a table is the simple case: it is stationary, but not free. Earth and the table are both relevant to its state.

This means the massive-certifier ambiguity has two layers.

First, the particle may be forced with nonzero acceleration, and a co-moving non-inertial frame may hide that acceleration.

Second, the particle may have zero net force but still not be free, because multiple forces cancel.

A massless particle does not automatically solve every version of the second problem. If the phrase "free" means "no interactions at all," then one still needs a way to know the photon is not interacting with a medium, mirror, plasma, or other optical structure.

So the note should be precise:

> The massless argument blocks hidden **force-route path assignment**. It does not magically certify the absence of every possible interaction. A photon in glass, for example, is not a clean free certifier.

### 15.2 The note may need a "vacuum photon" idealisation

The certifier should probably not be "a photon" in general. It should be:

```text
an ideal free photon in vacuum
```

or:

```text
a massless light-like path-object with no relevant optical medium interaction
```

This prevents silly objections. A photon in a medium bends, scatters, refracts, and can have an effective path that is not free. The argument needs the ideal free case.

### 15.3 The relation to null geodesics should be mentioned but not developed

A reader who knows relativity will immediately think:

```text
In GR, photons follow null geodesics.
```

The note can acknowledge this briefly:

> In relativity, the clean path route for massless particles is not Newton I but null geodesic motion. The present argument can be read as a Newtonian shadow of that later structure: massless particles demand a path law that does not pass through `F/m`.

But this should be a closing aside, not the main argument.

### 15.4 The result may be better called a conditional impossibility theorem

The central claim can be made theorem-like:

```text
Given:
  1. Newtonian force path assigns acceleration by a = F_net / m.
  2. A massless particle has m = 0.
  3. A path is force-assigned only if acceleration is determined.

Then:
  A massless particle cannot be assigned a force-produced trajectory
  by the Newtonian force path.
```

Then the frame-certification claim follows as a corollary:

```text
Theorem:
  Massless particles cannot be Newton-force-routed.

Corollary:
  Massless path-certifiers do not suffer the hidden force-route ambiguity.

Application:
  Photons, if admitted as massless path-objects, can certify inertial frames
  in a way massive particles cannot.
```

### 15.5 The title should avoid sounding too big

Possible titles:

```text
Massless Particles and the Certification of Inertial Frames

A Route-Asymmetry in Newtonian Frame Certification

Why Massive Particles Are Ambiguous Frame Certifiers

Massless Path-Objects and the First Inertial Frame

The Hidden-Force Ambiguity in Newtonian Frame Certification
```

The safest standalone title is probably:

> **A Route-Asymmetry in Newtonian Frame Certification**

It sounds modest and technical. It does not overclaim.
