import random

LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '1234567890'
SPECIAL_SYMBOLS = '!@#$%^&*()_+={}[]|'

characters = (UPPERCASE_LETTERS, LOWERCASE_LETTERS, NUMBERS, SPECIAL_SYMBOLS)

def generate_password(password_length):
    password = ""
    for _ in range(password_length):
        password += random.choice(random.choice(characters))
    return password