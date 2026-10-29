"""data/sinirlar.json'u 1610'dan 1640'a uzatır: Bağdat 1624–1638 Safevî, Revan 1635–36, Ahıska.
Bir kez çalıştırılmak üzere yazıldı; tarihlerin çoğu yaklaşıktır."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
OLD, END = 1610, 1640
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
setspan("bagdat", 1534, [[1534, 1624, O], [1624, 1638, "safevi"], [1638, END, O]])
for cid in ("hille", "basra"):
    setspan(cid, 1546, [[1546, END, O]])
setspan("revan", 1604, [[1604, 1635, "safevi"], [1635, 1636, O], [1636, END, "safevi"]])

known = {c["id"] for c in d["cities"]}
nv = sum(1 for x in d["cities"] if x.get("void"))
NEW = [
 ("ahiska", "Ahıska", 41.64, 42.98, [[1000, 1578, "gurcistan"], [1578, 1625, O], [1625, 1635, "safevi"], [1635, END, O]]),
]
for cid, tr, lat, lon, spans in NEW:
    if cid not in known:
        d["cities"].insert(len(d["cities"]) - nv, {"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": spans, "src": [], "yaklasik": True})
for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in d["states"], (c["id"], s); assert a < b, (c["id"], a, b)
d["meta"]["method"] += " 1610–1640 arasında Bağdat (1624–1638 Safevî), Revan ve Ahıska değişiklikleri eklendi."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(d["states"]), "devlet")
