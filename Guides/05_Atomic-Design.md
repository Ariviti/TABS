# Atomic Design Methodology
*Annexure to Ariviti Brand Guidelines · Not covered in core BG — the missing layer between "guidelines" and "shipped pages"*

## Why This Document Exists

A brand guideline defines the particles (hex codes, fonts). It rarely defines how those particles assemble into a shippable page without a designer re-deriving the logic every time. That gap is where small marketing teams lose the most hours. This closes it.

---

## The Hierarchy

| Level | Contains | Ariviti Example |
|---|---|---|
| **Tokens** | Raw values — colors, type sizes, spacing units | `#FF4D1C`, Space Grotesk Bold 48px, 8px spacing unit |
| **Components** | A single-function combination of tokens | Primary CTA button: Orange fill + white Plus Jakarta Sans SemiBold + 16px min |
| **Patterns** | Reusable multi-component blocks | The **Proof Block**: claim (Space Grotesk) + metric (bold, large) + source line (small, Soft Black 60%) |
| **Sections** | Complete functional page zones | Homepage hero, case study "Results" section, About page leadership grid |
| **Templates** | Full page types, pre-populated, ready to fill | Case study template, one-pager template, LinkedIn carousel template |
| **System** | The live, governed asset library in production | ariviti.com, sales kit, deck library, case study library |

**Rule:** nobody designs at the Section or Template level from scratch. They assemble from governed Components and Patterns. This is what makes a two-person marketing team's output look like a twenty-person team's — consistency by construction, not by review.

---

## The Proof Block (new pattern, addresses a real gap)

The single highest-leverage pattern in the system, because it's reused across web, decks, case studies, and LinkedIn — and because it's the atomic unit of GEO/LLM citability (see Templates doc).

```
[CLAIM — one line, Space Grotesk SemiBold]
[METRIC — large, bold, the number does the work]
[SOURCE — "Production data, Q[X] 20XX, [Client industry, not name if confidential]"]
```

**Do:** build every case study, every LinkedIn metric post, every deck slide with a proof point out of this exact pattern.
**Don't:** let copywriters freehand metric callouts — inconsistent formatting is what makes brand-compliance audits fail.

---

## Component Library — Minimum Viable Set

A two-person marketing team does not need forty components. It needs these, governed tightly:

| Component | Token Rules |
|---|---|
| Primary CTA | Orange fill, white text, Space Grotesk SemiBold, 16px min |
| Secondary CTA | Indigo outline, Indigo text, transparent fill |
| H1 | Space Grotesk Bold, 48–72px |
| H2 | Space Grotesk SemiBold, 28–36px |
| Body | Plus Jakarta Sans Regular, 16–18px min |
| Proof Block | See above |
| Leadership card | Photo + name + role + one proof point (never a group photo substitute) |
| Case study card | Client industry + challenge headline + one Proof Block + CTA |

---

## Derivation Discipline

Every new component proposed by anyone — internal or agency — must answer three questions before it's added to the library:

1. **Which token does it use, and is that token already governed?**
2. **Which existing component does it replace or extend — why wasn't the existing one sufficient?**
3. **Can it be described in one sentence to someone who's never seen it?**

If the answer to #3 takes more than one sentence, the component is actually two components pretending to be one — split it.

---

## Subsidiarity in Practice

Per the Implementation doc's decision-rights table: component-level decisions (does this button need a new state?) sit with whoever's building the page. Token-level decisions (new color, new font) escalate to the brand owner. This is what keeps the system fast *and* governed — most decisions never need to leave the builder's desk.
