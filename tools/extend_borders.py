"""data/sinirlar.json'u 1157 sonrasına (1310'a kadar) genişletir. Bir kez çalıştırılmak üzere yazıldı;
çıktı dosyası elle düzenlenmeye devam eder."""
import json
from pathlib import Path

P = Path(__file__).resolve().parent.parent / "data" / "sinirlar.json"
d = json.loads(P.read_text(encoding="utf-8"))
END = 1310

NEW_STATES = {
 "osmanli": {"tr": "Osmanlı Beyliği", "en": "Ottoman Beylik", "group": "turk", "color": "#1f8a8a"},
 "mengucek": {"tr": "Mengücüklüler", "en": "Mengujekids", "group": "beylik", "color": "#cf6a9b"},
 "karaman": {"tr": "Karamanoğulları", "en": "Karamanids", "group": "beylik", "color": "#cf6a9b"},
 "germiyan": {"tr": "Germiyanoğulları", "en": "Germiyanids", "group": "beylik", "color": "#cf6a9b"},
 "memluk": {"tr": "Memlükler", "en": "Mamluks", "group": "turk-diger", "color": "#a3795a"},
 "altin-orda": {"tr": "Altın Orda", "en": "Golden Horde", "group": "turk-diger", "color": "#a3795a"},
 "mogol": {"tr": "Moğollar (İlhanlılar)", "en": "Mongols (Ilkhanate)", "group": "diger", "color": "#8a8fa3"},
 "eyyubi": {"tr": "Eyyûbîler", "en": "Ayyubids", "group": "diger", "color": "#9db08a"},
 "latin": {"tr": "Latin devletleri", "en": "Latin states", "group": "diger", "color": "#b8877d"},
 "iznik-imp": {"tr": "İznik İmparatorluğu", "en": "Empire of Nicaea", "group": "diger", "color": "#a58cb0"},
 "trabzon": {"tr": "Trabzon Rum İmparatorluğu", "en": "Empire of Trebizond", "group": "diger", "color": "#ab95b8"},
 "bulgar2": {"tr": "Bulgar Çarlığı", "en": "Second Bulgarian Empire", "group": "diger", "color": "#a4a88f"},
 "kibris": {"tr": "Kıbrıs Krallığı", "en": "Kingdom of Cyprus", "group": "diger", "color": "#b5948a"},
}
d["states"].update(NEW_STATES)
d["states"]["ermeni"]["tr"] = "Ermeni prenslikleri / Kilikya Ermeni Krallığı"

