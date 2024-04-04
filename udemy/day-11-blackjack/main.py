# Project: Blackjack Game

from art import logo

def driver():
    # Game UI
    print(logo)
    
    # Game Presets
    still_continue = True
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

    while still_continue:



        choice_to_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()

        if choice_to_continue != 'y':
            still_continue = False

driver()