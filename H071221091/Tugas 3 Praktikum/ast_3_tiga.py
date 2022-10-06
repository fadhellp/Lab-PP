harga = int(input('harga barang: '))
bayar = int(input('nilai uang yang di bayarkan: '))

kembalian = bayar - harga

uang = [100000,50000,20000,10000,5000,1000]
for i in (uang):
    bagi = kembalian // i
    print('%d uang Rp %d'%(bagi,i))
    kembalian -= bagi * i


