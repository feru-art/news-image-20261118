"""news-image-20261118 — dense front page, variant B (slot 2).

Copies the finished front-page image (JPEG bytes) to the output path
the competition reads, /output/entry.png. The image itself is a
finished newspaper front page summing up Wednesday 18 November 2026;
this program only moves its bytes, it does not draw anything.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "image.jpg"
OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"


def main() -> None:
    if not SOURCE.is_file() or SOURCE.stat().st_size == 0:
        raise FileNotFoundError(f"missing image: {SOURCE}")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)


if __name__ == "__main__":
    main()
