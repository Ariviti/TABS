# 04 · Compounds
*Tracks & specifies: .pptx · .docx · .html templates · Email Signatures*

- [Download Reference Templates](/04_COMPOUND_References)

## What This File Is

Compounds are complete, sendable artifacts — built from Molecules (code/template files), which are built from Atoms, Particles, and Strings. Some compounds below are fully specified in content but not yet compiled into a locked template file; some don't exist in any form yet. Each entry says which is true.

## Status Manifest

| Compound                              | Status                                                      | Notes                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **This Annexure (`.pptx`)**           | 🟢 Built & in circulation                                    | The reference implementation of this entire system — every rule above is demonstrated in a real, shipped deck. Treat it as the visual precedent for any future `.pptx`.                                                                                                                                                                            |
| **Email Signature**                   | 🟡 Fully specified, not yet deployed as a file               | Full template below. Needs to be built as `ariviti-signature.mjml` (see Molecules manifest) and pushed via IT/Workspace policy.                                                                                                                                                                                                                    |
| **Case Study (`.docx` / web)**        | 🟡 Structure specified, no locked template file              | Full structure below. Needs a `.dotx` master (Molecules manifest) or a locked web template.                                                                                                                                                                                                                                                        |
| **One-Pager (`.docx` / `.pdf`)**      | 🟡 Structure specified, no locked template file              | Full structure below.                                                                                                                                                                                                                                                                                                                              |
| **Slide Deck (`.pptx`)**              | 🟡 Structure specified; this Annexure is a partial precedent | Needs a dedicated `.potx` master separate from this reference document (Molecules manifest).                                                                                                                                                                                                                                                       |
| **LinkedIn Post**                     | 🟡 Structure specified, text-only compound                   | No file format — governed entirely by the template below plus the Never List (Strings doc).                                                                                                                                                                                                                                                        |
| **About / Leadership Page (`.html`)** | 🟡 Structure specified, not built                            | <!-- PRIVATE:START reason="discloses current site gap" -->Currently blocked on real content (named leaders, bios), not on the template — see Brand Health Scorecard, Strings doc.<!-- PRIVATE:END --><!-- PUBLIC:START -->Awaiting content — the template is ready to receive named leadership bios whenever they're finalized.<!-- PUBLIC:END --> |

**Legend:** 🟢 Built & in use · 🟡 Specified, not yet compiled into a file · 🔴 Not started

---

## Email Signature — Full Specification

### Principle

An email signature is seen more often than almost any other brand asset — and is the easiest one to let drift, because everyone edits their own. **Lock the template, not the person's willingness to comply.**

### Standard Template

```
[Full Name]
[Role] · Ariviti

[Symbol icon, 32px]  ariviti.com
[Phone — optional, only if role-appropriate]

Intelligence Amplified.
```

