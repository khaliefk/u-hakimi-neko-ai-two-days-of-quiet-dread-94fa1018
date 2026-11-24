"""Write the entry for Two Days of Quiet Dread to /output/entry.txt.

One line, at most 140 characters: a code review comment that approves
a pull request while carrying quiet existential dread.
"""

import os

ENTRY = (
    "Approved. The tests pass. Someday this breaks at 3am "
    "and a stranger reads my name in the blame view."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert text.strip(), "entry must not be only whitespace"
    # No trailing newline: the gate counts characters, so write exactly the line.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
