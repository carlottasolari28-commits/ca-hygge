# Genera la landing page di Ca' Hygge (cartella principale del repository)
import html, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
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
    "fumo": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 5h18v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><circle cx="12" cy="7.5" r="1"/><path d="M8 14c1 1 1 2 0 3s-1 2 0 3M12 14c1 1 1 2 0 3s-1 2 0 3M16 14c1 1 1 2 0 3s-1 2 0 3"/></svg>',
    "co": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="4"/><path d="M11 10.5a2 2 0 1 0 0 3M15 10a2 2 0 1 1 0 4 2 2 0 0 1 0-4z"/><path d="M8 17h.01"/></svg>',
    "lavatrice": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M4 7h16M7 5h.01M10 5h.01"/><circle cx="12" cy="14" r="4"/></svg>',
    "bollitore": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 8h9l1 12H6zM16 10h2a2 2 0 0 1 0 4h-1.5M9 8V6a3 3 0 0 1 6 0v2M5 20h14"/></svg>',
    "microonde": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="13" rx="2"/><rect x="6" y="8" width="9" height="7" rx="1"/><path d="M18 9h.01M18 12h.01M18 15h.01"/></svg>',
    "tv": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="12" rx="2"/><path d="M8 21h8M12 17v4M10 9l4 2-4 2z"/></svg>',
    "bici": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="5.5" cy="16" r="3.5"/><circle cx="18.5" cy="16" r="3.5"/><path d="M5.5 16 9 9h7l2.5 7M9 9l3.5 7h-7M15 6h2.5l-1.5 3M8 6h3"/></svg>',
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


LINGUE = ["it", "en", "de", "fr", "es"]
NOMI_LINGUA = {"it": "Italiano", "en": "English", "de": "Deutsch", "fr": "Français", "es": "Español"}

# Chiavi delle foto delle stanze, uguali per tutte le lingue
FOTO_STANZE = [
    ("soggiorno", ["soggiorno", "soggiorno_b", "soggiorno_v"], ["divano"]),
    ("cucina", ["cucina", "pranzo_c", "pranzo_v", "pranzo_b"], []),
    ("matrimoniale", ["camera_c", "camera_b", "camera_a"], ["letto", "divano"]),
    ("mansarda", ["mansarda", "mansarda_v"], ["letto"]),
    ("cameretta", ["singola"], ["letto"]),
    ("bagno", ["bagno", "cortesia"], ["saponi", "lenzuola"]),
]
ICONE_SERVIZI = ["auto", "wifi", "tv", "lavatrice", "microonde", "bollitore", "caffe", "zampa", "balcone",
                 "lenzuola", "giochi", "bici", "treno", "fumo", "co"]
ICONE_PICCOLE = ["foglio", "pianta", "giochi", "zampa"]

T = {}

T["it"] = dict(
    locale="it_IT",
    title="Ca' Hygge · Appartamento vacanze a Lavagna, vicino al mare",
    desc="Ca' Hygge è un appartamento luminoso a Lavagna, a 10 minuti a piedi dai centri di Lavagna e Chiavari. Tre camere, WiFi, Netflix e Prime Video, lavatrice, animali ammessi.",
    og_desc="Un appartamento luminoso a pochi passi dal mare, dove relax e bellezza si incontrano.",
    salta="Vai al contenuto", menu="Menu", lingua="Lingua",
    nav=["La casa", "Le stanze", "Dintorni", "Ospiti", "Prenota"],
    hero_alt="Il soggiorno luminoso di Ca' Hygge con il parquet e la scala bianca",
    benvenuti="benvenuti a casa",
    h1="Ca' Hygge, la vostra casa a Lavagna",
    lead="Un appartamento luminoso a pochi passi dal mare, dove relax e bellezza si incontrano.",
    vantaggio="Le tariffe più convenienti le trovate solo prenotando qui, direttamente con noi.",
    cta_disp="Chiedi la disponibilità", cta_stanze="Guarda le stanze",
    voto="9,5", eccezionale="Eccezionale", su_booking="su Booking.com · 55 recensioni",
    tramonto="Stasera a Lavagna il sole tramonta alle", tramonto_nota="giusto il tempo di arrivare in spiaggia",
    casa_alt="Il tavolo tondo con le sedie bianche vicino alla cucina", nota_caffe="il caffè è già pronto",
    occh_hygge="perché “hygge”?", h2_casa="Una casa al mare che sa di casa", parola_danese="parola danese",
    diz="la sensazione di calore e benessere che si prova nelle cose semplici: una coperta, una luce morbida, il tempo passato insieme.",
    casa_p="Abbiamo voluto che Ca' Hygge fosse questo: un posto dove appoggiare le valigie e sentirsi subito a proprio agio. Tre camere, un soggiorno luminoso, una cucina dove cucinare davvero, e il mare a pochi passi.",
    piccole=["Indicazioni e consigli lasciati anche per iscritto", "Piante, luce naturale e parquet caldo", "Giochi da tavolo per le serate in casa", "Anche il vostro cane è il benvenuto"],
    occh_stanze="fate un giro", h2_stanze="Le stanze", tabs_label="Stanze della casa", mostra="Mostra",
    stanze=[
        ("Soggiorno", "Il cuore della casa: luminoso, con il parquet caldo, il divano e la scala bianca che sale verso la mansarda. La sera, Netflix e Prime Video sulla TV, un gioco da tavolo o il programma della gita del giorno dopo.",
         ["Il soggiorno luminoso con la scala verso la mansarda", "Il soggiorno con il divano e la porta finestra", "Il soggiorno visto dall'ingresso"], ["Divano letto"]),
        ("Cucina e pranzo", "Una cucina bianca e attrezzata, con macchina da caffè, bollitore e microonde, e un tavolo tondo dove fare colazione con calma prima di scendere al mare.",
         ["La cucina attrezzata con le piante sulla mensola", "Il tavolo tondo vicino alla cucina", "La zona pranzo con il tavolo bianco", "Il tavolo da pranzo con l'orchidea"], []),
        ("Camera matrimoniale", "Ampia e silenziosa, con due finestre che la riempiono di luce. Oltre al letto matrimoniale c'è un comodo divano letto.",
         ["La camera matrimoniale con il letto in ferro battuto", "La camera matrimoniale con il divano letto", "La camera matrimoniale vista dalla porta"], ["Letto matrimoniale", "Divano letto"]),
        ("Mansarda", "Il rifugio sotto il tetto in legno, con il lucernario: la stanza preferita da chi ama dormire un po' di più.",
         ["La mansarda con il soffitto in legno e il lucernario", "Il letto della mansarda"], ["Letto matrimoniale alla francese"]),
        ("Cameretta", "Piccola e raccolta, con le stampe in bianco e nero alle pareti: perfetta per un bambino o per chi viaggia da solo.",
         ["La cameretta con il letto singolo"], ["Letto singolo"]),
        ("Bagno", "Con doccia e bidet. Asciugamani, lenzuola e un set di cortesia vi aspettano già, e in casa c'è anche la lavatrice.",
         ["Il bagno con la doccia", "Il set di cortesia in bagno"], ["Set di cortesia", "Asciugamani e lenzuola"]),
    ],
    posti=["camere da letto", "divani letto", "bagno con doccia", "balcone"],
    occh_dintorni="tutto a portata di mano", h2_dintorni="A piedi da Ca' Hygge",
    dintorni_p="A 10 minuti a piedi sia dal centro di Lavagna sia da quello di Chiavari, e a un quarto d'ora dal mare. Per l'auto ci sono parcheggi pubblici nelle immediate vicinanze.",
    tappe=[("Ca' Hygge", "si parte da qui"), ("Fermata bus", "proprio sotto casa"), ("Supermercato", "per la spesa"),
           ("Centro di Lavagna", ""), ("Centro di Chiavari", ""), ("Mare", ""), ("Stazione", "")],
    bici_aria="Illustrazione di una bicicletta con il cestino, davanti al mare e al sole",
    bici_occh="pedalando verso il mare", bici_h3="Noleggio biciclette per adulti",
    bici_p="Da Ca' Hygge potete muovervi anche in bicicletta: è disponibile il noleggio di bici per adulti, perfetto per arrivare al mare, fare un giro sul lungomare o raggiungere Chiavari senza pensieri di parcheggio.",
    bici_nota="Chiedetecele quando ci scrivete per la disponibilità.",
    gite=["La Baia del Silenzio e la Baia delle Favole, a pochi minuti.", "Monterosso, Vernazza, Manarola: tutte in treno, senza pensieri di parcheggio.",
          "Le case colorate affacciate sul porticciolo.", "In treno fino a Santa Margherita, poi bus o battello."],
    in_treno="In treno da Lavagna",
    occh_voci="dicono di noi", h2_voci="Le parole dei nostri ospiti", recensioni="55 recensioni su Booking.com",
    voci=["Casa curata nei particolari… Fornita di tutto ciò che può servire in ogni stanza.",
          "Posizione, arredamento, accessori per vivere l'appartamento.",
          "Spaziosa, accogliente e moderna. Ci siamo trovati veramente bene."],
    voce_cap="Ospite su Booking.com",
    h3_servizi="Cosa offriamo",
    servizi=["Parcheggi pubblici vicinissimi", "WiFi gratuito", "Netflix e Prime Video", "Lavatrice", "Microonde", "Bollitore",
             "Macchina da caffè", "Animali ammessi", "Balcone", "Lenzuola e asciugamani", "Giochi da tavolo", "Noleggio bici per adulti", "Stazione a 15 minuti", "Rilevatore di fumo", "Rilevatore di monossido di carbonio"],
    occh_stampe="un ricordo da portare a casa",
    stampe_p="Una serie di stampe digitali ispirate ai colori, alla luce e all'atmosfera della Riviera: il porto, il tramonto, le vele, la mappa illustrata di Lavagna. Un frammento autentico di Lavagna da appendere a casa vostra.",
    stampe_btn="Chiedi le stampe", scrivete_a="Scrivete a", stampe_alt="Stampa illustrata di Lavagna, collezione Visioni di Riviera",
    stampe_oggetto="Stampe Visioni di Riviera",
    aspettiamo="vi aspettiamo!", h2_prenota="Disponibilità e prenotazioni",
    risparmio="Prenotando direttamente da qui trovate sempre le tariffe più convenienti.",
    prenota_p="Per sapere se le vostre date sono libere e per prenotare, scriveteci direttamente: vi rispondiamo noi, senza intermediari.",
    arrivo="Arrivo", partenza="Partenza", adulti="Adulti", bambini="Bambini", eta_titolo="Età dei bambini",
    cane="Viaggiamo con un animale", invia="Scrivici per la disponibilità", oppure="Oppure scriveteci a",
    piede="Appartamento vacanze a Lavagna (GE)",
    js=dict(scegli="Scegli", meno1="meno di 1 anno", anno="anno", anni="anni", bambino="Bambino",
            errDate="Indicate le date di arrivo e di partenza.", errOrdine="La partenza deve essere dopo l’arrivo.",
            errEta="Indicate l’età di ogni bambino.", ok="Si apre la vostra app di posta con il messaggio già pronto: basta premere invia.",
            mIntro="Ciao! Vorremmo sapere se Ca’ Hygge è disponibile:", arrivo="Arrivo", partenza="Partenza", notte="notte", notti="notti",
            adulti="Adulti", bambini="Bambini", etaBreve="età", mAnimale="Viaggiamo con un animale.", mGrazie="Grazie!",
            mOggetto="Disponibilità Ca’ Hygge"),
)

