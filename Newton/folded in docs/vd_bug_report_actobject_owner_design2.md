# VD Bug Report: Acting Object Ownership and Internal Observability

**Date:** 2026-03-06
**Affects:** Acting objects entries (E30–E32), closure triplet (E35–E40)
**Severity:** Structural — does not break existing entries but blocks correct closure detection
**Status:** Identified, fix deferred

---

## Summary

The current acting object entries define acting objects as standalone entities that "have" a paired particle. This means acting objects are not accessible from the particle's side — you can't start at a particle and enumerate its acting objects without searching the entire universe of acting objects. This breaks the requirement that the closure algorithm operate using only information internal to the mechanical system S.

## The Problem in Detail

The closure triplet (E35–E40) needs to determine whether a mechanical system S is closed by checking whether every interaction candidate is a closed interaction. To do this, we need to enumerate all interaction candidates that touch S. An interaction candidate touches S when at least one of the two particles involved (the one receiving the canonical force and the one receiving the reaction force) is in S.

There are four cases for an interaction candidate(p, q, acting_object), where p satisfies the activation condition and q is the paired particle:

**Case 1 (p ∈ S, q ∈ S):** Both forces internal. Should pass closure. Detectable from inside S — we can find acting objects associated with particles in S and verify both endpoints are in S.

**Case 2 (p ∈ S, q ∉ S):** Canonical force on p is internal, reaction force on q is external. Should fail closure. Currently detectable — we start at p, find p's acting objects, and discover that the paired particle q is not in S.

**Case 3 (p ∉ S, q ∈ S):** Canonical force on p is external, reaction force on q is internal. Should fail closure. NOT detectable from inside S under the current design — the acting object belongs to the external particle p, so starting from particles inside S, we have no way to find this acting object. All we observe is an unexplained force on q.

**Case 4 (p ∉ S, q ∉ S):** Both forces external. Irrelevant to S.

The bug is that Cases 2 and 3 are asymmetric in detectability. Case 2 is found by forward-tracing from internal particles to their acting objects. Case 3 can only be detected by observing an orphaned force on q — a force that doesn't match any acting object reachable from inside S.

## Why This Matters

The closure algorithm should work the way a physicist works: examine the particles in your system, examine the forces on them, and from that information alone determine closure. The current acting object design supports a "push" model (starting from the acting object, finding its effects) but not a "pull" model (starting from a particle, finding what acts on it).

This means the closure check can't be a clean iteration over a well-defined set. Instead, Case 3 detection becomes a negative inference: "there's a force here that none of our known internal acting objects explain." While this is physically correct (that's exactly how physicists discover new forces or identify external influences), it means the closure algorithm has two fundamentally different detection mechanisms for what should be symmetric cases.

## Proposed Fix Direction

Invert the ownership relation: acting objects should be properties of their paired particles, not standalone entities. Each particle p would carry a list of acting objects it sources. Concretely:

**Current design:** acting_object → {activation_condition, paired_particle, canonical_force_law}

**Proposed design:** particle.acting_objects → [{activation_condition, canonical_force_law}, ...]

Under this design, for every particle p ∈ S, we can enumerate p.acting_objects and find all interactions that p sources. This covers Case 1 and Case 2 directly. For Case 3, we would iterate over particles in S and check whether any of them are the *target* of an acting object belonging to an external particle — but we still can't access external particles' acting object lists from inside S.

So the ownership inversion alone does not fully solve Case 3. What it does is make the internal bookkeeping cleaner and make the asymmetry between Cases 2 and 3 more visible.

## The Deeper Issue

Case 3 may be irreducibly asymmetric. There might be no way to detect an external acting object firing into your system without either (a) observing its effect as an unexplained force, or (b) expanding your system to include the source particle. This asymmetry might not be a bug in the formalism but a genuine feature of how closed systems work — you can always tell when your own particles are acting outward (Case 2), but an external influence (Case 3) is only visible through its symptoms.

If this is the case, then the correct design acknowledges the asymmetry explicitly rather than trying to make both cases look the same. The closure check would have two legs:

1. **Internal completeness:** For every acting object sourced by a particle in S, verify the paired particle is also in S. (Catches Case 2.)
2. **No unexplained forces:** For every particle in S, verify that every force in its interacting forces set can be attributed to an acting object sourced by some particle in S. (Catches Case 3.)

Whether this two-legged check can be encoded minimally in E35 and E39 — without redundancy and without the double-counting problem — is the open design question for the closure triplet.

## Entries Affected

The following entries would need revision once the fix is implemented:

- **E30 (acting object chimney):** Rewrite to make acting objects properties of particles rather than standalone entities.
- **E31–E32 (acting object triplet/walls):** Update to reflect new ownership direction.
- **E35 (interaction candidate chimney):** Currently defines interaction candidates in terms of acting objects with paired particles. Would need to reflect the inverted ownership.
- **E39 (closed interaction wall):** The one-sided reaction force check may need to become the two-legged check described above, or E35's definition may need to generate candidates in a way that covers both legs.

## Interaction with Other Issues

This bug is related to but distinct from the double-counting / for-loop efficiency concern discussed in the same session. Both issues stem from the same root: the closure algorithm's iteration strategy. The ownership fix affects *what* gets iterated over; the double-counting fix affects *how* the iteration avoids redundancy. Both should be resolved together when the closure triplet is finalised.
