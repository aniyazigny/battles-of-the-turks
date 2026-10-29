"""Harita eksiği (EKSIKLER §3): Doğu Türkistan ve Moğolistan 1218 sonrası tek renkti (Çağatay / Koço Uygurları / Moğol boyları).
Bir kez çalıştırılmak üzere yazıldı. Dayanaklar (TDVİA): Kâşgar, Turfan, Uygurlar, Yâkub Beg; Yedisu ve Moğolistan dilimleri kaba tahmindir.
- Kâşgar: Çağatay 1218–1347; Moğolistan (Doğu Çağatay) Hanlığı ve Duğlat emîrleri 1347–1514; Yarkent (Saîdiye) Hanlığı 1514–1678;
  Âfâk Hoca ve Cungar hâkimiyeti 1678–1759; Çin 1759–1865; Yâkub Beg 1865–1877; Çin 1877 sonrası.
- Koço/Turfan: Uygur 1209'da Cengiz'e bağlandı, 1368'e kadar Moğol idaresinde varlığını sürdürdü (Uygur rengi korunur); Hızır Hoca
  (1389–1399) Turfan'ı aldı → Moğolistan Hanlığı; Yarkent 1514–1678; Cungar 1678–1758; Çin 1758–1868; Yâkub Beg 1868–1877; Çin.
- Yedisu (Balasagun noktası): Çağatay 1218–1347; Moğolistan Hanlığı 1347–1514; Kazak 1514–1680; Cungar 1680–1758; Kazak 1758–1864; Rusya 1864 sonrası.
- Ötüken: Moğol boyları 1125–1206; Moğol İmparatorluğu ve Yuan 1206–1368; Moğol boyları 1368–1691; Çin 1691–1911; Moğolistan 1911 sonrası."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
st = d["states"]
for k, (tr, en, g, col) in {
    "mogolistan-han": ("Moğolistan Hanlığı (Doğu Çağatay)", "Moghulistan Khanate", "turk-diger", "#a8946e"),
    "yarkent": ("Yarkent (Saîdiye) Hanlığı", "Yarkent Khanate", "turk-diger", "#b39a72"),
    "cungar": ("Cungarlar", "Dzungar Khanate", "diger", "#9a9488"),
    "qing": ("Çin (Çing hânedanı)", "Qing China", "diger", "#c49a8a"),
    "yakub": ("Kâşgar Hanlığı (Yâkub Beg)", "Kashgaria (Yaqub Beg)", "turk-diger", "#ad8f63"),
    "mogol-imp": ("Moğol İmparatorluğu ve Yuan", "Mongol Empire and Yuan", "diger", "#8a8fa3"),
}.items():
    st.setdefault(k, {"tr": tr, "en": en, "group": g, "color": col})
END = max(s[1] for c in d["cities"] for s in c.get("spans", []))
by = {c.get("id"): c for c in d["cities"]}


def replace_from(cid, start, items):
    c = by[cid]
    keep = [[a, min(b, start), s] for a, b, s in c["spans"] if a < start]
    assert items[0][0] == start and items[-1][1] == END, cid
    c["spans"] = keep + [list(x) for x in items]
    c["yaklasik"] = True
    c["src"] = sorted(set(c.get("src", []) + ["kasgar", "turfan", "uygurlar", "yakub-beg"]))


replace_from("kasgar", 1218, [[1218, 1347, "cagatay"], [1347, 1514, "mogolistan-han"], [1514, 1678, "yarkent"], [1678, 1759, "cungar"],
                              [1759, 1865, "qing"], [1865, 1877, "yakub"], [1877, END, "qing"]])
replace_from("koco", 840, [[840, 1368, "uygur"], [1368, 1514, "mogolistan-han"], [1514, 1678, "yarkent"], [1678, 1758, "cungar"],
                           [1758, 1868, "qing"], [1868, 1877, "yakub"], [1877, END, "qing"]])
replace_from("balasagun", 1218, [[1218, 1347, "cagatay"], [1347, 1514, "mogolistan-han"], [1514, 1680, "kazak"], [1680, 1758, "cungar"],
                                 [1758, 1864, "kazak"], [1864, END, "rusya"]])
replace_from("otuken", 1125, [[1125, 1206, "mogolistan"], [1206, 1368, "mogol-imp"], [1368, 1691, "mogolistan"], [1691, 1911, "qing"],
                              [1911, END, "mogolistan"]])

for c in d["cities"]:
    sp = c.get("spans", [])
    for a, b, s in sp:
        assert s in st, (c["id"], s); assert a < b, (c["id"], a, b)
    for x, y in zip(sp, sp[1:]):
        assert x[1] <= y[0], (c["id"], x, y)
d["meta"]["method"] += " Doğu Türkistan ve Moğolistan 1218 sonrası: Moğolistan Hanlığı, Yarkent Hanlığı, Cungarlar, Çing, Yâkub Beg dilimleri."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("tamam")
