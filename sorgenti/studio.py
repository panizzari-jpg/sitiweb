from core import *

D = "pangeastudio.it"
P = PANGEA
MS = "https://s0.wp.com/mshots/v1/https%3A%2F%2F{}%2F?w=1200"

CSS = """/* VOICE: studio locale serio, concreto, orgoglioso dei lavori pubblicati
IDEA: il portfolio come prova — siti veri di cantine, ristoranti, aziende dell'Oltrepò
PICTURE: finestra browser + smartphone con un sito di cantina in costruzione
COLOUR/TYPE: rosso vino dominante, pietra calda di supporto, blu cobalto d'accento; Schibsted Grotesk 800 + Inter
LAYOUT: hero a due colonne, bande servizi/settori/portfolio, CTA finale sul rosso */
:root{--fh:'Schibsted Grotesk',system-ui,sans-serif;--fb:'Inter',system-ui,sans-serif;
--bg:light-dark(#ffffff,#141015);--ink:light-dark(#221c24,#ece6ee);--head:light-dark(#170f19,#faf5fb);--mute:light-dark(#5d5460,#b9aebd);
--sup:light-dark(#f5f0ea,#1e1820);--card:light-dark(#ffffff,#1b151d);--line:light-dark(#e6ddd3,#382d3a);--line2:light-dark(#b9aa9b,#5b4b5e);
--dom:#5c1426;--dom2:#5c1426;--ondom:#fbeff1;--acc:#2a55e6;--acc2:#1f43bf;--onacc:#ffffff;--link:light-dark(#2447c7,#93acff);
--foot:#2b0b14;--onfoot:#f4e5e8;--phbg:light-dark(#efe6dc,#251d27);--phink:light-dark(#5c1426,#e8cfd5)}
:root[data-theme=light]{color-scheme:light}:root[data-theme=dark]{color-scheme:dark}
@media(prefers-color-scheme:dark){:root:not([data-theme=light]){--dom2:#d77d92}}
.pf .ph{aspect-ratio:3/2}
.sec{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 18px;padding:0;list-style:none}
.sec li{background:var(--sup);border-radius:999px;padding:6px 12px;font-size:14.5px}
.pk{display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr))}
.pk .card.rec{border:2px solid var(--acc)}
"""

HERO_SVG = """<svg viewBox="0 0 520 420" role="img" aria-label="Illustrazione: sito di una cantina su computer e smartphone">
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f3d9c4"/><stop offset="1" stop-color="#e7b9a0"/></linearGradient>
<linearGradient id="hill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7a8b4a"/><stop offset="1" stop-color="#4f6131"/></linearGradient></defs>
<ellipse cx="260" cy="398" rx="230" ry="14" fill="#000" opacity=".25"/>
<g transform="translate(14 30)">
<rect width="420" height="300" rx="14" fill="#fff"/>
<rect width="420" height="34" rx="14" fill="#efe7df"/><rect y="20" width="420" height="14" fill="#efe7df"/>
<circle cx="20" cy="17" r="5" fill="#e0675a"/><circle cx="36" cy="17" r="5" fill="#e8b84c"/><circle cx="52" cy="17" r="5" fill="#69b36a"/>
<rect x="80" y="10" width="250" height="14" rx="7" fill="#fff"/>
<rect x="0" y="34" width="420" height="150" fill="url(#sky)"/>
<path d="M0 150c60-40 120-30 180-8s120 10 240-30v72H0z" fill="url(#hill)"/>
<g stroke="#3d4d24" stroke-width="2" opacity=".6"><path d="M20 172l60-14M40 180l70-16M70 184l80-18M240 168l80-24M260 176l90-26"/></g>
<text x="26" y="88" font-family="Schibsted Grotesk,sans-serif" font-weight="800" font-size="26" fill="#5c1426">Vini dell'Oltrepò</text>
<rect x="26" y="102" width="112" height="26" rx="6" fill="#2a55e6"/><text x="38" y="120" font-family="Inter,sans-serif" font-size="12" font-weight="600" fill="#fff">Visita la cantina</text>
<g transform="translate(24 200)" font-family="Inter,sans-serif">
<rect width="118" height="80" rx="8" fill="#f5f0ea"/><rect x="132" width="118" height="80" rx="8" fill="#f5f0ea"/><rect x="264" width="118" height="80" rx="8" fill="#f5f0ea"/>
<rect x="48" y="10" width="20" height="50" rx="6" fill="#5c1426"/><rect x="180" y="10" width="20" height="50" rx="6" fill="#c9a24a"/><rect x="312" y="10" width="20" height="50" rx="6" fill="#8b2a3d"/>
<text x="30" y="74" font-size="10" fill="#4a3f4c">Pinot Nero</text><text x="160" y="74" font-size="10" fill="#4a3f4c">Metodo Classico</text><text x="292" y="74" font-size="10" fill="#4a3f4c">Bonarda</text></g>
</g>
<g transform="translate(380 128)">
<rect width="134" height="262" rx="22" fill="#1d1620"/>
<rect x="8" y="10" width="118" height="242" rx="16" fill="#fff"/>
<rect x="8" y="10" width="118" height="96" rx="16" fill="url(#sky)"/><rect x="8" y="80" width="118" height="26" fill="url(#hill)"/>
<text x="18" y="50" font-family="Schibsted Grotesk,sans-serif" font-weight="800" font-size="13" fill="#5c1426">Vini</text><text x="18" y="66" font-family="Schibsted Grotesk,sans-serif" font-weight="800" font-size="13" fill="#5c1426">dell'Oltrepò</text>
<rect x="18" y="118" width="98" height="30" rx="8" fill="#2a55e6"/><text x="36" y="137" font-family="Inter,sans-serif" font-size="10" font-weight="600" fill="#fff">Chiama la cantina</text>
<rect x="18" y="158" width="98" height="10" rx="5" fill="#e6ddd3"/><rect x="18" y="176" width="74" height="10" rx="5" fill="#e6ddd3"/><rect x="18" y="194" width="88" height="10" rx="5" fill="#e6ddd3"/>
<rect x="18" y="214" width="98" height="26" rx="8" fill="#f5f0ea"/>
</g></svg>"""

