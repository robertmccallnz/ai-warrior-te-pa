"""
Full social + Substack asset kit for AI Warrior × Te Pā Literacy /
The Kiwi Dialectic. Uses the site palette to keep visual unity across
Substack, X, Bluesky, Facebook, Instagram, LinkedIn, GitHub, YouTube.

Palette:
  Ōpōtiki black  #0f0b09
  kōura          #d9a441
  kōkōwai        #c86a2a
  toto           #a4181a
  paper          #efe6d3
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"

# ---------- palette ----------
BLACK  = (15, 11, 9)        # #0f0b09
GOLD   = (217, 164, 65)     # #d9a441
BURNT  = (200, 106, 42)     # #c86a2a
RED    = (164, 24, 26)      # #a4181a
CREAM  = (239, 230, 211)    # #efe6d3
MUTED  = (145, 130, 110)


# ---------- font loading ----------
FONT_DIRS = [
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
]

def _font(names, size):
    for d in FONT_DIRS:
        for n in names:
            p = Path(d) / n
            if p.exists():
                return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()

SERIF_BOLD = ["DejaVuSerif-Bold.ttf",  "LiberationSerif-Bold.ttf"]
SERIF_REG  = ["DejaVuSerif.ttf",       "LiberationSerif-Regular.ttf"]
SANS_BOLD  = ["DejaVuSans-Bold.ttf",   "LiberationSans-Bold.ttf"]
SANS_REG   = ["DejaVuSans.ttf",        "LiberationSans-Regular.ttf"]
MONO_REG   = ["DejaVuSansMono.ttf",    "LiberationMono-Regular.ttf"]


def tsize(draw, text, font):
    l, t, r, b = draw.textbbox((0, 0), text, font=font)
    return r - l, b - t, l, t


# ---------- shared graphic primitives ----------

def draw_circle_mark(d, cx, cy, radius, ring_w=None, peak_scale=0.72,
                    show_tick=True):
    """
    The circular AI Warrior mark: kōura ring, red mountain peak
    (8,32) → (20,8) → (32,32) on the original 40-unit grid, red sun,
    kōura horizon bar. Radius is the OUTER ring radius.
    """
    if ring_w is None:
        ring_w = max(4, int(radius * 0.068))

    d.ellipse([cx - radius, cy - radius, cx + radius, cy + radius],
              outline=GOLD, width=ring_w)

    # Peak
    peak_w = radius * 2 * peak_scale
    scale  = peak_w / 24.0
    peak_left  = cx - peak_w / 2
    peak_top_y = cy - radius * 0.42
    peak_bot_y = cy + radius * 0.39
    apex  = (cx, peak_top_y)
    left  = (peak_left,          peak_bot_y)
    right = (peak_left + peak_w, peak_bot_y)

    stroke = max(3, int(round(2.8 * scale)))
    d.line([left, apex],  fill=RED, width=stroke, joint="curve")
    d.line([apex, right], fill=RED, width=stroke, joint="curve")

    # Sun
    sun_r = int(round(3 * scale))
    sun_cy = peak_top_y + (peak_bot_y - peak_top_y) * (22 - 8) / (32 - 8)
    d.ellipse([cx - sun_r, sun_cy - sun_r, cx + sun_r, sun_cy + sun_r], fill=RED)

    # Horizon bar
    bar_x_frac = (12 - 8) / 24.0
    bar_x0 = peak_left + peak_w * bar_x_frac
    bar_x1 = peak_left + peak_w * (1 - bar_x_frac)
    bar_w  = max(3, int(round(2.6 * scale)))
    d.line([(bar_x0, peak_bot_y), (bar_x1, peak_bot_y)], fill=GOLD, width=bar_w)

    if show_tick and radius > 60:
        tick_h = max(6, int(radius * 0.055))
        d.line([(cx, peak_top_y - tick_h - 4),
                (cx, peak_top_y - 4)], fill=BURNT, width=max(2, int(radius * 0.017)))


def draw_square_mark(d, cx, cy, size, stroke_w_scale=1.0):
    """
    Square-frame version of the mark (matches the SVG in the site nav).
    Used for the banner left column where the frame reads cleanly.
    """
    s = size / 40.0
    half = size / 2
    x0 = cx - half
    y0 = cy - half

    def px(p): return (x0 + p[0] * s, y0 + p[1] * s)

    fw = max(2, int(round(2.4 * s * stroke_w_scale)))
    frame_r = max(2, int(round(2 * s)))
    d.rounded_rectangle([px((1.5, 1.5)), px((38.5, 38.5))],
                        radius=frame_r, outline=GOLD, width=fw)

    mw = max(2, int(round(2.8 * s * stroke_w_scale)))
    d.line([px((8, 32)), px((20, 8))],  fill=RED, width=mw, joint="curve")
    d.line([px((20, 8)), px((32, 32))], fill=RED, width=mw, joint="curve")

    r = 3 * s
    ccx, ccy = px((20, 22))
    d.ellipse([ccx - r, ccy - r, ccx + r, ccy + r], fill=RED)

    bw = max(2, int(round(2.2 * s * stroke_w_scale)))
    d.line([px((12, 32)), px((28, 32))], fill=GOLD, width=bw)


def draw_horizon_bars(d, x, y, w=150, gap=32, thickness=8):
    """Three stacked accent bars, kōura → kōkōwai → toto."""
    for i, color in enumerate([GOLD, BURNT, RED]):
        d.rectangle([x, y + i * gap, x + w, y + i * gap + thickness], fill=color)


def draw_hairline(d, x, y, w, color=GOLD, h=2):
    d.rectangle([x, y, x + w, y + h], fill=color)


# ---------- avatar variants ----------

def make_circle_avatar(size, path, ring_scale=0.92):
    """Circle-crop-safe avatar. Used for X, Bluesky, FB, IG, LinkedIn, YouTube."""
    path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (size, size), BLACK)
    d = ImageDraw.Draw(img)
    r = int(size / 2 * ring_scale)
    draw_circle_mark(d, size / 2, size / 2, r)
    img.save(path, "PNG", optimize=True)
    return path


def make_square_avatar(size, path):
    """Square avatar (GitHub uses square)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (size, size), BLACK)
    d = ImageDraw.Draw(img)
    mark_size = int(size * 0.68)
    draw_square_mark(d, size / 2, size / 2, mark_size, stroke_w_scale=1.05)
    img.save(path, "PNG", optimize=True)
    return path