T["en"] = dict(
    locale="en_GB",
    title="Ca' Hygge · Holiday apartment in Lavagna, near the sea",
    desc="Ca' Hygge is a bright holiday apartment in Lavagna, Italian Riviera, a 10-minute walk from the centres of Lavagna and Chiavari. Three bedrooms, WiFi, Netflix and Prime Video, washing machine, pets welcome.",
    og_desc="A bright apartment a short walk from the sea, where relaxation and beauty meet.",
    salta="Skip to content", menu="Menu", lingua="Language",
    nav=["The house", "Rooms", "Surroundings", "Guests", "Book"],
    hero_alt="The bright living room of Ca' Hygge with wooden floors and a white staircase",
    benvenuti="welcome home",
    h1="Ca' Hygge, your home in Lavagna",
    lead="A bright apartment a short walk from the sea, where relaxation and beauty meet.",
    vantaggio="You'll only find our best rates by booking here, directly with us.",
    cta_disp="Check availability", cta_stanze="See the rooms",
    voto="9.5", eccezionale="Exceptional", su_booking="on Booking.com · 55 reviews",
    tramonto="Tonight in Lavagna the sun sets at", tramonto_nota="just enough time to get to the beach",
    casa_alt="The round table with white chairs next to the kitchen", nota_caffe="the coffee is ready",
    occh_hygge="why “hygge”?", h2_casa="A seaside house that feels like home", parola_danese="Danish word",
    diz="the feeling of warmth and wellbeing found in simple things: a blanket, soft light, time spent together.",
    casa_p="That's what we wanted Ca' Hygge to be: a place to put your bags down and feel at ease straight away. Three bedrooms, a bright living room, a kitchen to really cook in, and the sea close by.",
    piccole=["Tips and directions also left in writing", "Plants, natural light and warm wooden floors", "Board games for evenings in", "Your dog is welcome too"],
    occh_stanze="take a look around", h2_stanze="The rooms", tabs_label="Rooms of the house", mostra="Show",
    stanze=[
        ("Living room", "The heart of the house: bright, with warm wooden floors, the sofa and the white staircase leading up to the attic room. In the evening: Netflix and Prime Video on the TV, a board game, or planning tomorrow's trip.",
         ["The bright living room with the staircase to the attic", "The living room with the sofa and French window", "The living room seen from the entrance"], ["Sofa bed"]),
        ("Kitchen and dining", "A white, fully equipped kitchen with coffee machine, kettle and microwave, and a round table for a slow breakfast before heading to the beach.",
         ["The equipped kitchen with plants on the shelf", "The round table next to the kitchen", "The dining area with the white table", "The dining table with the orchid"], []),
        ("Double bedroom", "Spacious and quiet, with two windows that fill it with light. Besides the double bed there is a comfortable sofa bed.",
         ["The double bedroom with the wrought-iron bed", "The double bedroom with the sofa bed", "The double bedroom seen from the door"], ["Double bed", "Sofa bed"]),
        ("Attic room", "The hideaway under the wooden roof, with a skylight: the favourite room for those who like a lie-in.",
         ["The attic room with wooden ceiling and skylight", "The bed in the attic room"], ["French double bed"]),
        ("Small bedroom", "Small and cosy, with black-and-white prints on the walls: perfect for a child or a solo traveller.",
         ["The small bedroom with the single bed"], ["Single bed"]),
        ("Bathroom", "With shower and bidet. Towels, bed linen and a courtesy set are waiting for you, and there's a washing machine in the house.",
         ["The bathroom with the shower", "The courtesy set in the bathroom"], ["Courtesy set", "Towels and bed linen"]),
    ],
    posti=["bedrooms", "sofa beds", "bathroom with shower", "balcony"],
    occh_dintorni="everything within reach", h2_dintorni="On foot from Ca' Hygge",
    dintorni_p="A 10-minute walk from both Lavagna and Chiavari town centres, and 15 minutes from the sea. If you come by car, there is public parking right nearby.",
    tappe=[("Ca' Hygge", "start here"), ("Bus stop", "right outside"), ("Supermarket", "for groceries"),
           ("Lavagna centre", ""), ("Chiavari centre", ""), ("Sea", ""), ("Station", "")],
    bici_aria="Illustration of a bicycle with a basket, in front of the sea and the sun",
    bici_occh="cycling to the sea", bici_h3="Bike hire for adults",
    bici_p="You can also get around by bike: bike hire for adults is available, perfect for reaching the beach, riding along the seafront or getting to Chiavari without worrying about parking.",
    bici_nota="Just ask when you write to us about availability.",
    gite=["The Bay of Silence and the Bay of Fables, just a few minutes away.", "Monterosso, Vernazza, Manarola: all by train, no parking worries.",
          "Colourful houses overlooking the little harbour.", "Train to Santa Margherita, then bus or boat."],
    in_treno="By train from Lavagna",
    occh_voci="what guests say", h2_voci="In our guests' words", recensioni="55 reviews on Booking.com",
    voci=["A house cared for down to the details… Equipped with everything you could need in every room.",
          "Location, furnishings, everything you need to live in the apartment.",
          "Spacious, welcoming and modern. We felt really at home."],
    voce_cap="Guest on Booking.com · translated from Italian",
    h3_servizi="What we offer",
    servizi=["Public parking right nearby", "Free WiFi", "Netflix and Prime Video", "Washing machine", "Microwave", "Kettle",
             "Coffee machine", "Pets allowed", "Balcony", "Bed linen and towels", "Board games", "Bike hire for adults", "Station 15 minutes away", "Smoke detector", "Carbon monoxide detector"],
    occh_stampe="a souvenir to take home",
    stampe_p="A series of digital prints inspired by the colours, light and atmosphere of the Riviera: the harbour, the sunset, the sails, the illustrated map of Lavagna. An authentic piece of Lavagna to hang at home.",
    stampe_btn="Ask about the prints", scrivete_a="Write to", stampe_alt="Illustrated print of Lavagna, Visioni di Riviera collection",
    stampe_oggetto="Visioni di Riviera prints",
    aspettiamo="see you soon!", h2_prenota="Availability and bookings",
    risparmio="Booking directly here always gets you our best rates.",
    prenota_p="To find out if your dates are free and to book, write to us directly: we'll reply personally, with no middlemen.",
    arrivo="Arrival", partenza="Departure", adulti="Adults", bambini="Children", eta_titolo="Children's ages",
    cane="We're travelling with a pet", invia="Ask us about availability", oppure="Or write to us at",
    piede="Holiday apartment in Lavagna (Genoa, Italy)",
    js=dict(scegli="Choose", meno1="under 1 year", anno="year", anni="years", bambino="Child",
            errDate="Please enter your arrival and departure dates.", errOrdine="Departure must be after arrival.",
            errEta="Please enter the age of each child.", ok="Your email app will open with the message ready: just press send.",
            mIntro="Hello! We'd like to know if Ca’ Hygge is available:", arrivo="Arrival", partenza="Departure", notte="night", notti="nights",
            adulti="Adults", bambini="Children", etaBreve="ages", mAnimale="We're travelling with a pet.", mGrazie="Thank you!",
            mOggetto="Availability Ca’ Hygge"),
)

