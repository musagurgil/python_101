sayi = int(input("Sayi: "))

faktoriyel = 1

if sayi < 0:
    print("Negatif sayıların faktoryeli hesaplanamaz")
elif sayi == 0:
    print("Sonuç : 1")
else:
    for i in range(1, sayi + 1):
        faktoriyel = faktoriyel * i

print("Sonuç : ",faktoriyel)
