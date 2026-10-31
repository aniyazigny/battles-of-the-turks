"""data/osmanli-1912-1913.json dosyasını üretir (Parti 18: Balkan Savaşları, 1912–1913)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "osmanli-1912-1913"
O = "Osmanlı Devleti"
W1 = "Birinci Balkan Savaşı (1912–1913)"
W2 = "İkinci Balkan Savaşı (1913)"
BG, SR, GR, KD = "Bulgaristan", "Sırbistan", "Yunanistan", "Karadağ"
KAB = "Kölemen Abdullah Paşa"

# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür)
R = [
("Limni (1912)", "Greek occupation of Lemnos (1912)", "1912-10-21", W1, "Limni adası", 39.90, 25.20, "region", "Yunanistan",
 GR, O, "", "", "dis", "L", "kesin",
 ["TDVIA:limni"], "", "", "", "land"),
("Kumanova (1912)", "Battle of Kumanovo", "1912-10-23", W1, "Kumanova", 42.13, 21.71, "known", "Kuzey Makedonya",
 SR, O, "", "Veliaht Prens Aleksandar", "dis", "L", "kesin",
 ["TDVIA:kumanova", "TDVIA:balkan-savasi", "TDVIA:uskup"], "",
 "23–24 Ekim'de Garp Ordusu'nun nizam ve redif askerleri üç Sırp ordu birliğine yenildi; Üsküp aynı günlerde Sırplar'ın eline geçti. Muharebe Makedonya'nın siyasî kaderini belirledi.",
 "On 23–24 October the regular and reserve troops of the Western Army were beaten by three Serbian armies; Skopje fell to the Serbs in the same days. The battle decided Macedonia's political fate.", "land"),
("Kırkkilise (1912)", "Battle of Kirk Kilisse", "1912-10-24", W1, "Kırkkilise (Kırklareli)", 41.735, 27.225, "known", "Türkiye",
 BG, O, KAB, "", "dis", "L", "kesin",
 ["TDVIA:kirklareli", "TDVIA:abdullah-pasa-kolemen", "TDVIA:balkan-savasi"], "",
 "Şark Ordusu kumandanı Kölemen Abdullah Paşa'nın savunduğu şehir 24 Ekim'de Bulgarlar'ca işgal edildi; Balkan Savaşı maddesi Şark Ordusu'nun kendisinden üç kat kalabalık Bulgar ordusuna 23 Ekim'de yenildiğini yazar.",
 "The town, defended by Eastern Army commander Kölemen Abdullah Pasha, was occupied by the Bulgarians on 24 October; the Balkan War article says the Eastern Army was beaten by a Bulgarian army three times its size on 23 October.", "land"),
("Selânik'in teslimi (1912)", "Surrender of Thessaloniki (1912)", "1912-10-26", W1, "Selânik", 40.64, 22.94, "known", "Yunanistan",
 GR, O, "Hasan Tahsin Paşa", "", "dis", "L", "kesin",
 ["TDVIA:selanik", "TDVIA:balkan-savasi"], "",
 "Vali Hasan Tahsin Paşa şehri 35.000 kişilik ordusuyla Yunanlılar'a teslim etti.",
 "Governor Hasan Tahsin Pasha surrendered the city to the Greeks with his 35,000-strong army.", "land"),
("Lüleburgaz (1912)", "Battle of Lule Burgas", "1912-10", W1, "Lüleburgaz", 41.405, 27.356, "known", "Türkiye",
 BG, O, KAB, "", "dis", "L", "kesin",
 ["TDVIA:luleburgaz", "TDVIA:abdullah-pasa-kolemen"], "",
 "Bulgar ordusu şehri büyük bir çatışma sonunda aldı; Abdullah Paşa Çatalca'ya çekildi. Şehir 1913'te geri alındı.",
 "The Bulgarian army took the town after a major clash; Abdullah Pasha fell back to Çatalca. The town was retaken in 1913.", "land"),
("Pınarhisar (1912)", "Battle of Pınarhisar (1912)", "1912-10", W1, "Pınarhisar", 41.62, 27.52, "known", "Türkiye",
 BG, O, "Cemal Bey (Konya Redif Fırkası)", "", "dis", "L", "kesin",
 ["TDVIA:cemal-pasa"], "", "Fırka yenilince Çatalca'daki savunma hattına çekildi.",
 "After its defeat the division fell back to the Çatalca defence line.", "land"),
("Taşoz ve Semadirek (1912)", "Greek occupation of Thasos and Samothrace (1912)", "1912-10-30", W1, "Taşoz ve Semadirek adaları", 40.68, 24.65, "region", "Yunanistan",
 GR, O, "", "", "dis", "L", "kesin",
 ["TDVIA:tasoz", "TDVIA:semadirek"], "Taşoz maddesi iki adanın 30 Ekim 1912'de birlikte işgal edildiğini, Semadirek maddesi Semadirek'in 1 Kasım 1912'de işgal edildiğini yazar.",
 "", "", "land"),
("Yenice-i Vardar (1912)", "Battle of Giannitsa", "1912-11", W1, "Yenice-i Vardar", 40.79, 22.41, "known", "Yunanistan",
 GR, O, "", "", "dis", "L", "kesin",
 ["TDVIA:yenice-i-vardar", "TDVIA:gazi-evrenosoglu-camii-ve-turbesi"], "Madde muharebeyi 11 Kasım 1912'ye koyar; Batı literatürü 1–2 Kasım'a (eski takvimle 19–20 Ekim) koyar.",
 "Kasaba muharebe sırasında büyük ölçüde yakıldı.", "The town was largely burned during the battle.", "land"),
("Manastır (1912)", "Battle of Monastir", "1912-11", W1, "Manastır (Bitola)", 41.03, 21.33, "known", "Kuzey Makedonya",
 SR, O, "", "", "dis", "L", "kesin",
 ["TDVIA:manastir--makedonya"], "",
 "Şehir 14–18 Kasım 1912'de Sırp kuvvetlerince işgal edildi; 530 yıllık Osmanlı hâkimiyeti sona erdi.",
 "The city was occupied by Serbian forces on 14–18 November 1912, ending 530 years of Ottoman rule.", "land"),
("Çatalca (1912)", "First Battle of Çatalca", "1912-11", W1, "Çatalca hattı", 41.14, 28.46, "region", "Türkiye",
 O, BG, "", "", "dis", "W", "kesin",
 ["TDVIA:fahreddin-pasa", "TDVIA:balkan-savasi", "TDVIA:cemal-pasa"], "",
 "Şark Ordusu Çatalca'ya kadar çekildi ve burada tutundu; Fahreddin Bey Çatalca savunmasındaki başarısıyla tanındı.",
 "The Eastern Army fell back to Çatalca and held there; Fahreddin Bey distinguished himself in the Çatalca defence.", "land"),
("Sakız (1912–1913)", "Greek capture of Chios (1912–1913)", "1912-11-25", W1, "Sakız adası", 38.37, 26.14, "region", "Yunanistan",
 GR, O, "", "", "dis", "L", "kesin",
 ["TDVIA:sakiz-adasi"], "", "25 Kasım'daki Yunan çıkarmasından sonra şiddetli çarpışmalar oldu; Osmanlı garnizonu 3 Ocak 1913'te teslim oldu.",
 "Heavy fighting followed the Greek landing of 25 November; the Ottoman garrison surrendered on 3 January 1913.", "land"),
("Yanya (1913)", "Siege of Ioannina (1912–1913)", "1913-03-06", W1, "Yanya", 39.67, 20.85, "known", "Yunanistan",
 GR, O, "Esad Paşa", "", "dis", "L", "kesin",
 ["TDVIA:yanya", "TDVIA:balkan-savasi"], "",
 "Hemen hemen altı ay süren cesurane bir müdafaadan sonra Yunan ordusunun eline geçti.",
 "Fell to the Greek army after a brave defence lasting almost six months.", "land"),
("Edirne (1913)", "Siege of Adrianople (1912–1913)", "1913-03-26", W1, "Edirne", 41.677, 26.556, "known", "Türkiye",
 BG, O, "Mehmed Şükrü Paşa", "", "dis", "L", "kesin",
 ["TDVIA:edirne", "TDVIA:balkan-savasi", "TDVIA:mahmud-sevket-pasa"], "",
 "Kuşatılıp top ateşine tutulan şehir Mehmed Şükrü Paşa'nın kahramanca savunmasına rağmen Bulgarlar'ca işgal edildi.",
 "Besieged and bombarded, the city was occupied by the Bulgarians despite Mehmed Şükrü Pasha's heroic defence.", "land"),
("İşkodra (1913)", "Siege of Scutari (1912–1913)", "1913-04-23", W1, "İşkodra", 42.07, 19.51, "known", "Arnavutluk",
 KD, O, "Esad Toptani Paşa", "", "dis", "L", "kesin",
 ["TDVIA:balkan-savasi"], "", "Balkan Savaşı maddesine göre şehir Esad Toptani Paşa'nın ihaneti üzerine Karadağlılar'ın eline geçti; 1913'te Arnavutluk'a dahil edildi.",
 "According to the Balkan War article the city fell to the Montenegrins through Esad Toptani Pasha's treachery; it was assigned to Albania in 1913.", "land"),
("Edirne'nin geri alınışı (1913)", "Ottoman recapture of Adrianople (1913)", "1913-07-21", W2, "Edirne", 41.677, 26.556, "known", "Türkiye",
 O, BG, "Enver Bey", "", "dis", "W", "borderline",
 ["TDVIA:balkan-savasi", "TDVIA:edirne", "TDVIA:kirklareli", "TDVIA:enver-pasa", "TDVIA:fahreddin-pasa"],
 "Balkan Savaşı, Edirne ve Kırklareli maddeleri 21 Temmuz der; Enver Paşa maddesi Enver Bey'in Edirne'ye girişini 22 Temmuz'a koyar.",
 "Dört devletle birden savaşan Bulgaristan'ın kuvvetsiz bıraktığı şehir hiçbir mukavemet görülmeden geri alındı; Kırkkilise de aynı gün kurtarıldı. Çatışma olmadığından borderline.",
 "Left weakly held by Bulgaria, then at war with four states, the city was retaken without resistance; Kirk Kilisse was freed the same day. Borderline, as there was no fighting.", "land"),
]

LEFT = [
    {"name": "Priştine (1912)", "reason": "Priştine maddesi Sırp işgalini savaş ilânından önceye (2 Ekim 1912) koyar; muharebe ayrıntısı yok.", "source": "TDVIA:pristine"},
    {"name": "Ohri, Pirlepe ve Üsküp işgalleri (1912)", "reason": "Maddeler yalnızca işgali anar; muharebe ayrıntısı yok. Üsküp Kumanova kaydında geçer.", "source": "TDVIA:ohri"},
    {"name": "Midilli, İmroz ve Bozcaada işgalleri (1912)", "reason": "Maddeler yalnızca işgal yılını verir.", "source": "TDVIA:midilli"},
    {"name": "Hamidiye kruvazörünün akınları ve Elli–Limni deniz muharebeleri (1912–1913)", "reason": "Orbay maddesi Hamidiye'nin deniz muharebelerini toplu anar; Elli ve Limni muharebeleri TDVİA'da yok.", "source": "TDVIA:orbay-huseyin-rauf"},
    {"name": "Şarköy çıkarması ve Bolayır (1913)", "reason": "TDVİA'da muharebe ayrıntısı yok; Mustafa Kemal maddesi yalnızca Bolayır'daki görevini anar.", "source": "TDVIA:mustafa-kemal-ataturk"},
    {"name": "Bâbıâli Baskını (1913)", "reason": "Hükümet darbesi; muharebe değil.", "source": "TDVIA:babiali-baskini"},
    {"name": "Garbî Trakya Hükûmet-i Muvakkatesi (1913)", "reason": "Osmanlı hükümeti desteklemedi; muharebe ayrıntısı yok.", "source": "TDVIA:bati-trakya"},
]

# Akademik tur (2026-10-31)
EXTRA_SRC = {
    "Limni (1912)": ["AKD:ozlu-2012", "AKD:ahbab-2016"],  # 21 Ekim 1912
    "Sakız (1912–1913)": ["AKD:ozlu-2012"],  # ada 3 Ocak 1913'te tamamen teslim oldu
    "Manastır (1912)": ["AKD:ahbab-2016"],  # Vardar Ordusu bakiyelerinin Sırplarla son muharebesi
    "İşkodra (1913)": ["AKD:kaytan-2019"],  # Esad Paşa ile Kral Nikola arasındaki antlaşmayla 23 Nisan 1913
}

recs = []
for i, r in enumerate(R, 1):
    (ntr, nen, date, war, place, lat, lon, loc, country, sa, sb, tc, oc, cat, res, status, src, disp, note, note_en, typ) = r
    src = src + [x for x in EXTRA_SRC.get(ntr, []) if x not in src]
    rec = {"id": i, "name_tr": ntr, "name_en": nen, "date": date, "hijri": "", "type": typ, "war": war, "place": place,
           "lat": lat, "lon": lon, "loc": loc, "country": country, "side_a": sa, "side_b": sb, "turkic_cmd": tc, "opp_cmd": oc,
           "category": cat, "result": res, "status": status, "sources": src,
           "verify": {"tdvia": True, "tdvia2": len([s for s in src if s.startswith("TDVIA:")]) >= 2, "wp": False, "rom": False, "academic": any(x.startswith("AKD:") for x in src)},
           "state": O, "home_batch": HB}
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    recs.append(rec)

pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 18 — Osmanlı: Balkan Savaşları (1912–1913)", "compiled": "2026-10-30", "status": "İkinci kaynak turu yapıldı (yeni madde bulunamadı).",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "osmanli-1912-1913.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
