"""Wednesday 18 November 2026 — in one image (dense V6, variant E).

Copies the finished front-page image to /output/entry.png. The image is a
JPEG; the competition accepts JPEG bytes at that path (told apart by the
file's first bytes).
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "image.jpg"
    if not source.is_file() or source.stat().st_size == 0:
        raise FileNotFoundError(f"missing or empty image: {source}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()
