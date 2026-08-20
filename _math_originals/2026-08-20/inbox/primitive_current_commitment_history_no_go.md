# Primitive Magnetic Current, Ohmic Current, and Charge Transport

## A commitment-history argument for a Newtonian-static electromagnetic branch

**Status:** working analysis note  
**Date:** 2026-08-19  
**Purpose:** isolate a candidate branch boundary in Galilean / instantaneous electromagnetism by refusing to identify several quantities merely because mature electromagnetism gives them the same name, `current`.

---

## 1. There is not one unique "Galilean electromagnetism"

A first source of confusion is the phrase **the Galilean limit of electromagnetism**. The limit is not unique.

José A. Heras shows that, when Maxwell's equations are written in a unit-independent form, **at least three Galilean limits** can be extracted:

1. the **electric limit**;
2. the **magnetic limit**;
3. the **instantaneous limit**, obtained by taking \(c\to\infty\).

The first two are ordinary nonrelativistic limits: they assume \(|\mathbf v|\ll c\) together with different relative scalings of electric and magnetic effects. The third is conceptually different. It sends the propagation speed to infinity. Heras emphasizes that the electric and instantaneous limits can have the same equation form while having different interpretations, because they were reached by different limiting commitments.

This matters structurally. A statement such as

> "Under a Galilean transformation, \(\mathbf E\) and \(\mathbf B\) transform as ..."

is incomplete unless the branch is named.

Marc de Montigny and Germain Rousseaux make the same point for the electric and magnetic limits: failure to distinguish them can lead to an **incoherent mixture** of two different Galilean theories.

The analogy with the complex logarithm is useful. The unrestricted complex logarithm is not a single-valued function until a branch is selected. Likewise, an unqualified appeal to "Galilean electromagnetism" can hide a branch choice.

### 1.1 Electric limit

The electric limit is the regime in which electric effects dominate magnetic effects. In this branch the electric field is the more nearly invariant object, while the magnetic field receives the boost-dependent correction. The current and charge transformations belong to that same electric-limit package.

### 1.2 Magnetic limit

The magnetic limit is the regime in which magnetic effects dominate electric effects. In this branch the magnetic field is the more nearly invariant object, while the electric field acquires the familiar motional correction. The source transformations are correspondingly different from those of the electric limit.

### 1.3 Instantaneous limit

Heras also considers an **instantaneous limit** obtained by

\[
c\to\infty.
\]

Its physical interpretation is that propagation becomes instantaneous rather than merely slow compared with \(c\). In the static sector Heras writes the unit-independent field equations in the form

\[
\nabla\cdot\mathbf E=\alpha\rho,
\qquad
\nabla\times\mathbf E=0,
\]

\[
\nabla\cdot\mathbf B=0,
\qquad
\nabla\times\mathbf B=\beta\mathbf J.
\]

No propagation speed occurs in these strictly static equations.

### 1.4 The branch discipline used in this note

The argument below studies an even more specific candidate, which will be called the **strict Newtonian-static sheet**.

It has the following intended commitment:

> At an instant, a primitive field source determines its field from the instantaneous source configuration. Giving the whole source configuration an arbitrary uniform Galilean boost does not, by itself, alter the source variable or slant the source-attached field.

This is modeled on Newtonian gravity: the Newtonian gravitational field of a point mass depends on its instantaneous position and mass, not on an additional source-velocity argument.

**Important:** this strict sheet is the object being tested here. It must not be silently identified with every transformation rule Heras obtains by taking limits of relativistic electromagnetism. In particular, if a transformation law already assumes that charge density and current form one inherited electromagnetic source structure, that law cannot be used to prove that those quantities must be identified in the first place.

That would go around the branch cut.

---

## 2. The methodological rule: preserve commitment history

The same symbol \(\mathbf J\) is conventionally used in several places:

- Biot-Savart / Ampere magnetostatics;
- Ohm's law;
- charge transport, such as \(\rho\mathbf v\).

Mature electromagnetism identifies these uses. But when reconstructing the theory from its commitments, that identification cannot be assumed merely because the same word, **current**, is normally used for all of them.

The safe procedure is to give each genealogy its own symbol until an explicit bridge is supplied.

Define:

\[
\rho_E
\]

as the **electric-field source density**;

\[
\mathbf K_B
\]

as the **magnetic-field source**;

\[
\mathbf K_O
\]

as the **Ohmic response quantity**;

and

\[
\mathbf K_T
\]

as the **charge-transport quantity**.

The central rule is:

\[
\boxed{
\text{Do not write all of these as }\mathbf J\text{ until the equalities have been separately licensed.}
}
\]

---

## 3. Magnetic-source current as a primitive

On the strict static magnetic side, let \(\mathbf K_B\) be whatever quantity sources the magnetic field:

