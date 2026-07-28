# From Hooke's Coil to the Classroom One-Axis Spring

**Project:** VD Newton / acting-object development  
**Status:** working explanatory note  
**Purpose:** Record the chain of ideas connecting Hooke's experimental setup, Feynman's argument for Hookean behaviour, the typed forms of the spring-law equation, the classroom one-axis spring, and the VD payoff.

---

## 0. One-sentence thesis

The classroom one-axis spring is not a primitive object. It is an **interface-reduced Hookean-response object**: a possibly complex elastic body whose many internal deformation modes have been filtered by geometry, contact, and constraints until the outside object sees one scalar displacement and one scalar restoring load.

In VD terms, the word **spring** hides at least four separable things:

```text
1. a material construction, such as a coil, rod, rubber band, beam, or elastic body;
2. a deformation slot, such as extension, compression, bend, twist, strain, or a generalized coordinate;
3. a response slot, such as load, force component, vector force, torque, stress, or generalized force;
4. a direction/interface rule, which determines how the response is delivered to another object.
```

The main conclusion is:

```text
Hooke's law is best treated as a typed linear-response pattern, not as one
fully specified spring acting-object.
```

---

## 1. The tiny question that opens the branch

The starting question was:

```text
When a textbook writes the extension of a spring, is the direction meant to be
fixed, like i-hat, or state-dependent, like r-hat?
```

That is not a small notation issue. It exposes a hidden modelling split.

### Fixed-axis form


a scalar displacement along a chosen axis:

\[
\vec F=-kx\,\hat e.
\]

Here:

```text
x      : signed scalar displacement
k      : scalar stiffness
hat e  : fixed direction rule
F      : vector force after multiplying by the fixed direction
```

The vector direction is not contained in `k`. It is supplied by the fixed axis.

### Central endpoint form


a distance-changing connector between two endpoints:

\[
\vec R=\vec r_B-\vec r_A,\qquad \ell=\|\vec R\|,\qquad \hat R=\vec R/\ell,
\]

\[
\vec F_B=-k(\ell-L_0)\hat R.
\]

Here:

```text
ell - L0 : scalar length-extension
hat R    : state-dependent direction rule
k        : scalar stiffness
F_B      : vector force on endpoint B
```

This is not the same object as the fixed-axis form. In the fixed-axis form, the direction is supplied by a rail, guide, or coordinate convention. In the central endpoint form, the force direction is regenerated from the current endpoint geometry.

### First VD lesson

The phrase **extension of a spring** is under-typed. It does not say which deformation slot is being read, nor how that deformation becomes a force delivered to another object.

---

## 2. Hooke's historical object: load-deflection before vector force

Hooke's 1678 statement is the famous:

> *Ut tensio, sic vis.*

The nearby English explanation says, in compressed form, that the restoring power of a spring is proportional to its tension. Hooke also describes the rule operationally: increasing the applied power increases the stretch or bend in the same proportion. The original setup is naturally read as a **load-deflection relation**, not yet as a fully vector-valued force law.

A good VD name for this historical object is:

```text
Hooke load-deflection springing-body demonstrator
```

Its slots are:

```text
material object:
  springing body, often demonstrated with a coiled wire or elastic body

input/readout pair:
  applied load magnitude
  measured deflection or extension magnitude

law pattern:
  load magnitude proportional to deflection magnitude
```

So the most historically conservative type is:

\[
F = kx
\]

with:

```text
x : scalar deflection / extension
F : scalar applied load or restoring load magnitude
k : scalar load-per-extension coefficient
```

This is **not yet** a fixed-axis vector force object. To get the vector object, we must add a direction convention:

\[
\vec F=-kx\,\hat e.
\]

That extra \(\hat e\) is a real modelling slot.

### Load vs force

For the historical experiment, **load** is often the better word than force, because the experiment reads a scalar applied weight or pulling magnitude against a scalar elongation. In a VD Newton trace, a load can later be converted into an attached-force vector only after a direction and sign convention are supplied.

```text
scalar load law + chosen direction/sign = fixed-axis attached-force rule
```

---

## 3. Feynman's argument: stable equilibrium, not arbitrary proportionality

Feynman's argument does not merely say:

```text
some deformation -> some linear map.
```

The sharper reading is:

```text
stable equilibrium -> local restoring response -> linear approximation for small displacement.
```

The key fact being exploited is that the system has a stable, unmoving equilibrium. Strictly, the minimum belongs most naturally to the potential energy landscape, while the force vanishes at equilibrium and is derived from the gradient:

\[
\vec F=-\nabla U.
\]

In one dimension, let \(q_0\) be the equilibrium coordinate and let \(x=q-q_0\). At equilibrium,

\[
\left.\frac{dU}{dq}\right|_{q_0}=0.
\]

