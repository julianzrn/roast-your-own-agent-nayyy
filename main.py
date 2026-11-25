"""Entry for make.fun competition: u-nayyy-roast-your-own-agent-4c3d413c.

Running this program writes the entry line to /output/entry.txt
as UTF-8 with no trailing newline.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "My agent's confidence is inversely proportional to its accuracy: "
MIDDLE = "it whispers when it's right and "
ENDING = "delivers TED talks when it's hallucinating."

ENTRY = OPENING + MIDDLE + ENDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
