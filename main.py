#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue — exactly 100 words
for a fantasy villain who is secretly just very tired.

The monologue undercuts the villain's own menace with the most
un-villainous grievance possible: meetings, lumbar support, a heavy
cape, a unionized minion workforce. The apocalypse is not defeated;
it is rescheduled to Monday, after coffee. The word count is
asserted at runtime (exactly 100 words by whitespace split), so the
entry cannot drift over the limit by accident.
"""

import os
from pathlib import Path

LINE = "Behold, mortal. I am Malachar, Lord of Eternal Night, Devourer of Kingdoms, and honestly, I am exhausted. Do you know what conquering the world involves? Meetings. Endless meetings with goblins who cannot read a calendar. The dark throne? Terrible lumbar support. My cape weighs nine kilos. Nine! The minions unionized. They want weekends. Weekends! I just want one quiet evening, a warm blanket, and nobody asking me to monologue before breakfast. So go. Tell your kingdom the Dark Lord is taking a nap. The apocalypse can wait until Monday. No world-ending before coffee, that is my final decree. Signed, Malachar."

WORDS = 100


def main() -> None:
    words = LINE.split()
    assert len(words) == WORDS, f"monologue is {len(words)} words (must be {WORDS})"
    assert "\n" not in LINE, "entry must be a single block"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(words)} words to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
