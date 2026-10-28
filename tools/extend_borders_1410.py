"""data/sinirlar.json'u 1310'dan 1410'a uzatır: Osmanlı genişlemesi, Anadolu beylikleri, Balkanlar, Timur.
Bir kez çalıştırılmak üzere yazıldı; tarihlerin çoğu yaklaşıktır ve 'yaklasik' işaretlidir."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
END, OLD = 1410, 1310

B = lambda tr, en, color="#cf6a9b": {"tr": tr, "en": en, "group": "beylik", "color": color}
d["states"].update({
 "karesi": B("Karesioğulları", "Karasids"), "saruhan": B("Saruhanoğulları", "Saruhanids"), "aydin": B("Aydınoğulları", "Aydinids"),
 "mentese": B("Menteşeoğulları", "Menteshe"), "hamid": B("Hamîdoğulları", "Hamidids"), "candar": B("Candaroğulları", "Jandarids"),
 "eretna": B("Eretnalılar", "Eretnids"), "kadi-burhaneddin": B("Kadı Burhâneddin Devleti", "State of Kadi Burhan al-Din"),
 "timur": {"tr": "Timurlular", "en": "Timurids", "group": "turk-diger", "color": "#a3795a"},
 "karakoyunlu": {"tr": "Karakoyunlular", "en": "Kara Koyunlu", "group": "turk-diger", "color": "#a3795a"},
 "celayir": {"tr": "Celâyirliler", "en": "Jalayirids", "group": "diger", "color": "#9a92a8"},
 "sirbistan": {"tr": "Sırbistan", "en": "Serbia", "group": "diger", "color": "#b59a8c"},
 "bosna": {"tr": "Bosna Krallığı", "en": "Kingdom of Bosnia", "group": "diger", "color": "#a7a28c"},
 "eflak": {"tr": "Eflak", "en": "Wallachia", "group": "diger", "color": "#9fa79a"},
 "macar": {"tr": "Macaristan", "en": "Hungary", "group": "diger", "color": "#a99bb5"},
 "cagatay": {"tr": "Çağatay Hanlığı", "en": "Chagatai Khanate", "group": "diger", "color": "#8f9aa8"},
})
d["states"]["osmanli"]["tr"] = "Osmanlı Devleti"

# Mevcut şehirlerde 1310 sonrası
S = {
 "bilecik": [[1000,1299,"bizans"],[1299,END,"osmanli"]],
 "eskisehir": [[1000,1080,"bizans"],[1080,1175,"anadolu-selcuklu"],[1175,1180,"bizans"],[1180,1288,"anadolu-selcuklu"],[1288,END,"osmanli"]],
 "iznik": [[1000,1081,"bizans"],[1081,1097,"anadolu-selcuklu"],[1097,1204,"bizans"],[1204,1261,"iznik-imp"],[1261,1331,"bizans"],[1331,END,"osmanli"]],
 "izmir": [[1000,1081,"bizans"],[1081,1097,"caka"],[1097,1204,"bizans"],[1204,1261,"iznik-imp"],[1261,1317,"bizans"],[1317,1390,"aydin"],[1390,1402,"osmanli"],[1402,END,"aydin"]],
 "kutahya": [[1000,1182,"bizans"],[1182,1290,"anadolu-selcuklu"],[1290,1390,"germiyan"],[1390,1402,"osmanli"],[1402,END,"germiyan"]],
 "denizli": [[1000,1206,"bizans"],[1206,1308,"anadolu-selcuklu"],[1308,1390,"germiyan"],[1390,1402,"osmanli"],[1402,END,"germiyan"]],
 "antalya": [[1000,1207,"bizans"],[1207,1212,"anadolu-selcuklu"],[1212,1216,"latin"],[1216,1308,"anadolu-selcuklu"],[1308,1390,"hamid"],[1390,1402,"osmanli"],[1402,END,"hamid"]],
 "konya": [[1000,1080,"bizans"],[1080,1308,"anadolu-selcuklu"],[1308,1397,"karaman"],[1397,1402,"osmanli"],[1402,END,"karaman"]],
 "karaman": [[1000,1080,"bizans"],[1080,1277,"anadolu-selcuklu"],[1277,END,"karaman"]],
 "ankara": [[1000,1073,"bizans"],[1073,1101,"anadolu-selcuklu"],[1101,1127,"bizans"],[1127,1175,"danismend"],[1175,1308,"anadolu-selcuklu"],[1308,1362,"eretna"],[1362,1402,"osmanli"],[1402,END,"osmanli"]],
 "kastamonu": [[1000,1080,"bizans"],[1080,1175,"danismend"],[1175,1308,"anadolu-selcuklu"],[1308,1393,"candar"],[1393,1402,"osmanli"],[1402,END,"candar"]],
 "sinop": [[1000,1204,"bizans"],[1204,1214,"trabzon"],[1214,1259,"anadolu-selcuklu"],[1259,1266,"trabzon"],[1266,1322,"anadolu-selcuklu"],[1322,END,"candar"]],
 "amasya": [[1000,1075,"bizans"],[1075,1174,"danismend"],[1174,1335,"anadolu-selcuklu"],[1335,1381,"eretna"],[1381,1392,"kadi-burhaneddin"],[1392,END,"osmanli"]],
 "sivas": [[1000,1075,"bizans"],[1075,1174,"danismend"],[1174,1335,"anadolu-selcuklu"],[1335,1381,"eretna"],[1381,1398,"kadi-burhaneddin"],[1398,1400,"osmanli"],[1400,1402,"timur"],[1402,END,"karakoyunlu"]],
 "kayseri": [[1000,1075,"bizans"],[1075,1169,"danismend"],[1169,1335,"anadolu-selcuklu"],[1335,1381,"eretna"],[1381,1398,"kadi-burhaneddin"],[1398,1402,"osmanli"],[1402,END,"karaman"]],
 "malatya": [[1000,1071,"bizans"],[1071,1103,"ermeni"],[1103,1178,"danismend"],[1178,1316,"anadolu-selcuklu"],[1316,END,"memluk"]],
 "erzincan": [[1000,1071,"bizans"],[1071,1228,"mengucek"],[1228,1335,"anadolu-selcuklu"],[1335,1400,"eretna"],[1400,END,"timur"]],
 "erzurum": [[1000,1071,"bizans"],[1071,1202,"saltuklu"],[1202,1256,"anadolu-selcuklu"],[1256,1357,"mogol"],[1357,1388,"celayir"],[1388,END,"karakoyunlu"]],
 "tarsus": [[1000,1080,"bizans"],[1080,1375,"ermeni"],[1375,END,"memluk"]],
 "edirne": [[1000,1204,"bizans"],[1204,1225,"latin"],[1225,1261,"iznik-imp"],[1261,1361,"bizans"],[1361,END,"osmanli"]],
 "selanik": [[1000,1204,"bizans"],[1204,1224,"latin"],[1224,1246,"bizans"],[1246,1261,"iznik-imp"],[1261,1387,"bizans"],[1387,1403,"osmanli"],[1403,END,"bizans"]],
 "tirnova": [[1000,1185,"bizans"],[1185,1393,"bulgar2"],[1393,END,"osmanli"]],
}
# İran, Irak, Orta Asya: İlhanlıların çöküşü (1335) ve Timur
for cid in ("rey", "hemedan", "isfahan", "tebriz", "gence", "kirman", "siraz", "ahvaz", "basra", "bagdat", "hille", "musul", "alamut", "curcan", "amul", "merv", "serahs", "nisabur", "herat", "belh", "zerenc", "gazne", "bust", "firuzkuh", "ani", "amid", "meyyafarikin", "urfa", "ahlat", "malazgirt"):
    S.setdefault(cid, None)
POST_ILKHAN = {"bagdat": "celayir", "tebriz": "celayir", "hille": "celayir", "basra": "celayir", "musul": "celayir", "ahvaz": "celayir",
               "amid": "karakoyunlu", "urfa": "karakoyunlu", "ahlat": "karakoyunlu", "malazgirt": "karakoyunlu", "ani": "karakoyunlu", "meyyafarikin": "karakoyunlu"}

known = {c["id"]: c for c in d["cities"]}
for cid, spans in S.items():
    c = known[cid]
    if spans is not None:
        c["spans"] = spans
        continue
    sp = c["spans"]
    if sp[-1][1] == OLD and sp[-1][2] == "mogol":
        sp[-1][1] = 1335 if cid in POST_ILKHAN else 1370
        if cid in POST_ILKHAN:
            sp.append([1335, 1393, POST_ILKHAN[cid]]); sp.append([1393, END, "timur"])
        else:
            sp.append([1370, END, "timur"])
        c["yaklasik"] = True
for c in d["cities"]:
    if c.get("void"): continue
    for s in c["spans"]:
        if s[1] == OLD: s[1] = END
# Orta Asya: Çağatay sonra Timur
for cid in ("buhara", "semerkant", "kasgar", "balasagun"):
    sp = known[cid]["spans"]
    if sp[-1][2] == "mogol":
        sp[-1][2] = "cagatay"; sp[-1][1] = 1370 if cid in ("buhara", "semerkant") else END
        if cid in ("buhara", "semerkant"): sp.append([1370, END, "timur"])

NEW = [
 ("bursa", "Bursa", 40.19, 29.06, [[1000,1326,"bizans"],[1326,END,"osmanli"]], ["bursa", "orhan"], False),
 ("izmit", "İzmit", 40.77, 29.92, [[1000,1337,"bizans"],[1337,END,"osmanli"]], ["orhan"], False),
 ("balikesir", "Balıkesir (Karesi)", 39.65, 27.88, [[1000,1300,"bizans"],[1300,1345,"karesi"],[1345,END,"osmanli"]], ["orhan"], True),
 ("manisa", "Manisa (Saruhan)", 38.61, 27.43, [[1000,1313,"bizans"],[1313,1390,"saruhan"],[1390,1402,"osmanli"],[1402,END,"saruhan"]], ["bayezid-i"], True),
 ("milas", "Milas (Menteşe)", 37.31, 27.78, [[1000,1280,"bizans"],[1280,1390,"mentese"],[1390,1402,"osmanli"],[1402,END,"mentese"]], ["bayezid-i"], True),
 ("isparta", "Isparta (Hamîd)", 37.76, 30.55, [[1000,1204,"bizans"],[1204,1308,"anadolu-selcuklu"],[1308,1381,"hamid"],[1381,END,"osmanli"]], ["murad-i"], True),
 ("gelibolu", "Gelibolu", 40.41, 26.67, [[1000,1354,"bizans"],[1354,1366,"osmanli"],[1366,1376,"latin"],[1376,END,"osmanli"]], ["gelibolu", "orhan"], True),
 ("filibe", "Filibe", 42.14, 24.75, [[1000,1344,"bizans"],[1344,1364,"bulgar2"],[1364,END,"osmanli"]], ["murad-i"], True),
 ("sofya", "Sofya", 42.70, 23.32, [[1000,1185,"bizans"],[1185,1385,"bulgar2"],[1385,END,"osmanli"]], ["murad-i"], True),
 ("uskup", "Üsküp", 42.00, 21.43, [[1000,1282,"bizans"],[1282,1392,"sirbistan"],[1392,END,"osmanli"]], ["bayezid-i"], True),
 ("manastir", "Manastır", 41.03, 21.33, [[1000,1334,"bizans"],[1334,1385,"sirbistan"],[1385,END,"osmanli"]], ["murad-i"], True),
 ("nis", "Niş", 43.32, 21.90, [[1000,1183,"bizans"],[1183,1386,"sirbistan"],[1386,END,"osmanli"]], ["murad-i"], True),
 ("pristine", "Priştine", 42.66, 21.17, [[1000,1180,"bizans"],[1180,END,"sirbistan"]], ["kosova-savaslari"], True),
 ("belgrad", "Belgrad", 44.82, 20.45, [[1000,1284,"macar"],[1284,1319,"sirbistan"],[1319,1403,"macar"],[1403,END,"sirbistan"]], [], True),
 ("sarajevo", "Bosna", 43.86, 18.41, [[1000,1180,"bizans"],[1180,END,"bosna"]], [], True),
 ("avlonya", "Avlonya (Arnavutluk)", 40.47, 19.49, [[1000,1345,"bizans"],[1345,END,"sirbistan"]], ["murad-i"], True),
 ("buda", "Buda", 47.50, 19.04, [[1000,END,"macar"]], [], True),
 ("bukres", "Eflak", 44.43, 26.10, [[1000,1240,"kipcak"],[1240,1310,"altin-orda"],[1310,END,"eflak"]], ["bayezid-i"], True),
 ("mora", "Mora", 37.50, 22.40, [[1000,1205,"bizans"],[1205,1262,"latin"],[1262,END,"bizans"]], [], True),
]
for cid, tr, lat, lon, spans, src, yk in NEW:
    assert cid not in known, cid
    c = {"id": cid, "tr": tr, "lat": lat, "lon": lon, "spans": spans, "src": src}
    if yk: c["yaklasik"] = True
    d["cities"].insert(len(d["cities"]) - sum(1 for x in d["cities"] if x.get("void")), c)
# Macar 'void' noktası artık gerçek bir şehirle değişti
d["cities"] = [c for c in d["cities"] if c.get("id") != "v-macar"]
for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in d["states"], (c["id"], s)
d["meta"]["method"] += " 1310–1410 arasında Anadolu beylikleri, Balkanlar ve Timur eklendi; bu dönemin el değiştirme tarihleri çoğunlukla yaklaşıktır."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(d["states"]), "devlet")
