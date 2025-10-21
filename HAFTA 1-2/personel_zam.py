# Personel maaşına yüzde zam ekleme

maas = float(input("Personelin maaşını girin: "))
zam_yuzdesi = float(input("Yüzde kaç zam yapılacak? "))

yeni_maas = maas + (maas * zam_yuzdesi / 100)
print(f"Yeni maaş: {yeni_maas:.2f} TL")