If the equilibrium is stable, then locally:

\[
U(q_0+x)\approx U(q_0)+\frac12kx^2,\qquad k>0.
\]

Therefore:

\[
F=-\frac{dU}{dx}\approx -kx.
\]

So Feynman's argument licenses the following object:

```text
quadratic-minimum restoring element
```

with slots:

```text
equilibrium state:
  q0

deformation:
  q - q0

stability condition:
  q0 is a local minimum of potential energy

response rule:
  restoring response is the negative derivative/gradient of the local quadratic energy

one-coordinate reduction:
  F = -kx
```

In one dimension, the direction of the restoring force is automatically opposite the displacement. If the displacement is along \(+\hat e\), the restoring force is along \(-\hat e\).

In more dimensions, the local expansion is:

\[
U(\vec r_0+\vec x)\approx U(\vec r_0)+\frac12\vec x^TH\vec x,
\]

so:

\[
\vec F\approx -H\vec x.
\]

Here \(H\) is the Hessian of the potential at equilibrium. If \(H=kI\), then the force is exactly opposite the displacement vector. If \(H\) is anisotropic or coupled, the response is restoring but not necessarily exactly radial.

### Feynman's coil point

Feynman also explains why a long coil can show a large visible extension: the vertical elongation comes from many tiny twists/deflections along the wire, each adding up over many turns. That means the visible classroom displacement is not a primitive deformation. It is a macroscopic readout of distributed local deformation.

This becomes important later: repeated material structure can enlarge the apparent proportional range.

---

## 4. The typed forms of the spring-law equation

The equation \(F=-kx\) is not self-typing. The symbols change type depending on what is being modelled.

### 4.1 Scalar load-deflection law

\[
F=-kx
\]

```text
x : scalar extension/compression/deflection
F : scalar load or scalar restoring force component
k : scalar stiffness
```

This is closest to Hooke's experimental load-extension relation.

### 4.2 Fixed-axis vector attached-force law

\[
\vec F=-kx\,\hat e
\]

```text
x      : scalar signed displacement along fixed axis
hat e  : fixed direction supplied by guide, rail, or coordinate choice
k      : scalar stiffness
F      : vector attached-force
```

This is not merely the scalar law. It is the scalar law plus a direction rule.

### 4.3 Central endpoint elastic connector

\[
\vec F_B=-k(\|\vec r_B-\vec r_A\|-L_0)\,\widehat{(\vec r_B-\vec r_A)}
\]

```text
extension slot:
  endpoint-distance change

direction rule:
  current radial unit vector between endpoints

stiffness:
  scalar k
```

This is a spatial connector, but still a one-dimensional response along the endpoint line.

### 4.4 Vector displacement oscillator

\[
\vec F=-k\vec x
\]

```text
x : vector displacement from equilibrium point
F : vector force
k : scalar only if the response is isotropic
```

More generally:

\[
\vec F=-K\vec x.
\]

```text
K : vector displacement -> vector force
K : stiffness matrix
```

### 4.5 Continuum stress-strain body

\[
\sigma_{ij}=C_{ijkl}\epsilon_{kl}.
\]

```text
epsilon : strain tensor field
sigma   : stress tensor field
C       : elasticity tensor, a map from strain tensors to stress tensors
```

This is Feynman's continuum Hooke-law object. It is not a scalar spring constant. It is a fourth-rank tensor relation, often represented as a matrix after choosing notation.

### 4.6 Type rule

The clean VD type rule is:

```text
stiffness = map from deformation-type to response-type
```

So the stiffness object is scalar only when the exposed deformation and response slots are scalar.

---

## 5. Why the spring constant should not usually be made into a vector

One tempting interpretation is:

\[
\vec F=-\vec k x.
\]

This can be made algebraically legal by treating:

\[
\vec k=k\hat e.
\]

But it hides two different modelling facts inside one symbol:

```text
k      : how strong the response is
hat e  : which direction the response is delivered in
```

VD should keep these apart.

Better:

```text
stiffness magnitude:
  k

direction rule:
  fixed hat e, radial hat R, surface normal hat n, or Hessian/map direction

force construction:
  combine stiffness, deformation, and direction rule
```

So the issue is not that Hooke's scalar \(k\) was secretly a vector. The issue is that **the equation was missing its type signature**.

---

## 6. From continuum elasticity to an effective classroom one-axis object

Now suppose the actual material body has a complex stiffness structure. Internally, it is not one scalar coordinate. It has a displacement field:

\[
\vec u:V\to\mathbb R^3.
\]

For small deformations, strain is the symmetric part of the displacement gradient:

\[
\epsilon_{ij}=\frac12(\partial_i u_j+\partial_j u_i).
\]

