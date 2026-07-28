# ⚠ ORIGINALS BANK — these files are NOT current

**Do not read, edit, or cite anything in this folder as if it were live.**

Every file here is a **pre-conversion snapshot** kept as a safety net by
`tools/normalize_math.py`. The live document is at the *same relative path
without the `_math_originals/<date>/` prefix*:

```text
_math_originals/2026-07-28/Newton/nml/nml2/nml2.1/NML2_1_CONTENT.md   <- snapshot, stale
Newton/nml/nml2/nml2.1/NML2_1_CONTENT.md                              <- the live file
```

## Why this folder is confusing, and how to tell

The paths here mirror the real tree exactly, so an open tab from this folder
looks identical to the real thing. **Check the path, not the filename.**

Snapshots still use the old LaTeX delimiters, so in a Markdown preview their
maths renders as literal brackets rather than as equations:

```text
in a snapshot:   [ \mathbf a(t)=\frac{\mathbf F(t)}{m}, ]      <- brackets, collapsed to one line
in the live file: renders as a proper centred equation
```

If you are seeing square brackets, stray commas where `\,` should be, or a
multi-line equation squashed onto one line, **you have opened a snapshot.**

## What to do with these

- **Recovering an original:** copy it back over the live file. It is the exact
  byte content from before conversion.
- **Applying an old patch:** a diff generated before conversion will not apply
  to the converted file. Patch the snapshot instead, then re-run
  `tools/normalize_math.py apply` on the result.
- **Checking what changed:** `MANIFEST.tsv` records, per file, the date, both
  SHA-256 hashes, the tool version, which rules fired, and any soft flags.

## Pruning

Nothing is pruned automatically. An entry may be removed only once the user has
confirmed the converted file renders correctly **and** the entry is more than 90
days old. Entries with unresolved soft flags are never auto-pruned.

See `tools/MATH_NORMALIZATION_SPEC.md` §2.2.
