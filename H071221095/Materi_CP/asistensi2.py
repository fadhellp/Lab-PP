list_angka = list(map(int, input().split()))
for i in range(len(list_angka)):
    for j in range(len(list_angka)):
        if list_angka[j] < list_angka[i]:
            list_angka[j], list_angka[i] = list_angka[i], list_angka[j]
print(list_angka)