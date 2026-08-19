# 01 · Particles
*Contains: Color Swatches · Typography System · Accessibility Standards*

Particles are the raw, indivisible values — hex codes, type scales, contrast ratios. Every component in the system (see Strings → Atomic Design Methodology) is built by naming a purposeful application of these particles. Get this file wrong and every downstream asset inherits the error.

---

# Part 1 — Color Swatches
*Reference: Core BG pages 14–15*

## Full Specification

| Swatch | Hex | RGB | Approx. CMYK* | Role |
|---|---|---|---|---|
| **Vibrant Orange** | `#FF4D1C` | 255, 77, 28 | 0 / 82 / 100 / 0 | Primary — energy, momentum, action |
| **Royal Indigo** | `#3B3EA9` | 59, 62, 169 | 78 / 76 / 0 / 0 | Primary — trust, precision, technology |
| **Dark Indigo** | `#1E1669` | 30, 22, 105 | 90 / 96 / 0 / 30 | Depth variant — headers on light, backgrounds on dark |
| **Soft Black** | `#2E2E2E` | 46, 46, 46 | 0 / 0 / 0 / 88 | Anchor — never pure `#000000` |
| **White** | `#FFFFFF` | 255, 255, 255 | 0 / 0 / 0 / 0 | Secondary — clarity, space, focus |

*CMYK values are approximate sRGB conversions for internal reference only. **Before any offset print run, get a professional Pantone/CMYK match from your printer** — screen-to-print color shift is real and this table is not a substitute for a physical proof.

## Usage Ratio (default page composition)

Not specified numerically in core BG — added for design consistency:

- **White / near-white:** ~65–75% of any layout — this is the "clarity" pillar made literal
- **Royal Indigo:** ~15–25% — headers, primary text, structural elements
- **Vibrant Orange:** ~5–10% — CTAs and accents only, never a dominant field color
- **Soft Black:** body text and fine structural lines

**Do:** treat Orange as a spice, not a base — if more than 10% of a layout is orange, you've built a warning page, not a brand page.

## Tints & Shades

For UI states (hover, disabled, background fields) — generate programmatically, don't eyeball:

| Color | 20% tint (on white) | 50% tint | 80% shade (toward black) |
|---|---|---|---|
| Royal Indigo | `#D4D5F0` | `#9D9FD4` | `#0C0D22` |
| Vibrant Orange | `#FFE0D3` | `#FFA687` | `#331000` |
| Soft Black | `#E9E9E9` | `#979797` | `#090909` |

**Use case:** Indigo 20% tint = card backgrounds and hover states. Never use Orange tints for large backgrounds — even at 20%, orange fields fight legibility of Indigo text.

## Pairing Matrix
*Cross-referenced with the verified contrast data in Part 3 of this document*

| Combination | Verdict | Use Case |
|---|---|---|
| Indigo text on White | ✓ Excellent (8.58:1) | Default body/heading pairing |
| Soft Black text on White | ✓ Excellent (13.58:1) | Long-form body copy |
| White text on Indigo | ✓ Excellent (8.58:1) | Dark section headers, dividers |
| White text on Soft Black | ✓ Excellent (13.58:1) | Footers, dark UI |
| Orange CTA (white text) on White page | ✓ Pass at 24px+ only | Primary buttons — large label required |
| **Orange on Indigo** | ✗ **Never** (2.59:1) | Forbidden in any context |
| Orange as small text/icon anywhere | ✗ Avoid | Reserve orange for large-scale, short elements only |

## Gradients

Core BG's "Don'ts" page prohibits gradients **on the logo mark**. It does not authorize free gradient use elsewhere — the cover treatments in the core deck (Indigo-to-black diagonal gradients) are agency-produced backgrounds, not a general license.

**Do:** if a gradient background is needed (event backdrop, deck cover), use Royal Indigo → Dark Indigo → Soft Black only, diagonal, subtle — matching the agency's own cover treatment.
**Don't:** introduce Orange into any gradient, or let anyone outside the brand owner originate a new gradient direction without sign-off.

