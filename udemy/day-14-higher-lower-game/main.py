# Higher-Lower Game
from art import logo, vs
from game_data import data
import os
import random

def driver():
    # Game Presets
    still_continue = True
    score = 0

    # Game UI
    os.system('clear')
    print(logo)

    while still_continue:
        # Generating A and B
        a = random.choice(data)
        b = random.choice(data)
        # Keep repicking if both A and B are the same
        while a == b:
            b = random.choice(data)
        # Determining the answer
        answer = 'A' if a['follower_count'] > b['follower_count'] else 'B'
        
        # Game UI
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

        if input("Who has more followers? Type 'A' or 'B': ").upper() != answer:
            still_continue = False
        else:
            score += 1

    os.system('clear')
    print(logo)
    print("Sorry, that's wrong. Final Score:",score)

driver()