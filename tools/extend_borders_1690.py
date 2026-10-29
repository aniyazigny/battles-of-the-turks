"""data/sinirlar.json'u 1640'tan 1690'a uzatır: Girit (1645–1669), Erdel/Varad, Uyvar, Podolya (1672–1699), 1683 sonrası kayıplar.
Bir kez çalıştırılmak üzere yazıldı; tarihlerin çoğu yaklaşıktır."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
OLD, END = 1640, 1690
d["states"].setdefault("lehistan", {"tr": "Lehistan-Litvanya", "en": "Poland–Lithuania", "group": "diger", "color": "#b7a0a8"})
d["states"].setdefault("venedik", {"tr": "Venedik", "en": "Venice", "group": "diger", "color": "#9fb0a4"})
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
setspan("girit", 1205, [[1205, 1645, "venedik"], [1645, END, O]])
setspan("estergon", 1605, [[1605, 1683, O], [1683, END, "habsburg"]])
setspan("buda", 1541, [[1541, 1686, O], [1686, END, "habsburg"]])

known = {c["id"] for c in d["cities"]}
nv = sum(1 for x in d["cities"] if x.get("void"))
NEW = [
 ("uyvar", "Uyvar", 47.99, 18.16, [[1000, 1526, "macar"], [1526, 1663, "habsburg"], [1663, 1685, O], [1685, END, "habsburg"]]),
 ("varad", "Varad", 47.07, 21.93, [[1000, 1526, "macar"], [1526, 1660, "erdel"], [1660, END, O]]),
 ("kamanice", "Kamaniçe", 48.67, 26.57, [[1000, 1672, "lehistan"], [1672, END, O]]),
 ("lviv", "İlbav (Lviv)", 49.84, 24.03, [[1000, END, "lehistan"]]),
 ("varsova", "Varşova", 52.23, 21.01, [[1000, END, "lehistan"]]),
]
d["states"].setdefault("erdel", {"tr": "Erdel Prensliği", "en": "Transylvania", "group": "diger", "color": "#b5a596"})
for cid, tr, lat, lon, spans in NEW:
    if cid not in known:
        d["cities"].insert(len(d["cities"]) - nv, {"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": spans, "src": [], "yaklasik": True})
for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in d["states"], (c["id"], s); assert a < b, (c["id"], a, b)
d["meta"]["method"] += " 1640–1690 arasında Girit, Varad, Uyvar, Podolya, Lehistan ve 1683 sonrası Estergon ile Budin kayıpları eklendi."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(d["states"]), "devlet")
