# Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
'''
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(multiply, 11, 11)
print(result)

# Nested Functions
def outer_function():
    print("I'm outer")
    def inner_function():
        print("I'm inner")

    inner_function()

outer_function()

# Functions can be returned from other functions
def outer_function():
    print("I'm outer")
    def inner_function():
        print("I'm inner")

    return inner_function

inner_function = outer_function()

inner_function()
'''
import time

## Python Decorator Function
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

say_greeting()