# Açık eksikler (ana liste)

Tüm partilerin "Bilinen eksikler" ve "Sonraki adımlar" maddeleri burada toplanır. Bir eksik kapanınca `[x]` yapılır ve kapandığı commit/tarih yazılır. Sayılar `tools/eksikler.py` ile güncellenir.

Son güncelleme: 2026-10-31

## 1. Kaynak eksikleri (tek TDVİA maddesine dayanan kayıtlar)
`python tools/eksikler.py` hepsini adıyla listeler. Durum (2026-10-31):

| Parti | Kayıt | Tek kaynaklı |
|---|---|---|
| Pilot Büyük Selçuklu | 80 | 8 |
| Anadolu Selçukluları | 72 | 15 |
| Beylikler ve atabeylikler | 72 | 21 |
| Gazneli ve Karahanlı | 37 | 7 |
| Osmanlı kuruluş | 31 | 6 |
| Osmanlı 1402–1481 | 46 | 8 |
| Osmanlı 1481–1520 | 26 | 5 |
| Osmanlı 1520–1566 | 30 | 5 |
| Osmanlı 1566–1606 | 28 | 6 |
| Osmanlı 1603–1640 | 23 | 6 |
| Osmanlı 1640–1683 | 27 | 8 |
| Osmanlı 1683–1718 | 27 | 6 |
| Osmanlı 1718–1774 | 34 | 6 |
| Osmanlı 1774–1812 | 40 | 9 |
| Osmanlı 1812–1839 | 31 | 6 |
| Osmanlı 1839–1878 | 46 | 11 |
| Osmanlı 1878–1912 | 20 | 7 |
| Osmanlı 1912–1913 | 15 | 5 |
| Osmanlı 1914–1918 | 41 | 7 |
| Millî Mücadele 1919–1922 | 23 | 4 |
| Göktürk–Uygur 552–911 | 27 | 8 |
| Türkistan hanlıkları | 28 | 6 |
| Bozkır devletleri (Hazar, Peçenek, Kırgız) | 31 | 8 |
| Hun, Avar ve Bulgar | 24 | 9 |
| Kıpçaklar | 9 | 3 |
| **Toplam** | **868** | **190** |

- [x] Gazneli–Karahanlı ikinci kaynak turu (2026-10-29; 20 → 9).
- [x] TDVİA'da otomatik ikinci madde taraması (2026-10-30, `tools/second_source_candidates.py`): 27 kayıt ikinci maddeye kavuştu; TDVİA bu açıdan büyük ölçüde tükendi.
- [ ] Tek maddeli kayıtlar için Türk akademik literatürü (Köymen, Kafesoğlu, Sevim, Turan, Demirkent, Kaymaz; DergiPark).

