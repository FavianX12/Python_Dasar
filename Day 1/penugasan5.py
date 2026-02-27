# Program Segitiga Bintang Sama Kaki
jumlah_baris = int(input("Masukkan jumlah baris: "))

for i in range(1, jumlah_baris + 1):
    # Loop untuk spasi
    for j in range(jumlah_baris - i):
        print(" ", end="")
    # Loop untuk bintang
    for k in range(2 * i - 1):
        print("*", end="")
    # Pindah baris
    print()