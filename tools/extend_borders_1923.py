"""data/sinirlar.json'u 1919'dan 1923'e uzatır (Millî Mücadele). Bir kez çalıştırılmak üzere yazıldı; tarihler yaklaşıktır.
- Ankara'da TBMM 23 Nisan 1920'de açıldı; işgal dışındaki Anadolu noktaları 1920'den itibaren TBMM Hükümeti rengiyle gösterilir.
  İstanbul ve Gelibolu saltanatın kaldırıldığı 1922'ye kadar Osmanlı, sonra TBMM (Millî Mücadele maddesi).
- Yunan işgali: İzmir ve Manisa 1919–1922; Bursa ve Balıkesir 1920–1922; Kütahya, Eskişehir ve Bilecik 1921–1922 (İzmir, Manisa, Bursa,
  Balıkesir Kongreleri, Kütahya, Eskişehir, Millî Mücadele maddeleri); Edirne 1920–1922 (Batı Trakya işgali ve Mudanya; Millî Mücadele maddesi).
- Fransız işgali: Maraş 1919–1920, Urfa 1919–1920 (Kahramanmaraş, Şanlıurfa maddeleri); Adana (Tarsus noktası) 1919–1922 (Adana maddesi);
  Antakya 1919'dan sonra Fransız idaresinde (Millî Mücadele maddesi: Ankara Antlaşması).
- Kars (Ani noktası) 1919'da Ermenilere verildi, 30 Ekim 1920'de geri alındı (Kars maddesi).
- Musul 1918 sonunda İngiliz işgaline girdi (Musul maddesi); Medine 1919'da teslim edildi (Şerîf Hüseyin maddesi); Ahvaz Basra ile birlikte İngiliz.
- Lahsâ 8 Temmuz 1913'te İbn Suûd'un eline geçti (Lahsâ maddesi) — EKSIKLER'deki harita hatasının düzeltmesi."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
OLD, END = 1919, 1923
O, T = "osmanli", "tbmm"
st = d["states"]
st.setdefault(T, {"tr": "TBMM Hükümeti (Ankara)", "en": "Government of the Grand National Assembly", "group": "turk", "color": "#2f9e6e"})
for c in d["cities"]:
    if c.get("void"): continue
    for s in c.get("spans", []):
        if s[1] == OLD: s[1] = END


def city(cid):
    return next(x for x in d["cities"] if x.get("id") == cid)


def tail(cid, items):
    c = city(cid)
    a, b, s = c["spans"][-1]
    assert b == END, (cid, c["spans"][-1])
    c["spans"] = c["spans"][:-1] + [[a, items[0][0], s]] + [list(x) for x in items]
    c["yaklasik"] = True


def occ(cid, start, stop, who):
    tail(cid, [[start, stop, who], [stop, END, T]])


# Lahsâ 1913: Osmanlı dilimini 1913'te kes, sonrasını Suûdî yap
ah = city("ahsa")
ah["spans"] = [x for x in ah["spans"] if x[0] < 1913]
ah["spans"][-1][1] = 1913
ah["spans"].append([1913, END, "suud"])

for cid in ("izmir", "manisa"):
    occ(cid, 1919, 1922, "yunanistan")
for cid in ("bursa", "balikesir"):
    tail(cid, [[1920, 1922, "yunanistan"], [1922, END, T]])
for cid in ("kutahya", "eskisehir", "bilecik"):
    tail(cid, [[1920, 1921, T], [1921, 1922, "yunanistan"], [1922, END, T]])
tail("edirne", [[1920, 1922, "yunanistan"], [1922, END, T]])
for cid in ("istanbul", "gelibolu"):
    tail(cid, [[1922, END, T]])
for cid in ("maras", "urfa"):
    tail(cid, [[1919, 1920, "fransa"], [1920, END, T]])
tail("tarsus", [[1919, 1922, "fransa"], [1922, END, T]])
tail("antakya", [[1919, END, "fransa"]])
tail("ani", [[1919, 1920, "ermenistan"], [1920, END, T]])
tail("musul", [[1919, END, "ingiltere"]])
tail("ahvaz", [[1914, END, "ingiltere"]])
tail("medine", [[1919, END, "hicaz"]])
for c in d["cities"]:
    if c.get("void") or not c.get("spans"): continue
    a, b, s = c["spans"][-1]
    if s == O and b == END:
        tail(c["id"], [[1920, END, T]])

for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in st, (c["id"], s); assert a < b, (c["id"], a, b)
    assert not (c.get("spans") and c["spans"][-1][2] == O and c["spans"][-1][1] == END), c["id"]
d["meta"]["method"] += " 1919–1923: Millî Mücadele — TBMM Hükümeti 1920; Yunan, Fransız ve Ermeni işgalleri ve kurtuluşlar; Lahsâ 1913 Suûdî."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(st), "devlet")
