---
tags: [meta]
---
# Setup

## Obsidian

1. Obsidian → **Open folder as vault** → point it at this folder.
2. Settings → **Appearance → CSS snippets** → refresh → enable `cael-callout`. This gives the Cael margin notes a mask icon and grey italic styling. Without it they still render fine, just plainly.
3. Optional plugins, in order of usefulness here:
   - **Dataview** — turns the dashboards into live queries instead of hand-maintained lists.
   - **Templater** — hotkey the files in `08 Templates`.
   - **Excalidraw** — for the faction/relationship map when it gets complicated.

### Optional: live dashboards

With Dataview installed, this in a note gives you every open thread automatically:

```dataview
TABLE status, first_seen
FROM #npc OR #faction
WHERE status = "active"
SORT file.name ASC
```

Keep the hand-written [[Dashboard]] anyway. Queries list things; a dashboard says what matters.

## Git

```bash
cd "path/to/this/vault"
git init
git add .
git commit -m "Vault: sessions 0.5 through 3"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

A `.gitignore` is already in place for Obsidian's workspace files, so you won't get a diff every time you move a pane.

Working alone, commit after each session. If the other players get write access, one branch per session and merge after — Obsidian has no locking and two people editing `Dashboard.md` at once will conflict.

**Obsidian Git** (community plugin) will auto-commit and sync on a timer, including on mobile. That is the setup that survives contact with actual play.

## Publishing as a site

The recommendation: **[Quartz v4](https://quartz.jzhao.xyz)**. It builds a static site out of an Obsidian vault, keeps double-bracket wikilinks, renders callouts, and gives you backlinks, full-text search and a graph view. It deploys to GitHub Pages from the same repository, so the vault stays the source of truth and the site is just a build step. No duplicate content, no rework.

Two things to sort before publishing:

1. **`_Restricted` must not ship.** Add it to Quartz's ignore patterns. If the site is public, treat that folder as if it were a private repo.
2. Same for anything under `08 Templates` — it will publish as empty pages otherwise.

Obsidian Publish is the paid alternative and needs no build step, but it costs monthly and gives you less control over what is excluded.

## The one habit that matters

Write the session note the same night, badly. A rough note that exists beats a good note that doesn't. Everything else in this vault is derived from `01 Sessions` and can be rebuilt from it.
