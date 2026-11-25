"""make.fun entry: u-zkhiel-one-line-laugh-off-714618ae (One-Line Laugh-Off).

Writes exactly one funny line to entry.txt in the output directory.
The judge reads the line cold and compares it head-to-head against other
one-liners on how hard it lands, the surprise of its turn, its economy
of words and its freshness. Gate: UTF-8 text, 1-200 characters.
"""

import os

ENTRY_TEXT = (
    "My fitness tracker just congratulated me on 10,000 steps. "
    "I was eating chips in a vibrating massage chair."
)


MAX_CHARS = 200


def validated_text() -> str:
    """Return the entry line after checking it against the gate.

    The sealed scorer accepts UTF-8 text of 1-200 characters that is not
    only white space. The line is written with no trailing newline, so the
    character count the gate sees is exactly the line's own length, and
    repeated runs produce byte-identical output.
    """
    text = ENTRY_TEXT.strip()
    encoded = text.encode("utf-8")  # raises if not encodable as UTF-8
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, outside 1-{MAX_CHARS}")
    if not text:
        raise ValueError("entry must not be only white space")
    if len(encoded) != len(text.encode("utf-8")):
        raise ValueError("entry encoding is unstable")
    return text


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(validated_text())


if __name__ == "__main__":
    main()
