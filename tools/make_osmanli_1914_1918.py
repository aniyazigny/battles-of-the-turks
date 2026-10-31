"""data/osmanli-1914-1918.json dosyasını üretir (Parti 19: Birinci Dünya Savaşı, 1914–1918)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "osmanli-1914-1918"
O = "Osmanlı Devleti"
WD = "Birinci Dünya Savaşı (1914–1918)"
WA = "Şerîf Hüseyin isyanı (1916–1918)"
RU, EN, EF, ER = "Rusya", "İngiltere", "İngiltere ve Fransa", "Ermeni kuvvetleri"
SH = "Şerîf Hüseyin"
MK = "Mustafa Kemal"
KK = "Kâzım Karabekir"
TW = "General Townshend"

# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür)
R = [
("Karadeniz baskını (1914)", "Black Sea raid (1914)", "1914-10", WD, "Sivastopol ve Novorossiysk önleri", 44.60, 33.52, "region", "Ukrayna",
 O, RU, "Amiral Souchon", "", "dis", "W", "kesin",
 ["TDVIA:birinci-dunya-savasi", "TDVIA:enver-pasa"], "",
 "Yavuz ve Midilli dahil Osmanlı donanması 27 Ekim'de Karadeniz'e açılıp Rus gemilerini batırdı, Sivastopol ve Novorossiysk limanlarını topa tuttu; Rusya 2 Kasım'da savaş ilân etti.",
 "The Ottoman fleet, including Yavuz and Midilli, sailed into the Black Sea on 27 October, sank Russian ships and shelled Sevastopol and Novorossiysk; Russia declared war on 2 November.", "sea"),
("Köprüköy (1914)", "Bergmann Offensive (Battle of Köprüköy)", "1914-11-06", WD, "Köprüköy", 39.98, 41.86, "known", "Türkiye",
 O, RU, "Hasan İzzet Paşa (Üçüncü Ordu)", "", "dis", "W", "kesin",
 ["TDVIA:birinci-dunya-savasi", "TDVIA:sarikamis-harekati", "TDVIA:enver-pasa"], "",
 "1 Kasım'da sınırı geçen Ruslar 6–9 Kasım'da Köprüköy'de yenilerek sınır yakınlarına çekildi.",
 "The Russians, who had crossed the border on 1 November, were beaten at Köprüköy on 6–9 November and fell back towards the frontier.", "land"),
("Basra (1914)", "Capture of Basra (1914)", "1914-11-22", WD, "Basra", 30.51, 47.81, "known", "Irak",
 EN, O, "Süleyman Şefik Paşa", "", "dis", "L", "kesin",
 ["TDVIA:basra", "TDVIA:birinci-dunya-savasi"], "Basra maddesi 22 Kasım, Birinci Dünya Savaşı maddesi 23 Kasım 1914 der.",
 "", "", "land"),
("Ardahan (1914)", "Capture of Ardahan (1914)", "1914-12", WD, "Ardahan", 41.11, 42.70, "known", "Türkiye",
 O, RU, "", "", "dis", "W", "kesin",
 ["TDVIA:sarikamis-harekati"], "", "Sarıkamış Harekâtı sırasında Çoruh vadisinden ilerleyen kuvvetler şehri aldı.",
 "Taken by the forces advancing up the Çoruh valley during the Sarıkamış operation.", "land"),
("Sarıkamış (1914–1915)", "Battle of Sarıkamış", "1914-12-22", WD, "Sarıkamış", 40.33, 42.59, "known", "Türkiye",
 RU, O, "Enver Paşa", "General Yudeniç", "dis", "L", "kesin",
 ["TDVIA:sarikamis-harekati", "TDVIA:birinci-dunya-savasi", "TDVIA:enver-pasa", "TDVIA:azerbaycan"],
 "Enver Paşa maddesi 90.000 şehit der; Sarıkamış Harekâtı maddesi bu rakamın doğru olmadığını, Rus defin kayıtlarına göre 23.000, toplamda 30.000 civarında şehit ve 20.000 kadar esir olduğunu yazar.",
 "22 Aralık 1914–4 Ocak 1915 kış taarruzu; Sarıkamış sokaklarına kadar girildiyse de Yudeniç'in 1 Ocak'ta başlattığı kuşatma üzerine 4 Ocak'ta ricat emri verildi. Dokuzuncu Kolordu kumandanı Ali İhsan Paşa karargâhıyla esir düştü.",
 "Winter offensive of 22 December 1914–4 January 1915; the Ottomans reached the streets of Sarıkamış, but after Yudenich's encirclement of 1 January a retreat was ordered on 4 January. IX Corps commander Ali İhsan Pasha was captured with his staff.", "land"),
("Birinci Kanal Harekâtı (1915)", "First Suez offensive (1915)", "1915-02", WD, "Süveyş Kanalı", 30.60, 32.30, "region", "Mısır",
 EN, O, "Cemal Paşa", "", "dis", "L", "kesin",
 ["TDVIA:cemal-pasa", "TDVIA:birinci-dunya-savasi"], "",
 "7 Ocak'ta Bi'rüssebi'de toplanan kuvvetler 14 Ocak'tan itibaren gece yürüyüşleriyle kanala yöneldi; istenen sonuç alınamadı.",
 "Gathered at Beersheba on 7 January, the force marched on the canal by night from 14 January; it failed to achieve its aim.", "land"),
("18 Mart Deniz Muharebesi (1915)", "Naval attack on the Dardanelles (18 March 1915)", "1915-03-18", WD, "Çanakkale Boğazı", 40.10, 26.38, "known", "Türkiye",
 O, EF, "", "", "dis", "W", "kesin",
 ["TDVIA:canakkale-muharebeleri", "TDVIA:birinci-dunya-savasi", "TDVIA:mustafa-kemal-ataturk"], "",
 "Boğaza giren İngiliz ve Fransız filoları tabyaların ateşi ve Karanlık Liman'a dökülen mayınlarla mevcutlarının % 35'ini kaybedip çekildi; Bouvet, Océan ve Irrésistible battı.",
 "The British and French fleets lost 35% of their strength to the forts and the mines laid in Karanlık Liman and withdrew; Bouvet, Océan and Irresistible sank.", "sea"),
("Arıburnu (1915)", "Landing at Anzac Cove", "1915-04-25", WD, "Arıburnu ve Conkbayırı", 40.24, 26.28, "known", "Türkiye",
 O, EN, MK + " (19. Tümen)", "General Hamilton", "dis", "W", "kesin",
 ["TDVIA:canakkale-muharebeleri", "TDVIA:mustafa-kemal-ataturk", "TDVIA:birinci-dunya-savasi"],
 "Çıkarma kuvvetleri dar bir kıyı şeridinde tutunabildi; Türk okumasıyla ilerleyiş durdurulduğu için zafer sayıldı.",
 "Akıntıyla Kabatepe yerine Arıburnu'na çıkan Anzak birliklerine Mustafa Kemal emir beklemeden 57. Alay'la karşı koydu.",
 "Mustafa Kemal, without waiting for orders, met the Anzac troops — carried by the current to Arıburnu instead of Kabatepe — with the 57th Regiment.", "land"),
("Seddülbahir (1915)", "Landing at Cape Helles", "1915-04-25", WD, "Seddülbahir", 40.05, 26.18, "known", "Türkiye",
 O, EF, "", "General Hamilton", "dis", "W", "kesin",
 ["TDVIA:canakkale-muharebeleri"], "Çıkarma kuvvetleri kıyıda tutundu; Türk okumasıyla zafer sayıldı.",
 "Yüzlerce geminin top ateşine rağmen Türk kuvvetleri çıkarmaya yeltenenlere ağır zayiat verdirdi.",
 "Despite fire from hundreds of ships, the Turkish troops inflicted heavy losses on the landing force.", "land"),
("Kerevizdere (1915)", "Battle of Kereves Dere", "1915-06-21", WD, "Kerevizdere", 40.06, 26.24, "known", "Türkiye",
 O, EF, "", "", "dis", "D", "kesin",
 ["TDVIA:canakkale-muharebeleri"], "", "Siper savaşlarının en şiddetli çarpışmalarından biri; madde sonuç vermez.",
 "One of the fiercest clashes of the trench war; the article gives no outcome.", "land"),
("Zığındere (1915)", "Battle of Gully Ravine", "1915-06-28", WD, "Zığındere", 40.07, 26.20, "known", "Türkiye",
 EN, O, "", "", "dis", "L", "kesin",
 ["TDVIA:canakkale-muharebeleri"], "", "Siper savaşlarının en şiddetli çarpışmalarından biri. İngilizler 28 Haziran'da Güney Grubu'nun sağ kanadında mevzi kazandı; kaybedilen mevzileri geri almak için 5 Temmuz'a kadar yapılan Türk karşı taarruzları sonuçsuz kaldı (Özdemir 2024).",
 "One of the fiercest clashes of the trench war. On 28 June the British gained ground on the right flank of the Southern Group; Turkish counter-attacks until 5 July to retake the lost trenches were fruitless (Özdemir 2024).", "land"),
("Anafartalar (1915)", "Battle of Sari Bair and Suvla landing", "1915-08-06", WD, "Anafartalar ve Conkbayırı", 40.26, 26.33, "known", "Türkiye",
 O, EN, "Yarbay " + MK, "", "dis", "W", "kesin",
 ["TDVIA:canakkale-muharebeleri", "TDVIA:cakmak-fevzi"], "",
 "6–7 Ağustos gecesi Suvla'ya çıkan İngilizler dört gün süren muharebeler sonunda Conkbayırı'nda durduruldu. İtilâf kuvvetleri 19–20 Aralık'ta Anafartalar ve Arıburnu'ndan, 8–9 Ocak 1916'da Seddülbahir'den çekildi.",
 "The British who landed at Suvla on the night of 6–7 August were stopped at Conkbayırı after four days of fighting. The Allies left Anafartalar and Arıburnu on 19–20 December and Seddülbahir on 8–9 January 1916.", "land"),
("Kûtülamâre'nin işgali (1915)", "Battle of Es Sinn (1915)", "1915-09-26", WD, "Kûtülamâre", 32.50, 45.82, "known", "Irak",
 EN, O, "Albay Yûsuf Nûreddin Bey", TW, "dis", "L", "kesin",
 ["TDVIA:kutulamare", "TDVIA:birinci-dunya-savasi"], "", "", "", "land"),
("Selmânıpâk (1915)", "Battle of Ctesiphon", "1915-11-22", WD, "Selmânıpâk", 33.09, 44.58, "known", "Irak",
 O, EN, "", TW, "dis", "W", "kesin",
 ["TDVIA:kutulamare", "TDVIA:dadayli-halid-bey"], "Kûtülamâre maddesi 22–26 Kasım 1915 der; Dadaylı Hâlid Bey maddesi muharebeyi 9 Kasım 1915'e koyar (Rumî takvim farkı olabilir).",
 "Bağdat'a 30 km. uzaklıkta çok sayıda kayıp veren İngilizler Kûtülamâre'ye çekildi; Osmanlı kuvvetleri 5 Aralık'ta kaleyi kuşattı.",
 "Thirty kilometres from Baghdad, the British suffered heavy losses and fell back on Kut; the Ottomans besieged the fortress on 5 December.", "land"),
("Erzurum (1916)", "Erzurum offensive (1916)", "1916-02-16", WD, "Erzurum", 39.90, 41.27, "known", "Türkiye",
 RU, O, "", "", "dis", "L", "kesin",
 ["TDVIA:erzurum"], "", "", "", "land"),
("Muş (1916)", "Russian capture of Muş (1916)", "1916-02-18", WD, "Muş", 38.75, 41.50, "known", "Türkiye",
 RU, O, "", "", "dis", "L", "kesin",
 ["TDVIA:mus"], "", "", "", "land"),
("Bitlis (1916)", "Russian capture of Bitlis (1916)", "1916-03-01", WD, "Bitlis", 38.40, 42.11, "known", "Türkiye",
 RU, O, "", "", "dis", "L", "kesin",
 ["TDVIA:bitlis"], "", "", "", "land"),
("Felâhiye (1916)", "Battles of Fallahiyah (1916)", "1916-04-05", WD, "Felâhiye", 32.55, 46.10, "approx", "Irak",
 O, EN, "", "General Percy Lake", "dis", "W", "kesin",
 ["TDVIA:kutulamare"], "", "Kûtülamâre'deki kuşatmayı yarmak için 5 Nisan'da başlayan dört günlük İngiliz taarruzu ve 21–22 Nisan'daki IV. Felâhiye saldırısı püskürtüldü.",
 "The four-day British offensive of 5 April to break the siege of Kut, and the fourth Fallahiyah attack of 21–22 April, were both repulsed.", "land"),
("Trabzon (1916)", "Trebizond campaign (1916)", "1916-04-18", WD, "Trabzon", 41.00, 39.72, "known", "Türkiye",
 RU, O, "", "", "dis", "L", "kesin",
 ["TDVIA:trabzon"], "", "Ruslar 14 Nisan'da Karadere savunma hattını yarıp 18 Nisan'da şehre girdi; işgal 24 Şubat 1918'e kadar sürdü.",
 "The Russians broke the Karadere line on 14 April and entered the city on 18 April; the occupation lasted until 24 February 1918.", "land"),
("Kûtülamâre kuşatması (1915–1916)", "Siege of Kut", "1916-04-29", WD, "Kûtülamâre", 32.50, 45.82, "known", "Irak",
 O, EN, "Halil Paşa", TW, "dis", "W", "kesin",
 ["TDVIA:kutulamare", "TDVIA:birinci-dunya-savasi", "TDVIA:dadayli-halid-bey"],
 "Kûtülamâre maddesi teslimi 29 Nisan, Birinci Dünya Savaşı maddesi 28 Nisan 1916'ya koyar.",
 "Beş ay süren kuşatmadan sonra 13.309 kişilik İngiliz ordusu kayıtsız şartsız teslim alındı.",
 "After a five-month siege the 13,309-strong British army surrendered unconditionally.", "land"),
("Medine (1916)", "Arab attack on Medina (1916)", "1916-06-05", WA, "Medine", 24.47, 39.61, "known", "Suudi Arabistan",
 O, SH, "Fahreddin Paşa", "Şerîf Hüseyin'in oğulları", "ic", "C", "kesin",
 ["TDVIA:medine", "TDVIA:fahreddin-pasa"], "",
 "Şerîf Hüseyin ve dört oğlu 3 Haziran'da demiryolu ve telgraf hatlarını tahrip edip 5–6 Haziran'da Medine karakollarına saldırdı; Fahreddin Paşa saldırıyı püskürttü.",
 "Sharif Husayn and his four sons cut the railway and telegraph on 3 June and attacked Medina's outposts on 5–6 June; Fahreddin Pasha drove them off.", "land"),
("Bi'riali (1916)", "Battle of Bir Ali (1916)", "1916-06-27", WA, "Bi'riali, el-İlâve ve Bi'rimâşî", 24.41, 39.54, "region", "Suudi Arabistan",
 O, SH, "Fahreddin Paşa", "", "ic", "C", "kesin",
 ["TDVIA:fahreddin-pasa"], "", "", "", "land"),
("Mekke (1916)", "Battle of Mecca (1916)", "1916-06", WA, "Mekke", 21.42, 39.83, "known", "Suudi Arabistan",
 SH, O, "", SH, "ic", "C", "kesin",
 ["TDVIA:mekke", "TDVIA:birinci-dunya-savasi"], "Mekke ve Birinci Dünya Savaşı maddeleri isyanı 27 Haziran 1916'ya, Medine ve Fahreddin Paşa maddeleri 3 Haziran 1916'ya koyar.",
 "Şerîf Hüseyin Cidde valisi ve diğer Osmanlı idarecilerinin faaliyetlerini engelleyip Mekke'ye hâkim oldu.",
 "Sharif Husayn thwarted the governor of Jeddah and the other Ottoman officials and took control of Mecca.", "land"),
("Muş'un kurtarılışı (1916)", "Ottoman recapture of Muş (1916)", "1916-07-26", WD, "Muş", 38.75, 41.50, "known", "Türkiye",
 O, RU, "", "", "dis", "W", "kesin",
 ["TDVIA:mus"], "", "Şehir 1 Mayıs 1917'de kesin olarak Rus işgalinden kurtarıldı.",
 "The town was finally freed from Russian occupation on 1 May 1917.", "land"),
("İkinci Kanal Harekâtı (1916)", "Battle of Romani", "1916-07", WD, "Sina yarımadası", 31.00, 32.65, "approx", "Mısır",
 EN, O, "Cemal Paşa (Dördüncü Ordu)", "", "dis", "L", "kesin",
 ["TDVIA:cemal-pasa"], "", "İstenen sonuç alınamadı.", "The offensive failed.", "land"),
("Bitlis'in kurtarılışı (1916)", "Ottoman recapture of Bitlis (1916)", "1916-08-08", WD, "Bitlis", 38.40, 42.11, "known", "Türkiye",
 O, RU, "", "", "dis", "W", "borderline",
 ["TDVIA:bitlis"], "", "Bitlis maddesi yalnızca Rus işgalinin 8 Ağustos 1916'da sona erdiğini yazar; çatışma ayrıntısı yok.",
 "The Bitlis article only says the Russian occupation ended on 8 August 1916; no fighting is described.", "land"),
("Tâif (1916)", "Siege of Taif (1916)", "1916-09-17", WA, "Tâif", 21.27, 40.42, "known", "Suudi Arabistan",
 SH, O, "", "", "ic", "C", "kesin",
 ["TDVIA:taif"], "", "", "", "land"),
("Kûtülamâre (1917)", "Second Battle of Kut", "1917-02", WD, "Kûtülamâre", 32.50, 45.82, "known", "Irak",
 EN, O, "", "", "dis", "L", "kesin",
 ["TDVIA:kutulamare"], "", "", "", "land"),
("Bağdat (1917)", "Fall of Baghdad (1917)", "1917-03-11", WD, "Bağdat", 33.34, 44.40, "known", "Irak",
 EN, O, "", "", "dis", "L", "kesin",
 ["TDVIA:birinci-dunya-savasi", "TDVIA:musul--irak"], "", "", "", "land"),
("Gazze (1917)", "Third Battle of Gaza", "1917-10-31", WD, "Gazze", 31.50, 34.47, "known", "Filistin",
 EN, O, "Mareşal Falkenhayn (Yıldırım Orduları Grubu)", "General Allenby", "dis", "L", "kesin",
 ["TDVIA:birinci-dunya-savasi", "TDVIA:gazze"], "", "Allenby 31 Ekim'de Yıldırım Orduları Grubu'na karşı taarruz başlattı ve Gazze'yi aldı.",
 "Allenby attacked the Yıldırım Army Group on 31 October and took Gaza.", "land"),
("Kudüs (1917)", "Fall of Jerusalem (1917)", "1917-12-09", WD, "Kudüs", 31.78, 35.22, "known", "İsrail",
 EN, O, "Mareşal Falkenhayn (Yıldırım Orduları Grubu)", "General Allenby", "dis", "L", "kesin",
 ["TDVIA:birinci-dunya-savasi", "TDVIA:kudus", "TDVIA:gazze"], "", "Kudüs'teki yaklaşık dört asırlık Osmanlı yönetimi sona erdi.",
 "Nearly four centuries of Ottoman rule in Jerusalem came to an end.", "land"),
("Erzurum'un kurtarılışı (1918)", "Ottoman recapture of Erzurum (1918)", "1918-03-12", WD, "Erzurum", 39.90, 41.27, "known", "Türkiye",
 O, ER, KK, "", "dis", "W", "kesin",
 ["TDVIA:erzurum", "TDVIA:birinci-dunya-savasi"], "", "Rus ordusu ihtilâlden sonra cepheyi bırakınca şehir Ermeni kuvvetlerinden kurtarıldı.",
 "After the Russian army left the front following the revolution, the city was taken back from Armenian forces.", "land"),
("Van'ın kurtarılışı (1918)", "Ottoman recapture of Van (1918)", "1918-04-02", WD, "Van", 38.50, 43.38, "known", "Türkiye",
 O, ER, "", "", "dis", "W", "kesin",
 ["TDVIA:van"], "", "", "", "land"),
("Tuzhurmatu (1918)", "Battle of Tuz Khurmatu", "1918-04", WD, "Tuzhurmatu", 34.88, 44.63, "known", "Irak",
 EN, O, "", "", "dis", "L", "kesin",
 ["TDVIA:kerkuk"], "", "Bozguna uğrayan Osmanlı birlikleri Kerkük'e çekildi.", "The routed Ottoman units fell back on Kirkuk.", "land"),
("Kars (1918)", "Ottoman recapture of Kars (1918)", "1918-04-25", WD, "Kars", 40.60, 43.10, "known", "Türkiye",
 O, ER, KK, "", "dis", "W", "kesin",
 ["TDVIA:kazim-karabekir"], "", "Brest-Litovsk Antlaşması ile Ruslar'ın bıraktığı Elviye-i Selâse'yi almak için yürütülen harekât.",
 "Part of the advance to take the three provinces (Kars, Ardahan, Batum) given up by Russia at Brest-Litovsk.", "land"),
("Gümrü (1918)", "Ottoman capture of Alexandropol (1918)", "1918-05-15", WD, "Gümrü", 40.79, 43.85, "known", "Ermenistan",
 O, ER, KK, "", "dis", "W", "kesin",
 ["TDVIA:kazim-karabekir"], "", "", "", "land"),
("Bakü (1918)", "Battle of Baku", "1918-09-15", WD, "Bakü", 40.41, 49.87, "known", "Azerbaycan",
 O, "Bakü'deki Rus ve Ermeni kuvvetleri", "Nûri Paşa (Kafkas İslâm Ordusu)", "", "dis", "W", "kesin",
 ["TDVIA:azerbaycan"], "Azerbaycan maddesi şehrin Ruslar'ın elinden alındığını yazar; Bakü maddesi şehrin 1917 ihtilâlinden sonra İngilizler'ce işgal edildiğini yazar.",
 "Azerbaycan maddesine göre Sovyetler şehre bolşevik ve Ermeniler'in yardımıyla Mart 1918'de hâkim olmuştu.",
 "According to the Azerbaijan article the Soviets had taken control of the city with Bolshevik and Armenian help in March 1918.", "land"),
("Şam (1918)", "Capture of Damascus (1918)", "1918-10-01", WD, "Şam", 33.51, 36.29, "known", "Suriye",
 EN, O, "", "", "dis", "L", "kesin",
 ["TDVIA:birinci-dunya-savasi", "TDVIA:sam--suriye"], "", "Osmanlı kuvvetleri Suriye'yi boşalttı; şehir İngiliz ordusuna bağlı Avustralya birliklerince alındı, Faysal 3 Ekim'de şehre geldi.",
 "The Ottomans evacuated Syria; the city was taken by Australian units of the British army, and Faisal arrived on 3 October.", "land"),
("Halep (1918)", "Capture of Aleppo (1918)", "1918-10-27", WD, "Halep", 36.20, 37.16, "known", "Suriye",
 "İngiltere ve Araplar", O, "Cemal Paşa (Dördüncü Ordu)", "", "dis", "L", "kesin",
 ["TDVIA:halep"], "", "Cemal Paşa başarısız savunma teşebbüslerinden vazgeçip çekildi; şehir önce Arap kuvvetleri, ardından İngilizler tarafından işgal edildi.",
 "Cemal Pasha gave up his failing defence and withdrew; the city was occupied first by Arab forces, then by the British.", "land"),
("Kerkük (1918)", "British capture of Kirkuk (1918)", "1918-10-28", WD, "Kerkük", 35.47, 44.39, "known", "Irak",
 EN, O, "", "", "dis", "L", "kesin",
 ["TDVIA:kerkuk"], "", "İngiliz hücumları üzerine Osmanlı birlikleri şehri boşaltıp Altınköprü'ye çekildi.",
 "Under British attack the Ottoman units evacuated the town and fell back to Altınköprü.", "land"),
]

LEFT = [
    {"name": "Çanakkale tabyalarının bombardımanları (3 Kasım 1914, 19 Şubat–Mart 1915)", "reason": "Muharebe değil, uzak bombardıman; sonuç yok.", "source": "TDVIA:canakkale-muharebeleri"},
    {"name": "Arıburnu'nda 27 Nisan 1915 Türk taarruzu ve diğer siper savaşları", "reason": "Madde sonuç vermez; büyük muharebeler ayrı kayıt.", "source": "TDVIA:canakkale-muharebeleri"},
    {"name": "Van 1915 (Ermeni isyanı ve Rus işgali)", "reason": "Van maddesi kuşatmayı anar; Rus işgalinin tarihi ve muharebe ayrıntısı yok.", "source": "TDVIA:van"},
    {"name": "İran harekâtı ve Hemedan (1916–1917)", "reason": "Sâbis maddesi Hemedan'ın zaptını terfi tarihiyle (1917) anar; muharebe tarihi yok.", "source": "TDVIA:sabis-ali-ihsan"},
    {"name": "Şeria muharebeleri (1918)", "reason": "Çakmak maddesi başarıları toplu anar.", "source": "TDVIA:cakmak-fevzi"},
    {"name": "Galiçya, Romanya ve Makedonya cephelerindeki Türk kolorduları", "reason": "Birinci Dünya Savaşı maddesi toplu anar; muharebe adı yok.", "source": "TDVIA:birinci-dunya-savasi"},
    {"name": "Filistin cephesinin çöküşü (Nablus, Eylül 1918)", "reason": "Nablus maddesi yalnızca Osmanlı hâkimiyetinin 1918'de sona erdiğini yazar.", "source": "TDVIA:nablus"},
    {"name": "Tebriz (Haziran 1918)", "reason": "Azerbaycan maddesi yalnızca şehre girildiğini yazar; çatışma yok.", "source": "TDVIA:azerbaycan"},
    {"name": "Musul'un işgali (Kasım 1918) ve Medine'nin teslimi (1919)", "reason": "Mondros Mütarekesi'nden sonra.", "source": "TDVIA:musul--irak"},
]

# İkinci kaynak turu.
EXTRA_SRC = {
    "Kerevizdere (1915)": ["TDVIA:cakmak-fevzi", "TDVIA:kazim-karabekir"],
    "Mekke (1916)": ["TDVIA:serif-huseyin", "TDVIA:fahreddin-pasa"],
    "Tâif (1916)": ["TDVIA:serif-huseyin", "TDVIA:fahreddin-pasa"],
    "Kudüs (1917)": ["TDVIA:osmanlilar"],
    "Bağdat (1917)": ["TDVIA:osmanlilar"],
    "Kars (1918)": ["TDVIA:kars"],
    "Şam (1918)": ["TDVIA:osmanlilar"],
    "Halep (1918)": ["TDVIA:osmanlilar"],
    # Akademik ikinci kaynak turu (2026-10-30)
    "Erzurum (1916)": ["AKD:capak-2014"],  # Ruslar 16 Şubat 1916'da Erzurum'u aldı
    "Muş (1916)": ["AKD:capak-2014"],  # 17 Şubat 1916
    "Bitlis (1916)": ["AKD:capak-2014"],  # 3 Mart 1916
    "Muş'un kurtarılışı (1916)": ["AKD:capak-2014"],  # 7 Ağustos 1916
    "Bitlis'in kurtarılışı (1916)": ["AKD:capak-2014"],  # 8 Ağustos 1916 (Mustafa Kemal'in telgrafı)
    "Trabzon (1916)": ["AKD:caykiran-2021"],  # işgal 8 Nisan 1916 – 24 Şubat 1918
    "Kûtülamâre (1917)": ["AKD:atabey-2019"],  # Kût 24 Şubat 1917'de düştü
    "Bakü (1918)": ["AKD:ak-2019"],  # Sabah, 17 Eylül 1918: "Bakü Zabt İdildi"
    "İkinci Kanal Harekâtı (1916)": ["AKD:atabey-2020"],  # 4-5 Ağustos 1916 Romani, Murray'ın Mısır Sefer Kuvveti büyük bir yenilgi verdi
    "Van'ın kurtarılışı (1918)": ["AKD:kardas-2015"],  # Türk ordusu 2 Nisan 1918'de harabe haldeki şehre girdi
    "Zığındere (1915)": ["AKD:ozdemir-2024"],  # 28 Haziran taarruzu; mevzileri geri alma denemeleri 5 Temmuz'a kadar sonuçsuz kaldı
    # Akademik tur (2026-10-31)
    "Ardahan (1914)": ["AKD:cevizliler-ozyurek-2019", "AKD:sadigov-2019"],  # Halid Bey 29 Aralık akşamı girdi; Ruslar 3 Ocak 1915'te geri aldı
    "Gümrü (1918)": ["AKD:bal-gumru"],  # 15 Mayıs muharebesi, 1. Kafkas Kolordusu
}
FIX = {
    "Ardahan (1914)": {
        "note": "Halid Bey (Karsıalan) kumandasındaki kuvvetler 29 Aralık 1914 akşamı şehre girdi; nizami kuvvetlerin kaybı 146 şehit ve 404 yaralıydı. Ruslar 3 Ocak 1915'te şehri geri aldı.",
        "note_en": "Forces under Halid Bey (Karsıalan) entered the town on the evening of 29 December 1914, the regular troops losing 146 killed and 404 wounded. The Russians retook it on 3 January 1915."},
    "İkinci Kanal Harekâtı (1916)": {"date": "1916-08-04"},
    "Kerevizdere (1915)": {"result": "W", "side_b": "Fransa",
        "note": "Fevzi (Çakmak) Bey'in tümeni Kerevizdere ve Kanlıdere mevzilerini başarıyla savundu; Kâzım Karabekir maddesi burada Fransızlar'a karşı savaşıldığını yazar.",
        "note_en": "Fevzi (Çakmak) Bey's division successfully held the Kereves Dere and Kanlıdere positions; the Kâzım Karabekir article says the fighting there was against the French."},
    "Mekke (1916)": {"date": "1916-07-07",
        "dispute": "Fahreddin Paşa maddesi âsilerin 9 Haziran'da genel saldırıya geçip 7 Temmuz'da Mekke'ye girdiğini yazar; Mekke ve Birinci Dünya Savaşı maddeleri isyanı 27 Haziran'a, Medine maddesi 3 Haziran'a koyar."},
    "Tâif (1916)": {"dispute": "Tâif ve Şerîf Hüseyin maddeleri 17 Eylül, Fahreddin Paşa maddesi 22 Eylül 1916 der."},
    "Kudüs (1917)": {"dispute": "Birinci Dünya Savaşı maddesi Allenby'nin 9 Aralık'ta Kudüs'e girdiğini, Osmanlılar maddesi şehrin 11 Aralık 1917'de düştüğünü yazar."},
    "Kars (1918)": {"dispute": "Kâzım Karabekir maddesi 25 Nisan, Kars maddesi 23 Nisan 1918 der."},
    "Bitlis (1916)": {"dispute": "Çapak 2014 (Azizan Şehitliği kitabesine dayanarak) 3 Mart 1916 der; kayıttaki 1 Mart TDVİA Bitlis maddesine göredir."},
    "Trabzon (1916)": {"dispute": "Çaykıran 2021 işgalin başlangıcını 8 Nisan 1916 verir (muhtemelen Rumî/Jülyen takvim farkı); TDVİA 18 Nisan der."},
}
NEW = {
    "Medine (1916)": [
        ("Cidde (1916)", "Battle of Jeddah (1916)", "1916-06-16", WA, "Cidde", 21.49, 39.19, "known", "Suudi Arabistan",
         SH, O, "", "", "ic", "C", "kesin",
         ["TDVIA:serif-huseyin", "TDVIA:fahreddin-pasa"], "", "Âsiler 9 Haziran'da genel saldırıya geçti; Fahreddin Paşa maddesi bunu Mekke Valisi Galib Paşa'nın tedbirsizliğine bağlar.",
         "The rebels launched a general attack on 9 June; the Fahreddin Pasha article blames the carelessness of Galib Pasha, governor of Mecca.", "land"),
    ],
}
RR = []
for r in R:
    RR.append(r)
    RR.extend(NEW.get(r[0], []))

recs = []
for i, r in enumerate(RR, 1):
    (ntr, nen, date, war, place, lat, lon, loc, country, sa, sb, tc, oc, cat, res, status, src, disp, note, note_en, typ) = r
    src = src + [x for x in EXTRA_SRC.get(ntr, []) if x not in src]
    fx = dict(FIX.get(ntr, {}))
    disp, note, note_en = fx.pop("dispute", disp), fx.pop("note", note), fx.pop("note_en", note_en)
    date, sb, res = fx.pop("date", date), fx.pop("side_b", sb), fx.pop("result", res)
    assert not fx, (ntr, fx)
    rec = {"id": i, "name_tr": ntr, "name_en": nen, "date": date, "hijri": "", "type": typ, "war": war, "place": place,
           "lat": lat, "lon": lon, "loc": loc, "country": country, "side_a": sa, "side_b": sb, "turkic_cmd": tc, "opp_cmd": oc,
           "category": cat, "result": res, "status": status, "sources": src,
           "verify": {"tdvia": True, "tdvia2": len([s for s in src if s.startswith("TDVIA:")]) >= 2, "wp": False, "rom": False, "academic": any(s.startswith("AKD:") for s in src)},
           "state": O, "home_batch": HB}
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    recs.append(rec)

dates = [r["date"] + ("-15" if len(r["date"]) == 7 else "") for r in recs]
assert dates == sorted(dates), [d for a, d in zip(dates, dates[1:]) if d < a]
pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 19 — Osmanlı: Birinci Dünya Savaşı (1914–1918)", "compiled": "2026-10-30", "status": "İkinci kaynak turu yapıldı.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "osmanli-1914-1918.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
