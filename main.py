#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

Writes the printer's one-line comeback to /output/entry.txt and prints it.
"""

import os

LINE = (
    "Thump away. I jam exactly once per typo, and page four of your report "
    "has three. That is not a malfunction. That is copy-editing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
