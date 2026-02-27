tinggi = int(input("Masukkan tinggi piramida: "))

for i in range(tinggi):
    print(" " * (tinggi - i - 1) + "*" * (2 * i + 1))