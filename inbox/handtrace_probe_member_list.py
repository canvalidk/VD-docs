"""Probe (scratch, 12 November 2026): a member-named interaction list through the
contribution recursion, recorded with the hand-trace recorder.

Scene, one vertical axis, upward positive, instant t0:

    ceiling -- spring s1 -- block A -- spring s2 -- block B

s1 is carried by the ceiling; s2 is carried by A. Near-surface gravity acts on
both blocks. So the lists are

    A: (A_s1, R_s2, A_gA)      B: (A_s2, A_gB)

A_x is the action of acting-object x (it lands on x's other participant);
R_x is its reaction (it lands on x's carrier, and its value is the action's
value negated). P1-P3 restate the 11 November contribution-law rows; P4-P8 are
this probe's wording of member-named force laws after the 15 August addendum
(`action-force_spring`, `reaction-force_...`). None of P1-P8 is a dictionary
entry.

Numbers: k1 = 20 N/m, x1 = -1 m; k2 = 10 N/m, x2 = -1/2 m (each x is the signed
displacement of the spring's other participant from the relaxed position);
g = 49/5; m_A = 2 kg, m_B = 1 kg; haze 0.
Expected: K_s1 = 20, K_s2 = 5, a_A = (20 - 5 - 98/5)/2 = -23/10,
a_B = (5 - 49/5)/1 = -24/5.

    VD_ENTRIES=entries_with_scratch.md python handtrace_probe_member_list.py
"""

from __future__ import annotations

import itertools
import os
import sys
from pathlib import Path

from handtrace import ROOT, Trace, frac, load_entries

ENTRIES = Path(os.environ.get("VD_ENTRIES", "entries_with_scratch.md"))

E8 = "its net-force-material-object divided by its inertial-mass-material-object."
P1 = "its haze-material-object plus its contribution-material-object"
P2_STEP = ("the impressed-force of one member of that set on the material-object plus the "
           "contribution-material-object of the same set without that member")
P2_IF = "the impressed-force of one member"
P2_TAIL = "the contribution-material-object of the same set without that member"
P3 = "For one material-object and an empty remaining interaction-set, the zero vector."
P4 = "For a member that is the action of an acting-object, the action-force of that acting-object."
P5 = "For a member that is the reaction of an acting-object, the reaction-force of that acting-object."
P6 = "For one acting-object, the negative of its action-force."
P7 = ("the negative of its stiffness times the displacement of its other participant from the relaxed "
      "position along the declared axis")
P8 = ("the negative of the gravitational-mass of its other participant times the local field-strength "
      "along the upward axis")

# Acting-object instances: kind, carrier, other participant, and the inputs of its action law.
INSTANCES = {
    "s1": dict(kind="spring", carrier="the ceiling", other="A", k=("k1", 20), x=("x1", -1)),
    "s2": dict(kind="spring", carrier="A", other="B", k=("k2", 10), x=("x2", "-1/2")),
    "gA": dict(kind="gravity", carrier="the Earth", other="A", mu=("mu_A", 2)),
    "gB": dict(kind="gravity", carrier="the Earth", other="B", mu=("mu_B", 1)),
}
# Member lists: (role, instance). The order is the order the tracer takes them in.
LISTS = {"A": [("A", "s1"), ("R", "s2"), ("A", "gA")], "B": [("A", "s2"), ("A", "gB")]}
MASS = {"A": 2, "B": 1}


def tag(member) -> str:
    return f"{member[0]}_{member[1]}"


def show(members) -> str:
    return "(" + ", ".join(tag(m) for m in members) + ")"


def ensure(t: Trace, frame: str, name: str, text: str = "") -> None:
    """Deliver name into frame unless it (and its value, if it has one) is already visible there."""
    seen = t.visible(frame, name) is not None
    if seen and (name not in t.values or t.value_visible(frame, name) is not None):
        return
    t.deliver_through(frame, name, text=text)


