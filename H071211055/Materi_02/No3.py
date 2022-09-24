try:
    x = list(input().split(' '))

    genap = 0
    ganjil = 0
    positif = 0
    negatif = 0

    input1 = int(x[0])
    if  input1 % 2 == 0: 
        genap+=1
    else:
        ganjil+=1

    if input1 >= 0:
        positif+=1
    else:
        negatif+=1


    input2 = int(x[1])
    if  input2 % 2 == 0: 
        genap+=1
    else:
        ganjil+=1

    if input2 >= 0:
        positif+=1
    else:
        negatif+=1


    input3 = int(x[2])
    if  input3 % 2 == 0: 
        genap+=1
    else:
        ganjil+=1

    if input3 >= 0:
        positif+=1
    else:
        negatif+=1

    input4 = int(x[3])
    if  input4 % 2 == 0: 
        genap+=1
    else:
        ganjil+=1

    if input4 >= 0:
        positif+=1
    else:
        negatif+=1
    

    input5 = int(x[4])
    if  input5 % 2 == 0: 
        genap+=1
    else:
        ganjil+=1

    if input5 >= 0:
        positif+=1
    else:
        negatif+=1



    print(genap,'Angka Genap')
    print(ganjil,'Angka Ganjil')
    print(positif,'Angka Positif')
    print(negatif,'Angka Negatif')

except:
    print("Inputan tidak valid")