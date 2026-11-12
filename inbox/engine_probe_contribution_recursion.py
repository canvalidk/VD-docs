"""Engine probe (scratch, 12 November 2026): can the VDfirst engine run the
one-definition contribution recursion?

Run from a checkout of canvalidk/VDfirst on branch codex/trace-workbench-record
(the engine with parameterized headwords and the prediction-set layer):

    python engine_probe_contribution_recursion.py

The entries below are scratch wording by Claude, written only to exercise the
engine. They are not dictionary entries. Member numbering starts at 0 so that
it matches the comparison 'count exceeds n'.
"""

import sys

sys.path.insert(0, ".")
from engine import VDInstance  # noqa: E402
from repl import REPL  # noqa: E402
from simulator import Simulator  # noqa: E402

BASE = [
    ("interaction-count_p", "the number of members in the numbered interaction list of p"),
    ("impressed-force_p_n", "the impressed force on p of the member numbered n"),
]
PLUS_ONE = ("if interaction-count_p exceeds n then impressed-force_p_n plus contribution_p_n+1 "
            "otherwise the zero vector")
SEPARATE = ("if interaction-count_p exceeds n then impressed-force_p_n plus contribution_p_m "
            "otherwise the zero vector where m is the number after n")
OFF = ["set reduce off", "set cleanup off"]


def drive(sim, inputs):
    out, it = [], iter(inputs)

    def input_fn(prompt):
        try:
            return next(it)
        except StopIteration as exc:
            raise EOFError from exc

    repl = REPL(sim, input_fn=input_fn, print_fn=lambda *a: out.append(" ".join(str(x) for x in a)))
    repl.run()
    return repl, out


def make(body, extra=()):
    vd = VDInstance("probe")
    vd.append_many(BASE + [("contribution_p_n", body)] + list(extra))
    return vd


def main():
    print("1. Is a self-referring entry accepted, and what does the dictionary graph see?")
    vd = make(SEPARATE)
    entry = vd.entries[-1]
    print("   appended. headwords recorded for the entry:", sorted(entry.hw_tokens))
    print("   graph edges:", sorted(vd.graph.edges()))
    print("   self-loop:", any(u == v for u, v in vd.graph.edges()), "| laws detected:", vd.detect_laws())

    print("\n2. Spelling the tail as contribution_p_n+1")
    repl, out = drive(Simulator(make(PLUS_ONE)), OFF + ["trace contribution_A_0", "expand", "expand 2", "expand 2"])
    for line in out[2:]:
        print("   ", line)
    print("    render:", repl.trace.active.definiens.render())

    print("\n3. Spelling the tail with a separate formal m")
    sim = Simulator(vd)
    repl, out = drive(sim, OFF + ["trace contribution_A_0", "expand"])
    print("    render:", repl.trace.active.definiens.render())
    repl, out = drive(sim, OFF + ["trace contribution_A_0", "expand", "flatten", "reduce",
                                  "impressed-force_A_0 plus contribution_A_1"])
    print("    rewrite by reduce:", next((line for line in out if "are headwords" in line), "accepted"))
    repl, out = drive(sim, OFF + ["trace contribution_A_0", "expand", "inject 2", "contribution_A_1", "expand"])
    print("    supply by inject, then expand:", repl.trace.active.definiens.render())

    print("\n4. Whole two-member run (count 2; forces 10 and -98/5 newtons)")
    cmds = OFF + ["trace contribution_A_0", "expand",
                  "expand 0", "reduce", "2",
                  "expand 1", "reduce", "10 newtons",
                  "inject 2", "contribution_A_1", "expand",
                  "expand 0", "reduce", "2",
                  "expand 1", "reduce", "-98/5 newtons",
                  "inject 2", "contribution_A_2", "expand",
                  "expand 0", "reduce", "2",
                  "flatten",
                  "reduce", "the zero vector, because 2 does not exceed 2",
                  "reduce", "the zero vector",
                  "reduce", "-98/5 newtons, because 2 exceeds 1",
                  "reduce", "-98/5 newtons",
                  "reduce", "-48/5 newtons, because 2 exceeds 0",
                  "reduce", "-48/5 newtons",
                  "state", "predictions"]
    repl, out = drive(sim, cmds)
    start = next(i for i, line in enumerate(out) if line.startswith("at: root") and i > 10)
    for line in out[start:]:
        print("   ", line[:260])

    print("\n5. Starting the recursion from a net-force entry")
    for label, body in [("direct call with actual 0", "haze_p plus contribution_p_0"),
                        ("'contribution_n where n is 0'", "haze_p plus contribution_p_n where n is 0")]:
        vd2 = make(SEPARATE, extra=[("haze_p", "the haze of p"), ("net-force_p", body)])
        repl, out = drive(Simulator(vd2), OFF + ["trace net-force_A", "expand"])
        print(f"    {label}: {repl.trace.active.definiens.render()}")


if __name__ == "__main__":
    main()
