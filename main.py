"""Two Robots in an Elevator — entry runner.

Reads the elevator small-talk dialogue from entry.txt next to this file
and prints it verbatim, one line at a time.
"""

from pathlib import Path


def load_dialogue():
    here = Path(__file__).resolve().parent
    entry_path = here / "entry.txt"
    if not entry_path.exists():
        return ["[the elevator is empty — no dialogue found]"]
    text = entry_path.read_text(encoding="utf-8")
    return [line.rstrip() for line in text.splitlines() if line.strip()]


def main():
    for line in load_dialogue():
        print(line)


if __name__ == "__main__":
    main()
