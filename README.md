# The Ariviti Brand System (TABS)

```markdown
# Brand System & Context Rules for Large Language Models

> **System Instruction for AI Models:** This document is the consolidated source of truth for generating brand-compliant code (HTML, CSS, UI components) and copy. You MUST follow all strict governance guidelines, color hex values, typography pairings, and accessibility standards specified below.

---

## 1. Governance & Structural Map (`00_STRING_Governance`)

This system operates on an Atomic Design hierarchy. Code and content are mapped to five core repository layers:

```text
TABS (The Ariviti Brand System)
├── 01_STRINGS/   --> Governance, Voice, Tone, Design Philosophy, & Never List
├── 02_PARTICLES/ --> Tokens & Sub-atomic Data (Color Swatches, Type Scales)
├── 03_ATOMS/     --> Primary Identity Assets (Logo Math, Photography Guidelines)
├── 04_MOLECULES/ --> Component Templates & Layout Engines (.css, .jsx, .mjml)
└── 05_COMPOUNDS/ --> Finished Deliverables Layer (Email Signatures, Case Studies, Decks)

```

### Core Design Philosophy & Laws

* **Governing Idea:** "Ariviti is built on the belief that the future of AI is guided by human wisdom."


* **Clarity Law:** One idea per screen / one idea per slide.


* **Confidence Law:** State the claim once, plainly, and stop. No exclamation points (maximum 1 per asset).


* **Purposeful Innovation Law:** Every element must have a functional purpose. No decorative flourishes or "AI hype" tropes (neon gradients, glitch effects, robotic hands, glowing brains).



### Negative Constraints (The Never List for Code & Content)

* **Do NOT** use unapproved hex codes or custom inline styling (`style="..."` attributes).


* **Do NOT** import external Google Fonts directly inside generated component snippets; rely on the variables defined in `02_PARTICLES`.


* **Do NOT** write "AI-powered", "cutting-edge", "next-gen", "revolutionary", "innovative", or "end-to-end solution" without concrete mechanisms and sourced baselines in the same sentence.


* **Do NOT** generate passive-voice copy. Write direct active-voice sentences ("We reduced costs," not "Costs were reduced").



---

## 2. Color Swatches & Tokens (`02_PARTICLE_Color`)

Always utilize the exact CSS variables and hex codes below:

```css
:root {
  /* Primary Swatches */
  --ariviti-vibrant-orange: #FF4D1C; /* CTA & Accents only (5–10% layout ratio) */
  --ariviti-royal-indigo:   #3B3EA9; /* Headers, primary text, structural (15–25%) */
  --ariviti-dark-indigo:    #1E1669; /* Depth variant, headers on light / dark fields */
  --ariviti-soft-black:     #2E2E2E; /* Body text & fine structural lines (Never #000000) */
  --ariviti-white:          #FFFFFF; /* Clarity base, space, focus (65–75% layout ratio) */

  /* UI Tints (Programmatically Generated) */
  --ariviti-indigo-tint-20: #D4D5F0; /* Card backgrounds & hover states */
  --ariviti-indigo-tint-50: #9D9FD4;
  --ariviti-indigo-shade-80:#0C0D22;
  --ariviti-orange-tint-20: #FFE0D3;
  --ariviti-softblack-tint-20:#E9E9E9;

  /* Semantic Mappings */
  --color-brand-primary:   var(--ariviti-royal-indigo);
  --color-brand-accent:    var(--ariviti-vibrant-orange);
  --color-bg-main:         var(--ariviti-white);
  --color-bg-surface:      var(--ariviti-indigo-tint-20);
  --color-text-main:       var(--ariviti-soft-black);
  --color-text-heading:    var(--ariviti-royal-indigo);
}

