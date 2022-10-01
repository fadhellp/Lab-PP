fruit = int(input("id buah: "))
kuantitas = int(input("kuantitas: "))
namabuah = ""
hargabuah = 0

match fruit:
    case 1:
        namabuah = "Apel"
        hargabuah = 10000
    case 2:
        namabuah = "Jeruk"
        hargabuah = 4000
    case 3:
        namabuah = "Semangka"
        hargabuah = 12000
    case 4:
        namabuah = "Mangga"
        hargabuah = 7000

print("----Nota----")
print(f'Rp{kuantitas*hargabuah}' )
