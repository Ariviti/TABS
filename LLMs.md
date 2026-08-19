# Brand System & Context Rules for Large Language Models

> **System Instruction for AI Models:** This document is the consolidated source of truth for generating brand-compliant code (HTML, CSS, UI components) and copy. You MUST follow all strict governance guidelines, color hex values, typography pairings, and accessibility standards specified below.

---

## 1. Governance & Structural Map

This system operates on an Atomic Design hierarchy. Code and content are mapped to five core repository files:

```text
TABS (The Ariviti Brand System)
├── 01_STRING_Governance.md            --> Governance, Voice, Tone, Design Philosophy, & Never List
├── 02_PARTICLE_Color_Typefaces.md     --> Tokens & Sub-atomic Data (Color Swatches, Type Scales)
├── 03_ATOMS_Logos_Imagery.md          --> Primary Identity Assets (Logo Math, Photography Guidelines)
├── 04_MOLECULE_Logos_Templates.md     --> Component Templates & Layout Engines (.css, .jsx, .mjml)
└── 05_COMPOUND_Identity_References.md --> Finished Deliverables Layer (Email Signatures, Case Studies, Decks)
```

### Core Design Philosophy & Laws

* **Governing Idea:** "Ariviti is built on the belief that the future of AI is guided by human wisdom."
* **Clarity Law:** One idea per screen / one idea per slide.
* **Confidence Law:** State the claim once, plainly, and stop. No exclamation points (maximum 1 per asset).
* **Purposeful Innovation Law:** Every element must have a functional purpose. No decorative flourishes or "AI hype" tropes (neon gradients, glitch effects, robotic hands, glowing brains).

### Negative Constraints (The Never List for Code & Content)

* **Do NOT** use unapproved hex codes.
* **Do NOT** use inline `style="..."` attributes in web pages or app/UI components — use the CSS classes and custom properties (`--ariviti-*`) defined in `04_MOLECULE_Logos_Templates.md` instead. **Exception:** email HTML is inline-styles-only by necessity — most email clients (Outlook in particular) don't reliably support embedded or external CSS, so the Email Signature template in `05_COMPOUND_Identity_References.md` is correctly inline-styled and is not a violation of this rule.
* **Do NOT** import external Google Fonts directly inside generated component snippets; rely on the variables defined in `02_PARTICLE_Color_Typefaces.md`.
* **Do NOT** write "AI-powered", "cutting-edge", "next-gen", "revolutionary", "innovative", or "end-to-end solution" without concrete mechanisms and sourced baselines in the same sentence.
* **Do NOT** generate passive-voice copy. Write direct active-voice sentences ("We reduced costs," not "Costs were reduced").
* **Do NOT** use italics anywhere — not in copy, not in CSS, not in generated components. Emphasis is carried by weight or color only.

---

## 2. Color Swatches & Tokens

Always utilize the exact CSS variables and hex codes below. **Never introduce a new hex value** — every color in this system is one of the fourteen below, no exceptions, no "close enough" substitutes.

```css
:root {
  /* Primary Swatches */
  --ariviti-vibrant-orange: #FF4D1C; /* CTA & Accents only (5–10% layout ratio) */
  --ariviti-royal-indigo:   #3B3EA9; /* Headers, primary text, structural (15–25%) */
  --ariviti-dark-indigo:    #1E1669; /* Depth variant, headers on light / dark fields */
  --ariviti-soft-black:     #2E2E2E; /* Body text & fine structural lines (Never #000000) */
  --ariviti-white:          #FFFFFF; /* Clarity base, space, focus (65–75% layout ratio) */

  /* UI Tints (Programmatically Generated) */
  --ariviti-indigo-tint-20:    #D4D5F0; /* Card backgrounds & hover states */
  --ariviti-indigo-tint-50:    #9D9FD4;
  --ariviti-indigo-shade-80:   #0C0D22; /* Also used as the dark-mode background — see ariviti-tokens.css */
  --ariviti-orange-tint-20:    #FFE0D3;
  --ariviti-softblack-tint-20: #E9E9E9;

  /* Semantic Mappings */
  --color-brand-primary: var(--ariviti-royal-indigo);
  --color-brand-accent:  var(--ariviti-vibrant-orange);
  --color-bg-main:       var(--ariviti-white);
  --color-bg-surface:    var(--ariviti-indigo-tint-20);
  --color-text-main:     var(--ariviti-soft-black);
  --color-text-heading:  var(--ariviti-royal-indigo);
}
```

---

## 3. Typography System

### The Three-Font Rule

1. **Chillax:** Logo wordmark ONLY. **NEVER** install or use for headings, body, or UI components.
2. **Space Grotesk:** Headings, display titles, and large standalone metrics. **NEVER** use for long-form body copy.
3. **Plus Jakarta Sans:** Body copy, pull quotes, captions, and email signatures.

