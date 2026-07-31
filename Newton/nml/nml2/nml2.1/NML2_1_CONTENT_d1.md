# NML2.1 Content Specification

## Status and purpose

This document records the content available to NML2.1. It is not yet a timed lesson plan and does not imply that every exercise below must appear in one lesson.

NML2.1 is the first Newton-II lesson. It begins with already identified material objects, already supplied inertial masses, and supplied or inferable net-force vectors. It teaches students to keep these quantities attached to the correct material object, use Newton II, and connect inertial acceleration back to trajectory.

The lesson does **not** yet explain how a material object is constructed from a changing scene, how an inertial-mass value is originally established, or how a net force is constructed from force contributions. It deliberately uses those items before teaching their later construction.

---

## Part I — Information that must be transferred

### 1. The Newton-II relation is an addressed triplet

For one material object `A`, over the same relevant time or interval and in the same inertial frame,

$$
\mathbf F_{\mathrm{net}}[A]=m[A]\mathbf a[A].
$$

The three quantities must belong to the same material object:

- `m[A]` is the inertial mass belonging to material object `A`;
- `a[A]` is the inertial acceleration obtained for `A` in the chosen inertial frame;
- `F_net[A]` is the net-force vector belonging to `A` over the relevant time or interval.

Newton II is therefore not merely the symbol pattern `F = ma`. It is a constraint joining three addressed quantities. A calculation is invalid even when its arithmetic and units are correct if it borrows the mass of one material object and the acceleration or net force of another.

### 2. Quantity types and units

Students must know that:

| Quantity | Type | Unit |
| --- | --- | --- |
| Inertial mass, `m` | Positive scalar | kilogram, `kg` |
| Inertial acceleration, `a` | Vector | metres per second squared, `m s^-2` |
| Net force, `F_net` | Vector | newton, `N` |

The unit relation is

$$
1\ \mathrm N=1\ \mathrm{kg\,m\,s^{-2}}.
$$

Vector answers require direction. A numerical magnitude alone is incomplete when direction is demanded.

### 3. The deliberately thin understanding of net force

By the end of NML2.1, students should understand `net-force` as:

- one vector belonging to a particular material object over a relevant time or interval;
- measured in newtons;
- related to that object's inertial mass and inertial acceleration by Newton II;
- a value that may be supplied as an opaque vector or inferred from the other two members of the Newton-II triplet.

NML2.1 does **not** yet identify net force with:

- “all the forces added together”;
- a newton-meter reading;
- a single push or pull;
- the name of whichever force contribution seems most noticeable;
- “the force that causes acceleration.”

Those claims require the later account of force contributions and acting objects. At this stage, Newton II can establish the net-force vector required by the motion without yet explaining which physical interactions produce it.

For a material object with finite positive inertial mass,

$$
\mathbf a=\mathbf 0
\quad\Longleftrightarrow\quad
\mathbf F_{\mathrm{net}}=\mathbf 0.
$$

However, zero net force does not imply zero velocity, that no force contributions exist, or that the material object has been established to be free.

### 4. The NML2.1 understanding of mass

#### 4.1 A given mass belongs to a material object

NML2.1 does not yet explain where an inertial-mass value comes from. It begins with statements such as:

> This cart has an inertial mass of `4 kg`.

The natural student-facing rule is:

> A given mass belongs to a particular material object. Keep using that mass for the object unless something happens that makes its reuse uncertain.

The more formal bookkeeping description is that the value exists at the material object's address. It is not a free-floating number available to every object in the problem.

A change in position, velocity, acceleration, direction of motion, or net force does not by itself cancel the mass value. The object may accelerate, stop, reverse direction, or follow a completely different trajectory while retaining the same supplied mass.

#### 4.2 The mass-reuse licence is persistent but defeasible

The previously supplied mass may normally be carried forward from one interval to the next. Its automatic reuse must be suspended when an identifiable event makes it uncertain that the old mass binding still applies. Examples include:

- a piece breaking off;
- the material object splitting;
- two material objects merging;
- material entering or leaving;
- continuous leakage or ejection;
- loss of confidence that the later target is the same mass-bearing material object.

