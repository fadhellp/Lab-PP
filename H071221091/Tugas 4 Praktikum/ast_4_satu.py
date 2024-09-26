
n = int(input())
datalist = list(map(int, (input().split(' ')))) #map untuk mencari objek


def ast():
    for i in range(len(datalist)):      #untuk membaca isinya parameter
        for j in range(len(datalist)):
            if datalist[i]<datalist[j]:
                iniv = datalist[i]
                datalist[i] = datalist[j]
                datalist[j] = iniv 

    for i in datalist :
        print(i, end = ' ')
ast()


# n = int(input())
# for x in range(n)
#     datalist = list(map(int, (input().split(' '))))
