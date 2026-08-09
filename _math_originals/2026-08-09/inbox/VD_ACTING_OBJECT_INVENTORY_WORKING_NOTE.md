# Acting-Object Inventory for VD Newton Design 3

**Status:** Working inventory  
**Project:** VD Newton / Design 3  
**Purpose:** Provide a broad preliminary catalogue of concrete `acting-object` candidates for later entry design.

## 1. Scope and provenance

This note is **not yet a literature-derived census of force mechanisms**.

The structure of the inventory is constrained by the current VD Design 3 acting-object architecture, in which a concrete acting object is expected to expose things such as:

- concrete type;
- activation condition;
- action-force;
- reaction-force;
- participant slots;
- parameters;
- modelling assumptions;
- force-accounting targets.

The specific mechanism list below was generated from general mechanics, engineering, fluids, and electromagnetism knowledge rather than from an exhaustive source survey.

Accordingly, the inventory should be treated as:

> a structured brainstorming map of plausible concrete acting-object types, to be researched, consolidated, split, or rejected before final entry-writing.

---

# 2. Working criterion for a concrete acting object

A concrete `acting-object` should represent a **force-producing or force-contributing physical mechanism**, rather than merely a name for a force component.

A useful working picture is:

```text
concrete acting-object
    |
    +-- participants
    +-- activation condition
    +-- parameters / modelling regime
    +-- action-force
    +-- reaction-force
    +-- force-accounting target(s)
```

The central question is:

> What mechanism is present which, when its activation conditions are fulfilled, contributes a force to the target's force account?

This is different from asking merely:

> What do textbooks call this force?

---

# 3. Proposed acting-object inventory

## 3.1 Gravity

| Candidate acting object | Typical action-force | Activation / participants | Notes |
|---|---|---|---|
| `point-gravity_acting-object` | \(\mathbf F=-GmM\,\hat{\mathbf r}/r^2\) | Two massive bodies | Basic Newtonian pair-gravity mechanism. |
| `spherical-gravity_acting-object` | External inverse-square field | Target outside spherical source | Probably a specialisation or modelling theorem rather than fundamentally new mechanism. |
| `uniform-gravity_acting-object` | \(m\mathbf g\) | Target in a region where \(\mathbf g\) is approximated as uniform | Extremely useful effective/local approximation. |

---

## 3.2 Elasticity

| Candidate acting object | Typical action-force | Activation / participants | Notes |
|---|---|---|---|
| `hookean-spring_acting-object` | \(-k\Delta\ell\,\hat{\mathbf e}\) | Spring connected and displaced from natural length | Excellent first concrete acting-object case. |
| `compression-spring_acting-object` | Hookean or nonlinear compression force | Contact plus compression | Unilateral activation: inactive when separated. |
| `elastic-cord_acting-object` | \(T(\ell)\hat{\mathbf e}\) | Cord stretched | Usually supports tension but not compression. |
| `nonlinear-spring_acting-object` | \(f(\Delta\ell)\hat{\mathbf e}\) | Connector deformed | General constitutive elastic connector. |
| `torsional-spring_acting-object` | \(\tau=-\kappa\theta\) | Relative angular displacement | Belongs naturally once rotational mechanics is opened. |

---

## 3.3 Ideal connectors and constraints

| Candidate acting object | Typical action-force | Activation / participants | Notes |
|---|---|---|---|
| `taut-string_acting-object` | \(T\hat{\mathbf e}\) | String attached and taut | `tension` is the force output, not the acting-object itself. |
| `cable_acting-object` | Tensile force along cable | Cable taut | More physical version of ideal string; may include elasticity and mass. |
| `rigid-rod_acting-object` | Axial tension or compression | Bodies linked by rigid rod | Bidirectional constraint unlike an ideal string. |
| `rigid-link_acting-object` | Constraint force | Fixed relative-distance condition | Generalisation of rod. |
| `hinge_acting-object` | Joint reaction force | Bodies connected at hinge | Reaction components normally determined through constraints. |
| `pin-joint_acting-object` | Joint reaction | Pin connection active | Engineering specialisation of hinge. |
| `slider-guide_acting-object` | Reaction perpendicular to allowed motion | Target constrained to slot or rail | Clean example of a geometric constraint mechanism. |
| `smooth-track_acting-object` | Normal constraint force | Target in contact with smooth track | Common textbook case. |
| `pulley-contact_acting-object` | Rope/pulley contact force | Rope wraps pulley | May ultimately be composite. |
| `gear-contact_acting-object` | Tooth contact force | Gear teeth engaged | Engineering extension. |

---

