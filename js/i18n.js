/* AI Warrior × Te Pā Literacy — i18n engine
 *
 * Scalable to any additional indigenous language: add a new dictionary block
 * (e.g. HAW, QU, SM) and add the code to LANGUAGES below.
 *
 * Usage in HTML:
 *   <h1 data-i18n="home.hero.title">Arm the pā</h1>
 *   <a data-i18n="nav.home">Home</a>
 *
 * For attributes:
 *   <input data-i18n-attr="placeholder:form.email.placeholder" placeholder="...">
 *
 * The default (untranslated) text stays in HTML as the EN fallback.
 */

const LANGUAGES = [
  { code: 'en', label: 'EN', name: 'English' },
  { code: 'mi', label: 'MI', name: 'Te Reo Māori' }
];

const DICT = {
  en: {}, // English keys resolve to the HTML default via fallback
  mi: {
    // ===== Nav =====
    'nav.home': 'Kāinga',
    'nav.curriculum': 'Marautanga',
    'nav.campaigns': 'Kokiritanga',
    'nav.rhizome': 'Wharawhara',
    'nav.tiriti': 'Te Tiriti',
    'nav.support': 'Tautoko Kaupapa',
    'nav.menu': 'Tahua',
    'nav.lang.label': 'Reo',

    // ===== Footer (shared) =====
    'footer.brand.title': 'AI Warrior',
    'footer.brand.body': 'Te Pā Literacy — te mātau matihiko kaupapa Māori mō ngā iwi, hapū me ngā whānau. He rāhui tuwhera. Ka utua e te whānau.',
    'footer.kaupapa': 'Kaupapa',
    'footer.support': 'Tautoko',
    'footer.support.crowdfund': 'Kohi pūtea',
    'footer.support.substack': 'The Kiwi Dialectic',
    'footer.support.tpm': 'Te Pāti Māori',
    'footer.open': 'Tuwhera',
    'footer.open.repo': 'Puna GitHub',
    'footer.open.data': 'Raraunga wharawhara (JSON)',
    'footer.open.licence': 'CC BY-SA 4.0',
    'footer.bottom': 'Nā te whānau, mā te whānau. · I hangaia ki Ōtepoti · Whakawhetai ki ia iwi, ia hapū, ia marae e mau ana i tēnei kaupapa.',

    // ===== Index (home) =====
    'home.title': 'AI Warrior × Te Pā Literacy — mō ngā iwi, whānau me ngā mokopuna',
    'home.hero.eyebrow': 'Kia mataara · He pā mātau matihiko kaupapa Māori',
    'home.hero.title.full': 'Whakangungua te <span class="accent">pā</span>.<br>Tiakina ngā <span class="accent">mokopuna</span>.',
    'home.hero.title.pre': 'Whakangungua te ',
    'home.hero.title.accent1': 'pā',
    'home.hero.title.mid': '. Tiakina ngā ',
    'home.hero.title.accent2': 'mokopuna',
    'home.hero.title.post': '.',
    'home.hero.sub': 'He kaupapa mātauranga tuwhera, whānau-tuatahi a AI Warrior × Te Pā Literacy. Ka whakaakona e mātou ngā iwi, ngā hapū me ngā whānau ki te pānui, ki te whakaeke, ki te whakaraupapa anō i ngā pūmanawa hangarau, ngā ataata pōhēhē me ngā mīhini kohi raraunga e whakatakoto nei i Aotearoa — e mau tonu ana ki Te Tiriti o Waitangi me te tino rangatiratanga.',
    'home.hero.cta.curriculum': 'Tīmata te Marautanga →',
    'home.hero.cta.crowdfund': 'Kohi Pūtea mō te Pā',
    'home.hero.cta.rhizome': 'Huakina te Wharawhara',

    'home.why.eyebrow': 'He aha ināianei',
    'home.why.title': 'Kua uru kē te whenua tāmi matihiko ki roto i te pā.',
    'home.why.deepfake.title': 'Pōhēhē kikokiko-kore',
    'home.why.deepfake.body': 'Kua horahia kētia ngā ataata me ngā reo waihanga o te tangata whenua, o ngā kaumātua me ngā mema pāremata i runga i a X, TikTok, Facebook — kua hangaia hei wehewehe i te whānau, hei whakaiti i te reo tōrangapū Māori.',
    'home.why.data.title': 'Kohi raraunga',
    'home.why.data.body': 'Kei te kohia te mātauranga iwi, te whakapapa, ngā waiata me te reo e ngā tauira AI o tāwāhi — kāore he whakaaetanga, kāore he wāhi tuari painga. He takahi Tiriti tēnei i te ao hou.',
    'home.why.silencing.title': 'Whakamū pūmanawa',
    'home.why.silencing.body': 'E whakaitia ana, e ārai ana, e huna ana ngā reo Māori. Ko te mātau ki te mīhini te mahi tuatahi o te tino rangatiratanga i te ao matihiko.',

    'home.pou.eyebrow': 'Ngā pou e rima',
    'home.pou.title': 'Whakaako · Whakangungu · Tiaki · Tuari · Whanake',
    'home.pou.intro': 'E ai ki ngā pou e rima e mau ai te whare o te mana motuhake matihiko. Ka mau tētahi akoranga, tētahi kete pāpāho, tētahi kokiritanga huarahi, tētahi wāhi wharawhara i ia pou.',
    'home.pou.1.title': '1. Whakaako — Educate',
    'home.pou.1.body': 'He akoranga poto, kore utu, i te reo Māori me te reo Pākehā. Ka tukua mā ',
    'home.pou.2.title': '2. Whakangungu — Arm',
    'home.pou.2.body': 'Ngā kete pāpāho pāpori tikiake, ngā tauira mīmī, ngā tuhinga whakautu me ngā whakarāpopototanga tirohanga meka.',
    'home.pou.3.title': '3. Tiaki — Protect',
    'home.pou.3.body': 'Ngā rārangi tirotiro mana raraunga mō ngā whakahaere iwi, marae me ngā kura. He aratohu kimi ataata pōhēhē.',
    'home.pou.4.title': '4. Tuari — Share',
    'home.pou.4.body': 'Ka tuaritia mā te wharawhara — kāore he pūmanawa hei ārai. Whānau ki te whānau.',
    'home.pou.5.title': '5. Whanake — Grow',
    'home.pou.5.body': 'He mea kohi pūtea, he rāhui tuwhera, ka taea te māakenga. Ka taea e ia marae te whakahaere i tōna anō Pā.',

    'home.tiriti.eyebrow': 'E mau ana ki Te Tiriti',
    'home.tiriti.title': 'Ia akoranga, ia kokiritanga, ia pona wharawhara — ka pānuihia mā Te Tiriti o Waitangi.',
    'home.tiriti.body': 'Ka whakaakona ngā tuhinga e toru hei taputapu ora, ehara i te taonga whare taonga: ko te kāwanatanga (te mana iti i tukua ki te Karauna), ko te tino rangatiratanga (te rangatiratanga Māori kaha ki runga i ngā taonga — tae atu ki te raraunga, te reo me te whakapapa), me te ōritetanga (te ōrite o te kirirarautanga). Ko ngā pūnaha AI e ngaro ana ki tētahi o ēnei e toru he takahi Tiriti.',
    'home.tiriti.cta': 'Pānuihia te tātaritanga Te Tiriti →',
    'home.tiriti.quote': '"Ko te reo te mauri o te mana Māori — ā, kua uru te waehere ki roto i te reo."',
    'home.tiriti.quote.cite': '— Te kaupapa Te Pā Literacy',

    'home.fork.eyebrow': 'Māakengia te pā',
    'home.fork.title': 'He kaupapa tuwhera tēnei. Māua, whakarerekētia, whakahaeretia i tō rohe.',
    'home.fork.body': 'Kei runga i GitHub te katoa o te kaupapa — ngā akoranga, ngā kete pāpāho, ngā raraunga wharawhara, ngā tauira kokiritanga — i raro i te rāhui Creative Commons. Kohia he pūtea mō te kōwae ā-mua, māakengia rānei, whakahangaia tō ake.',
    'home.fork.cta.crowdfund': 'Kohi Pūtea Ināianei',
    'home.fork.cta.mediakit': 'Tikiake te Kete Pāpāho',

    // ===== Curriculum =====
    'cur.title': 'Marautanga — AI Warrior × Te Pā Literacy',
    'cur.eyebrow': 'Marautanga · Ngā akoranga',
    'cur.h1': 'E rima ngā akoranga. Ka mau te katoa ki Te Tiriti.',
    'cur.intro.full': 'He kore utu ia akoranga, he poto (60–90 mīniti), ka tukua mā <a href="https://thekiwidialectic.substack.com/">The Kiwi Dialectic</a>, ā, ka tāpirihia he kete tikiake mō ngā marae, ngā kura me ngā whakahaere iwi. Whāia i te raupapa, hopo mai rānei ki tērā e hiahiatia ana e tō rohe.',
    'cur.c1.meta': 'Tuhinga 1 · Kāwanatanga · 60 mīniti · <a href="https://thekiwidialectic.substack.com/">Whakauru mā Substack →</a>',
    'cur.c2.meta': 'Tuhinga 3 · Ōritetanga · 75 mīniti · <a href="https://thekiwidialectic.substack.com/">Whakauru →</a>',
    'cur.c3.meta': 'Tuhinga 2 · Tino Rangatiratanga · 90 mīniti · <a href="https://thekiwidialectic.substack.com/">Whakauru →</a>',
    'cur.c4.meta': 'Tuhinga 2 · Tino Rangatiratanga · 75 mīniti · <a href="https://thekiwidialectic.substack.com/">Whakauru →</a>',
    'cur.c5.meta': 'Ngā Tuhinga 1, 2, 3 · 90 mīniti · <a href="https://thekiwidialectic.substack.com/">Whakauru →</a>',
    'cur.intro.pre': 'He kore utu ia akoranga, he poto (60–90 mīniti), ka tukua mā ',
    'cur.intro.mid': ', ā, ka tāpirihia he kete tikiake mō ngā marae, ngā kura me ngā whakahaere iwi. Whāia i te raupapa, hopo mai rānei ki tērā e hiahiatia ana e tō rohe.',
    'cur.c1.title': 'Ngā Take AI — He aha te AI?',
    'cur.c1.body': 'He aha te tauira reo nui? Nō whea mai te raraunga? Nō wai te ao e mau ana ki roto i ngā otinga? He whakamārama māmā mō te whānau o ia rōpū pakeke.',
    'cur.c1.meta.pre': 'Tuhinga 1 · Kāwanatanga · 60 mīniti · ',
    'cur.c1.meta.link': 'Whakauru mā Substack →',
    'cur.c2.title': 'Ataata Pōhēhē me te Whakawaitara — Te pōhēhē kikokiko-kore',
    'cur.c2.body': 'Me pēhea te kimi i ngā ataata me ngā reo waihanga. Ngā taputapu rapu-whakaahua-hurihuri, ngā taputapu takenga, me tētahi rākau whakatau mō ngā whakawhitiwhitinga rōpū whānau. Ka tāpirihia he rārangi tirotiro tikiake mō ngā kaumātua.',
    'cur.c2.meta.pre': 'Tuhinga 3 · Ōritetanga · 75 mīniti · ',
    'cur.c2.meta.link': 'Whakauru →',
    'cur.c3.title': 'Mana Raraunga — Ko wai te rangatira o ō tātou raraunga?',
    'cur.c3.body': 'Ko te whakapapa, te waiata, te reo hei taonga i raro i te Tuhinga 2. Ngā mātāpono ',
    'cur.c3.body.mid': ' e whakamahia ana. He rārangi tirotiro mō ngā whakahaere iwi e whiriwhiri ana ki ngā kaihoko hangarau.',
    'cur.c3.meta.pre': 'Tuhinga 2 · Tino Rangatiratanga · 90 mīniti · ',
    'cur.c3.meta.link': 'Whakauru →',
    'cur.c4.title': 'Tāmi Pūmanawa — Te tāmi a te pūmanawa',
    'cur.c4.body': 'Me pēhea ngā mīhini taunaki, ngā kaupapa here whakahaere me ngā kōwhiringa moni whakautu e patu ai i te reo Māori. Ngā tauira mai i a X, Meta me TikTok. Me aha ina ārahia koe.',
    'cur.c4.meta.pre': 'Tuhinga 2 · Tino Rangatiratanga · 75 mīniti · ',
    'cur.c4.meta.link': 'Whakauru →',
    'cur.c5.title': 'Te Pā Tuihono Whānau — Te hanga i tō pā tuihono',
    'cur.c5.body': 'He whakaharatau: whakaritea tō ake pae tukutuku marae, ngā whakawhitinga haumaru, te rārangi mēra me te pona wharawhara. He kore utu, he tauira māakenga, kāore he whakawhirinaki ki ngā papaaho tāmi.',
    'cur.c5.meta.pre': 'Ngā Tuhinga 1, 2, 3 · 90 mīniti · ',
    'cur.c5.meta.link': 'Whakauru →',
    'cur.feed.title': 'Puna akoranga — Ngā mea hou',
    'cur.feed.body': 'Ka tukua he kōwae hou ia marama. Ohaurutia kotahi noa, ā, ka tae atu ki tō pouaka mēra tētahi akoranga me te kete pāpāho katoa.',
    'cur.feed.cta': 'Ohaurutia ki The Kiwi Dialectic →',

    // ===== Campaigns =====
    'camp.title': 'Kokiritanga — AI Warrior × Te Pā Literacy',
    'camp.eyebrow': 'Kokiritanga · Ngā kokiritanga',
    'camp.h1': 'Ngā kete pāpāho, ngā pānui huarahi me ngā kokiritanga tuihono taketake.',
    'camp.intro.full': 'Ka taea te tikiake, te māakenga me te tuari anō i ia mea o tēnei whārangi i raro i te CC BY-SA 4.0. Mēnā he rerekētanga anō e hiahiatia ana e tō marae, tō rōpū, whakapā mai mā <a href="https://thekiwidialectic.substack.com/">The Kiwi Dialectic</a>.',
    'camp.intro.pre': 'Ka taea te tikiake, te māakenga me te tuari anō i ia mea o tēnei whārangi i raro i te CC BY-SA 4.0. Mēnā he rerekētanga anō e hiahiatia ana e tō marae, tō rōpū, whakapā mai mā ',
    'camp.intro.link': 'The Kiwi Dialectic',
    'camp.intro.post': '.',

    'camp.c1.label': '01 · Kete pāpori',
    'camp.c1.title': 'Whakangungu — Whakangungua tō pae',
    'camp.c1.body': 'Ngā tauira Instagram, ngā tuhinga whīti X/Twitter, ngā whakamārama TikTok me tētahi kete mīmī. Kua whakaritea mō ia papaaho. Ka tāpirihia ngā tapanga i te reo Māori me te reo Pākehā.',
    'camp.c1.li1': '10 tauira whakahuahua (Canva + Figma)',
    'camp.c1.li2': '25 tauira mīmī (PNG + SVG whakarerekē)',
    'camp.c1.li3': 'Ngā tuhinga whīti mō ngā kōrero AI-pōhēhē e rima',
    'camp.c1.li4': 'Aratohu āhuatanga tohu me te ingoa',
    'camp.c1.cta': 'Tikiake te kete pāpori (zip)',

    'camp.c2.label': '02 · Kokiritanga huarahi',
    'camp.c2.title': 'Ki te whenua — Ki runga i te whenua',
    'camp.c2.body': 'Ngā pānui A3, A2, ngā pepa noho papa marae, ngā pepa piri me tētahi puka whakapiri parāoa. Ka taea te tā ki runga i ia pūrere. Ngā PDF ka reri mō te whare tā i te 300dpi.',
    'camp.c2.li1': '6 hoahoa pānui (reo rua, mangu me te whero)',
    'camp.c2.li2': 'Pepa piri — 24 kei ia A4',
    'camp.c2.li3': 'Aratohu whakapiri parāoa (he ritenga haumaru, taiao)',
    'camp.c2.li4': 'Tauira pānui marae — DOCX whakarerekē',
    'camp.c2.cta': 'Tikiake te kete huarahi (zip)',

    'camp.c3.label': '03 · Kete pāpāho',
    'camp.c3.title': 'Ki te hunga pāpāho — Mō ngā kairīpoata',
    'camp.c3.body': 'Ngā mea katoa e hiahiatia ana e te kairīpoata, e te kaipāhihi hei kawe pai i te kaupapa: puka meka, kōrero mō ngā kaikōrero, ngā tohu paearu-teitei, aratohu whakamahi tohutō, me ngā whakaahua kua whakaaetia.',
    'camp.c3.li1': 'Puka meka whārangi rua (PDF)',
    'camp.c3.li2': 'Kete tohu — SVG, PNG, tae kotahi/tae maha',
    'camp.c3.li3': 'Aratohu āhuatanga me te whakahua',
    'camp.c3.li4': 'Kāri whakapā kaikōrero',
    'camp.c3.cta': 'Tikiake te kete pāpāho (zip)',

    'camp.c4.label': '04 · Kokiritanga tuihono',
    'camp.c4.title': 'Tuihono — Kokiritanga tuihono taketake',
    'camp.c4.body': 'He raupapa īmēra kua tuhia kētia, ngā tuhinga whakautu wāhanga whakahoki kōrero, ngā kete tuku Reddit/BlueSky/Mastodon, me tētahi kete tīmatanga rōpū Signal mō ngā kairuruku whānau.',
    'camp.c4.li1': 'Raupapa īmēra tīmatanga e 5',
    'camp.c4.li2': 'Puna whakautu (30+ ngā tuhinga)',
    'camp.c4.li3': 'Kete tīmatanga rōpū Signal',
    'camp.c4.li4': 'Ngā tauira tuari Substack',
    'camp.c4.cta': 'Tikiake te kete tuihono (zip)',

    'camp.cycle.eyebrow': 'Te huringa tuhi-me-te-tuari',
    'camp.cycle.title': 'Ka whāia e ia kokiritanga ngā mahi ōrite e ono.',
    'camp.cycle.1': 'Whakaaro — kōwhiria te kaupapa (kotahi anake te kōrero mārama).',
    'camp.cycle.2': 'Tuhi — tuhia i te reo hapori e kōrerohia ana e tō whānau.',
    'camp.cycle.3': 'Whakaahua — hangaia te whakaahua (mīmī, pānui, kāri whīti).',
    'camp.cycle.4': 'Tuku — tukua mā te wharawhara — kaua e utua, kaua e whakawāhia.',
    'camp.cycle.5': 'Whakautu — whakautua, kaua e tautohetohe. Nekehia ngā tāngata, kaua e riro.',
    'camp.cycle.6': 'Whakawhanaunga — pōhiritia rātou ki roto i te pā (ohauru, uru ki te Signal, haere mai ki te wānanga).',
    'camp.rule.title': 'Kotahi te ture',
    'camp.rule.body': 'Ki te kore e taea e tētahi kaumātua i runga i te Chromebook i te kīhini marae te whakahaere i te kokiritanga, ehara i a mātou tērā kokiritanga.',

    // ===== Rhizome =====
    'rz.title': 'Mapi Wharawhara — AI Warrior × Te Pā Literacy',
    'rz.eyebrow': 'Te Mapi Wharawhara',
    'rz.h1': 'Ehara i te rākau. He wharawhara.',
    'rz.intro': 'Whāia a Deleuze me Guattari — ā, tata mai ki te kāinga, ko te tipu tūturu o te kūmara — kāore he tihi, kāore he rangatira, kāore he tari matua o tēnei mapi. Ka hono katoa ngā pona ki te taha. Pāwhiritia tētahi pona kia kōkiri ki te puna. Toia hei tirotiro. Ko Te Pāti Māori tēnei, ōna kaupapa, ōna hononga ki ngā iwi, tā mātou marautanga me ngā kokiritanga, kei roto katoa i te wāhi kotahi.',
    'rz.filter.all': 'Katoa',
    'rz.filter.leader': 'Rangatira',
    'rz.filter.mp': 'MP',
    'rz.filter.iwi': 'Iwi',
    'rz.filter.kaupapa': 'Kaupapa',
    'rz.filter.policy': 'Kaupapa here',
    'rz.filter.campaign': 'Kokiritanga',
    'rz.filter.course': 'Akoranga',
    'rz.filter.fund': 'Pūtea',
    'rz.tip': 'Tohutohu · Pāwhiria tētahi pona hei huaki i tōna puna. Toia hei nuku. Panehia hei topa. I te waea, mihia.',
    'rz.print.eyebrow': 'Wharawhara pūmau — mō te tā, ngā pānui me te PDF',
    'rz.print.title': 'Ko te putanga taea te tā.',
    'rz.print.body': 'Ko ngā hononga ōrite, kua tāraia mā te ringa mō te tā A3. Whakairihia ki te pakitara marae, whakawhāitihia rānei ki roto i te pukapuka.',
    'rz.print.link.svg': 'Tikiake SVG kua reri mō te tā',
    'rz.print.link.data': 'Raraunga JSON',

    // ===== Tiriti =====
    'tir.title': 'Tātaritanga Te Tiriti — AI Warrior × Te Pā Literacy',
    'tir.eyebrow': 'Te Tiriti o Waitangi — pānuihia mā te AI',
    'tir.h1': 'E toru ngā tuhinga. Kotahi te taonga. He taputapu ora ki te whakahē i te tāmi matihiko.',
    'tir.intro.full': 'Ko te tuarā whakamāori tēnei o te kaupapa katoa. Ka pānuihia ia kōwae, ia kokiritanga, ia pona wharawhara mā ngā tuhinga e toru o <em>Te Tiriti o Waitangi</em> — te tuhinga Māori i hainatia ki Waitangi i te 6 o Pēpuere 1840. Ka whakamahia e mātou te tuhinga Māori, kaua ko te "Treaty" Pākehā, nā te mea koinā te tuhinga i hainatia e ngā rangatira. Pānuihia te whakarāpopototanga reo māmā i <a href="https://nzhistory.govt.nz/politics/treaty/the-treaty-in-brief">NZ History</a>, te whakataurite mātauranga rānei i <a href="https://teara.govt.nz/en/document/4216/the-three-articles-of-the-treaty-of-waitangi">Te Ara</a>.',
    'tir.intro.pre': 'Ko te tuarā whakamāori tēnei o te kaupapa katoa. Ka pānuihia ia kōwae, ia kokiritanga, ia pona wharawhara mā ngā tuhinga e toru o ',
    'tir.intro.em': 'Te Tiriti o Waitangi',
    'tir.intro.mid': ' — te tuhinga Māori i hainatia ki Waitangi i te 6 o Pēpuere 1840. Ka whakamahia e mātou te tuhinga Māori, kaua ko te "Treaty" Pākehā, nā te mea koinā te tuhinga i hainatia e ngā rangatira. Pānuihia te whakarāpopototanga reo māmā i ',
    'tir.intro.link1': 'NZ History',
    'tir.intro.or': ' te whakataurite mātauranga i ',
    'tir.intro.link2': 'Te Ara',
    'tir.intro.post': '.',

    'tir.a1.label': 'Tuhinga 1 · Kāwanatanga',
    'tir.a1.title': 'Kāwanatanga — he iti, i tukua, he here.',
    'tir.a1.body1': 'I tukua e ngā rangatira te kāwanatanga (governance) ki te Karauna — ehara i te rangatiratanga. I te ao AI, ko te tikanga: ka taea e te Karauna te whakahaere i ngā whakawhitiwhitinga, i te tuakiri matihiko me ngā kino papaaho — engari i roto anake i tōna mana iti kua tukua. Kāore e taea e ia te whakahaere i ngā raraunga Māori, i te reo Māori rānei.',
    'tir.a1.body2': 'Ka whakaakona e mātou: te rerekētanga i waenga i te kāwanatanga me te mana motuhake, me ngā rohe o ia mea i te ao matihiko.',

    'tir.a2.label': 'Tuhinga 2 · Tino Rangatiratanga',
    'tir.a2.title': 'Te mana kaha ki runga i ngā taonga katoa.',
    'tir.a2.body1': 'I puritia e ngā rangatira te tino rangatiratanga — te rangatiratanga kaha, tūturu — ki runga i ō rātou whenua, kāinga me ngā taonga katoa. He taonga te reo, te whakapapa, te waiata, te mātauranga, ā, ināianei, ko te raraunga hoki. Ko ia tauira AI kua whakangungutia ki ngā taonga Māori kāore he whakaaetanga tuwhera, mua, mātau — he takahi Tiriti tērā.',
    'tir.a2.body2': 'Ka whakaakona e mātou: ngā mātāpono ',
    'tir.a2.body2.mid': ', te kāwanatanga raraunga iwi, me te tuhi i tētahi whakaaetanga tuari raraunga hei tino tiaki i tō rohe.',

    'tir.a3.label': 'Tuhinga 3 · Ōritetanga',
    'tir.a3.title': 'Ōritetanga — o te kirirarautanga me ngā otinga.',
    'tir.a3.body1': 'I whakaaetia ki ngā Māori ngā motika me ngā tikanga ōrite ki ngā tāngata o Peretānia. Ka takahia te Tuhinga 3 ina hē ake ngā otinga o ngā pūnaha pūmanawa mō te Māori — i te tatau nama, i te whakatura pirihimana, i te kimi hē whiwhinga, i te whakarōpū hauora rānei. He papa te ōritetanga, ehara i te tuanui.',
    'tir.a3.body2': 'Ka whakaakona e mātou: me pēhea te tirotiro i tētahi pūmanawa mō te whai pānga rerekē, me te tuku pātai OIA, kerēme rānei ki te Rōpū Whakamana i te Tiriti.',

    'tir.a4.label': 'Te tuawhā ā-waha',
    'tir.a4.title': 'Wairuatanga — te oati ā-waha.',
    'tir.a4.body': 'I Waitangi, i whakaputaina e te Kāwana Hobson te whakaaetanga ā-waha o te herekore whakapono me te tikanga. Ka whakawhānuihia e mātou tēnei ki te wairuatanga matihiko: te motika ki te karakia, te tikanga, te tapu i te taha o te raraunga, te waehere me te whakawhitinga — te motika kia hangaia te AI e ngā ao Māori, kaua kia whakauruhia noatia rātou.',

    'tir.iwi.eyebrow': 'Iwi, mātauranga me te pā',
    'tir.iwi.title': 'Kua rangatira kē ia iwi i te ao matihiko — ka whakaatuhia noatia e te pā.',
    'tir.iwi.body1': 'Kei ngā mana whakahaere iwi te rangatiratanga o tō rātou rohe. He taputapu Te Pā Literacy ki te whakatinana i tēnā i te ao matihiko: he marautanga tāpiri, he kete kokiritanga tāpiri, he wharawhara tāpiri — engari ka whakahaere ia iwi i tōna pona ake. He rerekē te pā o Waikato-Tainui i te pā o Ngāi Tahu, he rerekē tērā i te pā o Ngāpuhi. Koinā te tikanga.',
    'tir.iwi.body2.pre': 'Ko te mātauranga te kaihono. Ina kōrero ',
    'tir.iwi.body2.link': 'te kaupapa mātauranga a Te Pāti Māori',
    'tir.iwi.body2.post': ' mō te mātauranga arahi-Māori, ka pānui mātou ki roto rā ko te akomanga matihiko hoki — ngā pūmanawa e whakaakona ana ā tātou tamariki i ia rā.',
    'tir.iwi.cta': 'Tirohia te mapi →',

    'tir.reading.eyebrow': 'Ētahi atu pānuitanga',
    'tir.reading.title': 'Ngā puna me ngā tuhinga tuatahi',

    // ===== Crowdfund =====
    'cf.title': 'Kohi Pūtea mō te Pā — AI Warrior × Te Pā Literacy',
    'cf.eyebrow': 'Kohi pūtea — Kohi pūtea',
    'cf.h1': 'Kua tuwhera te utu. Kua tuwhera te rāhui. Kua tuwhera te māakenga.',
    'cf.intro': 'Kāore he moni pānui a Te Pā Literacy, kāore he pūtea rangapū, kāore he here. Ka utua e te whānau te pā. Ka tukua ia tāra ki te whakaputa i te akoranga ā-mua, i te kete pāpāho ā-mua, i te wānanga ā-mua ki tētahi rohe e tono ana.',
    'cf.tautoko.title': 'E toru ngā ara tautoko:',
    'cf.tautoko.oneoff': 'Kotahi noa · Givealittle',
    'cf.tautoko.monthly': 'Ia marama · Ko-fi',
    'cf.tautoko.substack': 'Substack utu',
    'cf.tautoko.note': 'Tuhipoka · he hononga tauira i tēnei wā kia oti ai ngā pūkete. Whakahoutia ngā URL i roto i te crowdfund.html i mua i te tuku.',

    'cf.budget.title': 'Te tahua tuwhera',
    'cf.budget.r1.label': 'Whakaputanga akoranga (ia kōwae)',
    'cf.budget.r2.label': 'Hoahoa kete pāpāho',
    'cf.budget.r3.label': 'Tā pānui (500 x A3)',
    'cf.budget.r4.label': 'Haere ki te wānanga marae (ia rohe)',
    'cf.budget.r5.label': 'Whakahaere me te rohe (ā-tau)',
    'cf.budget.r6.label': 'Whakatakoto Pā katoa (kotahi rohe)',
    'cf.budget.note': 'Ka pūrongotia ngā whakapaunga katoa i te mutunga o ia kōwae i <a href="https://thekiwidialectic.substack.com/" style="color:var(--kōura)">The Kiwi Dialectic</a>.',
    'cf.budget.note.pre': 'Ka pūrongotia ngā whakapaunga katoa i te mutunga o ia kōwae i ',

    'cf.milestones.eyebrow': 'Ngā tohu · Ngā tohu',
    'cf.milestones.title': 'He aha ka whakawāteatia e ia tāra.',
    'cf.m1.title': 'Kōwae 6 · AI i te akomanga',
    'cf.m1.body': 'Akoranga + kete pāpāho + kotahi wānanga i tētahi kura e tono ana. Aro ki te kura kaupapa me te wharekura.',
    'cf.m2.title': 'Kete tauira mana raraunga iwi',
    'cf.m2.body': 'Ngā MOU tauira kua tirohia e te rōia mā ngā whakahaere iwi ki ngā kaihoko hangarau. Kore utu ki ia mana whakahaere iwi e tono ana.',
    'cf.m3.title': 'Haerenga · 6 rohe',
    'cf.m3.body': 'Ngā wānanga ā-kanohi ki ngā rohe e ono tae atu ki Te Tai Tokerau, Waikato-Tainui, Te Arawa, Tairāwhiti, Taranaki me Ōtākou.',
    'cf.m4.title': 'Whakamāoritanga o te marautanga katoa',
    'cf.m4.body': 'Ka whakamāoritia ia akoranga katoa ki te reo Māori me ngā hauraro kua tirohia e te kaiako mō ngā ataata.',

    'cf.share.eyebrow': 'Tuaria te kaupapa',
    'cf.share.title': 'Ko te tuari anō te kohi pūtea pai rawa atu.',
    'cf.share.body': 'Ki te kore e taea e koe te koha, tuaria. Tukua tēnei URL ki tētahi mema whānau, ki tētahi hoa mahi, ki tētahi mana whakahaere iwi. Ka tipu te wharawhara ki te taha.',
    'cf.share.cta': 'Tuaria ki runga i a X →'
  }
};

