**Download Iconography {#iconography-downloads-anchor}**
<div class="ariviti-file-list" data-r2-prefix="tabs/02_ATOM_Icons/"></div>

# Ariviti Icon Library

36 icons, stroke-based (Feather-derived, 2px stroke, 24×24 viewBox), matching
the geometric-but-warm feel of the brand's "guided pathway" symbol — circles,
clean line weight, no fill.

## Formats

- **`svg/*.svg`** — `currentColor` stroke, recolor via CSS `color` on the parent
- **`svg/{indigo,orange,black,gray,white}/*.svg`** — color-locked variants for
  contexts without CSS control (PowerPoint/Word embeds, print, raw `<img>` tags)
- **`sprite/ariviti-icons.svg`** — single-file sprite, reference any icon via
  `<svg><use href="ariviti-icons.svg#icon-target"/></svg>` — one HTTP request
  for the whole set

## Usage

**Web (currentColor, recolorable):**
```html
<img src="svg/target.svg" style="color: var(--ariviti-indigo)">
<!-- or inline the SVG directly so `color` actually applies (img tags don't inherit currentColor) -->
```

**Sprite (preferred for web — one request, CSS-recolorable):**
```html
<svg width="24" height="24" style="color: var(--ariviti-orange)">
  <use href="sprite/ariviti-icons.svg#icon-check"/>
</svg>
```

**PowerPoint / Word / print (color-locked variants):**
Use `svg/indigo/*.svg` etc. directly — these have the color baked in since
Office's SVG-to-shape conversion doesn't reliably preserve `currentColor`.

## Accessibility note

Icon color choices here use the **original** brand hex values (`3B3EA9` indigo,
`FF4D1C` orange), not the WCAG-corrected text variants from the contrast audit
— icons are graphical/non-text elements (WCAG 1.4.11, 3:1 threshold), and all
of these pass that bar comfortably. If an icon sits directly next to small text
of the same color, use the corrected `orange-on-light` (`#C23509`) variant
instead so icon and label read as a matched pair.

## Set (36)

target · trend · trend-down · users · shield · zap · layers · check · chart ·
pie-chart · clock · globe · cpu · award · arrow · grid · compass · database ·
mail · phone · map-pin · link · download · upload · settings · search ·
calendar · document · alert · info · star · lock · unlock · eye · filter · refresh