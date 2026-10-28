"""İndirilmiş TDVİA metinlerinde düzenli ifadeye uyan cümleleri listeler (çok bölümlü maddelerin bütün bölümleri dahil).
Kullanım: python -I -X utf8 tools/kw.py <regex> [raw/<slug>.txt ...]   (dosya verilmezse raw/ altındaki hepsi)"""
import sys, re, glob, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tdvia_text import sentences

pat = re.compile(sys.argv[1], re.I)
files = sys.argv[2:] or sorted(glob.glob('raw/*.txt'))
for f in files:
    out = [x for x in sentences(open(f, encoding='utf-8').read()) if pat.search(x)]
    if out:
        print('##', os.path.basename(f)[:-4])
        for x in out[:6]: print('  -', x[:420])
