price = int(input('price barang: '))
pay = int(input('nilai mata uang yang diberi: '))
kembalian = pay - price
money = [100000,50000,20000,10000,5000,1000]
for i in (money):
    bagi = kembalian // i
    if bagi == 0 :
        continue
    print('%d uang Rp %d'%(bagi,i))
    kembalian % i