#!/usr/bin/env python3
"""Writes demo/manifest.json: the list of the notes and images of the example campaign.

DM Vault reads this list to open the example campaign from GitHub Pages (a web browser cannot list the
files of a folder on a website by itself). The GitHub workflow runs this script automatically each time
you publish; you only need to run it yourself to test the site on your own computer:
    python3 tools/make-manifest.py
"""
import json, os, datetime

DEMO = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'demo')
KEEP = ('.md', '.markdown', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.bmp')
files = []
for root, dirs, names in os.walk(DEMO):
    dirs[:] = sorted(d for d in dirs if not d.startswith('.'))  # skip hidden folders (.obsidian...)
    for n in sorted(names):
        if n.lower().endswith(KEEP) and not n.startswith('.'):
            files.append(os.path.relpath(os.path.join(root, n), DEMO).replace(os.sep, '/'))
with open(os.path.join(DEMO, 'manifest.json'), 'w', encoding='utf-8') as f:
    json.dump({'generated': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'), 'files': files},
              f, ensure_ascii=False, indent=1)
print(len(files), 'files listed in demo/manifest.json')