NAV = [("Siti web", "/siti-web/"), ("Cantine", "/siti-web-cantine/"), ("Ristoranti", "/siti-web-ristoranti/"), ("Social", "/social-media/"), ("SEO", "/seo/"),
       ("Portfolio", "/portfolio/"), ("Metodo", "/metodo/"), ("Raccontaci il progetto", "/contatti/")]

def ctas(serv):
    return f'<div class="ctas"><a class="btn b1" href="/contatti/?servizio={serv.replace(" ", "+")}#richiesta">Raccontaci il progetto</a><a class="btn b2" href="/portfolio/">Guarda i lavori</a></div>'

ORG = {"@type": "ProfessionalService", "@id": f"https://{D}/#org", "name": "Pangea Studio", "url": f"https://{D}/",
       "description": "Siti web, SEO, social media e fotografia per aziende, cantine e ristoranti.",
       "telephone": "+39 0385 320302", "email": P["email"], "logo": f"https://{D}/brand/logo-ufficiale-20261110.png",
       "address": {"@type": "PostalAddress", "streetAddress": P["via"], "postalCode": P["cap"], "addressLocality": P["citta"], "addressRegion": P["prov"], "addressCountry": "IT"},
       "parentOrganization": {"@type": "Organization", "name": "Pangea Comunicazione", "url": "https://www.pangeacomunicazione.it/"},
       "sameAs": ["https://www.instagram.com/pangeastudio_official/"], "areaServed": ["Oltrepò Pavese", "Provincia di Pavia"]}

def service(name, path, desc):
    return {"@type": "Service", "name": name, "serviceType": name, "description": desc, "url": f"https://{D}{path}", "provider": {"@id": f"https://{D}/#org"}, "areaServed": "Provincia di Pavia"}

CTABAND = f"""<section class="ctaband band"><div class="wrap"><div><h2>Raccontaci cosa vuoi migliorare</h2>
<p>Bastano l’indirizzo del sito attuale (se c’è), i servizi su cui puntare e la zona in cui lavori. Ti rispondiamo con le attività da fare e un preventivo su misura.</p>
<div class="ctas"><a class="btn b1" href="/contatti/#richiesta">Raccontaci il progetto</a><a class="btn b2" href="{P['wa']}" rel="noopener">WhatsApp</a></div></div>
<div class="contact">Telefono <a href="tel:{P['tel_href']}">{P['tel']}</a><br>Email <a href="mailto:{P['email']}">{P['email']}</a><br>Studio: {P['via']}, {P['cap']} {P['citta']} ({P['prov']})</div></div></section>"""

FOOTER = f"""<footer><div class="wrap"><div class="cols">
<div><h2>Pangea Studio</h2><p>Siti web, SEO, social e fotografia. Lo studio digitale di Pangea Comunicazione, in Oltrepò Pavese.</p></div>
<div><h2>Servizi</h2><ul><li><a href="/siti-web/">Siti web e restyling</a></li><li><a href="/siti-web-cantine/">Siti per cantine</a></li><li><a href="/siti-web-ristoranti/">Siti per ristoranti</a></li><li><a href="/seo/">SEO</a></li><li><a href="/social-media/">Social media</a></li><li><a href="/fotografia/">Fotografia</a></li><li><a href="/fotografia-vino/">Fotografia vino</a></li><li><a href="/fotografia-food-etika/">Fotografia food</a></li><li><a href="/fotografia-prodotti/">Fotografia prodotti</a></li></ul></div>
<div><h2>Contatti</h2><ul><li><a href="tel:{P['tel_href']}">{P['tel']}</a></li><li><a href="mailto:{P['email']}">{P['email']}</a></li><li><a href="{P['wa']}" rel="noopener">WhatsApp</a></li><li>{P['via']}, {P['cap']} {P['citta']} ({P['prov']})</li><li><a href="https://www.instagram.com/pangeastudio_official/">Instagram</a></li></ul></div>
<div><h2>Gruppo Pangea</h2><ul><li><a href="https://www.pangeacomunicazione.it/">Pangea Comunicazione</a> · stampa e insegne</li><li><a href="https://insegneinlegno.com/">Insegne in Legno</a></li><li><a href="https://progettilaser.it/">Progetti Laser</a> · incisione laser</li></ul></div>
</div><div class="legal">© 2026 {P['ragione']} · P. IVA {P['piva']} · <a href="/privacy-policy/">Privacy e cookie</a></div></div></footer>"""

S = Site("pangeastudio", D, "Pangea Studio", NAV, CSS, [("Schibsted Grotesk", "schibsted-grotesk", [700, 800]), ("Inter", "inter", [400, 600])], FOOTER, "/brand/logo-ufficiale-20261110.png", ORG, CTABAND, keep_urls=open(__import__("os").path.join(__import__("os").path.dirname(__file__), "sitemap_attuale_studio.txt")).read().split())

