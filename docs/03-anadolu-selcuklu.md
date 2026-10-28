# Parti 2: Anadolu Selçukluları (1075–1308)

Tarih: 2026-10-28 · Veri: `data/anadolu-selcuklu.json` (üretici: `tools/make_anadolu.py`) · Durum: **ilk tur**

## Özet
- **64 kayıt**, 7 olay gerekçesiyle dışarıda bırakıldı.
- **Kategoriler:** 46 dış rakip, 7 Türk devletleri arası (Dânişmendliler), 11 iç savaş.
- **Dış rakiplere karşı:** 26 galibiyet, 19 mağlubiyet, 1 belirsiz (Akşehir 1116).
- **Türk devletleri arası:** 5 galibiyet, 2 mağlubiyet.
- **Statü:** 40 kesin, 19 borderline, 5 ihtilaflı.
- **Doğrulama:** Hepsi TDVİA'da; 25 kayıt iki ayrı TDVİA maddesinde. Kalan 39 kayıt yalnızca sultan maddesine dayanıyor ve ikinci tur bekliyor.

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

## Sonraki adımlar
- [ ] İkinci tur: 39 tek maddeli kaydı ikinci TDVİA maddesiyle ve Türk akademik literatürüyle kontrol etmek (Turan, *Selçuklular Zamanında Türkiye*; Demirkent, Haçlı çalışmaları; Kaymaz, Pervâne).
- [ ] Hicrî tarihleri (`hijri`) doldurmak.
- [ ] Dışarıda bırakılan Hyelion ve Leimocheir 1177'yi Roma veri setiyle kontrol etmek.
- [ ] Wikipedia listesiyle kapsam kontrolü (eksik savaş var mı?).
- [ ] Sonraki parti: Dânişmendliler, Saltuklular, Mengücüklüler, Artuklular, Ahlatşahlar ve atabeylikler. Pilottaki Sivas 1070, Kahire 1077 ve Harran 1104 bu partiye taşınacak.
