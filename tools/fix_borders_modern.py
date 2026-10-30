"""Harita: 1923'e kadar uzayan eskimiş son dilimler (kontrol turu, 2026-10-30). Bir kez çalıştırılmak üzere yazıldı.
Lejant 1922'de Napoli Krallığı, Lehistan-Litvanya, Kalmuklar, Habsburglar gibi o yıl artık var olmayan devletleri gösteriyordu.
Geçiş yılları genel tarih bilgisidir ve yıl çözünürlüğünde yaklaşıktır:
- Habsburg monarşisi 1918'de dağıldı: Viyana Avusturya, Macaristan şehirleri Macaristan, Pozsony Çekoslovakya, Erdel/Varad/Temeşvar
  Romanya (1918–1920), Bosna ve Sırbistan şehirleri Sırp-Hırvat-Sloven Krallığı, Uyvar Çekoslovakya, İlbav Polonya.
- Varşova: Lehistan'ın paylaşılması (1795) sonrası 1815'ten itibaren Rus yönetimi, 1918 Polonya. 1795–1815 Prusya ve Varşova Dukalığı
  dönemi Rusya dışı bir devletle gösterilmez; dilim Lehistan'da bırakıldı.
- Napoli 1861'de İtalya'ya katıldı; Malta 1800'de İngiltere'ye geçti; Fas 1912'de Fransız himayesine girdi.
- Kalmuk Hanlığı 1771'de Rusya'ya bağlandı (Hazar kuzeyi, Saraycık); Sır Derya ağzı (Yengikent) 1847'de Rus kalesi Raim ile Rusya.
- Gürcistan: İmereti (Kutais) 1810'da Rusya, 1918 Gürcistan Cumhuriyeti; Kafkas cumhuriyetleri 1920–1921'de Sovyet yönetimine geçti.
- Gazne, Büst, Gûr: Bâbürlüler 1738'e kadar (Nâdir Şah'ın seferi), sonra Afşarlar ve 1747 Dürrânîler; Afgan şehirleri 1826 sonrası
  Barakzay Afganistan'ı.
- Kâşgar ve Koço 1912'de Çin Cumhuriyeti; Hîve (Gürgenç) ve Buhara 1920'de Sovyet yönetimi; Halep ve Dımaşk 1920'de Fransız mandası."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
st = d["states"]
END = max(s[1] for c in d["cities"] for s in c.get("spans", []))
by = {c.get("id"): c for c in d["cities"]}
for k, (tr, en, col) in {
    "avusturya": ("Avusturya", "Austria", "#8f86a6"),
    "cekoslovakya": ("Çekoslovakya", "Czechoslovakia", "#7f9bb3"),
    "shs": ("Sırp-Hırvat-Sloven Krallığı", "Kingdom of Serbs, Croats and Slovenes", "#9a8fb8"),
    "polonya": ("Polonya", "Poland", "#b3858f"),
    "sovyet": ("Sovyet Rusya", "Soviet Russia", "#a3605a"),
    "afganistan": ("Afganistan Emirliği", "Emirate of Afghanistan", "#9fae7a"),
    "cin-cum": ("Çin Cumhuriyeti", "Republic of China", "#c9a35a"),
}.items():
    assert k not in st, k
    st[k] = {"tr": tr, "en": en, "group": "diger", "color": col}
assert "afsar" in st and "macar" in st


def tail(cid, cut, new):
    """cut yılından sonrasını siler, yerine new dilimlerini koyar (son dilim END'e uzar)."""
    c = by[cid]
    out = [[a, min(b, cut), s] for a, b, s in c["spans"] if a < cut]
    for i, (a, s) in enumerate(new):
        b = new[i + 1][0] if i + 1 < len(new) else END
        out.append([a, b, s])
    c["spans"] = out


tail("viyana", 1918, [(1918, "avusturya")])
for cid in ("buda", "estergon", "egri", "sigetvar", "kanije", "yanikkale"):
    tail(cid, 1918, [(1918, "macar")])
for cid in ("pozsony", "uyvar"):
    tail(cid, 1918, [(1918, "cekoslovakya")])
for cid in ("erdel", "varad"):
    tail(cid, 1918, [(1918, "romanya")])
tail("temesvar", 1919, [(1919, "romanya")])
for cid in ("sarajevo", "uskup", "manastir", "nis", "pristine", "belgrad", "semendire"):
    tail(cid, 1918, [(1918, "shs")])
tail("lviv", 1918, [(1918, "polonya")])
tail("varsova", 1815, [(1815, "rusya"), (1918, "polonya")])
tail("napoli", 1861, [(1861, "italya")])
tail("malta", 1798, [(1798, "fransa"), (1800, "ingiltere")])
tail("fas", 1912, [(1912, "fransa")])
for cid in ("desti-kipcak", "saraycik"):
    tail(cid, 1771, [(1771, "rusya")])
tail("yengikent", 1847, [(1847, "rusya")])
tail("kutais", 1810, [(1810, "rusya"), (1918, "gurcistan-cum"), (1921, "sovyet")])
tail("tiflis", 1921, [(1921, "sovyet")])
for cid in ("gence", "semahi", "revan"):
    tail(cid, 1920, [(1920, "sovyet")])
for cid in ("gazne", "bust", "firuzkuh"):
    tail(cid, 1738, [(1738, "afsar"), (1747, "durrani"), (1826, "afganistan")])
for cid in ("herat", "zerenc", "belh"):
    tail(cid, 1826, [(1826, "afganistan")])
for cid in ("kasgar", "koco"):
    tail(cid, 1912, [(1912, "cin-cum")])
for cid in ("halep", "dimask"):
    tail(cid, 1920, [(1920, "fransa")])
# Rusya'nın 1918 sonrası Sovyet dönemi: Rus dilimleri 1917 sonrasında "Sovyet Rusya" olur
for c in d["cities"]:
    sp = c.get("spans", [])
    if sp and sp[-1][2] == "rusya" and sp[-1][1] == END and sp[-1][0] < 1918:
        sp[-1][1] = 1918
        sp.append([1918, END, "sovyet"])
    elif sp and sp[-1][2] == "rusya" and sp[-1][1] == END:
        sp[-1][2] = "sovyet"  # Hîve ve Buhara 1920'de Sovyet yönetimine girdi

for c in d["cities"]:
    sp = c.get("spans", [])
    for a, b, s in sp:
        assert s in st, (c["id"], s); assert a < b, (c["id"], a, b)
    for x, y in zip(sp, sp[1:]):
        assert x[1] <= y[0], (c["id"], x, y)
d["meta"]["method"] += " 1923'e uzanan eskimiş son dilimler güncellendi (Habsburg mirası 1918, Sovyet dönemi, Afganistan, Çin Cumhuriyeti)."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("tamam")
