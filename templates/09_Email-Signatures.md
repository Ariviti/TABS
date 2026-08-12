# Email Signatures
*Annexure to Ariviti Brand Guidelines · Not covered in core BG — built fresh, low-maintenance by design*

## Principle

An email signature is seen more often than almost any other brand asset — and is the easiest one to let drift, because everyone edits their own. **Lock the template, not the person's willingness to comply.**

---

## Standard Template

```
[Full Name]
[Role] · Ariviti

[Symbol icon, 32px]  ariviti.com
[Phone — optional, only if role-appropriate]

Intelligence Amplified.
```

**Typography:** Plus Jakarta Sans only (Space Grotesk and Chillax don't render reliably across email clients — see rendering note below).
**Colors:** Name in Soft Black `#2E2E2E`. Role and links in Royal Indigo `#3B3EA9`. No Orange in signatures — small orange text fails contrast (see Accessibility doc) and email clients often can't render it consistently anyway.

---

## HTML Reference Block

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
    <td colspan="2" style="padding-top:8px; font-style:italic; color:#2E2E2E;">
      Intelligence Amplified.
    </td>
  </tr>
</table>
```

---

## Do / Don't

| Do | Don't |
|---|---|
| Use the symbol icon only (32px), never the full lockup — full lockup at signature scale falls below the 24px minimum size and blurs | Embed the full-color primary lockup as a large banner image |
| Use web-safe fallback fonts (`Arial, sans-serif`) since Plus Jakarta Sans isn't guaranteed to render in Outlook | Rely on custom fonts rendering correctly across all mail clients |
| Keep it to 4 lines maximum | Add quotes, social icons, calendar-booking banners, or promotional graphics — every addition is a new maintenance liability and a new place to go off-brand |
| Update centrally and redistribute (via IT/Google Workspace signature policy if available) | Let each employee hand-edit their own signature file |

---

## Why No Tagline Variation, No Campaign Banners

Signatures are infrastructure, not marketing real estate. Every "temporary" campaign banner in a signature outlives the campaign by months and becomes a compliance debt. If a campaign needs promotion, it goes in the newsletter or LinkedIn — never the signature.

---

## Governance

One person owns the signature template (see Implementation doc's decision-rights table). Updates ship as a single distributed file or workspace policy push — never as a "please update your signature" email that half the team ignores.
