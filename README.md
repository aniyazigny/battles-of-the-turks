# Battles of the Turks / Türklerin Savaştığı Yerler

[Where the Romans Fought](https://iosiflazaridis.github.io/battles-of-the-romans/) sitesinin Türk karşılığı. **Durum:** araştırma aşaması. Pilot verisiyle çalışan demo: https://aniyazigny.github.io/battles-of-the-turks/

## Belgeler
| Dosya | İçerik |
|---|---|
| [docs/METODOLOJI.md](docs/METODOLOJI.md) | Yöntem: kapsam, tanımlar, kategoriler, kaynak politikası, iş akışı, veri şeması |
| [docs/KAYNAKLAR.md](docs/KAYNAKLAR.md) | Kademeli bibliyografya ve kullanım durumu |
| [docs/KARARLAR.md](docs/KARARLAR.md) | Tarihli karar günlüğü |
| [docs/01-inceleme-ve-kaynak-plani.md](docs/01-inceleme-ve-kaynak-plani.md) | Orijinal sitenin incelemesi ve ilk plan |
| [docs/02-pilot-buyuk-selcuklu.md](docs/02-pilot-buyuk-selcuklu.md) | Pilot 1'in bulguları |

## Veri
- `data/pilot-buyuk-selcuklu.json`: Büyük Selçuklu dönemi (1035–1157), 83 kayıt.

## Araçlar
- `tools/tdvia.py`: TDVİA maddelerini tam metin indirir.
- `tools/body.py`: Madde gövdesini ve kaynakçasını çıkarır.
- `tools/grepbattle.py`: Savaş geçen cümleleri süzer.
- `tools/kw.py`: İndirilmiş maddelerde verilen ifadenin geçtiği cümleleri listeler.
- `tools/tdvia_search.py`: TDVİA'da başlık veya içerik araması yapar, madde adreslerini verir.

## Yol haritası
1. ~~Orijinal sitenin incelenmesi~~ ✅
2. ~~Pilot: Büyük Selçuklu~~ ✅
3. ~~Pilot kayıtlarının ikinci kaynakla kontrolü~~ ✅ (13 kayıt Türk akademik literatürüyle kontrol bekliyor)
4. Atabeylikler ve beylikler; Anadolu Selçukluları
5. Göktürk, Uygur, Karahanlı, Gazneli
6. Osmanlı (dönemlere bölünerek)
7. Türkiye Cumhuriyeti
8. Arayüz (harita, filtreler, tablolar, indirme seçenekleri)
