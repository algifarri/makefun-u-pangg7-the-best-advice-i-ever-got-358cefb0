#!/usr/bin/env python3
"""The Best Advice I Ever Got — make.fun entry.

Writes a single sentence (max 200 characters) about the best advice
the writer ever received to /output/entry.txt. Deterministic, stdlib-only.
"""

import os

ENTRY = (
    "My grandmother, hands deep in bread dough, told me: "
    "never trust someone who is kind only when others are watching."
)
# 114 characters: one sentence, one voice, one real moment.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.count(".") == 1, "entry must be a single sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
