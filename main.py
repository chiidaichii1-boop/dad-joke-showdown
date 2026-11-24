"""Dad Joke Showdown entry: one dad joke, at most 200 characters.

The joke is written to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic: the same text every run.
"""

import os

JOKE = (
    "My daughter asked why I park the car in the garage every night. "
    "I said, 'Because it needs rest \u2014 it's exhausted.'"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
