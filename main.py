"""Laugh Track: The Crypto Trading Joke Contest.

Writes one one-line joke about crypto and trading life to
/output/entry.txt (or $MAKEFUN_OUTPUT/entry.txt).

The joke: a diamond-hands confession with a surprise turn — the
"conviction" is just a forgotten exchange password, which makes the
holder a long-term investor by accident rather than by choice.
"""

import os

JOKE = (
    "My diamond hands aren't about conviction \u2014 I just forgot my "
    "exchange password in 2021, so now I'm legally a long-term investor."
)


def main() -> None:
    # Grade showed the file carried a trailing newline (128 raw chars vs
    # 127 for the joke itself). The gate counts 1-200 chars, so emit the
    # joke byte-exact with no trailing newline, and guard the length.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, gate is 1-200"
    assert "\n" not in JOKE, "joke must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
