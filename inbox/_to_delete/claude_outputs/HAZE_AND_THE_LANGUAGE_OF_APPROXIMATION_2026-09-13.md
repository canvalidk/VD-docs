# Haze and the language of approximation

**Date:** 2026-09-13.
**Status:** argument draft from the 2026-09-13 conversation (Can and Claude, VD-docs side). Builds on the five haze records VD-Newton holds in `pass to VD-docs/` at `9f9e3f8` (2026-09-10 to 09-12). Not an entry; no relation fields asserted.
**Terminology:** *haze* is Can's name for the bounded piece of a force account that stands for what the account did not include.

## 1. The sentence problem

`3 + 4 = 7` is a true sentence. `3.2 billion + 4 billion = 7 billion` is not, as written, though everyone says it. People have three ways of making it true, and they are not equally good.

The first is to weaken the relation: `3.2 bn + 4 bn ≈ 7 bn`. This has no algebra. Two `≈` sentences chained together do not give a third with the same tolerance, and nothing about how much slack was taken survives into the next line. A trace cannot run on it.

The second is to keep the relation exact and add a piece: `3.2 bn + 4 bn = 7 bn + s`, with `|s| ≤ 0.5 bn` written down. This is a true sentence in the plain sense; formally it is

$$
\exists\, s:\ \|s\|\le\epsilon\ \wedge\ 3.2\,\mathrm{bn}+4\,\mathrm{bn}=7\,\mathrm{bn}+s,
$$

which is what big-O notation abbreviates. Big-O has an algebra: bounds add under addition, scale under multiplication, and pass through integration. Note that "something small" with no number attached is *not* this convention; it is `≈` wearing an equals sign. The bound has to be in the sentence.

The third is to put the bound in the type of the number rather than in a term: "7 billion, to one figure". This is significant-figure arithmetic, and it is inter-translatable with the second convention (`7 bn` to one figure *is* `7 bn + O(0.5 bn)`), but it hides the commitment inside the representation of every quantity. The VD chooses the second convention for the same reason it chooses everything: the commitment must be visible where the audit can see it, and the piece must be a term so the trace can transport it.

## 2. Finite contributions and the bounded extra piece

The force sentence, written in the second convention, is

$$
\mathbf F_{\mathrm{net}}=\sum_{i\in S_\epsilon}\big(\widehat{\mathbf F}_i+\mathbf u_i\big)+\mathbf s_\epsilon,
\qquad
\|\mathbf u_i\|\le b_i,\quad \|\mathbf s_\epsilon\|\le\epsilon .
$$

The account is a finite list of contributions plus one extra piece. The two kinds of summand differ in type, and the difference is the whole content.

A **contribution** is keyed. It has an identity (an acting-object instance), a value or a rule for its value, and its own uncertainty $\mathbf u_i$, which belongs to it and travels with it.

The **extra piece** $\mathbf s_\epsilon$ is unkeyed. It has no identity, only a declared set it must lie in. It is not a member of the interacting-forces-set: it adds nothing to the member count (Logical Consequence 4) and may never be promoted to a member to balance the books (LC 22). It is the closer's term: the closer used to be asked for a universal negative ("no eligible acting-object remains"), which no physical trace can discharge; it is now asked for a bounded claim about the aggregate of everything not admitted, which can be discharged and can be refuted. There is exactly one such term per account, because two of them would merge into one bound.

The one piece of discipline this imposes: haze does not absorb the $\mathbf u_i$. The toy sentence above quietly mixes them, since "3.2 billion" is itself rounded and there is no addend that was left out; as written it is an example of member uncertainty, not of haze. A haze example needs an addend you did not list: `3.2 bn + 4 bn + (whatever I forgot) = 7 bn + s`.

Because the piece is a term, the dynamics act on it. For prescribed forces along a coasting motion,

$$
|x(T)-x_C(T)|\le\frac{bT^2}{2m},
$$

so a force-level bound becomes a position-level bound with an interval attached. This is also what removes the Major Logical Failure structurally rather than by vigilance: there was never a point prediction "5 m" to reinterpret after the fact, only "5 m + s′" with the bound already carried.

## 3. Newton has always been applied this way

No prediction in the history of Newtonian mechanics has used the complete interacting-forces-set. Every one has been a finite list plus a claim, spoken or unspoken, that the rest did not matter at the accuracy in play.

Newton's own Book III orders the planetary perturbations by size and sets the smaller aside. Laplace and Lagrange turned that into perturbation theory: expansions in a small parameter, truncated, with the truncation error estimated — the practice for which Bachmann and Landau later supplied the O-notation. The two most famous tests of the theory are the haze logic run to completion in both directions. In 1846 the residual in Uranus's motion could not be absorbed by the known perturbations at the available precision, so an omitted contribution of a recognised kind was licensed and Neptune was found: the extra piece exceeded its bound, and a keyed member was added. From 1859 Mercury's perihelion advance exceeded every bound the known account could support; the same repair was tried (Vulcan) and failed, and only then was the dynamical law itself put in question. Neither episode makes sense unless the practitioners held a bound on what they had left out and knew when the evidence had exceeded it.

