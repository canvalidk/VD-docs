# VD — Valid Dictionary

Version-controlled home for the VD project. Each top-level folder is a **branch** of the project — tied to a publishing strategy and (currently) to its own Claude AI project.

## Branches

| Folder | What it's for |
|--------|----------------|
| `Core/` | The VD as a rigorous set of mathematical rules, presented *without* justification. (First in line.) |
| `Theory/` | Philosophical writing justifying the VD's core commitments. |
| `Code/` | The VD as a codebase/application — but only the spec/management layer (specs, design notes, requirements). Links the code repo; does not hold the code itself. |
| `Newton/` | Bridges Newton-analysis and Code — the "program" that runs on the Code "compiler". |
| `Newton-analysis/` | Justifies the VD via the analyses it produces — the program's "output". |
| `inbox/` | Staging area. Currently holds `VD unsorted important/`, to be sorted into the branches later. |

**Code branch** — the Code branch lives in this repo as the spec/management layer for the VD codebase: it holds the specs, design notes, and requirements the code must satisfy (e.g. under `Code/specs/`). The actual code lives in its own repository, https://github.com/canvalidk/VDfirst , which is *responsible for* the code (the source of truth); the Code branch *links to* it. Context copies of code may live under `Code/` when useful, but VDfirst — not this repo — owns and maintains the code. Rule of thumb: don't manage or edit the code here; everything the code has to satisfy that isn't code is managed in `Code/`.

The compiler analogy: **Code** = compiler, **Newton-analysis** = the program's 