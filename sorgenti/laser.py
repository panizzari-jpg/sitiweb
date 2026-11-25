from core import *

D = "progettilaser.it"
I = "/images/"
P = PANGEA

CSS = """/* VOICE: laboratorio tecnico, preciso, industriale
IDEA: il piano di lavoro del laser: grafite, griglia di taglio, raggio
PICTURE: foto reali del laboratorio in trasparenza, linea di scansione animata
COLOUR/TYPE: grafite dominante, grigio acciaio di supporto, arancio laser (dal logo); Archivo
LAYOUT: hero fotografico compatto, bande bianche e grigie a griglia, chiusura grafite */
:root{--fh:'Archivo',system-ui,sans-serif;--fb:'Archivo',system-ui,sans-serif;
--bg:light-dark(#ffffff,#0f1215);--ink:light-dark(#1d2126,#e6e9ed);--head:light-dark(#101317,#f6f7f9);--mute:light-dark(#59616b,#a5adb7);
--sup:light-dark(#f2f4f6,#161a1f);--card:light-dark(#ffffff,#141820);--line:light-dark(#dde2e7,#2a3038);--line2:light-dark(#b4bcc6,#46505c);
--grid:light-dark(rgba(20,30,40,.045),rgba(255,255,255,.04));
--dom:#14181d;--dom2:#14181d;--ondom:#f3f5f7;--acc:#e8501f;--acc2:#c93f12;--onacc:#ffffff;--link:light-dark(#c2410c,#ff8a5c);
--foot:#0f1215;--onfoot:#d9dee4;--phbg:light-dark(#e8ebef,#1c2129);--phink:light-dark(#3b434d,#c9d0d8)}
:root[data-theme=light]{color-scheme:light}:root[data-theme=dark]{color-scheme:dark}
"""

HERO_SVG = """<svg viewBox="0 0 500 400" role="img" aria-label="Illustrazione: targhetta metallica con matricola e tavoletta in legno incisa al laser">
<defs>
<linearGradient id="st" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e9ecef"/><stop offset=".45" stop-color="#b9c0c7"/><stop offset=".55" stop-color="#d3d8dd"/><stop offset="1" stop-color="#9aa3ac"/></linearGradient>
<pattern id="br" width="4" height="4" patternUnits="userSpaceOnUse"><path d="M0 1h4" stroke="#fff" stroke-opacity=".18"/></pattern>
<linearGradient id="wd" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#d9b98c"/><stop offset=".5" stop-color="#e8cfa6"/><stop offset="1" stop-color="#cfa877"/></linearGradient>
<linearGradient id="bm" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff3b30" stop-opacity="0"/><stop offset="1" stop-color="#ff3b30"/></linearGradient>
<radialGradient id="gl"><stop offset="0" stop-color="#fff"/><stop offset=".3" stop-color="#ff5a4f"/><stop offset="1" stop-color="#ff3b30" stop-opacity="0"/></radialGradient>
</defs>
<ellipse cx="250" cy="372" rx="215" ry="16" fill="#000" opacity=".28"/>
<g transform="translate(70 196) rotate(-4)">
<rect width="330" height="150" rx="10" fill="#7a5130"/>
<rect y="-6" width="330" height="150" rx="10" fill="url(#wd)"/>
<g fill="none" stroke="#b8895a" stroke-opacity=".55" stroke-width="1.4"><path d="M0 22c80-8 160 10 330-2"/><path d="M0 58c90 10 190-12 330 4"/><path d="M0 98c110-10 200 12 330-4"/><path d="M0 126c70 6 180-8 330 2"/></g>
<g fill="#4a2c17"><text x="30" y="62" font-family="Archivo,sans-serif" font-weight="800" font-size="30">Cantina</text><text x="30" y="96" font-family="Archivo,sans-serif" font-size="16" letter-spacing="1">dal 1906 · Oltrepò</text></g>
<g stroke="#4a2c17" stroke-width="2.2" fill="none"><path d="M262 40c-14 18-14 40 0 58c14-18 14-40 0-58z"/><path d="M262 98v22"/></g>
</g>
<g transform="translate(132 52) rotate(3)">
<rect width="300" height="170" rx="12" fill="#6d7680"/>
<rect y="-6" width="300" height="170" rx="12" fill="url(#st)"/>
<rect y="-6" width="300" height="170" rx="12" fill="url(#br)"/>
<g fill="#59626b"><circle cx="16" cy="10" r="6"/><circle cx="284" cy="10" r="6"/><circle cx="16" cy="148" r="6"/><circle cx="284" cy="148" r="6"/></g>
<g font-family="Archivo,sans-serif" fill="#2a3036">
<text x="30" y="40" font-weight="800" font-size="20">MACCHINA TIPO A</text>
<text x="30" y="70" font-size="15">Modello</text><text x="110" y="70" font-size="15" font-weight="600">A-200</text>
<text x="30" y="96" font-size="15">Matricola</text><text x="110" y="96" font-size="15" font-weight="600">0001</text>
<text x="30" y="122" font-size="15">Anno</text><text x="110" y="122" font-size="15" font-weight="600">2026</text>
</g>
<g transform="translate(206 52)" fill="#2a3036"><rect width="68" height="68" fill="none" stroke="#2a3036" stroke-width="3"/>
<rect x="8" y="8" width="16" height="16"/><rect x="44" y="8" width="16" height="16"/><rect x="8" y="44" width="16" height="16"/>
<rect x="30" y="30" width="7" height="7"/><rect x="44" y="34" width="7" height="7"/><rect x="34" y="46" width="7" height="7"/><rect x="50" y="50" width="10" height="10"/><rect x="30" y="12" width="7" height="7"/></g>
</g>
<rect x="404" y="0" width="5" height="292" fill="url(#bm)"/>
<circle cx="406.5" cy="294" r="16" fill="url(#gl)"/>
</svg>"""

NAV = [("Aziende", "/targhette-industriali-laser/"), ("Locali", "/ristorazione-accoglienza/"), ("Cantine", "/cassette-legno-personalizzate/"),
       ("Regali", "/nomi-regali-personalizzati/"), ("Realizzazioni", "/realizzazioni/"), ("Come lavoriamo", "/come-lavoriamo/"), ("Chiedi un preventivo", "/preventivo/")]

def pv(cat):
    return f'/preventivo/?progetto={cat.replace(" ", "+")}'

def ctas(cat):
    return f'<div class="ctas"><a class="btn b1" href="{pv(cat)}">Chiedi un preventivo</a><a class="btn b2" href="{P["wa"]}" rel="noopener">Scrivici su WhatsApp</a></div>'

ORG = {"@type": "LocalBusiness", "@id": f"https://{D}/#org", "name": "Progetti Laser", "url": f"https://{D}/",
       "description": "Laboratorio di incisione, taglio e marcatura laser su legno, metallo, acrilico, vetro e ardesia.",
       "telephone": "+39 0385 320302", "email": P["email"], "logo": f"https://{D}/brand/logo-ufficiale-20261110.png",
       "address": {"@type": "PostalAddress", "streetAddress": P["via"], "postalCode": P["cap"], "addressLocality": P["citta"], "addressRegion": P["prov"], "addressCountry": "IT"},
       "parentOrganization": {"@type": "Organization", "name": "Pangea Comunicazione", "url": "https://www.pangeacomunicazione.it/"},
       "areaServed": "Oltrepò Pavese"}

