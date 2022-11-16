def toko(panjang) :
    list_item = list()
    x = input().split(' ')
    for i in range (panjang) :
        list_item.append(int(x[i]))
    return list_item

def total(list_k,list_m,uang) :
    total = -1

    for i in list_k :
        for a in list_m :
            if(i+a <= uang and i+a > total) :
                total = i+a

    print (total)

q = input().split(' ')
uang = int(q[0])
key = int(q[1])
mouse = int(q[2])

list_keyboard = toko(key)
list_mouse = toko(mouse)


total (list_keyboard,list_mouse, uang)