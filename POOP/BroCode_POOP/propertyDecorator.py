# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#           Benefit: Add additional logic when read, write, or deete attributes
#           Gives you getter, setter, and deleter method

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter for 'name'
    @property
    def name(self):
        return self._name

    # Setter for 'name'
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    # Deleter for 'name'
    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name

    # Getter for 'age'
    @property
    def age(self):
        return self._age

    # Setter for 'age'
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    # Deleter for 'age'
    @age.deleter
    def age(self):
        print("Deleting age...")
        del self._age

# Using the Person class
person = Person("Alice", 30)

# Accessing the property
print(person.name)  # Output: Alice
print(person.age)   # Output: 30

# Modifying the property
person.name = "Bob"
person.age = 25

# Deleting the property
del person.name
del person.age
