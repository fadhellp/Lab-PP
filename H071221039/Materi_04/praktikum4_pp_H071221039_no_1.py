print(40*"=")
print("Nama\t: Muhammad Khaekal")
print("NIM\t: H071221039")
print("Kelompok: C")
print(40*"=")

jumlah = int(input("Masukkan jumlah inputan angka : "))
list_angka = list(map(int,(input("Masukkan angka yang akan diurut : ").split(" "))))

def urutan():
    for i in range (len(list_angka)):
        for j in range (len(list_angka)):
            if list_angka[i]<list_angka[j]:
                urutan = list_angka[i]
                list_angka[i] = list_angka[j]
                list_angka[j] = urutan
    for i in list_angka:
        print(i, end = " ")

urutan()