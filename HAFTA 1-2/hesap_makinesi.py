# Basit hesap makinesi

print("Basit Hesap Makinesi")
print("İşlemler: +, -, *, /")

sayi1 = float(input("Birinci sayıyı girin: "))
islem = input("İşlem türünü girin (+, -, *, /): ")
sayi2 = float(input("İkinci sayıyı girin: "))

if islem == '+':
    print("Sonuç:", sayi1 + sayi2)
elif islem == '-':
    print("Sonuç:", sayi1 - sayi2)
elif islem == '*':
    print("Sonuç:", sayi1 * sayi2)
elif islem == '/':
    if sayi2 != 0:
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Hata: Sıfıra bölme yapılamaz!")
else:
    print("Geçersiz işlem seçtiniz.")
