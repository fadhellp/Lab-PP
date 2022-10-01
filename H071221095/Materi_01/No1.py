import math 
h =input("tinggi")
a =input("sudut a")
b =input("sudut b")




radian_a = a*math.pi/180
radian_b = b*math.pi/180

panjang_a = math.tan(radian_a)*100
panjang_b = math.tan(radian_b)*100

hasil = panjang_a-panjang_b


print("hasil :%.1f m"%hasil)
print(f"{hasil:.1f} m")