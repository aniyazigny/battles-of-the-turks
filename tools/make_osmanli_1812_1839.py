"""data/osmanli-1812-1839.json dosyasını üretir (Parti 15: II. Mahmud dönemi, 1812–1839)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "osmanli-1812-1839"
O = "Osmanlı Devleti"
WS = "Birinci Sırp isyanı (1804–1813)"
WV = "Vehhâbî seferi (1811–1818)"
WT = "Tepedelenli Ali Paşa isyanı (1820–1822)"
WY = "Yunan isyanı (1821–1829)"
WR = "Osmanlı–Rus savaşı (1828–1829)"
WA = "Fransa'nın Cezayir'i işgali (1830–1837)"
WB = "Arnavutluk ve Bosna isyanları (1831)"
WM = "Mehmed Ali Paşa isyanı (1831–1840)"
RU, FR = "Rusya", "Fransa"
REB = "Rum isyancıları"
VH = "Dir‘iye Emirliği (Vehhâbîler)"
MI = "Mısır Valisi Mehmed Ali Paşa kuvvetleri"
CZ = "Osmanlı Devleti (Cezayir)"
# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür)
R = [
("Mekke ve Medine'nin geri alınışı (1812–1813)", "Ottoman–Egyptian recovery of Mecca and Medina (1812–1813)", "1813", WV, "Medine ve Mekke", 22.90, 39.70, "region", "Suudi Arabistan",
 O, VH, "Tosun Paşa", "", "dis", "W", "kesin",
 ["TDVIA:vehhabilik", "TDVIA:taif"], "", "1811'de yola çıkan Mısır kuvvetleri 1813'e kadar iki şehri yeniden Osmanlı yönetimine aldı.",
 "The Egyptian forces that set out in 1811 brought both cities back under Ottoman rule by 1813.", "land"),
("Tâif (1813)", "Recapture of Taif (1813)", "1813-05-02", WV, "Tâif", 21.27, 40.42, "known", "Suudi Arabistan",
 O, VH, "Tosun Paşa", "", "dis", "W", "kesin",
 ["TDVIA:taif"], "", "", "", "land"),
("Belgrad'ın geri alınışı (1813)", "Ottoman recapture of Belgrade (1813)", "1813-10-03", WS, "Belgrad", 44.82, 20.45, "known", "Sırbistan",
 O, "Sırp isyancıları", "Sadrazam Hurşid Ahmed Paşa", "Kara Yorgi", "dis", "W", "kesin",
 ["TDVIA:hursid-ahmed-pasa", "TDVIA:sirbistan"], "", "İsyan bastırıldı; ordu Belgrad Kalesi'ne direnişsiz girdi, Kara Yorgi Avusturya'ya kaçtı.",
 "The revolt was crushed; the army entered Belgrade fortress unopposed and Karađorđe fled to Austria.", "land"),
("Dir‘iye (1818)", "Siege of Diriyah (1818)", "1818-09-09", WV, "Dir‘iye", 24.73, 46.57, "known", "Suudi Arabistan",
 O, VH, "İbrâhim Paşa (Kavalalı)", "Abdullah b. Suûd", "dis", "W", "kesin",
 ["TDVIA:kavalali-mehmed-ali-pasa", "TDVIA:ibrahim-pasa-kavalali", "TDVIA:vehhabilik", "TDVIA:lahsa"], "",
 "6 Nisan'da başlayan beş aylık kuşatmadan sonra alındı; Vehhâbî reisi Abdullah b. Suûd İstanbul'a götürülüp idam edildi.",
 "Taken after a five-month siege begun on 6 April; the Wahhabi leader Abdullah ibn Saud was taken to Istanbul and executed.", "land"),
("Yanya (1820–1822)", "Siege of Ioannina (1820–1822)", "1822-02-14", WT, "Yanya", 39.66, 20.85, "known", "Yunanistan",
 O, "Tepedelenli Ali Paşa", "Hurşid Ahmed Paşa", "Tepedelenli Ali Paşa", "ic", "C", "kesin",
 ["TDVIA:tepedelenli-ali-pasa", "TDVIA:hursid-ahmed-pasa"], "", "Kıstırılan Ali Paşa göldeki Pandeleimon Manastırı'na sığındı; 14 Şubat 1822'de çıkan çatışmada öldürüldü.",
 "Cornered, Ali Pasha took refuge in the Pandeleimon monastery on the lake; he was killed in the clash of 14 February 1822.", "land"),
("Navarin Kalesi (1821)", "Siege of Navarino (1821)", "1821-08", WY, "Navarin", 36.91, 21.70, "known", "Yunanistan",
 REB, O, "", "", "dis", "L", "kesin",
 ["TDVIA:navarin"], "", "Dört ay dayanan kale yardım gelmeyince teslim oldu.", "After holding out four months without relief the fortress surrendered.", "land"),
("Tripoliçe (1821)", "Siege of Tripolitsa (1821)", "1821", WY, "Tripoliçe", 37.51, 22.37, "known", "Yunanistan",
 REB, O, "", "", "dis", "L", "kesin",
 ["TDVIA:mora"], "", "1821 Yunan isyanında Tripoliçe'deki müslümanlar katledildi. (Kontrol turunda eklendi.)",
 "In the Greek revolt of 1821 the Muslims of Tripolitsa were massacred.", "land"),
("Sakız (1822)", "Chios revolt (1822)", "1822-04", WY, "Sakız adası", 38.37, 26.14, "known", "Yunanistan",
 O, REB, "Kaptanıderyâ Nasuhzâde Ali Paşa", "", "dis", "W", "kesin",
 ["TDVIA:sakiz-adasi"], "", "Sisam ve İpsara'dan gelen isyancılar kaleyi 23 Mart–11 Nisan arasında kuşattı; donanmanın ve takviyenin gelişiyle isyan bastırıldı.",
 "Rebels from Samos and Psara besieged the castle from 23 March to 11 April; the revolt was put down when the fleet and reinforcements arrived.", "land"),
("Gördüs (1822)", "Fall of Corinth (1822)", "1822", WY, "Gördüs", 37.94, 22.93, "known", "Yunanistan",
 REB, O, "Kâmil Bey", "", "dis", "L", "kesin",
 ["TDVIA:gordus"], "", "Kâmil Bey esir alındı.", "Kâmil Bey was taken prisoner.", "land"),
("Tripoliçe'nin geri alınışı (1825)", "Recapture of Tripolitsa (1825)", "1825-06-23", WY, "Tripoliçe", 37.51, 22.37, "known", "Yunanistan",
 O, REB, "Kavalalı İbrâhim Paşa", "", "dis", "W", "kesin",
 ["TDVIA:ibrahim-pasa-kavalali"], "", "Mora'ya çıkan İbrâhim Paşa önce Navarin'i (18 Mayıs), ardından Tripoliçe'yi (23 Haziran) zaptetti. (Kontrol turunda eklendi.)",
 "Having landed in the Morea, Ibrahim Pasha took Navarino (18 May) and then Tripolitsa (23 June).", "land"),
("Mesolongi (1826)", "Third siege of Missolonghi", "1826-04-23", WY, "Mesolongi (Mesleng)", 38.37, 21.43, "known", "Yunanistan",
 O, REB, "Reşid Mehmed Paşa, İbrâhim Paşa (Kavalalı)", "", "dis", "W", "kesin",
 ["TDVIA:ibrahim-pasa-kavalali", "TDVIA:resid-mehmed-pasa", "TDVIA:husrev-pasa-koca"], "",
 "Reşid Paşa Ağustos 1825'te kara tarafından kuşattı; İbrâhim Paşa'nın katılmasıyla isyancıların son direniş yeri alındı.",
 "Reşid Pasha invested it from the land side in August 1825; with İbrahim Pasha joining, the rebels' last stronghold was taken.", "land"),
("Navarin (1827)", "Battle of Navarino", "1827-10-20", WY, "Navarin limanı", 36.93, 21.69, "known", "Yunanistan",
 "İngiltere, Fransa ve Rusya", O, "", "Edward Codrington", "dis", "L", "kesin",
 ["TDVIA:navarin", "TDVIA:mahmud-ii--osmanli", "TDVIA:husrev-pasa-koca"], "",
 "Savaş hali yokken limandaki Osmanlı-Mısır donanmasına âni baskın yapıldı; elli iki gemi ve 6000 denizci kaybedildi.",
 "With no state of war, the Ottoman–Egyptian fleet in the harbour was suddenly attacked; fifty-two ships and 6,000 sailors were lost.", "sea"),
("Varna (1828)", "Siege of Varna (1828)", "1828-10", WR, "Varna", 43.21, 27.92, "known", "Bulgaristan",
 RU, O, "Sadrazam Dârendeli İzzet Mehmed Paşa", "Çar I. Nikola", "dis", "L", "kesin",
 ["TDVIA:varna", "TDVIA:resid-mehmed-pasa"], "", "Üç aylık kuşatmadan sonra alındı; sadrazam bu başarısızlık yüzünden azledildi.",
 "Taken after a three-month siege; the grand vizier was dismissed over the failure.", "land"),
("Kars (1828)", "Siege of Kars (1828)", "1828", WR, "Kars", 40.60, 43.10, "known", "Türkiye",
 RU, O, "", "", "dis", "L", "kesin",
 ["TDVIA:kars"], "", "Şehir işgal edilip tahrip edildi.", "The town was occupied and devastated.", "land"),
("Kulevçe (1829)", "Battle of Kulevcha", "1829-06", WR, "Külefçe Boğazı, Şumnu yakını", 43.13, 27.25, "approx", "Bulgaristan",
 RU, O, "Sadrazam Reşid Mehmed Paşa", "Hans Karl von Diebitsch", "dis", "L", "kesin",
 ["TDVIA:resid-mehmed-pasa"], "", "", "", "land"),
("Silistre (1829)", "Siege of Silistra (1829)", "1829", WR, "Silistre", 44.12, 27.26, "known", "Bulgaristan",
 RU, O, "", "", "dis", "L", "borderline",
 ["TDVIA:silistre"], "Silistre maddesi kalenin \"1827-1828 savaşı esnasında\" alındığını yazar; Edirne Antlaşması maddesine göre Ruslar Silistre'de 1836'ya kadar kaldı.",
 "Madde yalnızca kalenin alındığını anar.", "The article only states that the fortress was taken.", "land"),
("Erzurum (1829)", "Fall of Erzurum (1829)", "1829-07-08", WR, "Erzurum", 39.90, 41.27, "known", "Türkiye",
 RU, O, "", "İvan Paskeviç", "dis", "L", "kesin",
 ["TDVIA:erzurum"], "", "Edirne Antlaşması ile geri verildi (14 Eylül 1829).", "Returned under the Treaty of Edirne (14 September 1829).", "land"),
("Edirne (1829)", "Russian occupation of Edirne (1829)", "1829-08-22", WR, "Edirne", 41.68, 26.56, "known", "Türkiye",
 RU, O, "", "", "dis", "L", "borderline",
 ["TDVIA:edirne-antlasmasi", "TDVIA:mahmud-ii--osmanli"], "", "Rus kuvvetleri direnişle karşılaşmadan şehre girdi, Kırklareli ve Lüleburgaz'ı da işgal etti.",
 "Russian forces entered the city without resistance and also occupied Kırklareli and Lüleburgaz.", "land"),
("Cezayir (1830)", "Invasion of Algiers (1830)", "1830-07-05", WA, "Cezayir", 36.77, 3.06, "known", "Cezayir",
 FR, CZ, "Dayı Hüseyin Paşa", "", "dis", "L", "kesin",
 ["TDVIA:cezayir", "TDVIA:mahmud-ii--osmanli", "TDVIA:cezayirli-huseyin-pasa"], "", "1827'den beri abluka altındaki şehre çıkan Fransızlar 5 Temmuz'da işgal etti; dayı teslim oldu.",
 "The French, who had blockaded the city since 1827, landed and occupied it on 5 July; the dey surrendered.", "land"),
("Babuna (1831)", "Battle of Babuna (1831)", "1831-04-21", WB, "Babuna dağları, Pirlepe yakını", 41.40, 21.55, "approx", "Kuzey Makedonya",
 O, "Buşatlı Mustafa Paşa", "Sadrazam Reşid Mehmed Paşa", "Buşatlı Mustafa Paşa", "ic", "C", "kesin",
 ["TDVIA:resid-mehmed-pasa"], "", "Nizâmiye askerine karşı çıkan İşkodra valisi hezimete uğratıldı.", "The governor of Shkodër, who opposed the new army, was routed.", "land"),
("Priştine (1831)", "Battle near Pristina (1831)", "1831-07", WB, "Priştine yöresi", 42.66, 21.17, "approx", "Kosova",
 "Bosna âyanı (Boşnaklar)", O, "Sadrazam Reşid Mehmed Paşa", "", "ic", "C", "kesin",
 ["TDVIA:resid-mehmed-pasa"], "", "Boşnaklar sadrazam karşısında başarı kazandı.", "The Bosnians prevailed against the grand vizier.", "land"),
("Zerrâa (1832)", "Battle of Zerrâa (1832)", "1832-04-14", WM, "Zerrâa mevkii, Suriye", 34.40, 36.00, "region", "Suriye",
 MI, O, "", "İbrâhim Paşa (Kavalalı)", "ic", "C", "kesin",
 ["TDVIA:ibrahim-pasa-kavalali"], "", "İbrâhim Paşa'nın Osmanlı kuvvetleriyle ilk karşılaşması.", "İbrahim Pasha's first encounter with Ottoman forces.", "land"),
("Akkâ (1832)", "Siege of Acre (1831–1832)", "1832-05-27", WM, "Akkâ", 32.92, 35.07, "known", "İsrail",
 MI, O, "Akkâ Valisi Abdullah Paşa", "İbrâhim Paşa (Kavalalı)", "ic", "C", "kesin",
 ["TDVIA:kavalali-mehmed-ali-pasa", "TDVIA:ibrahim-pasa-kavalali", "TDVIA:akka"], "", "Altı aylık kuşatmadan sonra teslim oldu.", "Surrendered after a six-month siege.", "land"),
("Belen (1832)", "Battle of Beylan", "1832-07-29", WM, "Belen geçidi", 36.49, 36.22, "known", "Türkiye",
 MI, O, "Ağa Hüseyin Paşa", "İbrâhim Paşa (Kavalalı)", "ic", "C", "kesin",
 ["TDVIA:ibrahim-pasa-kavalali"], "", "Halep'in alınmasından (15 Temmuz) sonra yapıldı.", "Fought after the capture of Aleppo (15 July).", "land"),
("Konya (1832)", "Battle of Konya", "1832-12-21", WM, "Konya", 37.87, 32.49, "known", "Türkiye",
 MI, O, "Sadrazam Reşid Mehmed Paşa", "İbrâhim Paşa (Kavalalı)", "ic", "C", "kesin",
 ["TDVIA:mahmud-ii--osmanli", "TDVIA:ibrahim-pasa-kavalali", "TDVIA:resid-mehmed-pasa", "TDVIA:konya"], "",
 "Osmanlı ordusu dağıldı, sadrazam esir düştü; Mısır kuvvetleri Kütahya'ya kadar ilerledi (2 Şubat 1833).",
 "The Ottoman army broke up and the grand vizier was captured; the Egyptian forces advanced as far as Kütahya (2 February 1833).", "land"),
("Kostantîne (1836)", "First siege of Constantine (1836)", "1836", WA, "Kostantîne", 36.37, 6.61, "known", "Cezayir",
 CZ, FR, "Kostantîne Emîri Ahmed Bey", "", "dis", "W", "borderline",
 ["TDVIA:cezayir"], "", "Fransızlar Ahmed Bey karşısında ağır kayıplarla yenildi. Kostantîne Emîri Ahmed Bey dayının teslim olmasından sonra da mücadeleyi sürdürdü; Osmanlı adına savaştığı açık olmadığından kayıt borderline.",
 "The French were defeated by Ahmed Bey with heavy losses. Ahmed Bey, emir of Constantine, kept fighting after the dey surrendered; as it is unclear that he fought on the Ottoman side, the record is borderline.", "land"),
("Kostantîne (1837)", "Siege of Constantine (1837)", "1837-10-13", WA, "Kostantîne", 36.37, 6.61, "known", "Cezayir",
 FR, CZ, "Kostantîne Emîri Ahmed Bey", "", "dis", "L", "borderline",
 ["TDVIA:cezayir"], "", "Fransızlar batıdaki kuvvetlerini doğuya getirip şehri aldı.", "The French moved their western forces east and took the city.", "land"),
("Nizip (1839)", "Battle of Nezib", "1839-06-24", WM, "Nizip, Birecik yakını", 37.01, 37.79, "approx", "Türkiye",
 MI, O, "Hâfız Paşa", "İbrâhim Paşa (Kavalalı)", "ic", "C", "kesin",
 ["TDVIA:mahmud-ii--osmanli", "TDVIA:kavalali-mehmed-ali-pasa", "TDVIA:ibrahim-pasa-kavalali", "TDVIA:birecik"], "",
 "Kurmayında Moltke gibi Prusyalı subaylar bulunan Osmanlı ordusu yenildi; Anadolu yolu yeniden açıldı.",
 "The Ottoman army, whose staff included Prussian officers such as Moltke, was defeated, reopening the road into Anatolia.", "land"),
]

LEFT = [
 {"name": "Tripoliçe (1821) ve Mora'daki diğer kaleler", "reason": "Tripoliçe maddesi yalnızca 1825'te savaşsız geri alındığını yazar; düşüş tarihi indirilen maddelerde yok.", "source": "TDVIA:tripolice"},
 {"name": "Dervenaki (1822), Dramalı Mahmud Paşa", "reason": "TDVİA'da adıyla bulunamadı.", "source": ""},
 {"name": "Atina (1826–1827)", "reason": "Atina maddesi kalenin Reşid Paşa tarafından kurtarıldığını tarihsiz anar.", "source": "TDVIA:atina"},
 {"name": "Osmanlı–İran savaşı (1821–1823)", "reason": "Erzurum maddesi yalnızca barışı anar; savaşlar indirilen maddelerde yok.", "source": "TDVIA:erzurum"},
 {"name": "Bosna isyanının diğer çatışmaları (Hüseyin Kapudan, 1831–1832)", "reason": "Bosna-Hersek maddesinde ayrıntı bulunamadı.", "source": "TDVIA:resid-mehmed-pasa"},
 {"name": "Vehhâbî seferinin diğer savaşları (Turabe, Bîşe, er-Res)", "reason": "Kavalalı ve İbrâhim Paşa maddeleri toplu anlatır.", "source": "TDVIA:ibrahim-pasa-kavalali"},
 {"name": "Vak‘a-i Hayriyye (1826)", "reason": "Yeniçeriliğin kaldırılması; savaş sayılmadı.", "source": "TDVIA:mahmud-ii--osmanli"},
]

# İkinci kaynak turu
EXTRA_SRC = {"Tripoliçe'nin geri alınışı (1825)": ["TDVIA:tripolice"],   # kontrol turu
             "Mekke ve Medine'nin geri alınışı (1812–1813)": ["TDVIA:mekke", "TDVIA:medine"],
             "Dir‘iye (1818)": ["TDVIA:abdullah-b-suud", "TDVIA:medine"],
             "Sakız (1822)": ["TDVIA:mora"],
             "Kars (1828)": ["TDVIA:edirne-antlasmasi"],
             "Silistre (1829)": ["TDVIA:edirne-antlasmasi"],
             "Erzurum (1829)": ["TDVIA:edirne-antlasmasi"],
             "Babuna (1831)": ["TDVIA:mustafa-pasa-busatli"],
             "Priştine (1831)": ["TDVIA:bosna-hersek"],
             "Zerrâa (1832)": ["TDVIA:kavalali-mehmed-ali-pasa"],
             "Belen (1832)": ["TDVIA:kavalali-mehmed-ali-pasa", "TDVIA:huseyin-pasa-aga"],
             "Kostantîne (1836)": ["TDVIA:kostantine", "TDVIA:abdulkadir-el-cezairi"],
             "Kostantîne (1837)": ["TDVIA:kostantine", "TDVIA:abdulkadir-el-cezairi"]}
FIX = {"Tripoliçe'nin geri alınışı (1825)": {"status": "borderline", "note": "Mora'ya çıkan İbrâhim Paşa önce Navarin'i (18 Mayıs), ardından Tripoliçe'yi (23 Haziran) zaptetti. Tripoliçe maddesi şehrin savaşsız geri alındığını yazdığından borderline. (Kontrol turunda eklendi.)", "note_en": "Having landed in the Morea, Ibrahim Pasha took Navarino (18 May) and then Tripolitsa (23 June). Borderline, as the Tripolitsa article says the town was retaken without a fight."},
       "Mekke ve Medine'nin geri alınışı (1812–1813)": {
           "note": "Tosun Paşa iki haftalık kuşatmadan sonra Medine'yi 3 Aralık 1812'de geri aldı; Mekke'ye Şerîf Gālib'in yardımıyla 23 Ocak 1813'te girdi.",
           "note_en": "Tosun Pasha retook Medina on 3 December 1812 after a two-week siege, and entered Mecca with the help of Sharif Ghalib on 23 January 1813."},
       "Silistre (1829)": {"status": "kesin", "opp_cmd": "Hans Karl von Diebitsch",
           "dispute": "Silistre maddesi kalenin \"1827-1828 savaşı esnasında\" alındığını yazar; Edirne Antlaşması maddesi düşüşü 1829'daki ikinci harekâta, Diebitsch'in Edirne'ye yürüyüşünden önceye koyar.",
           "note": "Edirne Antlaşması'na göre Silistre savaş tazminatı ödenene kadar Rus elinde rehin kaldı.",
           "note_en": "Under the Treaty of Edirne Silistra stayed in Russian hands as a pledge until the indemnity was paid."},
       "Belen (1832)": {"turkic_cmd": "Serasker Ağa Hüseyin Paşa"},
       "Kostantîne (1836)": {"status": "kesin",
           "dispute": "Kostantîne maddesi Ahmed Bey'in burada bağımsız bir beylik kurmaya çalıştığını yazar; Abdülkādir el-Cezâirî maddesi onu \"Osmanlı tâbiiyetini sürdüren\" bir yönetici olarak anar. Bâbıâli'den paşa unvanı aldığı için Osmanlı tarafı sayıldı.",
           "note": "Genel Vali Mareşal Clauzel'in saldırısı Ahmed Bey tarafından geri püskürtüldü.",
           "note_en": "Governor-General Marshal Clauzel's attack was beaten back by Ahmed Bey."},
       "Kostantîne (1837)": {"status": "kesin", "opp_cmd": "General Valée",
           "dispute": "Ahmed Bey'in statüsü için 1836 kaydına bakınız.",
           "note": "Şehir General Valée kumandasındaki Fransız ordusunun kanlı bir hücumuyla alındı; Ahmed Bey Sahrâ'ya çekilip on bir yıl daha savaştı.",
           "note_en": "The city fell to a bloody assault by the French army under General Valée; Ahmed Bey withdrew to the Sahara and fought on for eleven more years."}}
NEW = {"Navarin Kalesi (1821)": [
        ("Benefşe (1821)", "Siege of Monemvasia (1821)", "1821", WY, "Benefşe (Monemvasia)", 36.69, 23.06, "known", "Yunanistan",
         REB, O, "", "", "dis", "L", "kesin",
         ["TDVIA:benefse"], "", "Açlık ve yokluk içindeki şehir dört aylık kuşatmadan sonra şartlı olarak teslim oldu.",
         "Starving and short of everything, the town surrendered on terms after a four-month siege.", "land")],
       "Gördüs (1822)": [
        ("Navarin'in geri alınışı (1825)", "Recapture of Navarino (1825)", "1825-05-18", WY, "Navarin", 36.91, 21.70, "known", "Yunanistan",
         O, REB, "İbrâhim Paşa (Kavalalı)", "", "dis", "W", "kesin",
         ["TDVIA:ibrahim-pasa-kavalali", "TDVIA:navarin"], "",
         "Mart 1825'te Modon'a çıkan İbrâhim Paşa önce Navarin'i, ardından Tripoliçe'yi (23 Haziran) aldı.",
         "Having landed at Modon in March 1825, İbrahim Pasha took Navarino first and then Tripolitsa (23 June).", "land")],
       "Akkâ (1832)": [
        ("Humus (1832)", "Battle of Homs (1832)", "1832-07-08", WM, "Humus", 34.73, 36.71, "known", "Suriye",
         MI, O, "Halep Valisi Mehmed Paşa", "İbrâhim Paşa (Kavalalı)", "ic", "C", "kesin",
         ["TDVIA:ibrahim-pasa-kavalali", "TDVIA:kavalali-mehmed-ali-pasa", "TDVIA:huseyin-pasa-aga"], "",
         "Şam'ı 16 Haziran'da alan İbrâhim Paşa, Ağa Hüseyin Paşa ordusunun öncüsünü yendi.",
         "İbrahim Pasha, who had taken Damascus on 16 June, defeated the vanguard of Ağa Hüseyin Pasha's army.", "land")]}
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
meta = {"batch": "Parti 15 — Osmanlı: II. Mahmud dönemi (1812–1839)", "compiled": "2026-10-29", "status": "İkinci kaynak turu yapıldı.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "osmanli-1812-1839.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