# ---------- banner base + composition helpers ----------

def _banner_base(W, H, bg=BLACK):
    img = Image.new("RGB", (W, H), bg)
    return img, ImageDraw.Draw(img)


def draw_wordmark(d, x, y, size_line1=70, size_line2=36,
                  line1="AI WARRIOR", line2="TE PĀ LITERACY",
                  color1=GOLD, color2=CREAM, cross_between=False):
    """Two-line wordmark. Returns bottom-y of the block."""
    f1 = _font(SERIF_BOLD, size_line1)
    w1, h1, lx1, ty1 = tsize(d, line1, f1)
    d.text((x - lx1, y - ty1), line1, font=f1, fill=color1)

    if cross_between:
        cs = int(size_line1 * 1.0)
        fc = _font(SERIF_REG, cs)
        w_cross, h_c, lx_c, ty_c = tsize(d, "×", fc)
        d.text((x + w1 + int(size_line1 * 0.28) - lx_c, y - ty_c),
               "×", font=fc, fill=BURNT)

    y2 = y + h1 + int(size_line1 * 0.22)
    f2 = _font(SERIF_REG, size_line2)
    w2, h2, lx2, ty2 = tsize(d, line2, f2)
    d.text((x - lx2, y2 - ty2), line2, font=f2, fill=color2)

    return y2 + h2


# ---------- banner recipes ----------

def make_substack_banner():
    """
    Substack publication header: 1456×180 recommended.
    Substack shows this above the title on the homepage. Left = mark,
    centre = wordmark, right = tagline + URL.
    """
    W, H = 1456, 180
    img, d = _banner_base(W, H)

    # Mark
    draw_circle_mark(d, cx=90, cy=H / 2, radius=72)

    # Wordmark
    x_text = 190
    f1 = _font(SERIF_BOLD, 42)
    line1 = "THE KIWI DIALECTIC"
    w1, h1, lx1, ty1 = tsize(d, line1, f1)
    y1 = H / 2 - h1 - 6
    d.text((x_text - lx1, y1 - ty1), line1, font=f1, fill=GOLD)

    f2 = _font(SERIF_REG, 22)
    line2 = "AI Warrior × Te Pā Literacy · socialist essays, kaupapa Māori tech"
    w2, h2, lx2, ty2 = tsize(d, line2, f2)
    y2 = H / 2 + 12
    d.text((x_text - lx2, y2 - ty2), line2, font=f2, fill=CREAM)

    # Right: URL + accent bars
    draw_horizon_bars(d, x=W - 220, y=H / 2 - 48, w=120, gap=20, thickness=5)
    fu = _font(MONO_REG, 16)
    url = "thekiwidialectic.substack.com"
    wu, hu, lxu, tyu = tsize(d, url, fu)
    d.text((W - 40 - wu - lxu, H - 40 - tyu), url, font=fu, fill=BURNT)

    path = OUT / "substack" / "substack-banner-1456x180.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "PNG", optimize=True)
    return path


