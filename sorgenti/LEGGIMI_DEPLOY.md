# Rifacimento Progetti Laser e Pangea Studio · 24/11/2026

## Struttura
- build/progettilaser/ e build/pangeastudio/: siti statici pronti per Hostinger (URL puliti con barra finale, come gli attuali)
- preview/: copia con link relativi, solo per l'anteprima
- laser.py, studio.py, core.py: sorgenti (testi e pagine). Rigenerare con `python3 laser.py` e `python3 studio.py`
- immagini_da_copiare.txt: percorsi delle immagini usate, da copiare dall'export ChatGPT

## Pagine rifatte (Fase 1)
Progetti Laser: / , /targhette-industriali-laser/, /marcatura-acciaio/, /ristorazione-accoglienza/, /cassette-legno-personalizzate/,
/taglieri-personalizzati/, /gadget-aziendali-personalizzati/, /nomi-regali-personalizzati/, /incisione-vetro-personalizzata/,
/realizzazioni/, /come-lavoriamo/, /preventivo/, /privacy/, /grazie/ (noindex)
Pangea Studio: / , /siti-web/, /siti-web-cantine/, /siti-web-ristoranti/, /seo/, /social-media/, /fotografia/, /portfolio/,
/metodo/, /contatti/, /privacy-policy/, /grazie/ (noindex)

## Pagine NON ancora rifatte (Fase 2) — restano online con il contenuto attuale
Laser: /lavori/*, /sagome-decorazioni-legno/, /premi-personalizzati/, /confezioni-natale-aziende/, /ardesia-personalizzata/,
/targhe-pannelli-legno/, /cerimonie-matrimoni-personalizzati/, /qr-code-tavolo-legno/, /segnaposto-numeri-tavolo-legno/,
/menu-portamenu-legno/, /sottobicchieri-legno/, /banco-punto-vendita/, /preparare-file-incisione-laser/, /novita-e-lavorazioni/,
/oggetti-personalizzati-3d/, /marcatura-laser-personalizzata/, /video/*
Studio: /fotografia-vino/, /fotografia-food-etika/, /fotografia-prodotti/, /portfolio/<progetto>/
Laser, anche: /stopper-espositori-legno/, /incisione-coperchi-legno-conto-terzi/, /tessere-legno-personalizzate/, /fotografia-ballabio/, /progetti-laser/, /cookie/.
Nessun URL viene eliminato: nessun redirect necessario in Fase 1. La sitemap nuova contiene TUTTI gli URL attuali (Laser 93, Studio 16).

## Pubblicazione consigliata (Hostinger, hosting classico)
1. Scaricare l'export completo del sito attuale (ZIP ChatGPT) = backup e base.
2. Estrarre l'export, poi copiare SOPRA il contenuto di build/<sito>/. Sovrascrive solo le pagine rifatte e sitemap/robots.
   CSS e font hanno nomi nuovi (/assets/<sito>-20261124.css, /assets/fonts-<sito>/): non toccano lo stile delle pagine Fase 2.
   NON sovrascrivere il .htaccess: unire a mano le regole di htaccess-da-unire.txt. 404-nuovo.html è separato dalla 404 attuale.
3. Verificare che i file in immagini_da_copiare.txt esistano con lo stesso nome (alcuni nomi sono da confermare: se manca, la scheda mostra una didascalia al posto della foto).
4. Caricare su un sottodominio di prova (es. nuovo.progettilaser.it) → test form FormSubmit con invio autorizzato → controllo mobile.
5. Solo dopo OK di Walter: puntare il dominio (DNS) mantenendo MX/SPF/DKIM invariati. Inviare sitemap in Search Console.

## Da fare prima della messa online
- Confermare i nomi file immagine (lista allegata).
- Primo invio FormSubmit: arriva una mail di attivazione a pangea@ da confermare.
- Decisione GA4 (una sola per dominio): le pagine Fase 2 e /cookie/ attuali usano GA4 con consenso; le pagine nuove non caricano GA4.
  La privacy nuova è coerente con questo (GA4 solo con consenso). Opzione consigliata: inserire GA4 + banner anche nelle pagine nuove quando c'è l'accesso.
- Far validare il testo privacy.
- Studio: le anteprime portfolio vengono da mShots (servizio esterno): meglio sostituirle con screenshot salvati in /portfolio/.
