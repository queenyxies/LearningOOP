# ENCAPSULATION - from the words ENCAPSULATE it encapsulates or wrap attributes and methods into a single class. 
#               -restricts direct access to some of the object's components
#               -help prevent accidental interference and misuse of the data.
print("=====================ENCAPSULATION===========================")
class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.__level = level  # Private attribute
    
    def get_level(self):
        return self.__level
    
    def set_level(self, level):
        if 1 <= level <= 100:
            self.__level = level
        else:
            print("Level must be between 1 and 100")

# Pikachu is a Pokemon with level 25
pikachu = Pokemon("Pikachu", 25)
print(pikachu.name)
print(pikachu.get_level())

# Attempting to set a new valid level
pikachu.set_level(30)
print(pikachu.get_level())

# Attempting to set an invalid level
pikachu.set_level(150)


#============================================================================

print("=====================INHERITANCE===========================")
#INHERITANCE = derives new classes from existing once, promotes code reuse 

class FirePokemon(Pokemon):
    def __init__(self, name, level, fire_power):
        super().__init__(name, level)  # Inherit from the Pokemon class
        self.fire_power = fire_power
    
    def fire_attack(self):
        return f"{self.name} uses a fire attack with {self.fire_power} power!"

# Charmander is a FirePokemon
charmander = FirePokemon("Charmander", 10, 50)
print(charmander.name)
print(charmander.get_level())
print(charmander.fire_attack())

#============================================================================

print("=====================POLYMORPHISM===========================")
class WaterPokemon(Pokemon):
    def __init__(self, name, level, water_power):
        super().__init__(name, level)
        self.water_power = water_power
    
    def attack(self):
        return f"{self.name} uses a water attack with {self.water_power} power!"

class GrassPokemon(Pokemon):
    def __init__(self, name, level, grass_power):
        super().__init__(name, level)
        self.grass_power = grass_power
    
    def attack(self):
        return f"{self.name} uses a grass attack with {self.grass_power} power!"

# Demonstrating polymorphism
squirtle = WaterPokemon("Squirtle", 12, 40)
bulbasaur = GrassPokemon("Bulbasaur", 15, 45)

# Both Pokemon have the same method name 'attack' but provide different implementations
print(squirtle.attack())
print(bulbasaur.attack())

print("=====================ABSTRACTION===========================")

from abc import ABC, abstractmethod

class Move(ABC):
    @abstractmethod
    def execute(self):
        pass

class ElectricMove(Move):
    def execute(self):
        print("Using Thunderbolt!")

class FireMove(Move):
    def execute(self):
        print("Using Flamethrower!")

# Demonstrating abstraction
electric_move = ElectricMove()
fire_move = FireMove()

# You don't need to know how Thunderbolt or Flamethrower works internally to use them
electric_move.execute()
fire_move.execute()

