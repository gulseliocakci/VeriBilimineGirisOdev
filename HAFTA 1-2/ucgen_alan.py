# Üç kenarı verilen üçgenin alanını hesaplama (Heron formülü)

import math

a = float(input("Birinci kenarı girin: "))
b = float(input("İkinci kenarı girin: "))
c = float(input("Üçüncü kenarı girin: "))

# Üçgen olup olmadığını kontrol
if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    alan = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Üçgenin alanı: {alan:.2f}")
else:
    print("Geçersiz üçgen kenarları!")
