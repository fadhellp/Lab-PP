print(25*"=")
print("Nama     : Muhammad Khaekal")
print("Nim      : H071221039")
print("Kelompok : C")
print(25*"=")

try :
    x = int(input("Masukkan angka x : "))
    y = int(input("Masukkan angka y : "))
    angka = 1
    # X < Y


    for i in range(y) :
        print(i+1, end=" ")
        if (i+1) % 4 == 0 :
            print()
except :
    print("Input salah")

print(25*"=")
print("Terima Kasih")
print(25*"=")