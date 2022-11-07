n = int(input("Masukkan Jumlah Baris: "))

for i in range(1, n+1):
    print((n-i) * "  " + (i * "* ") + ((i-1) * "* "))

for i in range(n, 0,-1):
    print((n-i) * "  " + (i * "* ") + ((i-1) * "* "))