"""Harita eksiği (EKSIKLER §3): Lahsâ 1818–1913. Lahsâ maddesine göre: 1818'den sonra Benî Hâlid kabilesi eski gücüne kavuştu;
İbrâhim Paşa'nın çekilmesinden sonra Faysal b. Türkî Benî Hâlid'i yenip Lahsâ'yı aldı (yıl maddede yok, yaklaşık 1830);
Osmanlı kuvvetleri geri gelip Faysal'ı sürgüne gönderdi (Ekim 1841); bölge Benî Hâlid ile Osmanlı adına hareket eden Suûdîler
arasında paylaşıldı; Midhat Paşa 1871'de Necid sancağını kurdu; İbn Suûd 8 Temmuz 1913'te bölgeyi aldı. Bir kez çalıştırılır."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
c = next(x for x in d["cities"] if x.get("id") == "ahsa")
i = c["spans"].index([1818, 1913, "osmanli"])
c["spans"][i:i + 1] = [[1818, 1830, "arap"], [1830, 1841, "suud"], [1841, 1871, "arap"], [1871, 1913, "osmanli"]]
c["yaklasik"] = True
c["src"] = sorted(set(c.get("src", []) + ["lahsa"]))
d["meta"]["method"] += " Lahsâ 1818–1913: Benî Hâlid, Suûdî (yaklaşık 1830–1841), 1871'den Osmanlı."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(c["spans"][-6:])
