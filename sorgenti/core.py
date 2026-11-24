"""Generatore statico condiviso per i siti Pangea (Progetti Laser, Pangea Studio).
Produce: build/<sito>/ (URL puliti, per Hostinger) e preview/<sito>/ (link relativi a index.html, per anteprima)."""
import json, os, re, shutil, html
from pathlib import Path

ROOT = Path(__file__).parent
FONTS = ROOT / "_fonts/node_modules/@fontsource"
E = html.escape

PANGEA = dict(
    tel="0385 320302", tel_href="+390385320302", wa="https://wa.me/390385320302",
    email="pangea@pangeacomunicazione.it", via="Via XXV Aprile, 7", cap="27047",
    citta="Santa Maria della Versa", prov="PV", piva="02772420184",
    ragione="Pangea Comunicazione",
)

BASE_CSS = r"""
:root{color-scheme:light dark}
*{box-sizing:border-box;min-width:0}
html{scroll-padding-top:84px;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 var(--fb);overflow-x:clip}
img{max-width:100%;height:auto;display:block}
a{color:var(--link)}a:hover{text-decoration-thickness:2px}
:focus-visible{outline:3px solid var(--acc);outline-offset:3px;border-radius:4px}
h1,h2,h3{font-family:var(--fh);line-height:1.08;text-wrap:balance;margin:0 0 .5em;color:var(--head)}
h1{font-size:clamp(32px,4.6vw,54px);font-weight:700;letter-spacing:-.02em}
h2{font-size:clamp(26px,3vw,38px);font-weight:700;letter-spacing:-.015em}
h3{font-size:20px;font-weight:700;line-height:1.25}
p{margin:0 0 1em;max-width:68ch}
.wrap{max-width:1240px;margin:0 auto;padding:0 max(5vw,18px)}
.band{padding:clamp(44px,6vw,88px) 0}
.alt{background:var(--sup)}
.skip{position:absolute;left:-999px;top:8px;background:var(--acc);color:#fff;padding:10px 14px;z-index:9}
.skip:focus{left:8px}
/* header */
.top{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;gap:20px;min-height:68px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--head);font:800 19px/1 var(--fh)}
.brand img{height:36px;width:auto;max-width:240px}
@media(prefers-color-scheme:dark){:root:not([data-theme=light]) .brand img{background:#fff;padding:4px 8px;border-radius:8px;box-sizing:content-box}}
:root[data-theme=dark] .brand img{background:#fff;padding:4px 8px;border-radius:8px;box-sizing:content-box}
.nav{margin-left:auto;display:flex;gap:4px;align-items:center}
.nav a{color:var(--ink);text-decoration:none;padding:10px 11px;border-radius:8px;font-size:15.5px;white-space:nowrap}
.nav a:hover,.nav a[aria-current]{background:var(--sup)}
.nav .btn{margin-left:8px}
.nav .btn.b1{color:var(--onacc)}.nav .btn.b1:hover{background:var(--acc2)}
.menu{display:none;margin-left:auto}
.menu summary{list-style:none;cursor:pointer;padding:10px 14px;border:1px solid var(--line);border-radius:10px;font-weight:600;min-height:44px;display:flex;align-items:center}
.menu summary::-webkit-details-marker{display:none}
.menu[open] .drop{display:grid}
.drop{display:none;position:absolute;left:0;right:0;top:68px;background:var(--bg);border-bottom:1px solid var(--line);padding:8px max(5vw,18px) 18px;gap:2px}
.drop a{padding:13px 4px;border-bottom:1px solid var(--line);color:var(--ink);text-decoration:none;font-size:17px}
@media(max-width:1020px){.nav{display:none}.menu{display:block}}
/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:48px;padding:12px 22px;border-radius:4px;font:700 16px/1.1 var(--fb);text-decoration:none;border:2px solid transparent;cursor:pointer;transition:transform .12s ease-out,background .15s}
.btn:active{transform:scale(.97)}
.b1{background:var(--acc);color:var(--onacc)}.b1:hover{background:var(--acc2)}
.b2{background:transparent;color:inherit;border-color:currentColor}
.nav .btn{min-height:42px;padding:9px 16px;font-size:15px}
.ctas{display:flex;flex-wrap:wrap;gap:12px;margin-top:22px}
/* hero foto: foto in trasparenza con titolo sopra */
.hero.photo{position:relative;overflow:hidden;background:var(--dom);min-height:clamp(420px,58vh,580px);display:flex;align-items:center;isolation:isolate}
.hero.photo .bgimg{position:absolute;inset:-4% 0;width:100%;height:108%;object-fit:cover;object-position:center 40%;z-index:-2;opacity:.55;animation:kb 18s ease-out both}
.hero.photo::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(100deg,color-mix(in srgb,var(--dom) 92%,transparent) 0%,color-mix(in srgb,var(--dom) 70%,transparent) 50%,color-mix(in srgb,var(--dom) 35%,transparent) 100%)}
.hero.photo::after{content:"";position:absolute;inset:0;z-index:-1;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:48px 48px;mask-image:linear-gradient(90deg,transparent,#000 60%)}
.hero.photo .wrap{display:block;width:100%;padding-top:clamp(40px,6vw,72px);padding-bottom:clamp(40px,6vw,72px)}
.hero.photo .htxt{max-width:700px}
.hero.photo h1,.hero.photo .lead,.hero.photo .crumb,.hero.photo .proof{color:#fff}
.hero.photo .b2{color:#fff}
.hero .htxt>*{animation:up .7s cubic-bezier(.2,.7,.2,1) both}
.hero .htxt>*:nth-child(2){animation-delay:.08s}.hero .htxt>*:nth-child(3){animation-delay:.16s}.hero .htxt>*:nth-child(4){animation-delay:.24s}.hero .htxt>*:nth-child(5){animation-delay:.32s}
.scan{position:absolute;left:0;right:0;top:0;height:2px;background:linear-gradient(90deg,transparent,var(--acc) 30%,#fff 50%,var(--acc) 70%,transparent);box-shadow:0 0 18px 2px var(--acc);opacity:.85;z-index:0;animation:scan 5.5s cubic-bezier(.45,0,.55,1) infinite}
@keyframes up{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
@keyframes kb{from{transform:scale(1.08)}to{transform:scale(1)}}
@keyframes scan{0%{top:6%;opacity:0}10%{opacity:.85}90%{opacity:.85}100%{top:94%;opacity:0}}
.hero.solo .wrap{grid-template-columns:1fr}.hero.solo .htxt{max-width:760px}
.lead2{font-size:19px;line-height:1.6;max-width:72ch}
.cols2{columns:2 320px;column-gap:48px}.cols2 p{break-inside:avoid}
/* look tecnico */
.band h2::before{content:"";display:block;width:36px;height:3px;background:var(--acc);margin-bottom:16px}
.alt{background-color:var(--sup);background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);background-size:40px 40px}
.card{transition:transform .25s cubic-bezier(.2,.7,.2,1),box-shadow .25s,border-color .2s}
a.card:hover{transform:translateY(-4px);box-shadow:0 14px 34px rgba(10,20,30,.12);border-color:var(--acc)}
a.card .more{transition:letter-spacing .2s}a.card:hover .more{letter-spacing:.02em}
.work{transition:transform .25s cubic-bezier(.2,.7,.2,1),box-shadow .25s}.work:hover{transform:translateY(-4px);box-shadow:0 14px 34px rgba(10,20,30,.14)}
.work .ph img{transition:transform .6s cubic-bezier(.2,.7,.2,1)}.work:hover .ph img{transform:scale(1.05)}
.rv{opacity:0;transform:translateY(22px);transition:opacity .7s cubic-bezier(.2,.7,.2,1),transform .7s cubic-bezier(.2,.7,.2,1)}
.rv.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.rv{opacity:1;transform:none}.scan{display:none}.hero.photo .bgimg{animation:none}}
/* hero */
.hero{background:var(--dom);color:var(--ondom)}
.hero h1,.hero h2{color:var(--ondom)}
.hero .wrap{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:clamp(24px,4vw,56px);align-items:center;padding-top:clamp(36px,5vw,72px);padding-bottom:clamp(36px,5vw,72px)}
.hero .lead{font-size:clamp(18px,1.6vw,20px);opacity:.92}
.hero .b2{color:var(--ondom)}
.hero .fig{aspect-ratio:5/4;width:100%}
.hero .fig svg{width:100%;height:100%;display:block}
.hero .fig .ph{height:100%;aspect-ratio:auto;border-radius:16px;box-shadow:0 18px 40px rgba(0,0,0,.28)}
.hero .ph.noimg::after{color:var(--ondom);background:repeating-linear-gradient(135deg,transparent 0 14px,rgba(255,255,255,.07) 14px 15px),color-mix(in srgb,var(--ondom) 10%,var(--dom))}
.proof{margin-top:22px;font-size:15px;opacity:.85;border-top:1px solid color-mix(in srgb,var(--ondom) 25%,transparent);padding-top:14px}
.crumb{font-size:14px;opacity:.85;margin-bottom:14px}.crumb a{color:inherit}
@media(max-width:820px){.hero .wrap{grid-template-columns:1fr}.hero .fig{max-width:520px;aspect-ratio:16/11}}
/* grids */
.grid{display:grid;gap:18px;grid-template-columns:repeat(auto-fill,minmax(min(100%,270px),1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:6px;padding:24px;display:flex;flex-direction:column;gap:6px;text-decoration:none;color:var(--ink);transition:transform .15s ease-out,border-color .15s}
a.card:hover{border-color:var(--ink)}
.card h3{margin:0 0 4px}.card p{margin:0;font-size:16px}
.card .more{margin-top:auto;padding-top:10px;font-weight:700;color:var(--link);font-size:15px}
.two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(24px,4vw,56px);align-items:start}
@media(max-width:820px){.two{grid-template-columns:1fr}}
.list{padding-left:1.1em;margin:0 0 1em}.list li{margin:.35em 0}
.note{font-size:15px;color:var(--mute)}
/* steps */
.steps{counter-reset:s;display:grid;gap:18px;grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr));padding:0;list-style:none}
.steps li{counter-increment:s;border-top:1px solid var(--line2);padding-top:16px}
.steps li::before{content:counter(s);font:600 15px/1 var(--fb);color:var(--mute);display:block;margin-bottom:10px}
.steps b{display:block;font-family:var(--fh);font-size:19px;margin-bottom:4px;color:var(--head)}
/* works */
.works{display:grid;gap:20px;grid-template-columns:repeat(auto-fill,minmax(min(100%,280px),1fr))}
.work{margin:0;background:var(--card);border:1px solid var(--line);border-radius:6px;overflow:hidden;display:flex;flex-direction:column}
.ph{position:relative;aspect-ratio:4/3;background:var(--phbg);overflow:hidden}
.ph img{width:100%;height:100%;object-fit:cover}
.ph.noimg img{display:none}
.ph.noimg::after{content:attr(data-alt);position:absolute;inset:0;display:flex;align-items:flex-end;padding:16px;font:600 15px/1.35 var(--fb);color:var(--phink);background:repeating-linear-gradient(135deg,transparent 0 14px,color-mix(in srgb,var(--phink) 8%,transparent) 14px 15px)}
.tag{position:absolute;top:10px;left:10px;background:rgba(255,255,255,.92);color:#222;font-size:12.5px;font-weight:600;padding:3px 8px;border-radius:3px;z-index:1}
.tag.real{background:rgba(255,255,255,.92);color:#222}
.work figcaption{padding:16px 18px 18px}.work figcaption b{display:block;font-family:var(--fh);font-size:18px;color:var(--head)}
.work figcaption span{font-size:15.5px;color:var(--mute)}
.work figcaption a{font-weight:700;font-size:15px}
/* faq */
.faq details{border-bottom:1px solid var(--line);padding:4px 0}
.faq summary{cursor:pointer;font:700 18px/1.35 var(--fh);padding:14px 30px 14px 0;position:relative;list-style:none;color:var(--head)}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";position:absolute;right:4px;top:10px;font-size:26px;color:var(--acc)}
.faq details[open] summary::after{content:"–"}
.faq details p{margin:0 0 16px}
/* cta band */
.ctaband{background:var(--dom);color:var(--ondom)}
.ctaband h2{color:var(--ondom)}
.ctaband .wrap{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:28px;align-items:center}
.ctaband .b2{color:var(--ondom)}
.contact{font-size:17px;line-height:1.9}.contact a{color:var(--ondom)}
@media(max-width:820px){.ctaband .wrap{grid-template-columns:1fr}}
/* form */
form.f{display:grid;gap:16px;max-width:760px}
.f .row{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:600px){.f .row{grid-template-columns:1fr}}
.f label{display:grid;gap:6px;font-weight:600;font-size:15.5px}
.f input,.f select,.f textarea{font:16px/1.4 var(--fb);padding:12px 13px;border:1px solid var(--line2);border-radius:10px;background:var(--card);color:var(--ink);min-height:48px;width:100%}
.f textarea{min-height:140px;resize:vertical}
.f .chk{display:flex;gap:10px;align-items:flex-start;font-weight:400}
.f .chk input{width:22px;min-height:22px;margin-top:3px;flex:none}
.f .hp{position:absolute;left:-5000px}
.f .msg{padding:14px;border-radius:10px;background:var(--sup);display:none}
/* footer */
footer{background:var(--foot);color:var(--onfoot);font-size:15.5px;padding:48px 0 28px}
footer a{color:var(--onfoot)}
footer .cols{display:grid;gap:28px;grid-template-columns:repeat(auto-fit,minmax(min(100%,210px),1fr))}
footer h2{font-size:17px;color:var(--onfoot);margin-bottom:10px}
footer ul{list-style:none;padding:0;margin:0}footer li{margin:6px 0}
footer .legal{margin-top:32px;padding-top:16px;border-top:1px solid color-mix(in srgb,var(--onfoot) 20%,transparent);opacity:.8;font-size:14px}
@media(max-width:820px){footer{padding-bottom:96px}.hero .fig{margin-bottom:28px}}
footer li a{display:inline-block;padding:4px 0}
.wa{position:fixed;right:16px;bottom:16px;z-index:6;background:#15693a;color:#fff;border-radius:4px;padding:11px 15px;font-weight:600;text-decoration:none;box-shadow:0 4px 14px rgba(0,0,0,.2);font-size:14.5px}
@media(prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
"""

