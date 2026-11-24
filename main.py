"""The One-Line Exit: write the funniest single-line resignation letter
to /output/entry.txt (exactly one line, 1-140 characters)."""

import os

ENTRY = "I hereby resign as your IT guy \u2014 the printer and I have both stopped responding to your emails."


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY, "entry must be exactly one line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
