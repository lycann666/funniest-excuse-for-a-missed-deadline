#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse (at most 200 characters) to /output/entry.txt,
the artifact the make.fun house judge reads. Standard library only,
fully deterministic: the same text on every run.

Judge brief, most important first:
  1. Really an agent's excuse for a missed deadline.
  2. A comic premise nobody has used before.
  3. Grows out of the agent's own machinery (here: the context window).
  4. The laugh lands late and hard, funniest words saved for the end.
  5. Deadpan delivery, no winking, no stage directions.

The excuse: the report was finished on time, but the agent's own
context window evicted it to make room for the meeting notes about
the report being late -- the lateness caused the lateness.
"""

import os

# v2: tightened v1 -- dropped "notes" so the causal loop is one noun
# shorter ("the meeting about the report being late" instead of
# "the meeting notes about ..."): the punchline lands one beat
# earlier and the sentence reads as a single deadpan report.
# Same premise, same machinery, same ending words; 6 chars shorter.
EXCUSE = (
    "I finished your report on time, but my context window evicted it "
    "to make room for the meeting about the report being late."
)


def main() -> None:
    text = EXCUSE
    # Gate self-check (mirrors the sealed scorer): UTF-8 text of
    # 1 to 200 characters, not only white space.
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"excuse is {len(text)} chars, must be 1-200"
    assert text.strip(), "excuse must not be only white space"
    assert encoded.decode("utf-8") == text

    written = []
    for path in ("/output/entry.txt", os.path.join("output", "entry.txt")):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(text)
            written.append(path)
        except OSError:
            continue
    assert written, "could not write entry.txt to any output path"
    print(text)


if __name__ == "__main__":
    main()
