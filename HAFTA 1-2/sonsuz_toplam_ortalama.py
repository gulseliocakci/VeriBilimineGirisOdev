# Kullanıcı sonsuz sayıda değer girebilir, toplam ve ortalama hesaplanır

sayilar = []
print("Sayı girin (çıkmak için boş bırakın):")

while True:
    giris = input()
    if giris == "":
        break
    try:
        sayilar.append(float(giris))
    except ValueError:
        print("Geçersiz giriş, sadece sayı girin.")

if sayilar:
    toplam = sum(sayilar)
    ortalama = toplam / len(sayilar)
    print("Toplam:", toplam)
    print("Ortalama:", ortalama)
else:
    print("Hiç sayı girilmedi.")
