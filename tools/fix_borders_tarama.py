"""Harita: sistematik tarama düzeltmeleri (kontrol turu, 2026-10-30). Bir kez çalıştırılmak üzere yazıldı.
Tarama: her devletin haritadaki ilk/son yılı tarihî ömrüyle karşılaştırıldı; başlangıcı geç, sonu erken veya boşluklu şehirler listelendi.
Düzeltilenler (yıllar genel tarih bilgisi, yaklaşık):
- İlhanlılar 1335'te dağıldı; İran ve Horasan şehirleri 1370'e kadar İlhanlı görünüyordu. 1335 sonrası: Kertler (Herat, Gûr, Gazne,
  Büst, Serahs; 1381 Timur), Serbedârîler (Nîşâbur 1337–1381), Muzafferîler (İsfahan, Kirman, Şîrâz; 1387–1393 Timur), Celâyirliler
  (Hemedan, Gence), Çağatay (Merv, Belh), yerel hânedanlar (Sîstan, Cürcân, Âmül, Rey, Alamut). Erzurum 1335–1357 Eretnalılar.
- Karakoyunlular Van, Ahlat, Malazgirt, Revan ve Ani'de 1375'ten (Kara Mehmed); 1335–1375 ve Amid, Meyyâfârikīn, Urfa'da 1335–1393
  yerel beylikler.
- Lahor ve Multan 1206'dan sonra boştu: Delhi Sultanlığı 1206–1526, Bâbürlüler 1526–1752, Dürrânîler, Sihler, İngiltere 1849.
- Merv 1785–1884 Özbek görünüyordu: Buhara (Mangıt) 1785–1823, Hîve 1823–1856, Teke Türkmenleri 1856–1884.
- Kıpçaklar Karadeniz kuzeyine 1060 civarında geldi; 1000–1060 Peçenekler.
- Viyana 1000–1278 Habsburg değil Kutsal Roma-Germen İmparatorluğu (Babenberg Avusturyası); Hafsîler 1229'da kuruldu, öncesi Zîrîler
  ve Muvahhidler; Güney İtalya 1071'e kadar Bizans; Toledo 1085'e kadar Endülüs.
- Boş kalan erken dönemler dolduruldu: Macaristan şehirleri 895'ten Macar; Revan, Ahıska; Fergana, Taşkent, Çimkent, Akmescid,
  Göktepe, Kızılsu; Astarhan, Saraycık, Sibir, Azak, Moskova; Yanya, İşkodra, Midilli, Sakız, Mekke; Gûr, Alamut."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
st = d["states"]
for k, (tr, en, g, col) in {
    "yerel": ("Yerel hânedanlar", "Local dynasties", "diger", "#a8a39a"),
    "kart": ("Kertler (Herat)", "Kartids", "diger", "#9fa08a"),
    "serbedar": ("Serbedârîler", "Sarbadars", "diger", "#a49a8e"),
    "muzaffari": ("Muzafferîler", "Muzaffarids", "diger", "#b09a86"),
    "delhi": ("Delhi Sultanlığı", "Delhi Sultanate", "turk-diger", "#b5986a"),
    "sih": ("Sih Devleti", "Sikh Empire", "diger", "#c0a070"),
    "kutsal-roma": ("Kutsal Roma-Germen İmparatorluğu", "Holy Roman Empire", "diger", "#9a96ae"),
    "ziri": ("Zîrîler ve Hammâdîler", "Zirids and Hammadids", "diger", "#a9a088"),
    "muvahhid": ("Muvahhidler", "Almohads", "diger", "#a69c84"),
    "endulus": ("Endülüs", "al-Andalus", "diger", "#b2a07e"),
}.items():
    assert k not in st, k
    st[k] = {"tr": tr, "en": en, "group": g, "color": col}

END = max(s[1] for c in d["cities"] for s in c.get("spans", []))
by = {c.get("id"): c for c in d["cities"]}


def setrange(cid, a, b, seq):
    """[a, b) aralığını seq ile değiştirir: seq = [(başlangıç, devlet), ...], ilk başlangıç a olmalı; son dilim b'de biter."""
    assert seq[0][0] == a, (cid, seq)
    c = by[cid]
    out = []
    for x, y, s in c["spans"]:
        if y <= a or x >= b:
            out.append([x, y, s])
            continue
        if x < a: out.append([x, a, s])
        if y > b: out.append([b, y, s])
    for i, (x, s) in enumerate(seq):
        out.append([x, seq[i + 1][0] if i + 1 < len(seq) else b, s])
    c["spans"] = sorted(out)


