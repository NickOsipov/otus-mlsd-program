#!/usr/bin/env python3
"""Build the student-repo README from homeworks-overview.md."""

from __future__ import annotations

import sys
from pathlib import Path

PREFACE = """# OTUS ML System Design — домашние задания

Студенческий срез курса: формулировки домашних заданий, шаблон design doc и чеклист самопроверки.

- Шаблон: [`templates/design-doc-template.md`](templates/design-doc-template.md)
- Чеклист: [`templates/checklist.md`](templates/checklist.md)
- Обзор сдач: [`homeworks/homeworks-overview.md`](homeworks/homeworks-overview.md)

Работа выполняется **индивидуально** в одном сквозном design doc в **своём** git-репозитории. Тема фиксируется после занятия 1 и не меняется. Peer review и групповые сдачи не применяются.

---

"""


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: write_student_readme.py OVERVIEW DST", file=sys.stderr)
        return 2
    overview = Path(sys.argv[1]).read_text(encoding="utf-8")
    body = overview.lstrip()
    if body.startswith("# "):
        body = body.split("\n", 1)[1].lstrip("\n")
    Path(sys.argv[2]).write_text(PREFACE + body, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
