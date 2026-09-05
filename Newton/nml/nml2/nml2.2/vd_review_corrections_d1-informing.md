> **Informing copy - do not edit here.**
> **Home:** the `particle_and_mass_origins` discussion - `Newton-analysis/_dscn_particle_and_mass_origins/vd_review_corrections_d1.md`.
> Placed in `nml2.2` because Parts I, II and V are the lesson-facing corrections to the three NML2.2 documents (the pre-water inventory, the 1D redundancy note, the glass-ball example) and the open-item list the lesson still owes. Custody moved to Newton-analysis on 2026-09-05 - the user's call, reversing his 2026-08-26 ruling that the file stay here for its third target's sake, once the lumping note's selection rule made its Part I (the rigidity-vs-redundancy collision) wanted on the analysis side. This copy is what stays behind. This is a read-only copy; refresh from home if the source changes.

---

# VD Newton — Review Corrections Record

**Status:** corrections record, d1
**Project:** VD Newton / NML2.2 and presentation track
**Date:** 24 July 2026
**Source:** adversarial review of `NML2_2_pre_water_student_content_inventory_d1.md`, `one_dimensional_redundancy_vscode_math_d1.md`, `glass_ball_mdp_example.md`

---

## 0. Scope note

Two tracks are now explicitly separated.

```text
LESSON TRACK      NML2.2, third lesson of Newtonian mechanics, first year
PRESENTATION      the volume commitment, the gates, the Mach dispute
```

Parts I and II are lesson-facing. Part III is presentation-facing and is not
expected to enter the lesson. Part V lists what remains open.

---

# Part I — Objections and resolutions

## 1. The redundancy criterion — resolved by splitting into two tolerances

**Objection.** The inventory (§14.1) and the 1D note (§4, §19) use different
criteria without flagging the change. The inventory tests offset preservation:

$$D_{ij}(t)=\bigl\|[\mathbf r_i-\mathbf r_j](t)-[\mathbf r_i-\mathbf r_j](t_0)\bigr\|\le\varepsilon$$

The 1D note tests compactness, $\max|h_i-h_j|\le\varepsilon_h$. These diverge
exactly in the fluid case: a stretching packet fails the first and passes the
second; a rigid convoy passes the first and fails the second.

**Resolution.** The offset criterion is the wrong one — it forbids rotation.
Replace it with distance preservation:

$$\Bigl|\;\bigl\|\mathbf r_i(t)-\mathbf r_j(t)\bigr\|-\bigl\|\mathbf r_i(t_0)-\mathbf r_j(t_0)\bigr\|\;\Bigr|\le\varepsilon_{\text{shape}}$$

Rotation preserves distances; bending does not. Objects may spin, may not bend.

Then carry **two** tolerances rather than one, and name what each buys:

| test | criterion | what it licenses |
|---|---|---|
| $\varepsilon_{\text{shape}}$ | distance preservation | the bundle is a **body** |
| $\varepsilon_{\text{trans}}$ | residual scatter about a chosen member | the body is **one particle** |

- Pass both → point particle. Any member track serves as representative. No
  centroid required.
- Pass shape only → rigid body with resolved rotational freedom. The
  representative must become a constructed centroid, which needs the CoM
  theorem, which needs Newton III. Out of licence at NML2.
- Pass neither → deformable. Subdivide.

The second tolerance is the protection: the centroid is only needed once spin is
resolved, and once spin is resolved the lesson has already ended. The criterion
is safe precisely where it is used.

**Two consequences to record.**

*Frame.* Distance preservation is invariant under arbitrary time-dependent
rotations of the observation frame, since it compares distances between
simultaneous positions. The criterion therefore cannot distinguish a spinning
body from a static body viewed from a carousel. This is an improvement on
§14.6: the inertial-frame commitment now does its work at the Newton II step
rather than leaking backwards into lumping.

*Interval coupling.* Velocity spread $\varepsilon_v$ over an interval of length
$T$ generates position spread of order $\varepsilon_v T$. So

$$\varepsilon_v T\lesssim\varepsilon_h$$

is a constraint on admissible interval length, not a free choice. This is what
forces re-lumping over a long fall.

**Also retained:** the 1D note's $\max|h_i-h_j|\le\varepsilon_h$ is a
*localisation* criterion, not a redundancy criterion. Keep both, named
separately. Redundancy asks whether following all supplies more than following
one; localisation asks whether the representative's position stands in for the
members'.

---

## 2. The force pipeline — objection withdrawn on scope

