# Metindeki ilk ve son kelimeyi bulma

metin = input("Bir cümle girin: ")
kelimeler = metin.split()

if len(kelimeler) >= 1:
    print("İlk kelime:", kelimeler[0])
    print("Son kelime:", kelimeler[-1])
else:
    print("Hiç kelime bulunamadı.")
