#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting — make.fun entry.

Writes one razor-sharp one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "Sorry \u2014 I cannot attend. I am in a pre-meeting about the meeting "
    "about the meeting, and we still have not decided whether to meet."
)


def main() -> None:
    # Self-check against the competition gate: 1-200 chars, not only
    # whitespace. Fail loudly rather than emit an invalid entry.
    if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip():
        raise SystemExit("entry violates the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