# 1157 sonrası değişen şehirler: yeni tam span listesi
S = {
 "merv": [[1000,1037,"gazneli"],[1037,1153,"buyuk-selcuklu"],[1153,1162,"oguz"],[1162,1221,"harizmsah"],[1221,END,"mogol"]],
 "serahs": [[1000,1038,"gazneli"],[1038,1153,"buyuk-selcuklu"],[1153,1162,"oguz"],[1162,1221,"harizmsah"],[1221,END,"mogol"]],
 "nisabur": [[1000,1038,"gazneli"],[1038,1039,"buyuk-selcuklu"],[1039,1040,"gazneli"],[1040,1153,"buyuk-selcuklu"],[1153,1187,"oguz"],[1187,1221,"harizmsah"],[1221,END,"mogol"]],
 "herat": [[1000,1040,"gazneli"],[1040,1158,"buyuk-selcuklu"],[1158,1175,"oguz"],[1175,1206,"gurlu"],[1206,1221,"harizmsah"],[1221,END,"mogol"]],
 "zerenc": [[1000,1041,"gazneli"],[1041,1158,"buyuk-selcuklu"],[1158,1221,"gurlu"],[1221,END,"mogol"]],
 "belh": [[1000,1043,"gazneli"],[1043,1153,"buyuk-selcuklu"],[1153,1160,"oguz"],[1160,1198,"karahitay"],[1198,1206,"gurlu"],[1206,1220,"harizmsah"],[1220,END,"mogol"]],
 "gazne": [[1000,1163,"gazneli"],[1163,1215,"gurlu"],[1215,1221,"harizmsah"],[1221,END,"mogol"]],
 "bust": [[1000,1150,"gazneli"],[1150,1215,"gurlu"],[1215,1221,"harizmsah"],[1221,END,"mogol"]],
 "lahor": [[1000,1186,"gazneli"],[1186,1206,"gurlu"]],
 "multan": [[1000,1175,"gazneli"],[1175,1206,"gurlu"]],
 "firuzkuh": [[1000,1215,"gurlu"],[1215,1221,"harizmsah"],[1221,END,"mogol"]],
 "gurgenc": [[1000,1041,"gazneli"],[1041,1043,"oguz"],[1043,1097,"buyuk-selcuklu"],[1097,1221,"harizmsah"],[1221,END,"altin-orda"]],
 "buhara": [[1000,1210,"karahanli"],[1210,1220,"harizmsah"],[1220,END,"mogol"]],
 "semerkant": [[1000,1212,"karahanli"],[1212,1220,"harizmsah"],[1220,END,"mogol"]],
 "kasgar": [[1000,1211,"karahanli"],[1211,1218,"karahitay"],[1218,END,"mogol"]],
 "balasagun": [[1000,1134,"karahanli"],[1134,1218,"karahitay"],[1218,END,"mogol"]],
 "yengikent": [[1000,1050,"oguz"],[1050,1237,"kipcak"],[1237,END,"altin-orda"]],
 "desti-kipcak": [[1000,1050,"oguz"],[1050,1237,"kipcak"],[1237,END,"altin-orda"]],
 "karadeniz-bozkiri": [[1000,1091,"pecenek"],[1091,1240,"kipcak"],[1240,END,"altin-orda"]],
 "idil": [[1000,1236,"bulgar"],[1236,END,"altin-orda"]],
 "kiev": [[1000,1240,"kiev"],[1240,END,"altin-orda"]],
 "curcan": [[1000,1043,"ziyari"],[1043,1157,"buyuk-selcuklu"],[1157,1220,"harizmsah"],[1220,END,"mogol"]],
 "amul": [[1000,1043,"ziyari"],[1043,1157,"buyuk-selcuklu"],[1157,1220,"harizmsah"],[1220,END,"mogol"]],
 "rey": [[1000,1042,"buveyhi"],[1042,1118,"buyuk-selcuklu"],[1118,1194,"irak-selcuklu"],[1194,1221,"harizmsah"],[1221,END,"mogol"]],
 "alamut": [[1000,1090,"buyuk-selcuklu"],[1090,1256,"nizari"],[1256,END,"mogol"]],
 "hemedan": [[1000,1046,"kakuyi"],[1046,1118,"buyuk-selcuklu"],[1118,1194,"irak-selcuklu"],[1194,1221,"harizmsah"],[1221,END,"mogol"]],
 "isfahan": [[1000,1051,"kakuyi"],[1051,1118,"buyuk-selcuklu"],[1118,1194,"irak-selcuklu"],[1194,1228,"harizmsah"],[1228,END,"mogol"]],
 "kirman": [[1000,1048,"buveyhi"],[1048,1187,"kirman-selcuklu"],[1187,1196,"oguz"],[1196,1222,"harizmsah"],[1222,END,"mogol"]],
 "siraz": [[1000,1062,"buveyhi"],[1062,1148,"buyuk-selcuklu"],[1148,1282,"salgurlu"],[1282,END,"mogol"]],
 "ahvaz": [[1000,1062,"buveyhi"],[1062,1118,"buyuk-selcuklu"],[1118,1194,"irak-selcuklu"],[1194,1258,"abbasi"],[1258,END,"mogol"]],
 "basra": [[1000,1055,"buveyhi"],[1055,1118,"buyuk-selcuklu"],[1118,1157,"irak-selcuklu"],[1157,1258,"abbasi"],[1258,END,"mogol"]],
 "bagdat": [[1000,1055,"buveyhi"],[1055,1058,"buyuk-selcuklu"],[1058,1060,"fatimi"],[1060,1118,"buyuk-selcuklu"],[1118,1152,"irak-selcuklu"],[1152,1258,"abbasi"],[1258,END,"mogol"]],
 "hille": [[1000,1163,"mezyedi"],[1163,1258,"abbasi"],[1258,END,"mogol"]],
 "musul": [[1000,1096,"ukayli"],[1096,1127,"buyuk-selcuklu"],[1127,1262,"zengi"],[1262,END,"mogol"]],
 "amid": [[1000,1085,"mervani"],[1085,1093,"buyuk-selcuklu"],[1093,1183,"inalogullari"],[1183,1232,"artuklu"],[1232,1241,"eyyubi"],[1241,1260,"anadolu-selcuklu"],[1260,END,"mogol"]],
 "meyyafarikin": [[1000,1085,"mervani"],[1085,1104,"buyuk-selcuklu"],[1104,1118,"ahlatsah"],[1118,1185,"artuklu"],[1185,1260,"eyyubi"],[1260,END,"mogol"]],
 "mardin": [[1000,1085,"mervani"],[1085,1104,"buyuk-selcuklu"],[1104,END,"artuklu"]],
 "hasankeyf": [[1000,1085,"mervani"],[1085,1101,"buyuk-selcuklu"],[1101,1232,"artuklu"],[1232,END,"eyyubi"]],
 "ahlat": [[1000,1085,"mervani"],[1085,1100,"buyuk-selcuklu"],[1100,1207,"ahlatsah"],[1207,1233,"eyyubi"],[1233,1243,"anadolu-selcuklu"],[1243,END,"mogol"]],
 "malazgirt": [[1000,1071,"bizans"],[1071,1100,"buyuk-selcuklu"],[1100,1207,"ahlatsah"],[1207,1233,"eyyubi"],[1233,1243,"anadolu-selcuklu"],[1243,END,"mogol"]],
 "erzurum": [[1000,1071,"bizans"],[1071,1202,"saltuklu"],[1202,1256,"anadolu-selcuklu"],[1256,END,"mogol"]],
 "ani": [[1000,1045,"ermeni"],[1045,1064,"bizans"],[1064,1072,"buyuk-selcuklu"],[1072,1199,"seddadi"],[1199,1236,"gurcistan"],[1236,END,"mogol"]],
 "gence": [[1000,1075,"seddadi"],[1075,1118,"buyuk-selcuklu"],[1118,1146,"irak-selcuklu"],[1146,1225,"ildenizli"],[1225,1231,"harizmsah"],[1231,END,"mogol"]],
 "tebriz": [[1000,1071,"ravvadi"],[1071,1118,"buyuk-selcuklu"],[1118,1175,"irak-selcuklu"],[1175,1225,"ildenizli"],[1225,1231,"harizmsah"],[1231,END,"mogol"]],
 "trabzon": [[1000,1204,"bizans"],[1204,END,"trabzon"]],
 "sivas": [[1000,1075,"bizans"],[1075,1174,"danismend"],[1174,END,"anadolu-selcuklu"]],
 "amasya": [[1000,1075,"bizans"],[1075,1174,"danismend"],[1174,END,"anadolu-selcuklu"]],
 "kayseri": [[1000,1075,"bizans"],[1075,1169,"danismend"],[1169,END,"anadolu-selcuklu"]],
 "malatya": [[1000,1071,"bizans"],[1071,1103,"ermeni"],[1103,1178,"danismend"],[1178,END,"anadolu-selcuklu"]],
 "konya": [[1000,1080,"bizans"],[1080,END,"anadolu-selcuklu"]],
 "iznik": [[1000,1081,"bizans"],[1081,1097,"anadolu-selcuklu"],[1097,1204,"bizans"],[1204,1261,"iznik-imp"],[1261,END,"bizans"]],
 "izmir": [[1000,1081,"bizans"],[1081,1097,"caka"],[1097,1204,"bizans"],[1204,1261,"iznik-imp"],[1261,END,"bizans"]],
 "antalya": [[1000,1207,"bizans"],[1207,1212,"anadolu-selcuklu"],[1212,1216,"latin"],[1216,END,"anadolu-selcuklu"]],
 "tarsus": [[1000,1080,"bizans"],[1080,END,"ermeni"]],
 "istanbul": [[1000,1204,"bizans"],[1204,1261,"latin"],[1261,END,"bizans"]],
 "edirne": [[1000,1204,"bizans"],[1204,1225,"latin"],[1225,1261,"iznik-imp"],[1261,END,"bizans"]],
 "selanik": [[1000,1204,"bizans"],[1204,1224,"latin"],[1224,1246,"bizans"],[1246,1261,"iznik-imp"],[1261,END,"bizans"]],
 "atina": [[1000,1204,"bizans"],[1204,END,"latin"]],
 "tirnova": [[1000,1185,"bizans"],[1185,END,"bulgar2"]],
 "kibris": [[1000,1191,"bizans"],[1191,END,"kibris"]],
 "antakya": [[1000,1084,"bizans"],[1084,1086,"anadolu-selcuklu"],[1086,1098,"buyuk-selcuklu"],[1098,1268,"hacli"],[1268,END,"memluk"]],
 "urfa": [[1000,1087,"bizans"],[1087,1095,"buyuk-selcuklu"],[1095,1098,"ermeni"],[1098,1144,"hacli"],[1144,1182,"zengi"],[1182,1260,"eyyubi"],[1260,END,"mogol"]],
 "halep": [[1000,1080,"mirdasi"],[1080,1086,"ukayli"],[1086,1094,"buyuk-selcuklu"],[1094,1117,"suriye-selcuklu"],[1117,1128,"artuklu"],[1128,1183,"zengi"],[1183,1260,"eyyubi"],[1260,END,"memluk"]],
 "dimask": [[1000,1076,"fatimi"],[1076,1079,"atsiz"],[1079,1104,"suriye-selcuklu"],[1104,1154,"boriler"],[1154,1174,"zengi"],[1174,1260,"eyyubi"],[1260,END,"memluk"]],
 "trablus": [[1000,1109,"ammar"],[1109,1289,"hacli"],[1289,END,"memluk"]],
 "sur": [[1000,1124,"fatimi"],[1124,1291,"hacli"],[1291,END,"memluk"]],
 "kudus": [[1000,1073,"fatimi"],[1073,1079,"atsiz"],[1079,1086,"suriye-selcuklu"],[1086,1098,"artuklu"],[1098,1099,"fatimi"],[1099,1187,"hacli"],[1187,1229,"eyyubi"],[1229,1244,"hacli"],[1244,1250,"eyyubi"],[1250,END,"memluk"]],
 "askalan": [[1000,1153,"fatimi"],[1153,1187,"hacli"],[1187,1250,"eyyubi"],[1250,END,"memluk"]],
 "kahire": [[1000,1171,"fatimi"],[1171,1250,"eyyubi"],[1250,END,"memluk"]],
 "iskenderiye": [[1000,1171,"fatimi"],[1171,1250,"eyyubi"],[1250,END,"memluk"]],
}
NEW_CITIES = [
 {"id": "kastamonu", "tr": "Kastamonu", "lat": 41.38, "lon": 33.78, "spans": [[1000,1080,"bizans"],[1080,1175,"danismend"],[1175,END,"anadolu-selcuklu"]], "src": ["mesud-i"], "yaklasik": True},
 {"id": "ankara", "tr": "Ankara", "lat": 39.93, "lon": 32.86, "spans": [[1000,1073,"bizans"],[1073,1101,"anadolu-selcuklu"],[1101,1127,"bizans"],[1127,1175,"danismend"],[1175,END,"anadolu-selcuklu"]], "src": ["haclilar", "suleyman-sah-i"], "yaklasik": True},
 {"id": "eskisehir", "tr": "Eskişehir", "lat": 39.78, "lon": 30.52, "spans": [[1000,1080,"bizans"],[1080,1175,"anadolu-selcuklu"],[1175,1180,"bizans"],[1180,1288,"anadolu-selcuklu"],[1288,END,"osmanli"]], "src": ["kilicarslan-ii", "eskisehir"], "yaklasik": True},
 {"id": "bilecik", "tr": "Bilecik (Söğüt)", "lat": 40.14, "lon": 29.98, "spans": [[1000,1299,"bizans"],[1299,END,"osmanli"]], "src": ["osman-i"], "yaklasik": True},
 {"id": "kutahya", "tr": "Kütahya", "lat": 39.42, "lon": 29.98, "spans": [[1000,1182,"bizans"],[1182,1290,"anadolu-selcuklu"],[1290,END,"germiyan"]], "src": ["mesud-ii"], "yaklasik": True},
 {"id": "denizli", "tr": "Lâdik (Denizli)", "lat": 37.78, "lon": 29.09, "spans": [[1000,1206,"bizans"],[1206,END,"anadolu-selcuklu"]], "src": ["keyhusrev-i"], "yaklasik": True},
 {"id": "karaman", "tr": "Lârende (Karaman)", "lat": 37.18, "lon": 33.22, "spans": [[1000,1080,"bizans"],[1080,1277,"anadolu-selcuklu"],[1277,END,"karaman"]], "src": ["keyhusrev-iii"], "yaklasik": True},
 {"id": "erzincan", "tr": "Erzincan", "lat": 39.75, "lon": 39.49, "spans": [[1000,1071,"bizans"],[1071,1228,"mengucek"],[1228,END,"anadolu-selcuklu"]], "src": ["keyhusrev-ii"], "yaklasik": True},
 {"id": "harput", "tr": "Harput", "lat": 38.70, "lon": 39.25, "spans": [[1000,1071,"bizans"],[1071,1112,"buyuk-selcuklu"],[1112,1234,"artuklu"],[1234,END,"anadolu-selcuklu"]], "src": ["keykubad-i"], "yaklasik": True},
 {"id": "sinop", "tr": "Sinop", "lat": 42.02, "lon": 35.15, "spans": [[1000,1204,"bizans"],[1204,1214,"trabzon"],[1214,1259,"anadolu-selcuklu"],[1259,1266,"trabzon"],[1266,END,"anadolu-selcuklu"]], "src": ["sinop", "keykavus-i"]},
 {"id": "alanya", "tr": "Alanya", "lat": 36.54, "lon": 32.00, "spans": [[1000,1221,"bizans"],[1221,END,"anadolu-selcuklu"]], "src": ["alanya"]},
]

known = {c["id"] for c in d["cities"]}
for c in d["cities"]:
    if c.get("void"): continue
    if c["id"] in S:
        c["spans"] = S[c["id"]]
    elif c["spans"] and c["spans"][-1][1] == 1200:
        c["spans"][-1][1] = END
for c in NEW_CITIES:
    assert c["id"] not in known
d["cities"][-21:-21] = NEW_CITIES  # 'void' noktalardan önce
for c in d["cities"]:
    for a, b, s in c.get("spans", []):
        assert s in d["states"], (c["id"], s)
d["meta"]["compiled"] = "2026-10-28"
d["meta"]["method"] += " 1243 sonrası Anadolu, Moğol metbûluğuna rağmen Anadolu Selçuklu rengindedir; doğrudan Moğol idaresine geçen doğu şehirleri Moğol rengini alır."
P.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(d["cities"]), "nokta,", len(d["states"]), "devlet")
