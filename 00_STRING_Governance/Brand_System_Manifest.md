# Ariviti Brand System — Manifest

Single index of every file delivered across this build, organized by the
atomic-design tier structure this system follows. See `Living_Style_Guide/index.html`
for the visual/rendered version of this same information.

**Note on scope:** this manifest covers everything built in this conversation.
It is not the same taxonomy as any separate "TABS" repository system you may
be running elsewhere — that system has its own `04-molecules.md` build
manifest with its own canonical values. If reconciling the two, treat that
repo's `02-particles.md` as authoritative for any color/type value conflict;
this manifest's tokens were derived independently and are a starting point
for that repo, not a replacement for it.

---

## 01 · Particle (indivisible tokens)

| File | Status |
|---|---|
| `Palette_Primary.ase`, `Palette_Secondary.ase`, `Palette_Print_CMYK.ase` | 🟢 Shipped — byte-verified via round-trip parse |
| `tokens_color.json`, `colors.css`, `colors.scss` | 🟢 Shipped |
| `colors_accessible_addendum.css` | 🟢 Shipped — WCAG-corrected supplementary shades |
| `tokens_typography.json`, `typography.css`, `typography.scss` | 🟢 Shipped |
| `Icon_Library.zip` (36 icons × 6 color variants + sprite) | 🟢 Shipped |
| `Generate_Palette_Apple_clr.applescript` | 🟢 Shipped — generator, not a hand-forged binary (see reasoning in its own file) |
| Logo vector (.ai/.eps/.svg), brand font files (.ttf/.otf) | ⏳ **You're handling separately** |

## 02 · Atom (smallest composed pieces)

| File | Status |
|---|---|
| Web Component Library — React ×6, Vue ×6, pixel-identical | 🟢 Shipped |
| `Chart_Style_Gallery.pptx` (4 native, editable charts) | 🟢 Shipped — replaces a hand-forged `.crtx` (see its README) |
| `Imagery_Guide.zip` (crop ratios, duotone treatment spec) | 🟢 Shipped — awaiting real photography to apply the rules to |
| `Figma_Tokens/ariviti.tokens.json` | 🟢 Shipped — bridge into Figma via Tokens Studio plugin, not a hand-forged `.fig` |
| Figma component file (native `.fig`) | ⚪ **Deliberately not built** — undocumented proprietary binary, no verification path |

## 03 · Molecule (reusable document/page shells)

| File | Status |
|---|---|
| `Ariviti_Proposal.potx` (22 layouts, MBB-hybrid) | 🟢 Shipped |
| `Ariviti_Presentation.potx`, `Ariviti_Report_POV.potx`, `Ariviti_Internal.potx`, `Ariviti_OnePager.potx`, `Ariviti_Brochure.potx`, `Printable_4x3_Master.potx` | 🟢 Shipped |
| `Corporate_Document_Master.dotx`, `Formal_Letterhead_Master.dotx` | 🟢 Shipped |
| `Email_Header_Footer_Wrapper.mjml` / `.html` | 🟢 Shipped |
| `Email_Signature_Template.html` | 🟢 Shipped |
| `Social_Templates.zip` (LinkedIn post, LinkedIn banner, OG image) | 🟢 Shipped |
| Business card / stationery die-line | ⚪ **Not built** — flag if you want it |
| `Palette_Print_CMYK.acb` (Adobe Color Book) | ⚪ **Deliberately not built** — see `01_PARTICLE_Color/README.md` |

## 04 · Organism (full assemblies)

| File | Status |
|---|---|
| `Demo_Monthly_Newsletter_Live.html`/`.mjml`, `Demo_Product_Announcement_Email.html`/`.mjml`, `Demo_Landing_Page.html` | 🟢 Shipped |
| `Living_Style_Guide/index.html` | 🟢 Shipped |

## Governance

| File | Status |
|---|---|
| `WCAG_Contrast_Audit.md` | 🟢 Shipped — 21 pairings audited, 6 findings, all 6 remediated with verified fixes |
| This manifest | 🟢 Shipped |

---

## What's genuinely still open

1. **Logo vector + brand font files** — yours, incoming separately.
2. **Business card / stationery die-line** — not built; real print production
   also needs the brochure's caveat (no bleed/trim in a plain HTML/PPTX
   pipeline) — worth a scoped follow-up once you confirm you want it.
3. **Applying the WCAG-corrected tokens to already-shipped files** — the
   audit documents and verifies the fixes, but hasn't gone back and patched
   every instance of the old orange/success/warning/danger values across
   15+ already-delivered files. That's a real, scoped patch pass, not a
   config flag.
4. **The TABS repo itself** — if that's where this system is meant to live
   long-term, none of today's output is wired into it. Everything here is
   portable (plain files, no repo dependency) and ready to be forward-fit
   once that repo's actual canonical token values are available to
   transcribe from.
