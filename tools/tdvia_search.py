"""TDVİA'da arama yapar ve sonuçları 'slug | başlık | açıklama' olarak yazar.
Kullanım: python -I -X utf8 tools/tdvia_search.py [-t] <sorgu> ...   (-t: madde içeriklerinde ara; varsayılan: başlıklarda)"""
import sys,re,html,urllib.request,urllib.parse
args=sys.argv[1:]; mode='m'
if args and args[0]=='-t': mode='t'; args=args[1:]
for q in args:
    url='https://islamansiklopedisi.org.tr/arama/?'+urllib.parse.urlencode({'q':q,'p':mode})
    s=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read().decode('utf-8','replace')
    print('#',q)
    for slug,title,desc in re.findall(r'<a href=/([^ >]+)>(.*?)</a><br /><span class="desc">(.*?)</span>',s):
        print(' ',slug,'|',html.unescape(re.sub(r'<[^>]+>','',title)).replace('\xa0',' ').strip(),'|',html.unescape(desc)[:110])