**Objection.** Mass receives address, value, provenance, uncertainty, failure
modes, expiry and reconstruction. Force is assumed. §19.1's dynamical route
requires an independently licensed net force, and the weight route measures
$F_g[S]$ and supplies $g$, both with unformalised failure modes.

**Resolution.** Withdrawn. Forces are the next lesson, and the determination
procedures in Part VIII are supplied as unjustified worked examples. The
teachable content is *what you would do if you knew where the value came from*,
not the values themselves.

**Two changes still required.**

1. **Declare the framing.** §19.1 currently reads as a justification: the
   dynamical route "is the reference route for inertial mass because it
   determines the quantity through its Newton-II role." As written, a reader
   cannot tell which parts are load-bearing. One paragraph at the head of Part
   VIII fixes it.

2. **Rebalance the checklist.** If the procedures are unjustified examples, the
   assessable content is the **record form** (§20 — inputs, assumptions, output,
   provenance, failure modes, re-determination triggers). The checklist gives
   the five families five lines and the record form none. Invert that weighting.

---

## 3. $M_A = M_B$ — partially retracted

**Objection as filed.** The partition equation and the assembly equation were
claimed to be different premises at different grades, making the boxed
$M_B = 1\ \mathrm{kg}$ overclaimed.

**Retracted.** They are the same additivity rule. Under the complete-coverage
stipulation the $t_0$ application is a refinement of the actual lumping, so it is
ledger additivity: analytic relative to lumping, exact. That half of the
objection is withdrawn.

**What survives.** The deduction works by cancelling a shared right-hand side:

$$M_A=\sum_i m_i,\qquad M_B=\sum_i m_i\;\;\Longrightarrow\;\;M_A=M_B$$

But the two sums are written at different times. That the $m_i$ in the second are
*the same numbers* as the $m_i$ in the first is not syntax. It is $n$ persistence
certificates plus mass-locality, one per fragment, across the scatter interval.
Every failure mode in §5.6 is a failure of exactly that co-reference.

**Action.** State the premise set explicitly:

```text
ledger additivity          (applied twice, same rule)
+ n persistence certificates   (one per P_i, across the interval)
+ material closure
-> M_A = M_B
```

The middle line is currently invisible because it is hiding inside the notation.

**Worth keeping as a result.** The whole reconstruction runs on **unbound**
addresses. No fragment mass is ever determined, and $M_B$ still follows. That is
the cleanest available demonstration that owning a mass and having a mass come
apart.

---

## 4. The flake pipeline — resolved, and promoted

**Objection as filed.** In the glass ball, $M_A=m[S]+m[R]$ holds only above the
measurement boundary. Sub-resolution loss $\delta\ge 0$ biases $m[R]$ upward,
always, never downward. The stated budget
$u(m[R])^2\approx u(M_A)^2+u(m[S])^2$ is a variance formula and cannot carry a
bias.

**Resolution — the objection's destination was wrong.** Absorbing $\delta$ into
an uncertainty budget is precisely what §28's halt discipline forbids: a value
borrowed without an address. The correct move is to give the lost material an
address and run it through the ordinary machinery.

### 4.1 The flake route

This is not an exception. It is the standard procedure for **all** suspected
unrepresented material, and it is reused wherever coverage is in doubt.

```text
suspected unrepresented material
  -> instantiate as a target with its own address
  -> bind it by the negligibility determination
  -> carry the resulting bound through the ledger
  -> re-audit if the bound is later violated
```

For the glass ball:

$$M_A = M_B + m_1$$

where $m_1$ is the flake target. The negligibility determination binds a bound,
and the deduction $M_A = M_B$ follows within it.

### 4.2 The bound is not zero

A zero-mass target cannot take Newton II — $a = F/0$. The binding is a bound,
not a value:

$$0\le m_1\le m_{\text{tol}}$$

so the deduction lands as

$$M_B\in\bigl[M_A-m_{\text{tol}},\;M_A\bigr].$$

The one-sidedness of the original objection survives, but as a declared
asymmetric bound on a named target rather than as a hidden bias. That is the
right disposition: the observation was correct, the proposed destination was not.

### 4.3 It is a distinct determination family

Negligibility is not dynamical, density, gravitational, assembly, or partition.
It is a determination whose output is a **bound** rather than a value, and §19
has no slot for it. Add it as a sixth family with the ordinary record: inputs,
assumption, failure conditions, re-determination trigger. Without that slot the
flake route reads as an exception being made rather than a procedure being
followed.

