print(40*"=")
print("Nama\t: Muhammad Khaekal")
print("NIM\t: H071221039")
print("Kelompok: C")
print(40*"=")

print("Selamat datang untuk memulai, silahkan input data anda.")
introduction = {
    "Nama" : input("Input Nama : "),
    "Umur" : int(input("Input Umur : ")),
    "Alamat" : input("Input Alamat : ")  
}
option1 = ["1. Detail Anda","2. Ubah Nama","3. Ubah Umur","4. Ubah Alamat", "5. Keluar"]

while True :
    print(42*"=")
    print("Selamat datang", introduction["Nama"],"silahkan pilih opsi")
    print(42*"=")
    for i in option1 :
        print(i)
    print(42*"=") 
    input_opsi = int(input("Input opsi : "))
    print(42*"=") 
    if input_opsi == 1 :
        print("Data anda adalah")
        print("Nama\t:", introduction["Nama"])
        print("Umur\t:", introduction["Umur"])
        print("Alamat\t:", introduction["Alamat"])
    elif input_opsi == 2 :
        new_name = input("Silahkan input nama baru : ")
        introduction["Nama"] = new_name
        print("Nama anda sukses diperbarui")
    elif input_opsi == 3 :
        new_age = int(input("Silahkan input umur baru : "))
        introduction["Umur"] = new_age
        print("Umur anda sukses diperbarui")
    elif input_opsi == 4 :
        new_address = input("Silahkan input alamat baru : ")
        introduction["Alamat"] = new_address
        print("Alamat anda sukses diperbarui")
    elif input_opsi == 5 :
        break
    else :
        print("Opsi yang anda pilih salah")

