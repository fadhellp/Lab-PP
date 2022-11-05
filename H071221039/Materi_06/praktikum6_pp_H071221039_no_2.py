print(40*"=")
print("Nama\t: Muhammad Khaekal")
print("NIM\t: H071221039")
print("Kelompok: C")
print(40*"=")

file_1 = input("Masukkan nama file : ") 
file_2 = input("Masukkan nama file salinan : ")
 
with open (f"{file_1}.txt","w") as file :
    a =  input("Masukkan isi baris pertama : ")
    b =  input("Masukkan isi baris kedua : ")
    c =  input("Masukkan isi baris ketiga : ")
    file.write(f"{a}\n{b}\n{c}\n") 
if len(a) > len(b) and len(a) > len (c):
    terpanjang = len(a)
elif len (b) > len (a) and len (b) > len (c):
    terpanjang = len(b)
else : 
    terpanjang = len(c)
if file_1 != file_2 :
    with open(f"{file_1}.txt", "r") as file :
        with open(f"{file_2}.txt", "w") as file_salinan:
         file_salinan.write(f"{a.rjust(terpanjang)}\n")
         file_salinan.write(f"{b.rjust(terpanjang)}\n")
         file_salinan.write(f"{c.rjust(terpanjang)}\n")
    print("Berhasil")
else : 
    print("Gagal")
file_1.close()
file_2.close()