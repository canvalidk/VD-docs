# Hand trace

**Question.** What is A's inertial acceleration at t0?

**Edition.** dictionary: Design 2.1 Draft 1 + scratch P1-P3; source: contribution_law_and_force_sum_decisions_2026-11-11.md

**Entry quotes verified against** 30 supplied entries.

## Steps

| Step | Frame | Label | Ref / kind | Content | Uses | Check |
|---|---|---|---|---|---|---|
| [1] | ROOT | INPUT | normalization | the question asks for inertial-acceleration-material-object(A, t0, R) ⇒ q_norm |  |  |
| [2] | ROOT | INPUT | model | R is a supplied inertial frame ⇒ R_inertial |  |  |
| [3] | ROOT | INPUT | convention | upward positive along the single axis ⇒ axis |  |  |
| [4] | ROOT | INPUT | haze | haze-material-object(A, t0) = 0 at a tolerance the haze wall would state (that wall is not written) ⇒ H = 0 N |  |  |
| [5] | ROOT | DEMAND |  | opens D1: inertial-acceleration-material-object(A, t0, R) |  |  |
| [6] | D1 | DELIVER | [1] | q_norm, delivered from ROOT (bound at [1]) with its qualifications: the question asks for inertial-acceleration-material-object(A, t0, R) | q_norm |  |
| [7] | D1 | DELIVER | [2] | R_inertial, delivered from ROOT (bound at [2]) with its qualifications: R is a supplied inertial frame | R_inertial |  |
| [8] | D1 | DELIVER | [4] | H = 0 N, delivered from ROOT (bound at [4]) with its qualifications: haze-material-object(A, t0) = 0 at a tolerance the haze wall would state (that wall is not written) | H |  |
| [9] | D1 | ENTRY | E8 | “For one material-object, its net-force-material-object divided by its inertial-mass-material-object.” — unknown a_A at inertial-acceleration(A, t0, R): the demanded inertial acceleration ⇒ a_A | q_norm |  |
| [10] | D1 | DEMAND | E8 | opens D1.1: E8: demand net-force-material-object(A, t0, R) |  |  |
| [11] | D1 | DEMAND | E8 | opens D1.2: E8: demand inertial-mass-material-object(A) |  |  |
| [12] | D1.2 | INPUT | value | inertial mass of A, supplied independently ⇒ m_A = 2 kg |  |  |
| [13] | D1.1 | ENTRY | E8 | “For one material-object, its net-force-material-object divided by its inertial-mass-material-object.” — unknown F_A at net-force(A, t0, R): net force on A ⇒ F_A |  |  |
| [14] | D1.1 | ENTRY | P1 | “its haze-material-object plus its contribution-material-object” — unknown C_0 at contribution(A \| {i_s, i_g}, t0, R): contribution of A's whole interaction-set ⇒ C_0 |  |  |
| [15] | D1.1 | ENTRY | P1 | `F_A = H + C_0` — “its haze-material-object plus its contribution-material-object” — the contribution law, net-force corner ⇒ p1 | H, F_A, C_0 |  |
| [16] | D1.1 | INPUT | recognition | spring s is attached to A, intact and Hookean: i_s acts on A ⇒ rec_s |  |  |
| [17] | D1.1 | INPUT | recognition | A is near the Earth's surface: i_g acts on A ⇒ rec_g |  |  |
| [18] | D1.1 | INPUT | completeness | no more elements to be added to interaction-set(A, t0) at this tolerance; everything else is left to haze (row 5.1's physical claim; the recorder's only kind for it is named 'completeness', which row 5.3 retires) ⇒ closed | rec_s, rec_g, H |  |
| [19] | D1.1 | READING |  | interaction-set(A, t0) = {i_s, i_g} ⇒ IS | rec_s, rec_g, closed |  |
| [20] | D1.1 | DEMAND | P1 | opens C1: contribution(A \| {i_s, i_g}) |  |  |
| [21] | C1 | DELIVER | [14] | C_0, delivered from D1.1 (bound at [14]) with its qualifications: contribution of A's whole interaction-set | C_0 |  |
| [22] | C1 | DELIVER | [19] | IS, delivered from D1.1 (bound at [19]) with its qualifications: interaction-set(A, t0) = {i_s, i_g} | IS |  |
| [23] | C1 | READING |  | case split: the remaining set is not empty, so P2 applies ⇒ split1 | IS |  |
| [24] | C1 | INPUT | choice | take i_s as the member at this step ⇒ pick1 |  |  |
| [25] | C1 | ENTRY | P2 | “the impressed-force of one member” — unknown f_s at impressed-force(i_s -> A, t0, R): impressed force of spring interaction i_s (spring s above A) on A ⇒ f_s | pick1 |  |
| [26] | C1 | ENTRY | P2 | “the contribution-material-object of the same set without that member” — unknown C_1 at contribution(A \| {i_g}, t0, R): contribution of the remaining set ⇒ C_1 | pick1 |  |
| [27] | C1 | READING |  | the remaining set without i_s is {i_g} ⇒ rest1 | IS, pick1 |  |
| [28] | C1 | ENTRY | P2 | `C_0 = f_s + C_1` — “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step ⇒ p2_1 | split1, pick1, rest1, C_0, f_s, C_1 |  |
| [29] | D1.1 | DERIVE | partial line, n = 1 | `F_A = H + f_s + C_1` — true before any member is evaluated | F_A, H, f_s, C_1, p1, p2_1 | checked: follows from p1, p2_1 |
| [30] | C1 | DEMAND | P2 | opens C1.S: impressed-force(i_s -> A, t0, R) |  |  |
| [31] | C1.S | DELIVER | [25] | f_s, delivered from C1 (bound at [25]) with its qualifications: impressed force of spring interaction i_s (spring s above A) on A | f_s |  |
| [32] | C1.S | INPUT | value | stiffness of s ⇒ k = 20 N/m |  |  |
| [33] | C1.S | INPUT | value | extension of s (stretched, so it pulls A up) ⇒ e = 1/2 m |  |  |
| [34] | C1.S | CONTRACT | C-spring (proposed connection, as in handtrace_example_spring_single) | `f_s = k*e` — spring dispatch: f(i_s -> A) = +k e (upward positive) ⇒ r_s | k, e, f_s |  |
| [35] | C1.S | DERIVE | spring value | `f_s = 10` ⇒ f_s = 10 N | f_s, r_s | checked: follows from r_s |
| [36] | C1 | DEMAND | P2 | opens C2: contribution(A \| {i_g}) |  |  |
| [37] | C2 | DELIVER | [26] | C_1, delivered from C1 (bound at [26]) with its qualifications: contribution of the remaining set | C_1 |  |
| [38] | C2 | READING |  | case split: the remaining set is not empty, so P2 applies ⇒ split2 | IS |  |
| [39] | C2 | INPUT | choice | take i_g as the member at this step ⇒ pick2 |  |  |
| [40] | C2 | ENTRY | P2 | “the impressed-force of one member” — unknown f_g at impressed-force(i_g -> A, t0, R): impressed force of gravity interaction i_g (Earth on A) on A ⇒ f_g | pick2 |  |
| [41] | C2 | ENTRY | P2 | “the contribution-material-object of the same set without that member” — unknown C_2 at contribution(A \| {}, t0, R): contribution of the remaining set ⇒ C_2 | pick2 |  |
| [42] | C2 | READING |  | the remaining set without i_g is {} ⇒ rest2 | IS, pick2 |  |
| [43] | C2 | ENTRY | P2 | `C_1 = f_g + C_2` — “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step ⇒ p2_2 | split2, pick2, rest2, C_1, f_g, C_2 |  |
| [44] | D1.1 | DERIVE | partial line, n = 2 | `F_A = H + f_s + f_g + C_2` — true before any member is evaluated | F_A, H, f_s, f_g, C_2, p1, p2_1, p2_2 | checked: follows from p1, p2_1, p2_2 |
| [45] | C2 | DEMAND | P2 | opens C2.G: impressed-force(i_g -> A, t0, R) |  |  |
| [46] | C2.G | DELIVER | [40] | f_g, delivered from C2 (bound at [40]) with its qualifications: impressed force of gravity interaction i_g (Earth on A) on A | f_g |  |
| [47] | C2.G | INPUT | value | local gravitational field strength ⇒ g = 49/5 m/s^2 |  |  |
| [48] | C2.G | INPUT | value | gravitational mass of A (its equality with the inertial mass is not used anywhere in this trace) ⇒ m_grav = 2 kg |  |  |
| [49] | C2.G | CONTRACT | C-gravity (proposed connection) | `f_g = -m_grav*g` — gravity dispatch: f(i_g -> A) = -m_grav g (upward positive) ⇒ r_g | g, m_grav, f_g |  |
| [50] | C2.G | DERIVE | gravity value | `f_g = -98/5` ⇒ f_g = -98/5 N | f_g, r_g | checked: follows from r_g |
| [51] | C2 | DEMAND | P2 | opens C3: contribution(A \| {}) |  |  |
| [52] | C3 | DELIVER | [41] | C_2, delivered from C2 (bound at [41]) with its qualifications: contribution of the remaining set | C_2 |  |
| [53] | C3 | READING |  | case split: the remaining set is empty, so P3 applies ⇒ split3 | IS |  |
| [54] | C3 | ENTRY | P3 | `C_2 = 0` — “For one material-object and an empty remaining interaction-set, the zero vector.” — base case ⇒ p3 | split3, C_2 |  |
| [55] | C3 | DERIVE | base case | `C_2 = 0` ⇒ C_2 = 0 N | C_2, p3 | checked: follows from p3 |
| [56] | C2 | DERIVE | return | `C_1 = -98/5` ⇒ C_1 = -98/5 N | C_1, p2_2 | checked: follows from p2_2 |
| [57] | C1 | DERIVE | return | `C_0 = -48/5` ⇒ C_0 = -48/5 N | C_0, p2_1 | checked: follows from p2_1 |
| [58] | D1.1 | DERIVE | contribution law | `F_A = -48/5` ⇒ F_A = -48/5 N | F_A, p1 | checked: follows from p1 |
| [59] | D1 | ENTRY | E8 | `a_A = F_A / m_A` — “For one material-object, its net-force-material-object divided by its inertial-mass-material-object.” — return through E8 ⇒ e8 | R_inertial, a_A, F_A, m_A |  |
| [60] | D1 | DERIVE |  | `a_A = -24/5` ⇒ a_A = -24/5 m/s^2 | a_A, e8 | checked: follows from e8 |
| [61] | ROOT | ANSWER | p1 | A's inertial acceleration, upward positive | a_A | a_A = -24/5 m/s^2 |