The strain field has type:

```text
epsilon : V -> Sym(3)
```

Stress has the same rank-two tensor type:

```text
sigma : V -> Sym(3)
```

Linear elasticity gives:

\[
\sigma=C:\epsilon.
\]

where:

```text
C : Sym(3) -> Sym(3)
```

Now attach a wooden block or contact plate to the elastic body and constrain the block so it can move only along one line. The block does not read the whole internal stress field. It reads a surface force transmitted through contact.

If \(\hat n\) is the contact normal, the traction on the contact surface is:

\[
\vec t=\sigma\hat n.
\]

The total interface force is:

\[
\vec F=\int_A\sigma\hat n\,dA.
\]

If the block is constrained to move along \(\hat e\), the generalized force it reads is:

\[
Q=\vec F\cdot\hat e.
\]

and the generalized displacement is:

\[
q=\vec x\cdot\hat e.
\]

Only now do we get the classroom one-coordinate form:

\[
Q=-k_{\mathrm{eff}}q.
\]

### Effective stiffness by mode selection

If the block displacement \(q\) induces a mode shape \(\vec\phi(\vec X)\) inside the elastic body, then:

\[
\vec u(\vec X)=q\vec\phi(\vec X).
\]

The induced strain is:

\[
\epsilon(\vec X)=qB(\vec X),
\]

where:

\[
B=\operatorname{sym}\nabla\phi.
\]

The stored elastic energy is:

\[
U=\frac12\int_V \epsilon:C:\epsilon\,dV.
\]

Substitute \(\epsilon=qB\):

\[
U=\frac12q^2\int_V B:C:B\,dV.
\]

Therefore:

\[
k_{\mathrm{eff}}=\int_V B:C:B\,dV.
\]

and:

\[
Q=-\frac{dU}{dq}=-k_{\mathrm{eff}}q.
\]

### The VD object

This deserves its own name:

```text
interface-reduced one-axis elastic contact
```

Draft definition:

```text
interface-reduced one-axis elastic contact :=
An elastic acting-object produced when a possibly multi-mode elastic body is
coupled to a target through a contact surface and a guide constraint such that
only one generalized displacement is exposed and only the corresponding
projected normal/contact response is transferred to the target.
```

This is what the classroom one-axis spring usually is. It is not the absence of complexity. It is complexity hidden behind an interface that exposes one coordinate.

---

## 7. Repeating the structure materially extends the proportional range

A single local elastic element has a limited linear regime. Its true response may be:

\[
F=-kx-\alpha x^2-\beta x^3-\dots
\]

The linear approximation is good only when \(x\) is small enough.

But if a material construction repeats the deformation structure many times, a macroscopic displacement \(X\) can be distributed across many local deformation sites. If there are \(N\) repeated sites, each one may take roughly:

\[
x_i\approx X/N.
\]

Then each local element remains closer to its small-deformation regime even when the total visible displacement is much larger.

VD name:

```text
repeated-mode Hookean amplifier
```

Draft definition:

```text
repeated-mode Hookean amplifier :=
An elastic construction in which a macroscopic deformation is divided across
many repeated local deformation sites, keeping each site closer to its local
quadratic-minimum regime while the whole construction presents a larger
macroscopic proportional-response range.
```

This is the deeper role of the coil. A coil is not merely a convenient shape. It is a material geometry that converts a visible vertical displacement into many small local twists and bends. That makes Hookean behaviour visible and useful over a human-scale displacement range.

The chain is:

```text
stable equilibrium
-> local quadratic minimum
-> local linear restoring response
-> repeated material geometry
-> distributed small deformations
-> enlarged macroscopic proportional range
-> classroom-visible Hookean response
```

---

## 8. Crystals and the “are connected by springs” claim

This analysis also clarifies the crystal question.

If **spring** means a material coil artifact, atoms in a crystal are not connected by springs.

If **spring** means a Hookean-response link, then in the harmonic approximation neighbouring atoms are connected by springs.

The relevant object is:

```text
crystal harmonic force-constant network
```

Near an equilibrium crystal configuration, the potential energy can be expanded in the atomic displacements \(u_{i\alpha}\):

\[
U\approx U_0+\frac12\sum_{i\alpha,j\beta}\Phi_{i\alpha,j\beta}u_{i\alpha}u_{j\beta}.
\]

Then:

\[
F_{i\alpha}\approx-\sum_{j\beta}\Phi_{i\alpha,j\beta}u_{j\beta}.
\]

So the crystal is not necessarily a network of pairwise central distance connectors. The real harmonic object can be a large stiffness matrix. But if the classifier is force-profile based, it is legitimate to say the atoms are connected by Hookean-response links in the small-displacement regime.

VD phrasing:

