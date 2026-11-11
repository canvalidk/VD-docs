# The Atwood Prediction's Hypothesis Set, Written by Hand

## A fixed comparison point, written before any set is read off a trace

**Status:** record. Claude-authored on 7 November 2026, at Can's request ("Yes,
write it"), in a Claude Code session on Can's computer. It is the first step of
the test proposed in `hypothesis_sets_from_traces_2026-11-05.md` §7. The test
writes the set a physicist would write by hand first, reads the set off a trace
second, and compares the two row by row.

**Fix it before use.** This file is meant to stay unchanged. Its SHA-256 is
given in the session that wrote it. A later edit makes a new file with a new
date, not a revision of this one.

**Vocabulary.** The body uses no VD vocabulary on purpose: no entries, walls,
residues or substitutions. It uses only the hypothesis-set paper's terms (d4
§§3–5) and ordinary mechanics.

**How blind it is.** It is blind to the trace's text, not to summaries of the
trace.

- **Not opened:** `Theory/vd_trace_level2_v3.md` was not opened in the session
  that wrote this.
- **Read beforehand:** three records that describe the trace.
  - `hypothesis_sets_from_traces_2026-11-05.md` §3 gives the trace's input
    categories. It also says the trace leaves out a frictionless pulley and
    the pulley's inertia, and that the mass values appear only in its demand
    tree.
  - `nobody_made_a_mistake_meaningful_substitutions.md` §7 lists its recorded
    arithmetic.
  - The same two records give the problem's numbers.
- **What that may have influenced:** probably the presence of pulley inertia
  and friction below, which any textbook treatment would include anyway. It
  probably did not influence the absence of Earth's recoil, which this set
  deliberately does not list (§5).

All numbers below are order-of-magnitude estimates done by hand, not checked by
anyone else.

---

## 1. The trial

**Problem, as taken from those summaries.**

- Two blocks, $m_1 = 3$ kg and $m_2 = 5$ kg, hang from a string that runs over
  a pulley fixed to a support.
- $g = 9.8\ \text{m/s}^2$.
- The heavier block descends.

**T.** Newton's three laws of motion and Newtonian gravitation, applied near
the Earth's surface as a uniform field. §6 says what changes if T is cut
differently.

**p.** The magnitude of each block's acceleration is

$$a = \frac{(m_2 - m_1)\,g}{m_1 + m_2} = \frac{2 \times 9.8}{8} = 2.45\ \text{m/s}^2 .$$

The tension prediction, 36.75 N, is a separate trial with its own set. It is
not written here.

**ε, declared.** p is held if the measured acceleration lies within 1.5% of
2.45 m/s², that is ±0.037 m/s². The 1.5% is split before any test:

| Share | Allotted to |
|---|---|
| 1.0% | the commitments of the derivation (§3) |
| 0.5% | the commitments of the measurement (§4) |

The split of the 1.0% among members is shown in the table's "Limit" column.
The shares add to the total because, to first order, the effects add. If each
member were tested against the whole 1.0%, the members could all be rejected
while p still failed, and T would be convicted for nothing. The split is a
choice. It is part of this record and must be kept fixed in the comparison.

**Measurement, declared.**

- Block 2 is held at rest by an electromagnet.
- Switching the magnet off starts a timer.
- A photogate $d = 1.000$ m below stops the timer.
- The measured acceleration is $a_{\text{obs}} = 2d/t^2$.
- The expected time is $t \approx 0.904$ s, and the speed at the gate is about
  2.21 m/s.

---

## 2. The derivation

| Step | Content | Uses |
|---|---|---|
| S1 | The string pulls both blocks with the same tension $F_T$ | ¬A6, ¬A7, ¬A8 rejected |
| S2 | Newton II on block 1, upward positive: $F_T - m_1 g = m_1 a$ | T; ¬A1, ¬A3, ¬A10, ¬A11 rejected |
| S3 | Newton II on block 2, downward positive, with the same $a$: $m_2 g - F_T = m_2 a$ | T; ¬A1, ¬A4, ¬A9, ¬A10, ¬A11 rejected |
| S4 | Add: $(m_2 - m_1)\,g = (m_1 + m_2)\,a$ | — |
| S5 | Solve: $a = (m_2 - m_1)\,g/(m_1 + m_2)$ | — |
| S6 | Evaluate: $2 \times 9.8 / 8 = 2.45$ | ¬A1, ¬A3, ¬A4 rejected |

Equal tension is a step here (S1), derived from three commitments. It is not
a commitment in its own right. Equal and opposite accelerations are the
content of ¬A9, used at S3.

---

## 3. The set: commitments of the derivation

