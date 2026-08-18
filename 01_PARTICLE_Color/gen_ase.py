"""
Adobe Swatch Exchange (.ase) writer.
Format is community-reverse-engineered but stable and widely implemented
(Illustrator, Photoshop, InDesign, Affinity, Sketch, Figma-via-plugin all
read it). Structure:

  4s   signature "ASEF"
  H H  version major, minor
  I    block count
  per block:
    H    block type (0xC001 group start, 0xC002 group end, 0x0001 color entry)
    I    block data length (bytes following this field)
    -- color entry data --
    H          name length, in UTF-16 code units INCLUDING null terminator
    (name)     UTF-16BE, null-terminated
    4s         color model ASCII, padded to 4 bytes: "RGB ", "CMYK", "GRAY", "LAB "
    floats     big-endian f32, count depends on model (RGB=3, CMYK=4, GRAY=1, LAB=3)
    H          color type: 0=Global, 1=Spot, 2=Process
"""
import struct

def _pack_name(name):
    utf16 = name.encode("utf-16-be") + b"\x00\x00"
    n_units = len(utf16) // 2
    return struct.pack(">H", n_units) + utf16

def _color_entry_block(name, model, values, color_type=2):
    """model: 'RGB ', 'CMYK', 'GRAY', 'LAB '. values: tuple of floats 0.0-1.0 (or 0-100 for LAB L)."""
    body = _pack_name(name)
    model_bytes = model.encode("ascii")
    assert len(model_bytes) == 4
    body += model_bytes
    for v in values:
        body += struct.pack(">f", v)
    body += struct.pack(">H", color_type)
    block_type = 0x0001
    return struct.pack(">HI", block_type, len(body)) + body

def _group_start(name):
    body = _pack_name(name)
    return struct.pack(">HI", 0xC001, len(body)) + body

def _group_end():
    return struct.pack(">HI", 0xC002, 0)

def write_ase(path, groups):
    """
    groups: list of (group_name_or_None, [(swatch_name, model, values), ...])
    If group_name is None, colors are written flat (no group wrapper).
    """
    blocks = []
    for group_name, swatches in groups:
        if group_name:
            blocks.append(_group_start(group_name))
        for name, model, values in swatches:
            blocks.append(_color_entry_block(name, model, values))
        if group_name:
            blocks.append(_group_end())

    block_count = 0
    for group_name, swatches in groups:
        block_count += len(swatches)
        if group_name:
            block_count += 2  # start + end

    header = b"ASEF" + struct.pack(">HHI", 1, 0, block_count)
    with open(path, "wb") as f:
        f.write(header)
        for b in blocks:
            f.write(b)

if __name__ == "__main__":
    from compute_colors import COLORS

    def rgb01(hexstr):
        r, g, b = int(hexstr[0:2], 16), int(hexstr[2:4], 16), int(hexstr[4:6], 16)
        return (r/255, g/255, b/255)

    # --- Palette_Primary.ase ---
    primary = [c for k, c in COLORS.items() if c["group"] == "primary"]
    swatches = [(c["label"], "RGB ", rgb01(c["hex"])) for c in primary]
    write_ase("01_PARTICLE_Color/Palette_Primary.ase", [("Ariviti Primary", swatches)])

    # --- Palette_Secondary.ase ---
    secondary = [c for k, c in COLORS.items() if c["group"] == "secondary"]
    swatches = [(c["label"], "RGB ", rgb01(c["hex"])) for c in secondary]
    write_ase("01_PARTICLE_Color/Palette_Secondary.ase", [("Ariviti Secondary", swatches)])

    # --- Palette_Print_CMYK.ase (CMYK color model, all brand colors) ---
    def cmyk01(c):
        return (c["cmyk"]["c"]/100, c["cmyk"]["m"]/100, c["cmyk"]["y"]/100, c["cmyk"]["k"]/100)
    all_brand = [c for k, c in COLORS.items() if c["group"] in ("primary", "secondary")]
    swatches = [(f"{c['label']} (CMYK)", "CMYK", cmyk01(c)) for c in all_brand]
    write_ase("01_PARTICLE_Color/Palette_Print_CMYK.ase", [("Ariviti Print (CMYK)", swatches)])

    print("Wrote 3 .ase files")
