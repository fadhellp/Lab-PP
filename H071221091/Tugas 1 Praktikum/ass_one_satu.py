data_list = ['Adrian Hidayat','H071221091']

print('Nama  :', data_list[0])
print('Nim   :', data_list[1])

print('\n==================\n')

print('Dik input 1: h=100   a=60    b=45\n'+'Dik input 2: h=120   a=87    b=50\n')

# from math import pi
# from math import tan
import math

tinggi = int(input('Tinggi Menara Kapal :'))
a = int(input('Masukkan sudut a :'))
b = int(input('masukkan sudut b :'))

a = a*math.pi/180     #180 ubah sudut ke radian
b = b*math.pi/180      #180 adalah nilai pi dalam python
panjang_a = math.tan(a)*(tinggi)
panjang_b = math.tan(b)*(tinggi)
panjang_kapal = panjang_a - panjang_b
print('Panjang kapal =', round(panjang_kapal,1),'m')    #round pembulatan angka diblkng koma

