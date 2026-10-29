"""data/sinirlar.json'u 1570'ten 1610'a uzatır: Kıbrıs, Tunus, Kafkasya (1578–1603), Uzun Savaş.
Ayrıca 1507'den sonra hâlâ Timurlu görünen yerleri Şeybânî Özbekleri, Safevîler ve Bâbürlülere verir.
Bir kez çalıştırılmak üzere yazıldı; tarihlerin çoğu yaklaşıktır."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
OLD, END = 1570, 1610
d["states"].update({
 "ozbek": {"tr": "Şeybânî Özbekleri", "en": "Shaybanid Uzbeks", "group": "turk-diger", "color": "#c9a46b"},
 "babur": {"tr": "Bâbürlüler", "en": "Mughals", "group": "turk-diger", "color": "#b98a8a"},
})
for c in d["cities"]:
    if c.get("void"): continue
    for s in c["spans"]:
        if s[1] == OLD: s[1] = END

def setspan(cid, tail_from, items):
    c = next(x for x in d["cities"] if x.get("id") == cid)
    keep = [[a, min(b, tail_from), s] for a, b, s in c["spans"] if a < tail_from]
    c["spans"] = keep + [list(x) for x in items]
    c["yaklasik"] = True

def after_timur(cid, items):
    c = next(x for x in d["cities"] if x.get("id") == cid)
    start = next(a for a, b, s in c["spans"] if s == "timur" and b == END)
    setspan(cid, start, [[start, items[0][0], "timur"]] + items if items[0][0] > start else items)

for cid in ("buhara", "semerkant"):
    after_timur(cid, [[1500, END, "ozbek"]])
for cid in ("belh",):
    after_timur(cid, [[1507, END, "ozbek"]])
for cid in ("merv", "serahs", "nisabur", "herat", "zerenc", "curcan", "amul", "alamut"):
    after_timur(cid, [[1507, END, "safevi"]])
for cid in ("gazne", "bust", "firuzkuh"):
    after_timur(cid, [[1504, END, "babur"]])

O = "osmanli"
setspan("kibris", 1570, [[1570, END, O]])
setspan("tunus", 1535, [[1535, 1574, "hafsi"], [1574, END, O]])
setspan("tiflis", 1578, [[1578, 1603, O], [1603, END, "gurcistan"]])
setspan("semahi", 1538, [[1538, 1578, "safevi"], [1578, 1606, O], [1606, END, "safevi"]])
setspan("gence", 1588, [[1588, 1606, O], [1606, END, "safevi"]])
setspan("tebriz", 1585, [[1585, 1603, O], [1603, END, "safevi"]])
setspan("erzurum", 1514, [[1514, END, O]])
setspan("ani", 1514, [[1514, END, O]])
setspan("estergon", 1543, [[1543, 1595, O], [1595, 1605, "habsburg"], [1605, END, O]])

known = {c["id"] for c in d["cities"]}
nv = sum(1 for x in d["cities"] if x.get("void"))
NEW = [
 ("yanikkale", "Yanıkkale (Győr)", 47.69, 17.63, [[1000, 1526, "macar"], [1526, 1594, "habsburg"], [1594, 1598, O], [1598, END, "habsburg"]]),
 ("kanije", "Kanije", 46.46, 16.99, [[1000, 1526, "macar"], [1526, 1600, "habsburg"], [1600, END, O]]),
 ("egri", "Eğri", 47.90, 20.38, [[1000, 1526, "macar"], [1526, 1596, "habsburg"], [1596, END, O]]),
 ("revan", "Revan", 40.18, 44.51, [[1000, 1501, "karakoyunlu"], [1501, 1583, "safevi"], [1583, 1604, O], [1604, END, "safevi"]]),
]
for cid, tr, lat, lon, spans in NEW:
    if cid not in known:
        d["cities"].insert(len(d["cities"]) - nv, {"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": spans, "src": [], "yaklasik": True})
for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in d["states"], (c["id"], s); assert a < b, (c["id"], a, b)
d["meta"]["method"] += " 1570–1610 arasında Kıbrıs, Tunus, Kafkasya ve Uzun Savaş değişiklikleri; Timurlu bölgeleri 1500'lerden sonra Özbek, Safevî ve Bâbürlülere verildi."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(d["states"]), "devlet")
