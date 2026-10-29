"""data/osmanli-1878-1912.json dosyasını üretir (Parti 17: Berlin'den Balkan Savaşı'na, 1878–1912)."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "osmanli-1878-1912"
O = "Osmanlı Devleti"
WA = "Arnavutluk isyanı (1878–1881)"
WG = "Osmanlı–Yunan savaşı (1897)"
WY = "Yemen ve Asîr isyanları (1904–1911)"
W31 = "Otuzbir Mart Vak‘ası (1909)"
WT = "Trablusgarp Savaşı (1911–1912)"
GR, IT = "Yunanistan", "İtalya"
ED = "Gazi Edhem Paşa"
YH = "İmam Yahyâ Hamîdüddin"

# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür)
R = [
("Kosova'nın geri alınışı (1881)", "Suppression of the League of Prizren (1881)", "1881-04", WA, "Prizren ve Kosova", 42.21, 20.74, "region", "Kosova",
 O, "Arnavut bağımsızlık yanlıları (Prizren Cemiyeti)", "Derviş Paşa", "", "ic", "C", "kesin",
 ["TDVIA:prizren"], "", "Derviş Paşa kumandasındaki Osmanlı kuvvetleri Arnavut bağımsızlık yanlılarının eline geçen bölgeleri geri aldı.",
 "Ottoman forces under Derviş Pasha recovered the districts held by the Albanian autonomists.", "land"),
("Milona (1897)", "Battle of Meluna Pass", "1897-04-18", WG, "Milona Geçidi", 39.93, 22.28, "approx", "Yunanistan",
 O, GR, ED, "", "dis", "W", "kesin",
 ["TDVIA:gazi-edhem-pasa"], "Tesalya maddesi savaşı 7 Nisan–18 Mayıs 1897 arasına koyar; Edhem Paşa maddesi Milona'yı savaş ilânının ertesi gününe, 18 Nisan'a koyar (takvim farkı olabilir).", "Savaş ilânının ertesi günü kazanıldı.", "Won the day after the declaration of war.", "land"),
("Yenişehir (1897)", "Ottoman capture of Larissa (1897)", "1897-04-25", WG, "Yenişehir (Larissa)", 39.64, 22.42, "known", "Yunanistan",
 O, GR, ED, "", "dis", "W", "kesin",
 ["TDVIA:gazi-edhem-pasa", "TDVIA:yenisehir"], "", "Şehir kısa bir süre Osmanlı idaresine alındı.", "The town was briefly brought back under Ottoman rule.", "land"),
("Çatalca (Fersala) (1897)", "Battle of Pharsala (1897)", "1897-05", WG, "Çatalca (Farsala)", 39.30, 22.38, "known", "Yunanistan",
 O, GR, ED, "", "dis", "W", "kesin",
 ["TDVIA:izzet-pasa-ahmed", "TDVIA:tesalya"], "", "Muharebe planlarının hazırlanmasında Ahmed İzzet Bey'in büyük emeği geçti.",
 "Ahmed İzzet Bey played a large part in drawing up the battle plans.", "land"),
("Velestin (1897)", "Battle of Velestino (1897)", "1897-05-06", WG, "Velestin", 39.38, 22.75, "known", "Yunanistan",
 O, GR, ED, "", "dis", "W", "kesin",
 ["TDVIA:velestin"], "", "Çatalca zaferinden sonra 6 Mayıs 1897'de Velestin tepeleri ve istasyonu alındı, 8 Mayıs'ta Volos Limanı'na girildi. (Kontrol turunda eklendi.)",
 "After the victory at Pharsala the Velestino heights and station were taken on 6 May 1897, and Volos harbour was entered on 8 May.", "land"),
("Tırhala (1897)", "Ottoman capture of Trikala (1897)", "1897-05-12", WG, "Tırhala (Trikala)", 39.56, 21.77, "known", "Yunanistan",
 O, GR, ED, "", "dis", "W", "kesin",
 ["TDVIA:gazi-edhem-pasa"], "", "", "", "land"),
("Dömeke (1897)", "Battle of Domokos", "1897-05-17", WG, "Dömeke (Domokos)", 39.13, 22.30, "known", "Yunanistan",
 O, GR, ED, "", "dis", "W", "kesin",
 ["TDVIA:gazi-edhem-pasa", "TDVIA:izzet-pasa-ahmed", "TDVIA:tesalya"], "",
 "Yunan ordusu büyük bir bozguna uğradı; ardından Termopil Geçidi 24 saatte aşılıp Atina yolu açıldı.",
 "The Greek army was heavily routed; the Thermopylae pass was then crossed in 24 hours, opening the road to Athens.", "land"),
("San‘a (1905)", "Fall of Sanaa (1905)", "1905-04", WY, "San‘a", 15.35, 44.21, "known", "Yemen",
 YH, O, "Vali Fâik Paşa", YH, "ic", "C", "kesin",
 ["TDVIA:mutevekkil-alellah-yahya-hamiduddin", "TDVIA:yemen"], "",
 "Kuşatma altındaki San‘a'da açlık baş gösterdi; İmam Yahyâ topladığı kabile kuvvetleriyle şehri ve çevresini aldı.",
 "Famine broke out in besieged Sanaa; Imam Yahya took the city and its surroundings with the tribal forces he had raised.", "land"),
("San‘a'nın geri alınışı (1905)", "Ottoman recapture of Sanaa (1905)", "1905-09-01", WY, "San‘a", 15.35, 44.21, "known", "Yemen",
 O, YH, "Ahmed Feyzi Paşa", YH, "ic", "C", "kesin",
 ["TDVIA:yemen"], "", "15 Temmuz–1 Eylül 1905 harekâtında Taiz'deki kuvvetlerin desteğiyle San‘a'ya girildi; isyancı kabile reisleri bertaraf edildi.",
 "In the operations of 15 July–1 September 1905, supported by the forces at Taizz, Sanaa was entered and the rebel tribal chiefs were dealt with.", "land"),
("Otuzbir Mart (1909)", "Suppression of the 31 March Incident", "1909-04-24", W31, "İstanbul", 41.01, 28.98, "known", "Türkiye",
 "Hareket Ordusu", "İstanbul'daki isyancı birlikler", "Mahmud Şevket Paşa, Hüseyin Hüsnü Paşa", "", "ic", "C", "borderline",
 ["TDVIA:otuzbir-mart-vakasi", "TDVIA:hareket-ordusu", "TDVIA:abdulhamid-ii", "TDVIA:mahmud-sevket-pasa"], "",
 "Selanik'ten gelen Hareket Ordusu 19 Nisan'da Yeşilköy'e ulaştı, 23–24 Nisan gecesi şehre girip 24 Nisan'da hâkimiyeti tamamen ele geçirdi. Çatışmanın boyutu maddelerde yazmadığından borderline.",
 "The Action Army from Salonica reached Yeşilköy on 19 April, entered the city on the night of 23–24 April and was in full control on 24 April. The articles do not describe the extent of the fighting, so the record is borderline.", "land"),
("Ebhâ (1911)", "Relief of Abha (1911)", "1911-06-11", WY, "Ebhâ", 18.22, 42.50, "known", "Suudi Arabistan",
 O, "Asîr isyancıları (Muhammed el-İdrîsî)", "Mekke Şerifi Hüseyin b. Ali", "Muhammed b. Ali el-İdrîsî", "ic", "C", "kesin",
 ["TDVIA:ebha", "TDVIA:asir--suudi-arabistan"], "",
 "1910'da isyan eden İdrîsî'nin yedi ay süren kuşatması, Osmanlı Devleti'nin emriyle Mekke Şerifi'nin gönderdiği kuvvetle kaldırıldı.",
 "Idrisi's seven-month siege, begun when he rose in 1910, was lifted by a force sent by the Sharif of Mecca on Ottoman orders.", "land"),
("San‘a kuşatmasının kaldırılması (1911)", "Relief of Sanaa (1911)", "1911", WY, "San‘a", 15.35, 44.21, "known", "Yemen",
 O, YH, "Ahmed İzzet Paşa", YH, "ic", "C", "kesin",
 ["TDVIA:yemen", "TDVIA:izzet-pasa-ahmed", "TDVIA:mutevekkil-alellah-yahya-hamiduddin"], "",
 "50.000 kişilik ordu San‘a kuşatmasını kaldırdı; İmam Yahyâ ile Daân Antlaşması imzalandı (9 Ekim 1911).",
 "An army of 50,000 lifted the siege of Sanaa; the Treaty of Daan was signed with Imam Yahya (9 October 1911).", "land"),
("Preveze (1911)", "Naval action off Preveza (1911)", "1911-09", WT, "Preveze limanı", 38.96, 20.75, "known", "Yunanistan",
 IT, O, "", "", "dis", "L", "kesin",
 ["TDVIA:trablusgarp-savasi"], "", "Tokat ve Alpagu torpidoları savaş ilânından bir gün önce saldırıya uğradı; Tokat saf dışı edildi, Preveze Limanı'na kaçan Alpagu burada bulunan Hamidiye torpidosuyla birlikte batırıldı.",
 "The torpedo boats Tokat and Alpagu were attacked the day before the declaration of war; the Tokat was put out of action, and the Alpagu, which fled to Preveza, was sunk there together with the torpedo boat Hamidiye.", "sea"),
("Tobruk (1911)", "Italian capture of Tobruk", "1911-10-08", WT, "Tobruk", 32.08, 23.96, "known", "Libya",
 IT, O, "", "", "dis", "L", "kesin",
 ["TDVIA:trablusgarp-savasi"], "", "", "", "land"),
("Trablusgarp (1911)", "Italian capture of Tripoli (1911)", "1911-10-09", WT, "Trablusgarp", 32.89, 13.19, "known", "Libya",
 IT, O, "", "", "dis", "L", "kesin",
 ["TDVIA:trablusgarp-savasi", "TDVIA:trablusgarp"], "", "Bombardımana direnmenin imkânsızlığı yüzünden şehir teslim olmak zorunda kaldı.",
 "As resisting the bombardment was impossible, the town had to surrender.", "land"),
("Derne (1911)", "Italian capture of Derna (1911)", "1911-10-16", WT, "Derne", 32.77, 22.64, "known", "Libya",
 IT, O, "", "Amiral Presbitero", "dis", "L", "kesin",
 ["TDVIA:trablusgarp-savasi", "TDVIA:derne"], "", "30 Eylül'de bombalanan şehir 16 Ekim'de işgal edildi.", "Bombarded on 30 September, the town was occupied on 16 October.", "land"),
("Bingazi (1911)", "Italian capture of Benghazi (1911)", "1911-10-21", WT, "Bingazi", 32.12, 20.07, "known", "Libya",
 IT, O, "", "", "dis", "L", "kesin",
 ["TDVIA:trablusgarp-savasi", "TDVIA:bingazi"], "", "", "", "land"),
("Trablus önü (1911)", "Battle outside Tripoli (23 October 1911)", "1911-10-23", WT, "Trablusgarp yöresi", 32.85, 13.25, "approx", "Libya",
 O, IT, "Neşet Bey, Ali Fethi Bey", "", "dis", "W", "kesin",
 ["TDVIA:trablusgarp-savasi"], "", "İtalyan kuvvetleri ağır zayiat verip yenildi; İtalya bunun üzerine Trablusgarp ve Bingazi'nin ilhakını ilân etti (5 Kasım 1911).",
 "The Italian forces were defeated with heavy losses; Italy then proclaimed the annexation of Tripolitania and Cyrenaica (5 November 1911).", "land"),
("Beyrut (1912)", "Bombardment of Beirut (1912)", "1912-02-24", WT, "Beyrut limanı", 33.90, 35.50, "known", "Lübnan",
 IT, O, "", "", "dis", "L", "kesin",
 ["TDVIA:trablusgarp-savasi"], "", "İtalyan savaş gemileri limandaki deniz vasıtalarını batırdı, şehri topa tuttu.",
 "Italian warships sank the vessels in the harbour and shelled the town.", "sea"),
("Rodos (1912)", "Italian occupation of Rhodes", "1912-05-17", WT, "Rodos", 36.43, 28.22, "known", "Yunanistan",
 IT, O, "", "", "dis", "L", "kesin",
 ["TDVIA:trablusgarp-savasi", "TDVIA:rodos"], "", "24 Nisan'da başlayan işgale karşı koyacak yeterli asker yoktu; Oniki Ada da işgal edildi.",
 "There were not enough troops to resist the occupation begun on 24 April; the Dodecanese were also occupied.", "land"),
]

LEFT = [
 {"name": "Girit'e Yunan çıkarması (1897)", "reason": "Girit maddesi çıkarmayı ve beyannâmeyi anar; muharebe yok.", "source": "TDVIA:girit"},
 {"name": "Termopil (1897)", "reason": "Edhem Paşa maddesi Termopil'in aşıldığını anar; muharebe ayrıntısı yok.", "source": "TDVIA:gazi-edhem-pasa"},
 {"name": "Tellülkebîr (1882)", "reason": "Mısır ordusu ile İngiltere arasında; padişah Urâbî'yi desteklemedi → Osmanlı devletinin savaşı sayılmadı.", "source": "TDVIA:urabi-pasa"},
 {"name": "Yemen isyanları 1891–1897 ve 1902–1904", "reason": "Yemen maddesi toplu anar; muharebe adı yok.", "source": "TDVIA:yemen"},
 {"name": "Arnavut ve Malisör isyanları (1909–1912)", "reason": "Arnavutluk ve Enver Paşa maddelerinde muharebe ayrıntısı yok.", "source": "TDVIA:arnavutluk"},
 {"name": "Derne ve Tobruk cephesi çatışmaları (1912, Enver ve Mustafa Kemal)", "reason": "Maddeler mart–ekim çatışmalarını toplu anar.", "source": "TDVIA:trablusgarp-savasi"},
 {"name": "Hudeyde ve Kunfüze bombardımanları (1912)", "reason": "Kısa bombardımanlar; muharebe sayılmadı.", "source": "TDVIA:yemen"},
 {"name": "Necid'e gönderilen Osmanlı kuvveti (1904)", "reason": "Lahsâ maddesi kuvvetin gönderildiğini anar; çatışma ayrıntısı yok.", "source": "TDVIA:lahsa"},
]

# İkinci kaynak turu: ikinci TDVİA maddeleri.
EXTRA_SRC = {
    "Kosova'nın geri alınışı (1881)": ["TDVIA:arnavutluk"],  # 1881'de Bâbıâli'nin gönderdiği ordu ile dağıtıldı
    "San‘a'nın geri alınışı (1905)": ["TDVIA:mutevekkil-alellah-yahya-hamiduddin"],  # Ahmed Feyzi Paşa karşısında şehri terketti
}

recs = []
for i, r in enumerate(R, 1):
    (ntr, nen, date, war, place, lat, lon, loc, country, sa, sb, tc, oc, cat, res, status, src, disp, note, note_en, typ) = r
    src = src + [x for x in EXTRA_SRC.get(ntr, []) if x not in src]
    rec = {"id": i, "name_tr": ntr, "name_en": nen, "date": date, "hijri": "", "type": typ, "war": war, "place": place,
           "lat": lat, "lon": lon, "loc": loc, "country": country, "side_a": sa, "side_b": sb, "turkic_cmd": tc, "opp_cmd": oc,
           "category": cat, "result": res, "status": status, "sources": src,
           "verify": {"tdvia": True, "tdvia2": len([s for s in src if s.startswith("TDVIA:")]) >= 2, "wp": False, "rom": False, "academic": False},
           "state": O, "home_batch": HB}
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    recs.append(rec)

pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 17 — Osmanlı: Berlin'den Balkan Savaşı'na (1878–1912)", "compiled": "2026-10-29", "status": "İkinci kaynak turu yapıldı.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "osmanli-1878-1912.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
