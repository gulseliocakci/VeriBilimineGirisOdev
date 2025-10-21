# Girilen sayıları toplayıp ortalamasını bulma

sayilar = []
while True:
    giris = input("Bir sayı girin (çıkmak için boş bırakın): ")
    if giris == "":
        break
    try:
        sayilar.append(float(giris))
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

if len(sayilar) > 0:
    toplam = sum(sayilar)
    ortalama = toplam / len(sayilar)
    print("Toplam:", toplam)
    print("Ortalama:", ortalama)
else:
    print("Hiç sayı girilmedi.")
