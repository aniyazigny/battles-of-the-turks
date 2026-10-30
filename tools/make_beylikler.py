"""data/beylikler-atabeylikler.json dosyasını üretir (Parti 3: Türk beylikleri ve atabeylikleri, 1070–1175).
Pilottan taşınan üç kayıt (Sivas 1070, Kahire 1077, Harran 1104) pilot dosyasından okunur ve burada yeniden numaralanır."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "beylikler-atabeylikler"
CAK = "Çaka Bey (İzmir Beyliği)"
ART, DAN, ZEN, BOR, SAL, ILD, MUS, ATS = ("Artuklular", "Dânişmendliler", "Zengîler", "Böriler (Dımaşk Atabegliği)",
                                         "Saltuklular", "İldenizliler", "Musul atabegleri (Porsukîler)", "Atsız b. Uvak")
HRN = "Hârûn b. Han (Kuzey Suriye Türkmenleri)"
RID = "Halep Selçuklu melikliği (Rıdvân)"
# (devlet, ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en)
R = [
(ATS, "Taberiye (1075)", "Battle of Tiberias (1075)", "1075-07", "Atsız'ın Suriye emîrliği", "Taberiye yöresi", 32.79, 35.53, "approx", "İsrail",
 "Atsız b. Uvak", "Şöklü, Kutalmışoğulları", "Atsız b. Uvak", "Şöklü", "turk_arasi", "W", "kesin",
 ["TDVIA:suleyman-sah-i"], "", "Şöklü ve oğlu öldürüldü; Süleyman Şah'ın kardeşleri Atsız'ın eline düştü ve Melikşah'a gönderildi.",
 "Shöklü and his son were killed; Sulayman's brothers fell into Atsiz's hands and were sent to Malikshah."),
(HRN, "Artah ve İm (1068)", "Turkmen capture of Artah and Imm (1068)", "1068-07-01", "Kuzey Suriye Türkmenlerinin Bizans'la mücadelesi", "Artah", 36.27, 36.57, "approx", "Türkiye",
 "Hârûn b. Han ve Mirdâsî Emîr Mahmûd", "Bizans", "Hârûn b. Han", "", "dis", "W", "kesin",
 ["TDVIA:harun-b-han"], "", "Türkmen ve Arap kuvvetlerini birleştiren Hârûn ve Emîr Mahmûd Bizans topraklarına gazâya başlayarak Artah ve İm kalelerini aldı; Halep Bizans saldırılarına karşı güçlendi. (Kontrol turunda eklendi.)",
 "Uniting Turkmen and Arab forces, Harun and Emir Mahmud raided Byzantine territory and took the castles of Artah and Imm."),
(HRN, "Artah'ın kaybı (1069)", "Byzantine recapture of Artah (1069–70)", "1069", "Kuzey Suriye Türkmenlerinin Bizans'la mücadelesi", "Artah", 36.27, 36.57, "approx", "Türkiye",
 "Bizans", "Hârûn b. Han ve Mirdâsî Emîr Mahmûd", "Hârûn b. Han", "", "dis", "L", "kesin",
 ["TDVIA:harun-b-han"], "Madde geri alışı 462 (1069-70) yılına koyar.", "Bizanslılar geri çekilen Türkmen ve Arap kuvvetlerini takip edemediyse de Artah ve İm kalelerini kolayca geri aldı. (Kontrol turunda eklendi.)",
 "The Byzantines did not dare pursue the retreating Turkmen and Arab forces but easily retook Artah and Imm."),
(RID, "Kınnesrîn (1097)", "Battle of Qinnasrin (1097)", "1097-03-22", "Tutuş'un oğulları arasındaki mücadele", "Kınnesrîn", 35.99, 37.05, "approx", "Suriye",
 "Rıdvân (Halep)", "Dukak (Dımaşk)", "Rıdvân b. Tutuş", "Dukak", "ic", "C", "kesin",
 ["TDVIA:ridvan-b-tutus"], "", "Halep'e saldıran Dukak Kınnesrîn'de bozguna uğradı. (Kontrol turunda eklendi.)", "Duqaq, who had attacked Aleppo, was routed at Qinnasrin."),
(ART, "Suruç (I)", "Battle of Saruj (I)", "1100", "Artukluların Haçlılarla mücadelesi", "Suruç", 36.98, 38.42, "known", "Türkiye",
 "Artuklular (Sökmen, Belek)", "Urfa Kontluğu, Suruç Senyörlüğü, Ermeni birlikleri", "Sökmen b. Artuk, Belek b. Behrâm", "II. Baudouin, Foulque de Chartres", "dis", "W", "ihtilafli",
 ["TDVIA:sokmen-b-artuk", "TDVIA:belek-b-behram"], "Tarih: Belek maddesi 1100 verir; Sökmen maddesi tarih vermez ve olayı 1098'deki işgalden sonraya koyar.",
 "Haçlı ve Ermeni kuvvetleri ağır yenildi, Foulque de Chartres öldü. Sökmen ardından iç kaleyi kuşattı.",
 "The Crusader and Armenian forces were heavily defeated and Fulcher of Chartres was killed. Sökmen then besieged the citadel."),
(ART, "Suruç (II)", "Battle of Saruj (II)", "1101", "Artukluların Haçlılarla mücadelesi", "Suruç", 36.98, 38.42, "known", "Türkiye",
 "Urfa Kontluğu (Antakya yardımıyla)", "Artuklular", "Sökmen b. Artuk, Belek b. Behrâm", "II. Baudouin", "dis", "L", "kesin",
 ["TDVIA:sokmen-b-artuk", "TDVIA:belek-b-behram"], "",
 "Sökmen düşmanı bozmak üzereyken bir kısım Türkmenin savaş alanını terk etmesiyle çekilmek zorunda kaldı.",
 "Sökmen was close to victory when part of his Turkmens left the field, forcing him to withdraw."),
(ART, "Âmid (Kürboğa'ya karşı)", "Battle of Amida (1101)", "1101", "Diyarbekir mücadeleleri", "Âmid", 37.91, 40.23, "approx", "Türkiye",
 "Kürboğa (Musul)", "Artuklular, İnaloğulları", "Sökmen b. Artuk", "Kürboğa", "turk_arasi", "L", "borderline",
 ["TDVIA:sokmen-b-artuk"], "", "Kürboğa savaşı kazandı ama şehri alamadı. Kürboğa Büyük Selçuklu valisidir; Artuklular ayrı hanedan olduğu için Türk devletleri arası.",
 "Kerbogha won the battle but could not take the city. Kerbogha was a Great Seljuk governor; the Artuqids were a separate dynasty, so inter-Turkic."),
(DAN, "Malatya (Bohemund'un esareti)", "Battle of Melitene (1100)", "1100-07", "Dânişmendlilerin Haçlılarla mücadelesi", "Malatya yakını", 38.35, 38.31, "approx", "Türkiye",
 "Dânişmendliler", "Antakya Prinkepsliği", "Gümüştegin Gazi", "Bohemund (esir), Richard de Salerno", "dis", "W", "kesin",
 ["TDVIA:danismendliler", "TDVIA:kilicarslan-i", "TDVIA:haclilar"], "Tarih: Dânişmendliler maddesi Ramazan 493 / Temmuz 1100, Kılıcarslan I maddesi Şevval 493 / Ağustos 1100.",
 "Bohemund pusuya düşürülüp esir alındı ve Niksar'da hapsedildi. Bu olay 1101 Haçlı seferinin Amasya–Niksar yönüne gitmesinin sebebidir.",
 "Bohemond was ambushed, captured and imprisoned at Niksar. This drew the 1101 Crusade towards Amasya and Niksar."),
(DAN, "Malatya'nın fethi (1102)", "Capture of Melitene (1102)", "1102-09-18", "Dânişmendlilerin Malatya seferi", "Malatya", 38.35, 38.31, "known", "Türkiye",
 "Dânişmendliler", "Ermeniler (Malatya, Gabriel)", "Gümüştegin Gazi", "Gabriel", "dis", "W", "kesin",
 ["TDVIA:danismendliler", "TDVIA:kilicarslan-i"], "", "Uzun kuşatmadan sonra kıtlık çeken halk Gabriel'e karşı döndü.", "After a long siege the starving townspeople turned against Gabriel."),
(ART, "Dârâ (Aksungur'a karşı)", "Battle of Dara (1115)", "1115", "İlgazi–Büyük Selçuklu", "Dârâ yakını", 37.18, 40.95, "approx", "Türkiye",
 "Artuklular", "Büyük Selçuklu ordusu (Aksungur el-Porsukī)", "İlgazi, Behrâm, Dâvud", "Aksungur el-Porsukī", "turk_arasi", "W", "kesin",
 ["TDVIA:ilgazi-necmeddin", "TDVIA:aksungur-el-porsuki"], "", "Sultanın oğlu Mesud esir alındı. İlgazi daha önce Haçlılara karşı cihada katılmayı reddetmişti.",
 "The sultan's son Mas'ud was captured. Ilghazi had earlier refused to join the campaign against the Crusaders."),
(ART, "Belâta (Ager Sanguinis)", "Battle of Ager Sanguinis", "1119-06-28", "Artukluların Haçlılarla mücadelesi", "Tel İfrîn vadisi, Sermedâ yakını", 36.18, 36.72, "approx", "Suriye",
 "Artuklular", "Antakya Prinkepsliği", "Necmeddin İlgazi", "Ruggero di Salerno (öldü)", "dis", "W", "kesin",
 ["TDVIA:ilgazi-necmeddin", "TDVIA:haclilar"], "", "Kaynaklarda \"Kanlı Meydan\" diye anılır; Haçlı ordusu âdeta imha edildi.", "Known as the Field of Blood; the Crusader army was all but destroyed."),
(ART, "Şiran (Bayburt yakını)", "Battle of Shiran (1120)", "1120", "Belek–Mengücüklüler ve Trabzon", "Şiran (Serman), Bayburt yakını", 40.19, 39.12, "approx", "Türkiye",
 "Artuklular (Belek), Dânişmendliler (Emîr Gazi)", "Mengücüklüler, Trabzon Dükalığı (Bizans)", "Belek b. Behrâm, Emîr Gazi", "Mengücüklü İshak, Konstantin Gabras", "dis", "W", "kesin",
 ["TDVIA:belek-b-behram", "TDVIA:danismendliler", "TDVIA:mengucukluler"], "Yer: Dânişmendliler maddesi Bayburt yakınında Serman (Şiran), Mengücüklüler maddesi Erzincan yakınında Sirvan der; Belek maddesi yalnızca Bayburt yakını der.",
 "Gabras ve Mengücükoğlu esir alındı; Gabras 30.000 dinar fidyeyle bırakıldı. Mengücüklüler Türk beyliğidir; asıl rakip Bizans'ın Trabzon dükü olduğu için dış rakip.",
 "Gabras and the Mengujekid ruler were captured; Gabras was ransomed for 30,000 dinars. The Mengujekids were a Turkic beylik; the main opponent was the Byzantine duke of Trebizond, so recorded as external."),
(ART, "Serûc (Josselin'in esareti)", "Battle of Saruj (1122)", "1122-09-13", "Artukluların Haçlılarla mücadelesi", "Serûc yakını", 36.98, 38.42, "approx", "Türkiye",
 "Artuklular", "Urfa Kontluğu", "Belek b. Behrâm", "Josselin de Courtenay (esir), Galéran du Puiset (esir)", "dis", "W", "kesin",
 ["TDVIA:belek-b-behram"], "", "Esirler Harput'ta hapsedildi.", "The prisoners were held at Harput."),
(ART, "Turuş (Kral Baudouin'in esareti)", "Battle of Gargar (1123)", "1123-04-18", "Artukluların Haçlılarla mücadelesi", "Turuş, Fırat'ın batı kıyısı", 37.85, 38.30, "approx", "Türkiye",
 "Artuklular", "Kudüs Krallığı", "Belek b. Behrâm", "II. Baudouin (esir)", "dis", "W", "kesin",
 ["TDVIA:belek-b-behram"], "", "Kral, Gerger'i kuşatan Belek'e karşı yardıma giderken baskına uğradı. Sultan Mahmud bu zaferden sonra Belek'i Haçlılara karşı başkumandan yaptı.",
 "The king was surprised while marching to relieve Gerger from Belek. Sultan Mahmud then made Belek commander-in-chief against the Crusaders."),
(ART, "Harput Kalesi'nin geri alınması", "Recapture of Kharpert (1123)", "1123-09", "Artukluların Haçlılarla mücadelesi", "Harput", 38.70, 39.25, "known", "Türkiye",
 "Artuklular", "Haçlı esirleri ve Ermeni yardımcıları", "Belek b. Behrâm", "Josselin'in adamları", "dis", "W", "kesin",
 ["TDVIA:belek-b-behram"], "", "Kaleyi ele geçiren Haçlı esirleri Belek yetişince yenildi; kral ve senyörler Harran'a gönderildi.",
 "The Crusader prisoners who had seized the castle were overcome when Belek arrived; the king and lords were sent to Harran."),
(ART, "Azâz kuşatması (1123–24)", "Siege of Azaz (1123–24)", "1124", "Artukluların Haçlılarla mücadelesi", "Azâz", 36.59, 37.05, "known", "Suriye",
 "Haçlılar", "Türk birleşik kuvvetleri", "Belek b. Behrâm'ın emîrleri", "", "dis", "L", "borderline",
 ["TDVIA:belek-b-behram"], "", "Kale garnizonu ile yardıma gelen Haçlılar arasında kalan Türk ordusu yenildi. Komutan ve tarih kaynakta net değil.",
 "Caught between the garrison and a relief force, the Turkish army was defeated. Commander and date are unclear in the source."),
(ART, "Meşhalâ", "Battle of Mashala (1124)", "1124", "Artukluların Haçlılarla mücadelesi", "Azâz yöresi", 36.55, 37.10, "region", "Suriye",
 "Artuklular", "Haçlılar", "Belek b. Behrâm'ın kuvvetleri", "", "dis", "W", "kesin",
 ["TDVIA:belek-b-behram"], "", "Ardından Mücedded Kalesi alındı.", "Mujaddad castle was then taken."),
(ART, "Menbic", "Battle of Manbij (1124)", "1124-05-05", "Artukluların Haçlılarla mücadelesi", "Menbic yakını", 36.53, 37.95, "approx", "Suriye",
 "Artuklular", "Urfa Kontluğu, Menbic hâkimi Hassân b. Gümüştegin'in kardeşi", "Belek b. Behrâm", "Josselin de Courtenay", "dis", "W", "kesin",
 ["TDVIA:belek-b-behram"], "", "Ertesi gün kuşatmayı sürdüren Belek kaleden atılan bir okla öldü (6 Mayıs 1124).",
 "Belek, continuing the siege next day, was killed by an arrow from the castle (6 May 1124)."),
(MUS, "Halep'in kurtarılması (1125)", "Relief of Aleppo (1125)", "1125-01", "Haçlılarla mücadele", "Halep", 36.20, 37.16, "known", "Suriye",
 "Musul atabegi Aksungur el-Porsukī", "Kudüs Krallığı, Dübeys b. Sadaka", "Aksungur el-Porsukī", "II. Baudouin, Dübeys b. Sadaka", "dis", "W", "kesin",
 ["TDVIA:aksungur-el-porsuki"], "", "Kuşatanlar çekildi; Aksungur şehri aldı.", "The besiegers withdrew and Aqsunqur took over the city."),
(MUS, "Azâz (1125)", "Battle of Azaz (1125)", "1125-06", "Haçlılarla mücadele", "Azâz", 36.59, 37.05, "approx", "Suriye",
 "Kudüs Krallığı, Antakya ve Trablus", "Musul atabegi Aksungur el-Porsukī, Tuğtegin", "Aksungur el-Porsukī, Tuğtegin", "II. Baudouin", "dis", "L", "kesin",
 ["TDVIA:aksungur-el-porsuki", "TDVIA:tugtegin"], "", "Ağır bir bozgun; Haçlılar takip edecek güç bulamadı.", "A heavy defeat; the Crusaders lacked the strength to pursue."),
(BOR, "Taberiye (1108)", "Battle of Tiberias (1108)", "1108", "Tuğtegin'in Haçlılarla mücadelesi", "Taberiye yakını", 32.79, 35.53, "approx", "İsrail",
 "Dımaşk (Tuğtegin)", "Kudüs Krallığı", "Tuğtegin", "Gervaise de Bazoches (esir, öldürüldü)", "dis", "W", "kesin",
 ["TDVIA:tugtegin"], "", "", ""),
(RID, "Tel Bâşir (1108)", "Battle of Turbessel (1108)", "1108-09", "Musul ve Halep emîrlerinin mücadelesi", "Tel Bâşir", 36.79, 37.82, "known", "Türkiye",
 "Rıdvân ve Antakya (Tankred)", "Çavlı (Musul), Urfa Kontluğu (Baudouin, Joscelin)", "Rıdvân b. Tutuş", "Çavlı Sakavu", "turk_arasi", "D", "kesin",
 ["TDVIA:ridvan-b-tutus"], "", "Bâlîs'i işgal eden Çavlı'ya karşı Rıdvân Tankred'le, Çavlı da Baudouin ve Joscelin'le ittifak yaptı; savaşta iki taraf da ağır kayıp verdi, Bâlîs Halep'e döndü. (Kontrol turunda eklendi.)",
 "Against Chavli, who had seized Balis, Ridwan allied with Tancred and Chavli with Baldwin and Joscelin; both sides suffered heavy losses and Balis returned to Aleppo."),
(BOR, "Refeniye (1115)", "Battle of Rafaniyya (1115)", "1115-11", "Tuğtegin'in Haçlılarla mücadelesi", "Refeniye", 34.95, 36.40, "approx", "Suriye",
 "Dımaşk (Tuğtegin)", "Haçlılar (Refeniye garnizonu)", "Tuğtegin", "", "dis", "W", "kesin",
 ["TDVIA:tugtegin"], "", "Haçlıların işgal ettiği Refeniye âni bir baskınla geri alındı (Cemâziyelâhir 509).", "Rafaniyya, occupied by the Crusaders, was recovered in a surprise attack (November 1115)."),
(BOR, "Kont Guillaume'un baskını", "Defeat by William-Jordan (1109)", "1109", "Tuğtegin'in Haçlılarla mücadelesi", "Trablus yöresi", 34.50, 36.00, "region", "Lübnan",
 "Trablus Kontluğu", "Dımaşk (Tuğtegin)", "Tuğtegin", "Guillaume Jourdain", "dis", "L", "borderline",
 ["TDVIA:tugtegin"], "", "Baskına uğrayan Tuğtegin ağır şartlarla anlaşmak zorunda kaldı.", "Surprised, Toghtekin was forced into a treaty on harsh terms."),
(BOR, "Pons'un yenilgisi (1137)", "Defeat of Pons of Tripoli (1137)", "1137", "Dımaşk–Trablus", "Trablus Kontluğu sınırı", 34.30, 36.10, "region", "Lübnan",
 "Dımaşk (Börîler)", "Trablus Kontluğu", "Dımaşk emîrleri", "Pons (öldü)", "dis", "W", "borderline",
 ["TDVIA:haclilar"], "", "Pons Dımaşklılara karşı savaşta öldü. Yeri ve Dımaşklı komutan kaynakta yok.", "Pons was killed fighting the Damascenes. Place and Damascene commander not given."),
(BOR, "Mercüssuffer", "Battle of Marj al-Saffar (1126)", "1126-01", "Tuğtegin'in Haçlılarla mücadelesi", "Mercüssuffer, Dımaşk güneyi", 33.25, 36.18, "approx", "Suriye",
 "Kudüs Krallığı", "Dımaşk (Tuğtegin)", "Tuğtegin", "II. Baudouin", "dis", "L", "kesin",
 ["TDVIA:tugtegin"], "", "Haçlı piyadesi ağır kayıp verdi ama Türk süvarisi bozuldu.", "The Crusader infantry suffered heavily but the Turkish cavalry was routed."),
(BOR, "Dımaşk (1148)", "Siege of Damascus (1148)", "1148-07-24", "İkinci Haçlı Seferi", "Dımaşk", 33.51, 36.29, "known", "Suriye",
 "Dımaşk (Üner)", "Haçlılar (Kudüs, Fransız ve Alman orduları)", "Muînüddin Üner", "VII. Louis, III. Konrad, III. Baudouin", "dis", "W", "kesin",
 ["TDVIA:haclilar"], "", "Yardımcı kuvvetler kuzey kapısından girince Üner karşı taarruza geçti; İkinci Haçlı Seferi böylece sonuçsuz kaldı.",
 "When relief forces entered by the north gate, Unur counter-attacked; the Second Crusade ended without result."),
(ZEN, "Serce (Artuklulara karşı)", "Battle of Serce (c. 1130)", "c. 1130", "Zengî–Artuklular", "Serce, Mardin–Nusaybin arası", 37.15, 41.00, "approx", "Türkiye",
 "Zengîler", "Artuklular (Dâvûd, Timurtaş)", "İmâdüddin Zengî", "Dâvûd b. Sökmen, Hüsâmeddin Timurtaş", "turk_arasi", "W", "kesin",
 ["TDVIA:zengi-imaduddin"], "", "Kaynaktaki sayılar (20.000 Türkmene karşı 4000) alınmadı.", "The source figures (4,000 against 20,000 Turkmens) are not used."),
(ZEN, "Esârib'in fethi", "Capture of al-Atharib (1130)", "1130", "Zengî'nin Haçlılarla mücadelesi", "Esârib", 36.14, 36.83, "approx", "Suriye",
 "Zengîler", "Antakya Prinkepsliği", "İmâdüddin Zengî", "", "dis", "W", "borderline",
 ["TDVIA:zengi-imaduddin"], "", "Çatışmanın ayrıntısı kaynakta yok.", "No detail of the fighting in the source."),
(ZEN, "Hama (1130)", "Seizure of Hama (1130)", "1130-09-24", "Zengî'nin Suriye siyaseti", "Hama", 35.13, 36.75, "known", "Suriye",
 "Zengîler", "Böriler (Dımaşk; Sevinç)", "İmâdüddin Zengî", "Sevinç b. Böri", "turk_arasi", "W", "borderline",
 ["TDVIA:zengi-imaduddin"], "", "Zengî, askerleriyle Halep'e gelen Dımaşk Atabegi Böri'nin oğlu Sevinç'i hapsettirip savunmasız kalan Hama'yı kolayca aldı (18 Şevval 524 / 24 Eylül 1130). Muharebe değil hile ile alındığından borderline. (Kontrol turunda eklendi.)",
 "Zengi imprisoned Sevinch, son of the atabeg of Damascus, who had come to Aleppo with his troops, and easily took the undefended Hama. Borderline, as it was taken by ruse rather than battle."),
(ZEN, "Karaca Sâkî'ye yenilgi", "Defeat by Qaraja al-Saqi", "c. 1132", "Irak Selçuklu taht mücadelesi", "Irak (yer belirsiz)", 34.50, 44.00, "region", "Irak",
 "Irak Selçukluları (Atabeg Karaca Sâkî)", "Zengîler", "İmâdüddin Zengî", "Karaca Sâkî", "turk_arasi", "L", "borderline",
 ["TDVIA:zengi-imaduddin"], "", "Zengî, Mesud'a katılmak üzere yola çıkmıştı. Atabeylik ile sultanlık arası olduğu için Türk devletleri arası sayıldı.",
 "Zengi had set out to join Mas'ud. Counted as inter-Turkic because it was between an atabegate and the sultanate."),
(ZEN, "Âmid (Dâvûd'a karşı)", "Battle near Amida (1134)", "1134-04-26", "Zengî–Artuklular", "Âmid yakını", 37.91, 40.23, "approx", "Türkiye",
 "Zengîler, Mardin Artukluları", "Hasankeyf Artukluları", "İmâdüddin Zengî, Timurtaş", "Dâvûd b. Sökmen", "turk_arasi", "W", "kesin",
 ["TDVIA:zengi-imaduddin"], "", "Âmid kuşatıldı ama alınamadı.", "Amida was besieged but not taken."),
(ZEN, "Humus kuşatması (1135)", "Siege of Homs (1135)", "1135-08", "Zengî'nin Suriye siyaseti", "Humus", 34.73, 36.71, "known", "Suriye",
 "Humus (Böriler)", "Zengîler", "İmâdüddin Zengî", "", "turk_arasi", "D", "kesin",
 ["TDVIA:zengi-imaduddin"], "", "Humus'u kuşatan Zengî, Musul'un halife tarafından kuşatılacağı haberi üzerine kuşatmayı kaldırıp Musul'a döndü (Ağustos 1135 başları). (Kontrol turunda eklendi.)",
 "Zengi, besieging Homs, lifted the siege and returned to Mosul on news that the caliph was about to besiege it."),
(ZEN, "Ba'rîn", "Battle of Montferrand (1137)", "1137-07", "Zengî'nin Haçlılarla mücadelesi", "Ba'rîn", 34.97, 36.47, "approx", "Suriye",
 "Zengîler", "Kudüs Krallığı, Trablus Kontluğu", "İmâdüddin Zengî", "Foulque, II. Raimond (esir)", "dis", "W", "kesin",
 ["TDVIA:zengi-imaduddin", "TDVIA:haclilar"], "", "Kral Foulque baskından güçlükle kurtuldu; Bizans seferi haberiyle kaleyi emanla teslim etti.",
 "King Fulk barely escaped; on news of the Byzantine campaign he surrendered the castle on terms."),
(ZEN, "Urfa'nın fethi", "Siege of Edessa (1144)", "1144-12-24", "Zengî'nin Haçlılarla mücadelesi", "Urfa", 37.16, 38.79, "known", "Türkiye",
 "Zengîler", "Urfa Kontluğu", "İmâdüddin Zengî", "II. Josselin (şehirde değildi)", "dis", "W", "kesin",
 ["TDVIA:zengi-imaduddin", "TDVIA:zengiler", "TDVIA:haclilar"], "",
 "İlk Haçlı devleti sona erdi; haber Avrupa'da İkinci Haçlı Seferi'ne yol açtı.", "The first Crusader state ended; the news led to the Second Crusade."),
(ZEN, "Bire kuşatması", "Siege of al-Bira (1145)", "1145", "Zengî'nin Haçlılarla mücadelesi", "Birecik", 37.03, 37.98, "known", "Türkiye",
 "Haçlılar (Bire garnizonu)", "Zengîler", "İmâdüddin Zengî", "", "dis", "L", "kesin",
 ["TDVIA:zengi-imaduddin"], "", "Kale düşmek üzereyken Musul nâibinin öldürüldüğü haberiyle kuşatma kaldırıldı.", "Lifted, with the castle about to fall, on news that his deputy in Mosul had been killed."),
(ZEN, "Suruç (1145)", "Capture of Saruj (1145)", "1145-01", "Zengî'nin Haçlılarla mücadelesi", "Suruç", 36.98, 38.42, "known", "Türkiye",
 "Zengîler", "Urfa Kontluğu", "İmâdüddin Zengî", "", "dis", "W", "kesin",
 ["TDVIA:zengi-imaduddin"], "", "Urfa'dan Suruç'a gelen Zengî, garnizonun terk ettiği şehri kolayca aldı (Receb 539 / Ocak 1145). (Kontrol turunda eklendi.)", "Coming from Edessa, Zengi easily took Saruj, abandoned by its garrison."),
(ZEN, "Ca'ber kuşatması (1146)", "Siege of Qal'at Ja'bar (1146)", "1146-09-14", "Zengî'nin el-Cezîre siyaseti", "Ca'ber Kalesi", 35.89, 38.48, "known", "Suriye",
 "Ukaylîler (Sâlim el-Ukaylî)", "Zengîler", "İmâdüddin Zengî", "Sâlim el-Ukaylî", "dis", "L", "kesin",
 ["TDVIA:zengi-imaduddin", "TDVIA:caber-kalesi"], "", "17 Mayıs 1146'dan beri kuşatılan kalenin önünde Zengî 14–15 Eylül 1146 gecesi kölesi Yarınkuş tarafından öldürüldü; kuşatma kaldırıldı. (Kontrol turunda eklendi.)",
 "Zengi, besieging the castle since 17 May 1146, was murdered by his slave Yarınkuş on the night of 14–15 September 1146; the siege was abandoned."),
(ZEN, "Urfa (1146)", "Edessa (1146)", "1146-11", "Nûreddin'in Haçlılarla mücadelesi", "Urfa", 37.16, 38.79, "known", "Türkiye",
 "Zengîler", "Urfa Kontluğu", "Nûreddin Mahmud, Şîrkûh, Savar", "II. Josselin", "dis", "W", "kesin",
 ["TDVIA:nureddin-zengi-mahmud", "TDVIA:sirkuh-el-mansur"], "", "Josselin iç kale dışında şehri ele geçirmişti; Nûreddin şehri geri aldı.", "Joscelin had seized the town except the citadel; Nur al-Din retook it."),
(ZEN, "Yağra", "Battle of Yaghra (1148)", "1148-11", "Nûreddin'in Haçlılarla mücadelesi", "Yağra, Antakya yakını", 36.30, 36.40, "approx", "Türkiye",
 "Zengîler", "Antakya Prinkepsliği", "Nûreddin Mahmud, Şîrkûh", "Raimond de Poitiers", "dis", "W", "kesin",
 ["TDVIA:nureddin-zengi-mahmud", "TDVIA:sirkuh-el-mansur"], "", "", ""),
(ZEN, "İnnib (İnab)", "Battle of Inab", "1149-06-29", "Nûreddin'in Haçlılarla mücadelesi", "İnnib, Azâz yöresi", 35.98, 36.43, "approx", "Suriye",
 "Zengîler", "Antakya Prinkepsliği, İsmâilîler", "Nûreddin Mahmud, Şîrkûh", "Raimond de Poitiers (öldü)", "dis", "W", "kesin",
 ["TDVIA:sirkuh-el-mansur", "TDVIA:nureddin-zengi-mahmud"], "Yer: Şîrkûh maddesi 'Azâz yakınlarındaki İnnib' der; Batı kaynaklarına göre İnab, Efâmiye yakınındadır.",
 "Efâmiye kalesi ardından teslim oldu.", "Apamea castle surrendered afterwards."),
(ZEN, "Josselin'e yenilgi", "Defeat by Joscelin II (c. 1150)", "c. 1150", "Nûreddin'in Haçlılarla mücadelesi", "Urfa Kontluğu'nun batı toprakları", 37.00, 37.50, "region", "Türkiye",
 "Urfa Kontluğu (Tel Bâşir)", "Zengîler", "Nûreddin Mahmud", "II. Josselin", "dis", "L", "borderline",
 ["TDVIA:nureddin-zengi-mahmud"], "", "Ardından Türkmenler Josselin'i yakalayıp Nûreddin'e teslim etti (Mayıs 1150).", "Turkmens then captured Joscelin and handed him over to Nur al-Din (May 1150)."),
(ZEN, "Banyas (1153)", "Banyas (1153)", "1153-05", "Nûreddin'in Haçlılarla mücadelesi", "Banyas", 33.25, 35.69, "approx", "Suriye",
 "Zengîler", "Kudüs Krallığı", "Nûreddin Mahmud", "", "dis", "D", "kesin",
 ["TDVIA:nureddin-zengi-mahmud"], "", "Askalân'ı kurtarma girişimi; savaştan sonuç alınamadı.", "An attempt to relieve Ascalon; the battle was inconclusive."),
(ZEN, "Dımaşk'ın alınışı (1154)", "Nur al-Din's capture of Damascus (1154)", "1154", "Nûreddin'in Suriye siyaseti", "Dımaşk", 33.51, 36.29, "known", "Suriye",
 "Zengîler (Nûreddin)", "Böriler (Mücîrüddin Abak)", "Nûreddin Mahmud Zengî; Şîrkûh", "Mücîrüddin Abak", "turk_arasi", "W", "kesin",
 ["TDVIA:nureddin-zengi-mahmud", "TDVIA:sirkuh-el-mansur"], "", "Mücîrüddin kumandanlarını uzaklaştırınca Nûreddin şehri kolayca aldı; Şîrkûh ağabeyi Necmeddin Eyyûb ile temas kurarak şehrin alınmasını sağladı (549/1154). (Kontrol turunda eklendi.)",
 "With Mujir al-Din having dismissed his commanders, Nur al-Din took the city easily; Shirkuh arranged it through his brother Najm al-Din Ayyub."),
(ZEN, "Hârim kuşatması (1156)", "Siege of Harim (1156)", "1156", "Nûreddin'in Haçlılarla mücadelesi", "Hârim", 36.20, 36.52, "known", "Suriye",
 "Antakya Prinkepsliği", "Zengîler", "Nûreddin Mahmud", "", "dis", "L", "kesin",
 ["TDVIA:nureddin-zengi-mahmud"], "", "", ""),
(ZEN, "Hısnülekrâd (el-Bukay'a)", "Battle of al-Buqaia (1163)", "1163", "Nûreddin'in Haçlılarla mücadelesi", "Hısnülekrâd önü", 34.76, 36.29, "approx", "Suriye",
 "Trablus Kontluğu ve müttefikleri", "Zengîler", "Nûreddin Mahmud", "", "dis", "L", "kesin",
 ["TDVIA:nureddin-zengi-mahmud", "TDVIA:zengiler"], "", "Ordu dinlenirken baskına uğradı; Nûreddin yakalanmaktan güçlükle kurtuldu. Ardından cihad çağrısı yaptı ve ertesi yıl Hârim'i aldı.",
 "The army was surprised while resting; Nur al-Din barely escaped capture. He then called for jihad and took Harim the next year."),
(ZEN, "Hârim (1164)", "Battle of Harim (1164)", "1164-08", "Nûreddin'in Haçlılarla mücadelesi", "Hârim", 36.20, 36.52, "known", "Suriye",
 "Zengîler", "Antakya Prinkepsliği, Trablus Kontluğu, Bizans ve Ermeni birlikleri", "Nûreddin Mahmud", "III. Bohemund, III. Raimond", "dis", "W", "kesin",
 ["TDVIA:sirkuh-el-mansur", "TDVIA:nureddin-zengi-mahmud"], "",
 "Hârim kalesi alındı. Bu baskı Haçlıları Mısır'da Şîrkûh'un kuşatmasını kaldırmaya zorladı.", "Harim castle was taken. The pressure forced the Crusaders to lift their siege of Shirkuh in Egypt."),
(ZEN, "Banyas (1164)", "Capture of Banias (1164)", "1164-10", "Nûreddin'in Haçlılarla mücadelesi", "Banyas", 33.25, 35.69, "approx", "Suriye",
 "Zengîler (Nûreddin)", "Kudüs Krallığı", "Nûreddin Mahmud Zengî", "", "dis", "W", "kesin",
 ["TDVIA:nureddin-zengi-mahmud"], "", "Hârim'in ardından 1148-49'dan beri Haçlılar'ın elindeki Banyas fethedildi (Zilhicce 559 / Ekim-Kasım 1164). (Kontrol turunda eklendi.)",
 "After Harim, Banias, held by the Crusaders since 1148–49, was taken (October–November 1164)."),
(ZEN, "Bilbîs (1164)", "Siege of Bilbeis (1164)", "1164", "Nûreddin'in Mısır seferleri", "Bilbîs", 30.42, 31.56, "known", "Mısır",
 "Zengîler (Şîrkûh)", "Şâver ve Kudüs Krallığı (Amaury)", "Şîrkûh", "Şâver, I. Amaury", "dis", "D", "kesin",
 ["TDVIA:sirkuh-el-mansur"], "", "Haçlılar'la birleşen Şâver'in ordusu Bilbîs'teki Şîrkûh'u kuşattı; Nûreddin'in Hârim ve Banyas'a yürümesi üzerine Haçlılar Şîrkûh'la anlaşıp kuşatmayı kaldırdı. (Kontrol turunda eklendi.)",
 "Shawar's army, joined by the Crusaders, besieged Shirkuh in Bilbeis; when Nur al-Din marched on Harim and Banias the Crusaders came to terms with Shirkuh and lifted the siege."),
(ZEN, "Bâbeyn", "Battle of al-Babein", "1167-03", "Nûreddin'in Mısır seferleri", "Bâbeyn, Nil'in batı yakası", 28.10, 30.75, "approx", "Mısır",
 "Zengîler (Şîrkûh)", "Kudüs Krallığı, Fâtımî veziri Şâver", "Esedüddin Şîrkûh", "I. Amaury, Şâver", "dis", "W", "kesin",
 ["TDVIA:nureddin-zengi-mahmud", "TDVIA:sirkuh-el-mansur"], "",
 "Şîrkûh Kürt kökenlidir ama Nûreddin'in komutanı olarak savaştı; K3 gereği Zengîlere yazıldı.", "Shirkuh was of Kurdish origin but fought as Nur al-Din's commander; under K3 recorded for the Zengids."),
(ZEN, "Mısır'ın alınışı (1169)", "Shirkuh's third Egyptian campaign (1168–1169)", "1169-01-18", "Nûreddin'in Mısır seferleri", "Kahire", 30.05, 31.25, "known", "Mısır",
 "Zengîler (Şîrkûh)", "Kudüs Krallığı (Amaury)", "Şîrkûh", "I. Amaury", "dis", "W", "kesin",
 ["TDVIA:sirkuh-el-mansur"], "", "4 Kasım 1168'de Bilbîs'i alıp Kahire'yi kuşatan Amaury, Şîrkûh'un geldiğini öğrenip çekildi; Şîrkûh Kahire'ye girip Fâtımî veziri oldu (18 Ocak 1169). (Kontrol turunda eklendi.)",
 "Amaury, who had taken Bilbeis on 4 November 1168 and besieged Cairo, withdrew on Shirkuh's approach; Shirkuh entered Cairo and became Fatimid vizier (18 January 1169)."),
(ZEN, "Dimyat (1169)", "Siege of Damietta (1169)", "1169-12", "Nûreddin'in Mısır seferleri", "Dimyat", 31.42, 31.81, "known", "Mısır",
 "Zengîler (Selâhaddin)", "Kudüs Krallığı ve Bizans", "Selâhaddîn-i Eyyûbî", "I. Amaury", "dis", "W", "kesin",
 ["TDVIA:dimyat", "TDVIA:nureddin-zengi-mahmud", "TDVIA:selahaddin-i-eyyubi"], "", "Haçlılar ve Bizanslılar Dimyat'ı elli gün kuşattıysa da Selâhaddin karşısında başarı elde edemedi (Kasım–Aralık 1169). Selâhaddin o sırada Nûreddin adına Fâtımî veziriydi. (Kontrol turunda eklendi.)",
 "The Crusaders and Byzantines besieged Damietta for fifty days but failed against Saladin (Nov–Dec 1169), then vizier on Nur al-Din's behalf."),
(ZEN, "Kilikya (Mleh'e destek)", "Cilician campaign (1173)", "1173", "Nûreddin–Bizans", "Kilikya", 36.95, 35.30, "region", "Türkiye",
 "Zengîler, Ermeni Mleh", "Bizans", "Nûreddin Mahmud'un kuvvetleri", "", "dis", "W", "borderline",
 ["TDVIA:nureddin-zengi-mahmud"], "", "Mleh Adana, Misis ve Tarsus'u aldı. Tarih yaklaşık.", "Mleh took Adana, Mamistra and Tarsus. Date approximate."),
(SAL, "Gürcülere karşı zafer (1131)", "Victory over the Georgians (1131)", "1131", "Saltuklu–Gürcü savaşları", "Oltu yöresi", 40.55, 42.00, "region", "Türkiye",
 "Saltuklular", "Gürcistan Krallığı", "Ziyâeddin Gazi", "İvani", "dis", "W", "borderline",
 ["TDVIA:saltuklular"], "", "Yer ve ayrıntı kaynakta az.", "Little detail on place or course in the source."),
(SAL, "Ani baskını (1154)", "Defeat at Ani (1154)", "1154", "Saltuklu–Gürcü savaşları", "Ani yöresi", 40.51, 43.57, "approx", "Türkiye",
 "Gürcistan Krallığı", "Saltuklular", "İzzeddin Saltuk (esir)", "III. Giorgi", "dis", "L", "kesin",
 ["TDVIA:saltuklular", "TDVIA:ahlatsahlar"], "", "", ""),
(SAL, "Ani (1161)", "Battle of Ani (1161)", "1161-08", "Türk emîrleri–Gürcistan", "Ani", 40.51, 43.57, "known", "Türkiye",
 "Gürcistan Krallığı", "Saltuklular, Ahlatşahlar ve müttefik emîrler", "İzzeddin Saltuk, Fahrüddevle Devletşah, Ahlatşah Sökmen II", "III. Giorgi", "dis", "L", "kesin",
 ["TDVIA:saltuklular", "TDVIA:ahlatsahlar"], "",
 "Saltuk savaş başlamadan ordugâhtan ayrıldı; yenilginin sebebi buydu. Esir sayısı kaynakta 9000'dir; alınmadı.",
 "Saltuk left the camp before the battle, which caused the defeat. The source gives 9,000 prisoners; not used."),
(ILD, "Lukri", "Battle of Lori (1163)", "1163-07", "İldeniz–Gürcistan", "Lukri Kalesi yakını", 41.00, 44.40, "approx", "Ermenistan",
 "İldenizliler, Ahlatşahlar ve müttefik emîrler", "Gürcistan Krallığı", "Şemseddin İldeniz, Ahlatşah Sökmen II", "III. Giorgi", "dis", "W", "kesin",
 ["TDVIA:ildeniz-semseddin", "TDVIA:ahlatsahlar", "TDVIA:saltuklular"], "", "Bir aydan uzun süren savaşın sonunda kralın ordugâhı yağmalandı.", "After more than a month of fighting the king's camp was plundered."),
(CAK, "Koyun Adaları (deniz savaşı)", "Battle of the Oinousses (1090)", "1090", "Çaka Bey–Bizans", "Koyun Adaları, Sakız yakını", 38.51, 26.22, "approx", "Yunanistan",
 "Çaka Bey", "Bizans donanması", "Çaka Bey", "", "dis", "W", "kesin",
 ["TDVIA:caka-bey", "ROM"], "", "Adaları kurtarmaya gelen Bizans donanması yenildi; Çaka Bey'in ilk deniz zaferi.", "A Byzantine fleet sent to recover the islands was defeated; Tzachas's first naval victory."),
(CAK, "Sakız (1090)", "Battle of Chios (1090)", "1090", "Çaka Bey–Bizans", "Sakız Adası", 38.37, 26.14, "approx", "Yunanistan",
 "Çaka Bey", "Bizans", "Çaka Bey", "Konstantinos Dalassenos", "dis", "W", "ihtilafli",
 ["TDVIA:caka-bey", "ROM"], "TDVİA (Çaka Bey): Dalassenos Sakız'daki kara savaşında yenildi. Alternatif okuma: Roma veri seti (Anna Komnene) Bizans zaferi kaydeder. Karar [P6]: TDVİA.",
 "", ""),
(CAK, "Midilli (1092)", "Mytilene (1092)", "1092", "Çaka Bey–Bizans", "Midilli", 39.11, 26.56, "approx", "Yunanistan",
 "Bizans", "Çaka Bey", "Çaka Bey", "Ioannes Dukas", "dis", "L", "borderline",
 ["ROM"], "", "Yalnızca Bizans kaynaklarına dayanan Roma veri setinde var.", "Recorded only in the Roman dataset, based on Byzantine sources."),
(CAK, "Efes (1097)", "Ephesus (1097)", "1097", "Bizans'ın Ege seferi", "Efes", 37.94, 27.34, "approx", "Türkiye",
 "Bizans", "Türk beylikleri (Çaka'nın halefleri)", "", "Ioannes Dukas", "dis", "L", "borderline",
 ["ROM"], "", "Yalnızca Bizans kaynaklarına dayanan Roma veri setinde var. Haçlıların İznik'i almasından sonraki Bizans Ege seferi.",
 "Recorded only in the Roman dataset, based on Byzantine sources. Part of the Byzantine Aegean campaign after the fall of Nicaea."),
(DAN, "Kastamonu (1132)", "Kastamon (1132)", "1132", "Dânişmendli–Bizans", "Kastamonu", 41.38, 33.78, "known", "Türkiye",
 "Bizans", "Dânişmendliler", "Emîr Gazi", "Ioannes II Komnenos", "dis", "L", "kesin",
 ["TDVIA:mesud-i", "ROM"], "Tarih: TDVİA 1132, Roma veri seti 1133.", "İmparator şehri alıp esirlerle İstanbul'a döndü.", "The emperor took the town and returned to Constantinople with captives."),
(DAN, "Kastamonu (1133)", "Recapture of Kastamon (1133)", "1133", "Dânişmendli–Bizans", "Kastamonu", 41.38, 33.78, "known", "Türkiye",
 "Dânişmendliler", "Bizans garnizonu", "Emîr Gazi", "", "dis", "W", "kesin",
 ["TDVIA:mesud-i"], "", "Kuşatmada açlık baş gösterince halk kapıları açtı (527/1133).", "When hunger set in during the siege the townspeople opened the gates (527/1133)."),
(DAN, "Çankırı (1135)", "Gangra (1135)", "1135", "Dânişmendli–Bizans", "Çankırı", 40.60, 33.62, "known", "Türkiye",
 "Bizans", "Dânişmendliler", "Melik Muhammed", "Ioannes II Komnenos", "dis", "L", "kesin",
 ["TDVIA:mesud-i", "ROM"], "", "İlk kuşatma Selçuklu birliğinin ayrılmasıyla kaldırıldı; ertesi bahar Kastamonu barışla, Çankırı kuşatmayla alındı.",
 "The first siege was lifted when the Seljuk contingent withdrew; next spring Kastamon was taken peacefully and Gangra by siege."),
(DAN, "Niksar (1140)", "Siege of Neocaesarea (1140)", "1140", "Dânişmendli–Bizans", "Niksar", 40.59, 36.95, "known", "Türkiye",
 "Dânişmendliler", "Bizans, Konstantin Gabras", "Melik Muhammed", "Ioannes II Komnenos", "dis", "W", "kesin",
 ["TDVIA:danismendliler", "ROM"], "", "Dânişmendlilerin merkezini almayı amaçlayan sefer başarısız oldu.", "The campaign against the Danishmendid capital failed."),
(ZEN, "Bizâa (Buzâa, 1138)", "Siege of Buza'a (1138)", "1138-04", "Zengî–Bizans", "Bizâa", 36.40, 37.56, "approx", "Suriye",
 "Bizans", "Zengîler", "", "Ioannes II Komnenos", "dis", "L", "kesin",
 ["TDVIA:zengi-imaduddin", "ROM"], "", "Şehir emanla teslim oldu; Zengî Eylül-Ekim 1138'de geri aldı.", "The town surrendered on terms; Zengi recovered it in September–October 1138."),
(ZEN, "Halep müdafaası (1138)", "Defence of Aleppo (1138)", "1138-04-19", "Zengî–Bizans", "Halep", 36.20, 37.16, "known", "Suriye",
 "Zengîler (Halep)", "Bizans", "", "Ioannes II Komnenos", "dis", "W", "kesin",
 ["TDVIA:zengi-imaduddin"], "", "İmparator üç günlük kuşatmadan sonra başarısız ayrıldı.", "The emperor withdrew unsuccessfully after a three-day siege."),
(ZEN, "Kefertâb, Esârib ve Bizâa'nın geri alınışı (1138)", "Recovery of Kafartab, al-Atharib and Buza'a (1138)", "1138-09", "Zengî'nin Haçlılarla mücadelesi", "Kefertâb, Esârib ve Bizâa", 36.10, 37.00, "region", "Suriye",
 "Zengîler", "Antakya Prinkepsliği ve Bizans", "İmâdüddin Zengî", "", "dis", "W", "kesin",
 ["TDVIA:zengi-imaduddin"], "", "İmparatorun seferi sırasında Haçlılar'ın aldığı Kefertâb, Esârib ve Bizâa geri alındı (Muharrem–Safer 533 / Eylül–Ekim 1138). (Kontrol turunda eklendi.)",
 "Kafartab, al-Atharib and Buza'a, taken by the Crusaders during the emperor's campaign, were recovered (Sept–Oct 1138)."),
(ZEN, "Ba'lebek (1139)", "Siege of Baalbek (1139)", "1139", "Zengî'nin Suriye siyaseti", "Ba'lebek", 34.01, 36.21, "known", "Lübnan",
 "Zengîler", "Böriler (Dımaşk Atabegliği)", "İmâdüddin Zengî", "", "turk_arasi", "W", "kesin",
 ["TDVIA:zengi-imaduddin"], "", "Zengî Ba'lebek'i ele geçirip Necmeddin Eyyûb'a iktâ etti. (Kontrol turunda eklendi.)", "Zengi took Baalbek and granted it to Najm al-Din Ayyub."),
]

# turk_arasi kayıtlarda karşı taraftaki kapsam içi Türk devleti (K1: kayıt onun tablosunda da görünür)
OPP_STATE = {"Âmid (Kürboğa'ya karşı)": "Büyük Selçuklu", "Dârâ (Aksungur'a karşı)": "Büyük Selçuklu",
             "Serce (Artuklulara karşı)": "Artuklular", "Karaca Sâkî'ye yenilgi": "Irak Selçukluları", "Âmid (Dâvûd'a karşı)": "Artuklular",
             "Hama (1130)": BOR, "Humus kuşatması (1135)": BOR, "Ba'lebek (1139)": BOR, "Dımaşk'ın alınışı (1154)": BOR}

# İkinci kaynak turu (2026-10-28): kayıt adına göre ek kaynaklar ve düzeltmeler
EXTRA_SRC = {"Niksar (1140)": ["TDVIA:niksar"], "Sivas (Sebasteia)": ["ROM"], "Hârim (1164)": ["ROM"], "Suruç (I)": ["AKD:celik-2021"], "Suruç (II)": ["AKD:celik-2021"], "Şiran (Bayburt yakını)": ["AKD:celik-2021"], "Harput Kalesi'nin geri alınması": ["AKD:celik-2021"], "Azâz kuşatması (1123–24)": ["AKD:celik-2021"], "Serûc (Josselin'in esareti)": ["TDVIA:artuklular", "AKD:celik-2021"], "Turuş (Kral Baudouin'in esareti)": ["TDVIA:artuklular", "AKD:celik-2021"],
             "Menbic": ["TDVIA:menbic", "AKD:erdem-2018", "AKD:celik-2021"], "Serce (Artuklulara karşı)": ["TDVIA:artuklular"], "Josselin'e yenilgi": ["TDVIA:gaziantep"],
             "Dımaşk (1148)": ["TDVIA:nureddin-zengi-mahmud"],
             # Kaynak turu 2026-10-30
             "Hama (1130)": ["TDVIA:hama", "AKD:kucuksipahioglu-2014", "AKD:akdemir-2022"],  # Zengî savunmasız Hama'yı Eylül 1130'da aldı
             "Bire kuşatması": ["TDVIA:birecik", "AKD:kucuksipahioglu-2014", "AKD:akdemir-2022"],  # kuşatma Nasîrüddin Çakır'ın ölümü haberiyle kalktı
             "Kefertâb, Esârib ve Bizâa'nın geri alınışı (1138)": ["TDVIA:savar"],  # Savar Esârib'deki Bizans garnizonunu kılıçtan geçirdi
             "Ba'lebek (1139)": ["TDVIA:balebek", "AKD:akdemir-2022"],  # Zengî şehri alıp Eyyûb'u vali yaptı
             "Esârib'in fethi": ["AKD:akdemir-2022"],  # 1130'da Haçlılar'daki Esârib Kalesi alındı
             "Âmid (Dâvûd'a karşı)": ["AKD:kucuksipahioglu-2014"],  # Zengî 1134 baharında Âmid'i almaya çalıştı
             "Suruç (1145)": ["AKD:kucuksipahioglu-2014", "AKD:akdemir-2022"],  # 1145'te Suruç alındı
             "Pons'un yenilgisi (1137)": ["AKD:kucuksipahioglu-2014"],  # Trablus kontu Pons 1137'de öldürüldü
             "Banyas (1164)": ["AKD:altan-2014"],  # Artâh zaferinin ardından Hârim (Ağustos) ve Banyas (Ekim–Kasım 1164)
             "Bilbîs (1164)": ["AKD:altan-2014"],  # Şîrkûh Bilbîs'i aldı; Kudüs kralı yardıma geldi
             "Mısır'ın alınışı (1169)": ["AKD:altan-2014"],  # Amaury 2 Ocak 1169'da çekildi; Şîrkûh 8 Ocak'ta Kahire'ye girdi, vezir oldu
             "Kilikya (Mleh'e destek)": ["AKD:turan-2017"]}  # Mleh Nûreddin'e sığındı, Misis, Adana ve Tarsus'u aldı
FIX = {"Suruç (I)": {"date": "1101", "dispute": "Tarih: Belek maddesi 1100 verir; Sökmen maddesi tarih vermez. Çelik (2021) iki Suruç çarpışmasını da 1101'e koyar; burada Çelik'e uyuldu."},
       "Azâz kuşatması (1123–24)": {"status": "kesin", "note": "Belek komutasındaki kuvvetler kaleyi kuşattı; Joscelin'in yardıma gelmesi ve garnizonun huruç hareketi üzerine Belek iki ateş arasında kalmamak için çekildi (Çelik 2021).", "note_en": "Forces under Belek besieged the castle; when Joscelin came to its relief and the garrison sallied, Belek withdrew to avoid being caught between them (Çelik 2021)."},
       "Serce (Artuklulara karşı)": {"date": "1130", "note": "Dâvûd ve Timurtaş yenilip Serce ile Dârâ'yı Zengî'ye bıraktı (Artuklular maddesi). Kaynaktaki sayılar (20.000 Türkmene karşı 4000) alınmadı.",
                                     "note_en": "Dawud and Timurtash were defeated and ceded Serce and Dara to Zengi (Artuqids article). The source figures (4,000 against 20,000 Turkmens) are not used."},
       "Josselin'e yenilgi": {"date": "1149/1150", "dispute": "Tarih: Gaziantep maddesi 1149; Nûreddin maddesi yenilgiyi Josselin'in Mayıs 1150'de teslim alınmasından önceye koyar."},
       "Bire kuşatması": {"dispute": "Birecik maddesi kuşatmayı Urfa'nın fethiyle aynı yıla (1144) koyar; Zengî maddesine göre 1145."},
       "Ba'lebek (1139)": {"dispute": "Ba'lebek maddesi Zengî'nin şehri 1136'da aldığını yazar; Zengî maddesi ve Akdemir (2022) kuşatmayı 1139'a koyar."},
       "Kilikya (Mleh'e destek)": {"dispute": "Turan (2017, Runciman'a dayanarak) Mleh'in Çukurova akınını 1170'e koyar; kayıttaki 1173 yaklaşıktır."},
       "Menbic": {"dispute": "Menbic maddesi Belek'in Safer 518 / Nisan 1124'te Menbic'e geldiğini yazar; savaş Belek maddesine göre 5 Mayıs 1124'tedir."}}

LEFT = [
 {"name": "Pilottan taşınan kayıtlar", "reason": "Büyük Selçuklu pilotundaki Sivas 1070 (#28), Kahire 1077 (#37) ve Harran 1104 (#59) K3 gereği bu partiye taşındı.", "source": "TDVIA:afsin"},
 {"name": "İlgazi'nin 1120 seferi", "reason": "TDVİA yalnızca 'başarılı mücadeleler' der; adı ve yeri belli bir savaş yok.", "source": "TDVIA:ilgazi-necmeddin"},
 {"name": "Emîr Gazi'nin 1119 Antakya akını", "reason": "Ager Sanguinis ile karışmış olabilir; ayrıca doğrulanmadı.", "source": "TDVIA:danismendliler"},
 {"name": "Dânişmendli–Anadolu Selçuklu savaşları", "reason": "Anadolu Selçuklu partisinde Türk devletleri arası olarak kayıtlı; burada tekrar edilmedi. Dânişmendli tablosu bu kayıtlardan da hesaplanmalı.", "source": "TDVIA:danismendliler"},
 {"name": "İldenizli ve Ahmedîlî iç mücadeleleri (Sâve 1161 vb.)", "reason": "Irak Selçuklu taht mücadelesinin parçası; Irak Selçukluları partisinde ele alınacak.", "source": "TDVIA:ildeniz-semseddin"},
 {"name": "Didgori 1121", "reason": "Pilotta Irak Selçukluları'na yazılı (K3: komutanı sultan atadı).", "source": "TDVIA:ilgazi-necmeddin"},
]

pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
moved = {p["id"]: p for p in pilot["battles"] if p["id"] in (28, 37, 59)}
recs = []
def add(rec):
    rec["id"] = len(recs) + 1
    recs.append(rec)

for pid, st in ((28, "Er Basgan"), (37, ATS), (59, ART)):
    p = dict(moved[pid]) if pid in moved else None
    if p is None:  # pilot zaten temizlendiyse taşınmış kayıt bu dosyada duruyor
        continue
    p["state"], p["home_batch"] = st, HB
    p["note"] = p["note"].split(" [K3]")[0] + " [K3] Sultan göndermedi; kendi adına hareket etti."
    p["note_en"] = p["note_en"].split(" [K3]")[0] + " [K3] Not sent by the sultan; acted on his own account."
    if pid == 59:
        p["side_a"] = "Artuklular (Sökmen), Musul (Çökürmüş)"
    add(p)

for r in R:
    (st, ntr, nen, date, war, place, lat, lon, loc, country, sa, sb, tc, oc, cat, res, status, src, disp, note, note_en) = r
    src = src + [x for x in EXTRA_SRC.get(ntr, []) if x not in src]
    rec = {"name_tr": ntr, "name_en": nen, "date": date, "hijri": "", "type": "land", "war": war, "place": place,
           "lat": lat, "lon": lon, "loc": loc, "country": country, "side_a": sa, "side_b": sb, "turkic_cmd": tc, "opp_cmd": oc,
           "category": cat, "result": res, "status": status, "sources": src,
           "verify": {"tdvia": True, "tdvia2": len([s for s in src if s.startswith("TDVIA:")]) >= 2, "wp": False, "rom": False, "academic": False},
           "state": st, "home_batch": HB}
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    if ntr in OPP_STATE: rec["opp_state"] = OPP_STATE[ntr]
    rec.update(FIX.get(ntr, {}))
    rec["verify"]["rom"] = "ROM" in rec["sources"]
    rec["verify"]["academic"] = any(x.startswith("AKD:") for x in rec["sources"])
    rec["verify"]["tdvia"] = any(x.startswith("TDVIA:") for x in rec["sources"])
    add(rec)

out_path = root / "data" / "beylikler-atabeylikler.json"
if not moved and out_path.exists():  # yeniden üretimde taşınmış kayıtları eski çıktıdan al
    old = json.loads(out_path.read_text(encoding="utf-8"))
    carried = [b for b in old["battles"] if b["name_tr"] in ("Sivas (Sebasteia)", "Kahire", "Harran")]
    recs = carried + recs[:]
    for i, r in enumerate(recs, 1): r["id"] = i

meta = {"batch": "Parti 3 — Türk beylikleri ve atabeylikleri (1070–1175)", "compiled": "2026-10-28",
        "status": "İlk tur. Kayıtlar hükümdar ve hanedan maddelerinden derlendi.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
out_path.write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")

# Pilot dosyasından taşınan kayıtları çıkar
if moved:
    pilot["battles"] = [p for p in pilot["battles"] if p["id"] not in moved]
    pilot["left_out"].append({"name": "Sivas 1070, Kahire 1077, Harran 1104",
                              "reason": "K3 gereği Parti 3'e (beylikler ve atabeylikler) taşındı; data/beylikler-atabeylikler.json.",
                              "source": "TDVIA:afsin"})
    (root / "data" / "pilot-buyuk-selcuklu.json").write_text(json.dumps(pilot, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli; pilotta", len(pilot["battles"]), "kayıt kaldı")
