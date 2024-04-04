# Number Guessing Game

import random

def driver():
    # Global Presets
    still_continue = False

    while still_continue:
        # Game UI
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
                print("Too low.")
            elif guess < key:
                print("Too high.")
            else:
                print(f"You have guess correctly! The number was {key}")
                break
            attempts -= 1
            if attempts > 0:
                print("Guess again.")
            else:
                print(f"You ran out of attempts! The number was {key}")

driver()