"""Monday Morning Punchlines — make.fun entry.

Writes one original joke about Monday mornings to /output/entry.txt.

Pure Python standard library only (pathlib). No third-party packages,
no network, no input files: the joke is a string literal in this file.
"""

from pathlib import Path

JOKE = (
    "My bed files for custody every Monday morning. "
    "My alarm testifies against me. "
    "I lose every time."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    assert text.strip(), "joke must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
