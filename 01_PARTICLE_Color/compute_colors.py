import json, colorsys

# ============================================================
# Canonical Ariviti color definitions
# Source: LY_-_Ariviti_Brand_Guidelines.pdf (Primary/Secondary),
# extended with the neutral/feedback ramps established in the
# Web_Component_Library tokens for a complete developer system.
# ============================================================
COLORS = {
    # --- Primary (from brand guideline) ---
    "orange":       {"hex": "FF4D1C", "label": "Vibrant Orange", "group": "primary"},
    "indigo":       {"hex": "3B3EA9", "label": "Royal Indigo",   "group": "primary"},
    "indigo-dark":  {"hex": "1E1669", "label": "Indigo Dark",    "group": "primary"},  # brand guide gradient endpoint

    # --- Secondary (from brand guideline) ---
    "white":        {"hex": "FFFFFF", "label": "White",     "group": "secondary"},
    "soft-black":   {"hex": "2E2E2E", "label": "Soft Black", "group": "secondary"},

    # --- Neutral ramp (developer extension, not in brand guideline) ---
    "mist":         {"hex": "F4F4F8", "label": "Mist",       "group": "neutral"},
    "mist-2":       {"hex": "ECEDF6", "label": "Mist 2",      "group": "neutral"},
    "line":         {"hex": "E1E2EC", "label": "Line",       "group": "neutral"},
    "gray":         {"hex": "6B6B76", "label": "Gray",       "group": "neutral"},
    "gray-light":   {"hex": "9A9AA6", "label": "Gray Light",  "group": "neutral"},

    # --- Feedback ramp (developer extension, not in brand guideline) ---
    "success":      {"hex": "1E9E5A", "label": "Success", "group": "feedback"},
    "warning":      {"hex": "B8860B", "label": "Warning", "group": "feedback"},
    "danger":       {"hex": "D42A2A", "label": "Danger",  "group": "feedback"},
}

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hsl(r, g, b):
    h, l, s = colorsys.rgb_to_hls(r/255, g/255, b/255)
    return round(h*360, 1), round(s*100, 1), round(l*100, 1)

def rgb_to_cmyk_naive(r, g, b):
    """Uncalibrated RGB->CMYK (device-independent formula). NOT a substitute
    for a proper ICC-profiled conversion — flagged in every output file."""
    if (r, g, b) == (0, 0, 0):
        return 0, 0, 0, 100
    rp, gp, bp = r/255, g/255, b/255
    k = 1 - max(rp, gp, bp)
    c = (1 - rp - k) / (1 - k) if k < 1 else 0
    m = (1 - gp - k) / (1 - k) if k < 1 else 0
    y = (1 - bp - k) / (1 - k) if k < 1 else 0
    return round(c*100), round(m*100), round(y*100), round(k*100)

# Compute full data for every color
for key, c in COLORS.items():
    r, g, b = hex_to_rgb(c["hex"])
    h, s, l = rgb_to_hsl(r, g, b)
    cy, m, ye, k = rgb_to_cmyk_naive(r, g, b)
    c.update({
        "rgb": {"r": r, "g": g, "b": b},
        "hsl": {"h": h, "s": s, "l": l},
        "cmyk": {"c": cy, "m": m, "y": ye, "k": k},
    })

print(json.dumps(COLORS, indent=2)[:800])
