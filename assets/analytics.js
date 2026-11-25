(function(){
var ID='G-0NF5P5ZGFE',K='pangea_studio_analytics_consent_v1',D=15552000;
if(location.hostname!=='pangeastudio.it')return;
function get(){var m=document.cookie.match('(?:^|; )'+K+'=([^;]*)');return m?m[1]:null}
function set(v){document.cookie=K+'='+v+'; Max-Age='+D+'; Path=/; SameSite=Lax; Secure'}
function load(){
if(document.getElementById('studio-ga4'))return;
window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};
gtag('consent','default',{analytics_storage:'denied',ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied'});
gtag('consent','update',{analytics_storage:'granted'});
gtag('js',new Date());
gtag('config',ID,{page_path:location.pathname,page_location:location.origin+location.pathname,page_referrer:'',allow_google_signals:false,allow_ad_personalization_signals:false,cookie_expires:D,cookie_flags:'SameSite=Lax;Secure'});
var s=document.createElement('script');s.id='studio-ga4';s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id='+ID;document.head.appendChild(s);
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;var h=a.getAttribute('href')||'',m=h.indexOf('tel:')==0?'phone':h.indexOf('mailto:')==0?'email':/^https:\/\/(wa\.me|api\.whatsapp\.com)\//.test(h)?'whatsapp':null;if(m)gtag('event','contact_click',{contact_method:m,page_path:location.pathname})});
}
function revoke(){
window['ga-disable-'+ID]=true;
document.cookie.split(';').forEach(function(c){var n=c.split('=')[0].trim();if(n==='_ga'||n.indexOf('_ga_')===0){['','; Domain=pangeastudio.it','; Domain=.pangeastudio.it'].forEach(function(d){document.cookie=n+'=; Max-Age=0; Path=/'+d+'; Secure; SameSite=Lax'})}});
}
function panel(){
var p=document.createElement('aside');p.setAttribute('aria-label','Preferenze statistiche');
p.style.cssText='position:fixed;left:16px;right:16px;bottom:16px;max-width:520px;z-index:9999;background:#fff;color:#111;border:1px solid #ccc;border-radius:12px;padding:16px;box-shadow:0 8px 30px rgba(0,0,0,.2);font:15px/1.45 system-ui,sans-serif';
p.innerHTML='<b>Cookie e privacy</b><p style="margin:8px 0">Con il tuo consenso usiamo Google Analytics per statistiche di navigazione e clic sui contatti. La scelta dura 180 giorni. Il modulo funziona anche se rifiuti. <a href="/privacy-policy/">Informativa</a>.</p><div style="display:flex;gap:8px;flex-wrap:wrap"><button type="button" data-v="rejected" style="padding:10px 14px;border:1px solid #111;background:#fff;color:#111;border-radius:8px;cursor:pointer">Rifiuta non necessari</button><button type="button" data-v="accepted" style="padding:10px 14px;border:1px solid #111;background:#111;color:#fff;border-radius:8px;cursor:pointer">Accetta statistiche</button></div>';
p.addEventListener('click',function(e){var v=e.target.getAttribute&&e.target.getAttribute('data-v');if(!v)return;var was=get();set(v);p.remove();if(v==='accepted')load();else if(was==='accepted'){revoke();location.reload()}});
document.body.appendChild(p);
}
function pref(){var b=document.createElement('button');b.type='button';b.textContent='Preferenze cookie';b.style.cssText='position:fixed;left:12px;bottom:12px;z-index:9998;font:13px system-ui,sans-serif;padding:6px 10px;border:1px solid #888;background:#fff;color:#111;border-radius:8px;cursor:pointer;opacity:.85';b.onclick=function(){if(!document.querySelector('aside[aria-label="Preferenze statistiche"]'))panel()};document.body.appendChild(b)}
function init(){pref();var c=get();if(c==='accepted')load();else if(!c)panel()}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