The conclusion at such a trigger is only:

> The previously given mass is no longer licensed for automatic reuse.

It does not follow that the mass is zero, that its new value is already known, or that the remainder automatically owns the original mass. If a new mass is explicitly supplied after the event, calculation may resume from that new binding.

#### 4.3 Three meanings of “mass” must not yet be silently identified

NML2.1 should distinguish three roles currently carried by the ordinary word *mass*:

1. **Material-amount or density mass:** the quantity used in descriptions such as `m = rho V`, associated with how much material is present.
2. **Gravitational mass:** the mass-side quantity involved in gravitational interaction and probed when weighing with a scale.
3. **Inertial mass:** the positive scalar in Newton II, characterising the response of a material object to a supplied net force.

NML2.1 does not establish why these agree in ordinary cases. In particular, a scale reading is not to be treated automatically as an inertial-mass measurement.

The same caution applies to additivity. Students should distinguish:

- material-amount additivity;
- measured-mass additivity as an empirical, tolerance-dependent regularity;
- representative or ledger-mass additivity, which requires an additional licence.

The lesson identifies these as different claims. It does not yet derive the connections among them.

### 5. Material objects and trajectories are distinct

The material object is the continuing thing being described. Its trajectory is a time-indexed record of its position in a chosen reference frame:

$$
\mathbf r_A(t).
$$

The distinction can be stated simply:

> The material object is the thing we follow. Its trajectory records what that thing does.

Consequently:

- a trajectory is not itself a material object;
- the trajectory does not own inertial mass or net force;
- inertial acceleration can be read from the trajectory;
- mass and net force belong to the material object whose motion the trajectory records;
- the same material object may have different trajectories in different reference frames;
- two different material objects can follow the same trajectory without having the same mass;
- a trajectory alone does not reveal inertial mass or the physical force contributions.

This distinction prevents the mathematical record of motion from being confused with the persistent mass-bearing target.

### 6. Newton II is a constraint, not an information generator

Students must check which independent information is present before calculating:

| Information supplied | What Newton II determines |
| --- | --- |
| Nothing | Nothing |
| Mass only | Neither acceleration nor net force uniquely |
| Net force only | Neither mass nor acceleration uniquely |
| Acceleration only | Neither mass nor net force uniquely |
| Mass and net force | Acceleration |
| Mass and acceleration | Net force |
| Suitable nonzero net force and acceleration | Inertial-mass magnitude |
| All three | A consistency check |

The algebraic forms are

$$
\mathbf a=\frac{\mathbf F_{\mathrm{net}}}{m},
\qquad
\mathbf F_{\mathrm{net}}=m\mathbf a,
\qquad
m=\frac{|\mathbf F_{\mathrm{net}}|}{|\mathbf a|}
\quad(\mathbf a\ne\mathbf 0).
$$

The final form is a formal Newton-II inference in a suitable nonzero case. It is not yet the general story of how inertial-mass values are obtained and bound to material objects. The `0/0` case determines no mass.

Students must distinguish zero, unknown, not supplied, not determined by the available information, undefined, and not licensed.

### 7. Exactly three routes to trajectory have been licensed so far

At this point in the course, students have three—and only three—licensed ways of determining a particle's trajectory:

| Route | Starting information | Operation |
| --- | --- | --- |
| **Observation** | Successive observed positions and times | Track the particle and record its trajectory. |
| **Newton I** | A free particle in an inertial frame, plus its initial position and velocity | Continue the particle in uniform motion. |
| **Newton II** | A material object, its given inertial mass, a supplied net-force history or rule, an inertial frame, and initial position and velocity | Calculate inertial acceleration, update velocity, and construct the trajectory. |

“Three and only three” means three routes licensed by the mechanics taught **so far**. It is not a claim that no other observational or theoretical method could ever exist.

### 8. Inertial acceleration can be transformed into trajectory

NML1 travelled from a known trajectory to inertial acceleration:

```text
known trajectory -> inertial acceleration
```