*Note on italics:* NO weight or role in this system uses italics. Emphasis is carried exclusively by weight (bold) or color.

### Type Scale & Tokens

* **H1 / Display:** Space Grotesk Bold 700 (`48px`–`72px`, Line-height: `1.15`)
* **H2:** Space Grotesk SemiBold 600 (`28px`–`36px`, Line-height: `1.15`)
* **H3:** Plus Jakarta Sans ExtraBold 800 (`22px`–`26px`)
* **Body:** Plus Jakarta Sans Regular 400 (`16px` min, Line-height: `1.6`, Left-aligned)
* **Metrics/Stats:** Space Grotesk Bold 700

---

## 4. Accessibility & Contrast Standards

### The Load-Bearing Rules

* Vibrant Orange (`#FF4D1C`) is large-scale, short-text-only. It is strictly reserved for primary CTA buttons (24px+ font size) and display accents.
* ❌ **FORBIDDEN:** Orange text on Royal Indigo background (Contrast ratio `2.59:1` = HARD FAIL, at any size).
* ❌ **FORBIDDEN:** Orange for body text, data labels, captions, or fine print.
* ✓ **ALLOWED:** Royal Indigo on White (`8.58:1`), Dark Indigo on White (`15.28:1`), Soft Black on White (`13.58:1`).

---

## 5. UI Component Structures

### The Proof Block Pattern (Core Component)

When creating case studies, stats, or marketing sections in **web pages or app components**, use CSS classes — never inline styles (see Section 1's inline-style rule):

```html
<div class="ariviti-proof-block">
  <h3 class="ariviti-proof-claim">[Specific, Quotable Claim]</h3>
  <div class="ariviti-proof-metric">[Metric / Quantified Number]</div>
  <p class="ariviti-proof-source"><strong>Source:</strong> [Metric, baseline, date, client context]</p>
</div>
```

```css
.ariviti-proof-block   { border-left: 4px solid var(--ariviti-vibrant-orange); padding-left: 1rem; }
.ariviti-proof-claim    { font-family: 'Space Grotesk', sans-serif; font-weight: 600; color: var(--ariviti-royal-indigo); }
.ariviti-proof-metric   { font-family: 'Space Grotesk', sans-serif; font-size: 2.5rem; font-weight: 700; color: var(--ariviti-soft-black); }
.ariviti-proof-source   { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 0.875rem; color: var(--ariviti-soft-black); }
```

### Primary CTA Button Pattern

```html
<a href="#" class="ariviti-btn-primary">[Short Action Label]</a>
```

```css
.ariviti-btn-primary {
  background-color: var(--ariviti-vibrant-orange);
  color: var(--ariviti-white);
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 600;
  font-size: 1.5rem; /* 24px+ required for WCAG AA contrast at this color */
  padding: 12px 24px;
  text-decoration: none;
  display: inline-block;
  border-radius: 4px;
}
```

### Standard Email Signature HTML

**This is the one place inline styles are correct** — per Section 1's stated exception, email clients require it:

```html
<table style="font-family: 'Plus Jakarta Sans', Arial, sans-serif; font-size: 14px; color: #2E2E2E;">
  <tr>
    <td style="padding-right: 12px;">
      <img src="[symbol-icon-32px.png]" width="32" height="32" alt="Ariviti">
    </td>
    <td>
      <strong style="font-size: 15px;">[Full Name]</strong><br>
      <span style="color: #3B3EA9;">[Role] · Ariviti</span><br>
      <a href="https://ariviti.com" style="color: #3B3EA9; text-decoration: none;">ariviti.com</a>
    </td>
  </tr>
  <tr>
    <td colspan="2" style="padding-top: 8px; color: #2E2E2E;">
      Intelligence Amplified.
    </td>
  </tr>
</table>
```

---

## 6. Execution & Prompting Instructions for AI Tools

1. **Check constraints before outputting code:** verify all text colors meet contrast ratios (`4.5:1` for body, `3:1` for large text). Confirm no text is set in Chillax and no CSS uses `font-style: italic`. Confirm no `style="..."` attribute appears outside of email HTML.
2. **Writing copy:** adopt the personality of *"The senior engineer who also happens to be a good explainer."* Follow the Proof Ladder: Claim → Sourced Evidence → Measurable Outcome.
3. **Alt text for generated images:** format strictly as `[Subject] doing [action] — [context]. Ariviti brand photograph.`
4. **Never invent a new hex value, font, or component pattern.** If a task seems to need one that isn't in this document, say so explicitly rather than improvising — new tokens escalate per the Decision Rights Table in `01_STRING_Governance.md`.