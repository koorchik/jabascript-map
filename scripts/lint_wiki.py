#!/usr/bin/env python3
"""Wiki health check: broken [[links]], orphan pages, missing frontmatter.

Usage: python3 scripts/lint_wiki.py
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "wiki"
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")

pages = {p.stem: p for p in ROOT.rglob("*.md")}
inbound = defaultdict(int)
broken = []

NAV = {"index", "log", "overview"}

for stem, path in sorted(pages.items()):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---") and stem not in NAV:
        print(f"NO FRONTMATTER: {path.relative_to(ROOT)}")
    for target in LINK_RE.findall(text):
        target = target.strip()
        if target in pages:
            if target != stem:
                inbound[target] += 1
        else:
            broken.append((str(path.relative_to(ROOT)), target))

for src, target in broken:
    print(f"BROKEN: {src} -> [[{target}]]")

NAV = {"index", "log", "overview"}
for stem, path in sorted(pages.items()):
    if stem in NAV:
        continue
    if inbound[stem] == 0:
        print(f"ORPHAN (no inbound links): {path.relative_to(ROOT)}")

print(f"\n{len(pages)} pages, {len(broken)} broken links")
sys.exit(1 if broken else 0)
