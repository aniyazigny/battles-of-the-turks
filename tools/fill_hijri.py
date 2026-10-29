"""Hicrî tarihleri kayıtların kendi TDVİA maddelerinden çıkarır ve data/hicri.json'a yazar (EKSIKLER §4).
Hesaplama yapılmaz: yalnızca maddede "<hicrî tarih> / <miladî tarih>" biçiminde yan yana yazılmış ve miladî kısmı kaydın
tarihiyle uyuşan ifadeler alınır. Örnek: "27 Şâban 460 / 1 Temmuz 1068". build_demo.py bu dosyayı kaydın boş 'hijri' alanına işler.
Anahtar: "<home_batch>|<name_tr>". raw/ yoksa (telif nedeniyle repoda değil) mevcut hicri.json korunur."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HM = ["Muharrem", "Safer", "Rebîülevvel", "Rebîülâhir", "Cemâziyelevvel", "Cemâziyelâhir", "Receb", "Şâban", "Ramazan", "Şevval",
      "Zilkade", "Zilhicce"]
GM = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
PAT = re.compile(r"(?:(\d{1,2}) )?(?:(" + "|".join(HM) + r") )?(\d{2,4}) ?/ ?(?:(\d{1,2}) )?(?:(" + "|".join(GM) + r") )?(\d{3,4})(?![\d-])")
BATCHES = [n for n, _ in __import__("ast").literal_eval(
    re.search(r"BATCHES = (\[.*?\])\n", (root / "tools" / "build_demo.py").read_text(encoding="utf-8"), re.S).group(1))]


def parse_date(s):
    m = re.match(r"(\d{3,4})(?:-(\d{2}))?(?:-(\d{2}))?", s)
    return (int(m.group(1)), int(m.group(2)) if m.group(2) else None, int(m.group(3)) if m.group(3) else None) if m else None


def best(text, y, mo, da):
    """Kaydın tarihiyle uyuşan en ayrıntılı hicrî ifadeyi döndürür. Çıktı kaydın kesinliğini aşmaz:
    yalnız yılı bilinen kayda yalnız hicrî yıl, ayı bilinene ay+yıl, günü bilinene (gün de uyuşursa) tam tarih yazılır."""
    out = []
    for m in PAT.finditer(text):
        hd, hm, hy, gd, gm, gy = m.groups()
        if int(gy) != y or not (1 <= int(hy) <= 1345) or abs((y - 622) * 33 / 32 - int(hy)) > 3:
            continue
        gmi = GM.index(gm) + 1 if gm else None
        if mo is None:
            out.append((1, hy))
            continue
        if gmi != mo or not hm:
            continue
        if da and gd and int(gd) == da and hd:
            out.append((3, f"{hd} {hm} {hy}"))
        elif not da or not gd:
            out.append((2, f"{hm} {hy}"))
    return max(out) if out else None


def main():
    path = root / "data" / "hicri.json"
    old = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    if not (root / "raw").exists():
        print("raw/ yok; hicri.json korunuyor"); return
    res, n = dict(old), 0
    for name in BATCHES:
        d = json.loads((root / "data" / name).read_text(encoding="utf-8"))
        for b in d["battles"]:
            key = f"{b['home_batch']}|{b['name_tr']}"
            if b.get("hijri"):
                continue
            pd = parse_date(b["date"])
            if not pd or pd[0] > 1925:
                continue
            cands = []
            for s in b["sources"]:
                if not s.startswith("TDVIA:"):
                    continue
                f = root / "raw" / (s[6:] + ".txt")
                if f.exists():
                    r = best(f.read_text(encoding="utf-8"), *pd)
                    if r:
                        cands.append((r[0], r[1], s[6:]))
            if cands:
                sc, h, src = max(cands)
                res[key] = {"hijri": h, "source": "TDVIA:" + src}
                n += 1
    path.write_text(json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    print(n, "kayda hicrî tarih bulundu;", len(res), "toplam")


if __name__ == "__main__":
    main()