def action_value(t: Trace, frame: str, inst: str) -> None:
    """Make K_<inst> (the instance's action-force) available with its value in frame.

    Computed once, from the instance's own state, wherever it is first demanded;
    any later use gets it by delivery."""
    name = f"K_{inst}"
    if name in t.values:
        ensure(t, frame, name, "the same action value, delivered, not computed again")
        return
    spec = INSTANCES[inst]
    d = t.demand(frame, f"{frame}.K", f"action-force({inst})", ref="P4" if True else "")
    ensure(t, d, name)
    if spec["kind"] == "spring":
        (kn, kv), (xn, xv) = spec["k"], spec["x"]
        t.input(d, kn, "value", f"stiffness of {inst}", value=kv, unit="N/m")
        t.input(d, xn, "value", f"signed displacement of {spec['other']} from {inst}'s relaxed position "
                "(negative: below it)", value=xv, unit="m")
        t.entry(d, "P7", P7, text=f"action-force_spring for {inst}", binds=f"law_{inst}",
                relation=f"{name} = -{kn}*{xn}", uses=[kn, xn])
    else:
        mn, mv = spec["mu"]
        ensure(t, d, "g")
        t.input(d, mn, "value", f"gravitational mass of {spec['other']}", value=mv, unit="kg")
        t.entry(d, "P8", P8, text=f"action-force_near-surface-gravity for {inst}", binds=f"law_{inst}",
                relation=f"{name} = -{mn}*g", uses=[mn, "g"])
    known = t.known_values(d)
    value = -known[spec["k"][0]] * known[spec["x"][0]] if spec["kind"] == "spring" else -known[spec["mu"][0]] * known["g"]
    t.derive(d, f"{name} = {frac(value)}", from_relations=[f"law_{inst}"], binds=name, tag=f"action value {inst}")


def member_value(t: Trace, frame: str, obj: str, member, f: str) -> None:
    """Evaluate one member's impressed force on obj: dispatch on the member's role."""
    role, inst = member
    d = t.demand(frame, f"{frame}.{tag(member)}", f"impressed-force({tag(member)} -> {obj}, t0, R)", ref="P2")
    t.deliver(d, f)
    if role == "A":
        t.reading(d, f"dispatch: {tag(member)} is the action of {inst}, so P4 applies", uses=[f"IS_{obj}"],
                  binds=f"disp_{obj}_{tag(member)}")
        action_value(t, d, inst)
        t.entry(d, "P4", P4, text="impressed force of an action member", binds=f"p4_{obj}_{inst}",
                relation=f"{f} = K_{inst}", uses=[f"disp_{obj}_{tag(member)}"])
        t.derive(d, f"{f} = {frac(t.values[f'K_{inst}'])}", from_relations=[f"p4_{obj}_{inst}"], binds=f,
                 tag=f"{tag(member)} on {obj}")
    else:
        t.reading(d, f"dispatch: {tag(member)} is the reaction of {inst}, so P5 applies", uses=[f"IS_{obj}"],
                  binds=f"disp_{obj}_{tag(member)}")
        t.unknown(d, f"Rf_{inst}", f"reaction-force of {inst} (lands on its carrier, {INSTANCES[inst]['carrier']})",
                  address=f"reaction-force({inst}, t0, R)", label="ENTRY", ref="P5", quote=P5, unit="N",
                  uses=[f"disp_{obj}_{tag(member)}"])
        action_value(t, d, inst)
        t.entry(d, "P6", P6, text="reaction by negation of the action", binds=f"p6_{inst}",
                relation=f"Rf_{inst} = -K_{inst}")
        t.derive(d, f"Rf_{inst} = {frac(-t.values[f'K_{inst}'])}", from_relations=[f"p6_{inst}"],
                 binds=f"Rf_{inst}", tag=f"reaction value {inst}")
        t.entry(d, "P5", P5, text="impressed force of a reaction member", binds=f"p5_{obj}_{inst}",
                relation=f"{f} = Rf_{inst}", uses=[f"disp_{obj}_{tag(member)}"])
        t.derive(d, f"{f} = {frac(t.values[f'Rf_{inst}'])}", from_relations=[f"p5_{obj}_{inst}"], binds=f,
                 tag=f"{tag(member)} on {obj}")


