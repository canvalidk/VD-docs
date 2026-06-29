# VD — Valid Dictionary

Version-controlled home for the VD project. Each top-level folder is a **branch** of the project — tied to a publishing strategy and (currently) to its own Claude AI project.

## Branches

| Folder | What it's for |
|--------|----------------|
| `Core/` | The VD as a rigorous set of mathematical rules, presented *without* justification. (First in line.) |
| `Theory/` | Philosophical writing justifying the VD's core commitments. |
| `Newton/` | Bridges Newton-analysis and Code — the "program" that runs on the Code "compiler". |
| `Newton-analysis/` | Justifies the VD via the analyses it produces — the program's "output". |
| `inbox/` | Staging area. Currently holds `VD unsorted important/`, to be sorted into the branches later. |

**Code branch** — implementation of the VD as a codebase/application. Lives in its own repository: https://github.com/canvalidk/VDfirst . Whether/how to integrate it here is still being decided.

The compiler analogy: **Code** = compiler, **Newton-analysis** = the program's output, **Newton** = the program that runs on the compiler.

## Note on duplicate files

Some files appear in more than one branch folder **on purpose**: each branch's AI project needs context from other branches, so documents are copied in. Don't dedupe these without checking which projects rely on them.

Caveat: git does **not** keep copies in sync — editing one copy won't update the others. A future cleanup could keep one canonical copy plus a small sync step.

## Bac