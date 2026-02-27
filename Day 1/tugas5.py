import math

# Ukuran "canvas"
width = 40
height = 20

# Titik tengah dan radius
center_x = width // 2
center_y = height // 2
radius = 8

for y in range(height):
    for x in range(width):
        # Jarak dari pusat lingkaran besar
        dist1 = math.sqrt((x - center_x)**2 + (y - center_y)**2)
        
        # Jarak dari pusat lingkaran kecil (untuk efek sabit)
        dist2 = math.sqrt((x - (center_x + 3))**2 + (y - center_y)**2)
        
        # Cetak jika di dalam lingkaran besar dan di luar lingkaran kecil
        if dist1 < radius and dist2 > radius - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()