### 4.4 The load-bearing gap: coverage has no mass scale

The flake route depends on coverage being a genuine precondition. It is — but
coverage is currently parameterised by the wrong quantity.

§9.2 records coverage as
$\operatorname{coverage}(\mathcal F;\mathrm{ROI},\varepsilon,[t_0,t_1],Q)$,
inheriting $\varepsilon$, which throughout the inventory is a **position**
tolerance from $D_{ij}\le\varepsilon$. A displacement bound does not bound
escaped mass. Wrong units.

**Required addition.** Coverage needs its own budget, declared alongside
$\varepsilon$:

> $\varepsilon_m$ — no unrepresented material transport exceeding
> $\varepsilon_m$ over the declared interval.

Then the pipeline closes:

- material believed above $\varepsilon_m$ → instantiate as a target, run the
  flake route;
- material below $\varepsilon_m$ → covered by the coverage declaration;
- $m_{\text{tol}} = \varepsilon_m$ supplies the bound in §4.2.

Without $\varepsilon_m$, "coverage is a precondition" does load-bearing work on
an undeclared parameter — the exact failure mode the project exists to catch.

**Open sub-item.** $\varepsilon_m$ is presumably an interval total rather than a
rate, so a long interval accumulates and forces re-determination. Same shape as
the $\varepsilon_v T\lesssim\varepsilon_h$ coupling in §1. Needs deciding.

---

## 5. Distinctiveness — retained, reclassified

**Objection.** Distinctiveness is not a coequal coverage aspect; §10.4 concedes
it sits on the tracker–coverage boundary and §12.3 treats it as a pre-filter.

**Resolution — conceded, with a relocation.** Distinctiveness stays, because it
is doing real work that the other four do not: extent, density, balance and
observability are all *where to put seeds in a given scene*, whereas
distinctiveness is *preparing the scene so that seeds exist at all*. Glitter in
the water. It is an intervention, not a selection.

Keep it in the list, but mark it as a different kind of thing. A student
reading five parallel knobs will not see that four are sampling design and one is
experimental preparation.

**New trade-off to add to §11.**

> **distinctiveness vs fidelity** — the more distinctive the tracer, the greater
> the risk that it tracks itself rather than the material. Density mismatch
> raises the Stokes number and the marker slips, which is §4.4's own failure
> mode arriving through the front door.

This is real experimental practice — it is the whole of PIV tracer selection —
and it is a good place for the lesson to touch something a practitioner
recognises.

**Ordering bug, unaffected by the above.** §12.2 audits all five aspects, §12.3
then deletes failed tracks, and extent, density and balance are never re-audited
on the survivors. A family that passes density at 40 nominal tracks can fail it
at 22 real ones. Add the re-audit step.

---

# Part II — The chain example

## 6. Replacing water as the lesson vehicle

After the presentation-track material is removed, the lesson-relevant payload of
the water example is a single claim: *redundancy may be licensed in the
task-relevant dimension only.* Water is an expensive vehicle for it. §36 needs
fourteen fence-posts to stop the example spilling into pressure, viscosity,
surface tension, mass flow and breakup. That much fencing indicates an example
over-powered for its point.

**The inextensible chain over a pulley** carries the same point at a fraction of
the cost.

- **3D redundancy fails exactly.** Elements on the descending side, the ascending
  side and the pulley arc have different velocity vectors, and straight-line
  separations change as elements round the pulley. Both $\varepsilon_{\text{shape}}$
  and $\varepsilon_{\text{trans}}$ fail. No tolerance argument needed.
- **Arc-length redundancy holds exactly.** Project $\mathbf r_i(t)\mapsto s_i(t)$.
  Inextensibility gives $\dot s_i = v$ for every element. The redundancy is exact,
  not tolerance-limited.
- **The projection is onto arc length, not a Cartesian axis**, which makes "the
  dimension the task needs" concrete rather than coordinate-flavoured.

**The pedagogical argument is the strong one.** Every first-year is already
taught to write *the whole chain has one speed $v$*, and none of them is told why
that is allowed. The lesson supplies the licence for a move they already make.
That is the licensing discipline working as designed — the move is ratified, not
revoked, and nothing has to be unlearned.

## 7. Chain and water as a contrast pair

Both project successfully. They differ in what the projection yields.

| | projection | result |
|---|---|---|
| chain | arc length | **one** bundle — common speed, exactly |
| water | fall direction | an **ordered many** — stream stretches under gravity |

