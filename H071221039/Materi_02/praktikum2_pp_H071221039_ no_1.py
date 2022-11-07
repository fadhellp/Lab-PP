print(26*"=")
print("Nama\t: Muhammad Khaekal")
print("NIM\t: H071221039")
print(26*"=")

nilai = int(input("Masukkan Nilai :"))
if nilai < 40 and nilai >= 0 :
    Hasil = "F"
elif nilai >= 90 and nilai <= 100:
    Hasil = "A"
elif nilai >= 80 and nilai <= 90 :
    Hasil = "B" 
elif nilai >= 70 and nilai <= 80 : 
    Hasil = "C"
elif nilai >= 60 and nilai <= 70:
    Hasil = "D" 
elif nilai >= 40 and nilai <= 60:
    Hasil = "E"
else :
    Hasil = "Anda terlalu jago"
print ("> nilai",nilai,"=", Hasil)

print(26*"=")
print("\tTerima Kasih")
print(26*"=")