## File Formats to Maintain

A minimum viable, low-maintenance asset kit:

- `.ase` (Adobe swatch) for Illustrator/Photoshop/InDesign
- CSS custom properties (`--ariviti-orange: #FF4D1C;` etc.) for all web/product work — tracked as a Molecule, see the Molecules manifest
- Figma shared color styles, published from one source library — never recreated per file

---

# Part 2 — Typography System
*Reference: Core BG pages 11–13*

## The Three-Font Rule

Core BG defines three fonts with three distinct, non-overlapping jobs. The single most common brand-compliance failure in any small marketing team is fonts drifting between jobs.

| Font | Job | Never Used For |
|---|---|---|
| **Chillax** | Logo wordmark only | Headings, body, decks, anywhere outside the locked logo file |
| **Space Grotesk** | Headings / display | Body copy, long-form text (its geometric character fatigues the eye at paragraph length) |
| **Plus Jakarta Sans** | Body copy | Headlines, display type (too neutral to carry brand presence at large sizes) |

**Do:** treat Chillax as a locked asset inside the logo file — never install it as a working typeface for content teams.
**Don't:** let a designer "match the vibe" with a geometric-sans lookalike (e.g., Poppins, Sora) when Space Grotesk isn't available in a tool. Install the real font. Substitution is how brand drift starts.

## Type Scale

| Role | Font | Weight | Web Size | Print Size |
|---|---|---|---|---|
| H1 / Display | Space Grotesk | Bold 700 | 48–72px | 36pt |
| H2 | Space Grotesk | SemiBold 600 | 28–36px | 24pt |
| H3 | Plus Jakarta Sans | ExtraBold 800 | 22–26px | 18pt |
| Body | Plus Jakarta Sans | Regular 400 | 16–18px min | 11pt min |
| Pull quotes / testimonials | Plus Jakarta Sans | Medium 500 | 20–24px | 16pt |
| Captions / metadata | Plus Jakarta Sans | Regular 400 | 13–14px | 9pt |

**Line height:** 1.6 for body, 1.15 for headings — tighter headings read as confident (Strings → Design Philosophy pillar), looser body reads as clear.

**Note on emphasis:** no weight or role in this system uses italics. Emphasis is carried by weight (bold), color (Orange for kickers), or size — never by slant. This applies everywhere, including HTML/email templates in the Compounds manifest.

## Numerals & Metrics

Not addressed in core BG — filling the gap, since metrics are central to Evidence-first voice (Strings → Voice, Tone & Vocabulary).

- Use **Space Grotesk Bold** for standalone large metrics (proof blocks, stat callouts) — the geometric weight gives numbers visual authority distinct from surrounding body copy.
- Use **Plus Jakarta Sans** for inline numbers within body sentences — switching fonts mid-sentence for a single digit is a common over-engineering mistake; don't do it.
- Never use a monospace font for data unless a future brand decision explicitly introduces one. The current system has no mono font — don't invent one under deadline pressure.

## Do / Don't

| Do | Don't |
|---|---|
| Load both fonts as web fonts with proper fallback stacks (`Space Grotesk, sans-serif` / `Plus Jakarta Sans, sans-serif`) | Fall back silently to system fonts — Arial/Calibri substitution is a brand violation, not a technical inconvenience |
| Keep body text at 16px minimum on every surface, no exceptions | Shrink body copy to fit a layout — resize the layout instead |
| Use weight and size to create hierarchy | Use color alone to create hierarchy (fails accessibility, see Part 3 below) |
| Left-align body text | Justify body text (creates uneven word-spacing "rivers," reads as low-budget) |

---

# Part 3 — Accessibility Standards
*Not covered in core BG — critical gap, closed here with verified numbers*

## Why This Section Is Non-Optional

