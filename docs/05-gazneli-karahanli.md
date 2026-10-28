# Parti 4: Gazneliler ve Karahanlılar

Tarih: 2026-10-28 · Veri: `data/gazneli-karahanli.json` (üretici: `tools/make_gazneli_karahanli.py`) · Durum: **ilk tur**

## Özet
- **30 kayıt** (Gazneliler 25, Karahanlılar 5). 4 olay gerekçesiyle dışarıda bırakıldı.
- **Gazneliler:** dış rakiplere karşı 19 galibiyet, 2 mağlubiyet; Karahanlılara karşı 3 galibiyet (Belh 1008 ve 1019, Debûsiye 1032); 1 iç savaş.
- **Karahanlılar:** dış rakiplere karşı 2 galibiyet, 3 mağlubiyet. Gazneli ve Selçuklu savaşları `opp_state` ile Karahanlı tablosunda da görünür.
- **Statü:** 15 kesin, 12 borderline, 3 ihtilaflı.
- **Doğrulama:** 11 kayıt iki ayrı TDVİA maddesinde.

Selçuklularla yapılan savaşlar (Dandanakan vb.) pilotta kayıtlıdır ve tekrar edilmedi.

Başlıca kayıtlar: Hindûşâhîlere karşı (986–87), Peşâver (1001), Vayhand (1008), Belh (1008, 1019), Kannevc (1018), Somnat (1026), Debûsiye (1032), Gazne'nin yakılması (1150); Talas (893), Hucend (1137).

## Kaynaklar
Sebük Tegin, Mahmûd-ı Gaznevî, Mesud b. Mahmud, Mevdûd b. Mesud, İbrâhim b. Mesud, Behram Şah, Altuntaş el-Hâcib, Gazneliler, Karahanlılar, Satuk Buğra Han, Hârun Buğra Han, Arslan Han.

## Yöntem notları
- **Araç düzeltmesi:** `tools/kw.py` ve `tools/grepbattle.py` çok bölümlü maddelerde (Selçuklular 9, Karahanlılar 3, Gazneliler 2 bölüm) yalnızca ilk bölümü okuyordu. Ortak gövde çıkarıcı `tools/tdvia_text.py` ile düzeltildi. Önceki partilerin tek maddeli kayıtları tam metinle yeniden tarandı; yalnızca pilottaki Belh 1102 kaydı yeni bir doğrulama kazandı (Karahanlılar ve Arslan Han maddeleri, 22 Mayıs 1102).
- **Sâmânî iç savaşları:** Sebük Tegin'in Ebû Ali Sîmcûrî'ye karşı savaşları dış rakip sayıldı; Sâmânîler Türk hanedanı değildir.
- **Kaynak sayıları** (Somnat'ta 30.000 atlı, Kannevc'te 20.000 gazi, 1400 gemi) notta "kaynak sayısı" olarak geçer, veriye alınmadı.

## Bilinen eksikler
- Mahmud'un on yedi Hint seferinin hepsi ayrı kayıt değil; TDVİA'da adı ve sonucu net olanlar alındı. Mathura, Thanesar ve Gwalior gibi seferler eksik.
- Karahanlı iç savaşları alınmadı.
- Haritadaki sınır tablosu 1000 yılında başladığı için 893 ve 990 savaşlarında sınırlar boş görünüyor.

## Sonraki adımlar
- [ ] İkinci kaynak turu (19 tek maddeli kayıt).
- [ ] Sınır tablosunu 900'e kadar geri uzatmak (Sâmânîler, Hindûşâhîler).
- [ ] Sonraki parti: Göktürkler ve Uygurlar ya da Osmanlı'nın kuruluş dönemi.