## 2. Kapsam eksikleri (henüz kayıt olmayan savaşlar)
- [ ] **Anadolu Selçukluları:** (Lâdik ve Efes 1147 "Menderes ve Honaz" kaydında; Akşehir 1190 için TDVİA'da ayrıntı yok, Konya 1190 kaydında), Sivrihisar, Turbessel 1150–51, İznik–Selçuklu savaşı 1225–31, Azat Musa'nın Gürcistan seferi; Hyelion ve Leimocheir 1177 (Roma veri setiyle kontrol).
- [ ] **Gazneliler:** Rama-Ganga 1019 (Triloçanpal), Gazne 1148 (Gurlu Sûrî), Tausi nehri 1019, Saffârî savaşı, İkinci Lamgân, Lahor 1186; Mathura seferi. (Nagarkot 1009, Thânesâr 1014, Lokhot 1021, Gevâliyâr–Kālincâr 1022 ve Hânsî–Thânesâr–Nagarkot'un kaybı c. 1043 eklendi, 2026-10-30.)
- [ ] **Karahanlılar:** iç savaşlar.
- [ ] **Zengîler:** Ayıntab, Maraş 1161, Kınnesrîn, Busrâ 1147 (madde savaş anlatmıyor), Butayha, Hûle 1157, Şeyzer 1157 (madde yalnız depremi anar), İskenderiye 1167; Fâmiye, Banyas 1157. (2026-10-30'da eklendi: Banyas 1164, Hama 1130, Humus 1135, Kefertâb–Esârib–Bizâa 1138, Ba'lebek 1139, Suruç 1145, Ca'ber 1146, Dımaşk 1154, Bilbîs 1164, Mısır 1169, Dimyat 1169.)
- [ ] **Dımaşk:** 1129 Haçlı saldırısı, Böri dönemi.
- [ ] **Beylikler ve Selçuklu emîrleri:** Gerger, Nehrülkelb, Kerec-i Ebû Dülef, Rakhsi, Musul kuşatmaları 1096/1104/1108, Maarretünnu'mân. (Artah 1068 ve 1069, Kınnesrîn 1097, Tel Bâşir 1108 eklendi, 2026-10-30.)
- [ ] **Osmanlı kuruluş:** Karesi'nin ilhakı, Çimpe ve Gelibolu 1354; İncügez, Çatalca, Aydos; 1302–1310 beylik savaşları (Katalanlar).
- [ ] **Osmanlı 1402–1481:** İskender Bey savaşları (Torvioll 1444, Otonetë, Kruya 1466–67); Bosna 1463; İşkodra 1474 ve 1478–79; Demirkapı 1442, Kunoviçe 1444, Akdere 1476. (Kefalonya, Zanta ve Ayamavra 1479 eklendi, 2026-10-30.)
- [ ] **Osmanlı 1481–1520:** Kefalonya 1500; Macar akınları. (Krbava 1493 eklendi, 2026-10-30.)
- [ ] **Osmanlı 1520–1566:** Seydi Ali Reis 1554; Safevî seferleri 1548, 1553–55. (Korfu ve Gorjani 1537 eklendi, 2026-10-30.)
- [ ] **Osmanlı 1566–1606:** (Revan 1604 eklendi, 2026-10-30); Kalugareni ve Yergöğü 1595 ayrı kayıt; diğer Celâlî çatışmaları. (Cehennem deresi 1600 eklendi, 2026-10-30.)
- [ ] **Osmanlı 1603–1640:** (Revan 1616 eklendi, 2026-10-30); Kalenderoğlu–Tekeli Mehmed Paşa (Ankara); Halil Paşa'nın Erzurum kuşatması 1627; Selmas/Urmiye yılı (Canbolatoğulları maddesi 1604 der).
- [ ] **Osmanlı 1640–1683:** (Kandiye 1649 hücumu, Varvar Ali Paşa 1648, Haydaroğlu isyanı 1648 eklendi, 2026-10-30); Kandiye 1647–48; Para 1651 ve Foça 1649 deniz savaşları; Hotin'in geri alınışı 1674; Abaza Hasan'ın Aksaray zaferi (tarihi maddede yok). (Yeni Zerinvar 1664 eklendi, 2026-10-30.)
- [ ] **Osmanlı 1683–1718:** Mora'nın kaybı 1685–87 (Koron, Navarin, Modon, Anabolu, Atina, İnebahtı). (Korfu 1716 eklendi, 2026-10-30.) Kırım Hanlığı: Orkapı 1689 ve Lemberg 1695 eklendi (2026-10-29).
- [ ] **Osmanlı 1718–1774:** 1723–25 İran seferinin tek tek kuşatmaları; Larga 1770 (İvazzâde maddesi Kartal ile bir tutar), Yergöğü, Kılburun; Kırım Hanlığı: 1736, 1737 ve 1738 istilâları eklendi (2026-10-30); Dinyester ve Azak denizi 1738 zaferleri eklendi.
- [x] **Kapsam kararı:** Kırım Hanlığı savaşları → Osmanlı ordusuyla birlikte ya da padişah emriyle olanlar borderline (KARARLAR, 2026-10-29). Orkapı 1689, Lemberg 1695 ve 1736–1738 istilâları eklendi (borderline).
- [ ] **Osmanlı 1774–1812:** Kalafat, Tendra ve Kelegra deniz savaşları; Sırp isyanının diğer savaşları (Belgrad 1806, Mişar, Deligrad, Çegar 1809); Aynaroz 1807 (Bozcaada 1807 eklendi, 2026-10-30), Arpaçay 1807; Rusçuk 1811 ve Slobozia; Vehhâbîlerin Tâif'i (Şubat 1803) ve Mekke'yi (30 Nisan 1803) alması (Mekke maddesi; Şerîf Gālib Osmanlı tâbiiyetinde olduğundan borderline adayı).
- [ ] **Osmanlı 1812–1839:** Dervenaki 1822, (Tripoliçe 1821 ve geri alınışı 1825 eklendi, 2026-10-30) Atina 1826–27, Osmanlı–İran savaşı 1821–23, Bosna isyanı (Hüseyin Kapudan), Vehhâbî seferinin diğer savaşları. Humus 1832 eklendi (2026-10-29).
- [ ] **Osmanlı 1839–1878:** (Karadağ seferi 1852–53 eklendi, 2026-10-30, borderline); Kafkas cephesi 1853–54 (Ahıska, Başgedikler, Kürekdere); Kars müdafaası 29 Eylül 1855; Arkadi 1866; Aleksinaç ve Cuniş 1876; Batum 1877–78; Vidin, Rusçuk ve Silistre direnişleri; Şeynova–Kazanlık ve Filibe 1878.
- [ ] **Millî Mücadele 1919–1922:** Antep savunması (sonuç için ikinci kaynak); Karakese 1918; Eskişehir harekâtları 1919–20; Pontus ve Koçgiri; Sarıkamış ve Gümrü 1920; Fransızlara karşı Adana–Pozantı çatışmaları.
- [ ] **Osmanlı 1914–1918:** Galiçya, Romanya, Makedonya kolorduları; İran harekâtı (Hemedan); Şeria 1918; Nablus–Megiddo 1918; Van 1915; Aden–Lahic; Medine müdafaası boyunca çatışmalar; Hicaz demiryolu baskınları; Akabe 1917; Erzincan 1918.
- [ ] **Osmanlı 1912–1913:** Hamidiye akınları; Elli ve Limni deniz muharebeleri; Şarköy ve Bolayır 1913; Priştine, Ohri, Pirlepe, Midilli, İmroz, Bozcaada işgalleri.
- [ ] **Osmanlı 1878–1912:** Termopil 1897 (Velestin 1897 eklendi, 2026-10-30); Yemen isyanları 1891–97 ve 1902–04; Arnavut ve Malisör isyanları 1909–12; Derne ve Tobruk cephesi 1912; Girit 1897.
- [x] **Türkistan hanlıkları:** Parti 22 ilk tur (2026-10-30, 28 kayıt; kapsam kullanıcı onayıyla). Harita: `tools/fix_borders_turkistan.py`, `tools/fix_borders_hanliklar.py`.
- [ ] **Türkistan eksikleri:** 6 tek kaynaklı kayıt (üçüncü turda Derekov 2015, Peler–Korkmaz 2024, Sadullayeva 2022, Selçuk–Gümbür 2022 ve Keserci 2020 ile Akmescid, Çimkent, İrcar, Kızılarvat, Bendesen, Yengikale, Hokand 1875 ve Kenesarı 1837–38 güçlendirildi; kalanlar: Irgız–Turgay 1838, Beş-Tumak 1839, Çimkent Temmuz 1864, Türkmen baskınları 1870 ve 1872, Hucend 1875) için akademik kaynak (Baymirza Hayit); Evliyaata 1864, Merv 1884, Hokand isyanları 1878–1898; 1916 isyanı ve Basmacılar (ayrı kapsam).
- [x] **Göktürkler ve Uygurlar:** Parti 21 ilk tur (2026-10-30, 26 kayıt).
- [ ] **Göktürk–Uygur eksikleri:** Sâsânî–Göktürk savaşları 569–571 ve 588–589, Kapgan'ın Semerkant müdahalesi 701, Karluk isyanları 711–714, Beşbalık 791, Uygur–Tibet savaşları, Uygur–Kırgız savaşları 821 sonrası; Orhon yazıtları için akademik kaynak (Erhan Aydın, Ahmet Taşağıl).
- [x] **Hazarlar, Peçenekler, İdil Bulgarları, Kırgızlar:** Parti 23 ilk tur (2026-10-30, 31 kayıt).
- [ ] **Parti 23 eksikleri:** 8 tek maddeli kayıt için akademik kaynak (Kurat, Kafalı; Hazar–Arap savaşları 722–730 Çelik 2013 ile, Derbend 714 Mesleme maddesiyle, Macarlar'ın sürülmesi 895 Macaristan maddesiyle güçlendirildi); Hazar akını 799, Kiev 968, Peçenek akınları 1035–36 ve 1197'ye kadar.
- [x] **Avrupa Hunları, Akhunlar, Avarlar, Tuna Bulgarları:** Parti 24 ilk tur (2026-10-30, 24 kayıt).
- [ ] **Parti 24 eksikleri:** 9 tek kaynaklı kayıt (Sofya 809, Nikephoros 811, Edirne 813 Uçar 2021; Attila 441, 447, 452 Yurdakul ve Dıngıl Ilgın; Filibe 834 ve Nîzek 709 TDVİA ile güçlendirildi); Avrupa Hunları 375–434 (Ahmetbeyoğlu); Avarlar'ın Pannonia ve Bizans savaşları 568–602; Akhunlar'ın Hindistan seferleri.
- [x] **Asya Hunları (MÖ):** Kapsam dışı (kullanıcı kararı 2026-10-30: "Milattan önce tarihlere gitmeye gerek yok").
- [x] **Kıpçaklar:** Parti 25 ilk tur (2026-10-30, 6 kayıt; kapsam kullanıcı onayıyla).
- [ ] **Parti 25 eksikleri:** Alta 1068, 1061 ve Torçesk 1093 Yücel 2006 ile eklendi (2026-10-30); bu üçü tek kaynaklı. Salnitsa 1111 ve Stugna 1093 için kaynak gerekir (Kurat).

## 3. Harita eksikleri
- [x] Sınır tablosu 400'e uzatıldı (2026-10-30, `tools/extend_borders_400.py`): Avrupa Hunları, Ogur boyları, Akhunlar, Juan-juanlar, Batı Roma, Franklar. `tools/check_battle_owners.py` ile hiçbir savaş sahipsiz bölgeye düşmüyor.
- [x] Sınır tablosu 1000 öncesine uzatıldı (2026-10-30, `tools/extend_borders_552.py`; kaba katman; Lahor ve Mültan `tools/fix_borders_pencap.py` ile eklendi).
- [x] Altın Orda 1502'den sonra da görünüyordu → `tools/fix_borders_altinorda.py` (2026-10-29): Kazan 1437–1552, Astarhan 1466–1556, Nogay 1502–1634, Kırım bozkırı, Hîve 1512–, Sibir 1490–1582, Kazak Hanlığı 1465–; Rusya, Kiev (Lehistan-Litvanya 1362–1667, Rusya 1667–), Kalmuklar 1634–.
- [x] Doğu Türkistan ve Moğolistan: Moğolistan Hanlığı, Yarkent Hanlığı, Cungarlar, Çing ve Yâkub Beg dilimleri işlendi (2026-10-30, `tools/fix_borders_dogu_turkistan.py`; Yedisu ve Moğolistan dilimleri kaba).
- [x] İran ve Irak 1405–1501 → `tools/fix_borders_iran_1405.py` (2026-10-29): Karakoyunlu Tebriz 1408, Irâk-ı Acem 1447–52, Kirman 1453; Akkoyunlu 1468–70'ten 1503'e; Celâyirli Bağdat 1405–1410; Horasan 1507–1510 Şeybânî; Van ve Revan'ın 1335 öncesi boş görünen dilimleri dolduruldu.
- [x] Lahsâ 1253 sonrası Uyûnî görünüyordu → `tools/extend_borders_1812.py` (2026-10-29).
- [x] Lahsâ 1818–1913: Benî Hâlid, Suûdî (yaklaşık 1830–1841), 1871'den Osmanlı (2026-10-30, `tools/fix_borders_lahsa.py`; Faysal'ın Lahsâ'yı aldığı yıl maddede yok).
- [x] Teselya 1881: Yenişehir noktası eklendi (2026-10-30, `tools/fix_borders_gaps_1.py`).
- [x] Lahsâ'nın 1913'te İbn Suûd'a geçişi (2026-10-30, `tools/extend_borders_1923.py`).
- [ ] Edirne'nin 1913 Bulgar işgali (yıl çözünürlüğünde görünmüyor). Kırkkilise noktası eklendi (2026-10-30).
- [x] Kıbrıs 1489–1570 Venedik (2026-10-30, `tools/fix_borders_gaps_1.py`).

## 4. Veri alanı eksikleri
- [ ] Hicrî tarihler (`hijri`): 2026-10-30'da `tools/fill_hijri.py` ile 180 kayda kaynak maddelerden hicrî tarih işlendi (`data/hicri.json`; toplam ~263/749). Kalanlar için maddelerde miladîyle yan yana hicrî tarih yok; ikinci kaynak gerekiyor.
- [ ] Koordinatlar: kayıtların çoğu yaklaşık (`loc` = approx/region). 2026-10-30: `tools/check_coords.py` ile ülke tutarlılığı kontrol edildi (773 kayıt, 0 hata); yaklaşık noktaların daraltılması için kaynak gerekiyor.
