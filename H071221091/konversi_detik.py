data_list = ['Adrian Hidayat','H071221091']

print('Nama  :', data_list[0])
print('Nim   :', data_list[1])

print('\n==================\n')

print('Konversi Detik')
a = 3 ; b = 3 ; hasil = (1000*a)+(100*b)-(10*a)
print(hasil)

print('\n==================\n')

n = int(input('masukkan detik awal : ' ))
jam = n // 3600 
#n = n - 3600*jam
n = n%3600                      
menit = n // 60
n = n%60
#detik = n - 60*menit
print(f'{jam:02d}:{menit:02d}:{detik:02d}')
