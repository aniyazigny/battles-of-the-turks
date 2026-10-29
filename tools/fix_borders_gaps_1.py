"""Harita eksikleri, kontrol turu 1 (EKSIKLER §3). Bir kez çalıştırılmak üzere yazıldı.
- Teselya: Yenişehir (Larissa) noktası eklendi. Osmanlı 1386–1881 (Yenişehir maddesi), 1881 sonrası Yunanistan; 1897 savaşında
  şehir kısa bir süre Osmanlı'ya geçtiyse de yıl çözünürlüğünde gösterilmez.
- Kırkkilise noktası eklendi: Osmanlı 1366 (fetih için 1361/1366/1368 verilir; Kırklareli maddesi), Bulgar işgali 24 Ekim 1912 –
  21 Temmuz 1913, Yunan işgali 26 Temmuz 1920 – 10 Kasım 1922 (Kırklareli maddesi).
- Kıbrıs: 1489'da Venedik'e geçti (Kıbrıs maddesi: Kraliçe Caterina 26 Şubat 1489'da tahttan çekildi)."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
st = d["states"]
END = max(s[1] for c in d["cities"] for s in c.get("spans", []))
by = {c.get("id"): c for c in d["cities"]}


def add(cid, tr, lat, lon, spans, src):
    assert cid not in by, cid
    d["cities"].append({"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": spans, "src": src, "yaklasik": True})


add("yenisehir", "Yenişehir (Larissa)", 39.64, 22.42,
    [[550, 1204, "bizans"], [1204, 1222, "latin"], [1222, 1348, "bizans"], [1348, 1386, "sirbistan"], [1386, 1881, "osmanli"], [1881, END, "yunanistan"]],
    ["yenisehir", "tesalya"])
add("kirkkilise", "Kırkkilise (Kırklareli)", 41.735, 27.225,
    [[550, 1366, "bizans"], [1366, 1912, "osmanli"], [1912, 1913, "bulgaristan"], [1913, 1920, "osmanli"], [1920, 1922, "yunanistan"], [1922, END, "tbmm"]],
    ["kirklareli"])

k = by["kibris"]
assert [1191, 1570, "kibris"] in k["spans"], k["spans"]
i = k["spans"].index([1191, 1570, "kibris"])
k["spans"][i:i + 1] = [[1191, 1489, "kibris"], [1489, 1570, "venedik"]]
k["src"] = sorted(set(k.get("src", []) + ["kibris"]))

for c in d["cities"]:
    sp = c.get("spans", [])
    for a, b, s in sp:
        assert s in st, (c["id"], s); assert a < b, (c["id"], a, b)
    for x, y in zip(sp, sp[1:]):
        assert x[1] <= y[0], (c["id"], x, y)
d["meta"]["method"] += " Kontrol turu 1: Yenişehir (Teselya 1881) ve Kırkkilise noktaları; Kıbrıs 1489–1570 Venedik."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta")
