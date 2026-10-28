"""İndirilmiş TDVİA metinlerinde düzenli ifadeye uyan cümleleri listeler.
Kullanım: python -I -X utf8 tools/kw.py <regex> [raw/<slug>.txt ...]   (dosya verilmezse raw/ altındaki hepsi)"""
import sys,re,glob,os
pat=re.compile(sys.argv[1],re.I)
files=sys.argv[2:] or sorted(glob.glob('raw/*.txt'))
for f in files:
    s=open(f,encoding='utf-8').read()
    i=s.find('Kopyalama metni'); j=s.find('BİBLİYOGRAFYA')
    if i<0: continue
    body=s[i+15:j if j>0 else None]
    out=[x.strip() for x in re.split(r'(?<=[.!?])\s+',body) if pat.search(x)]
    if out:
        print('##',os.path.basename(f)[:-4])
        for x in out[:6]: print('  -',x[:420])
