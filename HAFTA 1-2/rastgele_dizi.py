# 1 ile 100 arasında rastgele 10 tam sayı üretip listeye ekleme

import random

sayilar = []

for _ in range(10):
    sayilar.append(random.randint(1, 100))

print("Rastgele sayılar:", sayilar)
