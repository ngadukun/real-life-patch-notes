"""Real-Life Patch Notes: The Comedy Changelog - make.fun.

Writes one line (at most 160 characters) in the terse
register of a real software release note, patching a bug
in human biology: the 3 a.m. replay of an embarrassing
memory, re-released in higher resolution instead of fixed.
"""

import os
from pathlib import Path

ENTRY = (
    "v2.7.0: Brain no longer replays your most embarrassing "
    "moment from 2014 at 3 a.m. — it still does, just now "
    "in higher resolution."
)


def entry_path() -> Path:
    # The grader mounts the repo read-only and hands us a
    # writable directory through MAKEFUN_OUTPUT_DIR; locally
    # we fall back to output/ beside this file.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return Path(out_dir) / "entry.txt"
    return Path(__file__).resolve().parent / "output" / "entry.txt"


def main() -> None:
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
