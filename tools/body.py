import sys
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read()
    i=s.find('Kopyalama metni'); j=s.find('İlişkili Maddeler')
    b=s[i+15:j if j>0 else None]
    k=b.find('BİBLİYOGRAFYA')
    body,bib=(b[:k],b[k:]) if k>0 else (b,'')
    sys.stdout.buffer.write(('\n##### '+f+'\n'+body+'\n[BIB] '+' | '.join(l.strip() for l in bib.splitlines()[1:] if l.strip())[:1500]+'\n').encode('utf-8'))
