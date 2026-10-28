# Parti 5: Osmanlı kuruluş dönemi (1284–1402)

Tarih: 2026-10-28 · Veri: `data/osmanli-kurulus.json` (üretici: `tools/make_osmanli_kurulus.py`) · Durum: **ikinci kaynak turu yapıldı**

## Özet
- **31 kayıt**, 3 olay gerekçesiyle dışarıda bırakıldı.
- **Dış rakiplere karşı:** 22 galibiyet, 3 mağlubiyet (Bileća 1388, Pločnik 1388, Ankara 1402), 1 belirsiz (Ermeni Beli 1284).
- **Türk devletleri arası:** 3 galibiyet (Eretnalılar 1362, Frenkyazısı 1386/87, Akçay 1397), 1 mağlubiyet (Kadı Burhâneddin'e karşı Çorumlu 1392).
- **Statü:** 16 kesin, 10 borderline, 5 ihtilaflı.
- **Doğrulama:** 20 kayıt iki ayrı TDVİA maddesinde (ilk turda 13); 4 kayıt akademik yayınla destekli; 6 kayıt Roma veri setinde (Osman Gazi dönemi). 2 kayıt yalnızca Roma veri setine dayanıyor (Ermeni Beli, Kulaca Hisar).

Başlıca kayıtlar: Koyunhisar (Bafeus) 1302, Dimbos 1303, Pelekanon 1329, Dimetoka 1352, Sazlıdere 1361, Çirmen 1371, Savra 1385, Kosova 1389, Niğbolu 1396, Ankara 1402.

## Kaynaklar
TDVİA: Osman I, Orhan, Murad I, Bayezid I, Ankara Savaşı, Kosova Savaşları, Niğbolu Savaşı, Çirmen, Bursa, Edirne, İznik, Gelibolu, Kadı Burhâneddin, Karamanoğulları. Roma veri seti: 1284–1303 Osmanlı–Bizans savaşları.

## Verilen kararlar
| Kayıt | Karar | Alternatif okuma |
|---|---|---|
| Kosova 1389 | Osmanlı zaferi (P6) | Bosna Kralı Tvrtko zaferi kendine mal etti; Paris'te Türklerin bozguna uğradığı yazıldı |
| Argeş (Rovine) 1395 | Osmanlı zaferi (P6; TDVİA: Mircea yenildi, yerine Vlad getirildi) | Romen kaynakları: Mircea'nın zaferi |
| Ankara 1402 | Dış rakip | Timurlular Türk kökenlidir ama kapsam listesinde değildir |
| Karaman, Kadı Burhâneddin, Eretnalılar | Türk devletleri arası; `opp_state` ile karşı tarafın tablosunda da görünür | — |
| Bursa 1326, İznik 1331, İzmit 1337, Selânik 1387 | Borderline: uzun abluka sonunda teslim | — |
| Çirmen | 1371 (TDVİA) | Osmanlı kaynakları 1364-65 |
| Edirne | Sazlıdere 1361 | Edirne'nin fethi için 1361, 1362, 1367 ve 1369 önerilir |

## Haritadaki sınırlar (1310–1410)
`data/sinirlar.json` 1410'a kadar uzatıldı (`tools/extend_borders_1410.py`): 126 nokta, 78 devlet. Yeni devletler: Karesi, Saruhan, Aydın, Menteşe, Hamîd, Candar, Eretna, Kadı Burhâneddin, Timurlular, Karakoyunlular, Celâyirliler, Sırbistan, Bosna, Eflak, Macaristan, Çağatay. Yeni şehirler: Bursa, İzmit, Balıkesir, Manisa, Milas, Isparta, Gelibolu, Filibe, Sofya, Üsküp, Manastır, Niş, Priştine, Belgrad, Bosna, Avlonya, Buda, Eflak, Mora. Ankara (1402) sonrasında Batı Anadolu beylikleri yeniden kurulmuş olarak gösterilir. Kapsam dışı Türk devletlerine (Timurlular, Memlükler, Altın Orda, Karakoyunlular vb.) birbirinden ayrılabilen tonlar verildi.

Bu dönemin el değiştirme tarihleri çoğunlukla yaklaşıktır ve tabloda "yaklasik" işaretlidir.

## İkinci kaynak turu (2026-10-29)
TDVİA şehir ve kişi maddeleri: İzmit, Manastır, Niş, Selânik, Bosna-Hersek (Bileća), Eskişehir (Karacahisar), Karamanoğlu Alâeddin Bey (Akçay).
Akademik yayınlar: Şafakçı 2023 (Akçay), Derinöz 2022 ve Eroğlu (Kırkdilim), Heper 2023 (Argeş).

- **Akçay:** tarih 1397/1398, ihtilaflı. Kaynaklar 793 (1391) ile 800 (1397) arasında ayrılıyor; savaş iki gün sürdü, Konya on günlük kuşatmayla teslim oldu.
- **Kırkdilim 1392:** Osmanlı yenilgisi doğrulandı (üç gün). Şehzade Ertuğrul'un burada şehit düştüğü rivayeti Eroğlu tarafından sorgulanıyor; notta.
- **Karacahisar:** 1288 (Roma veri seti) ile 1291 (Osmanlı rivayeti) ihtilafı.
- **Manastır:** 1382-83 ile 1385 ihtilafı.

Hâlâ tek kaynaklı: Dimetoka 1352, Eretna 1362, Sozopol, Pikridion 1373, Savra 1385, Pločnik 1388; yalnızca Roma veri setine dayanan Ermeni Beli ve Kulaca Hisar.

## Bilinen eksikler
- Orhan döneminin Karesi'nin ilhakı ve Rumeli'ye geçiş (Çimpe, Gelibolu 1354) olayları ayrı kayıt değil.
- I. Murad'ın Balkan seferlerinde adı geçen küçük kuşatmalar (İncügez, Çatalca, Aydos) alınmadı.
- Bayezid'in Batı Anadolu beyliklerini ilhakı (1390) savaş kaydı olarak alınmadı; çoğu savaşsız oldu.
- Roma veri setindeki 1302–1310 "Türk beylikleri" savaşları (Katalanlar ve Bizans'a karşı) Anadolu beylikleri partisine bırakıldı.

## Sonraki adımlar
- [x] İkinci kaynak turu (20/31 iki TDVİA maddesiyle, 4 akademik).
- [ ] Parti 6: Fetret Devri ve klasik dönemin başı (1402–1481): Çamurlu, Varna, Kosova 1448, İstanbul'un fethi, Otlukbeli.
