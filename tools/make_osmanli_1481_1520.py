"""data/osmanli-1481-1520.json dosyasını üretir (Parti 7: II. Bayezid ve Yavuz Sultan Selim, 1481–1520)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "osmanli-1481-1520"
O = "Osmanlı Devleti"
DUL = "Dulkadıroğulları"
# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür)
R = [
("Yenişehir (1481)", "Battle of Yenişehir (1481)", "1481-06-22", "Cem Sultan olayı", "Yenişehir ovası", 40.26, 29.65, "approx", "Türkiye",
 "II. Bayezid", "Cem Sultan", "II. Bayezid, Gedik Ahmed Paşa", "Cem Sultan", "ic", "C", "kesin",
 ["TDVIA:bayezid-ii", "TDVIA:cem-sultan"], "", "Yenilen Cem Konya'ya, oradan Mısır'a çekildi; 1482'deki ikinci denemeden sonra Rodos şövalyelerine sığındı.",
 "The defeated Cem withdrew to Konya and then Egypt; after a second attempt in 1482 he took refuge with the Knights of Rhodes.", "land"),
("Kili", "Siege of Kiliya", "1484-07-15", "II. Bayezid'in Boğdan seferi", "Kili", 45.43, 29.27, "known", "Ukrayna",
 O, "Boğdan", "II. Bayezid", "III. Stefan", "dis", "W", "kesin",
 ["TDVIA:bayezid-ii", "TDVIA:kili"], "", "On gün topa tutulan kalenin kumandanı teslim oldu.", "After ten days of bombardment the castle's commander surrendered.", "land"),
("Akkirman", "Siege of Cetatea Albă", "1484-08-04", "II. Bayezid'in Boğdan seferi", "Akkirman", 46.20, 30.35, "known", "Ukrayna",
 O, "Boğdan", "II. Bayezid", "III. Stefan", "dis", "W", "kesin",
 ["TDVIA:bayezid-ii", "TDVIA:akkirman"], "", "Kırım'a karadan ulaşım sağlandı; Karadeniz kıyıları tamamen Osmanlı hâkimiyetine girdi.", "A land route to the Crimea was secured; the whole Black Sea coast came under Ottoman control.", "land"),
("Çukurova (1486)", "Campaign in Cilicia (1486)", "1486", "Osmanlı–Memlük savaşı (1485–1491)", "Çukurova", 37.00, 35.30, "region", "Türkiye",
 "Memlükler", O, "Hersekzâde Ahmed Paşa (esir)", "", "dis", "L", "kesin",
 ["TDVIA:hersekzade-ahmed-pasa", "TDVIA:kayitbay"], "", "Karagöz Paşa ile Hızır Beyzâde'nin yardım etmemesi yüzünden Hersekzâde yaralanıp esir düştü ve Kahire'de bir yıl tutuldu.",
 "Because Karagöz Pasha and Hızır Beyzade failed to support him, Hersekzade was wounded, captured and held in Cairo for a year.", "land"),
("Adana ve Tarsus (1487)", "Recapture of Adana and Tarsus (1487)", "1487", "Osmanlı–Memlük savaşı (1485–1491)", "Adana", 37.00, 35.32, "approx", "Türkiye",
 O, "Memlükler, Turgutoğulları ve Varsaklar", "Koca Dâvud Paşa", "", "dis", "W", "kesin",
 ["TDVIA:davud-pasa-koca", "TDVIA:kayitbay"], "", "Elden çıkmış Adana ve Tarsus geri alındı.", "Adana and Tarsus, which had been lost, were recovered.", "land"),
("Ağaçayırı", "Battle of Ağaçayırı", "1488-08-16", "Osmanlı–Memlük savaşı (1485–1491)", "Ağaçayırı, Adana yakını", 37.05, 35.40, "approx", "Türkiye",
 "Memlükler", O, "Hadım Ali Paşa", "", "dis", "L", "kesin",
 ["TDVIA:kayitbay", "TDVIA:hersekzade-ahmed-pasa"], "", "Başta üstün olan Osmanlı ordusu yenildi; Adana yeniden Memlüklere geçti. Donanma da İskenderun önünde fırtınada gemilerinin çoğunu kaybetti.",
 "The Ottoman army, initially successful, was defeated; Adana passed back to the Mamluks. The fleet also lost most of its ships in a storm off Iskenderun.", "land"),
("Krbava (1493)", "Battle of Krbava Field", "1493", "Osmanlı–Hırvat akınları", "Krbava ovası (Udbina yakını)", 44.53, 15.77, "known", "Hırvatistan",
 O, "Hırvatlar", "Hadım Yâkub Paşa", "", "dis", "W", "kesin",
 ["TDVIA:hirvatistan", "TDVIA:kirka"], "", "Akınları durdurmak isteyen Hırvatlar ile Bosna sancak beyi Hadım Yâkub Paşa kumandasındaki askerler arasındaki savaşı Osmanlılar kazandı; Hırvatlar çok sayıda soylu ve asker kaybetti. (Kontrol turunda eklendi.)",
 "The battle between the Croats, who sought to stop the raids, and the troops of Hadım Yakub Pasha, sanjak-bey of Bosnia, was won by the Ottomans; the Croats lost many nobles and soldiers.", "land"),
("İnebahtı (1499)", "Siege of Lepanto (1499)", "1499-08", "Osmanlı–Venedik savaşı (1499–1503)", "İnebahtı", 38.39, 21.83, "known", "Yunanistan",
 O, "Venedik", "II. Bayezid, Kemal Reis", "", "dis", "W", "kesin",
 ["TDVIA:kemal-reis"], "", "Donanma, karadan kuşatan orduya Venedik yardımını keserek destek verdi.", "The fleet supported the land siege by cutting off Venetian relief.", "land"),
("Sapienza (Zonchio)", "Battle of Zonchio", "1499-08", "Osmanlı–Venedik savaşı (1499–1503)", "Sapienza adası yakını", 36.75, 21.70, "approx", "Yunanistan",
 O, "Venedik donanması", "Kemal Reis, Burak Reis (öldü)", "Antonio Grimani", "dis", "W", "kesin",
 ["TDVIA:kemal-reis"], "", "Burak Reis gemisini feda ederek Venedik gemilerini yaktı. Bir ay sonra Holomiç, Çamlıca ve İnebahtı Boğazı'nda da zafer kazanıldı.",
 "Burak Reis sacrificed his ship to burn the Venetian vessels. Further victories followed a month later at Holomiç, Çamlıca and the Gulf of Lepanto.", "sea"),
("Modon", "Siege of Modon", "1500-08-10", "Osmanlı–Venedik savaşı (1499–1503)", "Modon", 36.82, 21.70, "known", "Yunanistan",
 O, "Venedik", "II. Bayezid", "", "dis", "W", "kesin",
 ["TDVIA:modon", "TDVIA:bayezid-ii"], "Tarih: Modon maddesi 14 Muharrem 906 / 10 Ağustos 1500, Bayezid II maddesi 9 Ağustos.", "Dört ay süren kanlı bir kuşatmadan sonra alındı.", "Taken after a bloody four-month siege.", "land"),
("Koron", "Fall of Coron", "1500-08-15", "Osmanlı–Venedik savaşı (1499–1503)", "Koron", 36.80, 21.96, "known", "Yunanistan",
 O, "Venedik", "II. Bayezid", "", "dis", "W", "borderline",
 ["TDVIA:bayezid-ii"], "", "Modon'un düşmesinden sonra teslim oldu.", "Surrendered after the fall of Modon.", "land"),
("Navarin (1500)", "Fall of Navarino (1500)", "1500-10", "Osmanlı–Venedik savaşı (1499–1503)", "Navarin", 36.91, 21.70, "known", "Yunanistan",
 O, "Venedik", "II. Bayezid", "", "dis", "W", "borderline",
 ["TDVIA:navarin", "TDVIA:koron"], "", "Modon'un fethinden sonra teslim alındı (Rebîülevvel 906).", "Surrendered after the fall of Modon (October 1500).", "land"),
("Midilli müdafaası (1501)", "Siege of Mytilene (1501)", "1501", "Osmanlı–Venedik savaşı (1499–1503)", "Midilli", 39.11, 26.56, "known", "Yunanistan",
 O, "Venedik, Fransa ve İspanya", "", "", "dis", "W", "kesin",
 ["TDVIA:bayezid-ii"], "", "Müttefik donanmanın Midilli ve Çeşme saldırıları sonuç vermedi.", "The allied fleet's attacks on Mytilene and Çeşme failed.", "land"),
("Kütahya (Şahkulu)", "Battle of Kütahya (1511)", "1511-04", "Şahkulu isyanı", "Kütahya önleri", 39.42, 29.98, "approx", "Türkiye",
 "Şahkulu Baba Tekeli", "Anadolu Beylerbeyi Karagöz Ahmed Paşa", "Karagöz Ahmed Paşa", "Şahkulu", "ic", "C", "kesin",
 ["TDVIA:sahkulu-baba-tekeli"], "", "Şahkulu yenilmiş gibi çekilip sonra karşı saldırıyla beylerbeyini bozdu.", "Shahkulu feigned defeat and then routed the governor with a counter-attack.", "land"),
("Çubuk (Gökçay)", "Battle of Gökçay (1511)", "1511-07", "Şahkulu isyanı", "Çubuk / Gökçay, Sivas yakını", 39.60, 37.30, "region", "Türkiye",
 "Osmanlı ordusu", "Şahkulu Baba Tekeli", "Vezîriâzam Hadım Ali Paşa (öldü)", "Şahkulu (öldü)", "ic", "C", "kesin",
 ["TDVIA:sahkulu-baba-tekeli"], "", "İsyan bastırıldı; vezîriâzam ve Şahkulu savaşta öldü.", "The revolt was crushed; the grand vizier and Shahkulu were both killed.", "land"),
("Uğraşdere (Çorlu)", "Battle of Uğraşdere", "1511-08", "Şehzadeler mücadelesi", "Uğraşdere, Çorlu yakını", 41.16, 27.80, "approx", "Türkiye",
 "II. Bayezid", "Şehzade Selim", "II. Bayezid", "Şehzade Selim", "ic", "C", "kesin",
 ["TDVIA:bayezid-ii", "TDVIA:selim-i"], "", "Âni bir saldırıyla geri çekilmeye zorlanan Selim Kefe'ye döndü.", "Forced back by a sudden attack, Selim returned to Caffa.", "land"),
("Yenişehir (1513)", "Battle of Yenişehir (1513)", "1513-04-15", "Şehzadeler mücadelesi", "Yenişehir ovası", 40.26, 29.65, "approx", "Türkiye",
 "Yavuz Sultan Selim", "Şehzade Ahmed", "Yavuz Sultan Selim", "Şehzade Ahmed (idam edildi)", "ic", "C", "kesin",
 ["TDVIA:selim-i"], "", "", "", "land"),
("Çaldıran", "Battle of Chaldiran", "1514-08-23", "Osmanlı–Safevî savaşı", "Çaldıran ovası", 39.13, 44.05, "approx", "Türkiye",
 O, "Safevîler", "Yavuz Sultan Selim", "Şah İsmâil", "dis", "W", "kesin",
 ["TDVIA:selim-i", "TDVIA:safeviler"], "", "Kanatlar bozulma gösterirken toplar ve yeniçeri tüfekçileri savaşı kazandırdı. Ardından Kemah, Harput ve Diyarbekir Osmanlılara geçti.",
 "As the wings wavered, the cannon and janissary musketeers won the battle. Kemah, Harput and Diyarbekir then passed to the Ottomans.", "land"),
("Erzincan (Nur Ali)", "Battle near Erzincan (1514)", "1514", "Osmanlı–Safevî savaşı", "Erzincan yakını", 39.75, 39.49, "approx", "Türkiye",
 O, "Safevîler", "Bıyıklı Mehmed Paşa", "Nur Ali Halife (öldü)", "dis", "W", "kesin",
 ["TDVIA:biyikli-mehmed-pasa"], "", "Karahisar, Kemah, Erzincan ve Tercan kuvvetleri birleştirilerek Safevî ordusu bozuldu. Tarih Çaldıran sonrası; ay belirsiz.",
 "The forces of Karahisar, Kemah, Erzincan and Tercan were combined and the Safavid army was routed. Date after Chaldiran; month uncertain.", "land"),
("Kemah", "Siege of Kemah", "1515-05", "Osmanlı–Safevî savaşı", "Kemah", 39.60, 39.03, "known", "Türkiye",
 O, "Safevîler", "Yavuz Sultan Selim", "", "dis", "W", "kesin",
 ["TDVIA:selim-i", "TDVIA:safeviler"], "", "", "", "land"),
("Turnadağ", "Battle of Turnadağ", "1515-06-12", "Osmanlı–Dulkadıroğulları", "Turnadağ, Elbistan yakını", 38.20, 37.00, "approx", "Türkiye",
 O, DUL, "Hadım Sinan Paşa", "Alâüddevle Bozkurt Bey (öldü)", "turk_arasi", "W", "kesin",
 ["TDVIA:selim-i"], "", "Alâüddevle savaşta öldü; Dulkadır beyliği Osmanlı himayesine girdi.", "Alaüddevle was killed; the Dulkadir beylik came under Ottoman protection.", "land"),
("Âmid (1515)", "Capture of Amida (1515)", "1515-09-19", "Osmanlı–Safevî savaşı", "Âmid (Diyarbakır)", 37.91, 40.23, "known", "Türkiye",
 O, "Safevîler", "Bıyıklı Mehmed Bey", "", "dis", "W", "kesin",
 ["TDVIA:selim-i", "TDVIA:safeviler"], "", "", "", "land"),
("Koçhisar", "Battle of Koçhisar", "1516-06", "Osmanlı–Safevî savaşı", "Koçhisar, Mardin yakını", 37.10, 40.70, "approx", "Türkiye",
 O, "Safevîler", "Bıyıklı Mehmed Paşa", "Kara Han (öldü)", "dis", "W", "kesin",
 ["TDVIA:selim-i"], "", "Kara Han yenilip öldürüldü; kesik başı Haziran 1516'da ordugâha ulaştı.", "Kara Khan was defeated and killed; his severed head reached the camp in June 1516.", "land"),
("Mercidâbık", "Battle of Marj Dabiq", "1516-08-24", "Osmanlı–Memlük savaşı", "Mercidâbık, Halep kuzeyi", 36.53, 37.27, "approx", "Suriye",
 O, "Memlükler", "Yavuz Sultan Selim", "Kansu Gavri (öldü)", "dis", "W", "kesin",
 ["TDVIA:mercidabik-muharebesi", "TDVIA:selim-i", "TDVIA:ridaniye-savasi"], "",
 "Memlük sultanı savaşta öldü. Memlükler Türk kökenlidir ama kapsam listesinde değildir; dış rakip sayıldı.", "The Mamluk sultan was killed. The Mamluks were of Turkic origin but outside the scope list, so recorded as external.", "land"),
("Gazze (1516)", "Battle of Khan Yunis", "1516-12-21", "Osmanlı–Memlük savaşı", "Gazze yöresi", 31.45, 34.35, "approx", "Filistin",
 O, "Memlükler", "Hadım Sinan Paşa", "Canberdi Gazâlî", "dis", "W", "kesin",
 ["TDVIA:ridaniye-savasi"], "", "Gazâlî yenilip Kahire'ye döndü (26 Zilkade 922).", "Ghazali was defeated and returned to Cairo (21 December 1516).", "land"),
("Ridâniye", "Battle of Ridaniya", "1517-01-22", "Osmanlı–Memlük savaşı", "Ridâniye, Kahire yakını", 30.07, 31.32, "approx", "Mısır",
 O, "Memlükler", "Yavuz Sultan Selim, Hadım Sinan Paşa (öldü)", "Tomanbay", "dis", "W", "kesin",
 ["TDVIA:ridaniye-savasi", "TDVIA:selim-i"], "", "Memlüklerin ikinci direnişi kırıldı; Osmanlılar Kahire'ye girdi.", "The Mamluks' second stand was broken; the Ottomans entered Cairo.", "land"),
]

OPP_STATE = {"Turnadağ": DUL}
# İkinci kaynak turu (2026-10-29)
EXTRA_SRC = {"Sapienza (Zonchio)": ["TDVIA:modon"], "Kütahya (Şahkulu)": ["TDVIA:kutahya"], "Çubuk (Gökçay)": ["TDVIA:elci-hani"], "Koçhisar": ["TDVIA:mardin"],   # kontrol turu
             "Koron": ["TDVIA:koron"], "Yenişehir (1513)": ["TDVIA:biyikli-mehmed-pasa"], "Âmid (1515)": ["TDVIA:biyikli-mehmed-pasa"],
             "Mercidâbık": ["TDVIA:memlukler"], "Ridâniye": ["TDVIA:memlukler"]}
# Üçüncü kaynak turu (2026-10-31): toplu TDVİA taraması
EXTRA_SRC.update({
    "İnebahtı (1499)": ["TDVIA:osmanlilar"],  # Mora'daki İnebahtı, Modon, Koron ve Navarin fethedildi (1499-1500)
    "Turnadağ": ["TDVIA:dulkadirogullari"],  # Ördekli mevkiinde Alâüddevle yenildi ve öldürüldü (13 Haziran 1515)
})
FIX = {"Âmid (1515)": {"dispute": "Tarih: Bıyıklı Mehmed Paşa maddesi şehrin anahtarlarının 10 Eylül 1515'te teslim alındığını, Selim I maddesi 10 Şâban 921 / 19 Eylül 1515'i verir. Kara Han şehri daha sonra yeniden kuşattı."},
       "Ridâniye": {"dispute": "Tarih: Ridâniye maddesi 28 Zilhicce 922 / 22 Ocak 1517 sabahı der ve takvim farkına dikkat çeker; Memlükler maddesi iki gün süren savaşı 29 Zilhicce 922 / 23 Ocak 1517'ye koyar."}}
FIX["Turnadağ"] = {"dispute": "Dulkadıroğulları maddesi savaşı Göksun ile Andırın arasında Ördekli mevkiine ve 13 Haziran 1515'e koyar; Selim I maddesi yer vermeden 12 Haziran der."}
LEFT = [
 {"name": "Kayseri (1490)", "reason": "Memlüklerin 1490 seferi; ayrıntı alınmadı.", "source": "TDVIA:kayitbay"},
 {"name": "Cem Sultan'ın ikinci denemesi (1482)", "reason": "Savaşın adı ve yeri kaynakta yok.", "source": "TDVIA:cem-sultan"},
 {"name": "Kahire sokak çatışmaları (1517)", "reason": "Ridâniye sonrası; ayrı bir meydan savaşı değil.", "source": "TDVIA:ridaniye-savasi"},
]

recs = []
for i, r in enumerate(R, 1):
    (ntr, nen, date, war, place, lat, lon, loc, country, sa, sb, tc, oc, cat, res, status, src, disp, note, note_en, typ) = r
    rec = {"id": i, "name_tr": ntr, "name_en": nen, "date": date, "hijri": "", "type": typ, "war": war, "place": place,
           "lat": lat, "lon": lon, "loc": loc, "country": country, "side_a": sa, "side_b": sb, "turkic_cmd": tc, "opp_cmd": oc,
           "category": cat, "result": res, "status": status, "sources": src,
           "verify": {"tdvia": True, "tdvia2": len([s for s in src if s.startswith("TDVIA:")]) >= 2, "wp": False, "rom": False,
                      "academic": any(s.startswith("AKD:") for s in src)},
           "state": O, "home_batch": HB}
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    if ntr in OPP_STATE: rec["opp_state"] = OPP_STATE[ntr]
    rec["sources"] += [x for x in EXTRA_SRC.get(ntr, []) if x not in rec["sources"]]
    rec.update(FIX.get(ntr, {}))
    rec["verify"]["tdvia2"] = len([x for x in rec["sources"] if x.startswith("TDVIA:")]) >= 2
    recs.append(rec)

pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 7 — Osmanlı: II. Bayezid ve Yavuz Sultan Selim (1481–1520)", "compiled": "2026-10-29", "status": "İlk tur.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "osmanli-1481-1520.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
