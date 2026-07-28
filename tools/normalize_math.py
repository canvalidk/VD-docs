#!/usr/bin/env python3
"""Normalize LaTeX math delimiters in AI-authored Markdown for VS Code (KaTeX).

NARROW SCOPE (see tools/MATH_NORMALIZATION_SPEC.md): this converts math
delimiters only. It is not a general Markdown formatter or linter.

Conversions, applied only outside protected regions:
    literal $        ->  \\$        (escape-literal-dollar)
    \\( ... \\)      ->  $...$      (inline-delim; interior whitespace stripped)
    \\[ / \\] alone  ->  $$ / $$    (display-delim-block)
    \\[ ... \\]      ->  $$...$$    (display-delim-inline)

Protected regions are never touched: fenced code (length-aware), indented code,
inline code spans, backslash escapes, existing $/$$ math, HTML comments, front
matter.

Every edit is journalled, and the journal is replayed backwards to prove the
output can be turned back into the input byte-for-byte before anything is
written. Four hard gates must pass or nothing is written.

Usage:
    normalize_math.py check  FILE...        # report only, never writes
    normalize_math.py apply  FILE... [--bank DIR] [--no-render-check]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

TOOL_VERSION = "1.0.0"

BACKSLASH = chr(92)
DOLLAR = "$"
OPEN_INLINE = BACKSLASH + "("
CLOSE_INLINE = BACKSLASH + ")"
OPEN_DISPLAY = BACKSLASH + "["
CLOSE_DISPLAY = BACKSLASH + "]"

FENCE_RE = re.compile(r"^([ ]{0,3})(`{3,}|~{3,})(.*)$")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


# --------------------------------------------------------------------------
# journal
# --------------------------------------------------------------------------
@dataclass
class Edit:
    in_offset: int
    out_offset: int
    before: str
    after: str
    rule: str

    def as_dict(self) -> dict:
        return {
            "in_offset": self.in_offset,
            "out_offset": self.out_offset,
            "before": self.before,
            "after": self.after,
            "rule": self.rule,
        }


@dataclass
class Result:
    text: str
    journal: list[Edit] = field(default_factory=list)
    flags: list[str] = field(default_factory=list)

    @property
    def changed(self) -> bool:
        return bool(self.journal)


# --------------------------------------------------------------------------
# protected regions
# --------------------------------------------------------------------------
def _line_spans(text: str) -> list[tuple[int, int, str]]:
    spans, pos = [], 0
    for line in text.splitlines(keepends=True):
        spans.append((pos, pos + len(line), line))
        pos += len(line)
    return spans


def _block_protected(text: str) -> list[tuple[int, int]]:
    """Line-structural protected regions: front matter, fenced code, indented
    code, HTML comments."""
    out: list[tuple[int, int]] = []
    lines = _line_spans(text)

    # front matter
    i = 0
    if lines and lines[0][2].rstrip("\n") == "---":
        for j in range(1, len(lines)):
            if lines[j][2].rstrip("\n") in ("---", "..."):
                out.append((lines[0][0], lines[j][1]))
                i = j + 1
                break

    fence: tuple[str, int] | None = None   # (char, length)
    fence_start = 0
    prev_blank = True
    indent_start: int | None = None

    while i < len(lines):
        start, end, line = lines[i]
        stripped = line.rstrip("\n")
        match = FENCE_RE.match(stripped)

        if fence is not None:
            # inside a fence: only a >= length fence of the same char closes it
            if match:
                char, marker = match.group(2)[0], match.group(2)
                if char == fence[0] and len(marker) >= fence[1] and not match.group(3).strip():
                    out.append((fence_start, end))
                    fence = None
            i += 1
            continue

        if indent_start is not None:
            if stripped.strip() == "" or line.startswith("    ") or line.startswith("\t"):
                i += 1
                continue
            out.append((indent_start, start))
            indent_start = None

        if match:
            fence = (match.group(2)[0], len(match.group(2)))
            fence_start = start
            i += 1
            continue

        # indented code block: >=4 spaces (or tab) opening after a blank line
        if prev_blank and stripped.strip() and (line.startswith("    ") or line.startswith("\t")):
            indent_start = start
            i += 1
            prev_blank = False
            continue

        prev_blank = stripped.strip() == ""
        i += 1

    if fence is not None:
        out.append((fence_start, len(text)))
    if indent_start is not None:
        out.append((indent_start, len(text)))

    for m in HTML_COMMENT_RE.finditer(text):
        out.append((m.start(), m.end()))

    return out


def _inline_protected(text: str, blocked: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Char-level protected regions outside the block regions: backslash
    escapes, inline code spans, and math already in $ / $$ form."""
    def in_block(p: int) -> bool:
        return any(a <= p < b for a, b in blocked)

    out: list[tuple[int, int]] = []
    i, n = 0, len(text)
    while i < n:
        if in_block(i):
            i += 1
            continue
        ch = text[i]

        # backslash escape: protect the pair
        if ch == BACKSLASH and i + 1 < n:
            nxt = text[i + 1]
            if nxt in (BACKSLASH, DOLLAR) or (nxt == BACKSLASH):
                out.append((i, i + 2))
                i += 2
                continue
            # \\( and \\[ are handled as rules, not escapes; a doubled
            # backslash before them was caught above.

        # inline code span
        if ch == "`":
            run = len(text[i:]) - len(text[i:].lstrip("`"))
            close = text.find("`" * run, i + run)
            while close != -1 and close + run < n and text[close + run] == "`":
                close = text.find("`" * run, close + run + 1)
            if close != -1:
                out.append((i, close + run))
                i = close + run
                continue

        # existing display math
        if text.startswith("$$", i):
            close = text.find("$$", i + 2)
            if close != -1:
                out.append((i, close + 2))
                i = close + 2
                continue

        # existing inline math: $x$ with no space adjacent to the delimiters
        if ch == DOLLAR and i + 1 < n and not text[i + 1].isspace():
            j = i + 1
            while j < n and text[j] != DOLLAR:
                if text[j] == "\n" and j + 1 < n and text[j + 1] == "\n":
                    break
                j += 1
            if j < n and text[j] == DOLLAR and not text[j - 1].isspace() and j > i + 1:
                out.append((i, j + 1))
                i = j + 1
                continue

        i += 1
    return out