def account(t: Trace, obj: str, members) -> None:
    """E8 for obj: net force by the contribution law and the Force-Sum recursion over members."""
    d1 = t.demand(ROOT, f"D{obj}", f"inertial-acceleration-material-object({obj}, t0, R)")
    t.deliver_many(d1, ["q_norm", "R_inertial", f"H_{obj}", f"a_{obj}"])
    dF = t.demand(d1, f"D{obj}.F", f"E8: demand net-force-material-object({obj}, t0, R)", ref="E8")
    dm = t.demand(d1, f"D{obj}.m", f"E8: demand inertial-mass-material-object({obj})", ref="E8")
    t.input(dm, f"m_{obj}", "value", f"inertial mass of {obj}, supplied independently", value=MASS[obj], unit="kg")
    t.deliver_through(dF, f"F_{obj}")
    t.deliver_through(dF, f"IS_{obj}")
    t.unknown(dF, f"C_{obj}0", f"contribution of {obj}'s whole list", address=f"contribution({obj} | {show(members)})",
              label="ENTRY", ref="P1", quote=P1, unit="N")
    t.entry(dF, "P1", P1, text="the contribution law, net-force corner", binds=f"p1_{obj}",
            relation=f"F_{obj} = H_{obj} + C_{obj}0", uses=[f"H_{obj}"])
    frame, cur, remaining, level = dF, f"C_{obj}0", list(members), 0
    steps = []
    while True:
        level += 1
        child = t.demand(frame, f"C{obj}{level}", f"contribution({obj} | {show(remaining)})",
                         ref="P1" if level == 1 else "P2")
        t.deliver(child, cur)
        if not remaining:
            t.reading(child, "case split: the remaining list is empty, so P3 applies", uses=[f"IS_{obj}"],
                      binds=f"split_{obj}{level}")
            t.entry(child, "P3", P3, text="base case", binds=f"p3_{obj}", relation=f"{cur} = 0",
                    uses=[f"split_{obj}{level}"])
            t.derive(child, f"{cur} = 0", from_relations=[f"p3_{obj}"], binds=cur, tag="base case")
            break
        member, rest = remaining[0], remaining[1:]
        f, nxt = f"f_{obj}_{tag(member)}", f"C_{obj}{level}"
        t.reading(child, "case split: the remaining list is not empty, so P2 applies", uses=[f"IS_{obj}"],
                  binds=f"split_{obj}{level}")
        t.input(child, f"pick_{obj}{level}", "choice", f"take {tag(member)} as the member at this step")
        t.unknown(child, f, f"impressed force of {tag(member)} on {obj}", label="ENTRY", ref="P2", quote=P2_IF,
                  address=f"impressed-force({tag(member)} -> {obj}, t0, R)", unit="N", uses=[f"pick_{obj}{level}"])
        t.unknown(child, nxt, "contribution of the remaining list", label="ENTRY", ref="P2", quote=P2_TAIL,
                  address=f"contribution({obj} | {show(rest)})", unit="N", uses=[f"pick_{obj}{level}"])
        t.reading(child, f"the remaining list without {tag(member)} is {show(rest)}",
                  uses=[f"IS_{obj}", f"pick_{obj}{level}"], binds=f"rest_{obj}{level}")
        t.entry(child, "P2", P2_STEP, text="the Force-Sum step", binds=f"p2_{obj}{level}",
                relation=f"{cur} = {f} + {nxt}",
                uses=[f"split_{obj}{level}", f"pick_{obj}{level}", f"rest_{obj}{level}"])
        member_value(t, child, obj, member, f)
        steps.append((child, cur, f, nxt, level))
        frame, cur, remaining = child, nxt, rest
    for child, cur, f, nxt, lvl in reversed(steps):
        t.derive(child, f"{cur} = {frac(t.values[f] + t.values[nxt])}", from_relations=[f"p2_{obj}{lvl}"],
                 binds=cur, tag="return")
    t.derive(dF, f"F_{obj} = {frac(t.values[f'H_{obj}'] + t.values[f'C_{obj}0'])}", from_relations=[f"p1_{obj}"],
             binds=f"F_{obj}", tag="contribution law")
    t.entry(d1, "E8", E8, text="return through E8", binds=f"e8_{obj}", relation=f"a_{obj} = F_{obj} / m_{obj}",
            uses=["R_inertial"])
    t.derive(d1, f"a_{obj} = {frac(t.values[f'F_{obj}'] / t.values[f'm_{obj}'])}", from_relations=[f"e8_{obj}"],
             binds=f"a_{obj}")


