# Battles of the Turks / Türklerin Savaştığı Yerler

## 🗺️ Haritayı aç: **[aniyazigny.github.io/battles-of-the-turks](https://aniyazigny.github.io/battles-of-the-turks/)**

[Where the Romans Fought](https://iosiflazaridis.github.io/battles-of-the-romans/) sitesinin Türk karşılığı. **Durum:** veri toplama ve doğrulama aşaması; demo her güncellemede GitHub Pages'te yenilenir.

## Belgeler
| Dosya | İçerik |
|---|---|
| [docs/METODOLOJI.md](docs/METODOLOJI.md) | Yöntem: kapsam, tanımlar, kategoriler, kaynak politikası, iş akışı, veri şeması |
| [docs/KAYNAKLAR.md](docs/KAYNAKLAR.md) | Kademeli bibliyografya ve kullanım durumu |
| [docs/EKSIKLER.md](docs/EKSIKLER.md) | Açık eksiklerin ana listesi |
| [docs/KARARLAR.md](docs/KARARLAR.md) | Tarihli karar günlüğü |
| [docs/01-inceleme-ve-kaynak-plani.md](docs/01-inceleme-ve-kaynak-plani.md) | Orijinal sitenin incelemesi ve ilk plan |
| [docs/02-pilot-buyuk-selcuklu.md](docs/02-pilot-buyuk-selcuklu.md) | Pilot 1'in bulguları |
| [docs/03-anadolu-selcuklu.md](docs/03-anadolu-selcuklu.md) | Parti 2: Anadolu Selçukluları |
| [docs/04-beylikler-atabeylikler.md](docs/04-beylikler-atabeylikler.md) | Parti 3: Türk beylikleri ve atabeylikleri |
| [docs/05-gazneli-karahanli.md](docs/05-gazneli-karahanli.md) | Parti 4: Gazneliler ve Karahanlılar |
| [docs/07-osmanli-kurulus.md](docs/07-osmanli-kurulus.md) | Parti 5: Osmanlı kuruluş dönemi (1284–1402) |
| [docs/08-osmanli-1402-1481.md](docs/08-osmanli-1402-1481.md) | Parti 6: Fetret Devri, II. Murad ve Fâtih (1402–1481) |
| [docs/09-osmanli-1481-1520.md](docs/09-osmanli-1481-1520.md) | Parti 7: II. Bayezid ve Yavuz (1481–1520) |
| [docs/10-osmanli-1520-1566.md](docs/10-osmanli-1520-1566.md) | Parti 8: Kanûnî (1520–1566) |
| [docs/11-osmanli-1566-1606.md](docs/11-osmanli-1566-1606.md) | Parti 9: II. Selim–III. Mehmed (1566–1606) |
| [docs/12-osmanli-1603-1640.md](docs/12-osmanli-1603-1640.md) | Parti 10: I. Ahmed–IV. Murad (1603–1640) |
| [docs/13-osmanli-1640-1683.md](docs/13-osmanli-1640-1683.md) | Parti 11: Sultan İbrâhim ve IV. Mehmed (1640–1683) |
| [docs/14-osmanli-1683-1718.md](docs/14-osmanli-1683-1718.md) | Parti 12: Kutsal İttifak, Prut, Pasarofça (1683–1718) |
| [docs/15-osmanli-1718-1774.md](docs/15-osmanli-1718-1774.md) | Parti 13: Lâle Devri–Küçük Kaynarca (1718–1774) |
| [docs/16-osmanli-1774-1812.md](docs/16-osmanli-1774-1812.md) | Parti 14: Küçük Kaynarca–Bükreş (1774–1812) |
| [docs/17-osmanli-1812-1839.md](docs/17-osmanli-1812-1839.md) | Parti 15: II. Mahmud dönemi (1812–1839) |
| [docs/18-osmanli-1839-1878.md](docs/18-osmanli-1839-1878.md) | Parti 16: Tanzimat'tan Berlin'e (1839–1878) |
| [docs/19-osmanli-1878-1912.md](docs/19-osmanli-1878-1912.md) | Parti 17: Berlin'den Balkan Savaşı'na (1878–1912) |
| [docs/20-osmanli-1912-1913.md](docs/20-osmanli-1912-1913.md) | Parti 18: Balkan Savaşları (1912–1913) |
| [docs/21-osmanli-1914-1918.md](docs/21-osmanli-1914-1918.md) | Parti 19: Birinci Dünya Savaşı (1914–1918) |
| [docs/22-milli-mucadele.md](docs/22-milli-mucadele.md) | Parti 20: Millî Mücadele (1919–1922) |
| [docs/23-gokturk-uygur.md](docs/23-gokturk-uygur.md) | Parti 21: Göktürkler, Türgişler, Karluklar ve Uygurlar (552–911) |
| [docs/06-dogrulama-turu.md](docs/06-dogrulama-turu.md) | Roma veri seti, akademik yayınlar ve Wikipedia ile doğrulama turu |

## Veri
- `data/pilot-buyuk-selcuklu.json`: Büyük Selçuklu dönemi (1035–1157), 80 kayıt (80 kayıt Parti 3'e taşındı).
- `data/anadolu-selcuklu.json`: Anadolu Selçukluları (1075–1308), 72 kayıt (ilk tur). Üretici: `tools/make_anadolu.py`.
- `data/beylikler-atabeylikler.json`: Türk beylikleri ve atabeylikleri (1070–1175), 57 kayıt. Üretici: `tools/make_beylikler.py`.
- `data/gazneli-karahanli.json`: Gazneliler ve Karahanlılar (893–1156), 32 kayıt. Üretici: `tools/make_gazneli_karahanli.py`.
- `data/osmanli-kurulus.json`: Osmanlı kuruluş dönemi (1284–1402), 31 kayıt. Üretici: `tools/make_osmanli_kurulus.py`.
- `data/osmanli-1402-1481.json`: Osmanlı 1402–1481, 46 kayıt. Üretici: `tools/make_osmanli_1402_1481.py`.
- `data/osmanli-1481-1520.json`: Osmanlı 1481–1520, 26 kayıt. Üretici: `tools/make_osmanli_1481_1520.py`.
- `data/osmanli-1520-1566.json`: Osmanlı 1520–1566, 30 kayıt. Üretici: `tools/make_osmanli_1520_1566.py`.
- `data/osmanli-1566-1606.json`: Osmanlı 1566–1606, 27 kayıt. Üretici: `tools/make_osmanli_1566_1606.py`.
- `data/osmanli-1603-1640.json`: Osmanlı 1603–1640, 22 kayıt. Üretici: `tools/make_osmanli_1603_1640.py`.
- `data/osmanli-1640-1683.json`: Osmanlı 1640–1683, 23 kayıt. Üretici: `tools/make_osmanli_1640_1683.py`.
- `data/osmanli-1683-1718.json`: Osmanlı 1683–1718, 27 kayıt. Üretici: `tools/make_osmanli_1683_1718.py`.
- `data/osmanli-1718-1774.json`: Osmanlı 1718–1774, 30 kayıt. Üretici: `tools/make_osmanli_1718_1774.py`.
- `data/osmanli-1774-1812.json`: Osmanlı 1774–1812, 39 kayıt. Üretici: `tools/make_osmanli_1774_1812.py`.
- `data/osmanli-1812-1839.json`: Osmanlı 1812–1839, 31 kayıt. Üretici: `tools/make_osmanli_1812_1839.py`.
- `data/osmanli-1839-1878.json`: Osmanlı 1839–1878, 46 kayıt. Üretici: `tools/make_osmanli_1839_1878.py`.
- `data/osmanli-1878-1912.json`: Osmanlı 1878–1912, 19 kayıt. Üretici: `tools/make_osmanli_1878_1912.py`.
- `data/osmanli-1912-1913.json`: Osmanlı 1912–1913 (Balkan Savaşları), 15 kayıt. Üretici: `tools/make_osmanli_1912_1913.py`.
- `data/osmanli-1914-1918.json`: Osmanlı 1914–1918 (Birinci Dünya Savaşı), 41 kayıt. Üretici: `tools/make_osmanli_1914_1918.py`.
- `data/milli-mucadele-1919-1922.json`: Millî Mücadele 1919–1922, 23 kayıt. Üretici: `tools/make_milli_mucadele.py`.
- `data/gokturk-uygur.json`: Göktürkler, Türgişler, Karluklar ve Uygurlar 552–911, 27 kayıt. Üretici: `tools/make_gokturk_uygur.py`.
- `data/akademik-kaynaklar.json`: `AKD:` anahtarıyla atıf yapılan akademik yayınların künyeleri.
- `data/sinirlar.json`: Haritadaki devlet sınırları için şehir bazlı hâkimiyet tablosu (1000–1310).

## Araçlar
- `tools/tdvia.py`: TDVİA maddelerini tam metin indirir.
- `tools/body.py`: Madde gövdesini ve kaynakçasını çıkarır.
- `tools/grepbattle.py`: Savaş geçen cümleleri süzer.
- `tools/tdvia_text.py`: Madde gövdesini çıkarır (çok bölümlü maddelerin bütün bölümleri).
- `tools/match_rom.py`: Kayıtları "Where the Romans Fought" veri setiyle eşleştirir.
- `tools/kw.py`: İndirilmiş maddelerde verilen ifadenin geçtiği cümleleri listeler.
- `tools/tdvia_search.py`: TDVİA'da başlık veya içerik araması yapar, madde adreslerini verir.

## Yol haritası
1. ~~Orijinal sitenin incelenmesi~~ ✅
2. ~~Pilot: Büyük Selçuklu~~ ✅
3. ~~Pilot kayıtlarının ikinci kaynakla kontrolü~~ ✅ (13 kayıt Türk akademik literatürüyle kontrol bekliyor)
4. Anadolu Selçukluları ✅ (46/64 kayıt iki maddeyle); beylikler ve atabeylikler ✅ ilk tur
5. Karahanlı, Gazneli ✅ ilk tur; Göktürk, Uygur
6. Osmanlı (dönemlere bölünerek): kuruluş dönemi 1284–1402 ✅, 1402–1481 ✅, 1481–1520 ✅, 1520–1566 ✅, 1566–1606 ✅, 1603–1640 ✅, 1640–1683 ✅, 1683–1718 ✅, 1718–1774 ✅, 1774–1812 ✅, 1812–1839 ✅, 1839–1878 ✅, 1878–1912 ✅, 1912–1913 ✅, 1914–1918 ✅, Millî Mücadele 1919–1922 ✅
7. Türkiye Cumhuriyeti
8. Arayüz (harita, filtreler, tablolar, indirme seçenekleri)
