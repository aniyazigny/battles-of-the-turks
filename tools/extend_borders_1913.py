"""data/sinirlar.json'u 1880'den 1913'e uzatır. Bir kez çalıştırılmak üzere yazıldı; tarihler yaklaşıktır.
- Tunus 1881'de Fransız himayesine girdi (Tunus maddesi; Bardo Antlaşması).
- Mısır 1882'de İngiliz işgaline uğradı (Mısır, Urâbî Paşa maddeleri); hukuken Osmanlı'ya bağlı kaldı, haritada fiilî yöneten gösterilir.
- Doğu Rumeli (Filibe) 1885'te Bulgaristan'a katıldı (II. Abdülhamid maddesi).
- Girit 1898'den sonra Osmanlı bayrağının çekilmediği özerk yönetim (Girit maddesi).
- Trablusgarp 1911'de, Rodos 1912'de İtalya'ya geçti (Trablusgarp Savaşı, Rodos maddeleri)."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
OLD, END = 1880, 1913
O = "osmanli"
st = d["states"]
st.setdefault("italya", {"tr": "İtalya", "en": "Italy", "group": "diger", "color": "#b5c4a0"})
st.setdefault("girit-ozerk", {"tr": "Girit (özerk yönetim)", "en": "Cretan State", "group": "diger", "color": "#a9bccc"})
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


setspan("tunus", 1574, [[1574, 1881, O], [1881, END, "fransa"]])
for cid in ("kahire", "iskenderiye"):
    setspan(cid, 1801, [[1801, 1882, O], [1882, END, "ingiltere"]])
setspan("filibe", 1364, [[1364, 1885, O], [1885, END, "bulgaristan"]])
setspan("girit", 1840, [[1840, 1898, O], [1898, END, "girit-ozerk"]])
setspan("trablusgarp", 1551, [[1551, 1911, O], [1911, END, "italya"]])
setspan("rodos", 1522, [[1522, 1912, O], [1912, END, "italya"]])

for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in st, (c["id"], s); assert a < b, (c["id"], a, b)
d["meta"]["method"] += " 1880–1913: Tunus 1881 Fransa; Mısır 1882 İngiliz işgali; Doğu Rumeli 1885 Bulgaristan; Girit 1898 özerk; Trablusgarp 1911 ve Rodos 1912 İtalya."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(st), "devlet")