# portfolio: (nome, settore, lavoro, dominio, immagine-locale-o-None, gruppo)
PF = [
    ("Cantine Monterosso", "Cantine e aziende vinicole", "Sito web", "cantinemonterosso.com", None, "cantine"),
    ("Belcredi Vini 1906", "Cantine e aziende vinicole", "Sito web", "belcredivini1906.com", None, "cantine"),
    ("Ca' Montebello", "Cantine e aziende vinicole", "Sito web", "camontebello.it", None, "cantine"),
    ("Massara Vini", "Cantine e aziende vinicole", "Sito web", "massaravini.it", None, "cantine"),
    ("Vigna Alta", "Cantine e aziende vinicole", "Sito web", "vignaalta.it", None, "cantine"),
    ("Shop Bosco Longhino", "E-commerce", "Sito e-commerce", "shop.boscolonghino.it", None, "cantine"),
    ("Trattoria Il Ceppo", "Ristorazione", "Sito web", "trattoriailceppo.it", None, "ospitalita"),
    ("Agricola Casa Garello", "Agriturismo e ospitalità", "Sito web", "agricolacasagarello.it", None, "ospitalita"),
    ("Verdi Cascina Vecchia", "Agriturismo e ospitalità", "Sito web", "verdicascinavecchia.it", None, "ospitalita"),
    ("Frutta Secca Distribuzione", "Aziende e distribuzione", "Sito web", "www.fruttaseccadistribuzione.it", "/portfolio/web-frutta-secca.webp", "aziende"),
    ("Steel Acciai", "Aziende e industria", "Sito web e brochure", "steelacciai.eu", "/portfolio/grafica-brochure-steel.webp", "aziende"),
    ("Mecap", "Aziende e industria", "Sito web", "mecap.it", None, "aziende"),
    ("Ecosoil Ambiente", "Ambiente e servizi tecnici", "Sito web", "ecosoil-ambiente.it", None, "aziende"),
    ("Costruzioni Edili Caputo", "Edilizia e impianti", "Sito web", "costruzioniedilicaputo.it", None, "aziende"),
    ("Termoclima Borghi", "Edilizia e impianti", "Sito web", "termoclimaborghi.it", None, "aziende"),
    ("Arredamenti Dossena", "Arredamento", "Sito web", "arredamentidossena.it", None, "aziende"),
    ("Luciano Brega", "Artigianato", "Sito web", "lucianobrega.it", None, "aziende"),
    ("Insegne in Legno", "Artigianato e comunicazione visiva", "Sito web", "insegneinlegno.com", None, "aziende"),
]

def pf_works(names=None, group=None):
    items = [x for x in PF if (names is None or x[0] in names) and (group is None or x[5] == group)]
    if names:
        items.sort(key=lambda x: names.index(x[0]))
    CASE = {"Frutta Secca Distribuzione": "/portfolio/frutta-secca-distribuzione/", "Insegne in Legno": "/portfolio/insegne-in-legno/"}
    out = []
    for n, sett, lav, dom, img, g in items:
        extra = f' · <a href="{CASE[n]}">Il progetto</a>' if n in CASE else ""
        out.append(dict(img=img or MS.format(dom), alt=f"Anteprima del sito {n}", title=n, text=f"{sett} · {lav}{extra}", href=f"https://{dom}/", cta="Visita il sito"))
    return '<div class="pf">' + works(out) + "</div>"

# ---------------- HOME ----------------
h_faq = [
    ("Quanto costa un sito?", "Dipende da pagine, contenuti, funzioni e obiettivi: facciamo sempre un preventivo su misura. I pacchetti Essenziale, Business e Performance sono il punto di partenza."),
    ("Posso tenere il mio dominio e il posizionamento attuale?", "Il dominio di solito si mantiene. In un rifacimento analizziamo le pagine che portano visite e prepariamo i reindirizzamenti, senza promettere posizioni su Google."),
    ("Fate anche le fotografie?", "Sì, con lo studio fotografico interno: prodotti, bottiglie, packaging e food. È un servizio quotato a parte."),
    ("Chi aggiorna il sito dopo la pubblicazione?", "Lo definiamo nel progetto: possiamo occuparci noi di manutenzione, backup, nuove pagine e miglioramenti SEO."),
]
S.page("/", "Siti web, restyling e campagne social in Oltrepò | Pangea Studio",
       "Siti web, restyling e campagne social per aziende, cantine e ristoranti dell’Oltrepò Pavese e della provincia di Pavia. 18 siti del portfolio da visitare.",
       "Siti web, restyling e campagne social per aziende, cantine e ristoranti dell’Oltrepò",
       "Siamo lo studio digitale di Pangea Comunicazione a Santa Maria della Versa (PV). Progettiamo e rifacciamo siti che spiegano bene cosa fai e portano richieste, li sosteniamo con campagne social mirate e SEO e, se serve, realizziamo le fotografie.",
       section("Un sito che lavora per te", '<div class="cols2"><p>Molte attività hanno un sito che non porta richieste: bello da vedere, ma difficile da trovare su Google e poco chiaro su cosa offre, dove e a chi. Il nostro lavoro parte da lì. Prima capiamo cosa vendi, a chi e in quale zona; poi costruiamo pagine che rispondono alle domande reali dei clienti e li portano a chiamarti, scriverti o chiedere un preventivo.</p><p>Il sito è il centro, ma non basta da solo. Lo colleghiamo a campagne social mirate su Facebook e Instagram, che portano le persone alle pagine giuste, e a un lavoro SEO misurato con Search Console. Quando servono immagini vere di prodotti, bottiglie o piatti, le realizziamo nel nostro studio fotografico.</p><p>Siamo in Oltrepò Pavese dal 2004 come Pangea Comunicazione: conosciamo cantine, ristoranti e aziende del territorio.</p></div>') +
       section("Servizi", cards([
           ("Siti web e restyling", "Siti aziendali, cataloghi e restyling che conservano le pagine già visibili su Google.", "/siti-web/"),
           ("Campagne social", "Piano editoriale, post, caroselli e campagne Facebook e Instagram che portano alle pagine giuste del sito.", "/social-media/"),
           ("SEO e Search Console", "Audit di indicizzazione, ricerche reali, SEO locale e controlli dopo ogni modifica.", "/seo/"),
           ("Fotografia a supporto", "Prodotti, vino, packaging e food quando il sito o la campagna ne hanno bisogno.", "/fotografia/"),
       ])) +
       section("Per chi lavoriamo", cards([
           ("Cantine", "Schede vini, storia e territorio, visite, contatti per distributori. Monterosso, Belcredi, Ca’ Montebello, Massara, Vigna Alta.", "/siti-web-cantine/", "Siti per cantine"),
           ("Ristoranti e agriturismi", "Menu, orari, indicazioni e prenotazioni facili da smartphone. Trattoria Il Ceppo, Casa Garello, Verdi Cascina Vecchia.", "/siti-web-ristoranti/", "Siti per ristoranti"),
           ("Aziende e artigiani", "Servizi, cataloghi, lavori reali e richiesta di preventivo. Steel Acciai, Mecap, Frutta Secca Distribuzione.", "/siti-web/", "Siti aziendali"),
       ]), alt=True) +
       section("Alcuni siti online", pf_works(["Cantine Monterosso", "Trattoria Il Ceppo", "Frutta Secca Distribuzione", "Belcredi Vini 1906", "Steel Acciai", "Agricola Casa Garello"]) + '<p style="margin-top:18px"><a href="/portfolio/">Tutti i progetti del portfolio →</a></p>') +
       section("Come lavoriamo", steps([
           ("Ascolto e obiettivi", "Attività, pubblico, servizi da promuovere e azioni da misurare."),
           ("Struttura, testi, grafica", "Navigazione, contenuti e stile pensati prima per lo smartphone."),
           ("Verifica e crescita", "Controlli prima della messa online, poi dati di Search Console per decidere i passi successivi."),
       ]) + '<p style="margin-top:18px"><a href="/metodo/">Il metodo in sette passaggi →</a></p>', alt=True) +
       section("Domande frequenti", faq(h_faq)),
       hero_img=("/portfolio/web-frutta-secca.webp", "Il sito Frutta Secca Distribuzione su più dispositivi, realizzato da Pangea Studio"), ctas=ctas("Sito web"),
       proof='<p class="proof">18 siti del portfolio online da visitare: cantine, ristoranti, agriturismi, industria ed edilizia.</p>',
       schema=[faq_schema(h_faq)])

