x = set(map(int, input("Masukkan Array 1: ").split()))
y = set(map(int, input("Masukkan Array 2: ").split()))

if len(x&y)==0:
    print('Tidak Ada Duplikat')
else:
    print(f"Terdapat {len(x&y)} buah duplikat yaitu {x&y}".replace("{","(").replace("}",")"))


































# x = list(map(int, input("Masukkan Array 1: ").split()))
# y = list(map(int, input("Masukkan Array 2: ").split())) ; n = []
# for i in x:
#     if i in y:
#         if i not in n:
#             n.append(i)
    
# if len(n) == 0:
#     print (f"tidak ada duplikat")
# else:
#     print(f"Terdapat {len(n)} buah duplikat yaitu {tuple((n))}")