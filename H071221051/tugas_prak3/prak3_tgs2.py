n=float(input('Masukkan nilai N (dalam derajat): '))
Hour=6
Minute=0
Day=24*3600
Second=round((n/360)*Day)

while Second>=3600 :
    Second-=3600
    Hour+=1

while Second>=60 :
    Second-=60
    Minute+=1

Hour%=24

if Hour<4 :
    print('Selamat Malam')
elif Hour<=10 :
    print('Selamat Pagi')
elif Hour<=14 :
    print('Selamat Siang')
elif Hour<=18 :
    print('Selamat Sore')
elif Hour<=24 :
    print('Selamat Malam')
    
print('%02d:%02d:%02d'%(Hour,Minute,Second))