This separates two things the 1D note currently runs together: *whether you may
project*, and *how many particles you get once you have*. §7 of the 1D note makes
the ordered-many point but has no foil, so it reads as a caveat rather than as a
result. With the chain in front of it, water becomes the case showing that
projection buys a licence, not an object count — and a stretching stream is the
honest bridge to the rocket / leaking-cart exit.

Water then needs about a page, not a document.

## 8. What the chain forces, and does not yet supply

The chain passes velocity redundancy and **fails localisation**: elements are
spread over the whole chain length, so there is one licensed velocity and no
licensed common position. This is the convoy case, and there is currently no
category for it in the taxonomy. See Part V.

---

# Part III — Volume is not a Newtonian quantity

*Presentation track. Not expected in the lesson.*

## 9. The claim

Newton's laws concern point particles. Nothing in them sanctions volume. Volume
enters through $\rho = m/V$, which is treated as Newtonian for historical reasons
and is in fact an additional and unjustified commitment — of the same kind as
the identification of gravitational with inertial mass, or as mass additivity.

**Density mass = inertial mass is a distinct commitment requiring its own
licence.**

## 10. The sharp form of the argument

Do not argue that volume is absent from Newton's text. Argue that volume is **not
constructible from the outputs of the pipeline**.

A volume requires a closed material boundary. Lumping never produces one. §16.4
states this directly: the representative carries no size, shape or orientation.
Lumping outputs bundles of tracked interior points. A convex hull of seeds is an
artefact of where seeding happened, and the true material boundary is a coverage
question §13.2 declares undischargeable.

This is much stronger than an appeal to Newton's silence, and it is a claim about
the machinery rather than about a text.

It also survives the obvious objections: moment of inertia needs
$I=\sum m_i r_i^2$, a mass distribution, not a volume; and Archimedes does not
rescue volume, since buoyancy runs through $p=\rho g h$ and presupposes the
density at issue.

## 11. Length is admissible; volume is not

The 1D note constructs an indefinitely refinable stream of massive particles with
no volume anywhere. $m_\tau$ comes from emission-time labelling; $\lambda=dm/dh$
divides by **particle spacing**, a difference of two positions.

> **Length is a difference of positions. Volume is a measure on a region.**

The first is inside the formalism. The second is not. This states exactly how
much continuity Newton pays for, explains why the 1D construction is legitimate,
and explains why the commitment only bites in three dimensions.

## 12. Do not call $\rho = m/V$ a thermodynamic equation

It is a definition, not an equation of state. No temperature, no entropy, no
heat, and it survives at absolute zero. Stated that way, a thermodynamicist
stands up.

The version that survives:

> **Volume is an extensive state variable that appears in no Newtonian law and
> is conjugate to pressure in the $p\,dV$ work term.**

It does no work in mechanics and is a primary coordinate in thermodynamics. That
is why importing it feels like importing thermodynamics: $V$ *is* the
mechanical–thermal coupling variable, and the moment a body has one, $p\,dV$ is
available and mechanics has an energy channel it did not previously have.

**Corollary worth putting on a slide.** Thermodynamics needs the extensive pair
$(N,V)$. The lumping construction **outputs** $N$ — particle count is its main
product — and **refuses** $V$. The formalism delivers exactly half the
thermodynamic configuration space and cannot deliver the other half.

## 13. Two gates, kept separate

They fail in different places and should not be merged.

| gate | requirement | fails at |
|---|---|---|
| **volume / boundary** | any 3D continuum, including ideal flow | the lumping output — no boundary, no $V$ |
| **constitutive closure** | viscous or compressible media | the force account — needs state discarded at Wall 1 |

## 14. Incompressible ideal flow — the contrast case

This is the best slide in the argument because it is the theory that looks most
Newtonian and still fails.

Ideal incompressible flow **passes** the constitutive gate. Euler's equations are
$F=ma$ on material parcels. Pressure is not thermodynamic there at all — it is a
Lagrange multiplier enforcing $\nabla\cdot\mathbf v=0$, fixed by a Poisson
equation, with no equation of state anywhere. The flow is reversible and
dissipation-free.

It **fails** the volume gate, and fails it definitionally: $\nabla\cdot\mathbf v=0$
*is* a statement that the flow preserves volume.

So the contrast to present is:

```text
inextensible chain     constraint fixes the internal force from kinematics
                       already licensed at lumping. No volume. Closed.

ideal incompressible   constraint fixes the internal force the same way —
flow                   pressure and tension are the same object — but the
                       constraint is on volume. Not closed.

viscous / compressible force account needs a material law over state
                       destroyed at Wall 1. Second gate.
```

