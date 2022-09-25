
nilai_a = int(input("Masukkan Nilai A : "))
nilai_b = int(input("Masukkan Nilai B : "))
nilai_c = int(input("Masukkan Nilai C : "))

if nilai_a >= nilai_b and nilai_a >= nilai_c:       #penggunaan nilai_a dan nilai_b ketika dirunning akan ada inputan nilai tertinggi, walaupun nilainya sama, begitupun di nilai_c
    print(f"> {nilai_a} adalah Nilai terbesar")
elif nilai_b >= nilai_c:                            #penggunaan nilai_b dan nilai_c diinput disini karena sebelumnya pasti tidak terbaca, jadi harus pakai variabel sendiri
    print(f"> {nilai_b} adalah Nilai terbesar")
else :
    print("salah salah")