def make_substack_logo():
    """Substack also has a small square publication logo (256×256)."""
    path = OUT / "substack" / "substack-logo-256.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    return make_circle_avatar(256, path)


# --- generic wide social banner factory ---

def make_social_banner(W, H, path, *,
                       mark_radius=None,
                       title="AI WARRIOR",
                       subtitle="TE PĀ LITERACY",
                       tagline="Kaupapa Māori digital literacy · openly licensed · whānau-funded",
                       url="thekiwidialectic.substack.com",
                       show_bars=True,
                       show_verse=True,
                       safe_center_fraction=0.55,
                       text_scale=1.0):
    """
    Wide banner. Everything critical stays inside the horizontal centre
    `safe_center_fraction` of the width, because most platforms crop the
    banner edges on mobile.
    """
    img, d = _banner_base(W, H)

    # Layout inside the safe centre band
    safe_w = int(W * safe_center_fraction)
    safe_x0 = (W - safe_w) // 2
    safe_x1 = safe_x0 + safe_w

    # Sizes scale with H, but also honour text_scale for banners where the safe
    # centre is much narrower than the full width (YouTube 2560×1440 with a
    # 1546-wide safe band, for example).
    scale = (H / 500.0) * text_scale
    mark_r = mark_radius if mark_radius else int(120 * scale)
    title_pt = max(28, int(78 * scale))
    sub_pt   = max(20, int(38 * scale))
    tag_pt   = max(14, int(22 * scale))
    url_pt   = max(12, int(18 * scale))

    # Mark on the left of the safe band
    mark_cx = safe_x0 + mark_r + int(20 * scale)
    mark_cy = H // 2
    draw_circle_mark(d, mark_cx, mark_cy, mark_r)

    # Wordmark to the right of the mark
    x_text = mark_cx + mark_r + int(50 * scale)
    f1 = _font(SERIF_BOLD, title_pt)
    w1, h1, lx1, ty1 = tsize(d, title, f1)
    y_title = mark_cy - h1 - int(10 * scale)
    d.text((x_text - lx1, y_title - ty1), title, font=f1, fill=GOLD)

    # × mark
    fc = _font(SERIF_REG, title_pt)
    cross_x = x_text + w1 + int(20 * scale)
    wc, hc, lxc, tyc = tsize(d, "×", fc)
    d.text((cross_x - lxc, y_title - tyc), "×", font=fc, fill=BURNT)

    # Subtitle
    f2 = _font(SERIF_REG, sub_pt)
    w2, h2, lx2, ty2 = tsize(d, subtitle, f2)
    y_sub = y_title + h1 + int(14 * scale)
    d.text((x_text - lx2, y_sub - ty2), subtitle, font=f2, fill=CREAM)

    # Hairline
    y_rule = y_sub + h2 + int(20 * scale)
    draw_hairline(d, x_text, y_rule, min(int(360 * scale), safe_x1 - x_text - 20))

    # Tagline
    ft = _font(SANS_REG, tag_pt)
    wt, ht, lxt, tyt = tsize(d, tagline, ft)
    y_tag = y_rule + int(20 * scale)
    d.text((x_text - lxt, y_tag - tyt), tagline, font=ft, fill=CREAM)

    # URL
    fu = _font(MONO_REG, url_pt)
    wu, hu, lxu, tyu = tsize(d, url, fu)
    y_url = y_tag + ht + int(14 * scale)
    d.text((x_text - lxu, y_url - tyu), url, font=fu, fill=BURNT)

    # Reserve verse block width first so we don't collide with the tagline.
    verse_lines = [
        "Whāia te iti kahurangi",
        "ki te tuohu koe",
        "me he maunga teitei.",
    ]
    fv = _font(SERIF_REG, max(14, int(20 * scale)))
    verse_w = max(tsize(d, ln, fv)[0] for ln in verse_lines)
    verse_h_total = sum(tsize(d, ln, fv)[1] for ln in verse_lines) + 2 * int(6 * scale)
    verse_right_pad = int(40 * scale)
    verse_x_start = W - verse_right_pad - verse_w

    # Widest text line in the wordmark block (subtitle, tagline, url)
    tagline_right = x_text + max(w2, tsize(d, tagline, _font(SANS_REG, tag_pt))[0])
    verse_fits = show_verse and (verse_x_start > tagline_right + int(60 * scale))

    # Right accent bars (may be outside safe area on mobile — that's OK)
    if show_bars and W - 120 > safe_x1:
        bar_x_right = verse_x_start - int(30 * scale) if verse_fits else W - int(40 * scale)
        bar_w = min(int(150 * scale), bar_x_right - max(safe_x1, tagline_right + int(40 * scale)))
        if bar_w > 40:
            draw_horizon_bars(d, x=bar_x_right - bar_w, y=mark_cy - int(40 * scale),
                              w=bar_w, gap=int(32 * scale), thickness=int(8 * scale))

    if verse_fits:
        vy = mark_cy - verse_h_total // 2 + int(20 * scale)
        for line in verse_lines:
            wv, hv, lxv, tyv = tsize(d, line, fv)
            d.text((W - verse_right_pad - wv - lxv, vy - tyv),
                   line, font=fv, fill=MUTED)
            vy += hv + int(6 * scale)

    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "PNG", optimize=True)
    return path


