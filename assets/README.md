# Brand assets · AI Warrior × Te Pā Literacy

All profile images and channel banners for the ecosystem. One palette, one mark,
one voice across every touchpoint.

## Palette

| Token           | Hex       | Use                                          |
| --------------- | --------- | -------------------------------------------- |
| Ōpōtiki black   | `#0f0b09` | Background for every asset                   |
| kōura (gold)    | `#d9a441` | Frame, wordmark, horizon bar, hairlines      |
| kōkōwai (burnt) | `#c86a2a` | Accent — `×`, URL, subtitle letter-spacing   |
| toto (red)      | `#a4181a` | Mountain peak, sun (the icon itself)         |
| paper (cream)   | `#efe6d3` | Body copy on dark, subtitle line             |

## Regenerating every asset

From the repo root:

```bash
python3 build/make_kofi_assets.py       # Ko-fi (avatar + banner)
python3 build/make_social_assets.py     # Substack + all social channels
```

Change the palette constants at the top of either script and everything stays
in sync.

---

## Directory map

```
assets/
├── kofi/                              # Ko-fi profile
│   ├── kofi-avatar-512.png            # 512×512  circular
│   └── kofi-banner-1500x500.png       # 1500×500 header
├── substack/
│   ├── substack-logo-256.png          # 256×256  publication logo (circular mark)
│   └── substack-banner-1456x180.png   # 1456×180 publication header
├── x/                                 # X / Twitter
│   ├── x-avatar-400.png               # 400×400  circular
│   └── x-header-1500x500.png          # 1500×500 header
├── bluesky/
│   ├── bluesky-avatar-400.png         # 400×400
│   └── bluesky-banner-3000x1000.png   # 3000×1000 header (3:1)
├── facebook/
│   ├── facebook-avatar-400.png        # 400×400
│   └── facebook-cover-820x312.png     # 820×312  Page cover
├── instagram/
│   ├── instagram-avatar-400.png       # 400×400
│   └── instagram-share-1080.png       # 1080×1080 square share tile
├── linkedin/
│   ├── linkedin-avatar-400.png        # 400×400
│   └── linkedin-banner-1584x396.png   # 1584×396 profile banner
├── github/
│   ├── github-avatar-500.png          # 500×500 square (org / repo avatar)
│   └── github-social-1280x640.png     # 1280×640 repo social preview
└── youtube/
    ├── youtube-avatar-800.png         # 800×800
    └── youtube-banner-2560x1440.png   # 2560×1440 channel banner
```

---

## Uploading — per-platform notes

### Substack

- **Publication logo** → Settings → Basics → *Publication logo*. Upload
  `substack-logo-256.png`. Shown as a small circle beside the publication name.
- **Header image** → Settings → Basics → *Header image*. Upload
  `substack-banner-1456x180.png`. Shown above the title on the homepage on
  desktop; hidden on mobile (Substack falls back to the logo).
- **Cover / OG image for individual posts** — you can reuse
  `../instagram/instagram-share-1080.png` as a fallback social card, or
  generate a fresh 1200×630 per post.

### X / Twitter

- **Profile photo** → Edit profile → tap avatar. Upload `x-avatar-400.png`.
  Rendered as a circle at ~48–120 px.
- **Header photo** → Edit profile → tap header. Upload `x-header-1500x500.png`.
  Bottom ~90 px is covered by your handle / display name on mobile; the design
  keeps that band empty.
- **Safe area on mobile:** roughly the central 85% width. All copy is inside.

### Bluesky

- **Avatar** → Settings → Profile → Edit → upload `bluesky-avatar-400.png`.
- **Banner** → Same screen. Upload `bluesky-banner-3000x1000.png` (Bluesky
  recommends 3:1). Bluesky crops heavily on mobile — the critical composition
  sits in the middle 55% of the width, which stays visible on all viewports.

### Facebook Page

- **Profile picture** → Page → three-dot menu → *Edit profile picture*.
  Upload `facebook-avatar-400.png`.
- **Cover photo** → *Edit cover photo* → *Upload photo*. Upload
  `facebook-cover-820x312.png`.
  - Desktop shows 820×312. Mobile crops to roughly 640×360 in the centre.
  - The composition is inside that 640 mobile-safe centre.
  - Facebook will overlay a small portion of the cover with the profile-photo
    circle on the left — the mark sits inside the safe band on the right of
    that.

### Instagram

- **Profile photo** → Edit Profile → *Change profile photo*. Upload
  `instagram-avatar-400.png`. Rendered as a circle at ~110 px.
- **Feed post / share tile** — post `instagram-share-1080.png` as your first
  post or a pinned announcement so anyone landing on the profile immediately
  sees the kaupapa. 1080×1080 is the native feed square.

### LinkedIn

- **Profile photo** → tap avatar → *Add photo*. Upload
  `linkedin-avatar-400.png`.
- **Background photo** → Cover camera icon → *Change photo*. Upload
  `linkedin-banner-1584x396.png`.
- **Note:** LinkedIn overlays the profile photo circle on the bottom-left of
  the banner. The composition is shifted right of centre so the mark and
  wordmark stay visible behind and beside that circle.

### GitHub

- **Repo social preview** → Repo → Settings → *Social preview* → *Edit*.
  Upload `github-social-1280x640.png`. This is the card that renders when
  someone shares the repo URL on Twitter/Slack/Discord.
- **Org or profile avatar** → Profile settings → *Change picture*. Upload
  `github-avatar-500.png`. GitHub keeps the square (it doesn't circle-crop
  the avatar the way social platforms do), so the square-frame variant of the
  mark is the right choice here.

### YouTube

- **Channel picture** → YouTube Studio → *Customization → Branding →
  Picture*. Upload `youtube-avatar-800.png`. Rendered as a circle.
- **Banner image** → *Customization → Branding → Banner image*. Upload
  `youtube-banner-2560x1440.png`. YouTube crops this differently on TV, desktop,
  and mobile:
  - TV: 2560×1440 full
  - Desktop: ~2560×423 slice from the vertical middle
  - Mobile: 1546×423 in the very centre
  - Everything critical is inside that 1546×423 mobile-safe box.

---

## After upload — verification checklist

1. Log out (or open incognito) and view each profile as a visitor.
2. Check both **mobile** and **desktop** — the majority of traffic is mobile.
3. Confirm the avatar reads as one recognisable mark at ~40 px (that's how big
   it appears in feeds and reply threads).
4. Confirm no critical text is cropped or blurred after the platform's
   compression pass.
5. If any platform re-compressed the PNG into visible artefacts, try uploading
   as WebP — modern platforms accept it and preserve more detail.

## Licence

All assets in this directory are released under **CC BY-SA 4.0**, same as the
rest of the repository. Fork, remix, use for any kaupapa aligned with the
project's values.
