# -100 ile +100 arasındaki 5'e tam bölünen sayıları yan yana yazdırma

for i in range(-100, 101):
    if i % 5 == 0:
        print(i, end=" ")

print("\nTamamlandı.")
