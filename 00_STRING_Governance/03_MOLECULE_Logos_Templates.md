# 03 · Molecules
*Tracks: .potx · .dotx · .css · .jsx · .mjml · .json*

- [Download Derived Logos](/03_MOLECULE_Logo_Derivatives/README.md)

- [Download Core Templates](/03_MOLECULE_Templates/README.md)

## What This File Is (and Isn't)

Molecules are not prose — they're working files. This document does not restate brand rules; it tracks **which template/code files exist, which don't, and which upstream document governs each one's build.** When a molecule is built, it must be built strictly from the Strings, Particles, and Atoms documents — never re-derived from memory or vibes.

If you're building one of these files, read the "Governed By" column first. That document is the spec. This manifest just tells you the file is needed and where the spec lives.

## Status Manifest

| File                         | Purpose                                                                        | Status                                                            | Governed By                                                                   | Owner                   |
| ---------------------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------- |
| **`ariviti-brand.potx`**     | Locked PowerPoint master — theme colors, slide masters, layouts pre-built      | 🔴 Not yet built                                                   | Particles (Color, Type Scale) + Compounds → Slide Deck Template               | Brand owner             |
| **`ariviti-brand.dotx`**     | Locked Word master — styles for headings, body, case study/one-pager structure | 🔴 Not yet built                                                   | Particles (Typography) + Compounds → Case Study & One-Pager Templates         | Brand owner             |
| **`ariviti-tokens.css`**     | CSS custom properties for every color and type value                           | 🟡 Partially specified — property names exist, full file not built | Particles → Color Swatches "File Formats to Maintain"; Particles → Typography | Web/product engineering |
| **`ariviti-components.jsx`** | React component library implementing the Component Library                     | 🔴 Not yet built                                                   | Strings → Atomic Design Methodology, "Component Library — Minimum Viable Set" | Web/product engineering |
| **`ariviti-signature.mjml`** | Responsive email-signature markup (replaces raw inline-HTML draft)             | 🔴 Not yet built                                                   | Compounds → Email Signatures (spec is written; MJML compile step is the gap)  | IT / Marketing ops      |
| **`ariviti-tokens.json`**    | Design-token export (colors, type scale) for Figma/pipeline consumption        | 🔴 Not yet built                                                   | Particles doc, in full                                                        | Brand owner             |

**Legend:** 🟢 Built & in use · 🟡 Partially specified · 🔴 Not yet built

## Build Principles (apply to every molecule above)

1. **No molecule invents a new value.** If a `.jsx` button component needs a color not in Particles → Color Swatches, that's a token-level decision — it escalates per the Decision Rights Table (Strings → Implementation & Governance), it does not get quietly added in code.
2. **No molecule skips accessibility.** Every component in `ariviti-components.jsx` must pass the Fragility Score (Particles → Accessibility) before merge — this includes contrast, alt text props, and keyboard focus states.
3. **Molecules are versioned with the system, not independently.** A `.css` token file that drifts from the Particles doc is a bug, not a style choice — see Version Control (Strings → Implementation & Governance).
4. **MJML over raw HTML for anything email-bound.** The current signature spec (Compounds doc) is written as a plain HTML table for readability; the actual production file should be MJML, which compiles to more reliable cross-client HTML than hand-written tables.

## Immediate Priority

Per the Brand Health Scorecard (Strings → Implementation & Governance), the two molecules with the highest near-term leverage are:

1. **`ariviti-tokens.css` / `ariviti-tokens.json`** — every other molecule and compound depends on these existing as a single source of truth instead of re-typed hex values scattered across files.
2. **`ariviti-signature.mjml`** — the signature spec has existed as a written standard since the Compounds doc was drafted; it is the one molecule where the content work is already done and only the build step remains.
