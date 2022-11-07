try:
    for x in range(0,360):
        nilaiM = float(input('M(0-360): '))
        if 0 <= nilaiM < 90:
            n = nilaiM*240    
            print('selamat pagi')
            break
        elif 90 <= nilaiM < 135:
            n = nilaiM*240
            print('selamat siang')
            break
        elif 135 <= nilaiM < 180:
            n = nilaiM*240
            print('selamat sore')
            break
        elif 180 <= nilaiM < 360:
            n = nilaiM*240
            print('selamat malam')
            break
        else:
            print('input salah')

    jam = n // 3600
    jam += 6
    if jam >= 24:
        jam -= 24
    sisa = n % 3600
    menit = sisa // 60
    detik = sisa % 60
    print("%02d:%02d:%02d"%(jam,menit,detik))
except:
    print("salah")