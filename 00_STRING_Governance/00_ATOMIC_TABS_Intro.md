[[00_ATMOS-INDEX]]

# TABS — The Ariviti Brand System

*This document is the index and the physical asset map. It does not restate any rule — every rule lives in exactly one of the five governing files below. This document only answers two questions: "which file governs this?" and "where does the actual asset file live?"*

---

## 🏷️ TABS Architecture Overview

```text
TABS (The Ariviti Brand System)
├── 01_STRINGS         --> Rules Layer            → governed by 01-strings.md
├── 02_PARTICLES       --> Values Layer            → governed by 02-particles.md
├── 03_ATOMS           --> Identity Assets Layer   → governed by 03-atoms.md
├── 04_MOLECULES       --> Build Manifest          → tracked in 04-molecules.md
└── 05_COMPOUNDS       --> Deliverables Layer      → tracked in 05-compounds.md
```

**The distinction that matters:** the five `.md` files are the *specification* — the rules, values, and content a person or an LLM reads before making anything. The folder structure below is the *physical asset map* — where the resulting files actually live on disk once built. Nothing in this document should ever disagree with the five files; if it does, the five files win and this document is stale.

---

## 🗂️ TABS Master Folder & File Structure

### `01_STRINGS/`

> **The Brain.** All positioning, voice, tone, atomic-design methodology, and governance rules. Fully authored in **`01-strings.md`** — that file is the spec, human- and LLM-readable, no separate `.pdf` fork needed.

Two areas named in earlier drafts of this architecture are **not yet authored** anywhere in the system:

| Gap | Status | Notes |
|---|---|---|
| Contextual rules for internal memos / informal touchpoints | 🔴 Not yet written | `01-strings.md` → Tone by Format covers five external-facing formats only (web hero, LinkedIn, case study, sales email, leadership bio). Internal-facing tone is a real gap, not an oversight to ignore. |
| Legal & taxonomy spec (rights, licensing, DAM metadata rules) | 🔴 Not yet written | No file in the system currently governs asset licensing or DAM metadata schema. Needed before the `02_PARTICLES` and `03_ATOMS` asset libraries below scale past a handful of files. |

**Note on "design rules":** earlier drafts of this architecture filed color/typography/logo-clearzone rules under Governance. They don't live there — color and typography rules are in `02-particles.md`, logo clearzone and construction rules are in `03-atoms.md`. Governance in this system is strictly non-visual: positioning, voice, methodology, and decision rights.

---

### `02_PARTICLES/`

> **The Sub-atomic Data.** Pure inputs — code values, fonts, audio — that can't be "viewed" as rendered objects. Full color and typography specification (hex/RGB values, contrast ratios, type scale) is authored in **`02-particles.md`**; this folder is where the corresponding asset *files* live once built (see `04-molecules.md` for build status).

* **`02_PARTICLE_Color/`**
  * `Palette_Primary.ase` / `Palette_Secondary.ase` — values per `02-particles.md` → Full Specification
  * `Palette_Print_CMYK.acb` / `Palette_Apple.clr`
  * `tokens_color.json` — tracked as `ariviti-tokens.json` in `04-molecules.md`
  * `colors.css` / `colors.scss` — tracked as `ariviti-tokens.css` in `04-molecules.md`

* **`02_PARTICLE_Typefaces/`**
  * `Web_Fonts/` (`.woff2`, `.woff`) — Space Grotesk, Plus Jakarta Sans per `02-particles.md` → Three-Font Rule
  * `Desktop_Fonts/` (`.otf`, `.ttf`) — Chillax is logo-file-only; never distributed as a working desktop font (`02-particles.md` explicit rule)
  * `font_fallback_map.json` — system fallbacks (Arial, sans-serif); see `02-particles.md` → Do/Don't

* **`02_PARTICLE_Audio_&_Motion/`** 🔴 Not yet specified
  * `Sonic_Logo_Primary.wav`
  * `Motion_Easing_Curves.json` / Lottie `.json` animations
  * No file in the system currently defines sonic or motion identity. Filed here as a placeholder folder only — do not populate until a governing spec exists.

---

### `03_ATOMS/`

> **The Basic Visual Building Blocks.** Logo construction, clearzone math, color-variant rules, and photography direction are fully authored in **`03-atoms.md`**. This folder is where the master asset *files* live.

* **`03_ATOM_Logos_Core/`** *(master, immutable brand logos direct from agency)*
  * `Master_Logo_Primary_Color.svg` / `.eps` / `.ai`
  * `Master_Logo_Monochrome_Black.svg`
  * `Master_Logo_Monochrome_White.svg`
  * Construction math (1X base unit, 2X clearspace, 24px minimum) and all Don'ts governing these files: `03-atoms.md` → Logo System

* **`03_ATOM_Logo_Derivatives/`** *(locked, pre-rendered size & organizational variants)*
  * `Favicon_AppIcon.ico` / `Favicon_512x512.png`
  * `Lockup_Division_Tech.svg`
  * `Lockup_Horizontal_Compact.svg`
  * Usage context for each: `03-atoms.md` → Symbol-Only Usage

