# Project: Blackjack Game

from art import logo, card_art
import os
import random

def driver():
    # Game Presets
    still_continue = True
    cards = [11,3,4,5,6,7,8,9,10,10,10,10]

    # Game Intialization
    choice_to_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()

    if choice_to_continue != 'y':
        still_continue = False

    while still_continue:
        # Game UI
        os.system('cls')
        print(logo)

        # New Game Settings
        player_hand = [random.choice(cards), random.choice(cards)]
        computer_hand = [random.choice(cards)]
        player_won = True

        # Ace Adjustment Logic
        while 11 in player_hand and sum(player_hand) > 21:
            player_hand[player_hand.index(11)] = 2

        print("Your cards:",player_hand)
        print("Computer's first card:",computer_hand[0])

        # Player Drawing Logic
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        while another_card == 'y':
            player_hand.append(random.choice(cards))
            # Ace Adjustment Logic
            while sum(player_hand) > 21 and 11 in player_hand:
                player_hand[player_hand.index(11)] = 2

            if sum(player_hand) > 21:
                break

            print("Your cards:",player_hand)
            print("Computer's first card:",computer_hand[0])
            
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")

        # Computer Drawing Logic
        while sum(computer_hand) < 17:
            computer_hand.append(random.choice(cards))
            # Ace Adjustment Logic
            while sum(computer_hand) > 21 and 11 in computer_hand:
                computer_hand[computer_hand.index(11)] = 2

        # Result Logic
        if sum(player_hand) > 21 or (sum(player_hand) < sum(computer_hand) and sum(computer_hand) <= 21):
            player_won = False
        
        # Result Display
        print("Your final hand:",player_hand)
        print("Computer's final hand:",computer_hand)
        if player_won:
            print("You Win")
        else:
            print("You Lose")

        choice_to_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()

        if choice_to_continue != 'y':
            still_continue = False

driver()