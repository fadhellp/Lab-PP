print(25*"=")
print("Nama     : Muhammad Khaekal")
print("Nim      : H071221039")
print("Kelompok : C")
print(25*"=")

try :
    n = int(input("Masukkan Nilai n :"))
    suku_pertama = 0
    suku_kedua = 1
    count = 0

    if n < 0 :
        print("Himpunan tidak tersedia")
    while count < n :
        print(suku_pertama, end=" ")
        bilangan_terakhir = suku_pertama + suku_kedua
        suku_pertama, suku_kedua = suku_kedua, bilangan_terakhir
        # suku_kedua = bilangan_terakhir
        count += 1
    print()

except :
    print("Inputan salah")
print(25*"=")
print("TERIMA KASIH")
print(25*"=")