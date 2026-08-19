#!/usr/bin/env python3
"""
redact_private.py

Runs at build time. Copies source markdown files from subfolders into docs/,
preserving folder hierarchy and stripping PRIVATE blocks along the way.
"""

import re
import shutil
from pathlib import Path

SOURCE_DIR = Path(__file__).resolve().parent.parent          # repo root
BUILD_DIR = SOURCE_DIR / "docs"                             # mkdocs input folder
STATIC_DIR = SOURCE_DIR / "docs_static"                     # static files (index.md, downloads.md, css, images)

SOURCE_FILES = [
    "00_ATOMIC_TABS_Intro/00_ATOMIC_TABS_Intro.md",
    "00_STRING_Governance/00_STRING_Governance.md",
    "02_PARTICLE_Color_Typefaces/02_PARTICLE_Color_Typefaces.md",
    "02_ATOMS_Logos_Imagery/02_ATOMS_Logos_Imagery.md",
    "03_MOLECULE_Logos_Templates/03_MOLECULE_Logos_Templates.md",
    "05_COMPOUND_Identity_References/05_COMPOUND_Identity_References.md",
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

    for rel_path_str in SOURCE_FILES:
        src_path = SOURCE_DIR / rel_path_str
        if not src_path.exists():
            print(f"  ! skipped (not found): {rel_path_str}")
            continue

        raw = src_path.read_text(encoding="utf-8")
        clean = redact(raw)

        # Create destination subfolder inside docs/ if it doesn't exist
        out_path = BUILD_DIR / rel_path_str
        out_path.parent.mkdir(parents=True, exist_ok=True)

        if clean != raw:
            redacted_count += 1
            print(f"  ✓ redacted {raw.count('PRIVATE:START')} block(s) in {rel_path_str}")
        else:
            print(f"  · no redaction needed: {rel_path_str}")

        out_path.write_text(clean, encoding="utf-8")

    # Copy static assets (index.md, downloads.md, stylesheets, images)
    if STATIC_DIR.exists():
        for item in STATIC_DIR.rglob("*"):
            if item.is_file():
                rel = item.relative_to(STATIC_DIR)
                dest = BUILD_DIR / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, dest)
        print(f"  ✓ copied static assets from {STATIC_DIR.name}/")

    # Sanity check: fail build loudly if a private marker leaked
    for out_path in BUILD_DIR.rglob("*.md"):
        if "PRIVATE:" in out_path.read_text(encoding="utf-8"):
            raise SystemExit(
                f"BUILD FAILED: unresolved PRIVATE marker leaked into {out_path.relative_to(BUILD_DIR)}. "
                f"Check marker syntax — build must not publish unredacted content."
            )

    print(f"\nDone. {redacted_count} file(s) had content redacted for the public build.")


if __name__ == "__main__":
    main()