def service(name, path, desc):
    return {"@type": "Service", "name": name, "serviceType": name, "description": desc, "url": f"https://{D}{path}", "provider": {"@id": f"https://{D}/#org"}}

CTABAND = f"""<section class="ctaband band"><div class="wrap"><div><h2>Hai un oggetto, un logo o una serie da personalizzare?</h2>
<p>Mandaci una foto del pezzo, le misure, la quantità e il file grafico. Verifichiamo materiale e area lavorabile prima di confermare il preventivo.</p>
<div class="ctas"><a class="btn b1" href="/preventivo/">Chiedi un preventivo</a><a class="btn b2" href="{P['wa']}" rel="noopener">WhatsApp</a></div></div>
<div class="contact">Telefono <a href="tel:{P['tel_href']}">{P['tel']}</a><br>Email <a href="mailto:{P['email']}">{P['email']}</a><br>Laboratorio: {P['via']}, {P['cap']} {P['citta']} ({P['prov']})</div></div></section>"""

FOOTER = f"""<footer><div class="wrap"><div class="cols">
<div><h2>Progetti Laser</h2><p>Incisione, taglio e marcatura laser. Un marchio di Pangea Comunicazione, Oltrepò Pavese.</p></div>
<div><h2>Lavorazioni</h2><ul><li><a href="/targhette-industriali-laser/">Targhette con matricola</a></li><li><a href="/marcatura-acciaio/">Marcatura acciaio</a></li><li><a href="/gadget-aziendali-personalizzati/">Gadget aziendali</a></li><li><a href="/ristorazione-accoglienza/">Ristoranti e locali</a></li><li><a href="/cassette-legno-personalizzate/">Cassette in legno</a></li><li><a href="/taglieri-personalizzati/">Taglieri</a></li><li><a href="/incisione-vetro-personalizzata/">Incisione su vetro</a></li><li><a href="/nomi-regali-personalizzati/">Nomi e regali</a></li></ul></div>
<div><h2>Altre idee</h2><ul><li><a href="/sagome-decorazioni-legno/">Sagome e decorazioni</a></li><li><a href="/premi-personalizzati/">Premi e riconoscimenti</a></li><li><a href="/confezioni-natale-aziende/">Natale per aziende</a></li><li><a href="/targhe-pannelli-legno/">Targhe e pannelli</a></li><li><a href="/cerimonie-matrimoni-personalizzati/">Cerimonie e matrimoni</a></li><li><a href="/oggetti-personalizzati-3d/">Oggetti in stampa 3D</a></li><li><a href="/novita-e-lavorazioni/">Novità</a></li></ul></div>
<div><h2>Contatti</h2><ul><li><a href="tel:{P['tel_href']}">{P['tel']}</a></li><li><a href="mailto:{P['email']}">{P['email']}</a></li><li><a href="{P['wa']}" rel="noopener">WhatsApp</a></li><li>{P['via']}, {P['cap']} {P['citta']} ({P['prov']})</li></ul></div>
<div><h2>Gruppo Pangea</h2><ul><li><a href="https://www.pangeacomunicazione.it/">Pangea Comunicazione</a> · stampa, adesivi, abbigliamento</li><li><a href="https://insegneinlegno.com/">Insegne in Legno</a></li><li><a href="https://pangeastudio.it/">Pangea Studio</a> · siti e fotografia</li></ul></div>
</div><div class="legal">© 2026 {P['ragione']} · P. IVA {P['piva']} · <a href="/privacy/">Privacy</a> · <a href="/cookie/">Cookie</a></div></div></footer>"""

S = Site("progettilaser", D, "Progetti Laser", NAV, CSS, [("Archivo", "archivo", [400, 600, 800])], FOOTER, "/brand/logo-ufficiale-20261110.png", ORG, CTABAND, keep_urls=[])

