# 01 · Strings
*The Ariviti Brand System — Rules Layer*
*Contains: Design Philosophy · Atomic Design Methodology · Voice, Tone & Vocabulary · Implementation & Governance*

Strings are the governing laws — the rules that don't have a hex code or a font size, but that every particle, atom, molecule, and compound in this system must trace back to. If a component, a sentence, or a decision can't be justified against something in this file, it isn't on-system.

---

# Part 1 — Design Philosophy
*Reference: Core BG page 3 ("Meaning")*

## The Governing Idea

Core BG states it plainly: *"Ariviti is built on the belief that the future of AI is guided by human wisdom."*

Every design decision downstream of that sentence must pass one test:

> **Does this make the human judgment visible, or does it make the AI look autonomous?**

If a layout, animation, or copy block makes AI look like it's operating alone, it contradicts the brand's core conviction — regardless of how polished it looks.

## Three Pillars → Three Design Laws

The core BG names three qualities the identity represents: **clarity, confidence, purposeful innovation.** Each converts into an enforceable design law, not a mood.

| Pillar | Design Law | In Practice |
|---|---|---|
| **Clarity** | One idea per screen / one idea per slide | No dashboard-style pages cramming five messages above the fold |
| **Confidence** | State the claim once, plainly, and stop | No stacked qualifiers, no hedge words, no exclamation marks |
| **Purposeful Innovation** | Every "new" element must trace to a functional reason | No design flourish added because it looks modern — only because it does something |

## Derivation Chain — How a Decision Traces Back

Example: why is the CTA button Vibrant Orange, not Royal Indigo?

```
Governing Idea: human wisdom guides AI, not the reverse
      ↓
Pillar: Purposeful Innovation — orange = "energy, creativity, forward momentum"
      ↓
Token: Vibrant Orange (#FF4D1C) reserved for action, never for information
      ↓
Component: Primary CTA button — orange fill, white text, Space Grotesk SemiBold
      ↓
Rule: Orange never carries body text (fails AA contrast — see Particles doc, Accessibility),
      so it is confined to short, large, high-confidence calls to action
      ↓
Page: Every page has exactly one orange CTA — never two competing actions
```

Any designer or agency should be able to run this chain backward from any executed asset to the governing idea. If they can't, the asset isn't on-system — it's decoration.

## What Ariviti Is Not (the design version of the Never List)

| Not This | Because |
|---|---|
| A "cutting-edge AI lab" aesthetic (dark mode, neon gradients, glitch effects) | Signals hype, not evidence — contradicts Evidence-first |
| A generic enterprise-SaaS template (rounded cards, pastel illustrations, flat mascots) | Indistinguishable from any B2B SaaS landing page — zero differentiation |
| A consultancy-generic deck (stock handshake photos, bullet-wall slides) | Contradicts Clarity — bullet walls are the opposite of one idea per slide |

<!-- PRIVATE:START reason="discloses revenue mix / go-to-market strategy" -->
## The Real-World Tension to Design Around

Ariviti's revenue is predominantly services and outsourcing; platform work (TurfAI) is a strategic wedge, not the whole business. This creates a genuine design risk: **a site that looks 100% platform-forward will misrepresent the company to enterprise buyers doing due diligence**, and sophisticated buyers notice the mismatch.

**Design response:**
- Platform pages (TurfAI, CoE) get full design-system investment — they're the differentiation story.
- Services pages get equal typographic and photographic rigor — never treated as the "boring" section styled with leftover templates.
- Never let site navigation imply platform-only revenue (e.g., a nav bar with five platform items and one buried "Services" link). Navigation architecture is a design-philosophy decision, not just an IA decision.
<!-- PRIVATE:END -->

## One-Sentence Test for Any New Asset

Before anything ships, ask: **"Would a technical evaluator trust this, and would a human buyer feel understood by this — at the same time?"** If an asset only satisfies one of the two, it's not finished.

---

# Part 2 — Atomic Design Methodology
*The missing layer between "guidelines" and "shipped pages"*

## Why This Section Exists

A brand guideline defines the particles (hex codes, fonts). It rarely defines how those particles assemble into a shippable page without a designer re-deriving the logic every time. That gap is where small marketing teams lose the most hours. This closes it.

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

## The Proof Block

The single highest-leverage pattern in the system, because it's reused across web, decks, case studies, and LinkedIn — and because it's the atomic unit of GEO/LLM citability (see the Compounds manifest, Templates entry).

```
[CLAIM — one line, Space Grotesk SemiBold]
[METRIC — large, bold, the number does the work]
[SOURCE — "Production data, Q[X] 20XX, [Client industry, not name if confidential]"]
```

**Do:** build every case study, every LinkedIn metric post, every deck slide with a proof point out of this exact pattern.
**Don't:** let copywriters freehand metric callouts — inconsistent formatting is what makes brand-compliance audits fail.

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

## Derivation Discipline

Every new component proposed by anyone — internal or agency — must answer three questions before it's added to the library:

