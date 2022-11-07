try:
    golongan=(input("golongan= ")).upper()
    daya=int(input("daya= "))
    pemakaian=int(input("pemakaian= "))

    tarif=0
    if golongan=="R1" and daya>=900:
        tarif= 1352
    elif golongan=="R1" and daya>= 1300:
        tarif= 144470
    elif golongan=="R1" and daya>= 2200:
        tarif= 144470
    elif golongan=="R2" and daya>= 3500 and daya<= 5500:
        tarif= 169953
    elif golongan=="R3" and daya>= 6600:
        tarif= 169953
    elif golongan=="B2" and daya>= 6600 and daya>= 200:
        tarif= 144470
    elif golongan=="B3" and daya> 200:
        tarif= 111474
    elif golongan=="I3" and daya>= 200:
        tarif= 131412
    elif golongan=="P1" and daya>= 6600 and daya>= 200:
        tarif= 152328
    else:
        print("data tidak valid")

    hasilsementara=f"Jumlah tagihan anda: {tarif*pemakaian:_}"
    hasilreplace=hasilsementara.replace("_", ".")
    print(hasilreplace)
except:
    print("data tidak valid")