Shares are of the 1.0% allotted to the derivation. They add to 1.0%.

| Member | Limit (share) | Kind of test | Held | Rejected |
|---|---|---|---|---|
| **p**: measured $a$ within 1.5% of 2.45 m/s² | ε | the measurement of §1 | within | outside |
| **¬A1** The local $g$ differs from 9.8 m/s² | ±0.015 m/s² (0.15%) | gravimetric survey value, or a pendulum on site | differs by more | agrees |
| **¬A2** The lab frame, with the support, is not inertial in the vertical: building sway, a moving floor, an elevator | ±1.2 mm/s² (0.05%) | accelerometer on the support during the run | above limit | below |
| **¬A3** $m_1$ is not 3 kg | ±2 g (0.125%) | calibrated balance | off by more | within |
| **¬A4** $m_2$ is not 5 kg | ±2 g (0.075%) | calibrated balance | off by more | within |
| **¬A5** The blocks run are not the blocks weighed, or a block's mass changes during the run | any | labels; reweigh after the run | mismatch or change | same blocks, same mass |
| **¬A6** The pulley's rotational inertia matters | $I/r^2 \le 12$ g (0.15%) | weigh the pulley and measure its radius; or a spin-down test | above limit | below |
| **¬A7** Friction at the pulley, at the axle or from the string sliding on it | rim force ≤ 20 mN, a 2 g hanging-mass equivalent (0.1%) | with equal masses on both sides, find the smallest added mass that starts motion | above limit | below |
| **¬A8** The string's mass matters, through its inertia or through the imbalance of string on the two sides | $m_s/(8\ \text{kg}) + \mu\lvert\Delta\rvert_{\max}/(2\ \text{kg}) \le 0.1\%$ | weigh the string; measure the side lengths over the run | above limit | below |
| **¬A9** The string's length changes during the timed drop: the stretch transient at release, slack, or a slipping knot | block-2 displacement error ≤ 1 mm (0.1%) | high-speed video of the knot and the release; string stiffness | above limit | below |
| **¬A10** A force other than gravity and string tension acts on a block (the existential member) | 0.1%, all versions together | see the versions below | a version found above limit | every version searched rejected, to the limit |
| **¬A11** The motion is not vertical: a block swings, or a string segment leans because of the pulley's offset | string angle ≤ 1.1°, the worst case, which is a lean on block 2's side (0.05%) | video; plumb line | above limit | below |
| **¬A13** A step S1–S6 was done wrongly (a family: one member per step) | — | independent recomputation | slip found | agrees |

¬A12 is cut-dependent and is listed in §6.

**Versions of ¬A10 and their tests:**

- **Air drag.** Compute the drag, and vary $d$. For compact iron blocks the
  drag at the gate is about 0.2% of the driving force. Its effect on $2d/t^2$
  over a 1 m drop is about 0.03%, because the effect builds up over the drop.
- **Buoyancy.** Compute it. It is about 0.015% here.
- **Contact with a guide or the wall.** Inspect, and rerun without guides.
- **Magnetic or electrostatic forces.** Inspect; residual magnetism from the
  release magnet is the likely case.
- **Air currents.** Shield the apparatus.

¬A10 closes only to a limit, as d4 §4 says. What can be rejected is "no
unaccounted force above 0.1% of the driving force, among the versions
searched".

**Some needed limits are not small.**

- **¬A1:** 9.8 m/s² holds in London ($g \approx 9.812$, off by 0.12%) and fails
  at the equator ($g \approx 9.780$, off by 0.20%). So at this ε the given $g$
  is a live member.
- **¬A6:** a uniform-disc pulley heavier than about 24 g fails it.
- **¬A9:** if block 2 is released while block 1 is hanging, the tension jumps
  from about 29.4 N to 36.75 N. A string of stiffness $k_s$ then carries a
  stretch oscillation of amplitude about $7.35\ \text{N}/k_s$, and block 2
  carries $m_1/(m_1+m_2) = 3/8$ of it. Staying under 1 mm needs $k_s$ above
  about $3 \times 10^3$ N/m, or a timing window that starts after the
  oscillation has damped. A long nylon line can fall below that stiffness.
  This is rough and unchecked, but it is the largest surprise in the set.

---

## 4. The set: commitments of the measurement

Shares are of the 0.5% allotted to the measurement. They add to 0.5%.

