"""Pilot verisini ve sınır tablosunu site/template.html içine gömüp site/index.html üretir (file:// ile açılabilsin diye)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
data = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
borders = json.loads((root / "data" / "sinirlar.json").read_text(encoding="utf-8"))
embed = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
html = (root / "site" / "template.html").read_text(encoding="utf-8").replace("/*DATA*/", embed(data), 1).replace("/*BORDERS*/", embed(borders), 1)
(root / "site" / "index.html").write_text(html, encoding="utf-8")
print("site/index.html", len(html), "bayt,", len(data["battles"]), "kayıt")
