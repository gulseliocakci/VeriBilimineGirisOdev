# Girilen sayının asal çarpanlarını bulma

n = int(input("Bir sayı girin: "))
sayi = n
carpanlar = []

i = 2
while i <= n:
    if n % i == 0:
        carpanlar.append(i)
        n //= i
    else:
        i += 1

print(f"{sayi} sayısının asal çarpanları:", carpanlar)
