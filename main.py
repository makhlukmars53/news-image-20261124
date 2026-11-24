"""Entry point for news-image-20261124.

Copies the bundled news image to the output directory make.fun reads.
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    with open(SOURCE, "rb") as src, open(dest, "rb") as out:
        if src.read() != out.read():
            raise SystemExit("output bytes differ from entry.png")
    print("wrote", dest)


if __name__ == "__main__":
    sys.exit(main())
