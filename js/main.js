// Baiata Equestrian Group — language switch, header state, mobile menu, enquiry form
(function () {
  var root = document.documentElement;

  function setLang(l) {
    root.setAttribute("data-lang", l);
    root.setAttribute("lang", l);
    root.setAttribute("dir", l === "ar" ? "rtl" : "ltr");
    document.querySelectorAll(".lang button").forEach(function (b) {
      b.setAttribute("aria-pressed", b.dataset.set === l ? "true" : "false");
    });
    document.querySelectorAll("option[data-ar]").forEach(function (o) {
      o.textContent = o.dataset[l];
    });
    try { localStorage.setItem("baiata-lang", l); } catch (e) {}
  }

  var saved = "ar";
  try { saved = localStorage.getItem("baiata-lang") || "ar"; } catch (e) {}
  setLang(saved === "en" || saved === "fr" ? saved : "ar");

  document.querySelectorAll(".lang button").forEach(function (b) {
    b.addEventListener("click", function () { setLang(b.dataset.set); });
  });

  var bar = document.getElementById("top-bar");
  if (bar) {
    var onScroll = function () { bar.classList.toggle("solid", window.scrollY > 60); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    var btn = document.getElementById("menu-btn");
    if (btn) {
      btn.addEventListener("click", function () {
        var open = bar.classList.toggle("open");
        btn.setAttribute("aria-expanded", open ? "true" : "false");
      });
      bar.querySelectorAll(".drawer a").forEach(function (a) {
        a.addEventListener("click", function () { bar.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); });
      });
    }
  }

  // Forms: sent to the Baiata inbox through FormSubmit (static-site form service)
  var INBOX = "baiataasma@gmail.com";
  var MSG = {
    sending: { ar: "جارٍ الإرسال…", fr: "Envoi en cours…", en: "Sending…" },
    ok: { ar: "شكراً لتواصلكم، وصلتنا رسالتكم وسنوافيكم بالرد قريباً.", fr: "Merci, nous avons bien reçu votre message. Nous vous répondrons très vite.", en: "Thank you, we have your message. We'll reply soon." },
    fail: { ar: "تعذّر الإرسال، وسيُفتح بريدكم الإلكتروني لإرسال الرسالة مباشرة.", fr: "L'envoi a échoué. Votre messagerie va s'ouvrir pour envoyer le message directement.", en: "Couldn't send. Your email app will open so you can send it directly." },
    invalid: { ar: "يُرجى إدخال الاسم والبريد الإلكتروني.", fr: "Merci d'indiquer votre nom et votre e-mail.", en: "Please fill in your name and email." }
  };
  function lang() { var l = root.getAttribute("data-lang"); return l === "en" || l === "fr" ? l : "ar"; }
  document.querySelectorAll("form.js-send").forEach(function (form) {
    var note = form.querySelector(".js-note");
    var btn = form.querySelector("button[type=submit]");
    function say(k) { note.textContent = MSG[k][lang()]; note.hidden = false; }
    form.setAttribute("novalidate", "");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { say("invalid"); return; }
      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = v; });
      data._subject = form.dataset.subject || "Baiata website";
      data._template = "table";
      data._captcha = "false";
      data.page = location.pathname;
      if (data.email) data._replyto = data.email;
      btn.disabled = true; say("sending");
      fetch("https://formsubmit.co/ajax/" + INBOX, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(data)
      }).then(function (r) { return r.json(); }).then(function (r) {
        if (!(r && (r.success === true || r.success === "true"))) throw new Error("not sent");
        say("ok"); form.reset();
      }).catch(function () {
        say("fail");
        var body = Object.keys(data).filter(function (k) { return k.charAt(0) !== "_"; })
          .map(function (k) { return k + ": " + data[k]; }).join("\n");
        location.href = "mailto:" + INBOX + "?subject=" + encodeURIComponent(data._subject) + "&body=" + encodeURIComponent(body);
      }).then(function () { btn.disabled = false; });
    });
  });
})();