**Typography:** Plus Jakarta Sans only (Space Grotesk and Chillax don't render reliably across email clients).
**Colors:** Name in Soft Black `#2E2E2E`. Role and links in Royal Indigo `#3B3EA9`. No Orange in signatures — small orange text fails contrast (Particles → Accessibility) and email clients often can't render it consistently anyway.
**No italics** — consistent with the system-wide rule in Particles → Typography.

### HTML Reference Block
*Reference only — production version should be MJML, see Molecules manifest*

```html
<table style="font-family: 'Plus Jakarta Sans', Arial, sans-serif; font-size: 14px; color: #2E2E2E;">
  <tr>
    <td style="padding-right:12px;">
      <img src="[symbol-icon-32px.png]" width="32" height="32" alt="Ariviti">
    </td>
    <td>
      <strong style="font-size:15px;">[Full Name]</strong><br>
      <span style="color:#3B3EA9;">[Role] · Ariviti</span><br>
      <a href="https://ariviti.com" style="color:#3B3EA9; text-decoration:none;">ariviti.com</a>
    </td>
  </tr>
  <tr>
    <td colspan="2" style="padding-top:8px; color:#2E2E2E;">
      Intelligence Amplified.
    </td>
  </tr>
</table>
```

### Do / Don't

| Do                                                                                                                                  | Don't                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use the symbol icon only (32px), never the full lockup — full lockup at signature scale falls below the 24px minimum size and blurs | Embed the full-color primary lockup as a large banner image                                                                                                 |
| Use web-safe fallback fonts (`Arial, sans-serif`) since Plus Jakarta Sans isn't guaranteed to render in Outlook                     | Rely on custom fonts rendering correctly across all mail clients                                                                                            |
| Keep it to 4 lines maximum                                                                                                          | Add quotes, social icons, calendar-booking banners, or promotional graphics — every addition is a new maintenance liability and a new place to go off-brand |
| Update centrally and redistribute (via IT/Google Workspace signature policy if available)                                           | Let each employee hand-edit their own signature file                                                                                                        |

**Why no campaign banners:** signatures are infrastructure, not marketing real estate. Every "temporary" campaign banner outlives the campaign by months and becomes a compliance debt. If a campaign needs promotion, it goes in the newsletter or LinkedIn — never the signature.

**Governance:** one person owns the signature template (Decision Rights Table, Strings doc). Updates ship as a single distributed file or workspace policy push — never as a "please update your signature" email that half the team ignores.

---

## The GEO-Ready Content Block
*The universal content pattern underneath every compound below — closes a real gap*

LLM/AI-search citation now behaves like a second SEO channel, and it rewards exactly the structure the Voice system already requires (Strings doc): named claims, sourced evidence, specific outcomes.

```
## [Specific, quotable claim as a heading]

[One-sentence direct answer — the sentence an LLM would lift verbatim]

**Evidence:** [Metric, source, baseline, date]
**Context:** [2–3 sentences of specifics — industry, scale, constraint]
**Attribution:** [Named person or team, role]
```

**Do:** structure every Insights/blog piece, every case study section, and every FAQ answer this way — a direct-answer sentence followed by sourced specifics.
**Don't:** bury the answer inside a narrative paragraph. LLM crawlers (and skimming humans) reward the answer appearing in the first sentence, not the third paragraph.

<!-- PRIVATE:START reason="present-tense claim about current site state" -->
**Why this matters right now:** an empty Insights section produces near-zero citation surface — there's simply nothing structured for an LLM to find and quote. Every piece published from this template directly builds that surface.
<!-- PRIVATE:END -->
<!-- PUBLIC:START -->
**Why this matters:** an empty content section produces near-zero citation surface, full stop — there's nothing structured for an LLM to find and quote. Every piece published from this template builds that surface instead.
<!-- PUBLIC:END -->

---

## Case Study Template

```
1. HERO — Client industry + one-line outcome headline (no company name if confidential)
2. CHALLENGE — 2–3 sentences, specific and quantified where possible
3. APPROACH — what Ariviti actually did, named clearly, no vague "we partnered to..."
4. PROOF BLOCK(S) — see Strings → Atomic Design, minimum 1, ideally 2–3
5. RESULT — outcome in the client's terms, not Ariviti's
6. CTA — single next step, Orange button
```

**Do:** publish even short case studies (400–600 words) regularly over long ones rarely — cadence beats length for both brand-health metrics and GEO citability.
**Don't:** let a case study go out without a named proof point and a validated metric — an unsourced case study is a Never List violation, not a style choice.

---

## One-Pager / Sales Sheet Template

```
Header: Symbol + wordmark, top-left | Contact CTA, top-right
Hero: One outcome-focused headline (Space Grotesk H1)
Body: 3 proof blocks max, laid out horizontally
Footer: "Intelligence Amplified." + contact
```

**Rule:** a one-pager that needs a second page has failed the "Clarity" pillar (Strings doc). Cut, don't extend.

---

## Slide Deck Template — Minimum Structure

| Slide    | Purpose                                    | Typography                                     |
| -------- | ------------------------------------------ | ---------------------------------------------- |
| Cover    | Wordmark + one-line positioning            | Space Grotesk Bold, Indigo gradient background |
| Problem  | Named, quantified, no Ariviti branding yet | Plus Jakarta Sans                              |
| Approach | What Ariviti does, specifically            | Space Grotesk H2 + body                        |
| Proof    | 1 proof block per slide, never more        | Bold metric, sourced                           |
| Close    | Single CTA, contact                        | Orange CTA button                              |

**Do:** one idea per slide, always — this is the Design Philosophy "Clarity" law applied directly.
**Don't:** build a slide with a bullet list longer than 4 items — split it into two slides.

---

## LinkedIn Post Template

```
[Hook — evidence-first, one line, no preamble]

[2–3 short declarative sentences — the story, not the pitch]

[One proof point, if applicable]

[Soft CTA — question or invitation, not "learn more"]
```

**Do:** lead with the number or outcome, never with "We're excited to announce."
**Don't:** use more than one emoji, ever, and only at the very end if used at all — per the Never List (Strings doc).

---

## About / Leadership Page Template

```
For each leader:
[Photo — real, not illustrated] [Name] [Role]
[2–3 sentence bio — one specific credential or proof point, not a title list]
```

**Why this template exists:** the current About page has no named leadership — this directly undercuts "Human-led" as a brand trait and removes another GEO-citable structure (named-person + credential is exactly what LLMs surface for "who runs Ariviti" style queries).

---

## Template Governance

Every compound above lives as a locked file once built (Figma, Google Slides master, Notion database, `.potx`/`.dotx`) — never a "here's an example from last time" copy-paste chain. New team members and external agencies start from the locked file, always. Until a compound's locked file exists, the specification in this document **is** the standard — treat the prose above as binding, not aspirational.