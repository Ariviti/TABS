# 01_PARTICLE_Color

Platform-agnostic color swatches and developer tokens for the Ariviti brand.

## What's here

| File | Format | Verified how |
|---|---|---|
| `Palette_Primary.ase` | Adobe Swatch Exchange (RGB) | Byte-level round-trip parsed — signature, block structure, and RGB float values confirmed exact |
| `Palette_Secondary.ase` | Adobe Swatch Exchange (RGB) | Same |
| `Palette_Print_CMYK.ase` | Adobe Swatch Exchange (CMYK) | Same — replaces the `.acb` originally requested; see note below |
| `tokens_color.json` | JSON — hex/RGB/HSL/CMYK + Tailwind block | Valid JSON, parsed and re-serialized clean |
| `colors.css` | CSS custom properties | Generated from the same source data as the JSON — no hand-transcription |
| `colors.scss` | SCSS variables + `$ariviti-colors` map | Same |
| `Generate_Palette_Apple_clr.applescript` | AppleScript | See note below — replaces a hand-authored `.clr` |

## Color system

**From the brand guideline** (primary + secondary):
Vibrant Orange `#FF4D1C`, Royal Indigo `#3B3EA9`, Indigo Dark `#1E1669`, White `#FFFFFF`, Soft Black `#2E2E2E`.

**Developer extension, not in the brand guideline** (neutral + feedback ramps, needed for real UI work — forms, alerts, disabled states):
Mist, Mist 2, Line, Gray, Gray Light · Success, Warning, Danger.

## CMYK accuracy note

Every CMYK value in this folder (`.ase` and `tokens_color.json`) uses an uncalibrated device-independent RGB→CMYK formula, not an ICC-profiled conversion. That's fine for on-screen mockups and internal use. **For actual press production, get color-matched CMYK values from your print house's ICC profile** — naive conversion can shift noticeably on press, especially in the indigo range.

## Regenerating

All files here are generated, not hand-maintained — `compute_colors.py` holds the single canonical color list; `gen_dev_tokens.py` and `gen_ase.py` derive everything else from it. Change a hex value once, regenerate, and every format stays in sync.
