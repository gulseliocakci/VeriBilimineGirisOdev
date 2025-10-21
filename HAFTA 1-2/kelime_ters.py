# Her kelimeyi tersten yazdırma

cumle = input("Bir cümle girin: ")
kelimeler = cumle.split()

ters_kelimeler = [kelime[::-1] for kelime in kelimeler]

print("Tersten kelimeler:", " ".join(ters_kelimeler))
