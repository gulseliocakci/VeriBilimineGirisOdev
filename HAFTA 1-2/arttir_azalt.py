# + veya - girildikçe sayıyı artıran veya azaltan program

sayi = 0
print("Başlangıç değeri:", sayi)
print("Her '+' basıldığında sayı 1 artar, '-' basıldığında 1 azalır. 'q' ile çık.")

while True:
    islem = input("İşlem (+, -, q): ")

    if islem == '+':
        sayi += 1
    elif islem == '-':
        sayi -= 1
    elif islem == 'q':
        print("Program sonlandırıldı.")
        break
    else:
        print("Geçersiz giriş.")
        continue

    print("Yeni değer:", sayi)
