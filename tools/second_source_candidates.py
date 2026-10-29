"""Tek TDVİA maddesine dayanan kayıtlar için ikinci madde adaylarını bulur (EKSIKLER §1).
Her kaydın yer adının ilk kelimesi TDVİA başlıklarında aranır; ilk sonuçlar raw/'a indirilir; kaydın yılını ve yer adını
birlikte geçiren cümleler aday olarak yazılır. Adaylar elle doğrulanır; bu araç veriye dokunmaz.
Kullanım: python -I -X utf8 tools/second_source_candidates.py <parti-dosyası.json> ... > rapor.txt"""
import html
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root / "tools"))
from tdvia_text import sentences  # noqa: E402

UA = {"User-Agent": "Mozilla/5.0"}
STOP = {"ve", "ile", "yakını", "yöresi", "önleri", "kalesi", "ovası", "nehri", "adası", "ırmağı", "boğazı", "körfezi", "dağı", "civarı"}


def search(q):
    url = "https://islamansiklopedisi.org.tr/arama/?" + urllib.parse.urlencode({"q": q, "p": "m"})
    s = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read().decode("utf-8", "replace")
    return [slug for slug, _t, _d in re.findall(r'<a href=/([^ >]+)>(.*?)</a><br /><span class="desc">(.*?)</span>', s)]


def fetch(slug):
    f = root / "raw" / (slug + ".txt")
    if f.exists():
        return f.read_text(encoding="utf-8")
    s = urllib.request.urlopen(urllib.request.Request("https://islamansiklopedisi.org.tr/" + slug, headers=UA), timeout=30).read().decode("utf-8", "replace")
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S)
    t = re.sub(r"<(br|p|div|h\d|li)[^>]*>", "\n", t)
    t = html.unescape(re.sub(r"<[^>]+>", "", t))
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    f.write_text(t, encoding="utf-8")
    return t


def terms(b):
    words = re.findall(r"[^\W\d_][\w‘’'-]+", re.sub(r"\(.*?\)", " ", b["place"] + " " + b["name_tr"]))
    out = []
    for w in words:
        w = w.strip("‘’'")
        if len(w) > 3 and w.lower() not in STOP and w not in out:
            out.append(w)
    return out[:3]


def main():
    for name in sys.argv[1:]:
        d = json.loads((root / "data" / name).read_text(encoding="utf-8"))
        for b in d["battles"]:
            if b["verify"].get("tdvia2"):
                continue
            y = re.match(r"\D*(\d{3,4})", b["date"])
            if not y:
                continue
            y = y.group(1)
            have = {s[6:] for s in b["sources"] if s.startswith("TDVIA:")}
            ts = terms(b)
            slugs = []
            for t in ts[:2]:
                try:
                    slugs += [s for s in search(t)[:3] if s not in slugs]
                except Exception as e:  # ağ hatası: sonraki terime geç
                    print("  ! arama", t, e)
            hits = []
            for sl in slugs:
                if sl in have:
                    continue
                try:
                    txt = fetch(sl)
                except Exception as e:
                    print("  ! indirme", sl, e); continue
                for x in sentences(txt):
                    if y in x and any(t[:5] in x for t in ts):
                        hits.append((sl, x[:260]))
            print(f"## {name} | {b['name_tr']} | {b['date']} | {sorted(have)}")
            for sl, x in hits[:4]:
                print(f"   {sl}: {x}")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
