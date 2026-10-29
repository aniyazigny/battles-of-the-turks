"""data/sinirlar.json'u 1815'ten 1840'a uzatır. Bir kez çalıştırılmak üzere yazıldı; tarihler yaklaşıktır.
- Belgrad 1813'te geri alındı (Hurşid Ahmed Paşa maddesi); Semendire yöresi 1830'dan sonra özerk Sırbistan (Sırbistan maddesi).
- Yunanistan: Mora ve Modon 1828'de (İbrâhim Paşa'nın çekilmesi, Navarin'in Fransızlara teslimi), Atina ve Eğriboz 1833'te (Atina maddesi).
- Cezayir 1830'da Fransa (Cezayir maddesi).
- Mehmed Ali Paşa'nın Suriye'si: Konya'dan sonra Kütahya'ya kadar ilerleyen Mısır kuvvetleri Suriye'yi ve Adana'yı 1840'a kadar elde tuttu.
  Halep 1832–1840 Mehmed Ali'nin elinde (Halep maddesi); Girit 1830'dan sonra Mehmed Ali'ye bırakıldı (Girit maddesi).
- Kafkasya: Revan 1828 Rusya; Ahıska Edirne Antlaşması (1829) ile Rusya (Ahıska maddesi)."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
OLD, END = 1815, 1840
O, RU = "osmanli", "rusya"
st = d["states"]
st.setdefault("yunanistan", {"tr": "Yunanistan", "en": "Greece", "group": "diger", "color": "#9fb3c8"})
st.setdefault("kavalali", {"tr": "Mehmed Ali Paşa yönetimi (Mısır)", "en": "Muhammad Ali's Egypt", "group": "diger", "color": "#c8b07a"})
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


setspan("belgrad", 1806, [[1806, 1813, "sirbistan"], [1813, END, O]])
setspan("semendire", 1806, [[1806, 1813, "sirbistan"], [1813, 1830, O], [1830, END, "sirbistan"]])
for cid in ("mora", "modon"):
    setspan(cid, 1715, [[1715, 1828, O], [1828, END, "yunanistan"]])
for cid in ("atina", "egriboz"):
    last0 = city(cid)["spans"][-1][0]
    setspan(cid, last0, [[last0, 1833, O], [1833, END, "yunanistan"]])
setspan("cezayir", 1516, [[1516, 1830, O], [1830, END, "fransa"]])
for cid in ("dimask", "trablus", "sur", "kudus", "askalan", "antakya", "halep"):
    setspan(cid, 1516, [[1516, 1832, O], [1832, END, "kavalali"]])
setspan("tarsus", 1516, [[1516, 1833, O], [1833, END, "kavalali"]])
setspan("girit", 1645, [[1645, 1830, O], [1830, END, "kavalali"]])
last0 = city("revan")["spans"][-1][0]
setspan("revan", last0, [[last0, 1828, city("revan")["spans"][-1][2]], [1828, END, RU]])
setspan("ahiska", 1635, [[1635, 1829, O], [1829, END, RU]])

for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in st, (c["id"], s); assert a < b, (c["id"], a, b)
d["meta"]["method"] += " 1815–1840: Belgrad 1813; Sırbistan 1830; Yunanistan 1828–1833; Cezayir 1830 Fransa; Mehmed Ali'nin Suriye'si ve Girit; Revan ve Ahıska Rusya."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(st), "devlet")
