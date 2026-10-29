"""data/sinirlar.json: İran, Irak ve Doğu Anadolu 1405–1510 düzeltmesi. Önceki tabloda İran 1501'e kadar Timurlu görünüyordu.
Tarihler TDVİA maddelerinden (karakoyunlular, cihan-sah, akkoyunlular, uzun-hasan, timurlular):
- Kara Yûsuf Serdrûd'da (Nisan 1408) Timurluları yendi → Tebriz ve Arrân Karakoyunlu.
- Cihan Şah Sultâniye ve Kazvin'i 1447'de, Rey, İsfahan ve Fars'ı 1452'de, Kirman'ı 1452–53'te aldı.
- Uzun Hasan 1467'de Cihan Şah'ı, 1469'da Ebû Said'i yendi; Kirman 1469, Bağdat 1470 Akkoyunlu.
- 1500 paylaşımında Irakeyn, Kirman ve Fars Murad'da kaldı; Murad 1503'te Hemedan'da Safevîlere yenildi.
- Şeybânî Han Herat'ı Mayıs 1507'de aldı; Şah İsmâil 1510'da Şeybânî'yi öldürdü → Horasan 1507–1510 Özbek.
- Karakoyunlu İskender Van'ı 1425'te aldı; Ahlat, Van, Revan ve Ani yöresi 1467'ye kadar Karakoyunlu.
Bir kez çalıştırılmak üzere yazıldı; tarihler yaklaşıktır."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
K, A, T, S, CL = "karakoyunlu", "akkoyunlu", "timur", "safevi", "celayir"


def setwin(cid, a, b, items):
    """[a, b) aralığını items ile değiştirir; dışındaki dilimlere dokunmaz, komşu aynı devletleri birleştirir."""
    c = next(x for x in d["cities"] if x.get("id") == cid)
    out = []
    for x, y, s in c["spans"]:
        if x < a: out.append([x, min(y, a), s])
        if y > b: out.append([max(x, b), y, s])
    out += [list(i) for i in items]
    out.sort()
    merged = []
    for x, y, s in out:
        if x >= y: continue
        if merged and merged[-1][2] == s and merged[-1][1] == x: merged[-1][1] = y
        else: merged.append([x, y, s])
    c["spans"] = merged
    c["yaklasik"] = True


# Azerbaycan ve Arrân
setwin("tebriz", 1393, 1501, [[1393, 1408, T], [1408, 1468, K], [1468, 1501, A]])
setwin("gence", 1370, 1501, [[1370, 1408, T], [1408, 1468, K], [1468, 1501, A]])
# Irâk-ı Arab: Celâyirli Ahmed Timur'dan sonra Bağdat'a döndü (1405–1410)
for cid in ("bagdat", "hille", "basra", "ahvaz"):
    setwin(cid, 1393, 1508, [[1393, 1405, T], [1405, 1410, CL], [1410, 1470, K], [1470, 1508, A]])
setwin("musul", 1393, 1508, [[1393, 1410, T], [1410, 1470, K], [1470, 1508, A]])
# Irâk-ı Acem, Fars, Kirman
for cid in ("alamut", "hemedan"):
    setwin(cid, 1370, 1510, [[1370, 1447, T], [1447, 1469, K], [1469, 1503, A], [1503, 1510, S]])
for cid in ("rey", "isfahan", "siraz"):
    setwin(cid, 1370, 1510, [[1370, 1452, T], [1452, 1469, K], [1469, 1503, A], [1503, 1510, S]])
setwin("kirman", 1370, 1510, [[1370, 1453, T], [1453, 1469, K], [1469, 1503, A], [1503, 1510, S]])
# Horasan: Şeybânî 1507–1510
for cid in ("herat", "merv", "serahs", "nisabur", "curcan"):
    setwin(cid, 1500, 1511, [[1500, 1507, T], [1507, 1510, "ozbek"], [1510, 1511, S]])
# Van gölü ve Aras yöresi: 1467'ye kadar Karakoyunlu
for cid in ("ahlat", "malazgirt", "ani"):
    setwin(cid, 1410, 1501, [[1410, 1468, K], [1468, 1501, A]])
ahlat = next(x for x in d["cities"] if x["id"] == "ahlat")["spans"]
ani = next(x for x in d["cities"] if x["id"] == "ani")["spans"]
setwin("van", 1000, 1501, [s for s in ahlat if s[1] <= 1335] + [[1335, 1393, K], [1393, 1410, T], [1410, 1468, K], [1468, 1501, A]])
setwin("revan", 1000, 1501, [s for s in ani if s[1] <= 1335] + [[1335, 1393, K], [1393, 1410, T], [1410, 1468, K], [1468, 1501, A]])
# Mardin: Karakoyunlu 1409, Akkoyunlu 1431
setwin("mardin", 1409, 1501, [[1409, 1431, K], [1431, 1501, A]])

for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in d["states"], (c["id"], s); assert a < b, (c["id"], a, b)
d["meta"]["method"] += " İran ve Irak 1405–1510: Karakoyunlu (1408–1469) ve Akkoyunlu (1468–1503) yayılması, Horasan'da Şeybânî dönemi (1507–1510) TDVİA maddelerine göre işlendi."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(d["states"]), "devlet")