NML2.1 also travels in the reverse direction:

```text
given inertial mass + supplied net force
    -> inertial acceleration
    -> velocity
    -> trajectory
```

In continuous form,

$$
\mathbf a(t)=\frac{\mathbf F_{\mathrm{net}}(t)}{m},
$$

$$
\mathbf v(t)=\mathbf v_0+\int_{t_0}^{t}\mathbf a(s)\,ds,
$$

$$
\mathbf r(t)=\mathbf r_0+\int_{t_0}^{t}\mathbf v(s)\,ds.
$$

For younger learners, the same logic can be installed discretely:

```text
known acceleration arrow
    -> change the velocity arrow
    -> use the updated velocity to draw the next path segment
    -> repeat
```

Acceleration alone does not uniquely determine a whole trajectory. The initial position, initial velocity, reference frame, and acceleration history or rule are also required.

The central conclusion is:

> It is possible to know the inertial acceleration of a material object before knowing its future trajectory.

Newton II can supply the acceleration from mass and net force. The future trajectory remains to be constructed from that acceleration and the initial conditions.

### 9. The lesson should end with an acknowledged boundary

NML2.1 can consume a supplied mass value, but Newton II does not itself explain why that value may continue to be reused. The lesson should eventually create a case in which the reuse licence fails.

For younger students, a material object may visibly lose a piece. For advanced students, a cart may leak or a rocket may eject material continuously. The correct response is to halt automatic reuse of the earlier mass, not to improvise an unlicensed replacement.

This creates the need for the later lesson:

> How is a continuing material object identified, how does it acquire a mass address, and what licenses that address to persist?

---

## Part II — Provisional classroom understanding of `material object`

Before NML2.2, `material object` should be introduced as an intuitive concept rather than as the result of a formal construction.

> A material object is the continuing physical thing whose trajectory we describe, whose inertial mass is given, and to which a net force belongs.

The learner may initially recognise a cart, ball, cup, or planet as one material object in the ordinary way that people recognise persisting physical things. NML2.1 uses that intuitive unity without yet analysing how it was achieved.

The minimal classroom picture is:

```text
material object A
    has a trajectory in the chosen frame
    has a given inertial mass
    has a net-force vector over the relevant interval
```

The trajectory is a description associated with the material object, not the material object itself. The supplied mass is a standing fact about that object until a reuse trigger occurs. Newton II joins the object's mass, its inertial acceleration, and its net force.

This is intentionally provisional. NML2.2 may later replace the unanalysed act of “recognising one object” with the explicit trackability, redundancy, tolerance, lumping, and address-construction account. NML2.1 must not presuppose that later derivation.

---

## Part III — Exercise and activity bank

### 1. Primitive ownership exercises

- Circle the material object the question asks about.
- Identify every material object mentioned in a problem.
- Circle or colour each object's mass, acceleration, and supplied net force in a matching colour.
- Draw lines connecting each numerical value to its owner.
- Copy each object's data into a separate row before calculating.
- Cross out irrelevant information.
- Rewrite free-floating symbols as `m[A]`, `a[A]`, and `F_net[A]`.
- Check that material object, time interval, and inertial frame agree before using Newton II.
- Present a tempting problem in which the arithmetic works only by borrowing one object's mass for another. Ask students to diagnose the error.
- Distinguish among:

```text
material object A
the inertial mass belonging to A
the numerical statement m[A] = 4 kg
```

### 2. Quantity, type, and unit sorting

- Sort cards into mass, acceleration, net force, velocity, position, and time.
- Match `kg`, `m s^-2`, and `N` to the correct quantities.
- Sort quantities into scalar and vector columns.
- Add missing directions to vector answers.
- Build `1 N = 1 kg m s^-2` from Newton II.
- Diagnose equations with correct units but mismatched material-object owners.
- Diagnose answers that use the correct owner and magnitude but omit direction.
- Separate zero values from blank, missing, or unlicensed entries.

### 3. Newton-II triplet exercises

