"""data/sinirlar.json'u 1720'den 1780'e uzatır: Belgrad 1739'da geri alındı, Temeşvar Habsburg'da kaldı, Azak 1736'dan sonra Rusya,
Kırım 1774'te bağımsız (Rus nüfuzu), Kafkasya ve İran sınırı (1724–1735 Osmanlı). Bir kez çalıştırılmak üzere yazıldı; tarihler yaklaşıktır."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
OLD, END = 1720, 1780
d["states"].setdefault("afsar", {"tr": "Afşarlar (Nâdir Şah)", "en": "Afsharids", "group": "turk-diger", "color": "#c4a27e"})
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
setspan("belgrad", 1717, [[1717, 1739, "habsburg"], [1739, END, O]])
setspan("azak", 1711, [[1711, 1736, O], [1736, END, "rusya"]])
setspan("bahcesaray", 1441, [[1441, 1774, "kirim"], [1774, END, "kirim"]])
for cid in ("tebriz", "gence", "revan", "tiflis"):
    c = next(x for x in d["cities"] if x.get("id") == cid)
    last = c["spans"][-1][2]
    setspan(cid, 1724, [[1724, 1735, O], [1735, 1736, "safevi"], [1736, 1747, "afsar"], [1747, END, last]])
for cid in ("rey", "isfahan", "hemedan", "kirman", "siraz", "merv", "serahs", "nisabur", "herat", "curcan", "amul", "alamut", "zerenc"):
    c = next(x for x in d["cities"] if x.get("id") == cid)
    if c["spans"][-1][2] == "safevi":
        setspan(cid, 1736, [[1736, 1747, "afsar"], [1747, END, "safevi"]])
for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in d["states"], (c["id"], s); assert a < b, (c["id"], a, b)
d["meta"]["method"] += " 1720–1780 arasında Belgrad (1739), Azak (1736), 1724–1735 Osmanlı Azerbaycanı ve Nâdir Şah'ın Afşar dönemi (1736–1747) eklendi."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(d["states"]), "devlet")
