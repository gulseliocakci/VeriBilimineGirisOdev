# Kullanıcı hatalarını önleyen hesap makinesi

print("Güvenli Hesap Makinesi")
print("İşlemler: +, -, *, /")

try:
    sayi1 = float(input("Birinci sayıyı girin: "))
    islem = input("İşlem türünü girin (+, -, *, /): ")
    sayi2 = float(input("İkinci sayıyı girin: "))

    if islem == '+':
        sonuc = sayi1 + sayi2
    elif islem == '-':
        sonuc = sayi1 - sayi2
    elif islem == '*':
        sonuc = sayi1 * sayi2
    elif islem == '/':
        if sayi2 == 0:
            print("Hata: Sıfıra bölme yapılamaz!")
            sonuc = None
        else:
            sonuc = sayi1 / sayi2
    else:
        print("Hata: Geçersiz işlem seçtiniz.")
        sonuc = None

    if sonuc is not None:
        print("Sonuç:", sonuc)

except ValueError:
    print("Hata: Lütfen sadece sayı giriniz.")
