"""data/milli-mucadele-1919-1922.json dosyasını üretir (Parti 20: Millî Mücadele, 1919–1922)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "milli-mucadele-1919-1922"
ST = "TBMM Hükümeti (Millî Mücadele)"
KM = "Kuvâ-yi Milliye"
TB = "TBMM Hükümeti"
WM = "Millî Mücadele (1919–1922)"
WI = "Millî Mücadele'de iç isyanlar (1919–1921)"
GR, FR, AR, GE = "Yunanistan", "Fransa", "Ermenistan", "Gürcistan"
MKP = "Mustafa Kemal Paşa"
IB = "İsmet Bey"
CE = "Çerkez Ethem"

# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür)
R = [
("Demirkapı (1919)", "Defeat of Anzavur at Demirkapı (1919)", "1919-11", WI, "Demirkapı (Susurluk)", 39.95, 28.15, "approx", "Türkiye",
 KM, "Anzavur kuvvetleri", CE, "Anzavur", "ic", "C", "kesin",
 ["TDVIA:balikesir-kongreleri", "TDVIA:milli-mucadele", "TDVIA:cerkez-ethem"],
 "Balıkesir Kongreleri maddesi Demirkapı'yı Kasım 1919'a, Millî Mücadele maddesi isyanın bastırılışını 28 Kasım'a koyar.",
 "İngilizler'in 21 Eylül'de Manyas civarında ayaklandırdığı Anzavur, Balıkesir üzerine yürürken Salihli'den gelen Çerkez Ethem kuvvetlerine yenildi.",
 "Anzavur, raised in revolt near Manyas by the British on 21 September, was beaten while marching on Balıkesir by Çerkez Ethem's forces from Salihli.", "land"),
("Akbaş baskını (1920)", "Raid on the Akbaş arsenal (1920)", "1920-01-26", WM, "Akbaş (Gelibolu yarımadası)", 40.30, 26.55, "approx", "Türkiye",
 KM, FR, "", "", "dis", "W", "borderline",
 ["TDVIA:milli-mucadele"], "", "Kuvâ-yi Milliye Fransızlar'ın koruduğu cephaneliği bastı; muharebe değil baskın olduğundan borderline.",
 "The Kuva-yi Milliye raided the French-guarded arsenal; borderline, as it was a raid rather than a battle.", "land"),
("Maraş (1920)", "Battle of Marash (1920)", "1920-02-12", WM, "Maraş", 37.58, 36.93, "known", "Türkiye",
 KM, FR, "Sütçü İmam", "", "dis", "W", "kesin",
 ["TDVIA:milli-mucadele", "TDVIA:kahramanmaras"], "Kahramanmaraş maddesi Fransızlar'ın 11 Şubat'ta boşaltmaya başladığını ve şehrin 11–12 Şubat'ta kurtulduğunu, Millî Mücadele maddesi hareketin 12 Şubat'ta zaferle sonuçlandığını yazar.",
 "21 Ocak'ta başlayan halk hareketi Fransızlar'ı şehri boşaltmaya zorladı.", "The popular rising begun on 21 January forced the French to evacuate the town.", "land"),
("Urfa (1920)", "Siege of Urfa (1920)", "1920-04-10", WM, "Urfa", 37.16, 38.79, "known", "Türkiye",
 KM, FR, "Ali Sâib Bey", "", "dis", "W", "kesin",
 ["TDVIA:sanliurfa", "TDVIA:milli-mucadele"], "",
 "7 Şubat'ta başlayan direnişin ardından Fransızlar 10 Nisan'da antlaşma şartlarıyla şehri boşaltmayı kabul edip ertesi gün terk etti.",
 "After the resistance begun on 7 February, the French agreed on 10 April to evacuate on terms and left the next day.", "land"),
("Anzavur isyanı (1920)", "Second Anzavur revolt (1920)", "1920-04-19", WI, "Biga", 40.23, 27.24, "known", "Türkiye",
 KM, "Anzavur kuvvetleri", CE, "Anzavur", "ic", "C", "kesin",
 ["TDVIA:milli-mucadele", "TDVIA:biga--canakkale", "TDVIA:cerkez-ethem"],
 "Millî Mücadele maddesi isyanın 19 Nisan'da bastırıldığını, Biga maddesi kasabanın 24 Nisan'a kadar Anzavur'un elinde kaldığını yazar.",
 "Anzavur 1920 Şubatında Biga'yı baskınla ele geçirmişti; 15 Mayıs'ta Geyve Boğazı'nda üçüncü kez ortaya çıktı.",
 "Anzavur had seized Biga in a raid in February 1920; he reappeared a third time at the Geyve gorge on 15 May.", "land"),
("Düzce isyanı (1920)", "Düzce revolt (1920)", "1920-05", WI, "Düzce ve Adapazarı", 40.84, 31.16, "region", "Türkiye",
 TB, "Düzce isyancıları", "Ali Fuad Paşa ve Refet Bey", "", "ic", "C", "kesin",
 ["TDVIA:milli-mucadele", "TDVIA:adapazari", "TDVIA:cerkez-ethem"],
 "Millî Mücadele maddesi isyanın 13 Nisan'da, Adapazarı maddesi 3 Nisan 1920'de başladığını yazar.",
 "Çerkez ve Abazalar'ın başlattığı isyan Bolu çevresine yayıldı; millî kuvvetler isyanı bastırıp âsileri destekleyen İngilizler'i İzmit'e kadar sürdü. 8 Ağustos'ta başlayan ikinci Düzce ayaklanması 23 Eylül'de bastırıldı.",
 "The revolt spread around Bolu; the national forces put it down and drove the British who backed the rebels back to İzmit. A second Düzce rising of 8 August was crushed on 23 September.", "land"),
("Yunan yaz taarruzu (1920)", "Greek summer offensive (1920)", "1920-07-08", WM, "Akhisar, Balıkesir ve Bursa", 40.19, 29.06, "region", "Türkiye",
 GR, KM, "", "", "dis", "L", "kesin",
 ["TDVIA:milli-mucadele", "TDVIA:bursa"], "",
 "22 Haziran'da üç koldan harekete geçen Yunan birlikleri Akhisar, Kırkağaç, Soma ve Balıkesir'den sonra 8 Temmuz'da Bursa'yı aldı.",
 "Advancing in three columns from 22 June, the Greek army took Akhisar, Kırkağaç, Soma and Balıkesir, then Bursa on 8 July.", "land"),
("Uşak (1920)", "Greek capture of Uşak (1920)", "1920-08-29", WM, "Uşak", 38.68, 29.41, "known", "Türkiye",
 GR, KM, "", "", "dis", "L", "kesin",
 ["TDVIA:milli-mucadele", "TDVIA:usak"], "", "", "", "land"),
("Kars (1920)", "Capture of Kars (1920)", "1920-10-30", WM, "Kars", 40.60, 43.10, "known", "Türkiye",
 TB, AR, "Kâzım Karabekir", "", "dis", "W", "kesin",
 ["TDVIA:kars", "TDVIA:milli-mucadele", "TDVIA:kazim-karabekir", "TDVIA:mustafa-kemal-ataturk"], "",
 "Kolordu Ermeni kuvvetlerini bozguna uğratarak Kars'ı geri aldı; 3 Aralık 1920'de imzalanan Gümrü Antlaşması ile Kars, Sarıkamış, Kağızman, Kulp ve Iğdır Türk topraklarına katıldı.",
 "The corps routed the Armenian forces and retook Kars; the Treaty of Alexandropol of 3 December 1920 returned Kars, Sarıkamış, Kağızman, Kulp and Iğdır.", "land"),
("Konya ve Bozkır isyanları (1920)", "Delibaş and Bozkır revolts (1920)", "1920-11-15", WI, "Konya ve Bozkır", 37.87, 32.49, "region", "Türkiye",
 TB, "Delibaş ve Bozkır isyancıları", "", "", "ic", "C", "kesin",
 ["TDVIA:milli-mucadele"], "", "3 Ekim'de Konya'da başlayan Delibaş İsyanı Isparta'ya kadar yayıldı; Bozkır ve Konya ayaklanmaları 15 Kasım'da bastırıldı.",
 "The Delibaş revolt, begun in Konya on 3 October, spread as far as Isparta; the Bozkır and Konya risings were put down on 15 November.", "land"),
("Yozgat isyanları (1920)", "Yozgat revolts (1920)", "1920-12-30", WI, "Yozgat", 39.82, 34.81, "region", "Türkiye",
 TB, "Yozgat isyancıları", CE, "", "ic", "C", "kesin",
 ["TDVIA:milli-mucadele"], "", "Yıldızeli, Yozgat ve Bozkır isyanları Haziran 1920'de başladı; 6 Eylül'deki ikinci Yozgat ayaklanması 30 Aralık'ta tamamen bertaraf edildi.",
 "The Yıldızeli, Yozgat and Bozkır revolts broke out in June 1920; the second Yozgat rising of 6 September was finally put down on 30 December.", "land"),
("Birinci İnönü (1921)", "First Battle of İnönü", "1921-01-10", WM, "İnönü", 39.82, 30.15, "known", "Türkiye",
 TB, GR, IB, "", "dis", "W", "kesin",
 ["TDVIA:milli-mucadele", "TDVIA:mustafa-kemal-ataturk"], "",
 "İsmet Bey kumandasındaki düzenli ordu birlikleri sayı ve teçhizatça üstün Yunan kuvvetlerini yendi.",
 "The regular army under İsmet Bey defeated Greek forces superior in numbers and equipment.", "land"),
("Gediz (1921)", "Suppression of Çerkez Ethem (1921)", "1921-01", WI, "Gediz", 39.00, 29.41, "known", "Türkiye",
 TB, CE + " ve kardeşleri", IB, CE, "ic", "C", "kesin",
 ["TDVIA:milli-mucadele"], "", "27 Aralık 1920'de başlatılan harekâtta Gediz'de bütün kuvvetleri çökertilen Çerkez Ethem ve kardeşleri Yunanlılar'a sığındı.",
 "In the operation begun on 27 December 1920, Çerkez Ethem and his brothers saw all their forces crushed at Gediz and fled to the Greeks.", "land"),
("Ardahan (1921)", "Recovery of Ardahan (1921)", "1921-02-23", WM, "Ardahan", 41.11, 42.70, "known", "Türkiye",
 TB, GE, "Kâzım Karabekir", "", "dis", "W", "kesin",
 ["TDVIA:elviye-i-selase", "TDVIA:kazim-karabekir", "TDVIA:ardahan"], "",
 "Ardahan, Çıldır ve Posof Gürcü işgalinden kurtarıldı; Batum dışındaki Elviye-i Selâse toprakları geri alındı.",
 "Ardahan, Çıldır and Posof were freed from Georgian occupation; the three provinces were recovered except Batum.", "land"),
("İkinci İnönü (1921)", "Second Battle of İnönü", "1921-04-01", WM, "İnönü", 39.82, 30.15, "known", "Türkiye",
 TB, GR, IB, "", "dis", "W", "kesin",
 ["TDVIA:milli-mucadele", "TDVIA:mustafa-kemal-ataturk", "TDVIA:cakmak-fevzi"], "",
 "23 Mart'ta Bilecik ve Afyon'u işgal eden Yunan ordusu 1 Nisan'da İnönü sırtlarında durduruldu; Mustafa Kemal'in telgrafında \"milletin mâkûs talihi\"nin yenildiği zafer.",
 "The Greek army, which had taken Bilecik and Afyon on 23 March, was stopped on the İnönü ridges on 1 April.", "land"),
("Aslıhanlar (1921)", "Battle of Aslıhanlar (1921)", "1921-04-07", WM, "Aslıhanlar (Dumlupınar)", 38.85, 30.0, "approx", "Türkiye",
 TB, GR, "", "", "dis", "W", "kesin",
 ["TDVIA:milli-mucadele"], "", "Yunanlılar ağır yenilgiye uğratılarak Afyon geri alındı.", "The Greeks were heavily defeated and Afyon was retaken.", "land"),
("Adapazarı'nın geri alınışı (1921)", "Recovery of Adapazarı (1921)", "1921-06-21", WM, "Adapazarı", 40.78, 30.40, "known", "Türkiye",
 TB, GR, "", "", "dis", "W", "kesin",
 ["TDVIA:adapazari"], "", "Şehir 25 Mart 1921'de Yunan işgaline uğramıştı.", "The town had been occupied by the Greeks on 25 March 1921.", "land"),
("Kütahya–Eskişehir (1921)", "Battle of Kütahya–Eskişehir", "1921-07-10", WM, "Kütahya ve Eskişehir", 39.60, 30.30, "region", "Türkiye",
 GR, TB, "", "Kral Konstantin", "dis", "L", "kesin",
 ["TDVIA:milli-mucadele", "TDVIA:eskisehir", "TDVIA:kutahya"], "",
 "Yunanlılar 10 Temmuz'da saldırıya geçti; hazırlıksız yakalanan Türk ordusu Mustafa Kemal Paşa'nın emriyle Eskişehir'i boşaltıp Sakarya'nın doğusuna çekildi. Eskişehir 20, Kütahya 21 Temmuz'da işgal edildi.",
 "The Greeks attacked on 10 July; caught unprepared, the Turkish army evacuated Eskişehir on Mustafa Kemal Pasha's orders and fell back east of the Sakarya. Eskişehir was occupied on 20 July, Kütahya on 21 July.", "land"),
("Sakarya (1921)", "Battle of the Sakarya", "1921-09-12", WM, "Sakarya nehri hattı", 39.55, 31.90, "region", "Türkiye",
 TB, GR, "Başkumandan " + MKP, "Kral Konstantin", "dis", "W", "kesin",
 ["TDVIA:milli-mucadele", "TDVIA:inonu-mustafa-ismet", "TDVIA:cebesoy-ali-fuat"], "",
 "Üç hafta süren savaş 12 Eylül'de düşmanın ağır yenilgisiyle sonuçlandı; Yunan birlikleri Eskişehir–Afyon hattına çekildi. Meclis 19 Eylül'de Mustafa Kemal Paşa'ya müşirlik rütbesi ve gazilik unvanı verdi.",
 "The three-week battle ended on 12 September with a heavy Greek defeat; the Greeks fell back to the Eskişehir–Afyon line. On 19 September the Assembly made Mustafa Kemal Pasha marshal and gazi.", "land"),
("Büyük Taarruz (1922)", "Great Offensive (1922)", "1922-08-26", WM, "Kocatepe ve Afyon", 38.75, 30.55, "known", "Türkiye",
 TB, GR, "Başkumandan " + MKP, "", "dis", "W", "kesin",
 ["TDVIA:milli-mucadele", "TDVIA:afyonkarahisar", "TDVIA:kutahya", "TDVIA:usak"], "",
 "26 Ağustos sabahı Afyon'dan başlayan taarruzda iki günde Yunan kuvvetlerinin yarısı savaş dışı bırakıldı; Afyon 27 Ağustos'ta kurtarıldı.",
 "In the offensive launched from Afyon on the morning of 26 August, half the Greek forces were put out of action within two days; Afyon was freed on 27 August.", "land"),
("Başkumandanlık Muharebesi (1922)", "Battle of Dumlupınar", "1922-08-30", WM, "Dumlupınar", 38.85, 30.00, "known", "Türkiye",
 TB, GR, "Başkumandan " + MKP, "General Trikopis", "dis", "W", "kesin",
 ["TDVIA:milli-mucadele", "TDVIA:cakmak-fevzi", "TDVIA:kutahya", "TDVIA:eskisehir"], "",
 "Kuşatma harekâtı bizzat Mustafa Kemal Paşa'nın yönettiği meydan savaşıyla tamamlandı; Yunan başkumandan vekili Trikopis ve pek çok asker esir alındı. \"Ordular ilk hedefiniz Akdeniz'dir ileri!\" emri bu muharebeden sonra verildi.",
 "The encirclement was completed in a pitched battle directed by Mustafa Kemal Pasha himself; the Greek deputy commander-in-chief Trikoupis and many soldiers were captured.", "land"),
("İzmir'in kurtuluşu (1922)", "Recapture of İzmir (1922)", "1922-09-09", WM, "İzmir", 38.42, 27.14, "known", "Türkiye",
 TB, GR, "Nûreddin Paşa", "", "dis", "W", "kesin",
 ["TDVIA:milli-mucadele", "TDVIA:izmir"], "",
 "Nûreddin Paşa'ya bağlı birlikler hükümet konağına Türk bayrağını çekti; çok sayıda düşman askeri esir edildi. Uşak 1, Eskişehir 2, Balıkesir 6, Aydın 7, Bursa 10–11 Eylül'de kurtarıldı.",
 "Nureddin Pasha's units raised the Turkish flag over the government house; many enemy soldiers were captured. Uşak was freed on 1, Eskişehir 2, Balıkesir 6, Aydın 7 and Bursa 10–11 September.", "land"),
]

LEFT = [
    {"name": "Karakese direnişi (Dörtyol, Aralık 1918)", "reason": "Madde ilk silâhlı direnişi anar; sonuç yok.", "source": "TDVIA:milli-mucadele"},
    {"name": "İzmir'in işgali (15 Mayıs 1919) ve İstanbul'un işgali (16 Mart 1920)", "reason": "İşgal; muharebe değil.", "source": "TDVIA:milli-mucadele"},
    {"name": "Eskişehir harekâtları (1919–1920)", "reason": "Cebesoy maddesi İngilizler'in İzmit'e çekilmesini toplu anar.", "source": "TDVIA:cebesoy-ali-fuat"},
    {"name": "Antep savunması (1920–1921)", "reason": "Gaziantep maddesi on aylık direnişi anar; sonucu (şehrin teslimi) maddede açık değil — ikinci kaynak gerekiyor.", "source": "TDVIA:gaziantep"},
    {"name": "Pontus isyanları ve Koçgiri isyanı", "reason": "Maddeler toplu anar; muharebe ayrıntısı yok.", "source": "TDVIA:milli-mucadele"},
    {"name": "Batı Trakya'nın işgali (1920)", "reason": "Muharebe ayrıntısı yok.", "source": "TDVIA:milli-mucadele"},
    {"name": "Büyük Taarruz sonrası şehir kurtuluşları (Eylül 1922)", "reason": "Takip harekâtı; İzmir kaydının notunda.", "source": "TDVIA:milli-mucadele"},
]

# İkinci kaynak turu.
EXTRA_SRC = {
    "Akbaş baskını (1920)": ["TDVIA:balikesir-kongreleri"],  # baskını Balıkesir Kongresi kararlaştırdı
    "Yozgat isyanları (1920)": ["TDVIA:cerkez-ethem"],  # 20 Haziran'da harekete geçip isyanı bir haftada bastırdı
    "Gediz (1921)": ["TDVIA:cerkez-ethem"],  # Kütahya'dan Gediz'e çekilen Ethem'e karşı kuvvete başvuruldu
    # Akademik tur (2026-10-31)
    "Gediz taarruzu (1920)": ["AKD:kilavuz-2011", "AKD:uca-2021"],  # 24 Ekim 1920 taarruzu, mağlup olundu
    "Aslıhanlar (1921)": ["AKD:uca-2021", "AKD:caykiran-2022"],
    "Adapazarı'nın geri alınışı (1921)": ["AKD:turkmen-1999"],  # işgal 21 Haziran 1921'e kadar yaklaşık dört ay sürdü
}
FIX = {
    "Aslıhanlar (1921)": {"result": "L", "date": "1921-04-08",
        "dispute": "Millî Mücadele maddesi Yunanlılar'ın Aslıhanlar'da ağır yenilgiye uğratıldığını ve 7 Nisan'da Afyon'un geri alındığını yazar. Uca 2021 (Nutuk'a dayanarak) Aslıhanlar ve Dumlupınar muharebelerinde belirgin bir üstünlük sağlanamadığını, Refet Paşa'nın yenildiği halde düşmanı yendiğini bildirdiğini; Çaykıran 2022 Yunan kuvvetlerinin 8–15 Nisan 1921'de Aslıhanlar–Dumlupınar'da yeniden taarruz edip ilerlediğini yazar. Kayıt akademik kaynaklara göre Türk tarafı için başarısız sayıldı.",
        "note": "II. İnönü'den sonra çekilen Yunan kuvvetlerini takip eden Refet Paşa'nın birlikleri 7 Nisan'da Afyon'a girdi; 8–15 Nisan'daki Aslıhanlar ve Dumlupınar muharebelerinde Yunan karşı taarruzu karşısında başarı sağlanamadı.",
        "note_en": "Pursuing the Greek forces withdrawing after the Second İnönü, Refet Pasha's troops entered Afyon on 7 April; in the Aslıhanlar and Dumlupınar battles of 8–15 April they failed against the Greek counter-offensive."},
}
NEW = {
    "Uşak (1920)": [
        ("Gediz taarruzu (1920)", "Gediz offensive (1920)", "1920-10", WM, "Gediz", 39.00, 29.41, "known", "Türkiye",
         GR, TB, "Ali Fuad Paşa (Batı Cephesi)", "", "dis", "L", "kesin",
         ["TDVIA:cebesoy-ali-fuat"], "", "Yunan ilerleyişini durdurmak için girişilen taarruzdan istenen sonuç alınamadı; Ali Fuad Paşa cephe kumandanlığından alındı (yerine 25 Ekim 1920'de İsmet Bey getirildi).",
         "The offensive launched to halt the Greek advance failed; Ali Fuad Pasha was removed from the front command (replaced by İsmet Bey on 25 October 1920).", "land"),
    ],
}
RR = []
for r in R:
    RR.append(r)
    RR.extend(NEW.get(r[0], []))

recs = []
for i, r in enumerate(RR, 1):
    (ntr, nen, date, war, place, lat, lon, loc, country, sa, sb, tc, oc, cat, res, status, src, disp, note, note_en, typ) = r
    src = src + [x for x in EXTRA_SRC.get(ntr, []) if x not in src]
    fx = dict(FIX.get(ntr, {}))
    disp, note, note_en = fx.pop("dispute", disp), fx.pop("note", note), fx.pop("note_en", note_en)
    date, res = fx.pop("date", date), fx.pop("result", res)
    assert not fx, (ntr, fx)
    rec = {"id": i, "name_tr": ntr, "name_en": nen, "date": date, "hijri": "", "type": typ, "war": war, "place": place,
           "lat": lat, "lon": lon, "loc": loc, "country": country, "side_a": sa, "side_b": sb, "turkic_cmd": tc, "opp_cmd": oc,
           "category": cat, "result": res, "status": status, "sources": src,
           "verify": {"tdvia": True, "tdvia2": len([s for s in src if s.startswith("TDVIA:")]) >= 2, "wp": False, "rom": False, "academic": any(x.startswith("AKD:") for x in src)},
           "state": ST, "home_batch": HB}
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    recs.append(rec)

dates = [r["date"] + ("-15" if len(r["date"]) == 7 else "") for r in recs]
assert dates == sorted(dates), [d for a, d in zip(dates, dates[1:]) if d < a]
pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 20 — Millî Mücadele (1919–1922)", "compiled": "2026-10-30", "status": "İkinci kaynak turu yapıldı.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "milli-mucadele-1919-1922.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
