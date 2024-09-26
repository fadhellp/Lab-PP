print(26*"=")
print("Nama\t: Muhammad Khaekal")
print("NIM\t: H071221039")
print(26*"=")

A = int(input("Masukkan Nilai A :"))
B = int(input("Masukkan Nilai B :"))
C = int(input("Masukkan Nilai C :"))
if A >= B and A >= C :
    nilai_terbesar = A
elif B >= C :
    nilai_terbesar = B
else :
    nilai_terbesar = C
print(">", nilai_terbesar, "adalah nilai terbesar")

print(26*"=")
print("\tTerima Kasih")
print(26*"=")