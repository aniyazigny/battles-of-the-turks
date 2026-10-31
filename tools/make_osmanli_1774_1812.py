"""data/osmanli-1774-1812.json dosyasını üretir (Parti 14: I. Abdülhamid, III. Selim, IV. Mustafa ve II. Mahmud'un ilk yılları, 1774–1812)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "osmanli-1774-1812"
O = "Osmanlı Devleti"
W7 = "Osmanlı–Rus–Avusturya savaşı (1787–1792)"
WF = "Fransa'nın Mısır seferi (1798–1801)"
W8 = "Osmanlı–Rus savaşı (1806–1812)"
WE = "Osmanlı–İngiliz savaşı (1807–1809)"
WK = "Mısır'daki Kölemen beyleri"
WS = "Birinci Sırp isyanı (1804–1813)"
RU, HA, FR, EN = "Rusya", "Habsburglar", "Fransa", "İngiltere"
# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür)
R = [
("Mısır seferi (1786–1787)", "Ottoman expedition to Egypt (1786–1787)", "1787-01-17", WK, "Mısır", 30.05, 31.25, "region", "Mısır",
 O, "Kölemen beyleri (Murad ve İbrâhim Bey)", "Cezayirli Gazi Hasan Paşa", "Murad Bey, İbrâhim Bey", "ic", "C", "kesin",
 ["TDVIA:cezayirli-gazi-hasan-pasa", "TDVIA:ibrahim-bey"], "", "Haziran 1786'da başlayan seferde beyler birkaç defa yenildi; 17 Ocak 1787'deki savaştan sonra az bir maiyetle kaçtılar.",
 "In the campaign begun in June 1786 the beys were beaten several times; after the battle of 17 January 1787 they fled with a small retinue.", "land"),
("Kılburun (1787)", "Battle of Kinburn (1787)", "1787-10", W7, "Kılburun", 46.50, 31.53, "approx", "Ukrayna",
 RU, O, "Özü muhafızı", "", "dis", "L", "borderline",
 ["TDVIA:abdulhamid-i"], "", "Savaş, Özü muhafızının Kılburun'u Ruslardan geri alma hücumuyla başladı; madde sonucu yazmaz, kale Rus elinde kaldı.",
 "The war opened with the attack of the Özi commander to retake Kinburn from the Russians; the article does not give the outcome, and the fort stayed Russian.", "land"),
("Yılan Adası (1788)", "Battle of Fidonisi (1788)", "1788-08", W7, "Yılan adası açıkları", 45.26, 30.20, "approx", "Ukrayna",
 O, RU, "Cezayirli Gazi Hasan Paşa", "", "dis", "W", "kesin",
 ["TDVIA:cezayirli-gazi-hasan-pasa"], "Batı kaynakları bu deniz savaşını (Fidonisi, Temmuz 1788) Rus zaferi sayar.", "Hasan Paşa Rus donanmasını yendi ama Özü'nün düşmesine engel olamadı.",
 "Hasan Pasha beat the Russian fleet but could not prevent the fall of Özi.", "sea"),
("Mehâdiye (1788)", "Battle of Mehadia (1788)", "1788-08", W7, "Mehâdiye", 44.90, 22.36, "approx", "Romanya",
 O, HA, "Koca Yûsuf Paşa, Kethüdâ Hasan Paşa", "", "dis", "W", "kesin",
 ["TDVIA:yusuf-pasa-koca"], "", "", "", "land"),
("Şebeş (1788)", "Battle of Karánsebes (1788)", "1788-09", W7, "Karánşebeş", 45.42, 22.22, "known", "Romanya",
 O, HA, "Koca Yûsuf Paşa, Kethüdâ Hasan Paşa", "", "dis", "W", "kesin",
 ["TDVIA:yusuf-pasa-koca"], "", "Mehâdiye ile birlikte savaşın Avusturya cephesindeki başarıları.", "With Mehadia, the successes of the war on the Austrian front.", "land"),
("Hotin'in kaybı (1788)", "Siege of Khotyn (1788)", "1788-09", W7, "Hotin", 48.52, 26.50, "known", "Ukrayna",
 "Rusya ve Habsburglar", O, "", "", "dis", "L", "kesin",
 ["TDVIA:hotin", "TDVIA:yusuf-pasa-koca"], "", "Avusturya ve Rus kuvvetleri ortaklaşa kuşattı; Yaş'ın da düşmesiyle Boğdan işgal edildi.",
 "Austrian and Russian forces besieged it jointly; with the fall of Iași as well, Moldavia was occupied.", "land"),
("Özü'nün kaybı (1788)", "Siege of Ochakov (1788)", "1788-12", W7, "Özü", 46.61, 31.54, "known", "Ukrayna",
 RU, O, "", "Grigory Potemkin", "dis", "L", "kesin",
 ["TDVIA:cezayirli-gazi-hasan-pasa", "TDVIA:abdulhamid-i", "TDVIA:yusuf-pasa-koca"], "İsmâil maddesi Özü'nün 1789'da düştüğünü yazar; Abdülhamid I maddesine göre haber padişaha Nisan 1789'dan önce ulaşmıştı.",
 "Donanmanın yardımı sığ sahiller yüzünden kaleye ulaşamadı. I. Abdülhamid Özü'nün işgalini bildiren yazıyı okurken felç geçirip öldü (7 Nisan 1789).",
 "Naval relief could not reach the fortress because of the shallow shore. Abdülhamid I suffered a fatal stroke while reading the report of its loss (7 April 1789).", "land"),
("Kalas (1789)", "Battle of Galați (1789)", "1789-05-01", W7, "Kalas", 45.44, 28.05, "known", "Romanya",
 RU, O, "", "", "dis", "L", "kesin",
 ["TDVIA:yusuf-pasa-koca"], "", "", "", "land"),
("Fokşan (1789)", "Battle of Focșani", "1789-08-01", W7, "Fokşan", 45.70, 27.18, "known", "Romanya",
 "Rusya ve Habsburglar", O, "", "Aleksandr Suvorov, Saksonya-Coburg Prensi", "dis", "L", "kesin",
 ["TDVIA:yusuf-pasa-koca", "TDVIA:cezayirli-gazi-hasan-pasa"], "", "", "", "land"),
("Boza (Rimnik) (1789)", "Battle of Rymnik", "1789-09-22", W7, "Rimnik nehri ve Boza suyu", 45.38, 27.05, "approx", "Romanya",
 "Rusya ve Habsburglar", O, "Kethüdâ (Cenaze) Hasan Paşa", "Aleksandr Suvorov, Saksonya-Coburg Prensi", "dis", "L", "kesin",
 ["TDVIA:yusuf-pasa-koca", "TDVIA:cezayirli-gazi-hasan-pasa"], "", "Ordu Remnik nehrini geçerken ve Boza suyu kıyısında ağır bozguna uğradı; serasker azledildi.",
 "The army was routed while crossing the Rymnik and on the Buzău; the commander was dismissed.", "land"),
("İsmâil önü (1789)", "Relief of Izmail (1789)", "1789", W7, "İsmâil", 45.35, 28.84, "known", "Ukrayna",
 O, RU, "Cezayirli Gazi Hasan Paşa", "", "dis", "W", "kesin",
 ["TDVIA:cezayirli-gazi-hasan-pasa"], "", "Serasker Hasan Paşa Rusları kale önünde yenip kuşatmayı kaldırdı; ardından sadrazam oldu (3 Aralık 1789).",
 "Commander Hasan Pasha defeated the Russians before the fortress and lifted the siege; he then became grand vizier (3 December 1789).", "land"),
("Belgrad'ın kaybı (1789)", "Siege of Belgrade (1789)", "1789-10", W7, "Belgrad", 44.82, 20.45, "known", "Sırbistan",
 HA, O, "", "Ernst Gideon von Laudon", "dis", "L", "kesin",
 ["TDVIA:belgrad"], "", "Ziştovi Antlaşması (1791) ile geri verildi.", "Returned by the Treaty of Sistova (1791).", "land"),
("Akkirman'ın kaybı (1789)", "Fall of Akkerman (1789)", "1789-10", W7, "Akkirman", 46.19, 30.35, "known", "Ukrayna",
 RU, O, "", "", "dis", "L", "kesin",
 ["TDVIA:akkirman"], "", "Yaş Antlaşması (1792) ile geri verildi.", "Returned by the Treaty of Jassy (1792).", "land"),
("Bender'in kaybı (1789)", "Fall of Bender (1789)", "1789-11-14", W7, "Bender", 46.83, 29.48, "known", "Moldova",
 RU, O, "", "Grigory Potemkin", "dis", "L", "kesin",
 ["TDVIA:yusuf-pasa-koca", "TDVIA:bender-kalesi"], "", "Kale teslim oldu.", "The fortress surrendered.", "land"),
("İsmâil'in kaybı (1790)", "Siege of Izmail (1790)", "1790-12-22", W7, "İsmâil", 45.35, 28.84, "known", "Ukrayna",
 RU, O, "", "Aleksandr Suvorov", "dis", "L", "kesin",
 ["TDVIA:ismail--ukrayna"], "Koca Yûsuf Paşa maddesi İsmâil'in 11 Ekim 1789'da teslim olduğunu yazar; İsmâil maddesi kalenin 22 Aralık 1790'da düştüğünü söyler.",
 "Yaş Antlaşması ile geri verildi.", "Returned by the Treaty of Jassy.", "land"),
("Anapa (1791)", "Siege of Anapa (1791)", "1791-07-26", W7, "Anapa", 44.89, 37.32, "known", "Rusya",
 RU, O, "", "Ivan Gudovich", "dis", "L", "kesin",
 ["TDVIA:anapa"], "", "Savaş boyunca üç defa kuşatıldı, üçüncüsünde düştü.", "Besieged three times during the war, it fell at the third.", "land"),
("Maçin (1791)", "Battle of Măcin", "1791-07-09", W7, "Maçin", 45.25, 28.14, "known", "Romanya",
 RU, O, "Koca Yûsuf Paşa", "Nikolai Repnin", "dis", "L", "kesin",
 ["TDVIA:yas-antlasmasi", "TDVIA:yusuf-pasa-koca", "TDVIA:osmanlilar", "TDVIA:tepedelenli-ali-pasa"],
 "Tarih maddelerde farklı: Yaş Antlaşması 8 Zilkade 1205 / 9 Temmuz 1791, Osmanlılar 5 Ağustos, Koca Yûsuf Paşa 6 Ağustos 1791 der.",
 "Genel bozgunun ardından ordu savaşmayı reddetti ve mütareke kabul edildi (11 Ağustos 1791).", "After the general rout the army refused to fight on and an armistice was accepted (11 August 1791).", "land"),
("Vidin kuşatması (1798)", "Siege of Vidin (1798)", "1798", "Pazvandoğlu isyanı", "Vidin", 43.99, 22.88, "known", "Bulgaristan",
 "Pazvandoğlu Osman", O, "Küçük Hüseyin Paşa", "Pazvandoğlu Osman", "ic", "C", "kesin",
 ["TDVIA:pazvandoglu-osman", "TDVIA:selim-iii"], "", "Aylarca süren kuşatma hezimetle bitti; Pazvandoğlu'na vezirlik verilerek uzlaşıldı (1799).",
 "The months-long siege ended in failure; a settlement followed, Pazvandoğlu being made a vizier (1799).", "land"),
("Ehramlar (1798)", "Battle of the Pyramids", "1798-07", WF, "Kahire yakını, Piramitler", 29.98, 31.13, "approx", "Mısır",
 FR, O, "Murad Bey", "Napoléon Bonaparte", "dis", "L", "kesin",
 ["TDVIA:ibrahim-bey", "TDVIA:misir"], "", "Fransızlar Temmuz 1798'de İskenderiye'yi aldıktan sonra Murad Bey'in fellâhlardan oluşan ordusunu yendi.",
 "After taking Alexandria in July 1798 the French defeated Murad Bey's army of untrained peasants.", "land"),
("Yafa (1799)", "Siege of Jaffa (1799)", "1799-03", WF, "Yafa", 32.05, 34.75, "known", "İsrail",
 FR, O, "", "Napoléon Bonaparte", "dis", "L", "kesin",
 ["TDVIA:yafa"], "Yafa maddesi işgali 6 Mayıs 1799'a koyar; Akkâ ve Cezzâr maddelerine göre Bonaparte Akkâ'yı 18–19 Mart'ta kuşatmaya başladığından Yafa ondan önce düşmüş olmalı.",
 "Esir alınan 4000 kişi sahilde kurşuna dizildi.", "The 4,000 prisoners were shot on the beach.", "land"),
("Akkâ (1799)", "Siege of Acre (1799)", "1799-05", WF, "Akkâ", 32.92, 35.07, "known", "İsrail",
 O, FR, "Cezzâr Ahmed Paşa", "Napoléon Bonaparte", "dis", "W", "kesin",
 ["TDVIA:cezzar-ahmed-pasa", "TDVIA:akka", "TDVIA:misir"], "", "18–19 Mart'ta başlayan kuşatmada İngiliz donanmasının da yardımıyla direnildi; Bonaparte geri çekildi ve Ağustos'ta Mısır'dan ayrıldı.",
 "The siege begun on 18–19 March was resisted with help from the British fleet; Bonaparte withdrew and left Egypt in August.", "land"),
("Ebûkır (1799)", "Battle of Abukir (1799)", "1799-07-25", WF, "Ebûkır", 31.32, 30.06, "known", "Mısır",
 FR, O, "Köse Mustafa Paşa", "Napoléon Bonaparte", "dis", "L", "kesin",
 ["TDVIA:ebukir"], "", "Karaya çıkan Osmanlı kuvvetleri yenildi ve kale Fransızlara geçti.", "The landed Ottoman force was defeated and the castle passed to the French.", "land"),
("Arîş (1799)", "Siege of El Arish (1799)", "1799-12-28", WF, "Arîş", 31.13, 33.80, "known", "Mısır",
 O, FR, "Sadrazam Yûsuf Ziyâ Paşa", "", "dis", "W", "kesin",
 ["TDVIA:yusuf-ziya-pasa"], "", "", "", "land"),
("Heliopolis (1800)", "Battle of Heliopolis", "1800-03-20", WF, "Heliopolis (Matariye), Kahire'nin kuzeyi", 30.13, 31.31, "approx", "Mısır",
 FR, O, "Sadrazam Yûsuf Ziyâ Paşa", "Jean-Baptiste Kléber", "dis", "L", "kesin",
 ["TDVIA:yusuf-ziya-pasa", "TDVIA:ibrahim-bey"], "", "Fransızlar sadrazamın kuvvetlerini hazırlıksız yakalayıp bozguna uğrattı.", "The French caught the grand vizier's forces unprepared and routed them.", "land"),
("Haneke (1801)", "Battle of El Khanka (1801)", "1801-05-31", WF, "Müneyyer köyü, Haneke yakını", 30.22, 31.37, "approx", "Mısır",
 O, FR, "Sadrazam Yûsuf Ziyâ Paşa", "", "dis", "W", "kesin",
 ["TDVIA:yusuf-ziya-pasa"], "", "Ardından Fransızlar Mısır'ı boşalttı; vali Hüsrev Paşa'ya teslim edildi (Şubat 1802).", "The French then evacuated Egypt, which was handed to Governor Husrev Pasha (February 1802).", "land"),
("Dimyat (1803)", "Battle of Damietta (1803)", "1803-07-04", WK, "Dimyat", 31.42, 31.81, "known", "Mısır",
 "Kölemen beyleri (Berdîsî Osman Bey)", O, "Mısır Valisi Hüsrev Paşa", "Berdîsî Osman Bey", "ic", "C", "kesin",
 ["TDVIA:husrev-pasa-koca"], "", "Yenilen Hüsrev Paşa Dimyat'ı bırakıp kaçtı.", "The defeated Husrev Pasha abandoned Damietta and fled.", "land"),
("Böğürdelen (1806)", "Fall of Šabac (1806)", "1806-01-26", WS, "Böğürdelen (Šabac)", 44.75, 19.70, "known", "Sırbistan",
 "Sırp isyancıları", O, "", "Kara Yorgi", "dis", "L", "kesin",
 ["TDVIA:bogurdelen"], "", "Kale Kara Yorgi'ye teslim edildi.", "The fortress was surrendered to Karađorđe.", "land"),
("Hotin'in kaybı (1806)", "Occupation of Khotyn (1806)", "1806", W8, "Hotin", 48.52, 26.50, "known", "Ukrayna",
 RU, O, "", "", "dis", "L", "borderline",
 ["TDVIA:hotin"], "", "Madde yalnızca işgali anar; savaş ayrıntısı yok.", "The article only mentions the occupation; no battle details.", "land"),
("Akkirman'ın kaybı (1806)", "Fall of Akkerman (1806)", "1806-11-30", W8, "Akkirman", 46.19, 30.35, "known", "Ukrayna",
 RU, O, "", "Prens Kantakuzino", "dis", "L", "kesin",
 ["TDVIA:akkirman"], "", "Tatarlar şehri terk etti; Bükreş Antlaşması (1812) ile Rusya'ya bırakıldı.", "The Tatars abandoned the town; it was ceded to Russia by the Treaty of Bucharest (1812).", "land"),
("Çanakkale Boğazı (1807)", "Duckworth's passage of the Dardanelles (1807)", "1807-02-19", WE, "Çanakkale Boğazı ve İstanbul önü", 40.15, 26.40, "approx", "Türkiye",
 O, EN, "", "John Duckworth", "dis", "W", "borderline",
 ["TDVIA:canakkale-bogazi", "TDVIA:selim-iii", "TDVIA:ebukir"], "", "İngiliz donanması boğazı fazla zorlanmadan geçti ama Şubat sonunda İstanbul önünden sonuç alamadan çekildi.",
 "The British fleet passed the strait without much difficulty but withdrew from before Istanbul at the end of February without result.", "sea"),
("Bozcaada (1807)", "Russian occupation of Tenedos (1807)", "1807-03", W8, "Bozcaada", 39.83, 26.07, "known", "Türkiye",
 RU, O, "", "", "dis", "L", "kesin",
 ["TDVIA:bozcaada", "TDVIA:dervis-mehmed-pasa--19-yy"], "", "İngiliz donanmasıyla birlikte Akdeniz'e gelen Rus donanması Bozcaada önüne demirledi (14 Mart 1807'de dokuz Rus gemisi); Ruslar adayı kısa bir süre işgal etti. (Kontrol turunda eklendi.)",
 "The Russian fleet, which came into the Mediterranean with the British, anchored off Tenedos (nine ships on 14 March 1807); the Russians briefly occupied the island.", "sea"),
("İngilizlerin Mısır seferi (1807)", "Alexandria expedition of 1807", "1807-03", WE, "İskenderiye ve Reşîd", 31.20, 29.92, "approx", "Mısır",
 O, EN, "Kavalalı Mehmed Ali Paşa", "", "dis", "W", "borderline",
 ["TDVIA:iskenderiye", "TDVIA:ebukir", "TDVIA:kavalali-mehmed-ali-pasa"], "", "İskenderiye Mart 1807'de İngilizlere teslim edildi; Mehmed Ali'nin başarısından ve görüşmelerden sonra İngilizler 19 Eylül 1807'de çekildi.",
 "Alexandria was surrendered to the British in March 1807; after Mehmed Ali's success and negotiations they withdrew on 19 September 1807.", "land"),
("Yergöğü (1809)", "Battle of Giurgiu (1809)", "1809-09", W8, "Yergöğü", 43.90, 25.97, "known", "Romanya",
 O, RU, "Sadrazam Yûsuf Ziyâ Paşa", "", "dis", "W", "kesin",
 ["TDVIA:yusuf-ziya-pasa"], "", "", "", "land"),
("İsmâil'in kaybı (1809)", "Fall of Izmail (1809)", "1809", W8, "İsmâil", 45.35, 28.84, "known", "Ukrayna",
 RU, O, "", "", "dis", "L", "borderline",
 ["TDVIA:ismail--ukrayna"], "", "Madde yalnızca işgali anar.", "The article only mentions the occupation.", "land"),
("Silistre (1809)", "Battle of Silistra (1809)", "1809-10-24", W8, "Silistre yakını", 44.12, 27.26, "approx", "Bulgaristan",
 O, RU, "Sadrazam Yûsuf Ziyâ Paşa", "", "dis", "W", "kesin",
 ["TDVIA:yusuf-ziya-pasa"], "", "Ardından ordu kışlamak üzere Şumnu'ya döndü.", "The army then returned to Shumen for the winter.", "land"),
("Varna (1810)", "Siege of Varna (1810)", "1810-06", W8, "Varna", 43.21, 27.92, "known", "Bulgaristan",
 O, RU, "Varna seraskeri Hüsrev Paşa", "Nikolay Kamenski", "dis", "W", "kesin",
 ["TDVIA:varna", "TDVIA:husrev-pasa-koca"], "", "Rus hücumu ağır kayıplarla püskürtüldü.", "The Russian assault was repulsed with heavy losses.", "land"),
("Rusçuk'un kaybı (1810)", "Siege of Ruse (1810)", "1810-09-26", W8, "Rusçuk", 43.85, 25.97, "known", "Bulgaristan",
 RU, O, "", "Nikolay Kamenski", "dis", "L", "kesin",
 ["TDVIA:ruscuk", "TDVIA:yusuf-ziya-pasa"], "Rusçuk maddesi 26 Eylül, Yûsuf Ziyâ Paşa maddesi 25 Eylül 1810 der.",
 "Üç aylık kuşatmadan sonra garnizon ve halkın güvenle çıkması şartıyla teslim oldu.", "After a three-month siege it surrendered on condition that garrison and civilians could leave safely.", "land"),
]

LEFT = [
 {"name": "Kırım'ın ilhakı (1783)", "reason": "Savaşsız ilhak; haritada işlendi.", "source": "TDVIA:yas-antlasmasi"},
 {"name": "Kalafat ve Tendra/Kelegra deniz savaşları (1790–1791)", "reason": "TDVİA'da adıyla bulunamadı.", "source": ""},
 {"name": "Yergöğü'nün kaybı (27 Eylül 1810)", "reason": "Yergöğü maddesi yalnızca tarihini verir; Rusçuk'un kaybıyla aynı harekât.", "source": "TDVIA:yergogu"},
 {"name": "Sırp isyanının diğer savaşları (Belgrad 1806, Mişar, Deligrad, Çegar 1809)", "reason": "İndirilen maddelerde adıyla bulunamadı.", "source": "TDVIA:sirbistan"},
 {"name": "Bozcaada ve Aynaroz deniz savaşları (1807), Arpaçay (1807)", "reason": "TDVİA'da adıyla bulunamadı.", "source": "TDVIA:bozcaada"},
 {"name": "Rusçuk (1811) ve Slobozia kuşatması", "reason": "Rusçuk maddesi 1811 yenilgilerini taraf belirtmeden anar.", "source": "TDVIA:ruscuk"},
 {"name": "Vehhâbîlerin Mekke ve Medine'yi alması (1803–1806)", "reason": "Savaş kaydı yok; Mısır'ın Vehhâbî seferi Parti 15'te.", "source": "TDVIA:selim-iii"},
]

# İkinci kaynak turu
NEW = {  # yeni kayıt: hangi kayıttan sonra gelecek
 "Bender'in kaybı (1789)": ("Yergöğü (1790)", "Battle of Giurgiu (1790)", "1790-06-08", W7, "Yergöğü", 43.90, 25.97, "known", "Romanya",
  O, HA, "", "", "dis", "W", "kesin",
  ["TDVIA:yergogu"], "", "Yergöğü'ne kadar inen Avusturya kuvvetleri geri püskürtüldü; Avusturya ile mütareke de burada yapıldı (19 Eylül 1790).",
  "The Austrian forces that had come down to Giurgiu were driven back; the armistice with Austria was also signed here (19 September 1790).", "land"),
 "Arîş (1799)": ("Dimyat (1799)", "Battle of Damietta (1799)", "1799-10", WF, "Dimyat", 31.42, 31.81, "known", "Mısır",
  FR, O, "", "Jean-Baptiste Kléber", "dis", "L", "kesin",
  ["TDVIA:dimyat"], "", "Karaya çıkan Osmanlı kuvvetleri yenildi.", "The Ottoman landing force was defeated.", "land"),
 "Silistre (1809)": ("İbrâil'in kaybı (1809)", "Siege of Brăila (1809)", "1809-12-02", W8, "İbrâil", 45.27, 27.96, "known", "Romanya",
  RU, O, "", "General Essen", "dis", "L", "kesin",
  ["TDVIA:ibrail"], "", "Kuşatılıp topa tutulan kale yiyecek sıkıntısı yüzünden teslim oldu.", "Besieged and bombarded, the fortress surrendered for lack of food.", "land"),
}
EXTRA_SRC = {"Mehâdiye (1788)": ["TDVIA:hasan-pasa-kethuda"], "Şebeş (1788)": ["TDVIA:hasan-pasa-kethuda"],
 "Özü'nün kaybı (1788)": ["TDVIA:ozu"], "Fokşan (1789)": ["TDVIA:hasan-pasa-kethuda"], "Boza (Rimnik) (1789)": ["TDVIA:hasan-pasa-kethuda"],
 "İsmâil önü (1789)": ["TDVIA:hasan-pasa-kethuda"], "Arîş (1799)": ["TDVIA:aris"], "Dimyat (1803)": ["TDVIA:dimyat"],
 # Akademik ikinci kaynak turu (2026-10-30)
 "Kılburun (1787)": ["AKD:fedakar-2015", "AKD:doganay-2024b"],  # Eylül 1787 çıkarması püskürtüldü; Osmanlı Kılburun'u alamadı
 "İsmâil'in kaybı (1790)": ["AKD:doganay-2024b"],  # 22/23 Aralık 1790 hücumu, serasker Aydoslu Mehmed Paşa şehit
 "Ebûkır (1799)": ["AKD:duzen-2024"],  # 25 Temmuz 1799 hezimeti, Köse Mustafa Paşa esir
 "Hotin'in kaybı (1806)": ["AKD:doganay-2024a"],  # Ruslar savaş ilanından önce Hotin, Bender, Kili ve Akkirman'ı aldı
 "Akkirman'ın kaybı (1806)": ["AKD:doganay-2024a"],
 "İsmâil'in kaybı (1809)": ["AKD:doganay-2024a"],  # üçüncü ve son Rus saldırısı 1809
 "Silistre (1809)": ["AKD:efe-silistre"],  # Pehlivan İbrahim Ağa'nın savunması, Ruslar Silistre önlerinden çekildi
 "Belgrad'ın kaybı (1789)": ["AKD:fedakar-2019"],  # Laudon 11 Eylül 1789'da kuşattı, Osman Paşa kaleyi Ekim 1789'da teslim etti
 "Kalas (1789)": ["AKD:fedakar-2019"],  # sadrazam Yûsuf Paşa Kalas ve Fokşan'da yenildi
 "Yergöğü (1790)": ["TDVIA:zistovi-antlasmasi"]}  # Coburg Yergöğü'nü sıkıştırdı, ağır kayıpla Bükreş'e döndü
EXTRA_SRC.update({"İbrâil'in kaybı (1809)": ["AKD:efe-2006"], "Anapa (1791)": ["AKD:kimya-2019"]})  # Ruslar Temmuz 1791'de aldı, İmam Mansur esir düştü  # akademik tur

FIX = {"Mehâdiye (1788)": {"turkic_cmd": "Vidin seraskeri Hasan Paşa (Kethüdâ), Koca Yûsuf Paşa"},
 "Şebeş (1788)": {"turkic_cmd": "Vidin seraskeri Hasan Paşa (Kethüdâ), Koca Yûsuf Paşa"},
 "Özü'nün kaybı (1788)": {"opp_cmd": "Aleksandr Suvorov",
  "note": "Aralık 1788'deki Rus hücumuna kale müdafileri şiddetli kışın da etkisiyle fazla dayanamadı; Ruslar sivil halkı katletti. Donanmanın yardımı sığ sahiller yüzünden ulaşamamıştı. I. Abdülhamid haberi okurken felç geçirip öldü (7 Nisan 1789).",
  "note_en": "The defenders could not hold out long against the Russian assault of December 1788, made worse by the harsh winter; the Russians massacred the civilians. Naval relief had failed to reach the fort because of the shallow shore. Abdülhamid I suffered a fatal stroke while reading the news (7 April 1789)."},
 "Fokşan (1789)": {"turkic_cmd": "Kemankeş Mustafa Paşa"},
 "Boza (Rimnik) (1789)": {"place": "Rimnik nehri yakını, Martineşti", "turkic_cmd": "Sadrazam Kethüdâ (Cenaze) Hasan Paşa",
  "note": "Fokşan'ın intikamını almak ve Bender ile Akkirman'ı kurtarmak için girişilen harekâtta sadrazam Rimnik nehri yakınında Martineşti'de bozguna uğradı ve azledildi (23 Kasım 1789).",
  "note_en": "In an operation to avenge Focșani and relieve Bender and Akkerman, the grand vizier was routed at Mărtinești near the Rymnik and was dismissed (23 November 1789)."},
 "Arîş (1799)": {"status": "ihtilafli",
  "dispute": "Yûsuf Ziyâ Paşa maddesi sadrazamın 28 Aralık 1799'da Arîş kuşatmasını zaferle bitirdiğini yazar; Arîş maddesi ise Napolyon'un 18 Şubat 1799'da aldığı şehrin 17 Kasım 1799'da özel bir anlaşmayla geri alındığını söyler."},
 "Dimyat (1803)": {"dispute": "Hüsrev Paşa maddesi yenilen paşanın Dimyat'ı bırakıp Abaza Kalesi'ne kaçtığını, Dimyat maddesi ise Dimyat'a sığınıp şehri tahkim ettiğini ve yakalanarak Kahire'ye götürüldüğünü yazar."}}

recs = []
RR = []
for r in R:
    RR.append(r)
    if r[0] in NEW: RR.append(NEW[r[0]])
for i, r in enumerate(RR, 1):
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
    rec["verify"]["academic"] = any(x.startswith("AKD:") for x in rec["sources"])
    recs.append(rec)

pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 14 — Osmanlı: Küçük Kaynarca'dan Bükreş'e (1774–1812)", "compiled": "2026-10-29", "status": "İkinci kaynak turu yapıldı.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "osmanli-1774-1812.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