| Member | Limit (share) | Kind of test | Held | Rejected |
|---|---|---|---|---|
| **¬B1** The drop distance $d$ is wrong | ±1.5 mm (0.15%) | calibrated rule between the release point and the gate beam | off by more | within |
| **¬B2** The time $t$ is wrong: clock calibration, gate latency, magnet release delay | ±0.9 ms (0.2%) | clock against a reference; latency test with a pendulum | off by more | within |
| **¬B3** Block 2 is not at rest when the timer starts | $v_0 \le 1.7$ mm/s (0.15%) | video at release | moving | at rest |
| **¬B4** The gate times something other than block 2's leading edge crossing $d$: the string, a swing, a reflection | — | inspection; a repeat with a flag on the block | wrong trigger | right trigger |
| **¬B5** $2d/t^2$ was computed wrongly | — | recomputation | slip found | agrees |

---

## 5. What is not a member, and why

These are inside a listed member's limit, or idle at this ε. They are versions
of a member, not members of their own.

- **The Earth's recoil toward the blocks.** It is of order $10^{-23}$ m/s². It
  is inside ¬A2.
- **The Coriolis force.** For vertical motion it acts horizontally, and it is
  of order $3 \times 10^{-4}$ m/s². It is inside ¬A2 and ¬A11.
- **Field non-uniformity over 1 m.** It is of order $3 \times 10^{-7}$ of $g$,
  inside ¬A1.
- **The blocks' gravitation on each other.** It is of order $10^{-8}$ N, inside
  ¬A10.
- **Relativistic corrections.** With $v/c$ of order $10^{-8}$, they are idle.
  In any case they belong to a rival's content, not to this set.
- **Equal tension.** It is a step, S1, not a commitment.
- **Equal and opposite accelerations.** They are ¬A9's content, not a separate
  member.

**Each listed member is needed** (the test of d4 §4). Drop any one and a world
is easy to build in which T and every other commitment hold, but p fails by
more than its share:

| Dropped | A world where p then fails |
|---|---|
| ¬A1 | run it at the equator |
| ¬A2 | run it in an accelerating lift |
| ¬A3, ¬A4 | 30 g of error in one block |
| ¬A5 | swap in the wrong block |
| ¬A6 | use a 200 g brass pulley |
| ¬A7 | use a rusted axle |
| ¬A8 | use a chain |
| ¬A9 | use a rubber cord |
| ¬A10 | add a guide rail with friction |
| ¬A11 | let the blocks swing at 10° |
| ¬B1–¬B4 | the obvious errors |

That shows each member is needed. It does not show that nothing else is.

---

## 6. Where T is cut, and what moves

- **If T is the laws of motion only,** the weights become inputs. ¬A1 then
  reads "the weights are $m_i g$ with $g = 9.8$", with the same test. A new
  member appears:
  - **¬A12** The mass in the weight differs from the mass in $m a$.
    Test: Eötvös-type comparison, far below ε. Under the T of §1, with
    Newtonian gravitation, this identity is part of T and ¬A12 is not a
    member.
- **If T includes universal gravitation with the Earth's mass and radius as
  inputs,** ¬A1 becomes "the Earth's GM, its radius, its rotation and the
  local anomaly are as used". The test is still a local measurement of $g$.
- **The force-completeness member** and its versions do not depend on the
  cut.

---

## 7. How to use this in the comparison

1. **Compare members by their tests,** as d4 §4 counts members. Groupings may
   differ: one trace member may be two of these, or the reverse.
   Strong-Kleene regrouping does not change verdicts.
2. **Expect step members to differ.** d4 §4 says different routes to the same
   p have different sets. The trace's arithmetic route is not S1–S6, so
   compare step members by count and by kind, not one by one.
3. **Expect the world members and the measurement members to correspond.**
   Same p, same ε, same physics. Any mismatch there is a finding.
4. **For each trace member, record one of:**
   - matches a member here;
   - a member this hand set missed;
   - used by the trace but not needed (§5 says why some are not members).
5. **For each member here, record:**
   - present in the trace;
   - absent from the trace;
   - absent from the trace and outside what a trace can contain. The whole of
     §4 may be in this category.
6. **Keep ε, its split and T fixed.** If a comparison needs a different ε or
   a different cut, redo this set first, as a new dated file.

---

## Provenance

- **Stated (Can's):** the request; the comparison design, quoted from
  `hypothesis_sets_from_traces_2026-11-05.md` §7, which is a Claude-authored
  record of a conversation with Can.
- **Analysis (Claude's):** everything in §§1–7, including:
  - the declared ε, its split and the measurement method, all chosen here;
  - all effect sizes, which are hand estimates and unchecked.
- **Sources consulted for form:** d4 §§3–5 (`Theory/_note_hypothesis_set_paper/hypothesis_set_paper_d4.md`).
- **Placement:** `inbox/` for sorting. Its natural home is beside
  `hypothesis_sets_from_traces` in `Theory/`, as the fixed input to that
  record's §7 test.
