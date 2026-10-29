"""data/sinirlar.json'u 1780'den 1815'e uzatır. Bir kez çalıştırılmak üzere yazıldı; tarihler yaklaşıktır.
- Kırım 1774'te bağımsız, 1783'te Rusya'ya ilhak (Yaş Antlaşması maddesi); Özü 1788'de Rus eline geçti (Yaş ile bırakıldı).
- Yeni noktalar: Yaş (Boğdan voyvodalığı), Bender ve Özü. Besarabya 1812 Bükreş Antlaşması ile Rusya'ya (Akkirman ve Bucak Kalesi maddeleri).
- Belgrad 1789–1791 Habsburg (Belgrad maddesi); Belgrad ve Semendire 1806'dan sonra Sırp isyancıları (Alacahisar, Böğürdelen maddeleri).
- Mısır 1798–1801 Fransız işgali (Mısır maddesi). Tiflis 1801, Gence 1804 Rusya.
- İran: Zendler 1751–1794 (Zendler maddesi), ardından Kaçarlar (Kaçarlar maddesi); Horasan 1796'ya kadar Afşar; Herat 1750'den sonra Dürrânî.
- Gence (1804) ve Şirvan (1805) hanlıkları Rusya'ya; Lahsâ: Uyûnîler sonrası Arap kabileleri, Osmanlı 1547, Suûdîler 1796 (Lahsâ maddesi).
- Lehistan'ın paylaşılması: Lviv 1772 Habsburg, Kamaniçe 1793 Rusya; Venedik 1797'de Habsburg'a, 1805'te Fransa'ya."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
OLD, END = 1780, 1815
O, RU = "osmanli", "rusya"
st = d["states"]
st.setdefault("bogdan", {"tr": "Boğdan Voyvodalığı", "en": "Moldavia", "group": "diger", "color": "#b8a98c"})
st.setdefault("zend", {"tr": "Zendler", "en": "Zand dynasty", "group": "diger", "color": "#c9a98b"})
st.setdefault("kacar", {"tr": "Kaçarlar", "en": "Qajars", "group": "turk-diger", "color": "#b8956a"})
st.setdefault("hanliklar", {"tr": "Azerbaycan hanlıkları", "en": "Azerbaijani khanates", "group": "turk-diger", "color": "#c7b08a"})
st.setdefault("arap", {"tr": "Arap kabileleri ve emirlikleri", "en": "Arab tribes and emirates", "group": "diger", "color": "#d6c7a8"})
st.setdefault("suud", {"tr": "Dir‘iye Emirliği (Suûdîler)", "en": "Emirate of Diriyah", "group": "diger", "color": "#c2b48f"})
st.setdefault("durrani", {"tr": "Dürrânî Afganları", "en": "Durrani Afghans", "group": "diger", "color": "#bfae8f"})
for c in d["cities"]:
    if c.get("void"): continue
    for s in c.get("spans", []):
        if s[1] == OLD: s[1] = END


def city(cid):
    return next(x for x in d["cities"] if x.get("id") == cid)


def setspan(cid, tail_from, items):
    c = city(cid)
    keep = [[a, min(b, tail_from), s] for a, b, s in c["spans"] if a < tail_from]
    c["spans"] = keep + [list(x) for x in items]
    c["yaklasik"] = True


def add(cid, tr, lat, lon, spans, src):
    if not any(x.get("id") == cid for x in d["cities"]):
        d["cities"].append({"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": spans, "src": src, "yaklasik": True})


add("yas", "Yaş (Boğdan)", 47.16, 27.59, [[1000, 1240, "kipcak"], [1240, 1359, "altin-orda"], [1359, END, "bogdan"]], ["bogdan"])
add("bender", "Bender (Bucak)", 46.83, 29.48,
    [[1000, 1240, "kipcak"], [1240, 1359, "altin-orda"], [1359, 1538, "bogdan"], [1538, 1812, O], [1812, END, RU]], ["bender-kalesi", "bogdan"])
add("ozu", "Özü", 46.61, 31.54,
    [[1000, 1240, "kipcak"], [1240, 1441, "altin-orda"], [1441, 1492, "kirim"], [1492, 1737, O], [1737, 1739, RU], [1739, 1788, O], [1788, END, RU]],
    ["abdullah-pasa-muhsinzade", "cezayirli-gazi-hasan-pasa"])
# Kırım
setspan("bahcesaray", 1441, [[1441, 1783, "kirim"], [1783, END, RU]])
setspan("karadeniz-bozkiri", 1441, [[1441, 1783, "kirim"], [1783, END, RU]])
setspan("kefe", 1475, [[1475, 1774, O], [1774, 1783, "kirim"], [1783, END, RU]])
# Balkanlar
setspan("belgrad", 1739, [[1739, 1789, O], [1789, 1791, "habsburg"], [1791, 1806, O], [1806, END, "sirbistan"]])
setspan("semendire", 1459, [[1459, 1806, O], [1806, END, "sirbistan"]])
setspan("lviv", 1000, [[1000, 1772, "lehistan"], [1772, END, "habsburg"]])
setspan("kamanice", 1699, [[1699, 1793, "lehistan"], [1793, END, RU]])
if any(x.get("id") == "venedik" for x in d["cities"]):
    v = city("venedik")
    if v["spans"][-1][2] == "venedik":
        setspan("venedik", v["spans"][-1][0], [[v["spans"][-1][0], 1797, "venedik"], [1797, 1805, "habsburg"], [1805, END, "fransa"]])
# Mısır
for cid in ("kahire", "iskenderiye"):
    setspan(cid, 1517, [[1517, 1798, O], [1798, 1801, "fransa"], [1801, END, O]])
# Kafkasya
setspan("tiflis", 1747, [[1747, 1801, "gurcistan"], [1801, END, RU]])
# İran
for cid in ("rey", "alamut", "hemedan", "isfahan", "kirman", "siraz", "amul", "curcan", "tebriz", "revan", "gence"):
    setspan(cid, 1747, [[1747, 1751, "afsar"], [1751, 1794, "zend"], [1794, END, "kacar"]])
# Gence ve Şirvan: XVIII. yüzyıl ortasında yarı bağımsız hanlıklar; Gence 3 Ocak 1804'te Rus eline geçti (Gence maddesi)
setspan("gence", 1747, [[1747, 1804, "hanliklar"], [1804, END, RU]])
setspan("semahi", 1606, [[1606, 1736, "safevi"], [1736, 1747, "afsar"], [1747, 1805, "hanliklar"], [1805, END, RU]])
# Lahsâ (Lahsâ maddesi): Uyûnîler 1073'te kuruldu; Osmanlı 1547; Suûdîler 1796; Mehmed Ali'nin seferiyle yeniden Osmanlı 1818
setspan("ahsa", 1077, [[1077, 1253, "uyuni"], [1253, 1547, "arap"], [1547, 1796, O], [1796, 1815, "suud"]])
for cid in ("nisabur", "serahs"):
    setspan(cid, 1747, [[1747, 1796, "afsar"], [1796, END, "kacar"]])
setspan("merv", 1747, [[1747, 1785, "afsar"], [1785, END, "ozbek"]])
for cid in ("herat", "zerenc"):
    setspan(cid, 1747, [[1747, 1750, "afsar"], [1750, END, "durrani"]])

for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in st, (c["id"], s); assert a < b, (c["id"], a, b)
d["meta"]["method"] += " 1780–1812: Kırım 1783, Özü 1788, Besarabya 1812 Rusya; Belgrad ve Semendire 1806'dan sonra Sırp; Mısır 1798–1801 Fransa; İran'da Zend ve Kaçar dönemleri; Lehistan'ın paylaşılması."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(st), "devlet")
