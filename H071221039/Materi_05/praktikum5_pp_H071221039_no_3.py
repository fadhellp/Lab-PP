print(40*"=")
print("Nama\t: Muhammad Khaekal")
print("NIM\t: H071221039")
print("Kelompok: C")
print(40*"=")

duplicate = []
array1 = input("Input array ke 1 : ").split(" ") 
array2 = input("Input array ke 2 : ").split(" ")

for i in array2 :
    if i in array1 :
        duplicate.append(int(i))
duplicate = tuple(duplicate)
print(f"Terdapat {len(duplicate)} buah duplikat yaitu {duplicate}")