"""Pagine mancanti di progettilaser.it (categorie, lavori, servizi, cookie, novità).
Testi sobri, basati solo su ciò che è noto dal sito (slug, foto, pagine esistenti): niente dati inventati.
I /video/* non hanno i filmati nel repository: sono reindirizzati (301) alla pagina di categoria."""
from core import *
from seo_lavori import SEO_LAVORI

I = "/images/"

# slug categoria -> (nome, descrizione breve, immagine, alt, [slug lavori correlati], [cosa realizziamo])
CATS = {
 "sagome-decorazioni-legno": ("Sagome e decorazioni in legno", "Sagome, scritte, alberi, animali e decorazioni tagliate al laser su legno, anche su più livelli.", "renne-abete-legno-taglio-laser-natale.webp", "Renne e abete in legno tagliati al laser", ["renne-decorazione-invernale", "pannello-cervo-geometrico", "scritta-giuseppe-sagomata", "sagome-cane-gatto", "lettere-xmas", "aeroplano-legno"], ["Sagome e profili su misura", "Scritte e nomi su più livelli", "Decorazioni stagionali e natalizie", "Pezzi a incastro"]),
 "premi-personalizzati": ("Premi e riconoscimenti personalizzati", "Targhe, premi e riconoscimenti in legno, metallo e plexiglass incisi e tagliati al laser.", "targa-metallo-incisa-laser-fbc-casteggio.webp", "Targa a scudo in metallo incisa al laser", ["targa-fbc-casteggio", "cuore-plexiglass-mamma", "stay-positive"], ["Targhe e premi per società e associazioni", "Riconoscimenti con logo e dedica", "Metallo, legno e plexiglass"]),
 "confezioni-natale-aziende": ("Confezioni di Natale per aziende", "Cassette e confezioni in legno personalizzate per i regali aziendali di Natale, con marchio o dedica.", "cassetta-vino-legno-incisa-ottavio.webp", "Cassette in legno per vino incise al laser", ["ottavio", "sparkling-world", "scatola-amedeo", "lettere-xmas"], ["Cassette per bottiglie con marchio", "Dediche diverse per ogni destinatario", "Confezioni in serie"]),
 "ardesia-personalizzata": ("Ardesia personalizzata", "Sottobicchieri, lastre e segnaposto in ardesia incisi al laser con logo, nome o grafica dedicata.", "sottobicchieri-ardesia-incisi-laser-resto-vintage.webp", "Sottobicchieri in ardesia incisi al laser", ["sottobicchieri-ardesia-vintage", "tonalini-ardesia"], ["Sottobicchieri con marchio", "Lastre per tavola e presentazione", "Segnaposto e targhe"]),
 "targhe-pannelli-legno": ("Targhe e pannelli in legno", "Targhe, pannelli e insegne da interno in legno tagliati e incisi al laser.", "pannello-legno-cervo-geometrico-laser.webp", "Pannello in legno con cervo geometrico tagliato al laser", ["pannello-cervo-geometrico", "albero-personalizzato-adam-valentina", "targa-orsetto-samuele"], ["Pannelli decorativi", "Targhe con nome o logo", "Scritte a rilievo"]),
 "cerimonie-matrimoni-personalizzati": ("Cerimonie e matrimoni personalizzati", "Nomi, date, tableau e decorazioni in legno e plexiglass per matrimoni, battesimi e ricorrenze.", "pannello-legno-albero-nomi-matrimonio.webp", "Pannello in legno con albero e nomi per un matrimonio", ["albero-personalizzato-adam-valentina", "giulia-matteo", "targhe-battesimo-legno", "albero-nomi-farfalle"], ["Alberi e pannelli con nomi e data", "Targhe per battesimo", "Segnaposto e decorazioni"]),
 "qr-code-tavolo-legno": ("QR code da tavolo in legno", "Supporti da tavolo in legno con QR code del menu e logo del locale, incisi al laser.", "qr-code-tavolo-legno-trattoria-il-ceppo.webp", "Supporti da tavolo in legno con QR code e logo", ["il-ceppo", "qr-code-marcatura-laser"], ["QR verso menu o sito", "Logo del locale", "Formati da tavolo"]),
 "segnaposto-numeri-tavolo-legno": ("Segnaposto e numeri tavolo in legno", "Cubi e segnatavolo numerati in legno con numero, logo e QR code incisi al laser.", "cubi-segnatavolo-legno-qr-italiano.webp", "Cubi segnatavolo in legno con numero e QR", ["italiano", "il-ceppo"], ["Numeri tavolo", "Cubi con più facce incise", "Logo del locale"]),
 "menu-portamenu-legno": ("Menu e portamenu in legno", "Copertine di menu, carte dei vini e portamenu in legno incisi e tagliati al laser.", "qr-code-tavolo-legno-trattoria-il-ceppo.webp", "Supporti in legno per tavolo di ristorante", ["carta-vini-legno", "il-ceppo"], ["Copertine in legno", "Carte dei vini", "Portamenu da tavolo"]),
 "sottobicchieri-legno": ("Sottobicchieri in legno", "Sottobicchieri in legno e ardesia con marchio o grafica dedicata, incisi al laser.", "sottobicchieri-ardesia-incisi-laser-resto-vintage.webp", "Sottobicchieri incisi al laser", ["sottobicchieri-ardesia-vintage", "tonalini-ardesia"], ["Logo del locale o della cantina", "Serie coordinate", "Legno o ardesia"]),
 "banco-punto-vendita": ("Banco e punto vendita", "Supporti, cartelli e piccoli espositori in legno per il banco e il punto vendita.", "taglieri-legno-personalizzati-logo-casaia.webp", "Taglieri in legno personalizzati per punto vendita", ["casaia", "stopper-espositori-legno"], ["Cartelli prezzo e nome", "Supporti per il banco", "Logo inciso"]),
 "stopper-espositori-legno": ("Stopper ed espositori in legno", "Stopper, supporti per bottiglie ed espositori in legno personalizzati al laser.", "cassetta-legno-incisa-sparkling-world-stifel.webp", "Confezione in legno per bottiglia incisa al laser", ["sparkling-world", "ottavio"], ["Espositori per bottiglie", "Stopper con marchio", "Supporti da scaffale"]),
 "incisione-coperchi-legno-conto-terzi": ("Incisione coperchi in legno conto terzi", "Incisione laser di coperchi e componenti in legno forniti dal cliente, per confezionatori e aziende.", "cassetta-vino-legno-incisa-ottavio.webp", "Cassette in legno per vino con coperchio inciso", ["ottavio", "sparkling-world"], ["Coperchi forniti dal cliente", "Serie con logo uguale", "Verifica del formato prima della conferma"]),
 "tessere-legno-personalizzate": ("Tessere in legno personalizzate", "Tessere e card in legno incise al laser con il marchio del locale o dell’azienda.", "portachiavi-legno-personalizzati-anniversario.webp", "Oggetti in legno incisi al laser con logo", ["portachiavi-legno-anniversario"], ["Tessere con logo", "Card numerate", "Serie personalizzate"]),
 "marcatura-laser-personalizzata": ("Marcatura laser personalizzata", "Marcatura laser su metallo, acciaio e plastica: loghi, matricole, QR code e codici per aziende.", "marcatura-laser-qr-code-acciaio.webp", "QR code marcati al laser su lamiera di acciaio", ["qr-code-marcatura-laser", "marcatura-bicolore-acciaio", "genoface-personalizzazione-serie"], ["Loghi e testi su acciaio", "Matricole e numeri di serie", "QR code"]),
 "oggetti-personalizzati-3d": ("Oggetti personalizzati in 3D", "Oggetti e componenti stampati in 3D e personalizzati, in coordinamento con il laboratorio laser.", "aeroplano-legno-taglio-laser-incastro.webp", "Biplano in legno tagliato al laser e montato a incastro", ["aeroplano-legno"], ["Pezzi singoli e prototipi", "Componenti coordinati con il laser", "Preventivo da disegno o idea"]),
 "fotografia-ballabio": ("Fotografia per Ballabio", "Fotografia di bottiglia e packaging per Ballabio, realizzata da Pangea Studio.", None, "", [], []),
}

