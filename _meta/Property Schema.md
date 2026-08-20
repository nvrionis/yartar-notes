---
tags: [meta]
---
# Property Schema

The single source of truth for frontmatter in this vault. [[Workflow|/session]] writes to this schema. `08 Templates` mirrors it. If they disagree, this file wins.

## The principle

**Tags say what a note *is*. Properties say what is *true* about it.**

A tag is a flat label with no value — you can only ask "has it or hasn't it". A property is `key: value`, so you can sort it, group it, compare it and filter on it. Anything with more than two possible states belongs in a property.

**Not every field must be filled.** Blank is a legitimate answer and means *not established in play*. Never guess a value to fill a gap — an empty `species` is information, a wrong one is a lie in a queryable field.

## Tags

One type tag per note, and nothing else — except the short list of cross-cutting sets below.

| Type tag | Folder |
|---|---|
| `npc` | `03 NPCs` |
| `pc` | `02 Party` |
| `faction` | `04 Factions` |
| `location` | `05 Locations` |
| `lore` | `06 Lore` |
| `item` | `07 Items & Loot` |
| `session` | `01 Sessions` |
| `dashboard` | `00 Dashboard` |
| `meta` | `_meta`, root |

**Cross-cutting sets** — these are groupings no property captures. Add sparingly.

| Tag | Means |
|---|---|
| `cael-circle` | People who will vouch for [[Cael]]'s twenty years on the road. His cover, in human form. |
| `former-party` | Adventured with the group and left. |
| `alias` | A redirect stub, not an entity. [[Doman Vein]] and [[Iskra Vein]] point at the notes that carry the real record. Excluded from NPC views on purpose. |

Everything else that used to be a tag is now a property. `antagonist` → `disposition: hostile`. `deceased` → `status: dead`. `district` → `type: district`. `magic` → `type: magic`.

---

## NPC

```yaml
tags: [npc]
tier: major              # major | recurring | minor | background
status: alive            # alive | dead | presumed-dead | missing | unknown
disposition: neutral     # ally | friendly | neutral | wary | hostile | employer | unknown
species: human
gender: male
faction: ["[[The Ravensworth]]"]
based: "[[Yartar]]"
first_seen: session-1
last_seen: session-3
aliases: [Doman Vein]
name_confirmed: true
source: "[[Tom Farow]]"
```

Three separate axes, because they answer three separate questions and used to be crushed into one:

- **`tier`** — how much they matter. `major` drives the plot; `recurring` has come back or will; `minor` had a scene; `background` is colour and cover.
- **`status`** — are they alive. Nothing else.
- **`disposition`** — where they stand *with the party*, as last observed.

`aliases` is an Obsidian built-in: with `aliases: [Doman Vein]` on [[The Knife]], a `[[Doman Vein]]` link resolves to him natively.

`name_confirmed: false` means the party has *heard* the name, not confirmed it. Mirrors [[Naming and Uncertainty]].

## Location

```yaml
tags: [location]
type: venue              # city | district | village | venue | region | ruin | landmark | planar
status: intact           # intact | damaged | destroyed | abandoned | unknown
danger: risky            # safe | watched | risky | deadly
access: open             # open | restricted | barred | unknown
parent: "[[Yartar]]"
controlled_by: "[[The Hand of Yartar]]"
first_seen: session-2
last_visited: session-2
```

**`status` is the state of the place. `danger` is the risk of going there. They are not the same field.**

[[The Last Pint]] is an ordinary working pub — `status: intact`, `access: open` — that happens to be `danger: risky`, because [[Reon Sahtar]] is sitting in it with a larger force. The building is fine. The company is not.

- **`status`** — is it still standing and functioning.
- **`danger`** — how likely the party is to get hurt there.
- **`access`** — can the party get in at all. [[Merchant Quarter]] is perfectly safe and `restricted`.
- **`parent`** — nesting. Districts and venues point at their city; this is what lets [[Yartar]]'s district table generate itself.

## Faction

```yaml
tags: [faction]
type: criminal           # criminal | political | mercantile | religious | military | noble | other
status: active           # active | broken | cold | unknown
threat: high             # none | low | moderate | high | unknown
disposition: hostile     # ally | friendly | neutral | wary | hostile | employer | unknown
base: "[[The Warrens]]"
leader: "[[Reon Sahtar]]"
members: ["[[Selda]]"]
first_seen: session-2
name_confirmed: false
```

`threat` is how dangerous they are in the abstract. `disposition` is whether they are currently pointed at the party. [[The Hand of Yartar]] is `threat: high`, `disposition: unknown` — they have never once looked at the party.

## Item

```yaml
tags: [item]
type: magic              # magic | mundane | document | consumable | artifact | condition | quest
status: held             # held | lost | spent | destroyed | unclaimed | active | unknown
holder: "[[Cael]]"
identified: false
attuned: false
origin: "[[Selda]]"
first_seen: session-2
```

`active` is for `type: condition` — [[The Poison]] is not carried, it is *running*.

`identified` is the D&D question — do we know what it does. [[Coin of Tymora]] is `held` and `identified: false`: the party has carried it since before the campaign and still cannot say what it does.

## Lore

```yaml
tags: [lore]
type: deity              # deity | history | theory | phenomenon | theme
confidence: reported     # established | reported | theory | disputed
source: "[[The Professor]]"
first_seen: session-3
```

These two carry the vault's truth discipline into a queryable field.

- **`confidence`** — `established` is witnessed by the party. `reported` is somebody told them. `theory` is somebody's argument. `disputed` is contradicted.
- **`source`** — who they heard it from.

[[Ilvaeris]] is `reported` from [[The Professor]], a man the vault itself describes as not neutral and not stable. That should be one query away, not buried in a sentence. `source` and `confidence` are valid on NPC and faction notes too, wherever the knowledge came from one mouth.

## Thread

```yaml
tags: [thread]
type: mystery            # quest | mystery | threat | promise
heat: hot                # hot | warm | cold
status: active           # active | resolved | abandoned
opened: session-2
closed:
involves: ["[[The Poison]]", "[[The Professor]]"]
```

One note per thread in `09 Threads`. [[Open Threads]] stays the curated running order — it says which one will hurt most, which no query can. The notes carry the detail and make the board queryable.

- **`type`** — `quest` is something the party is trying to do. `mystery` is something they want to know. `threat` is something coming for them. `promise` is something owed.
- **`heat`** — how urgent, matching the Hot/Warm/Cold sections of [[Open Threads]].
- **`involves`** — every entity the thread touches, so a thread shows up in the backlinks of each.

## Session

```yaml
tags: [session]
session: 3
title: Trail of Hope
pcs: ["[[Cael]]", "[[Vaelis]]", "[[Lorien]]"]
locations: ["[[The Drawbridge]]"]
npcs: ["[[Dell]]", "[[Beat]]"]
date_real:
date_in_world:
```

## PC

```yaml
tags: [pc]
player_character: true
player:
species: half-elf
class: cleric
level:
status: alive
first_seen: session-0.5
```

---

## Adding a value

Do not invent one silently. Add it to the list in this file in the same commit, or the views stop being trustworthy. If a value only ever applies to one note, it should probably be a sentence in the body instead.
