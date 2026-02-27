
# Menghitung volume tabung dan balok

# Input untuk tabung
r = float(input("Masukkan jari-jari tabung: "))
t_tabung = float(input("Masukkan tinggi tabung: "))

volume_tabung = 3.14 * r * r * t_tabung

# Input untuk balok
p = float(input("Masukkan panjang balok: "))
l = float(input("Masukkan lebar balok: "))
t_balok = float(input("Masukkan tinggi balok: "))

volume_balok = p * l * t_balok

# Output
print("\nVolume Tabung =", volume_tabung)
print("Volume Balok =", volume_balok)
