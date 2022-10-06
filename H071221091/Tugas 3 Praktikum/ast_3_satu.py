#program mencetak angka
try:
    input_x = int(input('x = '))
    input_y = int(input('y = '))

    if input_x < input_y:
        for angka in range(1,input_y+1):    #angka(iterasi) membaca nilai range
            print(angka, end=' ')            #end=' ' horizontal
            if(angka % input_x == 0):
                print('')                   #sebagai enter apabila kondisi terpenuhi
    else:
        print('x Harus lebih kecil dari y')
except:
    print('salaaaaaah')

