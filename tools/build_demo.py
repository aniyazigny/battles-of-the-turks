"""Parti verilerini ve sınır tablosunu site/template.html içine gömüp site/index.html üretir (file:// ile açılabilsin diye)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
# (dosya, kimlik öneki) — yeni partiler buraya eklenir
BATCHES = [("pilot-buyuk-selcuklu.json", "bs"), ("anadolu-selcuklu.json", "as"), ("beylikler-atabeylikler.json", "ba"), ("gazneli-karahanli.json", "gk"), ("osmanli-kurulus.json", "ok"), ("osmanli-1402-1481.json", "o2"), ("osmanli-1481-1520.json", "o3"), ("osmanli-1520-1566.json", "o4"), ("osmanli-1566-1606.json", "o5"), ("osmanli-1603-1640.json", "o6"), ("osmanli-1640-1683.json", "o7"), ("osmanli-1683-1718.json", "o8"), ("osmanli-1718-1774.json", "o9"), ("osmanli-1774-1812.json", "o10"), ("osmanli-1812-1839.json", "o11"), ("osmanli-1839-1878.json", "o12"), ("osmanli-1878-1912.json", "o13"), ("osmanli-1912-1913.json", "o14"), ("osmanli-1914-1918.json", "o15"), ("milli-mucadele-1919-1922.json", "mm"), ("gokturk-uygur.json", "gu"), ("turkistan-hanliklari.json", "th"), ("bozkir-devletleri.json", "bd"), ("hun-avar-bulgar.json", "hb"), ("kipcaklar.json", "kp")]

# kaynak maddelerden çıkarılmış hicrî tarihler (tools/fill_hijri.py); kaydın kendi alanı boşsa kullanılır
HIJRI = json.loads((root / "data" / "hicri.json").read_text(encoding="utf-8")) if (root / "data" / "hicri.json").exists() else {}
battles, left_out = [], []
for name, prefix in BATCHES:
    d = json.loads((root / "data" / name).read_text(encoding="utf-8"))
    for b in d["battles"]:
        b = {**b, "id": f"{prefix}-{b['id']}", "batch": d["meta"]["batch"]}
        h = HIJRI.get(f"{b['home_batch']}|{b['name_tr']}")
        if not b.get("hijri") and h:
            b["hijri"] = h["hijri"]
        battles.append(b)
    left_out += d["left_out"]
data = {"battles": battles, "left_out": left_out}
borders = json.loads((root / "data" / "sinirlar.json").read_text(encoding="utf-8"))
bib = json.loads((root / "data" / "akademik-kaynaklar.json").read_text(encoding="utf-8"))["works"]
embed = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
html = (root / "site" / "template.html").read_text(encoding="utf-8").replace("/*DATA*/", embed(data), 1).replace("/*BORDERS*/", embed(borders), 1).replace("/*BIB*/", embed(bib), 1)
(root / "site" / "index.html").write_text(html, encoding="utf-8")
print("site/index.html", len(html), "bayt,", len(battles), "kayıt")
