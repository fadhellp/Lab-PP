try:
    angka = int(input("A : "))
    if angka > 0 and angka % 2==0:
        print("bilangan positif dan genap")
    elif angka < 0 and angka % 2!=0:
        print("bilangan negatif dan ganjil")
    elif angka > 0 and angka % 2!=0:
        print("bilangan positif dan ganjil")
    elif angka < 0 and angka % 2==0:
        print("bilangan negatif dan genap")
    elif angka == 0:
        print("bilangan nol")
    else:
        print("input bukan angka")
except:
    print("input bukan angka")

