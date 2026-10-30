"""Harita: 400–1000 arasında boş kalan Akdeniz batısı, Pannonia, Pencap ve Hazar kuzeyi bölgeleri (kontrol turu, 2026-10-30; tablo 400'e
uzatıldıktan sonra bu şehirlerin ilk dilimi hâlâ 712–1000 arasında başlıyordu, harita bu dönemlerde İtalya, Kuzey Afrika, İspanya ve
Macaristan'ı boş gösteriyordu). Bir kez çalıştırılmak üzere yazıldı. Yıllar genel tarih bilgisi, yaklaşık.
- Germen kavimleri devleti genişletildi: Vandal (Kuzey Afrika 429/455–534), Vizigot (İspanya 470–711), Ostrogot (İtalya 476–536).
- Kuzey Afrika: Bizans 534–698, Emevî, Abbâsî, Ağlebî (800–909, yeni devlet), Fâtımî 909–972, ardından Zîrîler (mevcut 1000 dilimi).
- Malta: Ağlebîler 870, Fâtımî, Kelbî emirliği (yerel) 948–1091; mevcut 1000–1530 İspanya dilimi yanlıştı: 1091–1283 Normanlar ve
  halefleri (Sicilya–Napoli krallığı katmanı), 1283'ten Aragon (İspanya).
- İspanya (Madrid): Batı Roma, Vizigotlar 470, Emevî 711, Endülüs 756.
- Pannonia: Avarlar 796'da Franklar'a yenildi; Tuna'nın batısı 796–895 Frank, doğusu 805–895 Krum'un Bulgarları. Buda'da 796–895 boşluk
  vardı.
- Pencap ve Gūr: Akhunlar (Toramana ve Mihirakula) Lahor çevresini 500–540 arasında yönetti; Gūr 460–550 Gazne ile aynı.
- Kuzey İtalya için Milano ve Venedik noktaları eklendi (Lombardlar 569, Franklar 774, Venedik Cumhuriyeti 811–1797).
- Ahsâ: 630'a kadar yerel, sonra Râşidîn, Emevî, Abbâsî; Saraycık (Ural ağzı) Deşt-i Kıpçak ile aynı sırayla."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
st = d["states"]
assert "aglebi" not in st
st["aglebi"] = {"tr": "Ağlebîler", "en": "Aghlabids", "group": "diger", "color": "#b0a483"}
assert st["germen"]["tr"] == "Germen kavimleri (Gepid, Lombard)"
st["germen"]["tr"] = "Germen kavimleri (Got, Vandal, Gepid, Lombard)"
by = {c.get("id"): c for c in d["cities"]}


def prepend(cid, seq):
    """İlk dilimden önceki dönemi seq ile doldurur; son öğe mevcut ilk dilime kadar sürer."""
    c = by[cid]
    first = c["spans"][0][0]
    assert seq[-1][0] < first, (cid, seq, first)
    c["spans"] = [[a, seq[i + 1][0] if i + 1 < len(seq) else first, s] for i, (a, s) in enumerate(seq)] + c["spans"]


PANNONIA_W = [(400, "hun"), (454, "germen"), (568, "avar"), (796, "frank")]
PANNONIA_E = [(400, "hun"), (454, "germen"), (568, "avar"), (805, "bulgar1")]
for cid in ("pozsony", "estergon", "sigetvar", "yanikkale", "kanije"):
    prepend(cid, PANNONIA_W)
prepend("uyvar", PANNONIA_W + [(895, "macar")])
for cid in ("egri", "varad", "erdel"):
    prepend(cid, PANNONIA_E)
b = by["buda"]["spans"]
assert b[2] == [568, 796, "avar"] and b[3][0] == 895, b
b.insert(3, [796, 895, "frank"])
prepend("viyana", PANNONIA_W)

prepend("napoli", [(400, "bati-roma"), (476, "germen"), (536, "bizans")])
prepend("madrid", [(400, "bati-roma"), (470, "germen"), (711, "emevi"), (756, "endulus")])
prepend("fas", [(400, "yerel"), (710, "emevi"), (740, "yerel")])
prepend("tunus", [(400, "bati-roma"), (429, "germen"), (534, "bizans"), (698, "emevi"), (750, "abbasi"), (800, "aglebi"), (909, "fatimi"), (972, "ziri")])
prepend("cezayir", [(400, "bati-roma"), (429, "germen"), (534, "bizans"), (698, "emevi"), (750, "yerel"), (909, "fatimi"), (972, "ziri")])
prepend("trablusgarp", [(400, "bati-roma"), (455, "germen"), (534, "bizans"), (643, "rasidun"), (661, "emevi"), (750, "abbasi"), (800, "aglebi"),
                        (909, "fatimi"), (972, "ziri")])
m = by["malta"]["spans"]
assert m[0] == [1000, 1530, "ispanya"], m[0]
m[0:1] = [[1000, 1091, "yerel"], [1091, 1283, "napoli"], [1283, 1530, "ispanya"]]
prepend("malta", [(400, "bati-roma"), (454, "germen"), (535, "bizans"), (870, "aglebi"), (909, "fatimi"), (948, "yerel")])

prepend("lahor", [(400, "yerel"), (500, "akhun"), (540, "yerel")])
prepend("multan", [(400, "yerel")])
prepend("firuzkuh", [(400, "yerel"), (460, "akhun"), (550, "yerel")])
prepend("ahsa", [(400, "yerel"), (630, "rasidun"), (661, "emevi"), (750, "abbasi")])
prepend("saraycik", [(400, "hun"), (454, "onogur"), (552, "bati-gokturk"), (630, "hazar")])

# Kuzey İtalya'da hiç nokta yoktu (452 Aquileia ve Milano kayıtları boş toprağa düşüyordu)
END = max(x[1] for c in d["cities"] for x in c.get("spans", []))
for cid, tr, lat, lon, seq in [
    ("milano", "Milano (Lombardiya)", 45.46, 9.19, [(400, "bati-roma"), (476, "germen"), (553, "bizans"), (569, "germen"), (774, "frank"), (888, "yerel"),
                                                  (962, "kutsal-roma"), (1250, "yerel"), (1535, "ispanya"), (1714, "habsburg"), (1797, "fransa"),
                                                  (1815, "habsburg"), (1859, "italya")]),
    ("venedik", "Venedik", 45.44, 12.33, [(400, "bati-roma"), (476, "germen"), (540, "bizans"), (811, "venedik"), (1797, "habsburg"), (1805, "fransa"),
                                         (1815, "habsburg"), (1866, "italya")]),
]:
    assert cid not in by, cid
    d["cities"].append({"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": [[a, seq[i + 1][0] if i + 1 < len(seq) else END, s] for i, (a, s) in enumerate(seq)],
                        "src": [], "yaklasik": True})

# Bitişik aynı devlet dilimleri birleştirilir
for c in d["cities"]:
    sp = c.get("spans")
    if not sp:
        continue
    out = [sp[0]]
    for x in sp[1:]:
        if x[2] == out[-1][2] and x[0] == out[-1][1]:
            out[-1] = [out[-1][0], x[1], x[2]]
        else:
            out.append(x)
    c["spans"] = out
for c in d["cities"]:
    sp = c.get("spans", [])
    for a, b2, s in sp:
        assert s in st, (c["id"], s); assert a < b2, (c["id"], a, b2)
    for x, y in zip(sp, sp[1:]):
        assert x[1] <= y[0], (c["id"], x, y)
d["meta"]["method"] += " 400–1000 arasında boş kalan İtalya, Kuzey Afrika, Malta, İspanya, Pannonia, Pencap, Gūr, Ahsâ ve Ural ağzı dolduruldu (Germen krallıkları, Ağlebîler)."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("tamam")
