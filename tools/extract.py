# -*- coding: utf-8 -*-
import os, re, io, yaml, json

SKIP_DIRS = ['.git', '.obsidian', '.claude', '_Restricted', '08 Templates', '_raw', '_meta']
KIND = {
    '00 Dashboard': 'dashboard',
    '01 Sessions': 'session',
    '02 Party': 'party',
    '03 NPCs': 'npc',
    '04 Factions': 'faction',
    '05 Locations': 'location',
    '06 Lore': 'lore',
    '07 Items & Loot': 'item',
    '09 Threads': 'thread',
}

notes = []
for r, d, fs in os.walk('.'):
    if any(x in r for x in SKIP_DIRS):
        continue
    folder = r.replace('.' + os.sep, '').replace(os.sep, '/')
    if folder not in KIND:
        continue
    for f in sorted(fs):
        if not f.endswith('.md'):
            continue
        p = os.path.join(r, f)
        t = io.open(p, encoding='utf-8').read()
        m = re.match(r'---\n(.*?)\n---\n', t, re.S)
        fm = (yaml.safe_load(m.group(1)) if m else {}) or {}
        body = t[m.end():] if m else t
        # strip the leading H1, it duplicates the name
        body = re.sub(r'^\s*#\s+.*?\n', '', body, count=1)
        name = f[:-3]

        kind = KIND[folder]
        # alias redirect stubs are not entities
        tags = fm.get('tags') or []
        if isinstance(tags, str):
            tags = [tags]
        if 'alias' in tags:
            continue
        if kind == 'party' and 'npc' in tags:
            kind = 'npc'
        # the loot ledger is a hub note, not an item
        if 'ledger' in tags:
            kind = 'dashboard'

        clean = {}
        for k, v in fm.items():
            if k in ('tags',) or v is None or v == '':
                continue
            clean[k] = v

        notes.append({
            'name': name,
            'kind': kind,
            'tags': [x for x in tags if x not in KIND.values()],
            'props': clean,
            'body': body.strip(),
        })

# outbound links for the graph / related panel
names = set(n['name'] for n in notes)
for n in notes:
    outs = []
    for mm in re.findall(r'\[\[([^\]]+)\]\]', n['body'] + json.dumps(n['props'])):
        tgt = mm.split('|')[0].split('#')[0].strip().split('/')[-1]
        if tgt in names and tgt != n['name'] and tgt not in outs:
            outs.append(tgt)
    n['links'] = outs

data = json.dumps(notes, ensure_ascii=False, separators=(',', ':'))
io.open('vaultdata.json', 'w', encoding='utf-8').write(data)

import collections
c = collections.Counter(n['kind'] for n in notes)
print('notes:', len(notes))
for k, v in sorted(c.items()):
    print('  %-12s %d' % (k, v))
print('json size: %.1f KB' % (len(data) / 1024.0))
