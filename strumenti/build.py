# Genera la landing page di Ca' Hygge (cartella principale del repository)
import html, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BOOKING = "https://www.booking.com/hotel/it/ca-hygge.it.html"
EMAIL = "cahygge@gmail.com"

# Per ora le foto arrivano dallo spazio Wix: quando avremo gli originali basterà cambiare url().
def url(fid, w):
    ext = "png" if fid.endswith(".png") else "jpg"
    fid = fid.replace(".png", "")
    return f"https://static.wixstatic.com/media/edddbc_{fid}~mv2.{ext}/v1/fit/w_{w},h_{w},q_85/cahygge.{ext}"

def img(fid, alt, sizes="100vw", lazy=True, cls=""):
    srcset = ", ".join(f"{url(fid, w)} {w}w" for w in (640, 1000, 1600, 2400))
    extra = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ""
    return f'<img src="{url(fid, 1600)}" srcset="{srcset}" sizes="{sizes}" alt="{html.escape(alt)}"{c}{extra}>'

LOGO = "dc55cf7d66d94ac6b43c7e1e61e67f1d.png"
F = {
    "cucina": "a683a34e2d8d4b698606e16364d71dea", "soggiorno": "9b73cc7bd9f04071ac35682df0bffee0",
    "camera_a": "7d14192eaec44b7b944c1dcac2818e8f", "pranzo_v": "d5b009735f654d9284377e1a082292ff",
    "soggiorno_b": "51295462b0764803babaa12f28c2f6d8", "camera_b": "3db47b2293854832977bbc45e60ffd4b",
    "camera_c": "55f278b6b8654b3c865788ac1fbbb9d6", "pranzo_b": "f4b5d545070c4f9f81ca86aa1d3345fb",
    "mansarda": "1793146089aa4642b812ef6236527ca8", "mansarda_v": "b6702fa3e4d140a3b3c489ff93b903d4",
    "singola": "97987d299a0f41108032316a4727c451", "bagno": "f657a088bc6248c8af4dfdb213c288e0",
    "cortesia": "b46ecf5fd4fa4cedac4dd9b60b8a04dc", "soggiorno_v": "6fab1b5ebbaa478680a86e8b434a724c",
    "pranzo_c": "61315d983a00419294bbb2508bfce7ce",
}
STAMPE = ["96453811213c4c339860fdc627a31bcb.png", "08d2715b3a934c88a73bb23b8b44f724.png",
          "fbb45c9a8ed44872a9a31055bca9c958.png", "4211c9fc650b44938e92d3f520bab17c"]

ICONE = {
    "letto": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 18V7M3 14h18v4M21 14v-2a3 3 0 0 0-3-3h-7v5M7 11.5a1.5 1.5 0 1 0 0-.01"/></svg>',
    "divano": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 11V8a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3M2 13a2 2 0 0 1 4 0v2h12v-2a2 2 0 0 1 4 0v4H2zM5 17v2M19 17v2"/></svg>',
    "auto": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 16V11l2-5h10l2 5v5M3 16h18v3H3zM7 13h.01M17 13h.01"/></svg>',
    "wifi": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 9a15 15 0 0 1 20 0M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0M12 19.5h.01"/></svg>',
    "zampa": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 14c-2 2-3 5 0 6s3-1 4-1 2 2 4 1 2-4 0-6-2-3-4-3-2 1-4 3zM6 9.5a1.5 2 0 1 0 0 .01M10 6.5a1.5 2 0 1 0 0 .01M14 6.5a1.5 2 0 1 0 0 .01M18 9.5a1.5 2 0 1 0 0 .01"/></svg>',
    "balcone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21V13h18v8M3 17h18M7 13v8M12 13v8M17 13v8M7 13V4h10v9"/></svg>',
    "lenzuola": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6h16v4H4zM4 10v8h16v-8M8 14h8"/></svg>',
    "caffe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9h13v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5zM17 10h1.5a2.5 2.5 0 0 1 0 5H17M8 3v3M12 3v3"/></svg>',
    "giochi": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="3"/><path d="M9 9h.01M15 9h.01M12 12h.01M9 15h.01M15 15h.01"/></svg>',
    "treno": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="3" width="14" height="13" rx="3"/><path d="M5 10h14M9 13h.01M15 13h.01M8 20l2-4M16 20l-2-4"/></svg>',
    "cuore": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/></svg>',
    "foglio": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 3h9l3 3v15H6zM9 10h6M9 14h6M9 18h4"/></svg>',
    "pianta": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 15h10l-1.5 6h-7zM12 15V9M12 9c0-3 2-5 5-5 0 3-2 5-5 5zM12 11c0-2.5-1.8-4-4-4 0 2.5 1.8 4 4 4z"/></svg>',
    "saponi": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 3h6M10 3v3M14 3v3M8 6h8v14a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1z"/></svg>',
}

