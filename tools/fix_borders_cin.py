"""Harita: Çin, Tibet ve Moğolistan'ın doğu kenarı (kontrol turu, 2026-10-30; kullanıcı Çin'in küçük ve yer yer yanlış göründüğünü
bildirdi). Bir kez çalıştırılmak üzere yazıldı.
Önceden doğuda yalnız Koço, Kâşgar ve Ötüken noktaları vardı; Gansu, Kumul, İli, Hoten, Tibet ve asıl Çin için nokta yoktu, Batı
Moğolistan boş (void) hücreydi. Bu yüzden T'ang ve Çing dönemlerinde Çin birkaç hücreden ibaret görünüyor, Gansu koridoru boş kalıyordu.
Hanedan yılları genel tarih bilgisidir ve yaklaşıktır (TDVİA Çin, Tibet ve Hoten maddeleri genel çerçeveyi verir):
Sui 581–618, T'ang 618–907, Kuzey Song 960–1127, Cin (Cürçen) 1125–1234, Tangut (Batı Hsia) 1028–1227, Yuan 1271–1368 (Moğol
İmparatorluğu katmanıyla birlikte), Ming 1368–1644, Çing 1644–1912. Tibet İmparatorluğu Gansu'yu 764–848, Kumul'u 781–866 arasında,
Hoten'i 790–851 arasında tuttu. Kan-chou Uygurları 894–1028 (Tangutlar'ca yıkıldı). Hoten 1006'da Karahanlılar'a geçti (Hoten maddesi:
XI. yüzyıl başında tamamen Karahanlı idaresinde). Kumul 1697'de, İli 1758'de Çing'e geçti; İli 1871–1881 Rus işgalinde kaldı.
Batı Moğolistan 1634–1757 Cungar, 1757–1911 Çing. Güney Çin: Ch'en 557–589, On Krallık 907–960, Güney Song 1127–1279.
Ayrıca Gürgenç (Hârizm) 550–712 Sâsânî yerine Afrîgîler (Kuteybe'nin 712 fethi)."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
st = d["states"]
for k, (tr, en, g, col) in {
    "kuzey-cin": ("Kuzey Çin hanedanları", "Northern Chinese dynasties", "diger", "#c49a8a"),
    "sui": ("Çin (Sui)", "China (Sui)", "diger", "#c49a8a"),
    "song": ("Çin (Song)", "China (Song)", "diger", "#c49a8a"),
    "ming": ("Çin (Ming)", "China (Ming)", "diger", "#c49a8a"),
    "jin": ("Cin (Cürçen) Devleti", "Jin (Jurchen) dynasty", "diger", "#b5a08a"),
    "bati-xia": ("Tangutlar (Batı Hsia)", "Western Xia (Tangut)", "diger", "#b0a38f"),
    "tibet": ("Tibet", "Tibet", "diger", "#b8a0c0"),
    "hoten-krl": ("Hoten Krallığı", "Kingdom of Khotan", "diger", "#a9b0a0"),
    "kancou": ("Kan-chou Uygurları", "Ganzhou Uyghurs", "turk-diger", "#7fa59a"),
    "guney-cin": ("Güney Çin hanedanları", "Southern Chinese dynasties", "diger", "#c49a8a"),
    "afrigi": ("Hârizm (Afrîgîler)", "Khwarazm (Afrighids)", "diger", "#a8a48c"),
}.items():
    assert k not in st, k
    st[k] = {"tr": tr, "en": en, "group": g, "color": col}

END = max(s[1] for c in d["cities"] for s in c.get("spans", []))
by = {c.get("id"): c for c in d["cities"]}


def spans(seq):
    """[(başlangıç, devlet), ...] → [[a, b, devlet], ...]; son dilim END'e uzar."""
    return [[a, seq[i + 1][0] if i + 1 < len(seq) else END, s] for i, (a, s) in enumerate(seq)]


