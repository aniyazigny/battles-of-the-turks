"""data/kipcaklar.json dosyasını üretir (Parti 25: Kıpçaklar / Kumanlar, 1103–1239).

Kapsam kararı 2026-10-30 (kullanıcı: "Ekle"). Olaylar Kıpçaklar, Batu Han, Moğollar, Bulgaristan ve Dobruca maddelerinden derlendi.
Kıpçakların Bizans müttefiki olarak katıldığı Levunion 1091 Parti 23'te, Selçuklulara karşı Suğdak 1221 Parti 2'de, Gürcü hizmetindeki
Kıpçak kuvvetleri Didgori 1121 kaydında yer alır."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
HB = "kipcaklar"
KP = "Kıpçaklar (Kumanlar)"
WKR = "Kıpçak–Rus savaşları (1061–1185)"
WMO = "Moğol istilâsı"
RS = "Rus knezlikleri"

# (ad_tr, ad_en, tarih, harp, yer, lat, lon, loc, ülke, kazanan, kaybeden, türk_k, rakip_k, kategori, sonuç, statü,
#  kaynaklar, ihtilaf, not_tr, not_en, tür, devlet)
R = [
("Rus zaferi (1103)", "Rus victory over the Cumans (1103)", "1103", WKR, "Karadeniz kuzeyi bozkırı", 47.50, 35.50, "region", "Ukrayna",
 RS, KP, "", "", "dis", "L", "kesin",
 ["TDVIA:kipcaklar"], "", "Ruslar Kıpçaklar'a karşı büyük bir başarı kazandı; Kıpçaklar 1105–1111 arasında şiddetli akınlarla karşılık verdi.",
 "The Rus won a great success over the Cumans, who answered with fierce raids in 1105–1111.", "land", KP),
("Aksu (1184)", "Battle of the Orel (1184)", "1184", WKR, "Aksu nehri (Kiev'in güneydoğusu)", 49.00, 34.00, "approx", "Ukrayna",
 RS, KP, "", "Kiev knezi Svyatoslav", "dis", "L", "kesin",
 ["TDVIA:kipcaklar"], "", "Kiev civarına akın eden Aksu boyundaki Kıpçaklar, güney Rus knezliklerinin birleşik ordusuna yenildi.",
 "The Cumans of the Aksu, raiding around Kiev, were beaten by the united army of the southern Rus principalities.", "land", KP),
("Kayalı (1185)", "Battle of the Kayala (1185)", "1185", WKR, "Kayalı ırmağı (aşağı Don)", 47.80, 38.50, "approx", "Ukrayna / Rusya",
 KP, RS, "", "Novgorod-Seversk knezi İgor Svyatoslaviç", "dis", "W", "kesin",
 ["TDVIA:kipcaklar"], "", "Kıpçaklar'a sefere çıkan İgor Svyatoslaviç'in ordusu Kayalı kıyısında kuşatılıp imha edildi; sefer İgor Bölüğü Destanı'nda anlatılır.",
 "Igor Svyatoslavich's army, campaigning against the Cumans, was surrounded and destroyed on the Kayala; the campaign is the subject of the Lay of Igor's Campaign.", "land", KP),
("Asen ve Petar'ın ayaklanması (1186–1187)", "Cuman-backed Asen rising (1186–1187)", "1186", "Bulgar–Bizans savaşı (1185–1187)", "Kuzey Bulgaristan", 43.08, 25.63, "region", "Bulgaristan",
 "Asen ve Petar (Kuman kuvvetleriyle)", "Bizans", "", "", "dis", "W", "borderline",
 ["TDVIA:bulgaristan", "TDVIA:dobruca"], "",
 "Tuna'yı geçip Kumanlar'a sığınan Petar ve Asen kardeşler buradan sağladıkları orduyla Kuzey Bulgaristan'ı yeniden ele geçirdi ve 1187'de Bizans'ı barışa zorladı; Dobruca maddesi ikinci Bulgar devletinin Kumanlar'ca kurulduğunu yazar. Kumanlar yardımcı kuvvet olduğu için borderline.",
 "The brothers Peter and Asen, who had fled across the Danube to the Cumans, retook northern Bulgaria with a Cuman army and forced Byzantium to make peace in 1187; borderline as the Cumans were auxiliaries.", "land", KP),
("Kalka (1223)", "Battle of the Kalka River", "1223", WMO, "Kalka ırmağı", 47.30, 37.60, "approx", "Ukrayna",
 "Moğollar", "Kıpçaklar ve Rus knezlikleri", "", "Cebe Noyan, Sübütay", "dis", "L", "kesin",
 ["TDVIA:kipcaklar", "TDVIA:batu-han"], "",
 "Moğol istilâsına karşı Ruslar'la iş birliği yapan Kıpçaklar Cebe ve Sübütay kumandasındaki iki Moğol tümenine yenildi.",
 "Allied with the Rus against the Mongol invasion, the Cumans were defeated by two Mongol tümens under Jebe and Subutai.", "land", KP),
("Batu'nun Deşt-i Kıpçak seferi (1237–1239)", "Mongol conquest of the Cumans (1237–1239)", "1237", WMO, "Deşt-i Kıpçak", 47.50, 40.00, "region", "Rusya / Ukrayna",
 "Moğollar (Batu Han)", KP, "", "Batu Han, Subitay Noyan", "dis", "L", "kesin",
 ["TDVIA:batu-han", "TDVIA:mogollar", "TDVIA:kipcaklar"], "Batu Han maddesi son direnişin 1239'da kırıldığını, Moğollar maddesi istilâyı 1237–1241'e, Kıpçaklar maddesi Altın Orda'nın kuruluşunu 1241'e koyar.",
 "Kalka dönüşündeki yenilginin intikamını almak için Deşt-i Kıpçak'a saldıran Batu'nun ordusuyla Kıpçaklar arasında şiddetli çatışmalar oldu; 1239'da Kıpçaklar'ın son direnişi kırıldı.",
 "Avenging the defeat suffered on the way back from the Kalka, Batu attacked the Kipchak steppe; there was fierce fighting, and the Cumans' last resistance was broken in 1239.", "land", KP),
]

LEFT = [
    {"name": "Rus bozkırlarının alınışı (1061 sonrası)", "reason": "Kıpçaklar maddesi süreci toplu anar.", "source": "TDVIA:kipcaklar"},
    {"name": "Bizans'a akınlar (1083–1096, 1109–1114) ve Rus akınları (1105–1111)", "reason": "Toplu anılır; muharebe adı yok.", "source": "TDVIA:kipcaklar"},
    {"name": "Pereyaslavl'a hücum (1177–1179)", "reason": "Sonuç belirtilmez.", "source": "TDVIA:kipcaklar"},
    {"name": "Oğuz–Kıpçak savaşları", "reason": "Oğuzlar maddesi zaman zaman savaştıklarını yazar; tarih ve yer yok.", "source": "TDVIA:oguzlar"},
    {"name": "Kumanlar'ın Macaristan'a göçü (1239–1241)", "reason": "Macaristan maddesi yerleşmeyi anar; muharebe yok.", "source": "TDVIA:macaristan"},
]

recs = []
for i, r in enumerate(R, 1):
    (ntr, nen, date, war, place, lat, lon, loc, country, sa, sb, tc, oc, cat, res, status, src, disp, note, note_en, typ, state) = r
    rec = {"id": i, "name_tr": ntr, "name_en": nen, "date": date, "hijri": "", "type": typ, "war": war, "place": place,
           "lat": lat, "lon": lon, "loc": loc, "country": country, "side_a": sa, "side_b": sb, "turkic_cmd": tc, "opp_cmd": oc,
           "category": cat, "result": res, "status": status, "sources": src,
           "verify": {"tdvia": any(x.startswith("TDVIA:") for x in src), "tdvia2": len([s for s in src if s.startswith("TDVIA:")]) >= 2, "wp": False, "rom": False, "academic": any(x.startswith("AKD:") for x in src)},
           "state": state, "home_batch": HB}
    if disp: rec["dispute"] = disp
    if note: rec["note"], rec["note_en"] = note, note_en
    recs.append(rec)

dates = [r["date"] for r in recs]
assert dates == sorted(dates), dates
pilot = json.loads((root / "data" / "pilot-buyuk-selcuklu.json").read_text(encoding="utf-8"))
meta = {"batch": "Parti 25 — Kıpçaklar / Kumanlar (1103–1239)", "compiled": "2026-10-30", "status": "İlk tur.",
        "conventions": pilot["meta"]["conventions"], "source_keys": pilot["meta"]["source_keys"], "decisions": pilot["meta"]["decisions"]}
(root / "data" / "kipcaklar.json").write_text(json.dumps({"meta": meta, "battles": recs, "left_out": LEFT}, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(recs), "kayıt;", sum(r["verify"]["tdvia2"] for r in recs), "iki maddeli")