\[
\boxed{
\nabla\times\mathbf B=\beta\mathbf K_B
}
\]

with

\[
\nabla\cdot\mathbf B=0.
\]

Equivalently, \(\mathbf K_B\) is the source appearing in the corresponding instantaneous Biot-Savart solution.

Nothing in this definition says

\[
\mathbf K_B=\rho\mathbf v.
\]

That would be a new statement.

The point is conceptual: **magnetic-source current is defined by its role in the magnetic field law, not by an inherited picture of little charges moving through space.**

---

## 4. Ohm's law introduces a second genealogy

Independently define an Ohmic response quantity by

\[
\boxed{
\mathbf K_O=\sigma\mathbf E.
}
\]

At this stage, no contradiction exists and no identity with the magnetic source has been established.

The statement

\[
\boxed{
\mathbf K_B=\mathbf K_O
}
\]

is therefore an **additional bridge law**:

> The quantity produced by the Ohmic constitutive relation is the same quantity that sources the magnetostatic field.

This bridge is legitimate if stated explicitly. What is illegitimate, from a commitment-history perspective, is to hide it by using the same symbol \(\mathbf J\) on both sides from the beginning.

### 4.1 This bridge does not immediately contradict statics

Suppose

\[
\mathbf K_B=\mathbf K_O=\sigma\mathbf E.
\]

Magnetostatics gives

\[
\nabla\cdot\mathbf K_B=0
\]

because the divergence of a curl vanishes. Therefore

\[
\nabla\cdot(\sigma\mathbf E)=0.
\]

For homogeneous constant \(\sigma\),

\[
\nabla\cdot\mathbf E=0.
\]

Together with Gauss's law,

\[
\nabla\cdot\mathbf E=\alpha\rho_E,
\]

this yields

\[
\rho_E=0
\]

in the homogeneous bulk.

That is a constraint, not a contradiction. Surface or boundary charge may still support an electric field inside a conductor while the bulk charge density vanishes.

So the easy theorem

\[
\text{Ohm}+\text{Biot-Savart}\Rightarrow\bot
\]

does **not** follow here.

---

## 5. The third genealogy: literal charge transport

Now independently define charge transport:

\[
\boxed{
\mathbf K_T=\sum_s\rho_s\mathbf v_s,
}
\]

where \(s\) labels charged species.

This is the ordinary kinematic transport construction: charge density multiplied by coordinate velocity, summed over species.

Again, nothing yet implies

\[
\mathbf K_T=\mathbf K_B
\]

or

\[
\mathbf K_T=\mathbf K_O.
\]

Those are further bridge claims.

---

## 6. Galilean transformation of charge transport

Consider a Galilean boost by constant velocity \(\mathbf V\). Each particle/species velocity transforms as

\[
\mathbf v_s'=\mathbf v_s-\mathbf V.
\]

If charge density itself is unchanged under the ordinary Galilean spatial transformation, then

\[
\begin{aligned}
\mathbf K_T'
&=\sum_s\rho_s\mathbf v_s'\\
&=\sum_s\rho_s(\mathbf v_s-\mathbf V)\\
&=\mathbf K_T-\mathbf V\sum_s\rho_s.
\end{aligned}
\]

Writing the total charge density as

\[
\rho=\sum_s\rho_s,
\]

we obtain

\[
\boxed{
\mathbf K_T'=\mathbf K_T-\rho\mathbf V.
}
\]

This transformation follows directly from the transport definition and Galilean velocity addition. No electromagnetic field transformation has been imported.

---

## 7. The strict Newtonian-static source commitment

The strict sheet now adds its defining source commitment:

> A common uniform boost of the complete source configuration does not, merely by changing the coordinate velocity of that configuration, alter the primitive instantaneous magnetic-source quantity.

Therefore

\[
\boxed{
\mathbf K_B'=\mathbf K_B.
}
\]

This is the analogue of the Newtonian gravitational statement that the field of a source at a given instantaneous position does not acquire a new source term merely because the whole source is assigned a different uniform translational velocity.

This is the crucial assumption being tested. It is **not** being derived from relativistic electromagnetism.

---

## 8. No-go theorem for identifying magnetic source with charge transport

Now suppose we impose the bridge

\[
\boxed{
\mathbf K_B=\mathbf K_T
}
\]

and demand that it hold in every Galilean frame.

In the original frame,

\[
\mathbf K_B=\mathbf K_T.
\]

In the boosted frame the bridge requires

\[
\mathbf K_B'=\mathbf K_T'.
\]

But the two transformation rules derived above give

\[
\mathbf K_B'=\mathbf K_B,
\]

and

\[
\mathbf K_T'=\mathbf K_T-\rho\mathbf V.
\]

Therefore

\[
\mathbf K_B
=
\mathbf K_T-\rho\mathbf V.
\]

Using the original-frame bridge \(\mathbf K_B=\mathbf K_T\),