# ---------- Instagram / square share tile ----------

def make_square_share_tile(size=1080):
    """1080×1080 for IG feed, Threads, LinkedIn share, WhatsApp status."""
    img, d = _banner_base(size, size)

    cx = size / 2
    # Mark top-third
    mark_r = int(size * 0.22)
    mark_cy = int(size * 0.34)
    draw_circle_mark(d, cx, mark_cy, mark_r)

    # Title
    f1 = _font(SERIF_BOLD, int(size * 0.078))
    line1 = "AI WARRIOR"
    w1, h1, lx1, ty1 = tsize(d, line1, f1)
    y1 = mark_cy + mark_r + int(size * 0.08)
    d.text((cx - w1 / 2 - lx1, y1 - ty1), line1, font=f1, fill=GOLD)

    f2 = _font(SERIF_REG, int(size * 0.044))
    line2 = "Te Pā Literacy"
    w2, h2, lx2, ty2 = tsize(d, line2, f2)
    y2 = y1 + h1 + int(size * 0.02)
    d.text((cx - w2 / 2 - lx2, y2 - ty2), line2, font=f2, fill=CREAM)

    # Hairline centred
    hr_w = int(size * 0.28)
    y_rule = y2 + h2 + int(size * 0.035)
    d.rectangle([cx - hr_w / 2, y_rule, cx + hr_w / 2, y_rule + 2], fill=GOLD)

    # Tagline
    ft = _font(SANS_REG, int(size * 0.026))
    tag = "Kaupapa Māori digital literacy"
    wt, ht, lxt, tyt = tsize(d, tag, ft)
    y_tag = y_rule + int(size * 0.035)
    d.text((cx - wt / 2 - lxt, y_tag - tyt), tag, font=ft, fill=CREAM)

    ft2 = _font(SANS_REG, int(size * 0.022))
    tag2 = "openly licensed · whānau-funded"
    wt2, ht2, lxt2, tyt2 = tsize(d, tag2, ft2)
    y_tag2 = y_tag + ht + int(size * 0.012)
    d.text((cx - wt2 / 2 - lxt2, y_tag2 - tyt2), tag2, font=ft2, fill=MUTED)

    # URL near the bottom
    fu = _font(MONO_REG, int(size * 0.022))
    url = "thekiwidialectic.substack.com"
    wu, hu, lxu, tyu = tsize(d, url, fu)
    y_url = size - int(size * 0.10)
    d.text((cx - wu / 2 - lxu, y_url - tyu), url, font=fu, fill=BURNT)

    # Corner accent bars bottom-left
    draw_horizon_bars(d, x=int(size * 0.06), y=size - int(size * 0.14),
                      w=int(size * 0.14), gap=int(size * 0.02),
                      thickness=int(size * 0.008))

    path = OUT / "instagram" / "instagram-share-1080.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "PNG", optimize=True)
    return path


# ---------- YouTube channel banner ----------

def make_youtube_banner():
    """
    YouTube 2560×1440 with mobile-safe area 1546×423 in the centre.
    Everything critical goes in the safe area. text_scale=0.45 compresses
    the type so the full wordmark fits inside 1546 wide.
    """
    W, H = 2560, 1440
    path = OUT / "youtube" / "youtube-banner-2560x1440.png"
    make_social_banner(
        W, H, path,
        mark_radius=110,
        safe_center_fraction=1546 / 2560,   # ≈ 0.604
        show_verse=False,   # too far outside safe area to be reliable
        show_bars=False,
        text_scale=0.45,
    )
    return path