const CURRENT = {
  code: (typeof localStorage !== 'undefined' && localStorage.getItem('aiw_lang')) || 'en'
};

function t(key, fallback) {
  const dict = DICT[CURRENT.code];
  if (dict && Object.prototype.hasOwnProperty.call(dict, key)) return dict[key];
  return fallback != null ? fallback : key;
}

function applyTranslations(root) {
  const scope = root || document;

  scope.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (!el.hasAttribute('data-i18n-default')) {
      el.setAttribute('data-i18n-default', el.innerHTML);
    }
    const fallback = el.getAttribute('data-i18n-default');
    if (CURRENT.code === 'en' || !DICT[CURRENT.code] || !Object.prototype.hasOwnProperty.call(DICT[CURRENT.code], key)) {
      el.innerHTML = fallback;
    } else {
      el.innerHTML = DICT[CURRENT.code][key];
    }
  });

  scope.querySelectorAll('[data-i18n-attr]').forEach(el => {
    el.getAttribute('data-i18n-attr').split(';').forEach(pair => {
      const [attr, key] = pair.split(':').map(s => s.trim());
      if (!attr || !key) return;
      const defAttr = `data-i18n-default-${attr}`;
      if (!el.hasAttribute(defAttr)) {
        el.setAttribute(defAttr, el.getAttribute(attr) || '');
      }
      const fallback = el.getAttribute(defAttr);
      if (CURRENT.code === 'en' || !DICT[CURRENT.code] || !Object.prototype.hasOwnProperty.call(DICT[CURRENT.code], key)) {
        el.setAttribute(attr, fallback);
      } else {
        el.setAttribute(attr, DICT[CURRENT.code][key]);
      }
    });
  });

  // Update <html lang> and page title
  document.documentElement.setAttribute('lang', CURRENT.code === 'mi' ? 'mi' : 'en');
  const titleEl = document.querySelector('title[data-i18n]');
  if (titleEl) document.title = titleEl.textContent;

  // Update lang toggle chips
  document.querySelectorAll('.lang-toggle button').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-lang') === CURRENT.code);
    btn.setAttribute('aria-pressed', btn.getAttribute('data-lang') === CURRENT.code ? 'true' : 'false');
  });
}

function setLang(code) {
  if (!DICT[code]) return;
  CURRENT.code = code;
  try { localStorage.setItem('aiw_lang', code); } catch (e) {}
  applyTranslations();
  document.dispatchEvent(new CustomEvent('langchange', { detail: { code } }));
}

function injectToggle() {
  const nav = document.querySelector('.nav');
  if (!nav || nav.querySelector('.lang-toggle')) return;
  const wrap = document.createElement('div');
  wrap.className = 'lang-toggle';
  wrap.setAttribute('role', 'group');
  wrap.setAttribute('aria-label', 'Language / Reo');
  LANGUAGES.forEach(lang => {
    const b = document.createElement('button');
    b.type = 'button';
    b.setAttribute('data-lang', lang.code);
    b.setAttribute('title', lang.name);
    b.textContent = lang.label;
    b.addEventListener('click', () => setLang(lang.code));
    wrap.appendChild(b);
  });
  nav.appendChild(wrap);
}

document.addEventListener('DOMContentLoaded', () => {
  injectToggle();
  applyTranslations();
});

// Expose for other scripts (e.g. rhizome.js)
window.AIW_I18N = { t, setLang, applyTranslations, current: () => CURRENT.code };
