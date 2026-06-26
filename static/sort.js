// Lightweight click-to-sort for the families table. No dependencies.
document.addEventListener("DOMContentLoaded", function () {
  var table = document.querySelector("table.sortable");
  if (!table) return;
  var tbody = table.tBodies[0];
  var headers = table.querySelectorAll("th[data-col]");

  function num(s) {
    return /^[-+]?[0-9]*\.?[0-9]+$/.test(s) ? parseFloat(s) : null;
  }

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

      var rows = Array.prototype.slice.call(tbody.rows);
      rows.sort(function (a, b) {
        var x = a.cells[col].textContent.trim();
        var y = b.cells[col].textContent.trim();
        var nx = num(x), ny = num(y), r;
        if (nx !== null && ny !== null) r = nx - ny;       // numeric
        else if (nx !== null) r = -1;                       // numbers before "—"
        else if (ny !== null) r = 1;
        else r = x.localeCompare(y);                        // text
        return asc ? r : -r;
      });
      rows.forEach(function (r) { tbody.appendChild(r); });
    });
  });
});