## Ledger for answer p1

**Answer:** a_A = -24/5 m/s^2

### World commitments that feed the answer (members)

| Step | Name | Kind | Status | Countermodel | Content |
|---|---|---|---|---|---|
| [2] | R_inertial | model |  |  | R is a supplied inertial frame |
| [4] | H | haze |  |  | H = 0 N (haze-material-object(A, t0) = 0 at a tolerance the haze wall would state (that wall is not written)) |
| [12] | m_A | value |  |  | m_A = 2 kg (inertial mass of A, supplied independently) |
| [16] | rec_s | recognition |  |  | spring s is attached to A, intact and Hookean: i_s acts on A |
| [17] | rec_g | recognition |  |  | A is near the Earth's surface: i_g acts on A |
| [18] | closed | completeness |  |  | no more elements to be added to interaction-set(A, t0) at this tolerance; everything else is left to haze (row 5.1's physical claim; the recorder's only kind for it is named 'completeness', which row 5.3 retires) |
| [32] | k | value |  |  | k = 20 N/m (stiffness of s) |
| [33] | e | value |  |  | e = 1/2 m (extension of s (stretched, so it pulls A up)) |
| [47] | g | value |  |  | g = 49/5 m/s^2 (local gravitational field strength) |
| [48] | m_grav | value |  |  | m_grav = 2 kg (gravitational mass of A (its equality with the inertial mass is not used anywhere in this trace)) |

