# Kümülatif toplam hesaplama

sayilar = input("Sayıları aralarına boşluk koyarak girin: ").split()
kumulatif = 0
sonuclar = []

for s in sayilar:
    try:
        sayi = float(s)
        kumulatif += sayi
        sonuclar.append(kumulatif)
    except ValueError:
        print(f"{s} geçerli bir sayı değil, atlandı.")

print("Kümülatif toplamlar:", sonuclar)
