# Python Classes/Objects

# Source: https://www.w3schools.com/python/python_classes.asp

# Nearly everything in python is an object with properties/methods
# A class can be thought of as an object constructor, or "blue print" for creating objects

# The following is the most simplistic version on creating classes and objects

# Create a Class
class myClass:
    x = 5

# Create an Object
obj1 = myClass()
print(obj1.x)

# The __init__() Function:
# All classes have a built-in __init__() function, which is executed when the class is initiated. It might be necessary to set up default given/default values

# The __str__() Function:
# Contols what should be printed once the class object is returned as a string. If it is not set, then the string representation of the object is returned

# The self parameter - reference to the current instance of the class and used to access its respective variables. It can take any name though it must be the first parameter for any function of the class

class Car:
    def __init__(self, model, manufacturer, horsepower):
        self.model = model
        self.manufacturer = manufacturer
        self.horsepower = horsepower

    def __str__(self):
        return f"{self.manufacturer}, {self.model}:({self.horsepower}hp)"

c1 = Car("hrv", "honda", 234)

print(c1.model)
print(c1.horsepower)
print(c1)

# Object Methods - functions the belong to the object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
            print("My name is", self.name)

p1 = Person("John", 64)
p1.myfunc()

# Modifying object properties
p1.age = 22

print(p1.age)

# Object and their properties may be deleted use the del keyword
# 'del p1.age' will delete that objects age property
# 'del p1' will delete the object itself

# The pass Statement - to avoid getting errors on a class void of a definition

class Movie:
     pass