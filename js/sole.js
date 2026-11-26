/* Calcolo della posizione del sole (formule di SunCalc, V. Agafonkin, licenza BSD).
   Restituisce gli orari di tramonto, golden hour e ora blu per una data e un luogo. */
(function () {
  var PI = Math.PI, rad = PI / 180, giorno = 864e5, J1970 = 2440588, J2000 = 2451545, e = rad * 23.4397, J0 = 0.0009;
  function aGiorni(d) { return d.valueOf() / giorno - 0.5 + J1970 - J2000; }
  function daGiuliano(j) { return new Date((j + 0.5 - J1970) * giorno); }
  function anomalia(d) { return rad * (357.5291 + 0.98560028 * d); }
  function longitudine(M) {
    var C = rad * (1.9148 * Math.sin(M) + 0.02 * Math.sin(2 * M) + 0.0003 * Math.sin(3 * M));
    return M + C + rad * 102.9372 + PI;
  }
  function declinazione(l) { return Math.asin(Math.sin(e) * Math.sin(l)); }
  function transito(ds, M, L) { return J2000 + ds + 0.0053 * Math.sin(M) - 0.0069 * Math.sin(2 * L); }
  function approx(Ht, lw, n) { return J0 + (Ht + lw) / (2 * PI) + n; }

  /* data: oggetto Date (va bene mezzogiorno del giorno scelto); altezze in gradi */
  function orari(data, lat, lng) {
    var lw = rad * -lng, phi = rad * lat, d = aGiorni(data);
    var n = Math.round(d - J0 - lw / (2 * PI));
    var ds = approx(0, lw, n), M = anomalia(ds), L = longitudine(M), dec = declinazione(L);
    var Jmezzodi = transito(ds, M, L);
    function aAltezza(h) {
      var x = (Math.sin(h * rad) - Math.sin(phi) * Math.sin(dec)) / (Math.cos(phi) * Math.cos(dec));
      if (x < -1 || x > 1) return null;
      var Jsera = transito(approx(Math.acos(x), lw, n), M, L);
      return { mattina: daGiuliano(Jmezzodi - (Jsera - Jmezzodi)), sera: daGiuliano(Jsera) };
    }
    var a6 = aAltezza(6), tr = aAltezza(-0.833), b4 = aAltezza(-4), c6 = aAltezza(-6);
    return {
      alba: tr && tr.mattina,
      fineGoldenMattina: a6 && a6.mattina,
      inizioGolden: a6 && a6.sera,
      tramonto: tr && tr.sera,
      inizioBlu: b4 && b4.sera,
      fineBlu: c6 && c6.sera
    };
  }

  /* Mezzogiorno italiano del giorno "aaaa-mm-gg", indipendente dal fuso del visitatore */
  function mezzogiorno(iso) {
    var p = iso.split('-').map(Number);
    return new Date(Date.UTC(p[0], p[1] - 1, p[2], 11, 0, 0));
  }
  var fmt = new Intl.DateTimeFormat('it-IT', { hour: '2-digit', minute: '2-digit', timeZone: 'Europe/Rome' });
  function ora(d) { return d ? fmt.format(d) : '—'; }

  var LUOGHI = [
    ['Chiavari', 44.3169, 9.3222], ['Lavagna', 44.3076, 9.3443], ['Sestri Levante', 44.2721, 9.3967],
    ['Moneglia', 44.2390, 9.4910], ['Rapallo', 44.3497, 9.2306], ['Santa Margherita Ligure', 44.3346, 9.2117],
    ['Portofino', 44.3036, 9.2097], ['San Fruttuoso', 44.3157, 9.1745], ['Camogli', 44.3496, 9.1550],
    ['Recco', 44.3622, 9.1435], ['Genova', 44.4056, 8.9463], ['Nervi', 44.3810, 9.0370],
    ['Levanto', 44.1700, 9.6110], ['Monterosso al Mare', 44.1462, 9.6545], ['Vernazza', 44.1350, 9.6847],
    ['Manarola', 44.1067, 9.7280], ['Portovenere', 44.0507, 9.8355], ['Lerici', 44.0757, 9.9117],
    ['La Spezia', 44.1025, 9.8241], ['Varazze', 44.3596, 8.5757], ['Savona', 44.3091, 8.4772],
    ['Finale Ligure', 44.1693, 8.3437], ['Alassio', 44.0079, 8.1726], ['Sanremo', 43.8159, 7.7761]
  ];

  window.Sole = { orari: orari, mezzogiorno: mezzogiorno, ora: ora, LUOGHI: LUOGHI };
})();
