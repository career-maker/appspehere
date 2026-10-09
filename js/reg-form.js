/* Registration forms ([data-wa]): validate, then open WhatsApp with the details filled in */
(function () {
  document.querySelectorAll('form[data-wa]').forEach(function (f) {
    var st = f.querySelector('.sp-status');
    function wrap(el) { return el.closest('.sp-field'); }
    function err(el, msg) {
      var w = wrap(el), e = w.querySelector('.sp-error');
      if (!e) { e = document.createElement('p'); e.className = 'sp-error'; e.setAttribute('role', 'alert'); w.appendChild(e); }
      w.classList.toggle('has-error', !!msg); e.textContent = msg || ''; el.toggleAttribute('aria-invalid', !!msg);
    }
    function check(el) {
      if (el.checkValidity()) { err(el, ''); return true; }
      err(el, el.validity.valueMissing ? 'This field is required.' : 'Enter a valid ' + (el.type === 'email' ? 'email address.' : el.type === 'tel' ? 'mobile number.' : 'value.'));
      return false;
    }
    function live(e) { var w = wrap(e.target); if (w && w.classList.contains('has-error')) check(e.target); }
    f.addEventListener('input', live); f.addEventListener('change', live);
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var fields = [].slice.call(f.querySelectorAll('input,select,textarea'));
      var bad = fields.filter(function (el) { return !check(el); });
      if (bad.length) {
        st.className = 'sp-status sp-status--error is-visible';
        st.textContent = 'Please fix ' + bad.length + ' field' + (bad.length > 1 ? 's' : '') + ' before sending.';
        var first = bad[0]; (first.tagName === 'SELECT' && first.parentNode.querySelector('.cs__btn') || first).focus();
        return;
      }
      var lines = fields.map(function (el) {
        var l = f.querySelector('label[for="' + el.id + '"]');
        return el.value.trim() && l ? l.textContent.replace('*', '').trim() + ': ' + el.value.trim() : '';
      }).filter(Boolean);
      var text = f.getAttribute('data-wa') + '\n' + lines.join('\n');
      st.className = 'sp-status sp-status--success is-visible';
      st.textContent = 'Opening WhatsApp with your details…';
      window.open('https://wa.me/919778452007?text=' + encodeURIComponent(text), '_blank', 'noopener');
    });
  });
})();
