#!/usr/bin/env python3
"""
redact_private.py

Runs at build time, never by hand. It copies every source .md file into the
mkdocs docs/ folder, stripping anything wrapped in PRIVATE markers along
the way. If a PRIVATE block is immediately followed by a PUBLIC block,
the PUBLIC block's content is kept (unwrapped) in its place.

Marker syntax (HTML comments — invisible when rendered normally):
    <!-- PRIVATE:START reason="..." -->  sensitive content  <!-- PRIVATE:END -->
    <!-- PUBLIC:START -->                fallback content   <!-- PUBLIC:END -->

Source files (private repo, single source of truth) are never modified
by this script. Output only ever goes to the gitignored docs/ build folder.
"""

import re
import shutil
from pathlib import Path

SOURCE_DIR = Path(__file__).resolve().parent.parent          # repo root
BUILD_DIR = SOURCE_DIR / "docs"                     # mkdocs input folder (gitignored)
STATIC_DIR = SOURCE_DIR / "docs_static"             # committed: index.md, css, images — never redacted

SOURCE_FILES = [
    "00-intro.md",
    "01-strings.md",
    "02-particles.md",
    "03-atoms.md",
    "04-molecules.md",
    "05-compounds.md",
]

PRIVATE_BLOCK = re.compile(
    r"<!--\s*PRIVATE:START.*?-->.*?<!--\s*PRIVATE:END\s*-->"
    r"(?:\s*<!--\s*PUBLIC:START\s*-->(.*?)<!--\s*PUBLIC:END\s*-->)?",
    re.DOTALL,
)


def redact(text: str) -> str:
    def _sub(match: re.Match) -> str:
        public_fallback = match.group(1)
        return public_fallback.strip() if public_fallback else ""
    return PRIVATE_BLOCK.sub(_sub, text)


def main() -> None:
    BUILD_DIR.mkdir(exist_ok=True)
    redacted_count = 0

    for filename in SOURCE_FILES:
        src_path = SOURCE_DIR / filename
        if not src_path.exists():
            print(f"  ! skipped (not found): {filename}")
            continue

        raw = src_path.read_text(encoding="utf-8")
        clean = redact(raw)

        if clean != raw:
            redacted_count += 1
            print(f"  ✓ redacted {raw.count('PRIVATE:START') if 'PRIVATE:START' in raw else 0} block(s) in {filename}")
        else:
            print(f"  · no redaction needed: {filename}")

        (BUILD_DIR / filename).write_text(clean, encoding="utf-8")

    # sanity check: fail the build loudly if a marker leaked through
    for filename in SOURCE_FILES:
        out_path = BUILD_DIR / filename
        if out_path.exists() and "PRIVATE:" in out_path.read_text(encoding="utf-8"):
            raise SystemExit(
                f"BUILD FAILED: unresolved PRIVATE marker leaked into {filename}. "
                f"Check marker syntax — build must not publish unredacted content."
            )

    # Copy static assets (index.md, stylesheets, images) through untouched.
    # These live outside SOURCE_FILES entirely — nothing in docs_static/
    # is ever subject to redaction, so nothing sensitive should ever be
    # placed there. Sensitive content only ever exists inside the six
    # SOURCE_FILES above, guarded by PRIVATE markers.
    if STATIC_DIR.exists():
        for item in STATIC_DIR.rglob("*"):
            if item.is_file():
                rel = item.relative_to(STATIC_DIR)
                dest = BUILD_DIR / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, dest)
        print(f"  ✓ copied static assets from {STATIC_DIR.name}/")

    print(f"\nDone. {redacted_count} file(s) had content redacted for the public build.")


if __name__ == "__main__":
    main()
