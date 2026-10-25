import sys,re
pat=re.compile(r'savaş|yenil|mağlûp|bozgun|kuşat|muhasara|çarpış|muharebe|zaptet|esir al|hezimet|galip',re.I)
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read()
    i=s.find('Kopyalama metni'); j=s.find('BİBLİYOGRAFYA')
    body=s[i+15:j]
    sents=re.split(r'(?<=[.!?])\s+',body)
    out=[x.strip() for x in sents if pat.search(x)]
    sys.stdout.buffer.write(('\n##### '+f+'\n'+'\n'.join('- '+x for x in out)+'\n').encode('utf-8'))
