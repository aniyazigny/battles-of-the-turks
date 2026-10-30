"""data/bozkir-devletleri.json dosyasını üretir (Parti 23: Hazarlar, Peçenekler, İdil Bulgarları ve Kırgızlar, 652–1361).

Kapsam kararı 2026-10-30 (erken Türk devletleri). TDVİA maddesi olan dört topluluk bu partide toplandı; Hun, Akhun, Avar ve
Tuna Bulgar devletleri akademik kaynak gerektirdiğinden sonraki partiye kaldı. Olaylar Hazarlar, Peçenekler, İdil Bulgar
Hanlığı, Kırgızlar maddeleriyle Cerrâh b. Abdullah, Selmân b. Rebîa, Bâhilî, Yezîd II, Mesleme b. Abdülmelik, Mervân II,
Tiflis, Oğuzlar, Kıpçaklar, Edirne, Bizans, Rusya ve Tataristan maddelerinden derlendi."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "bozkir-devletleri"
HZ = "Hazar Kağanlığı"
PC = "Peçenekler"
IB = "İdil Bulgar Hanlığı"
KG = "Kırgızlar"
WHA = "Hazar–Arap savaşları (642–799)"
WPB = "Peçenek–Bizans savaşları (1035–1091)"
RS = "Râşid halifeler"
EM = "Emevîler"
AB = "Abbâsîler"
KR = "Kiev Rus Knezliği"
BZ = "Bizans"

# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür, devlet)
R = [
("Belencer (652–653)", "Battle of Balanjar (652–653)", "652", WHA, "Belencer", 43.10, 47.00, "approx", "Rusya (Dağıstan)",
 HZ, RS, "", "Abdurrahman b. Rebîa el-Bâhilî, Selmân b. Rebîa", "dis", "W", "kesin",
 ["TDVIA:hazarlar", "TDVIA:selman-b-rebia", "TDVIA:bahili-abdurrahman-b-rebia", "TDVIA:dagistan"],
 "Hazarlar maddesi seferi Selmân'a, Bâhilî maddesi Abdurrahman'ın Hz. Osman'ın halifeliğinin sekizinci yılında şehid düştüğünü yazar; Selmân maddesine göre Abdurrahman'ın ölümünden sonra kumandayı alan Selmân Belencer önünde geri çekilip muhtemelen orada şehid oldu (32/652-53).",
 "Derbend geçidini aşıp başşehir Belencer'e kadar sokulan ilk İslâm ordusu Hazarlar'a yenildi; Hazar kuvvetleri İrmîniye'ye kadar ilerledi.",
 "The first Muslim army to cross the Derbent pass and reach the capital Balanjar was beaten; the Khazars advanced as far as Armenia.", "land", HZ),
("Büyük Bulgarya'nın yıkılışı (c. 665)", "Khazar destruction of Old Great Bulgaria (after 665)", "c. 665", "Hazar–Bulgar savaşı", "Kuban ve Azak bozkırı", 45.50, 39.50, "region", "Rusya",
 HZ, "Büyük Bulgarya (Kurt'un ardılları)", "", "", "turk_arasi", "W", "kesin",
 ["TDVIA:idil-bulgar-hanligi"], "Madde yıkılışı kurucu Kurt'un 665'teki ölümünden sonraya koyar; kesin yıl yok.",
 "Kurt'un ölümünden sonra Hazar saldırılarıyla yıkılan devletin bir kolu Tuna'ya göçüp 681'de Tuna Bulgar Devleti'ni, bir kolu İdil Bulgarları'nı kurdu.",
 "After Kubrat's death the state fell to Khazar attacks; one branch moved to the Danube and founded the Danube Bulgar state in 681, another the Volga Bulgars.", "land", HZ),
("Mesleme'nin Hazar seferi (708)", "Maslama's campaign against the Khazars (708)", "708", WHA, "Dağıstan", 42.50, 47.50, "region", "Rusya (Dağıstan)",
 EM, HZ, "", "Mesleme b. Abdülmelik", "dis", "L", "kesin",
 ["TDVIA:hazarlar"], "", "Mesleme kumandasındaki İslâm kuvvetleri Hazarlar üzerine yürüyüp bazı şehir ve kaleleri fethetti.",
 "Muslim forces under Maslama marched on the Khazars and took several towns and fortresses.", "land", HZ),
("Derbend (714)", "Capture of Derbent (714)", "714", WHA, "Derbend (Bâbülebvâb)", 42.06, 48.29, "known", "Rusya (Dağıstan)",
 EM, HZ, "", "Mesleme b. Abdülmelik", "dis", "L", "kesin",
 ["TDVIA:hazarlar"], "", "Mesleme Derbend geçidini ele geçirdi.", "Maslama took the Derbent pass.", "land", HZ),
("Azerbaycan akını (717–718)", "Khazar invasion of Azerbaijan (717–718)", "717", WHA, "Azerbaycan", 38.50, 47.00, "region", "Azerbaycan / İran",
 EM, HZ, "", "Hâtim b. Nu'mân el-Bâhilî", "dis", "L", "kesin",
 ["TDVIA:hazarlar"], "",
 "Mesleme'nin İstanbul kuşatması için bölgeden ayrılmasıyla Bizans'ın isteği doğrultusunda Kafkaslar'ı aşan Hazar ordusu Azerbaycan'ın büyük kısmını ele geçirdiyse de Hâtim b. Nu'mân tarafından durduruldu (99/717-18).",
 "When Maslama left for the siege of Constantinople, the Khazars crossed the Caucasus at Byzantium's request and overran most of Azerbaijan, but were stopped by Hatim b. al-Nu'man (99/717–18).", "land", HZ),
("Mercülhicâre (722–723)", "Battle of Marj al-Hijara (722–723)", "722", WHA, "Mercülhicâre (İrmîniye)", 40.50, 46.50, "region", "Azerbaycan / Ermenistan",
 HZ, EM, "", "Sübeyt en-Nehrânî", "dis", "W", "kesin",
 ["TDVIA:hazarlar", "TDVIA:yezid-ii", "TDVIA:cerrah-b-abdullah"], "",
 "Kıpçaklar ve diğer Türk boylarının yardımını sağlayan Hazarlar müslüman ordusunu bozguna uğrattı; kurtulanlar büyük sıkıntılar içinde Dımaşk'a vardı.",
 "Aided by Kipchaks and other Turkic tribes, the Khazars routed the Muslim army; the survivors reached Damascus in great distress.", "land", HZ),
("Nehrürrân ve Belencer (722)", "Battle of the Rān river and capture of Balanjar (722)", "722-08", WHA, "Nehrürrân ve Belencer", 43.10, 47.00, "approx", "Rusya (Dağıstan)",
 EM, HZ, "hakanın oğlu", "Cerrâh b. Abdullah el-Hakemî", "dis", "L", "kesin",
 ["TDVIA:cerrah-b-abdullah", "TDVIA:hazarlar", "TDVIA:yezid-ii"], "",
 "Hazarlar'ı Derbend'in altı fersah kuzeyindeki Nehrürrân'da yenen Cerrâh yoldaki kaleleri alıp Belencer'i kuşattı; iki tarafın ağır kayıplarından sonra şehre Rebîülevvel 104'te (Ağustos-Eylül 722) girdi.",
 "Defeating the Khazars on the Rān six parasangs north of Derbent, Jarrah took the forts on the way and besieged Balanjar, entering it in Rabi I 104 (August–September 722) after heavy losses on both sides.", "land", HZ),
("İrmîniye akını (723–724)", "Khazar raid into Armenia (723–724)", "723", WHA, "İrmîniye", 40.20, 45.00, "region", "Ermenistan / Azerbaycan",
 EM, HZ, "", "Cerrâh b. Abdullah el-Hakemî", "dis", "L", "kesin",
 ["TDVIA:cerrah-b-abdullah"], "", "Öç almak için Derbend'i geçip İrmîniye'ye akın eden Hazar ordusunu Cerrâh yenip bazı şehirleri ele geçirdi.",
 "When the Khazars crossed Derbent to raid Armenia in revenge, Jarrah defeated them and took several towns.", "land", HZ),
("Mugan (725–726)", "Khazar victory in Mughan (725–726)", "725", WHA, "Mugan", 39.60, 48.30, "region", "Azerbaycan",
 HZ, EM, "Barcık (hakanın oğlu)", "Cerrâh b. Abdullah el-Hakemî", "dis", "W", "kesin",
 ["TDVIA:cerrah-b-abdullah"], "", "Komşu hükümdarlardan yardım alan Hazar ordusu Mugan'a kadar ilerledi; yardımcı kuvvetleri beklemeden savaşa giren Cerrâh ağır bir yenilgiye uğrayıp azledildi.",
 "Reinforced by neighbouring rulers, the Khazar army advanced to Mughan; Jarrah, fighting without waiting for reinforcements, was heavily defeated and dismissed.", "land", HZ),
("Allân (727)", "Maslama's victory in Alania (727)", "727", WHA, "Allân bölgesi", 43.20, 44.50, "region", "Rusya (Kuzey Kafkasya)",
 EM, HZ, "Türk hakanı", "Mesleme b. Abdülmelik", "dis", "L", "kesin",
 ["TDVIA:mesleme-b-abdulmelik"], "", "Mesleme Kafkas cephesindeki seferinden Allân bölgesinde Türk hakanını yenerek döndü.",
 "Maslama returned from his Caucasus campaign having defeated the Turkish khagan in Alania.", "land", HZ),
("Belencer ve Beyzâ (729)", "Jarrah takes Balanjar and al-Bayda (729)", "729", WHA, "Belencer ve Beyzâ", 43.10, 47.00, "region", "Rusya (Dağıstan)",
 EM, HZ, "", "Cerrâh b. Abdullah el-Hakemî", "dis", "L", "kesin",
 ["TDVIA:cerrah-b-abdullah"], "", "Yeniden vali olan Cerrâh yazın Tiflis üzerinden Belencer'e yürüyüp orayı, ardından Hazar başşehri Beyzâ'yı aldı.",
 "Reappointed, Jarrah marched via Tiflis to Balanjar in summer, took it and then the Khazar capital al-Bayda.", "land", HZ),
("Erdebil (730)", "Battle of Ardabil (730)", "730", WHA, "Erdebil", 38.25, 48.30, "known", "İran",
 HZ, EM, "", "Cerrâh b. Abdullah el-Hakemî", "dis", "W", "kesin",
 ["TDVIA:cerrah-b-abdullah", "TDVIA:hazarlar"], "",
 "Cerrâh'ın kışlamak için Azerbaycan'a dönmesinden faydalanan Hazarlar Erdebil yanındaki savaşı kazandı; Cerrâh ve askerlerinin çoğu öldü. Erdebil'i işgal eden Hazarlar Musul civarına kadar akın etti.",
 "Exploiting Jarrah's withdrawal to winter in Azerbaijan, the Khazars won the battle near Ardabil; Jarrah and most of his men fell. Occupying Ardabil, the Khazars raided as far as Mosul.", "land", HZ),
("Mervân'ın Hazar seferi (c. 737)", "Marwan's invasion of Khazaria (c. 737)", "c. 737", WHA, "İdil (Hazar başşehri) yolu", 46.50, 46.00, "region", "Rusya",
 EM, HZ, "Hazar hakanı", "Mervân b. Muhammed (Mervân II)", "dis", "L", "kesin",
 ["TDVIA:hazarlar", "TDVIA:mervan-ii"], "Maddeler sefere yıl vermez: Mervân 114'te (732) valiliğe atandı ve on iki yıl Hazarlar'a karşı başarılı seferler yaptı. Yıl yaklaşıktır.",
 "Derbend'i aşıp Belencer'e giren Mervân 150.000 kişilik orduyla iki koldan yeni başşehir İdil'e yürüdü; hakanın gönderdiği 40.000 kişilik ordu yenildi, 10.000 ölü ve 7000 esir verdi. Hakanın İslâmiyet'i kabulü şartıyla barış yapıldı.",
 "Crossing Derbent and entering Balanjar, Marwan advanced on the new capital Itil in two columns with 150,000 men; the khagan's 40,000-strong army was beaten with 10,000 dead and 7,000 captured. Peace was made on condition of the khagan's conversion.", "land", HZ),
("Tiflis (764)", "Khazar capture of Tiflis (764)", "764", "Hazar–Abbâsî savaşı (764)", "Tiflis", 41.69, 44.80, "known", "Gürcistan",
 HZ, AB, "As-Tarhan", "", "dis", "W", "kesin",
 ["TDVIA:hazarlar", "TDVIA:tiflis"], "",
 "Azerbaycan valisi Yezîd b. Üseyd ile evlendirilen hakan kızının doğumda ölmesinde kasıt arayan hakan As-Tarhan kumandasında bir orduyu İslâm topraklarına gönderdi; Tiflis ele geçirildi.",
 "Suspecting foul play in the death in childbirth of his daughter, married to the governor Yazid b. Usayd, the khagan sent an army under As-Tarkhan into Muslim lands; Tiflis was taken.", "land", HZ),
("Peçenekler'in İdil'in batısına sürülmesi (889)", "Khazar–Oğuz expulsion of the Pechenegs (889)", "889", "Hazar–Peçenek savaşı", "İdil ile Yayık arası", 49.00, 50.00, "region", "Rusya / Kazakistan",
 "Hazarlar ve Oğuzlar", PC, "", "", "turk_arasi", "W", "kesin",
 ["TDVIA:pecenekler", "TDVIA:oguzlar"], "Peçenekler maddesi 276/889 ve ayrıca 898, Oğuzlar maddesi 898–902 der.",
 "Hazarlar Oğuzlar'la ittifak kurup Peçenekler'e hücum etti ve onları İdil'in batısına geçmeye mecbur bıraktı.",
 "The Khazars allied with the Oğuz, attacked the Pechenegs and forced them west of the Volga.", "land", HZ),
("Macarlar'ın sürülmesi (895)", "Pecheneg expulsion of the Magyars (895)", "895", "Peçenek–Macar savaşı (895)", "Etelköz (Dinyeper–Tuna arası)", 47.00, 30.00, "region", "Ukrayna / Moldova",
 PC, "Macarlar", "", "", "dis", "W", "kesin",
 ["TDVIA:pecenekler"], "", "Bulgar kralı Simeon'un müttefiki olan Peçenekler Macarlar'a saldırıp onları Pannonia'ya göçe zorladı ve Don'dan Tuna'ya kadar bozkırı ele geçirdi.",
 "As allies of Tsar Simeon of Bulgaria the Pechenegs attacked the Magyars, drove them into Pannonia and took the steppe from the Don to the Danube.", "land", PC),
("K'i-tan istilâsı (920)", "Khitan expulsion of the Kyrgyz from the Ötüken (920)", "920", "Kırgız–K'i-tan savaşı", "Ötüken", 47.50, 102.50, "region", "Moğolistan",
 "K'i-tanlar", KG, "", "", "dis", "L", "kesin",
 ["TDVIA:kirgizlar"], "", "Bütün Moğolistan'ı ele geçiren K'i-tanlar Kırgızlar'ı Ötüken'den çıkarıp eski yurtlarına sürdü.",
 "Conquering all Mongolia, the Khitans drove the Kyrgyz out of the Ötüken back to their old homeland.", "land", KG),
("Rus istilâsı (964)", "Sviatoslav's attack on the Volga Bulgars (964)", "964", "Rus–Bulgar savaşları", "İdil Bulgar ülkesi", 54.98, 49.03, "region", "Rusya (Tataristan)",
 IB, KR, "", "Svyatoslav", "dis", "W", "ihtilafli",
 ["TDVIA:idil-bulgar-hanligi", "TDVIA:rusya"], "İdil Bulgar Hanlığı maddesi 964 ve 985 Rus istilâlarının etkisiz hale getirildiğini, Rusya maddesi Svyatoslav'ın Volga Bulgarları'nı yendiğini yazar (P6: Türk kaynağı tercih edildi; ihtilaflı).",
 "", "", "land", IB),
("Hazar Kağanlığı'nın çöküşü (965)", "Sviatoslav's destruction of Khazaria (965)", "965", "Rus–Hazar savaşı (965–969)", "İdil (Hazar başşehri)", 46.35, 48.05, "approx", "Rusya",
 KR, HZ, "", "Svyatoslav", "dis", "L", "kesin",
 ["TDVIA:hazarlar", "TDVIA:idil-bulgar-hanligi", "TDVIA:rusya"], "Hazarlar maddesi başşehrin 968 sonrasındaki Rus seferlerinde harap olduğunu ekler.",
 "Ruslar'dan ağır bir darbe yiyen Hazar Hakanlığı zayıfladı, hakan 965'te Hârizmliler'e sığındı; İdil Bulgarları bu yıl tam bağımsızlık kazandı.",
 "Struck a heavy blow by the Rus, the Khazar khaganate collapsed; the khagan took refuge with the Khwarazmians in 965 and the Volga Bulgars became fully independent.", "land", HZ),
("Dinyeper (972)", "Death of Sviatoslav at the Dnieper rapids (972)", "972", "Peçenek–Rus savaşları", "Dinyeper şelaleleri", 47.90, 35.10, "approx", "Ukrayna",
 PC, KR, "Küre", "Svyatoslav", "dis", "W", "kesin",
 ["TDVIA:pecenekler", "TDVIA:rusya"], "",
 "Bizans'ın müttefiki Peçenek başbuğu Küre 'Rus İskenderi' denilen Svyatoslav'ı yendi; Rus prensi savaş meydanında kaldı.",
 "The Pecheneg chief Küre, an ally of Byzantium, defeated Sviatoslav, called the 'Alexander of the Rus'; the prince fell on the field.", "land", PC),
("Rus istilâsı (985)", "Rus attack on the Volga Bulgars (985)", "985", "Rus–Bulgar savaşları", "İdil Bulgar ülkesi", 54.98, 49.03, "region", "Rusya (Tataristan)",
 IB, KR, "", "", "dis", "W", "borderline",
 ["TDVIA:idil-bulgar-hanligi"], "", "Kiev Rus Knezliği'nin ikinci istilâsı etkisiz hale getirildi; muharebe ayrıntısı yok.",
 "The second Kievan invasion was repelled; no battle details are given.", "land", IB),
("Yaroslav'ın zaferi (1036)", "Yaroslav's victory over the Pechenegs at Kiev (1036)", "1036", "Peçenek–Rus savaşları", "Kiev", 50.45, 30.52, "approx", "Ukrayna",
 KR, PC, "", "Yaroslav", "dis", "L", "kesin",
 ["TDVIA:pecenekler"], "Madde yalnızca Yaroslav'ın hükümdarlığını (1036–1054) verir; yıl yaklaşıktır.",
 "Prens Yaroslav Peçenekler'i ağır bir yenilgiye uğrattı; bu yenilgi ve Uz baskısı yüzünden Peçenekler Tuna kıyılarına göçtü.",
 "Prince Yaroslav inflicted a heavy defeat on the Pechenegs; this and Uz pressure drove them to the Danube.", "land", PC),
("Balkan akını (1048–1049)", "Pecheneg invasion of the Balkans (1048–1049)", "1048", WPB, "Bulgaristan ve Edirne", 42.20, 25.80, "region", "Bulgaristan / Türkiye",
 PC, BZ, "", "", "dis", "W", "borderline",
 ["TDVIA:pecenekler", "TDVIA:edirne"], "Peçenekler maddesi akını 1048'e, Edirne maddesi Edirne'ye hücumu 1049'a koyar.",
 "Bulgaristan'ı yakıp yıkan Peçenekler Balkanlar'ın diğer bölgelerini de yağmaladı; akın olduğu için borderline.",
 "The Pechenegs ravaged Bulgaria and plundered other Balkan regions; borderline as a raid.", "land", PC),
("Uzlar'ın dağıtılması (1065)", "Pecheneg defeat of the Uzes in the Balkans (1065)", "1065", "Peçenek–Uz savaşı", "Balkanlar", 43.00, 25.50, "region", "Bulgaristan",
 PC, "Uzlar (Oğuzlar)", "", "", "turk_arasi", "W", "kesin",
 ["TDVIA:pecenekler"], "", "Kıpçak baskısıyla Tuna'yı geçip Balkanlar'da geniş bir yağma akınına girişen Uzlar Peçenekler tarafından dağıtıldı (1064–1065).",
 "The Uzes, who crossed the Danube under Kipchak pressure and raided widely in the Balkans, were scattered by the Pechenegs (1064–1065).", "land", PC),
("Edirne (1078)", "Pecheneg–Cuman siege of Adrianople (1078)", "1078", WPB, "Edirne", 41.68, 26.56, "known", "Türkiye",
 BZ, "Peçenekler ve Kıpçaklar", "", "", "dis", "L", "kesin",
 ["TDVIA:pecenekler", "TDVIA:kipcaklar", "TDVIA:edirne"], "",
 "Malazgirt'ten sonraki karışıklıktan faydalanan Peçenekler Kıpçaklar'la birlikte Edirne'yi ikinci kez kuşattı; Bizanslılar onları geri çekilmeye mecbur bıraktı.",
 "Exploiting the disorder after Manzikert, the Pechenegs and Cumans besieged Adrianople a second time; the Byzantines forced them back.", "land", PC),
("Silistre (c. 1087)", "Battle of Dristra (c. 1087)", "c. 1087", WPB, "Silistre", 44.12, 27.26, "known", "Bulgaristan",
 PC, BZ, "", "", "dis", "W", "kesin",
 ["TDVIA:pecenekler", "TDVIA:silistre"], "Peçenekler maddesi savaşı 1078 ile 1091 arasında yılsız anlatır; yıl yaklaşıktır. Silistre maddesi şehrin XI. yüzyılda Peçenekler'ce defalarca alındığını ve Tatuş kumandasındaki Peçenekler'in bir süre burada yerleştiğini yazar.",
 "Bizanslılar Silistre yakınlarında Peçenekler tarafından ağır bir yenilgiye uğratıldı.",
 "The Byzantines suffered a heavy defeat by the Pechenegs near Dristra.", "land", PC),
("Levunion (1091)", "Battle of Levounion", "1091-04-29", WPB, "Levunion (Meriç ağzı)", 40.80, 26.20, "approx", "Türkiye",
 "Bizans ve Kumanlar", PC, "", "Aleksios Komnenos", "dis", "L", "kesin",
 ["TDVIA:pecenekler", "TDVIA:bizans", "TDVIA:istanbul", "TDVIA:dobruca"], "",
 "Çaka Bey ile anlaşıp 1090–91 kışında İstanbul'u karadan ve denizden kuşatan Peçenekler'e karşı Kumanlar'la anlaşan imparator onları kanlı bir savaşta ağır yenilgiye uğrattı; Anna Komnini'ye göre küçük bir topluluk sağ kurtuldu, Peçenekler siyasî ve askerî güç olmaktan çıktı.",
 "Allied with the Cumans against the Pechenegs, who had besieged Constantinople by land and sea with Çaka Bey in winter 1090–91, the emperor crushed them in a bloody battle; per Anna Komnene only a small group survived and the Pechenegs ceased to be a power.", "land", PC),
("Kırgızlar'ın yenilgisi (1218)", "Jochi's subjugation of the Kyrgyz (1218)", "1218", "Moğol istilâsı", "Yenisey", 53.70, 91.40, "region", "Rusya",
 "Moğollar", KG, "", "Cuci", "dis", "L", "kesin",
 ["TDVIA:kirgizlar"], "", "1217'de Moğollar'a karşı direnmeye kalkışan Kırgızlar ertesi yıl Cuci tarafından yenilip yeniden imparatorluğa bağlandı.",
 "The Kyrgyz, who tried to resist the Mongols in 1217, were defeated by Jochi the next year and resubjugated.", "land", KG),
("Samara (1223)", "Volga Bulgar ambush of the Mongols (1223)", "1223", "Moğol istilâsı", "İdil Bulgar sınırı (Samara dirseği)", 53.20, 50.10, "region", "Rusya",
 IB, "Moğollar", "", "", "dis", "W", "kesin",
 ["TDVIA:idil-bulgar-hanligi"], "", "Kalka Savaşı'nda Rus ve Kuman-Kıpçak ordularını bozguna uğratan Moğol ordusu İdil Bulgarları tarafından imha edildi.",
 "The Mongol army that had routed the Rus and Cuman-Kipchak armies at the Kalka was destroyed by the Volga Bulgars.", "land", IB),
("Bulgar (1236)", "Mongol destruction of Volga Bulgaria (1236)", "1236", "Moğol istilâsı", "Bulgar şehri", 54.98, 49.03, "known", "Rusya (Tataristan)",
 "Moğollar", IB, "", "Batu Han", "dis", "L", "kesin",
 ["TDVIA:idil-bulgar-hanligi", "TDVIA:tataristan"], "",
 "Batu Han 1223 yenilgisinin intikamını almak için ülkeyi baştan başa yakıp yıktı; Bulgar şehri de aynı âkıbete uğradı ve ahalisinin çoğu öldürüldü.",
 "Avenging the 1223 defeat, Batu laid the whole country waste; the city of Bulgar shared the fate and most of its people were killed.", "land", IB),
("Pulat Timur'un saldırısı (1361)", "Golden Horde attack on Bulgar (1361)", "1361", "Altın Orda iç savaşları", "Bulgar şehri", 54.98, 49.03, "known", "Rusya (Tataristan)",
 "Altın Orda (Pulat Timur)", IB, "", "Pulat Timur", "turk_arasi", "L", "kesin",
 ["TDVIA:idil-bulgar-hanligi"], "", "İdil Bulgar hanlarının yeniden kuvvetlenme arzusu Altın Orda hanı Pulat Timur'un saldırısıyla son buldu.",
 "The Volga Bulgar princes' hopes of revival ended with the attack of the Golden Horde khan Pulad Temür.", "land", IB),
]

LEFT = [
    {"name": "Hazar–Arap savaşları (642–646)", "reason": "Hazarlar maddesi ilk İslâm akınlarını toplu anar.", "source": "TDVIA:hazarlar"},
    {"name": "Hazar akını (799)", "reason": "Hazarlar maddesi akını anar; sonuç belirtilmez.", "source": "TDVIA:hazarlar"},
    {"name": "Kiev kuşatması (968)", "reason": "Peçenekler maddesi kuşatmayı ve Svyatoslav'ın dönüşünü anar; sonuç belirtilmez.", "source": "TDVIA:pecenekler"},
    {"name": "Peçenek akınları (1035–1036)", "reason": "Peçenekler maddesi Tuna'yı geçen akınları toplu anar.", "source": "TDVIA:pecenekler"},
    {"name": "İstanbul kuşatması (1090–1091)", "reason": "Bizans maddesi Çaka Bey ile birlikte kuşatmayı anar; Levunion kaydının notunda.", "source": "TDVIA:bizans"},
    {"name": "Peçenek akınları (1197'ye kadar)", "reason": "Peçenekler maddesi toplu anar.", "source": "TDVIA:pecenekler"},
    {"name": "Kırgızlar'ın Cengiz'e bağlanması (1207)", "reason": "Kırgızlar maddesi itaat altına alındıklarını yazar; muharebe yok.", "source": "TDVIA:kirgizlar"},
    {"name": "Kıpçaklar (Kumanlar)", "reason": "Kapsam listesinde yok; Kıpçaklar maddesi Rus knezlikleriyle savaşları anar (1184). Kapsam kararı gerekir.", "source": "TDVIA:kipcaklar"},
]

# Bulgar maddesi (2026-10-30, Parti 24 taraması sırasında bulundu)
EXTRA_SRC = {
    "Samara (1223)": ["TDVIA:bulgar"],  # Moğol ordusuna saldırıp onları yendiler
    "Bulgar (1236)": ["TDVIA:bulgar"],  # Batu Han'ın emriyle bütün şehirleri yakılıp yıkıldı
    "Pulat Timur'un saldırısı (1361)": ["TDVIA:bulgar"],  # Pulat Timur'un saldırısıyla şehirleri yıkıldı
    # Çelik 2013 (Cerrâh b. Abdullah, İstem 21), ikinci kaynak turu 2026-10-30
    "Mercülhicâre (722–723)": ["AKD:celik-2013"],  # Sübeyt en-Nehrânî'nin ordusu Hazarlar'a yenildi (104/722-723)
    "Nehrürrân ve Belencer (722)": ["AKD:celik-2013"],  # Ran nehri savaşı, Belencer'in fethi (104/722-723)
    "İrmîniye akını (723–724)": ["AKD:celik-2013"],  # Ramazan 105: hakan Ermeniyye'ye yürüdü, Elzem'de (Kür–Aras arası) yenildi
    "Mugan (725–726)": ["AKD:celik-2013"],  # Cerrâh 107/725-726'da Hazarlar'a yenilip azledildi
    "Belencer ve Beyzâ (729)": ["AKD:celik-2013"],  # ikinci valilik: Tiflis üzerinden Belencer ve el-Beyzâ (111/729-730)
    "Erdebil (730)": ["AKD:celik-2013"],  # Erdebil yakınında yenilip şehid düştü (112/730)
    "Edirne (1078)": ["AKD:yucel-2006"],  # Kumanlar 1078'de isyan eden Peçenekler'le birlikte Edirne'yi kuşattı
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
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    recs.append(rec)

key = lambda d: re.sub(r"^(\d{3})\b", r"0\1", re.sub(r"^c\. ", "", d))
dates = [key(r["date"]) for r in recs]
assert dates == sorted(dates), [d for a, d in zip(dates, dates[1:]) if d < a]
pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 23 — Hazarlar, Peçenekler, İdil Bulgarları ve Kırgızlar (652–1361)", "compiled": "2026-10-30", "status": "İlk tur.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "bozkir-devletleri.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