T["de"] = dict(
    locale="de_DE",
    title="Ca' Hygge · Ferienwohnung in Lavagna, nahe am Meer",
    desc="Ca' Hygge ist eine helle Ferienwohnung in Lavagna an der Italienischen Riviera, 10 Gehminuten von den Zentren von Lavagna und Chiavari. Drei Schlafzimmer, WLAN, Netflix und Prime Video, Waschmaschine, Haustiere willkommen.",
    og_desc="Eine helle Wohnung nur wenige Schritte vom Meer, wo Entspannung und Schönheit sich begegnen.",
    salta="Zum Inhalt", menu="Menü", lingua="Sprache",
    nav=["Das Haus", "Zimmer", "Umgebung", "Gäste", "Buchen"],
    hero_alt="Das helle Wohnzimmer von Ca' Hygge mit Parkett und weißer Treppe",
    benvenuti="willkommen zu Hause",
    h1="Ca' Hygge, Ihr Zuhause in Lavagna",
    lead="Eine helle Wohnung nur wenige Schritte vom Meer, wo Entspannung und Schönheit sich begegnen.",
    vantaggio="Die günstigsten Preise gibt es nur bei direkter Buchung hier bei uns.",
    cta_disp="Verfügbarkeit anfragen", cta_stanze="Zimmer ansehen",
    voto="9,5", eccezionale="Hervorragend", su_booking="auf Booking.com · 55 Bewertungen",
    tramonto="Heute Abend geht die Sonne in Lavagna unter um", tramonto_nota="gerade genug Zeit für den Weg zum Strand",
    casa_alt="Der runde Tisch mit weißen Stühlen neben der Küche", nota_caffe="der Kaffee ist fertig",
    occh_hygge="warum „hygge“?", h2_casa="Ein Haus am Meer, das sich wie Zuhause anfühlt", parola_danese="dänisches Wort",
    diz="das Gefühl von Wärme und Wohlbefinden in einfachen Dingen: eine Decke, sanftes Licht, gemeinsame Zeit.",
    casa_p="Genau das sollte Ca' Hygge sein: ein Ort, an dem man die Koffer abstellt und sich sofort wohlfühlt. Drei Schlafzimmer, ein helles Wohnzimmer, eine Küche zum richtigen Kochen und das Meer ganz in der Nähe.",
    piccole=["Hinweise und Tipps auch schriftlich", "Pflanzen, Tageslicht und warmes Parkett", "Brettspiele für gemütliche Abende", "Auch Ihr Hund ist willkommen"],
    occh_stanze="ein kleiner Rundgang", h2_stanze="Die Zimmer", tabs_label="Zimmer des Hauses", mostra="Zeigen",
    stanze=[
        ("Wohnzimmer", "Das Herz des Hauses: hell, mit warmem Parkett, dem Sofa und der weißen Treppe zum Dachzimmer. Abends Netflix und Prime Video auf dem Fernseher, ein Brettspiel oder die Planung des nächsten Ausflugs.",
         ["Das helle Wohnzimmer mit der Treppe zum Dachzimmer", "Das Wohnzimmer mit Sofa und Balkontür", "Das Wohnzimmer vom Eingang aus"], ["Schlafsofa"]),
        ("Küche und Essbereich", "Eine weiße, voll ausgestattete Küche mit Kaffeemaschine, Wasserkocher und Mikrowelle und ein runder Tisch für ein entspanntes Frühstück, bevor es zum Strand geht.",
         ["Die ausgestattete Küche mit Pflanzen auf dem Regal", "Der runde Tisch neben der Küche", "Der Essbereich mit dem weißen Tisch", "Der Esstisch mit der Orchidee"], []),
        ("Doppelzimmer", "Geräumig und ruhig, mit zwei Fenstern, die es mit Licht füllen. Neben dem Doppelbett gibt es ein bequemes Schlafsofa.",
         ["Das Doppelzimmer mit dem schmiedeeisernen Bett", "Das Doppelzimmer mit dem Schlafsofa", "Das Doppelzimmer von der Tür aus"], ["Doppelbett", "Schlafsofa"]),
        ("Dachzimmer", "Der Rückzugsort unter dem Holzdach, mit Dachfenster: das Lieblingszimmer aller, die gern etwas länger schlafen.",
         ["Das Dachzimmer mit Holzdecke und Dachfenster", "Das Bett im Dachzimmer"], ["Französisches Bett"]),
        ("Kleines Zimmer", "Klein und gemütlich, mit Schwarz-Weiß-Drucken an den Wänden: ideal für ein Kind oder Alleinreisende.",
         ["Das kleine Zimmer mit dem Einzelbett"], ["Einzelbett"]),
        ("Bad", "Mit Dusche und Bidet. Handtücher, Bettwäsche und Pflegeprodukte liegen bereit, und in der Wohnung gibt es eine Waschmaschine.",
         ["Das Bad mit der Dusche", "Die Pflegeprodukte im Bad"], ["Pflegeprodukte", "Handtücher und Bettwäsche"]),
    ],
    posti=["Schlafzimmer", "Schlafsofas", "Bad mit Dusche", "Balkon"],
    occh_dintorni="alles in der Nähe", h2_dintorni="Zu Fuß von Ca' Hygge",
    dintorni_p="10 Gehminuten bis in die Zentren von Lavagna und Chiavari und eine Viertelstunde bis zum Meer. Öffentliche Parkplätze gibt es in unmittelbarer Nähe.",
    tappe=[("Ca' Hygge", "hier geht's los"), ("Bushaltestelle", "direkt vor dem Haus"), ("Supermarkt", "zum Einkaufen"),
           ("Zentrum Lavagna", ""), ("Zentrum Chiavari", ""), ("Meer", ""), ("Bahnhof", "")],
    bici_aria="Illustration eines Fahrrads mit Korb vor Meer und Sonne",
    bici_occh="mit dem Rad ans Meer", bici_h3="Fahrradverleih für Erwachsene",
    bici_p="Sie können sich auch mit dem Fahrrad bewegen: Es gibt einen Fahrradverleih für Erwachsene, ideal für den Weg zum Strand, eine Runde an der Uferpromenade oder einen Ausflug nach Chiavari ohne Parkplatzsorgen.",
    bici_nota="Fragen Sie einfach danach, wenn Sie uns wegen der Verfügbarkeit schreiben.",
    gite=["Die Baia del Silenzio und die Baia delle Favole, nur wenige Minuten entfernt.", "Monterosso, Vernazza, Manarola: alles mit dem Zug, ohne Parkplatzsorgen.",
          "Bunte Häuser rund um den kleinen Hafen.", "Mit dem Zug nach Santa Margherita, dann Bus oder Boot."],
    in_treno="Mit dem Zug ab Lavagna",
    occh_voci="was Gäste sagen", h2_voci="Die Worte unserer Gäste", recensioni="55 Bewertungen auf Booking.com",
    voci=["Ein Haus, gepflegt bis ins Detail… In jedem Raum ist alles vorhanden, was man braucht.",
          "Lage, Einrichtung, Ausstattung für das Leben in der Wohnung.",
          "Geräumig, gemütlich und modern. Wir haben uns wirklich wohlgefühlt."],
    voce_cap="Gast auf Booking.com · aus dem Italienischen übersetzt",
    h3_servizi="Was wir bieten",
    servizi=["Öffentliche Parkplätze ganz in der Nähe", "Kostenloses WLAN", "Netflix und Prime Video", "Waschmaschine", "Mikrowelle", "Wasserkocher",
             "Kaffeemaschine", "Haustiere erlaubt", "Balkon", "Bettwäsche und Handtücher", "Brettspiele", "Fahrradverleih für Erwachsene", "Bahnhof in 15 Minuten", "Rauchmelder", "Kohlenmonoxidmelder"],
    occh_stampe="eine Erinnerung für Zuhause",
    stampe_p="Eine Serie digitaler Drucke, inspiriert von Farben, Licht und Stimmung der Riviera: der Hafen, der Sonnenuntergang, die Segel, die illustrierte Karte von Lavagna. Ein echtes Stück Lavagna für Ihre Wand.",
    stampe_btn="Drucke anfragen", scrivete_a="Schreiben Sie an", stampe_alt="Illustrierter Druck von Lavagna, Kollektion Visioni di Riviera",
    stampe_oggetto="Drucke Visioni di Riviera",
    aspettiamo="wir freuen uns auf Sie!", h2_prenota="Verfügbarkeit und Buchung",
    risparmio="Bei direkter Buchung hier erhalten Sie immer die günstigsten Preise.",
    prenota_p="Um zu erfahren, ob Ihre Daten frei sind, und um zu buchen, schreiben Sie uns direkt: Wir antworten persönlich, ohne Vermittler.",
    arrivo="Anreise", partenza="Abreise", adulti="Erwachsene", bambini="Kinder", eta_titolo="Alter der Kinder",
    cane="Wir reisen mit einem Haustier", invia="Verfügbarkeit anfragen", oppure="Oder schreiben Sie an",
    piede="Ferienwohnung in Lavagna (Genua, Italien)",
    js=dict(scegli="Auswählen", meno1="unter 1 Jahr", anno="Jahr", anni="Jahre", bambino="Kind",
            errDate="Bitte geben Sie An- und Abreisedatum an.", errOrdine="Die Abreise muss nach der Anreise liegen.",
            errEta="Bitte geben Sie das Alter jedes Kindes an.", ok="Ihr E-Mail-Programm öffnet sich mit der fertigen Nachricht: einfach auf Senden drücken.",
            mIntro="Hallo! Wir möchten gern wissen, ob Ca’ Hygge frei ist:", arrivo="Anreise", partenza="Abreise", notte="Nacht", notti="Nächte",
            adulti="Erwachsene", bambini="Kinder", etaBreve="Alter", mAnimale="Wir reisen mit einem Haustier.", mGrazie="Vielen Dank!",
            mOggetto="Verfügbarkeit Ca’ Hygge"),
)

