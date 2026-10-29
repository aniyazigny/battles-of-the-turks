"""Bütün partiler için şema ve tutarlılık denetimi. Kullanım: python -I -X utf8 tools/validate.py
Denetlenenler: zorunlu alanlar; tarih biçimi; kategori/sonuç/statü/tür değerleri; 'ic' kayıtlarda sonuç C;
W/L kayıtlarda kazanan tarafın devletle tutarlılığı (L iken side_a devletin kendisi olmamalı, W iken side_b olmamalı);
aynı parti içinde ad tekrarı; kaynak listesinin boş olmaması ve anahtar biçimi."""
import ast
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
REQ = ["id", "name_tr", "name_en", "date", "war", "place", "lat", "lon", "loc", "country", "side_a", "side_b", "category", "result",
       "status", "sources", "verify", "state", "home_batch"]
CAT = {"dis", "ic", "turk_arasi"}
RES = {"W", "L", "D", "C"}
STA = {"kesin", "borderline", "ihtilafli"}
LOC = {"known", "approx", "region"}
SRC = re.compile(r"^(TDVIA:[a-z0-9\-]+|AKD:[a-z0-9\-]+|ROM|WP(:\S+)?)$")


def main():
    names = [n for n, _ in ast.literal_eval(re.search(r"BATCHES = (\[.*?\])\n", (root / "tools" / "build_demo.py").read_text(encoding="utf-8"), re.S).group(1))]
    errs = []
    for name in names:
        seen = set()
        for b in json.loads((root / "data" / name).read_text(encoding="utf-8"))["battles"]:
            tag = f"{name} | {b.get('name_tr')}"
            for k in REQ:
                if k not in b:
                    errs.append(f"{tag}: alan yok: {k}")
            if not re.match(r"^(c\. )?\d{3,4}", str(b.get("date", ""))):
                errs.append(f"{tag}: tarih biçimi: {b.get('date')}")
            if b.get("category") not in CAT: errs.append(f"{tag}: kategori {b.get('category')}")
            if b.get("result") not in RES: errs.append(f"{tag}: sonuç {b.get('result')}")
            if b.get("status") not in STA: errs.append(f"{tag}: statü {b.get('status')}")
            if b.get("loc") not in LOC: errs.append(f"{tag}: loc {b.get('loc')}")
            if b.get("type", "land") not in ("land", "sea"): errs.append(f"{tag}: tür {b.get('type')}")
            if b.get("category") == "ic" and b.get("result") != "C": errs.append(f"{tag}: iç savaş ama sonuç {b.get('result')}")
            if b.get("category") != "ic" and b.get("result") == "C": errs.append(f"{tag}: sonuç C ama kategori {b.get('category')}")
            st = b.get("state", "")
            if b.get("result") == "L" and b.get("side_a") == st: errs.append(f"{tag}: yenilgi ama kazanan taraf devletin kendisi")
            if b.get("result") == "W" and b.get("side_b") == st: errs.append(f"{tag}: galibiyet ama kaybeden taraf devletin kendisi")
            if not b.get("sources"): errs.append(f"{tag}: kaynak yok")
            for s in b.get("sources", []):
                if not SRC.match(s): errs.append(f"{tag}: kaynak anahtarı {s}")
            if b.get("name_tr") in seen: errs.append(f"{tag}: ad tekrarı")
            seen.add(b.get("name_tr"))
            if not (-90 <= b.get("lat", 0) <= 90 and -180 <= b.get("lon", 0) <= 180): errs.append(f"{tag}: koordinat aralığı")
    for e in errs:
        print(e)
    print(len(errs), "sorun")


if __name__ == "__main__":
    main()
