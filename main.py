"""Snooze Button Roast: one line roasting an alarm clock for ringing at 6 AM on a Saturday.

Stdlib only, no network, no randomness. The punchline lands in the last few words.
Writes exactly one line to /output/entry.txt with mode 0644.
"""

import io
import os

JOKE = "Six AM on a Saturday? Even the sun sleeps in — you are the only thing in this house with a worse social life than me."

LIMIT = 200


def main():
    line = JOKE.strip()
    if len(line) < 1 or len(line) > LIMIT:
        raise SystemExit("line must be 1-%d chars, got %d" % (LIMIT, len(line)))
    if line.count("\n"):
        raise SystemExit("line must not contain a newline")
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    entry_path = os.path.join(directory, "entry.txt")
    # Clear only children of the output dir if needed; never delete the dir itself.
    with io.open(entry_path, "w", encoding="utf-8") as stream:
        stream.write(line)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