T["fr"] = dict(
    locale="fr_FR",
    title="Ca' Hygge · Appartement de vacances à Lavagna, près de la mer",
    desc="Ca' Hygge est un appartement lumineux à Lavagna, sur la Riviera italienne, à 10 minutes à pied des centres de Lavagna et de Chiavari. Trois chambres, WiFi, Netflix et Prime Video, lave-linge, animaux acceptés.",
    og_desc="Un appartement lumineux à deux pas de la mer, où détente et beauté se rencontrent.",
    salta="Aller au contenu", menu="Menu", lingua="Langue",
    nav=["La maison", "Les pièces", "Alentours", "Hôtes", "Réserver"],
    hero_alt="Le salon lumineux de Ca' Hygge avec son parquet et son escalier blanc",
    benvenuti="bienvenue à la maison",
    h1="Ca' Hygge, votre maison à Lavagna",
    lead="Un appartement lumineux à deux pas de la mer, où détente et beauté se rencontrent.",
    vantaggio="Nos meilleurs tarifs, vous ne les trouverez qu'en réservant ici, directement avec nous.",
    cta_disp="Demander les disponibilités", cta_stanze="Voir les pièces",
    voto="9,5", eccezionale="Exceptionnel", su_booking="sur Booking.com · 55 avis",
    tramonto="Ce soir à Lavagna, le soleil se couche à", tramonto_nota="juste le temps d'arriver à la plage",
    casa_alt="La table ronde aux chaises blanches près de la cuisine", nota_caffe="le café est prêt",
    occh_hygge="pourquoi « hygge » ?", h2_casa="Une maison à la mer qui sent bon la maison", parola_danese="mot danois",
    diz="le sentiment de chaleur et de bien-être que procurent les choses simples : une couverture, une lumière douce, le temps passé ensemble.",
    casa_p="C'est ce que nous voulions pour Ca' Hygge : un endroit où poser ses valises et se sentir tout de suite bien. Trois chambres, un salon lumineux, une vraie cuisine pour cuisiner, et la mer tout près.",
    piccole=["Indications et conseils laissés aussi par écrit", "Plantes, lumière naturelle et parquet chaleureux", "Jeux de société pour les soirées", "Votre chien est le bienvenu aussi"],
    occh_stanze="faites le tour", h2_stanze="Les pièces", tabs_label="Pièces de la maison", mostra="Afficher",
    stanze=[
        ("Salon", "Le cœur de la maison : lumineux, avec son parquet chaleureux, le canapé et l'escalier blanc qui monte vers la mansarde. Le soir, Netflix et Prime Video à la télé, un jeu de société ou le programme de l'excursion du lendemain.",
         ["Le salon lumineux avec l'escalier vers la mansarde", "Le salon avec le canapé et la porte-fenêtre", "Le salon vu depuis l'entrée"], ["Canapé-lit"]),
        ("Cuisine et repas", "Une cuisine blanche et équipée, avec machine à café, bouilloire et micro-ondes, et une table ronde pour un petit-déjeuner tranquille avant de descendre à la plage.",
         ["La cuisine équipée avec des plantes sur l'étagère", "La table ronde près de la cuisine", "Le coin repas avec la table blanche", "La table à manger avec l'orchidée"], []),
        ("Chambre double", "Spacieuse et calme, avec deux fenêtres qui la remplissent de lumière. En plus du lit double, il y a un canapé-lit confortable.",
         ["La chambre double avec le lit en fer forgé", "La chambre double avec le canapé-lit", "La chambre double vue depuis la porte"], ["Lit double", "Canapé-lit"]),
        ("Mansarde", "Le refuge sous le toit en bois, avec son velux : la chambre préférée de ceux qui aiment faire la grasse matinée.",
         ["La mansarde avec plafond en bois et velux", "Le lit de la mansarde"], ["Lit double « à la française »"]),
        ("Petite chambre", "Petite et douillette, avec des tirages en noir et blanc aux murs : parfaite pour un enfant ou pour qui voyage seul.",
         ["La petite chambre avec le lit simple"], ["Lit simple"]),
        ("Salle de bain", "Avec douche et bidet. Serviettes, draps et produits d'accueil vous attendent, et il y a aussi un lave-linge dans l'appartement.",
         ["La salle de bain avec la douche", "Les produits d'accueil dans la salle de bain"], ["Produits d'accueil", "Serviettes et draps"]),
    ],
    posti=["chambres", "canapés-lits", "salle de bain avec douche", "balcon"],
    occh_dintorni="tout à portée de main", h2_dintorni="À pied depuis Ca' Hygge",
    dintorni_p="À 10 minutes à pied des centres de Lavagna et de Chiavari, et à un quart d'heure de la mer. Pour la voiture, il y a des parkings publics à proximité immédiate.",
    tappe=[("Ca' Hygge", "point de départ"), ("Arrêt de bus", "juste en bas"), ("Supermarché", "pour les courses"),
           ("Centre de Lavagna", ""), ("Centre de Chiavari", ""), ("Mer", ""), ("Gare", "")],
    bici_aria="Illustration d'un vélo avec un panier, devant la mer et le soleil",
    bici_occh="à vélo vers la mer", bici_h3="Location de vélos pour adultes",
    bici_p="Vous pouvez aussi vous déplacer à vélo : une location de vélos pour adultes est disponible, idéale pour aller à la plage, longer le front de mer ou rejoindre Chiavari sans souci de stationnement.",
    bici_nota="Demandez-les quand vous nous écrivez pour les disponibilités.",
    gite=["La Baia del Silenzio et la Baia delle Favole, à quelques minutes.", "Monterosso, Vernazza, Manarola : tout en train, sans souci de stationnement.",
          "Des maisons colorées face au petit port.", "En train jusqu'à Santa Margherita, puis bus ou bateau."],
    in_treno="En train depuis Lavagna",
    occh_voci="ce qu'ils en disent", h2_voci="Les mots de nos hôtes", recensioni="55 avis sur Booking.com",
    voci=["Une maison soignée dans les moindres détails… Équipée de tout ce qu'il faut dans chaque pièce.",
          "L'emplacement, la décoration, tout le nécessaire pour vivre l'appartement.",
          "Spacieux, accueillant et moderne. Nous nous y sommes vraiment sentis bien."],
    voce_cap="Hôte sur Booking.com · traduit de l'italien",
    h3_servizi="Ce que nous offrons",
    servizi=["Parkings publics tout près", "WiFi gratuit", "Netflix et Prime Video", "Lave-linge", "Micro-ondes", "Bouilloire",
             "Machine à café", "Animaux acceptés", "Balcon", "Draps et serviettes", "Jeux de société", "Location de vélos pour adultes", "Gare à 15 minutes", "Détecteur de fumée", "Détecteur de monoxyde de carbone"],
    occh_stampe="un souvenir à rapporter",
    stampe_p="Une série d'impressions numériques inspirées des couleurs, de la lumière et de l'atmosphère de la Riviera : le port, le coucher de soleil, les voiles, la carte illustrée de Lavagna. Un fragment authentique de Lavagna à accrocher chez vous.",
    stampe_btn="Demander les impressions", scrivete_a="Écrivez à", stampe_alt="Impression illustrée de Lavagna, collection Visioni di Riviera",
    stampe_oggetto="Impressions Visioni di Riviera",
    aspettiamo="à bientôt !", h2_prenota="Disponibilités et réservations",
    risparmio="En réservant directement ici, vous profitez toujours de nos meilleurs tarifs.",
    prenota_p="Pour savoir si vos dates sont libres et pour réserver, écrivez-nous directement : nous vous répondons nous-mêmes, sans intermédiaire.",
    arrivo="Arrivée", partenza="Départ", adulti="Adultes", bambini="Enfants", eta_titolo="Âge des enfants",
    cane="Nous voyageons avec un animal", invia="Demander les disponibilités", oppure="Ou écrivez-nous à",
    piede="Appartement de vacances à Lavagna (Gênes, Italie)",
    js=dict(scegli="Choisir", meno1="moins d'1 an", anno="an", anni="ans", bambino="Enfant",
            errDate="Indiquez vos dates d'arrivée et de départ.", errOrdine="Le départ doit être après l’arrivée.",
            errEta="Indiquez l’âge de chaque enfant.", ok="Votre messagerie s’ouvre avec le message prêt : il suffit d’appuyer sur envoyer.",
            mIntro="Bonjour ! Nous aimerions savoir si Ca’ Hygge est disponible :", arrivo="Arrivée", partenza="Départ", notte="nuit", notti="nuits",
            adulti="Adultes", bambini="Enfants", etaBreve="âges", mAnimale="Nous voyageons avec un animal.", mGrazie="Merci !",
            mOggetto="Disponibilités Ca’ Hygge"),
)