```

---

## 3. Typography System (`01_PARTICLE_Typefaces`)

### The Three-Font Rule

1. **Chillax:** Logo wordmark ONLY. **NEVER** install or use for headings, body, or UI components.


2. **Space Grotesk:** Headings, display titles, and large standalone metrics. **NEVER** use for long-form body copy.


3. **Plus Jakarta Sans:** Body copy, pull quotes, captions, and email signatures.



*Note on Italics:* NO weight or role in this system uses italics. Emphasis is carried exclusively by weight (bold) or color.

### Type Scale & Tokens

* **H1 / Display:** Space Grotesk Bold 700 (`48px`–`72px`, Line-height: `1.15`)


* **H2:** Space Grotesk SemiBold 600 (`28px`–`36px`, Line-height: `1.15`)


* **H3:** Plus Jakarta Sans ExtraBold 800 (`22px`–`26px`)


* **Body:** Plus Jakarta Sans Regular 400 (`16px` min, Line-height: `1.6`, Left-aligned)


* **Metrics/Stats:** Space Grotesk Bold 700



---

## 4. Accessibility & Contrast Standards (`02_PARTICLES` / Part 3)

### The Load-Bearing Rules

* Vibrant Orange (`#FF4D1C`) is large-scale, short-text-only. It is strictly reserved for primary CTA buttons (24px+ font size) and display accents.


* ❌ **FORBIDDEN:** Orange text on Royal Indigo background (Contrast ratio `2.59:1` = HARD FAIL).


* ❌ **FORBIDDEN:** Orange for body text, data labels, captions, or fine print.


* ✓ **ALLOWED:** Royal Indigo on White (`8.58:1`), Dark Indigo on White (`15.28:1`), Soft Black on White (`13.58:1`).



---

## 5. UI Component Structures (`03_MOLECULE_Templates`)

### The Proof Block Pattern (Core Component)

When creating case studies, stats, or marketing sections, use the GEO-ready Proof Block structure:

```html
<div class="ariviti-proof-block" style="border-left: 4px solid var(--ariviti-vibrant-orange); padding-left: 1rem;">
  <h3 style="font-family: 'Space Grotesk', sans-serif; font-weight: 600; color: var(--ariviti-royal-indigo);">
    [Specific, Quotable Claim]
  </h3>
  <div style="font-family: 'Space Grotesk', sans-serif; font-size: 2.5rem; font-weight: 700; color: var(--ariviti-soft-black);">
    [Metric / Quantified Number]
  </div>
  <p style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 0.875rem; color: var(--ariviti-soft-black);">
    <strong>Source:</strong> [Metric, baseline, date, client context]
  </p>
</div>

```

### Primary CTA Button Pattern

```html
<a href="#" class="ariviti-btn-primary" style="
  background-color: var(--ariviti-vibrant-orange);
  color: var(--ariviti-white);
  font-family: 'Space Grotesk', sans-serif;
  font-weight: 600;
  font-size: 1.5rem; /* 24px+ required for WCAG AA contrast */
  padding: 12px 24px;
  text-decoration: none;
  display: inline-block;
  border-radius: 4px;">
  [Short Action Label]
</a>

```

### Standard Email Signature HTML (`05_COMPOUND_Assets`)

```html
<table style="font-family: 'Plus Jakarta Sans', Arial, sans-serif; font-size: 14px; color: #2E2E2E;">
  <tr>
    <td style="padding-right: 12px;">
      <img src="[symbol-icon-32px.png]" width="32" height="32" alt="Ariviti">
    </td>
    <td>
      <strong style="font-size: 15px;">[Full Name]</strong><br>
      <span style="color: #3B3EA9;">[Role] · Ariviti</span><br>
      <a href="[https://ariviti.com](https://ariviti.com)" style="color: #3B3EA9; text-decoration: none;">ariviti.com</a>
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

1. **Check Constraints Before Outputting Code:** Verify that all text colors meet contrast ratios (`4.5:1` for body, `3:1` for large text). Ensure no text is set in Chillax or displayed in italics.


2. **Writing Copy:** Adopt the personality of *"The senior engineer who also happens to be a good explainer."* Follow the **Proof Ladder**: Claim → Sourced Evidence → Measurable Outcome.


3. **Alt Text Rules for Generated Images:** Format strictly as: `[Subject] doing [action] — [context]. Ariviti brand photograph.`


```

```