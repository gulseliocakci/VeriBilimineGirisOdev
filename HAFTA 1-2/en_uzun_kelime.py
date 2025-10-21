# Metindeki en uzun kelimeyi bulma

metin = input("Bir metin girin: ")
kelimeler = metin.split()

if kelimeler:
    en_uzun = max(kelimeler, key=len)
    print("En uzun kelime:", en_uzun)
else:
    print("Hiç kelime bulunamadı.")
