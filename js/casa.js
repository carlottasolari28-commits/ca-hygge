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

// Richiesta di disponibilità: prepara un'email già compilata
{
  const f = document.getElementById('richiesta');
  if (f) {
    const arrivo = f.querySelector('#arrivo'), partenza = f.querySelector('#partenza'), avviso = f.querySelector('.avviso');
    const oggi = new Intl.DateTimeFormat('en-CA', { timeZone: 'Europe/Rome' }).format(new Date());
    arrivo.min = oggi; partenza.min = oggi;
    arrivo.addEventListener('change', () => { partenza.min = arrivo.value || oggi; });
    const it = v => v.split('-').reverse().join('/');
    const selB = f.querySelector('#bambini'), boxEta = f.querySelector('#eta'), campi = f.querySelector('.eta-campi');
    const opzioni = '<option value="">Scegli</option><option value="meno di 1 anno">meno di 1 anno</option>' +
      Array.from({ length: 17 }, (_, i) => '<option value="' + (i + 1) + (i ? ' anni' : ' anno') + '">' + (i + 1) + (i ? ' anni' : ' anno') + '</option>').join('');
    const aggiornaEta = () => {
      const n = Number(selB.value), vecchi = [...campi.querySelectorAll('select')].map(x => x.value);
      campi.innerHTML = Array.from({ length: n }, (_, i) =>
        '<div><label for="eta-' + i + '">Bambino ' + (i + 1) + '</label><select id="eta-' + i + '">' + opzioni + '</select></div>').join('');
      campi.querySelectorAll('select').forEach((x, i) => { if (vecchi[i]) x.value = vecchi[i]; });
      boxEta.hidden = n === 0;
    };
    selB.addEventListener('change', aggiornaEta);
    f.addEventListener('submit', ev => {
      ev.preventDefault();
      if (!arrivo.value || !partenza.value) { avviso.textContent = 'Indicate le date di arrivo e di partenza.'; return; }
      if (partenza.value <= arrivo.value) { avviso.textContent = 'La partenza deve essere dopo l’arrivo.'; return; }
      const eta = [...campi.querySelectorAll('select')].map(x => x.value);
      if (eta.some(v => !v)) { avviso.textContent = 'Indicate l\u2019età di ogni bambino.'; return; }
      const notti = Math.round((new Date(partenza.value) - new Date(arrivo.value)) / 864e5);
      const corpo = 'Ciao! Vorremmo sapere se Ca’ Hygge è disponibile:\n\n' +
        'Arrivo: ' + it(arrivo.value) + '\nPartenza: ' + it(partenza.value) + ' (' + notti + (notti === 1 ? ' notte' : ' notti') + ')\n' +
        'Adulti: ' + f.querySelector('#adulti').value + '\nBambini: ' + selB.value + (eta.length ? ' (età: ' + eta.join(', ') + ')' : '') + '\n' +
        (f.querySelector('#cane').checked ? 'Viaggiamo con un animale.\n' : '') + '\nGrazie!';
      const oggetto = 'Disponibilità Ca’ Hygge dal ' + it(arrivo.value) + ' al ' + it(partenza.value);
      location.href = 'mailto:cahygge@gmail.com?subject=' + encodeURIComponent(oggetto) + '&body=' + encodeURIComponent(corpo);
      avviso.textContent = 'Si apre la vostra app di posta con il messaggio già pronto: basta premere invia.';
    });
  }
}
