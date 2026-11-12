"""Probe (scratch, 11 November 2026): the contribution law and the Force-Sum recursion
on a two-member account, recorded with the hand-trace recorder.

Not an example of the dictionary: P1-P3 are Claude's wording of the rows of
contribution_law_and_force_sum_decisions_2026-11-11.md, appended to Design 2.1
Draft 1 in a scratch entries file (VD_ENTRIES) only so ENTRY quotes can be
verified. No wall entries exist for P1-P3.

Scene: block A hangs from spring s in uniform gravity, at instant t0, upward
positive. k = 20 N/m, extension 1/2 m (spring pulls A up), g = 49/5 m/s^2,
masses 2 kg, haze H = 0. Expected a = (10 - 98/5)/2 = -24/5 m/s^2.

    VD_ENTRIES=/path/entries_with_proposed.md python handtrace_probe_contribution_law.py
"""

from __future__ import annotations

import os
from fractions import Fraction
from pathlib import Path

from handtrace import ROOT, Trace, TraceError, load_entries

ENTRIES = Path(os.environ.get("VD_ENTRIES", "entries_with_proposed.md"))
SRC = "contribution_law_and_force_sum_decisions_2026-11-11.md"

E8 = ("For one material-object, its net-force-material-object divided by\n"
      "its inertial-mass-material-object.")
P1 = "its haze-material-object plus its contribution-material-object"
P2_STEP = ("the impressed-force of one member of that set on the material-object plus the "
           "contribution-material-object of the same set without that member")
P2_IF = "the impressed-force of one member"
P2_TAIL = "the contribution-material-object of the same set without that member"
P3 = "For one material-object and an empty remaining interaction-set, the zero vector."

MEMBERS = {
    "s": dict(iname="i_s", f="f_s", label="spring interaction i_s (spring s above A)"),
    "g": dict(iname="i_g", f="f_g", label="gravity interaction i_g (Earth on A)"),
}


def _member_value(t: Trace, frame: str, key: str) -> None:
    """Evaluate one member's impressed force in its own demand frame."""
    m = MEMBERS[key]
    d = t.demand(frame, f"{frame}.{key.upper()}", f"impressed-force({m['iname']} -> A, t0, R)", ref="P2")
    t.deliver(d, m["f"])
    if key == "s":
        t.input(d, "k", "value", "stiffness of s", value=20, unit="N/m")
        t.input(d, "e", "value", "extension of s (stretched, so it pulls A up)", value="1/2", unit="m")
        t.contract(d, "C-spring", "spring dispatch: f(i_s -> A) = +k e (upward positive)",
                   source="proposed connection, as in handtrace_example_spring_single", binds="r_s",
                   relation="f_s = k*e", uses=["k", "e"])
        t.derive(d, "f_s = 10", from_relations=["r_s"], binds="f_s", tag="spring value")
    else:
        t.input(d, "g", "value", "local gravitational field strength", value="49/5", unit="m/s^2")
        t.input(d, "m_grav", "value", "gravitational mass of A (its equality with the inertial mass is not "
                "used anywhere in this trace)", value=2, unit="kg")
        t.contract(d, "C-gravity", "gravity dispatch: f(i_g -> A) = -m_grav g (upward positive)",
                   source="proposed connection", binds="r_g", relation="f_g = -m_grav*g", uses=["g", "m_grav"])
        t.derive(d, "f_g = -98/5", from_relations=["r_g"], binds="f_g", tag="gravity value")


