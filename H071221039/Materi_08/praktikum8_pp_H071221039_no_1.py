class Person :
    def __init__(self):
        self.nama = nama
        self.age = 0
        self.isMale = True
    def setNama (self,nama) :
        self.nama = nama
    def getNama (self) :
        return self.nama
    def setAge (self,age) :
        self.age = age
    def getAge (self) :
        return self.age
    def setGender (self, gender ) :
        if gender == "laki-laki" :
            self.isMale = True
            self.gender = "laki-laki"
        elif gender == "perempuan" :
            self.isMale = False
            self.gender = "perempuan"
        else :
            print("inputan salah")
    def getGender (self) :
        return self.gender

nama = input ("Masukkan Nama :")
age = int(input("Masukkan umur :"))
gender = input("Masukkan gender :")


person1 = Person()
person1.setNama(nama)
person1.setAge(age)
person1.setGender(gender)
print(person1.getNama())
print(person1.getAge())
print(person1.getGender())
