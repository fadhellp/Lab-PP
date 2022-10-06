import math

tinggi = int(input('Tinggi Menara Kapal :'))
a = int(input('Masukkan sudut a :'))
b = int(input('masukkan sudut b :'))

a = int(a)*math.pi/180     
b = int(b)*math.pi/180
panjang_a = math.tan(a)*(tinggi)
panjang_b = math.tan(b)*(tinggi)
panjang_kapal = panjang_a - panjang_b
print('Panjang kapal =', round(panjang_kapal,1),'m')