def owner(cid, y):
    return next((s for a, b, s in by[cid]["spans"] if a <= y < b), None)


# İlhanlı sonrası (1335–1370)
for cid, seq in {
    "merv": [(1335, "cagatay")], "belh": [(1335, "cagatay")],
    "serahs": [(1335, "kart"), (1381, "timur")], "herat": [(1335, "kart"), (1381, "timur")],
    "gazne": [(1335, "kart"), (1381, "timur")], "bust": [(1335, "kart"), (1381, "timur")], "firuzkuh": [(1335, "kart"), (1381, "timur")],
    "nisabur": [(1335, "yerel"), (1337, "serbedar"), (1381, "timur")],
    "zerenc": [(1335, "yerel"), (1383, "timur")], "curcan": [(1335, "yerel"), (1384, "timur")],
    "amul": [(1335, "yerel"), (1392, "timur")], "rey": [(1335, "yerel"), (1384, "timur")], "alamut": [(1335, "yerel"), (1384, "timur")],
    "hemedan": [(1335, "celayir"), (1386, "timur")], "gence": [(1335, "celayir"), (1386, "timur")],
    "isfahan": [(1335, "muzaffari"), (1387, "timur")], "kirman": [(1335, "muzaffari"), (1393, "timur")],
    "siraz": [(1335, "muzaffari"), (1393, "timur")],
}.items():
    assert owner(cid, 1340) == "mogol", (cid, owner(cid, 1340))
    b = next(y for x, y, s in by[cid]["spans"] if s == "mogol" and x < 1340 < y)
    if seq[-1][1] == "timur":  # Timur'un geliş yılı sonraya kayar; mevcut Timur dilimi o yıldan başlar
        assert owner(cid, b) == "timur", cid
        b, seq = seq[-1][0], seq[:-1]
    setrange(cid, 1335, b, seq)
assert owner("erzurum", 1340) == "mogol"
setrange("erzurum", 1335, 1357, [(1335, "eretna")])
# Karakoyunlular 1375'ten
for cid in ("van", "ahlat", "malazgirt", "revan", "ani"):
    assert owner(cid, 1340) == "karakoyunlu", cid
    setrange(cid, 1335, 1375, [(1335, "yerel")])
for cid in ("amid", "meyyafarikin", "urfa"):
    assert owner(cid, 1340) == "karakoyunlu", cid
    setrange(cid, 1335, 1393, [(1335, "yerel")])
# Lahor, Multan
for cid in ("lahor", "multan"):
    assert by[cid]["spans"][-1][1] == 1206, cid
setrange("lahor", 1206, END, [(1206, "delhi"), (1526, "babur"), (1752, "durrani"), (1799, "sih"), (1849, "ingiltere")])
setrange("multan", 1206, END, [(1206, "delhi"), (1526, "babur"), (1752, "durrani"), (1818, "sih"), (1849, "ingiltere")])
# Merv 1785–1884
assert owner("merv", 1800) == "ozbek"
setrange("merv", 1785, 1884, [(1785, "buhara-mangit"), (1823, "hive"), (1856, "teke")])
# Kıpçaklar 1060'tan
for cid in ("bukres", "kefe", "bahcesaray", "yas", "bender", "ozu"):
    assert owner(cid, 1010) == "kipcak", cid
    setrange(cid, 1000, 1060, [(1000, "pecenek")])
# Batı ve Kuzey Afrika
setrange("viyana", 1000, 1278, [(1000, "kutsal-roma")])
for cid in ("cezayir", "tunus", "trablusgarp"):
    assert owner(cid, 1010) == "hafsi", cid
    setrange(cid, 1000, 1229, [(1000, "ziri"), (1152, "muvahhid")])
