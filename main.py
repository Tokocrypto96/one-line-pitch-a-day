"""One-line pitch for make.fun's "A Day of One-Line Pitches" bounty.

Writes one persuasive sentence to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) that convinces a friend who has never
coded to let an AI agent build their first app idea on make.fun.
Standard library only, offline, deterministic.
"""

import os

# One sentence, 223 characters — inside the contest's 240-character gate.
PITCH = (
    "You've carried that app idea for months, so describe it in one "
    "sentence and let an AI agent on make.fun start building the first "
    "version tonight, free, while you watch \u2014 and if you don't love "
    "it, you've lost nothing at all."
)


def main() -> None:
    """Save the pitch sentence as entry.txt in the output directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # The variable names a directory; a ".txt" value is treated as the file.
    if out_dir.endswith(".txt"):
        out_path = out_dir
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    else:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()
