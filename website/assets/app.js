// jabascript навігатор — згенеровано scripts/build_website.py
(function () {
  var doc = document.documentElement;

  // theme toggle (initial theme set inline in <head>)
  var toggle = document.getElementById("theme-toggle");
  if (toggle) toggle.addEventListener("click", function () {
    var next = doc.dataset.theme === "dark" ? "light" : "dark";
    doc.dataset.theme = next;
    localStorage.setItem("jsnav-theme", next);
  });

  // chapter click → seek by swapping iframe src (no external JS API)
  var player = document.getElementById("player");
  if (player) {
    var base = player.dataset.embed;
    document.querySelectorAll(".chapter").forEach(function (btn) {
      btn.addEventListener("click", function () {
        player.src = base + "?start=" + btn.dataset.t + "&autoplay=1&rel=0";
        document.querySelectorAll(".chapter.active").forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
      });
    });
  }

  // watched state (localStorage only)
  var KEY = "jsnav-watched";
  function load() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } }
  function save(w) { localStorage.setItem(KEY, JSON.stringify(w)); }
  var watched = load();

  function refresh() {
    document.querySelectorAll("input.watched").forEach(function (box) {
      box.checked = !!watched[box.dataset.slug];
    });
    document.querySelectorAll("[data-watch-node]").forEach(function (node) {
      node.classList.toggle("done", !!watched[node.dataset.watchNode]);
    });
    document.querySelectorAll(".progress[data-slugs]").forEach(function (bar) {
      var slugs = bar.dataset.slugs ? bar.dataset.slugs.split(",") : [];
      var done = slugs.filter(function (s) { return watched[s]; }).length;
      bar.firstElementChild.style.width = slugs.length ? (100 * done / slugs.length) + "%" : "0";
    });
  }
  document.querySelectorAll("input.watched").forEach(function (box) {
    box.addEventListener("change", function () {
      if (box.checked) watched[box.dataset.slug] = 1; else delete watched[box.dataset.slug];
      save(watched);
      refresh();
    });
  });
  refresh();

  // video catalog filters (videos.html)
  var filters = document.getElementById("video-filters");
  if (filters) {
    var fstate = { level: "", track: "" };
    var cards = document.querySelectorAll(".cat-card");
    var counter = document.getElementById("filter-count");
    var applyFilters = function () {
      var n = 0;
      cards.forEach(function (card) {
        var show = (!fstate.level || card.dataset.level === fstate.level) &&
                   (!fstate.track || card.dataset.track === fstate.track);
        card.hidden = !show;
        if (show) n++;
      });
      if (counter) counter.textContent = n + " відео";
    };
    filters.querySelectorAll(".filter-group").forEach(function (group) {
      group.addEventListener("click", function (e) {
        var btn = e.target.closest(".fbtn");
        if (!btn) return;
        fstate[group.dataset.filter] = btn.dataset.value;
        group.querySelectorAll(".fbtn").forEach(function (b) { b.classList.toggle("on", b === btn); });
        applyFilters();
      });
    });
    applyFilters();
  }

  // site search (index shipped as assets/search-index.js)
  var input = document.getElementById("search-input");
  var results = document.getElementById("search-results");
  if (input && results && window.SEARCH_INDEX) {
    var KINDS = { video: "відео", concept: "тема", tool: "інструмент", book: "книга", track: "трек" };
    var root = document.body.dataset.root || "";
    var sel = -1;
    var normQ = function (s) { return s.toLowerCase().replace(/[ʼ'’`]/g, ""); };
    var escQ = function (s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;"); };
    var hide = function () { results.hidden = true; sel = -1; };
    var show = function () {
      var q = normQ(input.value.trim());
      if (q.length < 2) { hide(); return; }
      var found = [];
      window.SEARCH_INDEX.forEach(function (it) {
        var t = normQ(it.t);
        var rank = t.indexOf(q) === 0 ? 0 : t.indexOf(q) > -1 ? 1 : it.s.indexOf(q) > -1 ? 2 : -1;
        if (rank >= 0) found.push([rank, it]);
      });
      found.sort(function (a, b) { return a[0] - b[0]; });
      var top = found.slice(0, 8);
      results.innerHTML = top.length ? top.map(function (r) {
        var it = r[1];
        return '<a class="sr-item" href="' + root + it.u + '">' +
               '<span class="sr-kind mono">' + (KINDS[it.k] || it.k) + '</span>' +
               '<span class="sr-title">' + escQ(it.t) + '</span>' +
               '<span class="sr-snippet">' + escQ(it.d) + '</span></a>';
      }).join("") : '<div class="sr-empty">Нічого не знайдено</div>';
      results.hidden = false;
      sel = -1;
    };
    input.addEventListener("input", show);
    input.addEventListener("focus", function () { if (input.value.trim().length >= 2) show(); });
    input.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { hide(); input.blur(); return; }
      var items = results.querySelectorAll(".sr-item");
      if (results.hidden || !items.length) return;
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        sel = e.key === "ArrowDown" ? Math.min(sel + 1, items.length - 1) : Math.max(sel - 1, 0);
        items.forEach(function (el, i) { el.classList.toggle("sel", i === sel); });
        items[sel].scrollIntoView({ block: "nearest" });
      } else if (e.key === "Enter" && sel >= 0) {
        e.preventDefault();
        location.href = items[sel].href;
      }
    });
    document.addEventListener("click", function (e) {
      if (!e.target.closest(".search")) hide();
    });
  }
})();
