print("1. Matrisi girin:")
matris1 = [[int(input("Bir eleman girin: ")) for _ in range(3)] for _ in range(3)]

print("2. Matrisi girin:")
matris2 = [[int(input("Bir eleman girin: ")) for _ in range(3)] for _ in range(3)]

print("Sonuç Matrisi:")
sonuc_matrisi = [[matris1[i][j] + matris2[i][j] for j in range(3)] for i in range(3)]
for satir in sonuc_matrisi:
    print(satir)