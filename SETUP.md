# Setup — turning this folder into a git repo

Run these on **your own machine** (Windows), not inside Cowork. The scaffold (README, `.gitignore`, folders) is already in place; these commands put it under version control and back it up to GitHub.

## 1. Install the tools (one time)

- **Git for Windows** — https://git-scm.com/download/win
- **GitHub Desktop** (optional, easiest GUI) — https://desktop.github.com/
- A free **GitHub account** — https://github.com/signup

If you'd rather avoid the command line entirely, GitHub Desktop can do everything below with buttons. The commands are here for reference and speed.

## 2. Open a terminal in this folder

In File Explorer, navigate to the `VD folders` folder, right-click → **Open Git Bash here** (or use PowerShell).

## 3. Initialize and make the first commit

```bash
git init -b main
git config user.name "Can"
git config user.email "can.validk@gmail.com"

git add .
git commit -m "Initial structure: README, .gitignore, base folders"
```

## 4. Create the private GitHub repo and push

**Option A — GitHub website + commands:**
1. Go to https://github.com/new
2. Name it (e.g. `vd-documents`), set it to **Private**, and do NOT add a README (we already have one).
3. Copy the two commands GitHub shows under "push an existing repository", which look like:

```bash
git remote add origin https://github.com/<your-username>/vd-documents.git
git push -u origin main
```

**Option B — GitHub Desktop:** File → Add Local Repository → pick this folder → Publish repository → check **Keep this code private**.

## 5. Day-to-day use

After changing or adding files:

```bash
git add .
git commit -m "Describe what changed"
git push
```

Or just click **Commit** then **Push** in GitHub Desktop.

## Large files (only if needed)

Plain git is great for text, markdown, and code. If you later add big binaries (large scans, video, design files), install **Git LFS** (https://git-lfs.com) and run:

```bash
git lfs install
git lfs track "*.pdf" "*.png"   # example file types
git add .gitattributes
```

This keeps the repo fast and small.

---

### Note on Cowork
Cowork can read and edit the files in this folder and help you organize, rename, summarize, and draft documents. It cannot run `git` against this folder directly (the way the folder is mounted into Cowork's sandbox blocks git's internal file operations). So: **let Cowork handle the documents, and run the `git`/`push` steps yourself** with the commands above. Once it's on GitHub, you can also ask Cowork to help with anything that doesn't require git itself.