setrange("napoli", 1000, 1071, [(1000, "bizans")])
setrange("madrid", 1000, 1085, [(1000, "endulus")])
# Boş kalan erken dönemler
for cid in ("pozsony", "estergon", "sigetvar", "yanikkale", "kanije", "egri", "temesvar", "varad", "erdel"):
    assert by[cid]["spans"][0][0] == 1000, cid
    setrange(cid, 895, 1000, [(895, "macar")])
setrange("revan", 550, 1000, [(550, "sasani"), (654, "emevi"), (750, "abbasi"), (885, "ermeni")])
setrange("ahiska", 550, 1000, [(550, "gurcistan")])
setrange("hokand", 552, 1710, [(552, "bati-gokturk"), (704, "turgis"), (766, "karluk"), (819, "samani"), (992, "karahanli"),
                               (1212, "harizmsah"), (1218, "cagatay"), (1370, "timur"), (1500, "ozbek")])
setrange("taskent", 552, 1808, [(552, "bati-gokturk"), (704, "turgis"), (751, "abbasi"), (819, "samani"), (992, "karahanli"),
                                (1212, "harizmsah"), (1218, "cagatay"), (1370, "timur"), (1500, "ozbek"), (1598, "kazak")])
setrange("cimkent", 552, 1808, [(552, "bati-gokturk"), (704, "turgis"), (766, "karluk"), (840, "karahanli"), (1212, "harizmsah"),
                                (1218, "cagatay"), (1370, "timur"), (1500, "ozbek"), (1598, "kazak")])
setrange("akmescid", 552, 1820, [(552, "bati-gokturk"), (766, "oguz"), (1050, "kipcak"), (1221, "altin-orda"), (1465, "kazak")])
setrange("goktepe", 550, 1800, [(550, "sasani"), (651, "emevi"), (750, "abbasi"), (900, "samani"), (999, "gazneli"), (1040, "buyuk-selcuklu"),
                                (1157, "harizmsah"), (1221, "mogol"), (1335, "yerel"), (1370, "timur"), (1507, "safevi"), (1736, "afsar"),
                                (1747, "teke")])
setrange("kizilsu", 550, 1800, [(550, "sasani"), (716, "emevi"), (750, "abbasi"), (900, "samani"), (1040, "buyuk-selcuklu"),
                                (1157, "harizmsah"), (1221, "mogol"), (1335, "yerel"), (1370, "timur"), (1512, "hive"), (1700, "teke")])
setrange("astarhan", 630, 1240, [(630, "hazar"), (965, "oguz"), (1050, "kipcak")])
setrange("saraycik", 750, 1240, [(750, "oguz"), (1050, "kipcak")])
setrange("sibir", 1050, 1240, [(1050, "kipcak")])
setrange("azak", 630, 1475, [(630, "hazar"), (965, "pecenek"), (1060, "kipcak"), (1240, "altin-orda")])
setrange("moskova", 1150, 1240, [(1150, "kiev")])
setrange("yanya", 550, 1430, [(550, "bizans"), (1348, "sirbistan")])
setrange("iskodra", 550, 1479, [(550, "bizans"), (1180, "sirbistan"), (1396, "venedik")])
setrange("midilli", 550, 1462, [(550, "bizans"), (1355, "latin")])
setrange("sakiz", 550, 1566, [(550, "bizans"), (1346, "latin")])
setrange("mekke", 550, 1517, [(550, "hicaz")])
setrange("firuzkuh", 870, 1000, [(870, "gurlu")])
setrange("alamut", 550, 1000, [(550, "sasani"), (651, "yerel"), (934, "buveyhi")])

for c in d["cities"]:
    sp = c.get("spans", [])
    for a, b, s in sp:
        assert s in st, (c["id"], s); assert a < b, (c["id"], a, b)
    for x, y in zip(sp, sp[1:]):
        assert x[1] <= y[0], (c["id"], x, y)
d["meta"]["method"] += " Sistematik tarama (2026-10-30): İlhanlı sonrası 1335–1370, Karakoyunlu başlangıcı, Lahor ve Multan 1206 sonrası, Merv, Kıpçak başlangıcı ve boş erken dönemler düzeltildi."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("tamam")
