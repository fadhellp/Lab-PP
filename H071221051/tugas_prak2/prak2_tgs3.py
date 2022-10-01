nilai_a = int(input("masukkan nilai a : "))
nilai_b = int(input("masukkan nilai b : "))
nilai_c = int(input("masukkan nilai c : "))

if nilai_a >= nilai_b and nilai_a >= nilai_c :
    print (f"{nilai_a} adalah yang terbsesar")
elif nilai_b >= nilai_a and nilai_b >= nilai_c :
    print (f"{nilai_b} adalah yang terbesar")

else :
    print(f"{nilai_c} adalah yang terbesar ")
    