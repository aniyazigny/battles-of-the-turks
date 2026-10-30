"""data/gazneli-karahanli.json dosyasını üretir (Parti 4: Gazneliler 977–1186 ve Karahanlılar 893–1212).
Selçuklularla yapılan savaşlar pilotta kayıtlıdır (opp_state ile bu devletlerin tablolarında da görünür); burada tekrar edilmez."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "gazneli-karahanli"
G, K = "Gazneliler", "Karahanlılar"
# (devlet, ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en)
R = [
(K, "Talas (Sâmânîler)", "Battle of Talas (893)", "893", "Karahanlı–Sâmânî", "Talas", 42.52, 72.23, "approx", "Kazakistan",
 "Sâmânîler", "Karahanlılar", "Kadır Han Oğulçak", "İsmâil b. Ahmed", "dis", "L", "kesin",
 ["TDVIA:karahanlilar", "TDVIA:satuk-bugra-han"], "", "Oğulçak Kâşgar'a çekildi. Kaynaktaki esir sayısı (15.000) alınmadı.", "Oghulchak withdrew to Kashgar. The source figure of 15,000 captives is not used."),
(K, "İsfîcâb'ın fethi", "Capture of Isfijab (990)", "990", "Karahanlı–Sâmânî", "İsfîcâb (Sayram)", 42.30, 69.75, "approx", "Kazakistan",
 "Karahanlılar", "Sâmânîler", "Hârun Buğra Han", "", "dis", "W", "borderline",
 ["TDVIA:karahanlilar", "TDVIA:harun-bugra-han"], "", "Muhalif Sâmânî kumandanlarının desteğiyle alındı; çatışmanın ayrıntısı yok.", "Taken with the help of dissident Samanid commanders; no detail of fighting."),
(G, "Hindûşâhîlere karşı (Lamgân)", "Battle against the Hindu Shahis (986–87)", "986–987", "Sebük Tegin'in Hint seferleri", "Lamgân–Peşâver arası", 34.40, 70.80, "region", "Afganistan",
 "Gazneliler", "Hindûşâhîler ve müttefik racalar", "Sebük Tegin", "Caypal", "dis", "W", "kesin",
 ["TDVIA:sebuk-tegin", "TDVIA:gazneliler"], "", "Sebük Tegin Kâbil nehri boyunca Peşâver'e kadar ilerledi. Caypal daha önce de iki kez yenilmişti.",
 "Sebüktegin advanced along the Kabul river as far as Peshawar. Jayapala had already been defeated twice."),
(G, "Herat (Ebû Ali Sîmcûrî)", "Battle of Herat (994)", "994", "Sâmânî iç savaşı", "Herat yakını", 34.35, 62.20, "approx", "Afganistan",
 "Gazneliler (Sâmânîler adına)", "Ebû Ali Sîmcûrî ve Fâik el-Hâssa", "Sebük Tegin, Mahmud", "Ebû Ali Sîmcûrî, Fâik", "dis", "W", "kesin",
 ["TDVIA:sebuk-tegin", "TDVIA:mahmud-i-gaznevi"], "", "Sebük Tegin Sâmânî emîri II. Nûh'un çağrısıyla savaştı.", "Sebüktegin fought at the call of the Samanid emir Nuh II."),
(G, "Tûs (Ebû Ali Sîmcûrî)", "Battle of Tus (995)", "995", "Sâmânî iç savaşı", "Tûs yakını", 36.48, 59.52, "approx", "İran",
 "Gazneliler", "Ebû Ali Sîmcûrî", "Sebük Tegin, Mahmud", "Ebû Ali Sîmcûrî", "dis", "W", "kesin",
 ["TDVIA:sebuk-tegin"], "", "Ebû Ali Buhara'da tutuklandı, Fâik Karahanlılara sığındı.", "Abu Ali was arrested in Bukhara; Fa'iq fled to the Karakhanids."),
(G, "Merv (Sâmânîler)", "Battle of Merv (999)", "999", "Gazneli–Sâmânî", "Merv yakını", 37.60, 61.83, "region", "Türkmenistan",
 "Gazneliler", "Sâmânîler", "Mahmud", "", "dis", "W", "borderline",
 ["TDVIA:mahmud-i-gaznevi"], "", "Horasan Gaznelilere geçti. Savaşın yeri kaynakta açık değil.", "Khurasan passed to the Ghaznavids. The site is not stated in the source."),
(G, "Gazne (998)", "Battle of Ghazni (998)", "998-03", "Gazneli taht mücadelesi", "Gazne yakını", 33.55, 68.42, "approx", "Afganistan",
 "Mahmud", "İsmâil b. Sebük Tegin", "Mahmud", "İsmâil", "ic", "C", "kesin",
 ["TDVIA:mahmud-i-gaznevi", "TDVIA:gazneliler"], "", "Mahmud kardeşi İsmâil'in kuvvetlerini yenip Gazneli tahtına çıktı (Rebîülevvel 388).", "Mahmud defeated his brother Isma'il and took the Ghaznavid throne (March 998)."),
(G, "Peşâver (Caypal)", "Battle of Peshawar (1001)", "1001-11", "Mahmud'un Hint seferleri", "Peşâver", 34.01, 71.57, "approx", "Pakistan",
 "Gazneliler", "Hindûşâhîler", "Mahmud", "Caypal", "dis", "W", "ihtilafli",
 ["TDVIA:mahmud-i-gaznevi"], "Tarih: TDVİA zaferi 392'ye (1002) koyar; yaygın tarih Kasım 1001'dir.",
 "Ardından Hindûşâhî merkezi Vayhand alındı.", "The Hindu Shahi capital Waihind was taken afterwards."),
(G, "Bhâtiya", "Siege of Bhatiya (1004–05)", "1004/1005", "Mahmud'un Hint seferleri", "Bhâtiya", 29.20, 71.80, "region", "Pakistan",
 "Gazneliler", "Bhâtiya racalığı", "Mahmud", "Beci Ray (Bacra)", "dis", "W", "kesin",
 ["TDVIA:mahmud-i-gaznevi"], "", "Üçüncü Hint seferi (395/1004-05). Bhâtiya'nın yeri tartışmalıdır (Bhera, Uç veya Bhatinda önerilir).", "Third Indian campaign (395/1004-05). The location of Bhatiya is disputed (Bhera, Uch or Bhatinda are proposed)."),
(G, "Mültan (1006)", "Multan (1006)", "1006", "Mahmud'un Hint seferleri", "Mültan", 30.20, 71.47, "known", "Pakistan",
 "Gazneliler", "Mültan Karmatîleri", "Mahmud", "Ebü'l-Fütûh Dâvûd", "dis", "W", "kesin",
 ["TDVIA:mahmud-i-gaznevi"], "", "", ""),
(G, "Belh (1008)", "Battle of Balkh (1008)", "1008-01", "Gazneli–Karahanlı", "Belh civarı", 36.76, 66.90, "approx", "Afganistan",
 "Gazneliler", "Karahanlılar", "Mahmud", "İlig Han Nasr, Yûsuf Kadır Han", "turk_arasi", "W", "ihtilafli",
 ["TDVIA:mahmud-i-gaznevi", "TDVIA:karahanlilar"], "Tarih: Mahmud maddesi Rebîülevvel 398 / Aralık 1007, Karahanlılar maddesi 398/1008.", "", ""),
(G, "Vayhand ovası (Anandpâl)", "Battle of Chach (1008)", "1008", "Mahmud'un Hint seferleri", "Vayhand karşısındaki ova", 34.05, 72.40, "approx", "Pakistan",
 "Gazneliler", "Hindûşâhîler ve müttefik racalar", "Mahmud", "Anandpâl", "dis", "W", "kesin",
 ["TDVIA:mahmud-i-gaznevi"], "", "Kaçanların sığındığı Nagarkot Kalesi üç günlük kuşatmayla alındı (399/1009).", "Nagarkot, where the fugitives took refuge, was taken after a three-day siege (399/1009)."),
(G, "Nagarkot (1009)", "Siege of Nagarkot (1009)", "1009", "Mahmud'un Hint seferleri", "Nagarkot (Bhim Nagar, Kangra)", 32.10, 76.27, "known", "Hindistan",
 "Gazneliler", "Hindûşâhîler (Anandpal)", "Mahmud", "Anandpal", "dis", "W", "kesin",
 ["TDVIA:mahmud-i-gaznevi", "TDVIA:hindusahiler"], "", "Vayhand savaşından kaçanların sığındığı Nagarkot Kalesi üç (Hindûşâhîler maddesine göre birkaç) günlük kuşatmadan sonra alındı. (Kontrol turunda eklendi.)",
 "The fortress of Nagarkot, where the fugitives from Vayhand had taken refuge, fell after a three-day siege."),
(G, "Mültan (1010)", "Multan (1010)", "1010", "Mahmud'un Hint seferleri", "Mültan", 30.20, 71.47, "known", "Pakistan",
 "Gazneliler", "Mültan Karmatîleri", "Mahmud", "", "dis", "W", "borderline",
 ["TDVIA:mahmud-i-gaznevi"], "", "Bölge zorlukla karşılaşmadan itaat altına alındı.", "The region submitted without serious resistance."),
(G, "Nandana (Triloçanpâl)", "Battle of Nandana (1014)", "1014", "Mahmud'un Hint seferleri", "Nandana kalesi", 32.72, 73.25, "approx", "Pakistan",
 "Gazneliler", "Hindûşâhîler", "Mahmud", "Triloçanpâl", "dis", "W", "kesin",
 ["TDVIA:mahmud-i-gaznevi"], "", "Zorlu bir savaştan sonra Nandana kalesi alındı; Mahmud ardından Keşmir'e kadar ilerledi (Palabıyık 2007: dokuzuncu sefer, 405/1014).", "After a hard battle Nandana fortress was taken; Mahmud then advanced towards Kashmir (Palabıyık 2007: ninth campaign, 405/1014)."),
(G, "Thânesâr (1014)", "Sack of Thanesar (1014)", "1014", "Mahmud'un Hint seferleri", "Thânesâr", 29.97, 76.83, "known", "Hindistan",
 "Gazneliler", "Thânesâr racası", "Mahmud", "", "dis", "W", "borderline",
 ["TDVIA:mahmud-i-gaznevi", "AKD:palabiyik-2007"], "", "Onuncu seferde racanın antlaşma teklifi kabul edilmedi; şehre girilip tapınaklar tahrip edildi. Muharebe adı geçmediği için borderline. (Kontrol turunda eklendi.)",
 "On the tenth expedition the raja's offer of terms was refused; the city was entered and its temples destroyed. Borderline, as no battle is named."),
(G, "Lokhot kuşatması", "Siege of Lohkot (1015)", "1015", "Mahmud'un Hint seferleri", "Lokhot (Loharin)", 33.90, 74.30, "approx", "Hindistan",
 "Keşmir", "Gazneliler", "Mahmud", "", "dis", "L", "kesin",
 ["TDVIA:mahmud-i-gaznevi"], "", "Şiddetli kış yüzünden kuşatma kaldırıldı.", "Lifted because of severe winter."),
(G, "Hârizm'in fethi (Hezâresb)", "Conquest of Khwarazm (1017)", "1017", "Gazneli–Me'mûnîler", "Hezâresb", 41.32, 61.07, "approx", "Özbekistan",
 "Gazneliler", "Hârizm (Me'mûnîler)", "Mahmud", "", "dis", "W", "borderline",
 ["TDVIA:mahmud-i-gaznevi", "TDVIA:altuntas-el-hacib"], "", "Eniştesi Me'mûn'un intikamı gerekçesiyle sefer yapıldı; Hârizm'e Altuntaş vali oldu. Yer ve gün kaynakta yok.",
 "The campaign was justified as revenge for his brother-in-law Ma'mun; Altuntash became governor. Place and day not given."),
(G, "Kannevc seferi", "Kannauj campaign (1018)", "1018-12", "Mahmud'un Hint seferleri", "Kannevc", 27.05, 79.92, "approx", "Hindistan",
 "Gazneliler", "Pratihâra racası", "Mahmud", "", "dis", "W", "borderline",
 ["TDVIA:mahmud-i-gaznevi", "TDVIA:gazneliler"], "", "Gazne'den 27 Eylül 1018'de çıkıldı; Mâverâünnehir'den 20.000 gazi katıldı (Gazneliler maddesi; sayı alınmadı).",
 "Left Ghazna on 27 September 1018; 20,000 volunteers from Transoxiana joined (Ghaznavids article; figure not used)."),
(G, "Belh (1019)", "Battle of Balkh (1019)", "1019", "Gazneli–Karahanlı", "Belh civarı", 36.76, 66.90, "approx", "Afganistan",
 "Gazneliler", "Karahanlılar", "Mahmud", "Yûsuf Kadır Han, Arslan İlig Han Mansûr", "turk_arasi", "W", "kesin",
 ["TDVIA:mahmud-i-gaznevi", "TDVIA:karahanlilar"], "", "Ardından Yûsuf Kadır Han Mahmud ile anlaştı.", "Yusuf Qadir Khan then came to terms with Mahmud."),
(G, "Ganda'ya karşı (Bari)", "Campaign against Ganda (1019)", "1019", "Mahmud'un Hint seferleri", "Bari–Kâlincer yöresi", 25.00, 80.50, "region", "Hindistan",
 "Gazneliler", "Çandela racası", "Mahmud", "Ganda", "dis", "W", "borderline",
 ["TDVIA:mahmud-i-gaznevi"], "", "Bari alındı; Ganda bir öncü savaşından sonra kaçtı.", "Bari was taken; Ganda fled after a vanguard clash."),
(G, "Lokhot (1021)", "Second siege of Lohkot (1021)", "1021", "Mahmud'un Hint seferleri", "Lokhot (Loharin)", 33.90, 74.30, "approx", "Hindistan",
 "Keşmir", "Gazneliler", "Mahmud", "", "dis", "L", "kesin",
 ["TDVIA:mahmud-i-gaznevi", "AKD:palabiyik-2007"], "", "On dördüncü seferde Lokhot Kalesi yeniden kuşatıldı; kış yüzünden kuşatma kaldırıldı ve Keşmir alınamadı. (Kontrol turunda eklendi.)",
 "On the fourteenth expedition Lohkot was besieged again; the siege was lifted because of winter and Kashmir was not taken."),
(G, "Gevâliyâr ve Kālincâr (1022)", "Campaign against Gwalior and Kalinjar (1022)", "1022", "Mahmud'un Hint seferleri", "Gevâliyâr (Gwalior) ve Kālincâr", 26.22, 78.17, "region", "Hindistan",
 "Gazneliler", "Ganda (Kālincâr) ve Arcan (Gevâliyâr)", "Mahmud", "Ganda, Arcan", "dis", "W", "kesin",
 ["TDVIA:mahmud-i-gaznevi", "AKD:palabiyik-2007"], "", "On beşinci seferde önce Gevâliyâr kuşatıldı, racası Arcan barış imzalayıp tâbi oldu; ardından Kālincâr'a yürünerek Ganda'nın barış teklifi kabul edildi ve itaat altına alındı. (Kontrol turunda eklendi.)",
 "On the fifteenth expedition Gwalior was besieged first and its raja Arjan submitted; Mahmud then marched on Kalinjar and accepted Ganda's submission."),
(G, "Somnat", "Siege of Somnath (1026)", "1026-01-08", "Mahmud'un Hint seferleri", "Somnat, Kathiavar", 20.89, 70.40, "known", "Hindistan",
 "Gazneliler", "Somnat savunucuları (Solanki racalığı)", "Mahmud", "", "dis", "W", "kesin",
 ["TDVIA:mahmud-i-gaznevi", "TDVIA:gazneliler"], "", "Ordu Ekim 1025'te Gazne'den çıktı. Zafer Mahmud'a İslâm dünyasında büyük itibar kazandırdı. Kaynaktaki ordu sayısı (30.000 atlı) alınmadı.",
 "The army left Ghazna in October 1025. The victory brought Mahmud great prestige in the Islamic world. The source figure of 30,000 horsemen is not used."),
(G, "İndus üzerinde Câtlar", "River battle against the Jats (1027)", "1027", "Mahmud'un Hint seferleri", "İndus nehri", 29.00, 70.50, "region", "Pakistan",
 "Gazneliler", "Câtlar", "Mahmud", "", "dis", "W", "kesin",
 ["TDVIA:mahmud-i-gaznevi"], "", "Mültan'da 1400 gemilik bir nehir filosu yaptırıldı (sayı kaynaktandır).", "A river fleet of 1,400 boats was built at Multan (source figure)."),
(G, "Rey'in alınması", "Capture of Rayy (1029)", "1029", "Gazneli–Büveyhî", "Rey", 35.59, 51.44, "known", "İran",
 "Gazneliler", "Büveyhîler", "Mahmud", "Mecdüddevle", "dis", "W", "borderline",
 ["TDVIA:gazneliler"], "", "Irâk-ı Acem Gazneli sınırlarına katıldı. Çatışmanın ayrıntısı kaynakta yok.", "Persian Iraq was added to the Ghaznavid realm. No detail of fighting."),
(G, "Debûsiye", "Battle of Dabusiyya (1032)", "1032", "Gazneli–Karahanlı", "Debûsiye", 39.98, 66.17, "approx", "Özbekistan",
 "Gazneliler", "Karahanlılar", "Altuntaş", "Ali Tegin", "turk_arasi", "W", "ihtilafli",
 ["TDVIA:mesud-b-mahmud-i-gaznevi", "TDVIA:karahanlilar"], "Karahanlılar maddesi Ali Tegin'in kuvvetlerinin bozulduğunu yazar; Mesud maddesine göre ağır yaralanan Altuntaş ancak bir antlaşmayla çekilebildi. Altuntaş yarasından öldü.",
 "", ""),
(G, "Sarsûtî Kalesi", "Siege of Sarsuti (1033)", "1033", "Mesud'un Hint seferleri", "Sarsûtî (Sirsa)", 29.53, 75.03, "approx", "Hindistan",
 "Gazneliler", "Sarsûtî", "Mesud", "", "dis", "W", "borderline",
 ["TDVIA:gazneliler"], "", "Ayrıntı yok; kale ele geçirildi.", "No detail; the fortress was taken."),
(G, "Mevdûd–Muhammed", "Mawdud against Muhammad (1041)", "1041-04-08", "Gazneli taht mücadelesi", "Nengrahâr yöresi", 34.40, 70.40, "region", "Afganistan",
 "Mevdûd", "Muhammed b. Mahmud", "Mevdûd", "Muhammed", "ic", "C", "kesin",
 ["TDVIA:mevdud-b-mesud-i-gaznevi"], "", "Mevdûd, babası Mesud'un öldürülmesinin intikamını aldı.", "Mawdud avenged the killing of his father Mas'ud."),
(G, "Hânsî, Thânesâr ve Nagarkot'un kaybı (c. 1043)", "Loss of Hansi, Thanesar and Nagarkot (c. 1043)", "c. 1043", "Gazneli–Hint racaları", "Hânsî, Thânesâr ve Nagarkot", 29.97, 76.83, "region", "Hindistan",
 "Birleşik Hint ordusu (üç raca)", "Gazneliler", "", "", "dis", "L", "kesin",
 ["TDVIA:mevdud-b-mesud-i-gaznevi"], "", "Birleşen üç raca Gazneliler'in elindeki Hânsî, Thânesâr, Nagarkot ve diğer bazı yerleri geri aldı; ardından Lahor yedi ay kuşatıldı. (Kontrol turunda eklendi.)",
 "Three allied rajas retook Hansi, Thanesar, Nagarkot and other places from the Ghaznavids, then besieged Lahore for seven months."),
(G, "Lahor müdafaası", "Defence of Lahore (c. 1043)", "c. 1043", "Gazneli–Hint racaları", "Lahor", 31.55, 74.34, "known", "Pakistan",
 "Gazneliler", "Birleşik Hint ordusu", "", "", "dis", "W", "borderline",
 ["TDVIA:mevdud-b-mesud-i-gaznevi"], "", "Şehir yedi ay kuşatıldı ama düşmedi. Kural gereği savunan kazandı.", "The city was besieged for seven months but did not fall; by rule the defender wins."),
(G, "Ecüdhen", "Siege of Ajodhan (1079)", "1079-08-13", "İbrâhim'in Hint seferleri", "Ecüdhen (Pakpatan)", 30.34, 73.39, "known", "Pakistan",
 "Gazneliler", "Ecüdhen", "İbrâhim b. Mesud", "", "dis", "W", "kesin",
 ["TDVIA:ibrahim-b-mesud-i-gaznevi"], "", "Ardından üç ay süren bir kuşatmayla bir kale daha alındı (Kasım 1079 – 1080).", "Another fortress was then taken after a three-month siege (November 1079 – 1080)."),
(G, "Gazne (Seyfeddin Sûrî)", "Recapture of Ghazna (1149)", "1149", "Gazneli–Gurlu", "Gazne", 33.55, 68.42, "known", "Afganistan",
 "Gazneliler", "Gurlular", "Behram Şah", "Seyfeddin Sûrî", "dis", "W", "kesin",
 ["TDVIA:behram-sah"], "", "Seyfeddin Sûrî idam edildi ve başı Sencer'e gönderildi.", "Sayf al-Din Suri was executed and his head sent to Sanjar."),
(G, "Gazne (Cihansûz)", "Sack of Ghazna (1150)", "1150", "Gazneli–Gurlu", "Gazne", 33.55, 68.42, "known", "Afganistan",
 "Gurlular", "Gazneliler", "Behram Şah", "Alâeddin Hüseyin Cihansûz", "dis", "L", "kesin",
 ["TDVIA:behram-sah", "TDVIA:gazneliler"], "Tarih: Gazneliler maddesi 545 (1150-51).", "Gurlular Gazne'yi yaktı; Behram Şah Hindistan'a çekildi ve 1152'de döndü.", "The Ghurids burned Ghazna; Bahram Shah withdrew to India and returned in 1152."),
(K, "Karahıtaylara karşı zafer", "Victory over the Qara Khitai (c. 1128)", "c. 1128", "Karahanlı–Karahıtay", "Kâşgar yöresi", 39.47, 75.99, "region", "Çin",
 "Karahanlılar", "Karahıtaylar", "Ahmed", "", "dis", "W", "borderline",
 ["TDVIA:karahanlilar"], "", "Karahıtay ilerleyişi bir süre durduruldu. Tarih 522 (1128) veya sonrası.", "The Qara Khitai advance was halted for a time. Date 522 (1128) or later."),
(K, "Hucend", "Battle of Khujand (1137)", "1137-06", "Karahanlı–Karahıtay", "Hucend yakını", 40.28, 69.62, "approx", "Tacikistan",
 "Karahıtaylar", "Karahanlılar", "Mahmûd Han", "", "dis", "L", "kesin",
 ["TDVIA:karahanlilar"], "", "Mahmûd Han Semerkant'a kaçtı; dört yıl sonra Katvân geldi (pilot #80).", "Mahmud Khan fled to Samarkand; Qatwan followed four years later (pilot #80)."),
(K, "Karluklara yenilgi", "Defeat by the Qarluqs (1156)", "1156", "Karahanlı–Karluk", "Mâverâünnehir", 39.80, 66.50, "region", "Özbekistan",
 "Karluklar", "Karahanlılar", "İbrâhim", "", "dis", "L", "borderline",
 ["TDVIA:karahanlilar"], "", "İbrâhim öldürüldü. Karluklar Türk boyudur ama kapsam listesinde değildir.", "Ibrahim was killed. The Qarluqs were a Turkic people outside the scope list."),
]

EXTRA_SRC = {n: ["AKD:palabiyik-2007"] for n in ("Peşâver (Caypal)", "Vayhand ovası (Anandpâl)", "Nandana (Triloçanpâl)", "Lokhot kuşatması",
                                              "Kannevc seferi", "Ganda'ya karşı (Bari)", "Somnat", "İndus üzerinde Câtlar")}
# Üçüncü kaynak turu (2026-10-31): toplu TDVİA taraması
EXTRA_SRC.update({
    "Tûs (Ebû Ali Sîmcûrî)": ["TDVIA:simcuriler"],  # Ebû Ali Tûs'ta yapılan savaşta yenilince (22 Temmuz 995) Hârizm'e kaçtı
})
FIX = {"Peşâver (Caypal)": {"dispute": "Tarih: TDVİA zaferi 392'ye (1002) koyar; Palabıyık (2007) bu ikinci seferi Vayhand seferi olarak 391-2/1001-2'ye tarihler ve Caypal'ın esir alındığını yazar; yaygın tarih 27 Kasım 1001'dir."},
       "Ganda'ya karşı (Bari)": {"status": "kesin", "note": "Bari alındı. Palabıyık'a (2007) göre on üçüncü seferde (410/1019) askerler Ramganga nehrini tulumlarla geçti ve Ganda ile müttefiklerine karşı büyük bir zafer kazanıldı.", "note_en": "Bari was taken. According to Palabıyık (2007), on the thirteenth campaign (410/1019) the troops crossed the Ramganga on inflated skins and won a great victory over Ganda and his allies."}}
# İkinci kaynak turu (2026-10-29)
SECOND = {"Merv (Sâmânîler)": ["TDVIA:samaniler"], "Peşâver (Caypal)": ["TDVIA:hindusahiler"], "Mültan (1006)": ["TDVIA:multan"],
          "Mültan (1010)": ["TDVIA:multan"], "Vayhand ovası (Anandpâl)": ["TDVIA:hindusahiler"], "Nandana (Triloçanpâl)": ["TDVIA:hindusahiler"],
          "Rey'in alınması": ["TDVIA:mesud-b-mahmud-i-gaznevi"], "Sarsûtî Kalesi": ["TDVIA:mesud-b-mahmud-i-gaznevi"],
          "Mevdûd–Muhammed": ["TDVIA:gazneliler"], "Karahıtaylara karşı zafer": ["TDVIA:karahitaylar"], "Hucend": ["TDVIA:hucend", "TDVIA:karahitaylar"]}
for n, v in SECOND.items():
    EXTRA_SRC[n] = EXTRA_SRC.get(n, []) + v
FIX["Peşâver (Caypal)"] = {"date": "1001-11-27", "dispute": "",
    "note": "Hindûşâhîler maddesi tarihi 8 Muharrem 392 / 27 Kasım 1001 olarak verir; Caypal oğulları ve kumandanlarıyla esir alındı.",
    "note_en": "The Hindushahis article dates it 8 Muharram 392 / 27 November 1001; Jayapala was captured with his sons and commanders."}
FIX["Karahıtaylara karşı zafer"] = {"date": "1128", "note": "Karahıtaylar Balasagun, Hoten ve Kâşgar bölgesine ilk girdiklerinde Doğu Karahanlı hükümdarı Arslan Han Ahmed b. Hasan'a yenildiler.",
    "note_en": "When the Qara Khitai first entered the Balasagun, Khotan and Kashgar region they were defeated by the Eastern Qarakhanid ruler Arslan Khan Ahmad b. Hasan."}
OPP_STATE = {"Belh (1008)": K, "Belh (1019)": K, "Debûsiye": K}
LEFT = [
 {"name": "Buhara (999)", "reason": "İlig Han Nasr şehri mukavemetle karşılaşmadan aldı; savaş yok.", "source": "TDVIA:karahanlilar"},
 {"name": "Lahor (1186)", "reason": "Gurlular Hüsrev Melik'i hileyle esir aldı; savaş kaydı yok.", "source": "TDVIA:gazneliler"},
 {"name": "Karahanlı iç savaşları", "reason": "Doğu ve Batı Karahanlı kolları arasındaki çok sayıdaki çatışma bu turda alınmadı.", "source": "TDVIA:karahanlilar"},
 {"name": "Gazneli–Selçuklu savaşları", "reason": "Pilotta kayıtlı (Dandanakan vb.); opp_state ile Gazneli tablosunda da görünür.", "source": "TDVIA:gazneliler"},
]

recs = []
for i, r in enumerate(R, 1):
    (st, ntr, nen, date, war, place, lat, lon, loc, country, sa, sb, tc, oc, cat, res, status, src, disp, note, note_en) = r
    rec = {"id": i, "name_tr": ntr, "name_en": nen, "date": date, "hijri": "", "type": "land", "war": war, "place": place,
           "lat": lat, "lon": lon, "loc": loc, "country": country, "side_a": sa, "side_b": sb, "turkic_cmd": tc, "opp_cmd": oc,
           "category": cat, "result": res, "status": status, "sources": src,
           "verify": {"tdvia": True, "tdvia2": len([s for s in src if s.startswith("TDVIA:")]) >= 2, "wp": False, "rom": False, "academic": False},
           "state": st, "home_batch": HB}
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    if ntr in OPP_STATE: rec["opp_state"] = OPP_STATE[ntr]
    rec["sources"] += [x for x in EXTRA_SRC.get(ntr, []) if x not in rec["sources"]]
    rec.update(FIX.get(ntr, {}))
    if not rec.get("dispute"): rec.pop("dispute", None)
    rec["verify"]["academic"] = any(x.startswith("AKD:") for x in rec["sources"])
    rec["verify"]["tdvia2"] = len([x for x in rec["sources"] if x.startswith("TDVIA:")]) >= 2
    recs.append(rec)

pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 4 — Gazneliler ve Karahanlılar", "compiled": "2026-10-28", "status": "İlk tur.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "gazneli-karahanli.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