def protected_regions(text: str) -> list[tuple[int, int]]:
    blocked = _block_protected(text)
    regions = blocked + _inline_protected(text, blocked)
    regions.sort()
    merged: list[tuple[int, int]] = []
    for a, b in regions:
        if merged and a <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else:
            merged.append((a, b))
    return merged


# --------------------------------------------------------------------------
# conversion
# --------------------------------------------------------------------------
def normalize(text: str) -> Result:
    regions = protected_regions(text)
    prot = {}
    for a, b in regions:
        prot[a] = b

    # preflight: if delimiters are unbalanced outside protected regions, do not
    # apply that rule family at all -- a lone converted delimiter corrupts every
    # block after it (defect 8). Flag it and let gate 5 block the file.
    unprot = _unprotected_text(text, regions)
    skip_display = unprot.count(OPEN_DISPLAY) != unprot.count(CLOSE_DISPLAY)
    skip_inline = unprot.count(OPEN_INLINE) != unprot.count(CLOSE_INLINE)

    out_parts: list[str] = []
    journal: list[Edit] = []
    flags: list[str] = []
    out_len = 0
    i, n = 0, len(text)
    line_start = 0
    dollar_count = 0

    def emit(s: str) -> None:
        nonlocal out_len
        out_parts.append(s)
        out_len += len(s)

    def record(in_off: int, before: str, after: str, rule: str) -> None:
        journal.append(Edit(in_off, out_len, before, after, rule))
        emit(after)

    while i < n:
        if i in prot:
            end = prot[i]
            emit(text[i:end])
            if "\n" in text[i:end]:
                line_start = i + text[i:end].rfind("\n") + 1
            i = end
            continue

        ch = text[i]
        if ch == "\n":
            emit(ch)
            i += 1
            line_start = i
            continue

        # rule: display-delim-block  (\[ or \] alone on a line)
        if not skip_display and (text.startswith(OPEN_DISPLAY, i)
                                 or text.startswith(CLOSE_DISPLAY, i)):
            eol = text.find("\n", i)
            eol = n if eol == -1 else eol
            before_txt = text[line_start:i]
            after_txt = text[i + 2:eol]
            if not before_txt.strip() and not after_txt.strip():
                record(i, text[i:i + 2], "$$", "display-delim-block")
                i += 2
                continue

        # rule: display-delim-inline  (\[ ... \] within a line)
        if not skip_display and text.startswith(OPEN_DISPLAY, i):
            close = text.find(CLOSE_DISPLAY, i + 2)
            if close != -1:
                inner = text[i + 2:close]
                if not _crosses_protection(i, close + 2, regions):
                    record(i, text[i:close + 2], "$$" + inner.strip() + "$$",
                           "display-delim-inline")
                    flags.append("display-math-inline")
                    i = close + 2
                    continue
            else:
                flags.append("unpaired-display-open")

        # rule: inline-delim  (\( ... \))
        if not skip_inline and text.startswith(OPEN_INLINE, i):
            close = text.find(CLOSE_INLINE, i + 2)
            if close != -1:
                inner = text[i + 2:close]
                if not _crosses_protection(i, close + 2, regions):
                    stripped = inner.strip()
                    if not stripped:
                        flags.append("empty-math-span")
                    record(i, text[i:close + 2], DOLLAR + stripped + DOLLAR,
                           "inline-delim")
                    i = close + 2
                    continue
            else:
                flags.append("unpaired-inline-open")

        # rule: escape-literal-dollar
        if ch == DOLLAR:
            record(i, DOLLAR, BACKSLASH + DOLLAR, "escape-literal-dollar")
            dollar_count += 1
            i += 1
            continue

        emit(ch)
        i += 1

    if skip_display:
        flags.append("unbalanced-display-delimiters")
    if skip_inline:
        flags.append("unbalanced-inline-delimiters")
    if dollar_count:
        flags.append(f"literal-dollars-escaped:{dollar_count}")

    styles = set()
    if OPEN_INLINE in text or OPEN_DISPLAY in text:
        styles.add("latex")
    if re.search(r"(?<!\\)\$", text):
        styles.add("dollar")
    if len(styles) > 1:
        flags.append("mixed-delimiter-styles")

    return Result("".join(out_parts), journal, sorted(set(flags)))


