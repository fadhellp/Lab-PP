from re import I


harga = int(input("harga barang: "))
jumlah_pembayaran = int(input("jumlah pembayaran: "))

kembalian = jumlah_pembayaran - harga
pecahan_uang = [100000,50000,20000,10000,5000,2000,1000] 
for i in (pecahan_uang):
    bagi = kembalian // i 
    print("%d uang Rp %d"%(bagi,i))
    kembalian % i
