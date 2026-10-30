"""Harita: Mohaç yılı ve Kili noktası (kontrol turu, 2026-10-31). Bir kez çalıştırılmak üzere yazıldı. Yıllar genel tarih bilgisi, yaklaşık.
- Batı ve Kuzey Macaristan şehirleri (Pozsony, Sigetvar, Yanıkkale, Kanije, Eğri, Uyvar) 1526'dan Habsburg görünüyordu. Bu yüzden Mohaç
  (29 Ağustos 1526) Habsburg toprağına düşüyordu. Ferdinand'ın Macaristan'da fiilen hâkim olması 1527'dir (Budin'e giriş, Tokay). Varad ve
  Erdel'in Zápolya (Erdel) dilimi de 1527'ye çekildi; 1526 boyunca hepsi Macar krallığı.
- Kili noktası eklendi. Kili 1484 kaydı en yakın nokta olan İbrail'e (Eflak) düşüyordu; şehir Boğdan'ındı. Sıra: bozkır kavimleri, Altın Orda,
  Ceneviz ve Dobruca (yerel, c. 1360), Eflak (1403, Ankara yenilgisinden sonra; TDVİA Kili), Boğdan (1426), Osmanlı 1484–1812, Rusya (Bükreş Antlaşması), Boğdan 1856 (Paris Antlaşması), Romanya 1859, Rusya 1878
  (Berlin), Romanya 1918."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
st = d["states"]
by = {c.get("id"): c for c in d["cities"]}

for cid in ("pozsony", "sigetvar", "yanikkale", "kanije", "egri", "uyvar", "varad", "erdel"):
    sp = by[cid]["spans"]
    i = next(i for i, x in enumerate(sp) if x[1] == 1526)
    assert sp[i][2] == "macar" and sp[i + 1][0] == 1526, (cid, sp[i:i + 2])
    sp[i][1] = sp[i + 1][0] = 1527

assert "kili" not in by
END = max(x[1] for c in d["cities"] for x in c.get("spans", []))
seq = [(400, "hun"), (454, "onogur"), (568, "avar"), (680, "bulgar1"), (895, "pecenek"), (1060, "kipcak"), (1240, "altin-orda"), (1360, "yerel"), (1403, "eflak"),
       (1426, "bogdan"), (1484, "osmanli"), (1812, "rusya"), (1856, "bogdan"), (1859, "romanya"), (1878, "rusya"), (1918, "romanya")]
d["cities"].append({"id": "kili", "tr": "Kili", "lat": 45.43, "lon": 29.27,
                    "spans": [[a, seq[i + 1][0] if i + 1 < len(seq) else END, s] for i, (a, s) in enumerate(seq)], "src": ["kili"], "yaklasik": True})

for c in d["cities"]:
    sp = c.get("spans", [])
    for a, b2, s in sp:
        assert s in st, (c["id"], s); assert a < b2, (c["id"], a, b2)
    for x, y in zip(sp, sp[1:]):
        assert x[1] <= y[0], (c["id"], x, y)
d["meta"]["method"] += " Macaristan'da Habsburg ve Erdel dilimleri 1527'den başlatıldı (Mohaç 1526 Macar toprağında); Kili noktası eklendi."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("tamam")