## 3.4 Ordinary solid contact

| Candidate acting object | Typical action-force | Activation / participants | Notes |
|---|---|---|---|
| `normal-contact_acting-object` | \(N\hat{\mathbf n}\) | Surfaces touching / preventing interpenetration | Probably indispensable. |
| `static-friction_acting-object` | Tangential force satisfying \(|F_t|\leq \mu_s N\) | Contact with no slip | Constraint-like magnitude; usually solved from dynamics. |
| `kinetic-friction_acting-object` | \(-\mu_kN\hat{\mathbf v}_{rel}\) | Contact plus sliding | More explicit force law than static friction. |
| `rolling-friction_acting-object` | Resistive contact force or torque | Rolling contact | Effective model. |
| `impact-contact_acting-object` | Large transient contact force / impulse | Collision and deformation | Important for collision mechanics. |
| `compliant-contact_acting-object` | e.g. \(k\delta+c\dot\delta\) | Bodies deform under contact | Useful computational contact model. |
| `adhesive-contact_acting-object` | Attractive contact force | Bonded or adhering surfaces | Covers glue/adhesion-type contact effects. |

---

## 3.5 Damping

| Candidate acting object | Typical action-force | Activation / participants | Notes |
|---|---|---|---|
| `linear-damper_acting-object` | \(-c\mathbf v_{rel}\) | Relative motion across damper | Standard dashpot. |
| `nonlinear-damper_acting-object` | \(-f(v_{rel})\hat{\mathbf v}\) | Relative motion | General damping family. |
| `shock-absorber_acting-object` | Spring plus damping force | Suspension deformation and relative motion | Probably a **composite acting object**, not primitive. |

---

## 3.6 Fluid contact

| Candidate acting object | Typical action-force | Activation / participants | Notes |
|---|---|---|---|
| `pressure-contact_acting-object` | Local traction \(-p\hat{\mathbf n}\,dA\) | Fluid contacting a surface | Potentially the primitive mechanical fluid-contact mechanism. |
| `hydrostatic-pressure_acting-object` | Pressure distribution | Body immersed in static fluid | Specialisation of pressure contact. |
| `buoyancy_acting-object` | \(-\rho V\mathbf g\) relative to gravity direction | Body immersed in fluid | Effective/macroscopic acting object; may instead be derived from pressure-contact contributions. |
| `linear-drag_acting-object` | \(-b\mathbf v_{rel}\) | Relative body-fluid motion | Phenomenological low-speed model. |
| `quadratic-drag_acting-object` | \(-\frac12\rho C_DA v^2\hat{\mathbf v}\) | Relative flow | Common high-Reynolds-number effective model. |
| `stokes-drag_acting-object` | \(-6\pi\eta R\mathbf v\) | Small sphere, low Reynolds number | Excellent example of an acting object with a strict approximation regime. |
| `viscous-shear_acting-object` | Tangential surface traction | Fluid shearing along surface | More local/primitive than a total drag law. |
| `lift_acting-object` | Transverse aerodynamic/hydrodynamic force | Appropriate flow around body | Effective and model-dependent. |
| `magnus_acting-object` | Transverse force from spin plus flow | Rotating body in fluid | Useful later example. |
| `added-mass_acting-object` | Fluid-inertial reaction | Accelerating body in fluid | Advanced; force can depend on acceleration. |
| `history-force_acting-object` | History-dependent viscous force | Unsteady low-Reynolds-number flow | Demonstrates that acting objects need not be memoryless. |

---

## 3.7 Interfaces and membranes

| Candidate acting object | Typical action-force | Activation / participants | Notes |
|---|---|---|---|
| `surface-tension_acting-object` | Surface/interface tension resultant | Liquid interface or contact line exists | Strong candidate for the core inventory. |
| `capillary-contact-line_acting-object` | Force involving \(\gamma\) and contact angle | Three-phase contact line | More specific surface-tension mechanism. |
| `membrane-tension_acting-object` | In-plane membrane tension | Membrane stretched | Bridge between strings, elastic sheets, and continuum mechanics. |

---

## 3.8 Propulsion and imposed actuators

