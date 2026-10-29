"""data/osmanli-1520-1566.json dosyasını üretir (Parti 8: Kanûnî Sultan Süleyman dönemi, 1520–1566)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "osmanli-1520-1566"
O = "Osmanlı Devleti"
# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür)
R = [
("Böğürdelen", "Siege of Šabac", "1521-07-07", "Kanûnî'nin Macar seferleri", "Böğürdelen (Šabac)", 44.75, 19.70, "known", "Sırbistan",
 O, "Macaristan", "Kanûnî Sultan Süleyman", "", "dis", "W", "kesin",
 ["TDVIA:suleyman-i"], "", "Kanûnî'nin ilk fethi.", "Süleyman's first conquest.", "land"),
("Belgrad'ın fethi", "Siege of Belgrade (1521)", "1521-08", "Kanûnî'nin Macar seferleri", "Belgrad", 44.82, 20.45, "known", "Sırbistan",
 O, "Macaristan", "Kanûnî Sultan Süleyman", "", "dis", "W", "kesin",
 ["TDVIA:belgrad", "TDVIA:macaristan"], "", "Halkın bir kısmı İstanbul'a gönderilip bugünkü Belgrad ormanlarına yerleştirildi.", "Part of the population was sent to Istanbul and settled in what is now the Belgrade Forest.", "land"),
("Rodos'un fethi", "Siege of Rhodes (1522)", "1522-12-20", "Kanûnî–Rodos şövalyeleri", "Rodos", 36.44, 28.22, "known", "Yunanistan",
 O, "Rodos şövalyeleri", "Kanûnî Sultan Süleyman", "Philippe Villiers de l'Isle-Adam", "dis", "W", "kesin",
 ["TDVIA:suleyman-i", "TDVIA:rodos"], "", "Kanlı çarpışmalardan sonra şövalyeler teslim oldu.", "After bloody fighting the knights surrendered.", "land"),
("Mohaç", "Battle of Mohács", "1526-08-29", "Kanûnî'nin Macar seferleri", "Mohaç ovası", 45.94, 18.68, "approx", "Macaristan",
 O, "Macaristan", "Kanûnî Sultan Süleyman, İbrâhim Paşa", "II. Lajos (öldü)", "dis", "W", "kesin",
 ["TDVIA:mohac-muharebesi", "TDVIA:macaristan"], "", "Macar kralı savaştan kaçarken öldü; Macar krallığının bağımsızlığı sona erdi.", "The Hungarian king died while fleeing; independent Hungary came to an end.", "land"),
("Budin (1529)", "Capture of Buda (1529)", "1529-09", "Kanûnî'nin Viyana seferi", "Budin", 47.50, 19.04, "known", "Macaristan",
 O, "Habsburg garnizonu", "Kanûnî Sultan Süleyman", "", "dis", "W", "borderline",
 ["TDVIA:budin"], "", "Kısa bir mücadeleden sonra alındı ve Szapolyai'ye bırakıldı.", "Taken after a short struggle and handed to Szapolyai.", "land"),
("Viyana kuşatması (1529)", "Siege of Vienna (1529)", "1529-10", "Kanûnî'nin Viyana seferi", "Viyana", 48.21, 16.37, "known", "Avusturya",
 "Habsburglar", O, "Kanûnî Sultan Süleyman", "", "dis", "L", "kesin",
 ["TDVIA:viyana"], "", "Mevsimin ilerlemesi yüzünden kuşatma kaldırıldı.", "The siege was lifted because the season was too far advanced.", "land"),
("Güns (Kőszeg)", "Siege of Kőszeg", "1532-08", "Kanûnî'nin Alman seferi", "Güns", 47.39, 16.54, "known", "Macaristan",
 O, "Habsburglar", "Kanûnî Sultan Süleyman", "Miklós Jurisics", "dis", "W", "ihtilafli",
 ["TDVIA:suleyman-i"], "TDVİA Güns'ün alındığını yazar. Alternatif okuma: Batı kaynaklarına göre küçük kale uzun süre direndi ve sembolik bir teslimle sefer Viyana'ya ulaşamadan bitti.",
 "", "", "land"),
("Koron'un kaybı (1532)", "Loss of Coron (1532)", "1532", "Osmanlı–Habsburg deniz savaşları", "Koron", 36.80, 21.96, "known", "Yunanistan",
 "Habsburg donanması (Andrea Doria)", O, "", "Andrea Doria", "dis", "L", "kesin",
 ["TDVIA:suleyman-i", "TDVIA:koron"], "", "Doria ayrıca Patras ve İnebahtı'ya asker çıkardı.", "Doria also landed troops at Patras and Lepanto.", "land"),
("Tunus (1534)", "Capture of Tunis (1534)", "1534-09-22", "Barbaros'un Kuzey Afrika seferi", "Tunus", 36.80, 10.18, "known", "Tunus",
 O, "Hafsîler", "Barbaros Hayreddin Paşa", "Mevlây Hasan", "dis", "W", "borderline",
 ["TDVIA:barbaros-hayreddin-pasa", "TDVIA:tunus"], "", "Mevlây Hasan'ın terk ettiği şehir alındı.", "The city abandoned by Mulay Hasan was taken.", "land"),
("Tebriz (1534)", "Occupation of Tabriz (1534)", "1534-08-06", "Irakeyn seferi", "Tebriz", 38.08, 46.29, "known", "İran",
 O, "Safevîler", "Pargalı İbrâhim Paşa", "", "dis", "W", "borderline",
 ["TDVIA:irakeyn-seferi"], "", "Küçük bir çarpışmadan sonra boşaltılmış şehre girildi.", "The evacuated city was entered after a small clash.", "land"),
("Bağdat (1534)", "Capture of Baghdad (1534)", "1534-11", "Irakeyn seferi", "Bağdat", 33.31, 44.36, "known", "Irak",
 O, "Safevîler", "Kanûnî Sultan Süleyman", "", "dis", "W", "borderline",
 ["TDVIA:irakeyn-seferi"], "", "Şehir savaşsız teslim alındı.", "The city was taken without a battle.", "land"),
("Tunus (1535)", "Conquest of Tunis (1535)", "1535-07", "Osmanlı–Habsburg savaşları", "Halkulvâdî ve Tunus", 36.81, 10.30, "known", "Tunus",
 "Habsburglar (V. Karl)", O, "Barbaros Hayreddin Paşa", "V. Karl", "dis", "L", "kesin",
 ["TDVIA:suleyman-i", "TDVIA:barbaros-hayreddin-pasa", "TDVIA:tunus"], "", "Barbaros'un savunduğu Halkulvâdî ve Tunus alındı.", "La Goulette and Tunis, defended by Barbarossa, were taken.", "land"),
("Preveze", "Battle of Preveza", "1538-09-28", "Osmanlı–Kutsal İttifak", "Preveze körfezi", 38.95, 20.75, "approx", "Yunanistan",
 O, "Kutsal İttifak donanması (Venedik, İspanya, Papalık)", "Barbaros Hayreddin Paşa", "Andrea Doria", "dis", "W", "kesin",
 ["TDVIA:preveze-deniz-muharebesi", "TDVIA:barbaros-hayreddin-pasa"], "", "Akdeniz'de Osmanlı deniz hâkimiyetini kesinleştirdi.", "Secured Ottoman naval supremacy in the Mediterranean.", "sea"),
("Diu kuşatması", "Siege of Diu (1538)", "1538", "Osmanlı–Portekiz", "Diu", 20.71, 70.98, "known", "Hindistan",
 "Portekiz", O, "Hadım Süleyman Paşa", "", "dis", "L", "kesin",
 ["TDVIA:diu"], "", "Portekiz savunması ve Gucerât'la güvensizlik yüzünden kuşatma kaldırıldı.", "The siege was lifted because of the Portuguese defence and mistrust with Gujarat.", "land"),
("Budin (1541)", "Siege of Buda (1541)", "1541-08", "Kanûnî'nin İstabur seferi", "Budin", 47.50, 19.04, "known", "Macaristan",
 O, "Habsburglar", "Kanûnî Sultan Süleyman", "Wilhelm von Roggendorf", "dis", "W", "kesin",
 ["TDVIA:suleyman-i", "TDVIA:budin"], "", "Habsburg kuşatması kırıldı; Budin beylerbeyiliği kuruldu.", "The Habsburg siege was broken; the province of Buda was created.", "land"),
("Cezayir (1541)", "Algiers expedition (1541)", "1541-10", "Osmanlı–Habsburg savaşları", "Cezayir", 36.75, 3.06, "known", "Cezayir",
 O, "Habsburglar (V. Karl)", "Hasan Ağa", "V. Karl", "dis", "W", "kesin",
 ["TDVIA:cezayir"], "", "V. Karl'ın da katıldığı İspanya seferi tam bir hezimetle sonuçlandı.", "The Spanish expedition, which Charles V joined in person, ended in complete disaster.", "land"),
("Peşte (1542)", "Siege of Pest (1542)", "1542-11", "Osmanlı–Habsburg savaşları", "Peşte", 47.50, 19.07, "known", "Macaristan",
 O, "Habsburglar", "", "", "dis", "W", "kesin",
 ["TDVIA:suleyman-i", "TDVIA:budin"], "", "Peşte'yi kuşatan Habsburg ordusu bozuldu.", "The Habsburg army besieging Pest was routed.", "land"),
("Estergon", "Siege of Esztergom (1543)", "1543-08-10", "Kanûnî'nin Macar seferi", "Estergon", 47.79, 18.74, "known", "Macaristan",
 O, "Habsburglar", "Kanûnî Sultan Süleyman", "", "dis", "W", "kesin",
 ["TDVIA:estergon"], "", "İki buçuk hafta dayanan muhafızlar teslim oldu.", "The garrison surrendered after holding out for two and a half weeks.", "land"),
("Nice", "Siege of Nice (1543)", "1543-08", "Osmanlı–Fransız ortak seferi", "Nice", 43.70, 7.27, "known", "Fransa",
 O + ", Fransa", "Savoya Dükalığı", "Barbaros Hayreddin Paşa", "", "dis", "W", "borderline",
 ["TDVIA:suleyman-i", "TDVIA:barbaros-hayreddin-pasa"], "", "Şehir alındı ama kale direndi.", "The town was taken but the citadel held out.", "land"),
("Trablusgarp", "Capture of Tripoli (1551)", "1551-08-15", "Osmanlı–Malta şövalyeleri", "Trablusgarp", 32.90, 13.18, "known", "Libya",
 O, "Malta şövalyeleri", "Sinan Paşa, Turgut Reis", "", "dis", "W", "kesin",
 ["TDVIA:trablusgarp", "TDVIA:turgut-reis"], "", "", "", "land"),
("Temeşvar (1552)", "Siege of Temesvár", "1552-07", "Osmanlı–Habsburg savaşları", "Temeşvar", 45.75, 21.23, "known", "Romanya",
 O, "Habsburglar", "Kara Ahmed Paşa, Sokullu Mehmed Paşa", "", "dis", "W", "kesin",
 ["TDVIA:egri", "TDVIA:suleyman-i"], "", "Ardından Szolnok da alındı.", "Szolnok was taken afterwards.", "land"),
("Eğri kuşatması (1552)", "Siege of Eger (1552)", "1552-10", "Osmanlı–Habsburg savaşları", "Eğri", 47.90, 20.38, "known", "Macaristan",
 "Habsburglar (Macar savunucular)", O, "Kara Ahmed Paşa, Hadım Ali Paşa", "István Dobó", "dis", "L", "kesin",
 ["TDVIA:egri"], "", "Yaklaşık kırk gün süren kuşatma kaldırıldı.", "The siege, lasting about forty days, was lifted.", "land"),
("Sigetvar kuşatması (1556)", "Siege of Szigetvár (1556)", "1556", "Osmanlı–Habsburg savaşları", "Sigetvar", 46.05, 17.80, "known", "Macaristan",
 "Habsburglar", O, "Hadım Ali Paşa", "", "dis", "L", "kesin",
 ["TDVIA:suleyman-i"], "", "", "", "land"),
("Konya (1559)", "Battle of Konya (1559)", "1559-05-30", "Şehzadeler mücadelesi", "Konya ovası", 37.87, 32.48, "approx", "Türkiye",
 "Şehzade Selim", "Şehzade Bayezid", "Şehzade Selim", "Şehzade Bayezid", "ic", "C", "kesin",
 ["TDVIA:suleyman-i"], "", "Yenilen Bayezid Safevîlere sığındı.", "The defeated Bayezid took refuge with the Safavids.", "land"),
("Cerbe", "Battle of Djerba", "1560-05-14", "Osmanlı–Kutsal İttifak", "Cerbe adası", 33.80, 10.85, "known", "Tunus",
 O, "Haçlı donanması (İspanya ve müttefikleri)", "Piyâle Paşa, Turgut Reis", "Juan de la Cerda", "dis", "W", "kesin",
 ["TDVIA:cerbe"], "", "Donanmanın ikiye ayrılarak yaptığı manevrayla kalabalık Haçlı donanması dağıtıldı.", "A manoeuvre splitting the fleet in two scattered the larger Crusader fleet.", "sea"),
("Cerbe Kalesi", "Siege of Djerba castle", "1560-07-30", "Osmanlı–Kutsal İttifak", "Cerbe adası", 33.80, 10.85, "known", "Tunus",
 O, "İspanya ve müttefik garnizon", "Piyâle Paşa, Turgut Reis", "", "dis", "W", "kesin",
 ["TDVIA:turgut-reis", "TDVIA:cerbe"], "", "Deniz zaferinin ardından yaklaşık iki ay süren kale kuşatması; ada 7 Zilkade 967'de fethedildi.", "The castle siege that followed the naval victory lasted about two months; the island fell on 30 July 1560.", "land"),
("Malta kuşatması", "Great Siege of Malta", "1565-09", "Osmanlı–Malta şövalyeleri", "Malta", 35.90, 14.51, "known", "Malta",
 "Malta şövalyeleri", O, "Lala Mustafa Paşa, Piyâle Paşa, Turgut Paşa (öldü)", "Jean de Valette", "dis", "L", "kesin",
 ["TDVIA:malta", "TDVIA:suleyman-i"], "", "Santarma (St. Elmo) alındığı gün Turgut Paşa öldü; kuşatma sonuç vermedi.", "Turgut Pasha died on the day St Elmo fell; the siege failed.", "land"),
("Sigetvar (1566)", "Siege of Szigetvár (1566)", "1566-09-07", "Kanûnî'nin son seferi", "Sigetvar", 46.05, 17.80, "known", "Macaristan",
 O, "Habsburglar", "Kanûnî Sultan Süleyman (kuşatma sırasında öldü), Sokullu Mehmed Paşa", "Miklós Zrínyi (öldü)", "dis", "W", "kesin",
 ["TDVIA:sigetvar", "TDVIA:suleyman-i"], "", "5 Eylül'de lağımla barut mahzeni patlatıldı; Zrínyi'nin huruç hareketiyle savunma çöktü. Kanûnî kuşatma sırasında vefat etti.",
 "On 5 September a mine blew up the powder store; Zrínyi's sortie ended the defence. Süleyman died during the siege.", "land"),
]

LEFT = [
 {"name": "Seydi Ali Reis'in Hint Okyanusu seferi (1554)", "reason": "Portekiz donanmasıyla çatışmaların sonucu indirilen metinde net değil; ikinci turda.", "source": "TDVIA:seydi-ali-reis"},
 {"name": "Gorjani (1537), Korfu (1537)", "reason": "TDVİA'da ayrıntı bu turda bulunamadı.", "source": "TDVIA:suleyman-i"},
 {"name": "Safevî seferleri 1548 ve 1553–55", "reason": "Büyük meydan savaşı yok; Van'ın alınması dışında kayıt açılmadı.", "source": "TDVIA:van"},
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
    recs.append(rec)

pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 8 — Osmanlı: Kanûnî Sultan Süleyman (1520–1566)", "compiled": "2026-10-29", "status": "İlk tur.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "osmanli-1520-1566.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
