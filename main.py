#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — make.fun entry.

Writes the 302-character rant to /output/entry.txt.
"""

import hashlib
import os
import sys

ENTRY = "Someone replied-all to a 400-person email with just 'Thanks!' Now 47 strangers are replying-all to say 'Please stop replying-all' — each one also replying-all. The thread has achieved sentience. HR sent a third email begging us to stop. Someone replied-all to that one too. I have now muted my own job."

EXPECTED_SHA256 = "6bc6667f0174816493c7db6aaf89c043b0840a664dc1437da6caf5dc01bb8849"


def main():
    # The contest entry must stay exactly 302 characters, byte-identical.
    assert len(ENTRY) == 302, f"entry must be 302 chars, got {len(ENTRY)}"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")
    # Verify the written bytes are exactly the contest entry.
    with open(path, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"ERROR: sha256 mismatch: {digest}", file=sys.stderr)
        return 1
    print(f"Verified sha256: {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
