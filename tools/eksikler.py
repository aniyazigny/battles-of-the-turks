"""Her partide tek TDVİA maddesine dayanan kayıtları ve dışarıda bırakılanları listeler (docs/EKSIKLER.md için)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
for f in sorted((root / "data").glob("*.json")):
    d = json.loads(f.read_text(encoding="utf-8"))
    if not isinstance(d, dict) or "battles" not in d:
        continue
    single = [b for b in d["battles"] if not b["verify"].get("tdvia2")]
    print(f"## {f.stem}: {len(d['battles'])} kayıt, {len(single)} tek kaynaklı")
    for b in single:
        print(f"  - {b['name_tr']} ({b['date']}) {', '.join(b['sources'])}")
    for x in d.get("left_out", []):
        print(f"  ~ dışarıda: {x['name']}")