def _unprotected_text(text: str, regions: list[tuple[int, int]]) -> str:
    parts, pos = [], 0
    for a, b in regions:
        parts.append(text[pos:a])
        pos = b
    parts.append(text[pos:])
    return "".join(parts)


def _crosses_protection(a: int, b: int, regions: list[tuple[int, int]]) -> bool:
    return any(a < rb and ra < b for ra, rb in regions)


# --------------------------------------------------------------------------
# gates
# --------------------------------------------------------------------------
def replay_reverse(output: str, journal: list[Edit]) -> str:
    text = output
    for edit in sorted(journal, key=lambda e: e.out_offset, reverse=True):
        start = edit.out_offset
        end = start + len(edit.after)
        if text[start:end] != edit.after:
            raise ValueError(f"journal desync at {start}: {text[start:end]!r}")
        text = text[:start] + edit.before + text[end:]
    return text


MATH_SPAN_RE = re.compile(
    r"\$\$.*?\$\$|(?<!\\)\$[^$\n]+?(?<!\\)\$"
    r"|" + re.escape(OPEN_DISPLAY) + r".*?" + re.escape(CLOSE_DISPLAY) +
    r"|" + re.escape(OPEN_INLINE) + r".*?" + re.escape(CLOSE_INLINE),
    re.DOTALL,
)


def skeleton(text: str) -> str:
    """Document with every math span collapsed and \\$ unescaped, so the
    non-math remainder can be compared across the transform."""
    masked = MATH_SPAN_RE.sub("\x00MATH\x00", text)
    return masked.replace(BACKSLASH + DOLLAR, DOLLAR)


def extract_spans(text: str) -> list[tuple[str, bool]]:
    spans = []
    for m in re.finditer(r"\$\$(.+?)\$\$|(?<!\\)\$([^$\n]+?)(?<!\\)\$", text, re.DOTALL):
        if m.group(1) is not None:
            spans.append((m.group(1), True))
        else:
            spans.append((m.group(2), False))
    return spans


