# 1. Objects is an instance of a class
# 2. Class is a blueprint of an object where it defines 
# the attributes (is/has) mrethods
# 3. Naming convention for class Names (capital)

# object = A "bundle" of related attributes (variables) and methods (functions)
# Ex. phone, cup, book
# You need a "class" to create many objects

# class  = (blueprint) used to design the structure and layout of an object

from POOP.BroCode_POOP.Introduction.pokemon import Pokemon

pokemon_1 = Pokemon("Pikachu", "Electric", 7, "yellow")
pokemon_2 = Pokemon("Bulbasaur", "Plant", 5, "green")

print(pokemon_1.make)
print(pokemon_1.type)
print(pokemon_1.age)
print(pokemon_1.color)

print(pokemon_2.make)
print(pokemon_2.type)
print(pokemon_2.age)
print(pokemon_2.color)

pokemon_1.attack()
pokemon_1.stop()
