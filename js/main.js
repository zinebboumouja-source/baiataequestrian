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
  setLang(saved === "en" ? "en" : "ar");

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

  var form = document.getElementById("enquiry-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      document.getElementById("form-note").hidden = false;
    });
  }
})();
