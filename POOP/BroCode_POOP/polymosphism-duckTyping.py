#               2. "Duck typing" = Object must have neccesary attributes/methods
# Another way to achieve polymorphism besides Inheritance
# object must have the minimum necessary attributes/methods
# "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Car:
    alive = False
    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()] #MY CAR NEEDS THE MINIMUM NEVESSARY ARGUMENTS TO BE CONSIDERED AN ANIMAL

for animal in animals:
    animal.speak()
    print(animal.alive)