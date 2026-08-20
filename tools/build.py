# -*- coding: utf-8 -*-
"""Rebuild docs/index.html from the vault.

Run from the vault root:   python tools/build.py

Reads every note, embeds them in the template, and writes the standalone
site. No dependencies beyond PyYAML.
"""
import io, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

subprocess.check_call([sys.executable, os.path.join("tools", "extract.py")])

tpl = io.open(os.path.join("tools", "index.template.html"), encoding="utf-8").read()
data = io.open("vaultdata.json", encoding="utf-8").read()
if "/*__DATA__*/" not in tpl:
    raise SystemExit("template is missing its /*__DATA__*/ placeholder")

out = tpl.replace("/*__DATA__*/", data)
io.open(os.path.join("docs", "index.html"), "w", encoding="utf-8", newline="\n").write(out)
os.remove("vaultdata.json")
print("docs/index.html  %.1f KB" % (len(out) / 1024.0))
