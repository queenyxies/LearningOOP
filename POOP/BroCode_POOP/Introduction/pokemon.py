class Pokemon:

    def __init__(self, make, type, age, color):
        self.make = make
        self.type = type
        self.age = age
        self.color = color
        

    def attack(self):
        print(f"This {self.make} is attacking")
    
    def stop(self):
        print(f"This {self.make} is stopped")