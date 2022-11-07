def inputan(p):
    data =[]
    n = input().split(' ')
    for i in range(p):
        val = int(n[i])
        data.append(val)
    return data
def hasil(lk,lm,uang):
    total = -1
    for x in lk:
        for y in lm:
            if x+y <= uang and x+y > total:
               total = x+y
    print(total)

bnm = input().split(' ')
uang,p_keyboard,p_mouse = int(bnm[0]),int(bnm[1]),int(bnm[2])
list_keyboards = inputan(p_keyboard)
list_mouse = inputan(p_mouse)

hasil(list_keyboards, list_mouse, uang)
