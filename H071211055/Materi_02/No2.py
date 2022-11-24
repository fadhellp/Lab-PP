import math
gol = (input('golongan = '))
p = int(input('daya = '))
kWH = int(input('pemakaian = '))

R1_900 = 1352
R1_1300 = 144470
R1_2200 = 144470

R2_3500 = 169953
R3_6600 = 169953

B2_6600 = 1444.7
B3_200 = 111474

I3_200 = 131412
P1_6600 = 152328

hasil = 0
if gol == 'R1':
    if p == 900:
        hasil = kWH*R1_900
    elif p == 1300:
        hasil = kWH*R1_1300
    elif p == 2200:
        hasil = kWH*R1_2200
elif gol == 'R2':
    if p >= 3500 and 5500:
        hasil = kWH*R2_3500
elif gol == 'R3':
    if p >= 6600:
        hasil = kWH*R3_6600

elif gol == 'B2':
    if p >= 6600 and  200:
        hasil = kWH*B2_6600
elif gol == 'B3':
    if p > 200:
        hasil = kWH*B3_200

elif gol == 'I3':
    if p > 200:
        hasil = kWH*I3_200

elif gol == 'P1':
    if p >= 6600 and 200:
        hasil = kWH*P1_6600
    else:
        print('data tidak valid')

tes = (f'jumlah tagihan anda {hasil:,.1f}')
# tes.replace(',', '.')
# indexT = tes.rindex('.')
# tes = tes[:indexT] + ',' + tes[indexT+1:]
print(tes)
