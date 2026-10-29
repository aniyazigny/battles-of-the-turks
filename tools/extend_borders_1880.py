"""data/sinirlar.json'u 1840'tan 1880'e uzatır. Bir kez çalıştırılmak üzere yazıldı; tarihler yaklaşıktır.
- Mehmed Ali Paşa'nın Suriye'si ve Girit 1840'ta Osmanlı'ya döndü (Akkâ, Filistin, Kavalalı Mehmed Ali Paşa maddeleri).
- Eflak ve Boğdan 1858'de birleşti, Bükreş Romanya'nın başşehri oldu (Eflak maddesi); 1878'de bağımsız.
- Sırbistan: Belgrad ve diğer kalelerdeki Osmanlı garnizonları 1867'de çekildi (Sırbistan maddesi); Niş 1878'de Sırbistan'a.
- Berlin Antlaşması (1878): Bulgaristan Prensliği (Tırnova, Sofya); Bosna-Hersek Avusturya-Macaristan işgaline girdi (Bosna-Hersek maddesi);
  Kars ve Ardahan (Ani noktası) Rusya'ya (Elviye-i Selâse maddesi); Kıbrıs İngiltere'nin idaresine (Berlin Antlaşması maddesi).
- Lahsâ: 1818'de Osmanlı (Lahsâ maddesi). Suûdîlerin aradaki dönemi yılı belirsiz olduğundan işlenmedi."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
OLD, END = 1840, 1880
O, RU = "osmanli", "rusya"
st = d["states"]
st.setdefault("romanya", {"tr": "Romanya", "en": "Romania", "group": "diger", "color": "#b9a98e"})
st.setdefault("bulgaristan", {"tr": "Bulgaristan Prensliği", "en": "Principality of Bulgaria", "group": "diger", "color": "#a9b98e"})
st.setdefault("ingiltere", {"tr": "İngiltere", "en": "Britain", "group": "diger", "color": "#c4a0a0"})
for c in d["cities"]:
    if c.get("void"): continue
    for s in c.get("spans", []):
        if s[1] == OLD: s[1] = END


def city(cid):
    return next(x for x in d["cities"] if x.get("id") == cid)


def setspan(cid, tail_from, items):
    c = city(cid)
    keep = [[a, min(b, tail_from), s] for a, b, s in c["spans"] if a < tail_from]
    c["spans"] = keep + [list(x) for x in items]
    c["yaklasik"] = True


for cid in ("dimask", "trablus", "sur", "kudus", "askalan", "antakya", "halep"):
    setspan(cid, 1832, [[1832, 1840, "kavalali"], [1840, END, O]])
setspan("tarsus", 1833, [[1833, 1840, "kavalali"], [1840, END, O]])
setspan("girit", 1830, [[1830, 1840, "kavalali"], [1840, END, O]])
setspan("bukres", 1310, [[1310, 1858, "eflak"], [1858, END, "romanya"]])
setspan("yas", 1359, [[1359, 1858, "bogdan"], [1858, END, "romanya"]])
setspan("belgrad", 1813, [[1813, 1867, O], [1867, END, "sirbistan"]])
setspan("nis", 1386, [[1386, 1878, O], [1878, END, "sirbistan"]])
for cid in ("tirnova", "sofya"):
    first = city(cid)["spans"][-1][0]
    setspan(cid, first, [[first, 1878, O], [1878, END, "bulgaristan"]])
setspan("sarajevo", 1463, [[1463, 1878, O], [1878, END, "habsburg"]])
setspan("ani", 1514, [[1514, 1878, O], [1878, END, RU]])
setspan("kibris", 1570, [[1570, 1878, O], [1878, END, "ingiltere"]])
setspan("ahsa", 1796, [[1796, 1818, "suud"], [1818, END, O]])

for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in st, (c["id"], s); assert a < b, (c["id"], a, b)
d["meta"]["method"] += " 1840–1880: Suriye ve Girit 1840'ta Osmanlı'ya döndü; Romanya 1858; Belgrad 1867 Sırbistan; Berlin 1878: Bulgaristan, Bosna (Avusturya), Kars (Rusya), Kıbrıs (İngiltere), Niş (Sırbistan)."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(st), "devlet")
