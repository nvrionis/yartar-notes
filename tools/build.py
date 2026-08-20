# -*- coding: utf-8 -*-
"""Rebuild the vault index site.

Run from the vault root:   python tools/build.py

Writes two files from one template:

  docs/index.html      a complete HTML document, for GitHub Pages
  .artifact/index.html the same page as a bare fragment, for publishing
                       as a Claude Artifact (which supplies its own
                       <head>). Gitignored.

The document wrapper matters more than it looks: without
<meta name="viewport"> a phone renders the page at a virtual ~980px and
scales it down, so every mobile media query is skipped and you get the
desktop layout in miniature.
"""
import io, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

subprocess.check_call([sys.executable, os.path.join("tools", "extract.py")])

tpl = io.open(os.path.join("tools", "index.template.html"), encoding="utf-8").read()
data = io.open("vaultdata.json", encoding="utf-8").read()
if "/*__DATA__*/" not in tpl:
    raise SystemExit("template is missing its /*__DATA__*/ placeholder")

body = tpl.replace("/*__DATA__*/", data)

DOC = u"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<meta name="description" content="Searchable index of the Yartar campaign vault.">
</head>
<body>
%s
</body>
</html>
"""

io.open(os.path.join("docs", "index.html"), "w", encoding="utf-8", newline="\n").write(DOC % body)

art = os.path.join(".artifact")
if not os.path.isdir(art):
    os.makedirs(art)
io.open(os.path.join(art, "index.html"), "w", encoding="utf-8", newline="\n").write(body)

os.remove("vaultdata.json")
print("docs/index.html        %.1f KB  (full document, for Pages)" % (len(DOC % body) / 1024.0))
print(".artifact/index.html   %.1f KB  (fragment, for the Artifact)" % (len(body) / 1024.0))
