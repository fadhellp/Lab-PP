def matriks (n):
    matriks = []
    for x in range (n):
        row = []
        input_row = input().split(" ")
        for k in range(n):
            row.append(int(input_row[k]))
        matriks.append(row)
    return matriks
def hasil (matriks):
    left = 0
    right = 0
    for x in range (len(matriks)):
        for k in range (len(matriks)):
            if x == k :
                left += matriks[x][k]
            if x + k == len(matriks) - 1 :
                right += matriks[x][k]
    print(abs(left - right))

n = int(input())
matriks1 = matriks(n)
hasil(matriks1)
