#!/usr/bin/env python3
"""Regression corpus for normalize_math.py — one case per defect in the spec."""
import sys, subprocess, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from normalize_math import normalize, run_gates, skeleton, extract_spans

B = chr(92)
CASES = [
    # (id, defect, input, must_contain, must_not_contain)
    ("d2-space-stripped", "defect 2: \\( x \\) must not become '$ x $'",
     "the mass " + B + "( m " + B + ") is positive",
     ["the mass $m$ is positive"], ["$ m $"]),

    ("d3-inline-display", "defect 3: \\[ ... \\] on one line converts",
     "see " + B + "[ F = ma " + B + "] here",
     ["$$F = ma$$"], [B + "["]),

    ("d4-code-span", "defect 4: inline code spans untouched",
     "use `" + B + "(a" + B + ")` in source",
     ["`" + B + "(a" + B + ")`"], ["`$a$`"]),

    ("d5-fence-length", "defect 5: longer fence not closed by shorter",
     "````text\n```\n" + B + "( not math " + B + ")\n```\n````\n",
     [B + "( not math " + B + ")"], ["$not math$"]),

    ("d6-indented-code", "defect 6: 4-space indented code untouched",
     "text\n\n    " + B + "( also not math " + B + ")\n\nmore\n",
     ["    " + B + "( also not math " + B + ")"], ["$also not math$"]),

    ("d7-escapes", "defect 7: escaped delimiters survive",
     "literal " + B + B + "( backslash-paren " + B + B + ")",
     [B + B + "("], [B + "$"]),

    # expected to BLOCK: an unpaired delimiter must never be half-converted
    ("d8-unpaired", "defect 8: unpaired \\[ blocks with a clear diagnostic",
     "text\n\n" + B + "[\nE = mc^2\n\nmore text\n",
     [], [], "gate5-residual"),

    ("d9-currency", "defect 9: pre-existing $ escaped before new math",
     "costs $5 and mass " + B + "( m " + B + ") is given",
     [B + "$5", "$m$"], []),

    ("block-display", "\\[ / \\] alone on lines become $$",
     "text\n\n" + B + "[\nF = ma\n" + B + "]\n\nmore\n",
     ["$$\nF = ma\n$$"], [B + "["]),

    ("indent-preserved", "indentation of block display preserved",
     "- item\n\n  " + B + "[\n  F = ma\n  " + B + "]\n",
     ["  $$"], []),

    ("existing-math-untouched", "already-converted files are a no-op",
     "the mass $m$ and $$F=ma$$ stay\n",
     ["$m$", "$$F=ma$$"], [B + "$"]),

    ("fence-protected", "math inside a normal fence untouched",
     "```python\nx = r'" + B + "( a " + B + ")'\n```\n",
     [B + "( a " + B + ")"], []),
]

def render_ok(text):
    """Ask the real renderer whether the math spans render as math."""
    script = """
const md=require('markdown-it')().use(require('markdown-it-texmath'),
  {engine:require('katex'),delimiters:'dollars'});
let i='';process.stdin.on('data',d=>i+=d);
process.stdin.on('end',()=>{process.stdout.write(md.render(JSON.parse(i)));});
"""
    p = subprocess.run(["node","-e",script], input=json.dumps(text),
                       capture_output=True, text=True, env=ENV)
    return "katex" in p.stdout

import os
ENV = dict(os.environ, NODE_PATH="/tmp/t/node_modules")

def main():
    failed = 0
    print(f"{'case':28} {'gates':6} {'assert':7} result")
    print("-" * 78)
    for case in CASES:
        cid, desc, src, must, mustnt = case[:5]
        expect_block = case[5] if len(case) > 5 else None
        r = normalize(src)
        gates = run_gates(src, r, render_check=True)
        problems = []
        if expect_block:
            if not any(expect_block in g for g in gates):
                problems.append(f"expected block {expect_block!r}, got {gates or 'no gate failure'}")
        elif gates:
            problems += [f"GATE {g}" for g in gates]
        for m in must:
            if m not in r.text:
                problems.append(f"missing {m!r}")
        for m in mustnt:
            if m in r.text:
                problems.append(f"present {m!r}")
        status = "PASS" if not problems else "FAIL"
        if problems: failed += 1
        gate_col = "blocks" if expect_block else ("ok" if not gates else "FAIL")
        print(f"{cid:28} {gate_col:6} {'ok' if not problems else 'FAIL':7} {status}")
        for p in problems:
            print(f"    - {p}")

    # live-render assertions for the two silent defects
    print("\nlive KaTeX render checks (the two silent defects):")
    checks = [
        ("d2 output renders as math", normalize("mass " + B + "( m " + B + ") ok").text, True),
        ("old script output does NOT", "mass $ m $ ok", False),
    ]
    for name, text, expect in checks:
        got = render_ok(text)
        ok = got == expect
        if not ok: failed += 1
        print(f"  {name:34} -> {'MATH' if got else 'plain':5} {'PASS' if ok else 'FAIL'}")

    print(f"\n{len(CASES)+2} checks, {failed} failed")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
