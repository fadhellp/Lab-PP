print(28*"=")
print("NAMA\t: Muhammad Khaekal\nNIM\t: H071221039\nKelompok: C")
print(28*"=")
print("Mengubah Detik ke Format Jam")
JumlahDetik = int(input("Total detik : "))
print(28*"-")
print("Hasilnya adalah :")

Jam = JumlahDetik // 3600
Sisa = JumlahDetik % 3600

Menit = Sisa // 60
Detik = Sisa % 60

print(Jam,":",Menit,":",Detik)
print(28*"=")
print("\tTerima Kasih")
print(28*"=")