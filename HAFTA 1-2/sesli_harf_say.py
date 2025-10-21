# Metindeki sesli harflerin sayısını bulma

metin = input("Bir metin girin: ").lower()
sesli = "aeıioöuü"

sayac = 0
for harf in metin:
    if harf in sesli:
        sayac += 1

print("Sesli harf sayısı:", sayac)
