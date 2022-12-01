class Person :
    def __init__ (self, name, age, isMale) :
                self.name = name  #atribut 
                self.age = age    
                self.isMale = isMale
    def setname  (self, name) :
                self.name = name 
    def setage (self, age) :
                self.age = age 
    def setisMale (self, isMale) :
                self.isMale = isMale
    def getname (self) :
                return self.name 
    def getage (self) :
                return self.age
    def getisMale (self) :
                if self.isMale == True : 
                    return ("Male")
                else :
                    return ("Female")


afifah = Person ("afifah", 18, False) #membuat objek
print (afifah.getname())
print (afifah.getage())
print (afifah.getisMale())

afifah.setname("salsabila")
print (afifah.getname())