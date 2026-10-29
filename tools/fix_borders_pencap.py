"""Harita eksiği (EKSIKLER §3): Lahor ve Mültan noktaları 1000 öncesinde boştu. Bir kez çalıştırılır.
- Mültan 712'de Muhammed b. Kāsım'la fethedildi (Mültan maddesi); Emevî 712–750, Abbâsî 750–960 (yerel emîrler, kaba), Karmatî
  yaklaşık 960–1006 (Gazneli Mahmud şehri Karmatî Dâvûd'dan aldı, 1006).
- Lahor: Hindûşâhîler Peşâver, Lahor ve Cullandâr'ı hâkimiyetleri altına almışlardı (Hindûşâhîler maddesi); 870–1000 Hindûşâhî (kaba)."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
d["states"].setdefault("hindusahi", {"tr": "Hindûşâhîler", "en": "Hindu Shahis", "group": "diger", "color": "#b8a48a"})
by = {c.get("id"): c for c in d["cities"]}
m, l = by["multan"], by["lahor"]
assert m["spans"][0][0] == 1000 and l["spans"][0][0] == 1000
m["spans"] = [[712, 750, "emevi"], [750, 960, "abbasi"], [960, 1000, "karmati"]] + m["spans"]
l["spans"] = [[870, 1000, "hindusahi"]] + l["spans"]
for c, s in ((m, "multan"), (l, "hindusahiler")):
    c["yaklasik"] = True
    c["src"] = sorted(set(c.get("src", []) + [s]))
d["meta"]["method"] += " Pencap 1000 öncesi: Mültan Emevî/Abbâsî/Karmatî, Lahor Hindûşâhî (kaba)."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(m["spans"][:5], l["spans"][:3])
