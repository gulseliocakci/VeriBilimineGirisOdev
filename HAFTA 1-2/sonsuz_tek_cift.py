# Sonsuz sayı girişi ve tek/çift yazdırma

print("Sayı girin (bitirmek için boş bırakın):")
while True:
    giris = input()
    if giris == "":
        break
    try:
        sayi = int(giris)
        if sayi % 2 == 0:
            print(sayi, "Çift")
        else:
            print(sayi, "Tek")
    except ValueError:
        print("Geçersiz giriş, lütfen sayı girin.")
