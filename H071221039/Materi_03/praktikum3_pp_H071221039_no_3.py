print(40*"=")
print("Nama     : Muhammad Khaekal")
print("Nim      : H071221039")
print("Kelompok : C")
print(40*"=")

try :
    total_pembayaran  = int(input("Masukkan jumlah pembayaran : "))
    harga_barang = int(input("Masukkan harga barang : "))

    pecahan_uang = [100000,50000,20000,10000,5000,2000,1000]

    kembalian = total_pembayaran - harga_barang

    if harga_barang > total_pembayaran :
        print("Uang tidak cukup")
    for x in pecahan_uang : # x =jenis pecahan_uang yang akan dikembalikan
        if kembalian < x:
            continue
        y = int(kembalian/x) # y = banyaknya jenis_uang yang akan dikembalikan
        kembalian = kembalian - (x*y)
        print(y, "Uang Rp.", x)
except :
    print("Inputan salah")

print(40*"=")
print("TERIMA KASIH")
print(40*"=")