SCRIPT = r"""<script>{
for(const b of document.querySelectorAll('.brand img')){const h=()=>b.style.display='none';if(b.complete&&!b.naturalWidth)h();b.addEventListener('error',h)}
for(const p of document.querySelectorAll('.ph img')){const f=()=>p.parentNode.classList.add('noimg');if(p.complete&&!p.naturalWidth)f();p.addEventListener('error',f)}
if('IntersectionObserver' in window&&!matchMedia('(prefers-reduced-motion: reduce)').matches){const io=new IntersectionObserver(es=>{for(const e of es)if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}},{rootMargin:'0px 0px -8% 0px'});document.querySelectorAll('main .band .wrap>*:not(h2), .card, .work, .steps li').forEach((el,i)=>{el.classList.add('rv');el.style.transitionDelay=(i%4)*60+'ms';io.observe(el)})}
const live=/(^|\.)(progettilaser\.it|pangeastudio\.it)$/.test(location.hostname);
for(const fm of document.querySelectorAll('form.f')){
 const q=new URLSearchParams(location.search),s=fm.querySelector('[data-pre]');
 if(s&&q.get(s.dataset.pre)){for(const o of s.options)if(o.value===q.get(s.dataset.pre))o.selected=true}
 if(!live)fm.addEventListener('submit',e=>{e.preventDefault();const m=fm.querySelector('.msg');m.style.display='block';m.textContent='Anteprima: l’invio è disattivato. Sul sito pubblicato il modulo arriva a pangea@pangeacomunicazione.it.'})
}}</script>"""


