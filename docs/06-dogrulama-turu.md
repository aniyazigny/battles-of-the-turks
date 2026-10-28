# Doğrulama ve ek kaynak turu (Partiler 1–4)

Tarih: 2026-10-28 · Kapsam: Büyük Selçuklu pilotu, Anadolu Selçukluları, beylikler ve atabeylikler, Gazneliler ve Karahanlılar.

## Ne yapıldı
1. **Roma veri seti ile eşleştirme** (`tools/match_rom.py`). "Where the Romans Fought" veri setindeki, Türk tarafının yer aldığı 1030–1310 arası 77 savaş kayıtlarımızla yıl (±1) ve yer (≤80 km) üzerinden eşleştirildi; sonuçlar elle denetlendi. Eşleşen kayıtlara `ROM` kaynağı ve `verify.rom` eklendi. İki yanlış eşleşme ayıklandı (Drakon–İznik, Dulhisar–Kibistra); koordinat farkı yüzünden kaçan üç eşleşme elle eklendi (Aras 1047–Stragna, Kösedağ, Konya 1146–Akroinon).
2. **Eksik savaşlar.** Roma veri setinde olup bizde olmayan savaşlar eklendi: Çaka Bey'in Ege savaşları (1090–1097), Dânişmendlilerin Kastamonu, Çankırı ve Niksar savaşları (1132–1140), Zengî'nin Bizâa ve Halep (1138), Anadolu Selçuklularının İznik 1113, Lâdik 1119, Uluborlu 1120, Menderes 1177, Harax 1178, Bolu 1179, Trabzon 1205 ve Sinop 1254/1259 savaşları. 1284 sonrası Osmanlı ve beylik savaşları Osmanlı partisine bırakıldı.
3. **Türk akademik literatürü** (karar P6). Encyclopaedia Iranica'ya erişim engelli (HTTP 403) olduğu için DergiPark ve İSAM'daki hakemli makalelere yönelindi. Altı makale okundu (künyeler `data/akademik-kaynaklar.json`; kaynak anahtarı `AKD:<anahtar>`):
   - Erdem 2018 ve Çelik 2021 (Belek): Suruç, Şiran, Serûc, Turuş, Harput, Azâz, Menbic.
   - Palabıyık 2007 (Gazneli Hint seferleri): Peşâver, Vayhand, Nandana, Lokhot, Kannevc, Ganda (Ramganga), Somnat, Câtlar.
   - Gökhan 2012 ve Çıtak 2025 (Keykâvus dönemi): Keben, Sinop, Antalya 1216.
   - İnce 2019 (II. Kılıçarslan–Bizans): Miryokefalon.
4. **Wikipedia kapsam kontrolü.** Kategori listeleri tarandı; TDVİA'da karşılığı bulunan üç savaş eklendi: Gazne 998, Bhâtiya 1004–05, Refeniye 1115. Diğerleri aşağıdaki aday listesinde.

## Akademik kaynaklarla gelen düzeltmeler
| Kayıt | Değişiklik | Kaynak |
|---|---|---|
| Suruç (I) | 1100 → 1101 | Çelik 2021 |
| Azâz 1123–24 | borderline → kesin; Belek'in Joscelin'in yardımı ve huruç üzerine çekildiği netleşti | Çelik 2021 |
| "Keşmir yolunda Triloçanpâl" | Nandana kalesinin fethi (405/1014) olarak düzeltildi, kesin | Palabıyık 2007 |
| Ganda 1019 | borderline → kesin; Ramganga geçişi ve büyük zafer | Palabıyık 2007 |
| Keben | tarih ihtilafı: 1216 / 1217 / 1218 | Gökhan 2012, Ayan |
| Sinop'un fethi | ikinci tarih: Anonim Selçuknâme 8 Şubat 1216 | Çıtak 2025 |
| Sakız 1090 | Roma veri seti Bizans zaferi der, TDVİA Çaka'nın zaferi; P6 gereği TDVİA | — |

## Doğrulama durumu
| Parti | Kayıt | İki TDVİA maddesi | Roma veri seti | Akademik yayın | Tek kaynak |
|---|---|---|---|---|---|
| Büyük Selçuklu | 80 | 68 | 10 | 2 | 8 |
| Anadolu Selçukluları | 72 | 46 | 19 | 4 | 15 |
| Beylikler ve atabeylikler | 57 | 28 | 10 | 7 | 19 |
| Gazneliler ve Karahanlılar | 32 | 12 | 0 | 8 | 14 |

"Tek kaynak": ne ikinci bir TDVİA maddesi ne Roma veri seti ne de akademik yayınla desteklenen kayıt. Ayrıca 9 kayıt yalnızca Roma veri setine (Bizans kaynaklarına) dayanıyor; bunlar `borderline` işaretli ve notlarında "Türk kaynağı bulunamadı" yazıyor.

## Kapsam adayları (Wikipedia'da var, kaynakla henüz doğrulanmadı)
Bunlar kayıt değildir; TDVİA veya akademik bir kaynakla doğrulanınca eklenecek.
- **Anadolu Selçukluları:** Lâdik 1147 ve Efes 1147 (İkinci Haçlı Seferi), Akşehir (Philomelion) 1190, Sivrihisar, Turbessel'in düşüşü 1150–51, İznik–Selçuklu savaşı 1225–1231, Azat Musa'nın Gürcistan seferi.
- **Gazneliler:** Tausi nehri (1019), Gazneli–Saffârî savaşı, İkinci Lamgân, Lahor 1186.
- **Zengîler:** Ayıntab, Maraş 1161, Kınnesrîn, Busrâ 1147, Butayha, Hûle gölü 1157, Şeyzer 1157, Ba'lebek, Hama 1130, Dimyat 1169, İskenderiye 1167.
- **Beylikler ve Selçuklu emîrleri:** Artah, Gerger, Nehrülkelb, Tel Bâşir 1108, Kerec-i Ebû Dülef, Rakhsi, Musul kuşatmaları (1096, 1104, 1108), Maarretünnu'mân.

## Yöntem kararları
- **Tek taraflı kayıt (P8):** Yalnızca karşı tarafın kaynağına (Roma veri seti) dayanan bir savaş, Türk kaynaklarında ona aykırı bir bilgi yoksa kayda alınır; ancak `borderline` işaretlenir ve notunda Türk kaynağı bulunamadığı yazılır. Türk kaynağı farklı bir sonuç verirse P6 uygulanır.
- **Akademik kaynak anahtarı:** `AKD:<yazar-yıl>`; künyeler `data/akademik-kaynaklar.json`'da. Sitedeki kaynak listesinde künye ve bağlantı olarak görünür.