# ---------------- SITI WEB ----------------
pk = '<div class="pk">' + "".join(f'<div class="card{" rec" if r else ""}"><h3>{t}</h3><p class="note">{who}</p><ul class="list">{"".join(f"<li>{x}</li>" for x in li)}</ul></div>' for t, who, li, r in [
    ("Essenziale", "Professionisti, artigiani, piccole attività", ["Struttura compatta e pagine essenziali", "Grafica su misura e versione mobile", "Modulo contatti e link social", "Testi essenziali e SEO tecnica di base", "Privacy, cookie, pubblicazione e assistenza iniziale"], False),
    ("Business · consigliato", "Aziende con più servizi", ["Pagine dedicate ai servizi", "Testi professionali e navigazione curata", "SEO tecnica e locale", "Modulo personalizzato e casi studio", "Dominio, hosting, redirect e manutenzione"], True),
    ("Performance", "Progetti che devono crescere nel tempo", ["Architettura completa e funzioni evolutive", "Strategia SEO e pagine dedicate", "Piano contenuti e casi studio", "Strumenti Google e monitoraggio", "Ottimizzazione e assistenza prioritaria"], False),
]) + '</div><p class="note" style="margin-top:14px">I pacchetti sono punti di partenza: il preventivo si costruisce su obiettivi, contenuti e funzioni.</p>'
sw_faq = [
    ("Quanto costa e quanto tempo serve?", "Dipende da pagine, contenuti e funzioni. Costi e tempi sono scritti nel preventivo, in base alla complessità e alla disponibilità dei materiali."),
    ("Rifate il sito senza perdere le visite?", "Partiamo dagli URL attuali e dalle pagine che portano visite, decidiamo cosa conservare e prepariamo i reindirizzamenti. Controlliamo navigazione e moduli prima del passaggio. Nessuno può garantire posizioni su Google."),
    ("Hosting, dominio, privacy e cookie sono inclusi?", "Dipende dal pacchetto e viene specificato nel preventivo."),
    ("Dopo il lancio?", "Manutenzione, aggiornamenti, nuove pagine, backup, hosting e miglioramenti SEO, secondo il servizio concordato."),
]
S.page("/siti-web/", "Siti web e restyling in provincia di Pavia | Pangea Studio",
       "Siti aziendali, cataloghi e siti per artigiani, ristoranti e cantine. Restyling che conserva le pagine indicizzate. Pacchetti Essenziale, Business, Performance.",
       "Realizzazione siti web e restyling per aziende",
       "Siti aziendali e cataloghi, siti per artigiani e professionisti, ristoranti e cantine: progettati per far capire subito cosa offri e portare il visitatore a contattarti.",
       section("Prima la struttura, poi la grafica", '<div class="cols2"><p>Un sito efficace nasce da una buona struttura: quali servizi meritano una pagina propria, quali domande deve trovare risolte chi arriva da Google, quale azione deve compiere alla fine. Per questo partiamo da un incontro sull’attività e sugli obiettivi, e solo dopo passiamo a grafica e testi.</p><p>Ogni pagina ha un titolo chiaro, testi specifici sul tuo lavoro, immagini reali e un contatto sempre raggiungibile da smartphone. Prima della pubblicazione controlliamo navigazione, moduli e collegamenti; dopo, verifichiamo in Search Console che Google legga correttamente le pagine.</p></div>') +
       section("Che sito ti serve", cards([
           ("Aziende e cataloghi online", "Catalogo prodotti, schede tecniche e contatto commerciale. Esempio: Frutta Secca Distribuzione."),
           ("Artigiani e professionisti", "Servizi, lavori reali, zona servita e richiesta di preventivo. Esempio: Insegne in Legno."),
           ("Ristoranti", "Menu, orari, posizione e prenotazione pensati per lo smartphone.", "/siti-web-ristoranti/"),
           ("Cantine", "Schede vini, visite in cantina e percorsi separati per clienti e distributori.", "/siti-web-cantine/"),
       ])) +
       section("Restyling di un sito esistente", '<div class="two"><div><ul class="list"><li>Partiamo dagli URL attuali e dalle pagine che portano visite</li><li>Decidiamo quali pagine conservare e quali reindirizzare</li><li>Controlliamo navigazione e moduli prima del passaggio</li><li>Dopo la pubblicazione verifichiamo le pagine in Search Console</li></ul></div><div><p>Un rifacimento fatto male azzera la visibilità costruita negli anni. Per questo il lavoro SEO parte prima della grafica: lo trovi descritto nella pagina <a href="/seo/">SEO</a>.</p></div></div>', alt=True) +
       section("Pacchetti", pk) +
       section("Domande frequenti", faq(sw_faq), alt=True),
       hero_img=("/portfolio/web-frutta-secca.webp", "Il sito Frutta Secca Distribuzione su più dispositivi, realizzato da Pangea Studio"), ctas=ctas("Sito web"), crumbs=[("Siti web", "/siti-web/")],
       schema=[service("Realizzazione siti web", "/siti-web/", "Siti aziendali, cataloghi e restyling con conservazione delle pagine indicizzate."), faq_schema(sw_faq)])

