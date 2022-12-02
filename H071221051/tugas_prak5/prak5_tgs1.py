matrix_1 = [[int(input ("input nilai matrix pertama index {}, {} :". format (baris, kolom ))) for kolom in range (1,2+1)] for baris in range (1, 2+1)]
matrix_2 = [[int(input ("input nilai matrix pertama index {}, {} :". format (baris, kolom ))) for kolom in range (1,2+1)] for baris in range (1, 2+1)]
muulti = []

for x in range(0, len(matrix_1)):
    row = []
    for y in range(0, len(matrix_1[0])):
        total = 0
        for z in range(0, len(matrix_2)):
            total = total + (matrix_1[x][z] * matrix_2[z][y])
        row.append(total)
    muulti.append(row)


for x in range(0, len(muulti)):
    for y in range(0, len(muulti[0])):
        print (muulti[x][y], end=' ')
    print ()