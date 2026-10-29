"""data/osmanli-1812-1839.json dosyasını üretir (Parti 15: II. Mahmud dönemi, 1812–1839)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "osmanli-1812-1839"
O = "Osmanlı Devleti"
WS = "Birinci Sırp isyanı (1804–1813)"
WV = "Vehhâbî seferi (1811–1818)"
WT = "Tepedelenli Ali Paşa isyanı (1820–1822)"
WY = "Yunan isyanı (1821–1829)"
WR = "Osmanlı–Rus savaşı (1828–1829)"
WA = "Fransa'nın Cezayir'i işgali (1830–1837)"
WB = "Arnavutluk ve Bosna isyanları (1831)"
WM = "Mehmed Ali Paşa isyanı (1831–1840)"
RU, FR = "Rusya", "Fransa"
REB = "Rum isyancıları"
VH = "Dir‘iye Emirliği (Vehhâbîler)"
MI = "Mısır Valisi Mehmed Ali Paşa kuvvetleri"
CZ = "Osmanlı Devleti (Cezayir)"
# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür)
R = [
("Mekke ve Medine'nin geri alınışı (1812–1813)", "Ottoman–Egyptian recovery of Mecca and Medina (1812–1813)", "1813", WV, "Medine ve Mekke", 22.90, 39.70, "region", "Suudi Arabistan",
 O, VH, "Tosun Paşa", "", "dis", "W", "kesin",
 ["TDVIA:vehhabilik", "TDVIA:taif"], "", "1811'de yola çıkan Mısır kuvvetleri 1813'e kadar iki şehri yeniden Osmanlı yönetimine aldı.",
 "The Egyptian forces that set out in 1811 brought both cities back under Ottoman rule by 1813.", "land"),
("Tâif (1813)", "Recapture of Taif (1813)", "1813-05-02", WV, "Tâif", 21.27, 40.42, "known", "Suudi Arabistan",
 O, VH, "Tosun Paşa", "", "dis", "W", "kesin",
 ["TDVIA:taif"], "", "", "", "land"),
("Belgrad'ın geri alınışı (1813)", "Ottoman recapture of Belgrade (1813)", "1813-10-03", WS, "Belgrad", 44.82, 20.45, "known", "Sırbistan",
 O, "Sırp isyancıları", "Sadrazam Hurşid Ahmed Paşa", "Kara Yorgi", "dis", "W", "kesin",
 ["TDVIA:hursid-ahmed-pasa", "TDVIA:sirbistan"], "", "İsyan bastırıldı; ordu Belgrad Kalesi'ne direnişsiz girdi, Kara Yorgi Avusturya'ya kaçtı.",
 "The revolt was crushed; the army entered Belgrade fortress unopposed and Karađorđe fled to Austria.", "land"),
("Dir‘iye (1818)", "Siege of Diriyah (1818)", "1818-09-09", WV, "Dir‘iye", 24.73, 46.57, "known", "Suudi Arabistan",
 O, VH, "İbrâhim Paşa (Kavalalı)", "Abdullah b. Suûd", "dis", "W", "kesin",
 ["TDVIA:kavalali-mehmed-ali-pasa", "TDVIA:ibrahim-pasa-kavalali", "TDVIA:vehhabilik", "TDVIA:lahsa"], "",
 "6 Nisan'da başlayan beş aylık kuşatmadan sonra alındı; Vehhâbî reisi Abdullah b. Suûd İstanbul'a götürülüp idam edildi.",
 "Taken after a five-month siege begun on 6 April; the Wahhabi leader Abdullah ibn Saud was taken to Istanbul and executed.", "land"),
("Yanya (1820–1822)", "Siege of Ioannina (1820–1822)", "1822-02-14", WT, "Yanya", 39.66, 20.85, "known", "Yunanistan",
 O, "Tepedelenli Ali Paşa", "Hurşid Ahmed Paşa", "Tepedelenli Ali Paşa", "ic", "C", "kesin",
 ["TDVIA:tepedelenli-ali-pasa", "TDVIA:hursid-ahmed-pasa"], "", "Kıstırılan Ali Paşa göldeki Pandeleimon Manastırı'na sığındı; 14 Şubat 1822'de çıkan çatışmada öldürüldü.",
 "Cornered, Ali Pasha took refuge in the Pandeleimon monastery on the lake; he was killed in the clash of 14 February 1822.", "land"),
("Navarin Kalesi (1821)", "Siege of Navarino (1821)", "1821-08", WY, "Navarin", 36.91, 21.70, "known", "Yunanistan",
 REB, O, "", "", "dis", "L", "kesin",
 ["TDVIA:navarin"], "", "Dört ay dayanan kale yardım gelmeyince teslim oldu.", "After holding out four months without relief the fortress surrendered.", "land"),
("Sakız (1822)", "Chios revolt (1822)", "1822-04", WY, "Sakız adası", 38.37, 26.14, "known", "Yunanistan",
 O, REB, "Kaptanıderyâ Nasuhzâde Ali Paşa", "", "dis", "W", "kesin",
 ["TDVIA:sakiz-adasi"], "", "Sisam ve İpsara'dan gelen isyancılar kaleyi 23 Mart–11 Nisan arasında kuşattı; donanmanın ve takviyenin gelişiyle isyan bastırıldı.",
 "Rebels from Samos and Psara besieged the castle from 23 March to 11 April; the revolt was put down when the fleet and reinforcements arrived.", "land"),
("Gördüs (1822)", "Fall of Corinth (1822)", "1822", WY, "Gördüs", 37.94, 22.93, "known", "Yunanistan",
 REB, O, "Kâmil Bey", "", "dis", "L", "kesin",
 ["TDVIA:gordus"], "", "Kâmil Bey esir alındı.", "Kâmil Bey was taken prisoner.", "land"),
("Mesolongi (1826)", "Third siege of Missolonghi", "1826-04-23", WY, "Mesolongi (Mesleng)", 38.37, 21.43, "known", "Yunanistan",
 O, REB, "Reşid Mehmed Paşa, İbrâhim Paşa (Kavalalı)", "", "dis", "W", "kesin",
 ["TDVIA:ibrahim-pasa-kavalali", "TDVIA:resid-mehmed-pasa", "TDVIA:husrev-pasa-koca"], "",
 "Reşid Paşa Ağustos 1825'te kara tarafından kuşattı; İbrâhim Paşa'nın katılmasıyla isyancıların son direniş yeri alındı.",
 "Reşid Pasha invested it from the land side in August 1825; with İbrahim Pasha joining, the rebels' last stronghold was taken.", "land"),
("Navarin (1827)", "Battle of Navarino", "1827-10-20", WY, "Navarin limanı", 36.93, 21.69, "known", "Yunanistan",
 "İngiltere, Fransa ve Rusya", O, "", "Edward Codrington", "dis", "L", "kesin",
 ["TDVIA:navarin", "TDVIA:mahmud-ii--osmanli", "TDVIA:husrev-pasa-koca"], "",
 "Savaş hali yokken limandaki Osmanlı-Mısır donanmasına âni baskın yapıldı; elli iki gemi ve 6000 denizci kaybedildi.",
 "With no state of war, the Ottoman–Egyptian fleet in the harbour was suddenly attacked; fifty-two ships and 6,000 sailors were lost.", "sea"),
("Varna (1828)", "Siege of Varna (1828)", "1828-10", WR, "Varna", 43.21, 27.92, "known", "Bulgaristan",
 RU, O, "Sadrazam Dârendeli İzzet Mehmed Paşa", "Çar I. Nikola", "dis", "L", "kesin",
 ["TDVIA:varna", "TDVIA:resid-mehmed-pasa"], "", "Üç aylık kuşatmadan sonra alındı; sadrazam bu başarısızlık yüzünden azledildi.",
 "Taken after a three-month siege; the grand vizier was dismissed over the failure.", "land"),
("Kars (1828)", "Siege of Kars (1828)", "1828", WR, "Kars", 40.60, 43.10, "known", "Türkiye",
 RU, O, "", "", "dis", "L", "kesin",
 ["TDVIA:kars"], "", "Şehir işgal edilip tahrip edildi.", "The town was occupied and devastated.", "land"),
("Kulevçe (1829)", "Battle of Kulevcha", "1829-06", WR, "Külefçe Boğazı, Şumnu yakını", 43.13, 27.25, "approx", "Bulgaristan",
 RU, O, "Sadrazam Reşid Mehmed Paşa", "Hans Karl von Diebitsch", "dis", "L", "kesin",
 ["TDVIA:resid-mehmed-pasa"], "", "", "", "land"),
("Silistre (1829)", "Siege of Silistra (1829)", "1829", WR, "Silistre", 44.12, 27.26, "known", "Bulgaristan",
 RU, O, "", "", "dis", "L", "borderline",
 ["TDVIA:silistre"], "Silistre maddesi kalenin \"1827-1828 savaşı esnasında\" alındığını yazar; Edirne Antlaşması maddesine göre Ruslar Silistre'de 1836'ya kadar kaldı.",
 "Madde yalnızca kalenin alındığını anar.", "The article only states that the fortress was taken.", "land"),
("Erzurum (1829)", "Fall of Erzurum (1829)", "1829-07-08", WR, "Erzurum", 39.90, 41.27, "known", "Türkiye",
 RU, O, "", "İvan Paskeviç", "dis", "L", "kesin",
 ["TDVIA:erzurum"], "", "Edirne Antlaşması ile geri verildi (14 Eylül 1829).", "Returned under the Treaty of Edirne (14 September 1829).", "land"),
("Edirne (1829)", "Russian occupation of Edirne (1829)", "1829-08-22", WR, "Edirne", 41.68, 26.56, "known", "Türkiye",
 RU, O, "", "", "dis", "L", "borderline",
 ["TDVIA:edirne-antlasmasi", "TDVIA:mahmud-ii--osmanli"], "", "Rus kuvvetleri direnişle karşılaşmadan şehre girdi, Kırklareli ve Lüleburgaz'ı da işgal etti.",
 "Russian forces entered the city without resistance and also occupied Kırklareli and Lüleburgaz.", "land"),
("Cezayir (1830)", "Invasion of Algiers (1830)", "1830-07-05", WA, "Cezayir", 36.77, 3.06, "known", "Cezayir",
 FR, CZ, "Dayı Hüseyin Paşa", "", "dis", "L", "kesin",
 ["TDVIA:cezayir", "TDVIA:mahmud-ii--osmanli", "TDVIA:cezayirli-huseyin-pasa"], "", "1827'den beri abluka altındaki şehre çıkan Fransızlar 5 Temmuz'da işgal etti; dayı teslim oldu.",
 "The French, who had blockaded the city since 1827, landed and occupied it on 5 July; the dey surrendered.", "land"),
("Babuna (1831)", "Battle of Babuna (1831)", "1831-04-21", WB, "Babuna dağları, Pirlepe yakını", 41.40, 21.55, "approx", "Kuzey Makedonya",
 O, "Buşatlı Mustafa Paşa", "Sadrazam Reşid Mehmed Paşa", "Buşatlı Mustafa Paşa", "ic", "C", "kesin",
 ["TDVIA:resid-mehmed-pasa"], "", "Nizâmiye askerine karşı çıkan İşkodra valisi hezimete uğratıldı.", "The governor of Shkodër, who opposed the new army, was routed.", "land"),
("Priştine (1831)", "Battle near Pristina (1831)", "1831-07", WB, "Priştine yöresi", 42.66, 21.17, "approx", "Kosova",
 "Bosna âyanı (Boşnaklar)", O, "Sadrazam Reşid Mehmed Paşa", "", "ic", "C", "kesin",
 ["TDVIA:resid-mehmed-pasa"], "", "Boşnaklar sadrazam karşısında başarı kazandı.", "The Bosnians prevailed against the grand vizier.", "land"),
("Zerrâa (1832)", "Battle of Zerrâa (1832)", "1832-04-14", WM, "Zerrâa mevkii, Suriye", 34.40, 36.00, "region", "Suriye",
 MI, O, "", "İbrâhim Paşa (Kavalalı)", "ic", "C", "kesin",
 ["TDVIA:ibrahim-pasa-kavalali"], "", "İbrâhim Paşa'nın Osmanlı kuvvetleriyle ilk karşılaşması.", "İbrahim Pasha's first encounter with Ottoman forces.", "land"),
("Akkâ (1832)", "Siege of Acre (1831–1832)", "1832-05-27", WM, "Akkâ", 32.92, 35.07, "known", "İsrail",
 MI, O, "Akkâ Valisi Abdullah Paşa", "İbrâhim Paşa (Kavalalı)", "ic", "C", "kesin",
 ["TDVIA:kavalali-mehmed-ali-pasa", "TDVIA:ibrahim-pasa-kavalali", "TDVIA:akka"], "", "Altı aylık kuşatmadan sonra teslim oldu.", "Surrendered after a six-month siege.", "land"),
("Belen (1832)", "Battle of Beylan", "1832-07-29", WM, "Belen geçidi", 36.49, 36.22, "known", "Türkiye",
 MI, O, "Ağa Hüseyin Paşa", "İbrâhim Paşa (Kavalalı)", "ic", "C", "kesin",
 ["TDVIA:ibrahim-pasa-kavalali"], "", "Halep'in alınmasından (15 Temmuz) sonra yapıldı.", "Fought after the capture of Aleppo (15 July).", "land"),
("Konya (1832)", "Battle of Konya", "1832-12-21", WM, "Konya", 37.87, 32.49, "known", "Türkiye",
 MI, O, "Sadrazam Reşid Mehmed Paşa", "İbrâhim Paşa (Kavalalı)", "ic", "C", "kesin",
 ["TDVIA:mahmud-ii--osmanli", "TDVIA:ibrahim-pasa-kavalali", "TDVIA:resid-mehmed-pasa", "TDVIA:konya"], "",
 "Osmanlı ordusu dağıldı, sadrazam esir düştü; Mısır kuvvetleri Kütahya'ya kadar ilerledi (2 Şubat 1833).",
 "The Ottoman army broke up and the grand vizier was captured; the Egyptian forces advanced as far as Kütahya (2 February 1833).", "land"),
("Kostantîne (1836)", "First siege of Constantine (1836)", "1836", WA, "Kostantîne", 36.37, 6.61, "known", "Cezayir",
 CZ, FR, "Kostantîne Emîri Ahmed Bey", "", "dis", "W", "borderline",
 ["TDVIA:cezayir"], "", "Fransızlar Ahmed Bey karşısında ağır kayıplarla yenildi. Kostantîne Emîri Ahmed Bey dayının teslim olmasından sonra da mücadeleyi sürdürdü; Osmanlı adına savaştığı açık olmadığından kayıt borderline.",
 "The French were defeated by Ahmed Bey with heavy losses. Ahmed Bey, emir of Constantine, kept fighting after the dey surrendered; as it is unclear that he fought on the Ottoman side, the record is borderline.", "land"),
("Kostantîne (1837)", "Siege of Constantine (1837)", "1837-10-13", WA, "Kostantîne", 36.37, 6.61, "known", "Cezayir",
 FR, CZ, "Kostantîne Emîri Ahmed Bey", "", "dis", "L", "borderline",
 ["TDVIA:cezayir"], "", "Fransızlar batıdaki kuvvetlerini doğuya getirip şehri aldı.", "The French moved their western forces east and took the city.", "land"),
("Nizip (1839)", "Battle of Nezib", "1839-06-24", WM, "Nizip, Birecik yakını", 37.01, 37.79, "approx", "Türkiye",
 MI, O, "Hâfız Paşa", "İbrâhim Paşa (Kavalalı)", "ic", "C", "kesin",
 ["TDVIA:mahmud-ii--osmanli", "TDVIA:kavalali-mehmed-ali-pasa", "TDVIA:ibrahim-pasa-kavalali", "TDVIA:birecik"], "",
 "Kurmayında Moltke gibi Prusyalı subaylar bulunan Osmanlı ordusu yenildi; Anadolu yolu yeniden açıldı.",
 "The Ottoman army, whose staff included Prussian officers such as Moltke, was defeated, reopening the road into Anatolia.", "land"),
]

LEFT = [
 {"name": "Tripoliçe (1821) ve Mora'daki diğer kaleler", "reason": "Tripoliçe maddesi yalnızca 1825'te savaşsız geri alındığını yazar; düşüş tarihi indirilen maddelerde yok.", "source": "TDVIA:tripolice"},
 {"name": "Dervenaki (1822), Dramalı Mahmud Paşa", "reason": "TDVİA'da adıyla bulunamadı.", "source": ""},
 {"name": "Atina (1826–1827)", "reason": "Atina maddesi kalenin Reşid Paşa tarafından kurtarıldığını tarihsiz anar.", "source": "TDVIA:atina"},
 {"name": "Osmanlı–İran savaşı (1821–1823)", "reason": "Erzurum maddesi yalnızca barışı anar; savaşlar indirilen maddelerde yok.", "source": "TDVIA:erzurum"},
 {"name": "Bosna isyanının diğer çatışmaları (Hüseyin Kapudan, 1831–1832)", "reason": "Bosna-Hersek maddesinde ayrıntı bulunamadı.", "source": "TDVIA:resid-mehmed-pasa"},
 {"name": "Vehhâbî seferinin diğer savaşları (Turabe, Bîşe, er-Res)", "reason": "Kavalalı ve İbrâhim Paşa maddeleri toplu anlatır.", "source": "TDVIA:ibrahim-pasa-kavalali"},
 {"name": "Humus (1832)", "reason": "TDVİA'da adıyla bulunamadı.", "source": ""},
 {"name": "Vak‘a-i Hayriyye (1826)", "reason": "Yeniçeriliğin kaldırılması; savaş sayılmadı.", "source": "TDVIA:mahmud-ii--osmanli"},
]

recs = []
for i, r in enumerate(R, 1):
    (ntr, nen, date, war, place, lat, lon, loc, country, sa, sb, tc, oc, cat, res, status, src, disp, note, note_en, typ) = r
    rec = {"id": i, "name_tr": ntr, "name_en": nen, "date": date, "hijri": "", "type": typ, "war": war, "place": place,
           "lat": lat, "lon": lon, "loc": loc, "country": country, "side_a": sa, "side_b": sb, "turkic_cmd": tc, "opp_cmd": oc,
           "category": cat, "result": res, "status": status, "sources": src,
           "verify": {"tdvia": True, "tdvia2": len([s for s in src if s.startswith("TDVIA:")]) >= 2, "wp": False, "rom": False, "academic": False},
           "state": O, "home_batch": HB}
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    recs.append(rec)

pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 15 — Osmanlı: II. Mahmud dönemi (1812–1839)", "compiled": "2026-10-29", "status": "İlk tur.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "osmanli-1812-1839.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
