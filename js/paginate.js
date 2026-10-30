/* Client-side pagination: <div data-paginate="6" data-paginate-item=".cls"> */
(function () {
  document.querySelectorAll('[data-paginate]').forEach(function (box) {
    var per = +box.dataset.paginate, items = Array.prototype.slice.call(box.querySelectorAll(box.dataset.paginateItem));
    var pages = Math.ceil(items.length / per);
    if (pages < 2) return;
    var nav = document.createElement('nav'); nav.className = 'pager'; nav.setAttribute('aria-label', 'Pagination');
    box.appendChild(nav);
    function go(p, scroll) {
      items.forEach(function (it, i) { it.hidden = Math.floor(i / per) !== p; });
      var h = '<button type="button" class="pager__b" data-p="' + (p - 1) + '"' + (p ? '' : ' disabled') + ' aria-label="Previous page">&larr;</button>';
      for (var i = 0; i < pages; i++) h += '<button type="button" class="pager__b' + (i === p ? ' is-on' : '') + '" data-p="' + i + '"' + (i === p ? ' aria-current="page"' : '') + '>' + (i + 1) + '</button>';
      h += '<button type="button" class="pager__b" data-p="' + (p + 1) + '"' + (p < pages - 1 ? '' : ' disabled') + ' aria-label="Next page">&rarr;</button>';
      nav.innerHTML = h;
      if (scroll) box.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
    nav.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-p]');
      if (b && !b.disabled) go(+b.dataset.p, true);
    });
    go(0);
  });
})();
