

def rot_str (kata):
    N_temp = kata + kata
    N_size = len (kata)         # len itu panjang dari parameter ini

    for i in range (N_size):        #untuk membaca isinya parameter
        for ii in range (N_size):
            print(N_temp[i+ii+1], end="")

        if i < N_size-1:
            print(end="|")

kata = input('Masukkan Kata :')     #dia harus diluar karna fungsi rekursif
rot_str(kata)