The twentieth century made the piece explicit in separate places that never cited each other. Metrology wrote the propagation rules for the $\mathbf u_i$ (the GUM). Interval arithmetic gave sound enclosures for computations carrying bounds (Moore, 1966). Statistical model calibration gave the extra piece a distribution under the name *model discrepancy* (Kennedy and O'Hagan, 2001). Philosophy of science found the hole from the other side: Cartwright's argument that a force law with only its stated forces is false of every real system, and true only with a ceteris-paribus clause. The haze term is that clause written as a summand with a bound. What none of them did is put it in the force sum as a typed term, unkeyed, one per account, keyed to the closer. The role is old. The placement is the contribution.

## 4. How we talk about approximations, read as hints for the form

The idioms of approximation are not loose talk; each one encodes a constraint the practitioner was actually respecting. Read that way, they say what shape haze has to have.

| What people say | What it is doing | Hint for the form of haze |
|---|---|---|
| "neglect air resistance" | Names the omitted interaction and sets it to zero | This is *not* haze. A named-and-neglected force is a keyed member at nominal zero, with a bound from its own law. Haze is only what was not named. Two different objects; the trace should keep them apart. |
| "to first order", "up to $O(\varepsilon^2)$" | Bounds the remainder as a function of a small parameter, not as a number | $\epsilon$ may be a scale rather than a value, and successive remainders nest — the haze at one order contains the haze at the next. Remainders replace one another; they are never added. |
| "good to three significant figures" | Carries a relative bound in every quantity | The bound is relative to the resultant, and every downstream quantity inherits it. The trace must carry it, not just the force sentence. |
| "within experimental error" | Puts the bound on the observable, not on the force | The tolerance belongs to the question. The force-level $\epsilon$ is derived *backwards* from the observable tolerance through the dynamics, not declared first. |
| "for short times", "over this interval" | Attaches a validity window | Haze is interval-indexed. For state-dependent forces the allowance shrinks exponentially with the interval; it has the same shape as the lumping horizon, $t_{\max}\sim\epsilon^2/D$. |
| "the correction is negligible" (after computing it) vs. "assume no other forces act" | Earns the licence by an estimate, or stipulates it | Two warrants for the same bound: *estimated* and *stipulated*. The account should record which; only the first can be checked without new evidence. |
| "$\pm$" | A symmetric bound | Symmetry is a choice, not a default. Drag is directed; the 09-12 record's persistent friction puts $\mathbf s$ in a half-space, not a ball. The set haze lives in is a set, and may have a direction. |
| "the error is random" | Replaces the bound with a distribution | A different "=" — true in distribution, tested by an evidential rule, never refuted by a single low-probability observation. This is the open type decision (§5). |
| "roughly", "is about" | States no bound at all | The one idiom the account forbids. It is `≈`, and it is where the Major Logical Failure lives. |

## 5. What the hints add up to

Put together, the idioms describe one object: a single unkeyed summand per account, whose value is existentially quantified over a declared set (a ball, a half-space, or a distribution), indexed by a question and an interval, with its warrant recorded as estimated or stipulated, and kept separate from the named-and-neglected members that sit in the account at nominal zero with bounds of their own.

Two things stay open. The first is the type the tracker carries: an interval (sound, but conservative, and growing with the interval) or a distribution (sharper, but the sentence is then only true in distribution and needs an evidential rule to test it). That decision fixes which "=" the force sentence has. The second is the map from the observable's tolerance back to the force-level bound for state-dependent forces, where the linear $bT^2/2m$ no longer applies. Everything in the table survives either choice.

## Sources and scope

The argument is the 2026-09-13 conversation. Its inputs are the five haze records in VD-Newton's `pass to VD-docs/` at commit `9f9e3f8` — in particular the 09-10 argument (three meanings of zero, uncertainties of the included parts versus sufficiency), the 09-11 MFP1 brief, and the 09-12 car record (bounded remainder, explicit nominal zero, required haze) — together with `NML3_LOGICAL_CONSEQUENCES_CONSOLIDATED_2026-08-08.md` (LC 4, 10, 17, 22, 23) and `lumping_horizon_and_thermodynamic_boundary.md` for the interval shape. External references are named in the text at the level of the claim they support (Principia Book III; Bachmann–Landau O-notation; Le Verrier and Adams, 1846; Le Verrier, 1859, and the Vulcan hypothesis; JCGM 100 / GUM; Moore, *Interval Analysis*, 1966; Kennedy and O'Hagan, 2001; Cartwright, *How the Laws of Physics Lie*, 1983). None of these is being claimed as a source of the placement; they are the sources of the pieces. This is a scoped argument, not a literature review or a priority claim.
