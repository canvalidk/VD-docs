# VD Documents

A version-controlled home for my documents. Git gives me automatic history (every change is saved and reversible), so I no longer need manual backups, and it makes sharing and collaborating on these files easy.

## Folder structure

| Folder | What goes here |
|--------|----------------|
| `documents/` | Finished/reference documents, organized by topic in subfolders. |
| `notes/` | Working notes, drafts, and markdown jottings. |
| `projects/` | Anything tied to a specific project or piece of work. |
| `archive/` | Old material kept for reference but no longer active. |
| `inbox/` | Temporary landing zone for new files before they're sorted. |

Adjust these to fit how you actually think about your documents — this is just a starting point.

## How I use it

- **Save a change ("commit"):** group related edits and record them with a short message describing what changed.
- **History:** every commit is recoverable, so nothing is ever truly lost.
- **Backup:** the repo is mirrored to a private GitHub repository (see `SETUP.md`).
- **Sharing:** I can share the whole repo or hand someone a single file.

## What does NOT belong here

- Passwords, API keys, or other secrets (see `.gitignore`).
- Very large binary files (big media, scans, archives). If I need those, I'll use Git LFS — see `SETUP.md`.

## Conventions

- Use clear, lowercase file and folder names; prefer hyphens over spaces (`tax-2025.md`, not `Tax 2025.md`).
- Write a meaningful commit message: `Add Q2 invoice`, not `update`.
