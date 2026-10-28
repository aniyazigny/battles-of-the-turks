"""data/sinirlar.json'u 1410'dan 1490'a uzatır: Fetret sonrası Osmanlı birliği, Fâtih'in fetihleri, Akkoyunlular, Kırım.
Bir kez çalıştırılmak üzere yazıldı; tarihlerin çoğu yaklaşıktır."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
OLD, END = 1410, 1490
d["states"].update({
 "akkoyunlu": {"tr": "Akkoyunlular", "en": "Aq Qoyunlu", "group": "turk-diger", "color": "#bd8a63"},
 "kirim": {"tr": "Kırım Hanlığı", "en": "Crimean Khanate", "group": "turk-diger", "color": "#9b8c6f"},
 "dulkadir": {"tr": "Dulkadıroğulları", "en": "Dulkadirids", "group": "beylik", "color": "#cf6a9b"},
})
for c in d["cities"]:
    if c.get("void"): continue
    for s in c["spans"]:
        if s[1] == OLD: s[1] = END

def setspan(cid, tail_from, items, yk=True):
    """cid şehrinin tail_from yılından sonraki bütün kesitlerini items ile değiştirir."""
    c = next(x for x in d["cities"] if x.get("id") == cid)
    keep = []
    for a, b, s in c["spans"]:
        if a >= tail_from: continue
        keep.append([a, min(b, tail_from), s])
    c["spans"] = keep + [list(x) for x in items]
    if yk: c["yaklasik"] = True

O = "osmanli"
setspan("istanbul", 1453, [[1453, END, O]], False)
setspan("selanik", 1403, [[1403, 1423, "bizans"], [1423, 1430, "latin"], [1430, END, O]], False)
setspan("mora", 1460, [[1460, END, O]])
setspan("atina", 1458, [[1458, END, O]])
setspan("trabzon", 1461, [[1461, END, O]], False)
setspan("sinop", 1461, [[1461, END, O]])
setspan("kastamonu", 1461, [[1461, END, O]])
for cid in ("izmir", "manisa", "milas", "kutahya", "denizli", "antalya"):
    setspan(cid, 1425, [[1425, END, O]])
setspan("konya", 1468, [[1468, END, O]])
setspan("karaman", 1474, [[1474, END, O]])
setspan("alanya", 1471, [[1471, END, O]])
setspan("kayseri", 1402, [[1402, 1474, "karaman"], [1474, END, "dulkadir"]])
setspan("amasya", 1400, [[1400, 1402, "timur"], [1402, END, O]])
setspan("sivas", 1400, [[1400, 1408, "timur"], [1408, END, O]])
setspan("erzincan", 1400, [[1400, 1410, "timur"], [1410, 1468, "karakoyunlu"], [1468, END, "akkoyunlu"]])
setspan("erzurum", 1388, [[1388, 1468, "karakoyunlu"], [1468, END, "akkoyunlu"]])
for cid in ("tebriz", "bagdat", "musul", "hille", "basra", "ahvaz"):
    setspan(cid, 1410, [[1410, 1468, "karakoyunlu"], [1468, END, "akkoyunlu"]])
for cid in ("amid", "urfa", "mardin", "hasankeyf", "meyyafarikin", "harput", "ahlat", "malazgirt", "ani"):
    setspan(cid, 1410, [[1410, END, "akkoyunlu"]])
setspan("malatya", 1410, [[1410, END, "memluk"]])
setspan("tirnova", 1393, [[1393, END, O]], False)
setspan("uskup", 1392, [[1392, END, O]], False)
setspan("pristine", 1455, [[1455, END, O]])
setspan("nis", 1386, [[1386, END, O]])
setspan("belgrad", 1403, [[1403, 1427, "sirbistan"], [1427, END, "macar"]])
setspan("sarajevo", 1463, [[1463, END, O]])
setspan("avlonya", 1417, [[1417, END, O]])
setspan("gelibolu", 1376, [[1376, END, O]])

known = {c["id"] for c in d["cities"]}
NEW = [
 ("semendire", "Semendire (Sırbistan)", 44.66, 20.93, [[1000, 1180, "bizans"], [1180, 1459, "sirbistan"], [1459, END, O]], ["murad-ii", "mehmed-ii"]),
 ("kruya", "Akçahisar (Kruya)", 41.51, 19.79, [[1000, 1345, "bizans"], [1345, 1443, "sirbistan"], [1443, 1478, "latin"], [1478, END, O]], ["mehmed-ii", "iskender-bey"]),
 ("kefe", "Kefe (Kırım)", 45.03, 35.38, [[1000, 1240, "kipcak"], [1240, 1266, "altin-orda"], [1266, 1475, "latin"], [1475, END, O]], ["mehmed-ii"]),
 ("bahcesaray", "Kırım içleri", 44.75, 33.86, [[1000, 1240, "kipcak"], [1240, 1441, "altin-orda"], [1441, END, "kirim"]], []),
 ("egriboz", "Eğriboz", 38.46, 23.60, [[1000, 1205, "bizans"], [1205, 1470, "latin"], [1470, END, O]], ["mehmed-ii"]),
 ("rodos", "Rodos", 36.44, 28.22, [[1000, 1309, "bizans"], [1309, END, "latin"]], ["rodos"]),
]
for cid, tr, lat, lon, spans, src in NEW:
    assert cid not in known, cid
    d["cities"].insert(len(d["cities"]) - sum(1 for x in d["cities"] if x.get("void")),
                       {"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": spans, "src": src, "yaklasik": True})
for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in d["states"], (c["id"], s)
        assert a < b, (c["id"], a, b)
d["meta"]["method"] += " 1410–1490 arasında Osmanlı'nın yeniden birleşmesi, Fâtih'in fetihleri, Akkoyunlular ve Kırım eklendi."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(d["states"]), "devlet")