| Candidate acting object | Typical action-force | Activation / participants | Notes |
|---|---|---|---|
| `prescribed-actuator_acting-object` | Supplied \(\mathbf F(t,\mathbf r,\mathbf v,\ldots)\) | Actuator engaged | Useful black-box acting object when internal mechanism is deliberately outside the model. |
| `motor-drive_acting-object` | Drive force or torque | Powered actuator coupled to target | Physically composite but common in engineering models. |
| `person-contact_acting-object` | Measured/modelled contact force | Person pushes or pulls object | Ordinary push/pull should resolve to a contact mechanism rather than become primitive force types. |
| `propeller-thrust_acting-object` | Thrust | Propeller operating in fluid | Effective open-system mechanism. |
| `jet-thrust_acting-object` | Momentum-flux thrust | Jet or exhaust operating | Effective open-system mechanism. |
| `rocket-thrust_acting-object` | Exhaust momentum flux | Mass ejection | Requires care because variable-mass mechanics enters. |

---

## 3.9 Electrostatic and electromagnetic extensions

These probably belong outside the first Newton-only concrete acting-object pack, but they are useful stress tests of the architecture.

| Candidate acting object | Typical action-force | Activation / participants | Notes |
|---|---|---|---|
| `coulomb_acting-object` | \(\frac{q_1q_2}{4\pi\epsilon_0r^2}\hat{\mathbf r}\) | Two charged bodies | Fits the pair-interaction picture well in electrostatics. |
| `electric-field_acting-object` | \(q\mathbf E\) | Charged target in specified electric field | Effective field formulation. |
| `magnetic-field_acting-object` | \(q\mathbf v\times\mathbf B\) | Charged moving target | Newton-III pairing becomes subtler because field momentum matters. |
| `lorentz-actuation_acting-object` | \(q(\mathbf E+\mathbf v\times\mathbf B)\) | Charged target in EM field | Natural later branch. |
| `magnetic-dipole_acting-object` | \(\nabla(\boldsymbol\mu\cdot\mathbf B)\) | Dipole in non-uniform field | Advanced. |

---

## 3.10 Radiation and field-momentum extensions

| Candidate acting object | Typical action-force | Activation / participants | Notes |
|---|---|---|---|
| `radiation-pressure_acting-object` | Momentum-transfer force | Radiation incident on matter | Mechanically usable but a useful stress test because the reaction can reside partly in field momentum. |

---

# 4. Recommended first concrete acting-object programme

The full inventory is too large to turn immediately into separate VD entry clusters.

A much smaller first programme could cover the most structurally informative cases:

1. `point-gravity_acting-object`
2. `hookean-spring_acting-object`
3. `normal-contact_acting-object`
4. `kinetic-friction_acting-object`
5. `static-friction_acting-object`
6. `taut-string_acting-object`
7. `rigid-rod_acting-object` or `slider-guide_acting-object`
8. `linear-damper_acting-object`
9. `drag_acting-object`
10. `pressure-contact_acting-object`
11. `surface-tension_acting-object`

This set deliberately samples several importantly different behaviours:

```text
prescribed pair force
displacement-dependent force
unilateral contact
velocity-dependent force
inequality-constrained force
dynamically determined constraint force
distributed contact
interface force
```

If the acting-object architecture survives all of these cleanly, it will have been stress-tested against much more than the standard spring/gravity examples.

---

# 5. Things that should probably NOT be acting objects

A crucial distinction is between:

```text
physical mechanism
```

and:

```text
name given to the force returned by that mechanism
```

The following should therefore not automatically become concrete acting-object types.

## 5.1 Tension

`tension` is normally a force returned by something like:

```text
taut-string_acting-object
cable_acting-object
elastic-cord_acting-object
```

It is not itself the mechanism.

---

## 5.2 Normal force

`normal-force` is normally the force output of:

```text
normal-contact_acting-object
smooth-track_acting-object
constraint-surface_acting-object
```

The acting object is the contact/constraint mechanism.

---

## 5.3 Friction force

Likewise, `friction-force` is the output.

Possible mechanism types include:

```text
static-friction_acting-object
kinetic-friction_acting-object
rolling-friction_acting-object
viscous-contact_acting-object
```

---

## 5.4 Centripetal force

`centripetal force` should **not** be a concrete acting object.

It names the inward/radial role of the net force in curved motion.

The same radial contribution can be supplied by:

```text
gravity
string tension
normal contact
friction
electromagnetic interaction
or a combination of several forces
```

So:

```text
centripetal-force != force-producing mechanism
```

---

## 5.5 Weight

`weight` is terminology-sensitive.

In many problems it simply names the gravity force on a body:

```text
gravity_acting-object -> gravitational attached-force
```

In some contexts "weight" instead means a support/apparent-weight reading.

It should therefore not automatically become its own acting-object type without first fixing the intended meaning.

---

## 5.6 Push and pull

`push` and `pull` are ordinary-language descriptions of the orientation/effect of contact forces.

They should generally resolve to mechanisms such as:

```text
person-contact_acting-object
normal-contact_acting-object
tension-producing connector
actuator
```

