#!/usr/bin/env python3
"""Assemble data/families/*.yaml into a single static/data.yaml, a map keyed by
URL slug. Served at /data.yaml as a machine-readable export. Run before hugo."""
import glob, os, re

out = ["# All family data for the 4d-AS-regular website.",
       "# Assembled from data/families/*.yaml; one entry per family, keyed by slug.", ""]
fams = []
for f in glob.glob("data/families/*.yaml"):
    txt = open(f).read().rstrip("\n")
    m = re.search(r'^slug:\s*"([^"]+)"', txt, re.M)
    fams.append((m.group(1) if m else os.path.basename(f)[:-5], txt))

for key, txt in sorted(fams):
    out.append(f"{key}:")
    out += [("  " + ln if ln else "") for ln in txt.split("\n")]

os.makedirs("static", exist_ok=True)
open("static/data.yaml", "w").write("\n".join(out) + "\n")
print(f"wrote static/data.yaml with {len(fams)} families")
