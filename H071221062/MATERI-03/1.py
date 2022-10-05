#program mencetak angka
try:
    input_x = int(input('x = '))
    input_y = int(input('y = '))

    if input_x < input_y:
        for angka in range(input_y):    #angka(iterasi) membaca nilai range
            print(angka+1, end=' ')            #end=' ' horizontal
            if((angka+1) % input_x == 0):
                print('')                   #sebagai enter apabila kondisi terpenuhi
    else:
        print('x Harus lebih kecil dari y')
except:
    print('salaaaaaah')

