def rot_str (kata):
    N_temp = kata + kata 
    N_size = len (kata)

    for i in range (N_size):
        for ii in range (N_size):
            print(N_temp[i+ii+1], end="")

        print(end="|")
    
kata = str (input('masukkan kata :'))
rot_str(kata)

