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
p.style.cssText='position:fixed;left:10px;bottom:10px;max-width:340px;z-index:9999;background:#fff;color:#222;border:1px solid #ddd;border-radius:10px;padding:10px 12px;box-shadow:0 2px 12px rgba(0,0,0,.12);font:13px/1.4 system-ui,sans-serif';
var bs='padding:6px 12px;border:1px solid #222;border-radius:6px;cursor:pointer;font:inherit;background:#fff;color:#222';
p.innerHTML='<span>Statistiche anonime con Google Analytics, solo se acconsenti. <a href="/privacy-policy/" style="color:inherit">Info</a></span><div style="display:flex;gap:8px;margin-top:8px"><button type="button" data-v="rejected" style="'+bs+'">No grazie</button><button type="button" data-v="accepted" style="'+bs+'">Ok</button></div>';
p.addEventListener('click',function(e){var v=e.target.getAttribute&&e.target.getAttribute('data-v');if(!v)return;var was=get();set(v);p.remove();if(v==='accepted')load();else if(was==='accepted'){revoke();location.reload()}});
document.body.appendChild(p);
}
function pref(){
var open=function(e){if(e)e.preventDefault();if(!document.querySelector('aside[aria-label="Preferenze statistiche"]'))panel()};
var f=document.querySelector('footer');
if(f){var a=document.createElement('a');a.href='#preferenze-cookie';a.textContent='Preferenze cookie';a.style.cssText='display:inline-block;margin:6px 0;font-size:13px;color:inherit;opacity:.75';a.onclick=open;f.appendChild(a)}
}
function init(){pref();var c=get();if(c==='accepted')load();else if(!c)panel()}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
