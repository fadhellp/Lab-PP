
for inputan in range(0,360):
    m_derajat = float(input('M(0-360): '))

    if 0 <= m_derajat < 90:
        posisi = m_derajat*240               #240 didaptkan 3600*24/360
        print('selamat pagi')
        break                                   #break harus agar ketika inputannya terbaca maka stop sampai dsitu
    elif 90 <= m_derajat < 135:
        posisi = m_derajat*240
        print('selamat siang')
        break
    elif 135 <= m_derajat < 180:
        posisi = m_derajat*240
        print('selamat sore')
        break
    elif 180 <= m_derajat < 360:
        posisi = m_derajat*240
        print('selamat malam')
        break
    else:
        print('input salah')

jam = posisi // 3600            #//pembulatan angka
jam += 6
if jam >= 24:
    jam -= 24
sisa = posisi % 3600            #%sisa hasil
menit = sisa // 60
detik = sisa % 60

print("%02d:%02d:%02d"%(jam,menit,detik))

# n=float(input('Masukkan nilai n (dalam derajat): '))
# jam=6
# menit=0
# hari=24*3600
# detik=round((n/360)*hari)

# while detik>=3600 :
#     detik-=3600
#     jam+=1

# while detik>=60 :
#     detik-=60
#     menit+=1

# jam %= 24

# if jam<4 :
#     print('Selamat Malam')
# elif jam<=10 :
#     print('Selamat Pagi')
# elif jam<=14 :
#     print('Selamat Siang')
# elif jam<=18 :
#     print('Selamat Sore')
# elif jam<=24 :
#     print('Selamat Malam')
    
# print('%02d:%02d:%02d'%(jam,menit,detik))