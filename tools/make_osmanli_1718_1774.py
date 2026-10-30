"""data/osmanli-1718-1774.json dosyasını üretir (Parti 13: III. Ahmed'in son yılları, I. Mahmud, III. Osman, III. Mustafa, 1718–1774)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "osmanli-1718-1774"
O = "Osmanlı Devleti"
WI = "Osmanlı–İran savaşları (1723–1746)"
W3 = "Osmanlı–Rus–Avusturya savaşı (1736–1739)"
W6 = "Osmanlı–Rus savaşı (1768–1774)"
# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür)
R = [
("İran seferi (1723–1725)", "Ottoman campaign in Iran (1723–1725)", "1724", WI, "Azerbaycan ve Batı İran", 38.08, 46.29, "region", "İran",
 O, "Safevîler", "", "", "dis", "W", "borderline",
 ["TDVIA:ahmed-iii"], "", "Gence, Nahcıvan, Hoy, Revan, Merend, Selmâs, Sine, Kirmanşah, Nihâvend ve Hemedan alındı; tek tek savaşları madde ayırmıyor.",
 "Ganja, Nakhchivan, Khoy, Erivan, Marand, Salmas, Sanandaj, Kermanshah, Nahavand and Hamadan were taken; the article does not separate the individual actions.", "land"),
("Nihâvend (1726)", "Battle of Nahavand (1726)", "1726-11", WI, "Nihâvend yöresi", 34.19, 48.37, "approx", "İran",
 "Eşref Han (Afgan Hotakîler)", O, "", "Eşref Han", "dis", "L", "kesin",
 ["TDVIA:ahmed-iii"], "", "Ardından 1727 Hemedan antlaşması yapıldı.", "The Treaty of Hamadan followed in 1727.", "land"),
("İran cephesi (1731)", "Ottoman victory over the Iranians (1731)", "1731-09-15", WI, "Batı İran", 34.80, 48.51, "region", "İran",
 O, "Safevîler (Tahmasb)", "Bağdat Valisi Ahmed Paşa, Hekimoğlu Ali Paşa", "II. Tahmasb", "dis", "W", "kesin",
 ["TDVIA:mahmud-i--osmanli", "TDVIA:nadir-sah--iran"], "", "Hekimoğlu Ali Paşa Urmiye ve Tebriz'e girdi; 1732'de barış yapıldı.", "Hekimoğlu Ali Pasha entered Urmia and Tabriz; peace followed in 1732.", "land"),
("Bağdat (1733)", "Siege of Baghdad (1733)", "1733-07-20", WI, "Bağdat ve Kerkük yöresi", 33.31, 44.36, "known", "Irak",
 O, "Nâdir (Safevî naibi)", "Topal Osman Paşa", "Nâdir", "dis", "W", "kesin",
 ["TDVIA:nadir-sah--iran"], "", "Bağdat'ı kuşatan Nâdir, yardıma gelen Topal Osman Paşa karşısında yaralı olarak Hemedan'a çekildi.", "Nader, besieging Baghdad, withdrew wounded to Hamadan before Topal Osman Pasha's relief army.", "land"),
("Akderbend (1733)", "Battle of Akdarband (1733)", "1733-12", WI, "Akderbend, Kerkük'ün kuzeyi", 35.70, 44.30, "approx", "Irak",
 "Nâdir (Safevî naibi)", O, "", "Nâdir", "dis", "L", "kesin",
 ["TDVIA:nadir-sah--iran"], "", "", "", "land"),
("Arpaçayı (1735)", "Battle of Yeghevard (1735)", "1735-06", WI, "Arpaçayı, Revan yöresi", 40.25, 44.65, "approx", "Ermenistan",
 "Nâdir (Safevî naibi)", O, "Abdullah Paşa", "Nâdir", "dis", "L", "kesin",
 ["TDVIA:mahmud-i--osmanli", "TDVIA:nadir-sah--iran"], "", "Ardından Gence (9 Temmuz), Tiflis (12 Ağustos) ve Revan (3 Ekim 1735) Nâdir'e geçti.", "Ganja (9 July), Tbilisi (12 August) and Erivan (3 October 1735) then fell to Nader.", "land"),
("Azak'ın kaybı (1736)", "Siege of Azov (1736)", "1736-07", W3, "Azak", 47.11, 39.42, "known", "Rusya",
 "Rusya", O, "", "", "dis", "L", "kesin",
 ["TDVIA:azak", "TDVIA:mahmud-i--osmanli"], "", "Aynı yaz Gözleve, Orkapı ve Kılburun da alındı.", "Gözleve, Perekop and Kinburn were also taken that summer.", "land"),
("Özü'nün kaybı (1737)", "Siege of Ochakov (1737)", "1737-07-11", W3, "Özü", 46.61, 31.54, "known", "Ukrayna",
 "Rusya", O, "Yahyâ Paşa", "Burkhard Christoph von Münnich", "dis", "L", "kesin",
 ["TDVIA:mahmud-i--osmanli"], "", "", "", "land"),
("Niş'in kaybı (1737)", "Loss of Niš (1737)", "1737-07", W3, "Niş", 43.32, 21.90, "known", "Sırbistan",
 "Habsburglar", O, "", "Friedrich Heinrich von Seckendorff", "dis", "L", "kesin",
 ["TDVIA:nis", "TDVIA:mahmud-i--osmanli"], "", "", "", "land"),
("Banaluka (1737)", "Battle of Banja Luka (1737)", "1737-08", W3, "Banaluka", 44.77, 17.19, "known", "Bosna-Hersek",
 O, "Habsburglar", "Abdullah Paşa, Hekimoğlu Ali Paşa", "", "dis", "W", "kesin",
 ["TDVIA:mahmud-i--osmanli"], "", "Avusturyalılar geri çekilmeye zorlandı. Madde Sadrazam Abdullah Paşa'yı Banaluka'da, Hekimoğlu Ali Paşa'yı Bosna'da gösterir.", "The Austrians were forced to withdraw.", "land"),
("Niş (1737)", "Recapture of Niš (1737)", "1737-10", W3, "Niş", 43.32, 21.90, "known", "Sırbistan",
 O, "Habsburglar", "Köprülüzâde Hâfız Ahmed Paşa", "", "dis", "W", "borderline",
 ["TDVIA:nis", "TDVIA:mahmud-i--osmanli"], "", "Savaşsız geri alındı.", "Retaken without a fight.", "land"),
("Mehâdiye (1738)", "Battle of Mehadia (1738)", "1738-07", W3, "Mehâdiye", 44.90, 22.36, "approx", "Romanya",
 O, "Habsburglar", "Yeğen Mehmed Paşa", "", "dis", "W", "kesin",
 ["TDVIA:mehmed-pasa-yegen"], "", "", "", "land"),
("Adakale (1738)", "Siege of Ada Kaleh (1738)", "1738-08", W3, "Adakale", 44.72, 22.47, "known", "Romanya",
 O, "Habsburglar", "Yeğen Mehmed Paşa", "", "dis", "W", "kesin",
 ["TDVIA:mehmed-pasa-yegen", "TDVIA:adakale"], "", "Üç ay kadar direnen kale teslim alındı; önce Orsova alınmıştı.", "The fortress surrendered after about three months; Orșova had been taken first.", "land"),
("Hisarcık (1739)", "Battle of Grocka (1739)", "1739-07", W3, "Belgrad–Hisarcık arası", 44.67, 20.72, "approx", "Sırbistan",
 O, "Habsburglar", "İvaz Mehmed Paşa", "", "dis", "W", "kesin",
 ["TDVIA:mahmud-i--osmanli"], "", "Şiddetli muharebelerden sonra Belgrad geri alındı; 1739 Belgrad Antlaşması izledi.", "After fierce fighting Belgrade was recovered; the Treaty of Belgrade followed in 1739.", "land"),
("Hotin'in kaybı (1739)", "Battle of Stavuchany and loss of Khotyn (1739)", "1739-08", W3, "Hotin", 48.52, 26.50, "known", "Ukrayna",
 "Rusya", O, "", "Burkhard Christoph von Münnich", "dis", "L", "kesin",
 ["TDVIA:hotin", "TDVIA:mahmud-i--osmanli"], "", "Belgrad Antlaşması'yla Osmanlılara geri verildi.", "Returned to the Ottomans by the Treaty of Belgrade.", "land"),
("Kerkük (1743)", "Siege of Kirkuk (1743)", "1743-07", WI, "Kerkük", 35.47, 44.39, "known", "Irak",
 "Nâdir Şah (Afşarlar)", O, "", "Nâdir Şah", "dis", "L", "kesin",
 ["TDVIA:mahmud-i--osmanli", "TDVIA:nadir-sah--iran"], "", "", "", "land"),
("Musul (1743)", "Siege of Mosul (1743)", "1743-10", WI, "Musul", 36.34, 43.13, "known", "Irak",
 O, "Nâdir Şah (Afşarlar)", "", "Nâdir Şah", "dis", "W", "kesin",
 ["TDVIA:nadir-sah--iran"], "", "27 Eylül'de başlayan kuşatma bir hafta sonra kaldırıldı.", "The siege begun on 27 September was lifted a week later.", "land"),
("Kars (1744)", "Siege of Kars (1744)", "1744-09", WI, "Kars", 40.60, 43.10, "known", "Türkiye",
 O, "Nâdir Şah (Afşarlar)", "", "Nâdir Şah", "dis", "W", "kesin",
 ["TDVIA:nadir-sah--iran"], "", "29 Temmuz'da başlayan iki aylık kuşatma sonuçsuz kaldı.", "The two-month siege begun on 29 July failed.", "land"),
("Kağaverd (1745)", "Battle of Kars (1745)", "1745-08-21", WI, "Kağaverd ovası, Revan yöresi", 40.30, 44.30, "approx", "Ermenistan",
 "Nâdir Şah (Afşarlar)", O, "Yeğen Mehmed Paşa (öldü)", "Nâdir Şah", "dis", "L", "kesin",
 ["TDVIA:nadir-sah--iran", "TDVIA:mehmed-pasa-yegen"], "", "Kazanmak üzereyken hastalanan serasker öldü ve ordu bozuldu.", "The commander fell ill and died when close to victory, and the army broke.", "land"),
("Hotin (1769)", "Siege of Khotyn (1769)", "1769-09", W6, "Hotin", 48.52, 26.50, "known", "Ukrayna",
 "Rusya", O, "", "Aleksandr Golitsyn", "dis", "L", "kesin",
 ["TDVIA:hotin"], "", "Haziran 1769'da ilk Rus kuşatmasına karşı bazı başarılar kazanılmıştı (Mustafa III maddesi).", "Some successes had been won against the first Russian siege in June 1769 (Mustafa III article).", "land"),
("Mora (1770)", "Orlov revolt in the Morea (1770)", "1770-04-19", W6, "Mora", 37.60, 22.40, "region", "Yunanistan",
 O, "Rusya ve Mora Rumları", "Muhsinzâde Mehmed Paşa", "Fyodor Orlov", "dis", "W", "kesin",
 ["TDVIA:muhsinzade-mehmed-pasa", "TDVIA:cesme-vakasi"], "", "Rumlar ve onlara yardım eden Ruslar bozguna uğratıldı.", "The Greek rebels and their Russian supporters were routed.", "land"),
("Sakız Boğazı (1770)", "Battle of Chios (1770)", "1770-07-05", W6, "Koyun adaları, Çeşme'nin kuzeyi", 38.45, 26.25, "approx", "Türkiye",
 O, "Rusya", "Cezayirli Hasan Bey, Hüsâmeddin Paşa", "Grigory Spiridov", "dis", "D", "kesin",
 ["TDVIA:cesme-vakasi", "TDVIA:cezayirli-gazi-hasan-pasa"], "", "Hasan Bey'in gemisiyle Spiridov'un kalyonu yandı; iki taraf da kesin galibiyet elde edemedi.", "Hasan Bey's ship and Spiridov's flagship burned; neither side won decisively.", "sea"),
("Çeşme (1770)", "Battle of Chesma", "1770-07-06", W6, "Çeşme limanı", 38.32, 26.30, "known", "Türkiye",
 "Rusya", O, "Kaptanıderyâ Hüsâmeddin Paşa", "Aleksey Orlov", "dis", "L", "kesin",
 ["TDVIA:cesme-vakasi", "TDVIA:cezayirli-gazi-hasan-pasa", "TDVIA:mustafa-iii"], "", "Limana sokulan donanma ateş gemileriyle yakıldı; yalnızca kaptanıderyânın baştardası kurtuldu.", "The fleet, packed into the harbour, was burned by fireships; only the admiral's galley escaped.", "sea"),
("Kartal (1770)", "Battle of Kagul", "1770-08-01", W6, "Kartal (Kagul) gölü yöresi", 45.80, 28.30, "approx", "Moldova",
 "Rusya", O, "", "Pyotr Rumyantsev", "dis", "L", "borderline",
 ["TDVIA:abaza-mehmed-pasa"], "", "TDVİA'da yalnızca bir paşanın biyografisinde anılır; ayrıntı yok.", "Only mentioned in a pasha's biography in TDVİA; no details.", "land"),
("Bender (1770)", "Siege of Bender (1770)", "1770-09", W6, "Bender", 46.83, 29.48, "known", "Moldova",
 "Rusya", O, "", "Pyotr Panin", "dis", "L", "kesin",
 ["TDVIA:bender-kalesi"], "", "İki ay süren kuşatmadan sonra alındı.", "Taken after a two-month siege.", "land"),
("Limni (1770)", "Relief of Lemnos (1770)", "1770", W6, "Limni", 39.87, 25.06, "known", "Yunanistan",
 O, "Rusya", "Cezayirli Hasan Bey", "Aleksey Orlov", "dis", "W", "kesin",
 ["TDVIA:cezayirli-gazi-hasan-pasa"], "", "10 Temmuz'da başlayan Rus kuşatmasındaki kaleyi bir fedai kafilesiyle kurtardı.", "With a band of volunteers he relieved the castle besieged by the Russians since 10 July.", "land"),
("Kırım'ın istilâsı (1771)", "Russian conquest of Crimea (1771)", "1771", W6, "Kırım", 45.00, 34.10, "region", "Ukrayna",
 "Rusya", O, "", "Vasily Dolgorukov", "dis", "L", "borderline",
 ["TDVIA:kirim", "TDVIA:kucuk-kaynarca-antlasmasi"], "", "Rus orduları yarımadayı istilâ etti; ayrıntılı savaş kaydı yok.", "Russian armies overran the peninsula; no detailed battle record.", "land"),
("Silistre (1773)", "Siege of Silistra (1773)", "1773-06", W6, "Silistre", 44.12, 27.26, "known", "Bulgaristan",
 O, "Rusya", "", "Pyotr Rumyantsev", "dis", "W", "kesin",
 ["TDVIA:silistre"], "", "Rus ordusu ağır kayıplarla çekildi.", "The Russian army withdrew with heavy losses.", "land"),
("Kozluca (1774)", "Battle of Kozludzha", "1774-06", W6, "Kozluca", 43.18, 27.71, "approx", "Bulgaristan",
 "Rusya", O, "", "Aleksandr Suvorov", "dis", "L", "kesin",
 ["TDVIA:abdulhamid-i"], "", "Ordu Kozluca ve Şumnu'da bozguna uğrayınca Küçük Kaynarca barışı kabul edildi.", "After the army was routed at Kozludzha and Shumen, the Treaty of Küçük Kaynarca was accepted.", "land"),
]

LEFT = [
 {"name": "1723–1725 İran seferinin tek tek kuşatmaları (Tiflis, Revan, Tebriz, Hemedan)", "reason": "Ahmed III maddesi toplu anlatır; tarihler yok.", "source": "TDVIA:ahmed-iii"},
 {"name": "Gence, Tiflis ve Revan'ın Nâdir'e geçişi (1735)", "reason": "Arpaçayı kaydının notunda; ayrı kayıt açılmadı.", "source": "TDVIA:nadir-sah--iran"},
 {"name": "Kırım'ın 1737 ve 1738 istilâları", "reason": "1736 istilâsı kaydedildi; sonraki yıllar indirilen maddelerde ayrıntılı geçmiyor.", "source": "TDVIA:kirim"},
 {"name": "Larga (1770), Yergöğü, Kılburun", "reason": "TDVİA'da adıyla ayrı savaş olarak bulunamadı; İvazzâde Halil Paşa maddesi Larga'yı Kartal ile bir tutar.", "source": "TDVIA:ivazzade-halil-pasa"},
]

# İkinci kaynak turu
EXTRA_SRC = {"İran seferi (1723–1725)": ["TDVIA:azerbaycan"],  # kontrol turu
             "Nihâvend (1726)": ["TDVIA:ahmed-pasa", "TDVIA:damad-ibrahim-pasa-nevsehirli"],
 "Bağdat (1733)": ["TDVIA:bagdat", "TDVIA:topal-osman-pasa--sadrazam"],
 "Akderbend (1733)": ["TDVIA:topal-osman-pasa--sadrazam"],
 "Özü'nün kaybı (1737)": ["TDVIA:abdullah-pasa-muhsinzade"],
 "Banaluka (1737)": ["TDVIA:bosna-hersek"],
 "Mehâdiye (1738)": ["TDVIA:haci-ivaz-pasa--sadrazam"],
 "Hisarcık (1739)": ["TDVIA:haci-ivaz-pasa--sadrazam"],
 "Musul (1743)": ["TDVIA:musul--irak"],
 "Kars (1744)": ["TDVIA:kars"],
 "Hotin (1769)": ["TDVIA:ivazzade-halil-pasa", "TDVIA:ali-pasa-moldovanci"],
 "Kartal (1770)": ["TDVIA:ivazzade-halil-pasa"],
 "Bender (1770)": ["TDVIA:ivazzade-halil-pasa"],
 "Limni (1770)": ["TDVIA:limni"],
 "Kozluca (1774)": ["TDVIA:kucuk-kaynarca-antlasmasi", "TDVIA:osmanlilar"]}
# Üçüncü kaynak turu (2026-10-31): toplu TDVİA taraması
EXTRA_SRC.update({
    "Kırım'ın istilâsı (1736)": ["TDVIA:kirim"],  # Rus kuvvetleri ilk defa 1736'da Münnich kumandasında Kırım yarımadasını istilâ etti
})
FIX = {"Nihâvend (1726)": {"turkic_cmd": "Bağdat Valisi Ahmed Paşa",
        "dispute": "Safevîler maddesi Eşref Han'ın savaşa yanaşmadan barış imzaladığını söyler; Ahmed III, Ahmed Paşa ve Damad İbrâhim Paşa maddeleri Kasım 1726'da savaş olduğunu yazar."},
 "Bağdat (1733)": {"place": "Dücum, Sâmerrâ yöresi (Bağdat'ın kuzeyi)", "lat": 34.20, "lon": 43.87, "loc": "approx",
        "dispute": "Topal Osman Paşa maddesi 19 Temmuz, Bağdat maddesi 20 Temmuz 1733 der.",
        "note": "Yedi aydır Bağdat'ı kuşatan Nâdir, Sâmerrâ yakınındaki Dücum'da Topal Osman Paşa'ya yenildi ve yaralı olarak çekildi; Bağdat Valisi Ahmed Paşa'nın savunduğu şehir kurtuldu.",
        "note_en": "Nader, who had besieged Baghdad for seven months, was defeated by Topal Osman Pasha at Dujum near Samarra and withdrew wounded; the city held by Governor Ahmed Pasha was relieved."},
 "Akderbend (1733)": {"turkic_cmd": "Topal Osman Paşa",
        "dispute": "Nâdir Şah maddesi Aralık, Topal Osman Paşa maddesi Kasım 1733 der.",
        "note": "Kışlağa çekilen ordunun askeri büyük ölçüde terhis edilmişti; Topal Osman Paşa savaş sırasında öldü ve Kerkük'te gömüldü.",
        "note_en": "Much of the army had been dismissed for the winter; Topal Osman Pasha died during the battle and was buried at Kirkuk."},
 "Özü'nün kaybı (1737)": {"note": "Bender seraskeri Abdullah Paşa'nın gönderdiği 3000 askerden başka yardım gelmedi.",
        "note_en": "No help arrived beyond the 3,000 men sent by Abdullah Pasha, commander at Bender."},
 "Mehâdiye (1738)": {"turkic_cmd": "Yeğen Mehmed Paşa, Hacı İvaz Mehmed Paşa"},
 "Hisarcık (1739)": {"date": "1739-07-22"},
 "Musul (1743)": {"turkic_cmd": "Musul Valisi Hüseyin Celil Paşa",
        "note": "En şiddetli hücum 4 Ekim 1743'te yapıldı; kale düşmedi.", "note_en": "The fiercest assault came on 4 October 1743; the fortress held."},
 "Hotin (1769)": {"turkic_cmd": "Moldovancı Ali Paşa"},
 "Kartal (1770)": {"turkic_cmd": "Sadrazam İvazzâde Halil Paşa", "status": "kesin",
        "dispute": "İvazzâde Halil Paşa maddesi savaşı \"Kartal (Larga) Muharebesi\" diye adlandırır ve 2 Ağustos 1770 tarihini verir; Larga ayrı bir savaştır (Temmuz 1770).",
        "note": "Serdâr-ı ekrem olarak kumanda eden sadrazam yenilip ordugâhı terk etmek zorunda kaldı.",
        "note_en": "The grand vizier, commanding in person, was defeated and had to abandon his camp."},
 "Kozluca (1774)": {"date": "1774-06-25"}}

# Eksik turu: Kırım Hanlığı'nın Osmanlı savaşları içindeki muharebeleri (KARARLAR: borderline)
KIRIM = {
 "Azak'ın kaybı (1736)": [("Kırım'ın istilâsı (1736)", "Russian invasion of Crimea (1736)", "1736-07", W3, "Orkapı, Gözleve, Bahçesaray", 45.60, 33.80, "region", "Ukrayna",
  "Rusya", "Kırım Hanlığı (Osmanlı tâbiiyetinde)", "", "Burkhard Christoph von Münnich", "dis", "L", "borderline",
  ["TDVIA:mahmud-i--osmanli"], "", "13 Temmuz 1736'ya kadar Ruslar Orkapı ve Gözleve'yi aldı, Bahçesaray ve Akmescid'i tahrip etti. Kırım Hanlığı kaydı (KARARLAR).",
  "By 13 July 1736 the Russians had taken Perekop and Gözleve and devastated Bakhchisaray and Akmescit. Crimean Khanate record (see KARARLAR).", "land")],
 "Banaluka (1737)": [("Kırım'ın istilâsı (1737)", "Russian invasion of Crimea (1737)", "1737", W3, "Kırım", 45.30, 34.10, "region", "Ukrayna",
  "Rusya", "Kırım Hanlığı (Osmanlı tâbiiyetinde)", "", "Peter Lacy", "dis", "L", "borderline",
  ["TDVIA:kirim"], "", "Ruslar Lascy idaresinde 1737'de yeniden gelip tahribatı sürdürdü. Kırım Hanlığı kaydı (KARARLAR). (Kontrol turunda eklendi.)",
  "The Russians returned under Lacy in 1737 and continued the devastation. Crimean Khanate record (see KARARLAR).", "land")],
 "Niş (1737)": [("Dinyester (1738)", "Repulse of the Russians on the Dniester (1738)", "1738", W3, "Dinyester", 46.85, 29.60, "region", "Moldova",
  O, "Rusya", "", "", "dis", "W", "kesin",
  ["TDVIA:mahmud-i--osmanli"], "", "Dinyester'i geçmek isteyen Ruslar 1738 başlarında püskürtüldü. (Kontrol turunda eklendi.)",
  "The Russians trying to cross the Dniester were repulsed in early 1738.", "land"),
  ("Azak denizi (1738)", "Destruction of the Russian Azov flotilla (1738)", "1738", W3, "Azak denizi ve Karadeniz", 45.80, 36.50, "region", "Rusya / Ukrayna",
  O, "Rusya", "Kaptanıderyâ Süleyman Paşa", "", "dis", "W", "kesin",
  ["TDVIA:mahmud-i--osmanli"], "", "Azak'tan Karadeniz'e çıkan Rus donanması Kaptanıderyâ Süleyman Paşa kumandasındaki Osmanlı filosu tarafından yakıldı. (Kontrol turunda eklendi.)",
  "The Russian flotilla sailing from Azov into the Black Sea was burned by the Ottoman fleet under Grand Admiral Süleyman Pasha.", "sea"),
  ("Kırım'ın istilâsı (1738)", "Russian invasion of Crimea (1738)", "1738", W3, "Kırım", 45.30, 34.10, "region", "Ukrayna",
  "Rusya", "Kırım Hanlığı (Osmanlı tâbiiyetinde)", "", "Peter Lacy", "dis", "L", "borderline",
  ["TDVIA:kirim"], "", "Ruslar Lascy idaresinde 1738'de de gelip tahribatı sürdürdü. Kırım Hanlığı kaydı (KARARLAR). (Kontrol turunda eklendi.)",
  "The Russians came again under Lacy in 1738 and continued the devastation. Crimean Khanate record (see KARARLAR).", "land")],
}
recs = []
RR = []
for r in R:
    RR.append(r)
    RR += KIRIM.get(r[0], [])
for i, r in enumerate(RR, 1):
    (ntr, nen, date, war, place, lat, lon, loc, country, sa, sb, tc, oc, cat, res, status, src, disp, note, note_en, typ) = r
    rec = {"id": i, "name_tr": ntr, "name_en": nen, "date": date, "hijri": "", "type": typ, "war": war, "place": place,
           "lat": lat, "lon": lon, "loc": loc, "country": country, "side_a": sa, "side_b": sb, "turkic_cmd": tc, "opp_cmd": oc,
           "category": cat, "result": res, "status": status, "sources": src,
           "verify": {"tdvia": True, "tdvia2": len([s for s in src if s.startswith("TDVIA:")]) >= 2, "wp": False, "rom": False, "academic": False},
           "state": O, "home_batch": HB}
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    rec["sources"] += [x for x in EXTRA_SRC.get(ntr, []) if x not in rec["sources"]]
    rec.update(FIX.get(ntr, {}))
    rec["verify"]["tdvia2"] = len([x for x in rec["sources"] if x.startswith("TDVIA:")]) >= 2
    recs.append(rec)

pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 13 — Osmanlı: Lâle Devri'nden Küçük Kaynarca'ya (1718–1774)", "compiled": "2026-10-29", "status": "İkinci kaynak turu yapıldı.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "osmanli-1718-1774.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