- Rotate which two triplet values are supplied and which is demanded.
- Practise `a = F_net/m` and `F_net = ma` as vector relations.
- Use `m = |F_net|/|a|` only in suitable nonzero trials and state why `0/0` does not determine mass.
- Ask how many independent values Newton II requires before the third can be calculated.
- Give all three values and ask whether the triplet is consistent.
- Give only one value and ask students to state precisely why calculation cannot proceed.
- Use three-object grids in which students must choose the correct row and operation.
- Begin with verbal comparison patterns and compress them into `a = F_net/m`.
- Begin with `a = F_net/m` and recover the qualitative comparison patterns.

### 4. Qualitative inertial-mass comparisons

- Same supplied net force, different inertial masses: compare accelerations.
- Same inertial mass, different supplied net forces: compare accelerations.
- Double the net force while holding mass fixed.
- Triple the mass while holding net force fixed.
- Double both mass and net force.
- Rank several material objects by acceleration under the same supplied net force.
- Compare velocity changes only after establishing that the action durations are equal.
- Separate “hard to accelerate sideways” from “hard to lift.”
- Ask the Earth–Moon question:

> The same cart receives the same sideways net force on Earth and on the Moon. Does its sideways inertial acceleration change?

The intended answer is no: gravitational circumstances differ, but the cart's supplied inertial mass and sideways net force are unchanged.

### 5. Zero, missing, undefined, and unlicensed cases

Ask students to classify cases using:

```text
zero
unknown
not supplied
not determined by the supplied information
undefined
calculation not licensed
```

Cases should include:

- finite positive mass and zero acceleration;
- zero net force with nonzero velocity;
- zero acceleration when physical force contributions may still exist;
- the `0/0` attempt to infer mass;
- a blank mass owner;
- a mass value with no identified material object;
- a massless-particle question incorrectly normalised into Newton II;
- a calculation attempted after a mass-reuse trigger.

### 6. Material-object versus trajectory exercises

- Pair a material-object card with its trajectory card while stating that they are not the same entity.
- Show two material objects following the same trajectory and ask whether they must have the same inertial mass. They do not.
- Show one material object described in two reference frames and ask whether the different trajectories imply two different objects. They do not.
- Change a material object's path several times while keeping its given mass card attached.
- Ask which items own mass and net force: the material object, its trajectory, the graph paper, or the reference frame.
- Give a trajectory without a material-object identity and ask what Newton-II calculation is blocked.
- Give a material object with mass and net force but no future trajectory and ask what can already be known. Its acceleration can be known.
- Ask whether a trajectory alone determines inertial mass. It does not.

### 7. Three-routes-to-trajectory exercises

- Sort short scenarios into observation, Newton I, or Newton II.
- For every scenario, circle the starting information that licenses the route.
- Present a free particle with initial conditions and ask why Newton II is unnecessary.
- Present a material object with mass, net-force history, and initial conditions and ask why Newton I is insufficient.
- Present recorded positions and times and ask why this is an observational trajectory rather than a prediction.
- Present a proposed fourth route and ask whether it has been licensed by anything taught so far.
- Give incomplete versions of each route and ask which required input is missing.

### 8. Trajectory-to-acceleration and acceleration-to-trajectory exercises

- Review how changes in velocity reveal inertial acceleration from a known trajectory.
- Classify motion as speeding up, slowing down, turning, doing both, or having zero acceleration.
- Begin with an initial position and velocity and provide an acceleration arrow for each equal time step.
- Update the velocity arrow and use it to draw the next trajectory segment.
- Repeat for acceleration:

  - along the velocity;
  - opposite the velocity;
  - perpendicular to the velocity;
  - changing direction from step to step;
  - zero over selected intervals.

- Supply mass and net force instead of acceleration, requiring students to calculate acceleration first.
- Compare the trajectory from constant-direction acceleration with one from rotating acceleration directions.
- Give acceleration without initial position or initial velocity and ask whether a unique trajectory follows.
- Give mass and net force but no initial conditions and ask students to separate “acceleration known” from “trajectory not yet determined.”
- Use the same acceleration history with different initial velocities to produce different trajectories.