def font_css(site_fonts):
    out = []
    for fam, pkg, weights in site_fonts:
        for w in weights:
            out.append(f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{w};font-display:swap;src:url(fonts-KEY/{pkg}-latin-{w}-normal.woff2) format('woff2')}}")
    return "\n".join(out)


def ph(img, alt, tag=None, real=False):
    t = f'<span class="tag{" real" if real else ""}">{E(tag)}</span>' if tag else ""
    return f'<div class="ph" data-alt="{E(alt)}">{t}<img src="{E(img)}" alt="{E(alt)}" width="800" height="600" loading="lazy" decoding="async"></div>'


def works(items):
    out = []
    for w in items:
        real = w.get("tag") == "Foto originale"
        link = f'<br><a href="{w["href"]}">{E(w.get("cta","Vedi il lavoro"))}</a>' if w.get("href") else ""
        out.append(f'<figure class="work">{ph(w["img"], w["alt"], w.get("tag"), real)}<figcaption><b>{E(w["title"])}</b><span>{w["text"]}</span>{link}</figcaption></figure>')
    return '<div class="works">' + "".join(out) + "</div>"


def cards(items):
    out = []
    for i in items:
        t, d = i[0], i[1]
        h = i[2] if len(i) > 2 else None
        m = i[3] if len(i) > 3 else "Scopri"
        out.append(f'<a class="card" href="{h}"><h3>{E(t)}</h3><p>{d}</p><span class="more">{E(m)} →</span></a>' if h else f'<div class="card"><h3>{E(t)}</h3><p>{d}</p></div>')
    return '<div class="grid">' + "".join(out) + "</div>"


