#!/usr/bin/env python3
"""Remove '## Примечание для преподавателя' sections from a markdown file."""

from __future__ import annotations

import sys
from pathlib import Path

HEADING = "## Примечание для преподавателя"


def strip_teacher_notes(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    skipping = False
    for line in lines:
        stripped = line.lstrip("\ufeff")
        if stripped.startswith(HEADING):
            skipping = True
            continue
        if skipping and stripped.startswith("## "):
            skipping = False
        if not skipping:
            out.append(line)
    result = "".join(out).rstrip() + "\n"
    return result


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: strip_teacher_notes.py SRC DST", file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(strip_teacher_notes(src.read_text(encoding="utf-8")), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