# ---------------- CANTINE ----------------
ca_faq = [
    ("Cosa serve per il preventivo?", "Il sito attuale se c’è, materiali aziendali (schede, etichette, foto), pubblico di riferimento, lingue e obiettivi."),
    ("Si può vendere il vino online?", "Sì, se serve: valutiamo funzioni di vendita e gestione in base al catalogo e a chi aggiornerà il sito. Un esempio è lo shop di Bosco Longhino."),
    ("Fate anche le foto delle bottiglie?", "Sì, con lo studio fotografico: bottiglie, astucci e dettagli del marchio, come nel lavoro per Ballabio."),
]
S.page("/siti-web-cantine/", "Siti web per cantine in Oltrepò | Pangea Studio",
       "Siti per cantine: schede vini, territorio, visite, contatti per distributori e vendita online. Portfolio: Monterosso, Belcredi, Ca’ Montebello, Vigna Alta.",
       "Siti web per cantine e aziende vinicole",
       "Lavoriamo in Oltrepò Pavese, tra le cantine. Realizziamo siti con schede dei vini verificate, storia e territorio, visite e contatti per clienti e distributori, e, se serve, con le fotografie del nostro studio.",
       section("Il sito come cantina aperta", '<div class="cols2"><p>Chi visita il sito di una cantina vuole capire chi siete, assaggiare il territorio attraverso le immagini e trovare in fretta i vini, le schede e il modo per contattarvi o venirvi a trovare. Un distributore cerca altre informazioni rispetto a un appassionato: per questo prevediamo percorsi distinti.</p><p>Abbiamo realizzato i siti di diverse cantine, da Cantine Monterosso a Belcredi Vini 1906, e conosciamo le esigenze tipiche: schede tecniche aggiornabili, versioni in lingua, visite e degustazioni, vendita online dove serve. Le fotografie di bottiglie e packaging possono essere realizzate nel nostro studio.</p></div>') +
       section("Cosa contiene un sito per cantina", cards([
           ("Schede dei vini", "Etichette, descrizioni e caratteristiche, verificate con la cantina prima della pubblicazione."),
           ("Storia e territorio", "Chi siete, dove sono le vigne, le referenze: il racconto che distingue la cantina."),
           ("Visite e degustazioni", "Informazioni e richiesta di visita, se previste."),
           ("Clienti e distributori", "Percorsi separati per chi compra una bottiglia e per chi vuole distribuire."),
           ("Lingue e vendita", "Versioni in lingua, catalogo aggiornabile e, se serve, vendita online."),
       ])) +
       section("Cantine che hanno scelto Pangea Studio", pf_works(group="cantine"), alt=True) +
       section("Domande frequenti", faq(ca_faq)),
       hero_img=("/photography/ballabio/packaging.webp", "Bottiglia Ballabio Farfalla Noir e astuccio, fotografia Pangea Studio"), ctas=ctas("Sito per cantina"), crumbs=[("Siti web", "/siti-web/"), ("Cantine", "/siti-web-cantine/")],
       schema=[service("Siti web per cantine", "/siti-web-cantine/", "Siti con schede vini, visite, contatti per distributori e vendita online."), faq_schema(ca_faq)])

# ---------------- RISTORANTI ----------------
ri_faq = [
    ("Cosa serve prima del preventivo?", "Menu, orari e contatti confermati; foto disponibili e identità del locale; i canali che usate davvero per richieste e prenotazioni; il sito attuale se c’è."),
    ("Si può aggiungere un sistema di prenotazione?", "Sì: colleghiamo i canali che già usate. Un sistema dedicato si valuta a parte, su funzioni e costi."),
    ("Chi aggiorna menu e orari?", "Lo definiamo nel progetto, prima della pubblicazione."),
]
S.page("/siti-web-ristoranti/", "Siti web per ristoranti e agriturismi | Pangea Studio",
       "Siti per ristoranti e agriturismi: menu, orari, indicazioni e prenotazioni facili da smartphone. Esempi: Trattoria Il Ceppo, Casa Garello.",
       "Siti web per ristoranti, trattorie e agriturismi",
       "Chi cerca un ristorante lo fa dal telefono e vuole quattro cose: menu, orari, dove siete e come prenotare. Le mettiamo in primo piano e, se serve, fotografiamo piatti e locale.",
       section("Pensato per chi cerca dal telefono", '<p class="lead2">Il sito di un ristorante si guarda quasi sempre dallo smartphone, spesso poco prima di decidere dove andare. Per questo mettiamo in primo piano menu, orari, posizione e prenotazione, con pagine leggere che si aprono subito. Il resto, la storia del locale, la cucina, gli eventi, viene dopo e serve a convincere chi è indeciso.</p>') +
       section("Cosa trovi nel sito", cards([
           ("Menu e proposte", "Sempre aggiornati e leggibili da smartphone."),
           ("Orari e indicazioni", "Indirizzo e indicazioni per arrivare, in evidenza."),
           ("Prenotazioni", "Telefono, WhatsApp, email e i canali di prenotazione che già usate."),
           ("Fotografia food", "Servizio a parte: piatti, sala e dettagli, come per A Tavola con Etika.", "/fotografia/"),
       ])) +
       section("Locali e agriturismi online", pf_works(group="ospitalita"), alt=True) +
       section("Domande frequenti", faq(ri_faq)),
       hero_img=("/photography/etika/brasato.webp", "Piatto fotografato per A Tavola con Etika"), ctas=ctas("Sito per ristorante"), crumbs=[("Siti web", "/siti-web/"), ("Ristoranti", "/siti-web-ristoranti/")],
       schema=[service("Siti web per ristoranti", "/siti-web-ristoranti/", "Siti con menu, orari, indicazioni e prenotazioni da smartphone."), faq_schema(ri_faq)])

