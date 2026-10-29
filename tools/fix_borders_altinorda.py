"""Eksik turu: Altın Orda'nın dağılışı. 1502'den sonra hâlâ Altın Orda görünen yerleri Kazan, Astarhan, Nogay, Kırım,
Hîve ve Sibir hanlıkları ile Rusya, Lehistan-Litvanya ve Kalmuklara verir. Tarihler TDVİA hanlık maddelerinden; çoğu yaklaşıktır."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
END = max(b for c in d["cities"] if not c.get("void") for a, b, s in c["spans"])
d["states"].update({
 "kazan": {"tr": "Kazan Hanlığı", "en": "Khanate of Kazan", "group": "turk-diger", "color": "#a5915f"},
 "astarhan": {"tr": "Astarhan Hanlığı", "en": "Khanate of Astrakhan", "group": "turk-diger", "color": "#b09a72"},
 "nogay": {"tr": "Nogay Ordası", "en": "Nogai Horde", "group": "turk-diger", "color": "#a08a66"},
 "hive": {"tr": "Hîve Hanlığı", "en": "Khanate of Khiva", "group": "turk-diger", "color": "#bfa070"},
 "sibir": {"tr": "Sibir Hanlığı", "en": "Khanate of Sibir", "group": "turk-diger", "color": "#9c9070"},
 "kazak": {"tr": "Kazak Hanlığı", "en": "Kazakh Khanate", "group": "turk-diger", "color": "#b3a27a"},
 "rusya": {"tr": "Rusya (Moskova)", "en": "Russia (Muscovy)", "group": "diger", "color": "#a9aeb8"},
 "kalmuk": {"tr": "Kalmuklar", "en": "Kalmyks", "group": "diger", "color": "#b8ad9c"},
})

def setspan(cid, tail_from, items):
    c = next(x for x in d["cities"] if x.get("id") == cid)
    keep = [[a, min(b, tail_from), s] for a, b, s in c["spans"] if a < tail_from]
    c["spans"] = keep + [list(x) for x in items]
    c["yaklasik"] = True

setspan("idil", 1236, [[1236, 1437, "altin-orda"], [1437, 1552, "kazan"], [1552, END, "rusya"]])
setspan("desti-kipcak", 1237, [[1237, 1502, "altin-orda"], [1502, 1634, "nogay"], [1634, END, "kalmuk"]])
setspan("yengikent", 1237, [[1237, 1465, "altin-orda"], [1465, END, "kazak"]])
setspan("gurgenc", 1221, [[1221, 1370, "altin-orda"], [1370, 1505, "timur"], [1505, 1512, "ozbek"], [1512, END, "hive"]])
setspan("karadeniz-bozkiri", 1240, [[1240, 1441, "altin-orda"], [1441, END, "kirim"]])
setspan("kiev", 1240, [[1240, 1362, "altin-orda"], [1362, 1667, "lehistan"], [1667, END, "rusya"]])

known = {c["id"] for c in d["cities"]}
nv = sum(1 for x in d["cities"] if x.get("void"))
NEW = [
 ("astarhan", "Astarhan", 46.35, 48.05, [[1240, 1466, "altin-orda"], [1466, 1556, "astarhan"], [1556, END, "rusya"]], ["TDVIA:astarhan-hanligi"]),
 ("moskova", "Moskova", 55.75, 37.62, [[1240, 1480, "altin-orda"], [1480, END, "rusya"]], ["TDVIA:altin-orda-hanligi"]),
 ("sibir", "Sibir (İsker)", 58.20, 68.25, [[1240, 1490, "altin-orda"], [1490, 1582, "sibir"], [1582, END, "rusya"]], ["TDVIA:sibir-hanligi"]),
 ("saraycik", "Saraycık (Nogay)", 47.50, 51.70, [[1240, 1502, "altin-orda"], [1502, 1634, "nogay"], [1634, END, "kalmuk"]], ["TDVIA:nogaylar"]),
]
for cid, tr, lat, lon, spans, src in NEW:
    if cid not in known:
        d["cities"].insert(len(d["cities"]) - nv, {"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": spans, "src": src, "yaklasik": True})
for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in d["states"], (c["id"], s); assert a < b, (c["id"], a, b)
d["meta"]["method"] += " Eksik turu: Altın Orda 1502 sonrası Kazan (1437–1552), Astarhan (1466–1556), Nogay, Kırım, Hîve (1512–), Sibir (–1582), Kazak hanlıkları ile Rusya, Lehistan-Litvanya ve Kalmuklara bölündü."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(d["states"]), "devlet, END", END)
