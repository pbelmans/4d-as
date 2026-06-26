// Click-to-sort + filter for every family table. No dependencies.
// Each sortable table may have a preceding `.table-controls` block with a
// `.fam-search` input and/or a `.hide-ore` checkbox; both compose with sorting.
document.addEventListener("DOMContentLoaded", function () {
  function num(s) {
    return /^[-+]?[0-9]*\.?[0-9]+$/.test(s) ? parseFloat(s) : null;
  }

  document.querySelectorAll("table.sortable").forEach(function (table) {
    var tbody = table.tBodies[0];
    if (!tbody) return;
    var headers = table.querySelectorAll("th[data-col]");

    headers.forEach(function (th) {
      th.addEventListener("click", function () {
        var col = +th.getAttribute("data-col");
        var asc = th.getAttribute("data-asc") !== "true";
        headers.forEach(function (h) {
          h.removeAttribute("data-asc");
          h.classList.remove("sorted-asc", "sorted-desc");
        });
        th.setAttribute("data-asc", asc);
        th.classList.add(asc ? "sorted-asc" : "sorted-desc");
        Array.prototype.slice.call(tbody.rows).sort(function (a, b) {
          var x = a.cells[col].textContent.trim();
          var y = b.cells[col].textContent.trim();
          var nx = num(x), ny = num(y), r;
          if (nx !== null && ny !== null) r = nx - ny;
          else if (nx !== null) r = -1;
          else if (ny !== null) r = 1;
          else r = x.localeCompare(y);
          return asc ? r : -r;
        }).forEach(function (r) { tbody.appendChild(r); });
      });
    });

    // controls: the .table-controls just before this table (or its wrapper)
    var wrap = table.closest(".table-responsive") || table;
    var controls = wrap.previousElementSibling;
    if (controls && !controls.classList.contains("table-controls")) controls = null;
    var search = controls && controls.querySelector(".fam-search");
    var hideOre = controls && controls.querySelector(".hide-ore");
    function applyFilter() {
      var q = (search ? search.value : "").trim().toLowerCase();
      Array.prototype.forEach.call(tbody.rows, function (r) {
        var hidden = hideOre && hideOre.checked && r.getAttribute("data-kind") === "double-Ore";
        var match = !q || r.textContent.toLowerCase().indexOf(q) !== -1;
        r.style.display = match && !hidden ? "" : "none";
      });
    }
    if (search) search.addEventListener("input", applyFilter);
    if (hideOre) hideOre.addEventListener("change", applyFilter);
  });
});
