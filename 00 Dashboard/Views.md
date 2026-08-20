---
tags: [dashboard]
---
# Views

Live tables built off the frontmatter defined in [[Property Schema]]. These list things. The [[Dashboard]] says what matters — keep both.

> [!danger] Open this folder as its own Obsidian vault
> There are **eight** nested `.obsidian` roots under `DnD`, and three other copies of this campaign sitting beside this one — `Long Campaigns/Yartar`, `Long Campaigns/Yartar - Copy`, and `Long Campaigns/Ledger/Grey Ledger Vault`. If Obsidian is opened at any folder above this one, every view double-counts: two Ravensworths, a stray *Voss Regime*, somebody else's `T - Faction` template.
>
> **Fix:** Obsidian → *Open folder as vault* → point it at `Long Campaigns/Vault`. It already has its own `.obsidian`. This also switches on the `cael-callout` CSS snippet, which lives in this folder and is inactive under any other root.

## The bases

Obsidian's **Bases** is a core feature, so these work on a clean install.

| Base | Views |
|---|---|
| `Threads.base` | *By heat* · *Hot* · *Quests* · *Threats* · *Mysteries* · *Closed* |
| `NPCs.base` | *Who matters* · *Allies* · *Pointed at us* · *Loose ends* · *Cael's cover* · *The dead* |
| `Locations.base` | *Everywhere* · *Do not walk in* · *Yartar* · *Gone or barred* |
| `Factions.base` | *All factions* · *Dangerous* · *Hostile to us* |
| `Items.base` | *Everything we hold* · *Unidentified* · *Not in our hands* |
| `Lore.base` | *What we believe* · *On one person's word* |

## The queries that matter

**What is going to hurt.** `Threads.base` → *Hot*. Three of them: [[Curing the poison]], [[Getting out past the horde]], [[Where Devon went]].

**Who is unaccounted for.** `status` in `unknown`, `missing`, `presumed-dead`. [[Devon Dale]] — the job — plus [[Brisk]], [[Sef]] and [[Fren]] with the files they walked off with, and [[Tom Farow]], who talked and vanished.

**What we are carrying that we do not understand.** `identified: false`. The [[Coin of Tymora]] has been in [[Cael]]'s pocket since before the campaign started. [[Selda's Signet Ring]] is the strongest unexamined lead the party owns.

**Where it is dangerous and why.** `danger` is separate from `status` on purpose. [[The Last Pint]] is an intact, open, working pub — the danger is that [[Reon Sahtar]] is sitting in it.

**What we believe because one man said so.** `confidence` and `source`. [[Ilvaeris]] and [[Time as Memory]] both trace to [[The Professor]], who is not neutral, is not stable, and is brewing the antidote.

## Dataview fallback

If you install the **Dataview** plugin, the same views work as queries in any note:

```dataview
TABLE heat, type, opened
FROM #thread
WHERE status = "active"
SORT heat ASC
```

```dataview
TABLE tier, status, disposition, faction, last_seen
FROM #npc
WHERE tier != "background"
SORT tier ASC, file.name ASC
```

```dataview
TABLE type, parent, status, danger, access
FROM #location
WHERE danger = "risky" OR danger = "deadly"
```

```dataview
TABLE type, holder, identified, origin
FROM #item
WHERE identified = false
```

```dataview
TABLE confidence, source
FROM #lore
WHERE confidence != "established"
```
