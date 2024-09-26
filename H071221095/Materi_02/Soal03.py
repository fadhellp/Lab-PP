print("Aplikasi Menghitung Luas")
print("[1]Luas Persegi")
print("[2]Luas Segitiga")
print("[3]Luas Lingkaran")
pilihan = int(input(">>"))

if pilihan == 1:
    s = float(input("Input sisi= "))
    Luas = s**2
    print("Luas Persegi= ",str(Luas))

elif pilihan == 2:
    a = float(input("Input Alas= "))
    t = float(input("Input Tinggi= "))
    luas = 1/2*a*t
    print("Luas Segitiga= ",str(luas))

elif pilihan == 3:
    r = float(input("Input Jari-Jari= "))
    pi = 3.14
    diameter = 2*r
    luas = pi*r*r
    print("Luas Lingkaran= ",str("%.2f" % luas))

else:
    print("Input Salah")




