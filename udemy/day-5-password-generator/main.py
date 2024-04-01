# Password Generator

import random

print("Welcome to the PyPassword Generator!")
print("How many letters would you like in your password?")
number_of_letters = int(input())

print("How many symbols would you like?")
number_of_symbols = int(input())

print("How many numbers would you like?")
number_of_numbers = int(input())

while number_of_letters + number_of_symbols + number_of_numbers:
    