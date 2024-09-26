class Human:
    def __init__(self, name, position):
        self.name = name
        self.__pos_x = position
    
    def setMovement(self, move):
        if move == 'L':
            self.__pos_x -= self._speed
        elif move == 'R':
            self.__pos_x += self._speed

    def getMovement(self):
        return self.__pos_x

class Hero(Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target):
        target._health -= self._power

    def getPower(self):
        return self._power

    def getHealth(self):
        return self._health

    def getArmor(self):
        return self._armor

    def getSpeed(self):
        return self._speed

class Warrior(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30
    
    def special(self, target):
        self._armor = 45
        self._power = 32
        target._health -= self._power

class Assassin(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 35
        self._speed = 4

    def special(self, target):
        self._speed = 7
        self._power = 42
        target._health -= self._power

class Support(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target):
        self._speed = 6
        target._health += 150

warrior = Warrior("bambang", pos_x=10)
assassin = Assassin("joko", pos_x=25)
support = Support("udin",pos_x=30)

# sebelum
print('Position Warrior (before) :', warrior.getMovement())
warrior.setMovement('L')
# sesudah
print('Position Warrior (after "L") :', warrior.getMovement())

# sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)
# sesudah
print("health (after)", warrior.getHealth())

print("-"*10)

# sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())

support.special(warrior)

# sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())

# sebelum
print('Position Support (before) :', support.getMovement())
support.setMovement('R')
print('Position Support (after "R") :', support.getMovement())