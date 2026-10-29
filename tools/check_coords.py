"""Koordinat tutarlılık kontrolü (EKSIKLER §4): kaydın lat/lon değeri 'country' alanındaki ülkenin kaba sınır kutusunun
dışındaysa raporlar. Kutular bilerek geniştir; yalnızca bariz hataları (enlem/boylam karışması, yanlış ülke) yakalar.
Kullanım: python -I -X utf8 tools/check_coords.py"""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
# (min_lat, max_lat, min_lon, max_lon)
BOX = {
    "Türkiye": (35.5, 42.5, 25.5, 45.0), "Yunanistan": (34.5, 41.9, 19.2, 29.8), "İran": (25.0, 40.0, 44.0, 63.5),
    "Irak": (29.0, 37.5, 38.7, 48.8), "Suriye": (32.2, 37.4, 35.6, 42.5), "Mısır": (22.0, 31.8, 24.5, 35.0),
    "İsrail": (29.4, 33.4, 34.2, 35.9), "Filistin": (31.2, 32.6, 34.2, 35.6), "Lübnan": (33.0, 34.8, 35.0, 36.7),
    "Bulgaristan": (41.2, 44.3, 22.3, 28.7), "Romanya": (43.6, 48.3, 20.2, 30.0), "Macaristan": (45.7, 48.6, 16.1, 22.9),
    "Sırbistan": (42.2, 46.2, 18.8, 23.1), "Ukrayna": (44.3, 52.4, 22.1, 40.3), "Rusya": (41.0, 70.0, 27.0, 180.0),
    "Ermenistan": (38.8, 41.4, 43.4, 46.7), "Azerbaycan": (38.3, 42.0, 44.7, 50.6), "Gürcistan": (41.0, 43.6, 40.0, 46.8),
    "Afganistan": (29.3, 38.5, 60.4, 75.0), "Pakistan": (23.6, 37.1, 60.8, 77.9), "Hindistan": (6.5, 35.6, 68.0, 97.5),
    "Özbekistan": (37.1, 45.6, 55.9, 73.2), "Türkmenistan": (35.1, 42.8, 52.4, 66.7), "Kazakistan": (40.5, 55.5, 46.5, 87.4),
    "Kırgızistan": (39.1, 43.3, 69.2, 80.3), "Suudi Arabistan": (16.3, 32.2, 34.5, 55.7), "Yemen": (12.1, 19.0, 41.8, 54.6),
    "Libya": (19.5, 33.2, 9.3, 25.2), "Tunus": (30.2, 37.6, 7.5, 11.6), "Cezayir": (18.9, 37.1, -8.7, 12.0),
    "Arnavutluk": (39.6, 42.7, 19.2, 21.1), "Karadağ": (41.8, 43.6, 18.4, 20.4), "Kosova": (41.8, 43.3, 20.0, 21.8),
    "Kuzey Makedonya": (40.8, 42.4, 20.4, 23.1), "Bosna-Hersek": (42.5, 45.3, 15.7, 19.7), "Hırvatistan": (42.3, 46.6, 13.4, 19.5),
    "Moldova": (45.4, 48.5, 26.6, 30.2), "Kıbrıs": (34.5, 35.8, 32.2, 34.7), "Avusturya": (46.3, 49.1, 9.5, 17.2),
    "Slovakya": (47.7, 49.7, 16.8, 22.6), "İtalya": (36.6, 47.1, 6.6, 18.6), "Malta": (35.7, 36.1, 14.1, 14.6),
    "Moğolistan": (41.5, 52.2, 87.7, 120.0), "Çin": (18.0, 53.6, 73.5, 135.1), "Tacikistan": (36.6, 41.1, 67.3, 75.2),
    "Fransa": (41.3, 51.1, -5.2, 9.6),
}


def main():
    names = [n for n, _ in __import__("ast").literal_eval(
        re.search(r"BATCHES = (\[.*?\])\n", (root / "tools" / "build_demo.py").read_text(encoding="utf-8"), re.S).group(1))]
    bad = 0
    for name in names:
        for b in json.loads((root / "data" / name).read_text(encoding="utf-8"))["battles"]:
            boxes = [BOX[c.strip()] for c in re.split(r"[/,]", b["country"]) if c.strip() in BOX]
            if not boxes:
                continue
            if not any(a - 0.3 <= b["lat"] <= z + 0.3 and w - 0.3 <= b["lon"] <= e + 0.3 for a, z, w, e in boxes):
                bad += 1
                print(f"{name} | {b['name_tr']} | {b['country']} | {b['lat']}, {b['lon']} | {b['loc']}")
    print(bad, "şüpheli koordinat")


if __name__ == "__main__":
    main()
