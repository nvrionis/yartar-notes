---
tags: [meta]
---
# _raw

Drop your session bullets here as a plain `.md` file — `S4.md`, `S5.md`, however you like. Typos, fragments and half-sentences are fine; that is what this folder is for.

Then in Claude Code, from the vault folder:

```
/session
```

It picks up the newest unprocessed file, asks you whatever it can't work out, writes the session note, and updates the rest of the vault.

Processed files move to `_raw/processed/` so they don't get ingested twice. **Never delete them** — they're the original record, and every note in the vault is derived from them. If the vault ever gets tangled, these are what it gets rebuilt from.