* **`03_ATOM_Icons/`** 🔴 Not yet specified
  * `System_Icons_16x24/` (`.svg` grid icons)
  * `Illustrative_Icons_48px/` (`.svg`)
  * No file in the system currently governs a general iconography style (stroke weight, corner radius, grid). `03-atoms.md` only covers the logo symbol used *as* an icon (favicon, avatar) — a broader icon system is a genuine gap, not yet authored.

* **`03_ATOM_Imagery/`**
  * `01_Executive_&_Leadership/` (`.jpg`, `.tiff`)
  * `02_Industry_&_Themes/` (`.jpg`, transparent `.png`)
  * `03_Abstract_&_Textures/` (`.jpg`, background `.mp4` loops)
  * `image_registry_&_alt_tags.csv` — alt-text format is fixed: `03-atoms.md` → Photography → Alt Text Format
  * Subject priority, color treatment, and Do/Don't governing everything shot for these folders: `03-atoms.md` → Photography Direction

---

### `04_MOLECULES/`

> **The Layout Engines.** Unpopulated, editable template source masters. Build status, ownership, and which spec governs each file: **`04-molecules.md`**.

* **`04_MOLECULE_PPTX_Masters/`**
  * `Ariviti_Corporate_16x9_Master.potx`
  * `Ariviti_Printable_4x3_Master.potx`
  * Both correspond to the single `ariviti-brand.potx` entry tracked in `04-molecules.md` — split into two aspect-ratio variants at build time, one manifest entry.

* **`04_MOLECULE_DOCX_Masters/`**
  * `Ariviti_Corporate_Document_Master.dotx`
  * `Ariviti_Formal_Letterhead_Master.dotx`
  * Both correspond to `ariviti-brand.dotx` in `04-molecules.md`.

* **`04_MOLECULE_HTML_Masters/`**
  * `Email_Header_Footer_Wrapper.html` / `.mjml`
  * `Web_UI_Components/` (`.css`, `.jsx`, `.vue`)
  * Correspond to `ariviti-signature.mjml` and `ariviti-components.jsx` in `04-molecules.md`. Vue components are a folder-structure allowance not yet reflected in the manifest — add a `.vue` row to `04-molecules.md` before building, don't build ahead of the manifest.

**Rule:** nothing in this folder is built by re-deriving values from memory. Every molecule traces to `04-molecules.md`, which traces to `01`–`03`. See `04-molecules.md` → Build Principles.

---

### `05_COMPOUNDS/`

> **The Execution Layer.** Operational corporate identity items and fully populated demo templates. Content specs for everything below (Email Signature, Case Study, One-Pager, Slide Deck, LinkedIn, About Page, the GEO-Ready Content Block) are fully authored in **`05-compounds.md`** — build status is tracked there too.

* **`05_COMPOUND_Assets_AD_ID/`**
  * `AD_User_Avatar_Overlay.png` *(Slack/Teams/Outlook frame)* — 🔴 not yet specified anywhere in the system
  * `Email_Signature_Template.html` / `.pdf` — fully specified: `05-compounds.md` → Email Signature
  * `Employee_ID_Card_Front_Back.ai` — 🔴 not yet specified
  * `Digital_Business_Card_vCard.vcf` — 🔴 not yet specified
  * `Zoom_Teams_Virtual_Backgrounds/` (`1920x1080.png`) — 🔴 not yet specified
  * `Swag_&_Print_Files/` (`.ai` for merchandise, event booths, office plates) — 🔴 not yet specified

* **`05_COMPOUND_Templates/`** *(gold-standard example documents showing perfect usage)*
  * `Demo_Executive_Board_Deck.pptx` — structure specified: `05-compounds.md` → Slide Deck Template
  * `Demo_Client_Sales_Pitch.pptx` — same template, sales context
  * `Demo_Strategy_Report_OnePager.docx` — structure specified: `05-compounds.md` → One-Pager Template
  * `Demo_Monthly_Newsletter_Live.html` — 🔴 not yet specified; nearest existing pattern is the GEO-Ready Content Block in `05-compounds.md`

**Note:** the five identity/ID items above (avatar overlay, ID card, vCard, virtual backgrounds, swag) are real operational needs with zero governing spec today. They're listed here so the gap is visible, not because a template exists — do not design one ad hoc. Escalate per the Decision Rights Table (`01-strings.md` → Implementation & Governance) before creating the first version, since a first version becomes precedent.

---

## ⚡ The TABS Handoff Rule

**TABS** ends at `05_COMPOUNDS`. Everything beyond this point feeds into your dynamic **Content Engine**:

$$\text{TABS (Static System)} \xrightarrow{\quad\text{Handoff Boundary}\quad} \text{Content Engine (Dynamic Production)}$$

* **Organisms:** Custom slide decks, live web pages, active sales documents.
* **Societies:** Multi-channel campaigns, event rollouts, email sequences.
* **Civilizations:** Published whitepapers, public websites, active marketing ecosystems.

Everything on the TABS side of the boundary is governed by the five files and versioned per `01-strings.md` → Version Control. Everything past the boundary is produced *from* TABS but is not itself part of TABS — a live sales deck can go stale, get deleted, or be one-off customized without that being a brand-system change. If a pattern repeats often enough on the Content Engine side that it deserves to be locked, that's a signal to promote it into `05_COMPOUNDS` as a new template — not to leave it floating as an undocumented habit.
