"""Harita (Parti 23): Ötüken'in K'i-tanlar'a geçişi Kırgızlar maddesine göre 920 (önceden 924). Bir kez çalıştırılmak üzere yazıldı."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
c = next(c for c in d["cities"] if c.get("id") == "otuken")
sp = c["spans"]
i = next(i for i, s in enumerate(sp) if s[2] == "kirgiz")
assert sp[i][1] == 924 and sp[i + 1] == [924, 1125, "kitan"], sp
sp[i][1] = 920
sp[i + 1][0] = 920
c["src"] = sorted(set(c.get("src", []) + ["kirgizlar"]))
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("tamam")