# ---------------- SEO ----------------
seo_faq = [
    ("Posso partire dal mio sito attuale?", "Sì. L’audit indica quali pagine rivedere e quali interventi tecnici servono; se serve un restyling, quali indirizzi conservare e quali reindirizzare."),
    ("Cosa vi serve per iniziare?", "L’indirizzo del sito, i servizi prioritari e la zona servita. L’accesso in sola lettura a Google Search Console aiuta a ricostruire il punto di partenza."),
    ("Garantite la prima pagina su Google?", "No, e diffida di chi lo fa. Misuriamo impressioni, clic e richieste prima e dopo ogni intervento."),
    ("Come valutate i risultati?", "Dopo la pubblicazione controlliamo lo stato delle pagine e confrontiamo impressioni e clic nel tempo, insieme alle richieste ricevute."),
]
S.page("/seo/", "Consulenza SEO a Pavia e in Oltrepò | Pangea Studio",
       "Audit SEO con Search Console per attività in provincia di Pavia: indicizzazione, ricerche reali, SEO locale e interventi in ordine di priorità.",
       "Consulenza SEO per attività della provincia di Pavia",
       "Analizziamo come Google legge il tuo sito e quali pagine trovano i clienti, poi ti consegniamo una lista di interventi in ordine di priorità e i controlli da ripetere dopo ogni modifica.",
       section("Perché la SEO locale conta", '<div class="cols2"><p>Per un’attività che lavora in una zona precisa, farsi trovare da chi cerca il servizio nelle vicinanze vale più di qualsiasi visita generica. Significa avere pagine chiare per ogni servizio, informazioni coerenti su sede e area servita, e un sito che Google riesce a leggere senza errori.</p><p>Non promettiamo posizioni: nessuno può farlo seriamente. Lavoriamo sui dati reali di Search Console, interveniamo sulle pagine che hanno già impressioni e misuriamo prima e dopo, così sai cosa ha funzionato.</p></div>') +
       section("Cosa controlliamo", steps([
           ("Indicizzazione e struttura", "Pagine leggibili da Google, risposte del server, sitemap, canonical e redirect; errori, duplicati e pagine importanti difficili da raggiungere."),
           ("Ricerche e contenuti", "Con Search Console: ricerche, impressioni e clic; titoli, testi e collegamenti interni rivisti su ciò che le persone cercano."),
           ("Ricerca locale", "Sede, contatti e area servita descritti in modo coerente sul sito e, dove presenti, nelle schede aziendali."),
           ("Piano d’azione", "Cosa si sistema sul sito attuale e cosa richiede sviluppo, partendo da servizi e percorsi di contatto."),
           ("Verifica dopo la pubblicazione", "Stato delle pagine e confronto di impressioni e clic nel tempo."),
       ])) +
       section("Cosa ricevi", '<div class="two"><div><ul class="list"><li>Lista di interventi ordinata per priorità</li><li>Controlli da ripetere dopo le modifiche</li><li>Elenco delle attività da preventivare, sul sito attuale o su un nuovo progetto</li></ul></div><div><p>Lavoriamo per attività che servono una zona precisa: Oltrepò Pavese, Pavia e provincia. Per chi deve rifare il sito, l’audit è il primo passo per non perdere le visite già conquistate.</p><p><a href="/siti-web/">Restyling senza perdere visibilità →</a></p></div></div>', alt=True) +
       section("Domande frequenti", faq(seo_faq)),
       hero_img=("/portfolio/web-frutta-secca.webp", "Il sito Frutta Secca Distribuzione su più dispositivi, realizzato da Pangea Studio"), ctas=ctas("SEO"), crumbs=[("SEO", "/seo/")],
       schema=[service("Consulenza SEO", "/seo/", "Audit di indicizzazione, Search Console, contenuti e SEO locale."), faq_schema(seo_faq)])

