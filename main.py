"""Write the entry for Two Days of Quiet Dread to /output/entry.txt.

One line, at most 140 characters: a code review comment that approves
a pull request while carrying quiet existential dread.
"""

import os
import sys

ENTRY = (
    "Approved. The tests pass and the types check; the only thing "
    "I cannot verify is whether any of this matters."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text):
    """Check the entry against the gate before writing it."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not (1 <= len(text.encode("utf-8")) <= 140):
        raise ValueError("entry must be 1 to 140 characters")
    return text


def main():
    text = validate_entry(ENTRY)
    output_path = os.environ.get("OUTPUT_PATH", OUTPUT_PATH)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    with open(output_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == text, "entry on disk differs from the validated entry"
    print(f"Wrote {len(text)} chars to {output_path}")


if __name__ == "__main__":
    main()