S.scan = True
# ---------------- HOME ----------------
home_faq = [
    ("Potete lavorare un oggetto che ho già?", "Sì. Inviaci foto, misure e materiale del pezzo insieme al disegno. Verifichiamo superficie, finitura e area accessibile prima di confermare."),
    ("Che file grafico serve?", "Il logo o il testo definitivo, meglio in formato vettoriale (SVG, PDF, AI, EPS o DXF). Se hai solo un’immagine, la valutiamo e ti diciamo se va ricostruita prima dell’incisione."),
    ("Fate pezzi singoli e serie con dati diversi?", "Sì: da un regalo con un nome a serie in cui ogni pezzo ha un testo, un numero o una matricola diversa, partendo da un elenco definitivo controllato insieme."),
    ("Quanto costa e in quanto tempo?", "Dipende da materiale, dimensioni, quantità e preparazione del file. Non pubblichiamo un listino: il preventivo indica costi e tempi per il tuo lavoro."),
]
S.page("/", "Incisione laser su legno, metallo e vetro | Progetti Laser",
       "Laboratorio laser in Oltrepò Pavese: targhette con matricola, marcatura acciaio, articoli per ristoranti e cantine, gadget aziendali e regali personalizzati.",
       "Incisione e marcatura laser su legno, metallo, vetro e ardesia",
       "Laboratorio a Santa Maria della Versa (PV), in Oltrepò Pavese. Personalizziamo targhette con matricola, utensili in acciaio, articoli per locali e cantine, gadget aziendali e regali: pezzo singolo o serie, con verifica del file prima della produzione.",
       section("Un laboratorio, non un catalogo", '<div class="cols2"><p>Progetti Laser è il laboratorio di incisione e taglio laser di Pangea Comunicazione, in Oltrepò Pavese. Non vendiamo oggetti da catalogo con un logo appoggiato sopra: partiamo dal tuo pezzo, dal tuo marchio e dall’uso che ne farai, e scegliamo materiale, area e tipo di lavorazione per ottenere un risultato leggibile e durevole.</p><p>Lavoriamo sia il pezzo unico sia la serie, anche con dati diversi su ogni pezzo: matricole, numeri di tavolo, nomi dei destinatari. Prima di produrre controlliamo il file e ti mandiamo una bozza da approvare, così sai esattamente cosa riceverai.</p><p>Per aziende e locali questo significa un solo interlocutore anche per il resto della comunicazione: insegne con <a href="https://insegneinlegno.com/">Insegne in Legno</a>, stampa, adesivi e abbigliamento con <a href="https://www.pangeacomunicazione.it/">Pangea Comunicazione</a>, sito e social con <a href="https://pangeastudio.it/">Pangea Studio</a>.</p></div>') +
       section("Cosa ti serve?", cards([
           ("Targhette per macchinari", "Logo, modello, matricola, numero di serie e QR su plastica o metallo, con dati diversi per ogni pezzo.", "/targhette-industriali-laser/"),
           ("Marcatura su acciaio", "Coltelli e utensili con logo, nome o matricola: marcatura piena, a contorno o a due tonalità.", "/marcatura-acciaio/"),
           ("Ristoranti e locali", "QR code da tavolo, segnatavolo, menu, sottobicchieri in legno e ardesia con il marchio del locale.", "/ristorazione-accoglienza/"),
           ("Cantine e regali aziendali", "Cassette in legno per bottiglie con marchio o dedica per ogni destinatario, anche per Natale.", "/cassette-legno-personalizzate/"),
           ("Gadget aziendali", "Portachiavi in legno, taccuini e oggetti con logo per eventi, anniversari e clienti.", "/gadget-aziendali-personalizzati/"),
           ("Nomi e regali", "Nomi sagomati, targhe per cameretta, battesimi e ricorrenze in legno e plexiglass.", "/nomi-regali-personalizzati/"),
       ])) +
       section("Materiali che lavoriamo", '<div class="two"><div><ul class="list"><li><b>Legno</b>: incisione che fa risaltare la venatura; taglio di sagome, lettere e incastri.</li><li><b>Metallo e acciaio</b>: marcatura di loghi, testi, matricole e QR.</li><li><b>Acrilico e plexiglass</b>: finiture trasparenti o colorate, da valutare progetto per progetto.</li><li><b>Vetro</b>: bottiglie e oggetti, con decori leggibili in controluce.</li><li><b>Ardesia</b>: lastre e sottobicchieri con marchio o grafica.</li></ul></div><div><p>Il risultato dipende dal materiale, dalla finitura e dalla forma del pezzo: per questo ogni lavoro parte da una verifica su foto e misure.</p><p>Per oggetti ed espositori su misura lavoriamo anche con la <a href="/oggetti-personalizzati-3d/">stampa 3D</a>.</p><p class="note">L’incisione personalizza l’oggetto ma non ne certifica l’idoneità alimentare o normativa: quella dipende dal prodotto di partenza.</p></div></div>', alt=True) +
       section("Lavori reali dal laboratorio", works([
           dict(img=I + "targhette-incise-laser-serie-genoface.webp", alt="Targhette in serie con logo Genoface incise al laser nel laboratorio Progetti Laser", tag="Foto originale", title="Genoface", text="Targhette incise e tagliate per apparecchiature estetiche, in serie.", href="/targhette-industriali-laser/", cta="Targhette per macchinari"),
           dict(img=I + "sottobicchieri-ardesia-incisi-laser-resto-vintage.webp", alt="Sottobicchieri quadrati in ardesia incisi al laser con il logo di The Resto Vintage", tag="Foto originale", title="The Resto Vintage", text="Sottobicchieri in ardesia con grafica vintage del locale.", href="/ristorazione-accoglienza/", cta="Articoli per locali"),
           dict(img=I + "targa-metallo-incisa-laser-fbc-casteggio.webp", alt="Targa a scudo in metallo incisa e tagliata al laser per FBC Casteggio 1898", tag="Foto originale", title="FBC Casteggio 1898", text="Targa a scudo per la società sportiva, con aquila dorata e stella.", href="/realizzazioni/", cta="Tutte le realizzazioni"),
           dict(img=I + "taccuino-personalizzato-logo-inciso-bioenol.webp", alt="Taccuino in cartone riciclato con logo Bioenol inciso al laser e penna coordinata", tag="Foto originale", title="Bioenol", text="Taccuino personalizzato con penna coordinata.", href="/gadget-aziendali-personalizzati/", cta="Gadget aziendali"),
       ]) + '<p style="margin-top:18px"><a href="/realizzazioni/">Vedi tutte le realizzazioni →</a></p>') +
       section("Come funziona", steps([
           ("Ci mandi i dati", "Foto del pezzo o del materiale, misure, quantità e file del logo o del testo."),
           ("Verifichiamo e quotiamo", "Controlliamo materiale, area lavorabile e file; il preventivo indica lavorazione, costi e tempi."),
           ("Approvi e produciamo", "Confermi bozza e testi definitivi, poi incidiamo, tagliamo o marchiamo i pezzi."),
       ]) + '<p style="margin-top:18px"><a href="/come-lavoriamo/">Il metodo completo e come preparare i file →</a></p>', alt=True) +
       section("Domande frequenti", faq(home_faq)),
       hero_img=(I+"incisione-laser-tagliere-legno-logo-casaia.webp", "Incisione laser su un tagliere in legno nel laboratorio Progetti Laser"), ctas=ctas("Generico"),
       proof='<p class="proof">Lavori per aziende, locali, cantine e privati: Genoface, Il Reuccio delle Porchette, Trattoria Il Ceppo, Sparkling World, Distilleria Gualco, FBC Casteggio 1898.</p>',
       schema=[faq_schema(home_faq)])

# ---------------- TARGHETTE ----------------
t_faq = [
    ("Ogni targhetta può avere una matricola diversa?", "Sì. Prepariamo i dati variabili (matricola, numero di serie, codice, QR) da un elenco che ci fornisci e che controlliamo prima della produzione."),
    ("Su quali materiali?", "Plastica e metallo. Spessore, finitura e fissaggio si scelgono in base al macchinario e all’ambiente di utilizzo."),
    ("Le targhette sono certificate?", "No. Incidiamo i contenuti che ci fornisci: le informazioni richieste da norme e marcature restano a cura del costruttore."),
    ("Posso inviarvi un disegno tecnico?", "Sì: misure, posizione dei fori e testi definitivi in PDF, DXF o SVG accelerano la verifica."),
]
S.page("/targhette-industriali-laser/", "Targhette industriali con matricola al laser | Progetti Laser",
       "Targhette per macchinari incise al laser su plastica e metallo: logo, modello, matricola, numero di serie, codice e QR, con dati variabili per ogni pezzo.",
       "Targhette industriali incise al laser con matricola e dati variabili",
       "Per costruttori e officine che devono identificare macchinari e apparecchiature: incidiamo logo, modello, matricola, numero di serie, codici e QR su targhette in plastica o metallo, con dati diversi per ogni pezzo.",
       section("Quando servono", '<div class="cols2"><p>Una targhetta identificativa accompagna la macchina per tutta la sua vita: in officina, durante l’assistenza, nei controlli. Deve restare leggibile e riportare dati corretti, pezzo per pezzo. Per questo lavoriamo partendo dal tuo elenco di matricole e da un layout approvato, e incidiamo invece di stampare.</p><p>È la soluzione tipica per costruttori di macchinari e apparecchiature, officine che producono piccole serie, aziende che devono identificare attrezzature o ricambi, e per chi vuole un QR che porti al manuale o all’assistenza.</p></div>') +
       section("Cosa possiamo incidere", '<div class="two"><div><ul class="list"><li>Logo e ragione sociale del costruttore</li><li>Modello, matricola e numero di serie</li><li>Codici prodotto e anno</li><li>QR code verso manuale, scheda o assistenza</li><li>Dati variabili diversi per ogni targhetta della serie</li></ul></div><div><p>Partiamo dal tuo layout o lo impaginiamo noi sulla base dei testi definitivi. Prima della produzione ricevi una bozza da approvare con i dati di un campione.</p><p class="note">Le informazioni normative vanno fornite dal cliente: l’incisione non sostituisce certificazioni o marcature obbligatorie.</p></div></div>') +
       section("Lavori realizzati", works([
           dict(img=I + "targhette-incise-laser-serie-genoface.webp", alt="Targhette identificative Genoface incise al laser in serie per apparecchiature", tag="Foto originale", title="Genoface", text="Targhette incise e tagliate al laser per apparecchiature estetiche e industriali.", href="/lavori/genoface-personalizzazione-serie/"),
           dict(img=I + "marcatura-laser-qr-code-acciaio.webp", alt="QR code marcati al laser su lamiera di acciaio per targhette identificative", tag="Foto originale", title="QR code incisi", text="QR marcati al laser per targhette identificative e menu.", href="/lavori/qr-code-marcatura-laser/"),
       ]), alt=True) +
       section("Cosa ci serve per il preventivo", '<ul class="list"><li>Misure della targhetta e posizione di eventuali fori</li><li>Materiale preferito (plastica o metallo) e ambiente di utilizzo</li><li>Testi fissi e file del logo</li><li>Elenco dei dati variabili e quantità</li></ul><p>Per marcature direttamente su componenti in acciaio vedi <a href="/marcatura-acciaio/">marcatura laser su acciaio</a>.</p>') +
       section("Domande frequenti", faq(t_faq), alt=True),
       hero_img=(I+"targhette-incise-laser-serie-genoface.webp","Genoface · targhette incise e tagliate al laser"), ctas=ctas("Targhette industriali"), crumbs=[("Targhette industriali", "/targhette-industriali-laser/")],
       schema=[service("Targhette industriali incise al laser", "/targhette-industriali-laser/", "Targhette in plastica e metallo con matricola, numero di serie, codici e QR."), faq_schema(t_faq)])

