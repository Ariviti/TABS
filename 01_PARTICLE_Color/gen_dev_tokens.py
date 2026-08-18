from compute_colors import COLORS
import json

OUT = "/home/claude/color_build/01_PARTICLE_Color"

# ============================================================
# tokens_color.json — full multi-format token export, incl.
# a Tailwind-ready `tailwindExtend` block
# ============================================================
def rgb_str(c): return f"rgb({c['rgb']['r']}, {c['rgb']['g']}, {c['rgb']['b']})"
def hsl_str(c): return f"hsl({c['hsl']['h']}, {c['hsl']['s']}%, {c['hsl']['l']}%)"
def cmyk_str(c): return f"cmyk({c['cmyk']['c']}%, {c['cmyk']['m']}%, {c['cmyk']['y']}%, {c['cmyk']['k']}%)"

tokens = {
    "$schema": "Ariviti color tokens — generated, do not hand-edit; regenerate from compute_colors.py",
    "meta": {
        "brand": "Ariviti",
        "source": "LY_-_Ariviti_Brand_Guidelines.pdf (primary/secondary); neutral + feedback ramps are a developer extension, not in the brand guideline",
        "cmykNote": "CMYK values use an uncalibrated device-independent formula (naive RGB->CMYK). For press production, get color-matched CMYK from your print house's ICC profile — do not rely on these for print-critical work.",
    },
    "colors": {},
    "tailwindExtend": {"colors": {}},
}

for key, c in COLORS.items():
    tokens["colors"][key] = {
        "label": c["label"],
        "group": c["group"],
        "hex": f"#{c['hex']}",
        "rgb": c["rgb"],
        "rgbString": rgb_str(c),
        "hsl": c["hsl"],
        "hslString": hsl_str(c),
        "cmyk": c["cmyk"],
        "cmykString": cmyk_str(c),
    }
    tokens["tailwindExtend"]["colors"][key] = f"#{c['hex']}"

with open(f"{OUT}/tokens_color.json", "w") as f:
    json.dump(tokens, f, indent=2)
    f.write("\n")

# ============================================================
# colors.css — CSS custom properties
# ============================================================
css_lines = [
    "/**",
    " * Ariviti Color Tokens — CSS Custom Properties",
    " * Generated file — see tokens_color.json for the source of truth",
    " * across formats (hex/rgb/hsl/cmyk) and compute_colors.py for the",
    " * conversion logic.",
    " *",
    " * CMYK values are NOT included here (CSS has no CMYK color function",
    " * in current browser support) — see tokens_color.json for print use.",
    " */",
    "",
    ":root {",
]
by_group = {}
for key, c in COLORS.items():
    by_group.setdefault(c["group"], []).append((key, c))

for group, items in by_group.items():
    css_lines.append(f"  /* {group.capitalize()} */")
    for key, c in items:
        css_lines.append(f"  --ariviti-{key}: #{c['hex']};  /* {c['label']} — {rgb_str(c)} */")
    css_lines.append("")
css_lines.append("}")

with open(f"{OUT}/colors.css", "w") as f:
    f.write("\n".join(css_lines).rstrip() + "\n")

# ============================================================
# colors.scss — SCSS variables + a $ariviti-colors map
# ============================================================
scss_lines = [
    "//",
    "// Ariviti Color Tokens — SCSS Variables",
    "// Generated file — see tokens_color.json for the source of truth.",
    "//",
    "",
]
for group, items in by_group.items():
    scss_lines.append(f"// {group.capitalize()}")
    for key, c in items:
        scss_lines.append(f"$ariviti-{key}: #{c['hex']};  // {c['label']}")
    scss_lines.append("")

scss_lines.append("// Map form, for programmatic access: map-get($ariviti-colors, 'orange')")
scss_lines.append("$ariviti-colors: (")
entries = []
for key, c in COLORS.items():
    entries.append(f"  '{key}': #{c['hex']}")
scss_lines.append(",\n".join(entries))
scss_lines.append(");")

with open(f"{OUT}/colors.scss", "w") as f:
    f.write("\n".join(scss_lines).rstrip() + "\n")

print("Generated tokens_color.json, colors.css, colors.scss")