# ---------------- SOCIAL ----------------
so_faq = [
    ("Devo aprire nuovi canali?", "Si parte dai canali già attivi, dal pubblico da raggiungere e dai materiali disponibili. Dove pubblicare e con che frequenza lo decidiamo insieme."),
    ("Chi approva i contenuti?", "Prima dell’avvio concordiamo chi fornisce i materiali, chi approva testi e immagini e come gestire gli aggiornamenti."),
    ("Il budget pubblicitario è compreso?", "No: il preventivo distingue la gestione dal budget delle campagne. Anche un servizio fotografico dedicato è indicato a parte."),
]
S.page("/social-media/", "Campagne social Facebook e Instagram | Pangea Studio",
       "Piano editoriale, post, caroselli, storie e campagne Facebook e Instagram collegati alle pagine del sito. Per aziende, cantine e ristoranti dell’Oltrepò Pavese.",
       "Campagne social mirate su Facebook e Instagram",
       "Contenuti costruiti su ciò che i tuoi clienti vogliono sapere, e collegati al sito: un prodotto rimanda alla sua scheda, un lavoro al portfolio, una promozione al modulo di contatto.",
       section("Campagne che portano al sito", '<div class="cols2"><p>Pubblicare tanto non basta: un post funziona quando risponde a una domanda dei clienti e porta a una pagina dove trovare la risposta e il contatto. Per questo costruiamo il piano editoriale partendo dai servizi su cui vuoi lavorare e dalle pagine del sito che li spiegano.</p><p>Per le campagne a pagamento definiamo prima obiettivo e pagina di arrivo, poi il contenuto. Il budget pubblicitario è separato dalla gestione e lo decidi tu.</p></div>') +
       section("Cosa comprende", cards([
           ("Piano editoriale", "Temi, frequenza, canali e approvazioni, partendo da domande dei clienti e servizi prioritari."),
           ("Testi, immagini e formati", "Post, caroselli e storie preparati sui materiali disponibili."),
           ("Campagne", "Obiettivo e pagina di arrivo definiti prima di spendere."),
           ("Collegamento al sito", "Ogni contenuto porta dove la persona trova la risposta e il contatto."),
       ])) +
       section("Domande frequenti", faq(so_faq), alt=True),
       hero_img=("/portfolio/grafica-brochure-steel.webp", "Materiale di comunicazione Steel Acciai realizzato da Pangea"), ctas=ctas("Social media"), crumbs=[("Social media", "/social-media/")],
       schema=[service("Gestione social media", "/social-media/", "Piano editoriale, contenuti e campagne Facebook e Instagram."), faq_schema(so_faq)])

# ---------------- FOTOGRAFIA ----------------
S.page("/fotografia/", "Fotografia di prodotto, vino e food | Pangea Studio",
       "Still life di prodotto, bottiglie e packaging, fotografia food per siti, cataloghi e social. Progetti: Ballabio, A Tavola con Etika.",
       "Fotografia di prodotto, vino e food",
       "A supporto di siti e campagne fotografiamo prodotti, bottiglie, packaging e piatti. Luci, sfondi e composizione si scelgono con te, sullo stile della tua attività.",
       section("Lavori fotografici", works([
           dict(img="/photography/ballabio/packaging.webp", alt="Bottiglia Ballabio Farfalla Noir e astuccio", tag="Foto originale", title="Ballabio · vino e packaging", text="Bottiglia, astuccio e dettagli del marchio.", href="/fotografia-vino/", cta="Il progetto"),
           dict(img="/photography/etika/brasato.webp", alt="Brasato fotografato per A Tavola con Etika", tag="Foto originale", title="A Tavola con Etika · food", text="Serie coordinata di piatti, usata anche nella grafica.", href="/fotografia-food-etika/", cta="Il progetto"),
           dict(img="/photography/ballabio/dettaglio-logo.webp", alt="Dettaglio del marchio Ballabio sulla confezione", tag="Foto originale", title="Fotografia di prodotto", text="Forma, materiali e dettagli, dallo scatto all’uso sul sito.", href="/fotografia-prodotti/", cta="Il servizio"),
           dict(img="/photography/dallo-scatto-alla-copertina.png", alt="Still life di frutta e proposta di copertina Naturalmente", tag="Proposta grafica", title="Dallo scatto alla copertina", text="Uno still life trasformato in copertina editoriale."),
       ])) +
       section("Come lavoriamo", steps([
           ("Prepariamo lo scatto", "Prodotti, quantità, stile e uso delle immagini."),
           ("Fotografiamo i dettagli", "Luce, composizione e resa delle superfici su ogni soggetto."),
           ("Consegniamo le immagini", "Selezionate e preparate nei formati per stampa e digitale."),
       ]), alt=True),
       hero_img=("/photography/ballabio/packaging.webp", "Bottiglia Ballabio Farfalla Noir e astuccio"), ctas=ctas("Fotografia"), crumbs=[("Fotografia", "/fotografia/")],
       schema=[service("Fotografia di prodotto e food", "/fotografia/", "Still life di prodotto, vino, packaging e food.")])

# ---------------- PORTFOLIO ----------------
S.page("/portfolio/", "Portfolio siti web e fotografia | Pangea Studio",
       "Siti web realizzati da Pangea Studio per cantine, ristoranti, agriturismi, industria ed edilizia, con link ai siti online, e progetti fotografici.",
       "Portfolio", "Siti veri, online, da visitare: è il modo migliore per capire come lavoriamo.",
       section("Cantine ed e-commerce del vino", pf_works(group="cantine")) +
       section("Ristoranti e ospitalità", pf_works(group="ospitalita"), alt=True) +
       section("Aziende, industria e artigiani", pf_works(group="aziende")),
       crumbs=[("Portfolio", "/portfolio/")], ctas=ctas("Sito web"), hero_img=("/portfolio/web-frutta-secca.webp", "Il sito Frutta Secca Distribuzione su più dispositivi, realizzato da Pangea Studio"))

# ---------------- METODO ----------------
S.page("/metodo/", "Il metodo di lavoro | Pangea Studio",
       "Sette passaggi dall’ascolto alla crescita: obiettivi, struttura e contenuti, grafica, sviluppo, verifica e pubblicazione, assistenza. Un referente diretto.",
       "Il nostro metodo", "Un referente diretto e sette passaggi chiari, con revisioni e approvazioni scritte nell’offerta.",
       section("Sette passaggi", steps([
           ("Ascolto e analisi", "Esigenze, materiali e informazioni sull’attività."),
           ("Obiettivi", "Pubblico, servizi da promuovere e azioni da misurare."),
           ("Struttura e contenuti", "Navigazione, testi e immagini di ogni pagina."),
           ("Progettazione grafica", "Stile, gerarchie e resa su desktop e smartphone."),
           ("Sviluppo e ottimizzazione", "Pagine, immagini e collegamenti ottimizzati."),
           ("Verifica e pubblicazione", "Navigazione, contatti e pagine controllati prima della messa online."),
           ("Assistenza e crescita", "Aggiornamenti e priorità successive decisi sui dati."),
       ])) +
       section("Cosa ti chiediamo", '<div class="two"><div><ul class="list"><li>Informazioni sulla tua attività e su cosa vuoi migliorare</li><li>Testi e immagini disponibili</li><li>Se vuoi, il sito attuale o un progetto di riferimento</li><li>Per un rifacimento, gli indirizzi da conservare</li></ul></div><div><h3>Dopo il lancio</h3><ul class="list"><li>Manutenzione tecnica e backup</li><li>Testi, immagini e nuove pagine</li><li>Hosting, dominio e controlli</li><li>Monitoraggio e SEO</li></ul></div></div>', alt=True),
       crumbs=[("Metodo", "/metodo/")], ctas=ctas("Sito web"))

