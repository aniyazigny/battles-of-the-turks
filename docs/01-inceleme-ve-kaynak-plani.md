# Battles of the Turks — İnceleme ve Kaynak Planı

Tarih: 2026-10-25 · Durum: ön araştırma (kod yok)

## 1. Orijinal proje: "Where the Romans Fought"

URL: https://iosiflazaridis.github.io/battles-of-the-romans/ (Iosif Lazaridis, Ekim 2026)

- Kapsam: MÖ 753 – MS 1475, **1.709 savaş** (236 iç savaş, 94 "geleneksel"/şüpheli, 649 "borderline").
- Teknik: Tek dosya statik HTML (~2,4 MB, veri gömülü), harici kütüphane yok, harita inline SVG
  (Natural Earth). Fontlar: Marcellus, Gentium Book Plus, IBM Plex Sans Condensed.
- Bölümler: dönem dönem harita (25 yıllık pencere + Oynat) · galibiyet/beraberlik/mağlubiyet tablosu ·
  filtrelenebilir liste · X için 18 görsel (3200×1800) · "Nasıl yapıldı" · "Verilen kararlar" · "Dışarıda bırakılanlar".
- İndirilebilir veri: CSV, JSON, XLSX, W-D-L CSV.
- Lisans belirtilmemiş → kod/veri kopyalanmaz, sadece fikir ve yapı örnek alınır.

### Kayıt şeması (JSON, savaş başına)
`id, key, name, year, month, day, date, type(land/sea), war, theatre, place, lat, lon,
loc(known/approx/region), country, side_a, side_b, allies_a, allies_b, roman_state, rome_role,
faction_a, faction_b, commanders_a, commanders_b, outcome, civil, traditional, doubt, borderline,
main_enemy, opponent_group, roman_force, languages, greek_share, greek_basis, greek_note,
composition_confidence, fame, sources, note`

Türk versiyonuna uyarlama: `roman_state → turkic_state`, `greek_share → turkic_share`
(ordudaki Türk unsurun tahmini payı; Memlük, Gazneli, Osmanlı devşirme vb. için anlamlı),
`opponent_group` Türk tarihine göre yeniden tanımlanır.

### Metodolojiden alınacak iyi uygulamalar
- Net "savaş" tanımı (adı olan meydan/deniz savaşı; gerçek çatışmalı kuşatmalar dahil, efsaneler hariç).
- Galip = sahada kazanan; stratejik sonuç ve kaynak ihtilafları notta.
- Şüpheli kayıtlar silinmez, **gerekçesiyle işaretlenir** (traditional / borderline).
- Her savaşa ayrı ayrı kaynak; ihtilaflar notta.
- Dönemsel araştırma partileri + çapraz doğrulama turları + çıkarılanlar listesi.
- Orijinal veride Türklere karşı 97 savaş var (Bizans perspektifinden) → çapraz kontrol için kullanılabilir.

## 2. Kaynak politikası (taslak)

Amaç: Türk/İslam karşıtı önyargıdan arınmış, ama milliyetçi abartıya da kaymayan, akademik
olarak savunulabilir bir veri seti. Önyargıya karşı en güçlü savunma: **her iddia için birbirinden
bağımsız taraflardan kaynak + modern akademik değerlendirme**.

### Birinci kademe (temel referans)
- **TDV İslâm Ansiklopedisi** (islamansiklopedisi.org.tr) — her savaş için ayrı hakemli madde,
  bibliyografyalı. Telif: metin kopyalanmaz, sadece atıf + kısa alıntı.
- **Türk Tarih Kurumu** yayınları ve *Belleten* dergisi; **TÜBA**, **İSAM** yayınları.
- Halil İnalcık (*Osmanlı İmparatorluğu Klasik Çağ*, *Devlet-i Aliyye*), Feridun Emecen,
  Osman Turan (*Selçuklular Tarihi ve Türk-İslâm Medeniyeti*), Mükrimin Halil Yinanç,
  İbrahim Kafesoğlu, Bahaeddin Ögel, Ahmet Taşağıl (Göktürkler).
- Uluslararası dengeli akademisyenler: Peter B. Golden (*An Introduction to the History of the
  Turkic Peoples*), Carole Hillenbrand (*Turkish Myth and Muslim Symbol: Manzikert*), Caroline Finkel
  (*Osman's Dream*), Rhoads Murphey (*Ottoman Warfare 1500–1700*), Gábor Ágoston, Colin Imber,
  Virginia Aksan (*Ottoman Wars 1700–1870*), A.C.S. Peacock (*The Great Seljuk Empire*),
  C.E. Bosworth (Gazneliler), *Cambridge History of Turkey*, *Encyclopaedia of Islam* (2./3. baskı).

### Birincil kaynaklar (çapraz kontrol için, iki taraftan)
- Türk/İslam tarafı: Orhun Yazıtları, Gerdizî, Beyhakî, İbnü'l-Esîr, Râvendî, İbn Bîbî,
  Âşıkpaşazâde, Oruç Bey, Neşrî, Kemalpaşazâde, Hoca Sâdeddin, Peçevî, Kâtib Çelebi, Naîmâ, Silahdar.
- Karşı taraf: Çin hanedan yıllıkları (Zhoushu, Suishu, Tang shu), Bizans kronikleri,
  Haçlı ve Avrupa kronikleri, Rus yıllıkları — **ihtilaf olduğunda her iki tarafın anlatısı notta**.

### Dikkatli kullanılacak / tek başına yeterli sayılmayacak
- Wikipedia: sadece **kapsam kontrolü** (savaş listesi eksik mi?) için; tek kaynak olamaz.
- Sadece tek tarafın propaganda anlatısına dayanan sayılar (ör. ordu büyüklükleri, kayıplar).
- 19. yy. oryantalist ve milliyetçi (her iki yönde) anlatılar, popüler tarih siteleri.
- Kaynaksız Türkçe popüler siteler, sosyal medya — Türk lehine olsa bile.

## 3. Kararlar
- **Kapsam (karar verildi):** ana hat devletleri — Göktürk → Uygur → Karahanlı/Gazneli →
  Büyük Selçuklu → Anadolu Selçuklu ve beylikler → Osmanlı → Türkiye Cumhuriyeti (552–1923+).
- **Dil (karar verildi):** iki dilli TR/EN; tek veri seti, alanlar `_tr`/`_en`.
- Açık: Türk devletleri arası savaşların (Ankara 1402, Otlukbeli 1473, Çaldıran 1514) "iç savaş" olarak
  işaretlenip skora dahil edilmemesi.

## 3b. Pilotun kaynak politikasına eklediği kurallar
- Bir olay için en az iki TDVİA maddesi okunur, çünkü maddeler kendi aralarında çelişebiliyor.
- Ordu büyüklükleri ve kayıplar hiçbir taraftan doğrudan alınmaz; aralık ve kaynakla verilir.
- WebFetch özetleri kayıplıdır; TDVİA maddeleri tam metin olarak indirilip okunur.
- Ayrıntılar: `02-pilot-buyuk-selcuklu.md`

## 4. Sonraki adımlar
1. Kapsam kararı → devlet/dönem listesi kesinleşir.
2. Dönem bazlı ilk ham liste (Wikipedia listeleri + TDVİA madde dizini ile kapsam).
3. Her dönem için araştırma partisi, savaş başına kaynak.
4. Doğrulama turları, "Verilen kararlar" ve "Dışarıda bırakılanlar" listeleri.
5. Ancak bundan sonra arayüz.
