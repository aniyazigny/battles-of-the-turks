"""Kayıtları 'Where the Romans Fought' veri setiyle (raw/rom/rom.json) eşleştirir.
Eşleşme: yıl farkı ≤1 ve yer farkı ≤80 km ve ROM kaydında Türk tarafı (Seljuks, Danishmends, Zengids, Turkish beyliks, Ottomans).
Kullanım: python -I -X utf8 tools/match_rom.py [--write]   (--write: verify.rom ve ROM kaynağını ekler; elle tutulan pilot dosyası
için doğrudan, üreticili partiler için tools/rom_matches.json aracılığıyla)"""
import json, math, re, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
rom = json.loads((root / "raw" / "rom" / "rom.json").read_text(encoding="utf-8"))
TURK = re.compile(r"Seljuk|Danishmend|Zengid|Artuq|Turkish beylik|Ottoman", re.I)
cand = [r for r in rom if r["year"] and 1030 <= r["year"] <= 1310 and TURK.search(" ".join(r["side_a"] + r["side_b"]))]

def km(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))

BATCHES = ["pilot-buyuk-selcuklu", "anadolu-selcuklu", "beylikler-atabeylikler", "gazneli-karahanli"]
matches, used = {}, set()
for name in BATCHES:
    d = json.loads((root / "data" / f"{name}.json").read_text(encoding="utf-8"))
    for b in d["battles"]:
        y = int(re.search(r"\d{3,4}", b["date"]).group())
        best = min(((km((b["lat"], b["lon"]), (r["lat"], r["lon"])), r) for r in cand if abs(r["year"] - y) <= 1), default=None, key=lambda t: t[0])
        if best and best[0] <= 80:
            r = best[1]; used.add(r["id"])
            matches[f"{name}:{b['id']}"] = {"rom_id": r["id"], "rom_name": r["name"], "rom_year": r["year"], "rom_winner": r["side_a"] if r["outcome"] == "A" else "draw",
                                            "ours": b["name_tr"], "our_result": b["result"], "km": round(best[0])}
for k, m in matches.items():
    print(k, "|", m["ours"], m["our_result"], "<->", m["rom_id"], m["rom_name"], m["rom_year"], m["rom_winner"], f"{m['km']} km")
print("\nEŞLEŞMEYEN ROM KAYITLARI:")
for r in cand:
    if r["id"] not in used:
        print(r["id"], r["year"], r["name"], r["side_a"], "v", r["side_b"], r["outcome"])
if "--write" in sys.argv:
    (root / "tools" / "rom_matches.json").write_text(json.dumps(matches, ensure_ascii=False, indent=1), encoding="utf-8")