Tension in an inextensible chain and pressure in an incompressible fluid are the
same kind of object: an internal force whose value is fixed entirely by a
kinematic constraint, never measured, never given a material law. The chain's
constraint is admissible and the fluid's is not, and the *only* difference is
that one constrains lengths and the other constrains volumes.

That is the cleanest available demonstration that the seam is volume rather than
continuity — a rigid body is continuous mass and perfectly Newtonian.

## 15. The Mach dispute — get there first

*Principia*, Definition I: quantity of matter arises from density and bulk taken
together. Newton defines mass **as** density times volume, on the first page,
before the laws.

Mach attacked exactly this in *Die Mechanik in ihrer Entwicklung* (1883): density
is mass per unit volume, so defining mass by density is circular. Anyone in a
philosophy-of-science audience will have this loaded, so the observation that
$\rho=m/V$ is unlicensed and only looks Newtonian for historical reasons must be
delivered from the podium, not extracted in Q&A.

What the VD adds beyond Mach — and these are real additions, not restatements:

1. **Where the circle is broken.** Mach says the definition is circular. The VD
   says mass is bound at an address by a determination process, and density is
   one such process among several, with its own inputs and failure modes. The
   circle is broken by separating the address from the value.
2. **What volume is for.** Mach has no account of this. The VD does: volume is
   what must be re-imported to obtain a 3D continuum, and it is constructible
   only under a material-boundary commitment that tracking never supplies.
3. **A successor construction.** Mach has none. The VD has a volume-free route to
   extended mass — the 1D projected particle stream — together with a statement
   of its limits.

Framed this way, Definition I stops being an embarrassment in Newton and becomes
the best evidence for the thesis: the very first line of the *Principia* silently
imports the commitment, which is why it has been invisible for three centuries.

---

# Part IV — Terminology

## 16. Rename MDP

"MDP" collides with Markov Decision Process, and the collision is unrecoverable
in a mixed audience. One file is currently named for it
(`glass_ball_mdp_example.md`).

Candidates: **mass determination (MD)**, **mass-binding process**, **mass
valuation**. "Valuation" has the advantage of pairing naturally with "address"
and of carrying no existing technical load in mechanics.

Rename before the presentation, not after. The term appears in every document and
the cost rises monotonically.

---

# Part V — Open items

## 17. Carried forward from this review

1. **No category for "one velocity, no common position."** The chain passes
   velocity redundancy and fails localisation. This is the convoy case flagged in
   the first review and it now has a first-year example sitting on it. The
   taxonomy has point particle, rigid body, and deformable — but no slot for a
   bundle with a licensed common velocity and no licensed common position. This
   is the sharpest gap the review found, because the standard first-year chain
   treatment lives entirely inside it.

2. **The chain's configuration variable is unhandled.** The chain problem needs a
   common $v$, a common $a$, a total $M$, *and* how much hangs on each side. The
   last is a shape fact, and §16.4 says the representative omits shape. So the
   chain forces the representative-omits-shape point and then immediately needs
   the omitted information. Whether that is a defect, a second address, or the
   designed entry to the variable-mass exit is undecided.

3. **$\varepsilon_m$ is new and unratified.** Part I §4.4. It closes the coverage
   half of the persistence certificate, which has been an open item in the
   ratification record, so it should be ratified rather than adopted silently.

4. **Negligibility as a sixth determination family** needs writing into §19 with
   the standard record form.

5. **Interval accumulation for $\varepsilon_m$** — total or rate. Undecided.

6. **Possible bearing on C8.** The flake route resolves a partition by *bounding*
   rather than by determining. Whether bounded partitions are a general partial
   answer to C8, or only work when one side is negligible, is worth a look. The
   glass ball's $M_A = m[S]+m[R]$ is the non-negligible case and gets no help
   from this.

7. **Chain vs water ordering in the ratified split.** The ratification record has
   fluids as a *defeat* case; the 1D note treats water as a *success* case
   rescued by projection. Part II §7 assumes both are intended and that the arc
   runs success → ordered many → exit failure. This reopens a ratified decision
   and should be confirmed against the ratification document, which was not
   retrievable during this review.

8. **The two tracks now want opposite things.** The lesson wants the chain and
   the licence-you-already-use argument. The presentation wants the gates, the
   volume commitment, and Mach. Maintaining them as one document set will
   degrade both.