STANZE = [
    ("soggiorno", "Soggiorno", "Il cuore della casa: luminoso, con il parquet caldo, il divano e la scala bianca che sale verso la mansarda. Qui la sera si gioca, si chiacchiera e si programma la gita del giorno dopo.",
     [("soggiorno", "Il soggiorno luminoso con la scala verso la mansarda"), ("soggiorno_b", "Il soggiorno con il divano e la porta finestra"), ("soggiorno_v", "Il soggiorno visto dall'ingresso")],
     [("divano", "Divano letto")]),
    ("cucina", "Cucina e pranzo", "Una cucina bianca e attrezzata, con macchina da caffè, e un tavolo tondo dove fare colazione con calma prima di scendere al mare.",
     [("cucina", "La cucina attrezzata con le piante sulla mensola"), ("pranzo_c", "Il tavolo tondo vicino alla cucina"), ("pranzo_v", "La zona pranzo con il tavolo bianco"), ("pranzo_b", "Il tavolo da pranzo con l'orchidea")],
     []),
    ("matrimoniale", "Camera matrimoniale", "Ampia e silenziosa, con due finestre che la riempiono di luce. Oltre al letto matrimoniale c'è un comodo divano letto.",
     [("camera_c", "La camera matrimoniale con il letto in ferro battuto"), ("camera_b", "La camera matrimoniale con il divano letto"), ("camera_a", "La camera matrimoniale vista dalla porta")],
     [("letto", "Letto matrimoniale"), ("divano", "Divano letto")]),
    ("mansarda", "Mansarda", "Il rifugio sotto il tetto in legno, con il lucernario: la stanza preferita da chi ama dormire un po' di più.",
     [("mansarda", "La mansarda con il soffitto in legno e il lucernario"), ("mansarda_v", "Il letto della mansarda")],
     [("letto", "Letto matrimoniale alla francese")]),
    ("cameretta", "Cameretta", "Piccola e raccolta, con le stampe in bianco e nero alle pareti: perfetta per un bambino o per chi viaggia da solo.",
     [("singola", "La cameretta con il letto singolo")],
     [("letto", "Letto singolo")]),
    ("bagno", "Bagno", "Con doccia e bidet. Asciugamani, lenzuola e un set di cortesia vi aspettano già.",
     [("bagno", "Il bagno con la doccia"), ("cortesia", "Il set di cortesia in bagno")],
     [("saponi", "Set di cortesia"), ("lenzuola", "Asciugamani e lenzuola")]),
]

TAPPE = [("Ca' Hygge", "0'", "si parte da qui"), ("Fermata bus", "1'", "proprio sotto casa"),
         ("Supermercato", "3'", "per la spesa"), ("Centro di Lavagna", "10'", "a piedi"),
         ("Centro di Chiavari", "10'", "a piedi"), ("Stazione", "15'", "a piedi")]

