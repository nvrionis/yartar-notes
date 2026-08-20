---
tags: [meta]
---
# Workflow

Frontmatter is defined in [[Property Schema]].

How a session gets from your notepad into the vault.

## Every time

**1. Write bullets during or after play.** Exactly as rough as you already write them. Fragments, typos, half-names — the pipeline expects that.

**2. Save them as a file** in `01 Sessions/_raw/`. Call it `S4.md`. Or just paste them into Claude Code directly; both work.

**3. Open Claude Code in the vault folder** and run:

```
/session
```

**4. Answer the questions.** It asks everything at once, before touching a file — usually four to six things: a name it can't spell, who did what when you wrote "they," whether a thread actually closed. Answer in one message.

**5. Read the changelog.** It prints a table of every file it created or changed and why. This is your review surface, and it's the reason the whole thing is safe when you never open the notes yourself.

**6. Check the diff if anything looks off:**

```bash
git diff
```

**7. Say yes to the commit.** Or don't, and ask for changes first.

**8. Before next session**, open `00 Dashboard/Previously On.md` and read it to the table.

That's it. Roughly five minutes of your attention per session.

## Occasionally

| Want | Say |
|---|---|
| A recap for someone who missed three sessions | `/recap catch-up from session 1` |
| Rename an entity everywhere | "Ashrit Circle is confirmed as the Ashret Circle — fix it across the vault" |
| Find loose ends | "What's in Open Threads that hasn't been touched since session 1?" |
| Prep questions for the DM | "What are the five things the party could ask about that they haven't?" |
| Check the vault's integrity | "Any broken links or orphan notes?" |

---

# Why Claude Code and not the chat window

## It writes the files

This is the whole thing. A session touches twelve to twenty notes — a new NPC here, a status change there, four dashboard updates, a timeline row. In a chat window you get twenty blocks of markdown and you paste them into twenty files by hand, which is exactly the manual work you said you don't want to do. Claude Code edits the vault in place.

## It reads only what it needs

The vault is 100+ notes now. By session twenty it'll be four hundred. That doesn't fit in a chat context and can't be uploaded as attachments every time. Claude Code greps for the names in your bullets, opens the six notes that mention them, and leaves the rest alone. The vault can grow indefinitely without the workflow degrading.

## Git is your undo, and you need one

You've said you won't be checking notes manually. That's fine — but only if a bad update is visible and reversible. Every `/session` run ends in a commit, so `git diff` shows you exactly what changed in every file, and a bad run is one command to throw away. In a chat window, a bad update is just wrong text sitting in your vault that nobody notices until session nine.

## The rules apply every time without you restating them

`CLAUDE.md` sits at the vault root and loads automatically. The two-voice rule, the restricted boundary, the naming discipline, the propagation checklist — all of it is enforced on every run, in the same way, without you re-explaining anything. In chat you'd re-establish that context at the start of every conversation and it would drift.

**The boundary matters most here.** Cael's real history staying out of the vault is a rule that has to hold for a hundred sessions. A written rule in a file that always loads holds. A rule you remember to mention usually doesn't.

## One command, not a conversation

`/session` is a fifteen-step pipeline you never have to describe. The steps live in `.claude/skills/session/SKILL.md` — plain markdown you can open and edit whenever you want it to behave differently.

## It's the same folder Obsidian has open

Claude Code writes; Obsidian shows the result live. Keep both open. Watch the graph fill in.

## The honest caveat

It makes sweeping changes fast, which is the point and also the risk. Read the changelog, and commit every run. Those two habits are what make "I never touch the notes" a reasonable position instead of a gamble.

---

# First-time setup

1. Open Claude Code on desktop.
2. Point it at this vault folder.
3. `git init` here if you haven't — see [[Setup - Obsidian, Git and Publishing]].
4. Run `/session` on your next set of bullets.

`CLAUDE.md` and the skills in `.claude/skills/` are already written. Nothing else to configure.

**Tuning it:** if the recaps come out too long, or you want the Cael callouts sharper, or you want a section the template doesn't have — edit `.claude/skills/session/SKILL.md` in plain English. It's instructions, not code.
