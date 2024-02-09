# Python Polymorphism

# Source: https://www.w3schools.com/python/python_polymorphism.asp

# "Many Forms" -> methods/functions/operators that share the same name which can be executed on many objects/classes

# Classic Polymorphism Example:

# x returns the number of characters
x = "hello"
print(len(x))

# y returns the number of elements
y = (1,2,3)
print(len(y))

# z returns the number of key/value pairs
z = {"name":"Ted","age":44,"nationality":"American", "height":"6ft"}
print(len(z))

class Animal():
    def __init__(self, type):
        self.type = type

    def speak(self):
        print("eeeek!")

# Class Polymorphism
class Cat(Animal):
    def __init__(self, name):
        super().__init__("Mammal")
        self.name = name

    def speak(self):
        print("Meow")

class Dog(Animal):
    def __init__(self, name):
        super().__init__("Mammal")
        self.name = name
        
    def speak(self):    
        print("Woof")

class Cow(Animal):
    def __init__(self, name):
        super().__init__("Mammal")
        self.name = name
    
    def speak(self):
        print("Moo")

c = Cat("Frank")
d = Dog("Dasher")
m = Cow("Bess")

for i in (c,d,m):
    i.speak()

# Inheritance Class Polymorphism
class Unicorn(Animal):
    def __init__(self, name):
        super().__init__("Mammal")
        self.name = name

u = Unicorn("Zeph")
print("\n\tClass Inheritance Polmorphism:")

for i in (c,d,m,u):
    i.speak()