### Pruned premises (feed the answer, not members)

- [1] q_norm: the question asks for inertial-acceleration-material-object(A, t0, R) (kind normalization is not a claim about the world)
- [24] pick1: take i_s as the member at this step (kind choice is not a claim about the world)
- [39] pick2: take i_g as the member at this step (kind choice is not a claim about the world)

### Theory side that feeds the answer

- [9] ENTRY E8: “For one material-object, its net-force-material-object divided by its inertial-mass-material-object.” — unknown a_A at inertial-acceleration(A, t0, R): the demanded inertial acceleration
- [13] ENTRY E8: “For one material-object, its net-force-material-object divided by its inertial-mass-material-object.” — unknown F_A at net-force(A, t0, R): net force on A
- [14] ENTRY P1: “its haze-material-object plus its contribution-material-object” — unknown C_0 at contribution(A \| {i_s, i_g}, t0, R): contribution of A's whole interaction-set
- [15] ENTRY P1: “its haze-material-object plus its contribution-material-object” — the contribution law, net-force corner
- [19] READING : interaction-set(A, t0) = {i_s, i_g}
- [23] READING : case split: the remaining set is not empty, so P2 applies
- [25] ENTRY P2: “the impressed-force of one member” — unknown f_s at impressed-force(i_s -> A, t0, R): impressed force of spring interaction i_s (spring s above A) on A
- [26] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_1 at contribution(A \| {i_g}, t0, R): contribution of the remaining set
- [27] READING : the remaining set without i_s is {i_g}
- [28] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [34] CONTRACT C-spring (proposed connection, as in handtrace_example_spring_single): spring dispatch: f(i_s -> A) = +k e (upward positive)
- [38] READING : case split: the remaining set is not empty, so P2 applies
- [40] ENTRY P2: “the impressed-force of one member” — unknown f_g at impressed-force(i_g -> A, t0, R): impressed force of gravity interaction i_g (Earth on A) on A
- [41] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_2 at contribution(A \| {}, t0, R): contribution of the remaining set
- [42] READING : the remaining set without i_g is {}
- [43] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [49] CONTRACT C-gravity (proposed connection): gravity dispatch: f(i_g -> A) = -m_grav g (upward positive)
- [53] READING : case split: the remaining set is empty, so P3 applies
- [54] ENTRY P3: “For one material-object and an empty remaining interaction-set, the zero vector.” — base case
- [59] ENTRY E8: “For one material-object, its net-force-material-object divided by its inertial-mass-material-object.” — return through E8

