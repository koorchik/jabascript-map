#!/usr/bin/env python3
"""Convert YouTube auto-caption .vtt files into timestamped transcripts.

Unlike clean_vtt.py (which strips all timing), this keeps periodic [mm:ss]
markers so chapter data can be authored against real video positions.
In rolling captions the payload line WITH inline word tags carries the new
words (untagged lines repeat the previous phrase), so tagged lines are the
canonical source here; the first inline tag time is the phrase's timestamp.

Output: transcripts/timed/<youtube_id>.uk.txt — one line per ~20s block:
    [m:ss] phrase phrase phrase ...

Usage: python3 scripts/vtt_to_timed.py raw/*.uk.vtt
"""
import re
import sys
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent.parent / "transcripts" / "timed"

CUE_RE = re.compile(r"^(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})", re.M)
TAG_RE = re.compile(r"<[^>]+>")
INLINE_TIME_RE = re.compile(r"<(\d{2}:\d{2}:\d{2}\.\d{3})>")
ID_RE = re.compile(r"\[([A-Za-z0-9_-]{11})\]\.(?:[a-z]{2})\.vtt$")

BLOCK_SECONDS = 20


def to_seconds(ts: str) -> float:
    h, m, s = ts.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)


def fmt(seconds: float) -> str:
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def phrases(vtt_text: str):
    """Yield (start_seconds, text) for each new phrase, deduplicated."""
    cue_start = None
    last_text = None
    for line in vtt_text.splitlines():
        line = line.strip()
        m = CUE_RE.match(line)
        if m:
            cue_start = to_seconds(m.group(1))
            continue
        if cue_start is None or not line:
            continue
        if line in ("WEBVTT", "Kind: captions") or line.startswith("Language:"):
            continue
        tagged = INLINE_TIME_RE.search(line)
        text = " ".join(TAG_RE.sub("", line).split())
        if not text:
            continue
        if tagged:
            start = to_seconds(tagged.group(1))
        elif text != last_text:
            # Safety net for non-rolling VTTs: untagged, genuinely new text.
            start = cue_start
        else:
            continue  # rolling repeat of the previous phrase
        if text == last_text:
            continue
        last_text = text
        yield start, text


def convert(vtt_path: Path) -> tuple[str, str, int]:
    text = vtt_path.read_text(encoding="utf-8")
    m = ID_RE.search(vtt_path.name)
    if not m:
        raise ValueError(f"no [youtube_id] in filename: {vtt_path.name}")
    youtube_id = m.group(1)

    ends = [to_seconds(e) for _, e in CUE_RE.findall(text)]
    duration = max(ends) if ends else 0

    lines = []
    block_start, block_words = None, []
    for start, phrase in phrases(text):
        if block_start is None:
            block_start = start
        if start - block_start >= BLOCK_SECONDS and block_words:
            lines.append(f"[{fmt(block_start)}] {' '.join(block_words)}")
            block_start, block_words = start, []
        block_words.append(phrase)
    if block_words:
        lines.append(f"[{fmt(block_start)}] {' '.join(block_words)}")

    stem = vtt_path.name[: -len(".vtt")]
    header = f"# {stem}\n# youtube_id: {youtube_id}\n# duration: {fmt(duration)}\n\n"
    return youtube_id, header + "\n".join(lines) + "\n", len(lines)


def main(paths):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for p in map(Path, paths):
        youtube_id, out_text, n_blocks = convert(p)
        out = OUT_DIR / f"{youtube_id}.uk.txt"
        out.write_text(out_text, encoding="utf-8")
        duration = out_text.splitlines()[2].split(": ")[1]
        print(f"{p.name} -> {out.name}, {n_blocks} blocks, {duration}")


if __name__ == "__main__":
    main(sys.argv[1:])
