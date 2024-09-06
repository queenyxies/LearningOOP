#Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensability
#               class Child(Parent)
class Character:
    def __init__(self, name):
        self.name = name
        self.is_Alive = True
        
    def eat(self):
        print(f"{self.name} is eating")
    
    def levelUp(self):
        print(f"{self.name} leveled up!")

class FFVII(Character):
    def useMateria(self):
        print(f"{self.name} uses materia!")

class FFIX(Character):
    def useWarp(self):
        print(f"{self.name} uses Warp!")

class FFXV(Character):
    def useEon(self):
        print(f"{self.name} uses Eon!")


character1_VII = FFVII("Tifa")
character1_IX = FFIX("Zidane")
character1_XV = FFXV("Noctis")

print(character1_VII.name)
print(character1_IX.is_Alive)
character1_XV.eat()

character1_VII.useMateria()
character1_IX.useWarp()
character1_XV.useEon()
