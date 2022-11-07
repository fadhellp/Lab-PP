import math
r = int(input("jari_jari_alas = "))
t = int(input("tinggi  = "))

s = math.sqrt(r**(2)+t**(2))

phi = math.pi 

volume = 1/3*phi*(r**2)*t
luas = math.pi*r*(r+s)

print(f"volume :{volume:.2f}")
print(f"luas :{luas:.2f}")