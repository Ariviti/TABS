# Color Swatches
*Annexure to Ariviti Brand Guidelines · Reference: Core BG pages 14–15*

## Full Specification

| Swatch | Hex | RGB | Approx. CMYK* | Role |
|---|---|---|---|---|
| **Vibrant Orange** | `#FF4D1C` | 255, 77, 28 | 0 / 82 / 100 / 0 | Primary — energy, momentum, action |
| **Royal Indigo** | `#3B3EA9` | 59, 62, 169 | 78 / 76 / 0 / 0 | Primary — trust, precision, technology |
| **Dark Indigo** | `#1E1669` | 30, 22, 105 | 90 / 96 / 0 / 30 | Depth variant — headers on light, backgrounds on dark |
| **Soft Black** | `#2E2E2E` | 46, 46, 46 | 0 / 0 / 0 / 88 | Anchor — never pure `#000000` |
| **White** | `#FFFFFF` | 255, 255, 255 | 0 / 0 / 0 / 0 | Secondary — clarity, space, focus |

*CMYK values are approximate sRGB conversions for internal reference only. **Before any offset print run, get a professional Pantone/CMYK match from your printer** — screen-to-print color shift is real and this table is not a substitute for a physical proof.

---

## Usage Ratio (default page composition)

Not specified numerically in core BG — added for design consistency:

- **White / near-white:** ~65–75% of any layout — this is the "clarity" pillar made literal
- **Royal Indigo:** ~15–25% — headers, primary text, structural elements
- **Vibrant Orange:** ~5–10% — CTAs and accents only, never a dominant field color
- **Soft Black:** body text and fine structural lines

**Do:** treat Orange as a spice, not a base — if more than 10% of a layout is orange, you've built a warning page, not a brand page.

---

## Tints & Shades

For UI states (hover, disabled, background fields) — generate programmatically, don't eyeball:

| Color | 20% tint (on white) | 50% tint | 80% shade (toward black) |
|---|---|---|---|
| Royal Indigo | `#D4D5F0` | `#9D9FD4` | `#0C0D22` |
| Vibrant Orange | `#FFE0D3` | `#FFA687` | `#331000` |
| Soft Black | `#E9E9E9` | `#979797` | `#090909` |

**Use case:** Indigo 20% tint = card backgrounds and hover states. Never use Orange tints for large backgrounds — even at 20%, orange fields fight legibility of Indigo text.

---

## Pairing Matrix (cross-referenced with verified contrast data)

| Combination | Verdict | Use Case |
|---|---|---|
| Indigo text on White | ✓ Excellent (8.58:1) | Default body/heading pairing |
| Soft Black text on White | ✓ Excellent (13.58:1) | Long-form body copy |
| White text on Indigo | ✓ Excellent (8.58:1) | Dark section headers, dividers |
| White text on Soft Black | ✓ Excellent (13.58:1) | Footers, dark UI |
| Orange CTA (white text) on White page | ✓ Pass at 24px+ only | Primary buttons — large label required |
| **Orange on Indigo** | ✗ **Never** (2.59:1) | Forbidden in any context |
| Orange as small text/icon anywhere | ✗ Avoid | Reserve orange for large-scale, short elements only |

Full derivation and rationale: see `07_Accessibility.md`.

---

## Gradients

Core BG's "Don'ts" page prohibits gradients **on the logo mark**. It does not authorize free gradient use elsewhere — the cover treatments in the core deck (Indigo-to-black diagonal gradients) are agency-produced backgrounds, not a general license.

**Do:** if a gradient background is needed (event backdrop, deck cover), use Royal Indigo → Dark Indigo → Soft Black only, diagonal, subtle — matching the agency's own cover treatment.
**Don't:** introduce Orange into any gradient, or let anyone outside the brand owner originate a new gradient direction without sign-off.

---

## File Formats to Maintain

A minimum viable, low-maintenance asset kit:

- `.ase` (Adobe swatch) for Illustrator/Photoshop/InDesign
- CSS custom properties (`--ariviti-orange: #FF4D1C;` etc.) for all web/product work
- Figma shared color styles, published from one source library — never recreated per file
