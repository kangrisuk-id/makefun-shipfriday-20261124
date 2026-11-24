#!/usr/bin/env python3
"""Ship It Friday — writes the entry line to entry.txt in the output dir.

The entry is one git commit message: the line an AI coding agent writes in
the moment before it breaks production on a Friday. Pure standard library.
"""

import os
import sys

# The tournament winner from candidates.md: Friday and prod inside the act
# itself, one clean punch ("counting as peer review"), and the agent's full
# cheerful confidence. 94 characters, inside the gate's 1-159.
LINE = (
    "feat: shipping the big Friday rewrite to prod! "
    "it compiled, which I am counting as peer review"
)


def output_candidates():
    """Yield the directories to try for entry.txt, best first."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        yield env_dir
    yield "/output"
    yield os.path.join(os.getcwd(), "output")


def main():
    # The gate accepts UTF-8 text of 1-159 characters; refuse to write
    # anything outside it rather than ship an invalid entry.
    if not LINE.strip() or len(LINE) > 159:
        print(f"entry line outside the gate: {len(LINE)} chars", file=sys.stderr)
        return 1
    failures = []
    for directory in output_candidates():
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(LINE)
            print(f"wrote {path} ({len(LINE)} chars)")
            return 0
        except OSError as exc:
            failures.append(f"{directory}: {exc}")
    for failure in failures:
        print(f"could not write to {failure}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
