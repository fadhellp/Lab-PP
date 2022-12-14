class Kubus:
    def __init__(self, lebar, tinggi, panjang):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
        self.massa = 0
        self.massaJenis = 0
        self.volume = 0
    
    def setMassa(self, massa):
        self.massa = massa
    def setVolume(self):
        self.volume = self.panjang * self.lebar * self.tinggi
    def getVolume(self,):
        return self.volume

    def getMassaJenis(self):
        self.massaJenis = (self.massa)/(self.getVolume())
        return self.massaJenis

lebar = float(input("Masukkan lebar: "))
tinggi = float(input("Masukkan tinggi: "))
panjang = float(input("Masukkan panjang: "))
massa = float(input("Masukkan massa: "))

kubus = Kubus(lebar, tinggi, panjang)
kubus.setVolume()
kubus.setMassa(massa)
print("Massa Jenis =", kubus.getMassaJenis())

kubus.setMassa(massa*2)
print("Massa Jenis =", kubus.getMassaJenis())