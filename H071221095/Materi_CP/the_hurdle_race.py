a = input().split()
jumlah_karakter = int(a[0])
tinggi_lompat = int(a[1])

tinggi_balok = input().split()

for i in range(jumlah_karakter):
    tinggi_balok[i] = int(tinggi_balok[i])

tinggi_balok.sort(reverse=True)

selisih = 0
for j in range(jumlah_karakter):
    if tinggi_lompat<tinggi_balok[j]:
        selisih = tinggi_balok[j]-tinggi_lompat
        break
print(selisih)