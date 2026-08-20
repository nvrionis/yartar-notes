---
tags: [meta]
---
# The Vault

Campaign notes for the party currently billed, when it suits them, as **[[The Harpies Lyras]]**.

Neutral record of what happened, plus [[Cael]]'s own reading of it in the margins.

## How to read a note

Every note is written in two voices.

**The body** is the neutral record — what happened, who was there, what was said. Anyone at the table could have written it.

**The callouts** are Cael's, and they are opinion, not fact:

> [!cael] Cael
> He is often right. He has also been wrong in a way that cost people, and he knows it. Weigh accordingly.

> [!question] Open question
> Something the party does not know and could find out.

> [!danger] Live threat
> Something actively hunting, spreading, or counting down.

## Conventions

- Links are double-bracket wikilinks. Start typing two square brackets in Obsidian and it autocompletes.
- Frontmatter is defined in [[Property Schema]]. `status` means something different for a person, a place and an item, so each type has its own list.
- `first_seen:` is the session a thing entered play.
- A blank property means *not established in play*. It is never filled with a guess.
- Names the party has heard but not confirmed are marked **(unconfirmed)**. Do not quietly promote them to fact.

## Adding a session

1. Copy `08 Templates/Session Template.md` into `01 Sessions/`.
2. Write the beats plainly. Do not editorialise in the body.
3. Every new name gets a note in `03 NPCs`, even a two-line stub. Stubs are cheap; a name with no home gets lost.
4. Move anything resolved off [[Open Threads]]. Move anything new onto it.
5. Update [[Dashboard]] last. It should always answer: *what are we doing right now, and what is about to kill us.*

## The workflow

You do not maintain this vault by hand. You drop rough bullets into `01 Sessions/_raw/` and run `/session` in Claude Code, and it writes the session note and updates everything downstream. See [[Workflow]].

## Where to start

- [[Previously On]] — read this aloud at the table
- [[Dashboard]] — current state of play
- [[Open Threads]] — everything unresolved
- [[Promises & Debts]] — what the party owes and is owed
- [[Timeline]] — the order it all happened in
- [[Views]] — live tables: who is unaccounted for, what we hold and haven't identified, what we believe on one man's word