### Step members (metalinguistic)

- [35] spring value: f_s = 10 (checked)
- [50] gravity value: f_g = -98/5 (checked)
- [55] base case: C_2 = 0 (checked)
- [56] return: C_1 = -98/5 (checked)
- [57] return: C_0 = -48/5 (checked)
- [58] contribution law: F_A = -48/5 (checked)
- [60] DERIVE: a_A = -24/5 (checked)

### Inputs that do not feed the answer

- [3] axis (convention): upward positive along the single axis

### Other steps that do not feed the answer

- [29] DERIVE partial line, n = 1: F_A = H + f_s + C_1
- [44] DERIVE partial line, n = 2: F_A = H + f_s + f_g + C_2

### Open items

- none

### Found mistakes

- none

### Conflicts

- none

### Unchecked steps

- none

### Solves that were not unique

- none

### Withdrawn premises

- none

### Undetermined unknowns

- none

### Warnings

- 10 commitment(s) have no status yet: R_inertial, H, m_A, rec_s, rec_g, closed, k, e, g, m_grav

### Hypothesis set for p1 (prediction side only)

- **p** the prediction holds: a_A = -24/5 m/s^2
- **A1** not (R is a supplied inertial frame)
- **A2** not (H = 0 N (haze-material-object(A, t0) = 0 at a tolerance the haze wall would state (that wall is not written)))
- **A3** not (m_A = 2 kg (inertial mass of A, supplied independently))
- **A4** not (spring s is attached to A, intact and Hookean: i_s acts on A)
- **A5** not (A is near the Earth's surface: i_g acts on A)
- **A6** not (no more elements to be added to interaction-set(A, t0) at this tolerance; everything else is left to haze (row 5.1's physical claim; the recorder's only kind for it is named 'completeness', which row 5.3 retires))
- **A7** not (k = 20 N/m (stiffness of s))
- **A8** not (e = 1/2 m (extension of s (stretched, so it pulls A up)))
- **A9** not (g = 49/5 m/s^2 (local gravitational field strength))
- **A10** not (m_grav = 2 kg (gravitational mass of A (its equality with the inertial mass is not used anywhere in this trace)))
- **M1** step [35] went wrong: f_s = 10
- **M2** step [50] went wrong: f_g = -98/5
- **M3** step [55] went wrong: C_2 = 0
- **M4** step [56] went wrong: C_1 = -98/5
- **M5** step [57] went wrong: C_0 = -48/5
- **M6** step [58] went wrong: F_A = -48/5
- **M7** step [60] went wrong: a_A = -24/5

Checks cover exact arithmetic and bookkeeping only. A countermodel marked [check: ...] was re-solved from the recorded premises; physics, recognition, meaning and unmarked countermodels are not checked, and the observation side of a trial is not modelled.
