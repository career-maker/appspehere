/* Gallery lightbox (native <dialog>) */
(function () {
  var items = Array.prototype.slice.call(document.querySelectorAll('.gal__item'));
  var lb = document.getElementById('lb');
  if (!items.length || !lb || !lb.showModal) return;
  var img = lb.querySelector('img'), cap = lb.querySelector('.lb__cap'), cur = 0;
  function show(i) {
    cur = (i + items.length) % items.length;
    var it = items[cur].querySelector('img');
    img.src = it.currentSrc || it.src; img.alt = it.alt;
    cap.textContent = items[cur].querySelector('span').textContent;
  }
  items.forEach(function (b, i) { b.addEventListener('click', function () { show(i); lb.showModal(); }); });
  lb.querySelector('.lb__x').addEventListener('click', function () { lb.close(); });
  lb.querySelector('.lb__p').addEventListener('click', function () { show(cur - 1); });
  lb.querySelector('.lb__n').addEventListener('click', function () { show(cur + 1); });
  lb.addEventListener('click', function (e) { if (e.target === lb || e.target.classList.contains('lb__in')) lb.close(); });
  lb.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') show(cur - 1);
    if (e.key === 'ArrowRight') show(cur + 1);
  });
})();
