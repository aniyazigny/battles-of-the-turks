"""data/sinirlar.json'u 1000'den geriye, 550'ye uzatır (Göktürk–Uygur partisi ve 893/990 Gazneli savaşları için).
Bir kez çalıştırılmak üzere yazıldı. Bu katman kabadır: büyük el değiştirmeler TDVİA maddelerine (Asya, Uygurlar, Tohâristan,
Talas Savaşı, Semerkant, Mâverâünnehir, Hazarlar, Sâsânîler, Kırgızlar, Turfan, Fergana) ve genel İslâm tarihi kronolojisine
dayanır; bütün yeni dilimler 'yaklasik' işaretlidir.
- Göktürk 552–630 ve 682–744; T'ang 630–682; Uygur Kağanlığı 744–840; Kırgızlar 840–924; Kıtaylar 924 sonrası (Ötüken).
- Batı Göktürk 552/557–659; Türgiş 704–766; Karluk 766–840; Karahanlı 840 sonrası (Yedisu).
- Soğd ve Tohâristan: Akhun –557, Batı Göktürk 557–659 (Tohâristan yabguları 705'e kadar), Emevî 705/712–750, Abbâsî 750–900, Sâmânî 900–999.
- İran ve Irak: Sâsânî –651, Emevî 651–750, Abbâsî 750–945, Büveyhî 935/945–1000; Taberistan Ziyârî 931 sonrası.
- Kafkasya ve Karadeniz bozkırı: Batı Göktürk 552–630, Hazar 630–965; Peçenek 889 sonrası; Volga Bulgar 922 sonrası.
- Suriye, Mısır, Hicaz: Bizans/Sâsânî –630'lar, Râşidîn 632–661, Emevî 661–750, Abbâsî 750–969, Fâtımî 969 sonrası; Halep Hamdânî 944 sonrası.
- Balkanlar: Bizans; Tuna Bulgar Devleti 681–1018 (Tırnova, Sofya, Üsküp, Niş, Belgrad, Eflak); Avarlar 568–796 ve Macarlar 895 sonrası (Budin)."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
st = d["states"]
NEW_STATES = {
    "gokturk": ("Göktürk Kağanlığı", "Göktürk Khaganate", "turk", "#3d6fb0"),
    "bati-gokturk": ("Batı Göktürk Kağanlığı", "Western Turkic Khaganate", "turk", "#5a86c2"),
    "turgis": ("Türgiş Kağanlığı", "Türgesh Khaganate", "turk", "#7a9cc9"),
    "karluk": ("Karluk Yabguluğu", "Karluk Yabghu", "turk", "#6d8fa8"),
    "uygur-kag": ("Uygur Kağanlığı", "Uyghur Khaganate", "turk", "#4f9a94"),
    "kirgiz": ("Kırgız Kağanlığı", "Yenisei Kyrgyz Khaganate", "turk-diger", "#8a9a6a"),
    "akhun": ("Akhunlar (Eftalitler)", "Hephthalites", "turk-diger", "#a58f6b"),
    "hazar": ("Hazar Kağanlığı", "Khazar Khaganate", "turk-diger", "#9b8a62"),
    "bulgar1": ("Tuna Bulgar Devleti", "First Bulgarian Empire", "turk-diger", "#a29a76"),
    "turk-sahi": ("Kâbil ve Zâbulistan Türk Şâhîleri", "Turk Shahis", "turk-diger", "#a88a6a"),
    "juan-juan": ("Juan-juanlar", "Rouran Khaganate", "diger", "#a4a4a4"),
    "sogd": ("Soğd şehir devletleri", "Sogdian city-states", "diger", "#b6aa8c"),
    "tang": ("Çin (T'ang)", "Tang China", "diger", "#c49a8a"),
    "kitan": ("Kıtaylar (Liao)", "Khitan Liao", "diger", "#a3a0b8"),
    "sasani": ("Sâsânîler", "Sasanian Empire", "diger", "#b59f7a"),
    "rasidun": ("Hulefâ-yi Râşidîn", "Rashidun Caliphate", "diger", "#7d9a72"),
    "emevi": ("Emevîler", "Umayyads", "diger", "#869e78"),
    "samani": ("Sâmânîler", "Samanids", "diger", "#9fae86"),
    "saffari": ("Saffârîler", "Saffarids", "diger", "#b1a07e"),
    "hamdani": ("Hamdânîler", "Hamdanids", "diger", "#a0aa8e"),
    "avar": ("Avar Kağanlığı", "Avar Khaganate", "diger", "#a89a86"),
    "mogolistan": ("Moğol boyları / Moğolistan", "Mongolian steppe", "diger", "#9a9fb0"),
}
for k, (tr, en, g, col) in NEW_STATES.items():
    st.setdefault(k, {"tr": tr, "en": en, "group": g, "color": col})

S, E, A, BZ = "sasani", "emevi", "abbasi", "bizans"
IRAN_E = [[550, 651, S], [651, 750, E], [750, 900, A], [900, 999, "samani"]]
PRE = {
    # Orta Asya
    "semerkant": [[550, 557, "akhun"], [557, 659, "bati-gokturk"], [659, 712, "sogd"], [712, 750, E], [750, 900, A], [900, 1000, "samani"]],
    "buhara": [[550, 557, "akhun"], [557, 659, "bati-gokturk"], [659, 709, "sogd"], [709, 750, E], [750, 900, A], [900, 1000, "samani"]],
    "belh": [[550, 557, "akhun"], [557, 705, "bati-gokturk"], [705, 750, E], [750, 900, A], [900, 1000, "samani"]],
    "merv": [[550, 651, S], [651, 750, E], [750, 900, A], [900, 1000, "samani"]],
    "serahs": [[550, 651, S], [651, 750, E], [750, 900, A], [900, 1000, "samani"]],
    "nisabur": [[550, 651, S], [651, 750, E], [750, 873, A], [873, 900, "saffari"], [900, 1000, "samani"]],
    "herat": [[550, 651, S], [651, 750, E], [750, 870, A], [870, 900, "saffari"], [900, 1000, "samani"]],
    "zerenc": [[550, 651, S], [651, 750, E], [750, 861, A], [861, 1000, "saffari"]],
    "bust": [[550, 870, "turk-sahi"], [870, 977, "saffari"], [977, 1000, "gazneli"]],
    "gazne": [[550, 870, "turk-sahi"], [870, 962, "saffari"], [962, 1000, "gazneli"]],
    "gurgenc": [[550, 712, S], [712, 750, E], [750, 900, A], [900, 1000, "samani"]],
    "yengikent": [[552, 659, "bati-gokturk"], [659, 750, "turgis"], [750, 1000, "oguz"]],
    "balasagun": [[552, 659, "bati-gokturk"], [659, 704, "tang"], [704, 766, "turgis"], [766, 840, "karluk"], [840, 1000, "karahanli"]],
    "kasgar": [[552, 659, "bati-gokturk"], [659, 790, "tang"], [790, 840, "karluk"], [840, 1000, "karahanli"]],
    "koco": [[552, 640, "gokturk"], [640, 790, "tang"], [790, 840, "uygur-kag"], [840, 1000, "uygur"]],
    # Bozkır ve Kafkasya
    "desti-kipcak": [[552, 630, "bati-gokturk"], [630, 965, "hazar"], [965, 1000, "oguz"]],
    "idil": [[552, 630, "bati-gokturk"], [630, 922, "hazar"], [922, 1000, "bulgar"]],
    "karadeniz-bozkiri": [[552, 630, "bati-gokturk"], [630, 889, "hazar"], [889, 1000, "pecenek"]],
    "kefe": [[550, 576, BZ], [576, 590, "bati-gokturk"], [590, 680, BZ], [680, 965, "hazar"], [965, 1000, "pecenek"]],
    "bahcesaray": [[550, 576, BZ], [576, 590, "bati-gokturk"], [590, 680, BZ], [680, 965, "hazar"], [965, 1000, "pecenek"]],
    "kiev": [[750, 882, "hazar"], [882, 1000, "kiev"]],
    "tiflis": [[550, 629, S], [629, 645, "bati-gokturk"], [645, 736, E], [736, 1000, "tiflis"]],
    "gence": [[550, 651, S], [651, 750, E], [750, 971, A], [971, 1000, "seddadi"]],
    "semahi": [[550, 651, S], [651, 750, E], [750, 861, A], [861, 1000, "sirvansah"]],
    "tebriz": [[550, 651, S], [651, 750, E], [750, 1000, A]],
    "ani": [[550, 640, S], [640, 750, E], [750, 885, A], [885, 1000, "ermeni"]],
    "kutais": [[550, 1000, "gurcistan"]],
    # İran ve Irak
    "curcan": [[550, 651, S], [651, 750, E], [750, 931, A], [931, 1000, "ziyari"]],
    "amul": [[550, 651, S], [651, 750, E], [750, 931, A], [931, 1000, "ziyari"]],
    "rey": [[550, 641, S], [641, 750, E], [750, 943, A], [943, 1000, "buveyhi"]],
    "hemedan": [[550, 642, S], [642, 750, E], [750, 945, A], [945, 1000, "buveyhi"]],
    "isfahan": [[550, 642, S], [642, 750, E], [750, 935, A], [935, 1000, "buveyhi"]],
    "kirman": [[550, 651, S], [651, 750, E], [750, 936, A], [936, 1000, "buveyhi"]],
    "siraz": [[550, 650, S], [650, 750, E], [750, 934, A], [934, 1000, "buveyhi"]],
    "ahvaz": [[550, 640, S], [640, 750, E], [750, 945, A], [945, 1000, "buveyhi"]],
    "basra": [[550, 636, S], [636, 661, "rasidun"], [661, 750, E], [750, 945, A], [945, 1000, "buveyhi"]],
    "bagdat": [[550, 637, S], [637, 661, "rasidun"], [661, 750, E], [750, 945, A], [945, 1000, "buveyhi"]],
    "hille": [[550, 637, S], [637, 661, "rasidun"], [661, 750, E], [750, 1000, A]],
    "musul": [[550, 637, S], [637, 661, "rasidun"], [661, 750, E], [750, 990, A], [990, 1000, "ukayli"]],
    # Yukarı Mezopotamya ve Anadolu'nun doğusu
    "amid": [[550, 639, BZ], [639, 661, "rasidun"], [661, 750, E], [750, 983, A], [983, 1000, "mervani"]],
    "meyyafarikin": [[550, 639, BZ], [639, 661, "rasidun"], [661, 750, E], [750, 983, A], [983, 1000, "mervani"]],
    "mardin": [[550, 639, BZ], [639, 661, "rasidun"], [661, 750, E], [750, 983, A], [983, 1000, "mervani"]],
    "hasankeyf": [[550, 639, BZ], [639, 661, "rasidun"], [661, 750, E], [750, 983, A], [983, 1000, "mervani"]],
    "ahlat": [[550, 654, S], [654, 750, E], [750, 983, A], [983, 1000, "mervani"]],
    "van": [[550, 654, S], [654, 750, E], [750, 908, A], [908, 1000, "ermeni"]],
    "malazgirt": [[550, 654, BZ], [654, 750, E], [750, 1000, A]],
    "erzurum": [[550, 653, BZ], [653, 750, E], [750, 949, A], [949, 1000, BZ]],
    "malatya": [[550, 656, BZ], [656, 750, E], [750, 934, A], [934, 1000, BZ]],
    "harput": [[550, 656, BZ], [656, 750, E], [750, 938, A], [938, 1000, BZ]],
    "erzincan": [[550, 1000, BZ]],
    "urfa": [[550, 639, BZ], [639, 661, "rasidun"], [661, 750, E], [750, 1000, A]],
    "maras": [[550, 637, BZ], [637, 661, "rasidun"], [661, 750, E], [750, 962, A], [962, 1000, BZ]],
    "tarsus": [[550, 665, BZ], [665, 750, E], [750, 965, A], [965, 1000, BZ]],
    "antakya": [[550, 638, BZ], [638, 661, "rasidun"], [661, 750, E], [750, 969, A], [969, 1000, BZ]],
    "halep": [[550, 637, BZ], [637, 661, "rasidun"], [661, 750, E], [750, 944, A], [944, 1000, "hamdani"]],
    # Suriye, Filistin, Mısır, Arabistan
    "dimask": [[550, 634, BZ], [634, 661, "rasidun"], [661, 750, E], [750, 970, A], [970, 1000, "fatimi"]],
    "trablus": [[550, 638, BZ], [638, 661, "rasidun"], [661, 750, E], [750, 970, A], [970, 1000, "fatimi"]],
    "sur": [[550, 638, BZ], [638, 661, "rasidun"], [661, 750, E], [750, 970, A], [970, 1000, "fatimi"]],
    "kudus": [[550, 637, BZ], [637, 661, "rasidun"], [661, 750, E], [750, 970, A], [970, 1000, "fatimi"]],
    "askalan": [[550, 640, BZ], [640, 661, "rasidun"], [661, 750, E], [750, 970, A], [970, 1000, "fatimi"]],
    "kahire": [[550, 641, BZ], [641, 661, "rasidun"], [661, 750, E], [750, 969, A], [969, 1000, "fatimi"]],
    "iskenderiye": [[550, 641, BZ], [641, 661, "rasidun"], [661, 750, E], [750, 969, A], [969, 1000, "fatimi"]],
    "medine": [[550, 632, "hicaz"], [632, 661, "rasidun"], [661, 750, E], [750, 965, A], [965, 1000, "hicaz"]],
    "ahsa": [[899, 1000, "karmati"]],
    # Balkanlar
    "tirnova": [[550, 681, BZ], [681, 971, "bulgar1"], [971, 1000, BZ]],
    "sofya": [[550, 809, BZ], [809, 1000, "bulgar1"]],
    "uskup": [[550, 850, BZ], [850, 1000, "bulgar1"]],
    "nis": [[550, 850, BZ], [850, 1000, "bulgar1"]],
    "belgrad": [[550, 568, BZ], [568, 796, "avar"], [796, 1000, "bulgar1"]],
    "bukres": [[550, 680, "avar"], [680, 895, "bulgar1"], [895, 1000, "pecenek"]],
    "buda": [[568, 796, "avar"], [895, 1000, "macar"]],
}
# Batı Anadolu, Balkanların güneyi ve adalar: 550–1000 Bizans
for cid in ("trabzon", "sivas", "amasya", "kayseri", "konya", "iznik", "izmir", "antalya", "istanbul", "edirne", "selanik", "atina",
            "kibris", "kastamonu", "ankara", "eskisehir", "bilecik", "kutahya", "denizli", "karaman", "sinop", "alanya", "bursa",
            "izmit", "balikesir", "manisa", "milas", "isparta", "gelibolu", "filibe", "manastir", "pristine", "sarajevo",
            "avlonya", "mora", "semendire", "kruya", "egriboz", "rodos", "girit", "modon"):
    PRE.setdefault(cid, [[550, 1000, BZ]])

by = {c.get("id"): c for c in d["cities"]}
for cid, spans in PRE.items():
    c = by[cid]
    assert c["spans"][0][0] == 1000, (cid, c["spans"][0])
    assert spans[-1][1] == 1000, cid
    c["spans"] = [list(x) for x in spans] + c["spans"]
    c["yaklasik"] = True

# Ötüken: yeni nokta, 1923'e kadar
END = max(s[1] for c in d["cities"] for s in c.get("spans", []))
d["cities"].append({"id": "otuken", "tr": "Ötüken", "lat": 47.43, "lon": 102.66, "yaklasik": True,
                    "src": ["asya", "uygurlar", "kirgizlar"],
                    "spans": [[550, 552, "juan-juan"], [552, 630, "gokturk"], [630, 682, "tang"], [682, 744, "gokturk"],
                              [744, 840, "uygur-kag"], [840, 924, "kirgiz"], [924, 1125, "kitan"], [1125, END, "mogolistan"]]})

for c in d["cities"]:
    sp = c.get("spans", [])
    for a, b, s in sp:
        assert s in st, (c["id"], s); assert a < b, (c["id"], a, b)
    for x, y in zip(sp, sp[1:]):
        assert x[1] <= y[0], (c["id"], x, y)
d["meta"]["method"] += " 550–1000 (kaba katman): Göktürk, Batı Göktürk, Türgiş, Karluk, Uygur, Kırgız, Hazar, Akhun, Sâsânî, Emevî, Abbâsî, Sâmânî, Saffârî, Büveyhî, Hamdânî, Fâtımî, Tuna Bulgar ve Bizans dilimleri; Ötüken noktası eklendi."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(st), "devlet")
