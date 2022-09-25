data_list = ['Adrian Hidayat','H071221091']

print('Nama  :', data_list[0])
print('Nim   :', data_list[1])

print('\n==================\n')

print('Devon    ','500.0    ','1230.30\n'+'Alif     ','700.0    ','0.00\n'+'Ikhsan   ','1700.0   ','1230.50')

input('Nama Seller: ')
g_pokok = float(input('Gaji Pokok: '))
total_p = float(input('Total Penjualan: '))
rumus_1 = total_p * 0.15            #0.15 karena 15%        #c = b karena di soal menerima 15% dari penjualannnya
rumus_2 = round(g_pokok + rumus_1,2)      #fungsi round untk mmbultkan angka dblkng koma,(2)dua sndri untk input dua angka diblkng koma

print('TOTAL = $',rumus_2)