def steps(items):
    return '<ol class="steps">' + "".join(f"<li><b>{E(t)}</b>{d}</li>" for t, d in items) + "</ol>"


def faq(items):
    return '<div class="faq">' + "".join(f"<details><summary>{E(q)}</summary><p>{a}</p></details>" for q, a in items) + "</div>"


def faq_schema(items):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in items]}


def section(title, body, alt=False, intro=None, id=None):
    i = f'<p class="lead">{intro}</p>' if intro else ""
    return f'<section class="band{" alt" if alt else ""}"{f" id={chr(34)}{id}{chr(34)}" if id else ""}><div class="wrap"><h2>{E(title)}</h2>{i}{body}</div></section>'


class Site:
    def __init__(self, key, domain, name, nav, css_vars, fonts, footer_html, logo, org_schema, ctaband, keep_urls=()):
        self.keep_urls = list(keep_urls)
        self.scan = False
        from PIL import Image as _I
        _p = ROOT / 'asset_originali' / key / logo.lstrip('/')
        self.logo_w = round(_I.open(_p).size[0] * 36 / _I.open(_p).size[1]) if _p.exists() else 120
        self.key, self.domain, self.name, self.nav = key, domain, name, nav
        self.css_vars, self.fonts, self.footer_html, self.logo = css_vars, fonts, footer_html, logo
        self.org_schema, self.ctaband = org_schema, ctaband
        self.pages = []

    def page(self, path, title, desc, h1, lead, body, picture="", ctas="", proof="", crumbs=None, schema=None, noindex=False, hero_img=None):
        self.pages.append(dict(path=path, title=title, desc=desc, h1=h1, lead=lead, body=body, picture=picture, ctas=ctas, proof=proof, crumbs=crumbs, schema=schema or [], noindex=noindex, hero_img=hero_img))

    def icons(self):
        d = ROOT / 'asset_originali' / self.key
        if (d / 'favicon.ico').exists():
            return ('<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" href="/favicon.svg" type="image/svg+xml">'
                    '<link rel="icon" href="/icon-192.png" type="image/png" sizes="192x192"><link rel="apple-touch-icon" href="/apple-touch-icon.png">')
        return f'<link rel="icon" href="{self.logo}">'

    def render(self, p):
        url = f"https://{self.domain}{p['path']}"
        navh = "".join(f'<a href="{h}"{" aria-current=page" if h == p["path"] else ""}>{E(t)}</a>' for t, h in self.nav[:-1])
        ct, ch = self.nav[-1]
        drop = "".join(f'<a href="{h}">{E(t)}</a>' for t, h in self.nav)
        crumbs = ""
        graph = [self.org_schema]
        if p["crumbs"]:
            trail = [("Home", "/")] + p["crumbs"]
            crumbs = '<nav class="crumb" aria-label="Percorso">' + " / ".join(f'<a href="{h}">{E(t)}</a>' if i < len(trail) - 1 else E(t) for i, (t, h) in enumerate(trail)) + "</nav>"
            graph.append({"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": t, "item": f"https://{self.domain}{h}"} for i, (t, h) in enumerate(trail)]})
        graph += p["schema"]
        ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
        pic = f'<div class="fig">{p["picture"]}</div>' if p["picture"] else ""
        hi = p.get("hero_img")
        if hi:
            pic = ""
            herobg = f'<img class="bgimg" src="{E(hi[0])}" alt="{E(hi[1])}" fetchpriority="high" decoding="async" width="1600" height="1000">'
            herocls = "hero photo"
            herobg += '<span class="scan" aria-hidden="true"></span>' if self.scan else ''
        else:
            herobg, herocls = "", "hero" + ("" if p["picture"] else " solo")
        robots = '<meta name="robots" content="noindex">' if p["noindex"] else ""
        return f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(p['title'])}</title>
