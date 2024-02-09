# Python Lambda

# Source: https://www.w3schools.com/python/python_lambda.asp

# A lambda function is a small anonymous function
# It can take an innumerable number of arguments but only one expression

# Syntax:
# lambda arguments : expression
square = lambda a : a * a
print(square(2))

# Example of lambda function with more arguments
sum = lambda a,b : a + b
print(sum(1,1))

# The purpose of a lambda function is useful as a return for another function
def my_func1(n):
    return lambda a : a / n

mydivider = my_func1(3)
print(mydivider(12))