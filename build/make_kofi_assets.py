"""
Generate Ko-fi avatar (512x512) and banner (1500x500) for
AI Warrior × Te Pā Literacy / The Kiwi Dialectic.

Palette (site tokens):
  Ōpōtiki black  #0f0b09    (paper/dark background)
  kōura          #d9a441    (gold — primary accent, headings)
  kōkōwai        #c86a2a    (burnt-orange — secondary accent)
  toto           #a4181a    (bright red — the mountain stroke in the site logo)
  paper (cream)  #efe6d3    (body text on dark)

Design language matches the site: geometric SVG mark (square frame, red mountain
peak, gold horizon bar, red circle 'sun'), Fraunces-inspired display type, quiet
Swiss composition. No AI-slop gradients, no busy backgrounds — one strong shape,
one strong wordmark, plenty of black space.
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

OUT = Path(__file__).resolve().parent.parent / "assets" / "kofi"
OUT.mkdir(parents=True, exist_ok=True)

# --- palette ---
BLACK = (15, 11, 9)         # #0f0b09
GOLD = (217, 164, 65)       # #d9a441
BURNT = (200, 106, 42)      # #c86a2a
RED = (164, 24, 26)         # #a4181a
CREAM = (239, 230, 211)     # #efe6d3
MUTED = (145, 130, 110)     # softer text

# --- fonts ---
# Bundled DejaVu fonts as safe fallbacks; pick the most Fraunces-adjacent for the
# wordmark (serif) and a clean sans for the subtitle/handle.
FONT_DIRS = [
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
]

def load_font(candidates, size):
    for d in FONT_DIRS:
        for name in candidates:
            p = Path(d) / name
            if p.exists():
                return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()

SERIF_BOLD = ["DejaVuSerif-Bold.ttf", "LiberationSerif-Bold.ttf"]
SERIF_REG = ["DejaVuSerif.ttf", "LiberationSerif-Regular.ttf"]
SANS_BOLD = ["DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf"]
SANS_REG = ["DejaVuSans.ttf", "LiberationSans-Regular.ttf"]
MONO_REG = ["DejaVuSansMono.ttf", "LiberationMono-Regular.ttf"]


# ---------- shared draw helpers ----------

def draw_logo_mark(draw, cx, cy, size, stroke_gold=GOLD, stroke_red=RED,
                   circle_red=RED, base_bar=GOLD, stroke_w_scale=1.0):
    """
    Render the AI Warrior logo mark centred at (cx, cy) with total edge length `size`.
    Faithfully reproduces the site's SVG (viewBox 0 0 40 40):
      - rounded-square frame (gold on dark)
      - red mountain peak: (8,32) → (20,8) → (32,32)
      - red 'sun' circle at (20,22) r=3
      - gold horizon bar at y=32 from x=12 to x=28
    """
    s = size / 40.0            # scale factor
    half = size / 2
    x0 = cx - half
    y0 = cy - half

    def px(p):
        return (x0 + p[0] * s, y0 + p[1] * s)

    # Frame
    fw = max(2, int(round(2.4 * s * stroke_w_scale)))
    frame_r = max(2, int(round(2 * s)))
    draw.rounded_rectangle(
        [px((1.5, 1.5)), px((38.5, 38.5))],
        radius=frame_r, outline=stroke_gold, width=fw,
    )

    # Mountain peak
    mw = max(2, int(round(2.8 * s * stroke_w_scale)))
    draw.line([px((8, 32)), px((20, 8))], fill=stroke_red, width=mw, joint="curve")
    draw.line([px((20, 8)), px((32, 32))], fill=stroke_red, width=mw, joint="curve")

    # Sun
    r = 3 * s
    ccx, ccy = px((20, 22))
    draw.ellipse([ccx - r, ccy - r, ccx + r, ccy + r], fill=circle_red)

    # Horizon bar
    bw = max(2, int(round(2.2 * s * stroke_w_scale)))
    draw.line([px((12, 32)), px((28, 32))], fill=base_bar, width=bw)


def text_size(draw, text, font):
    """Return (w, h) using getbbox for accurate metrics."""
    l, t, r, b = draw.textbbox((0, 0), text, font=font)
    return r - l, b - t, l, t


# ---------- Avatar 512x512 ----------

def make_avatar():
    """
    Ko-fi crops the avatar to a circle. Composition must survive that crop and
    stay legible at 80–120px. Strategy: drop the square frame + wordmark, scale
    the mountain-peak + sun icon to fill the circle, and use a solid burnt-orange
    ring instead of the square. That gives one instantly-readable silhouette.
    """
    W = H = 512
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)

    cx = cy = W / 2

    # kōura outer ring (survives circle crop; acts as the frame)
    ring_outer_r = 236
    ring_w = 16
    d.ellipse(
        [cx - ring_outer_r, cy - ring_outer_r, cx + ring_outer_r, cy + ring_outer_r],
        outline=GOLD, width=ring_w,
    )

    # Mountain peak, hugely scaled, centred vertically slightly high to give the
    # horizon bar room to breathe.
    # Original path in the 40-unit logo: (8,32) → (20,8) → (32,32). We render this
    # directly at ~360px total width.
    peak_w = 360
    scale = peak_w / 24.0                  # x-range 8..32 = 24
    peak_left = cx - peak_w / 2
    peak_top_y = cy - 100                  # apex y
    peak_bot_y = cy + 92                   # base y
    apex = (cx, peak_top_y)
    left = (peak_left, peak_bot_y)
    right = (peak_left + peak_w, peak_bot_y)

    stroke = max(4, int(round(2.8 * scale)))
    d.line([left, apex], fill=RED, width=stroke, joint="curve")
    d.line([apex, right], fill=RED, width=stroke, joint="curve")

    # Sun — red circle inside the peak
    sun_r = int(round(3 * scale))
    sun_cy = peak_top_y + (peak_bot_y - peak_top_y) * (22 - 8) / (32 - 8)
    d.ellipse([cx - sun_r, sun_cy - sun_r, cx + sun_r, sun_cy + sun_r], fill=RED)

    # Horizon bar in kōura, echoing the site logo (12–28 on x, y=32)
    bar_x_frac = (12 - 8) / 24.0           # 0.1667
    bar_x0 = peak_left + peak_w * bar_x_frac
    bar_x1 = peak_left + peak_w * (1 - bar_x_frac)
    bar_w = max(6, int(round(2.6 * scale)))
    d.line([(bar_x0, peak_bot_y), (bar_x1, peak_bot_y)], fill=GOLD, width=bar_w)

    # Tiny kōkōwai tick above the peak apex, invisible at 80px but classes it up
    # at larger sizes — signals kaupapa attention to detail.
    tick_h = 14
    d.line([(cx, peak_top_y - 22), (cx, peak_top_y - 22 - tick_h)],
           fill=BURNT, width=4)

    out = OUT / "kofi-avatar-512.png"
    img.save(out, "PNG", optimize=True)
    return out


# ---------- Banner 1500x500 ----------

def make_banner():
    W, H = 1500, 500
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)

    # Left composition: logo mark + wordmark stack
    mark_size = 260
    mark_cx = 220
    mark_cy = H / 2
    draw_logo_mark(d, cx=mark_cx, cy=mark_cy, size=mark_size, stroke_w_scale=1.05)

    # Wordmark to the right of the mark
    f_word = load_font(SERIF_BOLD, 78)
    f_word_sub = load_font(SERIF_REG, 40)
    f_tag = load_font(SANS_REG, 22)
    f_mono = load_font(MONO_REG, 18)

    x_text = mark_cx + mark_size / 2 + 46

    # Line 1
    line1 = "AI WARRIOR"
    tw, th, lx, ty = text_size(d, line1, f_word)
    y1 = mark_cy - 92
    d.text((x_text - lx, y1 - ty), line1, font=f_word, fill=GOLD)

    # Cross / multiplier
    f_x = load_font(SERIF_REG, 78)
    cross_x = x_text + tw + 22
    tw_x, th_x, lx_x, ty_x = text_size(d, "×", f_x)
    d.text((cross_x - lx_x, y1 - ty_x), "×", font=f_x, fill=BURNT)

    # Line 2 — Te Pā Literacy
    line2 = "TE PĀ LITERACY"
    tw2, th2, lx2, ty2 = text_size(d, line2, f_word_sub)
    y2 = y1 + th + 18
    d.text((x_text - lx2, y2 - ty2), line2, font=f_word_sub, fill=CREAM)

    # Divider rule (kōura hairline)
    y3 = y2 + th2 + 26
    d.rectangle([x_text, y3, x_text + 380, y3 + 2], fill=GOLD)

    # Tagline
    tag = "Kaupapa Māori digital literacy · openly licensed · whānau-funded"
    tw_t, th_t, lx_t, ty_t = text_size(d, tag, f_tag)
    d.text((x_text - lx_t, y3 + 22 - ty_t), tag, font=f_tag, fill=CREAM)

    # URL row
    url = "ko-fi.com/thekiwidialectic"
    tw_u, th_u, lx_u, ty_u = text_size(d, url, f_mono)
    d.text((x_text - lx_u, y3 + 60 - ty_u), url, font=f_mono, fill=BURNT)

    # Right-side accent: three stacked bars (echoing the horizon in the mark)
    bar_x = W - 220
    bar_w = 150
    for i, (color, dy) in enumerate([(GOLD, 0), (BURNT, 32), (RED, 64)]):
        bh = 8
        d.rectangle([bar_x, mark_cy - 40 + dy, bar_x + bar_w, mark_cy - 40 + dy + bh],
                    fill=color)

    # Vertical whakataukī column on the far right
    f_verse = load_font(SERIF_REG, 20)
    verse_lines = [
        "Whāia te iti kahurangi",
        "ki te tuohu koe",
        "me he maunga teitei.",
    ]
    vy = mark_cy + 60
    for line in verse_lines:
        tw_v, th_v, lx_v, ty_v = text_size(d, line, f_verse)
        d.text((W - 40 - tw_v - lx_v, vy - ty_v), line, font=f_verse, fill=MUTED)
        vy += th_v + 6

    # Subtle top/bottom safe-area markers (invisible in output — omitted)

    out = OUT / "kofi-banner-1500x500.png"
    img.save(out, "PNG", optimize=True)
    return out


if __name__ == "__main__":
    a = make_avatar()
    b = make_banner()
    print("avatar:", a)
    print("banner:", b)