GITE = [("Sestri Levante", "La Baia del Silenzio e la Baia delle Favole, a pochi minuti."),
        ("Cinque Terre", "Monterosso, Vernazza, Manarola: tutte in treno, senza pensieri di parcheggio."),
        ("Camogli", "Le case colorate sul porticciolo e la focaccia al formaggio."),
        ("Portofino", "In treno fino a Santa Margherita, poi bus o battello.")]

VOCI = [("Casa curata nei particolari… Fornita di tutto ciò che può servire in ogni stanza.", ),
        ("Posizione, parcheggio gratuito adiacente, ottima ristrutturazione. Proprietari gentilissimi.", ),
        ("Spaziosa, accogliente e moderna. Ci siamo trovati veramente bene.", )]

SERVIZI = [("auto", "Parcheggio gratuito"), ("wifi", "WiFi gratuito"), ("zampa", "Animali ammessi"), ("balcone", "Balcone"),
           ("lenzuola", "Lenzuola e asciugamani"), ("caffe", "Macchina da caffè"), ("giochi", "Giochi da tavolo"), ("treno", "Stazione a 15 minuti")]


def stanza_html(i, s):
    chiave, nome, testo, foto, letti = s
    mini = "".join(
        f'<button type="button" aria-pressed="{"true" if j == 0 else "false"}" data-src="{url(F[k], 1600)}" data-alt="{html.escape(a)}" aria-label="Mostra: {html.escape(a)}">'
        f'<img src="{url(F[k], 200)}" alt="" loading="lazy"></button>'
        for j, (k, a) in enumerate(foto)) if len(foto) > 1 else ""
    let = "".join(f'<li>{ICONE[ic]}<span>{t}</span></li>' for ic, t in letti)
    return f'''<div class="stanza" role="tabpanel" id="pannello-{chiave}" aria-labelledby="tab-{chiave}"{"" if i == 0 else " hidden"}>
      <div><div class="grande">{img(F[foto[0][0]], foto[0][1], "(max-width:860px) 92vw, 60vw", lazy=i > 0)}</div>
      {f'<div class="miniature">{mini}</div>' if mini else ''}</div>
      <div class="info"><h3>{nome}</h3><p>{testo}</p>{f'<ul class="letti">{let}</ul>' if let else ''}</div>
    </div>'''


