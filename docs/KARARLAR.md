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
