/* Contact page: Manufacturer / Distributor / Retailer enquiry tabs */
(function () {
  var tabs = [].slice.call(document.querySelectorAll('.ctabs [role=tab]'));
  if (!tabs.length) return;
  function show(i, focus) {
    tabs.forEach(function (t, k) {
      var on = k === i;
      t.setAttribute('aria-selected', String(on)); t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
      if (on && focus) t.focus();
    });
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { show(i); });
    t.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { e.preventDefault(); show((i + 1) % tabs.length, true); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); show((i + tabs.length - 1) % tabs.length, true); }
    });
  });
  var k = ['#manufacturer', '#distributor', '#retailer'].indexOf(location.hash);
  if (k > -1) show(k);
})();