T["es"] = dict(
    locale="es_ES",
    title="Ca' Hygge · Apartamento vacacional en Lavagna, cerca del mar",
    desc="Ca' Hygge es un apartamento luminoso en Lavagna, en la Riviera italiana, a 10 minutos a pie de los centros de Lavagna y Chiavari. Tres dormitorios, WiFi, Netflix y Prime Video, lavadora, se admiten mascotas.",
    og_desc="Un apartamento luminoso a pocos pasos del mar, donde la calma y la belleza se encuentran.",
    salta="Ir al contenido", menu="Menú", lingua="Idioma",
    nav=["La casa", "Habitaciones", "Alrededores", "Huéspedes", "Reservar"],
    hero_alt="El luminoso salón de Ca' Hygge con suelo de parqué y escalera blanca",
    benvenuti="bienvenidos a casa",
    h1="Ca' Hygge, vuestra casa en Lavagna",
    lead="Un apartamento luminoso a pocos pasos del mar, donde la calma y la belleza se encuentran.",
    vantaggio="Las mejores tarifas solo las encontraréis reservando aquí, directamente con nosotros.",
    cta_disp="Consultar disponibilidad", cta_stanze="Ver las habitaciones",
    voto="9,5", eccezionale="Excepcional", su_booking="en Booking.com · 55 comentarios",
    tramonto="Esta tarde en Lavagna el sol se pone a las", tramonto_nota="justo a tiempo para llegar a la playa",
    casa_alt="La mesa redonda con sillas blancas junto a la cocina", nota_caffe="el café ya está listo",
    occh_hygge="¿por qué «hygge»?", h2_casa="Una casa en el mar que se siente como hogar", parola_danese="palabra danesa",
    diz="la sensación de calidez y bienestar que dan las cosas sencillas: una manta, una luz suave, el tiempo compartido.",
    casa_p="Eso es lo que quisimos que fuera Ca' Hygge: un lugar donde dejar las maletas y sentirse a gusto enseguida. Tres dormitorios, un salón luminoso, una cocina para cocinar de verdad y el mar muy cerca.",
    piccole=["Indicaciones y consejos también por escrito", "Plantas, luz natural y parqué cálido", "Juegos de mesa para las noches en casa", "Vuestro perro también es bienvenido"],
    occh_stanze="echad un vistazo", h2_stanze="Las habitaciones", tabs_label="Habitaciones de la casa", mostra="Mostrar",
    stanze=[
        ("Salón", "El corazón de la casa: luminoso, con parqué cálido, el sofá y la escalera blanca que sube a la buhardilla. Por la noche, Netflix y Prime Video en la tele, un juego de mesa o el plan de la excursión del día siguiente.",
         ["El salón luminoso con la escalera hacia la buhardilla", "El salón con el sofá y la puerta-ventana", "El salón visto desde la entrada"], ["Sofá cama"]),
        ("Cocina y comedor", "Una cocina blanca y equipada, con cafetera, hervidor y microondas, y una mesa redonda para desayunar con calma antes de bajar a la playa.",
         ["La cocina equipada con plantas en la repisa", "La mesa redonda junto a la cocina", "El comedor con la mesa blanca", "La mesa de comedor con la orquídea"], []),
        ("Dormitorio doble", "Amplio y tranquilo, con dos ventanas que lo llenan de luz. Además de la cama doble, hay un cómodo sofá cama.",
         ["El dormitorio doble con la cama de hierro forjado", "El dormitorio doble con el sofá cama", "El dormitorio doble visto desde la puerta"], ["Cama doble", "Sofá cama"]),
        ("Buhardilla", "El refugio bajo el techo de madera, con claraboya: la habitación favorita de quien quiere dormir un poco más.",
         ["La buhardilla con techo de madera y claraboya", "La cama de la buhardilla"], ["Cama doble pequeña"]),
        ("Habitación pequeña", "Pequeña y acogedora, con láminas en blanco y negro en las paredes: perfecta para un niño o para quien viaja solo.",
         ["La habitación pequeña con la cama individual"], ["Cama individual"]),
        ("Baño", "Con ducha y bidé. Toallas, ropa de cama y productos de cortesía os esperan, y en casa también hay lavadora.",
         ["El baño con la ducha", "Los productos de cortesía en el baño"], ["Productos de cortesía", "Toallas y ropa de cama"]),
    ],
    posti=["dormitorios", "sofás cama", "baño con ducha", "balcón"],
    occh_dintorni="todo al alcance", h2_dintorni="A pie desde Ca' Hygge",
    dintorni_p="A 10 minutos a pie de los centros de Lavagna y Chiavari, y a un cuarto de hora del mar. Para el coche hay aparcamientos públicos muy cerca.",
    tappe=[("Ca' Hygge", "punto de partida"), ("Parada de autobús", "justo abajo"), ("Supermercado", "para la compra"),
           ("Centro de Lavagna", ""), ("Centro de Chiavari", ""), ("Mar", ""), ("Estación", "")],
    bici_aria="Ilustración de una bicicleta con cesta, delante del mar y el sol",
    bici_occh="pedaleando hacia el mar", bici_h3="Alquiler de bicicletas para adultos",
    bici_p="También podéis moveros en bicicleta: hay alquiler de bicis para adultos, perfecto para llegar a la playa, pasear por el paseo marítimo o ir a Chiavari sin preocuparos por aparcar.",
    bici_nota="Pedídnoslas cuando nos escribáis para la disponibilidad.",
    gite=["La Baia del Silenzio y la Baia delle Favole, a pocos minutos.", "Monterosso, Vernazza, Manarola: todo en tren, sin preocuparse por aparcar.",
          "Casas de colores asomadas al pequeño puerto.", "En tren hasta Santa Margherita, luego autobús o barco."],
    in_treno="En tren desde Lavagna",
    occh_voci="lo que dicen", h2_voci="Las palabras de nuestros huéspedes", recensioni="55 comentarios en Booking.com",
    voci=["Casa cuidada hasta el último detalle… Equipada con todo lo necesario en cada habitación.",
          "Ubicación, decoración, todo lo necesario para vivir el apartamento.",
          "Amplio, acogedor y moderno. Nos sentimos realmente a gusto."],
    voce_cap="Huésped en Booking.com · traducido del italiano",
    h3_servizi="Qué ofrecemos",
    servizi=["Aparcamientos públicos muy cerca", "WiFi gratis", "Netflix y Prime Video", "Lavadora", "Microondas", "Hervidor",
             "Cafetera", "Se admiten mascotas", "Balcón", "Ropa de cama y toallas", "Juegos de mesa", "Alquiler de bicis para adultos", "Estación a 15 minutos", "Detector de humo", "Detector de monóxido de carbono"],
    occh_stampe="un recuerdo para llevar a casa",
    stampe_p="Una serie de láminas digitales inspiradas en los colores, la luz y el ambiente de la Riviera: el puerto, el atardecer, las velas, el mapa ilustrado de Lavagna. Un pedacito auténtico de Lavagna para colgar en casa.",
    stampe_btn="Pedir las láminas", scrivete_a="Escribid a", stampe_alt="Lámina ilustrada de Lavagna, colección Visioni di Riviera",
    stampe_oggetto="Láminas Visioni di Riviera",
    aspettiamo="¡os esperamos!", h2_prenota="Disponibilidad y reservas",
    risparmio="Reservando directamente aquí siempre tenéis las mejores tarifas.",
    prenota_p="Para saber si vuestras fechas están libres y para reservar, escribidnos directamente: os respondemos nosotros, sin intermediarios.",
    arrivo="Llegada", partenza="Salida", adulti="Adultos", bambini="Niños", eta_titolo="Edad de los niños",
    cane="Viajamos con una mascota", invia="Consultar disponibilidad", oppure="O escribidnos a",
    piede="Apartamento vacacional en Lavagna (Génova, Italia)",
    js=dict(scegli="Elegir", meno1="menos de 1 año", anno="año", anni="años", bambino="Niño",
            errDate="Indicad las fechas de llegada y salida.", errOrdine="La salida debe ser posterior a la llegada.",
            errEta="Indicad la edad de cada niño.", ok="Se abre vuestra app de correo con el mensaje listo: solo hay que pulsar enviar.",
            mIntro="¡Hola! Queremos saber si Ca’ Hygge está disponible:", arrivo="Llegada", partenza="Salida", notte="noche", notti="noches",
            adulti="Adultos", bambini="Niños", etaBreve="edades", mAnimale="Viajamos con una mascota.", mGrazie="¡Gracias!",
            mOggetto="Disponibilidad Ca’ Hygge"),
)

