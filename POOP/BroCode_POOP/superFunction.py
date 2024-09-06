# super() = 
#         = Function used in a child to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
    def describe(self):
        super().describe()
        print(f"The radius of the circle is {3.14 * self.radius * self.radius}")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    
    def describe(self):
        super().describe()
        print(f"The area of a square is {self.width * self.width}")

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    
    def describe(self):
        print(f"The area of a triangle is {self.width * self.width / 2}")

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="yellow", is_filled=False, width=5)
triangle = Triangle(color="green", is_filled=True, width=10, height=10)
print(circle.color)
print(circle.is_filled)
print(circle.radius)

circle.describe()
square.describe()
triangle.describe()

