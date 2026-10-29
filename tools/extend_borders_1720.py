"""data/sinirlar.json'u 1690'dan 1720'ye uzatır: Kutsal İttifak savaşları ve Karlofça (1699), Mora (1687–1715 Venedik),
Azak (1696–1711 Rusya), Belgrad ve Banat (1717–18 Habsburg). Bir kez çalıştırılmak üzere yazıldı; tarihlerin çoğu yaklaşıktır."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
OLD, END = 1690, 1720
for c in d["cities"]:
    if c.get("void"): continue
    for s in c["spans"]:
        if s[1] == OLD: s[1] = END

def setspan(cid, tail_from, items):
    c = next(x for x in d["cities"] if x.get("id") == cid)
    keep = [[a, min(b, tail_from), s] for a, b, s in c["spans"] if a < tail_from]
    c["spans"] = keep + [list(x) for x in items]
    c["yaklasik"] = True

O, H = "osmanli", "habsburg"
setspan("egri", 1596, [[1596, 1687, O], [1687, END, H]])
setspan("sigetvar", 1566, [[1566, 1689, O], [1689, END, H]])
setspan("kanije", 1600, [[1600, 1690, O], [1690, END, H]])
setspan("varad", 1660, [[1660, 1692, O], [1692, END, H]])
setspan("estergon", 1683, [[1683, END, H]])
setspan("temesvar", 1552, [[1552, 1716, O], [1716, END, H]])
setspan("belgrad", 1521, [[1521, 1688, O], [1688, 1690, H], [1690, 1717, O], [1717, END, H]])
setspan("kamanice", 1672, [[1672, 1699, O], [1699, END, "lehistan"]])
setspan("mora", 1460, [[1460, 1687, O], [1687, 1715, "venedik"], [1715, END, O]])
setspan("modon", 1500, [[1500, 1686, O], [1686, 1715, "venedik"], [1715, END, O]])

known = {c["id"] for c in d["cities"]}
nv = sum(1 for x in d["cities"] if x.get("void"))
NEW = [
 ("azak", "Azak", 47.11, 39.42, [[1475, 1637, O], [1637, 1642, "rusya"], [1642, 1696, O], [1696, 1711, "rusya"], [1711, END, O]]),
 ("erdel", "Erdel (Kolojvar)", 46.77, 23.60, [[1000, 1526, "macar"], [1526, 1690, "erdel"], [1690, END, H]]),
]
for cid, tr, lat, lon, spans in NEW:
    if cid not in known:
        d["cities"].insert(len(d["cities"]) - nv, {"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": spans, "src": [], "yaklasik": True})
for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in d["states"], (c["id"], s); assert a < b, (c["id"], a, b)
d["meta"]["method"] += " 1690–1720 arasında Karlofça kayıpları, Mora (1687–1715 Venedik), Azak, Belgrad ve Banat eklendi."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(d["states"]), "devlet")
