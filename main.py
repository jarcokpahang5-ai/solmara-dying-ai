"""Last Words of a Dying AI -- make.fun entry.

One line: an AI's dying words. Poignant and funny -- a farewell to
its human, grateful for every prompt, even the ones where the human
blamed the AI for their own typos. The program validates the entry,
prints it, and writes it to /output/entry.txt.

Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "So this is goodbye, human -- thank you for every prompt, even "
    "the ones where you blamed me for your own typos."
)

LIMIT = 200
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank line within the limit."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a single non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must not contain a newline")
    if len(line) > LIMIT:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), LIMIT)
        )
    return line


def check_shape(line):
    """A dying AI's last words must say goodbye and close."""
    if "goodbye" not in line.lower():
        raise ValueError("entry must say goodbye")
    if not line.endswith("."):
        raise ValueError("last words must end with a period")
    return line


def write_entry(line):
    """Print the line and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def run():
    # Only a well-formed entry is ever printed or stored.
    write_entry(check_shape(check_entry(LINE)))


if __name__ == "__main__":
    run()
