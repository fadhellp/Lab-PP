a = input().split()
b = input().split()

for i in range(3):
    a[i] = int(a[i])
    b[i] = int(b[i])

nilai_a = 0
nilai_b = 0

for i in range(3):
    if (a[i]>b[i]):
        nilai_a += 1
    elif (b[i]>a[i]):
        nilai_b += 1
print(f'{nilai_a} {nilai_b}')
