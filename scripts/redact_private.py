#!/usr/bin/env python3
"""
redact_private.py

Build step: Process all markdown files, strip PRIVATE blocks,
and stage everything into docs/ for MkDocs.
"""

import re
import shutil
from pathlib import Path

SOURCE_DIR = Path(__file__).resolve().parent.parent          # repo root
BUILD_DIR = SOURCE_DIR / "docs"                             # staged build folder

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
    # 1. Reset build folder
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)

    redacted_count = 0
    processed_count = 0

    # 2. Process all .md files (root index.md & subfolder docs)
    for path in SOURCE_DIR.rglob("*.md"):
        rel_parts = path.relative_to(SOURCE_DIR).parts
        # Skip internal build/script/git folders
        if any(p in {"docs", "site", ".git", ".venv", "scripts", "docs_static"} for p in rel_parts):
            continue

        rel_path = path.relative_to(SOURCE_DIR)
        raw = path.read_text(encoding="utf-8")
        clean = redact(raw)

        out_path = BUILD_DIR / rel_path
        out_path.parent.mkdir(parents=True, exist_ok=True)

        if clean != raw:
            redacted_count += 1
            print(f"  ✓ redacted {raw.count('PRIVATE:START')} block(s) in {rel_path}")
        else:
            print(f"  · processed: {rel_path}")

        out_path.write_text(clean, encoding="utf-8")
        processed_count += 1

    # 3. Copy CSS tokens file to docs/
    css_file = SOURCE_DIR / "ariviti-tokens.css"
    if css_file.exists():
        shutil.copy2(css_file, BUILD_DIR / "ariviti-tokens.css")
        print("  ✓ copied ariviti-tokens.css")

    # 4. Copy logo assets folder to docs/02_ATOM_Logo_Core
    logo_dir = SOURCE_DIR / "02_ATOM_Logo_Core"
    if logo_dir.exists():
        shutil.copytree(logo_dir, BUILD_DIR / "02_ATOM_Logo_Core")
        print(f"  ✓ copied logo assets from {logo_dir.name}/")

    # Sanity check: prevent secret leaks
    for out_path in BUILD_DIR.rglob("*.md"):
        if "PRIVATE:" in out_path.read_text(encoding="utf-8"):
            raise SystemExit(
                f"BUILD FAILED: PRIVATE marker leaked into {out_path.relative_to(BUILD_DIR)}."
            )

    print(f"\nDone. Processed {processed_count} markdown file(s) ({redacted_count} redacted).")


if __name__ == "__main__":
    main()