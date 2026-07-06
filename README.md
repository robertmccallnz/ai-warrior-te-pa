# AI Warrior × Te Pā Literacy

**Kaupapa Māori digital literacy for iwi, hapū and whānau.**
Educate. Arm. Protect. Share. Grow.

This is an openly-licensed, whānau-funded, forkable education project. Every file — course outlines, media-kit templates, rhizome data, campaign scripts — is here for any iwi, marae, kura, roopu or organiser to remix and run in their rohe.

## The pages

| Page | Purpose |
|---|---|
| [`index.html`](./index.html) | Home — the kaupapa in one page |
| [`curriculum.html`](./curriculum.html) | Five free Tiriti-grounded courses |
| [`campaigns.html`](./campaigns.html) | Social, street, media and online kits |
| [`rhizome.html`](./rhizome.html) | Interactive rhizome mapper of Te Pāti Māori and iwi |
| [`tiriti.html`](./tiriti.html) | Living analysis of Te Tiriti in the AI age |
| [`crowdfund.html`](./crowdfund.html) | Three ways to tautoko — Givealittle, Ko-fi, Substack |

## The rhizome

Rather than a top-down org chart, the map in `rhizome.html` is a **rhizome** — no root, no head office, every node connects laterally. Data lives in [`data/rhizome.json`](./data/rhizome.json). Edit that file and the map updates. The static, print-ready version lives at [`assets/rhizome-print.svg`](./assets/rhizome-print.svg).

## The five pou

1. **Whakaako — Educate** — free courses delivered through [The Kiwi Dialectic](https://www.kiwidialectic.com/)
2. **Whakangungu — Arm** — social media kits, memes, response scripts
3. **Tiaki — Protect** — data-sovereignty checklists, deepfake detection guides
4. **Tuari — Share** — organic distribution across the rhizome
5. **Whanake — Grow** — crowdfunded, forkable, every marae can run its own Pā

## Te Tiriti spine

Every module is read through the three articles of *Te Tiriti o Waitangi*:

- **Article 1 — Kāwanatanga**: the Crown's limited, ceded authority
- **Article 2 — Tino Rangatiratanga**: unqualified Māori sovereignty over all taonga — including data
- **Article 3 — Ōritetanga**: equity of citizenship and outcomes

Plus the oral fourth — **wairuatanga** — the promise of freedom of belief and tikanga.

## Running locally

It's a static site. Any static server will do:

```bash
cd ai-warrior-te-pa
python3 -m http.server 8000
# then open http://localhost:8000
```

## Deploying

This repo is set up to deploy on GitHub Pages. In repo settings → Pages → Source: `main` branch, `/ (root)`. Live URL will be `https://<username>.github.io/<repo>/`.

## Licence

**Content, code and design: CC BY-SA 4.0.** Fork it, remix it, run it in your rohe. Attribution back to "AI Warrior × Te Pā Literacy" is enough.

## Contributing

Pull requests welcome — new courses, new iwi nodes on the rhizome, better te reo translations, campaign templates from your rohe. Tag issues with `[rohe: <rohe name>]` if the change is region-specific.

## Support the kaupapa

- **[Givealittle](https://givealittle.co.nz/)** — one-off
- **[Ko-fi](https://ko-fi.com/thekiwidialectic)** — monthly
- **[The Kiwi Dialectic Substack](https://www.kiwidialectic.com/)** — paid subscription

---

*Nā te whānau, mā te whānau.*
Made in Ōtepoti / Dunedin. Whakawhetai to every iwi, hapū and marae carrying this kaupapa.