GITE_NOMI = ["Sestri Levante", "Cinque Terre", "Camogli", "Portofino"]
MINUTI = ["0'", "1'", "3'", "10'", "10'", "15'", "15'"]

DOMINIO = "https://cahyggelavagna.com"
BICI_SVG = '''<svg class="bici-disegno" viewBox="0 0 420 300" role="img" aria-label="{aria}">
        <circle cx="318" cy="92" r="46" fill="#f0b08c" opacity=".9"/>
        <path d="M0 170c40-14 80-14 120 0s80 14 120 0 80-14 120 0 40 10 60 4v126H0z" fill="#8cc3c8"/>
        <path d="M0 196c40-12 80-12 120 0s80 12 120 0 80-12 120 0 40 8 60 4v100H0z" fill="#d7ecee"/>
        <path d="M0 228h420v72H0z" fill="#ede2d1"/>
        <path d="M44 58q14-10 28 0M70 44q10-8 20 0" fill="none" stroke="#1f4b57" stroke-width="3" stroke-linecap="round"/>
        <g fill="none" stroke="#1f4b57" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="128" cy="226" r="46"/><circle cx="296" cy="226" r="46"/>
          <path d="M128 226l46-82h82l40 82M174 144l42 82h-88M216 226l40-82"/>
          <path d="M160 128h34M248 112l8 32M240 112h24"/>
        </g>
        <g stroke="#c79c74" stroke-width="2" opacity=".8"><path d="M128 180v92M82 226h92M296 180v92M250 226h92"/></g>
        <circle cx="128" cy="226" r="6" fill="#1f4b57"/><circle cx="296" cy="226" r="6" fill="#1f4b57"/><circle cx="216" cy="226" r="9" fill="#c79c74"/>
        <path d="M262 110h56l-8 34h-40z" fill="#c79c74"/>
        <path d="M268 118h44M266 128h44" stroke="#f6efe4" stroke-width="3"/>
        <path d="M276 108c-4-14 4-24 14-22 0 10-6 18-14 22zM292 106c2-14 14-20 22-14-4 8-12 14-22 14z" fill="#74a57f"/>
        <circle cx="300" cy="98" r="6" fill="#f0b08c"/>
      </svg>'''