NEW = [
    ("kumul", "Kumul (Hami)", 42.83, 93.51, [(552, "gokturk"), (630, "tang"), (781, "tibet"), (866, "uygur"), (1368, "mogolistan-han"),
                                             (1514, "yarkent"), (1678, "cungar"), (1697, "qing"), (1912, "cin-cum")], ["cin--ulke"]),
    ("kancou", "Kan-chou (Gansu koridoru)", 38.93, 100.45, [(550, "kuzey-cin"), (581, "sui"), (618, "tang"), (764, "tibet"), (848, "tang"),
                                                            (894, "kancou"), (1028, "bati-xia"), (1227, "mogol-imp"), (1368, "ming"),
                                                            (1644, "qing"), (1912, "cin-cum")], ["cin--ulke"]),
    ("cangan", "Çang-an (Şian)", 34.27, 108.95, [(550, "kuzey-cin"), (581, "sui"), (618, "tang"), (907, "kuzey-cin"), (960, "song"), (1127, "jin"),
                                                 (1234, "mogol-imp"), (1368, "ming"), (1644, "qing"), (1912, "cin-cum")], ["cin--ulke"]),
    ("yinsan", "Yinşan ve Ordos (İç Moğolistan)", 40.84, 111.75, [(550, "juan-juan"), (552, "gokturk"), (630, "tang"), (682, "gokturk"), (744, "uygur-kag"),
                                                                 (840, "kuzey-cin"), (916, "kitan"), (1125, "jin"), (1215, "mogol-imp"),
                                                                 (1368, "mogolistan"), (1635, "qing"), (1912, "cin-cum")], ["cin--ulke"]),
    ("pekin", "Pekin", 39.90, 116.40, [(550, "kuzey-cin"), (581, "sui"), (618, "tang"), (907, "kuzey-cin"), (938, "kitan"), (1125, "jin"),
                                       (1215, "mogol-imp"), (1368, "ming"), (1644, "qing"), (1912, "cin-cum")], ["cin--ulke"]),
    ("lhasa", "Lhasa (Tibet)", 29.65, 91.10, [(550, "tibet"), (1240, "mogol-imp"), (1354, "tibet"), (1720, "qing"), (1912, "tibet")], ["tibet"]),
    ("hoten", "Hoten", 37.11, 79.93, [(550, "hoten-krl"), (648, "tang"), (790, "tibet"), (851, "hoten-krl"), (1006, "karahanli"), (1211, "karahitay"),
                                      (1218, "cagatay"), (1347, "mogolistan-han"), (1514, "yarkent"), (1678, "cungar"), (1759, "qing"),
                                      (1865, "yakub"), (1877, "qing"), (1912, "cin-cum")], ["hoten"]),
    ("gulca", "Gulca (İli vadisi)", 43.91, 81.28, [(552, "bati-gokturk"), (659, "tang"), (704, "turgis"), (766, "karluk"), (840, "karahanli"),
                                                   (1134, "karahitay"), (1218, "cagatay"), (1347, "mogolistan-han"), (1680, "cungar"), (1758, "qing"),
                                                   (1871, "rusya"), (1881, "qing"), (1912, "cin-cum")], ["cin--ulke"]),
    ("bati-mogol", "Batı Moğolistan (Kobdo)", 47.00, 96.00, [(552, "gokturk"), (630, "tang"), (682, "gokturk"), (744, "uygur-kag"), (840, "kirgiz"),
                                                            (920, "mogolistan"), (1206, "mogol-imp"), (1368, "mogolistan"), (1634, "cungar"),
                                                            (1757, "qing"), (1911, "mogolistan")], []),
    ("hangcou", "Hangçou (Güney Çin)", 30.27, 120.15, [(550, "guney-cin"), (589, "sui"), (618, "tang"), (907, "guney-cin"), (960, "song"),
                                                      (1279, "mogol-imp"), (1368, "ming"), (1644, "qing"), (1912, "cin-cum")], ["cin--ulke"]),
    ("cengdu", "Çengdu (Siçuan)", 30.67, 104.07, [(550, "kuzey-cin"), (581, "sui"), (618, "tang"), (907, "guney-cin"), (965, "song"),
                                                 (1271, "mogol-imp"), (1368, "ming"), (1644, "qing"), (1912, "cin-cum")], ["cin--ulke"]),
]
# Lhasa ve Çin hücreleri Hindistan'a ve Güneydoğu Asya'ya taşmasın diye boş (void) hücreler
VOID = [("v-bengal", 24.5, 89.0), ("v-birmanya", 21.0, 96.0), ("v-hindicin", 17.0, 104.0)]
# Batı Moğolistan'daki boş hücre gerçek bir bölgeyle değiştirilir
assert by["v-mogol"].get("void")
d["cities"] = [c for c in d["cities"] if c.get("id") != "v-mogol"]
for cid, tr, lat, lon, seq, src in NEW:
    assert cid not in by, cid
    d["cities"].append({"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": spans(seq), "src": src, "yaklasik": True})
for cid, lat, lon in VOID:
    assert cid not in by, cid
    d["cities"].append({"id": cid, "void": True, "lat": lat, "lon": lon})
# Hârizm 712'deki Kuteybe fethine kadar Sâsânî değil, yerli Afrîgî hânedanının elindeydi
g = by["gurgenc"]
assert g["spans"][0] == [550, 712, "sasani"], g["spans"][0]
g["spans"][0][2] = "afrigi"

for c in d["cities"]:
    sp = c.get("spans", [])
    for a, b, s in sp:
        assert s in st, (c["id"], s); assert a < b, (c["id"], a, b)
    for x, y in zip(sp, sp[1:]):
        assert x[1] <= y[0], (c["id"], x, y)
d["meta"]["method"] += " Çin, Tibet ve Moğolistan: Kumul, Kan-chou, Çang-an, Yinşan, Pekin, Lhasa, Hoten, Gulca ve Batı Moğolistan noktaları (Sui, T'ang, Song, Cin, Tangut, Ming, Çing hanedanları)."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("tamam")
