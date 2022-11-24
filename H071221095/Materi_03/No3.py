try:
    total, tunai = int(input("Total : ")), int(input("Uang Tunai: "))
    kembalian = tunai - total
    uang = [100000, 50000, 20000, 10000, 5000, 1000]

    if total < tunai:
        for i in uang:
            bagi = kembalian // i
            print ("%d uang Rp %d" % (bagi, i)) 
            kembalian -= bagi * i

    elif total > tunai:
        print("mengutang")

    else:
        print("uang pas")
except:
    print("salah")
