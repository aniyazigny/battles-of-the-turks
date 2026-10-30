"""Her savaşın yerinin, o yıl haritada en yakın şehrin sahibiyle uyumlu olup olmadığını denetler (sınır hatalarını bulmak için).
Kullanım: python -I tools/check_battle_owners.py   (SAHİPSİZ = o yıl sahibi olmayan bölge; diğerleri elle gözden geçirilir)"""
import json, glob, math, sys, re, collections
sys.stdout.reconfigure(encoding="utf-8")
d = json.load(open("data/sinirlar.json", encoding="utf-8")); st = d["states"]
cities = d["cities"]
def norm(s): return re.sub(r"[^a-zçğıöşüâîû ]", " ", s.lower().replace("İ","i").replace("I","ı"))
B = []
for f in glob.glob("data/*.json"):
    j = json.load(open(f, encoding="utf-8"))
    if "battles" in j: B += [(f[5:-5], b) for b in j["battles"]]
bad = collections.Counter(); out = []
for f, b in B:
    y = int(re.search(r"\d{3,4}", b["date"]).group())
    lat, lon = b["lat"], b["lon"]
    c = min(cities, key=lambda c: (c["lat"]-lat)**2 + ((c["lon"]-lon)*math.cos(math.radians(lat)))**2)
    if c.get("void"): continue
    o = next((s for a, e, s in c["spans"] if a <= y < e), None)
    if o is None:
        out.append(("SAHİPSİZ", y, b["name_tr"], c["id"])); continue
    words = [w for w in norm(st[o]["tr"]).split() if len(w) > 3][:2]
    txt = norm(" ".join([b["side_a"], b["side_b"], b["state"], b.get("opp_state",""), b["war"], b.get("note","")]))
    stem = lambda w: w[:5]
    if not any(stem(w) in txt for w in words):
        out.append((st[o]["tr"], y, b["name_tr"], c["id"])); bad[st[o]["tr"]] += 1
print(len(out), "uyuşmazlık /", len(B))
for r in sorted(out, key=lambda r: r[1]): print(r)
