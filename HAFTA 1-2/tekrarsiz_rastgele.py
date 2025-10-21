# Tekrarsız rastgele sayı üretme

import random

adet = int(input("Kaç adet rastgele sayı istiyorsunuz? "))
min_sayi = int(input("Minimum sayı: "))
max_sayi = int(input("Maksimum sayı: "))

if adet > (max_sayi - min_sayi + 1):
    print("Hata: Tekrarsız sayı üretmek için aralık yeterli değil.")
else:
    sayilar = random.sample(range(min_sayi, max_sayi+1), adet)
    print("Tekrarsız rastgele sayılar:", sayilar)
