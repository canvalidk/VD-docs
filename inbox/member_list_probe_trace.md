# Hand trace

**Question.** What are the inertial accelerations of A and B at t0?

**Edition.** dictionary: Design 2.1 Draft 1 + scratch P1-P8 (probe wording, not entries); member names: after the 15 August 2026 addendum: action-force_kind / reaction-force_kind

**Entry quotes verified against** 35 supplied entries.

## Steps

| Step | Frame | Label | Ref / kind | Content | Uses | Check |
|---|---|---|---|---|---|---|
| [1] | ROOT | INPUT | normalization | the question asks for inertial-acceleration-material-object of A and of B at t0 in R ⇒ q_norm |  |  |
| [2] | ROOT | INPUT | model | R is a supplied inertial frame ⇒ R_inertial |  |  |
| [3] | ROOT | INPUT | convention | one vertical axis, upward positive ⇒ axis |  |  |
| [4] | ROOT | INPUT | value | local field-strength, the same at A and at B ⇒ g = 49/5 m/s^2 |  |  |
| [5] | ROOT | INPUT | haze | haze-material-object(A, t0) = 0 ⇒ H_A = 0 N |  |  |
| [6] | ROOT | INPUT | haze | haze-material-object(B, t0) = 0 ⇒ H_B = 0 N |  |  |
| [7] | ROOT | INPUT | recognition | spring s1 is carried by the ceiling and attached to A; intact, Hookean ⇒ rec_s1 |  |  |
| [8] | ROOT | INPUT | recognition | spring s2 is carried by A and attached to B; intact, Hookean ⇒ rec_s2 |  |  |
| [9] | ROOT | INPUT | recognition | A is in the Earth's near-surface field ⇒ rec_gA |  |  |
| [10] | ROOT | INPUT | recognition | B is in the Earth's near-surface field ⇒ rec_gB |  |  |
| [11] | ROOT | INPUT | completeness | no more members to be added to A's list at this tolerance ⇒ closed_A | rec_s1, rec_s2, rec_gA, H_A |  |
| [12] | ROOT | INPUT | completeness | no more members to be added to B's list at this tolerance ⇒ closed_B | rec_s2, rec_gB, H_B |  |
| [13] | ROOT | READING |  | interaction-set(A, t0) = (A_s1, R_s2, A_gA): an instance gives its action to its other participant and its reaction to its carrier ⇒ IS_A | rec_s1, rec_s2, rec_gA, closed_A |  |
| [14] | ROOT | READING |  | interaction-set(B, t0) = (A_s2, A_gB) ⇒ IS_B | rec_s2, rec_gB, closed_B |  |
| [15] | ROOT | ENTRY | P7 | “the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis” — unknown K_s1 at action-force(s1, t0, R): action-force of s1 (lands on A) ⇒ K_s1 | rec_s1 |  |
| [16] | ROOT | ENTRY | P7 | “the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis” — unknown K_s2 at action-force(s2, t0, R): action-force of s2 (lands on B) ⇒ K_s2 | rec_s2 |  |
| [17] | ROOT | ENTRY | P8 | “the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis” — unknown K_gA at action-force(gA, t0, R): action-force of gA (lands on A) ⇒ K_gA | rec_gA |  |
| [18] | ROOT | ENTRY | P8 | “the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis” — unknown K_gB at action-force(gB, t0, R): action-force of gB (lands on B) ⇒ K_gB | rec_gB |  |
| [19] | ROOT | ENTRY | E8 | “its net-force-material-object divided by its inertial-mass-material-object.” — unknown a_A at inertial-acceleration(A, t0, R): the demanded inertial acceleration of A ⇒ a_A | q_norm |  |
| [20] | ROOT | ENTRY | E8 | “its net-force-material-object divided by its inertial-mass-material-object.” — unknown F_A at net-force(A, t0, R): net force on A ⇒ F_A |  |  |
| [21] | ROOT | ENTRY | E8 | “its net-force-material-object divided by its inertial-mass-material-object.” — unknown a_B at inertial-acceleration(B, t0, R): the demanded inertial acceleration of B ⇒ a_B | q_norm |  |
| [22] | ROOT | ENTRY | E8 | “its net-force-material-object divided by its inertial-mass-material-object.” — unknown F_B at net-force(B, t0, R): net force on B ⇒ F_B |  |  |
| [23] | ROOT | DEMAND |  | opens DA: inertial-acceleration-material-object(A, t0, R) |  |  |
| [24] | DA | DELIVER | [1] | q_norm, delivered from ROOT (bound at [1]) with its qualifications: the question asks for inertial-acceleration-material-object of A and of B at t0 in R | q_norm |  |
| [25] | DA | DELIVER | [2] | R_inertial, delivered from ROOT (bound at [2]) with its qualifications: R is a supplied inertial frame | R_inertial |  |
| [26] | DA | DELIVER | [5] | H_A = 0 N, delivered from ROOT (bound at [5]) with its qualifications: haze-material-object(A, t0) = 0 | H_A |  |
| [27] | DA | DELIVER | [19] | a_A, delivered from ROOT (bound at [19]) with its qualifications: the demanded inertial acceleration of A | a_A |  |
| [28] | DA | DEMAND | E8 | opens DA.F: E8: demand net-force-material-object(A, t0, R) |  |  |
| [29] | DA | DEMAND | E8 | opens DA.m: E8: demand inertial-mass-material-object(A) |  |  |
| [30] | DA.m | INPUT | value | inertial mass of A, supplied independently ⇒ m_A = 2 kg |  |  |
| [31] | DA | DELIVER | [20] | F_A, delivered from ROOT (bound at [20]) with its qualifications: net force on A | F_A |  |
| [32] | DA | DELIVER | [13] | IS_A, delivered from ROOT (bound at [13]) with its qualifications: interaction-set(A, t0) = (A_s1, R_s2, A_gA): an instance gives its action to its other participant and its reaction to its carrier | IS_A |  |
| [33] | DA.F | ENTRY | P1 | “its haze-material-object plus its contribution-material-object” — unknown C_A0 at contribution(A \| (A_s1, R_s2, A_gA)): contribution of A's whole list ⇒ C_A0 |  |  |
| [34] | DA.F | ENTRY | P1 | `F_A = H_A + C_A0` — “its haze-material-object plus its contribution-material-object” — the contribution law, net-force corner ⇒ p1_A | H_A, F_A, C_A0 |  |
| [35] | DA.F | DEMAND | P1 | opens CA1: contribution(A \| (A_s1, R_s2, A_gA)) |  |  |
| [36] | CA1 | DELIVER | [33] | C_A0, delivered from DA.F (bound at [33]) with its qualifications: contribution of A's whole list | C_A0 |  |
| [37] | CA1 | READING |  | case split: the remaining list is not empty, so P2 applies ⇒ split_A1 | IS_A |  |
| [38] | CA1 | INPUT | choice | take A_s1 as the member at this step ⇒ pick_A1 |  |  |
| [39] | CA1 | ENTRY | P2 | “the impressed-force of one member” — unknown f_A_A_s1 at impressed-force(A_s1 -> A, t0, R): impressed force of A_s1 on A ⇒ f_A_A_s1 | pick_A1 |  |
| [40] | CA1 | ENTRY | P2 | “the contribution-material-object of the same set without that member” — unknown C_A1 at contribution(A \| (R_s2, A_gA)): contribution of the remaining list ⇒ C_A1 | pick_A1 |  |
| [41] | CA1 | READING |  | the remaining list without A_s1 is (R_s2, A_gA) ⇒ rest_A1 | IS_A, pick_A1 |  |
| [42] | CA1 | ENTRY | P2 | `C_A0 = f_A_A_s1 + C_A1` — “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step ⇒ p2_A1 | split_A1, pick_A1, rest_A1, C_A0, f_A_A_s1, C_A1 |  |
| [43] | CA1 | DEMAND | P2 | opens CA1.A_s1: impressed-force(A_s1 -> A, t0, R) |  |  |
| [44] | CA1.A_s1 | DELIVER | [39] | f_A_A_s1, delivered from CA1 (bound at [39]) with its qualifications: impressed force of A_s1 on A | f_A_A_s1 |  |
| [45] | CA1.A_s1 | READING |  | dispatch: A_s1 is the action of s1, so P4 applies ⇒ disp_A_A_s1 | IS_A |  |
| [46] | CA1.A_s1 | DEMAND | P4 | opens CA1.A_s1.K: action-force(s1) |  |  |
| [47] | DA | DELIVER | [15] | K_s1, delivered from ROOT (bound at [15]) with its qualifications: action-force of s1 (lands on A) | K_s1 |  |
| [48] | CA1.A_s1.K | INPUT | value | stiffness of s1 ⇒ k1 = 20 N/m |  |  |
| [49] | CA1.A_s1.K | INPUT | value | signed displacement of A from s1's relaxed position (negative: below it) ⇒ x1 = -1 m |  |  |
| [50] | CA1.A_s1.K | ENTRY | P7 | `K_s1 = -k1*x1` — “the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis” — action-force_spring for s1 ⇒ law_s1 | k1, x1, K_s1 |  |
| [51] | CA1.A_s1.K | DERIVE | action value s1 | `K_s1 = 20` ⇒ K_s1 = 20 N | K_s1, law_s1 | checked: follows from law_s1 |
| [52] | CA1.A_s1 | ENTRY | P4 | `f_A_A_s1 = K_s1` — “For a member that is the action of an acting-object, the action-force of that acting-object.” — impressed force of an action member ⇒ p4_A_s1 | disp_A_A_s1, f_A_A_s1, K_s1 |  |
| [53] | CA1.A_s1 | DERIVE | A_s1 on A | `f_A_A_s1 = 20` ⇒ f_A_A_s1 = 20 N | f_A_A_s1, p4_A_s1 | checked: follows from p4_A_s1 |
| [54] | CA1 | DEMAND | P2 | opens CA2: contribution(A \| (R_s2, A_gA)) |  |  |
| [55] | CA2 | DELIVER | [40] | C_A1, delivered from CA1 (bound at [40]) with its qualifications: contribution of the remaining list | C_A1 |  |
| [56] | CA2 | READING |  | case split: the remaining list is not empty, so P2 applies ⇒ split_A2 | IS_A |  |
| [57] | CA2 | INPUT | choice | take R_s2 as the member at this step ⇒ pick_A2 |  |  |
| [58] | CA2 | ENTRY | P2 | “the impressed-force of one member” — unknown f_A_R_s2 at impressed-force(R_s2 -> A, t0, R): impressed force of R_s2 on A ⇒ f_A_R_s2 | pick_A2 |  |
| [59] | CA2 | ENTRY | P2 | “the contribution-material-object of the same set without that member” — unknown C_A2 at contribution(A \| (A_gA)): contribution of the remaining list ⇒ C_A2 | pick_A2 |  |
| [60] | CA2 | READING |  | the remaining list without R_s2 is (A_gA) ⇒ rest_A2 | IS_A, pick_A2 |  |
| [61] | CA2 | ENTRY | P2 | `C_A1 = f_A_R_s2 + C_A2` — “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step ⇒ p2_A2 | split_A2, pick_A2, rest_A2, C_A1, f_A_R_s2, C_A2 |  |
| [62] | CA2 | DEMAND | P2 | opens CA2.R_s2: impressed-force(R_s2 -> A, t0, R) |  |  |
| [63] | CA2.R_s2 | DELIVER | [58] | f_A_R_s2, delivered from CA2 (bound at [58]) with its qualifications: impressed force of R_s2 on A | f_A_R_s2 |  |
| [64] | CA2.R_s2 | READING |  | dispatch: R_s2 is the reaction of s2, so P5 applies ⇒ disp_A_R_s2 | IS_A |  |
| [65] | CA2.R_s2 | ENTRY | P5 | “For a member that is the reaction of an acting-object, the reaction-force of that acting-object.” — unknown Rf_s2 at reaction-force(s2, t0, R): reaction-force of s2 (lands on its carrier, A) ⇒ Rf_s2 | disp_A_R_s2 |  |
| [66] | CA2.R_s2 | DEMAND | P4 | opens CA2.R_s2.K: action-force(s2) |  |  |
| [67] | DA | DELIVER | [16] | K_s2, delivered from ROOT (bound at [16]) with its qualifications: action-force of s2 (lands on B) | K_s2 |  |
| [68] | CA2.R_s2.K | INPUT | value | stiffness of s2 ⇒ k2 = 10 N/m |  |  |
| [69] | CA2.R_s2.K | INPUT | value | signed displacement of B from s2's relaxed position (negative: below it) ⇒ x2 = -1/2 m |  |  |
| [70] | CA2.R_s2.K | ENTRY | P7 | `K_s2 = -k2*x2` — “the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis” — action-force_spring for s2 ⇒ law_s2 | k2, x2, K_s2 |  |
| [71] | CA2.R_s2.K | DERIVE | action value s2 | `K_s2 = 5` ⇒ K_s2 = 5 N | K_s2, law_s2 | checked: follows from law_s2 |
| [72] | CA2.R_s2 | ENTRY | P6 | `Rf_s2 = -K_s2` — “For one acting-object, the negative of its action-force.” — reaction by negation of the action ⇒ p6_s2 | Rf_s2, K_s2 |  |
| [73] | CA2.R_s2 | DERIVE | reaction value s2 | `Rf_s2 = -5` ⇒ Rf_s2 = -5 N | Rf_s2, p6_s2 | checked: follows from p6_s2 |
| [74] | CA2.R_s2 | ENTRY | P5 | `f_A_R_s2 = Rf_s2` — “For a member that is the reaction of an acting-object, the reaction-force of that acting-object.” — impressed force of a reaction member ⇒ p5_A_s2 | disp_A_R_s2, f_A_R_s2, Rf_s2 |  |
| [75] | CA2.R_s2 | DERIVE | R_s2 on A | `f_A_R_s2 = -5` ⇒ f_A_R_s2 = -5 N | f_A_R_s2, p5_A_s2 | checked: follows from p5_A_s2 |
| [76] | CA2 | DEMAND | P2 | opens CA3: contribution(A \| (A_gA)) |  |  |
| [77] | CA3 | DELIVER | [59] | C_A2, delivered from CA2 (bound at [59]) with its qualifications: contribution of the remaining list | C_A2 |  |
| [78] | CA3 | READING |  | case split: the remaining list is not empty, so P2 applies ⇒ split_A3 | IS_A |  |
| [79] | CA3 | INPUT | choice | take A_gA as the member at this step ⇒ pick_A3 |  |  |
| [80] | CA3 | ENTRY | P2 | “the impressed-force of one member” — unknown f_A_A_gA at impressed-force(A_gA -> A, t0, R): impressed force of A_gA on A ⇒ f_A_A_gA | pick_A3 |  |
| [81] | CA3 | ENTRY | P2 | “the contribution-material-object of the same set without that member” — unknown C_A3 at contribution(A \| ()): contribution of the remaining list ⇒ C_A3 | pick_A3 |  |
| [82] | CA3 | READING |  | the remaining list without A_gA is () ⇒ rest_A3 | IS_A, pick_A3 |  |
| [83] | CA3 | ENTRY | P2 | `C_A2 = f_A_A_gA + C_A3` — “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step ⇒ p2_A3 | split_A3, pick_A3, rest_A3, C_A2, f_A_A_gA, C_A3 |  |
| [84] | CA3 | DEMAND | P2 | opens CA3.A_gA: impressed-force(A_gA -> A, t0, R) |  |  |
| [85] | CA3.A_gA | DELIVER | [80] | f_A_A_gA, delivered from CA3 (bound at [80]) with its qualifications: impressed force of A_gA on A | f_A_A_gA |  |
| [86] | CA3.A_gA | READING |  | dispatch: A_gA is the action of gA, so P4 applies ⇒ disp_A_A_gA | IS_A |  |
| [87] | CA3.A_gA | DEMAND | P4 | opens CA3.A_gA.K: action-force(gA) |  |  |
| [88] | DA | DELIVER | [17] | K_gA, delivered from ROOT (bound at [17]) with its qualifications: action-force of gA (lands on A) | K_gA |  |
| [89] | DA | DELIVER | [4] | g = 49/5 m/s^2, delivered from ROOT (bound at [4]) with its qualifications: local field-strength, the same at A and at B | g |  |
| [90] | CA3.A_gA.K | INPUT | value | gravitational mass of A ⇒ mu_A = 2 kg |  |  |
| [91] | CA3.A_gA.K | ENTRY | P8 | `K_gA = -mu_A*g` — “the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis” — action-force_near-surface-gravity for gA ⇒ law_gA | mu_A, g, K_gA |  |
| [92] | CA3.A_gA.K | DERIVE | action value gA | `K_gA = -98/5` ⇒ K_gA = -98/5 N | K_gA, law_gA | checked: follows from law_gA |
| [93] | CA3.A_gA | ENTRY | P4 | `f_A_A_gA = K_gA` — “For a member that is the action of an acting-object, the action-force of that acting-object.” — impressed force of an action member ⇒ p4_A_gA | disp_A_A_gA, f_A_A_gA, K_gA |  |
| [94] | CA3.A_gA | DERIVE | A_gA on A | `f_A_A_gA = -98/5` ⇒ f_A_A_gA = -98/5 N | f_A_A_gA, p4_A_gA | checked: follows from p4_A_gA |
| [95] | CA3 | DEMAND | P2 | opens CA4: contribution(A \| ()) |  |  |
| [96] | CA4 | DELIVER | [81] | C_A3, delivered from CA3 (bound at [81]) with its qualifications: contribution of the remaining list | C_A3 |  |
| [97] | CA4 | READING |  | case split: the remaining list is empty, so P3 applies ⇒ split_A4 | IS_A |  |
| [98] | CA4 | ENTRY | P3 | `C_A3 = 0` — “For one material-object and an empty remaining interaction-set, the zero vector.” — base case ⇒ p3_A | split_A4, C_A3 |  |
| [99] | CA4 | DERIVE | base case | `C_A3 = 0` ⇒ C_A3 = 0 N | C_A3, p3_A | checked: follows from p3_A |
| [100] | CA3 | DERIVE | return | `C_A2 = -98/5` ⇒ C_A2 = -98/5 N | C_A2, p2_A3 | checked: follows from p2_A3 |
| [101] | CA2 | DERIVE | return | `C_A1 = -123/5` ⇒ C_A1 = -123/5 N | C_A1, p2_A2 | checked: follows from p2_A2 |
| [102] | CA1 | DERIVE | return | `C_A0 = -23/5` ⇒ C_A0 = -23/5 N | C_A0, p2_A1 | checked: follows from p2_A1 |
| [103] | DA.F | DERIVE | contribution law | `F_A = -23/5` ⇒ F_A = -23/5 N | F_A, p1_A | checked: follows from p1_A |
| [104] | DA | ENTRY | E8 | `a_A = F_A / m_A` — “its net-force-material-object divided by its inertial-mass-material-object.” — return through E8 ⇒ e8_A | R_inertial, a_A, F_A, m_A |  |
| [105] | DA | DERIVE |  | `a_A = -23/10` ⇒ a_A = -23/10 m/s^2 | a_A, e8_A | checked: follows from e8_A |
| [106] | ROOT | ANSWER | A | A's inertial acceleration, upward positive | a_A | a_A = -23/10 m/s^2 |
| [107] | ROOT | DEMAND |  | opens DB: inertial-acceleration-material-object(B, t0, R) |  |  |
| [108] | DB | DELIVER | [1] | q_norm, delivered from ROOT (bound at [1]) with its qualifications: the question asks for inertial-acceleration-material-object of A and of B at t0 in R | q_norm |  |
| [109] | DB | DELIVER | [2] | R_inertial, delivered from ROOT (bound at [2]) with its qualifications: R is a supplied inertial frame | R_inertial |  |
| [110] | DB | DELIVER | [6] | H_B = 0 N, delivered from ROOT (bound at [6]) with its qualifications: haze-material-object(B, t0) = 0 | H_B |  |
| [111] | DB | DELIVER | [21] | a_B, delivered from ROOT (bound at [21]) with its qualifications: the demanded inertial acceleration of B | a_B |  |
| [112] | DB | DEMAND | E8 | opens DB.F: E8: demand net-force-material-object(B, t0, R) |  |  |
| [113] | DB | DEMAND | E8 | opens DB.m: E8: demand inertial-mass-material-object(B) |  |  |
| [114] | DB.m | INPUT | value | inertial mass of B, supplied independently ⇒ m_B = 1 kg |  |  |
| [115] | DB | DELIVER | [22] | F_B, delivered from ROOT (bound at [22]) with its qualifications: net force on B | F_B |  |
| [116] | DB | DELIVER | [14] | IS_B, delivered from ROOT (bound at [14]) with its qualifications: interaction-set(B, t0) = (A_s2, A_gB) | IS_B |  |
| [117] | DB.F | ENTRY | P1 | “its haze-material-object plus its contribution-material-object” — unknown C_B0 at contribution(B \| (A_s2, A_gB)): contribution of B's whole list ⇒ C_B0 |  |  |
| [118] | DB.F | ENTRY | P1 | `F_B = H_B + C_B0` — “its haze-material-object plus its contribution-material-object” — the contribution law, net-force corner ⇒ p1_B | H_B, F_B, C_B0 |  |
| [119] | DB.F | DEMAND | P1 | opens CB1: contribution(B \| (A_s2, A_gB)) |  |  |
| [120] | CB1 | DELIVER | [117] | C_B0, delivered from DB.F (bound at [117]) with its qualifications: contribution of B's whole list | C_B0 |  |
| [121] | CB1 | READING |  | case split: the remaining list is not empty, so P2 applies ⇒ split_B1 | IS_B |  |
| [122] | CB1 | INPUT | choice | take A_s2 as the member at this step ⇒ pick_B1 |  |  |
| [123] | CB1 | ENTRY | P2 | “the impressed-force of one member” — unknown f_B_A_s2 at impressed-force(A_s2 -> B, t0, R): impressed force of A_s2 on B ⇒ f_B_A_s2 | pick_B1 |  |
| [124] | CB1 | ENTRY | P2 | “the contribution-material-object of the same set without that member” — unknown C_B1 at contribution(B \| (A_gB)): contribution of the remaining list ⇒ C_B1 | pick_B1 |  |
| [125] | CB1 | READING |  | the remaining list without A_s2 is (A_gB) ⇒ rest_B1 | IS_B, pick_B1 |  |
| [126] | CB1 | ENTRY | P2 | `C_B0 = f_B_A_s2 + C_B1` — “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step ⇒ p2_B1 | split_B1, pick_B1, rest_B1, C_B0, f_B_A_s2, C_B1 |  |
| [127] | CB1 | DEMAND | P2 | opens CB1.A_s2: impressed-force(A_s2 -> B, t0, R) |  |  |
| [128] | CB1.A_s2 | DELIVER | [123] | f_B_A_s2, delivered from CB1 (bound at [123]) with its qualifications: impressed force of A_s2 on B | f_B_A_s2 |  |
| [129] | CB1.A_s2 | READING |  | dispatch: A_s2 is the action of s2, so P4 applies ⇒ disp_B_A_s2 | IS_B |  |
| [130] | DB | DELIVER | [16] | K_s2 = 5 N, delivered from ROOT (bound at [16], value fixed at [71]) with its qualifications: action-force of s2 (lands on B) — the same action value, delivered, not computed again | K_s2 |  |
| [131] | CB1.A_s2 | ENTRY | P4 | `f_B_A_s2 = K_s2` — “For a member that is the action of an acting-object, the action-force of that acting-object.” — impressed force of an action member ⇒ p4_B_s2 | disp_B_A_s2, f_B_A_s2, K_s2 |  |
| [132] | CB1.A_s2 | DERIVE | A_s2 on B | `f_B_A_s2 = 5` ⇒ f_B_A_s2 = 5 N | f_B_A_s2, p4_B_s2 | checked: follows from p4_B_s2 |
| [133] | CB1 | DEMAND | P2 | opens CB2: contribution(B \| (A_gB)) |  |  |
| [134] | CB2 | DELIVER | [124] | C_B1, delivered from CB1 (bound at [124]) with its qualifications: contribution of the remaining list | C_B1 |  |
| [135] | CB2 | READING |  | case split: the remaining list is not empty, so P2 applies ⇒ split_B2 | IS_B |  |
| [136] | CB2 | INPUT | choice | take A_gB as the member at this step ⇒ pick_B2 |  |  |
| [137] | CB2 | ENTRY | P2 | “the impressed-force of one member” — unknown f_B_A_gB at impressed-force(A_gB -> B, t0, R): impressed force of A_gB on B ⇒ f_B_A_gB | pick_B2 |  |
| [138] | CB2 | ENTRY | P2 | “the contribution-material-object of the same set without that member” — unknown C_B2 at contribution(B \| ()): contribution of the remaining list ⇒ C_B2 | pick_B2 |  |
| [139] | CB2 | READING |  | the remaining list without A_gB is () ⇒ rest_B2 | IS_B, pick_B2 |  |
| [140] | CB2 | ENTRY | P2 | `C_B1 = f_B_A_gB + C_B2` — “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step ⇒ p2_B2 | split_B2, pick_B2, rest_B2, C_B1, f_B_A_gB, C_B2 |  |
| [141] | CB2 | DEMAND | P2 | opens CB2.A_gB: impressed-force(A_gB -> B, t0, R) |  |  |
| [142] | CB2.A_gB | DELIVER | [137] | f_B_A_gB, delivered from CB2 (bound at [137]) with its qualifications: impressed force of A_gB on B | f_B_A_gB |  |
| [143] | CB2.A_gB | READING |  | dispatch: A_gB is the action of gB, so P4 applies ⇒ disp_B_A_gB | IS_B |  |
| [144] | CB2.A_gB | DEMAND | P4 | opens CB2.A_gB.K: action-force(gB) |  |  |
| [145] | DB | DELIVER | [18] | K_gB, delivered from ROOT (bound at [18]) with its qualifications: action-force of gB (lands on B) | K_gB |  |
| [146] | DB | DELIVER | [4] | g = 49/5 m/s^2, delivered from ROOT (bound at [4]) with its qualifications: local field-strength, the same at A and at B | g |  |
| [147] | CB2.A_gB.K | INPUT | value | gravitational mass of B ⇒ mu_B = 1 kg |  |  |
| [148] | CB2.A_gB.K | ENTRY | P8 | `K_gB = -mu_B*g` — “the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis” — action-force_near-surface-gravity for gB ⇒ law_gB | mu_B, g, K_gB |  |
| [149] | CB2.A_gB.K | DERIVE | action value gB | `K_gB = -49/5` ⇒ K_gB = -49/5 N | K_gB, law_gB | checked: follows from law_gB |
| [150] | CB2.A_gB | ENTRY | P4 | `f_B_A_gB = K_gB` — “For a member that is the action of an acting-object, the action-force of that acting-object.” — impressed force of an action member ⇒ p4_B_gB | disp_B_A_gB, f_B_A_gB, K_gB |  |
| [151] | CB2.A_gB | DERIVE | A_gB on B | `f_B_A_gB = -49/5` ⇒ f_B_A_gB = -49/5 N | f_B_A_gB, p4_B_gB | checked: follows from p4_B_gB |
| [152] | CB2 | DEMAND | P2 | opens CB3: contribution(B \| ()) |  |  |
| [153] | CB3 | DELIVER | [138] | C_B2, delivered from CB2 (bound at [138]) with its qualifications: contribution of the remaining list | C_B2 |  |
| [154] | CB3 | READING |  | case split: the remaining list is empty, so P3 applies ⇒ split_B3 | IS_B |  |
| [155] | CB3 | ENTRY | P3 | `C_B2 = 0` — “For one material-object and an empty remaining interaction-set, the zero vector.” — base case ⇒ p3_B | split_B3, C_B2 |  |
| [156] | CB3 | DERIVE | base case | `C_B2 = 0` ⇒ C_B2 = 0 N | C_B2, p3_B | checked: follows from p3_B |
| [157] | CB2 | DERIVE | return | `C_B1 = -49/5` ⇒ C_B1 = -49/5 N | C_B1, p2_B2 | checked: follows from p2_B2 |
| [158] | CB1 | DERIVE | return | `C_B0 = -24/5` ⇒ C_B0 = -24/5 N | C_B0, p2_B1 | checked: follows from p2_B1 |
| [159] | DB.F | DERIVE | contribution law | `F_B = -24/5` ⇒ F_B = -24/5 N | F_B, p1_B | checked: follows from p1_B |
| [160] | DB | ENTRY | E8 | `a_B = F_B / m_B` — “its net-force-material-object divided by its inertial-mass-material-object.” — return through E8 ⇒ e8_B | R_inertial, a_B, F_B, m_B |  |
| [161] | DB | DERIVE |  | `a_B = -24/5` ⇒ a_B = -24/5 m/s^2 | a_B, e8_B | checked: follows from e8_B |
| [162] | ROOT | ANSWER | B | B's inertial acceleration, upward positive | a_B | a_B = -24/5 m/s^2 |
| [163] | ROOT | READING |  | unknown F_sys at net-force({A, B}, t0, R): net force on the system {A, B} ⇒ F_sys |  |  |
| [164] | ROOT | READING |  | `F_sys = F_A + F_B` — the system's net force is the sum of its members' net forces ⇒ sys | F_sys, F_A, F_B |  |
| [165] | ROOT | DERIVE |  | `F_sys = -47/5` ⇒ F_sys = -47/5 N | F_sys, sys | checked: follows from sys |
| [166] | ROOT | ANSWER | sys | net force on the two blocks together | F_sys | F_sys = -47/5 N |