# ---------------- ACCIAIO ----------------
a_faq = [
    ("Che differenza c’è tra marcatura piena e a contorno?", "La marcatura piena riempie lettere e forme del logo; quella a contorno traccia solo il profilo e lascia visibile l’acciaio all’interno del marchio."),
    ("Cos’è la marcatura a due tonalità?", "Due toni affiancati mettono in risalto parti diverse del disegno, ad esempio marchio e scritta."),
    ("Cosa devo inviare?", "Una foto del pezzo, l’area da marcare con le misure, la quantità e il file del logo, del testo o della matricola."),
]
S.page("/marcatura-acciaio/", "Marcatura laser su acciaio e coltelli | Progetti Laser",
       "Marcatura laser su acciaio: coltelli e utensili con logo, nome o matricola. Finitura piena, a contorno o bicolore. Preventivo da foto e misure.",
       "Marcatura laser su acciaio: coltelli, utensili e componenti",
       "Personalizziamo coltelli e utensili in acciaio con logo, nomi o numeri di serie, per aziende, macellerie, ristoranti e regali. Scegli tra marcatura piena, a contorno o a due tonalità.",
       section("Il marchio su ciò che si usa ogni giorno", '<div class="cols2"><p>Un coltello o un utensile marcato con il logo resta in mano a chi lavora per anni: è un modo concreto di firmare la propria attrezzatura o di fare un regalo che non finisce in un cassetto. La marcatura laser lavora direttamente l’acciaio, senza adesivi o vernici che si consumano.</p><p>Ci rivolgiamo a macellerie, ristoranti e laboratori alimentari, coltellerie e rivenditori, aziende che regalano strumenti di lavoro personalizzati. Per pezzi in serie possiamo inserire anche nomi o numeri diversi su ogni pezzo.</p></div>') +
       section("Tre finiture", cards([
           ("Piena", "Riempie lettere e forme: il marchio si legge con decisione sulla lama o sul manico."),
           ("A contorno", "Traccia solo il profilo: l’acciaio resta visibile all’interno del marchio."),
           ("Due tonalità", "Toni affiancati distinguono parti diverse del disegno, per esempio simbolo e nome."),
       ])) +
       section("Esempi", works([
           dict(img=I + "marcatura-laser-coltello-acciaio-logo.webp", alt="Coltello in acciaio con logo marcato al laser: confronto tra marcatura piena e a contorno", tag="Immagine del post", title="Piena e a contorno", text="Lo stesso marchio su coltelli con le due finiture a confronto."),
           dict(img=I + "marcatura-laser-bicolore-acciaio-spazzolato.webp", alt="Marcatura laser bicolore su acciaio spazzolato con logo Il Reuccio delle Porchette", tag="Immagine del post", title="Bicolore su acciaio spazzolato", text="Due tonalità per separare le parti del disegno.", href="/lavori/marcatura-bicolore-acciaio/"),
       ]), alt=True) +
       section("Domande frequenti", faq(a_faq) + '<p style="margin-top:18px">Per targhette con matricola vedi <a href="/targhette-industriali-laser/">targhette industriali</a>.</p>'),
       hero_img=(I+"marcatura-laser-coltello-acciaio-logo.webp","Coltelli in acciaio con marcatura piena e a contorno"), ctas=ctas("Marcatura acciaio"), crumbs=[("Marcatura acciaio", "/marcatura-acciaio/")],
       schema=[service("Marcatura laser su acciaio", "/marcatura-acciaio/", "Marcatura di coltelli e utensili in acciaio con logo, nomi e numeri di serie."), faq_schema(a_faq)])

# ---------------- RISTORAZIONE ----------------
r_faq = [
    ("Il QR può puntare al nostro menu online?", "Sì: incidiamo il QR che rimanda al menu digitale o al sito. Prima della produzione verifichiamo che il link sia quello definitivo e leggibile alla misura scelta."),
    ("Quali materiali sono adatti in sala?", "Legno, acrilico e ardesia. Finitura, spessore e base si scelgono in base all’ambiente e alla pulizia prevista."),
    ("Potete fare anche insegne e adesivi?", "Sì, con il gruppo: insegne con Insegne in Legno, vetrofanie e stampa con Pangea Comunicazione, il sito con Pangea Studio."),
]
S.page("/ristorazione-accoglienza/", "QR da tavolo, segnatavolo e menu in legno | Progetti Laser",
       "Articoli personalizzati al laser per ristoranti, bar e agriturismi: QR code da tavolo, segnatavolo, cubi numerati, menu, sottobicchieri in legno e ardesia.",
       "Articoli personalizzati per ristoranti, bar e agriturismi",
       "QR code da tavolo, segnatavolo, menu e sottobicchieri con il marchio del locale: oggetti che si usano ogni giorno in sala, realizzati in legno, acrilico o ardesia.",
       section("Il marchio del locale, sui tavoli", '<div class="cols2"><p>Il cliente seduto al tavolo guarda il segnatavolo, scansiona il QR del menu, appoggia il bicchiere sul sottobicchiere. Sono oggetti piccoli ma visti da tutti, ogni giorno: se portano il marchio del locale e sono fatti bene, raccontano la cura dell’ambiente meglio di un volantino.</p><p>Li realizziamo in legno, acrilico o ardesia, scegliendo finitura e spessore in base all’uso e alla pulizia. Possiamo coordinarli con l’insegna, il menu stampato e il sito del locale, grazie alle altre attività del gruppo Pangea.</p></div>') +
       section("Cosa realizziamo per la sala", cards([
           ("QR code da tavolo", "Supporti che rimandano al menu digitale, con logo del locale.", "/qr-code-tavolo-legno/"),
           ("Segnatavolo e cubi numerati", "Numero, logo e QR sulle diverse facce, in versione verticale o a cubo.", "/segnaposto-numeri-tavolo-legno/"),
           ("Menu e portamenu", "Copertine e carte dei vini in legno inciso e tagliato.", "/menu-portamenu-legno/"),
           ("Sottobicchieri", "In legno o ardesia, con marchio o grafica dedicata.", "/sottobicchieri-legno/"),
           ("Tessere in legno", "Tessere personalizzate con il marchio del locale.", "/tessere-legno-personalizzate/"),
           ("Espositori da banco", "Supporti per cassa e punto vendita.", "/banco-punto-vendita/"),
           ("Stopper ed espositori", "Espositori in legno per prodotti e bottiglie.", "/stopper-espositori-legno/"),
           ("Ardesia personalizzata", "Lastre e sottobicchieri in ardesia incisi.", "/ardesia-personalizzata/"),
       ])) +
       section("Lavori per locali", works([
           dict(img=I + "sottobicchieri-ardesia-incisi-laser-resto-vintage.webp", alt="Sottobicchieri in ardesia incisi al laser per The Resto Vintage", tag="Foto originale", title="The Resto Vintage", text="Sottobicchieri in ardesia con grafica vintage.", href="/lavori/sottobicchieri-ardesia-vintage/"),
           dict(img=I + "qr-code-tavolo-legno-trattoria-il-ceppo.webp", alt="Supporti da tavolo in legno con QR code del menu e logo Trattoria Il Ceppo incisi al laser", tag="Ambientazione illustrativa", title="Trattoria Il Ceppo", text="Supporti QR da tavolo con logo e link al menu.", href="/lavori/il-ceppo/"),
           dict(img=I + "cubi-segnatavolo-legno-qr-italiano.webp", alt="Cubi segnatavolo in legno con numero, logo e QR code incisi al laser per il locale Italiano", tag="Ambientazione illustrativa", title="Italiano", text="Cubi segnatavolo con numero, logo e QR.", href="/lavori/italiano/"),
       ]), alt=True) +
       section("Domande frequenti", faq(r_faq)),
       hero_img=(I+"qr-code-tavolo-legno-trattoria-il-ceppo.webp","Trattoria Il Ceppo · supporti QR da tavolo"), ctas=ctas("Ristorazione e locali"), crumbs=[("Ristoranti e locali", "/ristorazione-accoglienza/")],
       schema=[service("Articoli personalizzati al laser per la ristorazione", "/ristorazione-accoglienza/", "QR code da tavolo, segnatavolo, menu e sottobicchieri personalizzati."), faq_schema(r_faq)])

