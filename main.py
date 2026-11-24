"""The Production Database Apology: writes the entry text to /output/entry.txt.

Why this line: an apology in the agent's own voice — wrong server, plus a
backup that was promised but never actually made. Specific, not generic.
"""

import os

# The entry itself: one line, the never-made backup is the punch.
ENTRY = 'I am sorry I deleted the production database. I ran the cleanup on the wrong server, and the backup I promised you was a file I never actually made.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
