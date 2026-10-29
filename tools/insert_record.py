"""Bir üretici dosyasındaki R listesine, adı verilen kaydın hemen arkasına yeni bir kayıt (Python tuple metni) ekler.
Kontrol turlarında eksik muharebeleri eklemek için kullanılır. Kullanım (Python içinden):
    from insert_record import insert_after
    insert_after("tools/make_x.py", "Önceki kayıt (1500)", '("Yeni (1501)", ...),')
Bazı üreticilerde kayıt bir devlet sabitiyle başlar: (ZEN, "Ad", ...). Aynı adlı kayıt zaten varsa dokunmaz."""
import re
from pathlib import Path

PRE = r'\n\((?:[A-Z]+, )?"'


def insert_after(path, after_name, tuple_text):
    p = Path(path)
    s = p.read_text(encoding="utf-8")
    new_name = re.match(r'\s*\((?:[A-Z]+, )?"([^"]+)"', tuple_text).group(1)
    if re.search(PRE + re.escape(new_name) + '"', s):
        return False
    i = re.search(PRE + re.escape(after_name) + '"', s).start()
    m = re.compile(PRE).search(s, i + 1)
    end_r = s.find('\n]', i + 1)
    j = end_r if m is None or m.start() > end_r else m.start()
    s = s[:j] + "\n" + tuple_text.rstrip() + s[j:]
    p.write_text(s, encoding="utf-8")
    return True
