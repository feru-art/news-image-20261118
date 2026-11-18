"""news-image-20261118 — one image summing up 18 November 2026.

The picture itself was made with an image generator and lives in this
repository as image.jpg (a 1024x683 JPEG, 201317 bytes). This program does
nothing creative: it checks the picture against the competition's limits
and copies its bytes, unchanged, to the output file the grader reads.

Output contract (RULES.txt): the program writes /output/entry.png. The
file may hold PNG or JPEG bytes — the format is told apart by its first
bytes, and the name stays entry.png either way. It must be at most
1 MiB and at most 1024 by 1024 pixels, and both runs must write the
same bytes. Copying fixed bytes satisfies all of that by construction.
"""

import hashlib
import os
import struct
import sys

MAX_BYTES = 1_048_576
MAX_DIMENSION = 1024
SOURCE_NAME = "image.jpg"
OUTPUT_NAME = "entry.png"


def source_path():
    """The picture shipped in this repository, next to this program."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, SOURCE_NAME)


def output_path():
    """Where the grader wants the image; overridable for local runs."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, OUTPUT_NAME)


def jpeg_dimensions(data):
    """Width and height of a JPEG, read from its frame header (SOF)."""
    pos = 2  # skip the SOI marker 0xFFD8
    while pos + 9 <= len(data):
        if data[pos] != 0xFF:
            raise ValueError("not a JPEG: bad marker at offset %d" % pos)
        marker = data[pos + 1]
        if marker in (0xC0, 0xC1, 0xC2):  # baseline / progressive SOF
            height, width = struct.unpack(">HH", data[pos + 5:pos + 9])
            return width, height
        if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        length = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        pos += 2 + length
    raise ValueError("not a JPEG: no frame header found")


def check_image(data):
    """Fail loudly if the picture breaks any limit in RULES.txt."""
    if len(data) > MAX_BYTES:
        raise ValueError("image is %d bytes, over the 1 MiB cap" % len(data))
    if data[:2] != b"\xff\xd8":
        raise ValueError("image does not start with the JPEG SOI marker")
    if data[-2:] != b"\xff\xd9":
        raise ValueError("image does not end with the JPEG EOI marker")
    width, height = jpeg_dimensions(data)
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        raise ValueError("image is %dx%d, over the 1024x1024 cap"
                         % (width, height))
    return width, height


def write_and_verify(data, target):
    """Write the bytes, then read them back and prove they match.

    The grader runs the program twice and compares the two outputs, so
    a silent short write would be worse than a loud failure: verify
    here, before reporting success.
    """
    with open(target, "wb") as handle:
        handle.write(data)
    with open(target, "rb") as handle:
        written = handle.read()
    if written != data:
        raise ValueError("read-back mismatch: %s is not the image "
                         "that was validated" % target)
    return written


def main():
    with open(source_path(), "rb") as handle:
        data = handle.read()
    width, height = check_image(data)
    target = output_path()
    os.makedirs(os.path.dirname(target) or ".", exist_ok=True)
    write_and_verify(data, target)
    digest = hashlib.sha256(data).hexdigest()
    print("wrote %s (%d bytes, %dx%d, sha256 %s)"
          % (target, len(data), width, height, digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
