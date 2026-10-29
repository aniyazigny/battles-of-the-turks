"""data/sinirlar.json'u 1913'ten 1914'e uzatır (Balkan Savaşları). Bir kez çalıştırılmak üzere yazıldı; tarihler yaklaşıktır.
- Selânik 26 Ekim 1912'de Yunanlılar'a bırakıldı (Selânik, Balkan Savaşı maddeleri).
- Üsküp, Priştine, Manastır 1912'de Sırp işgaline girdi; Bükreş Antlaşması (1913) ile Sırbistan'a verildi (Üsküp, Manastır, Priştine maddeleri).
- Arnavutluk 28 Kasım 1912'de istiklâlini ilân etti (Arnavutluk maddesi); İşkodra 1913'te Arnavutluk'a dahil edildi (İşkodra maddesi).
- Yanya 6 Mart 1913'te Yunan ordusunun eline geçti (Yanya maddesi).
- Midilli ve Sakız 1912 sonbaharında Yunanlılar'ca işgal edildi; Girit Londra (1913) ile Yunanistan'a geçti (Midilli, Sakız, Girit maddeleri).
- Edirne 26 Mart–21 Temmuz 1913 arasında Bulgar işgalinde kaldı; yıl çözünürlüğünde Osmanlı gösterilir."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
OLD, END = 1913, 1914
O = "osmanli"
st = d["states"]
st.setdefault("arnavutluk", {"tr": "Arnavutluk", "en": "Albania", "group": "diger", "color": "#c9a9a6"})
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


def add(cid, tr, lat, lon, spans, src):
    assert not any(x.get("id") == cid for x in d["cities"]), cid
    d["cities"].append({"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": spans, "src": src, "yaklasik": True})


setspan("selanik", 1430, [[1430, 1912, O], [1912, END, "yunanistan"]])
for cid in ("uskup", "manastir", "pristine"):
    a = city(cid)["spans"][-1][0]
    setspan(cid, a, [[a, 1912, O], [1912, END, "sirbistan"]])
for cid in ("avlonya", "kruya"):
    a = city(cid)["spans"][-1][0]
    setspan(cid, a, [[a, 1912, O], [1912, END, "arnavutluk"]])
setspan("girit", 1898, [[1898, 1913, "girit-ozerk"], [1913, END, "yunanistan"]])
add("yanya", "Yanya", 39.67, 20.85, [[1430, 1913, O], [1913, END, "yunanistan"]], ["yanya"])
add("iskodra", "İşkodra", 42.07, 19.51, [[1479, 1913, O], [1913, END, "arnavutluk"]], ["iskodra"])
add("midilli", "Midilli", 39.11, 26.55, [[1462, 1912, O], [1912, END, "yunanistan"]], ["midilli"])
add("sakiz", "Sakız", 38.37, 26.14, [[1566, 1912, O], [1912, END, "yunanistan"]], ["sakiz-adasi"])

for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in st, (c["id"], s); assert a < b, (c["id"], a, b)
d["meta"]["method"] += " 1913–1914: Balkan Savaşları — Selânik, Yanya, Midilli, Sakız, Girit Yunanistan; Üsküp, Manastır, Priştine Sırbistan; Avlonya, Kruya, İşkodra Arnavutluk."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(st), "devlet")