1. **Which token does it use, and is that token already governed?**
2. **Which existing component does it replace or extend — why wasn't the existing one sufficient?**
3. **Can it be described in one sentence to someone who's never seen it?**

If the answer to #3 takes more than one sentence, the component is actually two components pretending to be one — split it.

## Subsidiarity in Practice

Component-level decisions (does this button need a new state?) sit with whoever's building the page. Token-level decisions (new color, new font) escalate to the brand owner. This is what keeps the system fast *and* governed — most decisions never need to leave the builder's desk. Full decision-rights table in Part 4 of this document.

---

# Part 3 — Voice, Tone & Vocabulary
*Reference: Core BG pages 16–17*

## The Four Traits, Operationalized

The core BG names four traits: **Clear & Direct, Knowledgeable, Evidence-first, Human-led.** Traits without tests are just adjectives. Here's the test for each.

| Trait | Fails If... | Passes If... |
|---|---|---|
| **Clear & Direct** | A sentence needs re-reading to find the verb | A reader states the point back correctly on first pass |
| **Knowledgeable** | The claim could be made by any AI vendor | The claim requires domain-specific context to be true |
| **Evidence-first** | A number appears without its source or baseline | Every metric answers "measured how, against what" |
| **Human-led** | AI is the subject of the sentence | A person or outcome is the subject; AI is the tool |

## The Proof Ladder

Every external claim climbs three rungs. Skipping a rung is how marketing copy becomes fiction.

1. **Claim** — the assertion ("we cut processing time")
2. **Evidence** — the number, source, and baseline ("from 7 weeks to 3 weeks, Q2 production data")
3. **Outcome** — what it meant for the client ("the backlog cleared before renewal season")

**Do:** write outcome-first, evidence-second in headlines; keep the claim itself out of the H1 unless it's already proven.
**Don't:** publish rung 1 without rungs 2 and 3 available on request. If they're not available, the claim isn't ready to publish.

## Vocabulary — Use This, Never This

Directly extending the core BG's two example shifts into a working system:

| Never This | Use This | Why |
|---|---|---|
| "We leverage AI to accelerate digital transformation" | "We put AI into production with measurable outcomes." | "Leverage" is a verb with no object — says nothing about what changed |
| "Our platform delivers cutting-edge AI solutions" | "We solve real business problems, not showcase technology." | "Cutting-edge" is a claim every competitor also makes — zero differentiation |
| "AI-powered" (unqualified) | Name what the AI does and what it produced | Unqualified "AI-powered" is now a red flag to sophisticated buyers, not a credential |
| "Innovative" / "next-generation" / "revolutionary" | The specific mechanism or result | These words have no verifiable content — they're vibes, not evidence |
| "End-to-end solution" | Name the start point and end point explicitly | "End-to-end" sounds complete but tells the reader nothing they can check |
| "Human in the loop" | "Human-led" / name the person's actual role | "In the loop" frames the human as an interruption to the AI, not the decision-maker |
| "Transformation" (unqualified) | From [state] to [state], by [date/metric] | Matches Evidence-first — an unqualified "transformation" is unfalsifiable |
| "Full-stack AI" | The specific layer or capability you own | Nobody owns the full stack; the claim signals inexperience to technical buyers |

## The Never List

Checked before any external asset ships.

- **Never** publish a metric without a source and baseline.
- **Never** write a passive-voice sentence in external copy. ("Costs were reduced" → "We reduced costs.")
- **Never** use "AI-powered," "cutting-edge," "next-gen," "revolutionary," or "innovative" without a concrete mechanism attached in the same sentence.
- **Never** open a case study, deck, or About page with company heritage/years-in-business. Heritage is due-diligence context, not a hook.
- **Never** let a technical process diagram outrank the human outcome in visual size or position on the same page.
- **Never** use more than one exclamation point per asset, ever.
- **Never** claim a result as achieved if it is a target or lab result. Say "target" or "pilot" explicitly.

## Personality — One Idea, Not a Framework

Resist inventing an elaborate persona system. Ariviti's personality is simple enough to fit in one sentence:

> **The senior engineer who also happens to be a good explainer.**

That's it. Test every sentence against it: would a senior engineer actually say this out loud to a CFO, without flinching at their own words? If not, cut it.

## Tone by Format

| Format | Register | Length Discipline |
|---|---|---|
| Website hero copy | Direct claim + immediate qualifier | One sentence, one idea |
| LinkedIn post | Evidence-first, short declaratives, pause after the number | Under 8 lines before "see more" |
| Case study | Challenge → Approach → Result, in that order, every time | No hedging language ("may," "could potentially") |
| Sales email | One idea per email, subject line states the outcome not the topic | Under 120 words |
| Leadership bio (About page) | Named, specific, credentialed — not a group photo caption | 2–3 sentences, one proof point per person |

<!-- PRIVATE:START reason="discloses current site gap" -->
**Note:** Named, specific leadership bios are currently absent from the site (per the last audit). This is a voice problem as much as a content problem — "Human-led" as a brand trait is unconvincing if the humans aren't named.
<!-- PRIVATE:END -->
**Evergreen version:** leadership bios must be named and specific, not a group-photo caption — "Human-led" as a brand trait depends on it.

