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
})();
