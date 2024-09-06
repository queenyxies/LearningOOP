#Abstract class: A class that cannot be instantiated on its own;  Meant to be subclassed.
#               They can contain abstract methods, which are declared but have no implementation.
#               Abstract classes benefits:
#               1. Previous instantiation of the class itself
#               2. Requires children to use inherited abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):
     @abstractmethod
     def go(self):
          pass
     
     @abstractmethod
     def stop(self):
          pass
     
class Car(Vehicle):

    def go(self):
        print("You drive the car")
    
    def stop(self):
        print("Stop the car!")

class Motor(Vehicle):
    def go(self):
        print("You drive the motor")
    
    def stop(self):
        print("Stop the motor!")



car = Car()
motor = Motor()
car.go()
car.stop()

motor.go()
motor.stop()