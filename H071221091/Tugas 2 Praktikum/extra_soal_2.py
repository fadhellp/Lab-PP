import sys

try:
    ix = float(input("X : "))
    iy = float(input("Y : "))
except:
    print (sys.exit("salah input"))


# if str(ix) or str(iy):
#     sys.exit("input salah")           #sys.exit keluar dari program atau hentikan sampai disitu


if ix < 0 and iy > 0 and ix < -iy:
    print('Koordinat berada pada kuadran 1')
elif ix <0 and iy > 0 and ix > -iy:
    print('Koordinat berada pada kuadran 2')
elif ix > 0 and iy < ix and iy > 0:
    print('Koordinat berada pada kuadran 3')
elif ix > 0 and iy > ix and iy > 0:
    print('Koordinat berada pada kuadran 4')
elif ix > 0 and iy < 0 and -iy < ix:
    print('Koordinat berada pada kuadran 5')
elif ix > 0 and iy < 0 and -iy > ix:
    print('Koordinat berada pada kuadran 6')
elif ix < 0 and iy < 0 and iy > ix:
    print('Koordinat berada pada kuadran 7')
elif ix < 0 and iy < 0 and iy < ix:
    print('Koordinat berada pada kuadran 8')

elif ix == 0 and iy < 0:
    print('berada pada garis -y')

elif ix == 0 and iy > 0:
    print('berada pada garis y')

elif iy == 0 and ix < 0:
    print('berada pada garis -x')

elif iy == 0 and ix > 0:
    print('berada pada garis x')


elif (ix > 0) and (iy > 0):
    print('berada pada garis x=y')

elif (ix > 0) and (iy < 0):
    print('berada pada garis x=-y')

elif (ix < 0) and (iy > 0):
    print('berada pada garis -x=y')

elif (ix < 0) and (iy < 0):
    print('berada pada garis -x=-y')

elif (ix==0) and (iy==0):
    print("berada pada titik pusat")

else:
    print("input salah")
 


