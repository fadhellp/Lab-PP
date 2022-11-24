print ("\t===AHMAD FAUZHAN RAMADHAN B===")
print ("\t=========H0721221062==========")
print ("\t===TUGAS PRAKTIKUM LAB PEKAN 2===")

print ("NOMOR 3")
try:
   # a, b, c, d, e= [int(x) for x in input("Masukkan Angka : "). split()]
   list_number = input("Masukkan Angka :").split(" ")
   print(list_number)
   a = int(list_number[0])
   b = int(list_number[1])
   c = int(list_number[2])
   d = int(list_number[3])
   e = int(list_number[4])
except:
    print("Inputan Tidak Valid")
else:
    genap=0
    ganjil=0
    positif=0
    negatif=0
    angka =[a,b,c,d,e]

    if (a%2==0) :
        genap += 1
    if (a%2) :
        ganjil += 1
    if (a>0) :
        positif +=1
    if (a<0) :
        negatif +=1

    if (b%2==0) :
        genap += 1
    if (b%2) :
        ganjil += 1
    if (b>0) :
        positif +=1
    if (b<0) :
        negatif +=1

    if (c%2==0) :
        genap += 1
    if (c%2) :
        ganjil += 1
    if (c>0) :
        positif +=1
    if (c<0) :
        negatif +=1

    if (d%2==0) :
        genap += 1
    if (d%2) :
        ganjil += 1
    if (d>0) :
        positif +=1
    if (d<0) :
        negatif +=1
    
    if (e%2==0) :
        genap += 1
    if (e%2) :
        ganjil += 1
    if (e>0) :
        positif +=1
    if (e<0) :
        negatif +=1

    print (genap, "Angka Genap")
    print (ganjil,"Angka Ganjil")
    print (positif, "Angka Positif")
    print (negatif, "Angka Negatif")