def pagina():
    tabs = "".join(f'<button type="button" role="tab" id="tab-{s[0]}" aria-controls="pannello-{s[0]}" aria-selected="{"true" if i == 0 else "false"}">{s[1]}</button>' for i, s in enumerate(STANZE))
    pannelli = "".join(stanza_html(i, s) for i, s in enumerate(STANZE))
    tappe = "".join(f'<div class="tappa"><small>{n}</small><b>{t}</b><span>{d}</span></div>' for n, t, d in TAPPE)
    gite = "".join(f'<div class="gita appare"><h3>{n}</h3><p>{d}</p><span class="treno">In treno da Lavagna</span></div>' for n, d in GITE)
    voci = "".join(f'<figure class="appare"><blockquote>{html.escape(v[0])}</blockquote><figcaption>Ospite su Booking.com</figcaption></figure>' for v in VOCI)
    servizi = "".join(f'<li>{ICONE[i]}<span>{t}</span></li>' for i, t in SERVIZI)
    stampe = "".join(img(s, "Stampa illustrata di Lavagna, collezione Visioni di Riviera", "(max-width:820px) 45vw, 20vw") for s in STAMPE)
    mail_stampe = f"mailto:{EMAIL}?subject=Stampe%20Visioni%20di%20Riviera"
    return f'''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ca' Hygge · Appartamento vacanze a Lavagna, vicino al mare</title>
<meta name="description" content="Ca' Hygge è un appartamento luminoso a Lavagna, a pochi passi dal mare e a 10 minuti a piedi dai centri di Lavagna e Chiavari. Tre camere, parcheggio gratuito, animali ammessi.">
<meta property="og:title" content="Ca' Hygge · Appartamento vacanze a Lavagna">
<meta property="og:description" content="Un appartamento luminoso a pochi passi dal mare, dove relax e bellezza si incontrano.">
<meta property="og:image" content="{url(F['soggiorno'], 1600)}">
<meta property="og:locale" content="it_IT">
<meta name="theme-color" content="#1f4b57">
<link rel="icon" href="{url(LOGO, 128)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://static.wixstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500&family=Karla:wght@400;500;600;700&family=Marcellus&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/stile.css?v=5">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"VacationRental","name":"Ca' Hygge","description":"Appartamento vacanze a Lavagna, a pochi passi dal mare.","image":"{url(F['soggiorno'], 1600)}","address":{{"@type":"PostalAddress","addressLocality":"Lavagna","addressRegion":"GE","addressCountry":"IT"}},"email":"{EMAIL}","sameAs":["{BOOKING}"]}}</script>
</head>
<body>
<a class="salta" href="#casa">Vai al contenuto</a>
<header class="testata">
  <div class="wrap">
    <a class="logo" href="#"><img src="{url(LOGO, 128)}" alt="" width="52" height="52"><b>CA' HYGGE</b></a>
    <nav aria-label="Menu"><ul class="menu">
      <li><a href="#casa">La casa</a></li><li><a href="#stanze">Le stanze</a></li><li><a href="#dintorni">Dintorni</a></li><li><a href="#ospiti">Ospiti</a></li>
      <li><a class="btn pesca" href="{BOOKING}" rel="noopener">Prenota</a></li>
    </ul></nav>
  </div>
</header>

<main>
<section class="hero">
  {img(F['soggiorno'], "Il soggiorno luminoso di Ca' Hygge con il parquet e la scala bianca", "100vw", lazy=False)}
  <div class="wrap">
    <div>
      <span class="mano">benvenuti a casa</span>
      <h1>Ca' Hygge, la vostra casa a Lavagna</h1>
      <p class="lead">Un appartamento luminoso a pochi passi dal mare, dove relax e bellezza si incontrano.</p>
      <div class="azioni"><a class="btn pesca" href="{BOOKING}" rel="noopener">Verifica la disponibilità</a><a class="btn chiaro" href="#stanze">Guarda le stanze</a></div>
    </div>
    <aside class="cartellino" data-tramonto>
      <div class="voto"><b>9,5</b><span>Eccezionale<small>su Booking.com · 55 recensioni</small></span></div>
      <hr>
      <p class="tramonto" style="margin:0">Stasera a Lavagna il sole tramonta alle <b data-ora>—</b>.<br><span class="mano" style="font-size:22px">giusto il tempo di arrivare in spiaggia</span></p>
    </aside>
  </div>
</section>
<div class="corda" aria-hidden="true"></div>

<section class="band" id="casa">
  <div class="wrap hygge">
    <div class="foto appare">{img(F['pranzo_c'], "Il tavolo tondo con le sedie bianche vicino alla cucina", "(max-width:820px) 90vw, 45vw")}<span class="nota">il caffè è già pronto</span></div>
    <div class="appare">
      <span class="occhiello">perché “hygge”?</span>
      <h2>Una casa al mare che sa di casa</h2>
      <p class="dizionario"><b>hygge</b> · <i>parola danese</i><br>la sensazione di calore e benessere che si prova nelle cose semplici: una coperta, una luce morbida, il tempo passato insieme.</p>
      <p>Abbiamo voluto che Ca' Hygge fosse questo: un posto dove appoggiare le valigie e sentirsi subito a proprio agio. Tre camere, un soggiorno luminoso, una cucina dove cucinare davvero, e il mare a pochi passi.</p>
      <ul class="piccole-cose">
        <li>{ICONE['foglio']}<span>Indicazioni e consigli lasciati anche per iscritto</span></li>
        <li>{ICONE['pianta']}<span>Piante, luce naturale e parquet caldo</span></li>
        <li>{ICONE['giochi']}<span>Giochi da tavolo per le serate in casa</span></li>
        <li>{ICONE['zampa']}<span>Anche il vostro cane è il benvenuto</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="band stanze" id="stanze">
  <div class="wrap">
    <span class="occhiello">fate un giro</span>
    <h2>Le stanze</h2>
    <div class="tabs" role="tablist" aria-label="Stanze della casa">{tabs}</div>
    {pannelli}
    <div class="posti">
      <div><b>3</b>camere da letto</div><div><b>2</b>divani letto</div><div><b>1</b>bagno con doccia</div><div><b>1</b>balcone</div>
    </div>
  </div>
</section>

<section class="band passeggiata" id="dintorni">
  <div class="wrap">
    <div class="intro appare">
      <div><span class="occhiello">tutto a portata di mano</span><h2>A piedi da Ca' Hygge</h2></div>
      <p style="max-width:42ch;margin:0">A pochi passi dal mare e a 10 minuti a piedi sia dal centro di Lavagna sia da quello di Chiavari. Qui la macchina potete lasciarla al parcheggio gratuito.</p>
    </div>
    <div class="percorso appare">{tappe}</div>
    <div class="gite">{gite}</div>
  </div>
</section>

<section class="band voci" id="ospiti">
  <div class="wrap">
    <div class="testa appare">
      <div><span class="occhiello">dicono di noi</span><h2>Le parole dei nostri ospiti</h2></div>
      <div class="punteggio"><b>9,5</b><div><strong>Eccezionale</strong><br><span style="color:var(--grigio);font-size:15px">55 recensioni su Booking.com</span></div></div>
    </div>
    <div class="citazioni">{voci}</div>
    <h3 style="margin-top:64px">Cosa trovate in casa</h3>
    <ul class="servizi">{servizi}</ul>
  </div>
</section>

<section class="band">
  <div class="wrap stampe">
    <div class="appare">
      <span class="occhiello">un ricordo da portare a casa</span>
      <h2>Visioni di Riviera</h2>
      <p>Una serie di stampe digitali ispirate ai colori, alla luce e all'atmosfera della Riviera: il porto, il tramonto, le vele, la mappa illustrata di Lavagna. Un frammento autentico di Lavagna da appendere a casa vostra.</p>
      <p><a class="btn chiaro" href="{mail_stampe}">Chiedi le stampe</a></p>
      <p style="font-size:14px;color:var(--grigio)">Scrivete a {EMAIL}</p>
    </div>
    <div class="quadri appare">{stampe}</div>
  </div>
</section>

<section class="band prenota">
  {img(F['mansarda'], "", "100vw")}
  <div class="wrap">
    <span class="mano" style="color:var(--pesca);font-size:34px">vi aspettiamo!</span>
    <h2>Il mare è qui, la casa pure</h2>
    <p>Controllate le date libere e prenotate su Booking.com. Per qualsiasi domanda, scriveteci: rispondiamo volentieri.</p>
    <div class="azioni"><a class="btn pesca" href="{BOOKING}" rel="noopener">Verifica la disponibilità</a><a class="btn chiaro" href="mailto:{EMAIL}">Scrivici</a></div>
  </div>
</section>
</main>

<footer class="piede">
  <div class="wrap">
    <a class="logo" href="#"><img src="{url(LOGO, 128)}" alt="" width="52" height="52"><b>CA' HYGGE</b></a>
    <span>Appartamento vacanze a Lavagna (GE)</span>
    <span><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{BOOKING}" rel="noopener">Booking.com</a></span>
  </div>
</footer>
<script src="js/sole.js"></script>
<script src="js/casa.js?v=5"></script>
</body>
</html>
'''

open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(pagina())
print("ok")
