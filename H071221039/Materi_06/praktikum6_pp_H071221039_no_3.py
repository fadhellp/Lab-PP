print(40*"=")
print("Nama\t: Muhammad Khaekal")
print("NIM\t: H071221039")
print("Kelompok: C")
print(40*"=")

nama_file = input("Masukkan nama file : ") + ".txt"
jumlah_asisten = int(input("Jumlah asisten : "))
buka_file = open(nama_file, "w+")

try:
    buka_file.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")
    buka_file.write("|" + " Nama" + " "*17 + "|" + " NIM" + " "*8 + "|" + " Angkatan" + " " + "|" + "\n")
    buka_file.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+\n")
    for i in range(jumlah_asisten):
        nama = input("Nama : ").replace(" ","_")
        if len(nama) > 20:
            raise TypeError 
        nim = input("NIM : ")
        angkatan = input("Angkatan : ")
        buka_file.write("|"+ nama + " "*(22 - (len(nama))) + "| " + nim +" "*(10-(len(nim)))+ " | " + angkatan + " "*(9-len(angkatan)) + "|" + "\n")
    buka_file.write("+" + "-"*22 + "+" + "-"*12 + "+" + "-"*10 + "+")
    print("Berhasil")
except:
    print("Gagal")
buka_file.close()