rather than becoming primitive physical mechanisms themselves.

---

# 6. Composite versus primitive acting objects

Some convenient engineering objects may contain several lower-level acting objects.

For example:

```text
shock absorber
    =
spring mechanism
+
damper mechanism
```

Likewise:

```text
car tyre-road interaction
```

might be represented as one large contact acting object, or decomposed into:

```text
normal contact
static friction
rolling resistance
deformation losses
```

Similarly:

```text
buoyancy
```

can be modelled as one effective force mechanism or derived from a distributed set of pressure-contact forces.

This suggests that the acting-object architecture should permit at least two levels:

```text
primitive / lower-level acting object
effective / coarse-grained acting object
```

The distinction may be modelling-relative rather than absolute.

---

# 7. The granularity problem

The inventory exposes an important open Design 3 question:

> When do two force-producing aspects count as one acting object, and when should they count as two?

Consider a block on a rough table.

Possible representation A:

```text
table-block-contact_acting-object
    -> one total vector contact force
```

Possible representation B:

```text
normal-contact_acting-object
static-friction_acting-object
```

Both can reproduce ordinary mechanics.

Likewise, for a body submerged in water:

```text
buoyancy_acting-object
```

might be a legitimate coarse-grained mechanism, while a lower-level representation is:

```text
many pressure-contact contributions over the surface
    -> resultant buoyant force
```

Therefore acting-object identity is unlikely to be fixed purely by textbook force vocabulary.

A future rule may need to consider:

- independence of activation conditions;
- independence of force laws;
- whether one mechanism can remain active while another becomes inactive;
- whether parameters belong to one shared physical apparatus;
- whether splitting produces independently meaningful reaction partners;
- whether one representation is merely a coarse-graining of another;
- what level of decomposition the current question demands.

---

# 8. Suggested taxonomy

A useful first taxonomy may therefore be:

```text
acting-object
|
+-- pair-interaction
|   +-- gravity
|   +-- Coulomb
|
+-- connector
|   +-- spring
|   +-- string
|   +-- rod
|   +-- damper
|
+-- contact
|   +-- normal contact
|   +-- static friction
|   +-- kinetic friction
|   +-- impact
|
+-- geometric constraint
|   +-- track
|   +-- hinge
|   +-- guide
|
+-- continuum contact
|   +-- pressure
|   +-- viscous shear
|   +-- drag
|
+-- interface
|   +-- surface tension
|   +-- membrane tension
|
+-- actuator / open-system
|   +-- prescribed actuator
|   +-- thrust
|
+-- field interaction
    +-- electric
    +-- magnetic
    +-- radiation pressure
```

This should be treated as provisional.

---

# 9. Design implication

The acting-object layer should probably not become:

```text
a giant dictionary of named textbook forces
```

Instead, it should become:

```text
a structured library of force-producing mechanisms
```

where each concrete acting object exposes enough information that the lazy VD trace can ask, when needed:

```text
What mechanism is this?
Who participates?
Is it active?
What force does it return?
What reaction does it generate?
What parameters or approximations are required?
What constraints does it impose?
Where does its reaction land?
```

That is the level at which the acting-object architecture can genuinely remove the blocked human-input gaps seen in earlier traces.

---

# 10. Immediate next research questions

Before final concrete entries are written, the following questions deserve explicit investigation:

1. Which of these mechanisms are treated as independent force laws in standard mechanics and engineering literature?
2. Which are normally understood as derived resultants of more local interactions?
3. Which distinctions in the inventory are merely approximation-regime distinctions?
4. What should determine acting-object granularity?
5. Can one acting object return several force components, or should independently parameterised components always become separate acting objects?
6. How should distributed forces be represented?
7. How should constraint forces whose magnitudes are determined by the global dynamics be encoded?
8. How should acting objects with memory or history dependence be represented?
9. How should coarse-grained acting objects relate to decomposed lower-level acting objects?
10. At what point do electromagnetic field momentum and continuum stresses require extensions to the simple particle-pair reaction architecture?

---

## Working conclusion

The useful target is not an exhaustive list of force **names**.

It is an exhaustive-enough inventory of the recurring **physical mechanisms that can contribute forces to Newtonian force accounting**.

The present list is a first map of that space. Its strongest immediate value is that it exposes the variety the eventual concrete acting-object architecture must survive:

```text
gravity
spring
contact
friction
constraint
damping
fluid traction
surface tension
actuation
field interaction
```

The next major conceptual question is likely not "what other force names exist?" but:

> **What makes one force-producing mechanism one acting object?**
