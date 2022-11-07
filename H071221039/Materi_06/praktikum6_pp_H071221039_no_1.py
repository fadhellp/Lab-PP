print(40*"=")
print("Nama\t: Muhammad Khaekal")
print("NIM\t: H071221039")
print("Kelompok: C")
print(40*"=")


file_1 = input("Masukkan nama file : ")
file_2 = input("Masukkan nama file salinan : ")

with open(f"{file_1}.txt", "w") as file :
    a = input("Masukkan isi baris pertama : ")
    b = input("Masukkan isi baris kedua : ")
    c = input("Masukkan isi baris ketiga : ")
    file.write(f"{a}\n{b}\n{c}")

if file_1 != file_2 :
    with open(f"{file_1}.txt", "r") as file_asli :
        with open(f"{file_2}.txt", "w") as file_salinan :
            file_salinan.write(file_asli.read())
        print("Berhasil")
else :
    print("Gagal")

file_1.close()
file_2.close()