## Ledger for answer A

**Answer:** a_A = -23/10 m/s^2

### World commitments that feed the answer (members)

| Step | Name | Kind | Status | Countermodel | Content |
|---|---|---|---|---|---|
| [2] | R_inertial | model |  |  | R is a supplied inertial frame |
| [4] | g | value |  |  | g = 49/5 m/s^2 (local field-strength, the same at A and at B) |
| [5] | H_A | haze |  |  | H_A = 0 N (haze-material-object(A, t0) = 0) |
| [7] | rec_s1 | recognition |  |  | spring s1 is carried by the ceiling and attached to A; intact, Hookean |
| [8] | rec_s2 | recognition |  |  | spring s2 is carried by A and attached to B; intact, Hookean |
| [9] | rec_gA | recognition |  |  | A is in the Earth's near-surface field |
| [11] | closed_A | completeness |  |  | no more members to be added to A's list at this tolerance |
| [30] | m_A | value |  |  | m_A = 2 kg (inertial mass of A, supplied independently) |
| [48] | k1 | value |  |  | k1 = 20 N/m (stiffness of s1) |
| [49] | x1 | value |  |  | x1 = -1 m (signed displacement of A from s1's relaxed position (negative: below it)) |
| [68] | k2 | value |  |  | k2 = 10 N/m (stiffness of s2) |
| [69] | x2 | value |  |  | x2 = -1/2 m (signed displacement of B from s2's relaxed position (negative: below it)) |
| [90] | mu_A | value |  |  | mu_A = 2 kg (gravitational mass of A) |

### Pruned premises (feed the answer, not members)

- [1] q_norm: the question asks for inertial-acceleration-material-object of A and of B at t0 in R (kind normalization is not a claim about the world)
- [38] pick_A1: take A_s1 as the member at this step (kind choice is not a claim about the world)
- [57] pick_A2: take R_s2 as the member at this step (kind choice is not a claim about the world)
- [79] pick_A3: take A_gA as the member at this step (kind choice is not a claim about the world)

### Theory side that feeds the answer

- [13] READING : interaction-set(A, t0) = (A_s1, R_s2, A_gA): an instance gives its action to its other participant and its reaction to its carrier
- [15] ENTRY P7: “the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis” — unknown K_s1 at action-force(s1, t0, R): action-force of s1 (lands on A)
- [16] ENTRY P7: “the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis” — unknown K_s2 at action-force(s2, t0, R): action-force of s2 (lands on B)
- [17] ENTRY P8: “the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis” — unknown K_gA at action-force(gA, t0, R): action-force of gA (lands on A)
- [19] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — unknown a_A at inertial-acceleration(A, t0, R): the demanded inertial acceleration of A
- [20] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — unknown F_A at net-force(A, t0, R): net force on A
- [33] ENTRY P1: “its haze-material-object plus its contribution-material-object” — unknown C_A0 at contribution(A \| (A_s1, R_s2, A_gA)): contribution of A's whole list
- [34] ENTRY P1: “its haze-material-object plus its contribution-material-object” — the contribution law, net-force corner
- [37] READING : case split: the remaining list is not empty, so P2 applies
- [39] ENTRY P2: “the impressed-force of one member” — unknown f_A_A_s1 at impressed-force(A_s1 -> A, t0, R): impressed force of A_s1 on A
- [40] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_A1 at contribution(A \| (R_s2, A_gA)): contribution of the remaining list
- [41] READING : the remaining list without A_s1 is (R_s2, A_gA)
- [42] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [45] READING : dispatch: A_s1 is the action of s1, so P4 applies
- [50] ENTRY P7: “the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis” — action-force_spring for s1
- [52] ENTRY P4: “For a member that is the action of an acting-object, the action-force of that acting-object.” — impressed force of an action member
- [56] READING : case split: the remaining list is not empty, so P2 applies
- [58] ENTRY P2: “the impressed-force of one member” — unknown f_A_R_s2 at impressed-force(R_s2 -> A, t0, R): impressed force of R_s2 on A
- [59] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_A2 at contribution(A \| (A_gA)): contribution of the remaining list
- [60] READING : the remaining list without R_s2 is (A_gA)
- [61] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [64] READING : dispatch: R_s2 is the reaction of s2, so P5 applies
- [65] ENTRY P5: “For a member that is the reaction of an acting-object, the reaction-force of that acting-object.” — unknown Rf_s2 at reaction-force(s2, t0, R): reaction-force of s2 (lands on its carrier, A)
- [70] ENTRY P7: “the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis” — action-force_spring for s2
- [72] ENTRY P6: “For one acting-object, the negative of its action-force.” — reaction by negation of the action
- [74] ENTRY P5: “For a member that is the reaction of an acting-object, the reaction-force of that acting-object.” — impressed force of a reaction member
- [78] READING : case split: the remaining list is not empty, so P2 applies
- [80] ENTRY P2: “the impressed-force of one member” — unknown f_A_A_gA at impressed-force(A_gA -> A, t0, R): impressed force of A_gA on A
- [81] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_A3 at contribution(A \| ()): contribution of the remaining list
- [82] READING : the remaining list without A_gA is ()
- [83] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [86] READING : dispatch: A_gA is the action of gA, so P4 applies
- [91] ENTRY P8: “the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis” — action-force_near-surface-gravity for gA
- [93] ENTRY P4: “For a member that is the action of an acting-object, the action-force of that acting-object.” — impressed force of an action member
- [97] READING : case split: the remaining list is empty, so P3 applies
- [98] ENTRY P3: “For one material-object and an empty remaining interaction-set, the zero vector.” — base case
- [104] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — return through E8

### Step members (metalinguistic)

- [51] action value s1: K_s1 = 20 (checked)
- [53] A_s1 on A: f_A_A_s1 = 20 (checked)
- [71] action value s2: K_s2 = 5 (checked)
- [73] reaction value s2: Rf_s2 = -5 (checked)
- [75] R_s2 on A: f_A_R_s2 = -5 (checked)
- [92] action value gA: K_gA = -98/5 (checked)
- [94] A_gA on A: f_A_A_gA = -98/5 (checked)
- [99] base case: C_A3 = 0 (checked)
- [100] return: C_A2 = -98/5 (checked)
- [101] return: C_A1 = -123/5 (checked)
- [102] return: C_A0 = -23/5 (checked)
- [103] contribution law: F_A = -23/5 (checked)
- [105] DERIVE: a_A = -23/10 (checked)

### Inputs that do not feed the answer

- [3] axis (convention): one vertical axis, upward positive
- [6] H_B (haze): H_B = 0 N (haze-material-object(B, t0) = 0)
- [10] rec_gB (recognition): B is in the Earth's near-surface field
- [12] closed_B (completeness): no more members to be added to B's list at this tolerance
- [114] m_B (value): m_B = 1 kg (inertial mass of B, supplied independently)
- [122] pick_B1 (choice): take A_s2 as the member at this step
- [136] pick_B2 (choice): take A_gB as the member at this step
- [147] mu_B (value): mu_B = 1 kg (gravitational mass of B)

### Other steps that do not feed the answer

- [14] READING : interaction-set(B, t0) = (A_s2, A_gB)
- [18] ENTRY P8: “the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis” — unknown K_gB at action-force(gB, t0, R): action-force of gB (lands on B)
- [21] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — unknown a_B at inertial-acceleration(B, t0, R): the demanded inertial acceleration of B
- [22] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — unknown F_B at net-force(B, t0, R): net force on B
- [117] ENTRY P1: “its haze-material-object plus its contribution-material-object” — unknown C_B0 at contribution(B \| (A_s2, A_gB)): contribution of B's whole list
- [118] ENTRY P1: “its haze-material-object plus its contribution-material-object” — the contribution law, net-force corner
- [121] READING : case split: the remaining list is not empty, so P2 applies
- [123] ENTRY P2: “the impressed-force of one member” — unknown f_B_A_s2 at impressed-force(A_s2 -> B, t0, R): impressed force of A_s2 on B
- [124] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_B1 at contribution(B \| (A_gB)): contribution of the remaining list
- [125] READING : the remaining list without A_s2 is (A_gB)
- [126] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [129] READING : dispatch: A_s2 is the action of s2, so P4 applies
- [131] ENTRY P4: “For a member that is the action of an acting-object, the action-force of that acting-object.” — impressed force of an action member
- [132] DERIVE A_s2 on B: f_B_A_s2 = 5
- [135] READING : case split: the remaining list is not empty, so P2 applies
- [137] ENTRY P2: “the impressed-force of one member” — unknown f_B_A_gB at impressed-force(A_gB -> B, t0, R): impressed force of A_gB on B
- [138] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_B2 at contribution(B \| ()): contribution of the remaining list
- [139] READING : the remaining list without A_gB is ()
- [140] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [143] READING : dispatch: A_gB is the action of gB, so P4 applies
- [148] ENTRY P8: “the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis” — action-force_near-surface-gravity for gB
- [149] DERIVE action value gB: K_gB = -49/5
- [150] ENTRY P4: “For a member that is the action of an acting-object, the action-force of that acting-object.” — impressed force of an action member
- [151] DERIVE A_gB on B: f_B_A_gB = -49/5
- [154] READING : case split: the remaining list is empty, so P3 applies
- [155] ENTRY P3: “For one material-object and an empty remaining interaction-set, the zero vector.” — base case
- [156] DERIVE base case: C_B2 = 0
- [157] DERIVE return: C_B1 = -49/5
- [158] DERIVE return: C_B0 = -24/5
- [159] DERIVE contribution law: F_B = -24/5
- [160] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — return through E8
- [161] DERIVE : a_B = -24/5
- [163] READING : unknown F_sys at net-force({A, B}, t0, R): net force on the system {A, B}
- [164] READING : the system's net force is the sum of its members' net forces
- [165] DERIVE : F_sys = -47/5

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

- 13 commitment(s) have no status yet: R_inertial, g, H_A, rec_s1, rec_s2, rec_gA, closed_A, m_A, k1, x1, k2, x2, mu_A

### Hypothesis set for A (prediction side only)

- **p** the prediction holds: a_A = -23/10 m/s^2
- **A1** not (R is a supplied inertial frame)
- **A2** not (g = 49/5 m/s^2 (local field-strength, the same at A and at B))
- **A3** not (H_A = 0 N (haze-material-object(A, t0) = 0))
- **A4** not (spring s1 is carried by the ceiling and attached to A; intact, Hookean)
- **A5** not (spring s2 is carried by A and attached to B; intact, Hookean)
- **A6** not (A is in the Earth's near-surface field)
- **A7** not (no more members to be added to A's list at this tolerance)
- **A8** not (m_A = 2 kg (inertial mass of A, supplied independently))
- **A9** not (k1 = 20 N/m (stiffness of s1))
- **A10** not (x1 = -1 m (signed displacement of A from s1's relaxed position (negative: below it)))
- **A11** not (k2 = 10 N/m (stiffness of s2))
- **A12** not (x2 = -1/2 m (signed displacement of B from s2's relaxed position (negative: below it)))
- **A13** not (mu_A = 2 kg (gravitational mass of A))
- **M1** step [51] went wrong: K_s1 = 20
- **M2** step [53] went wrong: f_A_A_s1 = 20
- **M3** step [71] went wrong: K_s2 = 5
- **M4** step [73] went wrong: Rf_s2 = -5
- **M5** step [75] went wrong: f_A_R_s2 = -5
- **M6** step [92] went wrong: K_gA = -98/5
- **M7** step [94] went wrong: f_A_A_gA = -98/5
- **M8** step [99] went wrong: C_A3 = 0
- **M9** step [100] went wrong: C_A2 = -98/5
- **M10** step [101] went wrong: C_A1 = -123/5
- **M11** step [102] went wrong: C_A0 = -23/5
- **M12** step [103] went wrong: F_A = -23/5
- **M13** step [105] went wrong: a_A = -23/10

## Ledger for answer B

**Answer:** a_B = -24/5 m/s^2

### World commitments that feed the answer (members)

| Step | Name | Kind | Status | Countermodel | Content |
|---|---|---|---|---|---|
| [2] | R_inertial | model |  |  | R is a supplied inertial frame |
| [4] | g | value |  |  | g = 49/5 m/s^2 (local field-strength, the same at A and at B) |
| [6] | H_B | haze |  |  | H_B = 0 N (haze-material-object(B, t0) = 0) |
| [8] | rec_s2 | recognition |  |  | spring s2 is carried by A and attached to B; intact, Hookean |
| [10] | rec_gB | recognition |  |  | B is in the Earth's near-surface field |
| [12] | closed_B | completeness |  |  | no more members to be added to B's list at this tolerance |
| [68] | k2 | value |  |  | k2 = 10 N/m (stiffness of s2) |
| [69] | x2 | value |  |  | x2 = -1/2 m (signed displacement of B from s2's relaxed position (negative: below it)) |
| [114] | m_B | value |  |  | m_B = 1 kg (inertial mass of B, supplied independently) |
| [147] | mu_B | value |  |  | mu_B = 1 kg (gravitational mass of B) |

### Pruned premises (feed the answer, not members)

- [1] q_norm: the question asks for inertial-acceleration-material-object of A and of B at t0 in R (kind normalization is not a claim about the world)
- [122] pick_B1: take A_s2 as the member at this step (kind choice is not a claim about the world)
- [136] pick_B2: take A_gB as the member at this step (kind choice is not a claim about the world)

### Theory side that feeds the answer

- [14] READING : interaction-set(B, t0) = (A_s2, A_gB)
- [16] ENTRY P7: “the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis” — unknown K_s2 at action-force(s2, t0, R): action-force of s2 (lands on B)
- [18] ENTRY P8: “the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis” — unknown K_gB at action-force(gB, t0, R): action-force of gB (lands on B)
- [21] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — unknown a_B at inertial-acceleration(B, t0, R): the demanded inertial acceleration of B
- [22] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — unknown F_B at net-force(B, t0, R): net force on B
- [70] ENTRY P7: “the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis” — action-force_spring for s2
- [117] ENTRY P1: “its haze-material-object plus its contribution-material-object” — unknown C_B0 at contribution(B \| (A_s2, A_gB)): contribution of B's whole list
- [118] ENTRY P1: “its haze-material-object plus its contribution-material-object” — the contribution law, net-force corner
- [121] READING : case split: the remaining list is not empty, so P2 applies
- [123] ENTRY P2: “the impressed-force of one member” — unknown f_B_A_s2 at impressed-force(A_s2 -> B, t0, R): impressed force of A_s2 on B
- [124] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_B1 at contribution(B \| (A_gB)): contribution of the remaining list
- [125] READING : the remaining list without A_s2 is (A_gB)
- [126] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [129] READING : dispatch: A_s2 is the action of s2, so P4 applies
- [131] ENTRY P4: “For a member that is the action of an acting-object, the action-force of that acting-object.” — impressed force of an action member
- [135] READING : case split: the remaining list is not empty, so P2 applies
- [137] ENTRY P2: “the impressed-force of one member” — unknown f_B_A_gB at impressed-force(A_gB -> B, t0, R): impressed force of A_gB on B
- [138] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_B2 at contribution(B \| ()): contribution of the remaining list
- [139] READING : the remaining list without A_gB is ()
- [140] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [143] READING : dispatch: A_gB is the action of gB, so P4 applies
- [148] ENTRY P8: “the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis” — action-force_near-surface-gravity for gB
- [150] ENTRY P4: “For a member that is the action of an acting-object, the action-force of that acting-object.” — impressed force of an action member
- [154] READING : case split: the remaining list is empty, so P3 applies
- [155] ENTRY P3: “For one material-object and an empty remaining interaction-set, the zero vector.” — base case
- [160] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — return through E8

### Step members (metalinguistic)

- [71] action value s2: K_s2 = 5 (checked)
- [132] A_s2 on B: f_B_A_s2 = 5 (checked)
- [149] action value gB: K_gB = -49/5 (checked)
- [151] A_gB on B: f_B_A_gB = -49/5 (checked)
- [156] base case: C_B2 = 0 (checked)
- [157] return: C_B1 = -49/5 (checked)
- [158] return: C_B0 = -24/5 (checked)
- [159] contribution law: F_B = -24/5 (checked)
- [161] DERIVE: a_B = -24/5 (checked)

### Inputs that do not feed the answer

- [3] axis (convention): one vertical axis, upward positive
- [5] H_A (haze): H_A = 0 N (haze-material-object(A, t0) = 0)
- [7] rec_s1 (recognition): spring s1 is carried by the ceiling and attached to A; intact, Hookean
- [9] rec_gA (recognition): A is in the Earth's near-surface field
- [11] closed_A (completeness): no more members to be added to A's list at this tolerance
- [30] m_A (value): m_A = 2 kg (inertial mass of A, supplied independently)
- [38] pick_A1 (choice): take A_s1 as the member at this step
- [48] k1 (value): k1 = 20 N/m (stiffness of s1)
- [49] x1 (value): x1 = -1 m (signed displacement of A from s1's relaxed position (negative: below it))
- [57] pick_A2 (choice): take R_s2 as the member at this step
- [79] pick_A3 (choice): take A_gA as the member at this step
- [90] mu_A (value): mu_A = 2 kg (gravitational mass of A)

### Other steps that do not feed the answer

- [13] READING : interaction-set(A, t0) = (A_s1, R_s2, A_gA): an instance gives its action to its other participant and its reaction to its carrier
- [15] ENTRY P7: “the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis” — unknown K_s1 at action-force(s1, t0, R): action-force of s1 (lands on A)
- [17] ENTRY P8: “the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis” — unknown K_gA at action-force(gA, t0, R): action-force of gA (lands on A)
- [19] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — unknown a_A at inertial-acceleration(A, t0, R): the demanded inertial acceleration of A
- [20] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — unknown F_A at net-force(A, t0, R): net force on A
- [33] ENTRY P1: “its haze-material-object plus its contribution-material-object” — unknown C_A0 at contribution(A \| (A_s1, R_s2, A_gA)): contribution of A's whole list
- [34] ENTRY P1: “its haze-material-object plus its contribution-material-object” — the contribution law, net-force corner
- [37] READING : case split: the remaining list is not empty, so P2 applies
- [39] ENTRY P2: “the impressed-force of one member” — unknown f_A_A_s1 at impressed-force(A_s1 -> A, t0, R): impressed force of A_s1 on A
- [40] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_A1 at contribution(A \| (R_s2, A_gA)): contribution of the remaining list
- [41] READING : the remaining list without A_s1 is (R_s2, A_gA)
- [42] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [45] READING : dispatch: A_s1 is the action of s1, so P4 applies
- [50] ENTRY P7: “the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis” — action-force_spring for s1
- [51] DERIVE action value s1: K_s1 = 20
- [52] ENTRY P4: “For a member that is the action of an acting-object, the action-force of that acting-object.” — impressed force of an action member
- [53] DERIVE A_s1 on A: f_A_A_s1 = 20
- [56] READING : case split: the remaining list is not empty, so P2 applies
- [58] ENTRY P2: “the impressed-force of one member” — unknown f_A_R_s2 at impressed-force(R_s2 -> A, t0, R): impressed force of R_s2 on A
- [59] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_A2 at contribution(A \| (A_gA)): contribution of the remaining list
- [60] READING : the remaining list without R_s2 is (A_gA)
- [61] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [64] READING : dispatch: R_s2 is the reaction of s2, so P5 applies
- [65] ENTRY P5: “For a member that is the reaction of an acting-object, the reaction-force of that acting-object.” — unknown Rf_s2 at reaction-force(s2, t0, R): reaction-force of s2 (lands on its carrier, A)
- [72] ENTRY P6: “For one acting-object, the negative of its action-force.” — reaction by negation of the action
- [73] DERIVE reaction value s2: Rf_s2 = -5
- [74] ENTRY P5: “For a member that is the reaction of an acting-object, the reaction-force of that acting-object.” — impressed force of a reaction member
- [75] DERIVE R_s2 on A: f_A_R_s2 = -5
- [78] READING : case split: the remaining list is not empty, so P2 applies
- [80] ENTRY P2: “the impressed-force of one member” — unknown f_A_A_gA at impressed-force(A_gA -> A, t0, R): impressed force of A_gA on A
- [81] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_A3 at contribution(A \| ()): contribution of the remaining list
- [82] READING : the remaining list without A_gA is ()
- [83] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [86] READING : dispatch: A_gA is the action of gA, so P4 applies
- [91] ENTRY P8: “the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis” — action-force_near-surface-gravity for gA
- [92] DERIVE action value gA: K_gA = -98/5
- [93] ENTRY P4: “For a member that is the action of an acting-object, the action-force of that acting-object.” — impressed force of an action member
- [94] DERIVE A_gA on A: f_A_A_gA = -98/5
- [97] READING : case split: the remaining list is empty, so P3 applies
- [98] ENTRY P3: “For one material-object and an empty remaining interaction-set, the zero vector.” — base case
- [99] DERIVE base case: C_A3 = 0
- [100] DERIVE return: C_A2 = -98/5
- [101] DERIVE return: C_A1 = -123/5
- [102] DERIVE return: C_A0 = -23/5
- [103] DERIVE contribution law: F_A = -23/5
- [104] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — return through E8
- [105] DERIVE : a_A = -23/10
- [163] READING : unknown F_sys at net-force({A, B}, t0, R): net force on the system {A, B}
- [164] READING : the system's net force is the sum of its members' net forces
- [165] DERIVE : F_sys = -47/5

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

- 10 commitment(s) have no status yet: R_inertial, g, H_B, rec_s2, rec_gB, closed_B, k2, x2, m_B, mu_B

### Hypothesis set for B (prediction side only)

- **p** the prediction holds: a_B = -24/5 m/s^2
- **A1** not (R is a supplied inertial frame)
- **A2** not (g = 49/5 m/s^2 (local field-strength, the same at A and at B))
- **A3** not (H_B = 0 N (haze-material-object(B, t0) = 0))
- **A4** not (spring s2 is carried by A and attached to B; intact, Hookean)
- **A5** not (B is in the Earth's near-surface field)
- **A6** not (no more members to be added to B's list at this tolerance)
- **A7** not (k2 = 10 N/m (stiffness of s2))
- **A8** not (x2 = -1/2 m (signed displacement of B from s2's relaxed position (negative: below it)))
- **A9** not (m_B = 1 kg (inertial mass of B, supplied independently))
- **A10** not (mu_B = 1 kg (gravitational mass of B))
- **M1** step [71] went wrong: K_s2 = 5
- **M2** step [132] went wrong: f_B_A_s2 = 5
- **M3** step [149] went wrong: K_gB = -49/5
- **M4** step [151] went wrong: f_B_A_gB = -49/5
- **M5** step [156] went wrong: C_B2 = 0
- **M6** step [157] went wrong: C_B1 = -49/5
- **M7** step [158] went wrong: C_B0 = -24/5
- **M8** step [159] went wrong: F_B = -24/5
- **M9** step [161] went wrong: a_B = -24/5

## Ledger for answer sys

**Answer:** F_sys = -47/5 N

### World commitments that feed the answer (members)

| Step | Name | Kind | Status | Countermodel | Content |
|---|---|---|---|---|---|
| [4] | g | value |  |  | g = 49/5 m/s^2 (local field-strength, the same at A and at B) |
| [5] | H_A | haze |  |  | H_A = 0 N (haze-material-object(A, t0) = 0) |
| [6] | H_B | haze |  |  | H_B = 0 N (haze-material-object(B, t0) = 0) |
| [7] | rec_s1 | recognition |  |  | spring s1 is carried by the ceiling and attached to A; intact, Hookean |
| [8] | rec_s2 | recognition |  |  | spring s2 is carried by A and attached to B; intact, Hookean |
| [9] | rec_gA | recognition |  |  | A is in the Earth's near-surface field |
| [10] | rec_gB | recognition |  |  | B is in the Earth's near-surface field |
| [11] | closed_A | completeness |  |  | no more members to be added to A's list at this tolerance |
| [12] | closed_B | completeness |  |  | no more members to be added to B's list at this tolerance |
| [48] | k1 | value |  |  | k1 = 20 N/m (stiffness of s1) |
| [49] | x1 | value |  |  | x1 = -1 m (signed displacement of A from s1's relaxed position (negative: below it)) |
| [68] | k2 | value |  |  | k2 = 10 N/m (stiffness of s2) |
| [69] | x2 | value |  |  | x2 = -1/2 m (signed displacement of B from s2's relaxed position (negative: below it)) |
| [90] | mu_A | value |  |  | mu_A = 2 kg (gravitational mass of A) |
| [147] | mu_B | value |  |  | mu_B = 1 kg (gravitational mass of B) |

### Pruned premises (feed the answer, not members)

- [38] pick_A1: take A_s1 as the member at this step (kind choice is not a claim about the world)
- [57] pick_A2: take R_s2 as the member at this step (kind choice is not a claim about the world)
- [79] pick_A3: take A_gA as the member at this step (kind choice is not a claim about the world)
- [122] pick_B1: take A_s2 as the member at this step (kind choice is not a claim about the world)
- [136] pick_B2: take A_gB as the member at this step (kind choice is not a claim about the world)

### Theory side that feeds the answer

- [13] READING : interaction-set(A, t0) = (A_s1, R_s2, A_gA): an instance gives its action to its other participant and its reaction to its carrier
- [14] READING : interaction-set(B, t0) = (A_s2, A_gB)
- [15] ENTRY P7: “the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis” — unknown K_s1 at action-force(s1, t0, R): action-force of s1 (lands on A)
- [16] ENTRY P7: “the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis” — unknown K_s2 at action-force(s2, t0, R): action-force of s2 (lands on B)
- [17] ENTRY P8: “the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis” — unknown K_gA at action-force(gA, t0, R): action-force of gA (lands on A)
- [18] ENTRY P8: “the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis” — unknown K_gB at action-force(gB, t0, R): action-force of gB (lands on B)
- [20] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — unknown F_A at net-force(A, t0, R): net force on A
- [22] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — unknown F_B at net-force(B, t0, R): net force on B
- [33] ENTRY P1: “its haze-material-object plus its contribution-material-object” — unknown C_A0 at contribution(A \| (A_s1, R_s2, A_gA)): contribution of A's whole list
- [34] ENTRY P1: “its haze-material-object plus its contribution-material-object” — the contribution law, net-force corner
- [37] READING : case split: the remaining list is not empty, so P2 applies
- [39] ENTRY P2: “the impressed-force of one member” — unknown f_A_A_s1 at impressed-force(A_s1 -> A, t0, R): impressed force of A_s1 on A
- [40] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_A1 at contribution(A \| (R_s2, A_gA)): contribution of the remaining list
- [41] READING : the remaining list without A_s1 is (R_s2, A_gA)
- [42] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [45] READING : dispatch: A_s1 is the action of s1, so P4 applies
- [50] ENTRY P7: “the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis” — action-force_spring for s1
- [52] ENTRY P4: “For a member that is the action of an acting-object, the action-force of that acting-object.” — impressed force of an action member
- [56] READING : case split: the remaining list is not empty, so P2 applies
- [58] ENTRY P2: “the impressed-force of one member” — unknown f_A_R_s2 at impressed-force(R_s2 -> A, t0, R): impressed force of R_s2 on A
- [59] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_A2 at contribution(A \| (A_gA)): contribution of the remaining list
- [60] READING : the remaining list without R_s2 is (A_gA)
- [61] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [64] READING : dispatch: R_s2 is the reaction of s2, so P5 applies
- [65] ENTRY P5: “For a member that is the reaction of an acting-object, the reaction-force of that acting-object.” — unknown Rf_s2 at reaction-force(s2, t0, R): reaction-force of s2 (lands on its carrier, A)
- [70] ENTRY P7: “the negative of its stiffness times the displacement of its other participant from the relaxed position along the declared axis” — action-force_spring for s2
- [72] ENTRY P6: “For one acting-object, the negative of its action-force.” — reaction by negation of the action
- [74] ENTRY P5: “For a member that is the reaction of an acting-object, the reaction-force of that acting-object.” — impressed force of a reaction member
- [78] READING : case split: the remaining list is not empty, so P2 applies
- [80] ENTRY P2: “the impressed-force of one member” — unknown f_A_A_gA at impressed-force(A_gA -> A, t0, R): impressed force of A_gA on A
- [81] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_A3 at contribution(A \| ()): contribution of the remaining list
- [82] READING : the remaining list without A_gA is ()
- [83] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [86] READING : dispatch: A_gA is the action of gA, so P4 applies
- [91] ENTRY P8: “the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis” — action-force_near-surface-gravity for gA
- [93] ENTRY P4: “For a member that is the action of an acting-object, the action-force of that acting-object.” — impressed force of an action member
- [97] READING : case split: the remaining list is empty, so P3 applies
- [98] ENTRY P3: “For one material-object and an empty remaining interaction-set, the zero vector.” — base case
- [117] ENTRY P1: “its haze-material-object plus its contribution-material-object” — unknown C_B0 at contribution(B \| (A_s2, A_gB)): contribution of B's whole list
- [118] ENTRY P1: “its haze-material-object plus its contribution-material-object” — the contribution law, net-force corner
- [121] READING : case split: the remaining list is not empty, so P2 applies
- [123] ENTRY P2: “the impressed-force of one member” — unknown f_B_A_s2 at impressed-force(A_s2 -> B, t0, R): impressed force of A_s2 on B
- [124] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_B1 at contribution(B \| (A_gB)): contribution of the remaining list
- [125] READING : the remaining list without A_s2 is (A_gB)
- [126] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [129] READING : dispatch: A_s2 is the action of s2, so P4 applies
- [131] ENTRY P4: “For a member that is the action of an acting-object, the action-force of that acting-object.” — impressed force of an action member
- [135] READING : case split: the remaining list is not empty, so P2 applies
- [137] ENTRY P2: “the impressed-force of one member” — unknown f_B_A_gB at impressed-force(A_gB -> B, t0, R): impressed force of A_gB on B
- [138] ENTRY P2: “the contribution-material-object of the same set without that member” — unknown C_B2 at contribution(B \| ()): contribution of the remaining list
- [139] READING : the remaining list without A_gB is ()
- [140] ENTRY P2: “the impressed-force of one member of that set on the material-object plus the contribution-material-object of the same set without that member” — the Force-Sum step
- [143] READING : dispatch: A_gB is the action of gB, so P4 applies
- [148] ENTRY P8: “the negative of the gravitational-mass of its other participant times the local field-strength along the upward axis” — action-force_near-surface-gravity for gB
- [150] ENTRY P4: “For a member that is the action of an acting-object, the action-force of that acting-object.” — impressed force of an action member
- [154] READING : case split: the remaining list is empty, so P3 applies
- [155] ENTRY P3: “For one material-object and an empty remaining interaction-set, the zero vector.” — base case
- [163] READING : unknown F_sys at net-force({A, B}, t0, R): net force on the system {A, B}
- [164] READING : the system's net force is the sum of its members' net forces

### Step members (metalinguistic)

- [51] action value s1: K_s1 = 20 (checked)
- [53] A_s1 on A: f_A_A_s1 = 20 (checked)
- [71] action value s2: K_s2 = 5 (checked)
- [73] reaction value s2: Rf_s2 = -5 (checked)
- [75] R_s2 on A: f_A_R_s2 = -5 (checked)
- [92] action value gA: K_gA = -98/5 (checked)
- [94] A_gA on A: f_A_A_gA = -98/5 (checked)
- [99] base case: C_A3 = 0 (checked)
- [100] return: C_A2 = -98/5 (checked)
- [101] return: C_A1 = -123/5 (checked)
- [102] return: C_A0 = -23/5 (checked)
- [103] contribution law: F_A = -23/5 (checked)
- [132] A_s2 on B: f_B_A_s2 = 5 (checked)
- [149] action value gB: K_gB = -49/5 (checked)
- [151] A_gB on B: f_B_A_gB = -49/5 (checked)
- [156] base case: C_B2 = 0 (checked)
- [157] return: C_B1 = -49/5 (checked)
- [158] return: C_B0 = -24/5 (checked)
- [159] contribution law: F_B = -24/5 (checked)
- [165] DERIVE: F_sys = -47/5 (checked)

### Inputs that do not feed the answer

- [1] q_norm (normalization): the question asks for inertial-acceleration-material-object of A and of B at t0 in R
- [2] R_inertial (model): R is a supplied inertial frame
- [3] axis (convention): one vertical axis, upward positive
- [30] m_A (value): m_A = 2 kg (inertial mass of A, supplied independently)
- [114] m_B (value): m_B = 1 kg (inertial mass of B, supplied independently)

### Other steps that do not feed the answer

- [19] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — unknown a_A at inertial-acceleration(A, t0, R): the demanded inertial acceleration of A
- [21] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — unknown a_B at inertial-acceleration(B, t0, R): the demanded inertial acceleration of B
- [104] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — return through E8
- [105] DERIVE : a_A = -23/10
- [160] ENTRY E8: “its net-force-material-object divided by its inertial-mass-material-object.” — return through E8
- [161] DERIVE : a_B = -24/5

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

- 15 commitment(s) have no status yet: g, H_A, H_B, rec_s1, rec_s2, rec_gA, rec_gB, closed_A, closed_B, k1, x1, k2, x2, mu_A, mu_B

### Hypothesis set for sys (prediction side only)

- **p** the prediction holds: F_sys = -47/5 N
- **A1** not (g = 49/5 m/s^2 (local field-strength, the same at A and at B))
- **A2** not (H_A = 0 N (haze-material-object(A, t0) = 0))
- **A3** not (H_B = 0 N (haze-material-object(B, t0) = 0))
- **A4** not (spring s1 is carried by the ceiling and attached to A; intact, Hookean)
- **A5** not (spring s2 is carried by A and attached to B; intact, Hookean)
- **A6** not (A is in the Earth's near-surface field)
- **A7** not (B is in the Earth's near-surface field)
- **A8** not (no more members to be added to A's list at this tolerance)
- **A9** not (no more members to be added to B's list at this tolerance)
- **A10** not (k1 = 20 N/m (stiffness of s1))
- **A11** not (x1 = -1 m (signed displacement of A from s1's relaxed position (negative: below it)))
- **A12** not (k2 = 10 N/m (stiffness of s2))
- **A13** not (x2 = -1/2 m (signed displacement of B from s2's relaxed position (negative: below it)))
- **A14** not (mu_A = 2 kg (gravitational mass of A))
- **A15** not (mu_B = 1 kg (gravitational mass of B))
- **M1** step [51] went wrong: K_s1 = 20
- **M2** step [53] went wrong: f_A_A_s1 = 20
- **M3** step [71] went wrong: K_s2 = 5
- **M4** step [73] went wrong: Rf_s2 = -5
- **M5** step [75] went wrong: f_A_R_s2 = -5
- **M6** step [92] went wrong: K_gA = -98/5
- **M7** step [94] went wrong: f_A_A_gA = -98/5
- **M8** step [99] went wrong: C_A3 = 0
- **M9** step [100] went wrong: C_A2 = -98/5
- **M10** step [101] went wrong: C_A1 = -123/5
- **M11** step [102] went wrong: C_A0 = -23/5
- **M12** step [103] went wrong: F_A = -23/5
- **M13** step [132] went wrong: f_B_A_s2 = 5
- **M14** step [149] went wrong: K_gB = -49/5
- **M15** step [151] went wrong: f_B_A_gB = -49/5
- **M16** step [156] went wrong: C_B2 = 0
- **M17** step [157] went wrong: C_B1 = -49/5
- **M18** step [158] went wrong: C_B0 = -24/5
- **M19** step [159] went wrong: F_B = -24/5
- **M20** step [165] went wrong: F_sys = -47/5

Checks cover exact arithmetic and bookkeeping only. A countermodel marked [check: ...] was re-solved from the recorded premises; physics, recognition, meaning and unmarked countermodels are not checked, and the observation side of a trial is not modelled.