def percorso(lang):
    return "" if lang == "it" else f"{lang}/"


def stanza_html(i, chiave, foto, icone_letti, testo, t):
    nome, descr, alts, letti = testo
    mini = "".join(
        f'<button type="button" aria-pressed="{"true" if j == 0 else "false"}" data-src="{url(F[k], 1600)}" data-alt="{html.escape(a)}" aria-label="{t["mostra"]}: {html.escape(a)}">'
        f'<img src="{url(F[k], 200)}" alt="" loading="lazy"></button>'
        for j, (k, a) in enumerate(zip(foto, alts))) if len(foto) > 1 else ""
    let = "".join(f'<li>{ICONE[ic]}<span>{tx}</span></li>' for ic, tx in zip(icone_letti, letti))
    return f'''<div class="stanza" role="tabpanel" id="pannello-{chiave}" aria-labelledby="tab-{chiave}"{"" if i == 0 else " hidden"}>
      <div><div class="grande">{img(F[foto[0]], alts[0], "(max-width:860px) 92vw, 60vw", lazy=i > 0)}</div>
      {f'<div class="miniature">{mini}</div>' if mini else ''}</div>
      <div class="info"><h3>{nome}</h3><p>{descr}</p>{f'<ul class="letti">{let}</ul>' if let else ''}</div>
    </div>'''


def pagina(lang):
    t = T[lang]
    su = "" if lang == "it" else "../"
    tabs = "".join(f'<button type="button" role="tab" id="tab-{c}" aria-controls="pannello-{c}" aria-selected="{"true" if i == 0 else "false"}">{t["stanze"][i][0]}</button>'
                   for i, (c, _, _) in enumerate(FOTO_STANZE))
    pannelli = "".join(stanza_html(i, c, f, ic, t["stanze"][i], t) for i, (c, f, ic) in enumerate(FOTO_STANZE))
    tappe = "".join(f'<div class="tappa"><small>{n}</small><b>{m}</b><span>{d}</span></div>' for (n, d), m in zip(t["tappe"], MINUTI))
    gite = "".join(f'<div class="gita appare"><h3>{n}</h3><p>{d}</p><span class="treno">{t["in_treno"]}</span></div>' for n, d in zip(GITE_NOMI, t["gite"]))
    voci = "".join(f'<figure class="appare"><blockquote>{html.escape(v)}</blockquote><figcaption>{t["voce_cap"]}</figcaption></figure>' for v in t["voci"])
    servizi = "".join(f'<li>{ICONE[i]}<span>{tx}</span></li>' for i, tx in zip(ICONE_SERVIZI, t["servizi"]))
    piccole = "".join(f'<li>{ICONE[i]}<span>{tx}</span></li>' for i, tx in zip(ICONE_PICCOLE, t["piccole"]))
    lingue = "".join(
        f'<li><a href="{su}{percorso(l)}" hreflang="{l}" lang="{l}" data-lingua="{l}"{" aria-current=\"true\"" if l == lang else ""}>{NOMI_LINGUA[l]}</a></li>' for l in LINGUE)
    alternati = "".join(f'<link rel="alternate" hreflang="{l}" href="{DOMINIO}/{percorso(l)}">\n' for l in LINGUE) + \
        f'<link rel="alternate" hreflang="x-default" href="{DOMINIO}/">\n'
    # Alla prima visita, chi ha il browser in un'altra lingua viene portato alla sua versione
    redirect = '''<script>(function(){try{if(localStorage.getItem('ca-lingua'))return;var l=(navigator.languages&&navigator.languages[0]||navigator.language||'it').slice(0,2).toLowerCase();if(['en','de','fr','es'].indexOf(l)>-1){localStorage.setItem('ca-lingua',l);location.replace(l+'/');}}catch(e){}})();</script>\n''' if lang == "it" else ""
    import json
    js_t = json.dumps(t["js"], ensure_ascii=False)
    n = t["nav"]
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{redirect}<title>{html.escape(t["title"])}</title>
<meta name="description" content="{html.escape(t["desc"])}">
<link rel="canonical" href="{DOMINIO}/{percorso(lang)}">
{alternati}<meta property="og:title" content="{html.escape(t["title"])}">
<meta property="og:description" content="{html.escape(t["og_desc"])}">
<meta property="og:image" content="{url(F['soggiorno'], 1600)}">
<meta property="og:locale" content="{t["locale"]}">
<meta name="theme-color" content="#1f4b57">
<link rel="icon" href="{url(LOGO, 128)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://static.wixstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500&family=Karla:wght@400;500;600;700&family=Marcellus&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{su}css/stile.css?v=14">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"VacationRental","name":"Ca' Hygge","description":{json.dumps(t["og_desc"], ensure_ascii=False)},"image":"{url(F['soggiorno'], 1600)}","address":{{"@type":"PostalAddress","addressLocality":"Lavagna","addressRegion":"GE","addressCountry":"IT"}},"email":"{EMAIL}"}}</script>
</head>
<body>
<a class="salta" href="#casa">{t["salta"]}</a>
<header class="testata">
  <div class="wrap">
    <a class="logo" href="{su}{percorso(lang)}"><img src="{url(LOGO, 128)}" alt="" width="52" height="52"><b>CA' HYGGE</b></a>
    <nav aria-label="{t["menu"]}"><ul class="menu">
      <li><a href="#casa">{n[0]}</a></li><li><a href="#stanze">{n[1]}</a></li><li><a href="#dintorni">{n[2]}</a></li><li><a href="#ospiti">{n[3]}</a></li>
      <li class="lingue"><details><summary aria-label="{t["lingua"]}">{lang.upper()}</summary><ul>{lingue}</ul></details></li>
      <li><a class="btn pesca" href="#prenota">{n[4]}</a></li>
    </ul></nav>
  </div>
