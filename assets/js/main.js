/* TIDEPOOL PEDIATRIC THERAPY - main.js v1.0.0
   Gentle interactions only: reveals, mobile nav, tide clock,
   demo forms, FAQ deep links, critter easter egg. */
(function () {
  "use strict";
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- toast ---------- */
  var toastZone = document.querySelector(".toast-zone");
  if (!toastZone) {
    toastZone = document.createElement("div");
    toastZone.className = "toast-zone";
    toastZone.setAttribute("role", "status");
    toastZone.setAttribute("aria-live", "polite");
    document.body.appendChild(toastZone);
  }
  function toast(msg) {
    var t = document.createElement("div");
    t.className = "toast";
    t.textContent = msg;
    toastZone.appendChild(t);
    requestAnimationFrame(function () { t.classList.add("show"); });
    setTimeout(function () {
      t.classList.remove("show");
      setTimeout(function () { t.remove(); }, 400);
    }, 3400);
  }

  /* ---------- mobile nav ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });
    links.addEventListener("click", function (e) {
      if (e.target.closest("a")) { links.classList.remove("open"); toggle.setAttribute("aria-expanded", "false"); }
    });
  }

  /* ---------- scroll reveals ---------- */
  var revealEls = document.querySelectorAll("[data-reveal]");
  if (!reduced && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("revealed");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("revealed"); });
  }

  /* ---------- tide clock (easter egg: shows fictional tide state) ---------- */
  var tideEls = document.querySelectorAll("[data-tide-clock]");
  if (tideEls.length) {
    var phases = ["low tide, calm water", "rising tide", "high tide, clear water", "ebbing tide"];
    function updateTide() {
      var d = new Date();
      var hour = d.getHours() + d.getMinutes() / 60;
      var phase = phases[Math.floor((hour % 6) / 1.5)];
      tideEls.forEach(function (el) { el.textContent = phase + " · " + d.toLocaleTimeString([], { hour: "numeric", minute: "2-digit" }); });
    }
    updateTide();
    setInterval(updateTide, 30000);
  }

  /* ---------- demo forms ---------- */
  document.querySelectorAll("form[data-demo]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var missing = false;
      form.querySelectorAll("[required]").forEach(function (field) {
        var empty = !field.value.trim();
        field.classList.toggle("field-error", empty);
        if (empty) missing = true;
      });
      if (missing) { toast("Please fill in the required fields. (Demo: nothing is sent anywhere.)"); return; }
      form.reset();
      toast("Thanks! This form is a demo: nothing was sent anywhere.");
    });
  });

  /* ---------- FAQ deep links + one-open-at-a-time within a group ---------- */
  document.querySelectorAll(".faq-group").forEach(function (group) {
    group.querySelectorAll("details").forEach(function (d) {
      d.addEventListener("toggle", function () {
        if (d.open) group.querySelectorAll("details[open]").forEach(function (o) { if (o !== d) o.open = false; });
      });
    });
  });
  if (location.hash) {
    var target = document.querySelector(location.hash);
    if (target && target.tagName === "DETAILS") target.open = true;
  }

  /* ---------- gentle drift parallax on critters (transform only) ---------- */
  if (!reduced) {
    var floaters = document.querySelectorAll("[data-drift]");
    if (floaters.length) {
      var lastY = -1;
      var raf = null;
      window.addEventListener("scroll", function () {
        if (raf) return;
        raf = requestAnimationFrame(function () {
          var y = window.scrollY;
          if (Math.abs(y - lastY) > 4) {
            lastY = y;
            floaters.forEach(function (el, i) {
              var speed = 0.03 + (i % 3) * 0.015;
              el.style.transform = "translateY(" + (y * speed % 40 - 20) + "px)";
            });
          }
          raf = null;
        });
      }, { passive: true });
    }
  }

  /* ---------- easter egg: type "tide" for a wave of critter emoji ---------- */
  var buffer = "";
  document.addEventListener("keydown", function (e) {
    if (e.target.matches("input, textarea, select")) return;
    buffer = (buffer + e.key.toLowerCase()).slice(-4);
    if (buffer !== "tide") return;
    buffer = "";
    var pool = ["🐚", "🦀", "🐙", "⭐", "🫧", "🪸", "🐬"];
    var W = window.innerWidth, H = window.innerHeight;
    for (var i = 0; i < 26; i++) {
      (function (i) {
        var s = document.createElement("span");
        s.textContent = pool[Math.floor(Math.random() * pool.length)];
        s.style.cssText = "position:fixed;z-index:500;pointer-events:none;font-size:1.6rem;left:" + (Math.random() * W) + "px;top:-2.5rem;transition:transform 2.6s " + (0.16, "ease-in") + ",opacity 2.6s;opacity:1";
        document.body.appendChild(s);
        setTimeout(function () {
          s.style.transform = "translateY(" + (H + 60) + "px) rotate(" + (Math.random() * 180 - 90) + "deg)";
          s.style.opacity = "0";
        }, 30 + i * 45);
        setTimeout(function () { s.remove(); }, 3400);
      })(i);
    }
    toast("🌊 demo tide rolls in. (Type \"tide\" anytime.)");
  });

  /* ---------- footer year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