\[
\rho\mathbf V=0.
\]

For arbitrary Galilean boosts,

\[
\boxed{
\rho=0.
}
\]

Hence:

> **On the strict Newtonian-static sheet, a primitive boost-invariant magnetic-source quantity cannot be identified Galilean-covariantly with literal charge transport for a source carrying nonzero net charge density.**

Equivalently, at least one of the following commitments must be abandoned:

1. the magnetic source is a primitive instantaneous Newtonian-static source;
2. magnetic-source current is literally charge transport;
3. Galilean relativity holds for the theory.

This is the candidate branch boundary.

---

## 9. The decisive witness: one moving charged particle

A neutral wire is a bad first witness because neutrality hides the conflict. A single charged particle is cleaner.

Consider one charged particle.

In one inertial frame it moves with velocity

\[
\mathbf v\neq0.
\]

The charge-transport construction assigns

\[
\mathbf K_T\sim\rho\mathbf v.
\]

Now boost into the particle's rest frame. Then

\[
\mathbf v'=0,
\]

so the transport quantity becomes

\[
\mathbf K_T'=0.
\]

But on the strict Newtonian-static source picture, changing inertial frame cannot by itself erase or create the primitive magnetic source:

\[
\mathbf K_B'=\mathbf K_B.
\]

Therefore the identification

\[
\mathbf K_B=\mathbf K_T
\]

cannot hold in both frames unless the magnetic source was zero to begin with.

This is the simplest geometric witness to the no-go.

---

## 10. Why the neutral-wire ant example hid the problem

For a neutral wire,

\[
\rho_{\text{total}}=0.
\]

Therefore the transport transformation reduces to

\[
\mathbf K_T'
=
\mathbf K_T-\rho_{\text{total}}\mathbf V
=
\mathbf K_T.
\]

So the literal transport current happens to be Galilean-invariant under a common transverse boost.

This is why the ant construction was so slippery.

The negative lattice charge and positive carrier/lattice bookkeeping can cancel the boost contribution. In the neutral case, the two genealogies

\[
\mathbf K_B
\quad\text{and}\quad
\mathbf K_T
\]

can masquerade as the same quantity.

The single non-neutral moving charge removes that accidental degeneracy.

---

## 11. What happens to Ohm's law?

The result is subtler than the initially hoped-for claim that Ohm's law is simply inconsistent with Newtonian statics.

On the strict sheet, the bridge

\[
\boxed{
\mathbf K_B=\mathbf K_O
}
\]

can be maintained without invoking charge transport at all.

If

\[
\mathbf K_O=\sigma\mathbf E
\]

and the relevant source-attached electric and magnetic quantities are carried unchanged by a common Galilean boost on this strict sheet, then

\[
\mathbf K_B'=
\mathbf K_B
=
\mathbf K_O
=
\sigma\mathbf E.
\]

No transport velocity appears.

Therefore the immediate conclusion is **not**:

\[
\boxed{
\text{Ohm's law is inconsistent.}
}
\]

It is instead:

\[
\boxed{
\text{Ohm's law may survive if its "current" is the primitive magnetic-source / Ohmic-response quantity, not literal moving charge.}
}
\]

The dangerous identification is the additional bridge

\[
\boxed{
\mathbf K_B=\mathbf K_T.
}
\]

Textbook notation normally hides the distinction because all three quantities are written as \(\mathbf J\):

\[
\boxed{
\mathbf K_B
=
\mathbf K_O
=
\mathbf K_T
\equiv
\mathbf J.
}
\]

From a commitment-history perspective, that notation compresses multiple empirical/theoretical bridges into a single word.

---

## 12. Relation to Heras's abstract instantaneous sources

Heras provides an especially suggestive comparison.

In his 2008 discussion of whether Maxwell's equations can be obtained from the continuity equation, he considers **abstract charge and current densities** \(\rho_e\) and \(\mathbf J_e\) that generate instantaneous electric and magnetic fields satisfying a Galilean electromagnetic system.

He then identifies a physical problem: we do not know how to prepare such abstract instantaneous sources in the laboratory for a real moving electron. A real moving electron produces the ordinary retarded Maxwell fields rather than the proposed instantaneous Galilean fields.

This is close to the distinction made here:

> A mathematically coherent primitive magnetic-source variable need not automatically be identified with the literal transport of a real electric charge.

However, a caution is necessary. In Heras's later \(c\to\infty\) construction, the source transformations are obtained by taking a limit of relativistic electromagnetic transformations. Such a procedure already places charge density and current inside a common inherited source structure.

Therefore those transformation laws cannot be used, within the present commitment-history exercise, to prove that \(\mathbf K_B\) and \(\mathbf K_T\) were identical before the bridge was introduced.

Doing so would assume the conclusion.

---

## 13. The branch-cut interpretation

The structural picture can now be written as two different sheets.

### Strict Newtonian-static sheet

\[
\rho_E
\quad\text{primitive electric source}
\]

\[
\mathbf K_B
\quad\text{primitive magnetic source}
\]

\[
\mathbf K_O=\sigma\mathbf E
\quad\text{Ohmic response}
\]

with an optional explicit bridge

\[
\mathbf K_B=\mathbf K_O.
\]

No statement that moving charge necessarily produces magnetism is built in.

### Mature electromagnetic / relativistic sheet

Charge density, current, electric field, and magnetic field belong to one linked electromagnetic structure. Source motion and field transformations are not independent commitments, and the usual single symbol \(\mathbf J\) carries all of this history.

The methodological danger is to begin on the first sheet, encounter a contradiction, and then import a transformation rule or identification whose justification already belongs to the second sheet.

That is the analogue of **going around the branch cut**.

---

## 14. Main result

The argument supports the following candidate theorem.

### Primitive-source / transport no-go

Let a Galilean instantaneous field theory satisfy:

1. \(\mathbf K_B\) is a primitive magnetic-source quantity;
2. a common Galilean boost does not change \(\mathbf K_B\):
   \[
   \mathbf K_B'=\mathbf K_B;
   \]
3. literal charge transport is
   \[
   \mathbf K_T=\sum_s\rho_s\mathbf v_s;
   \]
4. velocities transform Galilei-wise:
   \[
   \mathbf v_s'=\mathbf v_s-\mathbf V.
   \]

Then

\[
\mathbf K_T'=\mathbf K_T-\rho\mathbf V.
\]

Therefore the universal identification

\[
\mathbf K_B=\mathbf K_T
\]

is Galilean-covariant only in the special case

\[
\rho=0.
\]

For a non-neutral source, the identification fails.

### Consequence

A Newtonian-static theory may consistently possess a primitive magnetic-source current, but it cannot in general also define that source as the coordinate-frame transport of electric charge.

The neutral-wire case is exceptional because its total charge density vanishes and the conflict is hidden.

---

## 15. What has and has not been shown

### Shown, conditional on the strict-sheet assumptions

- Magnetic-source current, Ohmic current, and charge-transport current have distinct commitment histories.
- The identification \(\mathbf K_B=\mathbf K_O\) need not itself produce a contradiction.
- Literal transport current transforms as
  \[
  \mathbf K_T'=\mathbf K_T-\rho\mathbf V.
  \]
- A boost-invariant primitive magnetic source cannot be universally identified with literal charge transport when \(\rho\neq0\).
- Neutral conductors hide this conflict because \(\rho_{\rm total}=0\).

### Not shown

- That Ohm's law is itself inconsistent.
- That the strict Newtonian-static sheet is the unique or standard meaning of Heras's instantaneous limit.
- That mature electromagnetism is inconsistent. It is not; it uses a different linked structure.
- That experimental current meters operationally isolate \(\mathbf K_B\), \(\mathbf K_O\), or \(\mathbf K_T\) without further assumptions.

The result is therefore a **commitment-history no-go inside a deliberately frozen candidate theory**, not a claim that ordinary electromagnetism fails.

---

## 16. Open problem

The next question is now sharply posed:

> **What empirical or theoretical bridge first licenses the identification of the primitive magnetic-source quantity with literal charge transport?**

A related question is:

> **When Ohm's law is experimentally stated as \(\mathbf J=\sigma\mathbf E\), which genealogy of \(\mathbf J\) is actually measured, and what additional experiment licenses its identification with the magnetic source or with transported electric charge?**

These questions are preferable to beginning with the mature notation \(\mathbf J\), because the notation has already forgotten the commitment history that the present analysis is trying to recover.

---

## References

1. J. A. Heras, **“The Galilean limits of Maxwell's equations”**, arXiv:1012.1068 (2010).  
   Establishes at least three Galilean limits: electric, magnetic, and instantaneous; the instantaneous limit is obtained by \(c\to\infty\).

2. M. de Montigny and G. Rousseaux, **“On the electrodynamics of moving bodies at low velocities”**, arXiv:physics/0512200 (2005).  
   Reviews the distinct electric and magnetic Galilean limits and warns against mixing them incoherently.

3. J. A. Heras, **“Can Maxwell's equations be obtained from the continuity equation?”**, arXiv:0812.4785 (2008).  
   Discusses abstract conserved charge/current sources generating instantaneous Galilean fields and the difficulty of physically realizing such sources for a real moving electron.

---

## One-sentence summary

> **If magnetostatic current is born as a primitive instantaneous magnetic-field source, then identifying it with literal charge transport is an additional bridge, and on a strict Galilean-static sheet that bridge fails for non-neutral sources even though an Ohmic bridge to the primitive magnetic source may survive.**
