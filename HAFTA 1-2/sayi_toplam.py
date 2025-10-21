# Kullanıcının girdiği sayıların toplamını hesaplama

sayilar = input("Sayıları aralarına boşluk koyarak girin: ").split()
toplam = 0

for s in sayilar:
    try:
        toplam += float(s)
    except ValueError:
        print(f"{s} geçerli bir sayı değil, atlandı.")

print("Toplam =", toplam)