# ---------------- CONTATTI ----------------
SERV = ["Sito web", "Sito per cantina", "Sito per ristorante", "SEO", "Social media", "Fotografia", "Altro"]
FORM = f"""<form class="f" id="richiesta" action="https://formsubmit.co/{P['email']}" method="POST">
<input type="hidden" name="_subject" value="Nuova richiesta · Pangea Studio">
<input type="hidden" name="_next" value="https://{D}/grazie/"><input type="hidden" name="_captcha" value="false"><input type="hidden" name="_template" value="table">
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="row"><label>Nome e cognome *<input name="nome" required autocomplete="name"></label><label>Attività<input name="attivita" autocomplete="organization"></label></div>
<div class="row"><label>Email *<input type="email" name="email" required autocomplete="email"></label><label>Telefono<input type="tel" name="telefono" autocomplete="tel"></label></div>
<div class="row"><label>Servizio<select name="servizio" data-pre="servizio">{''.join(f'<option>{c}</option>' for c in SERV)}</select></label><label>Sito attuale (se c’è)<input name="sito" type="text" inputmode="url" placeholder="www.tuosito.it"></label></div>
<label>Raccontaci il progetto *<textarea name="messaggio" required placeholder="Cosa fai, cosa vuoi migliorare, zona servita…"></textarea></label>
<label class="chk"><input type="checkbox" name="privacy" required value="accettata"><span>Ho letto l’<a href="/privacy-policy/">informativa privacy</a> e acconsento all’uso dei dati per rispondere alla richiesta. *</span></label>
<button class="btn b1" type="submit">Invia la richiesta</button><p class="msg" role="status"></p>
</form>"""
S.page("/contatti/", "Contatti | Pangea Studio, Santa Maria della Versa (PV)",
       "Contatta Pangea Studio: telefono 0385 320302, WhatsApp, email o modulo. Via XXV Aprile, 7, Santa Maria della Versa (PV).",
       "Contatti", f"Chiamaci allo {P['tel']}, scrivici su WhatsApp o raccontaci il progetto con il modulo: ti rispondiamo con le attività da fare e un preventivo.",
       section("Raccontaci il progetto", f'<div class="two"><div>{FORM}</div><div><h3>Recapiti</h3><p>Telefono <a href="tel:{P["tel_href"]}">{P["tel"]}</a><br>WhatsApp <a href="{P["wa"]}">{P["tel"]}</a><br>Email <a href="mailto:{P["email"]}">{P["email"]}</a></p><h3>Dove siamo</h3><p>{P["via"]}<br>{P["cap"]} {P["citta"]} ({P["prov"]})</p></div></div>', id="richiesta-box"),
       crumbs=[("Contatti", "/contatti/")])

S.page("/grazie/", "Richiesta inviata · Pangea Studio", "Richiesta ricevuta.", "Grazie, abbiamo ricevuto la richiesta",
       "Ti ricontattiamo per capire meglio il progetto. Nel frattempo puoi guardare i lavori del portfolio.", "", ctas='<div class="ctas"><a class="btn b1" href="/portfolio/">Vai al portfolio</a></div>', noindex=True)

PRIV = f"""<section class="band"><div class="wrap">
<h2>Titolare del trattamento</h2><p>{P['ragione']}, {P['via']}, {P['cap']} {P['citta']} ({P['prov']}), P. IVA {P['piva']}. Contatti: <a href="mailto:{P['email']}">{P['email']}</a>, {P['tel']}.</p>
<h2>Dati raccolti e finalità</h2><p>Con il modulo raccogliamo nome, contatti, attività, sito attuale e messaggio, solo per rispondere e preparare un preventivo. Base giuridica: misure precontrattuali richieste dall’interessato. Nessuna newsletter.</p>
<h2>Servizi di terze parti</h2><p>Il modulo è inoltrato tramite FormSubmit (formsubmit.co) alla nostra casella email. Il sito è ospitato da Hostinger (log tecnici del server). Le anteprime del portfolio sono caricate dal servizio mShots di WordPress.com, che riceve l’indirizzo IP del visitatore. Google Analytics 4 si attiva solo con il consenso alle statistiche; non usiamo cookie di profilazione pubblicitaria; i link a WhatsApp e Instagram aprono servizi con informative proprie.</p>
<h2>Conservazione e diritti</h2><p>Conserviamo la corrispondenza per il tempo necessario alla richiesta. Puoi chiedere accesso, rettifica, cancellazione, limitazione o opposizione scrivendo a {P['email']} e proporre reclamo al Garante privacy.</p>
<p class="note">Aggiornata il 24/11/2026 · testo da validare con il consulente privacy prima della pubblicazione.</p></div></section>"""
S.page("/privacy-policy/", "Privacy e cookie | Pangea Studio", "Informativa privacy e cookie di Pangea Studio: titolare, dati del modulo, servizi terzi, conservazione e diritti.", "Privacy e cookie", "Come trattiamo i dati inviati tramite il sito.", PRIV, crumbs=[("Privacy", "/privacy-policy/")])

if __name__ == "__main__":
    b = S.build()
    make_preview(b, S.key)
    print(b, len(S.pages))