---

# Part 4 — Implementation & Governance
*The capstone — how the system stays alive with a small team*

## Principle: Subsidiarity

**Decide at the lowest level competent to decide, escalate only what's irreversible or system-wide.** A two-person marketing team that routes every button color through leadership review will ship nothing. A team with clear decision rights ships fast *and* stays governed.

### Decision Rights Table

| Decision | Who Decides | Escalates To | Why |
|---|---|---|---|
| Copy edits within voice/vocabulary rules | Content creator | No escalation | Reversible, low-risk, template-governed |
| New component (button state, card variant) | Designer/builder | Brand owner (async review) | Affects the system but is reversible |
| New color, new font, tagline change | — | **CEO** | Irreversible at scale, defines the whole system |
| Logo modification of any kind | — | **CEO** | Highest-irreversibility asset in the system |
| Case study / metric publication | Content creator drafts | Delivery team confirms metric accuracy | Evidence-first requires a non-marketing sign-off on numbers |
| External agency brand compliance | Agency | Brand owner, pre-work | Contractual condition, set before work starts, not reviewed after |

**Do:** publish this table where the team can see it — most bottlenecks are people escalating decisions that were theirs to make.
**Don't:** let "brand safety" become an excuse to centralize every decision — that's how brand systems die from neglect, not misuse.

## Approval Pipeline (async by default)

```
Draft → Self-check against Never List + Fragility Score → Async review (24hr SLA) → Publish
```

**Do:** default every review to asynchronous comment threads, not scheduled meetings. A 24-hour SLA on brand review is achievable and doesn't require anyone's calendar.
**Don't:** let "brand review" become a synchronous bottleneck — if a review consistently needs a live meeting, the guidelines aren't clear enough and need revision, not more meetings.

<!-- PRIVATE:START reason="live audit numbers and current-state admissions" -->
## Quantify Fragility: The Brand Health Scorecard

What gets measured gets protected — but only if the metric is quantified, not vibes-based.

| Metric | Method | Fragility If Ignored |
|---|---|---|
| **LLM/GEO citation rate** | Ask ChatGPT/Perplexity/Google AI "best AI implementation partners [category]" quarterly — count citations | **Currently near-zero** due to empty Insights section — this is the single most fragile metric in the system right now |
| **Named leadership presence** | Count named, bio'd leaders on About page | **Currently zero** — directly undercuts Human-led as a claim |
| **Case study depth** | Count published case studies with full Proof Block structure | Currently thin — every unpublished engagement is a missed GEO/trust asset |
| **Contrast compliance** | Run Fragility Score (Particles doc, Accessibility) on 5 random assets/quarter | Orange misuse is the most common failure mode — catch it before external distribution |
| **Voice compliance** | Brand owner reviews 10 random assets/quarter against Never List | Drift compounds silently if unchecked |
| **Visual recognition (blind test)** | Strip logo from 5 assets, show 5 ICP-profile testers, ask "which company?" | Tests whether the *system* — not just the logo — is doing recognition work |

**Do:** score these quarterly, log the trend, not just the snapshot. A single quarter's number is noise; three quarters is a trend.
**Don't:** treat a passing score as permission to stop measuring — brand health is a maintained system, not a certification.

## The Three Structural Risks
*From the last site audit — resolved here as governance items, not one-off fixes*

| Risk | Root Cause | Governance Fix |
|---|---|---|
| Meta-keywords carrying irrelevant taxonomy site-wide | No owner for technical SEO hygiene | Assign explicit ownership; add to quarterly audit checklist, not a one-time fix |
| Platform-forward site presentation vs. services-dominant revenue | No navigation/IA governance tying site structure to actual revenue mix | Nav architecture reviewed annually against actual revenue split — platform is the differentiation story, not the whole story |
| Thin case studies, empty Insights, unnamed leadership | No content cadence or template enforcement | Templates (Compounds manifest) + GEO-Ready Content Block used as the default, cadence tracked in scorecard above |
<!-- PRIVATE:END -->

## Version Control

| Element | Rule |
|---|---|
| Guidelines versioning | This annexure set versions alongside the core BG — cite core BG version in every file header |
| Asset library | Single source of truth (Drive/Figma/Notion — pick one, not three) |
| Change log | Every material change (new component, new color use case) logged with date, author, reason |

## Onboarding

Every person producing external content — internal or agency — completes a **single-session walkthrough** of: Voice/Vocabulary Never List, Logo Don'ts (Atoms doc), Accessibility Fragility Score (Particles doc), and the Decision Rights Table above. Under 60 minutes. Anything longer means the guidelines are too complex for a small team to actually run on.

## Final Principle

**A brand system a two-person team can't operate without constant senior review isn't a system — it's a bottleneck wearing a style guide's clothes.** Every rule in this file is written to be self-enforcing: templates that make compliance the default, a scorecard that makes fragility visible, and a decision-rights table that makes escalation the exception, not the norm.