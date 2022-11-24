a = input()
b = input()
c = open(f"{a}.txt","r")
d = c.read()                

try:
    with open(f"{b}.txt","w") as file:  #f{b} salinan dari file awal
        file.write(d)
        print('Berhasil')
except:
    print('Tidak berhasil')