input_f = int(input('jumlah : '))
k = 0

for i in range(1,input_f+1):
    print((input_f + 1 - i) * ' ',end =' ')

    while k !=(2*i-1):
        print('*',end= '')
        k += 1

    k=0
    print()

