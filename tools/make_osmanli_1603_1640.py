"""data/osmanli-1603-1640.json dosyasını üretir (Parti 10: I. Ahmed, I. Mustafa, II. Osman, IV. Murad, 1603–1640)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "osmanli-1603-1640"
O = "Osmanlı Devleti"
# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür)
R = [
("Peşte ve Vaç (1604)", "Recapture of Pest and Vác (1604)", "1604-10", "Uzun Savaş (1593–1606)", "Peşte", 47.50, 19.07, "known", "Macaristan",
 O, "Habsburglar", "Lala Mehmed Paşa", "", "dis", "W", "kesin",
 ["TDVIA:ahmed-i"], "", "Önce Peşte, ardından Vaç geri alındı.", "Pest and then Vác were retaken.", "land"),
("Estergon kuşatması (1604)", "Siege of Esztergom (1604)", "1604-11-23", "Uzun Savaş (1593–1606)", "Estergon", 47.79, 18.74, "known", "Macaristan",
 "Habsburglar", O, "Lala Mehmed Paşa", "", "dis", "L", "borderline",
 ["TDVIA:ahmed-i"], "", "Yağmur, kar ve askerin muhalefeti yüzünden kuşatma kaldırıldı.", "The siege was lifted because of rain, snow and the troops' opposition.", "land"),
("Estergon'un geri alınışı (1605)", "Recapture of Esztergom (1605)", "1605-10", "Uzun Savaş (1593–1606)", "Estergon", 47.79, 18.74, "known", "Macaristan",
 O, "Habsburglar", "Lala Mehmed Paşa", "", "dis", "W", "ihtilafli",
 ["TDVIA:ahmed-i", "TDVIA:estergon"], "Tarih: Estergon maddesi 3 Ekim 1605, Ahmed I maddesi 4 Kasım 1605 der.",
 "Önce Vişegrad ve Tepedelen alındı; şehir 1683'e kadar Osmanlıda kaldı.", "Visegrád and Nógrád were taken first; the town stayed Ottoman until 1683.", "land"),
("Kilis (1605)", "Battle of Kilis (1605)", "1605", "Celâlî isyanları", "Kilis dışı", 36.72, 37.12, "approx", "Türkiye",
 "Canbolatoğlu Hüseyin", O, "Nasuh Paşa (Halep beylerbeyi)", "Canbolatoğlu Hüseyin", "ic", "C", "kesin",
 ["TDVIA:nasuh-pasa"], "", "Yenilen Nasuh Paşa sonra Kütahya'ya kaçtı.", "The defeated Nasuh Pasha later fled to Kütahya.", "land"),
("Oruç ovası (1607)", "Battle of Oruç Ovası (1607)", "1607-10-24", "Celâlî isyanları", "Oruç ovası (Amik yöresi)", 36.35, 36.40, "approx", "Türkiye",
 O, "Canbolatoğlu Ali Paşa ve Ma'noğlu Fahreddin", "Kuyucu Murad Paşa", "Canbolatoğlu Ali Paşa", "ic", "C", "kesin",
 ["TDVIA:ahmed-i", "TDVIA:kuyucu-murad-pasa"], "", "Çatışmalar 23 Ekim'de başladı, asıl savaş 24 Ekim'de yapıldı; Murad Paşa ardından Halep'e girdi.", "Fighting began on 23 October and the main battle took place on 24 October; Murad Pasha then entered Aleppo.", "land"),
("Alaçayır (1608)", "Battle of Alaçayır (1608)", "1608-08-09", "Celâlî isyanları", "Alaçayır, Göksun yaylası", 38.02, 36.50, "approx", "Türkiye",
 O, "Celâlîler (Kalenderoğlu)", "Kuyucu Murad Paşa", "Kalenderoğlu Mehmed", "ic", "C", "kesin",
 ["TDVIA:kuyucu-murad-pasa", "TDVIA:kalenderoglu-mehmed"], "", "Kalenderoğlu İran'a kaçtı.", "Kalenderoğlu fled to Iran.", "land"),
("Revan (1616)", "Siege of Erivan (1616)", "1616", "Osmanlı–Safevî savaşı (1615–1618)", "Revan", 40.18, 44.51, "known", "Ermenistan",
 "Safevîler", O, "Öküz Mehmed Paşa", "", "dis", "L", "kesin",
 ["TDVIA:ahmed-i"], "", "Öküz Mehmed Paşa bir İran ordusunu yenip Revan'ı kuşattıysa da muhasara topları olmadığı ve şiddetli direniş yüzünden orduyu Erzurum'a çekti; sefer başarısız oldu, paşa azledildi. (Kontrol turunda eklendi.)",
 "Öküz Mehmed Pasha beat an Iranian army and besieged Erivan, but lacking siege guns and facing stiff resistance he withdrew to Erzurum; the campaign failed and he was dismissed.", "land"),
("İran cephesi (1618)", "Battle of Serav (1618)", "1618-09-10", "Osmanlı–Safevî savaşı (1615–1618)", "Erdebil yolu (Serav yöresi)", 37.93, 47.54, "region", "İran",
 "Safevîler", O, "", "", "dis", "L", "borderline",
 ["TDVIA:osman-ii"], "", "TDVİA yeri adlandırmıyor; ardından barış yapıldı.", "TDVİA does not name the place; peace followed.", "land"),
("Hotin (1621)", "Battle of Khotyn (1621)", "1621-09", "Osmanlı–Lehistan savaşı (1620–1621)", "Hotin", 48.52, 26.50, "known", "Ukrayna",
 O, "Lehistan-Litvanya ve Zaporojya Kazakları", "II. Osman", "Jan Karol Chodkiewicz", "dis", "D", "kesin",
 ["TDVIA:osman-ii", "TDVIA:hotin"], "", "Leh-Kazak istihkâmına yapılan hücumlar sonuç vermedi; barış Osmanlılar lehine yapıldı ve Hotin Boğdan'a bırakıldı.", "Assaults on the Polish–Cossack camp failed; the peace favoured the Ottomans and Khotyn went to Moldavia.", "land"),
("Bağdat'ın kaybı (1624)", "Loss of Baghdad (1624)", "1624", "Osmanlı–Safevî savaşı (1623–1639)", "Bağdat", 33.31, 44.36, "known", "Irak",
 "Safevîler", O, "", "Şah Abbas", "dis", "L", "borderline",
 ["TDVIA:murad-iv", "TDVIA:bagdat"], "", "Bekir Subaşı'nın isyanı sırasında şehir Safevîlere geçti.", "The city passed to the Safavids during Bekir Subaşı's revolt.", "land"),
("Karasu (Kayseri) 1624", "Battle of Karasu (1624)", "1624", "Abaza Paşa isyanı", "Karasu, Kayseri yakını", 38.75, 35.40, "approx", "Türkiye",
 O, "Abaza Paşa", "Hâfız Ahmed Paşa", "Abaza Mehmed Paşa", "ic", "C", "kesin",
 ["TDVIA:abaza-pasa"], "", "Abaza askerinin çoğunu kaybedip Erzurum'a kaçtı.", "Abaza lost most of his men and fled to Erzurum.", "land"),
("Cennetoğlu (1625)", "Defeat of Cennetoğlu (1625)", "1625-12", "Celâlî isyanları", "Manisa", 38.61, 27.43, "approx", "Türkiye",
 O, "Celâlîler (Cennetoğlu)", "", "Cennetoğlu", "ic", "C", "kesin",
 ["TDVIA:murad-iv"], "", "Balıkesir'de hükümet kuvvetlerini dağıtan Cennetoğlu Manisa'da yenildi, Birgi'de idam edildi.", "Cennetoğlu, who had scattered government troops at Balıkesir, was beaten at Manisa and executed at Birgi.", "land"),
("Bağdat kuşatması (1625–26)", "Siege of Baghdad (1625–26)", "1626", "Osmanlı–Safevî savaşı (1623–1639)", "Bağdat", 33.31, 44.36, "known", "Irak",
 "Safevîler", O, "Hâfız Ahmed Paşa", "Şah Abbas", "dis", "L", "kesin",
 ["TDVIA:murad-iv", "TDVIA:hafiz-ahmed-pasa", "TDVIA:bagdat"], "", "Çarpışmalardan sonuç alınamadı.", "The fighting brought no result.", "land"),
("Ahıska seferi (1626)", "Abaza's attack on the Akhaltsikhe army (1626)", "1626", "Abaza Paşa isyanı", "Erzurum", 39.90, 41.27, "known", "Türkiye",
 "Abaza Paşa", O, "Dişlenk Hüseyin Paşa (öldü)", "Abaza Mehmed Paşa", "ic", "C", "kesin",
 ["TDVIA:abaza-pasa"], "", "Abaza Erzurum'dan çıkıp Ahıska'ya giden orduya saldırdı.", "Abaza sallied from Erzurum and attacked the army marching to Akhaltsikhe.", "land"),
("Erzurum (1628)", "Siege of Erzurum (1628)", "1628", "Abaza Paşa isyanı", "Erzurum", 39.90, 41.27, "known", "Türkiye",
 O, "Abaza Paşa", "Hüsrev Paşa", "Abaza Mehmed Paşa", "ic", "C", "kesin",
 ["TDVIA:abaza-pasa", "TDVIA:murad-iv"], "", "Abaza emânla teslim oldu.", "Abaza surrendered under a promise of safety.", "land"),
("Mihriban (1630)", "Battle of Mahidasht (1630)", "1630-05-05", "Osmanlı–Safevî savaşı (1623–1639)", "Mihriban kalesi yakını", 34.70, 46.30, "approx", "İran",
 O, "Safevîler", "Hüsrev Paşa", "Zeynel Han", "dis", "W", "kesin",
 ["TDVIA:murad-iv"], "", "", "", "land"),
("Bağdat kuşatması (1630)", "Siege of Baghdad (1630)", "1630-10-06", "Osmanlı–Safevî savaşı (1623–1639)", "Bağdat", 33.31, 44.36, "known", "Irak",
 "Safevîler", O, "Hüsrev Paşa", "", "dis", "L", "kesin",
 ["TDVIA:murad-iv"], "", "6 Ekim 1630'da başlayan ikinci kuşatmadan da sonuç alınamadı.", "The second siege, begun on 6 October 1630, also failed.", "land"),
("Van (1633)", "Siege of Van (1633)", "1633", "Osmanlı–Safevî savaşı (1623–1639)", "Van", 38.50, 43.38, "known", "Türkiye",
 O, "Safevîler", "Murtaza Paşa", "", "dis", "W", "borderline",
 ["TDVIA:murad-iv"], "", "Safevî kuşatması kalktı.", "The Safavid siege was raised.", "land"),
("Revan (1635)", "Siege of Erivan (1635)", "1635-08-08", "IV. Murad'ın Revan seferi", "Revan", 40.18, 44.51, "known", "Ermenistan",
 O, "Safevîler", "IV. Murad", "", "dis", "W", "kesin",
 ["TDVIA:murad-iv", "TDVIA:revan"], "", "28–29 Temmuz'da başlayan kuşatmadan sonra teslim alındı; anısına Revan Köşkü yapıldı.", "Surrendered after a siege begun on 28–29 July; the Erivan Kiosk was built to commemorate it.", "land"),
("Ahıska (1635)", "Siege of Akhaltsikhe (1635)", "1635", "IV. Murad'ın Revan seferi", "Ahıska", 41.64, 42.98, "known", "Gürcistan",
 O, "Safevîler", "Kenan Paşa", "", "dis", "W", "kesin",
 ["TDVIA:murad-iv"], "", "Yirmi üç günlük kuşatmayla alındı.", "Taken after a 23-day siege.", "land"),
("Revan'ın kaybı (1636)", "Loss of Erivan (1636)", "1636-04-01", "Osmanlı–Safevî savaşı (1623–1639)", "Revan", 40.18, 44.51, "known", "Ermenistan",
 "Safevîler", O, "", "Şah Safî", "dis", "L", "kesin",
 ["TDVIA:murad-iv", "TDVIA:revan"], "", "", "", "land"),
("Azak'ın kaybı (1637)", "Loss of Azov (1637)", "1637", "Osmanlı–Don Kazakları", "Azak", 47.11, 39.42, "known", "Rusya",
 "Don Kazakları", O, "", "", "dis", "L", "kesin",
 ["TDVIA:azak"], "", "Kazaklar kaleyi ele geçirdi; 1642'ye kadar ellerinde kaldı.", "The Cossacks seized the fortress and held it until 1642.", "land"),
("Bağdat'ın fethi (1638)", "Siege of Baghdad (1638)", "1638-12-24", "IV. Murad'ın Bağdat seferi", "Bağdat", 33.31, 44.36, "known", "Irak",
 O, "Safevîler", "IV. Murad, Tayyar Mehmed Paşa (öldü)", "Bektaş Han", "dis", "W", "kesin",
 ["TDVIA:murad-iv", "TDVIA:bagdat"], "", "Metris sürülerek yapılan kuşatmadan sonra kale komutanı teslim oldu; 1639 Kasr-ı Şîrin barışı izledi.", "After a siege by trenches the commander surrendered; the Peace of Zuhab followed in 1639.", "land"),
]

# İkinci kaynak turu (2026-10-29)
EXTRA_SRC = {"Peşte ve Vaç (1604)": ["TDVIA:lala-mehmed-pasa"], "Karasu (Kayseri) 1624": ["TDVIA:husrev-pasa", "TDVIA:hafiz-ahmed-pasa"],
             "Mihriban (1630)": ["TDVIA:husrev-pasa"], "Bağdat kuşatması (1630)": ["TDVIA:husrev-pasa"], "Ahıska (1635)": ["TDVIA:ahiska"],
             "Bağdat kuşatması (1625–26)": ["TDVIA:husrev-pasa"], "Erzurum (1628)": ["TDVIA:husrev-pasa"]}
FIX = {"Peşte ve Vaç (1604)": {"note": "Peşte, Hatvan ve Vaç geri alındı.", "note_en": "Pest, Hatvan and Vác were retaken."},
       "Karasu (Kayseri) 1624": {"date": "1624-09-05", "turkic_cmd": "Çerkez Mehmed Paşa",
           "dispute": "Komutan: Hüsrev Paşa ve Hâfız Ahmed Paşa maddeleri Sadrazam Çerkez Mehmed Paşa der; Abaza Paşa maddesi Hâfız Paşa der."},
       "Bağdat kuşatması (1625–26)": {"date": "1626-07", "note": "13 Kasım 1625'te başlayan kuşatma yedi ay yirmi gün sürdü ve başarısız oldu.",
           "note_en": "The siege begun on 13 November 1625 lasted seven months and twenty days and failed."},
       "Mihriban (1630)": {"note": "10.000 kişilik Osmanlı birliği Zeynel Han'ın ordusunu yenip kaleyi aldı.", "note_en": "An Ottoman force defeated Zeynel Khan's army and took the castle."},
       "Bağdat kuşatması (1630)": {"date": "1630-11-14", "note": "6 Ekim'de başlayan kuşatma otuz dokuz gün sonra kaldırıldı.", "note_en": "The siege begun on 6 October was lifted after thirty-nine days."},
       "Erzurum (1628)": {"date": "1628-09-22", "note": "6 Eylül'de kuşatılan Erzurum'da Abaza dört günlük pazarlıktan sonra teslim oldu.", "note_en": "Besieged from 6 September, Abaza surrendered after four days of negotiation."}}

LEFT = [
 {"name": "Tebriz (1635)", "reason": "Boşaltılmış şehir tahrip edildi; savaş yok.", "source": "TDVIA:murad-iv"},
 {"name": "Çemhâl ovası (14 Temmuz 1630)", "reason": "Luristan hâkiminin saldırısı püskürtüldü; küçük çatışma.", "source": "TDVIA:husrev-pasa"},
 {"name": "Kazak akınları (Boğaziçi 1624 vb.)", "reason": "Akın; meydan savaşı değil.", "source": "TDVIA:murad-iv"},
 {"name": "Kalenderoğlu–Tekeli Mehmed Paşa (Ankara, 1607–08)", "reason": "Tarihi maddede verilmiyor.", "source": "TDVIA:kuyucu-murad-pasa"},
]

recs = []
for i, r in enumerate(R, 1):
    (ntr, nen, date, war, place, lat, lon, loc, country, sa, sb, tc, oc, cat, res, status, src, disp, note, note_en, typ) = r
    rec = {"id": i, "name_tr": ntr, "name_en": nen, "date": date, "hijri": "", "type": typ, "war": war, "place": place,
           "lat": lat, "lon": lon, "loc": loc, "country": country, "side_a": sa, "side_b": sb, "turkic_cmd": tc, "opp_cmd": oc,
           "category": cat, "result": res, "status": status, "sources": src,
           "verify": {"tdvia": True, "tdvia2": len([s for s in src if s.startswith("TDVIA:")]) >= 2, "wp": False, "rom": False, "academic": False},
           "state": O, "home_batch": HB}
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    rec["sources"] += [x for x in EXTRA_SRC.get(ntr, []) if x not in rec["sources"]]
    rec.update(FIX.get(ntr, {}))
    rec["verify"]["tdvia2"] = len([x for x in rec["sources"] if x.startswith("TDVIA:")]) >= 2
    recs.append(rec)

pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 10 — Osmanlı: I. Ahmed, II. Osman, IV. Murad (1603–1640)", "compiled": "2026-10-29", "status": "İlk tur.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "osmanli-1603-1640.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
