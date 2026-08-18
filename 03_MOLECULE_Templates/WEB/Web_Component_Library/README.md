# Ariviti Web Component Library

Framework-agnostic UI primitives for Ariviti digital properties (site, app,
internal tools). React and Vue implementations render pixel-identical output
because both consume the same `tokens/components.css` — there is exactly one
source of visual truth, not two component systems that can drift apart.

## Structure

```
Web_Component_Library/
├── tokens/
│   ├── tokens.css        # Design tokens: color, type, spacing, radius, motion
│   └── components.css    # Component styles — consumed by both React and Vue
├── react/
│   ├── Button.jsx
│   ├── Card.jsx
│   ├── Badge.jsx
│   ├── TextField.jsx
│   ├── Nav.jsx
│   └── Alert.jsx
├── vue/
│   ├── Button.vue
│   ├── Card.vue
│   ├── Badge.vue
│   ├── TextField.vue
│   ├── Nav.vue
│   └── Alert.vue
└── demo/
    └── index.html         # Static proof page — open directly in a browser
```

## Usage

**React**
```jsx
import Button from "./react/Button.jsx";
import Card from "./react/Card.jsx";

<Card eyebrow="Case Study" title="40% faster claims triage">
  A regional insurer cut manual review time using Ariviti's governed AI model.
</Card>
<Button variant="primary" onClick={handleClick}>Book a demo</Button>
```

**Vue**
```vue
<script setup>
import Button from "./vue/Button.vue";
import Card from "./vue/Card.vue";
</script>

<template>
  <Card eyebrow="Case Study" title="40% faster claims triage">
    A regional insurer cut manual review time using Ariviti's governed AI model.
  </Card>
  <Button variant="primary" @click="handleClick">Book a demo</Button>
</template>
```

Both frameworks import `tokens/components.css` automatically from within each
component file — you do not need to import it separately, though doing so
once globally (e.g. in your app's root layout) avoids duplicate `<style>`
injection when many components are used on one page.

## Components in this release

| Component | Variants / states |
|---|---|
| **Button** | primary, secondary, ghost · sm/md/lg · disabled |
| **Card** | static or interactive (hover-lift), optional eyebrow/title |
| **Badge** | neutral, brand, info, success, warning, danger |
| **TextField** | label, helper text, error state, required marker — full ARIA wiring |
| **Nav** | brand mark, link list with active state, action slot |
| **Alert** | info, success, warning, danger — icon + title + body |

## Design tokens

`tokens.css` defines primitives (`--ariviti-orange-500`, `--ariviti-indigo-700`,
etc.) and semantic aliases components actually consume (`--color-brand-primary`,
`--color-text-secondary`, etc.). Extending the palette or retheming happens by
editing token values only — never by editing component CSS directly.

Fonts (Space Grotesk / Plus Jakarta Sans) are referenced by name with a
system-font fallback stack. Load the actual webfonts in your app's `<head>`
(e.g. via Google Fonts or self-hosted `@font-face`) — this library does not
inject font-loading itself, so it stays framework- and build-tool-agnostic.

## What's not in this release

Scoped for a follow-up, not built here: Modal/Dialog, Select/Dropdown, Tabs,
Toast notifications, Table, Pagination, Tooltip. The six shipped here are the
highest-frequency primitives (every marketing page and most app screens need
buttons, cards, badges, inputs, nav, and alerts before anything else).

## Known limitation in this QA pass

The static demo screenshot (rendered via wkhtmltoimage, a legacy WebKit
engine) shows the nav links running together without visible gaps — that
engine predates CSS flexbox `gap` support (added to real browsers ~2020).
Every current browser (Chrome, Firefox, Safari, Edge) renders `.ar-nav__links`
with correct spacing; this is a QA-tool artifact, not a code defect.