# slug lavoro -> (titolo, categoria correlata, immagine|None, alt, testo)
WORKS = {
 "il-ceppo": ("Trattoria Il Ceppo", "qr-code-tavolo-legno", "qr-code-tavolo-legno-trattoria-il-ceppo.webp", "Supporti da tavolo in legno con QR code e logo Trattoria Il Ceppo", "Supporti da tavolo in legno con QR code del menu e logo del locale, incisi al laser."),
 "italiano": ("Italiano", "segnaposto-numeri-tavolo-legno", "cubi-segnatavolo-legno-qr-italiano.webp", "Cubi segnatavolo in legno con numero, logo e QR code per il locale Italiano", "Cubi segnatavolo in legno con numero, logo e QR code sulle diverse facce."),
 "cunsorsi": ("Cunsorsi", "segnaposto-numeri-tavolo-legno", None, "", "Lavoro di personalizzazione laser realizzato per Cunsorsi nel laboratorio Progetti Laser."),
 "ottavio": ("Ottavio", "confezioni-natale-aziende", "cassetta-vino-legno-incisa-ottavio.webp", "Cassette in legno per vino Ottavio Provincia di Pavia IGT incise al laser", "Confezioni vino in legno con il marchio inciso al laser."),
 "vitea": ("Vitea", "targhe-pannelli-legno", None, "", "Lavoro di personalizzazione laser realizzato per Vitea nel laboratorio Progetti Laser."),
 "casaia": ("La Casaia", "banco-punto-vendita", "taglieri-legno-personalizzati-logo-casaia.webp", "Taglieri in legno personalizzati con il logo La Casaia", "Taglieri in legno con il logo La Casaia inciso al laser."),
 "sparkling-world": ("Sparkling World / Stifel", "stopper-espositori-legno", "cassetta-legno-incisa-sparkling-world-stifel.webp", "Cassetta in legno per bottiglia incisa al laser con logo Sparkling World", "Cassetta in legno per bottiglia con logo inciso."),
 "giulia-matteo": ("Giulia e Matteo", "incisione-coperchi-legno-conto-terzi", None, "", "Lavoro in legno realizzato al laser per Giulia e Matteo."),
 "vorwerk": ("Vorwerk", "gadget-aziendali-personalizzati", None, "", "Personalizzazione laser realizzata per Vorwerk nel laboratorio Progetti Laser."),
 "gualco": ("Distilleria Gualco", "incisione-coperchi-legno-conto-terzi", None, "", "Personalizzazione laser realizzata per la Distilleria Gualco."),
 "val-tidone": ("Val Tidone", "incisione-coperchi-legno-conto-terzi", None, "", "Personalizzazione laser realizzata per Val Tidone."),
 "chiesa": ("Chiesa", "sagome-decorazioni-legno", None, "", "Lavoro in legno realizzato al laser."),
 "tonalini-ardesia": ("Tonalini in ardesia", "ardesia-personalizzata", None, "", "Lavoro in ardesia con incisione laser."),
 "sottobicchieri-ardesia-vintage": ("The Resto Vintage", "ardesia-personalizzata", "sottobicchieri-ardesia-incisi-laser-resto-vintage.webp", "Sottobicchieri quadrati in ardesia incisi al laser con il logo di The Resto Vintage", "Sottobicchieri quadrati in ardesia con il logo del locale, incisi al laser."),
 "bosco-longhino": ("Bosco Longhino", "confezioni-natale-aziende", None, "", "Personalizzazione laser realizzata per Bosco Longhino."),
 "bottiglia-vetro-incisa": ("Bottiglia in vetro incisa", "incisione-vetro-personalizzata", "bottiglia-vetro-incisa-laser-vintage.webp", "Bottiglia in vetro con decorazione Vintage Design incisa al laser", "Bottiglia in vetro con decoro inciso al laser."),
 "vigne-di-misinto": ("Vigne di Misinto", "targhe-pannelli-legno", None, "", "Personalizzazione laser realizzata per Vigne di Misinto."),
 "nomi-porta-cameretta": ("Nomi per la porta della cameretta", "nomi-regali-personalizzati", None, "", "Nomi in legno tagliati al laser per la porta della cameretta."),
 "lettere-xmas": ("Lettere di Natale", "sagome-decorazioni-legno", None, "", "Lettere in legno tagliate al laser per le decorazioni natalizie."),
 "corte-del-lupo": ("Corte del Lupo", "sagome-decorazioni-legno", None, "", "Personalizzazione laser realizzata per Corte del Lupo."),
 "carta-vini-legno": ("Carta dei vini in legno", "menu-portamenu-legno", None, "", "Carta dei vini in legno incisa al laser."),
 "stay-positive": ("Stay Positive", "premi-personalizzati", None, "", "Lavoro realizzato al laser."),
 "elisa-nome-sagomato": ("Nome sagomato Elisa", "nomi-regali-personalizzati", None, "", "Nome in legno sagomato al laser."),
 "gruppo-casa-30-anni": ("Gruppo Casa, 30 anni", "premi-personalizzati", None, "", "Lavoro in legno realizzato al laser per Gruppo Casa."),
 "aeroplano-legno": ("Aeroplano in legno", "sagome-decorazioni-legno", "aeroplano-legno-taglio-laser-incastro.webp", "Aeroplano biplano in legno tagliato al laser e montato a incastro", "Biplano in legno tagliato al laser e assemblato a incastro."),
 "genoface-personalizzazione-serie": ("Genoface", "targhette-industriali-laser", "targhette-incise-laser-serie-genoface.webp", "Targhette in serie con logo Genoface incise al laser", "Targhette incise e tagliate in serie per apparecchiature."),
 "orsetto-nicol-legno": ("Orsetto con nome", "nomi-regali-personalizzati", "orsetto-legno-nome-inciso.webp", "Orsetto in legno tagliato al laser con nome inciso sul cuore", "Orsetto in legno con il nome inciso sul cuore."),
 "portachiavi-legno-anniversario": ("Portachiavi per un anniversario", "gadget-aziendali-personalizzati", "portachiavi-legno-personalizzati-anniversario.webp", "Portachiavi tondi in legno incisi al laser per un anniversario", "Portachiavi tondi in legno incisi per un anniversario aziendale."),
 "scatola-amedeo": ("Scatola Amedeo", "confezioni-natale-aziende", None, "", "Scatola in legno personalizzata al laser."),
 "targa-fbc-casteggio": ("FBC Casteggio 1898", "premi-personalizzati", "targa-metallo-incisa-laser-fbc-casteggio.webp", "Targa a scudo in metallo incisa e tagliata al laser per FBC Casteggio 1898", "Targa a scudo in metallo con aquila e stella, incisa e tagliata al laser."),
 "taccuino-bioenol": ("Bioenol", "gadget-aziendali-personalizzati", "taccuino-personalizzato-logo-inciso-bioenol.webp", "Taccuino con logo Bioenol inciso al laser e penna coordinata", "Taccuino con spirale, fascia ed elastico blu e penna coordinata."),
 "pannello-cervo-geometrico": ("Cervo geometrico", "targhe-pannelli-legno", "pannello-legno-cervo-geometrico-laser.webp", "Pannello in legno con cervo geometrico tagliato al laser", "Pannello con profilo chiaro su legno scuro."),
 "renne-decorazione-invernale": ("Renne e abete", "sagome-decorazioni-legno", "renne-abete-legno-taglio-laser-natale.webp", "Renne e abete in legno tagliati al laser", "Sagome natalizie in legno tagliate al laser."),
 "cuore-plexiglass-mamma": ("Cuore in plexiglass", "premi-personalizzati", "cuore-plexiglass-inciso-dedica-mamma.webp", "Cuore in plexiglass inciso al laser con dedica su base in legno", "Cuore in plexiglass trasparente con dedica incisa, su base in legno."),
 "targhe-battesimo-legno": ("Targhe per battesimo", "cerimonie-matrimoni-personalizzati", "targhe-battesimo-legno-personalizzate.webp", "Targhe in legno per battesimo con angeli e dedica incisi al laser", "Targhe quadrate in legno con angeli, cuori e nome."),
 "targa-orsetto-samuele": ("Targa con orsetto", "nomi-regali-personalizzati", None, "", "Targa in legno con orsetto e nome, tagliata e incisa al laser."),
 "albero-personalizzato-adam-valentina": ("Adam e Valentina", "cerimonie-matrimoni-personalizzati", "pannello-legno-albero-nomi-matrimonio.webp", "Pannello in legno con albero, nomi e data tagliati al laser", "Albero con nomi, data e cuori tagliato al laser."),
 "taccuino-carnevale": ("Taccuino Carnevale", "gadget-aziendali-personalizzati", "taccuino-copertina-incisa-laser-carnevale.webp", "Taccuino a spirale con copertina incisa al laser a tema Carnevale", "Copertina in cartone incisa con un disegno a tema Carnevale."),
 "scritta-giuseppe-sagomata": ("Scritta Giuseppe", "nomi-regali-personalizzati", "scritta-legno-sagomata-nome-giuseppe.webp", "Scritta in legno sagomata al laser su più livelli con il nome Giuseppe", "Nome sagomato su più livelli."),
 "sagome-cane-gatto": ("Sagome cane e gatto", "sagome-decorazioni-legno", None, "", "Sagome di cane e gatto tagliate al laser in legno."),
 "arcobaleno-dedica-maestra": ("Arcobaleno per la maestra", "nomi-regali-personalizzati", None, "", "Arcobaleno in legno con dedica per la maestra."),
 "carlo-nome-decorativo": ("Nome decorativo Carlo", "nomi-regali-personalizzati", None, "", "Nome decorativo in legno tagliato al laser."),
 "orsetto-dedica-maestre": ("Orsetto con dedica per le maestre", "nomi-regali-personalizzati", None, "", "Orsetto in legno con dedica per le maestre."),
 "albero-nomi-farfalle": ("Albero con nomi e farfalle", "cerimonie-matrimoni-personalizzati", None, "", "Albero in legno con nomi e farfalle tagliati al laser."),
 "marcatura-bicolore-acciaio": ("Marcatura bicolore su acciaio", "marcatura-acciaio", "marcatura-laser-bicolore-acciaio-spazzolato.webp", "Marcatura laser bicolore su acciaio spazzolato", "Due tonalità su acciaio spazzolato."),
 "qr-code-marcatura-laser": ("QR code marcati al laser", "marcatura-laser-personalizzata", "marcatura-laser-qr-code-acciaio.webp", "QR code marcati al laser su lamiera di acciaio", "QR code marcati al laser su lamiera, per targhette e supporti."),
}

