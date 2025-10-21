# Kullanıcının girdiği sayılardan kümülatif toplam hesaplama

sayilar = input("Sayıları aralarına boşluk koyarak girin: ").split()
kumulatif = 0

for s in sayilar:
    try:
        sayi = float(s)
        kumulatif += sayi
        print(f"{s} eklendi, kümülatif toplam: {kumulatif}")
    except ValueError:
        print(f"{s} geçerli bir sayı değil, atlandı.")