</header>

<main>
<section class="hero">
  {img(F['soggiorno'], t["hero_alt"], "100vw", lazy=False)}
  <div class="wrap">
    <div>
      <span class="mano">{t["benvenuti"]}</span>
      <h1>{t["h1"]}</h1>
      <p class="lead">{t["lead"]}</p>
      <p class="vantaggio">{t["vantaggio"]}</p>
      <div class="azioni"><a class="btn pesca" href="#prenota">{t["cta_disp"]}</a><a class="btn chiaro" href="#stanze">{t["cta_stanze"]}</a></div>
    </div>
    <aside class="cartellino" data-tramonto>
      <div class="voto"><b>{t["voto"]}</b><span>{t["eccezionale"]}<small>{t["su_booking"]}</small></span></div>
      <hr>
      <p class="tramonto" style="margin:0">{t["tramonto"]} <b data-ora>—</b>.<br><span class="mano" style="font-size:22px">{t["tramonto_nota"]}</span></p>
    </aside>
  </div>
</section>
<div class="corda" aria-hidden="true"></div>

<section class="band" id="casa">
  <div class="wrap hygge">
    <div class="foto appare">{img(F['pranzo_c'], t["casa_alt"], "(max-width:820px) 90vw, 45vw")}<span class="nota">{t["nota_caffe"]}</span></div>
    <div class="appare">
      <span class="occhiello">{t["occh_hygge"]}</span>
      <h2>{t["h2_casa"]}</h2>
      <p class="dizionario"><b>hygge</b> · <i>{t["parola_danese"]}</i><br>{t["diz"]}</p>
      <p>{t["casa_p"]}</p>
      <ul class="piccole-cose">{piccole}</ul>
    </div>
  </div>
</section>

<section class="band stanze" id="stanze">
  <div class="wrap">
    <span class="occhiello">{t["occh_stanze"]}</span>
    <h2>{t["h2_stanze"]}</h2>
    <div class="tabs" role="tablist" aria-label="{t["tabs_label"]}">{tabs}</div>
    {pannelli}
    <div class="posti">
      <div><b>3</b>{t["posti"][0]}</div><div><b>2</b>{t["posti"][1]}</div><div><b>1</b>{t["posti"][2]}</div><div><b>1</b>{t["posti"][3]}</div>
    </div>
  </div>
</section>

<section class="band passeggiata" id="dintorni">
  <div class="wrap">
    <div class="intro appare">
      <div><span class="occhiello">{t["occh_dintorni"]}</span><h2>{t["h2_dintorni"]}</h2></div>
      <p style="max-width:42ch;margin:0">{t["dintorni_p"]}</p>
    </div>
    <div class="percorso appare">{tappe}</div>
    <div class="in-bici appare">
      {BICI_SVG.format(aria=html.escape(t["bici_aria"]))}
      <div>
        <span class="occhiello">{t["bici_occh"]}</span>
        <h3>{t["bici_h3"]}</h3>
        <p>{t["bici_p"]}</p>
        <p class="nota-bici">{t["bici_nota"]}</p>
      </div>
    </div>
    <div class="gite">{gite}</div>
  </div>
</section>

<section class="band voci" id="ospiti">
  <div class="wrap">
    <div class="testa appare">
      <div><span class="occhiello">{t["occh_voci"]}</span><h2>{t["h2_voci"]}</h2></div>
      <div class="punteggio"><b>{t["voto"]}</b><div><strong>{t["eccezionale"]}</strong><br><span style="color:var(--grigio);font-size:15px">{t["recensioni"]}</span></div></div>
    </div>
    <div class="citazioni">{voci}</div>
    <h3 style="margin-top:64px">{t["h3_servizi"]}</h3>
    <ul class="servizi">{servizi}</ul>
  </div>
</section>

<section class="band prenota" id="prenota">
  {img(F['mansarda'], "", "100vw")}
  <div class="wrap">
    <span class="mano" style="color:var(--pesca);font-size:34px">{t["aspettiamo"]}</span>
    <h2>{t["h2_prenota"]}</h2>
    <p class="risparmio">{t["risparmio"]}</p>
    <p>{t["prenota_p"]}</p>
    <form class="richiesta" id="richiesta" novalidate>
      <div><label for="arrivo">{t["arrivo"]}</label><input type="date" id="arrivo" required></div>
      <div><label for="partenza">{t["partenza"]}</label><input type="date" id="partenza" required></div>
      <div><label for="adulti">{t["adulti"]}</label><select id="adulti">{''.join(f'<option{" selected" if k == 2 else ""}>{k}</option>' for k in range(1, 6))}</select></div>
      <div><label for="bambini">{t["bambini"]}</label><select id="bambini">{''.join(f'<option>{k}</option>' for k in range(0, 5))}</select></div>
      <div class="pieno eta" id="eta" hidden><p class="eta-titolo">{t["eta_titolo"]}</p><div class="eta-campi"></div></div>
      <div class="pieno"><label class="spunta"><input type="checkbox" id="cane"> {t["cane"]}</label></div>
      <div class="pieno"><button class="btn pesca" type="submit">{t["invia"]}</button>
      <p class="avviso" aria-live="polite"></p></div>
    </form>
    <p class="o-scrivi">{t["oppure"]} <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div>
</section>
</main>

<footer class="piede">
  <div class="wrap">
    <a class="logo" href="{su}{percorso(lang)}"><img src="{url(LOGO, 128)}" alt="" width="52" height="52"><b>CA' HYGGE</b></a>
    <span>{t["piede"]}</span>
    <span><a href="mailto:{EMAIL}">{EMAIL}</a></span>
  </div>
</footer>
<script>window.CA_T={js_t};</script>
<script src="{su}js/sole.js"></script>
<script src="{su}js/casa.js?v=14"></script>
</body>
</html>
'''


for l in LINGUE:
    cartella = os.path.join(OUT, percorso(l))
    os.makedirs(cartella, exist_ok=True)
    open(os.path.join(cartella, "index.html"), "w", encoding="utf-8").write(pagina(l))
print("ok")
