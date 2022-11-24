print(35*"=")
print("nama\t: Muh. Fahdel Putra Mustafa")
print("NIM\t: H071221051")
print("\tMENGHITUNG JUMLAH TAGIHAN ")
print(35*"=")

Golongan = input("masukkan golongan: ").upper()
Daya = int(input("masukkan jumlah daya: "))
Pemakaian = int(input("masukkan jumlah pemakaian: "))
tarif = 0
rplc = ""

if Golongan =='R1' and Daya == 900:
    tarif = 1352
elif Golongan =='R1' and Daya == 1300:
    tarif = 1444.70
elif Golongan =='R1' and Daya == 2200:
    tarif = 1444.70
elif Golongan =='R2' and Daya >= 3500 and Daya <=5500:
    tarif = 1699.53
elif Golongan =='R3' and Daya >= 6600:
    tarif = 1699.53
elif Golongan =='B2' and Daya >= 6600 and Daya <=200000:
    tarif = 1444.70
elif Golongan =='B3' and Daya >=200000:
    tarif = 1114.70
elif Golongan =='I3' and Daya >=200000:
    tarif = 1314.12
elif Golongan =='P1' and Daya >=6600 and Daya <=200000:
    tarif = 1523.28
else:
    pesan='data tidak valid'

tagihan= f"Jumlah tagihan anda: {round(tarif * Pemakaian,1):_}". replace ("_",".")

ind = tagihan.rfind('.')   

rep = tagihan[:ind]+","+tagihan[ind+1:]
# print(rep)
print (tagihan)
print(ind)
print(rep)


