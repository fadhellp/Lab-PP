x = int(input('x = '))
y = int(input('y = '))
if x<y:
    for i in range(y):
        i+=1
        print(i,end=' ')
        if(i%x == 0):
            print('')
else:
    print('SALAH')
