# Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ''

print("Welcome to the PyPassword Generator!")
print("How many letters would you like in your password?")
number_of_letters = int(input())

print("How many symbols would you like?")
number_of_symbols = int(input())

print("How many numbers would you like?")
number_of_numbers = int(input())

while number_of_letters + number_of_symbols + number_of_numbers:
    character_type = random.randint(0,2)
    if character_type == 0 and number_of_letters:
        number_of_letters -= 1
        generated_letter = letters[random.randint(0,len(letters)-1)]
        password += generated_letter
    elif character_type == 1 and number_of_symbols:
        number_of_symbols -= 1
        generated_symbol = symbols[random.randint(0,len(symbols)-1)]
        password += generated_symbol
    elif number_of_numbers:
        number_of_numbers -= 1
        generated_number = numbers[random.randint(0,len(numbers)-1)]
        password += generated_number
    
print("Here is your password:",password)




