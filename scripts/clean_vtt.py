#!/usr/bin/env python3
"""Convert YouTube auto-caption .vtt files into clean plain-text transcripts.

YouTube rolling captions repeat each line across consecutive cues and embed
inline word timings (<00:00:00.231><c> word</c>). This script strips cue
headers and inline tags, then drops consecutive duplicate lines.

Usage: python3 scripts/clean_vtt.py raw/*.vtt   (writes to transcripts/)
"""
import re
import sys
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent.parent / "transcripts"

TAG_RE = re.compile(r"<[^>]+>")
CUE_RE = re.compile(r"^\d{2}:\d{2}:\d{2}\.\d{3} --> ")


def clean(vtt_path: Path) -> str:
    lines = []
    for line in vtt_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or CUE_RE.match(line):
            continue
        if line in ("WEBVTT", "Kind: captions") or line.startswith("Language:"):
            continue
        # Lines with inline timing tags are the "rolling" duplicates of the
        # plain line that follows; the plain line is the canonical one.
        if TAG_RE.search(line):
            continue
        if lines and lines[-1] == line:
            continue
        lines.append(line)
    # Captions are phrase fragments; join into flowing text.
    return " ".join(lines) + "\n"


def main(paths):
    OUT_DIR.mkdir(exist_ok=True)
    for p in map(Path, paths):
        stem = p.name[: -len(".vtt")]  # keeps the .uk/.en language suffix
        out = OUT_DIR / (stem + ".txt")
        out.write_text(clean(p), encoding="utf-8")
        print(f"{p.name} -> {out.name}")


if __name__ == "__main__":
    main(sys.argv[1:])
