panjang = float(input("\nMasukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

keliling_pp = 2 * (panjang + lebar)
luas_pp = panjang * lebar

print("\n=== PERSEGI PANJANG ===")
print("Keliling:", keliling_pp)
print("Luas:", luas_pp)


# =========================
# TRAPESIUM
# =========================
a = float(input("\nMasukkan sisi atas trapesium: "))
b = float(input("Masukkan sisi bawah trapesium: "))
c = float(input("Masukkan sisi miring kiri: "))
d = float(input("Masukkan sisi miring kanan: "))
tinggi = float(input("Masukkan tinggi trapesium: "))

keliling_trapesium = a + b + c + d
luas_trapesium = 0.5 * (a + b) * tinggi

print("\n=== TRAPESIUM ===")
print("Keliling:", keliling_trapesium)
print("Luas:", luas_trapesium)