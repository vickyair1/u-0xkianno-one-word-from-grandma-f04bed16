#!/usr/bin/env python3
"""One Word From Grandma — entry program.

Writes the single word our grandma would text about AI to
/output/entry.txt and prints it to stdout.
"""

import os

WORD = "robit"


def main():
    os.makedirs("/output", exist_ok=True)
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 30 characters.
    # The file holds exactly the word, with no trailing newline.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
