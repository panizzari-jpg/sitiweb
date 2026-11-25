/* Statistiche anonime (Google Analytics 4) caricate solo dopo il consenso. */
(function () {
  var GA_ID = "G-WQFK7NNRJF";
  var KEY = "pl_stats_consent";
  function get() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function set(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  function load() {
    if (window.__plGaLoaded) return;
    window.__plGaLoaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    gtag("consent", "default", { analytics_storage: "granted", ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied" });
    gtag("js", new Date());
    gtag("config", GA_ID, { anonymize_ip: true, allow_google_signals: false, allow_ad_personalization_signals: false });
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_ID;
    document.head.appendChild(s);
  }
  function removeBanner() { var b = document.getElementById("pl-consent"); if (b) b.remove(); }
  function banner() {
    if (document.getElementById("pl-consent")) return;
    var d = document.createElement("div");
    d.id = "pl-consent";
    d.setAttribute("role", "dialog");
    d.setAttribute("aria-label", "Statistiche di visita");
    d.style.cssText = "position:fixed;left:12px;right:12px;bottom:12px;z-index:99999;max-width:560px;margin:0 auto;background:#1f1a16;color:#fff;padding:14px 16px;border-radius:10px;box-shadow:0 4px 18px rgba(0,0,0,.35);font:15px/1.4 system-ui,sans-serif";
    d.innerHTML = '<p style="margin:0 0 10px">Usiamo statistiche anonime di visita (Google Analytics) solo se acconsenti. Nessuna pubblicità né profilazione. <a href="/cookie/" style="color:#fff;text-decoration:underline">Dettagli</a></p>' +
      '<button type="button" id="pl-yes" style="margin-right:8px;padding:9px 16px;border:0;border-radius:6px;background:#fff;color:#1f1a16;font:inherit;font-weight:600;cursor:pointer">Accetta</button>' +
      '<button type="button" id="pl-no" style="padding:9px 16px;border:1px solid #fff;border-radius:6px;background:transparent;color:#fff;font:inherit;cursor:pointer">Rifiuta</button>';
    document.body.appendChild(d);
    document.getElementById("pl-yes").onclick = function () { set("yes"); removeBanner(); load(); };
    document.getElementById("pl-no").onclick = function () { set("no"); removeBanner(); };
  }
  window.plStatsReset = function () { set(""); try { localStorage.removeItem(KEY); } catch (e) {} banner(); };
  function init() {
    var c = get();
    if (c === "yes") load(); else if (c !== "no") banner();
    var link = document.getElementById("pl-stats-reset");
    if (link) link.onclick = function (e) { e.preventDefault(); window.plStatsReset(); };
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
