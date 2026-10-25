#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KOMŞUNUN KÖPEĞİ HAVLAMA RİTMİ ANALİZİ
Dünyanın en ciddi bilimsel aracı. NASA bunu kullanmayı reddetti çünkü çok ileri seviyede.
"""

import random
import time
import base64

# Gizli saklı mesaj (decode etmeyin, ciddi):
_gizli_siyasi = base64.b64decode(b'c2l5YXNldCBrw7ZwZWsgaGF2bGFtYXNpbmRhbiBkYWhhIGfDvHJsw7xsdMO8IGFtYSBkYWhhIGF6IGFubGFtbMSx').decode('utf-8')
# Üstteki satırı çalıştırırsanız evren çöker. Sakladım.

def uret_havlama(sayi=5):
    """Rastgele havlama dizisi üretir. Bilimsel."""
    sesler = ["hav", "havv", "hav hav", "HAV!", "haf", "wuf", "miyav (yanlış köpek)", "havhavhav"]
    return " ".join(random.choice(sesler) for _ in range(sayi))

def analiz_et(havlama):
    """Ritmi analiz eder. %100 doğru, %0 işe yarar."""
    kelimeler = havlama.split()
    uzunluk = len(kelimeler)
    bpm = random.randint(60, 180)  # Köpek BPM'si, bilimsel
    yorum = random.choice([
        "Bu ritim Mahler'in senfonisinden daha derin.",
        "Komşu köpek varoluşsal kriz geçiriyor.",
        "Tahmin: Bir sonraki havlama 3.7 saniye sonra gelecek. Veya gelmeyecek.",
        "Analiz sonucu: Köpek 'idare eder' diyor.",
        "Bu ritim Türkçe'nin şiirsel ritmiyle örtüşüyor."
    ])
    return {
        "havlama_sayisi": uzunluk,
        "tahmini_bpm": bpm,
        "derin_yorum": yorum,
        "kesinlik": "%99.999 (yanılma payı %100)"
    }

def tahmin_et():
    """Gelecek havlamayı tahmin eder."""
    gelecek = uret_havlama(1)
    return f"Gelecek havlama: '{gelecek}' (veya 'hav' değil, 'niye' olabilir)"

def main():
    print("=== KOMŞUNUN KÖPEĞİ HAVLAMA RİTMİ ANALİZİ v1.0 ===")
    print("Bilim başlıyor... (asla bitmez)\n")
    time.sleep(1)
    
    for i in range(3):
        hav = uret_havlama(random.randint(3, 7))
        print(f"Kayıt {i+1}: {hav}")
        sonuc = analiz_et(hav)
        print(f"  Analiz: {sonuc['havlama_sayisi']} havlama, BPM: {sonuc['tahmini_bpm']}")
        print(f"  Yorum: {sonuc['derin_yorum']}")
        print(f"  Kesinlik: {sonuc['kesinlik']}\n")
        time.sleep(0.5)
    
    print(tahmin_et())
    print("\nAnaliz tamamlandı. Komşu köpek artık bilimsel olarak anlaşıldı.")
    print("Bu programı çalıştırmak için: python havlama_analizi.py")
    # print(_gizli_siyasi)  # Açma, saklı kalsın.

if __name__ == "__main__":
    main()
