nilai_a = int(input("Masukkan Nilai A : "))
nilai_b = int(input("Masukkan Nilai B : "))
nilai_c = int(input("Masukkan Nilai C : "))

if nilai_a >= nilai_b and nilai_a >= nilai_c:
    print(f"{nilai_a} adalah Nilai terbesar")
elif nilai_b >= nilai_a and nilai_b >= nilai_c:
    print(f"{nilai_b} adalah Nilai terbesar")
else:
    print(f"{nilai_c} adalah Nilai terbesar")