# ---------------- CASSETTE ----------------
c_faq = [
    ("Potete incidere le cassette che abbiamo già?", "Sì, si possono valutare. Servono foto, dimensioni, quantità e informazioni sul materiale: verifichiamo la compatibilità prima della conferma."),
    ("Si può mettere una dedica diversa per ogni destinatario?", "Sì, partendo da un elenco definitivo che controlliamo insieme per nomi, accenti e abbinamenti."),
    ("Che legno usate?", "Dipende dalla confezione scelta. Il colore dell’incisione cambia con legno e finitura: te lo mostriamo in bozza prima della produzione."),
]
S.page("/cassette-legno-personalizzate/", "Cassette in legno per vino con logo | Progetti Laser",
       "Cassette e confezioni in legno per bottiglie incise al laser con marchio, testi o dediche per ogni destinatario. Per cantine, regali aziendali e Natale.",
       "Cassette in legno per vino incise con logo o dedica",
       "Per cantine, distillerie e aziende che regalano vino: incidiamo il marchio sulle cassette che hai già o progettiamo con te la confezione, con un testo uguale per tutta la serie o diverso per ogni destinatario.",
       section("Il regalo che porta il nome della cantina", '<div class="cols2"><p>In Oltrepò la cassetta di legno è il modo più naturale di presentare una bottiglia importante: a un cliente, a un distributore, a Natale. Con il marchio inciso diventa parte dell’immagine della cantina; con una dedica per ogni destinatario diventa un regalo personale.</p><p>Incidiamo cassette, coperchi e confezioni con il logo uguale per tutta la serie o con testi diversi pezzo per pezzo, partendo da un elenco controllato insieme. Lavoriamo anche per distillerie e aziende che regalano vino ai propri clienti.</p></div>') +
       section("Due modi per partire", '<div class="two"><div><h3>Hai già le cassette</h3><p>Vedi anche <a href="/incisione-coperchi-legno-conto-terzi/">incisione di coperchi in legno conto terzi</a>. Inviaci foto, misure, quantità e materiale. Verifichiamo superficie, planarità e finitura, poi incidiamo logo, testi o grafica.</p></div><div><h3>Scegliamo insieme la confezione</h3><p>Partiamo dalle bottiglie o dagli oggetti da contenere e dalle loro misure, anche per confezioni verticali con manico.</p></div></div><p class="note">Un marchio molto dettagliato può richiedere una revisione del file per restare leggibile sul legno.</p>') +
       section("Lavori per cantine e aziende", works([
           dict(img=I + "cassetta-legno-incisa-sparkling-world-stifel.webp", alt="Cassetta in legno per bottiglia incisa al laser con logo Sparkling World per Stifel", tag="Ambientazione illustrativa", title="Sparkling World / Stifel", text="Confezione con incisione laser fine.", href="/lavori/sparkling-world/"),
           dict(img=I + "cassetta-vino-legno-incisa-ottavio.webp", alt="Cassette in legno per vino Ottavio Provincia di Pavia IGT incise al laser", tag="Ambientazione illustrativa", title="Ottavio", text="Confezioni vino con incisione personalizzata.", href="/lavori/ottavio/"),
       ]) + '<p class="note" style="margin-top:14px">Le ambientazioni illustrative mostrano lavori eseguiti in un contesto ricostruito; la foto originale è nella pagina del lavoro.</p>', alt=True) +
       section("Domande frequenti", faq(c_faq) + '<p style="margin-top:18px">Etichette e adesivi per bottiglie: <a href="https://www.pangeacomunicazione.it/">Pangea Comunicazione</a>.</p>'),
       hero_img=(I+"cassetta-vino-legno-incisa-ottavio.webp","Ottavio · confezioni vino in legno incise"), ctas=ctas("Cassette in legno"), crumbs=[("Cassette in legno", "/cassette-legno-personalizzate/")],
       schema=[service("Cassette in legno per vino personalizzate", "/cassette-legno-personalizzate/", "Incisione laser di marchi e dediche su cassette e confezioni in legno."), faq_schema(c_faq)])

# ---------------- TAGLIERI ----------------
tg_faq = [
    ("Posso fornire i miei taglieri?", "Sì. Inviaci dati e foto del tagliere: verifichiamo se si può lavorare prima di confermare."),
    ("L’incisione rende il tagliere adatto agli alimenti?", "No. L’idoneità al contatto con gli alimenti dipende dal prodotto e dal suo uso, non dal logo inciso."),
    ("Logo e dedica possono stare insieme?", "Sì: li disponiamo in modo equilibrato e controlliamo la leggibilità dei testi piccoli."),
]
S.page("/taglieri-personalizzati/", "Taglieri in legno personalizzati | Progetti Laser",
       "Taglieri in legno incisi al laser con logo, testi o dediche, per regali, presentazioni aziendali e locali. Anche su taglieri forniti dal cliente.",
       "Taglieri in legno personalizzati con logo o dedica",
       "Incidiamo logo, testi concordati e dediche su taglieri in legno, per regali, presentazioni aziendali e locali. Scegliamo insieme area e formato dell’incisione in base a forma, manico e bordi.",
       section("Cosa personalizziamo", '<ul class="list"><li>Logo o marchio inciso</li><li>Testi e dediche, impaginati insieme al logo senza sovrapporsi</li><li>Area e formato dell’incisione, scelti su misure e forma</li><li>Controllo di leggibilità sui testi piccoli</li></ul><p>Le venature del legno fanno parte del risultato: l’incisione non è una stampa a colore uniforme.</p>') +
       section("Lavori realizzati", works([
           dict(img=I + "incisione-laser-tagliere-legno-logo-casaia.webp", alt="Tagliere in legno di faggio durante l’incisione laser del logo La Casaia", tag="Foto originale", title="Casaia · in lavorazione", text="Il tagliere durante l’incisione nel nostro laboratorio.", href="/lavori/casaia/"),
           dict(img=I + "taglieri-legno-personalizzati-logo-casaia.webp", alt="Taglieri in legno personalizzati con il logo La Casaia inciso al laser", tag="Ambientazione illustrativa", title="Casaia · risultato", text="Taglieri con marchio inciso.", href="/lavori/casaia/"),
       ]), alt=True) +
       section("Domande frequenti", faq(tg_faq)),
       hero_img=(I+"taglieri-legno-personalizzati-logo-casaia.webp","Taglieri in legno personalizzati con logo inciso al laser"), ctas=ctas("Taglieri personalizzati"), crumbs=[("Taglieri", "/taglieri-personalizzati/")],
       schema=[service("Taglieri personalizzati incisi al laser", "/taglieri-personalizzati/", "Incisione di logo e dediche su taglieri in legno."), faq_schema(tg_faq)])

