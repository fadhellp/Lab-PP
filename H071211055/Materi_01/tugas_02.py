n = int(input("masukan detik yang akan diubah : "))

Jam = n // 3600
sisa_jam = n % 3600
Menit = sisa_jam // 60
Detik = sisa_jam % 60

print (str(Jam)+":"+str(Menit)+":"+str(Detik))