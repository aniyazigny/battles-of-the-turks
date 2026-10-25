import sys,re,html,urllib.request,os
out=sys.argv[1]
for slug in sys.argv[2:]:
    try:
        r=urllib.request.urlopen(urllib.request.Request('https://islamansiklopedisi.org.tr/'+slug,headers={'User-Agent':'Mozilla/5.0'}),timeout=30)
        s=r.read().decode('utf-8','replace')
    except Exception as e:
        print(slug,'ERR',e); continue
    m=re.search(r'<title>(.*?)</title>',s,re.S)
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
    t=re.sub(r'<(br|p|div|h\d|li)[^>]*>','\n',t)
    t=html.unescape(re.sub(r'<[^>]+>','',t))
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(os.path.join(out,slug+'.txt'),'w',encoding='utf-8').write(t)
    print(slug,'|',(m.group(1).strip() if m else '?')[:80],'|',len(t))
