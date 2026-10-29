"""data/osmanli-kurulus.json dosyasını üretir (Parti 5: Osmanlı kuruluş dönemi, 1284–1402)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "osmanli-kurulus"
O = "Osmanlı Devleti"
KAR, KB, ERT = "Karamanoğulları", "Kadı Burhâneddin Devleti", "Eretnalılar"
# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en)
R = [
("Ermeni Beli", "Battle of Mount Armenia", "1284", "Osman Gazi–Bizans", "Ermeni Beli, Bilecik–İnegöl arası", 40.00, 29.70, "approx", "Türkiye",
 O, "Bizans tekfurları", "Osman Gazi", "", "dis", "D", "borderline",
 ["ROM"], "", "Yalnızca Roma veri setinde (Bizans kaynakları) var; sonuç belirsiz. Osmanlı rivayetinde Saru Batu Savcı Bey'in şehit düştüğü çarpışmayla ilişkilendirilir; TDVİA'da ayrı bir kayıt bulunamadı.",
 "Recorded only in the Roman dataset (Byzantine sources); outcome unclear. Ottoman tradition links it to the clash in which Saru Batu Savcı Bey fell; no separate TDVİA account found."),
("Kulaca Hisar", "Siege of Kulaca Hisar", "1285", "Osman Gazi–Bizans", "Kulaca Hisar, İnegöl yakını", 40.05, 29.48, "approx", "Türkiye",
 O, "Bizans tekfurları", "Osman Gazi", "", "dis", "W", "borderline",
 ["ROM"], "", "Yalnızca Roma veri setinde var; TDVİA Osman maddesinde ayrıca anılmıyor.", "Recorded only in the Roman dataset; not separately mentioned in the TDVİA Osman article."),
("Domaniç (İkizce)", "Battle of Domaniç", "1286", "Osman Gazi–Bizans", "İkizce yakını, Domaniç beli", 39.82, 29.60, "approx", "Türkiye",
 O, "Bizans tekfurları (Karacahisar, Bilecik)", "Osman Gazi", "", "dis", "W", "ihtilafli",
 ["TDVIA:osman-i", "ROM"], "Tarih: TDVİA 685/1286, Roma veri seti 1287.", "TDVİA bunu Osman'ın gerçek anlamda ilk savaşı sayar.", "TDVİA considers this Osman's first real battle."),
("Karacahisar", "Siege of Karacahisar", "1288", "Osman Gazi–Bizans", "Karacahisar, Eskişehir yakını", 39.73, 30.47, "approx", "Türkiye",
 O, "Karacahisar tekfuru", "Osman Gazi", "", "dis", "W", "borderline",
 ["TDVIA:osman-i", "ROM"], "", "Fetih tarihi kaynaklarda tartışmalıdır; Roma veri seti 1288 verir.", "The date of the conquest is disputed; the Roman dataset gives 1288."),
("Koyunhisar (Bafeus)", "Battle of Bapheus", "1302-07-27", "Osman Gazi–Bizans", "Koyunhisar, Yalakova (İzmit yakını)", 40.73, 29.85, "approx", "Türkiye",
 O, "Bizans", "Osman Gazi", "Muzalon", "dis", "W", "kesin",
 ["TDVIA:osman-i", "TDVIA:orhan", "ROM"], "Tarih: Pachymeres 27 Temmuz 1302; Osmanlı kaynakları 701 (1301-02).",
 "İznik'i kurtarmaya gelen Bizans ordusu bozuldu. Savaş Osman'a hanedan kurucusu bir bey ünü kazandırdı.", "The Byzantine army sent to relieve Nicaea was routed. The battle made Osman's name as a dynastic founder."),
("Dimbos", "Battle of Dimbos", "1303", "Osman Gazi–Bizans", "Dimbos Boğazı (Erdoğan köyü)", 40.23, 29.55, "approx", "Türkiye",
 O, "Adranos, Bidnos, Kestel ve Kite tekfurları", "Osman Gazi, Orhan", "Kestel tekfuru (öldü)", "dis", "W", "kesin",
 ["TDVIA:osman-i", "TDVIA:orhan", "ROM"], "", "Kite tekfuru Ulubat Köprüsü'ne kadar kovalandı; Bursa ovası Türkmen yerleşmesine açıldı.", "The lord of Kite was chased to the Ulubat bridge; the Bursa plain opened to Turkmen settlement."),
("Bursa'nın teslimi", "Surrender of Bursa", "1326-04-06", "Orhan Gazi–Bizans", "Bursa", 40.19, 29.06, "known", "Türkiye",
 O, "Bizans", "Orhan Gazi", "", "dis", "W", "borderline",
 ["TDVIA:orhan", "TDVIA:bursa"], "", "Yirmi yılı aşan abluka sonunda ahidnâme ile teslim alındı; çatışma olmadığı için borderline.", "Surrendered on terms after a blockade of more than twenty years; borderline because there was no battle."),
("Pelekanon (Maltepe)", "Battle of Pelekanon", "1329-06-02", "Orhan Gazi–Bizans", "Pelekanon, Maltepe yakını", 40.80, 29.40, "approx", "Türkiye",
 O, "Bizans", "Orhan Gazi, Pazarlu", "III. Andronikos (yaralandı)", "dis", "W", "kesin",
 ["TDVIA:orhan", "TDVIA:osman-i"], "", "İki gün sürdü (1–2 Haziran). İmparator yaralandı, ordusu paniğe kapılıp kaçtı; Kocaeli ve ardından İznik Osmanlılara geçti.",
 "It lasted two days (1–2 June). The emperor was wounded and his army fled in panic; Kocaeli and then Nicaea passed to the Ottomans."),
("İznik'in teslimi", "Fall of Nicaea", "1331-03-02", "Orhan Gazi–Bizans", "İznik", 40.43, 29.72, "known", "Türkiye",
 O, "Bizans", "Orhan Gazi", "", "dis", "W", "borderline",
 ["TDVIA:orhan", "TDVIA:iznik"], "Tarih: 2 Mart 1331; İbn Kemal 734/1333 verir.", "Uzun abluka sonunda teslim; çatışma olmadığı için borderline.", "Surrendered after a long blockade; borderline because there was no battle."),
("Uzuncabel", "Battle of Uzuncabel", "c. 1330", "Orhan Gazi–Bizans", "Uzuncabel, Akyazı–Bolu arası", 40.70, 30.70, "region", "Türkiye",
 O, "Bizans", "Konuralp", "", "dis", "W", "borderline",
 ["TDVIA:osman-i", "TDVIA:orhan"], "", "İki gün iki gece süren savaştan sonra bölge ele geçirildi. Tarih yaklaşık.", "After two days and nights of fighting the area was taken. Date approximate."),
("İzmit'in teslimi", "Fall of Nicomedia", "1337", "Orhan Gazi–Bizans", "İzmit", 40.77, 29.92, "known", "Türkiye",
 O, "Bizans", "Orhan Gazi", "", "dis", "W", "borderline",
 ["TDVIA:orhan"], "", "Kuşatma sonunda ahidnâme ile teslim alındı.", "Surrendered on terms after a siege."),
("Dimetoka (Empythion)", "Battle of Demotika", "1352", "Bizans iç savaşı (Kantakuzenos'a destek)", "Meriç boyu, Dimetoka yakını", 41.35, 26.50, "approx", "Yunanistan",
 O + ", Kantakuzenos", "Sırbistan, Bulgaristan, V. Ioannes Palaiologos", "Şehzade Süleyman Paşa", "", "dis", "W", "kesin",
 ["TDVIA:orhan"], "", "Süleyman önce Bulgarları, ardından Sırp ve Bizans kuvvetlerini tam bir bozguna uğrattı. Kaynaktaki ordu sayısı alınmadı.",
 "Süleyman first defeated the Bulgarians, then routed the Serbian and Byzantine forces. The source's army size is not used."),
("Sazlıdere (Edirne)", "Battle of Sazlıdere", "1361-05", "I. Murad'ın Trakya fethi", "Sazlıdere vadisi, Edirne önü", 41.70, 26.50, "approx", "Türkiye",
 O, "Edirne tekfuru (Bizans)", "Şehzade Murad, Lala Şâhin", "Edirne tekfuru", "dis", "W", "kesin",
 ["TDVIA:murad-i", "TDVIA:edirne"], "Edirne'nin fetih tarihi tartışmalıdır: Murad maddesi 5 Mayıs 1361 verir; Edirne maddesi 1361, 1362, 1367 ve 1369 önerilerini sayar ve 1361 görüşünün ağırlık kazandığını belirtir.",
 "Tekfur yenilip gece gemiyle Enez'e kaçtı; Edirne halkı şehri teslim etti.", "The lord was defeated and fled by boat to Enez by night; the townspeople surrendered the city."),
("Eretna kuvvetlerine karşı", "Against the Eretnids (1362)", "1362", "I. Murad–Eretnalılar", "Eskişehir yöresi", 39.78, 30.52, "region", "Türkiye",
 O, "Eretnalı Moğol birlikleri", "I. Murad", "Barımbay ve Samagar kuvvetleri", "turk_arasi", "W", "borderline",
 ["TDVIA:murad-i"], "", "Karaman ordusu da püskürtüldü; ardından Ankara ahîleri şehri teslim etti. Eretnalılar Uygur kökenli bir Türk beyliğidir.",
 "The Karamanid army was also repulsed; the akhis of Ankara then surrendered the city. The Eretnids were a Turkic beylik of Uyghur origin."),
("Sozopol", "Sieges of Sozopolis", "c. 1367", "I. Murad'ın Balkan seferleri", "Sozopol", 42.42, 27.70, "known", "Bulgaristan",
 O, "Bizans", "I. Murad", "", "dis", "W", "borderline",
 ["TDVIA:murad-i"], "", "İlk kuşatma on beş gün sürüp başarısız oldu; şehir sonra eman ile alındı.", "A first fifteen-day siege failed; the town was later taken on terms."),
("Çirmen (Sırpsındığı)", "Battle of the Maritsa", "1371-09-26", "I. Murad–Sırp despotları", "Çirmen, Meriç kıyısı", 41.88, 26.38, "approx", "Yunanistan",
 O, "Sırp despotları (Vulkaşin, Uglyeşa)", "Hacı İlbeği", "Vulkaşin (öldü), Uglyeşa (öldü)", "dis", "W", "kesin",
 ["TDVIA:murad-i", "TDVIA:cirmen"], "Tarih: Osmanlı kaynakları 766 (1364-65) verir; hıristiyan kaynakları 26 Eylül 1371. TDVİA 1371'i doğru kabul eder.",
 "Öncü kuvvetlerin gece baskını; Sırplar birbirine girdi, çoğu Meriç'te boğuldu. Makedonya'daki Sırp prensleri Osmanlıya tâbi oldu.",
 "A night attack by the vanguard; the Serbs fell into confusion and many drowned in the Maritsa. The Serbian princes of Macedonia became Ottoman vassals."),
("Biga kuşatması", "Siege of Pegae", "1371", "I. Murad–Bizans", "Biga (Pegae)", 40.38, 27.12, "approx", "Türkiye",
 O, "Bizans", "I. Murad", "", "dis", "W", "kesin",
 ["TDVIA:murad-i", "TDVIA:orhan"], "Tarih: Osmanlı rivayeti 766/1364-65 verir; TDVİA 1371 yazını kesin sayar.", "Karadan ve denizden kuşatılarak alındı.", "Taken after a siege by land and sea."),
("Pikridion (Savcı Bey isyanı)", "Revolt of Savcı Bey", "1373-05-25", "Savcı Bey isyanı", "Pikridion, Boğaziçi", 41.05, 29.00, "approx", "Türkiye",
 "I. Murad, V. Ioannes", "Savcı Bey, Andronikos", "I. Murad", "Savcı Bey", "ic", "C", "kesin",
 ["TDVIA:murad-i"], "", "Savcı Bey Dimetoka'ya kaçtı ve teslim olduktan sonra cezalandırıldı.", "Savcı Bey fled to Didymoteicho and was punished after surrendering."),
("Savra (Muzakiye ovası)", "Battle of Savra", "1385", "I. Murad–Arnavutluk", "Muzakiye ovası", 40.80, 19.70, "approx", "Arnavutluk",
 O, "Balşa II", "Hayreddin Paşa", "Balşa II (öldü)", "dis", "W", "kesin",
 ["TDVIA:murad-i"], "", "Arnavutlukta Osmanlı hâkimiyetinin başlangıcı sayılır.", "Regarded as the beginning of Ottoman rule in Albania."),
("Manastır", "Capture of Bitola", "1385", "I. Murad–Makedonya", "Manastır (Bitola)", 41.03, 21.33, "known", "Kuzey Makedonya",
 O, "Makedonya'daki Sırp beyleri", "Timurtaş", "", "dis", "W", "kesin",
 ["TDVIA:murad-i"], "", "Zorlu bir savaştan sonra alındı; ardından İştip ele geçirildi.", "Taken after a hard fight; Štip followed."),
("Niş", "Capture of Niš", "1386", "I. Murad–Sırbistan", "Niş", 43.32, 21.90, "known", "Sırbistan",
 O, "Sırbistan (Lazar)", "I. Murad", "", "dis", "W", "kesin",
 ["TDVIA:murad-i"], "", "Çetin savaşlardan sonra yağma ilânıyla alındı.", "Taken after hard fighting following a declaration of plunder."),
("Frenkyazısı", "Battle of Frenkyazısı", "1386/1387", "I. Murad–Karamanoğulları", "Frenkyazısı, Konya yakını", 37.95, 32.55, "approx", "Türkiye",
 O, KAR, "I. Murad, Şehzade Bayezid", "Karamanoğlu Alâeddin Bey", "turk_arasi", "W", "kesin",
 ["TDVIA:murad-i", "TDVIA:bayezid-i"], "Tarih: Bayezid maddesi 1386; Murad maddesinde sefer 1386-87.",
 "Bayezid burada \"Yıldırım\" lakabını aldı. Karamanoğlu Konya'ya çekildi ve kuşatıldı.", "Bayezid earned the name 'Thunderbolt' here. The Karamanid withdrew to Konya and was besieged."),
("Selânik'in teslimi", "Fall of Thessalonica (1387)", "1387-04-09", "I. Murad–Bizans", "Selânik", 40.64, 22.94, "known", "Yunanistan",
 O, "Bizans (Manuel)", "Çandarlı Hayreddin Paşa", "Manuel Palaiologos", "dis", "W", "borderline",
 ["TDVIA:murad-i"], "", "1383'ten beri süren kuşatma sonunda teslim oldu.", "Surrendered after a siege that had lasted since 1383."),
("Bileća", "Battle of Bileća", "1388-08-27", "I. Murad–Bosna", "Bileća, Trebinye kuzeyi", 42.88, 18.43, "approx", "Bosna-Hersek",
 "Bosna Krallığı", O, "Kavala Şâhin", "Vlatko Vuković", "dis", "L", "kesin",
 ["TDVIA:murad-i"], "Tarih: 26 veya 27 Ağustos 1388.", "Baskına uğrayan Osmanlı akıncı kuvveti bozuldu; yenilgi Balkanlarda tâbi devletlerin ayaklanmasına yol açtı.",
 "The Ottoman raiding force was surprised and routed; the defeat set off revolts among the Balkan vassals."),
("Pločnik", "Battle of Pločnik", "1388", "I. Murad–Sırbistan", "Pločnik, Toplica vadisi", 43.17, 21.38, "approx", "Sırbistan",
 "Sırbistan (Lazar)", O, "", "Lazar", "dis", "L", "ihtilafli",
 ["TDVIA:kosova-savaslari"], "Tarih: Kosova Savaşları maddesi 790 (1388) verir; batı literatüründe 1386 veya 1387 de geçer.",
 "Murad'ın Kosova seferi bu yenilgiye bağlanır. Murad maddesinde ayrıca anılmaz.", "Murad's Kosovo campaign is linked to this defeat. It is not mentioned separately in the Murad article."),
("Kosova (1389)", "Battle of Kosovo", "1389-06-15", "I. Murad–Sırp ittifakı", "Kosova ovası", 42.70, 21.10, "approx", "Kosova",
 O, "Sırbistan (Lazar), Bosna, Vuk Branković ve müttefikleri", "I. Murad (şehit), Şehzade Bayezid", "Lazar (idam edildi), Vlatko Vuković", "dis", "W", "ihtilafli",
 ["TDVIA:murad-i", "TDVIA:bayezid-i", "TDVIA:kosova-savaslari"],
 "TDVİA: kesin Osmanlı zaferi. Alternatif okuma: Bosna Kralı Tvrtko zaferi kendisine mal etti ve Paris'te Türklerin bozguna uğradığı yazıldı; Stefan Lazareviç'in biyografı ise yenilgiyi açıkça kabul eder. Karar [P6]: Osmanlı zaferi.",
 "I. Murad savaş meydanında öldürüldü; Bayezid meydanda tahta çıkarıldı.", "Murad I was killed on the field; Bayezid was proclaimed sultan there."),
("Çorumlu (Kırkdilim)", "Battle of Kırkdilim", "1392", "Yıldırım Bayezid–Kadı Burhâneddin", "Çorumlu", 40.55, 34.95, "approx", "Türkiye",
 KB, O, "Şehzade Ertuğrul", "Kadı Burhâneddin", "turk_arasi", "L", "kesin",
 ["TDVIA:kadi-burhaneddin"], "", "Osmanlı kuvvetleri yenilip geri çekildi.", "The Ottoman forces were defeated and withdrew."),
("Argeş (Rovine)", "Battle of Rovine", "1395-05-17", "Yıldırım Bayezid–Eflak", "Argeş nehri yakını", 44.60, 24.90, "region", "Romanya",
 O, "Eflak (Mircea)", "Yıldırım Bayezid", "Mircea", "dis", "W", "ihtilafli",
 ["TDVIA:bayezid-i"], "TDVİA: Mircea yenildi ve yerine Vlad getirildi. Alternatif okuma: Romen kaynakları Rovine'yi Mircea'nın zaferi sayar; modern literatürde sonuç tartışmalıdır. Karar [P6]: Osmanlı zaferi.",
 "", ""),
("Niğbolu", "Battle of Nicopolis", "1396-09-25", "Niğbolu Haçlı Seferi", "Niğbolu", 43.70, 24.90, "approx", "Bulgaristan",
 O, "Haçlılar (Macar, Fransız, Alman, Eflak)", "Yıldırım Bayezid", "Sigismund", "dis", "W", "kesin",
 ["TDVIA:bayezid-i", "TDVIA:nigbolu-savasi"], "", "Bayezid İstanbul kuşatmasını kaldırıp Niğbolu'ya yetişti.", "Bayezid lifted the siege of Constantinople and hurried to Nicopolis."),
("Akçay", "Battle of Akçay", "1397", "Yıldırım Bayezid–Karamanoğulları", "Akçay, Konya yakını", 37.80, 32.40, "region", "Türkiye",
 O, KAR, "Yıldırım Bayezid", "Karamanoğlu Alâeddin Bey (öldürüldü)", "turk_arasi", "W", "kesin",
 ["TDVIA:bayezid-i"], "", "Alâeddin Bey Konya Kalesi'ne kapandı, yakalanıp öldürüldü.", "Alaeddin Bey shut himself in Konya castle and was captured and killed."),
("Ankara", "Battle of Ankara", "1402-07-28", "Osmanlı–Timur", "Çubuk ovası, Ankara", 40.05, 32.95, "approx", "Türkiye",
 "Timur", O, "Yıldırım Bayezid (esir)", "Timur", "dis", "L", "kesin",
 ["TDVIA:ankara-savasi", "TDVIA:bayezid-i"], "",
 "Bayezid esir düştü ve Akşehir'de öldü (8 Mart 1403). Timurlular Türk kökenlidir ama kapsam listesinde değildir; dış rakip sayıldı. Osmanlı Fetret Devri başladı.",
 "Bayezid was captured and died at Akşehir (8 March 1403). The Timurids were of Turkic origin but outside the scope list, so recorded as external. The Ottoman Interregnum followed."),
]

# İkinci kaynak turu (2026-10-29)
EXTRA_SRC = {"Kulaca Hisar": ["TDVIA:osman-i"], "Savra (Muzakiye ovası)": ["TDVIA:arnavutluk"],  # kontrol turu
             "İzmit'in teslimi": ["TDVIA:izmit"], "Manastır": ["TDVIA:manastir--makedonya"], "Niş": ["TDVIA:nis"],
             "Selânik'in teslimi": ["TDVIA:selanik"], "Bileća": ["TDVIA:bosna-hersek"], "Karacahisar": ["TDVIA:eskisehir"],
             "Akçay": ["TDVIA:alaeddin-bey--karamanogullari", "AKD:safakci-2023"],
             "Çorumlu (Kırkdilim)": ["AKD:derinoz-2022", "AKD:eroglu-sehzadeler"], "Argeş (Rovine)": ["AKD:heper-2023"]}
FIX = {"Argeş (Rovine)": {"dispute": "TDVİA: Mircea yenildi ve yerine Vlad getirildi. Heper (2023): Argeş ya da Rovine civarındaki savaştan sonra Mircea ile anlaşılıp Eflak'ta hâkimiyet sağlandı; savaşın yeri ve tarihi literatürde tartışmalıdır. Alternatif okuma: Romen kaynakları Rovine'yi Mircea'nın zaferi sayar. Karar [P6]: Osmanlı zaferi."},
       "Manastır": {"dispute": "Tarih: Manastır maddesi 784-785 (1382-83), bazı rivayetlere göre 787 (1385) verir."},
       "Niş": {"note": "Yirmi beş gün süren ağır bir kuşatmadan sonra yağma ilânıyla alındı (Niş maddesi).", "note_en": "Taken after a heavy 25-day siege following a declaration of plunder (Niš article)."},
       "Karacahisar": {"dispute": "Tarih: Roma veri seti 1288; Osmanlı rivayetleri 1291 (Eskişehir maddesi). Fetih tarihi kaynaklarda tartışmalıdır."},
       "Akçay": {"date": "1397/1398", "status": "ihtilafli",
                 "dispute": "Tarih: Alâeddin Bey maddesi 800 (1397-98) verir ve ayın belli olmadığını belirtir; Şafakçı (2023) Şükrullah'ın ikinci seferi 793 (1391), Karamanî Mehmed Paşa'nın 800 (1397) yılına koyduğunu gösterir.",
                 "note": "İki gün süren savaşta yenilen Alâeddin Bey Konya Kalesi'ne sığındı; kuşatmanın onuncu gününde şehir teslim oldu, Alâeddin Bey yakalanıp öldürüldü.",
                 "note_en": "Defeated in a two-day battle, Alaeddin Bey took refuge in Konya castle; the city surrendered on the tenth day of the siege and he was captured and killed."},
       "Çorumlu (Kırkdilim)": {"note": "Üç gün süren savaşı Osmanlılar kaybetti (Derinöz 2022). Osmanlı kroniklerine (Neşrî) dayanan yaygın görüşe göre Şehzade Ertuğrul burada şehit düştü; Eroğlu ise savaşı ayrıntılı anlatan Esterâbâdî'nin Ertuğrul'dan hiç söz etmediğine dikkat çekerek bunu sorgular.",
                               "note_en": "The Ottomans lost a three-day battle (Derinöz 2022). The common view based on Ottoman chronicles (Neşri) is that Prince Ertuğrul fell here; Eroğlu questions this, noting that Astarabadi, who describes the battle in detail, never mentions him."}}
OPP_STATE = {"Frenkyazısı": KAR, "Akçay": KAR, "Çorumlu (Kırkdilim)": KB, "Eretna kuvvetlerine karşı": ERT}
LEFT = [
 {"name": "Bilecik ve Yarhisar (1299)", "reason": "Rivayete göre hile ile alındı; meydan savaşı yok.", "source": "TDVIA:osman-i"},
 {"name": "İstanbul ablukası (1394–1402)", "reason": "Uzun süreli abluka; tek bir savaş değil.", "source": "TDVIA:bayezid-i"},
 {"name": "Sivas (1400)", "reason": "Timur'un Sivas'ı alması; şehir teslim oldu, savunan Osmanlı garnizonuydu. Ayrıntı için ikinci tur.", "source": "TDVIA:bayezid-i"},
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
    v["tdvia"] = any(x.startswith("TDVIA:") for x in srcs); v["tdvia2"] = len([x for x in srcs if x.startswith("TDVIA:")]) >= 2
    v["academic"] = any(x.startswith("AKD:") for x in srcs)
    recs.append(rec)

pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 5 — Osmanlı kuruluş dönemi (1284–1402)", "compiled": "2026-10-28", "status": "İlk tur.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "osmanli-kurulus.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli;", sum(r["verify"]["rom"] for r in recs), "ROM")
