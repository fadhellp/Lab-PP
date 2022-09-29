nama_penjual= input("Nama_penjual: ")
gaji_pokok= float(input("Gaji pokok: "))
total_penjualan= float(input("total penjualan: "))

persentase_yang_diterima_seller= 0.15
total_penjualan_yang_diterima_seller= persentase_yang_diterima_seller* total_penjualan
gaji= gaji_pokok+total_penjualan_yang_diterima_seller
print(round(gaji,2))