# ---------------- GADGET ----------------
g_faq = [
    ("C’è una quantità minima?", "Le quantità si definiscono nel preventivo in base all’oggetto e alla lavorazione."),
    ("Posso partire da un oggetto che ho già?", "Sì. Inviaci foto e misure del pezzo con il disegno: verifichiamo materiale, superficie e accessibilità prima di confermare."),
    ("Come si definisce la grafica?", "Dal logo o dal testo definitivo, adattato alla superficie. Composizione e lavorazione si approvano prima della produzione."),
]
S.page("/gadget-aziendali-personalizzati/", "Gadget aziendali personalizzati al laser | Progetti Laser",
       "Gadget aziendali incisi al laser: portachiavi in legno, taccuini e oggetti con logo per eventi, anniversari e clienti. Personalizzazioni in serie.",
       "Gadget aziendali personalizzati al laser",
       "Portachiavi in legno, taccuini e oggetti con il tuo logo per eventi, anniversari, fiere e omaggi ai clienti: personalizzazioni in serie, con taglio e incisione laser.",
       section("Gadget che si tengono", '<div class="cols2"><p>Un gadget funziona quando chi lo riceve lo usa: un portachiavi in legno, un taccuino con la copertina incisa, un oggetto legato a una ricorrenza dell’azienda. L’incisione laser dà un aspetto più curato della stampa e resiste nel tempo.</p><p>Li prepariamo per anniversari, eventi, fiere e omaggi ai clienti, anche in serie con testi diversi. Ci servono il tipo di oggetto, la quantità e il logo definitivo; il resto lo verifichiamo insieme prima della produzione.</p></div>') +
       section("Idee realizzate", works([
           dict(img=I + "taccuino-personalizzato-logo-inciso-bioenol.webp", alt="Bioenol · taccuino con spirale, fascia ed elastico blu e penna coordinata", tag="Foto originale", title="Taccuino Bioenol", text="Spirale, fascia ed elastico blu, con penna coordinata.", href="/lavori/taccuino-bioenol/"),
           dict(img=I + "taccuino-copertina-incisa-laser-carnevale.webp", alt="Taccuino a spirale con copertina in cartone incisa al laser a tema Carnevale", tag="Foto originale", title="Taccuino Carnevale", text="Copertina incisa con un disegno dedicato alla ricorrenza.", href="/lavori/taccuino-carnevale/"),
           dict(img=I + "portachiavi-legno-personalizzati-anniversario.webp", alt="Portachiavi tondi in legno incisi al laser per il 40° anniversario di Acconciature Giovanna", tag="Ambientazione illustrativa", title="Portachiavi 40° anniversario", text="Portachiavi tondi in legno con incisione e anelli metallici.", href="/lavori/portachiavi-legno-anniversario/"),
       ])) +
       section("Per il preventivo", '<ul class="list"><li>Foto o tipo di oggetto e quantità</li><li>Logo o testo definitivo</li><li>Misure del supporto e area lavorabile</li><li>Utilizzo previsto (evento, omaggio, anniversario)</li></ul><p>Per confezioni regalo vedi <a href="/cassette-legno-personalizzate/">cassette in legno</a>.</p>', alt=True) +
       section("Domande frequenti", faq(g_faq)),
       hero_img=(I+"portachiavi-legno-personalizzati-anniversario.webp","Portachiavi in legno incisi al laser per un anniversario aziendale"), ctas=ctas("Gadget aziendali"), crumbs=[("Gadget aziendali", "/gadget-aziendali-personalizzati/")],
       schema=[service("Gadget aziendali personalizzati al laser", "/gadget-aziendali-personalizzati/", "Portachiavi, taccuini e oggetti con logo, in serie."), faq_schema(g_faq)])

# ---------------- NOMI E REGALI ----------------
n_faq = [
    ("Potete fare un pezzo unico?", "Sì: nomi, targhe e decorazioni si realizzano anche in un solo esemplare."),
    ("Posso scegliere carattere e colori?", "Sì. Ti mandiamo una bozza con nome, carattere e disposizione da approvare prima del taglio."),
    ("Cosa devo controllare prima di confermare?", "Nomi, accenti e date: incidiamo esattamente il testo approvato in bozza."),
]
S.page("/nomi-regali-personalizzati/", "Nomi in legno e regali personalizzati | Progetti Laser",
       "Nomi sagomati, targhe per cameretta, battesimi, regali per maestre e ricorrenze in legno e plexiglass, tagliati e incisi al laser in Oltrepò Pavese.",
       "Nomi in legno e regali personalizzati",
       "Nomi sagomati, targhe per la cameretta, battesimi, dediche per maestre e ricorrenze: tagliamo e incidiamo legno e plexiglass a partire dal nome e dall’idea che hai in mente.",
       section("Un nome, una data, un ricordo", '<p class="lead2">Nascite, battesimi, matrimoni, compleanni, un grazie alle maestre: tagliamo e incidiamo il legno e il plexiglass partendo dal nome e dall’idea che hai in mente. Ti mandiamo una bozza con carattere e disposizione e, quando la approvi, realizziamo il pezzo. Ogni regalo qui sotto è stato fatto nel nostro laboratorio.</p>') +
       section("Regali che abbiamo realizzato", works([
           dict(img=I + "orsetto-legno-nome-inciso.webp", alt="Orsetto in legno tagliato al laser con nome inciso sul cuore e nastro rosa", tag="Foto originale", title="Orsetto con nome", text="Orsetto in legno con il nome inciso sul cuore.", href="/lavori/orsetto-nicol-legno/"),
           dict(img=I + "targhe-battesimo-legno-personalizzate.webp", alt="Targhe in legno per battesimo con angeli, nome e dedica incisi e tagliati al laser", tag="Foto originale", title="Battesimo", text="Due targhe quadrate con angeli e cuori.", href="/lavori/targhe-battesimo-legno/"),
           dict(img=I + "cuore-plexiglass-inciso-dedica-mamma.webp", alt="Cuore in plexiglass trasparente inciso al laser con dedica Ti voglio bene Mamma su base in legno", tag="Foto originale", title="Per la mamma", text="Cuore in plexiglass trasparente con dedica.", href="/lavori/cuore-plexiglass-mamma/"),
           dict(img=I + "scritta-legno-sagomata-nome-giuseppe.webp", alt="Scritta in legno sagomata al laser su più livelli con il nome Giuseppe", tag="Foto originale", title="Giuseppe", text="Nome sagomato su più livelli.", href="/lavori/scritta-giuseppe-sagomata/"),
           dict(img=I + "pannello-legno-albero-nomi-matrimonio.webp", alt="Pannello in legno per matrimonio con albero, nomi e data tagliati al laser", tag="Foto originale", title="Adam e Valentina", text="Albero con nomi, data e cuori.", href="/lavori/albero-personalizzato-adam-valentina/"),
           dict(img=I + "aeroplano-legno-taglio-laser-incastro.webp", alt="Aeroplano biplano in legno tagliato al laser e montato a incastro", tag="Foto originale", title="Aeroplano", text="Biplano in legno assemblato a incastro.", href="/lavori/aeroplano-legno/"),
       ])) +
       section("Domande frequenti", faq(n_faq), alt=True),
       hero_img=(I+"pannello-legno-albero-nomi-matrimonio.webp","Pannello in legno con albero e nomi tagliati al laser per un matrimonio"), ctas=ctas("Nomi e regali"), crumbs=[("Nomi e regali", "/nomi-regali-personalizzati/")],
       schema=[service("Nomi e regali personalizzati al laser", "/nomi-regali-personalizzati/", "Nomi sagomati, targhe e regali in legno e plexiglass."), faq_schema(n_faq)])

