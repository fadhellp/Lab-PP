print(45*"=")
print("Nama\t: Muhammad Khaekal")
print("NIM\t: H071221039")
print("Kelompok: C")
print(45*"=")


def buat_matriks (label,matriks):
    for x in range(1,3):
        row = []
        for y in range(1,3):
            nilai_matriks = int(input(f"Masukkan nilai matriks {label} index {x},{y} : "))
            row.append(nilai_matriks)
        matriks.append(row)
    return matriks

def hasil_kali(matriks1,matriks2):
    for i in range (2):
        for j in range (2):
            for k in range (2):
                hasil[i][j] += matriks1[i][k] * matriks2[k][j]

    print(f"|{matriks1[0][0]} {matriks1[0][1]}| x |{matriks2[0][0]} {matriks2[0][1]}| = |{hasil[0][0]} {hasil[0][1]}|")
    print(f"|{matriks1[1][0]} {matriks1[1][1]}| x |{matriks2[1][0]} {matriks2[1][1]}| = |{hasil[1][0]} {hasil[1][1]}|")

matriks1=[]
matriks2=[]

hasil = [[0,0],
        [0,0]]

matriks1 = buat_matriks("Pertama",matriks1)
matriks2 = buat_matriks("Kedua", matriks2)

hasil_kali(matriks1,matriks2)