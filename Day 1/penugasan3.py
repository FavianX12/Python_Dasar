# Program menghitung dan mencetak bilangan ganjil dan genap

batas = int(input("Masukkan batas angka: "))

print("\nBilangan Genap:")
for i in range(1, batas + 1):
    if i % 2 == 0:
        print(i, end=" ")

print("\n\nBilangan Ganjil:")
for i in range(1, batas + 1):
    if i % 2 != 0:
        print(i, end=" ")