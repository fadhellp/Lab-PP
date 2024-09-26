a = input()+'.txt'
b = input()+'.txt'
try:
    with open(a) as asli:
        file_as = asli.readlines()  #read semua file bentuk list
        n = []
        file_as[-1] += " " #untuk mengetahui baris terpanjang dalan len
        for x in file_as:
            n.append(len(x))
            with open(b, "w") as salinan:
                for i in file_as:
                    salinan.write(i.rjust(max(n))) #rjust untuk list dari kanan #max(n) nilai terpanjang dalam list
    print("Berhasil")
except:
    print("Invalid")