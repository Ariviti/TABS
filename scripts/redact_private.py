#!/usr/bin/env python3
"""
redact_private.py

Runs at build time, never by hand. Copies every source .md file into the
mkdocs docs/ folder, stripping anything wrapped in PRIVATE markers along
the way. If a PRIVATE block is immediately followed by a PUBLIC block,
the PUBLIC block's content is kept (unwrapped) in its place.
"""

import re
import shutil
from pathlib import Path

SOURCE_DIR = Path(__file__).resolve().parent.parent          # repo root
BUILD_DIR = SOURCE_DIR / "docs"                             # mkdocs input folder (gitignored)
STATIC_DIR = SOURCE_DIR / "docs_static"                     # committed: index.md, downloads.md, css, images

# Mapping: "Folder/Filename.md" -> "Target filename expected by mkdocs"
SOURCE_FILE_MAP = {
    "00_ATOMIC_TABS_Intro/00_ATOMIC_TABS_Intro.md": "00-intro.md",
    "00_STRING_Governance/00_STRING_Governance.md": "01-strings.md",
    "02_PARTICLE_Color_Typefaces/02_PARTICLE_Color_Typefaces.md": "02-particles.md",
    "02_ATOMS_Logos_Imagery/02_ATOMS_Logos_Imagery.md": "03-atoms.md",
    "03_MOLECULE_Logos_Templates/03_MOLECULE_Logos_Templates.md": "04-molecules.md",
    "05_COMPOUND_Identity_References/05_COMPOUND_Identity_References.md": "05-compounds.md",
}

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

    for src_rel_path, target_filename in SOURCE_FILE_MAP.items():
        src_path = SOURCE_DIR / src_rel_path
        if not src_path.exists():
            print(f"  ! skipped (not found): {src_rel_path}")
            continue

        raw = src_path.read_text(encoding="utf-8")
        clean = redact(raw)

        if clean != raw:
            redacted_count += 1
            print(f"  ✓ redacted {raw.count('PRIVATE:START')} block(s) in {src_rel_path}")
        else:
            print(f"  · no redaction needed: {src_rel_path}")

        (BUILD_DIR / target_filename).write_text(clean, encoding="utf-8")

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
    for out_path in BUILD_DIR.glob("*.md"):
        if "PRIVATE:" in out_path.read_text(encoding="utf-8"):
            raise SystemExit(
                f"BUILD FAILED: unresolved PRIVATE marker leaked into {out_path.name}. "
                f"Check marker syntax — build must not publish unredacted content."
            )

    print(f"\nDone. {redacted_count} file(s) had content redacted for the public build.")


if __name__ == "__main__":
    main()