### 9. Net-force inference and provenance exercises

- Give inertial mass and trajectory-derived acceleration; infer the Newton-II net-force vector.
- After the inference, ask students to separate what has and has not been established:

```text
established:
    the net-force vector required by Newton II

not established:
    the physical force contributions
    the acting objects responsible for them
    whether any meter directly measured the net force
```

- Show a newton-meter reading and ask whether it may automatically be renamed the material object's net force.
- Require the safe statement: “The meter measured a force transmitted through the meter.”
- Ask what question remains after Newton II supplies a net-force vector: “Which contributions and acting objects produce it?”
- Give several physically different stories with the same mass and acceleration and ask what Newton II can say identically about all of them.

### 10. Mass ownership, reuse, and halt exercises

- Carry a given mass through ordinary changes of position, velocity, acceleration, direction, and net force.
- Sort events into “continue reuse” and “suspend automatic reuse.”
- Present a two-scene problem in which a piece visibly breaks off.
- Ask whether the old mass may be assigned automatically to the remaining piece.
- Include tempting numerical data after a reuse trigger and award full credit for halting.
- Ask students to reject each invalid conclusion:

```text
the old mass is zero
the new mass is already known
the remainder automatically keeps the original mass
Newton II itself supplies the missing new mass
```

- Use a piecewise problem in which a new mass is explicitly supplied after the event and calculation may resume.
- Use a lost-label exercise in which the numerical mass survives but its material-object owner is missing.
- Ask students to write the minimum safe conclusion after a trigger: “The previous mass is no longer licensed for automatic reuse.”

### 11. Three meanings and additivity exercises

- Sort statements into material-amount mass, gravitational mass, and inertial mass.
- Identify which meaning is used in `m = rho V`, in a scale-based context, and in Newton II.
- Find places where a textbook problem silently substitutes one meaning for another.
- Ask which relation among the three meanings has actually been supplied or established.
- Sort claims into material-amount additivity, measured-mass additivity, and representative or ledger-mass additivity.
- Ask why “two objects together must have the sum of their inertial masses” is not licensed merely by writing an arithmetic sum.
- Use binding energy or the deuteron only as an advanced indication that measured additivity has a tolerance; do not turn it into a core calculation.

### 12. Integrated worksheet candidates

#### 12.1 Three-object ownership sheet

Use a boat, table, and cup. Supply a mass and an opaque net-force vector for each. Students must:

1. identify the demanded material object;
2. mark each value's owner;
3. select the correct row;
4. calculate acceleration without mixing values.

#### 12.2 Newton-II quantity cards

Give separate cards for separate material objects. Fill two triplet slots and ask students to determine the third or state that the trial is insufficient.

#### 12.3 Mystery net-force sheet

Supply a material object's mass and a trajectory from which acceleration can be read. Students infer the net-force vector and then list what remains unknown about its physical provenance.

#### 12.4 Force-to-trajectory sheet

Supply one material object, its mass, its initial position and velocity, and one opaque net-force vector for each interval. Students calculate acceleration and construct the trajectory step by step.

#### 12.5 Audit-then-calculate sheet

Each problem contains an earlier mass statement and a later scene. Students must first decide whether the mass remains reusable. They calculate only when the reuse licence remains intact or a new mass is supplied.

#### 12.6 Error-diagnosis sheet

Errors should include:

- target mixing;
- interval mixing;
- frame mixing;
- unit mixing;
- missing vector direction;
- treating a meter reading as net force;
- treating a trajectory as the material object;
- confusing zero with unknown;
- using `0/0` to infer mass;
- ignoring a mass-reuse trigger.

#### 12.7 Formula-compression sheet

Begin with several same-force/different-mass and same-mass/different-force comparisons. Ask students to construct `a = F_net/m`, then use it to predict new comparisons.

### 13. Demonstrations and investigations

#### 13.1 Low-friction carts under a repeatable action

Use carts with different supplied masses and the same controlled sideways action over the same duration. Compare their velocity changes or accelerations. The demonstration motivates inertial response without using weight as the explanation.

