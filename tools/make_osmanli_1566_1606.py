"""data/osmanli-1566-1606.json dosyasını üretir (Parti 9: II. Selim, III. Murad, III. Mehmed ve I. Ahmed'in ilk yılları, 1566–1606)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "osmanli-1566-1606"
O = "Osmanlı Devleti"
# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür)
R = [
("Lefkoşe", "Siege of Nicosia", "1570-09-09", "Kıbrıs seferi", "Lefkoşe", 35.17, 33.36, "known", "Kıbrıs",
 O, "Venedik", "Lala Mustafa Paşa", "Niccolò Dandolo", "dis", "W", "kesin",
 ["TDVIA:kibris", "TDVIA:lala-mustafa-pasa"], "", "Kırk beş gün süren kuşatmadan sonra alındı.", "Taken after a 45-day siege.", "land"),
("Magosa", "Siege of Famagusta", "1571-08-01", "Kıbrıs seferi", "Magosa", 35.12, 33.94, "known", "Kıbrıs",
 O, "Venedik", "Lala Mustafa Paşa", "Marcantonio Bragadin", "dis", "W", "kesin",
 ["TDVIA:kibris", "TDVIA:lala-mustafa-pasa", "TDVIA:magosa"], "", "Kıbrıs'ın fethi tamamlandı.", "The conquest of Cyprus was completed.", "land"),
("İnebahtı (1571)", "Battle of Lepanto", "1571-10-07", "Kıbrıs savaşı", "İnebahtı körfezi", 38.25, 21.10, "approx", "Yunanistan",
 "Kutsal İttifak (İspanya, Venedik, Papalık)", O, "Müezzinzâde Ali Paşa (öldü), Uluç Ali", "Don Juan de Austria", "dis", "L", "kesin",
 ["TDVIA:inebahti-deniz-savasi", "TDVIA:selim-ii"], "", "Osmanlı donanması ağır yenildi; kaptanıderyâ öldü. Donanma bir kış içinde yeniden kuruldu.", "The Ottoman fleet was heavily defeated and the admiral killed. The fleet was rebuilt within a winter.", "sea"),
("Tunus (1574)", "Conquest of Tunis (1574)", "1574", "Osmanlı–İspanya", "Halkulvâdî ve Tunus", 36.81, 10.30, "known", "Tunus",
 O, "İspanya", "Koca Sinan Paşa, Uluç Ali Paşa", "", "dis", "W", "kesin",
 ["TDVIA:tunus", "TDVIA:selim-ii"], "", "Şehir kesin olarak alındı ve eyalet yapıldı; Hafsî hânedanı sona erdi.", "The city was taken for good and made a province; the Hafsid dynasty ended.", "land"),
("Çıldır", "Battle of Çıldır", "1578-08-09", "Osmanlı–Safevî savaşı (1578–1590)", "Çıldır gölü yöresi", 41.13, 43.13, "approx", "Türkiye",
 O, "Safevîler", "Lala Mustafa Paşa, Özdemiroğlu Osman Paşa", "Tokmak Han", "dis", "W", "kesin",
 ["TDVIA:lala-mustafa-pasa", "TDVIA:osman-pasa-ozdemiroglu", "TDVIA:murad-iii"], "", "Gürcistan ve Dağıstan yolunu açtı.", "Opened the road to Georgia and Daghestan.", "land"),
("Koyungeçidi", "Battle of Koyungeçidi", "1578-09", "Osmanlı–Safevî savaşı (1578–1590)", "Alazan nehri yakını", 41.40, 46.20, "approx", "Azerbaycan",
 O, "Safevîler", "Lala Mustafa Paşa, Özdemiroğlu Osman Paşa", "", "dis", "W", "kesin",
 ["TDVIA:osman-pasa-ozdemiroglu", "TDVIA:murad-iii"], "", "Şirvan yolunu açtı.", "Opened the road to Shirvan.", "land"),
("Meşale Savaşı", "Battle of Torches", "1583-05-07", "Osmanlı–Safevî savaşı (1578–1590)", "Şirvan, Samur nehri yöresi", 41.60, 48.30, "region", "Azerbaycan",
 O, "Safevîler", "Özdemiroğlu Osman Paşa", "", "dis", "W", "kesin",
 ["TDVIA:osman-pasa-ozdemiroglu"], "", "Rivayete göre dört gün dört gece sürdü (7–11 Mayıs 1583).", "Said to have lasted four days and nights (7–11 May 1583).", "land"),
("Tebriz (1585)", "Capture of Tabriz (1585)", "1585", "Osmanlı–Safevî savaşı (1578–1590)", "Tebriz", 38.08, 46.29, "known", "İran",
 O, "Safevîler", "Özdemiroğlu Osman Paşa", "", "dis", "W", "kesin",
 ["TDVIA:murad-iii", "TDVIA:osman-pasa-ozdemiroglu"], "", "Osman Paşa şehri aldıktan sonra öldü.", "Osman Pasha died after taking the city.", "land"),
("Gence (1588)", "Capture of Ganja (1588)", "1588-09-01", "Osmanlı–Safevî savaşı (1578–1590)", "Gence", 40.68, 46.36, "known", "Azerbaycan",
 O, "Safevîler", "Ferhad Paşa", "", "dis", "W", "borderline",
 ["TDVIA:murad-iii", "TDVIA:ferhad-pasa"], "", "Şehre girildi; 1590 barışıyla fethedilen yerler Osmanlıda kaldı.", "The city was entered; the 1590 peace left the conquests in Ottoman hands.", "land"),
("Kulpa (Sisak)", "Battle of Sisak", "1593-06-20", "Uzun Savaş (1593–1606)", "Kulpa nehri, Sisak", 45.47, 16.38, "approx", "Hırvatistan",
 "Habsburglar (Hırvat kuvvetleri)", O, "Bosna Beylerbeyi Hasan Paşa (öldü)", "", "dis", "L", "kesin",
 ["TDVIA:murad-iii"], "", "Bosna kuvvetlerinin bozgunu Uzun Savaş'ın başlamasına yol açtı.", "The rout of the Bosnian forces led to the outbreak of the Long War.", "land"),
("Yanıkkale (1594)", "Siege of Győr (1594)", "1594-09-27", "Uzun Savaş (1593–1606)", "Yanıkkale (Győr)", 47.69, 17.63, "known", "Macaristan",
 O, "Habsburglar", "Koca Sinan Paşa", "", "dis", "W", "kesin",
 ["TDVIA:yanikkale", "TDVIA:murad-iii"], "", "Bir aydan fazla süren kuşatmadan sonra alındı.", "Taken after a siege of more than a month.", "land"),
("Eflak seferi (1595)", "Wallachian campaign (1595)", "1595-08", "Uzun Savaş (1593–1606)", "Eflak", 44.30, 26.00, "region", "Romanya",
 "Eflak (Mihai) ve müttefikleri", O, "Koca Sinan Paşa", "Mihai Viteazul", "dis", "L", "borderline",
 ["TDVIA:mehmed-iii"], "", "TDVİA cephedeki başarısızlıktan söz eder; Kalugareni ve Yergöğü adları Batı kaynaklarındandır.", "TDVİA speaks of failure on the front; the names Călugăreni and Giurgiu come from Western sources.", "land"),
("Estergon'un kaybı (1595)", "Siege of Esztergom (1595)", "1595-09-02", "Uzun Savaş (1593–1606)", "Estergon", 47.79, 18.74, "known", "Macaristan",
 "Habsburglar", O, "", "", "dis", "L", "kesin",
 ["TDVIA:mehmed-iii", "TDVIA:estergon"], "", "", "", "land"),
("Eğri'nin fethi (1596)", "Siege of Eger (1596)", "1596-10-12", "Uzun Savaş (1593–1606)", "Eğri", 47.90, 20.38, "known", "Macaristan",
 O, "Habsburglar", "III. Mehmed", "", "dis", "W", "kesin",
 ["TDVIA:hacova-meydan-savasi", "TDVIA:egri"], "", "", "", "land"),
("Haçova", "Battle of Mezőkeresztes", "1596-10-26", "Uzun Savaş (1593–1606)", "Haçova (Mezőkeresztes)", 47.83, 20.69, "approx", "Macaristan",
 O, "Habsburglar ve Erdel", "III. Mehmed, Cigalazâde Sinan Paşa", "Arşidük Maximilian, Zsigmond Báthory", "dis", "W", "kesin",
 ["TDVIA:hacova-meydan-savasi", "TDVIA:mehmed-iii"], "", "İlk çarpışmalar 25 Ekim'de başladı, asıl savaş 26 Ekim'de yapıldı.", "Skirmishing began on 25 October; the main battle was fought on 26 October.", "land"),
("Yanıkkale'nin kaybı (1598)", "Recapture of Győr (1598)", "1598-03-29", "Uzun Savaş (1593–1606)", "Yanıkkale (Győr)", 47.69, 17.63, "known", "Macaristan",
 "Habsburglar", O, "", "Adolf von Schwarzenberg", "dis", "L", "kesin",
 ["TDVIA:yanikkale"], "", "", "", "land"),
("Kanije (1600)", "Siege of Kanizsa (1600)", "1600-10-20", "Uzun Savaş (1593–1606)", "Kanije", 46.46, 16.99, "known", "Macaristan",
 O, "Habsburglar", "Damad İbrâhim Paşa", "", "dis", "W", "kesin",
 ["TDVIA:kanije", "TDVIA:mehmed-iii"], "Tarih: Kanije maddesi 11 Rebîülâhir 1009 / 20 Ekim 1600, Mehmed III maddesi 13 Rebîülâhir / 22 Ekim.",
 "Önce kale önündeki savaş kazanıldı, ardından kale anlaşmayla teslim alındı.", "The battle before the castle was won and the castle then surrendered on terms.", "land"),
("Kanije müdafaası (1601)", "Siege of Kanizsa (1601)", "1601-11-18", "Uzun Savaş (1593–1606)", "Kanije", 46.46, 16.99, "known", "Macaristan",
 O, "Habsburglar ve müttefikleri", "Tiryaki Hasan Paşa", "Arşidük Ferdinand", "dis", "W", "kesin",
 ["TDVIA:kanije", "TDVIA:mehmed-iii"], "", "10 Eylül–17 Kasım arasında süren kuşatma ağır kayıplarla kaldırıldı.", "The siege from 10 September to 17 November was lifted with heavy losses.", "land"),
("İstolni Belgrad (1601)", "Siege of Székesfehérvár (1601)", "1601-10", "Uzun Savaş (1593–1606)", "İstolni Belgrad", 47.19, 18.41, "known", "Macaristan",
 "Habsburglar", O, "", "Henri de Mercœur", "dis", "L", "kesin",
 ["TDVIA:istolni-belgrad"], "", "Şehir Habsburglarca alındı; bir ay sonra onu geri almaya gelen Osmanlı ordusu on altı gün süren meydan savaşında yenildi.", "The town was taken by the Habsburgs; a month later the Ottoman relief army was defeated in a sixteen-day field battle.", "land"),
("İstolni Belgrad (1602)", "Recapture of Székesfehérvár (1602)", "1602-08", "Uzun Savaş (1593–1606)", "İstolni Belgrad", 47.19, 18.41, "known", "Macaristan",
 O, "Habsburglar", "Yemişçi Hasan Paşa", "", "dis", "W", "ihtilafli",
 ["TDVIA:mehmed-iii", "TDVIA:istolni-belgrad"], "Tarih: Mehmed III maddesi Ağustos 1602, İstolni Belgrad maddesi 11 Ramazan 1011 / 22 Şubat 1603 der.", "Aynı yıl Peşte'yi alıp Budin'i kuşatan Habsburg ordusu çekilmek zorunda kaldı (18 Ekim 1602).", "The same year the Habsburg army that had taken Pest and besieged Buda had to withdraw (18 October 1602).", "land"),
("Budin müdafaası (1602)", "Siege of Buda (1602)", "1602-10-18", "Uzun Savaş (1593–1606)", "Budin", 47.50, 19.04, "known", "Macaristan",
 O, "Habsburglar", "", "", "dis", "W", "kesin",
 ["TDVIA:mehmed-iii"], "", "Peşte'yi alan Habsburg ordusu Budin önünden çekildi.", "The Habsburg army, having taken Pest, withdrew from before Buda.", "land"),
("Cehennem deresi (1600)", "Battle of Cehennem Deresi (1600)", "1600", "Celâlî isyanları", "Cehennem deresi, Divriği yakını", 39.37, 38.12, "approx", "Türkiye",
 O, "Celâlîler (Karayazıcı)", "Serdar Mehmed Paşa", "Karayazıcı Abdülhalim", "ic", "C", "kesin",
 ["TDVIA:karayazici-abdulhalim"], "", "Şiddetli savaşlardan sonra Karayazıcı Divriği civarında Cehennem deresi mevkiinde yenilip Sivas taraflarında dağlara çekildi. (Kontrol turunda eklendi.)",
 "After heavy fighting Karayazıcı was beaten at Cehennem Deresi near Divriği and withdrew into the mountains around Sivas.", "land"),
("Kayseri ovası (1600)", "Battle of Kayseri (1600)", "1600-09-23", "Celâlî isyanları", "Kayseri ovası", 38.72, 35.49, "approx", "Türkiye",
 "Celâlîler (Karayazıcı)", O, "Hacı İbrâhim Paşa", "Karayazıcı Abdülhalim", "ic", "C", "kesin",
 ["TDVIA:karayazici-abdulhalim", "TDVIA:celali-isyanlari"], "", "Halep beylerbeyinin kuvvetleri Karayazıcı'nın ordusuna yenildi.", "The forces of the governor of Aleppo were beaten by Karayazıcı's army.", "land"),
("Sepetli (1601)", "Battle of Sepetli (1601)", "1601-08-12", "Celâlî isyanları", "Sepetli, Elbistan yöresi", 38.20, 37.20, "approx", "Türkiye",
 O, "Celâlîler (Karayazıcı)", "Sokulluzâde Hasan Paşa", "Karayazıcı Abdülhalim", "ic", "C", "kesin",
 ["TDVIA:karayazici-abdulhalim", "TDVIA:celali-isyanlari", "TDVIA:mehmed-iii"], "Yer: Karayazıcı maddesi Elbistan yakınında Sepetli, Celâlî İsyanları maddesi Malatya yakını der.",
 "Karayazıcı yaralı olarak Canik dağlarına, kardeşi Deli Hasan Tokat Kalesi'ne çekildi.", "Karayazıcı fled wounded to the Canik mountains, his brother Deli Hasan to Tokat castle.", "land"),
("Tokat (1602)", "Battle of Tokat (1602)", "1602", "Celâlî isyanları", "Tokat", 40.31, 36.55, "approx", "Türkiye",
 "Celâlîler (Deli Hasan)", O, "Sokulluzâde Hasan Paşa (öldü)", "Deli Hasan", "ic", "C", "kesin",
 ["TDVIA:mehmed-iii"], "", "Celâlî serdarı kale kapısı önünde öldürüldü.", "The commander sent against the Celalis was killed before the castle gate.", "land"),
("Selmas (1605)", "Battle of Sufiyan (1605)", "1605", "Osmanlı–Safevî savaşı (1603–1612)", "Selmas yakını", 38.20, 44.77, "approx", "İran",
 "Safevîler", O, "Cigalazâde Sinan Paşa", "Şah Abbas", "dis", "L", "borderline",
 ["TDVIA:abbas-i"], "", "Yıl maddede doğrudan verilmiyor; Sinan Paşa'nın 1606'da Diyarbekir'de ölümünden önce.", "The year is not stated directly; before Sinan Pasha's death at Diyarbakır in 1606.", "land"),
("Tebriz'in kaybı (1603)", "Loss of Tabriz (1603)", "1603-10-21", "Osmanlı–Safevî savaşı (1603–1612)", "Tebriz", 38.08, 46.29, "known", "İran",
 "Safevîler", O, "", "Şah Abbas", "dis", "L", "kesin",
 ["TDVIA:mehmed-iii"], "", "Ardından Nahcıvan boşaltıldı, Revan kuşatıldı.", "Nakhchivan was then evacuated and Erivan besieged.", "land"),
("Revan'ın kaybı (1604)", "Siege of Erivan (1603–1604)", "1604", "Osmanlı–Safevî savaşı (1603–1612)", "Revan", 40.18, 44.51, "known", "Ermenistan",
 "Safevîler", O, "", "Şah I. Abbas", "dis", "L", "kesin",
 ["TDVIA:ahmed-i", "TDVIA:abbas-i"], "", "Şah Abbas Revan'ı muhasara sonunda teslim aldı, Kars'a girdi ve ancak Ahıska önlerinde durdurulabildi. (Kontrol turunda eklendi.)",
 "Shah Abbas took Erivan after a siege, entered Kars and was only stopped before Akhaltsikhe.", "land"),
]

# İkinci kaynak turu (2026-10-29)
EXTRA_SRC = {"Eflak seferi (1595)": ["TDVIA:koca-sinan-pasa"]}

LEFT = [
 {"name": "Revan (1604)", "reason": "Safevî karşı saldırısının diğer savaşları bu turda ayrıntılı alınmadı.", "source": "TDVIA:mehmed-iii"},
 {"name": "Kalugareni ve Yergöğü (1595)", "reason": "Tek kayıt altında (Eflak seferi 1595) toplandı; TDVİA adlarıyla anmıyor.", "source": "TDVIA:mehmed-iii"},
 {"name": "Celâlî isyanlarının diğer çatışmaları", "reason": "Bu partide yalnızca TDVİA'da adı geçen iki çatışma alındı.", "source": "TDVIA:mehmed-iii"},
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
    rec["verify"]["tdvia2"] = len([x for x in rec["sources"] if x.startswith("TDVIA:")]) >= 2
    recs.append(rec)

pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 9 — Osmanlı: II. Selim, III. Murad, III. Mehmed (1566–1606)", "compiled": "2026-10-29", "status": "İlk tur.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "osmanli-1566-1606.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
