"""data/turkistan-hanliklari.json dosyasını üretir (Parti 22: Türkistan hanlıkları ve Rus istilâsı, 1837–1881).

Kapsam kararı 2026-10-30: Hokand, Buhara ve Hîve hanlıkları ile Kazak (Kenesarı) ve Türkmen direnişinin Rus işgaline karşı
savaşları. Olaylar Hokand Hanlığı, Hokand, Hîve Hanlığı, Buhara, Taşkent, Semerkant, Çimkent, Hucend, Üsrûşene, Mergīnân,
Yâkub Beg, Kazakistan, Türkmenistan, Türkmenler, Özbekler, Kungrat ve Türkistan maddelerinden derlendi."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "turkistan-hanliklari"
HK = "Hokand Hanlığı"
BH = "Buhara Emirliği (Mangıtlar)"
HV = "Hîve Hanlığı"
KZ = "Kazaklar (Kenesarı)"
TM = "Türkmenler (Teke)"
RU = "Rusya"
WRI = "Rusya'nın Türkistan'ı istilâsı (1839–1884)"
WKN = "Kenesarı ayaklanması (1837–1847)"
WTM = "Rusya'nın Türkmenistan'ı istilâsı (1869–1881)"

# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür, devlet)
R = [
("Kenesarı'nın ilk savaşı (1837)", "Kenesary's first battle with Russia (1837)", "1837-11-15", WKN, "Orta cüz toprakları", 50.50, 68.00, "region", "Kazakistan",
 KZ, RU, "Sultan Kenesarı Kasımoğlu", "", "dis", "W", "kesin",
 ["TDVIA:kazakistan"], "", "Orta cüzde Rus kaleleri ve vergilerine karşı başlayan ayaklanmanın ilk savaşı Kazaklar'ın lehine sonuçlandı.",
 "The first battle of the Middle Horde rising against Russian forts and taxes went the Kazakhs' way.", "land", KZ),
("Irgız ve Turgay'ın geri alınışı (1838)", "Kenesary retakes Irgiz and Turgay (1838)", "1838", WKN, "Irgız ve Turgay", 49.63, 63.50, "region", "Kazakistan",
 KZ, RU, "Sultan Kenesarı Kasımoğlu", "", "dis", "W", "borderline",
 ["TDVIA:kazakistan"], "", "Kenasarı Rus işgalindeki Irgız ve Turgay bölgelerini geri aldı; muharebe adı verilmediğinden borderline.",
 "Kenesary recovered the Russian-held Irgiz and Turgay districts; borderline as no battle is named.", "land", KZ),
("Kenesarı'nın ikinci savaşı (1838)", "Kenesary's second battle with Russia (1838)", "1838-07-12", WKN, "Orta cüz toprakları", 50.50, 68.00, "region", "Kazakistan",
 RU, KZ, "Sultan Kenesarı Kasımoğlu", "", "dis", "L", "kesin",
 ["TDVIA:kazakistan"], "", "İkinci savaşı Ruslar kazandı.", "The Russians won the second battle.", "land", KZ),
("Beş-Tumak (1839)", "Battle of Besh-Tumak (Perovsky's Khiva expedition, 1839)", "1839-12-05", WRI, "Beş-Tumak vahası (Üstyurt)", 45.00, 56.00, "region", "Kazakistan / Özbekistan",
 HV, RU, "Allahkulı Han", "General Perovsky", "dis", "W", "kesin",
 ["TDVIA:hive-hanligi"], "",
 "14 Kasım 1839'da Orenburg'dan yola çıkan 13.000 kişilik Rus kuvveti Mangışlak'ın Üstyurt bölgesindeki Beş-Tumak vahasında yapılan savaşı kaybedip Orenburg'a çekildi.",
 "The 13,000-strong Russian force that left Orenburg on 14 November 1839 lost the battle at the Besh-Tumak oasis on the Ustyurt and fell back on Orenburg.", "land", HV),
("Lebedev ve Bisyanov'un yenilgisi (1843)", "Defeat of Lebedev and Bisyanov (1843)", "1843-06-05", WKN, "Kazak bozkırı", 48.00, 66.00, "region", "Kazakistan",
 KZ, RU, "Sultan Kenesarı Kasımoğlu", "General Lebedev, General Bisyanov", "dis", "W", "kesin",
 ["TDVIA:kazakistan"], "", "Kenasarı'nın Buhara ile ittifakından faydalanmak isteyen Ruslar iki generalin kumandasında yürüdüyse de başarısızlığa uğradı.",
 "Seeking to exploit Kenesary's alliance with Bukhara, the Russians advanced under two generals but failed.", "land", KZ),
("Kenesarı'nın 1844 zaferi", "Kenesary's victory of 1844", "1844-08-14", WKN, "Kazak bozkırı", 48.00, 66.00, "region", "Kazakistan",
 KZ, RU, "Sultan Kenesarı Kasımoğlu", "", "dis", "W", "kesin",
 ["TDVIA:kazakistan"], "", "Bu savaşı da kazanan Kenasarı Buhara ve Hîve hanlarınca Kazaklar'ın hanı olarak tanındı.",
 "After this victory Kenesary was recognised as khan of the Kazakhs by the khans of Bukhara and Khiva.", "land", KZ),
("Karatav'ın boşaltılması (1845)", "Russian two-pronged offensive against Kenesary (1845)", "1845", WKN, "Karatav", 43.50, 69.50, "region", "Kazakistan",
 RU, KZ, "Sultan Kenesarı Kasımoğlu", "", "dis", "L", "borderline",
 ["TDVIA:kazakistan"], "", "Orenburg ve Sibirya ordularının sonbahara kadar süren saldırılarına dayanamayan Kenasarı kuvvetleri Karatav'ı boşalttı; tek bir muharebe adı yok.",
 "Unable to withstand the attacks of the Orenburg and Siberian armies lasting until autumn, Kenesary's forces abandoned Karatau; no single battle is named.", "land", KZ),
("Mey-Tuble (c. 1847)", "Death of Kenesary (c. 1847)", "c. 1847", WKN, "Mey-Tuble vahası (yukarı Çu)", 42.80, 75.50, "approx", "Kırgızistan",
 "Kırgızlar", KZ, "Sultan Kenesarı Kasımoğlu", "", "turk_arasi", "L", "kesin",
 ["TDVIA:kazakistan"], "TDVİA maddesi yıl vermez; olay 1845 sonbaharından sonraki ikinci çekilmeden (bir yıl sonra Alatav) sonra anlatılır. Tansü ve Özdemir 1847 verir ve Kenesarı'nın kuvvetlerinin Almalı geçidinde kuşatıldığını yazar.",
 "Alatav'a çekilen Kenasarı'ya Ruslar'ın kışkırtmasıyla Kırgızlar saldırdı; Mey-Tuble vahasına çekilen Kenasarı ikinci baskında esir alınıp öldürüldü.",
 "Kenesary, withdrawn to the Alatau, was attacked by the Kyrgyz at Russian instigation; retreating to the Mey-Tuble oasis, he was captured and killed in a second raid.", "land", KZ),
("Akmescid (1853)", "Siege of Ak-Mechet (1853)", "1853", WRI, "Akmescid (Kızılorda)", 44.85, 65.51, "known", "Kazakistan",
 RU, HK, "Yâkub Beg (koşbegi)", "", "dis", "L", "kesin",
 ["TDVIA:yakub-beg"], "", "Yirmi altı gün süren Rus kuşatmasına Akmescid'in savunmasını üstlenen Yâkub Beg büyük bir başarıyla karşı koyduysa da kale Ruslar'ın eline geçti.",
 "Yaqub Beg, commanding the defence, resisted the 26-day Russian siege with great success, but Ak-Mechet fell to the Russians.", "land", HK),
("Çimkent'in düşüşü (1864)", "Fall of Chimkent (1864)", "1864", WRI, "Çimkent", 42.32, 69.60, "known", "Kazakistan",
 RU, HK, "Nur Muhammed", "", "dis", "L", "kesin",
 ["TDVIA:cimkent", "TDVIA:hokand-hanligi"], "Hokand Hanlığı maddesi Çimkent'in işgalini Kaufmann'a bağlar.",
 "Buhara emîrinin Hokand'a saldırması üzerine Âlim Kul ana kuvvetleriyle çekilince Nur Muhammed kumandasındaki az sayıda asker ve halk on sekiz gün savunduktan sonra şehri teslim etti.",
 "When the emir of Bukhara attacked Kokand and Alim Qul withdrew his main force, the small garrison under Nur Muhammad and the townspeople held out for eighteen days and then surrendered.", "land", HK),
("Çimkent (1864)", "First Russian assault on Chimkent (1864)", "1864-07-07", WRI, "Çimkent", 42.32, 69.60, "known", "Kazakistan",
 HK, RU, "Âlim Kul", "", "dis", "W", "kesin",
 ["TDVIA:cimkent"], "", "Ruslar 7 Temmuz 1864'te hücuma geçtiyse de bir hafta süren mücadeleden sonra geri püskürtüldü.",
 "The Russians attacked on 7 July 1864 but were repulsed after a week's fighting.", "land", HK),
("Taşkent (1865)", "Capture of Tashkent (1865)", "1865-06", WRI, "Taşkent", 41.31, 69.28, "known", "Özbekistan",
 RU, HK, "", "", "dis", "L", "kesin",
 ["TDVIA:taskent", "TDVIA:hokand-hanligi", "TDVIA:turkistan"], "Hokand Hanlığı maddesi işgali Kaufmann'a bağlar.",
 "Haziran 1865'te Çarlık orduları Taşkent'i işgal etti; şehir 1867'de Türkistan Genel Valiliği'nin merkezi yapıldı.",
 "Tsarist armies occupied Tashkent in June 1865; it became the seat of the Governor-Generalship of Turkestan in 1867.", "land", HK),
("İrcar (1866)", "Battle of Irjar (1866)", "1866", WRI, "İrcar (Seyhun kıyısı)", 40.45, 68.90, "approx", "Özbekistan",
 RU, BH, "Muzafferüddin", "", "dis", "L", "kesin",
 ["TDVIA:usrusene"], "",
 "Ruslar'la Buhara Hanlığı arasındaki İrcar savaşının ardından Ura-Tepe ve Cîzek Ruslar'ca işgal edildi; Buhara maddesi Muzafferüddin'in Ruslar'a defalarca yenildiğini yazar.",
 "After the battle of Irjar between Russia and Bukhara, Ura-Tyube and Jizzakh were occupied; the Bukhara article says Muzaffar was beaten by the Russians repeatedly.", "land", BH),
("Hucend (1866)", "Capture of Khujand (1866)", "1866", WRI, "Hucend", 40.28, 69.62, "known", "Tacikistan",
 RU, BH, "", "", "dis", "L", "kesin",
 ["TDVIA:hucend", "TDVIA:tacikistan"], "Hucend maddesi şehri 1842'den beri Buhara'nın elinde gösterir; Hokand Hanlığı maddesi Hucend'in 1866'da Hokand'dan alındığını ima eder.",
 "Şehir kanlı çarpışmalar sonucunda Ruslar'ca ele geçirildi.", "The city was taken by the Russians after bloody fighting.", "land", BH),
("Ura-Tepe ve Cîzek (1866)", "Capture of Ura-Tyube and Jizzakh (1866)", "1866", WRI, "Ura-Tepe ve Cîzek", 40.12, 67.84, "approx", "Tacikistan / Özbekistan",
 RU, BH, "", "", "dis", "L", "kesin",
 ["TDVIA:usrusene", "TDVIA:hokand-hanligi"], "", "İrcar savaşının ardından iki şehir Ruslar'ca işgal edildi.",
 "Both towns were occupied by the Russians after Irjar.", "land", BH),
("Semerkant (1868)", "Capture of Samarkand (1868)", "1868-05-14", WRI, "Semerkant", 39.65, 66.96, "known", "Özbekistan",
 RU, BH, "Muzafferüddin", "", "dis", "L", "kesin",
 ["TDVIA:semerkant", "TDVIA:buhara", "TDVIA:turkistan"], "",
 "Mâverâünnehir'de ilerleyen Ruslar Semerkant'ı zaptetti; Buhara Emirliği aynı yıl Rus himayesine girdi.",
 "Advancing through Transoxiana the Russians took Samarkand; the Emirate of Bukhara became a Russian protectorate that year.", "land", BH),
("Rus karargâhı baskını (1870)", "Turkmen raid on the Russian camp (1870)", "1870-10-20", WTM, "Kızılsu yöresi", 40.00, 53.00, "approx", "Türkmenistan",
 RU, TM, "Nur Verdi Han, Tıkma Serdar", "", "dis", "L", "kesin",
 ["TDVIA:turkmenistan"], "", "Türkmenler Rus karargâhına baskın düzenlediyse de yoğun topçu ateşi karşısında geri çekildi.",
 "The Turkmens raided the Russian camp but fell back under heavy artillery fire.", "land", TM),
("Nur Verdi Han'ın baskını (1872)", "Turkmen raid of 1872", "1872", WTM, "Hazar ötesi", 39.50, 55.00, "region", "Türkmenistan",
 RU, TM, "Nur Verdi Han", "", "dis", "L", "kesin",
 ["TDVIA:turkmenistan"], "", "Hîve istilâsının hazırlıklarını gören Nur Verdi Han yeni bir baskın düzenlediyse de Rus topçusu karşısında büyük zayiatla çekildi.",
 "Seeing the preparations against Khiva, Nur Verdi Khan raided again but withdrew with heavy losses before the Russian artillery.", "land", TM),
("Hîve (1873)", "Capture of Khiva (1873)", "1873-05-29", WRI, "Hîve", 41.38, 60.36, "known", "Özbekistan",
 RU, HV, "Seyyid Muhammed Rahim Bahadır Han", "General Kaufmann", "dis", "L", "kesin",
 ["TDVIA:hive-hanligi", "TDVIA:turkmenistan", "TDVIA:kungrat", "TDVIA:turkistan"], "",
 "Mart 1873'te yürüyen Ruslar Hîve kuvvetlerini yenip şehri kuşattı; Türkmenler'in savunma kararı üzerine şiddetli topçu ateşinden sonra şehri aldı. Hanlık Rus vasalı oldu.",
 "Marching in March 1873 the Russians beat the Khivan forces and besieged the city; when the Turkmens resolved to defend it, they took it after heavy bombardment. The khanate became a Russian vassal.", "land", HV),
("Hucend kuşatması (1875)", "Kokandi siege of Khujand (1875)", "1875", WRI, "Hucend", 40.28, 69.62, "known", "Tacikistan",
 RU, HK, "", "", "dis", "L", "kesin",
 ["TDVIA:hucend"], "", "Hokand Hanlığı'nda üslenen direnişçiler şehri bir süre kuşattıysa da kurtaramadı.",
 "Resistance fighters based in the Kokand Khanate besieged the city for a time but could not free it.", "land", HK),
("Hokand (1875)", "Russian siege of Kokand (1875)", "1875-08", WRI, "Hokand", 40.53, 70.94, "known", "Özbekistan",
 RU, HK, "", "", "dis", "L", "kesin",
 ["TDVIA:hokand"], "",
 "Halkın Hudâyâr'a karşı ayaklanmasını bahane eden Ruslar Hokand'ı kuşattı; şehir ertesi yıl ilhak edildi.",
 "Using the rising against Khudayar as a pretext, the Russians besieged Kokand; it was annexed the next year.", "land", HK),
("Endican (1876)", "Capture of Andijan (1876)", "1876-01-08", WRI, "Endican", 40.78, 72.34, "known", "Özbekistan",
 RU, HK, "Polat Bey", "", "dis", "L", "kesin",
 ["TDVIA:hokand-hanligi"], "", "", "", "land", HK),
("Polat Bey'in yenilgisi (1876)", "Suppression of Pulat Bey's rising (1876)", "1876-02-08", WRI, "Mergīnân", 40.47, 71.72, "known", "Özbekistan",
 RU, HK, "Polat Bey", "Skobelev", "dis", "L", "kesin",
 ["TDVIA:merginan", "TDVIA:hokand-hanligi"], "",
 "Rus kuklası Nasreddin'e karşı halkın han seçtiği Polat Bey'in ayaklanmasını Skobelev kanlı biçimde bastırıp onu Mergīnân'da idam ettirdi; Hokand Şubat 1876'da Fergana eyaleti adıyla Rusya'ya ilhak edildi.",
 "Skobelev crushed the rising of Pulat Bey, chosen khan by the people against the Russian puppet Nasreddin, and had him executed at Margilan; Kokand was annexed as the Fergana province in February 1876.", "land", HK),
("Kızılarvat (1877)", "Battle of Kyzyl-Arvat (1877)", "1877-05-12", WTM, "Kızılarvat", 38.98, 56.28, "known", "Türkmenistan",
 RU, TM, "Nur Verdi Han", "General Lomakin", "dis", "L", "kesin",
 ["TDVIA:turkmenistan"], "", "Türkmenler'le Ruslar arasındaki ilk ciddi muharebe; üstün topçu ve mitralyöz ateşine sahip Ruslar kazandı.",
 "The first serious battle between Turkmens and Russians; the Russians, superior in artillery and machine-guns, won.", "land", TM),
("Büyük Bendesen geçidi (1879)", "Great Bendesen pass (1879)", "1879-06", WTM, "Büyük Bendesen geçidi", 38.80, 56.80, "approx", "Türkmenistan",
 RU, TM, "", "General Lazaryev", "dis", "L", "kesin",
 ["TDVIA:turkmenistan"], "", "Rus ilerleyişi karşısında zayiat veren Türkmenler Göktepe'ye çekildi.",
 "Losing men before the Russian advance, the Turkmens fell back on Geok Tepe.", "land", TM),
("Göktepe (1879)", "First battle of Geok Tepe (1879)", "1879-09-09", WTM, "Göktepe", 38.16, 57.97, "known", "Türkmenistan",
 TM, RU, "Berdi Murad Han, Kara Batur", "General Lomakin", "dis", "W", "kesin",
 ["TDVIA:turkmenistan", "TDVIA:turkmenler", "TDVIA:ozbekler"], "",
 "Türkmen süvarilerini bertaraf edip kaleyi bombalayan Ruslar birinci surdan girince göğüs göğüse çarpışmada büyük zayiat verip Hazar kıyılarına çekildi; olay Rusya'da ve Avrupa'da tam bir Rus yenilgisi sayıldı.",
 "Having scattered the Turkmen cavalry and shelled the fortress, the Russians broke into the first wall but suffered heavy losses hand to hand and fell back to the Caspian; it was seen in Russia and Europe as an outright Russian defeat.", "land", TM),
("Yengikale (1881)", "Capture of Yangi-Kala (1881)", "1881-01-01", WTM, "Yengikale (Göktepe yolları)", 38.17, 57.95, "approx", "Türkmenistan",
 RU, TM, "", "General Skobelev", "dis", "L", "kesin",
 ["TDVIA:turkmenistan"], "", "Ruslar Göktepe'nin bütün yollarına hâkim olan Yengikale'yi iki koldan saldırıp aldı.",
 "The Russians took Yangi-Kala, which commanded every approach to Geok Tepe, in a two-pronged attack.", "land", TM),
("Göktepe (1881)", "Second battle of Geok Tepe (1881)", "1881-01-24", WTM, "Göktepe", 38.16, 57.97, "known", "Türkmenistan",
 RU, TM, "Mahtumkulu Han, Tıkma Serdar", "General Skobelev", "dis", "L", "kesin",
 ["TDVIA:turkmenistan", "TDVIA:turkmenler"], "",
 "Surların altına mayın yerleştiren Ruslar genel taarruzla kaleyi aldı; aman dileyen halkla birlikte bütün müdafiler öldürüldü. Skobelev 30 Ocak'ta Aşkābâd'a kadar ilerledi.",
 "Having mined the walls, the Russians stormed the fortress; all the defenders were killed along with the townspeople who begged for quarter. Skobelev advanced to Ashgabat on 30 January.", "land", TM),
]

LEFT = [
    {"name": "Evliyaata (1864)", "reason": "Hokand Hanlığı maddesi Çimkent ile birlikte işgal edildiğini yazar; muharebe ayrıntısı yok.", "source": "TDVIA:hokand-hanligi"},
    {"name": "Mergīnân'ın işgali (Eylül 1875)", "reason": "Mergīnân maddesine göre şehir direnişle karşılaşmadan işgal edildi.", "source": "TDVIA:merginan"},
    {"name": "Merv (1884)", "reason": "Merv ve Özbekler maddeleri yalnız ele geçirildiğini yazar; muharebe yok.", "source": "TDVIA:merv"},
    {"name": "Hokand isyanları (1878, 1882, 1892, 1893, 1898)", "reason": "Hokand Hanlığı maddesi toplu anar; muharebe ayrıntısı yok. Hanlık yıkıldıktan sonraki olaylar.", "source": "TDVIA:hokand-hanligi"},
    {"name": "1916 Türkistan ve Yedisu isyanı; Basmacı Hareketi (1918–1923)", "reason": "Hanlıkların yıkılışından sonraki ayaklanmalar; ayrı kapsam kararı gerekir.", "source": "TDVIA:kirgizistan"},
]

# İkinci kaynak turu (2026-10-30): Tansü ve Özdemir 2017 (Kenesarı İsyanı) Lebedov'un 1843 bozgununu, 14 Ağustos 1844 baskınını,
# 1845 sonbaharında Karatav'ın boşaltılmasını ve Kenesarı'nın 1847'de Ormon Han'ın Kırgızları'nca öldürülmesini yazar.
# Endican maddesi Rusya'nın şehri 1876'da aldığını yazar.
EXTRA_SRC = {
    "Lebedev ve Bisyanov'un yenilgisi (1843)": ["AKD:tansu-ozdemir-2017"],
    "Kenesarı'nın 1844 zaferi": ["AKD:tansu-ozdemir-2017"],
    "Karatav'ın boşaltılması (1845)": ["AKD:tansu-ozdemir-2017"],
    "Mey-Tuble (c. 1847)": ["AKD:tansu-ozdemir-2017"],
    "Endican (1876)": ["TDVIA:endican"],
    # Üçüncü kaynak turu (2026-10-30): Derekov 2015 (Rus İstilasına Karşı Türkmen Direnişi) Akmescid'in 3–27 Temmuz 1853 kuşatmasını,
    # Çimkent'in 22 Eylül 1864'te düşüşünü, Buhara'nın 5 Mayıs 1866 yenilgisini (İrcar), 12 Mayıs 1877 Kızılarvat'ı (Nur Verdi Han)
    # ve Ocak 1881'de Yengi Kale'nin alınışını yazar. Peler ve Korkmaz 2024 (Göktepe savaşlarında Kozaklar) Bendesen geçidi çatışmasını
    # ve iki Göktepe muharebesini, Sadullayeva 2022 II. Göktepe'yi (12 Ocak 1881, Jülyen) anlatır.
    # Selçuk ve Gümbür 2022 (Kenesarı Kasımoğlu önderliğinde kurtuluş mücadelesi) 1837'de Akdağ ve Akmola baskınlarını ve üzerine
    # gönderilen küçük Rus birliğinin kayıpla çekilişini, ardından gelen takviyeyle Kenesarı'nın Irgız–Turgay'a çekilmek zorunda
    # kalışını yazar. Keserci 2020 (Hokand örneği) Akmescid'in Temmuz 1853'te alınışını ve Ağustos 1875'te Mihrem kalesi önlerindeki
    # Rus zaferini anlatır.
    "Kenesarı'nın ilk savaşı (1837)": ["AKD:selcuk-gumbur-2022"],
    "Kenesarı'nın ikinci savaşı (1838)": ["AKD:selcuk-gumbur-2022"],
    "Hokand (1875)": ["AKD:keserci-2020"],
    "Akmescid (1853)": ["AKD:derekov-2015", "AKD:keserci-2020"],
    "Çimkent'in düşüşü (1864)": ["AKD:derekov-2015"],
    "İrcar (1866)": ["AKD:derekov-2015"],
    "Kızılarvat (1877)": ["AKD:derekov-2015"],
    "Büyük Bendesen geçidi (1879)": ["AKD:peler-korkmaz-2024"],
    "Göktepe (1879)": ["AKD:derekov-2015", "AKD:peler-korkmaz-2024"],
    "Yengikale (1881)": ["AKD:derekov-2015"],
    "Göktepe (1881)": ["AKD:derekov-2015", "AKD:peler-korkmaz-2024", "AKD:sadullayeva-2022"],
}
# Kaynakların tarihi farklı verdiği kayıtlar: kayıttaki tarih korunur, fark ihtilaf notuna yazılır
EXTRA_DISP = {
    "Büyük Bendesen geçidi (1879)": "Peler ve Korkmaz 2024 çatışmayı Lazarev'in 14 Ağustos 1879'daki ölümünden sonra, Lomakin'in Göktepe yürüyüşüne koyar (Haziran değil, Ağustos sonu).",
    "Göktepe (1881)": "Türkçe makaleler kalenin alınışını 12 Ocak 1881 (Jülyen takvimi) olarak verir; kayıttaki 24 Ocak Miladi karşılığıdır.",
    "Hokand (1875)": "Keserci 2020 Ağustos 1875 muharebesini Hokand şehri değil, hanlığa bağlı Mihrem (Mahram) kalesi önlerine koyar.",
    "Kenesarı'nın ikinci savaşı (1838)": "Selçuk ve Gümbür 2022 bu safhayı tarihsiz verir: Rus takviyesi üzerine Kenesarı Irgız ve Turgay'a çekildi.",
    "İrcar (1866)": "Derekov 2015 Rus saldırısını 5 Mayıs 1866 (Jülyen) olarak verir; muharebenin adını anmaz.",
}

recs = []
for i, r in enumerate(R, 1):
    (ntr, nen, date, war, place, lat, lon, loc, country, sa, sb, tc, oc, cat, res, status, src, disp, note, note_en, typ, state) = r
    src = src + [x for x in EXTRA_SRC.get(ntr, []) if x not in src]
    rec = {"id": i, "name_tr": ntr, "name_en": nen, "date": date, "hijri": "", "type": typ, "war": war, "place": place,
           "lat": lat, "lon": lon, "loc": loc, "country": country, "side_a": sa, "side_b": sb, "turkic_cmd": tc, "opp_cmd": oc,
           "category": cat, "result": res, "status": status, "sources": src,
           "verify": {"tdvia": any(x.startswith("TDVIA:") for x in src), "tdvia2": len([s for s in src if s.startswith("TDVIA:")]) >= 2, "wp": False, "rom": False, "academic": any(x.startswith("AKD:") for x in src)},
           "state": state, "home_batch": HB}
    if ntr in EXTRA_DISP: disp = (disp + " " if disp else "") + EXTRA_DISP[ntr]
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    recs.append(rec)

dates = [re.sub(r"^c\. ", "", r["date"]) for r in recs]
assert dates == sorted(dates), [d for a, d in zip(dates, dates[1:]) if d < a]
pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 22 — Türkistan hanlıkları ve Rus istilâsı (1837–1881)", "compiled": "2026-10-30", "status": "İlk tur.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "turkistan-hanliklari.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
