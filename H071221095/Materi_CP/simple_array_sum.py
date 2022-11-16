n = int(input())
# split digunakan untuk memisahkan karakter dlm string
arr = input().split()

# arr[i] utk mengakses list dlm indeks ke i
# i itu nilainya scra default 0 sampai n-1
for i in range(n):
    print(i)
    arr[i]= int(arr[i])

total = 0
for i in range(n):
    total = total+arr[i]
print(total)
