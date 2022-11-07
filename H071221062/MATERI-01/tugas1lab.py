print ("NAMA\t : AHMAD FAUZHAN RAMADHAN B")
print ("NIM\t : H071221062")
print ("Grup\t : A")

import math
jari_jari_alas = int(input( "Masukkan jari_Jari_alas :"))
tinggi = int(input( "Masukkan tinggi :" ))
s = math.sqrt (jari_jari_alas**2 + tinggi**2)
luas_permukaan = math.pi*jari_jari_alas * s + math.pi*jari_jari_alas**2
print (round(luas_permukaan,2))

volume = 1/3 * math.pi * jari_jari_alas**2 * tinggi
print (round(volume,2))

print ("=====ARIGATOOOO=====")