print ("NAMA\t : AHMAD FAUZHAN RAMADHAN B")
print ("NIM\t : H071221062")
print ("Grup\t : A")

print("Mengubah Detik ke Format Jam")
JumlahDetik = int(input("Total detik : "))
print("Hasilnya adalah :")

Jam = JumlahDetik // 3600
Sisa = JumlahDetik % 3600

Menit = Sisa // 60
Detik = Sisa % 60

print(Jam,":",Menit,":",Detik)

print ("=====ARIGATOOOO====")