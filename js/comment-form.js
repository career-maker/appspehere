/* Blog comment form: validates, then waits for the backend. */
(function () {
  var f = document.getElementById('commentForm');
  if (!f) return;
  var st = f.querySelector('.sp-status');
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!f.checkValidity()) { f.reportValidity(); return; }
    // TODO(backend): POST new FormData(f) to the comments endpoint, then show the moderation notice.
    st.className = 'sp-status sp-status--success is-visible';
    st.textContent = 'Thank you. Comment posting is being enabled shortly, please try again soon.';
  });
})();
