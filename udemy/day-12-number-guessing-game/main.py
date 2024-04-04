# Number Guessing Game
from art import logo
import random
import os

def driver():
    # Global Presets
    still_continue = True

    while still_continue:
        # Game UI
        os.system('clear')   
        print(logo)     
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100")
        
        # Game Presets
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        attempts = 5 if difficulty == 'hard' else 10
        key = random.randint(1,100)

        while attempts > 0:
            # Game UI
            print(f"You have {attempts} attemps remaining to guess the number.")
            guess = int(input("Make a guess: "))

            if guess > key:
                print("Too high.")
            elif guess < key:
                print("Too low.")
            else:
                print(f"You have guess correctly! The number was {key}")
                break
            attempts -= 1
            if attempts > 0:
                print("Guess again.")
            else:
                print(f"You ran out of attempts! The number was {key}")

        choice = input("Would you like to play again? Type 'y' or 'n': ")
        if choice != 'y':
            still_continue = False

driver()