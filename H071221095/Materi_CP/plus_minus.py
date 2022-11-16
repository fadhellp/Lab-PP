n = int(input())
arr = input().split()

for i in range(n):
    arr[i] = int(arr[i])

positif = 0
negatif = 0
nol = 0
for i in range(n):
    if (arr[i]>0):
        positif = positif+1
    elif (arr[i]<0):
        negatif = negatif+1
    else:
        nol = nol+1
print(f'{positif/n:.6f}')
print(f'{negatif/n:.6f}')
print(f'{nol/n:.6f}')