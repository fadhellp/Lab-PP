print("Nama\t: Muhammad Khaekal\nNIM\t: H071221039")
print(25*"=")
print("Menghitung panjang kapal")
print(25*"=")

import math
h = int(input("Tinggi menara ="))
a = int(input("Masukkan sudut elevasi a ="))
b = int(input("Masukkan sudut elevasi b ="))

a = (a)*math.pi/180
b = (b)*math.pi/180
panjang_a = math.tan(a)*(h)
panjang_b = math.tan(b)*(h)
panjang_kapal = panjang_a - panjang_b
print("Panjang kapal =" , round(panjang_kapal,1),"m")
#print(f"Panjang kapal = {panjang_kapal:.1f} m") #
print(25*"=")
print("\tTerima Kasih")
print(25*"=")