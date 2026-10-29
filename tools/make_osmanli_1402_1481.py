"""data/osmanli-1402-1481.json dosyasını üretir (Parti 6: Fetret Devri, II. Murad ve Fâtih dönemi)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "osmanli-1402-1481"
O = "Osmanlı Devleti"
KAR = "Karamanoğulları"
# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en)
R = [
# ---- Fetret Devri (1402-1413): şehzadeler arası iç savaşlar
("Yanbolu (1410)", "Battle of Yambol (1410)", "1410-02-13", "Fetret Devri", "Yanbolu", 42.48, 26.51, "approx", "Bulgaristan",
 "Mûsâ Çelebi", "Emîr Süleyman Çelebi", "Mûsâ Çelebi", "Emîr Süleyman", "ic", "C", "kesin",
 ["TDVIA:musa-celebi", "TDVIA:suleyman-celebi-emir", "TDVIA:mehmed-i"], "", "", ""),
("Süleyman Çelebi'nin Mûsâ'ya zaferleri", "Süleyman's victories over Musa (1410)", "1410-06", "Fetret Devri", "İstanbul önleri ve Edirne yöresi", 41.20, 28.40, "region", "Türkiye",
 "Emîr Süleyman Çelebi", "Mûsâ Çelebi", "Emîr Süleyman", "Mûsâ Çelebi", "ic", "C", "kesin",
 ["TDVIA:suleyman-celebi-emir", "TDVIA:mehmed-i", "TDVIA:musa-celebi"], "", "Mûsâ Haziran 1410'a kadar iki kez yenildi.", "Musa was defeated twice by June 1410."),
("Edirne (1411)", "Battle of Edirne (1411)", "1411", "Fetret Devri", "Edirne yakını", 41.68, 26.56, "approx", "Türkiye",
 "Mûsâ Çelebi", "Emîr Süleyman Çelebi", "Mûsâ Çelebi", "Emîr Süleyman (öldü)", "ic", "C", "kesin",
 ["TDVIA:musa-celebi"], "", "Mûsâ kardeşine ait kuvvetleri yenip Edirne'ye girdi; Süleyman kaçarken öldürüldü.", "Musa defeated his brother's forces and entered Edirne; Süleyman was killed while fleeing."),
("İstanbul kuşatması (1411)", "Siege of Constantinople (1411)", "1411", "Mûsâ Çelebi–Bizans", "İstanbul", 41.01, 28.98, "known", "Türkiye",
 "Bizans", O + " (Mûsâ Çelebi)", "Mûsâ Çelebi", "II. Manuel", "dis", "L", "kesin",
 ["TDVIA:musa-celebi", "TDVIA:istanbul"], "", "Kuşatma sonuç vermedi; Bizans donanması Yassıada yakınında Osmanlı filosunu da bozguna uğrattı.", "The siege failed; the Byzantine fleet also routed the Ottoman squadron near Yassıada."),
("Çamurlu", "Battle of Çamurlu", "1413-07-05", "Fetret Devri", "Çamurlu, Samokov yakını", 42.35, 23.55, "approx", "Bulgaristan",
 "Çelebi Mehmed", "Mûsâ Çelebi", "Çelebi Mehmed", "Mûsâ Çelebi (öldü)", "ic", "C", "kesin",
 ["TDVIA:mehmed-i", "TDVIA:musa-celebi"], "", "Uç beyleri ve vasal devletlerin desteğiyle kazanıldı; Fetret Devri sona erdi.", "Won with the support of the frontier lords and vassal states; the Interregnum ended."),
("Bursa müdafaası (1413)", "Defence of Bursa (1413)", "1413", "Osmanlı–Karamanoğulları", "Bursa", 40.19, 29.06, "known", "Türkiye",
 O, KAR, "", "Karamanoğlu Mehmed Bey", "turk_arasi", "W", "kesin",
 ["TDVIA:mehmed-i"], "", "Karamanlılar mahalleleri yaktı ama otuz bir günlük kuşatmadan sonra Çamurlu haberiyle çekildi.", "The Karamanids burned the suburbs but withdrew after a 31-day siege on news of Çamurlu."),
("Konya (1415)", "Konya campaign (1415)", "1415-03", "Osmanlı–Karamanoğulları", "Konya", 37.87, 32.48, "known", "Türkiye",
 O, KAR, "Çelebi Mehmed", "Karamanoğlu Mehmed Bey", "turk_arasi", "W", "kesin",
 ["TDVIA:mehmed-i"], "", "Karamanlılar yenildi ve Konya kuşatıldı.", "The Karamanids were defeated and Konya was besieged."),
# ---- II. Murad
("Ulubat (Düzmece Mustafa)", "Defeat of Mustafa the Impostor", "1422-01", "Düzmece Mustafa isyanı", "Ulubat", 40.18, 28.43, "approx", "Türkiye",
 "II. Murad", "Düzmece Mustafa", "II. Murad", "Mustafa Çelebi", "ic", "C", "kesin",
 ["TDVIA:murad-ii"], "", "Ulubat köprüsü yıkılınca Mustafa'nın ordusu dağıldı.", "With the Ulubat bridge destroyed, Mustafa's army broke up."),
("İstanbul kuşatması (1422)", "Siege of Constantinople (1422)", "1422-06", "II. Murad–Bizans", "İstanbul", 41.01, 28.98, "known", "Türkiye",
 "Bizans", O, "II. Murad", "II. Manuel", "dis", "L", "kesin",
 ["TDVIA:murad-ii", "TDVIA:istanbul"], "", "Genel taarruz sonuç vermedi; Küçük Mustafa'nın isyanı kuşatmanın kaldırılmasına yol açtı.", "The general assault failed; the revolt of Mustafa the Younger led to the siege being lifted."),
("Antalya müdafaası (1423)", "Defence of Antalya (1423)", "1423-01", "Osmanlı–Karamanoğulları", "Antalya", 36.89, 30.70, "known", "Türkiye",
 O, KAR, "", "Karamanoğlu Mehmed Bey (öldü)", "turk_arasi", "W", "kesin",
 ["TDVIA:murad-ii"], "", "Kuşatan Karamanoğlu Mehmed Bey kaleden atılan bir top güllesiyle öldü.", "The besieging Karamanid Mehmed Bey was killed by a cannonball from the castle."),
("Germe (Hexamilion, 1423)", "Hexamilion (1423)", "1423-05", "II. Murad–Mora", "Korint berzahı", 37.92, 22.98, "approx", "Yunanistan",
 O, "Mora Despotluğu", "Turahan Bey", "", "dis", "W", "kesin",
 ["TDVIA:murad-ii"], "", "Sur zaptedilip Mora'ya girildi.", "The wall was taken and the Morea entered."),
("Pippo'ya karşı (1426)", "Defeat of Pippo Spano (1426)", "1426", "II. Murad–Macaristan", "Tuna boyu", 44.60, 22.00, "region", "Sırbistan",
 O, "Macaristan, Eflak (Dan)", "", "Pippo Spano, Dan", "dis", "W", "borderline",
 ["TDVIA:murad-ii"], "", "Yer ve ayrıntı kaynakta yok.", "Place and detail not given."),
("Güvercinlik (1428)", "Siege of Golubac (1428)", "1428", "II. Murad–Macaristan", "Güvercinlik (Golubac)", 44.66, 21.63, "known", "Sırbistan",
 O, "Macaristan", "Sinan Bey (Vidin uç beyi)", "Sigismund", "dis", "W", "kesin",
 ["TDVIA:murad-ii"], "", "Macar kralı kuşatmayı kaldırdı; kuvvetlerinin önemli bir kısmı Tuna'da boğuldu veya esir düştü.", "The Hungarian king lifted the siege; much of his force drowned in the Danube or was captured."),
("Selânik'in fethi (1430)", "Fall of Thessalonica (1430)", "1430-03-29", "II. Murad–Venedik", "Selânik", 40.64, 22.94, "known", "Yunanistan",
 O, "Venedik", "II. Murad", "", "dis", "W", "kesin",
 ["TDVIA:selanik", "TDVIA:murad-ii"], "", "Bir ay süren şiddetli kuşatmadan sonra alındı; Venedik 1423'ten beri şehri elinde tutuyordu.", "Taken after a fierce month-long siege; Venice had held the city since 1423."),
("Semendire (1439)", "Siege of Smederevo (1439)", "1439-08-27", "II. Murad–Sırbistan", "Semendire", 44.66, 20.93, "known", "Sırbistan",
 O, "Sırp Despotluğu", "II. Murad", "Đurađ Branković", "dis", "W", "kesin",
 ["TDVIA:murad-ii", "TDVIA:mehmed-ii"], "", "", ""),
("Belgrad kuşatması (1440)", "Siege of Belgrade (1440)", "1440", "II. Murad–Macaristan", "Belgrad", 44.82, 20.45, "known", "Sırbistan",
 "Macaristan", O, "II. Murad", "", "dis", "L", "kesin",
 ["TDVIA:murad-ii", "TDVIA:belgrad"], "", "Altı ay süren kuşatma mukavemet ve salgın yüzünden kaldırıldı.", "The six-month siege was lifted because of resistance and an epidemic."),
("Hermannstadt (Sibiu, 1442)", "Battle of Hermannstadt", "1442", "II. Murad–Macaristan", "Erdel", 45.79, 24.15, "region", "Romanya",
 "Macaristan (Yanko)", O, "Mezid Bey", "János Hunyadi", "dis", "L", "borderline",
 ["TDVIA:murad-ii"], "", "TDVİA yalnızca \"Erdel'deki bozgun\"dan söz eder; komutan ve yer Batı kaynaklarındandır.", "TDVİA mentions only 'the rout in Transylvania'; commander and site come from Western sources."),
("Niş (1443)", "Battle of Niš (1443)", "1443-11", "Uzun Sefer (Haçlı)", "Niş yöresi", 43.32, 21.90, "region", "Sırbistan",
 "Haçlılar (Macaristan, Lehistan)", O, "Kasım Paşa", "János Hunyadi, Vladislav", "dis", "L", "borderline",
 ["TDVIA:varna-muharebesi"], "", "Varna maddesi Macarların Tuna'yı aşıp karşılarına çıkan Osmanlı birliklerini yendiğini yazar; yer adı Batı kaynaklarındandır.", "The Varna article says the Hungarians crossed the Danube and defeated the Ottoman units they met; the place name is from Western sources."),
("İzlâdi (Zlatitsa)", "Battle of Zlatitsa", "1443-12", "Uzun Sefer (Haçlı)", "İzlâdi geçidi", 42.71, 24.13, "approx", "Bulgaristan",
 O, "Haçlılar (Macaristan, Lehistan)", "II. Murad", "János Hunyadi", "dis", "W", "ihtilafli",
 ["TDVIA:varna-muharebesi", "TDVIA:gazavat-i-sultan-murad"],
 "TDVİA: Murad Macar birliklerini Zlatitsa geçidinde zorlukla durdurdu. Alternatif okuma: Batı kaynakları Haçlıların geri çekilişi sırasında Kunoviçe'de Osmanlıları yendiğini yazar. Karar [P6]: Osmanlı başarısı.",
 "Gazavât-ı Sultan Murad bu savaşın en ayrıntılı kaynağıdır.", "The Gazavat-i Sultan Murad is the most detailed source for this battle."),
("Varna", "Battle of Varna", "1444-11-10", "Varna Haçlı Seferi", "Varna", 43.21, 27.91, "approx", "Bulgaristan",
 O, "Haçlılar (Macaristan, Lehistan, Eflak)", "II. Murad", "Vladislav (öldü), János Hunyadi", "dis", "W", "kesin",
 ["TDVIA:varna-muharebesi", "TDVIA:gazavat-i-sultan-murad"], "", "Macar ve Leh kralı Vladislav savaşta öldü.", "King Władysław of Hungary and Poland was killed in the battle."),
("Germe (Hexamilion, 1446)", "Hexamilion (1446)", "1446-12", "II. Murad–Mora", "Korint berzahı", 37.92, 22.98, "approx", "Yunanistan",
 O, "Mora Despotluğu", "II. Murad", "Konstantin Palaiologos", "dis", "W", "kesin",
 ["TDVIA:mehmed-ii", "TDVIA:murad-ii"], "", "Despot Konstantin'in yeniden inşa ettirdiği surlar aşıldı.", "The wall rebuilt by Despot Constantine was breached."),
("Kosova (1448)", "Second Battle of Kosovo", "1448-10-17", "II. Murad–Macaristan", "Kosova ovası", 42.70, 21.10, "approx", "Kosova",
 O, "Macaristan (Yanko) ve müttefikleri", "II. Murad, Şehzade Mehmed", "János Hunyadi", "dis", "W", "kesin",
 ["TDVIA:murad-ii", "TDVIA:kosova-savaslari", "TDVIA:mehmed-ii"], "", "Üç gün sürdü (17-20 Ekim 1448). Şehzade Mehmed sağ kolda savaştı.", "It lasted three days (17–20 October 1448). Prince Mehmed fought on the right wing."),
("Akçahisar (Kruya, 1450)", "Siege of Krujë (1450)", "1450", "II. Murad–İskender Bey", "Akçahisar (Kruya)", 41.51, 19.79, "known", "Arnavutluk",
 "İskender Bey", O, "II. Murad", "İskender Bey", "dis", "L", "kesin",
 ["TDVIA:murad-ii", "TDVIA:mehmed-ii"], "", "Yanko'nun yeniden saldıracağı söylentisi üzerine uzayan kuşatma kaldırıldı.", "The prolonged siege was lifted on rumours of a new attack by Hunyadi."),
# ---- II. Mehmed (Fâtih)
("İstanbul'un fethi", "Fall of Constantinople", "1453-05-29", "II. Mehmed–Bizans", "İstanbul", 41.01, 28.98, "known", "Türkiye",
 O, "Bizans", "II. Mehmed", "XI. Konstantinos (öldü)", "dis", "W", "kesin",
 ["TDVIA:istanbul", "TDVIA:mehmed-ii"], "", "Asker şehre top yıktığı gedikten girdi (20 Cemâziyelevvel 857). Bizans İmparatorluğu sona erdi.", "The troops entered through the breach made by the cannon (29 May 1453). The Byzantine Empire ended."),
("Berat (1455)", "Siege of Berat (1455)", "1455-07-26", "II. Mehmed–İskender Bey", "Berat", 40.70, 19.95, "known", "Arnavutluk",
 O, "İskender Bey, Napoli kuvvetleri", "Evrenosoğlu Îsâ Bey", "İskender Bey", "dis", "W", "kesin",
 ["TDVIA:iskender-bey"], "", "Berat'ı kuşatanlar yardıma gelen Osmanlı ordusunca bozuldu; Napoli kuvvetleri ağır kayıp verdi.", "The besiegers of Berat were routed by the relieving Ottoman army; the Neapolitan troops suffered heavily."),
("Belgrad kuşatması (1456)", "Siege of Belgrade (1456)", "1456-07", "II. Mehmed–Macaristan", "Belgrad", 44.82, 20.45, "known", "Sırbistan",
 "Macaristan (Yanko)", O, "II. Mehmed", "János Hunyadi", "dis", "L", "kesin",
 ["TDVIA:mehmed-ii"], "", "Fâtih bozgunu önlemek için savaşa atıldı ve alnından yaralandı.", "The Conqueror threw himself into the fight to prevent a rout and was wounded in the forehead."),
("Albulena", "Battle of Albulena", "1457", "II. Mehmed–İskender Bey", "Albulena", 41.62, 19.85, "approx", "Arnavutluk",
 "İskender Bey", O, "Evrenosoğlu Îsâ Bey", "İskender Bey", "dis", "L", "kesin",
 ["TDVIA:mehmed-ii"], "", "", ""),
("Mora seferi (1460)", "Conquest of the Morea", "1460", "II. Mehmed–Mora", "Mora", 37.50, 22.40, "region", "Yunanistan",
 O, "Mora despotları", "II. Mehmed", "", "dis", "W", "borderline",
 ["TDVIA:mehmed-ii", "TDVIA:mora"], "", "Venedik kaleleri dışında bütün yarımada alındı; tek bir meydan savaşı değil.", "The whole peninsula except the Venetian fortresses was taken; not a single pitched battle."),
("Trabzon'un teslimi", "Fall of Trebizond", "1461-08", "II. Mehmed–Trabzon", "Trabzon", 41.00, 39.72, "known", "Türkiye",
 O, "Trabzon Rum İmparatorluğu", "II. Mehmed", "David Komnenos", "dis", "W", "borderline",
 ["TDVIA:trabzon", "TDVIA:mehmed-ii"], "Tarih: dört ya da altı haftalık kuşatmadan sonra Ağustos veya Eylül 1461.", "Şehir kuşatma sonunda teslim oldu.", "The city surrendered after a siege."),
("Eflak seferi (1462)", "Wallachian campaign (1462)", "1462-06", "II. Mehmed–Eflak", "Eflak", 44.60, 25.60, "region", "Romanya",
 O, "Eflak (Vlad Drakula)", "II. Mehmed", "Vlad III", "dis", "W", "ihtilafli",
 ["TDVIA:mehmed-ii", "AKD:heper-2023"], "TDVİA: Fâtih Eflak'ı istilâ edip Vlad'ı kaçırdı ve yerine Radu'yu getirdi. Alternatif okuma: Batı ve Romen kaynakları Vlad'ın Osmanlı ordugâhına yaptığı gece baskınını öne çıkarır. Karar [P6]: sefer Osmanlı başarısı.",
 "", ""),
("Midilli'nin fethi", "Conquest of Lesbos", "1462-09", "II. Mehmed–Gattilusio", "Midilli", 39.11, 26.56, "known", "Yunanistan",
 O, "Midilli (Gattilusio)", "II. Mehmed", "", "dis", "W", "borderline",
 ["TDVIA:mehmed-ii"], "", "", ""),
("Yayça (Jajce, 1463)", "Siege of Jajce (1463)", "1463-12-16", "II. Mehmed–Macaristan", "Yayça", 44.34, 17.27, "known", "Bosna-Hersek",
 "Macaristan", O, "", "Matyas Korvin", "dis", "L", "kesin",
 ["TDVIA:mehmed-ii"], "", "Bosna'nın fethinden sonra Macar kralı Yayça'yı ele geçirdi.", "After the conquest of Bosnia the Hungarian king took Jajce."),
("Eğriboz", "Siege of Negroponte", "1470-07-12", "II. Mehmed–Venedik", "Eğriboz", 38.46, 23.60, "known", "Yunanistan",
 O, "Venedik", "II. Mehmed, Mahmud Paşa", "", "dis", "W", "kesin",
 ["TDVIA:mehmed-ii"], "", "Ada ile kara arasında köprü kurularak şiddetli bir hücumla alındı.", "Taken by a fierce assault after a bridge was built between the island and the mainland."),
("Karamanoğlu Kasım'ın akını (1470)", "Kasım Bey's raid (1470)", "1470", "Osmanlı–Karamanoğulları", "Ankara yöresi", 39.93, 32.86, "region", "Türkiye",
 KAR, O, "", "Karamanoğlu Kasım Bey", "turk_arasi", "L", "borderline",
 ["TDVIA:mehmed-ii"], "", "Fâtih Eğriboz seferindeyken Kasım Bey mahallî kuvvetleri bozdu.", "While the Conqueror was at Negroponte, Kasım Bey defeated the local forces."),
("Lârende ve Niğde (1471)", "Larende and Niğde (1471)", "1471", "Osmanlı–Karamanoğulları", "Lârende (Karaman)", 37.18, 33.22, "approx", "Türkiye",
 O, KAR, "İshak Paşa", "", "turk_arasi", "W", "borderline",
 ["TDVIA:mehmed-ii"], "", "", ""),
("Fırat kıyısı (öncü yenilgisi, 1473)", "Battle near the Euphrates (1473)", "1473-08-04", "Osmanlı–Akkoyunlu", "Fırat kıyısı, Tercan yöresi", 39.70, 39.70, "region", "Türkiye",
 "Akkoyunlular", O, "Has Murad Paşa", "Uzun Hasan", "dis", "L", "kesin",
 ["TDVIA:uzun-hasan", "TDVIA:otlukbeli-savasi"], "", "Dar bir geçide çekilen Has Murad Paşa'nın birlikleri bozuldu (9 Rebîülevvel 878; Otlukbeli maddesi).", "Has Murad Pasha's units, drawn into a narrow pass, were routed (4 August 1473; Otlukbeli article)."),
("Otlukbeli", "Battle of Otlukbeli", "1473-08-11", "Osmanlı–Akkoyunlu", "Otlukbeli (Başkent), Tercan yakını", 39.78, 40.40, "approx", "Türkiye",
 O, "Akkoyunlular", "II. Mehmed, Şehzade Bayezid", "Uzun Hasan", "dis", "W", "kesin",
 ["TDVIA:otlukbeli-savasi", "TDVIA:uzun-hasan", "TDVIA:mehmed-ii"], "",
 "Osmanlı top ve tüfekleri savaşın kaderini belirledi. Akkoyunlular Türk kökenlidir ama kapsam listesinde değildir; dış rakip sayıldı.",
 "Ottoman cannon and handguns decided the battle. The Aq Qoyunlu were of Turkic origin but outside the scope list, so recorded as external."),
("Karaman seferi (1474)", "Karaman campaign (1474)", "1474", "Osmanlı–Karamanoğulları", "İçel", 36.70, 33.50, "region", "Türkiye",
 O, KAR, "Gedik Ahmed Paşa", "Karamanoğlu Kasım Bey", "turk_arasi", "W", "borderline",
 ["TDVIA:mehmed-ii"], "", "", ""),
("Akdere (Vaslui, 1475)", "Battle of Vaslui", "1475-01", "II. Mehmed–Boğdan", "Boğdan", 46.64, 27.73, "region", "Romanya",
 "Boğdan (Stefan)", O, "Hadım Süleyman Paşa", "III. Stefan", "dis", "L", "kesin",
 ["TDVIA:mehmed-ii"], "", "Rumeli beylerbeyinin ordusu bozguna uğradı (Ramazan 879).", "The army of the governor of Rumelia was routed (January 1475)."),
("Kefe", "Capture of Caffa", "1475-06-06", "II. Mehmed–Ceneviz", "Kefe", 45.03, 35.38, "known", "Ukrayna",
 O, "Cenevizliler", "Gedik Ahmed Paşa", "", "dis", "W", "kesin",
 ["TDVIA:mehmed-ii"], "", "Dört günlük kuşatmadan sonra teslim oldu.", "Surrendered after a four-day siege."),
("Akçahisar (Kruya, 1478)", "Siege of Krujë (1478)", "1478-06-16", "II. Mehmed–Venedik", "Akçahisar (Kruya)", 41.51, 19.79, "known", "Arnavutluk",
 O, "Venedik", "Evrenosoğlu", "", "dis", "W", "kesin",
 ["TDVIA:mehmed-ii"], "", "Abluka sonunda teslim oldu.", "Surrendered after a blockade."),
("Erdel (Ekmezö, 1479)", "Battle of Breadfield", "1479", "II. Mehmed–Macaristan", "Erdel", 45.95, 23.40, "region", "Romanya",
 "Macaristan", O, "", "", "dis", "L", "borderline",
 ["TDVIA:mehmed-ii"], "", "TDVİA yalnızca \"Erdel'de bozguna uğrayan Osmanlı kuvvetleri\"nden söz eder; ad ve tarih Batı kaynaklarındandır.", "TDVİA mentions only 'the Ottoman forces routed in Transylvania'; the name and date are from Western sources."),
("Kefalonya, Zanta ve Ayamavra (1479)", "Ottoman capture of Cephalonia, Zante and Leucas (1479)", "1479", "II. Mehmed–Venedik", "Kefalonya ve Ayamavra", 38.25, 20.50, "region", "Yunanistan",
 O, "Tocco hânedanı (Leonardo III)", "Gedik Ahmed Paşa", "Leonardo Tocco", "dis", "W", "kesin",
 ["TDVIA:ayamavra", "TDVIA:gedik-ahmed-pasa"], "", "Avlonya beyi Gedik Ahmed Paşa idaresindeki donanma Ayamavra'yı Kefalonya ve Zanta ile birlikte ele geçirdi; Leonardo ve Francesca İtalya'ya kaçtı. (Kontrol turunda eklendi.)",
 "The fleet under Gedik Ahmed Pasha, governor of Valona, took Leucas together with Cephalonia and Zante; Leonardo and Francesca fled to Italy."),
("Rodos kuşatması (1480)", "Siege of Rhodes (1480)", "1480-07-28", "II. Mehmed–Rodos şövalyeleri", "Rodos", 36.44, 28.22, "known", "Yunanistan",
 "Rodos şövalyeleri", O, "Mesih Paşa", "Pierre d'Aubusson", "dis", "L", "kesin",
 ["TDVIA:rodos", "TDVIA:mehmed-ii"], "", "Üç aylık kuşatmadan sonra 28 Temmuz'daki son büyük hücum da sonuç vermeyince kaldırıldı.", "After a three-month siege the last great assault on 28 July failed and the siege was lifted."),
("Otranto (1480)", "Capture of Otranto", "1480-08", "II. Mehmed–Napoli", "Otranto", 40.15, 18.49, "known", "İtalya",
 O, "Napoli Krallığı", "Gedik Ahmed Paşa", "", "dis", "W", "kesin",
 ["TDVIA:mehmed-ii"], "", "Güney İtalya'ya çıkarma; şehir alındı.", "A landing in southern Italy; the city was taken."),
("Otranto (1481)", "Siege of Otranto (1481)", "1481-09-10", "Osmanlı–Napoli", "Otranto", 40.15, 18.49, "known", "İtalya",
 "Napoli Krallığı", O, "", "", "dis", "L", "kesin",
 ["TDVIA:mehmed-ii"], "", "Fâtih'in ölümünden sonra ümitsizliğe düşen muhafızlar teslim oldu.", "After the Conqueror's death the despairing garrison surrendered."),
]

OPP_STATE = {r[0]: KAR for r in R if r[13] == "turk_arasi"}
# İkinci kaynak turu (2026-10-29)
EXTRA_SRC = {"Edirne (1411)": ["TDVIA:mehmed-i"], "Bursa müdafaası (1413)": ["TDVIA:karamanogullari"], "Antalya müdafaası (1423)": ["TDVIA:karamanogullari"],
             "Germe (Hexamilion, 1423)": ["TDVIA:mora"], "Niş (1443)": ["TDVIA:macaristan"], "Berat (1455)": ["TDVIA:berat--arnavutluk"],
             "Belgrad kuşatması (1456)": ["TDVIA:macaristan"], "Yayça (Jajce, 1463)": ["TDVIA:bosna-hersek", "TDVIA:macaristan"],
             "Eğriboz": ["TDVIA:egriboz"], "Karaman seferi (1474)": ["TDVIA:karamanogullari"], "Akdere (Vaslui, 1475)": ["TDVIA:bogdan"],
             "Kefe": ["TDVIA:kefe"], "Akçahisar (Kruya, 1478)": ["TDVIA:arnavutluk"], "Otranto (1480)": ["TDVIA:otranto-seferi", "TDVIA:gedik-ahmed-pasa"],
             "Otranto (1481)": ["TDVIA:otranto-seferi"], "İzlâdi (Zlatitsa)": ["TDVIA:macaristan"]}
FIX = {"Edirne (1411)": {"date": "1411-02-17", "note": "Mûsâ âni bir saldırıyla Edirne'yi aldı; Süleyman öldürüldü (22 Şevval 813; Mehmed I maddesi).",
                         "note_en": "Musa took Edirne in a surprise attack; Süleyman was killed (17 February 1411; Mehmed I article)."},
       "İzlâdi (Zlatitsa)": {"result": "D", "dispute": "TDVİA'nın kendi maddeleri çelişiyor: Varna Muharebesi maddesi Murad'ın Macar birliklerini Zlatitsa geçidinde zorlukla durdurduğunu, Macaristan maddesi ise İzlâdi'yi Hunyadi'nin Osmanlılara karşı ilk ciddi başarılarından biri olarak anar. Batı kaynakları da çekilişte Kunoviçe'de Haçlı başarısı yazar. P6 TDVİA'nın kendi içindeki çelişkiyi çözmediği için sonuç belirsiz (D)."},
       "Kefe": {"note": "Gedik Ahmed Paşa 100 parçalık donanmayla gönderildi; Kefe ile birlikte bütün sahil şeridi alındı. Dört günlük kuşatmadan sonra teslim oldu.",
                "note_en": "Gedik Ahmed Pasha was sent with a fleet of 100 ships; Caffa and the whole coastal strip were taken. The city surrendered after a four-day siege."}}
LEFT = [
 {"name": "Novoberda (1413)", "reason": "Mûsâ Çelebi'nin kuşatması; sonucu kaynakta yok.", "source": "TDVIA:musa-celebi"},
 {"name": "Demirkapı (1442), Kunoviçe (1444)", "reason": "TDVİA'da adıyla bulunamadı; kaynakla doğrulanınca eklenecek.", "source": "TDVIA:murad-ii"},
 {"name": "Şeyh Bedreddin ve Börklüce Mustafa isyanları (1416)", "reason": "İç isyanlar; savaşların adı ve yeri bu turda doğrulanmadı.", "source": "TDVIA:mehmed-i"},
 {"name": "Bosna'nın fethi (1463), İşkodra kuşatmaları (1474, 1478–79)", "reason": "Bu turda ayrıntı alınmadı.", "source": "TDVIA:mehmed-ii"},
]

recs = []
for i, r in enumerate(R, 1):
    (ntr, nen, date, war, place, lat, lon, loc, country, sa, sb, tc, oc, cat, res, status, src, disp, note, note_en) = r
    rec = {"id": i, "name_tr": ntr, "name_en": nen, "date": date, "hijri": "", "type": "land", "war": war, "place": place,
           "lat": lat, "lon": lon, "loc": loc, "country": country, "side_a": sa, "side_b": sb, "turkic_cmd": tc, "opp_cmd": oc,
           "category": cat, "result": res, "status": status, "sources": src,
           "verify": {"tdvia": any(s.startswith("TDVIA:") for s in src), "tdvia2": len([s for s in src if s.startswith("TDVIA:")]) >= 2,
                      "wp": False, "rom": "ROM" in src, "academic": any(s.startswith("AKD:") for s in src)},
           "state": O, "home_batch": HB}
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    if ntr in OPP_STATE: rec["opp_state"] = OPP_STATE[ntr]
    rec["sources"] += [x for x in EXTRA_SRC.get(ntr, []) if x not in rec["sources"]]
    rec.update(FIX.get(ntr, {}))
    v = rec["verify"]; srcs = rec["sources"]
    v["tdvia2"] = len([x for x in srcs if x.startswith("TDVIA:")]) >= 2
    v["academic"] = any(x.startswith("AKD:") for x in srcs)
    recs.append(rec)

pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 6 — Osmanlı: Fetret Devri, II. Murad ve Fâtih (1402–1481)", "compiled": "2026-10-29", "status": "İlk tur.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "osmanli-1402-1481.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