Accessibility is not a legal checkbox layered on top of the brand — it *is* brand architecture. A color pairing that fails contrast fails the "Clarity" pillar (Strings → Design Philosophy) for a meaningful share of real readers, regardless of how it looks to the designer choosing it.

## Verified Contrast Ratios (WCAG 2.1)

Calculated directly from the core BG hex values in Part 1 above — not estimated.

| Pairing | Ratio | Normal Text (needs 4.5:1) | Large Text 24px+ (needs 3:1) |
|---|---|---|---|
| Royal Indigo `#3B3EA9` on White | **8.58:1** | ✓ Pass | ✓ Pass |
| Dark Indigo `#1E1669` on White | **15.28:1** | ✓ Pass | ✓ Pass |
| Soft Black `#2E2E2E` on White | **13.58:1** | ✓ Pass | ✓ Pass |
| **Vibrant Orange `#FF4D1C` on White** | **3.32:1** | ✗ **Fail** | ✓ Pass (large only) |
| Vibrant Orange on Soft Black | **4.09:1** | ✗ Fail (marginal) | ✓ Pass |
| Vibrant Orange on Royal Indigo | **2.59:1** | ✗ **Fail** | ✗ **Fail — never use** |

### The Load-Bearing Rule

**Vibrant Orange is a large-scale, short-text-only color.** It is your most energetic brand asset and your least accessible one — the guidelines' "energy and momentum" color is, by the physics of the color itself, unsuitable for anything read at length.

| Use Orange For | Never Use Orange For |
|---|---|
| CTA buttons (short label, large type, 24px+) | Body copy, at any size |
| Large display numerals in proof blocks | Data labels, captions, legal/fine print |
| Icon accents, dividers, underlines | Text on Royal Indigo background — 2.59:1 is a hard fail at any size |
| Logo, brand marks | Small UI text — form labels, error messages, table headers |

**Do:** pair Orange CTAs with white or near-white backgrounds and keep the label under 4 words at 24px+.
**Don't:** ever place Orange text on Indigo — this combination fails at every text size and should be flagged automatically in any design-review checklist.

## Standards Checklist

| Standard | Requirement | Ariviti Application |
|---|---|---|
| WCAG 2.1 AA | 4.5:1 normal text, 3:1 large text | Use Indigo, Dark Indigo, or Soft Black for all body/UI text. Orange reserved per table above. |
| Minimum font size | 16px web body / 11pt print | Enforced in the Type Scale token set (Part 2) — no manual overrides |
| Alt text | Every image, descriptive | Format: `[Subject] doing [action] — [context]. Ariviti brand photograph.` (see Atoms doc, Photography) |
| Keyboard navigation | All interactive elements reachable and visibly focused | Verify before every page launch — add to the launch checklist, not a post-launch audit |
| Video captions | All video content captioned | Human-reviewed before publishing, not auto-caption-only |
| Color-blind safety | Never color alone conveys meaning | Every status indicator pairs color with an icon or label — e.g., a "validated" badge always carries a ✓ or the word "Verified," never just a green fill |
| Data visualization | Max 3 colors per chart, always labeled | Orange + Indigo + Soft Black is the default 3-color chart palette; label every series directly, don't rely on a legend alone |

## The Fragility Score

A quick self-audit for any new asset — score 0 (fail) or 1 (pass) per item, sum out of 6:

1. Body/UI text meets 4.5:1 contrast
2. No Orange-on-Indigo anywhere
3. Every image has real (non-generic) alt text
4. Every status/meaning indicator has a non-color cue
5. Font size ≥16px web / 11pt print, no exceptions
6. Chart/visualization uses ≤3 colors, all labeled

**5–6/6:** ship it. **3–4/6:** fix before external distribution. **0–2/6:** the asset is not brand-compliant regardless of how it looks — send it back.

This score is referenced directly in the Brand Health Scorecard (Strings → Implementation & Governance) as the quarterly audit mechanism.