def build(order_a=None, order_b=None, *, both_members_of_s2_on_a: bool = False) -> Trace:
    entries = load_entries(str(ENTRIES)) if ENTRIES.exists() else None
    t = Trace("What are the inertial accelerations of A and B at t0?",
              {"dictionary": "Design 2.1 Draft 1 + scratch P1-P8 (probe wording, not entries)",
               "member names": "after the 15 August 2026 addendum: action-force_kind / reaction-force_kind"},
              entries=entries)
    la = list(order_a or LISTS["A"])
    lb = list(order_b or LISTS["B"])
    if both_members_of_s2_on_a:
        la = la + [("A", "s2")]

    t.input(ROOT, "q_norm", "normalization", "the question asks for inertial-acceleration-material-object of A and of B at t0 in R")
    t.input(ROOT, "R_inertial", "model", "R is a supplied inertial frame")
    t.input(ROOT, "axis", "convention", "one vertical axis, upward positive")
    t.input(ROOT, "g", "value", "local field-strength, the same at A and at B", value="49/5", unit="m/s^2")
    for obj in "AB":
        t.input(ROOT, f"H_{obj}", "haze", f"haze-material-object({obj}, t0) = 0", value=0, unit="N")
    # Recognitions name each acting-object instance with its carrier. One recognition of s2
    # puts a member in two lists: its action in B's, its reaction in A's.
    t.input(ROOT, "rec_s1", "recognition", "spring s1 is carried by the ceiling and attached to A; intact, Hookean")
    t.input(ROOT, "rec_s2", "recognition", "spring s2 is carried by A and attached to B; intact, Hookean")
    t.input(ROOT, "rec_gA", "recognition", "A is in the Earth's near-surface field")
    t.input(ROOT, "rec_gB", "recognition", "B is in the Earth's near-surface field")
    t.input(ROOT, "closed_A", "completeness", "no more members to be added to A's list at this tolerance",
            uses=["rec_s1", "rec_s2", "rec_gA", "H_A"])
    t.input(ROOT, "closed_B", "completeness", "no more members to be added to B's list at this tolerance",
            uses=["rec_s2", "rec_gB", "H_B"])
    t.reading(ROOT, f"interaction-set(A, t0) = {show(la)}: an instance gives its action to its other "
              "participant and its reaction to its carrier", binds="IS_A",
              uses=["rec_s1", "rec_s2", "rec_gA", "closed_A"])
    t.reading(ROOT, f"interaction-set(B, t0) = {show(lb)}", binds="IS_B", uses=["rec_s2", "rec_gB", "closed_B"])
    # One addressed quantity per instance action, per net force and per acceleration.
    for inst, spec in INSTANCES.items():
        law, quote = ("P7", P7) if spec["kind"] == "spring" else ("P8", P8)
        t.unknown(ROOT, f"K_{inst}", f"action-force of {inst} (lands on {spec['other']})",
                  address=f"action-force({inst}, t0, R)", label="ENTRY", ref=law, quote=quote, unit="N",
                  uses=[f"rec_{inst}"])
    for obj in "AB":
        t.unknown(ROOT, f"a_{obj}", f"the demanded inertial acceleration of {obj}",
                  address=f"inertial-acceleration({obj}, t0, R)", label="ENTRY", ref="E8", quote=E8,
                  unit="m/s^2", uses=["q_norm"])
        t.unknown(ROOT, f"F_{obj}", f"net force on {obj}", address=f"net-force({obj}, t0, R)", label="ENTRY",
                  ref="E8", quote=E8, unit="N")
    account(t, "A", la)
    t.answer(["a_A"], "A's inertial acceleration, upward positive", label="A")
    account(t, "B", lb)
    t.answer(["a_B"], "B's inertial acceleration, upward positive", label="B")
    # The system total, to see what the pair does to it.
    t.unknown(ROOT, "F_sys", "net force on the system {A, B}", address="net-force({A, B}, t0, R)",
              label="READING", unit="N")
    t.reading(ROOT, "the system's net force is the sum of its members' net forces", binds="sys",
              relation="F_sys = F_A + F_B")
    t.derive(ROOT, f"F_sys = {frac(t.values['F_A'] + t.values['F_B'])}", from_relations=["sys"], binds="F_sys")
    t.answer(["F_sys"], "net force on the two blocks together", label="sys")
    return t


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    t = build()
    if "--markdown" in sys.argv:
        print(t.to_markdown())
        raise SystemExit
    print("answers:", {lb: t.steps[i].detail for lb, i in t.answers})
    print("steps:", len(t.steps))
    for lb in ("A", "B", "sys"):
        led = t.ledger(lb)
        kinds = {}
        for row in led["theory"]:
            kinds[row["op"]] = kinds.get(row["op"], 0) + 1
        print(f"\n[{lb}] members: {[c['name'] for c in led['commitments']]}")
        print(f"[{lb}] theory side: {kinds}; step members: {len(led['step_members'])}; "
              f"conflicts: {len(led['conflicts'])}; warnings other than missing statuses: "
              f"{[w for w in led['warnings'] if 'no status yet' not in w]}")
    print("\n-- every order of A's list gives the same answer")
    seen = set()
    for perm in itertools.permutations(LISTS["A"]):
        seen.add(build(order_a=perm).values["a_A"])
    print("a_A over 6 orders:", sorted(frac(v) for v in seen))
    print("\n-- what the spring between the blocks is needed for (x2 removed, then changed)")
    for lb in ("A", "B", "sys"):
        removed = t.check_countermodel("x2", answer=lb, remove=["x2"])
        changed = t.check_countermodel("x2", answer=lb, replace={"x2": -1})
        print(f"[{lb}] x2 removed: {removed['summary']} | x2 = -1: {changed['summary']}")
    print("\n-- both members of s2 put in A's list (the exclusivity the list is supposed to respect)")
    try:
        bad = build(both_members_of_s2_on_a=True)
        print("accepted; a_A =", frac(bad.values["a_A"]), "| warnings:",
              [w for w in bad.ledger("A")["warnings"] if "no status yet" not in w])
    except Exception as exc:  # noqa: BLE001 - report whatever the recorder says
        print("refused:", type(exc).__name__, exc)
