"""data/hun-avar-bulgar.json dosyasını üretir (Parti 24: Avrupa Hunları, Akhunlar, Avarlar ve Tuna Bulgarları, 427–834).

Kapsam kararı 2026-10-30 (erken Türk devletleri). TDVİA'da bu devletlerin müstakil maddesi yok; Akhun, Avar ve Tuna Bulgar
olayları Behrâm-ı Gûr, Sâsânîler, Mezdekiyye, Belh, Edirne, İstanbul, Bizans, Bulgar, Bulgaristan ve Dimetoka maddelerinden;
Avrupa Hun olayları Türkçe akademik yayınlardan (AKD:erkoc-447, AKD:yurdakul-2023, AKD:dingil-ilgin-2022) derlendi.
Asya Hunları (MÖ) negatif yıl gerektirdiği için şema kararı bekliyor. Tuna Bulgarları için kesim: Hıristiyanlığın kabulü (864)
öncesi; Bulgar maddesi bu tarihten sonra Slavlaştıklarını yazar."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "hun-avar-bulgar"
AH = "Avrupa Hun İmparatorluğu"
AK = "Akhunlar (Eftalitler)"
AV = "Avar Kağanlığı"
TB = "Tuna Bulgar Hanlığı"
UB = "Utigur Bulgarları"
SS = "Sâsânîler"
BZ = "Doğu Roma (Bizans)"
BR = "Batı Roma ve müttefikleri"
WAB = "Attila'nın Balkan seferleri (441–447)"
WAW = "Attila'nın Galya ve İtalya seferleri (451–452)"
WAS = "Akhun–Sâsânî savaşları (427–484)"
WBB = "Bulgar–Bizans savaşları (680–834)"

# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür, devlet)
R = [
("Rey (427)", "Bahram V's victory over the Hephthalites (427)", "427", WAS, "Rey", 35.59, 51.43, "approx", "İran",
 SS, AK, "", "Behrâm-ı Gûr", "dis", "L", "kesin",
 ["TDVIA:behram-i-gur"], "", "Bir gece baskınıyla İran sınırını geçip Hazar denizinin güneyini ele geçiren Akhunlar Rey'de yenildi ve Ceyhun gerisine atıldı.",
 "The Hephthalites, who had crossed into Iran in a night raid and seized the land south of the Caspian, were beaten at Rayy and driven beyond the Oxus.", "land", AK),
("Birinci Balkan seferi (441–443)", "Attila's first Balkan campaign (441–443)", "441", WAB, "İllirya ve Trakya (Naissus)", 43.32, 21.90, "region", "Sırbistan / Bulgaristan",
 AH, BZ, "Attila ve Bleda", "", "dis", "W", "kesin",
 ["AKD:erkoc-447"], "Bazı araştırmacılar 441 ve 443 seferlerini tek sefer sayar; Anatolius barışının tarihi 442/443 ve 447/448 arasında tartışmalıdır.",
 "Margus piskoposunun Hun mezarlarını soymasını ve antlaşmaya uyulmamasını gerekçe gösteren Attila Tuna'yı geçip İllirya'da pek çok şehri aldı; Váczy'ye göre Sirmium, Singidunum, Viminacium, Ratiaria, Naissus ve Philippopolis yerle bir edildi, Chersonesus'ta Doğu Roma ordusu bozguna uğratıldı.",
 "Citing the bishop of Margus's robbing of Hunnic graves and the broken treaty, Attila crossed the Danube and took many towns in Illyricum; per Váczy, Sirmium, Singidunum, Viminacium, Ratiaria, Naissus and Philippopolis were razed and an East Roman army was routed in the Chersonese.", "land", AH),
("Amuderya (443)", "Yazdegerd II's victory over the Hephthalites (443)", "443", WAS, "Horasan ve Amuderya", 37.50, 62.00, "region", "Türkmenistan / Afganistan",
 SS, AK, "", "II. Yezdicerd", "dis", "L", "kesin",
 ["TDVIA:sasaniler"], "", "Bizans'la barış yapan II. Yezdicerd doğuda yeniden saldırıya geçen Akhunlar'ı yenip Amuderya'nın ötesine sürdü.",
 "Having made peace with Byzantium, Yazdegerd II turned on the Hephthalites, defeated them and drove them beyond the Oxus.", "land", AK),
("Utus (447)", "Battle of the Utus", "447", WAB, "Utus (Vid) ırmağı", 43.40, 24.60, "approx", "Bulgaristan",
 AH, BZ, "Attila", "Arnegisclus", "dis", "W", "kesin",
 ["AKD:erkoc-447"], "",
 "Konstantinopolis surlarını yıkan depremin ardından sefere çıkan Attila'ya karşı Dacia Ripensis'te Utus ırmağında cesurca savaşan Magister Militum Arnegisclus, Hunlar'ın çoğu ölmesine karşın Attila tarafından öldürüldü; Attila Thermopylae'ye kadar ilerledi.",
 "After the earthquake that brought down the walls of Constantinople, Attila invaded; the magister militum Arnegisclus fought bravely on the Utus in Dacia Ripensis and, though many Huns fell, was killed by Attila, who advanced as far as Thermopylae.", "land", AH),
("Marcianopolis (447)", "Sack of Marcianopolis (447)", "447", WAB, "Marcianopolis (Devnya)", 43.22, 27.57, "approx", "Bulgaristan",
 AH, BZ, "Attila", "", "dis", "W", "kesin",
 ["AKD:erkoc-447"], "Chronicon Paschale şehrin 447'de alındığını ve Anargiscus'un öldürüldüğünü yazar ama Hunlar'ı anmaz; Váczy Marcianopolis'i Hunlar'ın yaktığı yetmiş şehir arasında sayar.",
 "Marcianopolis ve Serdica dahil yetmiş şehir yakılıp yıkıldı.", "Seventy towns, Marcianopolis and Serdica among them, were sacked.", "land", AH),
("Metz (451)", "Sack of Metz (451)", "451-04-07", WAW, "Metz (Divodurum)", 49.12, 6.18, "known", "Fransa",
 AH, BR, "Attila", "", "dis", "W", "kesin",
 ["AKD:yurdakul-2023", "AKD:dingil-ilgin-2022"], "",
 "Ren'i aşan Attila Metz'e ulaşıp şehri 7 Nisan 451'de (Paskalya) aldı; ardından kuzey Galya'yı Haziran'a kadar tahrip etti.",
 "Crossing the Rhine, Attila reached Metz and took it on 7 April 451 (Easter); he then ravaged northern Gaul until June.", "land", AH),
("Katalaunum (451)", "Battle of the Catalaunian Plains", "451-06-20", WAW, "Katalaunum düzlükleri (Campus Mauriacus)", 48.95, 4.36, "approx", "Fransa",
 AH, BR, "Attila", "Aetius, Vizigot kralı Theodoricus", "dis", "D", "ihtilafli",
 ["AKD:yurdakul-2023", "AKD:dingil-ilgin-2022"],
 "Batı kaynaklarında ve ağırlıklı görüşte Roma–Vizigot zaferi; Yurdakul (Kaçar'a dayanarak) savaşın tek kaybedeninin Attila olmadığını, Dıngıl Ilgın hiçbir tarafın kazanmadığını yazar. P6 gereği sonuç belirsiz (D).",
 "Vizigot kralı savaşta öldü; Thorismund ve Aetius bir süre ordularının komutasını yitirdi. Aetius Hunlar'ın çekilmesine engel olmadı; Attila ertesi yıl İtalya seferine çıktı.",
 "The Visigothic king fell; Thorismund and Aetius briefly lost control of their armies. Aetius did not hinder the Hunnic withdrawal, and Attila invaded Italy the next year.", "land", AH),
("Aquileia (452)", "Siege of Aquileia (452)", "452", WAW, "Aquileia", 45.77, 13.37, "known", "İtalya",
 AH, BR, "Attila", "", "dis", "W", "kesin",
 ["AKD:yurdakul-2023"], "Düşüş tarihi kesin değildir; Maenchen-Helfen Priscus'a dayanarak Ağustos sonu–Eylül başı der.",
 "Jülyen Alpleri'ni aşan Hunlar Aquileia'yı üç ay kuşatıp aldı ve yakıp yıktı; bunun üzerine öteki şehirler kapılarını açtı.",
 "Crossing the Julian Alps, the Huns besieged Aquileia for three months, took it and razed it; other towns then opened their gates.", "land", AH),
("Milano ve Ticinum (452)", "Sack of Milan and Pavia (452)", "452", WAW, "Mediolanum ve Ticinum", 45.46, 9.19, "known", "İtalya",
 AH, BR, "Attila", "", "dis", "W", "kesin",
 ["AKD:yurdakul-2023"], "", "Patavium, Concordia, Altinum, Vicentia, Verona, Brixia ve Bergomum üzerinden Po vadisinde ilerleyen Hunlar Milano'yu yağmalayıp büyük yıkıma yol açtı ve Ticinum'u aldı.",
 "Advancing up the Po valley via Patavium, Concordia, Altinum, Vicentia, Verona, Brixia and Bergomum, the Huns sacked Milan and took Ticinum.", "land", AH),
("Fîrûz'un esir düşmesi (469)", "Capture of Peroz by the Hephthalites (469)", "469", WAS, "Horasan", 36.50, 61.50, "region", "Afganistan / Türkmenistan",
 AK, SS, "", "Fîrûz", "dis", "W", "kesin",
 ["TDVIA:sasaniler"], "", "Fîrûz Akhunlar'a esir düştü ve ağır şartlarla barışa razı oldu.",
 "Peroz was captured by the Hephthalites and accepted peace on harsh terms.", "land", AK),
("Kutrigur–Utigur savaşı (482)", "Utigur–Kutrigur war (482)", "482", "Bulgar boyları arası savaş", "Karadeniz kuzeyi", 46.50, 35.00, "region", "Ukrayna / Rusya",
 UB, "Kutrigur Bulgarları", "", "", "turk_arasi", "W", "kesin",
 ["TDVIA:bulgar"], "", "Bizans imparatoru Zenon'un kışkırtmasıyla iki Bulgar boyu savaştı; yenilen Kutrigurlar'dan 2000 kadar aile Bizans hizmetine girip Trakya'ya yerleşti.",
 "Incited by Emperor Zeno, the two Bulgar tribes fought; some 2,000 families of the beaten Kutrigurs entered Byzantine service and settled in Thrace.", "land", UB),
("Fîrûz'un ölümü (484)", "Battle of Herat (484)", "484", WAS, "Doğu İran", 35.50, 62.50, "region", "Afganistan / İran",
 AK, SS, "", "Fîrûz", "dis", "W", "kesin",
 ["TDVIA:sasaniler", "TDVIA:mezdekiyye"], "",
 "Akhunlar iki yıl Doğu İran'ı yağmaladı; karşı koymaya çalışan Fîrûz'un ordusu yok edildi, kendisi öldürüldü. Sâsânîler Akhunlar'a vergi ödemek zorunda kaldı.",
 "The Hephthalites plundered eastern Iran for two years; Peroz's army was destroyed and he was killed. The Sasanians had to pay tribute.", "land", AK),
("Edirne kuşatması (586)", "Avar siege of Adrianople (586)", "586", "Avar–Bizans savaşları", "Edirne (Hadrianopolis)", 41.68, 26.56, "known", "Türkiye",
 AV, BZ, "", "", "dis", "D", "borderline",
 ["TDVIA:edirne"], "", "Edirne maddesi yalnızca şehrin Avarlar'ca muhasara edildiğini yazar; sonuç verilmez.",
 "The Edirne article only records the Avar siege; no outcome is given.", "land", AV),
("İstanbul kuşatması (626)", "Siege of Constantinople (626)", "626", "Avar–Bizans savaşları", "İstanbul", 41.01, 28.96, "known", "Türkiye",
 BZ, "Avarlar ve Sâsânîler", "", "", "dis", "L", "kesin",
 ["TDVIA:istanbul", "TDVIA:bizans", "TDVIA:sasaniler", "TDVIA:hazarlar"], "",
 "Balkanlar'ı ele geçiren Avar ve Slav orduları Boğaziçi'ne kadar ilerleyen İran ordularıyla anlaşarak İstanbul'u kuşattı; kuşatma zorlu bir direniş ve donanmanın başarısıyla atlatıldı.",
 "The Avar and Slav armies that had overrun the Balkans besieged Constantinople in concert with the Persians on the Bosporus; the siege was beaten off by stubborn resistance and the fleet.", "land", AV),
("Asparuh'un zaferi (680–681)", "Asparukh's victory over Byzantium (680–681)", "681", WBB, "Dobruca ve Trakya", 44.00, 28.20, "region", "Romanya / Bulgaristan",
 TB, BZ, "Asparuh (Esperih)", "IV. Konstantin", "dis", "W", "kesin",
 ["TDVIA:bulgar", "TDVIA:bulgaristan"], "",
 "Müslümanların İstanbul kuşatmalarından faydalanan Kutrigur Bulgarları Bizanslılar'ı yenip anlaşmaya mecbur bıraktı; imparator yıllık vergi ödemeyi kabul edip devleti tanıdı.",
 "Exploiting the Muslim sieges of Constantinople, the Kutrigur Bulgars defeated the Byzantines and forced a treaty; the emperor agreed to pay annual tribute and recognised the state.", "land", TB),
("Nîzek isyanı (709)", "Revolt of Tarkhan Nizak (709)", "709", "Emevîlerin Tohâristan fethi", "Belh", 36.76, 66.90, "known", "Afganistan",
 "Emevîler", AK, "Tarhan Nîzek", "Kuteybe b. Müslim", "dis", "L", "kesin",
 ["TDVIA:belh"], "", "Kuteybe'ye karşı ayaklanan Eftalit prensi Tarhan Nîzek Belh'i aldıysa da Kuteybe'nin gönderdiği kuvvetlere yenildi.",
 "The Hephthalite prince Tarkhan Nizak rose against Qutayba and took Balkh, but was defeated by the forces Qutayba sent.", "land", AK),
("Tervel'in Arap seferi (717–718)", "Bulgar attack on the Arab besiegers of Constantinople (717–718)", "717", "Arapların İstanbul kuşatması (717–718)", "Trakya (İstanbul önleri)", 41.10, 28.50, "region", "Türkiye",
 TB, "Emevîler", "Tervel", "", "dis", "W", "kesin",
 ["TDVIA:bulgaristan"], "", "Han Tervel Araplar'ın İstanbul'u kuşatması üzerine Trakya'da Arap güçlerine saldırarak Bizans'a yardım etti.",
 "Khan Tervel aided Byzantium by attacking the Arab forces in Thrace during their siege of Constantinople.", "land", TB),
("Avar topraklarının alınışı (805)", "Krum's conquest of the Avar lands (805)", "805", "Bulgar–Avar savaşı", "Tisa'nın doğusu", 46.50, 21.00, "region", "Macaristan / Romanya",
 TB, "Avarlar", "Krum", "", "turk_arasi", "W", "kesin",
 ["TDVIA:bulgaristan"], "", "Han Krum Tisa'nın doğusundaki Avar topraklarını ve madenlerini ele geçirdi.",
 "Khan Krum seized the Avar lands and mines east of the Tisza.", "land", TB),
("Sofya (809)", "Capture of Serdica (809)", "809", WBB, "Sofya (Sredets)", 42.70, 23.32, "known", "Bulgaristan",
 TB, BZ, "Krum", "", "dis", "W", "kesin",
 ["TDVIA:bulgaristan"], "", "", "", "land", TB),
("Nikephoros'un yenilgisi (811)", "Battle of Pliska (811)", "811", WBB, "Pliska yakını geçitler", 43.10, 26.90, "approx", "Bulgaristan",
 TB, BZ, "Krum", "I. Nikephoros", "dis", "W", "kesin",
 ["TDVIA:bizans"], "", "Bulgarlar üzerine sefere çıkan İmparator Nikephoros pusuya düşürülüp öldürüldü; devlet çok zor durumda kaldı.",
 "Emperor Nikephoros, campaigning against the Bulgars, was ambushed and killed, leaving the empire in dire straits.", "land", TB),
("Edirne (813)", "Krum's capture of Adrianople (813)", "813", WBB, "Edirne", 41.68, 26.56, "known", "Türkiye",
 TB, BZ, "Krum", "", "dis", "W", "ihtilafli",
 ["TDVIA:bulgaristan"], "Bulgaristan maddesi Edirne'nin 813'te alındığını, Edirne maddesi şehrin Bulgarlar'ca 914'te zaptedildiğini yazar.",
 "", "", "land", TB),
("Dimetoka (813)", "Krum's capture of Didymoteicho (813)", "813", WBB, "Dimetoka", 41.35, 26.50, "known", "Yunanistan",
 TB, BZ, "Krum", "", "dis", "W", "kesin",
 ["TDVIA:dimetoka"], "", "Türk/Bulgar hanı Krum şehri ele geçirdi.", "The Turkic/Bulgar khan Krum took the town.", "land", TB),
("İstanbul kuşatması (813)", "Krum's siege of Constantinople (813)", "813", WBB, "İstanbul", 41.01, 28.96, "known", "Türkiye",
 BZ, TB, "Krum", "V. Leon", "dis", "L", "kesin",
 ["TDVIA:istanbul", "TDVIA:bulgaristan"], "",
 "Bulgar ordusu İstanbul'a kadar geldi; başşehir surlarının sağlamlığı sayesinde kurtuldu. 814'teki ikinci kuşatma Krum'un ani ölümüyle sona erdi.",
 "The Bulgar army reached Constantinople; the capital was saved by its strong walls. A second siege in 814 ended with Krum's sudden death.", "land", TB),
("Filibe (c. 834)", "Malamir's capture of Philippopolis (c. 834)", "c. 834", WBB, "Filibe", 42.15, 24.75, "known", "Bulgaristan",
 TB, BZ, "Malamir", "", "dis", "W", "borderline",
 ["TDVIA:bulgaristan"], "Madde yalnızca Malamir'in hükümdarlığını (831–836) verir; yıl yaklaşıktır.",
 "Malamir Filibe'yi ele geçirdi; muharebe ayrıntısı yok.", "Malamir took Philippopolis; no battle details.", "land", TB),
]

OPP_STATE = {"Avar topraklarının alınışı (805)": AV}
# İkinci kaynak turu (2026-10-30): Uçar 2021, 811 Kroniği çevirisinin girişinde Krum'un 809'da Sofya'yı alışını, Nikephoros'un 811
# seferini ve ölümünü, ikinci fragmanın 813–814 Trakya savaşlarını ve Edirne'nin istilâsını anar.
EXTRA_SRC = {
    "Sofya (809)": ["AKD:ucar-811"],
    "Nikephoros'un yenilgisi (811)": ["AKD:ucar-811"],
    "Edirne (813)": ["AKD:ucar-811"],
    # Yurdakul 2023: 441 yazından 442 baharına süren sefer ve 443 Anatolius barışı; 447'de Marcianopolis'in alınışı
    "Birinci Balkan seferi (441–443)": ["AKD:yurdakul-2023"],
    "Marcianopolis (447)": ["AKD:yurdakul-2023"],
    # Dıngıl Ilgın 2022: 452'de Aquileia kuşatması, Venedik'ten Milano'ya kadar şehirlerin harap edilmesi
    "Aquileia (452)": ["AKD:dingil-ilgin-2022"],
    "Milano ve Ticinum (452)": ["AKD:dingil-ilgin-2022"],
    "Filibe (c. 834)": ["TDVIA:filibe"],  # Bulgar Hanı Malamir (831-836) Filibe'yi topraklarına kattı
    "Nîzek isyanı (709)": ["TDVIA:kuteybe-b-muslim", "TDVIA:toharistan"],  # isyan ve Nîzek'in ortadan kaldırılması (91/709-10)
}

LEFT = [
    {"name": "Asya Hunları (MÖ 209–MS 216)", "reason": "Kapsam dışı: MÖ tarihler alınmaz (kullanıcı kararı 2026-10-30).", "source": "TDVIA:asya"},
    {"name": "Avrupa Hunları'nın Got yenilgisi (375) ve Uldız–Rua dönemi", "reason": "Erkoç yalnızca 375 istilâsını anar; muharebe ayrıntısı için Ahmetbeyoğlu (Avrupa Hun İmparatorluğu, TTK 2001) gerekir.", "source": "AKD:erkoc-447"},
    {"name": "Orleans (451)", "reason": "Kuşatmanın olup olmadığı tartışmalı (Yurdakul).", "source": "AKD:yurdakul-2023"},
    {"name": "Kubâd'ın Akhun ordusuyla tahta dönüşü (498)", "reason": "Sâsânîler maddesine göre Câmasb savaş yapmadan tahtı bıraktı.", "source": "TDVIA:sasaniler"},
    {"name": "Akhunlar'ın Gupta ve Keşmir saldırıları (V–VI. yüzyıl)", "reason": "Hindistan ve Keşmir maddeleri toplu anar.", "source": "TDVIA:hindistan"},
    {"name": "Avarlar'ın Pannonia'yı alışı (568), Maurikios'un Avar savaşları (592–602), Singidunum", "reason": "Belgrad ve Bizans maddeleri toplu anar; karşı taraf veya sonuç yok.", "source": "TDVIA:belgrad"},
    {"name": "Tuna Bulgarları 864 sonrası (Simeon ve sonrası)", "reason": "Bulgar maddesine göre Hıristiyanlığın kabulüyle Slavlaştılar; kapsam dışı.", "source": "TDVIA:bulgar"},
]

recs = []
for i, r in enumerate(R, 1):
    (ntr, nen, date, war, place, lat, lon, loc, country, sa, sb, tc, oc, cat, res, status, src, disp, note, note_en, typ, state) = r
    src = src + [x for x in EXTRA_SRC.get(ntr, []) if x not in src]
    rec = {"id": i, "name_tr": ntr, "name_en": nen, "date": date, "hijri": "", "type": typ, "war": war, "place": place,
           "lat": lat, "lon": lon, "loc": loc, "country": country, "side_a": sa, "side_b": sb, "turkic_cmd": tc, "opp_cmd": oc,
           "category": cat, "result": res, "status": status, "sources": src,
           "verify": {"tdvia": any(x.startswith("TDVIA:") for x in src), "tdvia2": len([s for s in src if s.startswith("TDVIA:")]) >= 2, "wp": False, "rom": False, "academic": any(x.startswith("AKD:") for x in src)},
           "state": state, "home_batch": HB}
    if ntr in OPP_STATE: rec["opp_state"] = OPP_STATE[ntr]
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    recs.append(rec)

key = lambda d: re.sub(r"^(\d{3})\b", r"0\1", re.sub(r"^c\. ", "", d))
dates = [key(r["date"]) for r in recs]
assert dates == sorted(dates), [d for a, d in zip(dates, dates[1:]) if d < a]
pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 24 — Avrupa Hunları, Akhunlar, Avarlar ve Tuna Bulgarları (427–834)", "compiled": "2026-10-30", "status": "İlk tur.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "hun-avar-bulgar.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli;", sum(r["verify"]["academic"] for r in recs), "akademik")