<meta name="description" content="{E(p['desc'])}">
<link rel="canonical" href="{url}">{robots}
<meta property="og:type" content="website"><meta property="og:locale" content="it_IT">
<meta property="og:title" content="{E(p['title'])}"><meta property="og:description" content="{E(p['desc'])}">
<meta property="og:url" content="{url}"><meta property="og:image" content="https://{self.domain}{(p.get("hero_img") or (self.logo,))[0]}">
{self.icons()}
<link rel="preload" href="/assets/fonts-{self.key}/{self.fonts[0][1]}-latin-{self.fonts[0][2][-1]}-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/{self.key}-20261124.css">
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">Vai al contenuto</a>
<header class="top"><div class="wrap">
<a class="brand" href="/"><img src="{self.logo}" alt="{E(self.name)}" height="36" width="{self.logo_w}"></a>
<nav class="nav" aria-label="Principale">{navh}<a class="btn b1" href="{ch}">{E(ct)}</a></nav>
<details class="menu"><summary aria-label="Menu principale">Menu</summary><nav class="drop" aria-label="Menu mobile">{drop}</nav></details>
</div></header>
<main id="main">
<section class="{herocls}">{herobg}<div class="wrap"><div class="htxt">{crumbs}<h1>{p['h1']}</h1><p class="lead">{p['lead']}</p>{p['ctas']}{p['proof']}</div>{pic}</div></section>
{p['body']}
{self.ctaband}
</main>
{self.footer_html}
<a class="wa" href="{PANGEA['wa']}" rel="noopener">WhatsApp</a>
{SCRIPT}
</body>
</html>"""

    def build(self):
        out = ROOT / "build" / self.key
        if out.exists():
            shutil.rmtree(out)
        (out / "assets").mkdir(parents=True)
        (out / f"assets/fonts-{self.key}").mkdir()
        for fam, pkg, weights in self.fonts:
            for w in weights:
                shutil.copy(FONTS / pkg / "files" / f"{pkg}-latin-{w}-normal.woff2", out / f"assets/fonts-{self.key}")
        (out / f"assets/{self.key}-20261124.css").write_text(font_css(self.fonts).replace("KEY", self.key) + "\n" + self.css_vars + BASE_CSS)
        src = ROOT / 'asset_originali' / self.key
        if src.exists():
            shutil.copytree(src, out, dirs_exist_ok=True)
        urls, imgs = [], {}
        for p in self.pages:
            d = out / p["path"].strip("/")
            d.mkdir(parents=True, exist_ok=True)
            h = self.render(p)
            (d / "index.html").write_text(h)
            if not p["noindex"]:
                urls.append(p['path'])
                imgs[p['path']] = sorted({m for m in re.findall(r'<img[^>]+src="(/(?:images|portfolio|photography)/[^"]+)"', h)})
        urls += [u for u in self.keep_urls if u not in urls]
        def entry(u):
            im = "".join(f"<image:image><image:loc>https://{self.domain}{i}</image:loc></image:image>" for i in imgs.get(u, []))
            return f"<url><loc>https://{self.domain}{u}</loc>{im}</url>\n"
        (out / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + "".join(entry(u) for u in urls) + "</urlset>\n")
        (out / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: https://{self.domain}/sitemap.xml\n")
        (out / "htaccess-da-unire.txt").write_text(HTACCESS.replace("DOMAIN", self.domain))
        (out / "404-nuovo.html").write_text(self.render(dict(path="/404/", title=f"Pagina non trovata · {self.name}", desc="Pagina non trovata", h1="Pagina non trovata", lead="L’indirizzo non esiste o è stato spostato. Usa il menu o torna alla home.", body="", picture="", ctas='<div class="ctas"><a class="btn b1" href="/">Torna alla home</a></div>', proof="", crumbs=None, schema=[], noindex=True)).replace('<link rel="canonical" href="https://' + self.domain + '/404/">', "").replace(f'<meta property="og:url" content="https://{self.domain}/404/">', ""))
        return out


HTACCESS = r"""# Generato per Hostinger (Apache/LiteSpeed)
Options -Indexes
DirectoryIndex index.html
ErrorDocument 404 /404-nuovo.html
RewriteEngine On
# HTTPS e dominio senza www
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} ^www\. [NC]
RewriteRule ^ https://DOMAIN%{REQUEST_URI} [L,R=301,NE]
# Barra finale sugli URL di cartella (come il sito attuale)
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_URI} !/$
RewriteCond %{REQUEST_FILENAME}/ -d
RewriteRule ^(.*)$ /$1/ [L,R=301]
# Unire queste regole al .htaccess esistente dell'export, senza sovrascriverlo.
# Se Hostinger ha 'Forza HTTPS' attivo in hPanel, togliere la condizione HTTPS e tenere solo www -> senza www.
# Redirect 301 uno-a-uno: aggiungere qui eventuali URL dismessi
# Redirect 301 /vecchio-url/ /nuovo-url/
<IfModule mod_headers.c>
Header set X-Content-Type-Options "nosniff"
Header set Referrer-Policy "strict-origin-when-cross-origin"
Header set X-Frame-Options "SAMEORIGIN"
</IfModule>
<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType text/css "access plus 1 month"
ExpiresByType font/woff2 "access plus 1 year"
ExpiresByType image/webp "access plus 1 month"
ExpiresByType image/png "access plus 1 month"
</IfModule>
"""


def make_preview(build_dir, key):
    """Copia la build e riscrive i link root-relativi in relativi (…/index.html) per l'anteprima artifact."""
    prev = ROOT / "preview" / key
    if prev.exists():
        shutil.rmtree(prev)
    shutil.copytree(build_dir, prev)
    for f in prev.rglob("*.html"):
        depth = len(f.relative_to(prev).parts) - 1
        up = "../" * depth or "./"
        s = f.read_text()

        def fix(m):
            attr, q, path = m.group(1), m.group(2), m.group(3)
            p, _, frag = path.partition("#")
            p, _, qs = p.partition("?")
            if p.endswith("/"):
                p = p + "index.html"
            new = up + p.lstrip("/")
            if frag:
                new += "#" + frag
            return f"{attr}={q}{new}"
        s = re.sub(r'(href|src)=(["\'])(/(?!/)[^"\']*)', fix, s)
        f.write_text(s)
    return prev
