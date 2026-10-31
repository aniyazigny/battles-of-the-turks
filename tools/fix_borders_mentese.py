"""Harita: Menteşe (Muğla yöresi), Rodos, Bodrum ve komşu beyliklerin Osmanlı'ya geçiş yılları (kontrol turu, 2026-10-31). Bir kez
çalıştırılmak üzere yazıldı. Batı Anadolu beyliklerinin 1402 sonrası dilimleri hep 1425'te bitiyordu; bu bir yer tutucuydu, TDVİA
maddelerine göre ayrı ayrı düzeltildi.
- Menteşe (Milas noktası): Karya 1261'den Menteşeoğulları'nın (TDVİA Muğla; dilim 1280'den başlıyordu), Yıldırım 1390'da aldı, kesin
  Osmanlı ilhakı 1424 (TDVİA Muğla: "827 (1424) yılında kesin şekilde"). 23 Temmuz 1919–1921 İtalyan işgali (TDVİA Muğla, Milas).
- Germiyan (Kütahya, Denizli): Yâkub Bey ülkesini Osmanlılar'a vasiyet etti, 1428'de Edirne'ye gitti ve bir yıl sonra öldü; ilhak 1429
  (TDVİA Germiyanoğulları).
- Saruhan (Manisa): Saruhan ülkesi 1411'den sonra, 1415'ten önce Çelebi Mehmed'e geçti (TDVİA Saruhanoğulları); 1414 alındı, yaklaşık.
- Antalya: 1402'den sonra da Osmanlı'da kaldı (TDVİA Tekeoğulları: 1402–1415 "Antalya ve Alâiye dışında" Teke-ili Karamanoğlu'nun;
  Osman Çelebi'nin Ocak 1423 kuşatması başarısız). Hamîd dilimi 1402–1425 yanlıştı. 29 Nisan 1919–1 Haziran 1921 İtalyan işgali
  (TDVİA Antalya).
- Rodos: 717–718 Arap işgali (TDVİA Rodos), Menteşe Beyi Mesud Bey adanın önemli kısmını 1300'de aldı, şövalyeler 1309'da hâkim oldu
  (TDVİA Menteşeoğulları, Rodos).
- Bodrum noktası eklendi: Rodos şövalyeleri 1415'ten Kanûnî'nin 1522 Rodos seferine kadar burada kale tuttu; 11 Mayıs 1919'da İtalyan
  işgali, 1921'de çekildiler (TDVİA Bodrum)."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
st = d["states"]
by = {c.get("id"): c for c in d["cities"]}


def setspans(cid, old, new):
    """old dilimlerini sırayla bulur ve new ile değiştirir."""
    sp = by[cid]["spans"]
    i = sp.index(old[0])
    assert sp[i:i + len(old)] == old, (cid, sp[i:i + len(old)])
    assert old[0][0] == new[0][0] and old[-1][1] == new[-1][1], (cid, old, new)
    sp[i:i + len(old)] = new


setspans("milas", [[400, 1280, "bizans"], [1280, 1390, "mentese"], [1390, 1402, "osmanli"], [1402, 1425, "mentese"], [1425, 1920, "osmanli"], [1920, 1923, "tbmm"]],
         [[400, 1261, "bizans"], [1261, 1390, "mentese"], [1390, 1402, "osmanli"], [1402, 1424, "mentese"], [1424, 1919, "osmanli"], [1919, 1921, "italya"],
          [1921, 1923, "tbmm"]])
for cid in ("kutahya", "denizli"):
    setspans(cid, [[1402, 1425, "germiyan"], [1425, 1920, "osmanli"]], [[1402, 1429, "germiyan"], [1429, 1920, "osmanli"]])
setspans("manisa", [[1402, 1425, "saruhan"], [1425, 1919, "osmanli"]], [[1402, 1414, "saruhan"], [1414, 1919, "osmanli"]])
setspans("antalya", [[1390, 1402, "osmanli"], [1402, 1425, "hamid"], [1425, 1920, "osmanli"], [1920, 1923, "tbmm"]],
         [[1390, 1919, "osmanli"], [1919, 1921, "italya"], [1921, 1923, "tbmm"]])
setspans("rodos", [[400, 1309, "bizans"]], [[400, 717, "bizans"], [717, 718, "emevi"], [718, 1300, "bizans"], [1300, 1309, "mentese"]])

assert "bodrum" not in by
END = max(x[1] for c in d["cities"] for x in c.get("spans", []))
seq = [(400, "bizans"), (1261, "mentese"), (1390, "osmanli"), (1402, "mentese"), (1415, "latin"), (1522, "osmanli"), (1919, "italya"), (1921, "tbmm")]
d["cities"].append({"id": "bodrum", "tr": "Bodrum (Rodos şövalyeleri kalesi)", "lat": 37.03, "lon": 27.43,
                    "spans": [[a, seq[i + 1][0] if i + 1 < len(seq) else END, s] for i, (a, s) in enumerate(seq)], "src": ["bodrum", "mugla"], "yaklasik": True})
for cid, s in (("milas", ["mugla", "milas", "menteseogullari"]), ("kutahya", ["germiyanogullari"]), ("denizli", ["germiyanogullari"]),
               ("manisa", ["saruhanogullari"]), ("antalya", ["antalya", "tekeogullari"]), ("rodos", ["menteseogullari"])):
    src = by[cid].setdefault("src", [])
    src += [x for x in s if x not in src]

for c in d["cities"]:
    sp = c.get("spans", [])
    for a, b2, s in sp:
        assert s in st, (c["id"], s); assert a < b2, (c["id"], a, b2)
    for x, y in zip(sp, sp[1:]):
        assert x[1] <= y[0], (c["id"], x, y)
d["meta"]["method"] += (" Batı Anadolu beyliklerinin Osmanlı'ya kesin geçiş yılları ayrı ayrı düzeltildi (Menteşe 1424, Germiyan 1429, Saruhan c. 1414;"
                        " Antalya 1402'den sonra da Osmanlı'da); Menteşe 1261'den; Rodos'ta Arap ve Menteşe dönemleri; Bodrum noktası; Muğla ve Antalya'da 1919–1921 İtalyan işgali.")
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("tamam")
