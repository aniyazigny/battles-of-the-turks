"""data/gokturk-uygur.json dosyasını üretir (Parti 21: Göktürkler, Türgişler, Karluklar ve Uygurlar, 552–911).

TDVİA'da Göktürkler için müstakil madde yok; olaylar Asya, Uygurlar, Dokuz Oğuzlar, Karluklar, Yabgu, Tohâristan,
Talas Savaşı, Semerkant, Mâverâünnehir, Hazarlar ve Emevî valileri maddelerinden derlendi."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "gokturk-uygur"
GK = "Göktürk Kağanlığı"
BG = "Batı Göktürk Kağanlığı"
TR = "Türgiş Kağanlığı"
KR = "Karluk Yabguluğu"
UY = "Uygur Kağanlığı"
KU = "Kan-chou Uygurları"
WG1 = "Birinci Göktürk Kağanlığı (552–630)"
WBG = "Batı Göktürk Kağanlığı (552–659)"
WG2 = "İkinci Göktürk Kağanlığı (682–744)"
WTA = "Türgiş–Arap savaşları (720–738)"
WUY = "Uygur Kağanlığı (744–840)"
CN = "Çin (T'ang)"
EM = "Emevîler"

# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür, devlet)
R = [
("Juan-juan'ın yenilgisi (552)", "Fall of the Rouran Khaganate (552)", "552", WG1, "Moğolistan", 47.50, 102.50, "region", "Moğolistan",
 GK, "Juan-juan", "Bumın", "", "dis", "W", "kesin",
 ["TDVIA:asya"], "", "Juan-juan kuvvetlerini hezimete uğratan Bumın kendini hükümdar ilân etti; Göktürk Kağanlığı kuruldu.",
 "Bumin routed the Rouran forces and proclaimed himself ruler, founding the Göktürk Khaganate.", "land", GK),
("Akhun (Eftalit) Devleti'nin yıkılışı (557)", "Destruction of the Hephthalite state (557)", "557", WBG, "Soğd ve Tohâristan", 39.65, 66.96, "region", "Özbekistan",
 BG, "Akhunlar (Eftalitler)", "İstemi Yabgu", "", "turk_arasi", "W", "kesin",
 ["TDVIA:toharistan", "TDVIA:sogd", "TDVIA:semerkant", "TDVIA:maveraunnehir"],
 "Tohâristan maddesi Akhun Devleti'nin yıkılışını 557'ye, Soğd maddesi bölgenin Göktürk hâkimiyetine girişini 558'e, Semerkant maddesi Semerkant'ın alınışını 562'ye, Mâverâünnehir maddesi bağlanmayı 565'e koyar.",
 "Akhun Devleti Göktürk ve Sâsânî imparatorluklarının askerî harekâtıyla yıkıldı; Soğd ve Semerkant Batı Göktürk hâkimiyetine girdi. TDVİA Akhunlar'ı Halaç Türkleri olarak anar → `turk_arasi`.",
 "The Hephthalite state was destroyed by joint Göktürk and Sasanian operations; Sogdia and Samarkand came under West Göktürk rule.", "land", BG),
("Kerç (576)", "Capture of Bosporus (576)", "576", WBG, "Kerç", 45.36, 36.47, "known", "Ukrayna",
 BG, "Bizans", "", "", "dis", "W", "kesin",
 ["TDVIA:hazarlar"], "", "Kırım'daki Kerç Kalesi'nin alınmasıyla Göktürk sınırları Karadeniz'e ulaştı.",
 "With the capture of the fortress of Kerch in the Crimea, the Göktürk frontier reached the Black Sea.", "land", BG),
("Tiflis (627–629)", "Siege of Tiflis (627–629)", "629", WBG, "Tiflis", 41.69, 44.80, "known", "Gürcistan",
 BG, "Sâsânîler", "", "", "dis", "W", "kesin",
 ["TDVIA:hazarlar"], "",
 "Batı Göktürkleri'ne bağlı Hazarlar Bizans'ın müttefiki olarak Derbend'i aşıp Tiflis'i kuşattı; 626'da Herakleios'a 40.000 kişilik yardım gönderildi, şehir 629'da alındı.",
 "The Khazars, then subject to the West Göktürks, crossed Derbent as Byzantium's allies and besieged Tiflis; 40,000 men were sent to Heraclius in 626 and the city fell in 629.", "land", BG),
("Doğu Göktürk'ün yıkılışı (630)", "Fall of the Eastern Turkic Khaganate (630)", "630", WG1, "Ötüken ve Çin sınırı", 41.00, 111.00, "region", "Moğolistan / Çin",
 CN, GK, "", "", "dis", "L", "kesin",
 ["TDVIA:asya", "TDVIA:turfan"], "",
 "Zayıflayan Doğu Göktürk Hakanlığı Çin ile uzun mücadeleyi kaybetti; elli yıl sürecek esaret dönemi başladı.",
 "The weakened Eastern Göktürk Khaganate lost its long struggle with China; fifty years of subjection followed.", "land", GK),
("Fergana (649)", "Göktürk attack on Ferghana (649)", "649", WBG, "Fergana", 40.39, 71.78, "region", "Özbekistan",
 BG, "Fergana hânedanı", "", "", "dis", "W", "kesin",
 ["TDVIA:fergana"], "", "Fergana'yı yöneten hânedanın son hükümdarı Göktürkler'le yapılan savaşta öldürüldü.",
 "The last ruler of Ferghana's dynasty was killed fighting the Göktürks.", "land", BG),
("Batı Göktürk'ün yıkılışı (657)", "Tang conquest of the Western Turks (657)", "657", WBG, "Yedisu ve Tanrı dağları", 42.90, 75.00, "region", "Kırgızistan / Kazakistan",
 CN, BG, "Aşena Ho-lu", "", "dis", "L", "kesin",
 ["TDVIA:toharistan", "TDVIA:karluklar", "TDVIA:talas-savasi", "TDVIA:semerkant"],
 "Karluklar maddesi Çin taarruzunu 656'ya, Tohâristan maddesi yenilgileri 657–658'e, Fergana maddesi yıkılışı 658'e, Talas Savaşı ve Semerkant maddeleri 659'a koyar.",
 "Hakan Aşena Ho-lu Çin ordularına peş peşe yenildi; Karluklar da onunla birlikte mücadeleyi kaybetti.",
 "Khagan Ashina Helu was defeated by Chinese armies in succession; the Karluks, his allies, lost with him.", "land", BG),
("İkinci Göktürk Kağanlığı'nın kuruluşu (682)", "Revolt of Ilterish (682)", "682", WG2, "Ötüken", 47.50, 102.50, "region", "Moğolistan",
 GK, CN, "Kutluğ (İlteriş Kağan)", "", "dis", "W", "borderline",
 ["TDVIA:asya", "TDVIA:dokuz-oguzlar"], "",
 "Kutluğ Çin'e karşı ayaklanarak hakanlığı yeniden kurdu ve on yıl boyunca Çin'e, Kıtaylar'a ve Oğuzlar'a başarılı seferler yaptı; tek bir muharebe olmadığından borderline.",
 "Kutlugh rose against China, restored the khaganate and campaigned successfully for ten years; borderline as no single battle is named.", "land", GK),
("Türgiş seferi (711)", "Battle of Bolchu (711)", "711", WG2, "Bolçu (Cungarya)", 46.50, 87.50, "approx", "Çin (Doğu Türkistan)",
 GK, "Türgişler", "Kapgan Kağan", "", "turk_arasi", "W", "kesin",
 ["TDVIA:yabgu", "TDVIA:talas-savasi"], "",
 "Kapgan Kağan Türgişler'i yenip kendisine bağladı; Türgiş yabgusu, şadı ve kağanı öldürüldü.",
 "Kapghan Khagan defeated and subjugated the Türgesh; the Türgesh yabgu, shad and khagan were killed.", "land", GK),
("Togubalık (715)", "Battle of Toghu Balık (715)", "715", WG2, "Tula ırmağı yakını", 47.90, 106.90, "approx", "Moğolistan",
 GK, "Oğuzlar", "", "", "ic", "C", "kesin",
 ["TDVIA:dokuz-oguzlar"], "", "Oğuzlar'la bir yıl içinde dört kez savaşıldı; ilki Tula yakınındaki Togubalık'ta.",
 "The Göktürks fought the Oğuz four times within a year; the first battle was at Toghu Balık near the Tola.", "land", GK),
("Agu (716)", "Battle of Agu (716)", "716", WG2, "Agu", 47.50, 104.00, "region", "Moğolistan",
 GK, "Oğuzlar ve Tatarlar", "Tarduş Şad (Bilge Kağan)", "", "ic", "C", "kesin",
 ["TDVIA:dokuz-oguzlar"], "", "Agu'daki iki çarpışmada Oğuz ve Tatarlar bozguna uğradı.",
 "The Oğuz and Tatars were routed in two clashes at Agu.", "land", GK),
("Kapgan Kağan'ın ölümü (716)", "Death of Kapghan Khagan (716)", "716-07-22", WG2, "Tula ırmağı", 48.00, 106.00, "region", "Moğolistan",
 "Bayırkular", GK, "Kapgan Kağan", "", "ic", "C", "kesin",
 ["TDVIA:dokuz-oguzlar"], "", "Baykal çevresindeki Bayırkular'a sefere çıkan Kapgan Kağan öldürüldü; kağanlık mücadelesi başladı.",
 "Kapghan Khagan, campaigning against the Bayırku around Lake Baikal, was killed; a succession struggle followed.", "land", GK),
("Semerkant seferi (721)", "Türgesh campaign on Samarkand (720–721)", "721", WTA, "Semerkant", 39.65, 66.96, "known", "Özbekistan",
 TR, EM, "Su-lu Kağan", "", "dis", "W", "kesin",
 ["TDVIA:talas-savasi", "TDVIA:semerkant"], "",
 "Su-lu Kağan liderliğindeki Türgiş ordusu Soğd halkına yardım için Semerkant üzerine yürüdü; önce yenildiyse de ardından Araplar'ı mağlûp etti.",
 "Under Suluk Khagan the Türgesh marched on Samarkand to aid the Sogdians; beaten at first, they then defeated the Arabs.", "land", TR),
("Mâverâünnehir'in alınışı (728)", "Türgesh reconquest of Transoxiana (728)", "728", WTA, "Semerkant ve Buhara", 39.77, 64.42, "region", "Özbekistan",
 TR, EM, "Su-lu Kağan", "", "dis", "W", "kesin",
 ["TDVIA:semerkant", "TDVIA:maveraunnehir", "TDVIA:buhara"], "",
 "Soğd kuvvetleriyle birleşen Türgişler Semerkant ve Debûsiye dışında bütün bölgeyi ele geçirip Semerkant'ı kuşattı; bir ara Buhara'yı da işgal ettiler.",
 "Joined by Sogdian forces, the Türgesh took the whole region except Samarkand and Dabusiya and besieged Samarkand; they briefly held Bukhara too.", "land", TR),
("Buhara ve Beykend (729)", "Battles of Bukhara and Baykand (729)", "729", WTA, "Buhara ve Beykend", 39.77, 64.42, "approx", "Özbekistan",
 EM, TR, "", "Cüneyd el-Mürrî", "dis", "L", "kesin",
 ["TDVIA:cuneyd-el-murri"], "", "Takviye gelince hakan Buhara önlerinden çekildi; Cüneyd Beykend yakınında Türkler'i yenip hakanın yeğenini (Belâzürî'ye göre oğlunu) esir aldı.",
 "With reinforcements arriving the khagan withdrew from Bukhara; Junayd beat the Turks near Baykand and captured the khagan's nephew (his son, per al-Baladhuri).", "land", TR),
("Semerkant (731)", "Battle of the Defile (731)", "731-11", WTA, "Semerkant–Buhara yolu", 39.70, 66.00, "region", "Özbekistan",
 EM, TR, "", "Cüneyd el-Mürrî", "dis", "L", "kesin",
 ["TDVIA:cuneyd-el-murri", "TDVIA:nasr-b-seyyar"], "",
 "Cüneyd Semerkant'ı alırken İslâm ordusu Türkler ve Soğdlar karşısında hezimetten güçlükle kurtuldu; Kasım 731'de Buhara'ya varan Cüneyd hakanı çekilmeye mecbur etti.",
 "The Muslim army barely escaped disaster against the Turks and Sogdians while Junayd took Samarkand; reaching Bukhara in November 731, Junayd forced the khagan to withdraw.", "land", TR),
("Haristan (737)", "Battle of Kharistan (737)", "737", WTA, "Tohâristan", 36.70, 66.90, "region", "Afganistan",
 EM, TR, "Su-lu Kağan", "Esed b. Abdullah el-Kasrî", "dis", "L", "kesin",
 ["TDVIA:esed-b-abdullah-el-kasri", "TDVIA:toharistan"], "",
 "Önce Türk hakanı galip geldiyse de daha sonra yenildi ve ordusu dağıldı; Hâris b. Süreyc Türk tarafına geçmişti. Su-lu 738'de öldü, Türgişler bölgeden çekildi.",
 "The Turkish khagan at first prevailed but was then defeated and his army scattered; al-Harith b. Surayj had joined the Turks. Suluk died in 738 and the Türgesh withdrew.", "land", TR),
("Ozmış Kağan'ın yenilgisi (743)", "Fall of the Second Göktürk Khaganate (742–743)", "743", WG2, "Ötüken", 47.50, 102.50, "region", "Moğolistan",
 "Karluk, Basmıl ve Uygur oymakları", GK, "Ozmış Kağan", "", "turk_arasi", "L", "kesin",
 ["TDVIA:uygurlar", "TDVIA:karluklar", "TDVIA:asya"], "Uygurlar maddesi 742–743, Karluklar maddesi yıkılışı 745, Asya maddesi 744 der.",
 "Göktürk hâkimiyetindeki Karluk, Basmıl ve Uygur oymakları Ozmış Kağan'ı yenip öldürdü; Göktürk Devleti 744'te yıkıldı.",
 "The Karluk, Basmil and Uyghur tribes under Göktürk rule defeated and killed Ozmış Khagan; the Göktürk state fell in 744.", "land", GK),
("Basmıl'ın yenilgisi (745)", "Uyghur defeat of the Basmil (745)", "745", WUY, "Ötüken", 47.50, 102.50, "region", "Moğolistan",
 UY, "Basmıllar", "Kutluğ Bilge Köl Kağan", "", "turk_arasi", "W", "kesin",
 ["TDVIA:uygurlar", "TDVIA:asya"], "Uygurlar maddesi 745, Asya maddesi Uygur iktidarını 744'e koyar.",
 "Uygur yabgusu Basmıl kağanını yenip kendini kağan ilân etti; Büyük Uygur Kağanlığı kuruldu.",
 "The Uyghur yabgu defeated the Basmil khagan and proclaimed himself khagan, founding the Uyghur Khaganate.", "land", UY),
("Oğuz ve Tatar isyanı (749)", "Suppression of the Oğuz–Tatar revolt (749)", "749", WUY, "Ötüken çevresi", 47.50, 104.00, "region", "Moğolistan",
 UY, "Oğuzlar ve Dokuz Tatarlar", "İl İtmiş Bilge Kağan (Moyen-çor)", "", "ic", "C", "kesin",
 ["TDVIA:dokuz-oguzlar"], "", "Kağan 749'un ilk aylarından güze kadar isyanla uğraştı, başarılar elde edip Oğuzlar'ın büyük kısmını esir aldı.",
 "From early 749 until autumn the khagan fought the revolt, winning successes and capturing most of the Oğuz commoners.", "land", UY),
("Çik seferi (750)", "Campaign against the Chik (750)", "750", WUY, "Kem (Yenisey) ırmağı", 51.70, 94.40, "region", "Rusya (Tuva)",
 UY, "Çikler", "İl İtmiş Bilge Kağan (Moyen-çor)", "", "turk_arasi", "W", "kesin",
 ["TDVIA:dokuz-oguzlar"], "", "Kem ırmağı kıyısındaki Çikler'e karşı sefer.", "Campaign against the Chik on the Kem (upper Yenisei).", "land", UY),
("Talas (751)", "Battle of Talas", "751-07", "Talas Savaşı (751)", "Talas nehri (Atlah)", 42.52, 72.24, "known", "Kırgızistan / Kazakistan",
 "Karluklar ve Abbâsîler", CN, "", "Kao Sien-chih", "dis", "W", "kesin",
 ["TDVIA:talas-savasi", "TDVIA:maveraunnehir", "TDVIA:asya", "TDVIA:turfan"], "",
 "Beş gün süren savaşın son günü Karluklar Çin ordusuna arkadan saldırdı; iki ateş arasında kalan Çinliler ağır yenildi ve Batı Türkistan'dan çekildi.",
 "On the last of five days the Karluks attacked the Chinese army from the rear; caught between two fires, the Chinese were heavily defeated and withdrew from western Turkestan.", "land", KR),
("Çin'e yardım: Ch'ang-an ve Lo-yang (757)", "Uyghur intervention in the An Lushan rebellion (757)", "757", WUY, "Ch'ang-an ve Lo-yang", 34.27, 108.95, "region", "Çin",
 UY, "An Lu-shan isyancıları", "", "", "dis", "W", "kesin",
 ["TDVIA:toharistan", "TDVIA:uygurlar"], "",
 "757'nin ilk aylarında Uygur yardımcı kuvvetleri T'ang hânedanına yardıma geldi; Uygurlar Çin'de otorite kurmak için bu ülkeye yardım edip yıllık vergi aldılar.",
 "In early 757 Uyghur auxiliaries came to the aid of the Tang; the Uyghurs helped China and received annual tribute.", "land", UY),
("Kırgızlar'ın bağlanması (758)", "Uyghur subjugation of the Kyrgyz (758)", "758", WUY, "Yenisey", 53.70, 91.40, "region", "Rusya",
 UY, "Kırgızlar", "Moyen-çor Kağan", "", "turk_arasi", "W", "kesin",
 ["TDVIA:kirgizlar"], "", "", "", "land", UY),
("Uygur Kağanlığı'nın yıkılışı (840)", "Kyrgyz destruction of the Uyghur Khaganate (840)", "840", WUY, "Ötüken (Ordu-balık)", 47.43, 102.66, "known", "Moğolistan",
 "Kırgızlar", UY, "", "", "turk_arasi", "L", "kesin",
 ["TDVIA:uygurlar", "TDVIA:kirgizlar", "TDVIA:asya", "TDVIA:turfan"], "",
 "Kırgızlar şiddetli bir hücumla Uygur Devleti'ni yıkıp Ötüken'de hâkimiyet kurdu; Uygurlar Kansu, Turfan ve Beşbalık'a dağıldı.",
 "The Kyrgyz destroyed the Uyghur state in a violent assault and took the Ötüken; the Uyghurs scattered to Gansu, Turfan and Beshbalik.", "land", UY),
("Tun-huang (911)", "Ganzhou Uyghur capture of Dunhuang (911)", "911", "Kan-chou Uygurları (847–1028)", "Tun-huang", 40.14, 94.66, "known", "Çin",
 KU, "Tun-huang özerk devleti", "Tegin", "", "dis", "W", "kesin",
 ["TDVIA:uygurlar"], "", "Bölge ticaretini ele geçirmeye kalkışan krallığın merkezi Tun-huang Tegin kumandasındaki Uygur ordusunca alındı.",
 "The capital of the kingdom that tried to seize the region's trade, Dunhuang, was taken by the Uyghur army under Tegin.", "land", KU),
]

LEFT = [
    {"name": "Sâsânî–Göktürk savaşları (569–571, 588–589)", "reason": "Sâsânîler maddesi IV. Hürmüz döneminin savaşlarla geçtiğini toplu anar; muharebe adı yok.", "source": "TDVIA:sasaniler"},
    {"name": "Kapgan Kağan'ın Semerkant müdahalesi (701)", "reason": "Semerkant ve Mâverâünnehir maddeleri başarılı askerî müdahaleyi anar; karşı taraf ve muharebe belirsiz.", "source": "TDVIA:semerkant"},
    {"name": "Kırgız seferi (710, Kögmen)", "reason": "TDVİA'da yok; Orhon yazıtlarından akademik kaynakla eklenecek (Erhan Aydın, Sibirya Araştırmaları 2007).", "source": "TDVIA:orhon-yazitlari"},
    {"name": "Karluk isyanları (711, 714)", "reason": "Karluklar maddesi isyanları anar; muharebe ayrıntısı yok.", "source": "TDVIA:karluklar"},
    {"name": "Beşbalık (791)", "reason": "Beşbalık maddesi şehrin Karluklar'ca alındığını yazar; karşı taraf belirtilmemiş.", "source": "TDVIA:besbalik"},
    {"name": "Uygur–Kırgız savaşları (821 sonrası)", "reason": "Uygurlar maddesi toplu anar.", "source": "TDVIA:uygurlar"},
]

recs = []
for i, r in enumerate(R, 1):
    (ntr, nen, date, war, place, lat, lon, loc, country, sa, sb, tc, oc, cat, res, status, src, disp, note, note_en, typ, state) = r
    rec = {"id": i, "name_tr": ntr, "name_en": nen, "date": date, "hijri": "", "type": typ, "war": war, "place": place,
           "lat": lat, "lon": lon, "loc": loc, "country": country, "side_a": sa, "side_b": sb, "turkic_cmd": tc, "opp_cmd": oc,
           "category": cat, "result": res, "status": status, "sources": src,
           "verify": {"tdvia": True, "tdvia2": len([s for s in src if s.startswith("TDVIA:")]) >= 2, "wp": False, "rom": False, "academic": False},
           "state": state, "home_batch": HB}
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    recs.append(rec)

dates = [r["date"] for r in recs]
assert dates == sorted(dates), [d for a, d in zip(dates, dates[1:]) if d < a]
pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 21 — Göktürkler, Türgişler, Karluklar ve Uygurlar (552–911)", "compiled": "2026-10-30", "status": "İlk tur.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "gokturk-uygur.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
