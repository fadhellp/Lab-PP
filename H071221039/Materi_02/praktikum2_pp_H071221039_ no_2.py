print(40*"=")
print("Nama\t: Muhammad Khaekal")
print("NIM\t: H071221039")
print(40*"=")

Golongan = input("Masukkan Golongan :").upper() #upper untuk memberikan kapital pada hasil input
Daya = int(input("Masukkan Daya :")) # Dalam satuan VA
Pemakaian = int(input("Masukkan Pemakaian:")) # Hari
if Golongan == "R1" :
    if Daya == 900 :
        Tarif = 1352
    elif Daya == 1300 and Daya == 2200 :
        Tarif = 1444.70
elif Golongan == "R2" :
    if Daya >= 3500 and Daya <= 5500 :
        Tarif = 1699.53
elif Golongan == "R3" :
    if Daya >= 6600 :
        Tarif = 1699.53
elif Golongan == "B2" :
    if Daya >= 6600 and Daya <= 200000 : #kVA diubah ke VA
        Tarif = 1444.70
elif Golongan == "B3" :
    if Daya >= 200000 :        
        Tarif = 1114.74
elif Golongan == "I3" :
    if Daya >= 200000 :
        Tarif = 1314.12
elif Golongan == "P1" :
    if Daya >= 6600 and Daya <= 200000 :
        Tarif = 1523.28
else :
    print("data tidak valid")


Tagihan = f"> Jumlah Tagihan Anda : {round(Tarif * Pemakaian,1):_}".replace("_",".") #round digunakan untuk membatasi jumlah angka dibelakang koma, replace untuk mngubah atau mengganti sinmbol
ind = Tagihan.rfind(".") #rfind digunakan untuk menemukan simbol pada progrram
rep = Tagihan[:ind]+','+Tagihan[ind+1:] #rep = replication untuk menggabungkan indeks indeks yang telah diubah , ind = indeks, [:ind]+ untuk menunjukkan simbol kesekian yang akan diubah, [ind+1] untuk menampilkan angka kesatu setelah koma
print(rep)

print(40*"=")
print("Terima Kasih")
print(40*"=")