class Hewan:

    def __init__(self, nama, jenis, speed):
        self.nama = nama
        self.jenis = jenis
        self.speed = speed
  
    def showinfo(self):
        print(f'Nama Hewan : {self.nama}\nJenis : {self.jenis}\nKecepatan : {self.speed} Km/jam')

class Reptil(Hewan):
    
    def __init__(self, nama, jenis, speed):
        super().__init__(nama, jenis ,speed)
        super().showinfo()   

class Mamalia(Hewan):
    
    def __init__(self, nama, jenis, speed):
        super().__init__(nama, jenis, speed)
        print()
        super().showinfo()

hewan1 = Reptil('Buaya Amerika', 'Reptil', 32)
hewan2 = Mamalia('Kucing', 'Mamalia', 48)

class Person:
    
    def __init__(self,nama,umur,gender):
        self.__nama = nama
        self.__umur = umur
        self.__gender = gender

    def setdata(self,nama,umur,gender):
        self.__nama = nama
        self.__umur = umur
        self.__gender = gender
    
    def getdata(self):
        print(f'Nama : {self.__nama}\nUmur : {self.__umur}\nGender : {self.__gender}')
    
data = Person('Raehan',19,'Laki - Laki')
data.getdata()        

 
class Cheetah:
    def kecepatan(self):
        return 'Cheetah hewan paling cepat di dunia'

class Siput:
    def kecepatan(self):
        return 'Kukang hewan paling lambat didunia'

hewan1 = Cheetah()
hewan2 = Siput()

print(hewan1.kecepatan())
print(hewan2.kecepatan())
