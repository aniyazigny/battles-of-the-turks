"""Bir üretici dosyasındaki R listesine, adı verilen kaydın hemen arkasına yeni bir kayıt (Python tuple metni) ekler.
Kontrol turlarında eksik muharebeleri eklemek için kullanılır. Kullanım (Python içinden):
    from insert_record import insert_after
    insert_after("tools/make_x.py", "Önceki kayıt (1500)", '("Yeni (1501)", ...),')
Aynı adlı kayıt zaten varsa dokunmaz."""
import re
from pathlib import Path


def insert_after(path, after_name, tuple_text):
    p = Path(path)
    s = p.read_text(encoding="utf-8")
    new_name = re.match(r'\s*\("([^"]+)"', tuple_text).group(1)
    if f'("{new_name}"' in s:
        return False
    key = f'\n("{after_name}"'
    i = s.index(key)
    j = s.find('\n("', i + 1)
    end_r = s.find('\n]', i + 1)
    j = end_r if j == -1 or j > end_r else j
    s = s[:j] + "\n" + tuple_text.rstrip() + s[j:]
    p.write_text(s, encoding="utf-8")
    return True