for _k,(_t,_d) in SEO_LAVORI.items():
    _w=WORKS[_k]
    WORKS[_k]=(_t.split(":")[0] if False else _t,_w[1],_w[2],_w[3],_d)

ILLUSTRATIVE = {"qr-code-tavolo-legno-trattoria-il-ceppo.webp", "cubi-segnatavolo-legno-qr-italiano.webp", "cassetta-legno-incisa-sparkling-world-stifel.webp",
                "cassetta-vino-legno-incisa-ottavio.webp", "taglieri-legno-personalizzati-logo-casaia.webp", "portachiavi-legno-personalizzati-anniversario.webp"}
POST = {"marcatura-laser-bicolore-acciaio-spazzolato.webp", "marcatura-laser-coltello-acciaio-logo.webp"}


def tg(f):
    return "Ambientazione illustrativa" if f in ILLUSTRATIVE else ("Immagine del post" if f in POST else "Foto originale")


PATHS_EXISTING = {"targhette-industriali-laser": "Targhette industriali", "marcatura-acciaio": "Marcatura acciaio", "incisione-vetro-personalizzata": "Incisione su vetro",
                  "nomi-regali-personalizzati": "Nomi e regali", "gadget-aziendali-personalizzati": "Gadget aziendali", "ristorazione-accoglienza": "Ristoranti e locali",
                  "cassette-legno-personalizzate": "Cassette in legno"}


