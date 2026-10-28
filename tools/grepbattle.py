"""İndirilmiş TDVİA maddelerinden savaş geçen cümleleri süzer (çok bölümlü maddelerin bütün bölümleri dahil)."""
import sys, re, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tdvia_text import sentences

pat = re.compile(r'savaş|yenil|mağlûp|bozgun|kuşat|muhasara|çarpış|muharebe|zaptet|esir al|hezimet|galip', re.I)
for f in sys.argv[1:]:
    out = [x for x in sentences(open(f, encoding='utf-8').read()) if pat.search(x)]
    sys.stdout.buffer.write(('\n##### ' + f + '\n' + '\n'.join('- ' + x for x in out) + '\n').encode('utf-8'))
