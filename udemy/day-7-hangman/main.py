# Hangman

import random
import hangmanui
import dictionary

def driver():
    while 1:
        # Presets
        stage = 0
        chosen_word = random.choice(dictionary.dictionary)
        game_complete = False
        display = ['_'] * len(chosen_word)
        lives = 4
        seen = {}

        # Title Screen
        print(hangmanui.title)

        while not game_complete:
            print(hangmanui.stages[stage])
            print(' '.join(display))
            print("Letters Guessed:",' '.join(seen))

            guess = input("Guess a Letter: ")

            for position in range(len(chosen_word)):
                if guess == chosen_word[position]:
                    display[position] = guess
            
            if guess not in chosen_word and guess not in seen:
                lives -= 1
                stage += 1
            
            if guess not in seen:    
                seen[guess] = ''    
        
            if '_' not in display:
                print(hangmanui.won_screen)
                print("Congrats, you won!")
                game_complete = True

            if lives <= 0:
                print(hangmanui.stages[stage])
                print(' '.join(display))
                print("Letters Guessed:",' '.join(seen))
                print(hangmanui.lose_screen)
                print("Sorry, you lost! Better luck next time.")
                print("The word was",chosen_word)
                game_complete = True

        print("Would you like to play again? (y = Yes, n = No):")
        choice = input().lower()
        if choice != 'y':
            break

driver()