def build(order=("s", "g"), *, past_the_end: str = "", partial: bool = False) -> Trace:
    """order: which member the tracer takes first.
    past_the_end: '' (normal), 'reuse' (take i_g again from the empty set),
    'invent' (supply a further member i_x)."""
    entries = load_entries(str(ENTRIES)) if ENTRIES.exists() else None
    t = Trace("What is A's inertial acceleration at t0?",
              {"dictionary": "Design 2.1 Draft 1 + scratch P1-P3", "source": SRC}, entries=entries)

    # -- scene-wide inputs
    t.input(ROOT, "q_norm", "normalization", "the question asks for inertial-acceleration-material-object(A, t0, R)")
    t.input(ROOT, "R_inertial", "model", "R is a supplied inertial frame")
    t.input(ROOT, "axis", "convention", "upward positive along the single axis")
    t.input(ROOT, "H", "haze", "haze-material-object(A, t0) = 0 at a tolerance the haze wall would state "
            "(that wall is not written)", value=0, unit="N")

    d1 = t.demand(ROOT, "D1", "inertial-acceleration-material-object(A, t0, R)")
    t.deliver_many(d1, ["q_norm", "R_inertial", "H"])
    t.unknown(d1, "a_A", "the demanded inertial acceleration", address="inertial-acceleration(A, t0, R)",
              label="ENTRY", ref="E8", quote=E8, unit="m/s^2", uses=["q_norm"])
    d11 = t.demand(d1, "D1.1", "E8: demand net-force-material-object(A, t0, R)", ref="E8")
    d12 = t.demand(d1, "D1.2", "E8: demand inertial-mass-material-object(A)", ref="E8")
    t.input(d12, "m_A", "value", "inertial mass of A, supplied independently", value=2, unit="kg")

    # -- the contribution law (P1): net force = haze + contribution
    t.unknown(d11, "F_A", "net force on A", address="net-force(A, t0, R)", label="ENTRY", ref="E8",
              quote=E8, unit="N")
    t.unknown(d11, "C_0", "contribution of A's whole interaction-set", label="ENTRY", ref="P1",
              quote=P1, address="contribution(A | {i_s, i_g}, t0, R)", unit="N")
    t.entry(d11, "P1", P1, text="the contribution law, net-force corner", binds="p1",
            relation="F_A = H + C_0", uses=["H"])

    # -- membership: built behind the interaction-set's wall, NOT inside Force-Sum
    t.input(d11, "rec_s", "recognition", "spring s is attached to A, intact and Hookean: i_s acts on A")
    t.input(d11, "rec_g", "recognition", "A is near the Earth's surface: i_g acts on A")
    t.input(d11, "closed", "completeness",
            "no more elements to be added to interaction-set(A, t0) at this tolerance; everything else is "
            "left to haze (row 5.1's physical claim; the recorder's only kind for it is named 'completeness', "
            "which row 5.3 retires)", uses=["rec_s", "rec_g", "H"])
    t.reading(d11, "interaction-set(A, t0) = {i_s, i_g}", binds="IS", uses=["rec_s", "rec_g", "closed"])

    # -- Force-Sum expansion: P2 steps, P3 base. Frames hold the remaining set.
    remaining = list(order)
    frame, cur = d11, "C_0"
    level = 0
    while True:
        level += 1
        child = t.demand(frame, f"C{level}", f"contribution(A | {{{', '.join(MEMBERS[k]['iname'] for k in remaining)}}})"
                         if remaining else "contribution(A | {})", ref="P1" if level == 1 else "P2")
        t.deliver(child, cur)
        t.deliver(child, "IS") if level == 1 else None
        if not remaining:
            if past_the_end:
                break
            t.reading(child, "case split: the remaining set is empty, so P3 applies", uses=["IS"],
                      binds=f"split{level}")
            t.entry(child, "P3", P3, text="base case", binds=f"p3", relation=f"{cur} = 0", uses=[f"split{level}"])
            t.derive(child, f"{cur} = 0", from_relations=["p3"], binds=cur, tag="base case")
            break
        key = remaining[0]
        rest = remaining[1:]
        m = MEMBERS[key]
        t.reading(child, f"case split: the remaining set is not empty, so P2 applies", uses=["IS"],
                  binds=f"split{level}")
        t.input(child, f"pick{level}", "choice", f"take {m['iname']} as the member at this step")
        nxt = f"C_{level}"
        t.unknown(child, m["f"], f"impressed force of {m['label']} on A", label="ENTRY", ref="P2",
                  quote=P2_IF, address=f"impressed-force({m['iname']} -> A, t0, R)", unit="N", uses=[f"pick{level}"])
        rest_txt = ", ".join(MEMBERS[k]["iname"] for k in rest)
        t.unknown(child, nxt, "contribution of the remaining set", label="ENTRY", ref="P2", quote=P2_TAIL,
                  address=f"contribution(A | {{{rest_txt}}}, t0, R)", unit="N", uses=[f"pick{level}"])
        t.reading(child, f"the remaining set without {m['iname']} is {{{rest_txt}}}", uses=["IS", f"pick{level}"],
                  binds=f"rest{level}")
        t.entry(child, "P2", P2_STEP, text="the Force-Sum step", binds=f"p2_{level}",
                relation=f"{cur} = {m['f']} + {nxt}", uses=[f"split{level}", f"pick{level}", f"rest{level}"])
        if partial:
            taken = [MEMBERS[k]["f"] for k in order[:level]]
            t.derive(d11, "F_A = H + " + " + ".join(taken) + f" + {nxt}",
                     from_relations=["p1"] + [f"p2_{j}" for j in range(1, level + 1)],
                     tag=f"partial line, n = {level}", text="true before any member is evaluated")
        _member_value(t, child, key)
        frame, cur, remaining = child, nxt, rest

    if past_the_end == "reuse":
        # Past the end, with no input: re-take i_g. The tail's address is a free string.
        t.reading(child, "case split misread: P2 applied to the empty set, taking i_g again", uses=["IS"],
                  binds="split_bad")
        t.deliver(child, "f_g")
        t.unknown(child, "C_x", "tail after the extra step", label="ENTRY", ref="P2", quote=P2_TAIL,
                  address="contribution(A | {} without i_g, t0, R)", unit="N")
        t.entry(child, "P2", P2_STEP, text="a step past the end", binds="p2_x", relation=f"{cur} = f_g + C_x", uses=["split_bad"])
        t.entry(child, "P3", P3, text="base case", binds="p3", relation="C_x = 0")
        t.derive(child, "C_x = 0", from_relations=["p3"], binds="C_x")
        t.derive(child, f"{cur} = -98/5", from_relations=["p2_x"], binds=cur)
    elif past_the_end == "invent":
        t.input(child, "rec_x", "recognition", "a further interaction i_x acts on A")
        t.unknown(child, "f_x", "impressed force of i_x on A", label="ENTRY", ref="P2", quote=P2_IF,
                  address="impressed-force(i_x -> A, t0, R)", unit="N", uses=["rec_x"])
        t.unknown(child, "C_x", "tail after i_x", label="ENTRY", ref="P2", quote=P2_TAIL,
                  address="contribution(A | {} without i_x, t0, R)", unit="N", uses=["rec_x"])
        t.entry(child, "P2", P2_STEP, text="a step past the end", binds="p2_x", relation=f"{cur} = f_x + C_x")

    # -- return up the recursion
    for lvl in range(level - 1, 0, -1):
        f = f"C{lvl}"
        cname = "C_0" if lvl == 1 else f"C_{lvl - 1}"
        if cname in t.values:
            continue
        missing = [n for n in t.bindings[f"p2_{lvl}"].equation.split("=")[1].replace("+", " ").split()
                   if n not in t.values]
        if missing:
            rep = t.solve(f, [f"p2_{j}" for j in range(lvl, level)] + (["p2_x"] if "p2_x" in t.bindings else []),
                          [n for n in ["C_0", "C_1", "C_2", "f_x", "C_x"] if n in t.bindings and n not in t.values],
                          text="what the relations fix once the expansion runs past the end")
            t.open(f, f"return blocked at {cname}: {', '.join(missing)} has no value; solve says: {rep.detail}")
            return t
        try:
            t.derive(f, f"{cname} = {frac_val(t, lvl)}", from_relations=[f"p2_{lvl}"], binds=cname,
                     tag="return")
        except TraceError as exc:
            t.open(f, f"return blocked: {exc}")
            return t
    t.derive(d11, f"F_A = {t.values['C_0']}", from_relations=["p1"], binds="F_A", tag="contribution law")
    t.entry(d1, "E8", E8, text="return through E8", binds="e8", relation="a_A = F_A / m_A", uses=["R_inertial"])
    t.derive(d1, f"a_A = {t.values['F_A'] / t.values['m_A']}", from_relations=["e8"], binds="a_A")
    t.answer(["a_A"], "A's inertial acceleration, upward positive")
    return t


def frac_val(t: Trace, lvl: int) -> Fraction:
    """The value C_{lvl-1} should take on return: its step relation's two summands."""
    rel = t.bindings[f"p2_{lvl}"].equation
    _, rhs = rel.split("=")
    a, b = [s.strip() for s in rhs.split("+")]
    return t.values[a] + t.values[b]


if __name__ == "__main__":
    t = build()
    print(t.to_markdown())
