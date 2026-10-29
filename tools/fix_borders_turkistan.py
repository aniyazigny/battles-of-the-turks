"""Harita eksiği (EKSIKLER §2, Türkistan hanlıkları): Rus ve Afgan ilerleyişi. Bir kez çalıştırılır.
- Semerkant 14 Mayıs 1868'de Ruslar'ca alındı (Semerkant maddesi).
- Buhara Emirliği Rus himayesinde 1920'ye kadar sürdü; Ağustos 1920'de Kızılordu şehri aldı (Buhara maddesi) → 1920 Rusya.
- Hîve Hanlığı 1873'te Rus himayesine girdi, 1920'de ortadan kalktı (Hîve Hanlığı maddesi) → 1920 Rusya.
- Merv bölgesi 1884'te Ruslar'ca ele geçirildi (Merv maddesi).
- Belh 1751'de Ahmed Şah Dürrânî'nin egemenliğine girdi, 1826'da Buhara'nın eline geçti, 1841'den sonra sürekli Afganların elinde kaldı (Belh maddesi)."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
END = max(s[1] for c in d["cities"] for s in c.get("spans", []))
by = {c.get("id"): c for c in d["cities"]}


def tail(cid, start, items):
    c = by[cid]
    keep = [[a, min(b, start), s] for a, b, s in c["spans"] if a < start]
    c["spans"] = keep + [list(x) for x in items]
    assert items[-1][1] == END
    c["yaklasik"] = True


tail("semerkant", 1868, [[1868, END, "rusya"]])
tail("buhara", 1920, [[1920, END, "rusya"]])
tail("gurgenc", 1920, [[1920, END, "rusya"]])
tail("merv", 1884, [[1884, END, "rusya"]])
tail("belh", 1751, [[1751, 1826, "durrani"], [1826, 1841, "ozbek"], [1841, END, "durrani"]])
for cid, s in (("semerkant", "semerkant"), ("buhara", "buhara"), ("gurgenc", "hive-hanligi"), ("merv", "merv"), ("belh", "belh")):
    by[cid]["src"] = sorted(set(by[cid].get("src", []) + [s]))
for c in d["cities"]:
    sp = c.get("spans", [])
    for x, y in zip(sp, sp[1:]):
        assert x[1] <= y[0], (c["id"], x, y)
d["meta"]["method"] += " Türkistan: Semerkant 1868, Merv 1884 Rusya; Buhara ve Hîve 1920'ye kadar hanlık; Belh 1751 Dürrânî, 1826–1841 Buhara, sonra Afgan."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("tamam")
