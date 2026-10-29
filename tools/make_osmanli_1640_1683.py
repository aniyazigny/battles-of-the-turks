"""data/osmanli-1640-1683.json dosyasını üretir (Parti 11: Sultan İbrâhim ve IV. Mehmed, Köprülüler dönemi, 1640–1683)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "osmanli-1640-1683"
O = "Osmanlı Devleti"
# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür)
R = [
("Azak (1642)", "Recovery of Azov (1642)", "1642", "Osmanlı–Don Kazakları", "Azak", 47.11, 39.42, "known", "Rusya",
 O, "Don Kazakları", "Sultanzâde Mehmed Paşa, Kırım Hanı Mehmed Giray", "", "dis", "W", "borderline",
 ["TDVIA:ibrahim--padisah"], "", "Seferi haber alan Kazaklar kaleyi terk etti.", "The Cossacks abandoned the fortress on hearing of the campaign.", "land"),
("Hanya (1645)", "Siege of Chania (1645)", "1645-08-19", "Girit savaşı (1645–1669)", "Hanya", 35.51, 24.02, "known", "Yunanistan",
 O, "Venedik", "Yûsuf Paşa", "", "dis", "W", "kesin",
 ["TDVIA:girit", "TDVIA:ibrahim--padisah"], "", "27 Haziran'da başlayan kuşatmadan sonra 19 Ağustos'ta teslim oldu (Girit maddesi: elli dört gün).", "Besieged from 27 June, it surrendered on 19 August (the Crete article says 54 days).", "land"),
("Resmo (1646)", "Siege of Rethymno (1646)", "1646-11-15", "Girit savaşı (1645–1669)", "Resmo", 35.37, 24.47, "known", "Yunanistan",
 O, "Venedik", "Deli Hüseyin Paşa", "", "dis", "W", "kesin",
 ["TDVIA:resmo"], "", "Kırk günlük kuşatmadan sonra emanla teslim alındı.", "Surrendered on terms after a forty-day siege.", "land"),
("Çanakkale (1654)", "Battle of the Dardanelles (1654)", "1654", "Girit savaşı (1645–1669)", "Çanakkale Boğazı", 40.15, 26.40, "approx", "Türkiye",
 O, "Venedik", "Kara Murad Paşa", "", "dis", "W", "kesin",
 ["TDVIA:mehmed-iv"], "", "Boğaz Osmanlı gemilerine açıldı. Yıl maddedeki olay sırasından çıkarıldı.", "The Straits were reopened to Ottoman ships. The year is inferred from the article's sequence of events.", "sea"),
("Çanakkale (1656)", "Battle of the Dardanelles (1656)", "1656-06-26", "Girit savaşı (1645–1669)", "Çanakkale Boğazı", 40.08, 26.25, "approx", "Türkiye",
 "Venedik", O, "Kenan Paşa", "Lazzaro Mocenigo", "dis", "L", "kesin",
 ["TDVIA:mehmed-iv"], "", "Büyük hezimet İstanbul'u savunmasız bıraktı; Venedikliler Bozcaada, Limni ve Semadirek'i işgal etti.", "The heavy defeat left Istanbul exposed; Venice occupied Tenedos, Lemnos and Samothrace.", "sea"),
("Bozcaada ve Limni (1657)", "Recapture of Tenedos and Lemnos (1657)", "1657-08-30", "Girit savaşı (1645–1669)", "Bozcaada", 39.83, 26.05, "known", "Türkiye",
 O, "Venedik", "Köprülü Mehmed Paşa", "", "dis", "W", "kesin",
 ["TDVIA:koprulu-mehmed-pasa", "TDVIA:bozcaada"], "", "25 Ağustos'ta karaya çıkan kuvvet kaleyi kuşattı; Venedikliler 30 Ağustos'ta adayı boşalttı. Boğazın güvenliği sağlandı.", "A force landed on 25 August and besieged the castle; the Venetians evacuated the island on 30 August. The Straits were secured.", "land"),
("Yanova (1658)", "Siege of Ineu (1658)", "1658-09", "Erdel seferi (1658)", "Yanova", 46.43, 21.84, "known", "Romanya",
 O, "Erdel (II. György Rákóczi)", "Köprülü Mehmed Paşa", "", "dis", "W", "kesin",
 ["TDVIA:yanova", "TDVIA:koprulu-mehmed-pasa"], "", "30 Ağustos'ta varılan kale anlaşmayla teslim oldu.", "The castle, reached on 30 August, surrendered on terms.", "land"),
("Ilgın (1658)", "Battle of Ilgın (1658)", "1658-12-11", "Abaza Hasan isyanı", "Ilgın", 38.28, 31.91, "approx", "Türkiye",
 "Abaza Hasan", O, "Murtaza Paşa", "Abaza Hasan Paşa", "ic", "C", "kesin",
 ["TDVIA:koprulu-mehmed-pasa", "TDVIA:abaza-hasan"], "", "Abaza kış gelince Halep'e çekildi ve orada öldürüldü.", "Abaza withdrew to Aleppo for the winter and was killed there.", "land"),
("Varad (1660)", "Siege of Várad (1660)", "1660-08", "Erdel seferi (1660)", "Varad", 47.07, 21.93, "known", "Romanya",
 O, "Erdel (II. György Rákóczi)", "Köse Ali Paşa", "", "dis", "W", "kesin",
 ["TDVIA:varad"], "Tarih: 27 Ağustos 1660 maddede Rákóczi'nin savaş açtığı gün olarak geçer; kırk beş gün süren kuşatmanın bitişi değildir.",
 "Kırk beş günlük kuşatmadan sonra teslim alındı; Varad eyaleti kuruldu.", "Surrendered after a 45-day siege; the province of Várad was created.", "land"),
("Uyvar (1663)", "Siege of Érsekújvár (1663)", "1663-09-24", "Osmanlı–Habsburg savaşı (1663–1664)", "Uyvar", 47.99, 18.16, "known", "Slovakya",
 O, "Habsburglar", "Köprülüzâde Fâzıl Ahmed Paşa", "Ádám Forgách", "dis", "W", "kesin",
 ["TDVIA:kopruluzade-fazil-ahmed-pasa", "TDVIA:uyvar"], "", "17 Ağustos'ta kuşatılan kale şartlı teslim edildi; ardından Novigrad, Nitra ve Leva alındı.", "Besieged from 17 August, the fortress surrendered on terms; Nógrád, Nitra and Léva followed.", "land"),
("Saint Gotthard (1664)", "Battle of Saint Gotthard", "1664-08-01", "Osmanlı–Habsburg savaşı (1663–1664)", "Rába nehri, Szentgotthárd", 46.95, 16.27, "approx", "Macaristan",
 "Habsburglar ve müttefikleri", O, "Köprülüzâde Fâzıl Ahmed Paşa", "Raimondo Montecuccoli", "dis", "L", "kesin",
 ["TDVIA:saint-gotthard-muharebesi", "TDVIA:kopruluzade-fazil-ahmed-pasa"], "",
 "Açık bir yenilgi; ancak Fâzıl Ahmed Paşa maddesine göre tam bir bozgun değildi ve dokuz gün sonra Vasvár Antlaşması yapıldı.", "A clear defeat, though according to the Fazıl Ahmed Pasha article not a complete rout; the Peace of Vasvár followed nine days later.", "land"),
("Kandiye (1669)", "Siege of Candia", "1669-09-06", "Girit savaşı (1645–1669)", "Kandiye", 35.34, 25.13, "known", "Yunanistan",
 O, "Venedik", "Köprülüzâde Fâzıl Ahmed Paşa", "Francesco Morosini", "dis", "W", "kesin",
 ["TDVIA:kandiye", "TDVIA:girit", "TDVIA:kopruluzade-fazil-ahmed-pasa"], "", "Son evresi 1667'de başlayan uzun kuşatma on sekiz maddelik teslim anlaşmasıyla bitti; Girit'in fethi tamamlandı.", "The long siege, whose last phase began in 1667, ended with an eighteen-article capitulation; the conquest of Crete was complete.", "land"),
("Kamaniçe (1672)", "Siege of Kamianets (1672)", "1672-08-27", "Osmanlı–Lehistan savaşı (1672–1676)", "Kamaniçe", 48.67, 26.57, "known", "Ukrayna",
 O, "Lehistan", "IV. Mehmed, Köprülüzâde Fâzıl Ahmed Paşa", "", "dis", "W", "kesin",
 ["TDVIA:kamanice", "TDVIA:kopruluzade-fazil-ahmed-pasa"], "", "Dokuz gün süren kuşatmadan sonra alındı; Bucaş Antlaşması'yla Podolya Osmanlıya geçti.", "Taken after a nine-day siege; the Treaty of Buczacz gave Podolia to the Ottomans.", "land"),
("Hotin (1673)", "Battle of Khotyn (1673)", "1673-11-10", "Osmanlı–Lehistan savaşı (1672–1676)", "Hotin", 48.52, 26.50, "known", "Ukrayna",
 "Lehistan", O, "", "Jan Sobieski", "dis", "L", "kesin",
 ["TDVIA:kopruluzade-fazil-ahmed-pasa"], "", "Eflak ve Boğdan voyvodalarının Leh tarafına geçmesiyle kale elden çıktı.", "The fortress was lost after the voivodes of Wallachia and Moldavia went over to the Polish side.", "land"),
("Human (1674)", "Capture of Uman (1674)", "1674-08", "Osmanlı–Lehistan savaşı (1672–1676)", "Human (Uman)", 48.75, 30.22, "known", "Ukrayna",
 O, "Lehistan", "Merzifonlu Kara Mustafa Paşa", "", "dis", "W", "borderline",
 ["TDVIA:merzifonlu-kara-mustafa-pasa"], "", "", "", "land"),
("İzvança (1676)", "Battle of Żurawno (1676)", "1676-10", "Osmanlı–Lehistan savaşı (1672–1676)", "İzvança (Zhuravno)", 49.25, 24.27, "known", "Ukrayna",
 O, "Lehistan", "", "Jan III Sobieski", "dis", "W", "borderline",
 ["TDVIA:mehmed-iv"], "", "Çarpışmaların ardından Leh kralı anlaşmayı kabul etti.", "After the fighting the Polish king accepted the treaty.", "land"),
("Çehrin (1677)", "First Chyhyryn campaign (1677)", "1677-08", "Osmanlı–Rus savaşı (1676–1681)", "Çehrin", 49.08, 32.66, "known", "Ukrayna",
 "Rusya ve Kazaklar", O, "Şeytan İbrâhim Paşa", "Grigory Romodanovsky", "dis", "L", "kesin",
 ["TDVIA:cehrin-seferi"], "", "Üç hafta süren sefer sonuç vermedi; birçok top düşmana kaldı.", "The three-week campaign failed; many guns were lost.", "land"),
("Çehrin (1678)", "Siege of Chyhyryn (1678)", "1678-08-21", "Osmanlı–Rus savaşı (1676–1681)", "Çehrin", 49.08, 32.66, "known", "Ukrayna",
 O, "Rusya ve Kazaklar", "Merzifonlu Kara Mustafa Paşa", "Grigory Romodanovsky", "dis", "W", "kesin",
 ["TDVIA:cehrin-seferi", "TDVIA:merzifonlu-kara-mustafa-pasa"], "", "21 Temmuz'da başlayan kuşatmanın 33. günü lağım ve genel hücumla alındı; kale yıkıldı.", "Taken on the 33rd day of the siege by mines and a general assault; the fortress was razed.", "land"),
("Viyana kuşatması (1683)", "Siege of Vienna (1683)", "1683-09-12", "Osmanlı–Kutsal İttifak savaşı (1683–1699)", "Viyana, Kahlenberg", 48.21, 16.37, "known", "Avusturya",
 "Habsburglar, Lehistan ve müttefikleri", O, "Merzifonlu Kara Mustafa Paşa", "Jan III Sobieski", "dis", "L", "kesin",
 ["TDVIA:viyana", "TDVIA:merzifonlu-kara-mustafa-pasa"], "", "14 Temmuz–12 Eylül arasındaki kuşatma Sobieski'nin kurtarma ordusuyla büyük bir bozguna döndü.", "The siege of 14 July–12 September turned into a heavy defeat when Sobieski's relief army arrived.", "land"),
("Estergon (1683)", "Loss of Esztergom (1683)", "1683-10", "Osmanlı–Kutsal İttifak savaşı (1683–1699)", "Estergon", 47.79, 18.74, "known", "Macaristan",
 "Habsburglar ve Lehistan", O, "Kara Mehmed Paşa", "", "dis", "L", "kesin",
 ["TDVIA:merzifonlu-kara-mustafa-pasa"], "", "Ciğerdelen (Parkan) ve Estergon Avusturyalıların eline geçti.", "Párkány and Esztergom fell to the Austrians.", "land"),
]

LEFT = [
 {"name": "Kandiye kuşatmasının ilk evreleri (1647–1648)", "reason": "Uzun kuşatma tek kayıtta (1669) toplandı.", "source": "TDVIA:ibrahim--padisah"},
 {"name": "Para (Paros) 1651 ve Değirmenlik (Milos) deniz savaşları", "reason": "Tarih ve sonuç TDVİA'da net değil.", "source": "TDVIA:mehmed-iv"},
 {"name": "Varvar Ali Paşa ve Abaza'nın Aksaray zaferi (1648, 1655)", "reason": "Celâlî çatışmaları; bu turda tarih ayrıntısı eksik.", "source": "TDVIA:ibrahim--padisah"},
 {"name": "Yeni Zerinvar (1664)", "reason": "Saint Gotthard maddesinde arka plan olarak geçer; ayrı kayıt açılmadı.", "source": "TDVIA:saint-gotthard-muharebesi"},
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
meta = {"batch": "Parti 11 — Osmanlı: Sultan İbrâhim ve IV. Mehmed (1640–1683)", "compiled": "2026-10-29", "status": "İlk tur.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "osmanli-1640-1683.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
