"""Harita: sınır tablosunu 400'e uzatır ve Tuna–Turla kalelerini ekler (kontrol turu, 2026-10-30; EKSIKLER: tablo 550'de başlıyordu,
Parti 24'ün 427–550 kayıtları sahipsiz görünüyordu). Bir kez çalıştırılmak üzere yazıldı. Yıllar genel tarih bilgisi, yaklaşık.
- 550'de Bizans, Sâsânî, Kuzey/Güney Çin, Tibet, Hoten, Gürcistan, Hicaz ve Hârizm ile başlayan şehirler 400'e uzatıldı.
- Avrupa Hunları 400–454 (Attila'nın ölümü ve Nedao); Karadeniz ve Hazar kuzeyi 454–552 Ogur ve Bulgar boyları (Kutrigur, Utigur, Sabir).
- Pannonia 454–568 Germen kavimleri (Gepid, Lombard); Avarlar 568'de geldi (Bükreş 550'den Avar görünüyordu).
- Akhunlar Toharistan ve Mâverâünnehir'de 450'den, Kâşgar, Yedisu ve Fergana'da 470'ten; öncesi yerel (Kidarit) yönetim.
- İdil boyu ve Sır Derya ağzı 552 öncesi boş bırakıldı (kaynak yok).
- Galya 486'ya kadar Batı Roma (451 Katalaunum ve Metz kayıtları), sonra Franklar. Moğolistan ve Turfan 400–552 Juan-juanlar.
- Tuna kaleleri: Silistre ve Rusçuk 1388–1878 Osmanlı; İbrail 1540–1829 Osmanlı; Hotin 1713–1806 Osmanlı. Bu savaşlar önceden
  en yakın şehir olan Bükreş'e (Eflak) veya Kamaniçe'ye (Lehistan) düşüyordu."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
st = d["states"]
for k, (tr, en, g, col) in {
    "hun": ("Avrupa Hun İmparatorluğu", "Hunnic Empire", "turk", "#6a7fb5"),
    "onogur": ("Ogur ve Bulgar boyları", "Ogur and Bulgar tribes", "turk-diger", "#8a9cb8"),
    "germen": ("Germen kavimleri (Gepid, Lombard)", "Germanic peoples", "diger", "#a3a89a"),
    "bati-roma": ("Batı Roma İmparatorluğu", "Western Roman Empire", "diger", "#b3a0b0"),
    "frank": ("Frank Krallığı", "Frankish Kingdom", "diger", "#9fa6b8"),
}.items():
    assert k not in st, k
    st[k] = {"tr": tr, "en": en, "group": g, "color": col}
assert "akhun" in st and "yerel" in st, "önce fix_borders_tarama.py çalıştırılmalı"

END = max(s[1] for c in d["cities"] for s in c.get("spans", []))
by = {c.get("id"): c for c in d["cities"]}


def prepend(cid, seq):
    """İlk dilimden önceki dönemi seq ile doldurur: seq = [(başlangıç, devlet), ...]; son öğe mevcut ilk dilime kadar sürer."""
    c = by[cid]
    first = c["spans"][0][0]
    assert seq[-1][0] < first, (cid, seq, first)
    new = [[a, seq[i + 1][0] if i + 1 < len(seq) else first, s] for i, (a, s) in enumerate(seq)]
    c["spans"] = new + c["spans"]


# Aynı devletle 550'de başlayan şehirler 400'e uzar
SAME = {"bizans", "sasani", "kuzey-cin", "guney-cin", "tibet", "hoten-krl", "gurcistan", "hicaz", "afrigi", "juan-juan"}
for c in d["cities"]:
    sp = c.get("spans")
    if sp and sp[0][0] == 550 and sp[0][2] in SAME and c["id"] != "cengdu":
        sp[0][0] = 400
prepend("cengdu", [(400, "guney-cin")])  # Siçuan 553'e kadar güney hanedanlarındaydı
# Akhunlar
for cid in ("buhara", "semerkant", "belh"):
    assert by[cid]["spans"][0][:1] == [550], cid
    by[cid]["spans"][0][0] = 450
    prepend(cid, [(400, "yerel")])
for cid in ("gazne", "bust"):
    prepend(cid, [(400, "yerel"), (460, "akhun")])
for cid in ("kasgar", "balasagun", "gulca", "hokand", "taskent", "cimkent"):
    prepend(cid, [(400, "yerel"), (470, "akhun")])
# Bozkır ve Pannonia
for cid in ("karadeniz-bozkiri", "desti-kipcak"):
    prepend(cid, [(400, "hun"), (454, "onogur")])
b = by["bukres"]
assert b["spans"][0] == [550, 680, "avar"], b["spans"][0]
b["spans"][0][0] = 568
prepend("bukres", [(400, "hun"), (454, "germen")])
prepend("buda", [(400, "hun"), (454, "germen")])
prepend("temesvar", [(400, "hun"), (454, "germen"), (568, "avar"), (805, "bulgar1")])  # Krum Avar topraklarını 805'te aldı
prepend("bender", [(400, "hun"), (454, "onogur"), (568, "avar"), (680, "bulgar1"), (895, "pecenek")])
for cid in ("yas", "ozu"):
    prepend(cid, [(895, "pecenek")])
# Doğu
for cid in ("koco", "kumul", "bati-mogol"):
    prepend(cid, [(400, "juan-juan")])
for cid in ("otuken", "yinsan"):
    assert by[cid]["spans"][0][2] == "juan-juan"
    by[cid]["spans"][0][0] = 400
# Galya
assert by["fransa"]["spans"][0][0] == 1000
prepend("fransa", [(400, "bati-roma"), (486, "frank")])

# Tuna ve Turla kaleleri
for cid, tr, lat, lon, seq, src in [
    ("silistre", "Silistre", 44.12, 27.26, [(400, "bizans"), (680, "bulgar1"), (971, "bizans"), (1185, "bulgar2"), (1388, "osmanli"),
                                            (1878, "bulgaristan"), (1913, "romanya")], ["silistre"]),
    ("ruscuk", "Rusçuk", 43.85, 25.95, [(400, "bizans"), (680, "bulgar1"), (971, "bizans"), (1185, "bulgar2"), (1388, "osmanli"),
                                        (1878, "bulgaristan")], ["ruscuk"]),
    ("ibrail", "İbrail", 45.27, 27.96, [(400, "hun"), (454, "germen"), (568, "avar"), (680, "bulgar1"), (895, "pecenek"), (1060, "kipcak"),
                                        (1240, "altin-orda"), (1310, "eflak"), (1540, "osmanli"), (1829, "eflak"), (1858, "romanya")], ["ibrail"]),
    ("hotin", "Hotin", 48.52, 26.49, [(895, "pecenek"), (1060, "kipcak"), (1240, "altin-orda"), (1359, "bogdan"), (1713, "osmanli"),
                                      (1806, "rusya"), (1918, "romanya")], ["hotin"]),
]:
    assert cid not in by, cid
    sp = [[a, seq[i + 1][0] if i + 1 < len(seq) else END, s] for i, (a, s) in enumerate(seq)]
    d["cities"].append({"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": sp, "src": src, "yaklasik": True})

for c in d["cities"]:
    sp = c.get("spans", [])
    for a, b2, s in sp:
        assert s in st, (c["id"], s); assert a < b2, (c["id"], a, b2)
    for x, y in zip(sp, sp[1:]):
        assert x[1] <= y[0], (c["id"], x, y)
d["meta"]["method"] += " Tablo 400'e uzatıldı (Avrupa Hunları, Ogur boyları, Akhunlar, Juan-juanlar, Batı Roma, Franklar); Tuna ve Turla kaleleri eklendi."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("tamam")
