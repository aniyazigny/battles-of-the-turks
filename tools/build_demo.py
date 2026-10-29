"""Parti verilerini ve sınır tablosunu site/template.html içine gömüp site/index.html üretir (file:// ile açılabilsin diye)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
# (dosya, kimlik öneki) — yeni partiler buraya eklenir
BATCHES = [("pilot-buyuk-selcuklu.json", "bs"), ("anadolu-selcuklu.json", "as"), ("beylikler-atabeylikler.json", "ba"), ("gazneli-karahanli.json", "gk"), ("osmanli-kurulus.json", "ok"), ("osmanli-1402-1481.json", "o2"), ("osmanli-1481-1520.json", "o3"), ("osmanli-1520-1566.json", "o4"), ("osmanli-1566-1606.json", "o5")]

battles, left_out = [], []
for name, prefix in BATCHES:
    d = json.loads((root / "data" / name).read_text(encoding="utf-8"))
    for b in d["battles"]:
        battles.append({**b, "id": f"{prefix}-{b['id']}", "batch": d["meta"]["batch"]})
    left_out += d["left_out"]
data = {"battles": battles, "left_out": left_out}
borders = json.loads((root / "data" / "sinirlar.json").read_text(encoding="utf-8"))
bib = json.loads((root / "data" / "akademik-kaynaklar.json").read_text(encoding="utf-8"))["works"]
embed = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
html = (root / "site" / "template.html").read_text(encoding="utf-8").replace("/*DATA*/", embed(data), 1).replace("/*BORDERS*/", embed(borders), 1).replace("/*BIB*/", embed(bib), 1)
(root / "site" / "index.html").write_text(html, encoding="utf-8")
print("site/index.html", len(html), "bayt,", len(battles), "kayıt")
