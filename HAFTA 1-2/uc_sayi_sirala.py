# Üç sayıyı karşılaştırıp küçükten büyüğe sıralama

a = float(input("Birinci sayıyı girin: "))
b = float(input("İkinci sayıyı girin: "))
c = float(input("Üçüncü sayıyı girin: "))

sayilar = [a, b, c]
sayilar.sort()

print("Sıralama:", sayilar)
