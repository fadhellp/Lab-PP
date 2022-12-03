from hero import Warrior, Assassin, Support

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