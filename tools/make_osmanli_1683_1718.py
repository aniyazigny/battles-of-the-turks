"""data/osmanli-1683-1718.json dosyasını üretir (Parti 12: Kutsal İttifak savaşları, Prut ve Pasarofça, 1683–1718)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "osmanli-1683-1718"
O = "Osmanlı Devleti"
HL = "Osmanlı–Kutsal İttifak savaşı (1683–1699)"
# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür)
R = [
("Uyvar'ın kaybı (1685)", "Siege of Érsekújvár (1685)", "1685-08-19", HL, "Uyvar", 47.99, 18.16, "known", "Slovakya",
 "Habsburglar", O, "", "", "dis", "L", "kesin",
 ["TDVIA:uyvar"], "", "7 Temmuz'da başlayan kuşatmayla bölgedeki Osmanlı varlığı sona erdi.", "The siege begun on 7 July ended the Ottoman presence in the region.", "land"),
("Budin'in kaybı (1686)", "Siege of Buda (1686)", "1686-09-02", HL, "Budin", 47.50, 19.04, "known", "Macaristan",
 "Kutsal İttifak (Habsburglar ve müttefikleri)", O, "Abdurrahman Abdi Paşa (öldü)", "Lothringen Dükü Karl", "dis", "L", "kesin",
 ["TDVIA:budin"], "", "Genel hücumla alındı; son Budin beylerbeyi şehid düştü.", "Taken by a general assault; the last governor of Buda was killed.", "land"),
("Mohaç (1687)", "Battle of Mohács (1687)", "1687-08-12", HL, "Mohaç ovası (Harsány dağı)", 45.86, 18.40, "approx", "Macaristan",
 "Habsburglar", O, "Sarı Süleyman Paşa", "Lothringen Dükü Karl", "dis", "L", "kesin",
 ["TDVIA:varadin", "TDVIA:mehmed-iv"], "", "Yenilginin ardından ordu ayaklandı ve IV. Mehmed tahttan indirildi.", "The defeat led to an army revolt and the deposition of Mehmed IV.", "land"),
("Belgrad'ın kaybı (1688)", "Siege of Belgrade (1688)", "1688", HL, "Belgrad", 44.82, 20.45, "known", "Sırbistan",
 "Habsburglar", O, "", "Bavyera Elektörü Maximilian Emanuel", "dis", "L", "kesin",
 ["TDVIA:belgrad"], "", "", "", "land"),
("Niş'in kaybı (1689)", "Loss of Niš (1689)", "1689-09-25", HL, "Niş", 43.32, 21.90, "known", "Sırbistan",
 "Habsburglar", O, "", "Baden Uçbeyi Ludwig Wilhelm", "dis", "L", "kesin",
 ["TDVIA:suleyman-ii"], "", "Ardından Eflak istilâ edildi.", "Wallachia was overrun afterwards.", "land"),
("Vidin'in kaybı (1689)", "Loss of Vidin (1689)", "1689-10", HL, "Vidin", 43.99, 22.88, "known", "Bulgaristan",
 "Habsburglar", O, "", "Baden Uçbeyi Ludwig Wilhelm", "dis", "L", "borderline",
 ["TDVIA:vidin"], "", "Savaşmadan ele geçirildi.", "Taken without a fight.", "land"),
("Niş (1690)", "Recapture of Niš (1690)", "1690-09", HL, "Niş", 43.32, 21.90, "known", "Sırbistan",
 O, "Habsburglar", "Köprülüzâde Fâzıl Mustafa Paşa", "", "dis", "W", "kesin",
 ["TDVIA:nis", "TDVIA:kopruluzade-fazil-mustafa-pasa"], "", "Üç hafta süren kuşatmadan sonra geri alındı.", "Retaken after a three-week siege.", "land"),
("Belgrad'ın geri alınışı (1690)", "Siege of Belgrade (1690)", "1690-10-08", HL, "Belgrad", 44.82, 20.45, "known", "Sırbistan",
 O, "Habsburglar", "Köprülüzâde Fâzıl Mustafa Paşa", "", "dis", "W", "kesin",
 ["TDVIA:suleyman-ii", "TDVIA:belgrad", "TDVIA:kopruluzade-fazil-mustafa-pasa"], "", "Sekiz günde geri alındı; Vidin, Semendire ve diğer kaleler de alındı.", "Retaken in eight days; Vidin, Smederevo and other fortresses were also recovered.", "land"),
("Salankamen (1691)", "Battle of Slankamen", "1691-08-19", HL, "Salankamen", 45.14, 20.25, "approx", "Sırbistan",
 "Habsburglar", O, "Köprülüzâde Fâzıl Mustafa Paşa (öldü)", "Baden Uçbeyi Ludwig Wilhelm", "dis", "L", "kesin",
 ["TDVIA:kopruluzade-fazil-mustafa-pasa", "TDVIA:ahmed-ii"], "", "Sadrazam askeri cesaretlendirmek için öne çıkınca vuruldu; ordu dağıldı.", "The grand vizier was shot while leading from the front; the army dispersed.", "land"),
("Belgrad müdafaası (1693)", "Siege of Belgrade (1693)", "1693-09-12", HL, "Belgrad", 44.82, 20.45, "known", "Sırbistan",
 O, "Habsburglar", "", "Duc de Croÿ", "dis", "W", "kesin",
 ["TDVIA:ahmed-ii"], "", "Osmanlı ordusu yaklaşınca Habsburg kuşatması kaldırıldı.", "The Habsburg siege was lifted as the Ottoman army approached.", "land"),
("Varadin kuşatması (1694)", "Siege of Petrovaradin (1694)", "1694-10-04", HL, "Varadin (Petrovaradin)", 45.25, 19.86, "known", "Sırbistan",
 "Habsburglar", O, "Sürmeli Ali Paşa", "", "dis", "L", "kesin",
 ["TDVIA:varadin", "TDVIA:ahmed-ii"], "", "Yirmi iki gün süren çarpışmalardan sonuç alınamadı.", "Twenty-two days of fighting brought no result.", "land"),
("Sakız'ın kaybı (1694)", "Loss of Chios (1694)", "1694", HL, "Sakız adası", 38.37, 26.14, "known", "Yunanistan",
 "Venedik", O, "", "", "dis", "L", "borderline",
 ["TDVIA:mustafa-ii"], "", "Madde yalnızca adanın Venediklilerin eline düştüğünü anar.", "The article only mentions that the island fell to Venice.", "land"),
("Sakız (1695)", "Recapture of Chios (1695)", "1695-02", HL, "Sakız adası", 38.37, 26.14, "known", "Yunanistan",
 O, "Venedik", "Mezemorta Hüseyin Paşa", "", "dis", "W", "kesin",
 ["TDVIA:mustafa-ii"], "", "Geri alınış Edirne'de şenliklerle kutlandı.", "The recapture was celebrated with festivities at Edirne.", "sea"),
("Azak müdafaası (1695)", "First siege of Azov (1695)", "1695", HL, "Azak", 47.11, 39.42, "known", "Rusya",
 O, "Rusya", "Kaplan Giray, Kefe Beylerbeyi Mustafa Paşa", "I. Petro", "dis", "W", "kesin",
 ["TDVIA:azak", "TDVIA:mustafa-ii"], "", "Doksan beş gün süren Rus kuşatması başarısız kaldı.", "The 95-day Russian siege failed.", "land"),
("Lipova (1695)", "Capture of Lipova (1695)", "1695-09", HL, "Lipova", 46.09, 21.69, "known", "Romanya",
 O, "Habsburglar", "II. Mustafa, Elmas Mehmed Paşa", "", "dis", "W", "kesin",
 ["TDVIA:elmas-mehmed-pasa"], "", "", "", "land"),
("Lugos (1695)", "Battle of Lugos (1695)", "1695-09", HL, "Tımış suyu kenarı (Lugos)", 45.69, 21.90, "approx", "Romanya",
 O, "Habsburglar", "II. Mustafa, Elmas Mehmed Paşa", "Federico Veterani (öldü)", "dis", "W", "kesin",
 ["TDVIA:mustafa-ii", "TDVIA:elmas-mehmed-pasa"], "", "Padişahın da katıldığı savaşta Veterani öldü.", "Veterani was killed in a battle at which the sultan was present.", "land"),
("Azak'ın kaybı (1696)", "Second siege of Azov (1696)", "1696-08-06", HL, "Azak", 47.11, 39.42, "known", "Rusya",
 "Rusya", O, "", "I. Petro", "dis", "L", "kesin",
 ["TDVIA:azak", "TDVIA:mustafa-ii"], "", "Don'da kurulan donanmayla karadan ve denizden kuşatıldı.", "Besieged by land and by a fleet built on the Don.", "land"),
("Ulaş (1696)", "Battle of Ulaş (1696)", "1696-08-27", HL, "Ulaş, Bega suyu kenarı", 45.60, 21.10, "approx", "Romanya",
 O, "Habsburglar", "II. Mustafa", "", "dis", "W", "kesin",
 ["TDVIA:mustafa-ii"], "", "Tımışvar kuşatmasını kaldıran Avusturyalılar yenildi.", "The Austrians, having lifted the siege of Timișoara, were defeated.", "land"),
("Zenta (1697)", "Battle of Zenta", "1697-09-11", HL, "Zenta, Tisa geçidi", 45.93, 20.08, "approx", "Sırbistan",
 "Habsburglar", O, "II. Mustafa, Elmas Mehmed Paşa (öldü)", "Savoyalı Eugène", "dis", "L", "kesin",
 ["TDVIA:zenta", "TDVIA:mustafa-ii", "TDVIA:elmas-mehmed-pasa"], "", "Tisa'yı geçerken basılan ordu bozguna uğradı; sadrazam öldü.", "The army was caught crossing the Tisza and routed; the grand vizier was killed.", "land"),
("Prut (1711)", "Pruth River Campaign", "1711-07-22", "Osmanlı–Rus savaşı (1710–1711)", "Prut nehri, Stănilești", 47.38, 27.85, "approx", "Romanya",
 O, "Rusya", "Baltacı Mehmed Paşa", "I. Petro", "dis", "W", "kesin",
 ["TDVIA:baltaci-mehmed-pasa", "TDVIA:prut-antlasmasi", "TDVIA:azak"], "", "18 Temmuz'da başlayan dört günlük çarpışmada Rus ordusu kuşatıldı; çar barış istedi ve Azak geri alındı.", "In four days of fighting from 18 July the Russian army was surrounded; the tsar sued for peace and Azov was returned.", "land"),
("Mora seferi (1715)", "Ottoman reconquest of the Morea", "1715", "Osmanlı–Venedik savaşı (1714–1718)", "Mora", 37.60, 22.40, "region", "Yunanistan",
 O, "Venedik", "Silâhdar (Şehid) Ali Paşa, Canım Hoca Mehmed Paşa", "", "dis", "W", "kesin",
 ["TDVIA:sehid-ali-pasa"], "", "Gördüs, Anabolu, Argos, Modon, Koron ve Navarin alındı; yalnızca Modon'da direniş görüldü.", "Corinth, Nauplia, Argos, Methoni, Koroni and Navarino were taken; only Methoni resisted.", "land"),
("Petervaradin (1716)", "Battle of Petrovaradin", "1716-08-05", "Osmanlı–Habsburg savaşı (1716–1718)", "Varadin (Petrovaradin)", 45.25, 19.86, "known", "Sırbistan",
 "Habsburglar", O, "Silâhdar (Şehid) Ali Paşa (öldü)", "Savoyalı Eugène", "dis", "L", "kesin",
 ["TDVIA:sehid-ali-pasa", "TDVIA:varadin", "TDVIA:pasarofca-antlasmasi"], "", "Sadrazam hücuma geçerken alnından vurularak öldü.", "The grand vizier was shot in the forehead while leading a charge.", "land"),
("Temeşvar'ın kaybı (1716)", "Siege of Temesvár (1716)", "1716-10", "Osmanlı–Habsburg savaşı (1716–1718)", "Temeşvar", 45.75, 21.23, "known", "Romanya",
 "Habsburglar", O, "", "Savoyalı Eugène", "dis", "L", "borderline",
 ["TDVIA:pasarofca-antlasmasi"], "", "Banat bölgesi ve Tımışvar Avusturya'ya geçti.", "The Banat and Timișoara passed to Austria.", "land"),
("Belgrad (1717)", "Siege of Belgrade (1717)", "1717-08", "Osmanlı–Habsburg savaşı (1716–1718)", "Belgrad", 44.82, 20.45, "known", "Sırbistan",
 "Habsburglar", O, "Hacı Halil Paşa", "Savoyalı Eugène", "dis", "L", "kesin",
 ["TDVIA:varadin", "TDVIA:pasarofca-antlasmasi"], "", "Osmanlı ordusu Belgrad önünde yenildi ve şehir düştü.", "The Ottoman army was defeated before Belgrade and the city fell.", "land"),
]

# İkinci kaynak turu (2026-10-29)
EXTRA_SRC = {"Budin'in kaybı (1686)": ["TDVIA:suleyman-pasa-sari"], "Mohaç (1687)": ["TDVIA:suleyman-pasa-sari"],
             "Sakız'ın kaybı (1694)": ["TDVIA:mezemorta-huseyin-pasa", "TDVIA:ahmed-ii"], "Sakız (1695)": ["TDVIA:mezemorta-huseyin-pasa"],
             "Temeşvar'ın kaybı (1716)": ["TDVIA:timisvar"]}
FIX = {"Budin'in kaybı (1686)": {"note": "Yetmiş sekiz günlük kuşatma sonunda genel hücumla alındı; 14 Ağustos'ta Sarı Süleyman Paşa'nın yardım hücumu yenilgiyle bitmişti. Son Budin beylerbeyi şehid düştü.",
                                 "note_en": "Taken by general assault after a 78-day siege; Sarı Süleyman Pasha's relief attack on 14 August had failed. The last governor of Buda was killed."},
       "Sakız'ın kaybı (1694)": {"date": "1694-09", "status": "ihtilafli",
           "dispute": "Mezemorta ve Mustafa II maddeleri adayı Venedik'in işgal ettiğini söyler; Ahmed II maddesi işgali Malta ve papalık gemilerine bağlar ve 21 Eylül 1695 tarihini verir (Ahmed II Şubat 1695'te ölmüştü)."},
       "Sakız (1695)": {"name_tr": "Koyunadaları ve Sakız (1695)", "name_en": "Battle of the Oinousses and recapture of Chios (1695)",
           "note": "Mezemorta Hüseyin Paşa Koyunadaları önünde Venedik donanmasını yendi; Venedik adadan çekildi.",
           "note_en": "Mezzomorto Hüseyin Pasha defeated the Venetian fleet off the Oinousses islands; Venice withdrew from Chios."},
       "Temeşvar'ın kaybı (1716)": {"status": "kesin"}}

LEFT = [
 {"name": "Mora'nın kaybı (1685–1687): Koron, Navarin, Modon, Anabolu, Atina, İnebahtı", "reason": "TDVİA Mora maddesinde tarihli savaş cümlesi bulunamadı.", "source": "TDVIA:mora"},
 {"name": "Çatalköprü (1686)", "reason": "Budin'den sonra Avusturya birliklerini takip eden kuvvetin yenilgisi; tarih verilmiyor.", "source": "TDVIA:suleyman-pasa-sari"},
 {"name": "Korfu kuşatması (1716)", "reason": "Sonuç maddede net değil.", "source": "TDVIA:sehid-ali-pasa"},
 {"name": "Bebe Süleyman isyanı (1699)", "reason": "Küçük çaplı; tarih ve yer ayrıntısı eksik.", "source": "TDVIA:mustafa-ii"},
]

# Eksik turu: Kırım Hanlığı'nın Osmanlı savaşları içindeki muharebeleri (KARARLAR: borderline)
KIRIM = {
 "Belgrad'ın kaybı (1688)": [("Orkapı (1689)", "Battle of Perekop (1689)", "1689-05-30", "Kutsal İttifak savaşları (1683–1699)", "Orkapı (Perekop)", 46.16, 33.69, "known", "Ukrayna",
  "Kırım Hanlığı (Osmanlı tâbiiyetinde)", "Rusya", "Selim Giray Han", "Vasiliy Golitsyn", "dis", "W", "borderline",
  ["TDVIA:suleyman-ii"], "", "Osmanlı ordusuyla birlikte bulunan han memleketine dönüp Rusları Orkapı'da bozguna uğrattı. Kırım Hanlığı kaydı (KARARLAR).",
  "The khan, who had been with the Ottoman army, returned home and routed the Russians at Perekop. Crimean Khanate record (see KARARLAR).", "land")],
 "Sakız (1695)": [("Lemberg akını (1695)", "Tatar raid to Lviv (1695)", "1695", "Kutsal İttifak savaşları (1683–1699)", "Lemberg (Lviv) yöresi", 49.84, 24.03, "region", "Ukrayna",
  "Kırım Hanlığı (Osmanlı tâbiiyetinde)", "Lehistan", "Şahbaz Giray", "", "dis", "W", "borderline",
  ["TDVIA:ahmed-ii", "TDVIA:mustafa-ii"], "", "1695 ilkbaharında Lehistan'a giren Şahbaz Giray Lemberg taraflarına akın etti, kralın ordusunu yendi ve çok esir ve ganimetle döndü. Kırım Hanlığı kaydı (KARARLAR).",
  "Entering Poland in spring 1695, Şahbaz Giray raided around Lviv, defeated the king's army and returned with many captives and much booty. Crimean Khanate record (see KARARLAR).", "land")],
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
meta = {"batch": "Parti 12 — Osmanlı: Kutsal İttifak savaşları, Prut ve Pasarofça (1683–1718)", "compiled": "2026-10-29", "status": "İlk tur.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "osmanli-1683-1718.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