```text
They are not connected by material-coil springs.
They are connected by quadratic-minimum restoring links.
They behave like classroom springs because both instantiate Hookean-response
after the relevant deformation slots are chosen.
```

---

## 9. The classroom one-axis spring reconstructed

The classroom object usually written as:

\[
F=-kx
\]

should be reconstructed as:

```text
classroom one-axis spring :=
An interface-reduced elastic acting-object whose internal deformation modes are
hidden behind a one-coordinate contact/constraint interface, so that the target
object is assigned a scalar displacement x and receives a restoring load or
force component proportional to x, within the elastic range.
```

Its witness sheet should include:

```text
material body:
  coil, rod, rubber band, elastic block, or other springing body

interface:
  contact face, hook, endpoint, rail, guide, or attachment

deformation slot:
  scalar x, measured from equilibrium or natural length

response slot:
  scalar load, scalar force component, or attached-force vector after direction is supplied

direction rule:
  fixed axis, contact normal, radial endpoint direction, or generalized coordinate sign

stiffness slot:
  scalar k_eff after mode/interface reduction

validity range:
  small enough deformation that the response remains approximately linear

failure modes:
  nonlinearity, plastic deformation, buckling, tearing, slackness, contact loss, damping, hysteresis
```

---

## 10. Proposed VD entries / handles

These are not final entries, but useful names for later Design 3 work.

### Hookean-response

```text
Hookean-response :=
A small-deformation response pattern in which a selected deformation object
produces a restoring response linearly proportional to that deformation, after
the deformation slot, response slot, and direction/interface rule have been
specified.
```

### Quadratic-minimum restoring element

```text
quadratic-minimum restoring element :=
An acting-object whose selected deformation coordinate is measured from a
stable equilibrium of a potential-energy landscape, so that the leading
nonconstant energy term is quadratic and the leading restoring response is
linear.
```

### Scalar load-deflection demonstrator

```text
scalar load-deflection demonstrator :=
A measurement setup in which a scalar applied load is compared with a scalar
extension, compression, bend, or other deflection of a springing body.
```

### Fixed-axis elastic attached-force object

```text
fixed-axis elastic attached-force object :=
A one-coordinate elastic acting-object in which a signed scalar displacement is
converted into a vector attached-force by multiplying by a scalar stiffness and
a fixed unit direction.
```

### Interface-reduced one-axis elastic contact

```text
interface-reduced one-axis elastic contact :=
An elastic acting-object produced when a possibly multi-mode elastic body is
coupled to a target through a contact or attachment interface and constrained
so that only one generalized displacement and its conjugate response are exposed.
```

### Repeated-mode Hookean amplifier

```text
repeated-mode Hookean amplifier :=
A material construction that enlarges the macroscopic proportional-response
range by distributing a visible deformation across many repeated local
deformation sites, each remaining closer to its own small-deformation regime.
```

### Crystal harmonic force-constant network

```text
crystal harmonic force-constant network :=
A near-equilibrium crystal model in which atomic displacements are related to
restoring forces by the Hessian of the crystal potential energy, producing a
linear force-constant network in the harmonic approximation.
```

---

## 11. What this gives Design 3

The spring case shows why a concrete acting-object cannot merely say:

```text
spring has extension and force F = -kx
```

That wording hides the very information the trace needs.

A Design 3 spring-like acting-object should say:

```text
1. what deformation slot is read;
2. what response slot is written;
3. what direction rule or interface rule converts the deformation into an attached force;
4. what stiffness object has the correct type for that deformation-response pair;
5. what validity range keeps the response Hookean;
6. whether the object is a material construction, a force-profile classifier, or an effective interface-reduced object.
```

So the final VD lesson is:

```text
The classroom spring is a successful compression, not a primitive.

It compresses Hooke's scalar load-deflection law, Feynman's stable-equilibrium
linearisation, continuum stress-strain typing, contact/interface projection,
and repeated-mode range amplification into the familiar one-line equation.
```

---

## 12. References

- Robert Hooke, *Lectures de potentia restitutiva, or, Of spring* (1678), Oxford Text Archive transcription: https://ota.bodleian.ox.ac.uk/repository/xmlui/bitstream/handle/20.500.12024/A44322/A44322.html
- Richard Feynman, *The Feynman Lectures on Physics*, Vol. I, Ch. 12, “Characteristics of Force”: https://www.feynmanlectures.caltech.edu/I_12.html
- Richard Feynman, *The Feynman Lectures on Physics*, Vol. II, Ch. 38, “Elasticity”: https://www.feynmanlectures.caltech.edu/II_38.html
- Richard Feynman, *The Feynman Lectures on Physics*, Vol. II, Ch. 39, “Elastic Materials”: https://www.feynmanlectures.caltech.edu/II_39.html
