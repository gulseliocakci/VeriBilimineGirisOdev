# Sayısal notu harf karşılığına çevirme

notu = float(input("Notunuzu girin (0-100): "))

if 90 <= notu <= 100:
    harf = "AA"
elif 85 <= notu < 90:
    harf = "BA"
elif 80 <= notu < 85:
    harf = "BB"
elif 75 <= notu < 80:
    harf = "CB"
elif 70 <= notu < 75:
    harf = "CC"
elif 65 <= notu < 70:
    harf = "DC"
elif 60 <= notu < 65:
    harf = "DD"
elif 50 <= notu < 60:
    harf = "FD"
else:
    harf = "FF"

print("Harf notunuz:", harf)
