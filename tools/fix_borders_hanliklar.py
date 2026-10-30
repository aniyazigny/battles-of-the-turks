"""Harita (Parti 22): Türkistan hanlıkları ve Rus istilâsı. Bir kez çalıştırılmak üzere yazıldı.
Dayanaklar (TDVİA): Hokand Hanlığı (1710–1876; Taşkent ve Çimkent 1808'de alındı, 1864–1865'te Rus), Akmescid 1853 (Yâkub Beg),
Mangıtlar ve Buhara (Mangıt hânedanı 1785 sonrası), Türkmenistan (Kızılsu Rus üssü 1869–1871, Göktepe 1881).
Akmescid'in Hokand'a geçiş yılı ve Türkmen dilimlerinin başlangıcı kaba tahmindir (yaklasik)."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
st = d["states"]
for k, (tr, en, g, col) in {
    "hokand": ("Hokand Hanlığı", "Khanate of Kokand", "turk-diger", "#b89868"),
    "buhara-mangit": ("Buhara Emirliği (Mangıtlar)", "Emirate of Bukhara", "turk-diger", "#c2a166"),
    "teke": ("Türkmen boyları (Teke)", "Turkmen tribes (Teke)", "turk-diger", "#a99a6c"),
}.items():
    st.setdefault(k, {"tr": tr, "en": en, "group": g, "color": col})
END = max(s[1] for c in d["cities"] for s in c.get("spans", []))
by = {c.get("id"): c for c in d["cities"]}
for cid, tr, lat, lon, spans, src in [
    ("hokand", "Hokand", 40.53, 70.94, [[1710, 1876, "hokand"], [1876, END, "rusya"]], ["hokand-hanligi", "hokand"]),
    ("taskent", "Taşkent", 41.31, 69.28, [[1808, 1865, "hokand"], [1865, END, "rusya"]], ["hokand-hanligi", "taskent"]),
    ("cimkent", "Çimkent", 42.32, 69.60, [[1808, 1864, "hokand"], [1864, END, "rusya"]], ["hokand-hanligi", "cimkent"]),
    ("akmescid", "Akmescid (Kızılorda)", 44.85, 65.51, [[1820, 1853, "hokand"], [1853, END, "rusya"]], ["yakub-beg"]),
    ("goktepe", "Göktepe", 38.16, 57.97, [[1800, 1881, "teke"], [1881, END, "rusya"]], ["turkmenistan"]),
    ("kizilsu", "Kızılsu (Krasnovodsk)", 40.02, 52.97, [[1800, 1869, "teke"], [1869, END, "rusya"]], ["turkmenistan"]),
]:
    assert cid not in by, cid
    d["cities"].append({"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": spans, "src": src, "yaklasik": True})
for cid, start, end in [("buhara", 1785, 1920), ("semerkant", 1785, 1868)]:
    c = by[cid]
    out = []
    for a, b, s in c["spans"]:
        if s == "ozbek" and a < end and b > start:
            if a < start: out.append([a, start, s])
            out.append([max(a, start), min(b, end), "buhara-mangit"])
            if b > end: out.append([end, b, s])
        else:
            out.append([a, b, s])
    c["spans"] = out
    c["src"] = sorted(set(c.get("src", []) + ["mangitlar", "buhara"]))

for c in d["cities"]:
    sp = c.get("spans", [])
    for a, b, s in sp:
        assert s in st, (c["id"], s); assert a < b, (c["id"], a, b)
    for x, y in zip(sp, sp[1:]):
        assert x[1] <= y[0], (c["id"], x, y)
d["meta"]["method"] += " Türkistan hanlıkları: Hokand, Taşkent, Çimkent, Akmescid, Göktepe ve Kızılsu noktaları; Buhara ve Semerkant 1785 sonrası Mangıt."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("tamam")