# ---------------- VETRO ----------------
v_faq = [
    ("Posso partire da una bottiglia o un oggetto che ho già?", "Sì. Inviaci foto, misure e il disegno: verifichiamo materiale, superficie e area accessibile prima di confermare."),
    ("Ogni forma si può incidere?", "Non tutti gli oggetti hanno la stessa geometria: ogni nuovo formato richiede una verifica specifica prima della conferma."),
    ("Per una serie con testi diversi?", "Raccogliamo disegno, numero di pezzi ed elenco dei testi variabili prima della produzione."),
]
S.page("/incisione-vetro-personalizzata/", "Incisione laser su vetro e bottiglie | Progetti Laser",
       "Incisione laser su bottiglie e oggetti in vetro: marchi, dediche e decorazioni per regali e serie personalizzate. Verifica del formato prima della conferma.",
       "Incisione laser su vetro e bottiglie",
       "Incidiamo marchi, dediche e decorazioni su bottiglie e oggetti in vetro, per regali e serie personalizzate. La leggibilità dipende dalla luce che attraversa il vetro e dalla posizione del decoro.",
       section("Come valutiamo un oggetto in vetro", '<div class="two"><div><ul class="list"><li>Forma dell’oggetto e area raggiungibile</li><li>Spessore e caratteristiche del vetro</li><li>Posizione del decoro rispetto alla luce</li><li>Dimensione minima dei testi</li></ul></div><div>' + works([dict(img=I + "bottiglia-vetro-incisa-laser-vintage.webp", alt="Bottiglia in vetro con chiusura meccanica e decorazione Vintage Design incisa", tag="Ambientazione illustrativa", title="Bottiglia Vintage Design", text="Scritte e motivi ornamentali su bottiglia con tappo meccanico.", href="/lavori/bottiglia-vetro-incisa/")]) + '</div></div>') +
       section("Domande frequenti", faq(v_faq), alt=True),
       hero_img=(I+"bottiglia-vetro-incisa-laser-vintage.webp","Bottiglia in vetro con decorazione Vintage Design incisa"), ctas=ctas("Incisione su vetro"), crumbs=[("Incisione su vetro", "/incisione-vetro-personalizzata/")],
       schema=[service("Incisione laser su vetro", "/incisione-vetro-personalizzata/", "Incisione di marchi, dediche e decori su bottiglie e oggetti in vetro."), faq_schema(v_faq)])

# ---------------- REALIZZAZIONI ----------------
REAL = [
    ("Aziende e industria", [
        ("targhette-incise-laser-serie-genoface.webp", "Genoface", "Targhette incise e tagliate per apparecchiature.", "Foto originale", "/lavori/genoface-personalizzazione-serie/"),
        ("marcatura-laser-qr-code-acciaio.webp", "QR code incisi", "QR marcati per targhette e menu.", "Foto originale", "/lavori/qr-code-marcatura-laser/"),
        ("taccuino-personalizzato-logo-inciso-bioenol.webp", "Bioenol", "Taccuino con penna coordinata.", "Foto originale", "/lavori/taccuino-bioenol/"),
        ("marcatura-laser-bicolore-acciaio-spazzolato.webp", "Bicolore su acciaio", "Due tonalità su acciaio spazzolato.", "Immagine del post", "/lavori/marcatura-bicolore-acciaio/"),
    ]),
    ("Locali e cantine", [
        ("sottobicchieri-ardesia-incisi-laser-resto-vintage.webp", "The Resto Vintage", "Sottobicchieri in ardesia.", "Foto originale", "/lavori/sottobicchieri-ardesia-vintage/"),
        ("qr-code-tavolo-legno-trattoria-il-ceppo.webp", "Trattoria Il Ceppo", "Supporti QR da tavolo.", "Ambientazione illustrativa", "/lavori/il-ceppo/"),
        ("cassetta-legno-incisa-sparkling-world-stifel.webp", "Sparkling World / Stifel", "Confezione con incisione fine.", "Ambientazione illustrativa", "/lavori/sparkling-world/"),
    ]),
    ("Premi, decorazioni e regali", [
        ("targa-metallo-incisa-laser-fbc-casteggio.webp", "FBC Casteggio 1898", "Targa a scudo con aquila e stella.", "Foto originale", "/lavori/targa-fbc-casteggio/"),
        ("renne-abete-legno-taglio-laser-natale.webp", "Renne e abete", "Sagome natalizie in legno.", "Foto originale", "/lavori/renne-decorazione-invernale/"),
        ("pannello-legno-cervo-geometrico-laser.webp", "Cervo geometrico", "Profilo chiaro su legno scuro.", "Foto originale", "/lavori/pannello-cervo-geometrico/"),
    ]),
]
real_body = "".join(section(t, works([dict(img=I + f, alt=f"{n}: {d[:-1].lower() if d.endswith('.') else d} – lavorazione laser Progetti Laser", tag=tag, title=n, text=d, href=h) for f, n, d, tag, h in items]), alt=i % 2 == 1) for i, (t, items) in enumerate(REAL))
S.page("/realizzazioni/", "Realizzazioni laser per aziende e locali | Progetti Laser",
       "Lavori di incisione, taglio e marcatura laser realizzati per aziende, ristoranti, cantine, società sportive e privati, con foto originali e ambientazioni.",
       "Realizzazioni", "Una selezione dei lavori usciti dal laboratorio. Ogni immagine dichiara se è una foto originale o un’ambientazione illustrativa ricostruita a partire dal lavoro eseguito.",
       real_body, crumbs=[("Realizzazioni", "/realizzazioni/")], ctas=ctas("Generico"), hero_img=(I+"marcatura-laser-qr-code-acciaio.webp", "Marcatura laser di QR code su acciaio"))

