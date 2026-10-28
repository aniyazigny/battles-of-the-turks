"""İndirilmiş TDVİA sayfasından madde gövdesini çıkarır.
Çok bölümlü maddelerde ('3 bölümden oluşan maddenin 1. bölümüdür') her bölüm ayrı bir 'Kopyalama metni' ile başlar
ve kendi 'BİBLİYOGRAFYA'sıyla biter; bütün bölümlerin gövdeleri birleştirilir."""
import re


def body(text):
    parts = []
    for chunk in text.split("Kopyalama metni")[1:]:
        k = chunk.find("BİBLİYOGRAFYA")
        parts.append(chunk[:k] if k >= 0 else chunk)
    return "\n".join(parts)


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", body(text)) if s.strip()]
