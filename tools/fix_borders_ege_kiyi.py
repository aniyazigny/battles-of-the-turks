"""Harita: Ege kıyısında adaların hücreleri karaya taşıyordu (kontrol turu, 2026-10-31). Bir kez çalıştırılmak üzere yazıldı.
Sınırlar en yakın şehir noktasına göre (Voronoi) çizildiği için Çeşme–Karaburun Sakız'a (Cenevizliler, 1566'ya kadar), Ayvalık–Edremit–
Bergama Midilli'ye (Gattilusio, 1462'ye kadar), Marmaris–Köyceğiz–Fethiye Rodos'a ve Datça Bodrum'a (şövalyeler, 1522'ye kadar) düşüyor,
bu kıyılar 1400'ler ve 1500'lerde Latin görünüyordu. Oysa Latinler yalnız adaları ve Bodrum kalesini tutuyordu; karşı kıyılar Karesi,
Aydın ve Menteşe beyliklerinin, sonra Osmanlı'nındı. Kara noktaları eklendi:
- Muğla, Datça, Marmaris, Meğri (Fethiye): Menteşe sırası, Milas ile aynı (TDVİA Muğla, Menteşeoğulları: Ahmed Gazi Bey "güneyde Makri ve
  Marmaris bölgesinde"; Muğla kazasına bağlı Dadya/Datça).
- Çeşme: Aydın sırası, İzmir ile aynı (TDVİA Aydınoğulları).
- Bergama: Bizans, 1302'den Karesioğulları, c. 1341'den Osmanlı (TDVİA Bergama); Edremit: Balıkesir ile aynı Karesi sırası.
- Eğriboz noktası Halkis boğazından adanın içine alındı (38.60, 23.70). Harita artık ada noktalarını ayrı çiziyor; boğazdaki nokta ana karaya
  sayılıyor ve Venedik'in 1470'e kadarki dilimi Beotya kıyısını boyuyordu."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
st = d["states"]
by = {c.get("id"): c for c in d["cities"]}
cp = lambda cid: [list(x) for x in by[cid]["spans"]]
assert by["milas"]["spans"][1] == [1261, 1390, "mentese"] and by["izmir"]["spans"][5] == [1317, 1390, "aydin"]
END = max(x[1] for c in d["cities"] for x in c.get("spans", []))
bal = cp("balikesir")
assert bal[1] == [1300, 1345, "karesi"], bal
new = [
    ("mugla", "Muğla", 37.21, 28.36, cp("milas"), ["mugla", "menteseogullari"]),
    ("datca", "Datça (Dadya)", 36.73, 27.69, cp("milas"), ["mugla", "menteseogullari"]),
    ("marmaris", "Marmaris", 36.85, 28.27, cp("milas"), ["menteseogullari"]),
    ("megri", "Meğri (Fethiye)", 36.62, 29.11, cp("milas"), ["menteseogullari"]),
    ("cesme", "Çeşme", 38.32, 26.30, cp("izmir"), ["aydinogullari"]),
    ("bergama", "Bergama", 39.12, 27.18, [[400, 1302, "bizans"], [1302, 1341, "karesi"], [1341, bal[2][1], "osmanli"]] + bal[3:], ["bergama"]),
    ("edremit", "Edremit", 39.59, 27.02, bal, ["karesiogullari"]),
]
e = by["egriboz"]
assert (e["lat"], e["lon"]) == (38.46, 23.6), e
e["lat"], e["lon"] = 38.60, 23.70
for cid, tr, lat, lon, spans, src in new:
    assert cid not in by, cid
    d["cities"].append({"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": spans, "src": src, "yaklasik": True})

for c in d["cities"]:
    sp = c.get("spans", [])
    for a, b2, s in sp:
        assert s in st, (c["id"], s); assert a < b2, (c["id"], a, b2)
    for x, y in zip(sp, sp[1:]):
        assert x[1] <= y[0], (c["id"], x, y)
d["meta"]["method"] += " Ege kıyısına kara noktaları eklendi (Muğla, Datça, Marmaris, Meğri, Çeşme, Bergama, Edremit); Sakız, Midilli, Rodos ve Bodrum hücreleri artık karşı kıyıyı kaplamıyor."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("tamam")
