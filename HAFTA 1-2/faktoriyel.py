# Faktöriyel hesaplama ve açılımını yazdırma

n = int(input("Bir sayı girin: "))

faktoriyel = 1
aciklama = ""

for i in range(n, 0, -1):
    faktoriyel *= i
    aciklama += str(i)
    if i != 1:
        aciklama += " * "

print(f"{n}! =", faktoriyel)
print("Açılım:", aciklama)