def add_extra(S, ctas, service, P, D):
    def cat_name(slug):
        return CATS[slug][0] if slug in CATS else PATHS_EXISTING.get(slug, slug)

    # ----- categorie -----
    for slug, (nome, desc, img, alt, rel, cosa) in CATS.items():
        if slug == "fotografia-ballabio":
            continue
        works_html = ""
        rel_cats = [r for r in rel if r in CATS]
        rel = [r for r in rel if r in WORKS]
        if rel_cats:
            works_html += section("Vedi anche", cards([(CATS[r][0], CATS[r][1], f"/{r}/") for r in rel_cats]))
        if rel:
            items = [dict(img=I + WORKS[r][2], alt=WORKS[r][3], tag=tg(WORKS[r][2]), title=WORKS[r][0], text=WORKS[r][4], href=f"/lavori/{r}/") if WORKS[r][2]
                     else None for r in rel]
            with_img = [x for x in items if x]
            if with_img:
                works_html += section("Lavori realizzati", works(with_img), alt=True)
            no_img = [r for r in rel if not WORKS[r][2]]
            if no_img:
                works_html += section("Altri lavori", cards([(WORKS[r][0], WORKS[r][4], f"/lavori/{r}/", "Vedi il lavoro") for r in no_img]))
        body = (section("Cosa realizziamo", '<ul class="list">' + "".join(f"<li>{c}</li>" for c in cosa) + "</ul>"
                        + '<p>Ogni lavoro parte dalla verifica di materiale, misure e file: ti mandiamo una bozza da approvare prima della produzione.</p>') if cosa else "")
        body += works_html
        body += section("Come richiedere un preventivo", '<p>Invia foto o disegno, misure, quantità e, se li hai, i file del logo o dei testi. '
                        'Il preventivo indica lavorazione, costi e tempi. Trovi il metodo completo in <a href="/come-lavoriamo/">come lavoriamo</a> '
                        'e le indicazioni sui file in <a href="/preparare-file-incisione-laser/">preparare il file per il laser</a>.</p>', alt=True)
        S.page(f"/{slug}/", f"{nome} | Progetti Laser", desc, nome, desc, body,
               hero_img=(I + img, alt) if img else None, ctas=ctas(nome), crumbs=[(nome, f"/{slug}/")],
               schema=[service(nome, f"/{slug}/", desc)])

    # ----- lavori -----
    for slug, (titolo, cat, img, alt, testo) in WORKS.items():
        rel_link = (f'<p>Questo lavoro fa parte della categoria <a href="/{cat}/">{cat_name(cat)}</a>.</p>' if cat else "")
        body = section("Il lavoro", f"<p>{testo}</p>{rel_link}<p>Hai un progetto simile? Chiedici un preventivo: partiamo da misure, materiale e file grafico e ti mandiamo una bozza prima di produrre.</p>")
        crumbs = [("Realizzazioni", "/realizzazioni/"), (titolo, f"/lavori/{slug}/")]
        S.page(f"/lavori/{slug}/", f"{titolo} | Progetti Laser", f"{testo} Guarda il lavoro e richiedi una personalizzazione per il tuo progetto."[:158], titolo, testo, body,
               hero_img=(I + img, alt) if img else None, ctas=ctas(cat_name(cat) if cat else "Generico"), crumbs=crumbs)

    # ----- Ballabio (fotografia, Pangea Studio) -----
    S.page("/fotografia-ballabio/", "Fotografia Ballabio · bottiglia e packaging | Progetti Laser",
           "Fotografia di bottiglia e astuccio per Ballabio, realizzata da Pangea Studio: ambientazione e dettaglio del marchio.",
           "Fotografia per Ballabio", "Immagini di bottiglia, astuccio e dettaglio del marchio realizzate da Pangea Studio.",
           section("Le immagini", works([
               dict(img="/photography/fotografia-bottiglia-in-astuccio-ballabio.webp", alt="Fotografia di una bottiglia in astuccio per Ballabio", tag="Foto originale", title="Bottiglia in astuccio", text="Still life della bottiglia con il suo astuccio."),
               dict(img="/photography/fotografia-dettaglio-marchio-ballabio.webp", alt="Dettaglio fotografico del marchio Ballabio", tag="Foto originale", title="Dettaglio del marchio", text="Particolare del marchio su confezione."),
           ])) + section("Altri servizi fotografici", '<p>Fotografia di prodotto, food e packaging: vedi <a href="https://pangeastudio.it/">Pangea Studio</a>.</p>', alt=True),
           ctas=ctas("Altro"), crumbs=[("Fotografia Ballabio", "/fotografia-ballabio/")])

    # ----- hub e servizio -----
    S.page("/progetti-laser/", "Progetti Laser · laboratorio di incisione e taglio laser",
           "Chi siamo: il laboratorio di incisione, taglio e marcatura laser di Pangea Comunicazione a Santa Maria della Versa, in Oltrepò Pavese.",
           "Progetti Laser", "Il laboratorio laser di Pangea Comunicazione: incisione, taglio e marcatura su legno, metallo, plexiglass, vetro e ardesia.",
           section("Il laboratorio", f'<p>Progetti Laser è il laboratorio di incisione e taglio laser di Pangea Comunicazione, in {P["via"]}, {P["cap"]} {P["citta"]} ({P["prov"]}). '
                   'Lavoriamo per aziende, locali, cantine, società sportive e privati, dal pezzo singolo alla serie.</p>'
                   '<p>Fa parte del gruppo Pangea: <a href="https://www.pangeacomunicazione.it/">Pangea Comunicazione</a> per stampa e adesivi, '
                   '<a href="https://pangeastudio.it/">Pangea Studio</a> per grafica e fotografia, <a href="https://insegneinlegno.com/">Insegne in Legno</a> per le insegne.</p>') +
           section("Cosa facciamo", cards([("Aziende e industria", "Targhette con matricola, marcatura su acciaio, gadget.", "/targhette-industriali-laser/"),
                                          ("Locali e cantine", "QR da tavolo, menu, sottobicchieri, cassette.", "/ristorazione-accoglienza/"),
                                          ("Regali e cerimonie", "Nomi, targhe, matrimoni e battesimi.", "/nomi-regali-personalizzati/")]), alt=True),
           ctas=ctas("Generico"), crumbs=[("Progetti Laser", "/progetti-laser/")])

    S.page("/preparare-file-incisione-laser/", "Come preparare il file per l'incisione laser | Progetti Laser",
           "Guida pratica: formati vettoriali, testi, misure e colori per preparare un file di incisione o taglio laser.",
           "Preparare il file per l’incisione laser", "Che cosa inviare per ricevere un preventivo preciso e una bozza corretta.",
           section("Formati", '<ul class="list"><li>Vettoriali: SVG, PDF, AI, EPS o DXF</li><li>Immagini: PNG o JPG ad alta risoluzione, da valutare caso per caso</li><li>Testi: indica il carattere o convertili in tracciati</li><li>Misure reali in millimetri</li></ul>') +
           section("Taglio e incisione", '<ul class="list"><li>Linee di taglio separate dalle aree da incidere</li><li>Nessun tracciato doppio o aperto</li><li>Testi piccoli: verifichiamo la leggibilità sul materiale scelto</li></ul>', alt=True) +
           section("Dati variabili", '<p>Per serie con nomi, numeri o matricole diversi invia un elenco definitivo (foglio di calcolo). Lo controlliamo insieme prima della produzione.</p>'),
           ctas=ctas("Generico"), crumbs=[("Preparare il file", "/preparare-file-incisione-laser/")])

    S.page("/novita-e-lavorazioni/", "Novità e lavorazioni | Progetti Laser",
           "Le ultime lavorazioni del laboratorio Progetti Laser e dove trovarle.",
           "Novità e lavorazioni", "Una selezione dei lavori più recenti con rimando alle pagine di dettaglio.",
           section("Lavori recenti", works([
               dict(img=I + WORKS[k][2], alt=WORKS[k][3], tag=tg(WORKS[k][2]), title=WORKS[k][0], text=WORKS[k][4], href=f"/lavori/{k}/")
               for k in ("renne-decorazione-invernale", "targa-fbc-casteggio", "pannello-cervo-geometrico", "taccuino-carnevale")])) +
           section("Tutte le realizzazioni", '<p><a href="/realizzazioni/">Vai alle realizzazioni →</a></p>', alt=True),
           ctas=ctas("Generico"), crumbs=[("Novità e lavorazioni", "/novita-e-lavorazioni/")])

    # ----- cookie -----
    S.page("/cookie/", "Cookie · Progetti Laser", "Informativa sui cookie del sito Progetti Laser.", "Informativa cookie",
           "Il sito usa solo risorse tecniche.",
           section("Cookie", '<p>Il sito non usa cookie di profilazione né strumenti di analisi o pubblicità. Può essere memorizzata la scelta del tema chiaro/scuro nel browser. '
                   'Il modulo di preventivo prepara un’email nel tuo programma di posta; per i dettagli vedi l’<a href="/privacy/">informativa privacy</a>.</p>'
                   '<p class="note">Aggiornata il 24/11/2026 · testo da validare con il consulente privacy.</p>'),
           crumbs=[("Cookie", "/cookie/")])


REDIRECT_VIDEO = ["ristorazione-accoglienza", "cassette-legno-personalizzate", "taglieri-personalizzati", "nomi-regali-personalizzati", "sagome-decorazioni-legno",
                  "premi-personalizzati", "confezioni-natale-aziende", "ardesia-personalizzata", "incisione-vetro-personalizzata", "targhe-pannelli-legno",
                  "gadget-aziendali-personalizzati", "cerimonie-matrimoni-personalizzati", "targhette-industriali-laser"]


def redirects(domain):
    return "\n# Vecchie pagine /video/*: i filmati non sono nel nuovo sito, reindirizzo alla pagina di categoria\n" + "\n".join(
        f"Redirect 301 /video/{s}/ https://{domain}/{s}/" for s in REDIRECT_VIDEO) + "\n"
