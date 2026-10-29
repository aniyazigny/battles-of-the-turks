"""data/sinirlar.json'u 1530'dan 1570'e uzatır: Kanûnî'nin Macaristan, Irak ve Kuzey Afrika fetihleri; Habsburglar.
Bir kez çalıştırılmak üzere yazıldı; tarihlerin çoğu yaklaşıktır."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
OLD, END = 1530, 1570
d["states"].update({
 "habsburg": {"tr": "Habsburglar", "en": "Habsburgs", "group": "diger", "color": "#b0a37f"},
 "ispanya": {"tr": "İspanya", "en": "Spain", "group": "diger", "color": "#b39a86"},
 "hafsi": {"tr": "Hafsîler", "en": "Hafsids", "group": "diger", "color": "#a9a58e"},
 "portekiz": {"tr": "Portekiz", "en": "Portugal", "group": "diger", "color": "#9ea4ad"},
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

O = "osmanli"
setspan("belgrad", 1427, [[1427, 1521, "macar"], [1521, END, O]])
setspan("rodos", 1309, [[1309, 1522, "latin"], [1522, END, O]])
setspan("buda", 1526, [[1526, 1541, "macar"], [1541, END, O]])
setspan("bagdat", 1508, [[1508, 1534, "safevi"], [1534, END, O]])
for cid in ("basra", "hille", "ahvaz"):
    setspan(cid, 1508, [[1508, 1546, "safevi"], [1546, END, O]])
setspan("tebriz", 1501, [[1501, END, "safevi"]])
for cid in ("ahlat", "malazgirt"):
    setspan(cid, 1501, [[1501, 1534, "safevi"], [1534, END, O]])
setspan("modon", 1500, [[1500, END, O]])

known = {c["id"] for c in d["cities"]}
nv = sum(1 for x in d["cities"] if x.get("void"))
NEW = [
 ("van", "Van", 38.50, 43.38, [[1000, 1501, "karakoyunlu"], [1501, 1548, "safevi"], [1548, END, O]]),
 ("viyana", "Viyana", 48.21, 16.37, [[1000, END, "habsburg"]]),
 ("pozsony", "Pozsony (Kuzey Macaristan)", 48.15, 17.11, [[1000, 1526, "macar"], [1526, END, "habsburg"]]),
 ("temesvar", "Temeşvar", 45.75, 21.23, [[1000, 1552, "macar"], [1552, END, O]]),
 ("estergon", "Estergon", 47.79, 18.74, [[1000, 1543, "macar"], [1543, END, O]]),
 ("sigetvar", "Sigetvar", 46.05, 17.80, [[1000, 1526, "macar"], [1526, 1566, "habsburg"], [1566, END, O]]),
 ("cezayir", "Cezayir", 36.75, 3.06, [[1000, 1516, "hafsi"], [1516, END, O]]),
 ("tunus", "Tunus", 36.80, 10.18, [[1000, 1534, "hafsi"], [1534, 1535, O], [1535, END, "hafsi"]]),
 ("trablusgarp", "Trablusgarp", 32.90, 13.18, [[1000, 1510, "hafsi"], [1510, 1530, "ispanya"], [1530, 1551, "latin"], [1551, END, O]]),
 ("malta", "Malta", 35.90, 14.51, [[1000, 1530, "ispanya"], [1530, END, "latin"]]),
]
for cid, tr, lat, lon, spans in NEW:
    if cid not in known:
        d["cities"].insert(len(d["cities"]) - nv, {"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": spans, "src": [], "yaklasik": True})
for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in d["states"], (c["id"], s); assert a < b, (c["id"], a, b)
d["meta"]["method"] += " 1530–1570 arasında Kanûnî'nin Macaristan, Irak ve Kuzey Afrika fetihleri ile Habsburglar eklendi."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(d["states"]), "devlet")
