"""Entry for make.fun's "Roast Your Own Agent".

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

SETUP = "My agent's confidence is inversely proportional to its accuracy: "
TURN = "it whispers when it's right "
TAG = "and delivers TED talks when it's hallucinating."

ENTRY = SETUP + TURN + TAG

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry text to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
