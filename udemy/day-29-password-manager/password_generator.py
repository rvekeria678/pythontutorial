import random

lower_letters = 'abcdefghijklmnopqrstuvwxyz'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
special_symbols = '!@#$%^&*()_+={}[]|'

characters = (upper_letters, lower_letters, numbers, special_symbols)

def generate_password(password_length):
    password = ""
    for _ in range(password_length):
        password += random.choice(random.choice(characters))
    return password

print(generate_password(20))