

golongan = input("Golongan = ").upper()       #.upper penginputan variabel untuk kapital dan non kapital
daya = int(input("Daya = "))
Pemakaian = int(input("Pemakaian = "))
tarif = 0
rplc = ""

if golongan =='R1' and daya == 900:
    tarif = 1352
elif golongan =='R1' and daya == 1300:
    tarif = 1444.70
elif golongan =='R1' and daya == 2200:
    tarif = 1444.70
elif golongan =='R2' and daya >= 3500 and daya <=5500:
    tarif = 1699.53
elif golongan =='R3' and daya >= 6600:
    tarif = 1699.53
elif golongan =='B2' and daya >= 6600 and daya <=200000:
    tarif = 1444.70
elif golongan =='B3' and daya >=200000:
    tarif = 1114.70
elif golongan =='I3' and daya >=200000:
    tarif = 1314.12
elif golongan =='P1' and daya >=6600 and daya <=200000:
    tarif = 1523.28
else:
    pesan='data tidak valid'

tagihan= f"Jumlah tagihan anda: {round(tarif * Pemakaian,1):_}".replace("_",".") #replace untuk penggantian suatu tanda baca atau bisa saja isi dari variabel

ind = tagihan.rfind('.')   #.rfind mengembalikkan posisi string sebelumnya  

rep = tagihan[:ind]+','+tagihan[ind+1:] #input [ind+1] untuk jumlah berapa angka dibelakang koma yang diganti dari .rfind sebelumnya
print(rep)
