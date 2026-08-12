# Accessibility Standards
*Annexure to Ariviti Brand Guidelines · Not covered in core BG — critical gap, closed here with verified numbers*

## Why This Document Is Non-Optional

Accessibility is not a legal checkbox layered on top of the brand — it *is* brand architecture. A color pairing that fails contrast fails the "Clarity" pillar for a meaningful share of real readers, regardless of how it looks to the designer choosing it.

---

## Verified Contrast Ratios (WCAG 2.1)

Calculated directly from the core BG hex values — not estimated.

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

---

## Standards Checklist

| Standard | Requirement | Ariviti Application |
|---|---|---|
| WCAG 2.1 AA | 4.5:1 normal text, 3:1 large text | Use Indigo, Dark Indigo, or Soft Black for all body/UI text. Orange reserved per table above. |
| Minimum font size | 16px web body / 11pt print | Enforced in Typography doc token set — no manual overrides |
| Alt text | Every image, descriptive | Format: `[Subject] doing [action] — [context]. Ariviti brand photograph.` (see Photography doc) |
| Keyboard navigation | All interactive elements reachable and visibly focused | Verify before every page launch — add to the launch checklist, not a post-launch audit |
| Video captions | All video content captioned | Human-reviewed before publishing, not auto-caption-only |
| Color-blind safety | Never color alone conveys meaning | Every status indicator pairs color with an icon or label — e.g., a "validated" badge always carries a ✓ or the word "Verified," never just a green fill |
| Data visualization | Max 3 colors per chart, always labeled | Orange + Indigo + Soft Black is the default 3-color chart palette; label every series directly, don't rely on a legend alone |

---

## The Fragility Score

A quick self-audit for any new asset — score 0 (fail) or 1 (pass) per item, sum out of 6:

1. Body/UI text meets 4.5:1 contrast
2. No Orange-on-Indigo anywhere
3. Every image has real (non-generic) alt text
4. Every status/meaning indicator has a non-color cue
5. Font size ≥16px web / 11pt print, no exceptions
6. Chart/visualization uses ≤3 colors, all labeled

**5–6/6:** ship it. **3–4/6:** fix before external distribution. **0–2/6:** the asset is not brand-compliant regardless of how it looks — send it back.
