# Sınıfı geçmek için gereken final notunu hesaplama

vize = float(input("Vize notunuzu girin (0-100): "))
gecme_notu = 50  # Örn: geçme notu 50

# Varsayım: vize %40, final %60
gereken_final = (gecme_notu - vize*0.4) / 0.6

if gereken_final > 100:
    print("Maalesef geçmek için gereken final notu 100'den yüksek!")
elif gereken_final < 0:
    print("Zaten geçtiniz, finale gerek yok!")
else:
    print(f"Geçmek için finalden en az {gereken_final:.2f} almalısınız.")
