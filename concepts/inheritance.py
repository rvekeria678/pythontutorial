# Python Inheritance

# Source: https://www.w3schools.com/python/python_inheritance.asp

# Allows a class the ability to inherit the methods/properies from another class

# Parent class is the class being inherited from (also known as the base class)

# Child class is the class that inherits from another class (also known as the derived class)


# Creating a Parent Class (any class can be a parent class)

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
    
    def welcome(self):
        print("Default Welcome Message: Glad you could join us!")

p1 = Person("Tom", "Locker")
p1.printname()

# Creating a Child Class:
# To create a class that inherits from another class, send the parent class as a parameter of the child class

# *If the __init__() function is not defined in the child class, then it will inherit the __init__() of the parent class

# super() function will make the child class inherit all the methods and properties from its parent 

class Student(Person):
    def __init__(self, fname, lname, year):
        # Alternative way of inheritance of the Parent Class
        # Person.__init__(self,fname,lname)
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname,"to the class of", self.graduationyear)

s1 = Student("Mike", "Olsen", 2042)
s1.printname()
# If a method of the same name of a function in the parent class is added to the child, the inheritance of the parent method will be overridden
s1.welcome()