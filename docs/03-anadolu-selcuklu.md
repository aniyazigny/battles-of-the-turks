# Parti 2: Anadolu Selçukluları (1075–1308)

Tarih: 2026-10-28 · Veri: `data/anadolu-selcuklu.json` (üretici: `tools/make_anadolu.py`) · Durum: **ikinci kaynak turu yapıldı**

## Özet
- **64 kayıt**, 7 olay gerekçesiyle dışarıda bırakıldı.
- **Kategoriler:** 46 dış rakip, 7 Türk devletleri arası (Dânişmendliler), 11 iç savaş.
- **Dış rakiplere karşı:** 26 galibiyet, 19 mağlubiyet, 1 belirsiz (Akşehir 1116).
- **Türk devletleri arası:** 5 galibiyet, 2 mağlubiyet.
- **Statü:** 40 kesin, 19 borderline, 5 ihtilaflı.
- **Doğrulama:** Hepsi TDVİA'da; **46 kayıt iki ayrı TDVİA maddesinde** (ilk turda 25). 18 kayıt için TDVİA'da ikinci madde bulunamadı; bunlar Türk akademik literatürüyle kontrol bekliyor: İznik c. 1080, Akşehir 1116, Menderes 1148, Malatya 1143, Aksaray 1155, Yağıbasan 1162, Niksar 1176, Ra'bân 1179, Ankara 1204, Samsun c. 1205, Keben 1216, Kilikya 1225, el-Kâmil 1234, Hârizmliler c. 1238 ve 1240, Tarsus 1246, Kılıcarslan Kervansarayı 1249, Dulhisar 1304.

## Kaynaklar
Sultan maddeleri: Süleyman Şah I, Kılıcarslan I–IV, Mesud I–II, Keyhusrev I–III, Süleyman Şah II, Keykâvus I–II, Keykubad I–III.
Olay ve yer maddeleri: Haçlılar, Kösedağ Savaşı, Miryokefalon Savaşı, Dânişmendliler, İznik, Antalya, Alanya, Sinop, Erzurum, Kayseri.

## Verilen kararlar
| Kayıt | Karar | Alternatif okuma |
|---|---|---|
| Akşehir (Philomelion) 1116 | Belirsiz (D). TDVİA savaştan sonra Bizans'ın sultana para verdiği bir barıştan söz eder, yenilgiden söz etmez. | Anna Komnene: Bizans zaferi |
| Konya önleri 1146 | Selçuklu zaferi (P6). TDVİA: pusu ve baskınlarla ağır Bizans kaybı, imparator geri döndü. | Kinnamos: barışı sultan istedi |
| Menderes ve Honaz 1148 | Selçuklu başarısı, borderline (tek bir meydan savaşı değil) | Batı kaynakları: Menderes geçişinde Fransız başarısı |
| Konya 1190 | Yenilgi (L), ihtilaflı. Şehir saldıranın eline geçti. | TDVİA Haçlılar maddesi meydan savaşından kaçınıldığını yazar; Kılıcarslan II maddesi meliklerin savaştığını yazar |
| Basian 1202 | Gürcü zaferi; tarih TDVİA'ya göre Temmuz 1202 | Gürcü kaynakları: 1203 |
| Tarsus 1245–46 | Kuşatma kural gereği yenilgi (L); Hetum'un tâbiiyet ve vergi kabulü notta | Lehte bir antlaşmayla bittiği için Selçuklu başarısı |
| Elbistan 1277 | Borderline. Selçuklu birlikleri Moğol tarafındaydı ama ciddi savaşmadı. Memlükler kapsam dışı Türk devleti sayılarak dış rakip. | Selçuklu tarafı sayılmaz |
| Dânişmendli savaşları | `turk_arasi` (K2: farklı hanedan) | — |
| Karaman, Cimri ve Germiyan | İç savaş (devlet içi uç beylikleri ve isyanlar) | Türk devletleri arası |

## Haritadaki sınırlar (1157–1310)
`data/sinirlar.json` 1310'a kadar uzatıldı (`tools/extend_borders.py`). Yeni devletler: Osmanlı Beyliği, Eyyûbîler, Memlükler, Moğollar (İlhanlılar), Altın Orda, Latin devletleri, İznik ve Trabzon imparatorlukları, Bulgar Çarlığı, Kıbrıs Krallığı, Mengücüklüler, Karamanoğulları, Germiyanoğulları. Yeni şehirler: Kastamonu, Ankara, Eskişehir, Bilecik, Kütahya, Denizli, Karaman, Erzincan, Harput, Sinop, Alanya.

1243 sonrasında Anadolu, Moğol metbûluğuna rağmen Anadolu Selçuklu renginde gösterilir; doğrudan Moğol idaresine geçen doğu şehirleri Moğol rengini alır. İran ve Orta Asya'daki 1157 sonrası el değiştirmeler kabadır ve "yaklaşık" işaretlidir.

## İkinci kaynak turu (2026-10-28)
Kullanılan ikinci maddeler: Antakya, Halep, Malatya, Şanlıurfa, Gaziantep, Dânişmendliler, el-Melikü'l-Eşref, Hüsâmeddin Çoban, Çobanoğulları, Trabzon, Hârizmşahlar, Baba İlyas, Babaîlik, Baybars I, Muînüddin Süleyman Pervâne, Karamanoğulları, Germiyanoğulları, Selçuklular. Yeni arama: `tools/tdvia_search.py -t` (madde içeriklerinde).

- **Suğdak 1224:** borderline → kesin. Çobanoğulları maddesine göre şehir geri alındı, Kıpçak hanı ve Rus knezleri itaat etti.
- **Germiyan:** tarih c. 1286 → 1288; yer Denizli yöresi (Germiyanoğulları maddesi).
- **Tel Bâşir 1150:** kesin → borderline. Gaziantep maddesine göre Franklar savaşa girmedi.
- **Yeni tarih ihtilafları:** Malatya 1105/1106, Âmid 1240/1241.

## Sonraki adımlar
- [x] İkinci TDVİA turu (46/64).
- [ ] Kalan 18 kayıt için Türk akademik literatürü (Turan, *Selçuklular Zamanında Türkiye*; Demirkent, Haçlı çalışmaları; Kaymaz, *Pervâne Muînüddîn Süleyman*; DergiPark makaleleri).
- [ ] Hicrî tarihleri (`hijri`) doldurmak.
- [ ] Dışarıda bırakılan Hyelion ve Leimocheir 1177'yi Roma veri setiyle kontrol etmek.
- [ ] Wikipedia listesiyle kapsam kontrolü (eksik savaş var mı?).
- [ ] Sonraki parti: Dânişmendliler, Saltuklular, Mengücüklüler, Artuklular, Ahlatşahlar ve atabeylikler. Pilottaki Sivas 1070, Kahire 1077 ve Harran 1104 bu partiye taşınacak.
