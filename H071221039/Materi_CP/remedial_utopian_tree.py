def utopian_tree ():
    n = int(input()) #menandakan periode keberapa
    h = 1 # tinggi awal pohon
    for i in range (1,n+1):
        if i % 2 != 0 :
            h = h*2
        else : 
            h += 1
    print(h)

jumlah_periode = int(input())
for y in range(jumlah_periode):
    utopian_tree()