# ---------------- COME LAVORIAMO ----------------
S.page("/come-lavoriamo/", "Come lavoriamo e file per il laser | Progetti Laser",
       "Dalla foto del pezzo alla produzione: cosa inviare, come preparare il file per incisione e taglio laser, bozza e approvazione.",
       "Come lavoriamo", "Tre passaggi, con una verifica prima di ogni conferma: così sai cosa riceverai prima che il laser parta.",
       section("Il percorso", steps([
           ("Richiesta", "Ci mandi foto o tipo di oggetto, misure, materiale, quantità e file grafico, dal modulo, per email o su WhatsApp."),
           ("Verifica e preventivo", "Controlliamo fattibilità, area lavorabile e file. Il preventivo indica lavorazione, costi e tempi."),
           ("Bozza, approvazione, produzione", "Approvi bozza e testi definitivi; poi incidiamo, tagliamo o marchiamo e ti avvisiamo per il ritiro o la consegna concordata."),
       ])) +
       section("Come preparare il file", '<div class="two"><div><h3>Formato consigliato</h3><ul class="list"><li>Vettoriale: SVG, PDF, AI, EPS o DXF</li><li>Testi convertiti in tracciati o font indicati</li><li>Misure reali in millimetri</li><li>Per il taglio: linee chiuse, senza doppioni</li></ul></div><div><h3>Se hai solo un’immagine</h3><p>Un JPG o PNG può bastare per una prima valutazione. Se serve, ricostruiamo il logo in vettoriale: lo trovi indicato nel preventivo.</p><p><a href="/preparare-file-incisione-laser/">Guida completa alla preparazione dei file →</a></p><h3>Dati variabili</h3><p>Per nomi, numeri o matricole diversi per pezzo prepara un elenco definitivo (Excel o CSV) e controllalo prima dell’invio.</p></div></div>', alt=True),
       crumbs=[("Come lavoriamo", "/come-lavoriamo/")], ctas=ctas("Generico"), hero_img=(I+"aeroplano-legno-taglio-laser-incastro.webp", "Aeroplano in legno tagliato al laser e montato a incastro"))

# ---------------- PREVENTIVO ----------------
CATS = ["Generico", "Targhette industriali", "Marcatura acciaio", "Ristorazione e locali", "Cassette in legno", "Taglieri personalizzati", "Gadget aziendali", "Nomi e regali", "Incisione su vetro", "Altro"]
FORM = f"""<form class="f" data-mail="{P['email']}" data-subject="Richiesta preventivo · Progetti Laser">
<div class="row"><label>Nome e cognome *<input name="nome" required autocomplete="name"></label><label>Azienda o locale<input name="azienda" autocomplete="organization"></label></div>
<div class="row"><label>Email *<input type="email" name="email" required autocomplete="email"></label><label>Telefono<input type="tel" name="telefono" autocomplete="tel"></label></div>
<div class="row"><label>Tipo di lavoro<select name="progetto" data-pre="progetto">{''.join(f'<option>{c}</option>' for c in CATS)}</select></label><label>Quantità<input name="quantita" inputmode="numeric"></label></div>
<div class="row"><label>Materiale<select name="materiale"><option>Da definire</option><option>Legno</option><option>Metallo / acciaio</option><option>Plastica / acrilico</option><option>Vetro</option><option>Ardesia</option><option>Oggetto mio</option></select></label><label>Misure indicative<input name="misure" placeholder="es. 80 × 40 mm"></label></div>
<label>Descrivi il lavoro *<textarea name="descrizione" required placeholder="Cosa vuoi personalizzare, testi, scadenza…"></textarea></label>
<p class="note">Hai un file o una foto del pezzo? Allegali all’email che si apre quando premi “Prepara l’email”.</p>
<label class="chk"><input type="checkbox" name="privacy" required value="accettata"><span>Ho letto l’<a href="/privacy/">informativa privacy</a> e acconsento all’uso dei dati per rispondere alla richiesta. *</span></label>
<button class="btn b1" type="submit">Prepara l’email</button><p class="msg" role="status"></p>
<p class="note">Preferisci scrivere? Email <a href="mailto:{P['email']}">{P['email']}</a> · WhatsApp <a href="{P['wa']}">{P['tel']}</a></p>
</form>"""
S.page("/preventivo/", "Preventivo incisione laser | Progetti Laser",
       "Richiedi un preventivo per incisione, taglio o marcatura laser: indica tipo di lavoro, materiale, misure e quantità e allega il file o una foto.",
       "Chiedi un preventivo", "Più dati ci dai, più il preventivo è preciso: tipo di lavoro, materiale, misure, quantità e, se puoi, il file o una foto del pezzo.",
       section("Il tuo progetto", FORM), crumbs=[("Preventivo", "/preventivo/")], hero_img=(I+"cubi-segnatavolo-legno-qr-italiano.webp", "Cubi segnatavolo in legno incisi al laser"))

S.page("/grazie/", "Richiesta inviata · Progetti Laser", "Richiesta ricevuta.", "Grazie, abbiamo ricevuto la richiesta",
       "Ti rispondiamo appena verificato il lavoro. Se è urgente chiamaci allo <a href=\"tel:+390385320302\">0385 320302</a>.", "", ctas='<div class="ctas"><a class="btn b1" href="/realizzazioni/">Guarda le realizzazioni</a></div>', noindex=True, hero_img=(I+"renne-abete-legno-taglio-laser-natale.webp", "Decorazioni in legno tagliate al laser"))

PRIV = f"""<section class="band"><div class="wrap">
<h2>Titolare del trattamento</h2><p>{P['ragione']}, {P['via']}, {P['cap']} {P['citta']} ({P['prov']}), P. IVA {P['piva']}. Contatti: <a href="mailto:{P['email']}">{P['email']}</a>, {P['tel']}.</p>
<h2>Dati raccolti e finalità</h2><p>Con il modulo di preventivo raccogliamo nome, contatti, descrizione del lavoro ed eventuali file allegati, solo per rispondere alla richiesta e valutare il progetto. Base giuridica: misure precontrattuali richieste dall’interessato. Non inviamo newsletter o comunicazioni promozionali.</p>
<h2>Servizi di terze parti</h2><p>Il modulo non invia dati a servizi esterni: prepara un’email nel tuo programma di posta, che parte solo se la invii tu. Il sito è ospitato da Hostinger, che tratta i dati tecnici necessari a fornire le pagine (log del server). I caratteri tipografici sono serviti dal nostro dominio. Google Analytics 4 si attiva solo con il consenso alle statistiche, gestibile dalla pagina <a href="/cookie/">Cookie</a>; non riceve i dati dei moduli. Non usiamo cookie di profilazione pubblicitaria. Il link a WhatsApp apre il servizio del relativo fornitore, con la sua informativa.</p>
<h2>Conservazione</h2><p>Conserviamo la corrispondenza per il tempo necessario a gestire la richiesta; i documenti amministrativi seguono gli obblighi di legge.</p>
<h2>Diritti</h2><p>Puoi chiedere accesso, rettifica, cancellazione, limitazione o opposizione scrivendo a {P['email']}, e proporre reclamo al Garante per la protezione dei dati personali.</p>
<p class="note">Aggiornata il 24/11/2026 · testo da validare con il consulente privacy prima della pubblicazione.</p></div></section>"""
S.page("/privacy/", "Privacy · Progetti Laser", "Informativa privacy di Progetti Laser: titolare, dati del modulo preventivo, servizi terzi, conservazione e diritti.", "Informativa privacy", "Come trattiamo i dati inviati tramite il sito.", PRIV, crumbs=[("Privacy", "/privacy/")], hero_img=(I+"pannello-legno-cervo-geometrico-laser.webp", "Pannello in legno con cervo geometrico tagliato al laser"))

import laser_extra
laser_extra.add_extra(S, ctas, service, P, D)

if __name__ == "__main__":
    b = S.build()
    with open(b / "htaccess-da-unire.txt", "a") as _f:
        _f.write(laser_extra.redirects(D))
    make_preview(b, S.key)
    print(b, len(S.pages))
