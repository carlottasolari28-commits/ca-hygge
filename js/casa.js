/* Ca' Hygge · comportamenti della pagina */
{
  // Intestazione piena quando si scorre
  const testata = document.querySelector('.testata');
  const aggiornaTestata = () => testata.classList.toggle('piena', window.scrollY > 60);
  window.addEventListener('scroll', aggiornaTestata, { passive: true });
  aggiornaTestata();

  // Schede delle stanze
  const tabs = [...document.querySelectorAll('[role=tab]')];
  const mostra = tab => {
    tabs.forEach(t => {
      const attiva = t === tab;
      t.setAttribute('aria-selected', attiva ? 'true' : 'false');
      t.tabIndex = attiva ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !attiva;
    });
  };
  tabs.forEach((t, i) => {
    t.addEventListener('click', () => mostra(t));
    t.addEventListener('keydown', ev => {
      if (ev.key !== 'ArrowRight' && ev.key !== 'ArrowLeft') return;
      const n = tabs[(i + (ev.key === 'ArrowRight' ? 1 : tabs.length - 1)) % tabs.length];
      n.focus(); mostra(n);
    });
  });

  // Miniature: cambiano la foto grande della stanza
  document.querySelectorAll('.stanza').forEach(st => {
    const grande = st.querySelector('.grande img');
    st.querySelectorAll('.miniature button').forEach(b => b.addEventListener('click', () => {
      st.querySelectorAll('.miniature button').forEach(x => x.setAttribute('aria-pressed', x === b ? 'true' : 'false'));
      grande.style.opacity = '0';
      const nuova = new Image();
      nuova.onload = () => { grande.removeAttribute('srcset'); grande.src = b.dataset.src; grande.alt = b.dataset.alt; grande.style.opacity = '1'; };
      nuova.src = b.dataset.src;
    }));
  });

  // Comparsa morbida
  const el = document.querySelectorAll('.appare');
  if ('IntersectionObserver' in window) {
    const oss = new IntersectionObserver(v => v.forEach(x => { if (x.isIntersecting) { x.target.classList.add('visto'); oss.unobserve(x.target); } }), { rootMargin: '0px 0px -8% 0px' });
    el.forEach(e => oss.observe(e));
  } else el.forEach(e => e.classList.add('visto'));

  // Tramonto di oggi a Lavagna
  const box = document.querySelector('[data-tramonto] [data-ora]');
  if (box && window.Sole) {
    const oggi = new Intl.DateTimeFormat('en-CA', { timeZone: 'Europe/Rome' }).format(new Date());
    box.textContent = Sole.ora(Sole.orari(Sole.mezzogiorno(oggi), 44.3076, 9.3443).tramonto);
  }
}