#### 13.2 Hanging balls struck sideways

Use balls of different supplied masses and compare their immediate sideways response to similar taps. Treat this as a qualitative prompt unless the action has genuinely been controlled.

#### 13.3 Constant-kick or controlled-pull device

Use a repeatable device to act on targets of different masses for equal durations. Keep impulse informal unless it has already been introduced.

#### 13.4 Supplied-force simulation

A simulation is the cleanest formal demonstration because it can supply exact net-force vectors, masses, initial conditions, and equal time steps. Students can observe the full chain:

```text
mass + net force -> acceleration -> changing velocity -> trajectory
```

#### 13.5 Several markers on one translating cart

Track several visible markers while continuing to refer to one cart. Use the scene only to seed the distinction between a continuing material object and motion records. Do not yet formalise track redundancy or lump construction.

#### 13.6 Newton-meter misconception demonstration

Place a newton meter in a situation where other physical contributions may also act on the target. Ask what the meter reads and whether that reading alone is licensed as the target's net force.

#### 13.7 Planetary trajectory investigation

Provide time-indexed orbital data and a planet's supplied mass. Students follow:

```text
trajectory
    -> inertial acceleration
    -> Newton-II-inferred net-force vectors
    -> graph of magnitude or direction against orbital position
```

This must not be presented as an independent measurement of net force or as a derivation of the gravitational force law.

#### 13.8 Visible mass-reuse failure

Use a demonstration, animation, or sequence of images in which a material object loses a piece. Ask exactly when the earlier mass statement ceases to support automatic reuse.

### 14. Advanced extensions

- Use a continuous supplied `F_net(t)` with constant given mass.
- Use a position-dependent supplied `F_net(r)` and solve the resulting differential equation from initial conditions.
- Show the discrete force-to-trajectory construction approaching the continuous integral form.
- Differentiate a supplied planetary trajectory twice and infer its net-force history.
- Compare parameterised families of separately supplied fixed-mass material objects.
- Use piecewise-constant mass only when a new mass is explicitly supplied at every boundary.
- Ask the photon-path question and the Newton-II question separately to test whether students normalise the demand to the correct particle type.
- Contrast an instantaneous acceleration value with a complete acceleration history or rule.

### 15. Final boundary or “burn” activities

#### Younger version

A material object visibly loses a piece between two scenes. The worksheet invites use of the original mass in the second scene. The intended success is to refuse the calculation because the old mass is no longer licensed for the new target.

#### Advanced version

A leaking cart or rocket continuously loses material. Invite the tempting substitution

$$
\mathbf F_{\mathrm{net}}=m(t)\mathbf a.
$$

Then reveal that this alone is not sufficient to solve the open-system problem: departing material can carry momentum relative to the retained target. Do not solve the rocket or leaking-cart problem in NML2.1.

The lesson-level conclusion is:

> Newton II can use a mass value, but Newton II does not by itself license that value's continued reuse.

---

## Part IV — Explicit exclusions and later destinations

The following material should not be taught as part of NML2.1:

- adding physical force contributions;
- conventional free-body diagrams;
- calculations with weight, normal reaction, friction, tension, or spring-force components;
- treating a newton meter as a net-force meter;
- treating a scale as an automatic inertial-mass instrument;
- Newton III and interaction-pair analysis;
- centre-of-mass derivations;
- constructing a material object from observed feature-tracks;
- the full account of trackability, redundancy, tolerance, lumping, and representative particles;
- deriving mass additivity from rigidity;
- automatically assigning masses to fragments after a split;
- solving rockets, leaking carts, or other open systems;
- momentum and formal impulse methods;
- torque, rotation, and deformation mechanics.

NML2.1 should leave two cleanly stated open questions:

1. **Mass-address question:** How is one continuing material object identified, given a mass address, and licensed to retain it? This motivates NML2.2.
2. **Net-force provenance question:** Which physical force contributions and acting objects produce the Newton-II net-force vector? This belongs to the later force-composition lesson.
