# Metodoloji

Bu belge projenin nasıl yürütüldüğünü anlatan **kalıcı referanstır**. Kararlar değiştikçe güncellenir; her değişiklik ayrıca `KARARLAR.md`'ye kaydedilir.
Son güncelleme: 2026-10-25

## 1. Amaç
"Where the Romans Fought" ([battles-of-the-romans](https://iosiflazaridis.github.io/battles-of-the-romans/)) sitesinin Türk karşılığını hazırlamak. Bu, Türk devletlerinin adı bilinen her kara ve deniz savaşının yeri, tarihi, tarafları, komutanları, sonucu ve kaynaklarıyla birlikte haritalandığı bir başvuru eseri olacak.

**İlke:** Hem Türk ve İslâm karşıtı önyargıdan hem de milliyetçi abartıdan uzak durmak. Hedef, akademik olarak savunulabilir olmak. Bunu belirli bir "tarafın" kaynağını seçerek değil, **her iddiayı birden fazla bağımsız kaynakla kontrol ederek ve çelişkileri saklamadan göstererek** sağlıyoruz.

## 2. Kapsam

### Hangi devletler "Türk" sayılır
Ana hat devletleri:
1. Göktürkler
2. Uygurlar
3. Karahanlılar ve Gazneliler
4. Büyük Selçuklu (Irak, Suriye ve Kirman kollarıyla)
5. Anadolu Selçukluları ve beylikler
6. Osmanlı Devleti
7. Türkiye Cumhuriyeti

Bu listede olmayan Türk kökenli devlet ve topluluklar (Hârizmşahlar, Memlükler, Altın Orda, Timurlular, Akkoyunlu ve Karakoyunlu, Hazarlar, Peçenekler, Kıpçaklar, Karluklar, Babürlüler vb.) şimdilik **rakip** olarak kaydedilir. Notta Türk kökenleri belirtilir. Kapsam genişletilirse bunların savaşları "Türk devletleri arası" kategorisine geçer.

### Zaman aralığı
552 (Göktürk Kağanlığı'nın kuruluşu) ile 1923 arası, gerekirse sonrası. Kuruluş öncesi olaylar (ör. 1040 öncesi Selçuklular) ilgili devletin altında "kuruluş dönemi" olarak kaydedilir.

## 3. Tanımlar

### Ne "savaş" sayılır
- Bir Türk kuvvetinin asıl taraf olarak veya ayrı bir müttefik birlik olarak katıldığı, **adı bilinen** kara ya da deniz savaşı.
- Kuşatmalar ancak gerçek çatışma olduysa sayılır (hücum, huruç, kuşatmayı kırmaya gelen ordunun savaşı). Bir kuşatmanın içinde ayrıca adı olan bir meydan savaşı varsa, o ayrı bir kayıttır.
- **Sayılmaz:** adsız küçük çatışmalar, savaş olmadan yapılan katliamlar ve baskınlar, çatışmasız teslimler ve fetihler, efsaneler.
- Bir olayın savaş sayılıp sayılmayacağı şüpheliyse kayıt **silinmez**; `borderline` olarak işaretlenir ve gerekçesi yazılır.

### Kazanan
- Sahada kazanan taraf sayılır: alanı tutan, düşmanı bozguna uğratan, şehri alan veya donanmayı yok eden. Stratejik sonuç ve kaynaklar arasındaki ihtilaf notta belirtilir.
- **Kuşatmalarda:** şehir düştüyse kuşatan, kuşatma kaldırıldıysa savunan kazanmış sayılır. Haraç alınması gibi durumlar notta yazılır.
- **Berabere (D):** sonucu belirsiz savaşlar ile iki tarafın da zafer iddia ettiği ve modern akademik literatürün net hüküm vermediği savaşlar.

### Kategoriler (karar K1, K2)
| Kod | Anlamı | Skora etkisi |
|---|---|---|
| `dis` | Türk olmayan rakip | Hem devletin kendi tablosuna hem "Türkler toplamı"na girer |
| `turk_arasi` | Farklı hanedanlardan Türk devletleri veya toplulukları arası (Selçuklu–Gazneli, Osmanlı–Timurlu vb.) | İki devletin kendi tablolarına girer, "Türkler toplamı"na girmez |
| `ic` | Aynı hanedan veya devlet içi (Selçuklu kolları arası, taht kavgaları, isyanlar) | Skora girmez; haritada gri gösterilir |

### Savaş hangi devlete yazılır (karar K3)
Savaşı sultan emrettiyse veya komutanı sultan atadıysa, savaş sultanın devletine yazılır. Emîr veya atabey kendi inisiyatifiyle savaştıysa kayıt kendi beyliğine ya da atabeyliğine yazılır.

### Statü
- `kesin`: savaş ve sonucu kaynaklarda net.
- `borderline`: savaş sayılıp sayılmayacağı veya hangi devlete ait olduğu tartışmalı.
- `ihtilafli`: tarih veya sonuç kaynaklar arasında çelişkili. Çelişki `dispute` alanında yazılır ve verilen karar `KARARLAR.md`'ye eklenir.

## 4. Kaynak politikası
Ayrıntılı bibliyografya `KAYNAKLAR.md`'de.

1. **Temel referans:** TDV İslâm Ansiklopedisi (TDVİA). Hakemli, maddeleri kaynakçalı, Türk ve İslâm tarafının anlatısını ciddiyetle ele alıyor.
2. **Bağımsız akademik kontrol:** Türk dışından da olan dengeli akademisyenler (Peacock, Bosworth, Golden, Haldon, Hillenbrand, Finkel, Murphey, Ágoston, Aksan vb.).
3. **Karşı tarafın anlatısı:** Bizans, Ermeni, Gürcü, Haçlı, Avrupa ve Çin kaynakları. Roma veri seti bu iş için hazır bir çapraz kontrol aracıdır.
4. **Wikipedia:** Yalnızca **kapsam kontrolü** için ("eksik savaş var mı?"). Hiçbir zaman tek kaynak olarak kullanılmaz.
5. **Kullanılmayanlar:** kaynaksız popüler siteler, sosyal medya, 19. yüzyıl oryantalist veya milliyetçi anlatılar (hangi yönde olursa olsun).

### Pilot çalışmada öğrenilen kurallar
- **İki madde kuralı:** TDVİA'nın kendi maddeleri birbiriyle çelişebiliyor (Talhâb, Rûzrâver, Hoy). Bu yüzden her olay en az iki ayrı maddeden okunur. Örneğin bir sultan maddesi ve bir komutan maddesi.
- **Sayı kuralı:** Ordu büyüklükleri ve kayıplar, hangi taraftan gelirse gelsin, doğrudan alınmaz. Ortaçağ sayıları "kaynak X'e göre" diye aktarılır, modern tahmin ise aralık olarak verilir. Örnek: TDVİA Malazgirt'te Bizans ordusunu 200.000 verir; modern tahmin ~40.000'dir (Haldon).
- **Zayıf ikincil kaynak kuralı:** Birincil kaynağa dayanmayan Wikipedia kayıtları, doğrulanana kadar ayrı kayıt olarak alınmaz (ör. Gence 1046).
- **Karşı taraf kuralı:** Karşı tarafın kaynağı farklı bir sonuç veriyorsa iki anlatı da notta yazılır. Karar modern akademik değerlendirmeye göre verilir ve alternatif okuma da kaydedilir (ör. Pasinler 1048).

## 5. İş akışı (her dönem için tekrarlanır)
1. **Ham liste:** Sultan veya hükümdar maddeleri, devlet maddesi ve "ilişkili maddeler" sayfaları taranarak oluşturulur. Wikipedia listeleri ve Roma veri seti ile eksikler kontrol edilir.
2. **Araştırma partisi:** Her savaş için iki TDVİA maddesi okunur. Tarih hem hicri hem miladi yazılır. Taraflar, komutanlar, sonuç ve kaynaklar kaydedilir.
3. **Çapraz kontrol:** Karşı tarafın kaynağı ve bağımsız akademik kaynakla karşılaştırılır. `verify` alanı güncellenir.
4. **Kararlar:** Çelişkiler `dispute` alanına, verilen kararlar `KARARLAR.md`'ye yazılır.
5. **Dışarıda bırakılanlar:** Kural gereği alınmayan olaylar gerekçesiyle `left_out` listesine eklenir.
6. **Son kontroller:** Mükerrer kayıtlar, adlar ve koordinatlar (`known`, `approx`, `region`) kontrol edilir.

## 6. Veri şeması
Her dönem için ayrı bir dosya tutulur: `data/<parti>.json`.

| Alan | Açıklama |
|---|---|
| `id`, `name_tr`, `name_en` | Kimlik, Türkçe ve İngilizce ad |
| `date`, `hijri` | Miladi tarih (ISO ya da yaklaşık), hicri tarih |
| `type` | `land` (kara) veya `sea` (deniz) |
| `war`, `place`, `lat`, `lon`, `loc`, `country` | Savaşın bağlı olduğu harp, yer, koordinat, kesinlik düzeyi, bugünkü ülke |
| `side_a`, `side_b` | **Kazanan önce yazılır** |
| `turkic_cmd`, `opp_cmd` | Türk tarafının ve rakibin komutanları |
| `state`, `home_batch` | Savaşan Türk devleti; kaydın nihai olarak ait olduğu parti |
| `category` | `dis`, `turk_arasi` veya `ic` |
| `result` | Türk tarafı için W (kazandı), L (kaybetti), D (berabere), C (iç savaş) |
| `status` | `kesin`, `borderline` veya `ihtilafli` |
| `strength` | Ordu büyüklükleri (kaynağıyla birlikte) |
| `sources` | Kaynaklar; anahtar biçimi `TDVIA:<slug>`, `WP:<başlık>`, `ROM` |
| `verify` | `tdvia`, `wp`, `rom`, `academic` (doğrulandıysa true) |
| `dispute`, `note` | Kaynaklar arası çelişki, açıklama |

Her dosyada ayrıca bir `left_out` listesi (gerekçeli) ve kuralları içeren bir `meta` bölümü bulunur.

İleride eklenecek alanlar: `note_en` ve Romalılar sitesindeki "Rum dili payı"na karşılık gelen `turkic_share` (ordudaki Türk unsurunun tahmini payı).

## 7. Teknik notlar
- **TDVİA'dan okuma:** WebFetch özetleri kayıplıdır. Maddeler `tools/tdvia.py` ile tam metin olarak indirilir:

  ```
  python -I tools/tdvia.py <çıktı_klasörü> <slug> ...
  ```

  Gövde ve kaynakça `tools/body.py` ile, savaş geçen cümleler `tools/grepbattle.py` ile çıkarılır.
- **Madde adresleri** tahmin edilemez (ör. `meliksah--buyuk-selcuklu`, `ilgazi-necmeddin`). Doğru adresler bir maddenin `https://islamansiklopedisi.org.tr/<slug>/iliskili-maddeler` sayfasından çıkarılır.
- **Telif:** TDVİA metinleri telifle korunur. Projeye metin kopyalanmaz; yalnızca olgular, atıf ve kısa alıntı kullanılır. İndirilen ham metinler repoya konmaz.
- **Arayüz** (sonraki aşama): Orijinal site gibi tek dosyalık statik bir site olacak; inline SVG harita (Natural Earth), dönem kaydırıcısı, filtreler, kazanma-kaybetme tabloları, "Verilen kararlar" ve "Dışarıda bırakılanlar" bölümleri, CSV/JSON/XLSX indirme seçeneği. Orijinal sitenin lisansı belirtilmediği için kodu kopyalanmaz.
