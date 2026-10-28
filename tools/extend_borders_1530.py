"""data/sinirlar.json'u 1490'dan 1530'a uzatır: Safevîler, Yavuz'un doğu ve Memlük seferleri, Venedik'ten alınan Mora limanları.
Bir kez çalıştırılmak üzere yazıldı; tarihlerin çoğu yaklaşıktır."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
OLD, END = 1490, 1530
d["states"]["safevi"] = {"tr": "Safevîler", "en": "Safavids", "group": "diger", "color": "#9c8fb0"}
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
for cid in ("tebriz", "hemedan", "rey", "isfahan", "siraz", "kirman", "gence", "ani", "ahlat", "malazgirt", "erzurum"):
    setspan(cid, 1501, [[1501, END, "safevi"]])
setspan("bagdat", 1468, [[1468, 1508, "akkoyunlu"], [1508, END, "safevi"]])
for cid in ("basra", "hille", "ahvaz"):
    setspan(cid, 1468, [[1468, 1508, "akkoyunlu"], [1508, END, "safevi"]])
setspan("musul", 1468, [[1468, 1508, "akkoyunlu"], [1508, 1517, "safevi"], [1517, END, O]])
setspan("erzincan", 1468, [[1468, 1501, "akkoyunlu"], [1501, 1515, "safevi"], [1515, END, O]])
setspan("harput", 1468, [[1468, 1501, "akkoyunlu"], [1501, 1515, "safevi"], [1515, END, O]])
for cid in ("amid", "mardin", "hasankeyf", "meyyafarikin", "urfa"):
    setspan(cid, 1410, [[1410, 1501, "akkoyunlu"], [1501, 1516, "safevi"], [1516, END, O]])
setspan("kayseri", 1474, [[1474, 1515, "dulkadir"], [1515, END, O]])
for cid in ("malatya", "tarsus", "antakya", "halep", "dimask", "trablus", "sur", "kudus", "askalan"):
    setspan(cid, 1500, [[1500, 1516, "memluk"], [1516, END, O]])
for cid in ("kahire", "iskenderiye"):
    setspan(cid, 1500, [[1500, 1517, "memluk"], [1517, END, O]])
setspan("medine", 1517, [[1517, END, O]])

known = {c["id"] for c in d["cities"]}
nv = sum(1 for x in d["cities"] if x.get("void"))
for cid, tr, lat, lon, spans in [
    ("modon", "Modon ve Koron", 36.82, 21.80, [[1000, 1205, "bizans"], [1205, 1500, "latin"], [1500, END, O]]),
    ("maras", "Maraş (Dulkadır)", 37.58, 36.93, [[1000, 1100, "ermeni"], [1100, 1149, "hacli"], [1149, 1337, "anadolu-selcuklu"], [1337, 1522, "dulkadir"], [1522, END, O]]),
]:
    if cid not in known:
        d["cities"].insert(len(d["cities"]) - nv, {"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": spans, "src": [], "yaklasik": True})
for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in d["states"], (c["id"], s); assert a < b, (c["id"], a, b)
d["meta"]["method"] += " 1490–1530 arasında Safevîler, Yavuz'un doğu ve Memlük seferleri eklendi."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(d["states"]), "devlet")
