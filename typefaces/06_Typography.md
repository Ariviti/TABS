# Typography System
*Annexure to Ariviti Brand Guidelines · Reference: Core BG pages 11–13*

## The Three-Font Rule

Core BG defines three fonts with three distinct, non-overlapping jobs. The single most common brand-compliance failure in any small marketing team is fonts drifting between jobs. This document exists to prevent that.

| Font | Job | Never Used For |
|---|---|---|
| **Chillax** | Logo wordmark only | Headings, body, decks, anywhere outside the locked logo file |
| **Space Grotesk** | Headings / display | Body copy, long-form text (its geometric character fatigues the eye at paragraph length) |
| **Plus Jakarta Sans** | Body copy | Headlines, display type (too neutral to carry brand presence at large sizes) |

**Do:** treat Chillax as a locked asset inside the logo file — never install it as a working typeface for content teams.
**Don't:** let a designer "match the vibe" with a geometric-sans lookalike (e.g., Poppins, Sora) when Space Grotesk isn't available in a tool. Install the real font. Substitution is how brand drift starts.

---

## Type Scale

| Role | Font | Weight | Web Size | Print Size |
|---|---|---|---|---|
| H1 / Display | Space Grotesk | Bold 700 | 48–72px | 36pt |
| H2 | Space Grotesk | SemiBold 600 | 28–36px | 24pt |
| H3 | Plus Jakarta Sans | ExtraBold 800 | 22–26px | 18pt |
| Body | Plus Jakarta Sans | Regular 400 | 16–18px min | 11pt min |
| Pull quotes / testimonials | Plus Jakarta Sans | Italic 500 | 20–24px | 16pt |
| Captions / metadata | Plus Jakarta Sans | Regular 400 | 13–14px | 9pt |

**Line height:** 1.6 for body, 1.15 for headings — tighter headings read as confident (Design Philosophy pillar), looser body reads as clear.

---

## Numerals & Metrics

Not addressed in core BG — filling the gap, since metrics are central to Evidence-first voice.

- Use **Space Grotesk Bold** for standalone large metrics (proof blocks, stat callouts) — the geometric weight gives numbers visual authority distinct from surrounding body copy.
- Use **Plus Jakarta Sans** for inline numbers within body sentences — switching fonts mid-sentence for a single digit is a common over-engineering mistake; don't do it.
- Never use a monospace font for data unless a future brand decision explicitly introduces one. The current system has no mono font — don't invent one under deadline pressure.

---

## Do / Don't

| Do | Don't |
|---|---|
| Load both fonts as web fonts with proper fallback stacks (`Space Grotesk, sans-serif` / `Plus Jakarta Sans, sans-serif`) | Fall back silently to system fonts — Arial/Calibri substitution is a brand violation, not a technical inconvenience |
| Keep body text at 16px minimum on every surface, no exceptions | Shrink body copy to fit a layout — resize the layout instead |
| Use weight and size to create hierarchy | Use color alone to create hierarchy (fails accessibility, see next doc) |
| Left-align body text | Justify body text (creates uneven word-spacing "rivers," reads as low-budget) |

---

## Accessibility Minimums (cross-reference)

- **16px web / 11pt print** body — no exceptions, enforced at the token level, not the reviewer level.
- Never rely on font-weight alone (e.g., bold vs. regular) to convey meaning for screen-reader users — pair with semantic HTML heading tags in all web builds.

See `07_Accessibility.md` for full contrast and compliance detail.