# ---------- GitHub social preview ----------

def make_github_social():
    """GitHub social preview card: 1280×640 (2:1)."""
    W, H = 1280, 640
    img, d = _banner_base(W, H)

    # Left: square mark
    mark_size = 340
    draw_square_mark(d, cx=270, cy=H / 2, size=mark_size, stroke_w_scale=1.1)

    # Right: wordmark stack
    x_text = 500
    y_top = 180
    f1 = _font(SERIF_BOLD, 68)
    l1 = "AI WARRIOR"
    w1, h1, lx1, ty1 = tsize(d, l1, f1)
    d.text((x_text - lx1, y_top - ty1), l1, font=f1, fill=GOLD)

    fc = _font(SERIF_REG, 68)
    d.text((x_text + w1 + 20, y_top - ty1), "×", font=fc, fill=BURNT)

    f2 = _font(SERIF_REG, 40)
    l2 = "TE PĀ LITERACY"
    w2, h2, lx2, ty2 = tsize(d, l2, f2)
    y2 = y_top + h1 + 20
    d.text((x_text - lx2, y2 - ty2), l2, font=f2, fill=CREAM)

    draw_hairline(d, x_text, y2 + h2 + 26, 380)

    ft = _font(SANS_REG, 22)
    tag = "Kaupapa Māori digital literacy — openly licensed, whānau-funded"
    wt, ht, lxt, tyt = tsize(d, tag, ft)
    d.text((x_text - lxt, y2 + h2 + 60 - tyt), tag, font=ft, fill=CREAM)

    fu = _font(MONO_REG, 20)
    url = "github.com/robertmccallnz/ai-warrior-te-pa"
    wu, hu, lxu, tyu = tsize(d, url, fu)
    d.text((x_text - lxu, y2 + h2 + 100 - tyu), url, font=fu, fill=BURNT)

    # Bottom-right accent
    draw_horizon_bars(d, x=W - 200, y=H - 130, w=150, gap=22, thickness=6)

    path = OUT / "github" / "github-social-1280x640.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, "PNG", optimize=True)
    return path


# ============================================================
#                        MAIN
# ============================================================

def build_all():
    produced = []

    # --- Substack ---
    produced.append(make_substack_banner())
    produced.append(make_substack_logo())

    # --- X / Twitter ---
    produced.append(make_circle_avatar(400, OUT / "x" / "x-avatar-400.png"))
    produced.append(make_social_banner(
        1500, 500, OUT / "x" / "x-header-1500x500.png",
        safe_center_fraction=0.85,
    ))

    # --- Bluesky ---
    produced.append(make_circle_avatar(400, OUT / "bluesky" / "bluesky-avatar-400.png"))
    produced.append(make_social_banner(
        3000, 1000, OUT / "bluesky" / "bluesky-banner-3000x1000.png",
        safe_center_fraction=0.55,
        text_scale=0.85,
    ))

    # --- Facebook ---
    produced.append(make_circle_avatar(400, OUT / "facebook" / "facebook-avatar-400.png"))
    # FB cover is 820×312 desktop but shows 640×360 on mobile — safe zone 640×312 centre
    produced.append(make_social_banner(
        820, 312, OUT / "facebook" / "facebook-cover-820x312.png",
        safe_center_fraction=640 / 820,
        show_verse=False,
        show_bars=False,
    ))

    # --- Instagram ---
    produced.append(make_circle_avatar(400, OUT / "instagram" / "instagram-avatar-400.png"))
    produced.append(make_square_share_tile(1080))

    # --- LinkedIn ---
    produced.append(make_circle_avatar(400, OUT / "linkedin" / "linkedin-avatar-400.png"))
    # LinkedIn banner 1584×396. Left ~350px hidden behind profile pic circle on desktop.
    produced.append(make_social_banner(
        1584, 396, OUT / "linkedin" / "linkedin-banner-1584x396.png",
        safe_center_fraction=0.70,
    ))

    # --- GitHub ---
    produced.append(make_square_avatar(500, OUT / "github" / "github-avatar-500.png"))
    produced.append(make_github_social())

    # --- YouTube ---
    produced.append(make_circle_avatar(800, OUT / "youtube" / "youtube-avatar-800.png"))
    produced.append(make_youtube_banner())

    return produced


if __name__ == "__main__":
    for p in build_all():
        print(p)
