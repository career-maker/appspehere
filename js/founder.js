/* About: founder message "Click to Read More" toggle */
(function () {
  var btn = document.querySelector('.founder-btn'), more = document.getElementById('founder-more');
  if (!btn || !more) return;
  btn.addEventListener('click', function () {
    var open = more.hidden;
    more.hidden = !open;
    btn.setAttribute('aria-expanded', String(open));
    btn.textContent = open ? 'Click to Read Less' : 'Click to Read More';
  });
})();
