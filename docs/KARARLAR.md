# Karar Günlüğü

Projenin seyrini etkileyen her karar buraya **tarih ve gerekçesiyle** yazılır. Bir karar değişirse eski karar silinmez, "yerine geçti" notu düşülür.

## Proje kararları
| # | Tarih | Karar | Gerekçe |
|---|---|---|---|
| P1 | 2026-10-25 | Önce araştırma ve doğrulama, arayüz sonra | Kullanıcı talebi; verinin kalitesi önce gelir |
| P2 | 2026-10-25 | Kapsam: ana hat devletleri (Göktürk → … → TC) | Kullanıcı seçimi; tahminen 1.500–2.500 savaş |
| P3 | 2026-10-25 | İki dilli (TR/EN), tek veri seti | Kullanıcı seçimi; uluslararası paylaşılabilirlik |
| P4 | 2026-10-25 | Temel referans TDVİA; Wikipedia yalnızca kapsam kontrolü için | Önyargısız ve kaynakçalı temel; bkz. METODOLOJI §4 |
| P5 | 2026-10-25 | Orijinal sitenin kodu ve verisi kopyalanmaz, yalnızca yöntemi örnek alınır | Orijinal sitede lisans belirtilmemiş |
| P6 | 2026-10-28 | Kaynaklar çatıştığında Türk ve İslâm tarafının akademik literatürü (TDVİA, sonra Türk akademisyenler) esas alınır; karşı tarafın anlatısı "alternatif okuma" olarak kayıtta kalır. K4'teki karşı taraf kuralının yerine geçer | Kullanıcı tercihi. Şeffaflık korunuyor: alternatif okuma her kayıtta görünür |
| P8 | 2026-10-28 | Yalnızca karşı taraf kaynağına (Roma veri seti) dayanan savaş, Türk kaynaklarında aykırı bilgi yoksa `borderline` olarak kayda alınır; notunda Türk kaynağı bulunamadığı yazılır | Bizans kaynaklarında iyi belgelenmiş savaşların (Hyelion 1177 vb.) haritada eksik kalmaması |
| P9 | 2026-10-28 | Bağımsız akademik kontrol için Türk hakemli dergileri (DergiPark, İSAM) kullanılır; atıf anahtarı `AKD:<yazar-yıl>` | P6 ile uyumlu; Encyclopaedia Iranica erişime kapalı (403) |
| P7 | 2026-10-28 | Haritada devlet sınırları, kaynaklı bir "bölge → sahip" tablosundan üretilir; hazır tarihî sınır setleri (historical-basemaps vb.) kullanılmaz | Hazır setler bu dönem için hatalı (ör. 1200 haritasında 1062'de yıkılan Büveyhîler) ve GPL-3 lisanslı |

## Yöntem kararları
| # | Tarih | Karar | Gerekçe |
|---|---|---|---|
| K1 | 2026-10-25 | Üç kategori (`dis`, `turk_arasi`, `ic`). Kazanma-kaybetme tablosu her devlet için ayrı tutulur; "Türkler toplamı" yalnızca `dis` kategorisinden hesaplanır | Dandanakan gibi Türk devletleri arası savaşlar hem görünür kalsın hem de toplamı şişirmesin |
| K2 | 2026-10-25 | Selçuklu hanedanının kolları arasındaki savaşlar `ic` sayılır; farklı hanedanlardan Türk devletleri arası savaşlar `turk_arasi` sayılır | Romalılar sitesinin halef devletleri tek devlet sayma yaklaşımıyla tutarlı |
| K3 | 2026-10-25 | Sultan emrettiyse veya komutanı atadıysa savaş sultanın devletine yazılır; emîr kendi inisiyatifiyle savaştıysa kendi beyliğine | Her savaşın tek ve savunulabilir bir sahibi olsun |
| K4 | 2026-10-25 | İki madde kuralı, sayı kuralı, zayıf ikincil kaynak kuralı, karşı taraf kuralı | Pilotta ortaya çıkan sorunlar; bkz. METODOLOJI §4. *Karşı taraf kuralı 2026-10-28'de P6'nın öncelik kuralıyla yer değiştirdi.* |

## Kayıt kararları (Pilot 1: Büyük Selçuklu)
| Kayıt | Karar | Alternatif okuma |
|---|---|---|
| Pasinler 1048 (#11) | ~~Belirsiz (D)~~ → **Selçuklu zaferi (W)** (P6, 2026-10-28; TDVİA'nın dört maddesi) | Skylitzes, Kaldellis, Beihammer: belirsiz |
| Talhâb 1038 (#2) | Selçuklu zaferi, 1038 | TDVİA Dandanakan maddesi: 1039 yenilgisi |
| Gence 1046/47 (#9) | TDVİA'ya göre başarısız kuşatma | Wikipedia: Liparit'e karşı zafer (zayıf kaynak) |
| Debîl 1045/46 (#8) | Kutalmış'ın zaferi, ihtilaflı olarak işaretli; P6 gereği kayıtta kalır | Bizans kaynakları zaferi Şeddâdîlere atfediyor |
| Konya 1069 (#27) | ~~Bizans zaferi (L)~~ → **Selçuklu akını başarılı (W)**, borderline (P6, 2026-10-28) | Attaleiates: akıncılar dönüşte Manuel Komnenos'a yenildi |
| Partskhisi (#35) | Tarih 1074 → **1076–1079** (P6; TDVİA Melikşah maddesi) | Gürcü kaynakları: 1074 |
| İsfahan 1050–51 (#13) | kesin → borderline: TDVİA İsfahan maddesine göre şehir "sulhen" teslim alındı | — |
| Gence 1110 (#66) | borderline → kesin: TDVİA Gence maddesi David'in bozguna uğratıldığını yazar | — |
| Urfa 1070 (#29) | Kuşatma kaldırıldı, savunan kazandı (haraç alındığı notta) | Selçuklu başarısı |
| Habur 1107 (#60) | İç savaş (K2) | Türk devletleri arası |
| Didgori 1121 (#75) | Irak Selçukluları'na yazıldı (K3: komutanı Sultan Mahmud atadı) | Artuklu savaşı |
| Sivas 1070, Kahire 1077, Harran 1104 (#28, 37, 59) | Atabeylikler ve beylikler partisine taşınacak (K3) | Büyük Selçuklu |
| Hârizmşahlar, Karluklar | Rakip (`dis`) | Kapsam genişlerse `turk_arasi` |

## Kayıt kararları (Parti 2: Anadolu Selçukluları, 2026-10-28)
| Kayıt | Karar | Alternatif okuma |
|---|---|---|
| Akşehir (Philomelion) 1116 | Belirsiz (D); TDVİA yenilgiden söz etmez | Anna Komnene: Bizans zaferi |
| Konya önleri 1146 | Selçuklu zaferi (P6) | Kinnamos: barışı sultan istedi |
| Menderes ve Honaz 1148 | Selçuklu başarısı, borderline | Batı kaynakları: Menderes geçişinde Fransız başarısı |
| Konya 1190 | Yenilgi, ihtilaflı (şehir Haçlıların eline geçti) | TDVİA: meydan savaşından kaçınıldı |
| Tarsus 1245–46 | Kural gereği yenilgi; lehte antlaşma notta | Selçuklu başarısı |
| Elbistan 1277 | Borderline; Memlükler dış rakip | Selçuklu taraf sayılmaz |
| Karaman, Cimri, Germiyan | İç savaş | Türk devletleri arası |
| Harita, 1243 sonrası | Anadolu, Moğol metbûluğuna rağmen Anadolu Selçuklu renginde | Moğol rengi |

## Kayıt kararları (Parti 3: beylikler ve atabeylikler, 2026-10-28)
| Kayıt | Karar | Alternatif okuma |
|---|---|---|
| Sivas 1070, Kahire 1077, Harran 1104 | Pilottan Parti 3'e taşındı (K3) | Büyük Selçuklu |
| Bâbeyn 1167 | Zengîlere yazıldı (Şîrkûh, Nûreddin'in komutanı) | Eyyûbî |
| Şiran 1120 | Dış rakip (Trabzon dükü Gabras) | Türk devletleri arası (Mengücüklüler) |
| Zengî–Artuklu, Zengî–Irak Selçuklu, Artuklu–Büyük Selçuklu | Türk devletleri arası | İç savaş |

## Kayıt kararları (Parti 5: Osmanlı kuruluş dönemi, 2026-10-28)
| Kayıt | Karar | Alternatif okuma |
|---|---|---|
| Kosova 1389 | Osmanlı zaferi (P6) | Tvrtko ve bazı Batı kaynakları: Türk yenilgisi |
| Argeş (Rovine) 1395 | Osmanlı zaferi (P6) | Romen kaynakları: Mircea'nın zaferi |
| Ankara 1402 | Dış rakip (Timurlular kapsam dışı) | Türk devletleri arası |
| Osmanlı–Karaman, Kadı Burhâneddin, Eretna | Türk devletleri arası | İç savaş |

## Kayıt kararları (Parti 6: Osmanlı 1402–1481, 2026-10-29)
| Kayıt | Karar | Alternatif okuma |
|---|---|---|
| İzlâdi 1443 | ~~Osmanlı başarısı~~ → belirsiz (D), 2026-10-29: TDVİA'nın Varna ve Macaristan maddeleri çelişiyor | Batı kaynakları: Kunoviçe'de Haçlı başarısı |
| Eflak 1462 | Osmanlı başarısı (P6) | Vlad'ın gece baskını |
| Otlukbeli 1473 | Dış rakip (Akkoyunlular kapsam dışı) | Türk devletleri arası |
| Fetret şehzade savaşları | İç savaş | — |

## Kayıt kararları (Parti 7: Osmanlı 1481–1520, 2026-10-29)
| Kayıt | Karar | Alternatif okuma |
|---|---|---|
| Çaldıran ve diğer Safevî savaşları | Dış rakip (Safevîler kapsam listesinde değil) | — |
| Mercidâbık, Gazze, Ridâniye | Dış rakip (Memlükler kapsam dışı Türk devleti) | Türk devletleri arası |
| Turnadağ 1515 | Türk devletleri arası (Dulkadıroğulları) | — |

## Kayıt kararları (Parti 8: Osmanlı 1520–1566, 2026-10-29)
| Kayıt | Karar | Alternatif okuma |
|---|---|---|
| Güns 1532 | Osmanlı başarısı, ihtilaflı | Batı kaynakları: sembolik teslim |
| Cerbe 1560 | Deniz savaşı ve kale kuşatması ayrı kayıt | — |

## Kayıt kararları (Parti 9: Osmanlı 1566–1606, 2026-10-29)
| Kayıt | Karar | Alternatif okuma |
|---|---|---|
| Kanije 1600 | 20 Ekim (Kanije maddesi) | Mehmed III maddesi: 22 Ekim |
| Eflak seferi 1595 | Tek kayıt, borderline | Kalugareni ve Yergöğü ayrı savaşlar (Batı kaynakları) |
| İstolni Belgrad 1602 | Ağustos 1602, ihtilaflı (TDVİA içi çelişki) | 22 Şubat 1603 |

## Kayıt kararları (Parti 10: Osmanlı 1603–1640, 2026-10-29)
| Kayıt | Karar | Alternatif okuma |
|---|---|---|
| Hotin 1621 | Belirsiz (D) | Batı kaynakları: Leh zaferi |
| Estergon 1605 | Ekim 1605, ihtilaflı (TDVİA içi) | 3 Ekim / 4 Kasım |

## Kayıt kararları (Parti 11: Osmanlı 1640–1683, 2026-10-29)
| Kayıt | Karar | Alternatif okuma |
|---|---|---|
| Saint Gotthard 1664 | Yenilgi | Fâzıl Ahmed Paşa maddesi: tam bozgun değil |
| Kandiye 1647–1669 | Tek kayıt (teslim tarihi) | — |

## Kayıt kararları (Parti 13: Osmanlı 1718–1774, 2026-10-29)
| Kayıt | Karar |
|---|---|
| Nâdir Şah ve Afşarlar | Türk hânedanı ama kapsam listesinde yok → `dis`, haritada `turk-diger` |
| Sakız Boğazı 1770 | Belirsiz (D) |
| Kartal 1770 | Borderline (TDVİA'da yalnızca anılıyor) |

## Kayıt kararları (Parti 14: Osmanlı 1774–1812, 2026-10-29)
| Kayıt | Karar |
|---|---|
| Kölemen beyleri, Pazvandoğlu | Osmanlı yöneticileri ve âyanı → `ic` |
| Sırp isyancıları (Kara Yorgi) | `dis` (Mora Rumları 1770 gibi) |
| Yılan Adası 1788 | TDVİA'ya göre W; Batı okuması `dispute`'ta |
| Kaçarlar, Azerbaycan hanlıkları | Türk hânedanları ama kapsam dışı → haritada `turk-diger` |
| Kırım Hanlığı | Osmanlı ordusuyla birlikte ya da padişah emriyle yaptığı savaşlar Osmanlı tablosuna borderline girer; kendi başına yaptıkları dışarıda (2026-10-29, kullanıcı itiraz etmedi) |

## Kayıt kararları (Parti 15: Osmanlı 1812–1839, 2026-10-29)
| Kayıt | Karar |
|---|---|
| Mehmed Ali Paşa savaşları (1831–1839) | Osmanlı valisinin isyanı → `ic` |
| Vehhâbî seferi | Mısır kuvvetleri Osmanlı tarafı; Dir‘iye Emirliği `dis` |
| Kostantîne 1836–37 | İlk turda borderline; ikinci turda kesin (Kostantîne ve Abdülkādir el-Cezâirî maddeleri) |

## Kayıt kararları (Parti 16: Osmanlı 1839–1878, 2026-10-29)
| Kayıt | Karar |
|---|---|
| Suriye 1840 (Beyrut, Akkâ) | Mehmed Ali isyanının devamı → `ic`; kazanan taraf "Osmanlı Devleti, İngiltere ve Avusturya" |
| Kırım Savaşı müttefik harekâtı (Sivastopol) | Osmanlı birlikleri katıldığı için kayıt; taraf "İngiltere, Fransa, Osmanlı Devleti ve Piyemonte" |
| Sinop 1853 | Tek TDVİA maddesi "1854 başları" der; 30 Kasım 1853 tarihi kullanıldı, fark `dispute`'ta |
| Girit, Hersek ve Sırp isyancıları, Karadağ | `dis` (önceki partilerle aynı) |
| Asîr emîri Muhammed b. Âiz | Osmanlı kaymakamlığı verilmişti → `ic` |
| Yemen (San‘a 1872) | Osmanlı'nın yeniden fethi → `dis` |
| Ziştovi 1877, Edirne 1878 | Ciddi direniş yok → borderline |
| Bosna 1878 | Berlin'den sonra; devlet savaşmadı → dışarıda |
| Tarih takvimi | TDVİA'nın verdiği tarih kullanıldı (93 Harbi tarihlerinin bir kısmı Rumî/Jülyen olabilir); fark not edilmedi |

## Kayıt kararları (Parti 17: Osmanlı 1878–1912, 2026-10-29)
| Kayıt | Karar |
|---|---|
| Arnavut bağımsızlık yanlıları, İmam Yahyâ, İdrîsî | Osmanlı tebaasının isyanı → `ic` |
| Otuzbir Mart 1909 | Ordu içi çatışma → `ic`, borderline |
| Tellülkebîr 1882 | Urâbî'nin Mısır ordusu; padişah desteklemedi → dışarıda |
| Mısır 1882 sonrası haritada | Fiilî yöneten İngiltere gösterilir |

## Kayıt kararları (Parti 18: Balkan Savaşları 1912–1913, 2026-10-30)
| Kayıt | Karar |
|---|---|
| Selânik 1912, Edirne ve Yanya 1913, adaların işgali | Muharebesiz teslim ve çıkarma ile işgaller de yenilgi (`L`) sayıldı; Rodos 1912 örneğine uyuldu |
| Edirne'nin geri alınışı 1913 | Mukavemet görülmedi → borderline; tarih 21 Temmuz (üç madde), Enver maddesindeki 22 Temmuz `dispute` |
| Edirne 1913 savunması | Balkan Savaşı maddesindeki "Yanya'yı, Mehmed Şükrü Paşa'nın kahramanca savunmasına rağmen, Bulgarlar ... Edirne'yi" cümlesi Şükrü Paşa'ya Edirne savunmasını verir; Yanya maddesi Yanya'yı Esad Paşa'nın savunduğunu yazar |
| Yenice-i Vardar 1912 | Madde 11 Kasım der; Batı literatürü 1–2 Kasım → tarih ay düzeyinde, `dispute` |
| Edirne haritada | 26 Mart–21 Temmuz 1913 Bulgar işgali yıl çözünürlüğünde gösterilmez |
| Bâbıâli Baskını | Hükümet darbesi; muharebe değil → dışarıda |

## Kayıt kararları (Parti 19: Birinci Dünya Savaşı 1914–1918, 2026-10-30)
| Kayıt | Karar |
|---|---|
| Şerîf Hüseyin isyanı (Medine, Mekke, Bi'riali, Tâif) | Mekke emîrinin isyanı; Müslüman vali/emîr isyanı kuralı → `ic`, sonuç `C` |
| Arıburnu ve Seddülbahir çıkarmaları (25 Nisan 1915) | Çıkarma kuvvetleri kıyıda tutundu; Türk okumasıyla (P6) ilerleyiş durdurulduğu için `W`, `dispute` notuyla |
| Zığındere | Madde sonuç vermez → `D` |
| Kerevizdere | İkinci turda Çakmak maddesi mevzilerin başarıyla savunulduğunu yazdığı için `W` |
| Bitlis'in kurtarılışı 1916 | Madde yalnızca işgalin sona erdiğini yazar → borderline |
| Ermeni kuvvetleri (1918) | Rus ordusu çekildikten sonra karşı taraf; `dis` |
| Sarıkamış kayıpları | Enver Paşa maddesindeki 90.000 rakamı Sarıkamış Harekâtı maddesince düzeltilir → `dispute` |
| Karadeniz baskını 1914 | Osmanlı donanmasını Alman Amiral Souchon yönetti; Osmanlı kaydı sayıldı |
| Musul (Kasım 1918), Medine'nin teslimi (1919) | Mütarekeden sonra → dışarıda |
| Şam ve Halep 1918 haritada | Faysal'ın Arap yönetimi Hâşimî (hicaz) rengiyle gösterilir |

## Kayıt kararları (Parti 20: Millî Mücadele 1919–1922, 2026-10-30)
| Kayıt | Karar |
|---|---|
| Devlet alanı (`state`) | "TBMM Hükümeti (Millî Mücadele)"; 1919 kayıtlarında taraf "Kuvâ-yi Milliye", 1920 sonrası "TBMM Hükümeti" |
| Anzavur, Düzce, Delibaş/Bozkır, Yozgat isyanları, Çerkez Ethem | Müslüman tebaanın Ankara'ya karşı isyanı → `ic`, sonuç `C` |
| Akbaş baskını 1920 | Cephanelik baskını; muharebe değil → borderline |
| Sakarya | Tarih maddenin verdiği bitiş günü (12 Eylül 1921); "üç hafta süren" notta |
| Antep savunması | Madde sonucu (teslim) açıkça yazmadığından dışarıda; ikinci kaynakla eklenecek |
| Harita | TBMM Hükümeti 1920'den itibaren ayrı renk (yeşil); İstanbul ve Gelibolu 1922'ye kadar Osmanlı |
| Lahsâ | 8 Temmuz 1913'te İbn Suûd'a geçti (Lahsâ maddesi) → harita düzeltildi |

## Kayıt kararları (Parti 21: Göktürkler, Türgişler, Karluklar ve Uygurlar 552–911, 2026-10-30)
| Kayıt | Karar |
|---|---|
| Kaynak | TDVİA'da Göktürk maddesi yok; olaylar Asya, Uygurlar, Dokuz Oğuzlar, Karluklar, Yabgu, Tohâristan, Talas Savaşı, Semerkant, Mâverâünnehir, Hazarlar, Kırgızlar, Turfan, Fergana ve Emevî valileri maddelerinden derlendi |
| Kapsam | Göktürk (doğu ve batı), Türgiş, Karluk ve Uygur kağanlıkları ile 840 sonrası Kan-chou Uygurları; Hazar, Avar, Tuna Bulgar, Hun ve Akhun devletleri bu partiye alınmadı (ayrı kapsam kararı bekliyor) |
| Akhunlar | TDVİA Akhunlar'ı Halaç Türkleri olarak anar → Akhun yıkılışı `turk_arasi` |
| Oğuz, Tatar ve Bayırku savaşları | Kağanlığa bağlı boyların isyanı → `ic` |
| Ozmış'ın yenilgisi 743, Basmıl 745, Uygur'un yıkılışı 840 | Türk toplulukları arası → `turk_arasi` |
| Tiflis 627–629 | Batı Göktürk'e bağlı Hazarlar'ın Bizans müttefiki olarak yaptığı sefer → Batı Göktürk kaydı |
| İkinci Göktürk'ün kuruluşu 682 | Tek bir muharebe adı yok → borderline |
| Talas 751 | Karluklar'ın kaydı (Abbâsîlerle birlikte) |
| Harita 550–1000 | Kaba katman (`tools/extend_borders_552.py`); bütün dilimler `yaklasik`; Ötüken noktası eklendi |

## Hicrî tarihler (2026-10-30)
| Konu | Karar |
|---|---|
| Kaynak | Hicrî tarih hesaplanmaz; yalnızca kaydın TDVİA maddesinde "<hicrî> / <miladî>" biçiminde yan yana yazılmış ve miladî kısmı kaydın tarihiyle uyuşan ifade alınır (`tools/fill_hijri.py` → `data/hicri.json`). |
| Kesinlik | Çıktı kaydın kesinliğini aşmaz: yalnız yılı bilinen kayda hicrî yıl, ayı bilinene ay ve yıl, günü bilinene gün de uyuşuyorsa tam tarih. |
| Gösterim | `build_demo.py` kaydın kendi `hijri` alanı boşsa bu dosyadaki değeri kullanır. |

## Kapsam kararları (2026-10-30)
| Konu | Karar |
|---|---|
| Türkistan hanlıkları | Kullanıcı onayı: Hokand, Buhara, Hîve, Kazak ve Türkmen direnişinin Rus işgaline karşı savaşları girer (Parti 22) |
| Erken Türk devletleri | Kullanıcı onayı: Asya ve Avrupa Hunları, Akhunlar, Avarlar, Hazarlar, Tuna Bulgarları, Peçenekler, İdil Bulgarları ve Kırgızlar ayrı partiler olarak girer. Sıra: TDVİA maddesi olanlar önce (Hazar, Peçenek, İdil Bulgar, Kırgız), akademik kaynak gerektirenler sonra (Hun, Akhun, Avar, Tuna Bulgar) |

## Kayıt kararları (Parti 22: Türkistan hanlıkları ve Rus istilâsı 1837–1881, 2026-10-30)
| Kayıt | Karar |
|---|---|
| Devletler | Hokand Hanlığı, Buhara Emirliği (Mangıtlar), Hîve Hanlığı, Kazaklar (Kenesarı), Türkmenler (Teke) |
| Rusya'ya karşı bütün savaşlar | `dis` |
| Mey-Tuble c. 1847 | Ruslar'ın kışkırttığı Kırgız baskını → `turk_arasi`, Kazak mağlubiyeti |
| Irgız ve Turgay 1838, Karatav 1845 | Muharebe adı yok → borderline |
| Çimkent 1864 | İki kayıt: 7 Temmuz hücumu püskürtüldü (W); on sekiz günlük savunmadan sonra teslim (L) |
| Hucend 1866 | Hucend maddesine göre Buhara'nın elindeydi → Buhara kaydı, `dispute` notuyla |
| Merv 1884, Mergīnân 1875, Evliyaata 1864 | Muharebe anlatılmıyor → dışarıda |
| 1916 isyanı ve Basmacılar | Hanlıkların yıkılışından sonra → dışarıda (ayrı kapsam) |

## Kayıt kararları (Parti 23: Hazarlar, Peçenekler, İdil Bulgarları ve Kırgızlar 652–1361, 2026-10-30)
| Kayıt | Karar |
|---|---|
| Parti yapısı | TDVİA maddesi olan dört topluluk tek partide; Hun, Akhun, Avar, Tuna Bulgar sonraki partide (akademik kaynak) |
| Hazar–Arap savaşları | Râşid halifeler, Emevîler ve Abbâsîler'e karşı → `dis` |
| Büyük Bulgarya c. 665, Peçenekler 889, Uzlar 1065, Pulat Timur 1361 | Türk toplulukları arası → `turk_arasi` |
| Rus istilâsı 964 | İki madde çelişir → ihtilaflı; P6 gereği Türk kaynağına (İdil Bulgar Hanlığı) göre W |
| Balkan akını 1048–49, Rus istilâsı 985 | Akın veya ayrıntısız savunma → borderline |
| Yılı vermeyen olaylar | `c.` önekiyle yaklaşık yıl ve `dispute` notu (Büyük Bulgarya, Mervân, Silistre) |
| Kiev 968, Hazar akını 799 | Sonuç yok → dışarıda |
| Kıpçaklar | Kapsam listesinde yok → dışarıda; kullanıcıya sorulacak |

## Kayıt kararları (Parti 24: Avrupa Hunları, Akhunlar, Avarlar ve Tuna Bulgarları 427–834, 2026-10-30)
| Kayıt | Karar |
|---|---|
| Kaynak | TDVİA'da müstakil madde yok; Avrupa Hunları için Türkçe akademik yayınlar (Erkoç, Yurdakul, Dıngıl Ilgın) birincil kaynak sayıldı |
| Tuna Bulgarları | 864 (Hıristiyanlığın kabulü) öncesi alındı; sonrası Slavlaşma gerekçesiyle kapsam dışı |
| Asya Hunları | MÖ yılları için şema (negatif yıl) ve zaman çizelgesi değişikliği gerekir; arayüz turunda karar verilecek |
| Katalaunum 451 | Türk yazarlara göre (P6) sonuç `D`, ihtilaflı |
| Edirne kuşatması 586 | Sonuç verilmez → `D`, borderline |
| Kutrigur–Utigur 482, Krum'un Avar seferi 805 | `turk_arasi` (805'te `opp_state` Avar) |
| Akhun kayıtları | Sâsânî ve Emevîlere karşı → `dis`; Nîzek 709 Akhun kaydı sayıldı (TDVİA "Eftalit prensi") |
| Parti 23 ek | Bulgar maddesi Samara 1223, Bulgar 1236 ve Pulat Timur 1361 için ikinci kaynak oldu |

## Kayıt kararları (Parti 25: Kıpçaklar / Kumanlar 1103–1239, 2026-10-30)
| Kayıt | Karar |
|---|---|
| Kapsam | Kullanıcı onayı ("Ekle", 2026-10-30) |
| Başka partilerdeki Kıpçak muharebeleri | Tekrar kayıt açılmadı; Levunion 1091'de `side_a` "Bizans ve Kumanlar" yapıldı |
| Asen ve Petar 1186–87 | Kuman ordusu yardımcı kuvvet → borderline, Kıpçak kaydı |
| Kalka 1223 | Kıpçak–Rus ittifakı yenildi → Kıpçak kaydı, `dis` |

## Arayüz turu 1 (kullanıcı geri bildirimi, 2026-10-30)
| Konu | Karar |
|---|---|
| MÖ tarihler | Kapsam dışı (kullanıcı: "Milattan önce tarihlere gitmeye gerek yok"); Asya Hunları alınmaz |
| Sınır lejantı | Yalnız seçili yılda haritanın görünen kısmında toprağı olan devletler; Türk / diğer olarak iki bölüm, bölge sayısına göre sıralı, ilk 10 + 8 gösterilir, gerisi "+N devlet daha" ile açılır. Lejant öğesinin üstüne gelince devletin bölgeleri haritada öne çıkar |
| Renkler | `sinirlar.json` rengi esastır; görünen iki devletin rengi çok yakınsa (Lab uzaklığı < 20, komşu olmayanlarda gevşek) sonraki devlete kendi grubunun paletinden en ayırt edici renk verilir; atanan renk oturum boyunca hatırlanır. Lejant kareleri haritadaki saydamlıkla aynı tonda çizilir |
| Savaş listesi filtreleri | Arama (ad, yer, harp, taraflar, komutanlar), Türk devleti (Türk devletleri arası savaşlarda `opp_state` de eşleşir), rakip (ilk ada göre gruplanır, metin içinde aranır), yıl aralığı (harita kaydırıcılarıyla eş), sonuç, kategori, tür. Filtreler haritaya ve istatistik kartlarına da uygulanır; harita üstünde etkin filtreler ve "temizle" bağlantısı görünür |
| Liste uzunluğu | 100'er satır gösterilir, "daha göster" ile genişler; "Türk devleti" sütunu eklendi |
| Eskimiş sınır dilimleri | 1923'e uzanan son dilimler güncellendi (`tools/fix_borders_modern.py`): Habsburg mirası 1918, Sırp-Hırvat-Sloven Krallığı, Polonya, Sovyet dönemi, Kalmukların Rusya'ya bağlanması 1771, Afganistan 1826, Çin Cumhuriyeti 1912 |

## İkinci kaynak turu, Parti 22–25 (2026-10-30)
| Kaynak | Desteklediği kayıtlar |
|---|---|
| Tansü ve Özdemir 2017 (`AKD:tansu-ozdemir-2017`) | Lebedev 1843, Kenesarı 1844, Karatav 1845, Mey-Tuble 1847 (yıl akademik kaynağa göre 1847) |
| TDVİA Endican | Endican 1876 |
| Uçar 2021 (`AKD:ucar-811`) | Sofya 809, Nikephoros 811, Edirne 813 |
| Çelik 2013 (`AKD:celik-2013`) | Mercülhicâre 722–723, Nehrürrân ve Belencer 722, İrmîniye 723–724 (Elzem, Kür–Aras arası), Mugan 725–726, Belencer ve Beyzâ 729, Erdebil 730. Allân 727'ye eklenmedi: Çelik 726–727'de hakanın Azerbaycan akınının püskürtüldüğünü yazar, yer farklı |
| Yücel 2006 (`AKD:yucel-2006`) | Rus zaferi 1103, Aksu 1184, Kayalı 1185, Edirne 1078; yeni kayıtlar Pereyaslavl 1061, Alta 1068, Torçesk 1093 |
| Torçesk 1093 | Şehir Rus hizmetindeki Uzlar'ın yerleşimiydi; karşı taraf "Kiev knezliği (Torçesk Uzları)", kategori `dis` |

## Akademik ikinci kaynak turu 2 (2026-10-30)
Tüm partilerde tek kaynaklı kayıt: 244 → 232.
| Kaynak | Desteklediği kayıtlar |
|---|---|
| Yurdakul 2023, Dıngıl Ilgın 2022 (zaten kayıtlı) | Birinci Balkan seferi 441–443, Marcianopolis 447; Aquileia 452, Milano ve Ticinum 452 |
| TDVİA Filibe; Kuteybe b. Müslim, Toharistan | Filibe c. 834; Nîzek isyanı 709 |
| Akcakaya 2023 (`AKD:akcakaya-2023`, Mehmed Arif Bey hatıratı) | 93 Harbi Kafkas cephesi: Doğubayazıt, Ardahan, Halyaz, Zivin, Gedikler, Yahniler, Alacadağ, Deveboynu (1877) |
| Çapak 2014 (`AKD:capak-2014`) | Erzurum, Muş, Bitlis 1916 işgalleri; Muş ve Bitlis'in kurtarılışı (7–8 Ağustos 1916). Bitlis'in düşüşü için 3 Mart verir (TDVİA 1 Mart) → `dispute` |
| Çaykıran 2021 (`AKD:caykiran-2021`) | Trabzon 1916; işgal başlangıcı 8 Nisan (TDVİA 18 Nisan) → `dispute` |
| Atabey 2019 (`AKD:atabey-2019`) | Kûtülamâre 1917 (24 Şubat) |
| Ak 2019 (`AKD:ak-2019`) | Bakü 1918 |
| Bakılıp kullanılmayan | Ege Tarih Dergisi Hokand kroniği (taranmış görüntü, metin yok); OMÜ Hîve bölümü (sunucuya erişilemedi); Atatürk Araştırma Merkezi Bitlis ve Gazi Akademik Bakış Trabzon makaleleri (DergiPark 429 hız sınırı, sonra denenecek) |

## Harita: Çin, Tibet ve Moğolistan (kullanıcı geri bildirimi, 2026-10-30)
| Konu | Karar |
|---|---|
| Sorun | Doğuda yalnız Koço, Kâşgar ve Ötüken noktaları vardı; Çin birkaç hücreden ibaretti, Gansu koridoru ve Batı Moğolistan boş görünüyordu |
| Çözüm | `tools/fix_borders_cin.py`: Kumul, Kan-chou, Çang-an, Yinşan, Pekin, Hangçou, Çengdu, Lhasa, Hoten, Gulca ve Batı Moğolistan noktaları; Sui, T'ang, Song, Cin (Cürçen), Tangut, Ming, Çing ile Kuzey/Güney Çin hanedanları ve Tibet. Tibet ve Çin hücreleri Hindistan'a ve Güneydoğu Asya'ya taşmasın diye Bengal, Birmanya ve Hindiçin'e boş hücre |
| Yan düzeltme | Gürgenç (Hârizm) 550–712 Sâsânî değil, Afrîgîler |
| Sınırlılık | Hanedan yılları genel tarih bilgisi, yaklaşık; Voronoi yöntemi nedeniyle seyrek noktalı bozkırda (ör. 659–704 Balasagun T'ang) bölgeler olduğundan geniş görünebilir |

## Harita: sistematik tarama (2026-10-30)
Yöntem: her devletin haritadaki ilk ve son yılı tarihî ömrüyle karşılaştırıldı; geç başlayan, erken biten ve boşluklu şehirler listelendi. Düzeltmeler `tools/fix_borders_tarama.py`'de.
| Sorun | Düzeltme |
|---|---|
| İran ve Horasan 1335–1370 İlhanlı | Kertler, Serbedârîler, Muzafferîler, Celâyirliler, Çağatay, "yerel hânedanlar"; Timur'un geliş yılları şehir bazında (1381–1393) |
| Karakoyunlular 1335'te başlıyordu | 1375 (Kara Mehmed); öncesi yerel beylikler |
| Lahor ve Multan 1206 sonrası boş | Delhi Sultanlığı, Bâbürlüler, Dürrânîler, Sihler, İngiltere |
| Merv 1785–1884 Özbek | Buhara (Mangıt), Hîve, Teke Türkmenleri |
| Kıpçaklar 1000'de başlıyordu | 1060; öncesi Peçenekler |
| Viyana 1000'den Habsburg; Hafsîler 1000'den | Kutsal Roma 1000–1278; Zîrîler, Muvahhidler 1229'a kadar; Güney İtalya 1071'e kadar Bizans; Toledo 1085'e kadar Endülüs |
| Boş erken dönemler | Macaristan şehirleri 895'ten; Revan, Ahıska, Fergana, Taşkent, Çimkent, Akmescid, Göktepe, Kızılsu, Astarhan, Saraycık, Sibir, Azak, Moskova, Yanya, İşkodra, Midilli, Sakız, Mekke, Gûr, Alamut |
| Kalan sınırlılık | "Yerel hânedanlar" etiketi parçalı dönemler için toplu ad; Kazak bozkırının kuzeyi seyrek noktalı |

## Harita: 400–550 ve Tuna kaleleri (2026-10-30)
| Konu | Karar |
|---|---|
| Denetim aracı | `tools/check_battle_owners.py`: her savaşın yeri o yıl en yakın şehrin sahibiyle karşılaştırılır. 868 kayıttan 71 uyuşmazlık kaldı; bunlar yakındaki şehrin hücresine düşen kuşatma ve ittifak durumları (elle gözden geçirildi), sahipsiz bölge yok |
| 400–550 | `tools/extend_borders_400.py`; İdil boyu ve Sır Derya ağzı 552 öncesi kaynak olmadığı için boş |
| Tuna ve Turla | Silistre, Rusçuk, İbrail ve Hotin noktaları; bu kalelerdeki savaşlar önceden Eflak'a veya Lehistan'a düşüyordu |
| Bükreş | 550–568 Avar değil; Avarlar 568'de geldi |

## Kaynak turu: Türk beylikleri ve atabeylikleri (2026-10-30)
| Kaynak | Desteklediği kayıtlar |
|---|---|
| TDVİA Hama, Birecik, Savar, Ba'lebek | Hama 1130, Bire 1145, Esârib–Kefertâb 1138, Ba'lebek 1139 (Ba'lebek maddesi 1136 der → `dispute`; Birecik maddesi 1144 der → `dispute`) |
| Küçüksipahioğlu 2014 (`AKD:kucuksipahioglu-2014`) | Hama 1130, Âmid 1134, Pons 1137, Suruç ve Bire 1145 |
| Akdemir 2022 (`AKD:akdemir-2022`) | Esârib 1130, Hama 1130, Ba'lebek 1139, Suruç ve Bire 1145 |
| Altan 2014 (`AKD:altan-2014`) | Bilbîs 1164, Banyas 1164, Mısır 1169 |
| Turan 2017 (`AKD:turan-2017`) | Kilikya (Mleh) — akını 1170'e koyar → `dispute` |
| Kalan 21 tek kaynaklı | Tuğtegin'in savaşları (1108–1126), Hârûn b. Han (1068–69), Çaka Bey (ROM), Saltuklu 1131 vb.; Alptekin'in *Dımaşk Atabegliği* ve Küçüksipahioğlu'nun Tuğtegin makalesi (Şarkiyat Mecmuası 2024) aday |

## Kaynak turu: Anadolu Selçukluları (2026-10-30)
| Kaynak | Desteklediği kayıtlar |
|---|---|
| Balık 2021a, 2021b (`AKD:balik-2021a`, `AKD:balik-2021b`) | Menderes ve Honaz 1148 (1 Ocak Menderes geçişi, 7–8 Ocak Kazıkbeli pususu) |
| Aktaş 2015 (`AKD:aktas-2015`) | Ra'bân 1179 |
| Bingöl ve Çopur 2025 (`AKD:bingol-copur-2025`) | Kilikya seferi 1225 |
| İnce 2019 (zaten kayıtlı) | Lâdik 1119; Uluborlu (İnce 1121 der → `dispute`) |
| Kalan 15 tek kaynaklı | Aksaray 1155 ve Yağıbasan 1162 (Işık 2019 ve Aktaş genel anlatır, muharebe yok), Hârizmliler 1238–1240, el-Kâmil 1234, Tarsus 1246, Roma verisine dayanan 1113–1179 Bizans çatışmaları |

## Arayüz turu 2: zaman çizelgesi (2026-10-30)
Kullanıcı geri bildirimi: iki ayrı yıl kaydırıcısı kafa karıştırıyordu; tek, uzun bir çubuk, oynatmaya hız ayarı ve açılışta 1453 istendi.
- İki `range` girdisi yerine haritanın üstünde tam genişlikte tek zaman çizelgesi: en eski kayıttan (427) en sona (1922). Üzerinde iki tutamaç; uçlar sürüklenir, seçili bant sürüklenince aralık kayar, boş yere tıklayınca en yakın uç oraya gelir; ok, Shift+ok, PageUp/PageDown, Home/End tuşları.
- Çubuğun arka planında on yıllık savaş sayısı histogramı (karekök ölçekli); seçili aralıktakiler vurgulu. Altta yüzyıl ekseni.
- Kontrol noktaları: 18 önemli savaş (Katalaunum'dan Büyük Taarruz'a). Etiketler önem sırasıyla iki satıra yerleşir, sığmayan yalnız çentik olarak kalır (fareyle adı görünür). Tıklayınca aralık o savaşla biter ve kayıt panelde açılır.
- Oynatma: aralığın genişliği korunarak ileri kayar (aralık çok genişse 25 yıllık pencere); hız 8, 20, 50 veya 120 yıl/sn; Duraklat/Devam.
- Açılış: 1403–1453, sınırlar 1453'e göre, panelde İstanbul'un fethi.
- Zaman çizelgesi yalnız haritayı etkiler. Liste ve zafer–yenilgi tabloları kendi yıl filtresini kullanır (varsayılan: tüm yıllar), yoksa açılışta liste 1403–1453 ile daralmış görünürdü.

## Kaynak turu: Türkistan ve bozkır devletleri (2026-10-30)
- Türkistan (Parti 22) için beş DergiPark makalesi eklendi: Derekov 2015, Peler–Korkmaz 2024, Sadullayeva 2022, Selçuk–Gümbür 2022, Keserci 2020. Tek kaynaklı kayıt sayısı 14'ten 6'ya indi.
- Rus kaynaklarına dayanan Türkçe makaleler tarihleri Jülyen takvimiyle verir (Göktepe 12 Ocak 1881 = 24 Ocak Miladi; İrcar 5 Mayıs 1866). Kayıtlar Miladi tarihte bırakıldı; fark ihtilaf notunda belirtildi.
- Bozkır devletleri (Parti 23) için iki TDVİA maddesi (Mesleme b. Abdülmelik, Macaristan) ve Çelik 2013 eklendi; 11'den 8'e indi.
- Elenen adaylar:
  - Hun–Avar–Bulgar için ek kaynak bulunamadı.
  - Cecota 2011 (Bulgarlar ve 717–718 Arap kuşatması) kaynakların olayların seyrini kesin kurmaya izin vermediğini söylediği için kullanılmadı.
  - Keserci, Temmuz 1864 Çimkent kuşatmasını yazar ama Rusların püskürtüldüğünü söylemez. Bu yüzden Temmuz 1864 kaydına eklenmedi.

## Harita: 400–1000 boşlukları (2026-10-30)
Tablo 400'e uzatıldıktan sonra İtalya, Kuzey Afrika, Malta, İspanya, Pannonia, Pencap, Gūr, Ahsâ ve Ural ağzındaki şehirlerin ilk dilimi hâlâ 712–1000 arasında başlıyordu. Bu bölgeler o dönemlerde haritada boş görünüyordu. Kuzey İtalya'da ise hiç nokta yoktu. `tools/fix_borders_erken.py`:
- Germen kavimleri devleti Got ve Vandal krallıklarını da kapsayacak şekilde genişletildi. Ağlebîler (800–909) yeni devlet olarak eklendi.
- Pannonia'da Avarlar'dan sonra Tuna'nın batısı 796–895 Frank, doğusu 805–895 Bulgar oldu. Buda'daki 796–895 boşluğu kapandı.
- Malta'nın 1000–1530 İspanya dilimi düzeltildi: 1000–1091 Kelbî emirliği, 1091–1283 Sicilya–Napoli, 1283'ten Aragon.
- Lahor 500–540 Akhun (Toramana ve Mihirakula).
- Milano ve Venedik noktaları eklendi.
- `check_battle_owners.py`: bir yeni uyuşmazlık çıktı, zararsız. Nice 1543 artık Milano'ya (İspanya) düşüyor; şehir Savoya'nındı.

## Kaynak turu: Osmanlı 1774–1812, 1839–1878, 1914–1918 (2026-10-31)
- Altı akademik yayın ve bir TDVİA maddesi eklendi: Fedakâr 2019, Gölen 2014, Atabey 2020, Kardaş 2015, Özdemir 2024 ve Ziştovi Antlaşması maddesi. Tek kaynaklı kayıt 197'den 190'a, bu üç partide 34'ten 27'ye (12 → 9, 12 → 11, 10 → 7) indi. Partilerin önceki sayıları EKSIKLER tablosunda güncel değildi; tablo yeniden sayıldı.
- **Zığındere 1915:** Sonuç `D`'den `L`'ye çevrildi; kazanan taraf İngilizler. Özdemir 2024, kaybedilen mevzileri geri almak için yapılan karşı taarruzların sonuçsuz kaldığını yazar.
- **İkinci Kanal Harekâtı:** Tarih Temmuz 1916'dan 4 Ağustos 1916'ya (Romani) düzeltildi; kayıt partide Muş'un kurtarılışından sonraya taşındı.
- **Grahova:** Tarih Mayıs 1858'e daraltıldı.
- Kardaş 2015 için yalnız yayının özeti okundu. Özet olayı ve tarihi doğrudan veriyor.

## Kaynak turu: beylikler ve Anadolu Selçukluları (2026-10-31)
- Yeni indirilen 40'a yakın TDVİA maddesi (yer adları ve hânedanlar) tek kaynaklı kayıtlar için tarandı. Dört maddede eşleşme çıktı: Mirdâsîler, Tuğtegin, Çaka Bey, Eyyûbîler. Bunlara Karakuş 2018 eklendi. Tek kaynaklı kayıt 190'dan 184'e indi (beylikler 21 → 16, Anadolu Selçukluları 15 → 14).
- **Midilli 1092:** Kayıt Roma veri setinden gelmişti; Çaka Bey maddesi aynı olayı anlattığı için notu Türkçe kaynağa göre yeniden yazıldı. Durum `borderline` kaldı: Çaka'nın beyliği Türk devleti sayılır mı sorusu değişmedi.
- **Artah'ın kaybı:** İki madde de geri alışı 1069–70'e koyduğu için kayıt yılı 1069'da bırakıldı, fark `dispute`'ta duruyor.

## Harita: Mohaç yılı ve Kili (2026-10-31)
`tools/fix_borders_mohac_kili.py`:
- Batı ve Kuzey Macaristan şehirleri 1526'dan Habsburg görünüyordu. Mohaç (Ağustos 1526) bu yüzden Habsburg toprağına düşüyordu. Habsburg ve Erdel (Zápolya) dilimleri 1527'den başlatıldı; Ferdinand ülkeye 1527'de fiilen hâkim oldu.
- Kili noktası eklendi; Kili 1484 kaydı önceden İbrail'e (Eflak) düşüyordu. Sıra TDVİA Kili maddesine göre: Ceneviz ve Dobruca, 1403'ten Eflak, ardından Boğdan, 1484–1812 Osmanlı, sonra Rusya, Boğdan, Romanya, Rusya, Romanya.
- `check_battle_owners.py`: 72 → 70. Kalan uyuşmazlıklar gözden geçirildi. Savaşlar ya sınırda ya da saldırılan tarafın toprağında geçiyor.
