/* =========================================================
   ST Стоматологія — app.js
   Ванільний JS, без залежностей. Прогресивне покращення:
   без JS сайт залишається читабельним і навігованим.
   ========================================================= */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var isTouch = window.matchMedia("(hover: none)").matches;

  /* ---------------------------------------------------------
     1. SCROLL REVEAL
     --------------------------------------------------------- */
  var revealEls = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var revealIO = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            revealIO.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
    );
    revealEls.forEach(function (el) {
      revealIO.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
      el.classList.add("is-visible");
    });
  }

  /* ---------------------------------------------------------
     2. HEADER: приховування при скролі вниз + стан
     --------------------------------------------------------- */
  var header = document.querySelector("[data-header]");
  var progressBar = document.querySelector("[data-progress-bar]");
  var stickyCta = document.querySelector("[data-sticky-cta]");
  var lastY = window.scrollY;
  var scrollTicking = false;

  function onScrollFrame() {
    var y = window.scrollY;
    var docH = document.documentElement.scrollHeight - window.innerHeight;

    /* прогрес читання */
    if (progressBar) {
      var pct = docH > 0 ? (y / docH) * 100 : 0;
      progressBar.style.width = Math.min(100, Math.max(0, pct)).toFixed(2) + "%";
    }

    if (header) {
      header.classList.toggle("is-scrolled", y > 24);
      var goingDown = y > lastY && y > 320;
      if (!document.body.classList.contains("is-locked")) {
        header.classList.toggle("is-hidden", goingDown);
      }
    }

    /* липка кнопка з'являється після геро */
    if (stickyCta) {
      stickyCta.classList.toggle("is-visible", y > window.innerHeight * 0.65);
    }

    lastY = y;
    scrollTicking = false;
  }

  window.addEventListener(
    "scroll",
    function () {
      if (!scrollTicking) {
        scrollTicking = true;
        window.requestAnimationFrame(onScrollFrame);
      }
    },
    { passive: true }
  );
  onScrollFrame();

  /* ---------------------------------------------------------
     3. МОБІЛЬНЕ МЕНЮ (+ свайп для закриття)
     --------------------------------------------------------- */
  var burger = document.querySelector("[data-burger]");
  var mobileNav = document.querySelector("[data-mobile-nav]");
  var scrim = document.querySelector("[data-scrim]");

  function openNav() {
    if (!mobileNav) return;
    mobileNav.classList.add("is-open");
    mobileNav.setAttribute("aria-hidden", "false");
    if (scrim) {
      scrim.hidden = false;
      requestAnimationFrame(function () {
        scrim.classList.add("is-open");
      });
    }
    if (burger) burger.setAttribute("aria-expanded", "true");
    document.body.classList.add("is-locked");
    if (header) header.classList.remove("is-hidden");
  }

  function closeNav() {
    if (!mobileNav) return;
    mobileNav.classList.remove("is-open");
    mobileNav.setAttribute("aria-hidden", "true");
    if (scrim) {
      scrim.classList.remove("is-open");
      window.setTimeout(function () {
        if (!mobileNav.classList.contains("is-open")) scrim.hidden = true;
      }, 350);
    }
    if (burger) burger.setAttribute("aria-expanded", "false");
    document.body.classList.remove("is-locked");
  }

  if (burger) {
    burger.addEventListener("click", function () {
      if (mobileNav.classList.contains("is-open")) closeNav();
      else openNav();
    });
  }
  if (scrim) scrim.addEventListener("click", closeNav);

  var navClose = document.querySelector("[data-nav-close]");
  if (navClose) navClose.addEventListener("click", closeNav);

  if (mobileNav) {
    mobileNav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", closeNav);
    });

    /* свайп вправо закриває панель */
    var navStartX = 0;
    var navStartY = 0;
    var navSwiping = false;
    mobileNav.addEventListener(
      "touchstart",
      function (e) {
        navStartX = e.touches[0].clientX;
        navStartY = e.touches[0].clientY;
        navSwiping = true;
      },
      { passive: true }
    );
    mobileNav.addEventListener(
      "touchmove",
      function (e) {
        if (!navSwiping) return;
        var dx = e.touches[0].clientX - navStartX;
        var dy = Math.abs(e.touches[0].clientY - navStartY);
        if (dx > 62 && dy < 46) {
          navSwiping = false;
          closeNav();
        }
      },
      { passive: true }
    );
    mobileNav.addEventListener("touchend", function () {
      navSwiping = false;
    });
  }

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && mobileNav && mobileNav.classList.contains("is-open")) closeNav();
  });

  /* ---------------------------------------------------------
     3.5. МОДАЛЬНЕ ВІКНО ЗАПИСУ (dialog)
     Відкривається з будь-якої кнопки [data-open-booking] на
     будь-якій сторінці сайту (шапка, геро, мобменю, футер,
     липка панель, картки послуг).
     --------------------------------------------------------- */
  var bookingModal = document.getElementById("booking-modal");
  var bookingOpenTriggers = document.querySelectorAll("[data-open-booking]");
  var bookingCloseTriggers = bookingModal ? bookingModal.querySelectorAll("[data-close-booking]") : [];
  var modalReturnFocus = null;

  function openBookingModal(trigger) {
    if (!bookingModal) return;
    modalReturnFocus = document.activeElement;

    /* якщо кнопка веде з конкретної послуги — підставляємо напрям у select */
    var presetService = trigger && trigger.getAttribute && trigger.getAttribute("data-service");
    if (presetService) {
      var select = bookingModal.querySelector("#mf-service");
      if (select) {
        var match = Array.prototype.find.call(select.options, function (opt) {
          return opt.value === presetService || opt.textContent.trim() === presetService;
        });
        if (match) select.value = match.value || match.textContent.trim();
      }
    }

    if (typeof bookingModal.showModal === "function") {
      bookingModal.showModal();
    } else {
      bookingModal.setAttribute("open", "");
    }
    document.body.classList.add("is-locked");
    if (header) header.classList.remove("is-hidden");

    var firstField = bookingModal.querySelector("#mf-name");
    if (firstField) window.setTimeout(function () { firstField.focus(); }, 60);
  }

  function closeBookingModal() {
    if (!bookingModal) return;
    if (typeof bookingModal.close === "function" && bookingModal.open) {
      bookingModal.close();
    } else {
      bookingModal.removeAttribute("open");
    }
  }

  bookingOpenTriggers.forEach(function (trigger) {
    trigger.addEventListener("click", function (e) {
      e.preventDefault();
      openBookingModal(trigger);
    });
  });
  bookingCloseTriggers.forEach(function (btn) {
    btn.addEventListener("click", closeBookingModal);
  });

  if (bookingModal) {
    /* клік по backdrop (сама dialog, поза .modal-shell) закриває */
    bookingModal.addEventListener("click", function (e) {
      if (e.target === bookingModal) closeBookingModal();
    });
    /* прибираємо блокування скролу після закриття (ESC, .close(), backdrop) */
    bookingModal.addEventListener("close", function () {
      document.body.classList.remove("is-locked");
      if (modalReturnFocus && typeof modalReturnFocus.focus === "function") {
        modalReturnFocus.focus();
      }
    });
  }

  /* якщо хтось лишив старе посилання #booking (наприклад, зовнішній лінк) —
     відкриваємо модалку замість скролу в порожнє місце */
  if (window.location.hash === "#booking" && bookingModal) {
    openBookingModal(null);
  }

  /* ---------------------------------------------------------
     4. АКТИВНИЙ ПУНКТ НАВІГАЦІЇ
     --------------------------------------------------------- */
  var navLinks = Array.prototype.slice.call(document.querySelectorAll(".nav-link"));
  var sections = navLinks
    .filter(function (a) {
      var href = a.getAttribute("href") || "";
      return href.charAt(0) === "#" && href.length > 1;
    })
    .map(function (a) {
      return document.querySelector(a.getAttribute("href"));
    })
    .filter(Boolean);

  if ("IntersectionObserver" in window && sections.length) {
    var navIO = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          navLinks.forEach(function (a) {
            a.classList.toggle("is-active", a.getAttribute("href") === "#" + entry.target.id);
          });
        });
      },
      { rootMargin: "-45% 0px -50% 0px" }
    );
    sections.forEach(function (s) {
      navIO.observe(s);
    });
  }

  /* ---------------------------------------------------------
     5. КАРУСЕЛЬ (галерея + відгуки): свайп, drag, стрілки, точки
     --------------------------------------------------------- */
  function initCarousel(opts) {
    var root = document.querySelector(opts.root);
    if (!root) return;
    var track = root.querySelector(opts.track);
    if (!track) return;

    var items = Array.prototype.slice.call(track.children);
    var dotsWrap = opts.dots ? root.querySelector(opts.dots) : null;
    var prevBtn = opts.prev ? root.querySelector(opts.prev) : null;
    var nextBtn = opts.next ? root.querySelector(opts.next) : null;
    var currentOut = opts.current ? root.querySelector(opts.current) : null;
    var totalOut = opts.total ? root.querySelector(opts.total) : null;
    var index = 0;

    function pad(n) {
      return (n < 10 ? "0" : "") + n;
    }

    if (totalOut) totalOut.textContent = pad(items.length);

    /* точки */
    var dots = [];
    if (dotsWrap) {
      items.forEach(function (item, i) {
        var b = document.createElement("button");
        b.type = "button";
        b.setAttribute("role", "tab");
        b.setAttribute("aria-label", "Слайд " + (i + 1));
        b.setAttribute("aria-selected", i === 0 ? "true" : "false");
        b.addEventListener("click", function () {
          goTo(i);
        });
        dotsWrap.appendChild(b);
        dots.push(b);
      });
    }

    function goTo(i) {
      index = Math.max(0, Math.min(items.length - 1, i));
      var target = items[index];
      var left = target.offsetLeft - (track.clientWidth - target.clientWidth) / 2;
      track.scrollTo({ left: Math.max(0, left), behavior: reduceMotion ? "auto" : "smooth" });
      sync();
    }

    function nearestIndex() {
      var center = track.scrollLeft + track.clientWidth / 2;
      var best = 0;
      var bestDist = Infinity;
      items.forEach(function (item, i) {
        var itemCenter = item.offsetLeft + item.clientWidth / 2;
        var d = Math.abs(itemCenter - center);
        if (d < bestDist) {
          bestDist = d;
          best = i;
        }
      });
      return best;
    }

    function sync() {
      dots.forEach(function (d, i) {
        d.setAttribute("aria-selected", i === index ? "true" : "false");
      });
      if (currentOut) currentOut.textContent = pad(index + 1);
      if (prevBtn) prevBtn.disabled = index === 0;
      if (nextBtn) nextBtn.disabled = index === items.length - 1;
    }

    if (prevBtn)
      prevBtn.addEventListener("click", function () {
        goTo(index - 1);
      });
    if (nextBtn)
      nextBtn.addEventListener("click", function () {
        goTo(index + 1);
      });

    /* синхронізація при нативному свайпі */
    var scrollTO;
    track.addEventListener(
      "scroll",
      function () {
        window.clearTimeout(scrollTO);
        scrollTO = window.setTimeout(function () {
          index = nearestIndex();
          sync();
        }, 90);
      },
      { passive: true }
    );

    /* клавіатура */
    track.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") {
        e.preventDefault();
        goTo(index + 1);
      } else if (e.key === "ArrowLeft") {
        e.preventDefault();
        goTo(index - 1);
      }
    });

    /* drag мишкою (десктоп) */
    if (!isTouch) {
      var dragging = false;
      var startX = 0;
      var startScroll = 0;
      var moved = 0;

      track.addEventListener("pointerdown", function (e) {
        if (e.pointerType === "touch") return;
        dragging = true;
        moved = 0;
        startX = e.clientX;
        startScroll = track.scrollLeft;
        track.classList.add("is-dragging");
        track.setPointerCapture(e.pointerId);
      });

      track.addEventListener("pointermove", function (e) {
        if (!dragging) return;
        var dx = e.clientX - startX;
        moved = Math.abs(dx);
        track.scrollLeft = startScroll - dx;
      });

      function endDrag() {
        if (!dragging) return;
        dragging = false;
        track.classList.remove("is-dragging");
        goTo(nearestIndex());
      }

      track.addEventListener("pointerup", endDrag);
      track.addEventListener("pointercancel", endDrag);
      track.addEventListener("click", function (e) {
        if (moved > 8) {
          e.preventDefault();
          e.stopPropagation();
        }
      });
    }

    window.addEventListener(
      "resize",
      function () {
        index = nearestIndex();
        sync();
      },
      { passive: true }
    );

    sync();
  }

  initCarousel({
    root: "[data-gallery]",
    track: "[data-gallery-track]",
    dots: "[data-gallery-dots]",
    prev: "[data-gallery-prev]",
    next: "[data-gallery-next]",
    current: "[data-gallery-current]",
    total: "[data-gallery-total]",
  });

  initCarousel({
    root: "[data-reviews]",
    track: "[data-reviews-track]",
    dots: "[data-reviews-dots]",
    prev: "[data-reviews-prev]",
    next: "[data-reviews-next]",
  });

  /* ---------------------------------------------------------
     6. BEFORE / AFTER: range + drag + touch
     --------------------------------------------------------- */
  document.querySelectorAll("[data-ba]").forEach(function (slider) {
    var range = slider.querySelector(".ba-range");
    if (!range) return;

    function setPos(val) {
      var v = Math.max(0, Math.min(100, val));
      slider.style.setProperty("--ba-pos", v + "%");
      range.value = v;
    }

    range.addEventListener("input", function () {
      setPos(parseFloat(range.value));
    });

    function posFromEvent(clientX) {
      var rect = slider.getBoundingClientRect();
      return ((clientX - rect.left) / rect.width) * 100;
    }

    /* безпосереднє перетягування (працює і на тач, і на мишці) */
    var active = false;
    slider.addEventListener(
      "pointerdown",
      function (e) {
        active = true;
        setPos(posFromEvent(e.clientX));
      },
      { passive: true }
    );
    slider.addEventListener(
      "pointermove",
      function (e) {
        if (!active) return;
        setPos(posFromEvent(e.clientX));
      },
      { passive: true }
    );
    ["pointerup", "pointercancel", "pointerleave"].forEach(function (ev) {
      slider.addEventListener(ev, function () {
        active = false;
      });
    });

    setPos(parseFloat(range.value));
  });

  /* ---------------------------------------------------------
     7. АНІМАЦІЯ ЦИФР
     --------------------------------------------------------- */
  var counters = document.querySelectorAll("[data-count]");
  if (counters.length && "IntersectionObserver" in window) {
    var countIO = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          animateCount(entry.target);
          countIO.unobserve(entry.target);
        });
      },
      { threshold: 0.55 }
    );
    counters.forEach(function (el) {
      countIO.observe(el);
    });
  }

  function animateCount(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var suffix = el.getAttribute("data-suffix") || "";
    var decimals = parseInt(el.getAttribute("data-decimals") || "0", 10);

    function fmt(v) {
      var out = decimals > 0 ? v.toFixed(decimals) : Math.round(v).toLocaleString("uk-UA");
      return out + suffix;
    }

    if (reduceMotion) {
      el.textContent = fmt(target);
      return;
    }

    var duration = 1300;
    var start = performance.now();

    function step(now) {
      var p = Math.min(1, (now - start) / duration);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(target * eased);
      if (p < 1) requestAnimationFrame(step);
      else el.textContent = fmt(target);
    }
    requestAnimationFrame(step);
  }

  /* ---------------------------------------------------------
     8. ЛЕГКИЙ ПАРАЛАКС (тільки десктоп, без reduced-motion)
     --------------------------------------------------------- */
  var parallaxEls = document.querySelectorAll("[data-parallax]");
  if (parallaxEls.length && !reduceMotion && !isTouch) {
    var pxTicking = false;
    window.addEventListener(
      "scroll",
      function () {
        if (pxTicking) return;
        pxTicking = true;
        requestAnimationFrame(function () {
          parallaxEls.forEach(function (el) {
            var rect = el.getBoundingClientRect();
            if (rect.bottom < 0 || rect.top > window.innerHeight) return;
            var factor = parseFloat(el.getAttribute("data-parallax")) || 0.05;
            var offset = (rect.top + rect.height / 2 - window.innerHeight / 2) * -factor;
            el.style.transform = "translate3d(0," + offset.toFixed(2) + "px,0)";
          });
          pxTicking = false;
        });
      },
      { passive: true }
    );
  }

  /* ---------------------------------------------------------
     9. АКОРДЕОНИ: у групі відкритий лише один (тільки ціни)
     --------------------------------------------------------- */
  var priceAcc = document.querySelector(".price-accordion");
  if (priceAcc) {
    var accItems = Array.prototype.slice.call(priceAcc.querySelectorAll(".acc"));
    accItems.forEach(function (acc) {
      acc.addEventListener("toggle", function () {
        if (!acc.open) return;
        accItems.forEach(function (other) {
          if (other !== acc) other.open = false;
        });
      });
    });
  }

  /* ---------------------------------------------------------
     10. ФОРМА ЗАПИСУ: валідація + маска телефону + відправка
     Форма живе всередині модалки (#booking-modal). Немає
     власного бекенду в статичному сайті — POST йде на
     /api/notify (serverless-функція), яка й стукається в
     Telegram Bot API зі свого боку, токен нікому не видно.
     --------------------------------------------------------- */
  var BOOKING_ENDPOINT = "/api/notify";

  document.querySelectorAll("[data-booking]").forEach(function (form) {
    var phone = form.querySelector('[name="phone"]');
    var success = form.querySelector("[data-form-success]");
    var errorMsg = form.querySelector("[data-form-error]");
    var btn = form.querySelector('button[type="submit"]');
    var btnLabel = btn ? btn.querySelector("[data-btn-label]") : null;
    var defaultBtnText = btnLabel ? btnLabel.textContent : (btn ? btn.textContent : "");

    if (phone) {
      phone.addEventListener("input", function () {
        var digits = phone.value.replace(/\D/g, "");
        if (digits.indexOf("380") === 0) digits = digits.slice(3);
        else if (digits.indexOf("0") === 0) digits = digits.slice(1);
        digits = digits.slice(0, 9);

        var out = "+380";
        if (digits.length) out += " " + digits.slice(0, 2);
        if (digits.length > 2) out += " " + digits.slice(2, 5);
        if (digits.length > 5) out += " " + digits.slice(5, 7);
        if (digits.length > 7) out += " " + digits.slice(7, 9);
        phone.value = out;
      });

      phone.addEventListener("focus", function () {
        if (!phone.value) phone.value = "+380 ";
      });
    }

    function setError(input, message) {
      var field = input.closest(".field");
      var slot = field ? field.querySelector(".field-error") : null;
      if (field) field.classList.toggle("has-error", Boolean(message));
      if (slot) slot.textContent = message || "";
      input.setAttribute("aria-invalid", message ? "true" : "false");
    }

    function validate() {
      var ok = true;

      var name = form.querySelector('[name="name"]');
      if (name) {
        if (name.value.trim().length < 2) {
          setError(name, "Вкажіть ім'я — щонайменше 2 символи");
          ok = false;
        } else setError(name, "");
      }

      if (phone) {
        var digits = phone.value.replace(/\D/g, "");
        if (digits.length !== 12) {
          setError(phone, "Введіть повний номер у форматі +380 XX XXX XX XX");
          ok = false;
        } else setError(phone, "");
      }

      return ok;
    }

    function setBusy(isBusy) {
      if (!btn) return;
      btn.disabled = isBusy;
      var text = isBusy ? "Надсилаємо…" : defaultBtnText;
      if (btnLabel) btnLabel.textContent = text;
      else btn.textContent = text;
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (success) success.hidden = true;
      if (errorMsg) errorMsg.hidden = true;

      if (!validate()) {
        var firstBad = form.querySelector(".field.has-error input");
        if (firstBad) firstBad.focus();
        return;
      }

      var payload = {
        name: (form.querySelector('[name="name"]') || {}).value || "",
        phone: (phone || {}).value || "",
        service: (form.querySelector('[name="service"]') || {}).value || "",
        note: (form.querySelector('[name="note"]') || {}).value || "",
        page: window.location.href,
      };

      setBusy(true);

      fetch(BOOKING_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      })
        .then(function (res) {
          if (!res.ok) throw new Error("Bad response " + res.status);
          return res.json().catch(function () { return {}; });
        })
        .then(function () {
          form.reset();
          setBusy(false);
          if (success) {
            success.hidden = false;
            success.scrollIntoView({ block: "nearest", behavior: reduceMotion ? "auto" : "smooth" });
          }
          /* автозакриття модалки, якщо форма в ній */
          var parentDialog = form.closest("dialog");
          if (parentDialog) {
            window.setTimeout(function () {
              if (typeof parentDialog.close === "function") parentDialog.close();
            }, 1800);
          }
        })
        .catch(function () {
          setBusy(false);
          if (errorMsg) {
            errorMsg.hidden = false;
            errorMsg.scrollIntoView({ block: "nearest", behavior: reduceMotion ? "auto" : "smooth" });
          }
        });
    });

    form.querySelectorAll("input").forEach(function (input) {
      input.addEventListener("blur", function () {
        if (input.closest(".field").classList.contains("has-error")) validate();
      });
    });
  });

  /* ---------------------------------------------------------
     11. Плавний скрол з урахуванням фіксованої шапки
     (для браузерів без scroll-padding)
     --------------------------------------------------------- */
  if (!CSS.supports || !CSS.supports("scroll-padding-top", "1px")) {
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
      link.addEventListener("click", function (e) {
        var id = link.getAttribute("href");
        if (id === "#" || id.length < 2) return;
        var target = document.querySelector(id);
        if (!target) return;
        e.preventDefault();
        var headerH = header ? header.offsetHeight : 0;
        var top = target.getBoundingClientRect().top + window.scrollY - headerH - 12;
        window.scrollTo({ top: top, behavior: reduceMotion ? "auto" : "smooth" });
      });
    });
  }
  /* ---------------------------------------------------------
     12. ГРЕЙСФУЛ-ФОЛБЕК ДЛЯ ФОТО, ЯКИХ ЩЕ НЕМАЄ
     Поки реальні фото пацієнтів/лікарів/кабінету не завантажені,
     показуємо фірмову замінну картинку замість зламаної іконки
     браузера — виглядає як навмисний дизайн, а не як помилка.
     --------------------------------------------------------- */
  var PLACEHOLDER_SRC =
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200'%3E" +
    "%3Crect width='200' height='200' fill='%2316150F'/%3E" +
    "%3Ccircle cx='100' cy='100' r='96' fill='none' stroke='%23C8A96A' stroke-opacity='.25' stroke-width='1'/%3E" +
    "%3Cg fill='none' stroke='%23C8A96A' stroke-opacity='.75' stroke-width='2.2'%3E" +
    "%3Cpath d='M100 62c-16 0-28 11-28 27 0 14 6 24 10 34 3 8 5 15 8 15s4-9 6-16 3-8 4-8 2 1 4 8 3 16 6 16 5-7 8-15c4-10 10-20 10-34 0-16-12-27-28-27z'/%3E" +
    "%3C/g%3E%3C/svg%3E";

  document.querySelectorAll("img").forEach(function (img) {
    img.addEventListener(
      "error",
      function () {
        if (img.dataset.fallback) return; // не зациклюємось, якщо і плейсхолдер не завантажиться
        img.dataset.fallback = "1";
        img.src = PLACEHOLDER_SRC;
        img.classList.add("is-placeholder");
        img.removeAttribute("srcset");
      },
      { once: true }
    );
  });

})();
