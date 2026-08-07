function showToast(msg, ms) {
  let el = document.getElementById('__toast');
  if (!el) {
    el = document.createElement('div');
    el.id = '__toast';
    el.className = 'toast';
    document.body.appendChild(el);
  }
  el.textContent = msg;
  requestAnimationFrame(() => el.classList.add('show'));
  clearTimeout(el._t);
  el._t = setTimeout(() => el.classList.remove('show'), ms || 2200);
}

function qs(name, fallback) {
  const v = new URLSearchParams(location.search).get(name);
  return v == null ? fallback : v;
}
