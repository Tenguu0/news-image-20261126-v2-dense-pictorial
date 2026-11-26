#!/usr/bin/env python3
"""news-image-20261126 v2-dense-pictorial — dense newspaper front page.

Renders entry.png (1024x1024, deterministic, no network) from the
AI-pictorial illustrations in assets/ and the bundled DejaVu fonts.

Usage:
    python3 main.py                       # writes entry.png beside main.py
    MAKEFUN_OUTPUT_DIR=out python3 main.py  # writes out/entry.png
"""
import os
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
FONTS = ASSETS / "fonts"

W, H = 1024, 1024
PAPER = (247, 243, 234)      # off-white newsprint
INK = (24, 24, 24)
RED = (178, 34, 34)
BLUE = (31, 68, 120)
GREY = (96, 96, 96)
RULE = (24, 24, 24)


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to a pixel width; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit(path, w, h):
    """Center-crop the asset to exactly w x h (deterministic)."""
    return ImageOps.fit(Image.open(path).convert("RGB"), (w, h),
                        Image.LANCZOS, centering=(0.5, 0.5))


def para(draw, x, y, text, fnt, width, fill=INK, leading=None, max_lines=None):
    """Draw wrapped paragraph; returns y after last line."""
    leading = leading or int(fnt.size * 1.28)
    lines = wrap(draw, text, fnt, width)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        while lines and draw.textlength(lines[-1] + "…", font=fnt) > width:
            lines[-1] = lines[-1][:-1]
        lines[-1] += "…"
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    MX = 22                      # side margin
    CW = W - 2 * MX              # content width

    # ---- Masthead -------------------------------------------------------
    title = "THE WORLD IN ONE PAGE"
    tf = SERIF_B(44)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 14), title, font=tf, fill=INK)
    d.line([(MX, 72), (W - MX, 72)], fill=RULE, width=3)
    d.line([(MX, 78), (W - MX, 78)], fill=RULE, width=1)
    date = "THURSDAY 26 NOVEMBER 2026"
    df = SANS_B(17)
    d.text((MX, 86), date, font=df, fill=RED)
    tag = "WORLD NEWS IN ONE IMAGE"
    d.text((W - MX - d.textlength(tag, font=df), 86), tag, font=df, fill=INK)
    d.line([(MX, 112), (W - MX, 112)], fill=RULE, width=1)

    # ---- Lead story -----------------------------------------------------
    ly, lh = 122, 216
    img.paste(fit(ASSETS / "lead-refinery.png", 470, lh), (MX, ly))
    lx = MX + 470 + 16
    lw = W - MX - lx
    y = ly
    d.text((lx, y), "MIDDLE EAST  •  OIL", font=SANS_B(13), fill=RED)
    y += 22
    y = para(d, lx, y,
             "Houthis say they hit Ras Tanura; Brent jumps past $94",
             SERIF_B(27), lw, leading=32)
    y += 4
    y = para(d, lx, y,
             "Yemen's Houthis said they attacked Saudi Arabia's Ras Tanura "
             "refinery and Riyadh's financial district. Saudi forces said "
             "they shot down four drones over Ras Tanura.",
             SANS(15), lw, leading=19)
    y += 6
    d.text((lx, y), "Brent $94.61 (+3.5%)  •  WTI $83.68 (+2%)",
           font=SANS_B(14), fill=BLUE)

    d.line([(MX, 352), (W - MX, 352)], fill=RULE, width=2)

    # ---- Grid 4 x 3 ------------------------------------------------------
    stories = [
        ("STRAIT OF HORMUZ", "hormuz-tankers.png",
         "Tankers hit by mines in Strait of Hormuz",
         "Two tankers hit naval mines in the strait, raising "
         "fears for shipping."),
        ("GAZA", "gaza-strike.png",
         "Israel kills Hamas security chief in Gaza",
         "Hamas colonel Abuelouf was killed; his wife and two "
         "children also died."),
        ("UKRAINE", "ukraine-refinery.png",
         "Ukraine hits two Russian oil refineries",
         "Two Russian refineries were struck overnight; Putin "
         "vowed retaliation."),
        ("SPACE", "astronaut-tiangong.png",
         "First Pakistani astronaut heads to Tiangong",
         "Zeeshan Ali will fly on Shenzhou-24, the first "
         "foreigner to visit Tiangong."),
        ("TRADE", "tariffs-port.png",
         "US proposes tariffs of up to 15% on Taiwan goods",
         "The plan targets semiconductors; Taiwan says its rate "
         "is in the lowest tier."),
        ("SCIENCE", "asteroid-crater.png",
         "Hera reveals crater on asteroid DART struck",
         "Hera showed Dimorphos flattened by a stadium-size "
         "crater from the 2022 test."),
        ("CHESS", "chess-gukesh.png",
         "Gukesh draws Game 2 of world title match",
         "The champion drew with Sindarov in 20 moves with "
         "white in Geneva."),
        ("CRICKET", "cricket-record.png",
         "Sooryavanshi, 15, smashes record double century",
         "Sooryavanshi hit 204 off 53 balls vs UAE, the fastest "
         "List A double hundred."),
        ("INDIA", "india-constitution.png",
         "India marks Constitution Day and 26/11 anniversary",
         "The nation marked Samvidhan Divas and 18 years since the "
         "2008 Mumbai attacks."),
        ("BANGLADESH", "bangladesh-garment.png",
         "Bangladesh raises garment wage by 36%",
         "The minimum monthly wage for entry-level garment workers "
         "rises sharply."),
        ("ECONOMY", "fed-beige.png",
         "Fed: modest growth, prices still pressured",
         "The Beige Book found modest growth, wage gains and "
         "persistent price pressure."),
        ("EGYPT", "cairo-fire.png",
         "Cairo tanker fire kills at least 30",
         "A tanker crash set a Cairo highway ablaze, killing "
         "at least 30 people."),
    ]
    gx, gy = MX, 360
    gap = 10
    cell_w = (CW - 3 * gap) // 4
    cell_h = 170
    img_h = 100
    for i, (kicker, asset, head, body) in enumerate(stories):
        r, c = divmod(i, 4)
        x = gx + c * (cell_w + gap)
        yy = gy + r * (cell_h + 8)
        img.paste(fit(ASSETS / asset, cell_w, img_h), (x, yy))
        ty = yy + img_h + 5
        d.text((x, ty), kicker, font=SANS_B(10), fill=RED)
        ty += 14
        ty = para(d, x, ty, head, SANS_B(14), cell_w, leading=16, max_lines=2)
        para(d, x, ty, body, SANS(11), cell_w, leading=13, max_lines=2)

    # ---- Also today strip ------------------------------------------------
    ay = 908
    d.line([(MX, ay), (W - MX, ay)], fill=RULE, width=2)
    d.text((MX, ay + 8), "ALSO TODAY", font=SANS_B(13), fill=RED)
    also = [
        "IPL 2027 auction draws 1,220 players",
        "Solomon Islands and Australia sign security treaty",
        "North Korea orders Swiss office in Pyongyang shut",
        "Duran Duran guitarist Andy Taylor dies at 65",
    ]
    ax = MX
    for item in also:
        para(d, ax, ay + 28, "•  " + item, SANS(12), cell_w, leading=15)
        ax += cell_w + gap

    # ---- Footer ----------------------------------------------------------
    fy = 982
    d.line([(MX, fy), (W - MX, fy)], fill=RULE, width=1)
    foot = ("All pictures are AI-generated illustrations, not photographs of "
            "the events.  •  Sources: Reuters, ESA, BBC, 26 November 2026.")
    ff = SANS(11)
    fw = d.textlength(foot, font=ff)
    d.text(((W - fw) / 2, fy + 8), foot, font=ff, fill=GREY)

    outdir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", str(ROOT)))
    outdir.mkdir(parents=True, exist_ok=True)
    out = outdir / "entry.png"
    img.save(out, "PNG")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
