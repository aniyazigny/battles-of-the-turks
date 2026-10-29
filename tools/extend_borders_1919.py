"""data/sinirlar.json'u 1914'ten 1919'a uzatır (Birinci Dünya Savaşı). Bir kez çalıştırılmak üzere yazıldı; tarihler yaklaşıktır.
- Basra 22 Kasım 1914'te, Bağdat 11 Mart 1917'de İngilizler'ce işgal edildi (Basra, Birinci Dünya Savaşı, Musul maddeleri); Hille Bağdat ile birlikte gösterilir.
- Gazze ve Kudüs 1917'de İngilizler'in eline geçti (Gazze, Kudüs maddeleri).
- Şam 1 Ekim 1918'de alındı, Faysal 3 Ekim'de şehre geldi; Halep 27 Ekim 1918'de önce Arap kuvvetlerince işgal edildi (Şam, Halep maddeleri) → Hâşimî (hicaz) rengi.
  Trablusşam ve Sur 1918'de İtilâf işgaline girdi (Birinci Dünya Savaşı maddesi: Suriye boşaltıldı).
- Mekke 1916'da Şerîf Hüseyin'in eline geçti (Mekke maddesi); Medine 1919'a kadar Osmanlı'da kaldı.
- Erzurum 16 Şubat 1916–12 Mart 1918, Trabzon 18 Nisan 1916–24 Şubat 1918 Rus işgalinde; Van 1915–2 Nisan 1918 (Erzurum, Trabzon, Van maddeleri).
- Kars (Ani noktası) 25 Nisan 1918'de geri alındı (Kâzım Karabekir maddesi).
- Gence ve Şamahı 1918'de Azerbaycan Cumhuriyeti'ne, Tiflis Gürcistan'a, Revan Ermenistan'a geçti (Azerbaycan, Kafkasya maddeleri)."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
OLD, END = 1914, 1919
O = "osmanli"
st = d["states"]
st.setdefault("azerbaycan", {"tr": "Azerbaycan Cumhuriyeti", "en": "Azerbaijan Democratic Republic", "group": "diger", "color": "#a9c2b0"})
st.setdefault("gurcistan-cum", {"tr": "Gürcistan Cumhuriyeti", "en": "Democratic Republic of Georgia", "group": "diger", "color": "#c0a77a"})
st.setdefault("ermenistan", {"tr": "Ermenistan Cumhuriyeti", "en": "First Republic of Armenia", "group": "diger", "color": "#b49a8a"})
for c in d["cities"]:
    if c.get("void"): continue
    for s in c.get("spans", []):
        if s[1] == OLD: s[1] = END


def city(cid):
    return next(x for x in d["cities"] if x.get("id") == cid)


def tail(cid, items):
    """Son dilimi (başlangıcı korunarak) verilen dilimlerle değiştirir."""
    c = city(cid)
    a, b, s = c["spans"][-1]
    assert b == END, (cid, c["spans"][-1])
    c["spans"] = c["spans"][:-1] + [[a, items[0][0], s]] + [list(x) for x in items]
    c["yaklasik"] = True


def add(cid, tr, lat, lon, spans, src):
    assert not any(x.get("id") == cid for x in d["cities"]), cid
    d["cities"].append({"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": spans, "src": src, "yaklasik": True})


tail("basra", [[1914, END, "ingiltere"]])
for cid in ("bagdat", "hille"):
    tail(cid, [[1917, END, "ingiltere"]])
for cid in ("kudus", "askalan"):
    tail(cid, [[1917, END, "ingiltere"]])
for cid in ("dimask", "halep"):
    tail(cid, [[1918, END, "hicaz"]])
for cid in ("trablus", "sur"):
    tail(cid, [[1918, END, "ingiltere"]])
tail("erzurum", [[1916, 1918, "rusya"], [1918, END, O]])
tail("trabzon", [[1916, 1918, "rusya"], [1918, END, O]])
tail("van", [[1915, 1918, "rusya"], [1918, END, O]])
tail("ani", [[1918, END, O]])
for cid in ("gence", "semahi"):
    tail(cid, [[1918, END, "azerbaycan"]])
tail("tiflis", [[1918, END, "gurcistan-cum"]])
tail("revan", [[1918, END, "ermenistan"]])
add("mekke", "Mekke", 21.42, 39.83, [[1517, 1916, O], [1916, END, "hicaz"]], ["mekke"])

for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in st, (c["id"], s); assert a < b, (c["id"], a, b)
d["meta"]["method"] += " 1914–1919: Birinci Dünya Savaşı — Basra 1914, Bağdat ve Kudüs 1917, Şam, Halep, Trablusşam 1918; Mekke 1916 Hâşimî; Erzurum, Trabzon, Van Rus işgali ve 1918'de geri alınış; Kafkas cumhuriyetleri 1918."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(st), "devlet")
