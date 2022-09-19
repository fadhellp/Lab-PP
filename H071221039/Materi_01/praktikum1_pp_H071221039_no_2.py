print(28*"=")
print("NAMA\t: Muhammad Khaekal\nNIM\t: H071221039\nKelompok: C")
print(28*"=")
print("Mengubah Detik ke Format Jam")
JumlahDetik = int(input("Total detik : "))
print(28*"-")
print("Hasilnya adalah :")

Jam = JumlahDetik // 3600
# Sisa = JumlahDetik % 3600

Menit = JumlahDetik // 60
# Detik = Sisa % 60

print("%02d:%02d:%02d"%(Jam, Menit % 60, JumlahDetik % 60))
print(28*"=")
print("\tTerima Kasih")
print(28*"=")