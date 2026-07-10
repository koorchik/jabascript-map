#!/usr/bin/env python3
"""Regenerate wiki/index.md from page contents (first sentence of each page).

Usage: python3 scripts/build_index.py
"""
import re
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent / "wiki"
SECTIONS = [
    ("Кластери", "clusters"),
    ("Концепції", "concepts"),
    ("Відео", "videos"),
    ("Інструменти", "tools"),
    ("Книги", "books"),
]
LINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\]")


def first_sentence(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    body = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    body = re.sub(r"^#.*$", "", body, flags=re.M)          # headings
    body = re.sub(r"^>.*$", "", body, flags=re.M)          # blockquotes
    body = LINK_RE.sub(lambda m: m.group(2) or m.group(1), body)
    body = body.replace("**", "").replace("*", "")
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith(("-", "|")):
            continue
        m = re.match(r"(.{20,158}?[.!?])(\s|$)", line)
        return (m.group(1) if m else line[:158]).strip()
    return ""


lines = ["# Індекс", "",
         "Каталог усіх сторінок вікі. Перегенеровуйте командою "
         "`python3 scripts/build_index.py` після кожного інджесту.", ""]
for title, folder in SECTIONS:
    pages = sorted((WIKI / folder).glob("*.md"))
    lines.append(f"## {title} ({len(pages)})")
    lines.append("")
    for p in pages:
        lines.append(f"- [[{p.stem}]] — {first_sentence(p)}")
    lines.append("")

(WIKI / "index.md").write_text("\n".join(lines), encoding="utf-8")
print(f"index.md written: {sum(1 for l in lines if l.startswith('- '))} entries")
