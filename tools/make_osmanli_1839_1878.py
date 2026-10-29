"""data/osmanli-1839-1878.json dosyasını üretir (Parti 16: Tanzimat'tan Berlin'e, 1839–1878)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "osmanli-1839-1878"
O = "Osmanlı Devleti"
WM = "Mehmed Ali Paşa isyanı (1831–1840)"
WK = "Karadağ savaşları (1852–1862)"
WC = "Kırım Savaşı (1853–1856)"
WG = "Girit isyanı (1866–1869)"
WY = "Asîr ve Yemen harekâtı (1869–1872)"
WB = "Hersek isyanı ve Sırp-Karadağ savaşı (1875–1876)"
WR = "Osmanlı–Rus savaşı (Doksanüç Harbi, 1877–1878)"
RU = "Rusya"
MI = "Mısır Valisi Mehmed Ali Paşa kuvvetleri"
KD = "Karadağ"
OM = "Ömer Lutfi Paşa"
AMP = "Gazi Ahmed Muhtar Paşa"
OP = "Gazi Osman Paşa"
OA = "Osmanlı Devleti, İngiltere ve Avusturya"

# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür)
R = [
("Beyrut (1840)", "Bombardment of Beirut (1840)", "1840", WM, "Beyrut", 33.90, 35.50, "known", "Lübnan",
 OA, MI, "", "İbrâhim Paşa (Kavalalı)", "ic", "C", "kesin",
 ["TDVIA:beyrut", "TDVIA:kavalali-mehmed-ali-pasa"], "",
 "Londra Antlaşması'nın (15 Temmuz 1840) reddedilmesi üzerine Osmanlı, İngiliz ve Avusturya donanması şehri bombalayıp aldı; Sayda ve Hayfa da ele geçirildi.",
 "After the Treaty of London (15 July 1840) was rejected, the Ottoman, British and Austrian fleet bombarded and took the city; Sidon and Haifa were also taken.", "sea"),
("Akkâ (1840)", "Bombardment of Acre (1840)", "1840", WM, "Akkâ", 32.92, 35.07, "known", "İsrail",
 OA, MI, "", "", "ic", "C", "kesin",
 ["TDVIA:akka", "TDVIA:filistin"], "",
 "Sur ve Sayda'dan sonra Mehmed Ali Paşa'nın bölgedeki son dayanağı olan Akkâ yeniden Osmanlı yönetimine girdi.",
 "After Tyre and Sidon, Acre, Muhammad Ali's last stronghold in the region, returned to Ottoman rule.", "sea"),
("Olteniçe (1853)", "Battle of Oltenița", "1853-11-05", WC, "Olteniçe (Oltenița)", 44.09, 26.64, "known", "Romanya",
 O, RU, OM, "", "dis", "W", "kesin",
 ["TDVIA:omer-lutfi-pasa", "TDVIA:mehmed-ali-pasa-musir"],
 "Ömer Lutfi Paşa maddesi 5 Kasım 1853, Müşir Mehmed Ali Paşa maddesi 2 Kasım 1853 der.",
 "Ömer Paşa Tuna'yı geçip Rusların saldırı planını boşa çıkardı.", "Omar Pasha crossed the Danube and thwarted the Russian plan of attack.", "land"),
("Sinop (1853)", "Battle of Sinop", "1853-11-30", WC, "Sinop limanı", 42.02, 35.15, "known", "Türkiye",
 RU, O, "", "", "dis", "L", "kesin",
 ["TDVIA:sinop"],
 "Sinop maddesi baskını \"1854 yılı başlarına\" koyar. Savaş 4 Ekim 1853'te ilân edilmişti; genel kabul gören tarih 30 Kasım 1853'tür. TDVİA'da ikinci bir madde bulunamadı.",
 "Limandaki Osmanlı donanması Rus baskınına uğradı; on iki gemi battı, 2000'den fazla asker şehid düştü.",
 "The Ottoman squadron in the harbour was attacked by the Russian fleet; twelve ships were sunk and more than 2,000 men killed.", "sea"),
("Çatana (1854)", "Battle of Cetate", "1854-01-05", WC, "Çatana (Cetate), Kalafat yakını", 44.10, 23.05, "approx", "Romanya",
 O, RU, OM, "", "dis", "W", "kesin",
 ["TDVIA:omer-lutfi-pasa"], "", "Bu zaferden sonra Ömer Paşa'ya \"serdâr-ı ekrem\" unvanı verildi.",
 "After this victory Omar Pasha was given the title serdar-ı ekrem.", "land"),
("Rusçuk (1854)", "Siege of Ruse (1854)", "1854-01", WC, "Rusçuk", 43.85, 25.97, "known", "Bulgaristan",
 O, RU, "", "", "dis", "W", "kesin",
 ["TDVIA:ruscuk"], "", "Kuşatılıp bombardıman edilen şehir ele geçirilemedi.", "Besieged and bombarded, the town was not taken.", "land"),
("Silistre (1854)", "Siege of Silistra (1854)", "1854-06-25", WC, "Silistre", 44.12, 27.26, "known", "Bulgaristan",
 O, RU, "", "", "dis", "W", "kesin",
 ["TDVIA:silistre", "TDVIA:mehmed-ali-pasa-musir"], "",
 "15 Mayıs'ta başlayan Rus kuşatması 25 Haziran'da püskürtüldü; şehrin tabyaları savunmada önemli rol oynadı.",
 "The Russian siege begun on 15 May was beaten off on 25 June; the town's redoubts played a major part in the defence.", "land"),
("Doğubayazıt (1854)", "Russian capture of Bayazid (1854)", "1854-07-29", WC, "Doğubayazıt", 39.55, 44.08, "known", "Türkiye",
 RU, O, "", "", "dis", "L", "kesin",
 ["TDVIA:dogubayazit"], "", "Şehir yağmalanıp yakıldı; Paris Antlaşması ile geri verildi.",
 "The town was plundered and burned; it was returned under the Treaty of Paris.", "land"),
("Gözleve (1855)", "Battle of Eupatoria", "1855-02-17", WC, "Gözleve (Yevpatoriya)", 45.19, 33.37, "known", "Ukrayna",
 O, RU, OM, "", "dis", "W", "kesin",
 ["TDVIA:omer-lutfi-pasa"], "", "Gözleve'ye saldıran Ruslar ağır bir yenilgiye uğradı.", "The Russians who attacked Eupatoria suffered a heavy defeat.", "land"),
("Sivastopol (1854–1855)", "Siege of Sevastopol (1854–1855)", "1855-09-08", WC, "Sivastopol (Akyar)", 44.60, 33.52, "known", "Ukrayna",
 "İngiltere, Fransa, Osmanlı Devleti ve Piyemonte", RU, OM, "", "dis", "W", "kesin",
 ["TDVIA:paris-antlasmasi", "TDVIA:omer-lutfi-pasa", "TDVIA:mehmed-ali-pasa-musir"],
 "Fransa maddesi şehrin 1854'te alındığını yazar; Paris Antlaşması maddesi düşüş tarihini 8 Eylül 1855 verir.",
 "Eylül 1854'teki çıkarmadan sonra uzun bir kuşatmayla alındı; şehrin düşmesi tarafları barışa yanaştırdı.",
 "Taken after a long siege following the landing of September 1854; its fall brought the sides to the peace table.", "land"),
("İngur (1855)", "Battle of the Ingur", "1855-11-07", WC, "İngur ırmağı", 42.48, 41.75, "approx", "Gürcistan",
 O, RU, OM, "", "dis", "W", "kesin",
 ["TDVIA:omer-lutfi-pasa"], "", "Kars'ı kurtarmak için Kafkasya'ya geçen Ömer Paşa bir Rus ordusunu yendi, fakat hava şartları yüzünden Kars'a ulaşamadı.",
 "Omar Pasha, who had moved to the Caucasus to relieve Kars, defeated a Russian army but bad weather kept him from reaching Kars.", "land"),
("Kars (1855)", "Siege of Kars (1855)", "1855-11-26", WC, "Kars", 40.60, 43.10, "known", "Türkiye",
 RU, O, "", "", "dis", "L", "kesin",
 ["TDVIA:paris-antlasmasi", "TDVIA:kars", "TDVIA:omer-lutfi-pasa", "TDVIA:ardahan"], "",
 "Uzun kuşatmadan sonra kale Rusların eline geçti; Paris Antlaşması ile geri verildi.",
 "After a long siege the fortress fell to the Russians; it was returned under the Treaty of Paris.", "land"),
("Grahova (1858)", "Battle of Grahovac", "1858", WK, "Grahova", 42.66, 18.67, "approx", "Karadağ",
 KD, O, "Hüseyin Paşa", "", "dis", "L", "kesin",
 ["TDVIA:karadag"], "", "Yenilginin ardından tarafsız Grahova arazisi 1859'da Karadağ'a bırakıldı.",
 "After the defeat the neutral Grahovo district was ceded to Montenegro in 1859.", "land"),
("Reika (1862)", "Battle of Rijeka Crnojevića (1862)", "1862-08-23", WK, "Reika (Rijeka Crnojevića)", 42.36, 19.03, "approx", "Karadağ",
 O, "Karadağ ve Hersek isyancıları", OM, "Mirko Petroviç", "dis", "W", "kesin",
 ["TDVIA:omer-lutfi-pasa", "TDVIA:karadag", "TDVIA:abdulaziz", "TDVIA:mehmed-ali-pasa-musir"], "",
 "1862 baharında iki koldan Karadağ'a giren Osmanlı kuvvetleri âsileri bozguna uğrattı; Prens Nikola Osmanlı isteklerini kabul etti.",
 "Ottoman forces entered Montenegro in two columns in spring 1862 and routed the rebels; Prince Nikola accepted the Ottoman terms.", "land"),
("Laşit (1866)", "Battle of Lasithi (1866)", "1866", WG, "Laşit (Lasithi)", 35.18, 25.47, "region", "Yunanistan",
 O, "Girit isyancıları", OM, "", "dis", "W", "kesin",
 ["TDVIA:omer-lutfi-pasa", "TDVIA:mehmed-ali-pasa-musir"], "",
 "Ömer Paşa kuvvetlerini iki koldan sevkedip âsileri yendi.", "Omar Pasha advanced in two columns and defeated the rebels.", "land"),
("Asîr isyanı (1869)", "Asir revolt (1869)", "1869", WY, "Asîr sahili", 17.90, 42.30, "region", "Suudi Arabistan",
 "Asîr emîri Muhammed b. Âiz", O, "", "Muhammed b. Âiz", "ic", "C", "kesin",
 ["TDVIA:asir--suudi-arabistan", "TDVIA:ebha"], "",
 "1866'da Asîr kaymakamı yapılan Muhammed b. Âiz yeniden ayaklanıp Osmanlı kuvvetlerini sahil şehirlerinden çekilmeye mecbur etti.",
 "Muhammad ibn A'id, made kaymakam of Asir in 1866, rose again and forced the Ottoman troops out of the coastal towns.", "land"),
("Reyde (1871)", "Capture of Reyde (1871)", "1871", WY, "Reyde, Asîr", 18.22, 42.50, "region", "Suudi Arabistan",
 O, "Asîr emîri Muhammed b. Âiz", "Redif Paşa, Ahmed Muhtar Paşa", "Muhammed b. Âiz", "ic", "C", "kesin",
 ["TDVIA:gazi-ahmed-muhtar-pasa", "TDVIA:yemen", "TDVIA:ebha"], "",
 "Reyde'nin teslim alınmasıyla Asîr isyanı sona erdi; Âiz ortadan kaldırıldı.",
 "The surrender of Reyde ended the Asir revolt; Ibn A'id was eliminated.", "land"),
("San‘a (1872)", "Ottoman capture of Sanaa (1872)", "1872", WY, "San‘a", 15.35, 44.21, "known", "Yemen",
 O, "Yemen isyancıları", AMP, "", "dis", "W", "kesin",
 ["TDVIA:gazi-ahmed-muhtar-pasa", "TDVIA:yemen"], "",
 "Ahmed Muhtar Paşa San‘a'yı teslim alarak Yemen'de devlet otoritesini yeniden kurdu; 1872'de vilâyet teşkilâtı kuruldu.",
 "Ahmed Muhtar Pasha received the surrender of Sanaa and restored state authority in Yemen; a province was set up in 1872.", "land"),
("Duga (1876)", "Battle of Duga Pass (1876)", "1876", WB, "Duga Boğazı, Hersek", 42.88, 18.68, "approx", "Karadağ",
 O, "Hersek isyancıları", AMP, "", "dis", "W", "kesin",
 ["TDVIA:gazi-ahmed-muhtar-pasa"], "", "13 Ocak 1876'da Mostar'a gelen Ahmed Muhtar Paşa'nın âsilere karşı harekâtında kazanıldı; ardından Gaçka'ya yürüdü.",
 "Won during Ahmed Muhtar Pasha's operations against the rebels after he reached Mostar on 13 January 1876; he then marched on Gacko.", "land"),
("Sırp ordusunun bozguna uğratılması (1876)", "Defeat of the Serbian army (1876)", "1876-07", WB, "Sırbistan sınırı, Vidin yöresi", 43.85, 22.35, "region", "Sırbistan",
 O, "Sırbistan Prensliği", OP, "Rus generalleri", "dis", "W", "kesin",
 ["TDVIA:gazi-osman-pasa", "TDVIA:doksanuc-harbi"], "",
 "Prens Milan'ın 2 Temmuz 1876'da savaş ilân etmesi üzerine Vidin kumandanı Osman Paşa, Rus generallerinin kumanda ettiği Sırp ordusunu bozguna uğrattı.",
 "After Prince Milan declared war on 2 July 1876, Osman Pasha, commander at Vidin, routed the Serbian army led by Russian generals.", "land"),
("Ziştovi (1877)", "Russian crossing of the Danube at Svishtov", "1877-06-27", WR, "Ziştovi (Svištov)", 43.62, 25.35, "known", "Bulgaristan",
 RU, O, "Serdârıekrem Abdülkerim Nâdir Paşa", "Grandük Nikola", "dis", "L", "borderline",
 ["TDVIA:doksanuc-harbi", "TDVIA:plevne-muharebeleri"], "",
 "Ruslar Tuna'yı ciddi bir direnişle karşılaşmadan geçip Ziştovi'yi, 1 Temmuz'da Tırnova'yı aldı.",
 "The Russians crossed the Danube without serious resistance and took Svishtov, then Tarnovo on 1 July.", "land"),
("Niğbolu (1877)", "Siege of Nikopol (1877)", "1877-07-04", WR, "Niğbolu", 43.70, 24.90, "known", "Bulgaristan",
 RU, O, "", "", "dis", "L", "kesin",
 ["TDVIA:nigbolu", "TDVIA:doksanuc-harbi"], "", "Ağır bombardımandan ve bir süre savunmadan sonra teslim oldu.",
 "Surrendered after heavy bombardment and a short defence.", "land"),
("Plevne I (1877)", "First Battle of Plevna", "1877-07-08", WR, "Plevne", 43.42, 24.61, "known", "Bulgaristan",
 O, RU, OP, "General Schilder", "dis", "W", "kesin",
 ["TDVIA:plevne-muharebeleri", "TDVIA:gazi-osman-pasa", "TDVIA:doksanuc-harbi"],
 "Plevne Muharebeleri maddesi Osman Paşa'nın Plevne'ye 7 Temmuz'da, Doksanüç Harbi maddesi 18 Temmuz'da geldiğini yazar.",
 "Takviye almamış Osmanlı birliklerini mevziden atmak isteyen Ruslar başarılı olamadı.",
 "The Russians failed to dislodge the Ottoman troops, who had not yet been reinforced.", "land"),
("Plevne II (1877)", "Second Battle of Plevna", "1877-07-18", WR, "Plevne", 43.42, 24.61, "known", "Bulgaristan",
 O, RU, OP, "General Krüdener", "dis", "W", "kesin",
 ["TDVIA:plevne-muharebeleri", "TDVIA:doksanuc-harbi"], "",
 "Sabahtan akşama süren muharebeden sonra Ruslar ağır kayıplarla çekildi; Gurko Balkanların kuzeyine dönmek zorunda kaldı.",
 "After a battle lasting from morning to sunset the Russians withdrew with heavy losses; Gurko had to fall back north of the Balkans.", "land"),
("Şıpka (Temmuz 1877)", "Russian capture of the Shipka Pass (1877)", "1877-07-19", WR, "Şıpka Geçidi", 42.75, 25.32, "known", "Bulgaristan",
 RU, O, "", "", "dis", "L", "kesin",
 ["TDVIA:doksanuc-harbi"], "", "Birçok saldırıya karşı koyan Osmanlı kuvvetleri yenileceklerine kanaat getirince geçidi gizlice tahliye etti.",
 "Having resisted repeated attacks, the Ottoman troops secretly evacuated the pass when they judged defeat inevitable.", "land"),
("Eski Zağra (1877)", "Battle of Stara Zagora", "1877-07", WR, "Eski Zağra", 42.43, 25.64, "known", "Bulgaristan",
 O, RU, "Süleyman Hüsnü Paşa", "General Gurko", "dis", "W", "kesin",
 ["TDVIA:doksanuc-harbi", "TDVIA:bulgaristan"], "",
 "Gurko 22 Temmuz'da Eski Zağra'yı aldı; Karadağ cephesinden gelen Süleyman Paşa onu yenip Balkanların güneyindeki yerleri geri aldı.",
 "Gurko took Stara Zagora on 22 July; Süleyman Pasha, arriving from the Montenegrin front, defeated him and recovered the places south of the Balkans.", "land"),
("Şıpka (Ağustos 1877)", "Battle of the Shipka Pass (August 1877)", "1877-08-21", WR, "Şıpka Geçidi", 42.75, 25.32, "known", "Bulgaristan",
 RU, O, "Süleyman Hüsnü Paşa", "", "dis", "L", "kesin",
 ["TDVIA:doksanuc-harbi"], "", "21 Ağustos'tan itibaren yapılan şiddetli taarruzlara rağmen geçit geri alınamadı.",
 "Despite fierce attacks from 21 August the pass could not be retaken.", "land"),
("Lofça (1877)", "Battle of Lovech (1877)", "1877-08-23", WR, "Lofça", 43.14, 24.72, "known", "Bulgaristan",
 RU, O, "Rifat Paşa", "", "dis", "L", "kesin",
 ["TDVIA:lofca"],
 "Lofça maddesi şehrin 5 Haziran 1877'de işgal edildiğini, Rifat Paşa'nın 15 Haziran'da Rusları geri püskürttüğünü yazar; Doksanüç Harbi maddesine göre Ruslar Tuna'yı ancak 27 Haziran'da geçmişti.",
 "Rifat Paşa'nın Rusları bir kez geri püskürtmesine rağmen şehir 23 Ağustos'ta terkedildi.",
 "Although Rifat Pasha once drove the Russians back, the town was abandoned on 23 August.", "land"),
("Plevne III (1877)", "Third Battle of Plevna", "1877-09-11", WR, "Plevne", 43.42, 24.61, "known", "Bulgaristan",
 O, "Rusya ve Romanya", OP, "Grandük Nikola", "dis", "W", "kesin",
 ["TDVIA:plevne-muharebeleri", "TDVIA:doksanuc-harbi"], "",
 "7–11 Eylül arasındaki topçu ateşinin ardından yapılan Rus-Rumen genel hücumu başarısız oldu; Plevne önündeki Rus kaybı 50.000'e yaklaştı.",
 "The Russo-Romanian general assault after the bombardment of 7–11 September failed; Russian losses before Plevna neared 50,000.", "land"),
("Rusçuk önü (1877)", "Battles before Ruse (1877)", "1877", WR, "Rusçuk yöresi", 43.70, 26.10, "region", "Bulgaristan",
 O, RU, "Müşir Mehmed Ali Paşa", "Grandük Nikola", "dis", "W", "kesin",
 ["TDVIA:doksanuc-harbi"], "", "Tuna ordusu kumandanlığına getirilen Mehmed Ali Paşa Rusçuk üzerine yürüyen Rus kuvvetlerini yendi.",
 "Mehmed Ali Pasha, newly given command of the Danube army, defeated the Russian forces marching on Ruse.", "land"),
("Plevne'nin düşüşü (1877)", "Fall of Plevna", "1877-12-10", WR, "Plevne", 43.42, 24.61, "known", "Bulgaristan",
 "Rusya ve Romanya", O, OP, "Grandük Nikola", "dis", "L", "kesin",
 ["TDVIA:plevne-muharebeleri", "TDVIA:doksanuc-harbi", "TDVIA:suleyman-husnu-pasa"], "",
 "Kuşatma çemberini yarma girişimi başarısız oldu; yaralanan Osman Paşa teslim olmak zorunda kaldı. Plevne'nin düşmesi İstanbul yolunu açtı.",
 "The attempt to break the encirclement failed; Osman Pasha, wounded, had to surrender. The fall of Plevna opened the road to Istanbul.", "land"),
("Edirne (1878)", "Russian occupation of Edirne (1878)", "1878-01-20", WR, "Edirne", 41.68, 26.56, "known", "Türkiye",
 RU, O, "Vali Eyüp Paşa", "", "dis", "L", "borderline",
 ["TDVIA:doksanuc-harbi", "TDVIA:mehmed-ali-pasa-musir", "TDVIA:edirne"], "",
 "Vali mühimmat depolarını tahrip edip çekilince şehir direnişsiz teslim oldu.",
 "When the governor destroyed the munitions depots and withdrew, the city surrendered without resistance.", "land"),
("Andrayoviç (1877)", "Battle of Andrijevica (1877)", "1877", WR, "Andrayoviç (Andrijevica)", 42.73, 19.79, "approx", "Karadağ",
 O, KD, "Müşir Mehmed Ali Paşa", "", "dis", "W", "kesin",
 ["TDVIA:mehmed-ali-pasa-musir"], "", "Karadağlılar yeniden harekete geçince Mehmed Ali Paşa Lim suyunu aşarak onları yendi.",
 "When the Montenegrins took the field again, Mehmed Ali Pasha crossed the Lim and defeated them.", "land"),
("Nikşiç, Bar ve Ülgün'ün kaybı (1877–1878)", "Montenegrin capture of Nikšić, Bar and Ulcinj", "1878-01", WR, "Nikşiç, Bar ve Ülgün", 42.77, 18.94, "region", "Karadağ",
 KD, O, "", "", "dis", "L", "kesin",
 ["TDVIA:karadag"], "", "Karadağ savaşın sonlarına doğru Nikşiç, Podgorica ve Bar'ı aldı, Ülgün'ü ele geçirdi.",
 "Towards the end of the war Montenegro took Nikšić, Podgorica and Bar, and seized Ulcinj.", "land"),
("Doğubayazıt (1877)", "Russian capture of Bayazid (1877)", "1877-04-30", WR, "Doğubayazıt", 39.55, 44.08, "known", "Türkiye",
 RU, O, "", "General Hugossof", "dis", "L", "kesin",
 ["TDVIA:dogubayazit", "TDVIA:doksanuc-harbi"], "", "", "", "land"),
("Ardahan (1877)", "Battle of Ardahan (1877)", "1877-05-17", WR, "Ardahan", 41.11, 42.70, "known", "Türkiye",
 RU, O, "", "General Melikof", "dis", "L", "kesin",
 ["TDVIA:gazi-ahmed-muhtar-pasa", "TDVIA:doksanuc-harbi"], "", "Şiddetli çarpışmalardan sonra Ruslar şehre girdi.", "The Russians entered the town after heavy fighting.", "land"),
("Halyaz (Delibaba) (1877)", "Battle of Taghir (Delibaba)", "1877-06-21", WR, "Delibaba, Eleşkirt yakını", 39.73, 42.60, "approx", "Türkiye",
 O, RU, AMP, "", "dis", "W", "kesin",
 ["TDVIA:gazi-ahmed-muhtar-pasa"], "", "Kars'ı kuşatan Ruslara karşı başlatılan karşı hücumun ilk muharebesi.",
 "The first battle of the counter-offensive against the Russians besieging Kars.", "land"),
("Zivin (1877)", "Battle of Zivin", "1877-06-25", WR, "Zivin", 40.15, 42.45, "approx", "Türkiye",
 O, RU, AMP, "", "dis", "W", "kesin",
 ["TDVIA:gazi-ahmed-muhtar-pasa", "TDVIA:doksanuc-harbi"],
 "Ahmed Muhtar Paşa maddesi muharebeyi 25–27 Haziran'a koyar; Doksanüç Harbi maddesi Erzurum'a yürüyen Rusların 15 Temmuz'da yenilip sınır dışına atıldığını yazar.",
 "Ruslar Gümrü önlerine kadar çekildi.", "The Russians fell back as far as Gyumri.", "land"),
("Gedikler (Kızıltepe) (1877)", "Battle of Kızıltepe", "1877-08-25", WR, "Gedikler (Kızıltepe), Kars yakını", 40.55, 43.35, "approx", "Türkiye",
 O, RU, AMP, "", "dis", "W", "kesin",
 ["TDVIA:gazi-ahmed-muhtar-pasa"], "", "Âni bir hücumla kazanıldı.", "Won by a surprise attack.", "land"),
("Yahniler (1877)", "Battle of Yahniler", "1877-10-02", WR, "Yahniler, Kars yakını", 40.50, 43.40, "approx", "Türkiye",
 O, RU, AMP, "", "dis", "W", "kesin",
 ["TDVIA:gazi-ahmed-muhtar-pasa"], "", "Takviye alan 70.000 kişilik Rus ordusunun üç gün süren hücumu 34.000 kişilik Osmanlı kuvvetince püskürtüldü.",
 "The three-day attack of the reinforced 70,000-strong Russian army was beaten off by 34,000 Ottoman troops.", "land"),
("Alacadağ (1877)", "Battle of Aladzha", "1877-10-15", WR, "Alacadağ, Kars yakını", 40.45, 43.50, "approx", "Türkiye",
 RU, O, AMP, "", "dis", "L", "kesin",
 ["TDVIA:gazi-ahmed-muhtar-pasa"], "", "Ruslar bir kısım Osmanlı askerini teslim aldı; Ahmed Muhtar Paşa Kars'a çekildi.",
 "The Russians took part of the Ottoman force prisoner; Ahmed Muhtar Pasha withdrew to Kars.", "land"),
("Deveboynu (1877)", "Battle of Deve Boynu", "1877-11-04", WR, "Deveboynu, Erzurum", 39.95, 41.45, "approx", "Türkiye",
 RU, O, AMP, "", "dis", "L", "kesin",
 ["TDVIA:gazi-ahmed-muhtar-pasa"], "", "Elinde az sayıda asker kalan Ahmed Muhtar Paşa Erzurum'a çekildi.",
 "Left with few troops, Ahmed Muhtar Pasha withdrew to Erzurum.", "land"),
("Aziziye (1877)", "Battle of the Aziziye redoubts", "1877-11-08", WR, "Aziziye tabyaları, Erzurum", 39.92, 41.30, "known", "Türkiye",
 O, RU, AMP, "", "dis", "W", "kesin",
 ["TDVIA:gazi-ahmed-muhtar-pasa", "TDVIA:doksanuc-harbi"], "",
 "Tabyalara hücum eden Ruslar Erzurum halkının da katıldığı çarpışmada Deveboynu'na kadar püskürtüldü; Nene Hatun ahaliyi savunmaya teşvik etti.",
 "The Russians who stormed the redoubts were driven back to Deve Boynu in fighting joined by the people of Erzurum; Nene Hatun rallied the townsfolk.", "land"),
("Kars (1877)", "Battle of Kars (1877)", "1877-11-18", WR, "Kars", 40.60, 43.10, "known", "Türkiye",
 RU, O, "Hâmi Paşa", "General Lazarof", "dis", "L", "kesin",
 ["TDVIA:gazi-ahmed-muhtar-pasa", "TDVIA:doksanuc-harbi", "TDVIA:kars"], "", "", "", "land"),
]

LEFT = [
 {"name": "Karadağ seferi (1852–1853)", "reason": "Ömer Lutfi Paşa maddesi seferi ve 3 Mart 1853 anlaşmasını anar; muharebe adı yok.", "source": "TDVIA:omer-lutfi-pasa"},
 {"name": "Kafkas cephesi 1853–1854 (Ahıska, Başgedikler, Kürekdere)", "reason": "İndirilen maddelerde adıyla bulunamadı; Şeyh Şâmil maddesi yalnızca Kars-Gümrü yönündeki muharebeleri toplu anar.", "source": "TDVIA:seyh-samil"},
 {"name": "Kars müdafaası (29 Eylül 1855)", "reason": "Yalnızca kaynakçada (\"1855 Kars Zaferi\") geçiyor.", "source": "TDVIA:namik-kemal"},
 {"name": "Lübnan ve Şam olayları (1860)", "reason": "Topluluklar arası çatışma; Osmanlı devletinin savaşı sayılmadı.", "source": "TDVIA:lubnan"},
 {"name": "Girit isyanının diğer çatışmaları (Arkadi 1866)", "reason": "Girit maddesinde ayrıntı yok.", "source": "TDVIA:girit"},
 {"name": "Sırp savaşı 1876 (Aleksinaç, Cuniş) ve Karadağ çarpışmaları 1876", "reason": "TDVİA'da adıyla bulunamadı; Osman Paşa'nın zaferi toplu kayıt olarak alındı.", "source": "TDVIA:gazi-osman-pasa"},
 {"name": "Batum (1877–1878)", "reason": "Batum maddesinde savaş ayrıntısı yok.", "source": "TDVIA:batum"},
 {"name": "Vidin, Rusçuk ve Silistre direnişleri (1877–1878)", "reason": "Maddeler direnişi tarihsiz ve toplu anar.", "source": "TDVIA:vidin"},
 {"name": "Şeynova–Kazanlık ve Filibe (1878)", "reason": "TDVİA'da bulunamadı.", "source": ""},
 {"name": "Bosna'nın Avusturya-Macaristan tarafından işgali (1878)", "reason": "Berlin Antlaşması'ndan sonra; Osmanlı devleti savaşmadı, direniş Bosna müslümanlarınındı.", "source": "TDVIA:bosna-hersek"},
 {"name": "Belgradcık isyanı (1841, 1850)", "reason": "Belgradcık maddesi iki isyanı birlikte anar; tarih ayrılamadı.", "source": "TDVIA:belgradcik"},
]

# İkinci kaynak turu
EXTRA_SRC = {"Sinop (1853)": ["TDVIA:mehmed-emin-pasa-kibrisli"],
             "Eski Zağra (1877)": ["TDVIA:suleyman-husnu-pasa", "TDVIA:eski-zagra"],
             "Şıpka (Temmuz 1877)": ["TDVIA:suleyman-husnu-pasa"],
             "Şıpka (Ağustos 1877)": ["TDVIA:suleyman-husnu-pasa"],
             "Ziştovi (1877)": ["TDVIA:tirnova--bulgaristan"],
             "Deveboynu (1877)": ["TDVIA:erzurum"],
             "Aziziye (1877)": ["TDVIA:erzurum"]}
FIX = {"Sinop (1853)": {
           "dispute": "Sinop ve Kıbrıslı Mehmed Emin Paşa maddeleri baskını \"1854 yılı başlarına\" koyar. Savaş 4 Ekim 1853'te ilân edilmişti; genel kabul gören tarih 30 Kasım 1853'tür.",
           "note": "Limandaki Osmanlı donanması Rus baskınına uğradı; on iki gemi battı, 2000'den fazla asker şehid düştü. Kaptanıderyâ Mahmud Paşa bu yüzden görevden alındı.",
           "note_en": "The Ottoman squadron in the harbour was attacked by the Russian fleet; twelve ships were sunk and more than 2,000 men killed. Grand Admiral Mahmud Pasha was dismissed over it."},
       "Ziştovi (1877)": {"dispute": "Tırnova'nın düşüşü: Doksanüç Harbi maddesi 1 Temmuz, Tırnova maddesi 24 Haziran 1877 der."},
       "Eski Zağra (1877)": {
           "note": "Gurko 22 Temmuz'da Eski ve Yeni Zağra'yı aldı. Hersek'teki kolordusunu Bar'dan gemilerle Dedeağaç'a getiren Süleyman Paşa 26 Temmuz'da mevzi aldı ve şehirleri savunan Rus ve Bulgarları yendi.",
           "note_en": "Gurko took Stara and Nova Zagora on 22 July. Süleyman Pasha, who had shipped his Herzegovina corps from Bar to Dedeağaç, took up position on 26 July and defeated the Russians and Bulgarians defending the towns."}}
NEW = {"Plevne'nin düşüşü (1877)": [
        ("Maçka (1877)", "Battle of Mechka", "1877-12-11", WR, "Maçka (Mečka), Rusçuk yakını", 43.77, 26.12, "approx", "Bulgaristan",
         RU, O, "Süleyman Hüsnü Paşa", "", "dis", "L", "kesin",
         ["TDVIA:suleyman-husnu-pasa"], "", "Kuşatılmış Plevne'ye yardım için yürüyen Süleyman Paşa bu muharebeyi kaybetti.",
         "Süleyman Pasha lost this battle while marching to the relief of besieged Plevna.", "land")]}
RR = []
for r in R:
    RR.append(r)
    RR += NEW.get(r[0], [])

recs = []
for i, r in enumerate(RR, 1):
    (ntr, nen, date, war, place, lat, lon, loc, country, sa, sb, tc, oc, cat, res, status, src, disp, note, note_en, typ) = r
    rec = {"id": i, "name_tr": ntr, "name_en": nen, "date": date, "hijri": "", "type": typ, "war": war, "place": place,
           "lat": lat, "lon": lon, "loc": loc, "country": country, "side_a": sa, "side_b": sb, "turkic_cmd": tc, "opp_cmd": oc,
           "category": cat, "result": res, "status": status, "sources": src,
           "verify": {"tdvia": True, "tdvia2": len([s for s in src if s.startswith("TDVIA:")]) >= 2, "wp": False, "rom": False, "academic": False},
           "state": O, "home_batch": HB}
    rec["sources"] += [x for x in EXTRA_SRC.get(ntr, []) if x not in rec["sources"]]
    for k, v in FIX.get(ntr, {}).items():
        if k == "dispute": disp = v
        elif k == "note": note = v
        elif k == "note_en": note_en = v
        else: rec[k] = v
    rec["verify"]["tdvia2"] = len([x for x in rec["sources"] if x.startswith("TDVIA:")]) >= 2
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    recs.append(rec)

pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 16 — Osmanlı: Tanzimat'tan Berlin'e (1839–1878)", "compiled": "2026-10-29", "status": "İkinci kaynak turu yapıldı.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "osmanli-1839-1878.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
