# Battles of the Turks / Türklerin Savaştığı Yerler

[Where the Romans Fought](https://iosiflazaridis.github.io/battles-of-the-romans/) sitesinin Türk karşılığı. **Durum:** araştırma aşaması. Pilot verisiyle çalışan demo: https://aniyazigny.github.io/battles-of-the-turks/

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
| [docs/06-dogrulama-turu.md](docs/06-dogrulama-turu.md) | Roma veri seti, akademik yayınlar ve Wikipedia ile doğrulama turu |

## Veri
- `data/pilot-buyuk-selcuklu.json`: Büyük Selçuklu dönemi (1035–1157), 80 kayıt (3 kayıt Parti 3'e taşındı).
- `data/anadolu-selcuklu.json`: Anadolu Selçukluları (1075–1308), 64 kayıt (ilk tur). Üretici: `tools/make_anadolu.py`.
- `data/beylikler-atabeylikler.json`: Türk beylikleri ve atabeylikleri (1070–1175), 46 kayıt. Üretici: `tools/make_beylikler.py`.
- `data/gazneli-karahanli.json`: Gazneliler ve Karahanlılar (893–1156), 30 kayıt. Üretici: `tools/make_gazneli_karahanli.py`.
- `data/osmanli-kurulus.json`: Osmanlı kuruluş dönemi (1284–1402), 31 kayıt. Üretici: `tools/make_osmanli_kurulus.py`.
- `data/osmanli-1402-1481.json`: Osmanlı 1402–1481, 45 kayıt. Üretici: `tools/make_osmanli_1402_1481.py`.
- `data/osmanli-1481-1520.json`: Osmanlı 1481–1520, 25 kayıt. Üretici: `tools/make_osmanli_1481_1520.py`.
- `data/osmanli-1520-1566.json`: Osmanlı 1520–1566, 28 kayıt. Üretici: `tools/make_osmanli_1520_1566.py`.
- `data/osmanli-1566-1606.json`: Osmanlı 1566–1606, 26 kayıt. Üretici: `tools/make_osmanli_1566_1606.py`.
- `data/osmanli-1603-1640.json`: Osmanlı 1603–1640, 22 kayıt. Üretici: `tools/make_osmanli_1603_1640.py`.
- `data/osmanli-1640-1683.json`: Osmanlı 1640–1683, 22 kayıt. Üretici: `tools/make_osmanli_1640_1683.py`.
- `data/osmanli-1683-1718.json`: Osmanlı 1683–1718, 26 kayıt. Üretici: `tools/make_osmanli_1683_1718.py`.
- `data/osmanli-1718-1774.json`: Osmanlı 1718–1774, 30 kayıt. Üretici: `tools/make_osmanli_1718_1774.py`.
- `data/osmanli-1774-1812.json`: Osmanlı 1774–1812, 39 kayıt. Üretici: `tools/make_osmanli_1774_1812.py`.
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
6. Osmanlı (dönemlere bölünerek): kuruluş dönemi 1284–1402 ✅, 1402–1481 ✅, 1481–1520 ✅, 1520–1566 ✅, 1566–1606 ✅, 1603–1640 ✅, 1640–1683 ✅, 1683–1718 ✅, 1718–1774 ✅, 1774–1812 ✅
7. Türkiye Cumhuriyeti
8. Arayüz (harita, filtreler, tablolar, indirme seçenekleri)
