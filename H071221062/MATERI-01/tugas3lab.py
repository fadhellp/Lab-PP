print ("NAMA\t : AHMAD FAUZHAN RAMADHAN B")
print ("NIM\t : H071221062")
print ("Grup\t : A")

import math
h = int(input("Tinggi menara ="))
a = int(input("Masukkan sudut elevasi a ="))
b = int(input("Masukkan sudut elevasi b ="))

a = a*math.pi/180
b = b*math.pi/180
panjang_a = math.tan(a)*h
panjang_b = math.tan(b)*h
panjang_kapal = panjang_a - panjang_b
print (round(panjang_kapal, 1))

print ("=====ARIGATOOOO=====")