def katex_check(spans: list[tuple[str, bool]]) -> tuple[bool, list[str]]:
    if not spans:
        return True, []
    script = """
const katex = require('katex');
let input = '';
process.stdin.on('data', d => input += d);
process.stdin.on('end', () => {
  const spans = JSON.parse(input);
  const errs = [];
  spans.forEach(([src, display], idx) => {
    try { katex.renderToString(src, {displayMode: display, throwOnError: true}); }
    catch (e) { errs.push(idx + ': ' + e.message.split('\\n')[0]); }
  });
  process.stdout.write(JSON.stringify(errs));
});
"""
    try:
        proc = subprocess.run(
            ["node", "-e", script],
            input=json.dumps(spans),
            capture_output=True, text=True, timeout=120,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False, ["__unavailable__"]
    if proc.returncode != 0:
        return False, ["__unavailable__"]
    return True, json.loads(proc.stdout or "[]")


def run_gates(source: str, result: Result, render_check: bool) -> list[str]:
    failures: list[str] = []

    try:
        if replay_reverse(result.text, result.journal) != source:
            failures.append("gate1-roundtrip: reverse replay did not reproduce input")
    except ValueError as exc:
        failures.append(f"gate1-roundtrip: {exc}")

    if render_check:
        ok, errs = katex_check(extract_spans(result.text))
        if not ok:
            failures.append(
                "gate2-parse: node/katex unavailable "
                "(install, or pass --no-render-check to accept a weaker check)"
            )
        elif errs:
            failures.append("gate2-parse: " + "; ".join(errs[:5]))
    else:
        text = result.text
        if text.count("$$") % 2:
            failures.append("gate2-parse(weak): odd number of $$ delimiters")

    if skeleton(source) != skeleton(result.text):
        failures.append("gate3-skeleton: non-math content changed")

    residual = _unprotected_text(result.text, protected_regions(result.text))
    leftover = []
    if OPEN_INLINE in residual or CLOSE_INLINE in residual:
        leftover.append(OPEN_INLINE + " ... " + CLOSE_INLINE)
    if OPEN_DISPLAY in residual or CLOSE_DISPLAY in residual:
        leftover.append(OPEN_DISPLAY + " ... " + CLOSE_DISPLAY)
    if leftover:
        failures.append(
            "gate5-residual: unconverted delimiters remain outside code ("
            + ", ".join(leftover)
            + ") -- usually an unpaired delimiter in the source; fix it and re-run"
        )

    second = normalize(result.text)
    if second.changed:
        failures.append(
            f"gate4-idempotence: re-running produced {len(second.journal)} more edits"
        )

    return failures


# --------------------------------------------------------------------------
# bank + cli
# --------------------------------------------------------------------------
def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def bank_original(bank_root: Path, source_path: Path, repo_root: Path,
                  text: str) -> Path:
    try:
        rel = source_path.resolve().relative_to(repo_root.resolve())
    except ValueError:
        rel = Path(source_path.name)
    dest = bank_root / date.today().isoformat() / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    return dest


def append_manifest(bank_root: Path, row: list[str]) -> None:
    manifest = bank_root / "MANIFEST.tsv"
    header = ("date\toriginal_path\tfinal_path\tsha256_before\tsha256_after"
              "\ttool_version\trules_applied\tflags\n")
    bank_root.mkdir(parents=True, exist_ok=True)
    if not manifest.exists():
        manifest.write_text(header, encoding="utf-8")
    with manifest.open("a", encoding="utf-8") as handle:
        handle.write("\t".join(row) + "\n")


def process(path: Path, args: argparse.Namespace) -> int:
    source = path.read_text(encoding="utf-8")
    result = normalize(source)

    if not result.changed:
        print(f"  {path}: no math delimiters to convert")
        return 0

    failures = run_gates(source, result, render_check=not args.no_render_check)
    rules = sorted({e.rule for e in result.journal})

    print(f"  {path}: {len(result.journal)} edits [{', '.join(rules)}]")
    if result.flags:
        print(f"    flags: {', '.join(result.flags)}")

    if failures:
        print("    BLOCKED — nothing written:")
        for failure in failures:
            print(f"      - {failure}")
        return 1

    if args.command == "check":
        print("    all gates pass (check mode; not written)")
        return 0

    bank_root = Path(args.bank)
    banked = bank_original(bank_root, path, Path(args.repo_root), source)
    path.write_text(result.text, encoding="utf-8")
    append_manifest(bank_root, [
        date.today().isoformat(), str(path), str(path),
        sha256(source), sha256(result.text), TOOL_VERSION,
        ",".join(rules), ",".join(result.flags) or "-",
    ])
    print(f"    written; original banked at {banked}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["check", "apply"])
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--bank", default="_math_originals")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--no-render-check", action="store_true",
                        help="skip the KaTeX parse gate (weaker balance check instead)")
    args = parser.parse_args()

    print(f"normalize_math {TOOL_VERSION} — {args.command}")
    worst = 0
    for path in args.files:
        if not path.exists():
            print(f"  {path}: NOT FOUND")
            worst = 1
            continue
        worst = max(worst, process(path, args))
    return worst


if __name__ == "__main__":
    raise SystemExit(main())
