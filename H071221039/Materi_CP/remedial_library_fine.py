x = list(map(int,(input().split(" ")))) #waktu pengembalian
y = list(map(int,(input().split(" ")))) #jatuh tempo

d1 = x[0]
m1 = x[1]
y1 = x[2]
d2 = y[0]
m2 = y[1]
y2 = y[2]

def denda(d1,m1,y1,d2,m2,y2):
    if y1 < y2:
        return 0
    elif y1 == y2 and m1 < m2 :
        return 0
    elif y1 == y2 and m1 == m2 and d1 < d2:
        return 0
    elif y1 > y2 :
        return 10000
    elif m1 > m2 :
        return (m1-m2) * 500
    return (d1-d2) * 15

denda = denda(d1,m1,y1,d2,m2,y2) 
print(denda)