#!/usr/bin/env python3
"""Wrap existing English HTML content with data-i18n attributes.

Runs once. Uses precise string replacements per page — safer than regex tag rewriting.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ----- Shared replacements (nav + footer) -----
SHARED = [
    # Nav links
    ('<a href="index.html">Home</a>',
     '<a href="index.html" data-i18n="nav.home">Home</a>'),
    ('<a href="curriculum.html">Curriculum</a>',
     '<a href="curriculum.html" data-i18n="nav.curriculum">Curriculum</a>'),
    ('<a href="campaigns.html">Campaigns</a>',
     '<a href="campaigns.html" data-i18n="nav.campaigns">Campaigns</a>'),
    ('<a href="rhizome.html">Rhizome</a>',
     '<a href="rhizome.html" data-i18n="nav.rhizome">Rhizome</a>'),
    ('<a href="tiriti.html">Te Tiriti</a>',
     '<a href="tiriti.html" data-i18n="nav.tiriti">Te Tiriti</a>'),
    ('<a href="crowdfund.html" class="nav-cta">Support Kaupapa</a>',
     '<a href="crowdfund.html" class="nav-cta" data-i18n="nav.support">Support Kaupapa</a>'),
    ('<button class="nav-toggle" aria-label="Menu">≡</button>',
     '<button class="nav-toggle" aria-label="Menu" data-i18n-attr="aria-label:nav.menu">≡</button>'),

    # Footer
    ('<h4>AI Warrior</h4>\n        <p style="font-size:var(--text-sm);">Te Pā Literacy — kaupapa Māori digital literacy for iwi, hapū and whānau. Openly licensed. Whānau-funded.</p>',
     '<h4 data-i18n="footer.brand.title">AI Warrior</h4>\n        <p style="font-size:var(--text-sm);" data-i18n="footer.brand.body">Te Pā Literacy — kaupapa Māori digital literacy for iwi, hapū and whānau. Openly licensed. Whānau-funded.</p>'),
    ('<h4>Kaupapa</h4>\n        <ul>\n          <li><a href="curriculum.html">Curriculum</a></li>\n          <li><a href="campaigns.html">Campaigns</a></li>\n          <li><a href="rhizome.html">Rhizome</a></li>\n          <li><a href="tiriti.html">Te Tiriti</a></li>',
     '<h4 data-i18n="footer.kaupapa">Kaupapa</h4>\n        <ul>\n          <li><a href="curriculum.html" data-i18n="nav.curriculum">Curriculum</a></li>\n          <li><a href="campaigns.html" data-i18n="nav.campaigns">Campaigns</a></li>\n          <li><a href="rhizome.html" data-i18n="nav.rhizome">Rhizome</a></li>\n          <li><a href="tiriti.html" data-i18n="nav.tiriti">Te Tiriti</a></li>'),
    ('<h4>Support</h4>\n        <ul>\n          <li><a href="crowdfund.html">Crowdfund</a></li>\n          <li><a href="https://thekiwidialectic.substack.com/">The Kiwi Dialectic</a></li>\n          <li><a href="https://www.maoriparty.org.nz/">Te Pāti Māori</a></li>',
     '<h4 data-i18n="footer.support">Support</h4>\n        <ul>\n          <li><a href="crowdfund.html" data-i18n="footer.support.crowdfund">Crowdfund</a></li>\n          <li><a href="https://thekiwidialectic.substack.com/" data-i18n="footer.support.substack">The Kiwi Dialectic</a></li>\n          <li><a href="https://www.maoriparty.org.nz/" data-i18n="footer.support.tpm">Te Pāti Māori</a></li>'),
    ('<h4>Open</h4>\n        <ul>\n          <li><a href="https://github.com/robertmccallnz/ai-warrior-te-pa">GitHub repo</a></li>\n          <li><a href="rhizome.html">Rhizome data (JSON)</a></li>\n          <li><a href="#">CC BY-SA 4.0</a></li>',
     '<h4 data-i18n="footer.open">Open</h4>\n        <ul>\n          <li><a href="https://github.com/robertmccallnz/ai-warrior-te-pa" data-i18n="footer.open.repo">GitHub repo</a></li>\n          <li><a href="rhizome.html" data-i18n="footer.open.data">Rhizome data (JSON)</a></li>\n          <li><a href="#" data-i18n="footer.open.licence">CC BY-SA 4.0</a></li>'),
    ('<div class="footer-bottom">\n      Nā te whānau, mā te whānau. · Made in Ōtepoti / Dunedin · Whakawhetai to every iwi, hapū and marae carrying this kaupapa.\n    </div>',
     '<div class="footer-bottom" data-i18n="footer.bottom">\n      Nā te whānau, mā te whānau. · Made in Ōtepoti / Dunedin · Whakawhetai to every iwi, hapū and marae carrying this kaupapa.\n    </div>'),

    # Include i18n.js just before nav.js (nav.js is on every page)
    ('<script src="js/nav.js"></script>',
     '<script src="js/i18n.js"></script>\n<script src="js/nav.js"></script>'),
]

# ----- Per-page replacements -----
PAGES = {
    'index.html': [
        ('<title>AI Warrior × Te Pā Literacy — for iwi, whānau & mokopuna</title>',
         '<title data-i18n="home.title">AI Warrior × Te Pā Literacy — for iwi, whānau & mokopuna</title>'),
        ('<p class="hero-eyebrow">Kia mataara · Stay awake · A kaupapa Māori digital literacy pā</p>',
         '<p class="hero-eyebrow" data-i18n="home.hero.eyebrow">Kia mataara · Stay awake · A kaupapa Māori digital literacy pā</p>'),
        ('<h1>Arm the <span class="accent">pā</span>. Protect the <span class="accent">mokopuna</span>.</h1>',
         '<h1 data-i18n="home.hero.title.full">Arm the <span class="accent">pā</span>. Protect the <span class="accent">mokopuna</span>.</h1>'),
        ('<p class="hero-sub"><strong>AI Warrior × Te Pā Literacy</strong> is an open, whānau-first education kaupapa. We teach iwi, hapū and whānau how to read, resist and redirect the algorithms, deepfakes and data-extraction machines now shaping Aotearoa — grounded in <em>Te Tiriti o Waitangi</em> and <em>tino rangatiratanga</em>.</p>',
         '<p class="hero-sub" data-i18n="home.hero.sub"><strong>AI Warrior × Te Pā Literacy</strong> is an open, whānau-first education kaupapa. We teach iwi, hapū and whānau how to read, resist and redirect the algorithms, deepfakes and data-extraction machines now shaping Aotearoa — grounded in <em>Te Tiriti o Waitangi</em> and <em>tino rangatiratanga</em>.</p>'),
        ('<a href="curriculum.html" class="btn btn-primary">Start the Curriculum →</a>',
         '<a href="curriculum.html" class="btn btn-primary" data-i18n="home.hero.cta.curriculum">Start the Curriculum →</a>'),
        ('<a href="crowdfund.html" class="btn btn-ghost">Crowdfund the Pā</a>',
         '<a href="crowdfund.html" class="btn btn-ghost" data-i18n="home.hero.cta.crowdfund">Crowdfund the Pā</a>'),
        ('<a href="rhizome.html" class="btn btn-ghost">Open the Rhizome</a>',
         '<a href="rhizome.html" class="btn btn-ghost" data-i18n="home.hero.cta.rhizome">Open the Rhizome</a>'),
        ('<p class="eyebrow">Why now</p>\n    <h2>The digital colonial frontier is already inside the pā.</h2>',
         '<p class="eyebrow" data-i18n="home.why.eyebrow">Why now</p>\n    <h2 data-i18n="home.why.title">The digital colonial frontier is already inside the pā.</h2>'),
        ('<h3>Deepfake pōhēhē</h3>\n        <p>Synthetic video and voice of tangata whenua, kaumātua and MPs is already circulating on X, TikTok and Facebook — designed to divide whānau and discredit Māori political voice.</p>',
         '<h3 data-i18n="home.why.deepfake.title">Deepfake pōhēhē</h3>\n        <p data-i18n="home.why.deepfake.body">Synthetic video and voice of tangata whenua, kaumātua and MPs is already circulating on X, TikTok and Facebook — designed to divide whānau and discredit Māori political voice.</p>'),
        ('<h3>Data extraction</h3>\n        <p>Iwi mātauranga, whakapapa, waiata, and reo are being harvested by foreign AI models with zero consent or benefit-sharing. This is a <em>Tiriti breach</em> in a new medium.</p>',
         '<h3 data-i18n="home.why.data.title">Data extraction</h3>\n        <p data-i18n="home.why.data.body">Iwi mātauranga, whakapapa, waiata, and reo are being harvested by foreign AI models with zero consent or benefit-sharing. This is a <em>Tiriti breach</em> in a new medium.</p>'),
        ('<h3>Algorithmic silencing</h3>\n        <p>Māori voices are demonetised, throttled and shadow-banned. Learning the machine is the first act of <em>tino rangatiratanga</em> in the digital age.</p>',
         '<h3 data-i18n="home.why.silencing.title">Algorithmic silencing</h3>\n        <p data-i18n="home.why.silencing.body">Māori voices are demonetised, throttled and shadow-banned. Learning the machine is the first act of <em>tino rangatiratanga</em> in the digital age.</p>'),
        ('<p class="eyebrow" style="color:var(--kōura)">The five pou</p>\n      <h2 style="color:var(--kōura)">Educate · Arm · Protect · Share · Grow</h2>\n      <p>Te Pā Literacy is built on five pou (posts) that hold up the whare of digital sovereignty. Each pou has a course, a media kit, a street campaign, and a place on the rhizome.</p>',
         '<p class="eyebrow" style="color:var(--kōura)" data-i18n="home.pou.eyebrow">The five pou</p>\n      <h2 style="color:var(--kōura)" data-i18n="home.pou.title">Educate · Arm · Protect · Share · Grow</h2>\n      <p data-i18n="home.pou.intro">Te Pā Literacy is built on five pou (posts) that hold up the whare of digital sovereignty. Each pou has a course, a media kit, a street campaign, and a place on the rhizome.</p>'),
        ('<h3 style="color:var(--kōura)">1. Whakaako — Educate</h3>\n          <p>Free, short-form courses in te reo and English. Delivered through <a href="https://thekiwidialectic.substack.com/" style="color:var(--kōura)">The Kiwi Dialectic</a>.</p>',
         '<h3 style="color:var(--kōura)" data-i18n="home.pou.1.title">1. Whakaako — Educate</h3>\n          <p data-i18n="home.pou.1.body">Free, short-form courses in te reo and English. Delivered through <a href="https://thekiwidialectic.substack.com/" style="color:var(--kōura)">The Kiwi Dialectic</a>.</p>'),
        ('<h3 style="color:var(--kōura)">2. Whakangungu — Arm</h3>\n          <p>Downloadable social media kits, meme templates, response scripts and fact-check briefs.</p>',
         '<h3 style="color:var(--kōura)" data-i18n="home.pou.2.title">2. Whakangungu — Arm</h3>\n          <p data-i18n="home.pou.2.body">Downloadable social media kits, meme templates, response scripts and fact-check briefs.</p>'),
        ('<h3 style="color:var(--kōura)">3. Tiaki — Protect</h3>\n          <p>Data-sovereignty checklists for iwi orgs, marae and kura. Deepfake-detection guides.</p>',
         '<h3 style="color:var(--kōura)" data-i18n="home.pou.3.title">3. Tiaki — Protect</h3>\n          <p data-i18n="home.pou.3.body">Data-sovereignty checklists for iwi orgs, marae and kura. Deepfake-detection guides.</p>'),
        ('<h3 style="color:var(--kōura)">4. Tuari — Share</h3>\n          <p>Organic distribution through the rhizome — no algorithm gatekeeping. Whānau to whānau.</p>',
         '<h3 style="color:var(--kōura)" data-i18n="home.pou.4.title">4. Tuari — Share</h3>\n          <p data-i18n="home.pou.4.body">Organic distribution through the rhizome — no algorithm gatekeeping. Whānau to whānau.</p>'),
        ('<h3 style="color:var(--kōura)">5. Whanake — Grow</h3>\n          <p>Crowdfunded, openly-licensed, forkable. Every marae can run its own Pā.</p>',
         '<h3 style="color:var(--kōura)" data-i18n="home.pou.5.title">5. Whanake — Grow</h3>\n          <p data-i18n="home.pou.5.body">Crowdfunded, openly-licensed, forkable. Every marae can run its own Pā.</p>'),
        ('<p class="eyebrow">Grounded in Te Tiriti</p>\n      <h2>Every course, every campaign, every mapper node — read through Te Tiriti o Waitangi.</h2>\n      <p>We teach the three articles as living instruments, not museum pieces: <strong>kāwanatanga</strong> (the limited authority ceded to the Crown), <strong>tino rangatiratanga</strong> (unqualified Māori sovereignty over taonga — including data, reo and whakapapa), and <strong>ōritetanga</strong> (equity of citizenship). AI systems that ignore any of the three are Tiriti breaches.</p>\n      <a href="tiriti.html" class="btn btn-ghost">Read the Te Tiriti analysis →</a>',
         '<p class="eyebrow" data-i18n="home.tiriti.eyebrow">Grounded in Te Tiriti</p>\n      <h2 data-i18n="home.tiriti.title">Every course, every campaign, every mapper node — read through Te Tiriti o Waitangi.</h2>\n      <p data-i18n="home.tiriti.body">We teach the three articles as living instruments, not museum pieces: <strong>kāwanatanga</strong> (the limited authority ceded to the Crown), <strong>tino rangatiratanga</strong> (unqualified Māori sovereignty over taonga — including data, reo and whakapapa), and <strong>ōritetanga</strong> (equity of citizenship). AI systems that ignore any of the three are Tiriti breaches.</p>\n      <a href="tiriti.html" class="btn btn-ghost" data-i18n="home.tiriti.cta">Read the Te Tiriti analysis →</a>'),
        ('“Ko te reo te mauri o te mana Māori — and the reo now includes the code.”\n        <cite>— Te Pā Literacy kaupapa</cite>',
         '<span data-i18n="home.tiriti.quote">“Ko te reo te mauri o te mana Māori — and the reo now includes the code.”</span>\n        <cite data-i18n="home.tiriti.quote.cite">— Te Pā Literacy kaupapa</cite>'),
        ('<p class="eyebrow" style="padding:0;margin-bottom:12px">Fork the pā</p>\n    <h2>This is an open kaupapa. Take it, remix it, run it in your rohe.</h2>\n    <p style="margin: 0 auto var(--s-6); max-width:60ch;">The whole project — courses, media kits, rhizome data, campaign templates — is on GitHub under a Creative Commons licence. Crowdfund the next module, or fork it and build your own.</p>',
         '<p class="eyebrow" style="padding:0;margin-bottom:12px" data-i18n="home.fork.eyebrow">Fork the pā</p>\n    <h2 data-i18n="home.fork.title">This is an open kaupapa. Take it, remix it, run it in your rohe.</h2>\n    <p style="margin: 0 auto var(--s-6); max-width:60ch;" data-i18n="home.fork.body">The whole project — courses, media kits, rhizome data, campaign templates — is on GitHub under a Creative Commons licence. Crowdfund the next module, or fork it and build your own.</p>'),
        ('<a href="crowdfund.html" class="btn btn-primary">Crowdfund Now</a>\n      <a href="campaigns.html" class="btn btn-ghost">Download Media Kit</a>',
         '<a href="crowdfund.html" class="btn btn-primary" data-i18n="home.fork.cta.crowdfund">Crowdfund Now</a>\n      <a href="campaigns.html" class="btn btn-ghost" data-i18n="home.fork.cta.mediakit">Download Media Kit</a>'),
    ],

    'curriculum.html': [
        ('<title>Curriculum — AI Warrior × Te Pā Literacy</title>',
         '<title data-i18n="cur.title">Curriculum — AI Warrior × Te Pā Literacy</title>'),
        ('<p class="eyebrow">Curriculum · Ngā akoranga</p>\n    <h1 style="font-size:var(--text-3xl); max-width:22ch;">Five courses. Every one grounded in Te Tiriti.</h1>\n    <p style="max-width:70ch;">Each course is free, short (60–90 mins), delivered through <a href="https://thekiwidialectic.substack.com/">The Kiwi Dialectic</a>, and comes with a downloadable pack for marae, kura and iwi orgs. Do them in order or dip in wherever your rohe needs it.</p>',
         '<p class="eyebrow" data-i18n="cur.eyebrow">Curriculum · Ngā akoranga</p>\n    <h1 style="font-size:var(--text-3xl); max-width:22ch;" data-i18n="cur.h1">Five courses. Every one grounded in Te Tiriti.</h1>\n    <p style="max-width:70ch;" data-i18n="cur.intro.full">Each course is free, short (60–90 mins), delivered through <a href="https://thekiwidialectic.substack.com/">The Kiwi Dialectic</a>, and comes with a downloadable pack for marae, kura and iwi orgs. Do them in order or dip in wherever your rohe needs it.</p>'),
        ('<h3>AI Literacy Basics — He aha te AI?</h3>\n        <p>What is a large language model, actually? Where does the data come from? Whose worldview is baked into the outputs? A plain-language demystification for whānau of any age.</p>\n        <p class="course-meta">Article 1 · Kāwanatanga · 60 min · <a href="https://thekiwidialectic.substack.com/">Enrol on Substack →</a></p>',
         '<h3 data-i18n="cur.c1.title">AI Literacy Basics — He aha te AI?</h3>\n        <p data-i18n="cur.c1.body">What is a large language model, actually? Where does the data come from? Whose worldview is baked into the outputs? A plain-language demystification for whānau of any age.</p>\n        <p class="course-meta" data-i18n="cur.c1.meta">Article 1 · Kāwanatanga · 60 min · <a href="https://thekiwidialectic.substack.com/">Enrol on Substack →</a></p>'),
        ('<h3>Deepfakes & Disinformation — Te pōhēhē kikokiko-kore</h3>\n        <p>How to spot synthetic video and voice. Reverse-image search, provenance tools, and a decision tree for whānau group chats. Includes a downloadable checklist for kaumātua.</p>\n        <p class="course-meta">Article 3 · Ōritetanga · 75 min · <a href="https://thekiwidialectic.substack.com/">Enrol →</a></p>',
         '<h3 data-i18n="cur.c2.title">Deepfakes & Disinformation — Te pōhēhē kikokiko-kore</h3>\n        <p data-i18n="cur.c2.body">How to spot synthetic video and voice. Reverse-image search, provenance tools, and a decision tree for whānau group chats. Includes a downloadable checklist for kaumātua.</p>\n        <p class="course-meta" data-i18n="cur.c2.meta">Article 3 · Ōritetanga · 75 min · <a href="https://thekiwidialectic.substack.com/">Enrol →</a></p>'),
        ('<h3>Data Sovereignty — Ko wai te rangatira o ō tātou raraunga?</h3>\n        <p>Whakapapa, waiata, and reo as taonga under Article 2. The <a href="https://www.temanararaunga.maori.nz/">Te Mana Raraunga</a> principles applied in practice. A checklist for iwi organisations negotiating with tech vendors.</p>\n        <p class="course-meta">Article 2 · Tino Rangatiratanga · 90 min · <a href="https://thekiwidialectic.substack.com/">Enrol →</a></p>',
         '<h3 data-i18n="cur.c3.title">Data Sovereignty — Ko wai te rangatira o ō tātou raraunga?</h3>\n        <p data-i18n="cur.c3.body">Whakapapa, waiata, and reo as taonga under Article 2. The <a href="https://www.temanararaunga.maori.nz/">Te Mana Raraunga</a> principles applied in practice. A checklist for iwi organisations negotiating with tech vendors.</p>\n        <p class="course-meta" data-i18n="cur.c3.meta">Article 2 · Tino Rangatiratanga · 90 min · <a href="https://thekiwidialectic.substack.com/">Enrol →</a></p>'),
        ('<h3>Algorithmic Colonialism — Te tāmi a te pūmanawa</h3>\n        <p>How recommendation engines, moderation policies and monetisation choke Māori voice. Case studies from X, Meta and TikTok. What to do when you\'re shadow-banned.</p>\n        <p class="course-meta">Article 2 · Tino Rangatiratanga · 75 min · <a href="https://thekiwidialectic.substack.com/">Enrol →</a></p>',
         '<h3 data-i18n="cur.c4.title">Algorithmic Colonialism — Te tāmi a te pūmanawa</h3>\n        <p data-i18n="cur.c4.body">How recommendation engines, moderation policies and monetisation choke Māori voice. Case studies from X, Meta and TikTok. What to do when you\'re shadow-banned.</p>\n        <p class="course-meta" data-i18n="cur.c4.meta">Article 2 · Tino Rangatiratanga · 75 min · <a href="https://thekiwidialectic.substack.com/">Enrol →</a></p>'),
        ('<h3>Whānau Digital Pā — Te hanga i tō pā tuihono</h3>\n        <p>Practical, hands-on: set up your marae\'s own website, secure comms, mailing list and rhizome node. Zero cost, forkable templates, no reliance on colonial platforms.</p>\n        <p class="course-meta">Articles 1, 2, 3 · 90 min · <a href="https://thekiwidialectic.substack.com/">Enrol →</a></p>',
         '<h3 data-i18n="cur.c5.title">Whānau Digital Pā — Te hanga i tō pā tuihono</h3>\n        <p data-i18n="cur.c5.body">Practical, hands-on: set up your marae\'s own website, secure comms, mailing list and rhizome node. Zero cost, forkable templates, no reliance on colonial platforms.</p>\n        <p class="course-meta" data-i18n="cur.c5.meta">Articles 1, 2, 3 · 90 min · <a href="https://thekiwidialectic.substack.com/">Enrol →</a></p>'),
        ('<h2 style="color:var(--kōura)">Course feed — Ngā mea hou</h2>\n      <p>New modules drop monthly. Subscribe once and every course lands in your inbox with the full media kit.</p>\n      <a href="https://thekiwidialectic.substack.com/" class="btn btn-primary" style="border-color:var(--kōura); background:var(--kōura); color:var(--muku);">Subscribe on The Kiwi Dialectic →</a>',
         '<h2 style="color:var(--kōura)" data-i18n="cur.feed.title">Course feed — Ngā mea hou</h2>\n      <p data-i18n="cur.feed.body">New modules drop monthly. Subscribe once and every course lands in your inbox with the full media kit.</p>\n      <a href="https://thekiwidialectic.substack.com/" class="btn btn-primary" style="border-color:var(--kōura); background:var(--kōura); color:var(--muku);" data-i18n="cur.feed.cta">Subscribe on The Kiwi Dialectic →</a>'),
    ],

    'campaigns.html': [
        ('<title>Campaigns — AI Warrior × Te Pā Literacy</title>',
         '<title data-i18n="camp.title">Campaigns — AI Warrior × Te Pā Literacy</title>'),
        ('<p class="eyebrow">Campaigns · Ngā kokiritanga</p>\n    <h1 style="font-size:var(--text-3xl); max-width:24ch;">Media kits, street posters, and organic online campaigns.</h1>\n    <p style="max-width:70ch;">Everything on this page is free to download, remix and redistribute under CC BY-SA 4.0. If your marae, roopu or collective needs a bespoke variation, get in touch through <a href="https://thekiwidialectic.substack.com/">The Kiwi Dialectic</a>.</p>',
         '<p class="eyebrow" data-i18n="camp.eyebrow">Campaigns · Ngā kokiritanga</p>\n    <h1 style="font-size:var(--text-3xl); max-width:24ch;" data-i18n="camp.h1">Media kits, street posters, and organic online campaigns.</h1>\n    <p style="max-width:70ch;" data-i18n="camp.intro.full">Everything on this page is free to download, remix and redistribute under CC BY-SA 4.0. If your marae, roopu or collective needs a bespoke variation, get in touch through <a href="https://thekiwidialectic.substack.com/">The Kiwi Dialectic</a>.</p>'),
        ('<p class="mono" style="color:var(--toto)">01 · Social media toolkit</p>\n        <h3>Whakangungu — Arm your feed</h3>\n        <p>Instagram carousels, X/Twitter thread scripts, TikTok explainers and a meme pack. Sized and formatted for every platform. Includes suggested captions in te reo and English.</p>',
         '<p class="mono" style="color:var(--toto)" data-i18n="camp.c1.label">01 · Social media toolkit</p>\n        <h3 data-i18n="camp.c1.title">Whakangungu — Arm your feed</h3>\n        <p data-i18n="camp.c1.body">Instagram carousels, X/Twitter thread scripts, TikTok explainers and a meme pack. Sized and formatted for every platform. Includes suggested captions in te reo and English.</p>'),
        ('<li>10 carousel templates (Canva + Figma)</li>\n          <li>25 meme templates (PNG + editable SVG)</li>\n          <li>Thread scripts for the 5 most common AI-panic narratives</li>\n          <li>Hashtag & handle style guide</li>\n        </ul>\n        <a href="#" class="btn btn-ghost">Download social kit (zip)</a>',
         '<li data-i18n="camp.c1.li1">10 carousel templates (Canva + Figma)</li>\n          <li data-i18n="camp.c1.li2">25 meme templates (PNG + editable SVG)</li>\n          <li data-i18n="camp.c1.li3">Thread scripts for the 5 most common AI-panic narratives</li>\n          <li data-i18n="camp.c1.li4">Hashtag & handle style guide</li>\n        </ul>\n        <a href="#" class="btn btn-ghost" data-i18n="camp.c1.cta">Download social kit (zip)</a>'),
        ('<p class="mono" style="color:var(--toto)">02 · Street campaigns</p>\n        <h3>Ki te whenua — On the ground</h3>\n        <p>A3 and A2 posters, marae noticeboard flyers, sticker sheets and a wheat-paste manual. Printable on any inkjet. Print-shop-ready PDFs at 300dpi.</p>',
         '<p class="mono" style="color:var(--toto)" data-i18n="camp.c2.label">02 · Street campaigns</p>\n        <h3 data-i18n="camp.c2.title">Ki te whenua — On the ground</h3>\n        <p data-i18n="camp.c2.body">A3 and A2 posters, marae noticeboard flyers, sticker sheets and a wheat-paste manual. Printable on any inkjet. Print-shop-ready PDFs at 300dpi.</p>'),
        ('<li>6 poster designs (bilingual, black & red)</li>\n          <li>Sticker sheet — 24 per A4</li>\n          <li>Wheat-paste guide (safe, biodegradable recipe)</li>\n          <li>Marae pānui template — editable DOCX</li>\n        </ul>\n        <a href="#" class="btn btn-ghost">Download street kit (zip)</a>',
         '<li data-i18n="camp.c2.li1">6 poster designs (bilingual, black & red)</li>\n          <li data-i18n="camp.c2.li2">Sticker sheet — 24 per A4</li>\n          <li data-i18n="camp.c2.li3">Wheat-paste guide (safe, biodegradable recipe)</li>\n          <li data-i18n="camp.c2.li4">Marae pānui template — editable DOCX</li>\n        </ul>\n        <a href="#" class="btn btn-ghost" data-i18n="camp.c2.cta">Download street kit (zip)</a>'),
        ('<p class="mono" style="color:var(--toto)">03 · Press & media kit</p>\n        <h3>Ki te hunga pāpāho — For journalists</h3>\n        <p>Everything a reporter or podcaster needs to cover the kaupapa fairly: fact sheet, kaikōrero bios, hi-res logos, correct macron usage guide and pre-cleared imagery.</p>',
         '<p class="mono" style="color:var(--toto)" data-i18n="camp.c3.label">03 · Press & media kit</p>\n        <h3 data-i18n="camp.c3.title">Ki te hunga pāpāho — For journalists</h3>\n        <p data-i18n="camp.c3.body">Everything a reporter or podcaster needs to cover the kaupapa fairly: fact sheet, kaikōrero bios, hi-res logos, correct macron usage guide and pre-cleared imagery.</p>'),
        ('<li>2-page fact sheet (PDF)</li>\n          <li>Logo pack — SVG, PNG, mono/colour</li>\n          <li>Style & pronunciation guide</li>\n          <li>Kaikōrero contact card</li>\n        </ul>\n        <a href="#" class="btn btn-ghost">Download press kit (zip)</a>',
         '<li data-i18n="camp.c3.li1">2-page fact sheet (PDF)</li>\n          <li data-i18n="camp.c3.li2">Logo pack — SVG, PNG, mono/colour</li>\n          <li data-i18n="camp.c3.li3">Style & pronunciation guide</li>\n          <li data-i18n="camp.c3.li4">Kaikōrero contact card</li>\n        </ul>\n        <a href="#" class="btn btn-ghost" data-i18n="camp.c3.cta">Download press kit (zip)</a>'),
        ('<p class="mono" style="color:var(--toto)">04 · Online campaigns</p>\n        <h3>Tuihono — Organic online kokiri</h3>\n        <p>Pre-written email sequences, comment-section response scripts, Reddit/BlueSky/Mastodon posting kits, and a Signal group starter pack for whānau coordinators.</p>',
         '<p class="mono" style="color:var(--toto)" data-i18n="camp.c4.label">04 · Online campaigns</p>\n        <h3 data-i18n="camp.c4.title">Tuihono — Organic online kokiri</h3>\n        <p data-i18n="camp.c4.body">Pre-written email sequences, comment-section response scripts, Reddit/BlueSky/Mastodon posting kits, and a Signal group starter pack for whānau coordinators.</p>'),
        ('<li>5-email onboarding sequence</li>\n          <li>Reply-guy response bank (30+ scripts)</li>\n          <li>Signal group starter pack</li>\n          <li>Substack cross-post templates</li>\n        </ul>\n        <a href="#" class="btn btn-ghost">Download online kit (zip)</a>',
         '<li data-i18n="camp.c4.li1">5-email onboarding sequence</li>\n          <li data-i18n="camp.c4.li2">Reply-guy response bank (30+ scripts)</li>\n          <li data-i18n="camp.c4.li3">Signal group starter pack</li>\n          <li data-i18n="camp.c4.li4">Substack cross-post templates</li>\n        </ul>\n        <a href="#" class="btn btn-ghost" data-i18n="camp.c4.cta">Download online kit (zip)</a>'),
        ('<p class="eyebrow">The write-and-share cycle</p>\n      <h2>Every campaign follows the same six moves.</h2>',
         '<p class="eyebrow" data-i18n="camp.cycle.eyebrow">The write-and-share cycle</p>\n      <h2 data-i18n="camp.cycle.title">Every campaign follows the same six moves.</h2>'),
        ('<li><strong>Whakaaro</strong> — pick the kaupapa (one clear message).</li>',
         '<li data-i18n="camp.cycle.1"><strong>Whakaaro</strong> — pick the kaupapa (one clear message).</li>'),
        ('<li><strong>Tuhi</strong> — write it in the working-class vernacular your whānau actually speak.</li>',
         '<li data-i18n="camp.cycle.2"><strong>Tuhi</strong> — write it in the working-class vernacular your whānau actually speak.</li>'),
        ('<li><strong>Whakaahua</strong> — make the visual (meme, poster, thread card).</li>',
         '<li data-i18n="camp.cycle.3"><strong>Whakaahua</strong> — make the visual (meme, poster, thread card).</li>'),
        ('<li><strong>Tuku</strong> — post organically across the rhizome — never boost, never pay.</li>',
         '<li data-i18n="camp.cycle.4"><strong>Tuku</strong> — post organically across the rhizome — never boost, never pay.</li>'),
        ('<li><strong>Whakautu</strong> — reply, don\'t argue. Move people, don\'t own them.</li>',
         '<li data-i18n="camp.cycle.5"><strong>Whakautu</strong> — reply, don\'t argue. Move people, don\'t own them.</li>'),
        ('<li><strong>Whakawhanaunga</strong> — invite them into the pā (subscribe, join the Signal, come to the wānanga).</li>',
         '<li data-i18n="camp.cycle.6"><strong>Whakawhanaunga</strong> — invite them into the pā (subscribe, join the Signal, come to the wānanga).</li>'),
        ('<h3 style="color:var(--kōura)">One rule</h3>\n        <p style="font-size:var(--text-lg);">If a campaign can\'t be run by a kaumātua on a Chromebook in a marae kitchen, it\'s not our campaign.</p>',
         '<h3 style="color:var(--kōura)" data-i18n="camp.rule.title">One rule</h3>\n        <p style="font-size:var(--text-lg);" data-i18n="camp.rule.body">If a campaign can\'t be run by a kaumātua on a Chromebook in a marae kitchen, it\'s not our campaign.</p>'),
    ],

    'rhizome.html': [
        ('<title>Rhizome Mapper — AI Warrior × Te Pā Literacy</title>',
         '<title data-i18n="rz.title">Rhizome Mapper — AI Warrior × Te Pā Literacy</title>'),
        ('<p class="eyebrow">The Rhizome Mapper</p>\n    <h1 style="font-size:var(--text-3xl); max-width:22ch;">Not a tree. A rhizome.</h1>\n    <p style="max-width:70ch;">Following Deleuze &amp; Guattari — and, closer to home, the way a kūmara vine actually grows — this map has no top, no boss, no head office. Every node connects laterally. Click any node to jump to the source. Drag to explore. This is Te Pāti Māori, its kaupapa, its iwi relationships, our curriculum and campaigns, all in one field.</p>',
         '<p class="eyebrow" data-i18n="rz.eyebrow">The Rhizome Mapper</p>\n    <h1 style="font-size:var(--text-3xl); max-width:22ch;" data-i18n="rz.h1">Not a tree. A rhizome.</h1>\n    <p style="max-width:70ch;" data-i18n="rz.intro">Following Deleuze &amp; Guattari — and, closer to home, the way a kūmara vine actually grows — this map has no top, no boss, no head office. Every node connects laterally. Click any node to jump to the source. Drag to explore. This is Te Pāti Māori, its kaupapa, its iwi relationships, our curriculum and campaigns, all in one field.</p>'),
        ('<button class="btn btn-ghost active" data-filter="all" style="padding:6px 12px;">All</button>',
         '<button class="btn btn-ghost active" data-filter="all" style="padding:6px 12px;" data-i18n="rz.filter.all">All</button>'),
        ('<button class="btn btn-ghost" data-filter="leader" style="padding:6px 12px;">Leaders</button>',
         '<button class="btn btn-ghost" data-filter="leader" style="padding:6px 12px;" data-i18n="rz.filter.leader">Leaders</button>'),
        ('<button class="btn btn-ghost" data-filter="mp" style="padding:6px 12px;">MPs</button>',
         '<button class="btn btn-ghost" data-filter="mp" style="padding:6px 12px;" data-i18n="rz.filter.mp">MPs</button>'),
        ('<button class="btn btn-ghost" data-filter="iwi" style="padding:6px 12px;">Iwi</button>',
         '<button class="btn btn-ghost" data-filter="iwi" style="padding:6px 12px;" data-i18n="rz.filter.iwi">Iwi</button>'),
        ('<button class="btn btn-ghost" data-filter="kaupapa" style="padding:6px 12px;">Kaupapa</button>',
         '<button class="btn btn-ghost" data-filter="kaupapa" style="padding:6px 12px;" data-i18n="rz.filter.kaupapa">Kaupapa</button>'),
        ('<button class="btn btn-ghost" data-filter="policy" style="padding:6px 12px;">Policy</button>',
         '<button class="btn btn-ghost" data-filter="policy" style="padding:6px 12px;" data-i18n="rz.filter.policy">Policy</button>'),
        ('<button class="btn btn-ghost" data-filter="campaign" style="padding:6px 12px;">Campaigns</button>',
         '<button class="btn btn-ghost" data-filter="campaign" style="padding:6px 12px;" data-i18n="rz.filter.campaign">Campaigns</button>'),
        ('<button class="btn btn-ghost" data-filter="course" style="padding:6px 12px;">Courses</button>',
         '<button class="btn btn-ghost" data-filter="course" style="padding:6px 12px;" data-i18n="rz.filter.course">Courses</button>'),
        ('<button class="btn btn-ghost" data-filter="fund" style="padding:6px 12px;">Funding</button>',
         '<button class="btn btn-ghost" data-filter="fund" style="padding:6px 12px;" data-i18n="rz.filter.fund">Funding</button>'),
        ('<p class="mono mt-6" style="color:var(--kōkōwai)">Tip · Click any node to open its source. Drag to move. Scroll to zoom. On mobile, pinch.</p>',
         '<p class="mono mt-6" style="color:var(--kōkōwai)" data-i18n="rz.tip">Tip · Click any node to open its source. Drag to move. Scroll to zoom. On mobile, pinch.</p>'),
        ('<p class="eyebrow">Static rhizome — for print, posters &amp; PDF</p>\n    <h2>The printable version.</h2>\n    <p style="max-width:70ch;">Same relationships, hand-composed for A3 print. Drop this on a marae wall or fold it into a zine.</p>',
         '<p class="eyebrow" data-i18n="rz.print.eyebrow">Static rhizome — for print, posters &amp; PDF</p>\n    <h2 data-i18n="rz.print.title">The printable version.</h2>\n    <p style="max-width:70ch;" data-i18n="rz.print.body">Same relationships, hand-composed for A3 print. Drop this on a marae wall or fold it into a zine.</p>'),
        ('<p class="mono mt-6"><a href="assets/rhizome-print.svg">Download print-ready SVG</a> · <a href="data/rhizome.json">Raw JSON data</a></p>',
         '<p class="mono mt-6"><a href="assets/rhizome-print.svg" data-i18n="rz.print.link.svg">Download print-ready SVG</a> · <a href="data/rhizome.json" data-i18n="rz.print.link.data">Raw JSON data</a></p>'),
    ],

    'tiriti.html': [
        ('<title>Te Tiriti Analysis — AI Warrior × Te Pā Literacy</title>',
         '<title data-i18n="tir.title">Te Tiriti Analysis — AI Warrior × Te Pā Literacy</title>'),
        ('<p class="eyebrow">Te Tiriti o Waitangi — read through AI</p>\n    <h1 style="font-size:var(--text-3xl); max-width:24ch;">Three articles. One taonga. A living instrument against digital colonisation.</h1>\n    <p style="max-width:70ch;">This is the interpretive spine of the whole kaupapa. Every module, every campaign, every rhizome node is read through the three articles of <em>Te Tiriti o Waitangi</em> — the Māori text signed at Waitangi on 6 February 1840. We use the Māori text, not the English "Treaty," because it is the text the rangatira signed. Read the plain-language summary at <a href="https://nzhistory.govt.nz/politics/treaty/the-treaty-in-brief">NZ History</a> or the scholarly comparison at <a href="https://teara.govt.nz/en/document/4216/the-three-articles-of-the-treaty-of-waitangi">Te Ara</a>.</p>',
         '<p class="eyebrow" data-i18n="tir.eyebrow">Te Tiriti o Waitangi — read through AI</p>\n    <h1 style="font-size:var(--text-3xl); max-width:24ch;" data-i18n="tir.h1">Three articles. One taonga. A living instrument against digital colonisation.</h1>\n    <p style="max-width:70ch;" data-i18n="tir.intro.full">This is the interpretive spine of the whole kaupapa. Every module, every campaign, every rhizome node is read through the three articles of <em>Te Tiriti o Waitangi</em> — the Māori text signed at Waitangi on 6 February 1840. We use the Māori text, not the English "Treaty," because it is the text the rangatira signed. Read the plain-language summary at <a href="https://nzhistory.govt.nz/politics/treaty/the-treaty-in-brief">NZ History</a> or the scholarly comparison at <a href="https://teara.govt.nz/en/document/4216/the-three-articles-of-the-treaty-of-waitangi">Te Ara</a>.</p>'),
        ('<p class="mono" style="color:var(--toto)">Article 1 · Kāwanatanga</p>\n        <h3>Governance — limited, ceded, conditional.</h3>\n        <p>Rangatira ceded <em>kāwanatanga</em> (governance) to the Crown — not sovereignty. In the AI age, this means: the Crown may regulate telecommunications, digital ID and platform harms — but only within its ceded, limited authority. It cannot regulate <em>away</em> Māori data or Māori voice.</p>\n        <p><strong>What we teach:</strong> the difference between kāwanatanga and mana motuhake, and where each begins and ends in the digital domain.</p>',
         '<p class="mono" style="color:var(--toto)" data-i18n="tir.a1.label">Article 1 · Kāwanatanga</p>\n        <h3 data-i18n="tir.a1.title">Governance — limited, ceded, conditional.</h3>\n        <p data-i18n="tir.a1.body1">Rangatira ceded <em>kāwanatanga</em> (governance) to the Crown — not sovereignty. In the AI age, this means: the Crown may regulate telecommunications, digital ID and platform harms — but only within its ceded, limited authority. It cannot regulate <em>away</em> Māori data or Māori voice.</p>\n        <p data-i18n="tir.a1.body2"><strong>What we teach:</strong> the difference between kāwanatanga and mana motuhake, and where each begins and ends in the digital domain.</p>'),
        ('<p class="mono" style="color:var(--toto)">Article 2 · Tino Rangatiratanga</p>\n        <h3>Unqualified authority over all taonga.</h3>\n        <p>Rangatira retained <em>te tino rangatiratanga</em> — full, unqualified chieftainship — over their whenua, kāinga and <em>taonga katoa</em>. Language, whakapapa, waiata, mātauranga and now <em>data</em> are all taonga. Any AI model trained on Māori taonga without free, prior and informed consent is a Tiriti breach.</p>\n        <p><strong>What we teach:</strong> the <a href="https://www.temanararaunga.maori.nz/">Te Mana Raraunga</a> principles, iwi data governance, and how to write a data-sharing agreement that actually protects your rohe.</p>',
         '<p class="mono" style="color:var(--toto)" data-i18n="tir.a2.label">Article 2 · Tino Rangatiratanga</p>\n        <h3 data-i18n="tir.a2.title">Unqualified authority over all taonga.</h3>\n        <p data-i18n="tir.a2.body1">Rangatira retained <em>te tino rangatiratanga</em> — full, unqualified chieftainship — over their whenua, kāinga and <em>taonga katoa</em>. Language, whakapapa, waiata, mātauranga and now <em>data</em> are all taonga. Any AI model trained on Māori taonga without free, prior and informed consent is a Tiriti breach.</p>\n        <p data-i18n="tir.a2.body2"><strong>What we teach:</strong> the <a href="https://www.temanararaunga.maori.nz/">Te Mana Raraunga</a> principles, iwi data governance, and how to write a data-sharing agreement that actually protects your rohe.</p>'),
        ('<p class="mono" style="color:var(--toto)">Article 3 · Ōritetanga</p>\n        <h3>Equity — of citizenship and outcomes.</h3>\n        <p>Māori were guaranteed the same rights and duties as British subjects. Where algorithmic systems produce worse outcomes for Māori — in credit scoring, predictive policing, welfare fraud detection, or health triage — Article 3 is breached. Equity is a floor, not a ceiling.</p>\n        <p><strong>What we teach:</strong> how to audit an algorithm for disparate impact, and how to make an OIA request or Waitangi Tribunal claim about it.</p>',
         '<p class="mono" style="color:var(--toto)" data-i18n="tir.a3.label">Article 3 · Ōritetanga</p>\n        <h3 data-i18n="tir.a3.title">Equity — of citizenship and outcomes.</h3>\n        <p data-i18n="tir.a3.body1">Māori were guaranteed the same rights and duties as British subjects. Where algorithmic systems produce worse outcomes for Māori — in credit scoring, predictive policing, welfare fraud detection, or health triage — Article 3 is breached. Equity is a floor, not a ceiling.</p>\n        <p data-i18n="tir.a3.body2"><strong>What we teach:</strong> how to audit an algorithm for disparate impact, and how to make an OIA request or Waitangi Tribunal claim about it.</p>'),
        ('<p class="mono" style="color:var(--toto)">The oral fourth</p>\n        <h3>Wairuatanga — the spoken promise.</h3>\n        <p>At Waitangi, Governor Hobson\'s spoken assurance included freedom of belief and custom. We extend this to <em>digital wairuatanga</em>: the right to karakia, tikanga and tapu around data, code and communication — the right for AI to be shaped by Māori worldviews, not just accommodated to them.</p>',
         '<p class="mono" style="color:var(--toto)" data-i18n="tir.a4.label">The oral fourth</p>\n        <h3 data-i18n="tir.a4.title">Wairuatanga — the spoken promise.</h3>\n        <p data-i18n="tir.a4.body">At Waitangi, Governor Hobson\'s spoken assurance included freedom of belief and custom. We extend this to <em>digital wairuatanga</em>: the right to karakia, tikanga and tapu around data, code and communication — the right for AI to be shaped by Māori worldviews, not just accommodated to them.</p>'),
        ('<p class="eyebrow" style="color:var(--kōura)">Iwi, education & the pā</p>\n      <h2 style="color:var(--kōura)">Every iwi is already a digital sovereign — the pā just makes it visible.</h2>\n      <p>Iwi authorities already hold rangatiratanga over their rohe. Te Pā Literacy is a tool for exercising it in the digital domain: a shared curriculum, a shared campaign kit, and a shared rhizome — but each iwi runs its own node. Waikato-Tainui\'s pā looks different from Ngāi Tahu\'s, which looks different from Ngāpuhi\'s. That is the point.</p>\n      <p>Education is the connector. When <a href="https://www.maoriparty.org.nz/education_training">Te Pāti Māori\'s education kaupapa</a> talks about Māori-led education, we read it as including the digital classroom — the algorithms our tamariki learn from every day.</p>\n      <a href="rhizome.html" class="btn btn-primary" style="border-color:var(--kōura); background:var(--kōura); color:var(--muku);">See how it maps →</a>',
         '<p class="eyebrow" style="color:var(--kōura)" data-i18n="tir.iwi.eyebrow">Iwi, education & the pā</p>\n      <h2 style="color:var(--kōura)" data-i18n="tir.iwi.title">Every iwi is already a digital sovereign — the pā just makes it visible.</h2>\n      <p data-i18n="tir.iwi.body1">Iwi authorities already hold rangatiratanga over their rohe. Te Pā Literacy is a tool for exercising it in the digital domain: a shared curriculum, a shared campaign kit, and a shared rhizome — but each iwi runs its own node. Waikato-Tainui\'s pā looks different from Ngāi Tahu\'s, which looks different from Ngāpuhi\'s. That is the point.</p>\n      <p data-i18n="tir.iwi.body2">Education is the connector. When <a href="https://www.maoriparty.org.nz/education_training">Te Pāti Māori\'s education kaupapa</a> talks about Māori-led education, we read it as including the digital classroom — the algorithms our tamariki learn from every day.</p>\n      <a href="rhizome.html" class="btn btn-primary" style="border-color:var(--kōura); background:var(--kōura); color:var(--muku);" data-i18n="tir.iwi.cta">See how it maps →</a>'),
        ('<p class="eyebrow">Further reading</p>\n    <h2>Sources &amp; primary texts</h2>',
         '<p class="eyebrow" data-i18n="tir.reading.eyebrow">Further reading</p>\n    <h2 data-i18n="tir.reading.title">Sources &amp; primary texts</h2>'),
    ],

    'crowdfund.html': [
        ('<title>Crowdfund the Pā — AI Warrior × Te Pā Literacy</title>',
         '<title data-i18n="cf.title">Crowdfund the Pā — AI Warrior × Te Pā Literacy</title>'),
        ('<p class="eyebrow">Crowdfund — Kohi pūtea</p>\n      <h1 style="font-size:var(--text-3xl); max-width:22ch;">Openly funded. Openly licensed. Openly forked.</h1>\n      <p style="max-width:60ch;">Te Pā Literacy has no ad money, no foundation grants, and no strings. Whānau fund the pā. Every dollar goes to producing the next course, the next media kit, and the next wānanga in a rohe that asks for it.</p>\n      <p><strong>Three ways to tautoko:</strong></p>',
         '<p class="eyebrow" data-i18n="cf.eyebrow">Crowdfund — Kohi pūtea</p>\n      <h1 style="font-size:var(--text-3xl); max-width:22ch;" data-i18n="cf.h1">Openly funded. Openly licensed. Openly forked.</h1>\n      <p style="max-width:60ch;" data-i18n="cf.intro">Te Pā Literacy has no ad money, no foundation grants, and no strings. Whānau fund the pā. Every dollar goes to producing the next course, the next media kit, and the next wānanga in a rohe that asks for it.</p>\n      <p data-i18n="cf.tautoko.title"><strong>Three ways to tautoko:</strong></p>'),
        ('<a href="https://givealittle.co.nz/" class="btn btn-primary">One-off · Givealittle</a>\n        <a href="https://ko-fi.com/" class="btn btn-ghost">Monthly · Ko-fi</a>\n        <a href="https://thekiwidialectic.substack.com/subscribe" class="btn btn-ghost">Paid Substack</a>',
         '<a href="https://givealittle.co.nz/" class="btn btn-primary" data-i18n="cf.tautoko.oneoff">One-off · Givealittle</a>\n        <a href="https://ko-fi.com/" class="btn btn-ghost" data-i18n="cf.tautoko.monthly">Monthly · Ko-fi</a>\n        <a href="https://thekiwidialectic.substack.com/subscribe" class="btn btn-ghost" data-i18n="cf.tautoko.substack">Paid Substack</a>'),
        ('<p class="mono mt-7" style="color:var(--kōkōwai)">Note · placeholder links until each account is finalised. Update the URLs in <code>crowdfund.html</code> before you launch.</p>',
         '<p class="mono mt-7" style="color:var(--kōkōwai)" data-i18n="cf.tautoko.note">Note · placeholder links until each account is finalised. Update the URLs in <code>crowdfund.html</code> before you launch.</p>'),
        ('<h3 style="color:var(--kōura)">The transparent budget</h3>',
         '<h3 style="color:var(--kōura)" data-i18n="cf.budget.title">The transparent budget</h3>'),
        ('<tr><td style="padding:8px 0; border-bottom:1px solid rgba(239,230,211,0.15);">Course production (per module)</td>',
         '<tr><td style="padding:8px 0; border-bottom:1px solid rgba(239,230,211,0.15);" data-i18n="cf.budget.r1.label">Course production (per module)</td>'),
        ('<tr><td style="padding:8px 0; border-bottom:1px solid rgba(239,230,211,0.15);">Media kit design</td>',
         '<tr><td style="padding:8px 0; border-bottom:1px solid rgba(239,230,211,0.15);" data-i18n="cf.budget.r2.label">Media kit design</td>'),
        ('<tr><td style="padding:8px 0; border-bottom:1px solid rgba(239,230,211,0.15);">Poster printing (500 x A3)</td>',
         '<tr><td style="padding:8px 0; border-bottom:1px solid rgba(239,230,211,0.15);" data-i18n="cf.budget.r3.label">Poster printing (500 x A3)</td>'),
        ('<tr><td style="padding:8px 0; border-bottom:1px solid rgba(239,230,211,0.15);">Marae wānanga travel (per rohe)</td>',
         '<tr><td style="padding:8px 0; border-bottom:1px solid rgba(239,230,211,0.15);" data-i18n="cf.budget.r4.label">Marae wānanga travel (per rohe)</td>'),
        ('<tr><td style="padding:8px 0; border-bottom:1px solid rgba(239,230,211,0.15);">Hosting &amp; domains (annual)</td>',
         '<tr><td style="padding:8px 0; border-bottom:1px solid rgba(239,230,211,0.15);" data-i18n="cf.budget.r5.label">Hosting &amp; domains (annual)</td>'),
        ('<tr><td style="padding:8px 0; font-weight:700;">Full pā rollout (one rohe)</td>',
         '<tr><td style="padding:8px 0; font-weight:700;" data-i18n="cf.budget.r6.label">Full pā rollout (one rohe)</td>'),
        ('<p style="font-size:var(--text-sm); margin-top:var(--s-4);">All spending will be reported openly at the end of each module in <a href="https://thekiwidialectic.substack.com/" style="color:var(--kōura)">The Kiwi Dialectic</a>.</p>',
         '<p style="font-size:var(--text-sm); margin-top:var(--s-4);" data-i18n="cf.budget.note">All spending will be reported openly at the end of each module in <a href="https://thekiwidialectic.substack.com/" style="color:var(--kōura)">The Kiwi Dialectic</a>.</p>'),
        ('<p class="eyebrow">Milestones · Ngā tohu</p>\n    <h2>What each dollar unlocks.</h2>',
         '<p class="eyebrow" data-i18n="cf.milestones.eyebrow">Milestones · Ngā tohu</p>\n    <h2 data-i18n="cf.milestones.title">What each dollar unlocks.</h2>'),
        ('<h3>Module 6 · AI in the classroom</h3>\n        <p>Course + media kit + one wānanga in a school that requests it. Focus on kura kaupapa and wharekura.</p>',
         '<h3 data-i18n="cf.m1.title">Module 6 · AI in the classroom</h3>\n        <p data-i18n="cf.m1.body">Course + media kit + one wānanga in a school that requests it. Focus on kura kaupapa and wharekura.</p>'),
        ('<h3>Iwi data-sovereignty template pack</h3>\n        <p>Lawyer-reviewed template MOUs iwi orgs can use with tech vendors. Free to any iwi authority that asks.</p>',
         '<h3 data-i18n="cf.m2.title">Iwi data-sovereignty template pack</h3>\n        <p data-i18n="cf.m2.body">Lawyer-reviewed template MOUs iwi orgs can use with tech vendors. Free to any iwi authority that asks.</p>'),
        ('<h3>Roadshow · 6 rohe</h3>\n        <p>In-person wānanga across six rohe including Te Tai Tokerau, Waikato-Tainui, Te Arawa, Tairāwhiti, Taranaki and Ōtākou.</p>',
         '<h3 data-i18n="cf.m3.title">Roadshow · 6 rohe</h3>\n        <p data-i18n="cf.m3.body">In-person wānanga across six rohe including Te Tai Tokerau, Waikato-Tainui, Te Arawa, Tairāwhiti, Taranaki and Ōtākou.</p>'),
        ('<h3>Full curriculum translation</h3>\n        <p>Every course fully translated into te reo Māori with kaiako-reviewed subtitles for video content.</p>',
         '<h3 data-i18n="cf.m4.title">Full curriculum translation</h3>\n        <p data-i18n="cf.m4.body">Every course fully translated into te reo Māori with kaiako-reviewed subtitles for video content.</p>'),
        ('<p class="eyebrow" style="padding:0; margin-bottom:12px;">Share the kaupapa</p>\n    <h2 style="max-width:22ch; margin:0 auto var(--s-5);">The best fundraising is a repost.</h2>\n    <p style="max-width:60ch; margin:0 auto var(--s-6);">If you can\'t give, share. Send this URL to one whānau member, one workmate, one iwi authority. The rhizome grows sideways.</p>',
         '<p class="eyebrow" style="padding:0; margin-bottom:12px;" data-i18n="cf.share.eyebrow">Share the kaupapa</p>\n    <h2 style="max-width:22ch; margin:0 auto var(--s-5);" data-i18n="cf.share.title">The best fundraising is a repost.</h2>\n    <p style="max-width:60ch; margin:0 auto var(--s-6);" data-i18n="cf.share.body">If you can\'t give, share. Send this URL to one whānau member, one workmate, one iwi authority. The rhizome grows sideways.</p>'),
        ('class="btn btn-primary">Share on X →</a>',
         'class="btn btn-primary" data-i18n="cf.share.cta">Share on X →</a>'),
    ],
}


def apply(path, reps):
    p = ROOT / path
    src = p.read_text(encoding='utf-8')
    for old, new in reps:
        if old not in src:
            print(f"  [MISS] {path}: {old[:70]}...")
            continue
        src = src.replace(old, new, 1)
    p.write_text(src, encoding='utf-8')
    print(f"  [OK]   {path}")


for page in ['index.html', 'curriculum.html', 'campaigns.html', 'rhizome.html', 'tiriti.html', 'crowdfund.html']:
    print(f"→ {page}")
    apply(page, SHARED + PAGES.get(page, []))

print("Done.")
