# Ariviti Imagery & Photography Treatment Guide

**No real brand photography exists yet.** Every example image in this folder
is a synthetic stand-in (gradient + shapes) used only to verify the treatment
*mechanics* — crop math and duotone color mapping — work correctly. Do not
mistake `sample_source.jpg` for brand photography; swap in real photos and
re-run the same treatment rules once they exist.

## Crop ratios

| Ratio | Use case | Example file |
|---|---|---|
| 16:9 | Slide/deck imagery, video thumbnails, web hero banners | `crop_16x9.jpg` |
| 1:1 | Social posts (LinkedIn square), avatar/team photos | `crop_1x1.jpg` |
| 4:5 | LinkedIn/Instagram portrait posts | `crop_4x5.jpg` |

**Crop from center, always.** Don't crop tighter than necessary to hit the
ratio — the goal is a consistent frame across a photo set, not maximum zoom.
For photos with a clear single subject (headshots, product shots), bias the
crop to keep the subject in the upper third, not dead-center, per standard
portrait composition.

## Duotone treatment

Two approved duotone maps, built with a verified per-channel lookup table
(shadow color → highlight color, mapped across the full tonal range — not a
simple color overlay, which muddies mid-tones):

| Name | Shadow | Highlight | When to use |
|---|---|---|---|
| **Indigo Duotone** (primary) | `#1E1669` (Indigo Dark) | `#F4F4F8` (Mist) | Default treatment — case study headers, report cover imagery, section dividers behind photography |
| **Orange Duotone** (accent) | `#2E2E2E` (Soft Black) | `#FF8A5C` (orange tint) | High-energy contexts only — event photography, culture/hiring content. Don't use for client-facing case studies; it reads as promotional, not evidentiary |

**Why duotone instead of full color:** it's the single highest-leverage move
for making photos from different sources (stock, phone photos, professional
shoots) look like one consistent library, without needing every photo to be
professionally shot and color-graded. It also print-reproduces reliably
(no color-matching risk the way full-color CMYK photography has).

**Do not:** apply duotone to photos that already contain brand-colored UI
screenshots (dashboards, product screens) — it will shift the product's own
colors and misrepresent the interface. Duotone is for people/place/environment
photography only.

## What's still open

- Real photography doesn't exist — this guide is ready to apply the moment
  a shoot or licensed photo library is available.
- No guidance yet on illustration/iconography-over-photo compositing style,
  or motion/video treatment — scope for a follow-up once static photography
  direction is confirmed as correct.
